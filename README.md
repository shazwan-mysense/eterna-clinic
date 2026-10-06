# ÉTERNA Clinic: website mockup

Static mockup for ÉTERNA Clinic (依特娜医美诊所), Desa ParkCity, Kuala Lumpur, to be rebuilt in
**WordPress + Elementor Pro**. The design is a re-skin of the CMSMasters **Pure Skin** template
with the ÉTERNA brand kit (cream `#EAE0D3`, taupe `#CCBBAA`, brown `#5B473E`; Marcellus as a
free stand-in for Tan Mon Cheri, Montserrat, Noto Serif/Sans SC).

Content follows the client brief **"ÉTERNA WEBSITE .pdf" (Oct 2026)** and all photography comes
from the client's **"ETERNA WEBSITE IMAGES"** folder.

## Pages (53)

| Path | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About Us |
| `contact.html` | Contact + booking form + Google Map |
| `treatments.html` | Treatments landing (all 10 categories) |
| `treatments/<category>.html` | 9 category pages (Botox links straight to its treatment page) |
| `treatments/<treatment>.html` | 41 treatment pages |

## How to edit

Pages are generated, so edit the source and rebuild rather than editing the HTML:

```bash
python3 build/generate.py
```

- `build/content.py` holds all copy, the category structure, and which client photo goes where.
- `build/generate.py` holds the page layouts, header/footer, and the image pipeline.
- `assets/css/style.css` and `assets/js/main.js` are hand-written.

The image pipeline reads the client folder at `~/Downloads/ETERNA WEBSITE IMAGES`, converts
everything to WebP (about 10 MB total, down from ~34 MB), and makes any crops deliberately at build
time. Every photo is shown in a frame of its own ratio, with no overlays, tints or filters. The
build stops if the same photo would appear twice on one page.

## Open items to confirm with the client

1. **Pink Booster** is listed under Skin Boosters but the brief has no copy for it. It shows as a
   card with an "Enquire" button until the copy arrives.
2. **Pink Peel** has full copy in the brief but no images and no place in the treatment
   navigation. It is built and listed under Pigmentation with a "photo to come" placeholder.
3. **Face Contouring vs Body Contouring.** The navigation structure and home cards say "Face
   Contouring", the Treatments landing notes say "Body Contouring". The site uses Face Contouring.
4. **Social links.** Facebook and Instagram icons are placeholders (`#`); WhatsApp is live.
5. **Booking form** is a demo. It needs connecting to the clinic (Elementor form, WhatsApp or a
   booking system).
6. **Low-resolution sources** that look soft on retina screens: Red Carpet Glow card
   (332 px), Face Lifting cover (307 px), Acne & Scars and Botox covers (~420 px),
   PRP blood-draw photo (617 px).
7. **Small copy corrections made:** "SIGNATRUE SECRETOME" → "Signature Secretome"; "I mmediate"
   → "Immediate". Everything else is verbatim from the brief.

## Elementor rebuild notes

- Global colours: cream `#EAE0D3`, soft `#F1E9DE`, background `#FAF7F2`, taupe `#CCBBAA`,
  brown `#5B473E`, deep `#46362F`, ink `#3B302A`.
- Treatment pages share one layout: split hero, "About / What is", How it works (accordion or
  component cards), Benefits panel, Who is it for (concern photo grid), related treatments, booking.
  Build it once as a Single template and reuse.
- Accordions use the Accordion widget (first item open), carousels use Loop Carousel, the booking
  form maps to the Form widget, entrance animations are fadeInUp / zoomIn (0.9 s, 120 ms stagger).
