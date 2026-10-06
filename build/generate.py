# -*- coding: utf-8 -*-
"""Builds the ÉTERNA static mockup.

    python3 build/generate.py

Reads copy from build/content.py and the client's photo folder (SRC), writes
optimised WebP images to assets/img/ and every page to the site root and
treatments/. Header, footer and section patterns live here so all ~55 pages
stay identical in structure.
"""
import hashlib
import html
import json
import re
import shutil
from urllib.parse import quote
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))
from content import ABOUT, CATEGORIES, CLINIC, CONCERN_CARDS, HOME, T  # noqa: E402

SRC = Path.home() / "Downloads" / "ETERNA WEBSITE IMAGES"
OUT = ROOT / "assets" / "img"
CREAM = (241, 233, 222)
CAT = {c["slug"]: c for c in CATEGORIES}

# ---------------------------------------------------------------- images

_cache, _by_hash = {}, {}
RATIOS = {"45": 4 / 5, "43": 4 / 3, "11": 1.0, "34": 3 / 4, "22": 2.2}
TARGET_W = {"45": 720, "43": 960, "11": 640, "34": 720, "22": 1000}


def _slug(s):
    s = s.lower().replace("é", "e").replace("₂", "2").replace("®", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def _has_alpha(im):
    return im.mode == "RGBA" and im.getchannel("A").getextrema()[0] < 250


def _flatten(im, colour):
    bg = Image.new("RGBA", im.size, colour + (255,))
    bg.alpha_composite(im)
    return bg.convert("RGB")


def img(spec):
    """spec: "path" | (path, mode) | (path, mode, (fx, fy)) -> dict(src, w, h)"""
    if spec is None:
        return None
    if isinstance(spec, str):
        spec = (spec, "n")
    rel, mode = spec[0], spec[1]
    focus = spec[2] if len(spec) > 2 else (0.5, 0.5)
    key = (rel, mode, focus)
    if key in _cache:
        return _cache[key]
    path = ROOT / "build" / rel if rel.startswith("stock/") else SRC / rel
    raw = path.read_bytes()
    digest = hashlib.md5(raw).hexdigest()[:8]
    hkey = (digest, mode, focus)
    if hkey in _by_hash:
        _cache[key] = _by_hash[hkey]
        return _cache[key]

    im = Image.open(path)
    im.load()
    if im.mode == "CMYK":
        im = im.convert("RGB")
    if im.mode in ("P", "LA", "L") or (im.mode == "RGBA"):
        im = im.convert("RGBA")
    alpha = _has_alpha(im)
    if im.mode == "RGBA" and not alpha:
        im = im.convert("RGB")

    if mode == "n":
        if max(im.size) > 1600:
            im.thumbnail((1600, 1600), Image.LANCZOS)
    elif mode.startswith("c"):  # contain on a fixed-ratio canvas
        r = RATIOS[mode[1:]]
        base = _flatten(im, (255, 255, 255)) if im.mode == "RGBA" else im.convert("RGB")
        w, h = base.size
        cw, ch = (w, round(w / r)) if w / h > r else (round(h * r), h)
        canvas = Image.new("RGB", (cw, ch), (255, 255, 255))
        canvas.paste(base, ((cw - w) // 2, (ch - h) // 2))
        im = canvas
        im.thumbnail((TARGET_W[mode[1:]], 2000), Image.LANCZOS)
        alpha = False
    else:  # deliberate crop
        r = RATIOS[mode]
        if im.mode == "RGBA":
            im = _flatten(im, CREAM)
            alpha = False
        w, h = im.size
        fx, fy = focus
        if w / h > r:
            cw, ch = round(h * r), h
        else:
            cw, ch = w, round(w / r)
        left = min(max(round(fx * w - cw / 2), 0), w - cw)
        top = min(max(round(fy * h - ch / 2), 0), h - ch)
        im = im.crop((left, top, left + cw, top + ch))
        if im.width > TARGET_W[mode]:
            im = im.resize((TARGET_W[mode], round(TARGET_W[mode] / r)), Image.LANCZOS)

    folder = _slug(Path(rel).parent.name) if Path(rel).parent.name else "covers"
    name = f"{_slug(Path(rel).stem)}{'' if mode == 'n' else '-' + mode}"
    if focus != (0.5, 0.5):
        name += f"-f{int(focus[0]*100)}{int(focus[1]*100)}"
    dest = OUT / folder / f"{name}.webp"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
    im.save(dest, "WEBP", quality=82, method=6)
    out = {"src": f"assets/img/{folder}/{name}.webp", "w": im.width, "h": im.height, "alpha": alpha}
    _cache[key] = _by_hash[hkey] = out
    return out


class Page:
    """Tracks the images used on one page so the same photo never appears twice."""

    def __init__(self, prefix):
        self.p = prefix
        self.used = set()

    def pic(self, spec, alt, cls="", eager=False, allow_dup=False):
        I = img(spec)
        if I is None:
            return ""
        if I["src"] in self.used and not allow_dup:
            raise ValueError(f"duplicate image on page: {I['src']}")
        self.used.add(I["src"])
        load = "eager" if eager else "lazy"
        c = f' class="{cls}"' if cls else ""
        return (f'<img{c} src="{self.p}{I["src"]}" width="{I["w"]}" height="{I["h"]}" '
                f'alt="{esc(alt)}" loading="{load}" decoding="async">')

    def src_of(self, spec):
        return img(spec)["src"]


def esc(s):
    return html.escape(s or "", quote=True)


# ---------------------------------------------------------------- helpers

def t_href(slug, prefix, anchor=None):
    return f"{prefix}treatments/{slug}.html" + (f"#{anchor}" if anchor else "")


def cat_href(cat, prefix):
    if cat.get("direct"):
        return t_href(cat["direct"], prefix)
    return f"{prefix}treatments/{cat['slug']}.html"


def h1_of(t):
    return t.get("h1", t["name"])


def service_options(selected=None):
    out = ['<option value="">Not sure yet, consultation first</option>']
    for c in CATEGORIES:
        out.append(f'<optgroup label="{esc(c["title"])}">')
        seen = set()
        for m in c["members"]:
            if isinstance(m, dict):
                name = m["name"]
            else:
                name = T[m]["name"]
            if name in seen:
                continue
            seen.add(name)
            sel = " selected" if selected and name == selected else ""
            out.append(f"<option{sel}>{esc(name)}</option>")
        out.append("</optgroup>")
    return "\n".join(out)


LOGO_SVG = """<svg width="{w}" height="{h}" viewBox="0 0 40 56" fill="none" aria-hidden="true">
        <ellipse cx="20" cy="28" rx="18.5" ry="26.5" stroke="{c}" stroke-width="1"/>
        <ellipse cx="20" cy="28" rx="15.5" ry="23.5" stroke="{c}" stroke-width=".7"/>
        <text x="20" y="36.5" text-anchor="middle" font-family="Marcellus, serif" font-size="21" fill="{c}">É</text>
      </svg>"""

LINE_ART = """<path d="M96 396 C64 344 86 300 90 256 C94 212 68 194 66 146 C64 90 98 32 158 28 C218 24 250 78 246 134 C243 174 224 198 220 228 C216 258 230 288 254 312"/>
    <path d="M140 130 C152 122 166 122 174 130"/>
    <path d="M160 142 C157 160 150 170 158 176 C165 181 172 176 172 176"/>
    <path d="M150 200 C162 209 178 206 188 197"/>
    <path d="M120 262 C150 286 196 282 224 258"/>"""

ICON_PIN = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-5.1-7-11a7 7 0 0 1 14 0c0 5.9-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>'
ICON_PHONE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 5c0 8 7 15 15 15l2-4-4-2-2 2c-3-1.5-5.5-4-7-7l2-2-2-4-4 2z"/></svg>'
ICON_SEARCH = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>'
ICON_FB = '<svg viewBox="0 0 24 24"><path d="M13.5 21v-8.2h2.8l.4-3.2h-3.2V7.5c0-.9.3-1.6 1.6-1.6h1.7V3.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.3v3.2h2.8V21h3.4z"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2-.1-1.3-.1-1.7-.1-4.9s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4 1.3-.1 1.7-.1 4.9-.1zm0 2c-3.1 0-3.5 0-4.8.1-1.1.1-1.5.2-1.8.3-.4.2-.7.3-.9.6-.3.3-.5.5-.6.9-.1.3-.3.7-.3 1.8-.1 1.3-.1 1.7-.1 4.8s0 3.5.1 4.8c.1 1.1.2 1.5.3 1.8.2.4.3.7.6.9.3.3.5.5.9.6.3.1.7.3 1.8.3 1.3.1 1.7.1 4.8.1s3.5 0 4.8-.1c1.1-.1 1.5-.2 1.8-.3.4-.2.7-.3.9-.6.3-.3.5-.5.6-.9.1-.3.3-.7.3-1.8.1-1.3.1-1.7.1-4.8s0-3.5-.1-4.8c-.1-1.1-.2-1.5-.3-1.8-.2-.4-.3-.7-.6-.9-.3-.3-.5-.5-.9-.6-.3-.1-.7-.3-1.8-.3-1.3-.1-1.7-.1-4.8-.1zm0 3.4a5.4 5.4 0 1 1 0 10.8 5.4 5.4 0 0 1 0-10.8zm0 8.9a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zm5.6-9.1a1.3 1.3 0 1 1-2.5 0 1.3 1.3 0 0 1 2.5 0z"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 1.8a8.2 8.2 0 1 1-4.2 15.3l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 0 1 12 3.8zm-3.1 4c-.2 0-.5.1-.7.4-.2.3-.9.9-.9 2.1s.9 2.4 1 2.6c.1.2 1.8 2.9 4.5 4 2.2.9 2.7.7 3.2.7.5-.1 1.6-.7 1.8-1.3.2-.6.2-1.2.2-1.3-.1-.1-.2-.2-.5-.3l-1.8-.9c-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-2-1.2 7.5 7.5 0 0 1-1.4-1.7c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.8-2c-.2-.5-.4-.4-.6-.4h-.5z"/></svg>'


# ---------------------------------------------------------------- chrome

def head(title, desc, p):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Marcellus+SC&family=Montserrat:wght@300;400;500;600&family=Noto+Serif+SC:wght@400;500&family=Noto+Sans+SC:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/style.css">
</head>
<body>
"""


def topbar(home):
    contact = f"""<div class="topbar__contact">
      <a href="tel:{CLINIC['phone_tel']}">{CLINIC['phone_display']}</a>
      <a href="mailto:{CLINIC['email']}">{CLINIC['email']}</a>
    </div>"""
    if home:
        items = [CLINIC["area"], '<span class="cn">永恒之美，为你定制</span>', "Doctor-guided aesthetic, regenerative and wellness care", "Open daily, 10am to 6pm"]
        track = "".join(f"<span>{i}</span><span class=\"dot\">·</span>" for i in items) * 2
        return f"""<div class="topbar">
  <div class="container topbar__inner">
    <div class="topbar__marquee"><div class="topbar__track">{track}</div></div>
    {contact}
  </div>
</div>
"""
    return f"""<div class="topbar topbar--light">
  <div class="container topbar__inner">
    <span class="loc">{ICON_PIN} {CLINIC['area']}</span>
    {contact}
  </div>
</div>
"""


def header(active, p):
    def li(key, label, href, extra=""):
        cls = ' class="is-active"' if key == active else ""
        return f'<li{cls}><a class="nav__link" href="{href}">{label}</a>{extra}</li>'

    drop = "".join(f'<a href="{cat_href(c, p)}">{esc(c["title"])} <span class="cn">{c["cn"]}</span></a>' for c in CATEGORIES)
    drop += f'<a class="all" href="{p}treatments.html">All treatments <span class="cn">全部疗程</span></a>'
    return f"""<header class="header">
  <div class="container header__inner">
    <a class="logo" href="{p}index.html" aria-label="ÉTERNA Clinic, home">
      {LOGO_SVG.format(w=38, h=54, c="#5B473E")}
      <span class="logo__text"><span class="logo__name">ÉTERNA</span><span class="logo__sub">依特娜</span></span>
    </a>
    <nav aria-label="Main">
      <ul class="nav">
        {li("home", "Home", p + "index.html")}
        {li("about", "About", p + "about.html")}
        {li("treatments", 'Treatments<span class="caret">▼</span>', p + "treatments.html", f'<div class="dropdown">{drop}</div>')}
        {li("contact", "Contact", p + "contact.html")}
      </ul>
    </nav>
    <div class="header__cta">
      <a class="icon-btn" href="{p}treatments.html" aria-label="Browse treatments">{ICON_SEARCH}</a>
      <a class="btn btn--boxed" href="{p}contact.html#book">Book a Visit</a>
      <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<main>
"""


def footer(active, p):
    def a(key, label, href):
        cls = ' class="is-active"' if key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    addr = "<br>".join(CLINIC["address_lines"])
    hours = "<br>".join(CLINIC["hours_lines"])
    return f"""</main>

<footer class="footer">
  <svg class="footer__art line-art line-art--light" viewBox="0 0 300 420" aria-hidden="true">
    {LINE_ART}
  </svg>
  <div class="container">
    <div class="footer__grid">
      <div>
        <a class="logo" href="{p}index.html" aria-label="ÉTERNA Clinic, home">
          {LOGO_SVG.format(w=44, h=62, c="#46362F")}
          <span class="logo__text"><span class="logo__name">ÉTERNA</span><span class="logo__sub">依特娜</span></span>
        </a>
      </div>
      <div>
        <h4>Address</h4>
        <div class="footer__meta"><span>{addr}</span><span>{hours}</span></div>
      </div>
      <div>
        <h4>Say Hello</h4>
        <div class="footer__meta">
          <a href="tel:{CLINIC['phone_tel']}">{CLINIC['phone_display']}</a>
          <a href="mailto:{CLINIC['email']}">{CLINIC['email']}</a>
        </div>
        <div class="socials">
          <a href="#" aria-label="Facebook">{ICON_FB}</a>
          <a href="#" aria-label="Instagram">{ICON_IG}</a>
          <a href="{CLINIC['wa']}" aria-label="WhatsApp">{ICON_WA}</a>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <nav>
        {a("home", "Home", p + "index.html")}
        {a("about", "About Us", p + "about.html")}
        {a("treatments", "Treatments", p + "treatments.html")}
        {a("contact", "Contact", p + "contact.html")}
      </nav>
      <p class="note">© 2026 ÉTERNA Clinic · All rights reserved<span class="cn">永恒之美，为你定制</span></p>
    </div>
  </div>
</footer>

<script src="{p}assets/js/main.js"></script>
</body>
</html>
"""


def appt(pg, image_spec, selected=None, title="Take the next step and schedule an appointment today"):
    return f"""
  <section class="section section--tight" id="book">
    <div class="container appt">
      <div class="appt__panel">
        <span class="chip reveal">Schedule Your Visit Online</span>
        <h2 class="display-md reveal d-1">{title}</h2>
        <p class="sub reveal d-1">It just takes a few minutes to book a visit online.</p>
        <form class="form-grid reveal d-2" data-demo>
          <div class="field field--select full">
            <label>Treatment</label>
            <select name="service">{service_options(selected)}</select>
          </div>
          <div class="field"><label>Your Name *</label><input type="text" placeholder="How should we address you?" required></div>
          <div class="field"><label>Your Phone</label><input type="tel" placeholder="+60 12-345 6789" required></div>
          <div class="field"><label>Date</label><input type="date"></div>
          <div class="field"><label>Time</label><input type="time" min="10:00" max="18:00"></div>
          <div class="full">
            <button class="btn btn--solid" type="submit" style="width:100%">Make An Appointment</button>
            <p class="form-note">Open daily, 10am to 6pm. Prefer WhatsApp? <a href="{CLINIC['wa']}" style="text-decoration:underline">Message us on {CLINIC['phone_display']}</a>.</p>
          </div>
        </form>
      </div>
      <div class="appt__media reveal-zoom">{pg.pic(image_spec, "Inside ÉTERNA Clinic")}</div>
    </div>
  </section>
"""


def t_card(pg, entry, cat_label):
    """entry: treatment slug or dict from a category's members list"""
    p = pg.p
    if isinstance(entry, str):
        t = T[entry]
        name, href, desc = t["name"], t_href(entry, p), t.get("card", t["lead"])
        spec = t.get("thumb")
        if spec and img(spec)["src"] in pg.used and t.get("thumb_alt"):
            spec = t["thumb_alt"]
        btn = "View Treatment"
    else:
        name, desc, spec = entry["name"], entry.get("desc"), entry.get("image")
        href = t_href(entry["page"], p, entry.get("anchor")) if entry.get("page") else f"{p}contact.html?service={quote(entry['name'])}#book"
        btn = "View Treatment" if entry.get("page") else "Enquire"
    media = pg.pic(spec, name) if spec else '<div class="t-card__ph">Treatment photo to come</div>'
    desc_html = f"<p>{esc(desc)}</p>" if desc else ""
    return f"""<article class="t-card reveal">
          <a href="{href}">{media}</a>
          <div class="t-card__body">
            <p class="t-card__cat">{esc(cat_label)}</p>
            <h3><a href="{href}">{esc(name)}</a></h3>
            {desc_html}
            <span class="t-card__spacer"></span>
            <a class="btn btn--boxed btn--sm" href="{href}">{btn}</a>
          </div>
        </article>"""


def chip_short(cat):
    return cat["chip"].split(" · ")[0]


# ---------------------------------------------------------------- blocks

def block(pg, b, t, slug, flip):
    kind = b[0]
    p = pg.p
    cta = t.get("cta", "Book This Treatment")
    book = f'<a class="btn btn--solid" href="#book">{esc(cta)}</a>'

    if kind == "about":
        _, title, paras, banner = b
        body = "".join(f"<p>{esc(x)}</p>" for x in paras)
        fig = ""
        if banner:
            I = img(banner)
            fig = f'<div class="figure reveal-zoom" style="max-width:{min(I["w"], 1000)}px">{pg.pic(banner, title)}</div>'
        return f"""
  <section class="section">
    <div class="container">
      <div class="prose-center reveal"><h2 class="display-lg">{esc(title)}</h2>{body}</div>
      {fig}
    </div>
  </section>"""

    if kind == "figure":
        _, title, spec, paras = b
        I = img(spec)
        head_html = f'<h2 class="display-lg">{esc(title)}</h2>' if title else ""
        body = "".join(f"<p>{esc(x)}</p>" for x in (paras or []))
        prose = f'<div class="prose-center reveal">{head_html}{body}</div>' if (title or paras) else ""
        return f"""
  <section class="section section--tight">
    <div class="container">
      {prose}
      <div class="figure reveal-zoom" style="max-width:{min(I["w"], 1100)}px">{pg.pic(spec, title or t["name"])}</div>
    </div>
  </section>"""

    if kind == "pair":
        _, title, specs = b
        figs = "".join(f'<div class="reveal-zoom">{pg.pic(s, title)}</div>' for s in specs)
        return f"""
  <section class="section section--tight">
    <div class="container">
      <div class="prose-center reveal"><h2 class="display-lg">{esc(title)}</h2></div>
      <div class="pair" style="margin-top:34px">{figs}</div>
    </div>
  </section>"""

    if kind == "split":
        _, title, paras, spec = b
        body = "".join(f"<p>{esc(x)}</p>" for x in paras)
        media = f'<div class="reveal-zoom">{pg.pic(spec, title)}</div>'
        text = f'<div class="reveal"><h2 class="display-lg">{esc(title)}</h2>{body}</div>'
        inner = text + media if not flip else media + text
        return f"""
  <section class="section">
    <div class="container split2">{inner}</div>
  </section>"""

    if kind == "acc":
        _, items, spec = b
        if len(items) == 1:
            h, txt = items[0]
            content = f'<h2 class="display-lg reveal">{esc(h)}</h2><p class="single reveal d-1">{esc(txt)}</p>'
        else:
            acc = "".join(f"""<div class="acc-item"><button class="acc-item__head"><span>{esc(h)}</span><span class="acc-item__icon">+</span></button><div class="acc-item__body"><p>{esc(txt)}</p></div></div>""" for h, txt in items)
            title = HOW_TITLE if items[0][0] == "How It Works" else "What to Know"
            content = f'<h2 class="display-lg reveal">{title}</h2><div class="accordion reveal d-1">{acc}</div>'
        if spec:
            return f"""
  <section class="section howit">
    <div class="container howit__grid">
      <div>{content}</div>
      <div class="reveal-zoom">{pg.pic(spec, t["name"])}</div>
    </div>
  </section>"""
        return f"""
  <section class="section howit howit--plain">
    <div class="container howit__grid"><div>{content}</div></div>
  </section>"""

    if kind == "benefits":
        _, title, items, spec = b
        lis = "".join(f"<li>{esc(x)}</li>" for x in items)
        if spec:
            return f"""
  <section class="section">
    <div class="container">
      <div class="outline-panel">
        <div class="reveal-zoom">{pg.pic(spec, t["name"])}</div>
        <div class="reveal"><h2 class="display-md">{esc(title)}</h2><ul class="checklist">{lis}</ul>{book}</div>
      </div>
    </div>
  </section>"""
        return f"""
  <section class="section">
    <div class="container">
      <div class="outline-panel outline-panel--solo reveal">
        <div><h2 class="display-md">{esc(title)}</h2><ul class="checklist checklist--2" style="text-align:left">{lis}</ul>{book}</div>
      </div>
    </div>
  </section>"""

    if kind == "who":
        _, title, items = b
        if all(spec for _, spec in items):
            n = len(items)
            mod = {3: " who-grid--3", 4: " who-grid--4"}.get(n, "")
            cells = "".join(f'<div class="who reveal">{pg.pic((spec, "11"), label)}<span>{esc(label)}</span></div>' for label, spec in items)
            grid = f'<div class="who-grid{mod}">{cells}</div>'
        else:
            grid = '<ul class="who-list reveal d-1">' + "".join(f"<li>{esc(label)}</li>" for label, _ in items) + "</ul>"
        return f"""
  <section class="section section--tint">
    <div class="container">
      <div class="sec-head sec-head--center"><h2 class="display-lg reveal">{esc(title)}</h2></div>
      {grid}
      <div class="related-foot reveal">{book}</div>
    </div>
  </section>"""

    if kind == "cards":
        _, title, items, outro = b
        n = len(items)
        cls = {2: "card-grid card-grid--2", 3: "card-grid", 4: "card-grid card-grid--4"}[n]
        cards = []
        for it in items:
            body = f"<p>{esc(it['text'])}</p>" if it.get("text") else ""
            if it.get("bullets"):
                body += '<ul class="checklist">' + "".join(f"<li>{esc(x)}</li>" for x in it["bullets"]) + "</ul>"
            cards.append(f'<article class="info-card reveal">{pg.pic(it["image"], it["name"])}<div class="info-card__body"><h3>{esc(it["name"])}</h3>{body}</div></article>')
        head_html = f'<div class="sec-head sec-head--center"><h2 class="display-lg reveal">{esc(title)}</h2></div>' if title else ""
        out = f'<p class="outro reveal">{esc(outro)}</p>' if outro else ""
        style = ' style="max-width:880px;margin-inline:auto"' if n == 2 else ""
        return f"""
  <section class="section">
    <div class="container">
      {head_html}
      <div class="{cls}"{style}>{"".join(cards)}</div>
      {out}
    </div>
  </section>"""

    if kind == "tiles":
        _, title, items = b
        head_html = f'<div class="sec-head sec-head--center"><h2 class="display-lg reveal">{esc(title)}</h2></div>' if title else ""
        tiles = "".join(f'<div class="tile reveal"><h3>{esc(h)}</h3><p>{esc(x)}</p></div>' for h, x in items)
        style = ' style="max-width:880px;margin-inline:auto"' if len(items) == 2 else ""
        return f"""
  <section class="section section--tight">
    <div class="container">
      {head_html}
      <div class="tiles"{style}>{tiles}</div>
    </div>
  </section>"""

    if kind == "steps":
        _, title, items = b[:3]
        intro = b[3] if len(b) > 3 else None
        intro_html = f"<p>{esc(intro)}</p>" if intro else ""
        steps = "".join(f'<div class="step reveal">{pg.pic(spec, h)}<p class="step__num">Step {i}</p><h3>{esc(h)}</h3><p>{esc(x)}</p></div>'
                        for i, (h, x, spec) in enumerate(items, 1))
        return f"""
  <section class="section">
    <div class="container">
      <div class="sec-head sec-head--center"><h2 class="display-lg reveal">{esc(title)}</h2>{intro_html}</div>
      <div class="steps4" style="grid-template-columns:repeat({len(items)},1fr)">{steps}</div>
    </div>
  </section>"""

    if kind == "variants":
        _, title, items = b
        rows = []
        for i, it in enumerate(items):
            lis = "".join(f"<li>{esc(x)}</li>" for x in it["bullets"])
            rows.append(f"""<div class="variant{' variant--flip' if i % 2 else ''}" id="{it['id']}">
        <div class="variant__media reveal-zoom">{pg.pic(it['image'], it['name'])}</div>
        <div class="reveal"><h3>{esc(it['name'])}</h3><p>{esc(it['text'])}</p><ul class="checklist">{lis}</ul>
          <div class="suit"><b>Who is this treatment suitable for?</b>{esc(it['suit'])}</div>{book}</div>
      </div>""")
        return f"""
  <section class="section">
    <div class="container">
      <div class="sec-head sec-head--center"><h2 class="display-lg reveal">{esc(title)}</h2></div>
      {"".join(rows)}
    </div>
  </section>"""

    if kind == "modes":
        _, items = b
        rows = []
        for i, it in enumerate(items):
            lis = "".join(f"<li>{esc(x)}</li>" for x in it["bullets"])
            rows.append(f"""<div class="variant{' variant--flip' if i % 2 else ''}">
        <div class="variant__media reveal-zoom">{pg.pic(it['image'], it['name'] + ' before and after')}</div>
        <div class="reveal"><h3>{esc(it['name'])}</h3><p>{esc(it['text'])}</p><ul class="checklist checklist--2">{lis}</ul>{book}</div>
      </div>""")
        return f"""
  <section class="section">
    <div class="container">{"".join(rows)}</div>
  </section>"""

    if kind == "timeline":
        _, title, items = b
        cells = "".join(f'<div class="reveal"><h3>{esc(h)}</h3><p>{esc(x)}</p></div>' for h, x in items)
        return f"""
  <section class="section section--tight">
    <div class="container">
      <div class="sec-head sec-head--center"><h2 class="display-lg reveal">{esc(title)}</h2></div>
      <div class="timeline">{cells}</div>
    </div>
  </section>"""

    raise ValueError(kind)


HOW_TITLE = "How It Works"


# ---------------------------------------------------------------- pages

def hero_split(pg, spec, chip, title, leads, flip=False, extra="", tag="h1", eager=True):
    I = img(spec)
    portrait = I["w"] / I["h"] < 1.15
    cls = "split-hero" + (" split-hero--flip" if flip else "") + (" split-hero--portrait" if portrait else "")
    leads_html = "".join(f'<p class="lead reveal d-2">{x}</p>' for x in leads)
    return f"""
  <section class="{cls}">
    <div class="split-hero__panel">
      <span class="chip reveal">{chip}</span>
      <{tag} class="display-xl reveal d-1">{title}</{tag}>
      {leads_html}
      {extra}
    </div>
    <div class="split-hero__media reveal-zoom">{pg.pic(spec, re.sub('<[^>]+>', '', title), eager=eager)}</div>
  </section>"""


def write(path, text):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_treatment(slug):
    t = T[slug]
    pg = Page("../")
    cat = CAT[t["cat"]]
    title_h1 = h1_of(t)
    crumb = f'<p class="crumb reveal d-3"><a href="../treatments.html">Treatments</a> / ' + (
        f'<a href="{cat_href(cat, "../")}">{esc(cat["title"])}</a>' if not cat.get("direct") else esc(cat["title"])) + "</p>"
    mode = t.get("hero_mode", "split")
    if mode == "split":
        hero = hero_split(pg, t["hero"], cat["chip"], esc(title_h1), [esc(t["lead"])], flip=True, extra=crumb)
    else:
        fig = ""
        if t.get("hero"):
            I = img(t["hero"])
            fig = f'<div class="figure reveal-zoom" style="max-width:{min(I["w"], 1200)}px">{pg.pic(t["hero"], title_h1, eager=True)}</div>'
        hero = f"""
  <section class="page-head page-head--center">
    <div class="container">
      <span class="chip reveal">{cat['chip']}</span>
      <h1 class="display-xl reveal d-1">{esc(title_h1)}</h1>
      <p class="lead reveal d-2">{esc(t['lead'])}</p>
      {crumb}
      {fig}
    </div>
  </section>"""

    body = []
    flip = False
    for b in t["blocks"]:
        body.append(block(pg, b, t, slug, flip))
        if b[0] in ("split",):
            flip = not flip

    # related: other members of the primary category
    related = [m for m in cat["members"] if isinstance(m, str) and m != slug][:3]
    rel_html = ""
    if related:
        cards = "".join(t_card(pg, m, chip_short(cat)) for m in related)
        n = len(related)
        cls = {1: "card-grid", 2: "card-grid card-grid--2", 3: "card-grid"}[n]
        style = ' style="max-width:880px;margin-inline:auto"' if n == 2 else (' style="max-width:420px;margin-inline:auto;grid-template-columns:1fr"' if n == 1 else "")
        rel_html = f"""
  <section class="section">
    <div class="container">
      <div class="sec-head"><div><span class="chip reveal">{cat['chip']}</span><h2 class="display-lg reveal d-1">More in {esc(cat['title'])}</h2></div>
        <a class="btn btn--boxed reveal d-2" href="{cat_href(cat, '../') if not cat.get('direct') else '../treatments.html'}">View All</a></div>
      <div class="{cls}"{style}>{cards}</div>
    </div>
  </section>"""

    page = (head(f"{t['name']} | ÉTERNA Clinic", t["lead"], "../") + topbar(False) + header("treatments", "../")
            + hero + "".join(body) + rel_html
            + appt(pg, "ABOUT US/clinic 1.png", selected=t["name"])
            + footer("treatments", "../"))
    write(f"treatments/{slug}.html", page)


def build_category(cat):
    pg = Page("../")
    leads = [esc(cat["intro"])] if cat.get("intro") else []
    hero = hero_split(pg, cat["cover"], cat["chip"], esc(cat["title"]), leads,
                      extra='<p class="crumb reveal d-3"><a href="../treatments.html">All treatments</a></p>')
    cards = "".join(t_card(pg, m, chip_short(cat)) for m in cat["members"])
    grid_title = cat.get("grid_title", f"Explore {cat['title']}")
    page = (head(f"{cat['title']} | ÉTERNA Clinic", cat.get("intro") or f"{cat['title']} treatments at ÉTERNA Clinic, Desa ParkCity, Kuala Lumpur.", "../")
            + topbar(False) + header("treatments", "../") + hero + f"""
  <section class="section">
    <div class="container">
      <div class="sec-head sec-head--center"><h2 class="display-lg reveal">{esc(grid_title)}</h2></div>
      <div class="card-grid">{cards}</div>
    </div>
  </section>""" + appt(pg, "ABOUT US/clinic 1.png") + footer("treatments", "../"))
    write(f"treatments/{cat['slug']}.html", page)


def build_landing():
    pg = Page("")
    rows = []
    for c in CATEGORIES:
        names = []
        seen = set()
        for m in c["members"]:
            if isinstance(m, dict):
                if not m.get("page"):
                    continue
                n, href = m["name"], t_href(m["page"], "", m.get("anchor"))
            else:
                n, href = T[m]["name"], t_href(m, "")
            if n in seen:
                continue
            seen.add(n)
            names.append(f'<li><a href="{href}">{esc(n)}</a></li>')
        href = cat_href(c, "")
        rows.append(f"""<article class="cat-row reveal">
        <a class="cat-row__img" href="{href}">{pg.pic((c['cover'], '45'), c['title'])}</a>
        <div class="cat-row__body">
          <span class="chip">{c['chip']}</span>
          <h2><a href="{href}">{esc(c['title'])}</a></h2>
          <ul>{''.join(names)}</ul>
          <a class="text-link" href="{href}">{'View treatment' if c.get('direct') else 'Explore ' + esc(c['title'])} <span class="arr">→</span></a>
        </div>
      </article>""")
    page = (head("Treatments | ÉTERNA Clinic", "Aesthetic, regenerative and wellness treatments at ÉTERNA Clinic, Desa ParkCity, Kuala Lumpur.", "")
            + topbar(False) + header("treatments", "") + f"""
  <section class="page-head page-head--center">
    <div class="container">
      <span class="chip reveal">Our Treatments · 疗程</span>
      <h1 class="display-xl reveal d-1">Treatments</h1>
      <p class="lead reveal d-2">Discover personalised aesthetic, regenerative and wellness care at ÉTERNA.</p>
    </div>
  </section>
  <section class="section">
    <div class="container cat-list">{''.join(rows)}</div>
  </section>""" + appt(pg, "ABOUT US/clinic 1.png") + footer("treatments", ""))
    write("treatments.html", page)


def build_home():
    pg = Page("")
    H = HOME
    concern = []
    for name, slug in CONCERN_CARDS:
        c = CAT[slug]
        concern.append(f"""<a class="c-card reveal" href="{cat_href(c, '')}">
          <div class="c-card__img">{pg.pic((c['cover'], '45'), name)}</div>
          <span class="c-card__label">{esc(name)} <span class="text-link"><span class="arr">→</span></span></span>
        </a>""")
    sig = CAT["signature-facials"]
    sig_cards = "".join(t_card(pg, m, "Signature Facials") for m in sig["members"])
    steps = "".join(f"""<div class="step reveal">{pg.pic(spec, en)}<p class="step__num">Step {i}</p>
          <h3>{esc(en)}<span class="cn">{cn}</span></h3><p>{esc(txt)}</p></div>""" for i, (en, cn, txt, spec) in enumerate(H["approach"], 1))
    trio = "".join(f'<div class="reveal-zoom{" d-" + str(i) if i else ""}">{pg.pic(s, a)}</div>' for i, (s, a) in enumerate([
        (("HOME PAGE/home page 1.jpg", "34"), "Facial treatment at ÉTERNA"),
        ("ABOUT US/clinic 1.png", "ÉTERNA Clinic lounge"),
        ("ABOUT US/clinic 2.png", "ÉTERNA Clinic entrance")]))

    page = (head("ÉTERNA Clinic | Eternal Beauty, Crafted for You | 依特娜医美诊所",
                 "ÉTERNA is a medical aesthetics clinic in Desa ParkCity, Kuala Lumpur. Personalised aesthetic, regenerative and wellness care. 永恒之美，为你定制。", "")
            + topbar(True) + header("home", "") + f"""
  <section class="hero">
    <aside class="hero__rail reveal">
      <div class="hero__rail-arch">{pg.pic("HOME PAGE/home page 2.png", "Portrait with soft natural skin", eager=True)}</div>
      <div class="hero__call"><span class="t">Call Us:</span><a href="tel:{CLINIC['phone_tel']}">{CLINIC['phone_display']}</a></div>
    </aside>
    <div class="hero__main">
      <div class="hero__copy">
        <h1 class="reveal">{H['hero_title']}</h1>
        <p class="lead reveal d-1">{esc(H['hero_text'])}</p>
        <div class="reveal d-2"><a class="btn btn--solid" href="contact.html#book">Book a Visit</a></div>
      </div>
      <div class="hero__visual">
        <div class="hero__blob"></div>
        <svg class="hero__line-art line-art" viewBox="0 0 300 420" aria-hidden="true">{LINE_ART}</svg>
        <div class="hero__visual-arch reveal-zoom">{pg.pic("HOME PAGE/home page 4.jpg", "Woman with calm, luminous skin", eager=True)}</div>
      </div>
    </div>
  </section>

  <section class="section statement">
    <div class="container">
      <h2 class="display-lg reveal">{esc(H['made_title'])}</h2>
      <p class="reveal d-1">{esc(H['made_text'])}</p>
      <span class="cn-line reveal d-1">{H['made_cn']}</span>
      <a class="btn btn--solid reveal d-2" href="about.html">Discover ÉTERNA</a>
      <div class="trio">{trio}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sec-head sec-head--center">
        <span class="chip reveal">Explore by Concern · 从你的需求开始</span>
        <h2 class="display-lg reveal d-1">Start With What You Want to Improve.</h2>
      </div>
      <div class="card-grid card-grid--4">{''.join(concern)}</div>
    </div>
  </section>

  <section class="section section--peach">
    <div class="container" data-carousel>
      <div class="sec-head">
        <div>
          <span class="chip reveal">Curated by ÉTERNA · 精选疗程</span>
          <h2 class="display-lg reveal d-1">Discover Our Signatures.</h2>
        </div>
        <div class="carousel__nav reveal d-2">
          <button class="carousel__btn" data-prev aria-label="Previous">←</button>
          <button class="carousel__btn" data-next aria-label="Next">→</button>
        </div>
      </div>
      <div class="carousel__track">{sig_cards}</div>
      <div class="related-foot reveal"><a class="btn btn--boxed" href="treatments/signature-facials.html">Explore Signature Facials</a></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sec-head sec-head--center">
        <span class="chip reveal">ÉTERNA Approach · 我们的流程</span>
        <h2 class="display-lg reveal d-1">Personalised Care, From Consultation to Aftercare.</h2>
      </div>
      <div class="steps4">{steps}</div>
    </div>
  </section>
""" + appt(pg, "HOME PAGE/home page 3.jpg") + footer("home", ""))
    write("index.html", page)


def build_about():
    pg = Page("")
    A = ABOUT
    wwd = "".join(f"""<article class="reveal">{pg.pic((spec, "22"), en)}<div class="wwd__body"><h3>{esc(en)}<span class="cn">{cn}</span></h3>
          <p>{esc(txt)}</p><p class="cn">{cntxt}</p></div></article>""" for en, cn, txt, cntxt, spec in A["what_we_do"])
    icons = ["about-us/mission-icon-1", "about-us/mission-icon-2", "about-us/mission-icon-3"]
    pillars = "".join(f"""<div class="pillar reveal"><img src="assets/img/{icons[i]}.webp" width="200" height="200" alt="" loading="lazy">
          <h3>{esc(en)}<span class="cn">{cn}</span></h3><p>{esc(txt)}</p></div>""" for i, (en, cn, txt) in enumerate(A["mission"]))
    why = "".join(f'<li><h3>{esc(en)} <span class="cn">{cn}</span></h3><p>{esc(txt)}</p></li>' for en, cn, txt in A["why"])
    I = img("ABOUT US/Eterna PHILOSOPHY.png")
    phil_cn = f'<p class="lead reveal d-2 cn" style="color:var(--brown)">{A["philosophy_cn"]}</p>'

    page = (head("About ÉTERNA | Beauty, Treated with Intention | 依特娜医美诊所",
                 "At ÉTERNA, we believe beauty is not about changing who you are, but helping you return to your best, most confident state.", "")
            + topbar(False) + header("about", "")
            + hero_split(pg, "ABOUT US/clinic 3.png", "Our Philosophy · 品牌理念", esc(A["philosophy_title"]),
                         [esc(x) for x in A["philosophy"]], extra=phil_cn)
            + f"""
  <section class="section section--tight">
    <div class="container"><div class="figure reveal-zoom" style="max-width:{I['w']}px">{pg.pic("ABOUT US/Eterna PHILOSOPHY.png", "ÉTERNA philosophy")}</div></div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sec-head sec-head--center"><span class="chip reveal">What We Do · 我们的领域</span></div>
      <div class="wwd">{wwd}</div>
    </div>
  </section>

  <section class="section quoteband section--tint">
    <div class="container">
      <span class="chip reveal">Our Vision · 愿景</span>
      <blockquote class="reveal d-1">{esc(A['vision'])}</blockquote>
      <span class="cn-line reveal d-2">{A['vision_cn']}</span>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sec-head sec-head--center"><span class="chip reveal">Our Mission · 使命</span></div>
      <div class="pillars">{pillars}</div>
    </div>
  </section>

  <section class="section section--peach">
    <div class="container split2">
      <div class="reveal-zoom">{pg.pic("ABOUT US/clinic 2.png", "ÉTERNA Clinic entrance")}</div>
      <div>
        <span class="chip reveal">Why ÉTERNA · 为什么选择我们</span>
        <ul class="why-list reveal d-1">{why}</ul>
      </div>
    </div>
  </section>
""" + hero_split(pg, "ABOUT US/clinic 1.png", "Final CTA · 预约咨询".replace("Final CTA", "Book a Consultation"), esc(A["cta_title"]),
                 [esc(A["cta_text"])], flip=True, tag="h2", eager=False,
                 extra='<div class="hero-actions reveal d-3"><a class="btn btn--solid" href="contact.html#book">Book a Consultation</a></div>')
            + footer("about", ""))
    write("about.html", page)


def build_contact():
    pg = Page("")
    addr = "<br>".join(CLINIC["address_lines"])
    hours = "<br>".join(CLINIC["hours_lines"])
    q = CLINIC["address_full"].replace(" ", "+").replace(",", "%2C")
    maps = f"https://www.google.com/maps/search/?api=1&query={q}"
    embed = f"https://maps.google.com/maps?q={q}&z=16&output=embed"
    page = (head("Contact ÉTERNA Clinic | Desa ParkCity, Kuala Lumpur | 联系我们",
                 f"Visit ÉTERNA Clinic at Plaza Arkadia, Desa ParkCity. Open daily 10am to 6pm. Call or WhatsApp {CLINIC['phone_display']}.", "")
            + topbar(False) + header("contact", "")
            + hero_split(pg, "CONTACT US/contact us 1.png", "Contact Us · 联系我们", "Reach Us Easily Online, by Phone or by Dropping In", [],
                         flip=True, extra=f"""<div class="hero-actions reveal d-2">
        <a class="btn btn--solid" href="#book">Book Online</a><span class="divider"></span>
        <a class="phone-pill" href="tel:{CLINIC['phone_tel']}"><span class="ic">{ICON_PHONE}</span>Call: {CLINIC['phone_display']}</a></div>""")
            + f"""
  <section class="section">
    <div class="container split2 split2--top">
      <div>
        <h2 class="display-lg reveal">Contact Information</h2>
        <p class="reveal d-1">We are here to help with any questions about our treatments, your suitability or booking a visit.</p>
        <div class="kv reveal d-2">
          <div><b>Address:</b><p>{addr}</p></div>
          <div><b>Clinic Hours:</b><p>{hours}</p></div>
          <div><b>Phone &amp; WhatsApp:</b><p><a href="tel:{CLINIC['phone_tel']}">{CLINIC['phone_display']}</a><br><a href="{CLINIC['wa']}">WhatsApp us</a></p></div>
          <div><b>Email:</b><p><a href="mailto:{CLINIC['email']}">{CLINIC['email']}</a></p></div>
        </div>
      </div>
      <div class="map-frame reveal-zoom"><iframe src="{embed}" title="ÉTERNA Clinic on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </div>
  </section>

  <section class="section section--peach">
    <div class="container split2">
      <div class="reveal-zoom">{pg.pic("CONTACT US/visit us.png", "ÉTERNA Clinic storefront at Plaza Arkadia")}</div>
      <div>
        <span class="chip reveal">Visit Us · 到访</span>
        <h2 class="display-lg reveal d-1">ÉTERNA Clinic, Plaza Arkadia</h2>
        <div class="kv reveal d-2">
          <div><b>Address:</b><p>{addr}</p></div>
          <div><b>Clinic Hours:</b><p>{hours}</p></div>
        </div>
        <div class="reveal d-3" style="margin-top:26px"><a class="text-link" href="{maps}" target="_blank" rel="noopener">Get Directions <span class="arr">→</span></a></div>
      </div>
    </div>
  </section>

  <section class="section" id="book">
    <div class="container split2">
      <div class="reveal-zoom">{pg.pic("CONTACT US/contact us 2.png", "Consultation at ÉTERNA")}</div>
      <div>
        <span class="chip reveal">Schedule Your Visit Online</span>
        <h2 class="display-lg reveal d-1">Book a Consultation</h2>
        <p class="reveal d-1" style="margin:14px 0 28px">Leave your details and preferred time, and our team will confirm your appointment.</p>
        <form class="form-grid reveal d-2" data-demo>
          <div class="field field--select full"><label>Treatment</label><select name="service">{service_options()}</select></div>
          <div class="field"><label>Your Name *</label><input type="text" placeholder="How should we address you?" required></div>
          <div class="field"><label>Your Phone</label><input type="tel" placeholder="+60 12-345 6789" required></div>
          <div class="field"><label>Date</label><input type="date"></div>
          <div class="field"><label>Time</label><input type="time" min="10:00" max="18:00"></div>
          <div class="field full"><label>Your Message</label><textarea placeholder="Skin concerns, questions or anything we should know"></textarea></div>
          <div class="full">
            <button class="btn btn--solid" type="submit">Make An Appointment</button>
            <p class="form-note">Prefer WhatsApp? <a href="{CLINIC['wa']}" style="text-decoration:underline">Message us on {CLINIC['phone_display']}</a>.</p>
          </div>
        </form>
      </div>
    </div>
  </section>
""" + footer("contact", ""))
    write("contact.html", page)


def mission_icons():
    """Splits the client's 4-icon strip into individual icons (first three are used for the mission pillars)."""
    src = Image.open(SRC / "ABOUT US/eterna mission.png").convert("RGBA")
    alpha = src.getchannel("A")
    cols = [x for x in range(src.width) if alpha.crop((x, 0, x + 1, src.height)).getextrema()[1] > 20]
    groups, start = [], cols[0]
    for a, b in zip(cols, cols[1:]):
        if b - a > 5:
            groups.append((start, a)); start = b
    groups.append((start, cols[-1]))
    groups = [g for g in groups if g[1] - g[0] > 40]
    (OUT / "about-us").mkdir(parents=True, exist_ok=True)
    for i, (x0, x1) in enumerate(groups, 1):
        icon = src.crop((x0, 0, x1 + 1, src.height))
        bbox = icon.getbbox()
        icon = icon.crop(bbox)
        side = max(icon.size)
        sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        sq.paste(icon, ((side - icon.width) // 2, (side - icon.height) // 2))
        sq.resize((200, 200), Image.LANCZOS).save(OUT / "about-us" / f"mission-icon-{i}.webp", "WEBP", quality=90)
    return len(groups)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    old = ROOT / "treatments"
    if old.exists():
        shutil.rmtree(old)
    n_icons = mission_icons()
    build_home()
    build_about()
    build_contact()
    build_landing()
    for c in CATEGORIES:
        if not c.get("direct"):
            build_category(c)
    for slug in T:
        build_treatment(slug)
    files = list((OUT).rglob("*.webp"))
    size = sum(f.stat().st_size for f in files)
    print(json.dumps({"pages": 4 + sum(1 for c in CATEGORIES if not c.get('direct')) + len(T),
                      "images": len(files), "image_mb": round(size / 1e6, 1), "mission_icons": n_icons}))


if __name__ == "__main__":
    main()
