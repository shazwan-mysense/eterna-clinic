# -*- coding: utf-8 -*-
"""Builds v3: the 15-page version of the ÉTERNA mockup (published as /v4/ until 23 Nov 2026).

    python3 build/generate_v3.py

Pages: Home, About Us, Treatments (overview), the client's 10 treatment
categories, FAQ, and Contact & Booking. Like the 10-page version, every treatment is a
section on its category page; unlike it, the categories follow the client's
brief one to one, so a treatment listed under several categories appears on
each of those pages. Reuses the 10-page generator (generate_10page.py), and through it v2's design
system, images and fonts. v2 is not touched.
"""
import shutil

import generate_10page as ten
from content import CATEGORIES, CLINIC, T

g = ten.g
esc = g.esc
ROOT = g.ROOT
SITE = ROOT / "v3"
g.SITE = ten.SITE = SITE
g.OUT = SITE / "assets" / "img"

# ---------------------------------------------------------------- structure

def members(cat):
    """Category members as treatment slugs: Rejuran's two variant cards become one section, Pink Booster a stub."""
    out = []
    for m in cat["members"]:
        if isinstance(m, dict):
            m = m["page"] or "pink-booster"
        if m not in out:
            out.append(m)
    return out


V4 = [{**{k: c[k] for k in ("slug", "title", "chip", "cn", "cover")}, "intro": c.get("intro"), "members": members(c)}
      for c in CATEGORIES]

# Botox's card photo is the Botox category cover, which now heads its own page; the section uses the treatment shot instead.
T["botox"] = {**T["botox"], "thumb": (T["botox"]["hero"], "45")}

# the 10-page module's helpers (home_cat, service_options, cat_href, tx_section) read these at call time
ten.V3[:] = V4
ten.V3BY.clear()
ten.V3BY.update({c["slug"]: c for c in V4})
ten.V2_TO_V3.clear()
ten.V2_TO_V3.update({c["slug"]: f"{c['slug']}.html" for c in V4})


# ---------------------------------------------------------------- chrome overrides

def header(active, p):
    def li(key, inner, extra=""):
        cls = ' class="is-active"' if key == active else ""
        return f"<li{cls}>{inner}{extra}</li>"

    drop = "".join(f'<a href="{p}{c["slug"]}.html">{esc(c["title"])} <span class="cn">{c["cn"]}</span></a>' for c in V4)
    drop += f'<a class="all" href="{p}treatments.html">All treatments <span class="cn">全部疗程</span></a>'
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
        {li("faq", f'<a class="nav__link" href="{p}faq.html">FAQ</a>')}
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
    cls = ' class="is-active"' if active == "faq" else ""
    return out.replace(f'<a href="{p}contact.html"', f'<a href="{p}faq.html"{cls}>FAQ</a>\n        <a href="{p}contact.html"', 1)


g.header = ten.header = header
g.footer = ten.footer = footer


# ---------------------------------------------------------------- pages

def build_category(cat):
    pg = g.Page("")
    leads = [esc(cat["intro"])] if cat.get("intro") else []
    names = [(m, ten.STUBS[m]["name"] if m in ten.STUBS else T[m]["name"]) for m in cat["members"]]
    hero = g.hero_split(pg, cat["cover"], cat["chip"], esc(cat["title"]), leads,
                        extra=f'<div class="hero-actions reveal d-3"><a class="btn btn--solid" href="{ten.book_href("", cat)}">Book Now</a></div>'
                              '<p class="crumb reveal d-3"><a href="treatments.html">All treatments</a></p>')
    # the jump bar only earns its place when there are a few sections to jump between
    jump = ""
    if len(names) >= 3:
        jump = '<nav class="jump" aria-label="Treatments on this page"><div class="container jump__inner">' + \
               "".join(f'<a href="#{m}">{esc(n)}</a>' for m, n in names) + "</div></nav>"
    sections = "".join(ten.tx_section(pg, m, cat, i) for i, (m, _) in enumerate(names))
    desc = cat.get("intro") or f"{cat['title']} treatments at ÉTERNA Clinic, Desa ParkCity, Kuala Lumpur: " + ", ".join(n for _, n in names) + "."
    page = (g.head(f"{cat['title']} | ÉTERNA Clinic", desc, "") + g.topbar(False) + header("treatments", "")
            + hero + jump + sections
            + g.appt(pg, "ABOUT US/clinic 1.png", selected=cat["title"])
            + footer("treatments", ""))
    g.write(f"{cat['slug']}.html", page)


def build_landing():
    pg = g.Page("")
    rows = []
    for c in V4:
        href = f"{c['slug']}.html"
        names = "".join(f'<li><a href="{href}#{m}">{esc(ten.STUBS[m]["name"] if m in ten.STUBS else T[m]["name"])}</a></li>' for m in c["members"])
        rows.append(f"""<article class="cat-row reveal">
        <a class="cat-row__img" href="{href}">{pg.pic((c['cover'], '45'), c['title'])}</a>
        <div class="cat-row__body">
          <span class="chip">{c['chip']}</span>
          <h2><a href="{href}">{esc(c['title'])}</a></h2>
          <ul>{names}</ul>
          <a class="text-link" href="{href}">Explore {esc(c['title'])} <span class="arr">→</span></a>
        </div>
      </article>""")
    page = (g.head("Treatments | ÉTERNA Clinic", "Aesthetic, regenerative and wellness treatments at ÉTERNA Clinic, Desa ParkCity, Kuala Lumpur.", "")
            + g.topbar(False) + header("treatments", "") + f"""
  <section class="page-head page-head--center">
    <div class="container">
      <span class="chip reveal">Our Treatments · 疗程</span>
      <h1 class="display-xl reveal d-1">Treatments</h1>
      <p class="lead reveal d-2">Discover personalised aesthetic, regenerative and wellness care at ÉTERNA.</p>
    </div>
  </section>
  <section class="section">
    <div class="container cat-list">{''.join(rows)}</div>
  </section>""" + g.appt(pg, "ABOUT US/clinic 1.png") + footer("treatments", ""))
    g.write("treatments.html", page)


# Answers are drawn from the client's brief (CLINIC details and treatment copy in content.py).
FAQ = [
    ("Visiting & Booking", "到访与预约", [
        ("Where is ÉTERNA Clinic?",
         [f"We are at {CLINIC['address_full']}. Directions and a map are on our <a href=\"contact.html\">Contact &amp; Booking</a> page."]),
        ("What are your opening hours?",
         ["We are open daily, Monday to Sunday, from 10am to 6pm."]),
        ("How do I book an appointment?",
         [f"Use the booking form on our <a href=\"contact.html#book\">Contact &amp; Booking</a> page, call us on "
          f"<a href=\"tel:{CLINIC['phone_tel']}\">{CLINIC['phone_display']}</a> or <a href=\"{CLINIC['wa']}\">message us on WhatsApp</a>. "
          "Leave your details and preferred time, and our team will confirm your appointment."]),
        ("I'm not sure which treatment I need. Where do I start?",
         ["Start with a consultation. It is where we understand your concerns, goals and suitability before planning any treatment. "
          "When you book, choose “Not sure yet, consultation first”."]),
    ]),
    ("About Our Treatments", "关于疗程", [
        ("Is there any downtime?",
         ["It depends on the treatment. Many of our facials are designed with little or no downtime. Peels may cause mild tingling, "
          "redness or light peeling, and injectable treatments can leave small bumps, redness or mild bruising for a short time.",
          "Each treatment's Comfort &amp; Downtime details are listed on its <a href=\"treatments.html\">treatment page</a>."]),
        ("Are the treatments comfortable?",
         ["Most of our treatments are well tolerated. Depending on the treatment, you may feel temporary warmth, tingling or tenderness. "
          "DENSITY, for example, uses integrated cooling to keep the treatment comfortable."]),
        ("How many sessions will I need?",
         ["This depends on your concern and how your skin responds, and is planned with you at your consultation. Some treatments follow a set course: "
          "the official NCTF® 135 HA protocol, for example, commonly uses 3 sessions around 3 weeks apart."]),
        ("When will I see results?",
         ["Some treatments show a difference straight away. With premium facial fillers, results are usually visible immediately. "
          "Regenerative treatments work more gradually: with DENSITY, some tightening may be seen early, with progressive improvement over 4–6 months."]),
        ("Can treatments be combined?",
         ["Yes, some are designed to work together. Skin Reset Signature pairs Glo2Facial with ADVATx Yellow Laser in a structured programme, "
          "and Eye Rejuvenation may combine eye skinboosters, scaffold threads, collagen-supporting injectables or energy-based treatments, "
          "depending on the cause of the concern."]),
        ("What aftercare should I follow?",
         ["Your practitioner will give you aftercare advice for your treatment. In general, keep skincare gentle, stay hydrated, use sun protection every day "
          "and avoid rubbing or pressing on treated areas. Our ongoing aftercare also supports your recovery, maintenance and long-term treatment planning."]),
    ]),
]


def build_faq():
    pg = g.Page("")
    groups = []
    for title, cn, items in FAQ:
        rows = "".join(f'<div class="acc-item"><button class="acc-item__head" type="button"><span>{esc(q)}</span><span class="acc-item__icon">+</span></button>'
                       f'<div class="acc-item__body"><div class="acc-content">{"".join(f"<p>{a}</p>" for a in answer)}</div></div></div>'
                       for q, answer in items)
        groups.append(f"""<div class="faq-group">
        <h2 class="display-md reveal">{esc(title)} <span class="cn">{cn}</span></h2>
        <div class="accordion reveal d-1">{rows}</div>
      </div>""")
    page = (g.head("FAQ | ÉTERNA Clinic", "Answers to common questions about visiting ÉTERNA Clinic, booking, downtime, sessions, results and aftercare.", "")
            + g.topbar(False) + header("faq", "")
            + g.hero_split(pg, "ABOUT US/clinic 2.png", "FAQ · 常见问题", "Frequently Asked Questions",
                           ["Answers to the questions we hear most about visiting ÉTERNA and what to expect from your treatment."], flip=True,
                           extra='<div class="hero-actions reveal d-3"><a class="btn btn--solid" href="contact.html#book">Book a Consultation</a></div>')
            + f"""
  <section class="section">
    <div class="container faq">{''.join(groups)}</div>
  </section>""" + g.appt(pg, "ABOUT US/clinic 1.png") + footer("faq", ""))
    g.write("faq.html", page)


# ---------------------------------------------------------------- main

def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets" / "css").mkdir(parents=True)
    (SITE / "assets" / "js").mkdir(parents=True)
    css = "".join((ROOT / f).read_text() for f in ("v2/assets/css/style.css", "build/extra-sections.css", "build/extra-15page.css"))
    (SITE / "assets" / "css" / "style.css").write_text(css)
    shutil.copy(ROOT / "v2" / "assets" / "js" / "main.js", SITE / "assets" / "js" / "main.js")
    g.OUT.mkdir(parents=True)
    g.mission_icons()

    g.build_home()
    g.build_about()
    g.build_contact()
    build_landing()
    for c in V4:
        build_category(c)
    build_faq()

    home = SITE / "index.html"
    home.write_text(home.read_text().replace('href="treatments/signature-facials.html"', 'href="signature-facials.html"'))
    cp = SITE / "contact.html"
    cp.write_text(cp.read_text().replace("<title>Contact ÉTERNA Clinic", "<title>Contact &amp; Booking | ÉTERNA Clinic"))

    g.inject_fonts()
    pages = sorted(p.name for p in SITE.glob("*.html"))
    imgs = list(g.OUT.rglob("*.webp"))
    print({"pages": len(pages), "files": pages, "images": len(imgs), "image_mb": round(sum(f.stat().st_size for f in imgs) / 1e6, 1)})


if __name__ == "__main__":
    main()
