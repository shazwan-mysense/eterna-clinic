# Éterna Clinic — website mockup

Six-page static mockup for the Éterna medical aesthetics clinic (依特娜医美诊所),
designed to be rebuilt 1:1 in **WordPress + Elementor Pro**.

Design direction follows the CMSMasters **Pure Skin** template the client liked
(currently imported at eternaclinic.com.my/pure-skin-home/), re-skinned with the
Éterna brand kit: cream `#EAE0D3` · taupe `#CCBBAA` · brown `#5B473E`,
Marcellus (stand-in for Tan Mon Cheri) + Montserrat + Noto Serif/Sans SC.

## Pages

| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About / brand story |
| `treatments.html` | All treatments |
| `treatment-skin-booster.html` | Treatment detail (master layout — reuse for the other 5) |
| `pricing.html` | Full price guide |
| `contact.html` | Contact + booking |

Open `index.html` directly in a browser — no build step, no dependencies.

## ⚠️ Placeholder facts — confirm with client before launch

Every business fact below is **invented for the mockup**:

- Address: "Unit 3-2, Jalan Setia 1, 50480 Kuala Lumpur"
- Phone +60 3-1234 5678 / WhatsApp +60 12-345 6789
- Email hello@eternaclinic.com.my
- Hours: Tue–Sun 10am–7pm, closed Mondays
- Doctors/team names: Dr. Chloe Tan, Dr. Wei Lin Ong, Sandra Lim
- All stats (10+ years, 6,000+ treatments, 98%, 4.9 rating / 300+ reviews)
- All prices (RM) and treatment claims/durations
- All testimonials (written for the mockup)
- Treatment menu itself (6 services assumed — confirm actual services & licensing,
  e.g. whether injectables can be advertised under Malaysian regulations)

Images are hotlinked Unsplash stock (Asian-looking models per brief) — replace
with the clinic's own photography for launch.

## Elementor rebuild notes

- **Fonts**: headings = Tan Mon Cheri (client owns license? else keep Marcellus,
  free on Google Fonts). Body = Montserrat. Chinese = Noto Serif SC / Noto Sans SC.
- Global colors → Elementor kit: cream `#EAE0D3`, soft `#F1E9DE`, bg `#FAF7F2`,
  taupe `#CCBBAA`, brown `#5B473E`, deep `#46362F`, ink `#3B302A`.
- Announcement marquee → HTML widget (same markup) or a ticker plugin.
- Sticky shrinking header → Elementor Pro sticky header + "scrolling effect" class.
- Reveal animations → native entrance animations (fadeInUp / zoomIn, 0.9s,
  staggered 120ms delays).
- Arch images → image widget with border-radius `999px 999px 0 0`.
- Carousels (treatments, reviews) → Loop Carousel / Testimonial Carousel.
- Accordions (steps, FAQs) → Accordion widget, first item open.
- Counters → Counter widget.
- Price lists → Price List widget inside a bordered container
  (offset shadow: box-shadow `5px 5px 0 rgba(204,187,170,.22)`).
- Booking form → Elementor Pro Form widget (fields already match).
- Custom cursor dot → optional; HTML widget with the snippet from
  `assets/js/main.js`, or drop it entirely for WP.
- Oval review cards → large border-radius on a container; line-art SVGs → SVG
  image widgets (files can be exported from the HTML).
