# -*- coding: utf-8 -*-
"""The 10-page version of the ÉTERNA mockup (published as /v3/ until 23 Nov 2026, then retired).

    python3 build/generate_10page.py   (writes to 10-page/, which is not published)

The 15-page build (build/generate_v3.py) reuses this module's treatment sections and chrome.

Pages: Home, About Us, Contact & Booking, and 7 treatment category pages.
Every treatment is a section on its category page (no per-treatment pages).
Reuses the v2 generator (generate.py) for the design system, images and
fonts; v2 itself is not touched.
"""
import re
import shutil
from urllib.parse import quote

import generate as g
from content import CLINIC, T

ROOT = g.ROOT
SITE = ROOT / "10-page"
g.SITE = SITE
g.OUT = SITE / "assets" / "img"
esc = g.esc

# ---------------------------------------------------------------- structure

V3 = [
    {"slug": "signature-facials", "title": "Signature Facials", "chip": "Skin Wellness · 肌肤管理", "cn": "肌肤管理",
     "cover": "SIGNATURE FACIAL COVER.jpg",
     "members": ["skin-reset-signature", "red-carpet-glow", "red-carpet-glow-gold", "exoglow-dep", "fire-and-ice", "oxygeneo", "glo2facial-geneo-x"]},
    {"slug": "acne-scars-pigmentation", "title": "Acne, Scars & Pigmentation", "chip": "Skin Clarity · 痘肌修复 · 色素管理", "cn": "痘肌 · 色素",
     "cover": "Acne & Scars COVER.png",
     "members": ["advatx-yellow-laser", "clarity-acne-peel", "epn-microneedling", "co2-laser", "pico-laser", "brightening-peel", "renewal-retinol-peel", "pink-peel"]},
    {"slug": "skin-boosters", "title": "Skin Boosters", "chip": "Injectable Skincare · 水光焕肤", "cn": "水光焕肤",
     "cover": "SKIN BOOSTER COVER.jpg",
     "intro": "Personalised injectable and regenerative treatments designed to improve hydration, skin quality, repair and overall rejuvenation.",
     "members": ["cellbooster", "nctf-135-ha", "restylane-vital-light", "neauvia-hydro-deluxe", "revok50", "rejuran", "plinest-newest",
                 "pink-booster", "profhilo", "nxo-exosome", "nadrx-skinbooster", "elesome-skinbooster", "prp-face"]},
    {"slug": "botox-rejuvenation", "title": "Botox & Rejuvenation", "chip": "Aesthetic Rejuvenation · 面部年轻化", "cn": "面部年轻化",
     "cover": "EYE & FACE REJUVENATION COVER .jpg",
     "members": ["botox", "premium-facial-fillers", "eye-rejuvenation"]},
    {"slug": "face-lifting-contouring", "title": "Face Lifting & Contouring", "chip": "Lift & Contour · 提拉紧致 · 塑形管理", "cn": "提拉 · 塑形",
     "cover": "Face Lifting & Tightening COVER_.png",
     "members": ["density", "facial-biostimulators", "pb-serum"]},
    {"slug": "hair-scalp", "title": "Hair & Scalp", "chip": "Hair Health · 头皮护理", "cn": "头皮护理",
     "cover": "HAIR COVER.jpg",
     "members": ["cellbooster", "nxo-exosome"]},
    {"slug": "wellness-longevity", "title": "Wellness & Longevity", "chip": "Integrative Wellness · 健康抗衰", "cn": "健康抗衰",
     "cover": "WELLNESS COVER.png",
     "members": ["hydrogen-drip", "nmn-drip", "glow-infusion-drip", "signature-secretome", "exosome-therapy", "herrestore-signature", "emsella"]},
]
V3BY = {c["slug"]: c for c in V3}

# The brief has photos but no copy for Pink Booster, so it gets a short section with a booking button.
STUBS = {"pink-booster": {"name": "PINK BOOSTER", "thumb": ("Skin Booster/Pink Booster/pink booster 2.png", "45")}}

# v2 category -> v3 page (used by the home page "Explore by concern" cards)
V2_TO_V3 = {
    "signature-facials": "signature-facials.html", "acne-scars": "acne-scars-pigmentation.html",
    "pigmentation": "acne-scars-pigmentation.html#pico-laser", "skin-boosters": "skin-boosters.html",
    "face-lifting": "face-lifting-contouring.html", "botox": "botox-rejuvenation.html",
    "face-eye-rejuvenation": "botox-rejuvenation.html", "face-contouring": "face-lifting-contouring.html#pb-serum",
    "hair": "hair-scalp.html", "wellness": "wellness-longevity.html",
}


def home_cat(slug):
    """First v3 page that lists a treatment (where its Book Now and links point)."""
    return next(c for c in V3 if slug in c["members"])


def book_href(p, cat):
    return f"{p}contact.html?service={quote(cat['title'])}#book"


# ---------------------------------------------------------------- chrome overrides

def service_options(selected=None):
    out = ['<option value="">Not sure yet, consultation first</option>']
    for c in V3:
        sel = " selected" if selected == c["title"] else ""
        out.append(f"<option{sel}>{esc(c['title'])}</option>")
    return "\n".join(out)


def header(active, p):
    def li(key, inner, extra=""):
        cls = ' class="is-active"' if key == active else ""
        return f"<li{cls}>{inner}{extra}</li>"

    drop = "".join(f'<a href="{p}{c["slug"]}.html">{esc(c["title"])} <span class="cn">{c["cn"]}</span></a>' for c in V3)
    return f"""<header class="header">
  <div class="container header__inner">
    <a class="logo" href="{p}index.html" aria-label="ÉTERNA Clinic, home">
      {g.LOGO_SVG.format(w=38, h=54, c="#5B473E")}
      <span class="logo__text"><span class="logo__name">ÉTERNA</span><span class="logo__sub">依特娜</span></span>
    </a>
    <nav aria-label="Main">
      <ul class="nav">
        {li("home", f'<a class="nav__link" href="{p}index.html">Home</a>')}
        {li("about", f'<a class="nav__link" href="{p}about.html">About Us</a>')}
        {li("treatments", '<button class="nav__toggle" type="button" aria-expanded="false" aria-haspopup="true">Treatments<span class="caret">▼</span></button>', f'<div class="dropdown">{drop}</div>')}
        {li("contact", f'<a class="nav__link" href="{p}contact.html">Contact</a>')}
      </ul>
    </nav>
    <div class="header__cta">
      <a class="btn btn--boxed" href="{p}contact.html#book">Book Now</a>
      <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<main>
"""


def footer(active, p):
    out = g._v2_footer(active, p)
    return out.replace(f'href="{p}treatments.html"', f'href="{p}index.html#treatments"')


def cat_href(cat, prefix):
    return prefix + V2_TO_V3[cat["slug"]]


def t_card(pg, entry, cat_label):
    """Home page signature cards: image and title open the section, button books."""
    t = T[entry]
    cat = home_cat(entry)
    href = f"{pg.p}{cat['slug']}.html#{entry}"
    return f"""<article class="t-card reveal">
          <a href="{href}">{pg.pic(t['thumb'], t['name'])}</a>
          <div class="t-card__body">
            <p class="t-card__cat">{esc(cat_label)}</p>
            <h3><a href="{href}">{esc(t['name'])}</a></h3>
            <p>{esc(t.get('card', t['lead']))}</p>
            <span class="t-card__spacer"></span>
            <a class="btn btn--boxed btn--sm" href="{book_href(pg.p, cat)}">Book Now</a>
          </div>
        </article>"""


g._v2_footer = g.footer
g.header, g.footer, g.service_options, g.cat_href, g.t_card = header, footer, service_options, cat_href, t_card


# ---------------------------------------------------------------- treatment sections

def para(x):
    return f"<p>{esc(x)}</p>"


def ul(items):
    return "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"


def details(pg, t, slug):
    """Turns a treatment's v2 content blocks into accordion items: (title, html)."""
    items, figs = [], []

    def fig(spec, alt):
        I = g.img(spec)
        if I["src"] in pg.used:
            return ""
        return pg.pic(spec, alt, cls="tx__fig")

    for b in t["blocks"]:
        k = b[0]
        if k in ("benefits", "who"):
            continue
        if k == "about":
            _, title, paras, banner = b
            items.append((title, "".join(para(x) for x in paras) + (fig(banner, title) if banner else "")))
        elif k == "acc":
            for h, txt in b[1]:
                items.append((h, para(txt)))
            # the v2 side image for this block joins the first of these items
            if b[2]:
                h0, html0 = items[-len(b[1])]
                items[-len(b[1])] = (h0, html0 + fig(b[2], t["name"]))
        elif k == "cards":
            _, title, cards, outro = b
            body = ""
            for c in cards:
                body += f"<h4>{esc(c['name'])}</h4>" + (para(c["text"]) if c.get("text") else "") + (ul(c["bullets"]) if c.get("bullets") else "")
            if outro:
                body += para(outro)
            items.append((title or "Key Features", body))
        elif k == "tiles":
            _, title, tl = b
            items.append((title or "Programme Components", "".join(f"<h4>{esc(h)}</h4>{para(x)}" for h, x in tl)))
        elif k == "steps":
            title, st = b[1], b[2]
            intro = para(b[3]) if len(b) > 3 and b[3] else ""
            items.append((title, intro + "<ol>" + "".join(f"<li><b>{esc(h)}</b>: {esc(x)}</li>" for h, x, _ in st) + "</ol>"))
        elif k == "variants":
            for v in b[2]:
                items.append((v["name"].title().replace("Hb", "HB"),
                              para(v["text"]) + ul(v["bullets"]) + f'<div class="suit"><b>Who is this treatment suitable for?</b>{esc(v["suit"])}</div>'))
        elif k == "modes":
            for m in b[1]:
                items.append((m["name"], para(m["text"]) + ul(m["bullets"]) + fig(m["image"], m["name"] + " before and after")))
        elif k == "figure":
            _, title, spec, paras = b
            html = "".join(para(x) for x in (paras or [])) + fig(spec, title or t["name"])
            if title:
                items.append((title, html))
            else:
                figs.append(html)
        elif k == "pair":
            _, title, specs = b
            items.append((title, '<div class="tx__pair">' + "".join(fig(s, title) for s in specs) + "</div>"))
        elif k == "split":
            _, title, paras, spec = b
            items.append((title, "".join(para(x) for x in paras) + fig(spec, title)))
        elif k == "timeline":
            _, title, tl = b
            items.append((title, "".join(f"<h4>{esc(h)}</h4>{para(x)}" for h, x in tl)))
    if figs and items:
        h0, html0 = items[0]
        items[0] = (h0, html0 + "".join(figs))
    elif figs:
        items.append(("Overview", "".join(figs)))
    return items


def tx_section(pg, slug, cat, i):
    flip = " tx--flip" if i % 2 else ""
    book = f'<a class="btn btn--solid" href="{book_href(pg.p, cat)}">Book Now</a>'
    if slug in STUBS:
        s = STUBS[slug]
        return f"""
  <section class="tx{flip}" id="{slug}">
    <div class="container tx__grid">
      <div class="tx__media reveal-zoom">{pg.pic(s['thumb'], s['name'])}</div>
      <div class="tx__body reveal">
        <h2 class="display-md">{esc(s['name'])}</h2>
        <p class="lead">Ask our team about {esc(s['name'].title())} at your consultation.</p>
        <div class="tx__actions">{book}</div>
      </div>
    </div>
  </section>"""

    t = T[slug]
    body = []
    for b in t["blocks"]:
        if b[0] == "benefits":
            body.append(f'<h3 class="tx__h">{esc(b[1])}</h3><ul class="checklist checklist--2">' + "".join(f"<li>{esc(x)}</li>" for x in b[2]) + "</ul>")
        elif b[0] == "who":
            body.append(f'<h3 class="tx__h">{esc(b[1])}</h3><ul class="pills">' + "".join(f"<li>{esc(l)}</li>" for l, _ in b[2]) + "</ul>")
    media = pg.pic(t["thumb"], t["name"])
    acc = details(pg, t, slug)
    acc_html = ""
    if acc:
        rows = "".join(f'<div class="acc-item"><button class="acc-item__head" type="button"><span>{esc(h)}</span><span class="acc-item__icon">+</span></button>'
                       f'<div class="acc-item__body"><div class="acc-content">{html}</div></div></div>' for h, html in acc)
        # treatments with no benefits list show their first detail panel open, so the section isn't bare
        collapsed = " data-collapsed" if any(b[0] == "benefits" for b in t["blocks"]) else ""
        acc_html = f'<p class="tx__details-label">Treatment details</p><div class="accordion"{collapsed}>{rows}</div>'
    return f"""
  <section class="tx{flip}" id="{slug}">
    <div class="container tx__grid">
      <div class="tx__media reveal-zoom">{media}</div>
      <div class="tx__body reveal">
        <h2 class="display-md">{esc(g.h1_of(t))}</h2>
        <p class="lead">{esc(t['lead'])}</p>
        {''.join(body)}
        <div class="tx__actions">{book}</div>
        {acc_html}
      </div>
    </div>
  </section>"""


def build_category(cat):
    pg = g.Page("")
    leads = [esc(cat["intro"])] if cat.get("intro") else []
    names = [(m, STUBS[m]["name"] if m in STUBS else T[m]["name"]) for m in cat["members"]]
    hero = g.hero_split(pg, cat["cover"], cat["chip"], esc(cat["title"]), leads,
                        extra=f'<div class="hero-actions reveal d-3"><a class="btn btn--solid" href="{book_href("", cat)}">Book Now</a></div>')
    jump = '<nav class="jump" aria-label="Treatments on this page"><div class="container jump__inner">' + \
           "".join(f'<a href="#{m}">{esc(n)}</a>' for m, n in names) + "</div></nav>"
    sections = "".join(tx_section(pg, m, cat, i) for i, (m, _) in enumerate(names))
    desc = cat.get("intro") or f"{cat['title']} treatments at ÉTERNA Clinic, Desa ParkCity, Kuala Lumpur: " + ", ".join(n for _, n in names) + "."
    page = (g.head(f"{cat['title']} | ÉTERNA Clinic", desc, "") + g.topbar(False) + header("treatments", "")
            + hero + jump + sections
            + g.appt(pg, "ABOUT US/clinic 1.png", selected=cat["title"])
            + footer("treatments", ""))
    g.write(f"{cat['slug']}.html", page)


# ---------------------------------------------------------------- main

def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets" / "css").mkdir(parents=True)
    (SITE / "assets" / "js").mkdir(parents=True)
    css = (ROOT / "v2" / "assets" / "css" / "style.css").read_text() + (ROOT / "build" / "extra-sections.css").read_text()
    (SITE / "assets" / "css" / "style.css").write_text(css)
    shutil.copy(ROOT / "v2" / "assets" / "js" / "main.js", SITE / "assets" / "js" / "main.js")
    g.OUT.mkdir(parents=True)
    g.mission_icons()

    g.build_home()
    g.build_about()
    g.build_contact()
    for c in V3:
        build_category(c)

    # home: anchor for the footer's "Treatments" link, and the signatures button
    home = SITE / "index.html"
    s = home.read_text()
    i = s.index("Explore by Concern")
    j = s.rfind('<section class="section">', 0, i)
    s = s[:j] + '<section class="section" id="treatments">' + s[j + len('<section class="section">'):]
    s = s.replace('href="treatments/signature-facials.html"', 'href="signature-facials.html"')
    home.write_text(s)
    # contact page is now "Contact & Booking"
    cp = SITE / "contact.html"
    cp.write_text(cp.read_text().replace("<title>Contact ÉTERNA Clinic", "<title>Contact &amp; Booking | ÉTERNA Clinic"))

    g.inject_fonts()
    pages = sorted(p.name for p in SITE.glob("*.html"))
    imgs = list(g.OUT.rglob("*.webp"))
    print({"pages": len(pages), "files": pages, "images": len(imgs), "image_mb": round(sum(f.stat().st_size for f in imgs) / 1e6, 1)})


if __name__ == "__main__":
    main()
