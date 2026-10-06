# -*- coding: utf-8 -*-
"""ÉTERNA site content, transcribed from the client brief "ÉTERNA WEBSITE .pdf" (Oct 2026).

Copy is kept verbatim from the brief. Image paths are relative to the client's
"ETERNA WEBSITE IMAGES" folder (see SRC in generate.py).

Image spec: "path" (natural ratio) or ("path", mode) / ("path", mode, focus)
  modes: n = natural, 45 / 43 / 11 / 34 = deliberate centre crops, c43 = contain on a 4:3 canvas
"""

CLINIC = {
    "phone_display": "011-6511 8845",
    "phone_tel": "+601165118845",
    "wa": "https://wa.me/601165118845",
    "email": "eternaclinickl@gmail.com",
    "address_lines": ["H-G-8, Perdana, Plaza Arkadia,", "3, Jalan Intisari, Desa Parkcity,", "52200 Kuala Lumpur"],
    "address_full": "H-G-8, Perdana, Plaza Arkadia, 3, Jalan Intisari, Desa Parkcity, 52200 Kuala Lumpur, Federal Territory of Kuala Lumpur",
    "hours_lines": ["Open Daily", "Mon – Sun: 10am – 6pm"],
    "area": "Desa ParkCity, Kuala Lumpur",
}

# ---------------------------------------------------------------- shared concern figures
SR = "ETERNA SIGNATURE FACIALS/Skin Reset Signature/"
FIG = {
    "dull": SR + "dull skin.jpg",
    "dry": SR + "dry skin.jpg",
    "uneven": SR + "uneven skin tone.webp",
    "redness": SR + "redness.jpg",
    "rough": SR + "Rough Skin texture.jpg",
}

# ---------------------------------------------------------------- categories
# order = treatment navigation structure in the brief
CATEGORIES = [
    {"slug": "signature-facials", "title": "Signature Facials", "chip": "Skin Wellness · 肌肤管理", "cn": "肌肤管理",
     "cover": "SIGNATURE FACIAL COVER.jpg", "grid_title": "Explore Our Signature Facials",
     "members": ["skin-reset-signature", "red-carpet-glow", "red-carpet-glow-gold", "exoglow-dep", "fire-and-ice", "oxygeneo", "glo2facial-geneo-x"]},
    {"slug": "acne-scars", "title": "Acne & Scars", "chip": "Acne Solutions · 痘肌修复", "cn": "痘肌修复",
     "cover": "Acne & Scars COVER.png",
     "members": ["advatx-yellow-laser", "clarity-acne-peel", "epn-microneedling", "co2-laser", "pico-laser", "skin-reset-signature"]},
    {"slug": "pigmentation", "title": "Pigmentation", "chip": "Skin Clarity · 色素管理", "cn": "色素管理",
     "cover": "PIGMENTATION COVER.png",
     "members": ["pico-laser", "co2-laser", "advatx-yellow-laser", "brightening-peel", "renewal-retinol-peel", "skin-reset-signature", "pink-peel"]},
    {"slug": "skin-boosters", "title": "Skin Boosters", "chip": "Injectable Skincare · 水光焕肤", "cn": "水光焕肤",
     "cover": "SKIN BOOSTER COVER.jpg",
     "intro": "Personalised injectable and regenerative treatments designed to improve hydration, skin quality, repair and overall rejuvenation.",
     "members": ["cellbooster", "nctf-135-ha", "restylane-vital-light", "neauvia-hydro-deluxe", "revok50",
                 {"name": "Rejuran HB Plus", "page": "rejuran", "anchor": "hb-plus", "image": ("Skin Booster/Rejuran HB Plus/rejuran hb 2.jpg", "45"),
                  "desc": "Rejuran HB is mainly used to strengthen the skin’s regenerative ability whilst providing an intense hydration effect on dehydrated areas."},
                 {"name": "Rejuran Healer", "page": "rejuran", "anchor": "healer", "image": ("Skin Booster/Rejuran Healer/rejuran healer 3.png", "45"),
                  "desc": "Rejuran Healer repairs and rejuvenates aging or damaged skin."},
                 "plinest-newest",
                 {"name": "PINK BOOSTER", "page": None, "image": ("Skin Booster/Pink Booster/pink booster 2.png", "45"),
                  "desc": None},
                 "profhilo", "nxo-exosome", "nadrx-skinbooster", "elesome-skinbooster", "prp-face"]},
    {"slug": "face-lifting", "title": "Face Lifting & Tightening", "chip": "Lift & Firm · 提拉紧致", "cn": "提拉紧致",
     "cover": "Face Lifting & Tightening COVER_.png",
     "members": ["density", "facial-biostimulators", "profhilo", "plinest-newest", "cellbooster"]},
    {"slug": "botox", "title": "Botox", "chip": "Expression Line Care · 动态纹管理", "cn": "动态纹管理",
     "cover": "BOTOX COVER.jpg", "direct": "botox", "members": ["botox"]},
    {"slug": "face-eye-rejuvenation", "title": "Face & Eye Rejuvenation", "chip": "Aesthetic Rejuvenation · 面部年轻化", "cn": "面部年轻化",
     "cover": "EYE & FACE REJUVENATION COVER .jpg",
     "members": ["premium-facial-fillers", "facial-biostimulators", "eye-rejuvenation", "rejuran", "profhilo", "plinest-newest", "prp-face", "density"]},
    {"slug": "face-contouring", "title": "Face Contouring", "chip": "Contour Refinement · 塑形管理", "cn": "塑形管理",
     "cover": "Face Contouring COVER.jpg", "members": ["pb-serum", "cellbooster"]},
    {"slug": "hair", "title": "Hair", "chip": "Hair Health · 头皮护理", "cn": "头皮护理",
     "cover": "HAIR COVER.jpg", "members": ["cellbooster", "nxo-exosome"]},
    {"slug": "wellness", "title": "Wellness", "chip": "Integrative Wellness · 健康抗衰", "cn": "健康抗衰",
     "cover": "WELLNESS COVER.png",
     "members": ["hydrogen-drip", "nmn-drip", "glow-infusion-drip", "signature-secretome", "exosome-therapy", "herrestore-signature", "emsella"]},
]

# Home "Explore by concern" visual cards (names as written in the brief)
CONCERN_CARDS = [
    ("Acne & Scars", "acne-scars"), ("Pigmentation", "pigmentation"), ("Skin Boosters", "skin-boosters"),
    ("Face Lifting", "face-lifting"), ("Face & Eye Rejuvenation", "face-eye-rejuvenation"), ("Hair & Scalp", "hair"),
    ("Face Contouring", "face-contouring"), ("Wellness & Longevity", "wellness"),
]

HOW, COMFORT, RESULTS = "How It Works", "Comfort & Downtime", "Results & Aftercare"

# ---------------------------------------------------------------- treatments
# blocks: ("about", title, [paras], banner?) | ("acc", [(h, text)], image?) | ("cards", title, [items], outro?)
#         ("tiles", title, [(h, text)]) | ("steps", title, [(h, text, image)]) | ("benefits", title, items, image?)
#         ("who", title, [(label, image?)]) | ("figure", title, image, text?) | ("split", title, [paras], image)
#         ("timeline", title, [(h, text)])
T = {}

# ---------- Signature Facials
T["skin-reset-signature"] = dict(
    name="Skin Reset Signature", cat="signature-facials",
    lead="A structured skin programme combining advanced facial technology with targeted laser care for progressively healthier-looking skin.",
    card="A structured ÉTERNA skin programme combining facial care with ADVATx Yellow Laser for progressive improvement in overall skin quality.",
    hero=SR + "skin reset COVER.jpg", thumb=(SR + "skin reset COVER.jpg", "45"),
    blocks=[
        ("about", "About Skin Reset Signature", ["ÉTERNA Skin Reset Signature combines Glo2Facial + ADVATx Yellow Laser in a structured programme designed to progressively improve hydration, clarity, texture and overall skin quality."], SR + "skin reset signature.png"),
        ("cards", HOW, [
            {"name": "Glo2Facial", "text": "Glo2Facial supports exfoliation, oxygenation, hydration and skin conditioning.", "image": (SR + "GLOW2FACIAL 2.png", "43")},
            {"name": "ADVATx Yellow Laser", "text": "ADVATx Yellow Laser helps address selected redness, acne-prone skin concerns and overall skin clarity.", "image": (SR + "ADVATX YELLOW LASER 1.png", "43")},
        ], "Together, both treatments form a planned programme for more consistent and progressive skin improvement."),
        ("benefits", "Benefits", ["Improves skin hydration", "Enhances skin clarity", "Supports smoother skin texture", "Helps improve the appearance of redness", "Restores a healthier-looking glow"], SR + "GLOW2FACIAL 1.avif"),
        ("acc", [(COMFORT, "Treatment experience and downtime vary according to the skin condition and treatments performed during each visit."),
                 (RESULTS, "Skin improvement is designed to be progressive across the programme. Gentle skincare, hydration and daily sun protection are recommended.")],
         SR + "ADVATX YELLOW LASER 2.jpg"),
        ("who", "Who Is It For?", [("Dull skin", FIG["dull"]), ("Dry skin", FIG["dry"]), ("Uneven skin tone", FIG["uneven"]), ("Mild redness", FIG["redness"]), ("Rough texture", FIG["rough"])]),
    ])

RC = "ETERNA SIGNATURE FACIALS/ÉTERNA Red Carpet Glow Facial/"
T["red-carpet-glow"] = dict(
    name="ÉTERNA Red Carpet Glow Facial", cat="signature-facials",
    lead="A signature glow facial combining active exfoliation, hydration and skin conditioning to refresh dull, uneven-looking skin and reveal a smoother, more luminous complexion.",
    card="A signature maintenance facial designed for refreshed, hydrated and luminous-looking skin.",
    hero=RC + "LED-Facial-scaled.webp", thumb=(RC + "active peel 2_COVER.png", "45"),
    blocks=[
        ("about", "About Red Carpet Glow", ["Designed for skin that looks dull, tired or uneven, this treatment combines with IS Clinical active peel with hydrating and soothing steps to refine texture and restore radiance."], RC + "is clinical product.png"),
        ("acc", [(HOW, "The active peel helps remove surface buildup and dull skin cells, while the remaining facial steps replenish hydration and condition the skin for a fresh, polished finish.")], RC + "active peel 1.png"),
        ("benefits", "Benefits", ["Brightens dull-looking skin", "Refines rough texture", "Improves skin smoothness", "Enhances hydration", "Restores a healthy-looking glow"], None),
        ("who", "Who Is It For?", [("Dull skin", FIG["dull"]), ("Dry skin", FIG["dry"]), ("Uneven skin tone", FIG["uneven"]), ("Mild redness", FIG["redness"]), ("Rough texture", FIG["rough"])]),
    ])

RG = "ETERNA SIGNATURE FACIALS/ÉTERNA RED CARPET GLOW & GOLD FACIAL/"
T["red-carpet-glow-gold"] = dict(
    name="ÉTERNA Red Carpet Glow & Gold Facial", cat="signature-facials",
    lead="An elevated combination facial designed to refine, brighten and restore a polished, radiant-looking complexion.",
    card="An elevated version of our Red Carpet Glow experience for those seeking a more indulgent skin-conditioning treatment.",
    hero=RG + "good skin.jpg", thumb=(RG + "COVER.jpg", "45"),
    blocks=[
        ("about", "About Red Carpet Glow & Gold", ["A refined combination facial pairing with IS Clinical active peel + ADVATx Yellow Laser to improve skin clarity, texture and radiance."], None),
        ("cards", HOW, [
            {"name": "IS Clinical Active Peel", "text": "The active peel helps remove surface buildup and refine dull, uneven-looking skin.", "image": (RG + "active peel.png", "43")},
            {"name": "ADVATx Yellow Laser", "text": "The ADVATx Yellow Laser then helps address selected redness and skin-clarity concerns.", "image": (RG + "ADVATX YELLOW LASER.png", "43")},
        ], "Together, they create a more intensive glow-focused facial for a smoother, clearer-looking complexion."),
        ("benefits", "Benefits", ["Brightens dull-looking skin", "Refines skin texture", "Improves skin clarity", "Supports a more even-looking complexion", "Enhances overall radiance"], RG + "is clinical product.png"),
        ("acc", [(COMFORT, "Mild warmth or temporary redness may occur depending on individual skin sensitivity."),
                 (RESULTS, "Skin may appear smoother, clearer and brighter following treatment. Gentle skincare and daily sun protection are recommended.")],
         RG + "acne peel_.jpg"),
        ("who", "Who Is It For?", [("Dull skin", RG + "dull skin.jpg"), ("Uneven skin tone", RG + "uneven skin tone.webp"), ("Mild redness", RG + "redness.jpg"), ("Rough texture", RG + "Rough Skin texture.jpg")]),
    ])

EX = "ETERNA SIGNATURE FACIALS/ExoGlow DEP facial/"
T["exoglow-dep"] = dict(
    name="ÉTERNA ExoGlow Hydrating DEP Facial", cat="signature-facials",
    lead="A needle-free hydration treatment powered by dermoelectroporation technology for refreshed, comfortable and luminous-looking skin.",
    card="A hydration-focused facial incorporating advanced delivery technology to support skin comfort, moisture and radiance.",
    hero=EX + "dep 3.jpg", thumb=(EX + "dep treatment process COVER.png", "45"),
    blocks=[
        ("about", "About ExoGlow", ["A needle-free facial using dermoelectroporation (DEP) technology to enhance the delivery of selected hydrating ingredients, helping replenish moisture and revive tired-looking skin."], EX + "how dep work.jpg"),
        ("acc", [(HOW, "Controlled electrical pulses temporarily increase skin permeability, allowing selected hydrating and skin-conditioning ingredients to penetrate more effectively without injections."),
                 (COMFORT, "Non-invasive, comfortable and designed with no downtime."),
                 (RESULTS, "Skin may feel softer, more hydrated and comfortable, while appearing fresher and more radiant. Continue moisturising skincare and daily sunscreen.")],
         EX + "DEP MACHINE.jpg"),
        ("benefits", "5 Key Benefits", ["Needle-free treatment", "Supports deeper hydration", "Enhances delivery of selected active ingredients", "Improves skin comfort", "Restores a fresher, more luminous appearance"], EX + "hydrate skin.jpg"),
        ("who", "Who Is It For?", [("Dry skin", None), ("Dehydrated skin", None), ("Dull complexion", None), ("Skin feeling tight or uncomfortable", None), ("Those wanting hydration without injections", None)]),
    ])

FI = "ETERNA SIGNATURE FACIALS/Fire and Ice Facial/"
T["fire-and-ice"] = dict(
    name="iS Clinical Fire & Ice Facial", cat="signature-facials",
    lead="A professional resurfacing treatment combining intensive skin renewal with soothing hydration for a smoother, brighter complexion.",
    card="A professional resurfacing facial designed to refresh dull-looking, congested or uneven skin.",
    hero=FI + "fire and ice 1.webp", thumb=(FI + "COVER.png", "45"),
    blocks=[
        ("figure", None, FI + "fice and ice 4.webp", None),
        ("cards", "Two Masques, One Treatment", [
            {"name": "The Fire Part", "text": "The warming Intensive Resurfacing Masque uses botanical acids and extracts from sugarcane, citrus and apple to provide intensive exfoliation and refine skin texture.", "image": (FI + "fire and ice 2.webp", "45")},
            {"name": "The Ice Part", "text": "The cooling Rejuvenating Masque combines hyaluronic acid with aloe, rosemary and peppermint extracts to soothe, nourish and replenish hydration after resurfacing.", "image": (FI + "fire and ice 3.webp", "45")},
        ], None),
        ("split", "The Benefits", ["Reveal smoother, clearer and more radiant-looking skin while refining rough texture, blemishes, fine lines and congested pores. Fire & Ice delivers professional resurfacing with no residual peeling or downtime, leaving dull, tired skin looking refreshed and revitalised."], FI + "fire and ice 5.png"),
    ])

OX = "ETERNA SIGNATURE FACIALS/Oxygeneo x/"
T["oxygeneo"] = dict(
    name="OxyGeneo Facial", h1="Oxygenating Facial", cat="signature-facials",
    lead="A 3-in-1 facial combining exfoliation, oxygenation and infusion to refresh, hydrate and condition the skin.",
    card="A multi-step facial experience combining exfoliation, oxygenation and targeted skin conditioning.",
    hero=OX + "oxygeneo 1.jpg", thumb=(OX + "OXYGENEO COVER.webp", "45"),
    blocks=[
        ("about", "About OxyGeneo", ["OxyGeneo combines exfoliation + oxygenation + infusion in one comfortable treatment for smoother, fresher and more radiant-looking skin."], None),
        ("steps", HOW, [("Exfoliate", "Helps remove surface buildup and smooth the skin.", (OX + "Exfoliate.png", "c43")),
                        ("Oxygenate", "Supports the skin's natural oxygenation response.", (OX + "Oxygenate_.png", "c43")),
                        ("Nourish", "Delivers selected skin-conditioning ingredients to support hydration and nourishment.", (OX + "Nourish.png", "c43"))]),
        ("benefits", "5 Key Benefits", ["Improves skin radiance", "Supports smoother texture", "Enhances hydration", "Refreshes tired-looking skin", "Suitable for regular skin maintenance"], OX + "oxygeneo 2.jpg"),
        ("acc", [(COMFORT, "Designed as a comfortable facial with minimal expected downtime."),
                 (RESULTS, "Skin may appear smoother, fresher and more luminous following treatment. Maintain hydration and daily sun protection.")],
         OX + "oxygeneo x 3.jpg"),
        ("who", "Who Is It For?", [("Dull-looking skin", None), ("Mild dehydration", None), ("Rough skin texture", None), ("Uneven-looking complexion", None), ("Skin needing regular maintenance", None)]),
    ])

GX = "ETERNA SIGNATURE FACIALS/Glo2Facial Geneo-X/"
T["glo2facial-geneo-x"] = dict(
    name="Glo2Facial Geneo-X", h1="Glo2Facial Geneo X", cat="signature-facials",
    lead="An advanced five-technology facial designed to improve firmness, hydration, texture and overall skin radiance.",
    card="An advanced facial treatment designed to support exfoliation, oxygenation and personalised skin rejuvenation.",
    hero=GX + "glo2 facial 2.png", thumb=(GX + "treatment process_ COVER.png", "45"),
    blocks=[
        ("about", "About Glo2Facial", ["Glo2Facial Geneo-X combines OxyGeneo, TriPollar RF, ESA, Ultrasound and Neo Massage techniques in one advanced treatment targeting multiple aspects of skin quality."], None),
        ("figure", "Technologies Behind Geneo X", GX + "5 technology of GENEO X.png", None),
        ("tiles", None, [("OxyGeneo", "Exfoliates, oxygenates and enhances active ingredient absorption for fresher, more radiant skin."),
                         ("TriPollar RF", "Uses controlled RF heating to stimulate collagen and elastin for firmer, smoother skin."),
                         ("ESA", "Combines electrical impulses and RF energy to activate deeper skin renewal and improve elasticity."),
                         ("Ultrasound", "Uses gentle ultrasound waves to improve circulation and active ingredient absorption."),
                         ("Neo Massage", "Helps reduce puffiness and redness while sculpting the skin and enhancing ingredient infusion.")]),
        ("benefits", "5 Key Benefits", ["Supports firmer-looking skin", "Improves hydration", "Refines skin texture", "Enhances delivery of selected active ingredients", "Restores a brighter, more radiant complexion"], GX + "glo2facial-.jpg"),
        ("acc", [(COMFORT, "Designed to be comfortable with minimal expected downtime for most patients."),
                 (RESULTS, "Skin may appear smoother, more hydrated, firmer and more radiant following treatment. Maintain gentle skincare, hydration and daily sun protection.")],
         GX + "geneo x machine.jpeg"),
        ("who", "Who Is It For?", [("Dull or tired-looking skin", None), ("Dehydrated skin", None), ("Rough or uneven texture", None), ("Skin lacking radiance", None), ("Early loss of firmness", None)]),
    ])

# ---------- Acne, scars & pigmentation
AD = "Advatx Yellow Laser/"
T["advatx-yellow-laser"] = dict(
    name="ADVATx Yellow Laser", h1="Advanced Yellow Laser", cat="acne-scars",
    lead="A dual-wavelength laser treatment designed to improve redness, acne-related concerns, skin clarity and overall skin quality with minimal social downtime.",
    hero=AD + "advatx 2.png", thumb=(AD + "advatx-laser 5.jpg", "45"),
    blocks=[
        ("about", "What Is ADVATx Yellow Laser?", ["ADVATx is a medical solid-state dual-wavelength laser combining 589 nm yellow light and 1319 nm infrared energy in one platform. The two wavelengths work at different levels of the skin, allowing treatment to be tailored according to different skin concerns."], AD + "advatx 1.avif"),
        ("tiles", "Dual-Wavelength Technology", [
            ("589 nm Yellow Laser", "Targets selected redness and vascular concerns, helping improve the appearance of a flushed or uneven-looking complexion."),
            ("1319 nm Infrared Laser", "Provides controlled deeper heating to support skin rejuvenation, acne-related concerns and overall skin quality. The manufacturer also notes that this wavelength supports fibroblast activity and helps reduce sebum production.")]),
        ("benefits", "Benefits", ["Helps improve the appearance of redness", "Supports clearer-looking acne-prone skin", "Helps improve acne marks and scars", "Supports smoother, healthier-looking skin"], AD + "AdvaTx machine.png"),
        ("acc", [(COMFORT, "ADVATx is designed for little to no downtime. Temporary warmth or mild redness may occur depending on treatment settings and individual skin response."),
                 (RESULTS, "Results develop progressively depending on the concern being treated and the number of sessions required. After treatment, maintain gentle skincare, good hydration and daily sun protection as advised by your practitioner.")],
         AD + "advatx-laser- 6.jpg"),
        ("who", "Who Is It For?", [("Active Acne", AD + "active acne.png"), ("Redness", AD + "redness.jpg"), ("Acne Marks & Scars", AD + "acne-scar-1.jpg"), ("Uneven Skin Tone", AD + "uneven skin tone.webp"), ("Dull, Tired-Looking Skin", AD + "dull skin.jpg")]),
    ])

PI = "Pico Laser Treatment/"
T["pico-laser"] = dict(
    name="Pico Laser", cat="pigmentation",
    lead="An advanced laser treatment designed to target pigmentation, uneven skin tone, dullness and selected textural concerns with minimal disruption to daily activities.",
    hero=PI + "pico laser 1.png", thumb=(PI + "pico laser 1.png", "45"), thumb_alt=(PI + "pigmentasi.jpeg", "45", (0.62, 0.5)),
    blocks=[
        ("about", "What Is Pico Laser?", ["Pico Laser delivers ultra-short pulses of laser energy in picoseconds to target unwanted pigment while limiting unnecessary heat exposure to surrounding skin.",
                                          "The treatment can be customised according to the type and depth of pigmentation, as well as the patient’s overall skin condition."], PI + "Picohi machine.jpg"),
        ("figure", HOW, PI + "how it work_.webp", ["Pico Laser delivers energy in extremely short pulses to break targeted pigment into smaller particles, allowing the body’s natural clearance processes to gradually remove them.",
                                                   "Selected settings may also be used to support skin clarity, texture refinement and overall rejuvenation."]),
        ("benefits", "Benefits", ["Helps improve pigmentation", "Brightens dull-looking skin", "Supports a more even skin tone", "Helps refine skin texture", "Improves overall skin clarity"], None),
        ("acc", [(COMFORT, "Treatment is generally well tolerated with minimal expected downtime. Temporary redness, warmth or mild sensitivity may occur depending on the treatment settings and area treated."),
                 (RESULTS, "Pigmentation and overall skin clarity may improve progressively over a series of treatments. After treatment, maintain gentle skincare, good hydration and strict daily sun protection.")], None),
        ("who", "Who Is It For?", [("Sun Spots / Freckles", PI + "sun spot.jpg"), ("Pigmentation", PI + "pigmentasi.jpeg"), ("Uneven Skin Tone", PI + "uneven skin tone.webp"), ("Dull-Looking Skin", PI + "dull skin.jpg"), ("Rough Texture", PI + "Rough Skin texture.jpg")]),
    ])

AP = "ACNE CLARIFYING PEEL/"
T["clarity-acne-peel"] = dict(
    name="Clarity Acne Peel", cat="acne-scars",
    lead="A professional chemical peel designed for acne-prone, congested and oily skin, helping remove surface buildup and improve overall skin clarity.",
    hero=AP + "acne peel 1.jpg", thumb=(AP + "acne peel 3.jpg", "45"),
    blocks=[
        ("acc", [(HOW, "The peel uses selected exfoliating acids to loosen dead skin cells, clear surface congestion and support a smoother, clearer-looking complexion."),
                 (COMFORT, "Mild tingling, redness or light peeling may occur after treatment. Downtime is usually minimal and varies according to skin sensitivity."),
                 (RESULTS, "Skin may appear clearer and smoother over the following days. Use gentle skincare, good hydration and daily sun protection after treatment.")],
         AP + "acne peel 2.jpg"),
        ("benefits", "5 Key Benefits", ["Helps improve active breakouts", "Clears congested pores", "Refines rough skin texture", "Helps reduce excess oiliness", "Improves overall skin clarity"], AP + "acne peel 4.jpg"),
        ("who", "Who Is It For?", [("Active Acne", AP + "active acne.jpg"), ("Redness", AP + "redness.jpg"), ("Congested Pores", AP + "Congested Pores.jpg"), ("Blackheads", AP + "blackheads.png")]),
    ])

EP = "EPN microneedling/"
T["epn-microneedling"] = dict(
    name="EPN Microneedling", cat="acne-scars",
    lead="A skin-renewal treatment combining microneedling with targeted ingredient delivery to improve texture, pores, acne scars and overall skin quality.",
    hero=EP + "microneedling 4.jpg", thumb=(EP + "microneedling 1.jpg", "45"),
    blocks=[
        ("about", "What Is EPN Microneedling?", ["EPN creates controlled microchannels in the skin while supporting the delivery of selected active ingredients, helping stimulate the skin’s natural renewal process."], EP + "epn machine 1.webp"),
        ("acc", [(HOW, "Microneedling creates tiny controlled channels in the skin to support collagen renewal and skin repair, while selected ingredients are delivered during treatment to enhance overall skin conditioning.")], EP + "epn-machine-2.jpg"),
        ("benefits", "Benefits", ["Refines skin texture", "Helps reduce the appearance of enlarged pores", "Improves acne scars", "Supports collagen renewal", "Improves overall skin quality"], EP + "epn-machine-3.jpg"),
        ("figure", "Results", EP + "before and after.png", None),
        ("who", "Who Is It For?", [("Enlarged Pores", None), ("Acne Scars", None), ("Rough Skin Texture", None), ("Uneven Skin Surface", None), ("Early Fine Lines", None)]),
    ])

CO = "CO2 laser/"
T["co2-laser"] = dict(
    name="CO₂ Laser", h1="Fractional CO₂ Laser", cat="acne-scars", hero_mode="banner",
    lead="CO₂ laser is a versatile treatment that can be used for both fractional skin resurfacing and the precise removal of selected superficial skin lesions.",
    hero=CO + "CO₂ Precision Removal.jpg", thumb=(CO + "CO₂ Laser Resurfacing.png", "45"),
    blocks=[
        ("modes", [
            {"name": "CO₂ Laser Resurfacing", "text": "Fractional CO₂ creates controlled microscopic treatment zones to stimulate skin renewal and collagen remodelling, improving deeper textural concerns.",
             "bullets": ["Acne Scars", "Enlarged Pores", "Rough Skin Texture", "Fine Lines", "Uneven Skin Surface"], "image": CO + "co2 resurfacing before and after.png"},
            {"name": "CO₂ Precision Removal", "text": "Focused CO₂ energy can also be used to precisely remove suitable skin tags and selected superficial benign lesions while limiting unnecessary treatment of surrounding skin.",
             "bullets": ["Skin Tags", "Small Raised Bumps", "Selected Benign Superficial Lesions", "Localised Unwanted Growths"], "image": CO + "co2 removal before and after.png"},
        ]),
        ("about", COMFORT, ["Recovery depends on the treatment performed. Fractional resurfacing typically involves several days of redness, swelling and peeling, while small-area removal may cause temporary redness, tenderness or crusting."], None),
    ], cta="Book a Consultation")

BP = "Brightening Peel/"
T["brightening-peel"] = dict(
    name="Brightening Peel", cat="pigmentation",
    lead="A professional chemical peel designed to improve dullness, uneven skin tone and superficial pigmentation by removing surface buildup and encouraging skin renewal.",
    hero=BP + "brightening peel 1.jpg", thumb=(BP + "brighteing 4.jpg", "45"),
    blocks=[
        ("acc", [(HOW, "Selected exfoliating acids help lift away dead skin cells and improve surface turnover, allowing the complexion to appear brighter, smoother and more even-looking."),
                 (COMFORT, "Mild tingling, redness or light peeling may occur. Downtime is usually minimal and varies according to skin sensitivity."),
                 (RESULTS, "Skin may appear brighter and smoother over the following days. Maintain gentle skincare, hydration and daily sun protection.")],
         BP + "brightening 3.jpg"),
        ("benefits", "5 Key Benefits", ["Brightens dull-looking skin", "Improves uneven skin tone", "Helps reduce the appearance of superficial pigmentation", "Refines skin texture", "Restores a fresher-looking glow"], BP + "brightening 2.jpg"),
        ("who", "Who Is It For?", [("Dull Skin", None), ("Uneven Skin Tone", None), ("Superficial Pigmentation", None), ("Sun-Damaged Appearance", None), ("Rough, Lacklustre Skin", None)]),
    ])

RP = "RETINOL RENEWAL PEEL/"
T["renewal-retinol-peel"] = dict(
    name="Renewal Retinol Peel", cat="pigmentation",
    lead="A retinol-based professional peel designed to support skin renewal, smoother texture and a fresher-looking complexion.",
    hero=RP + "retinol 1.jpg", thumb=(RP + "retinol 4.jpg", "45"),
    blocks=[
        ("figure", None, RP + "Renewal Retinol Peel 5.png", None),
        ("acc", [(HOW, "Retinol supports skin-cell turnover, helping improve the appearance of rough texture, fine lines and uneven-looking skin over time."),
                 (COMFORT, "Dryness, mild redness or visible peeling may occur after treatment. Downtime varies according to individual skin response."),
                 (RESULTS, "Skin may gradually appear smoother and more refined as the renewal process continues. Use gentle skincare, hydration and strict daily sun protection.")],
         RP + "retinol 2.jpg"),
        ("benefits", "5 Key Benefits", ["Supports skin renewal", "Refines rough texture", "Softens the appearance of fine lines", "Improves uneven-looking skin", "Restores a smoother, fresher-looking complexion"], RP + "retinol 3.jpg"),
        ("who", "Who Is It For?", [("Fine Lines", None), ("Rough Skin Texture", None), ("Dull Skin", None), ("Uneven Skin Tone", None), ("Early Ageing Skin", None)]),
    ])

T["pink-peel"] = dict(
    name="Pink Peel", cat="pigmentation", hero_mode="text", hero=None, thumb=None,
    lead="A professional peel designed for selected intimate or friction-prone areas where uneven tone or dull-looking skin may develop.",
    blocks=[
        ("acc", [(HOW, "Selected exfoliating ingredients help remove surface buildup and support more even-looking skin in appropriate treatment areas."),
                 (COMFORT, "Mild sensitivity, dryness or light peeling may occur temporarily depending on the area and individual skin response."),
                 (RESULTS, "Improvement develops progressively. Follow the recommended aftercare, avoid unnecessary friction and use appropriate skincare for the treated area.")], None),
        ("benefits", "5 Key Benefits", ["Helps improve uneven-looking tone", "Supports a brighter-looking appearance", "Refines rough surface texture", "Helps refresh dull-looking skin", "Designed for selected delicate areas"], None),
        ("who", "Who Is It For?", [("Uneven Intimate-Area Tone", None), ("Inner-Thigh Discolouration", None), ("Underarm Darkening", None), ("Friction-Related Dullness", None), ("Rough or Uneven Texture", None)]),
    ])

# ---------- Skin boosters
CB = "Skin Booster/CELLBOOSTER/"
T["cellbooster"] = dict(
    name="CELLBOOSTER®", h1="Suisselle Skin Booster", cat="skin-boosters",
    lead="CELLBOOSTER® is a Swiss-made injectable range powered by patented CHAC Technology, combining stabilised hyaluronic acid with selected active ingredients for different skin, contour and hair concerns.",
    hero=CB + "cellbooster 2.webp", thumb=(CB + "cellbooster 1.png", "45"),
    blocks=[
        ("cards", "The CELLBOOSTER® Range", [
            {"name": "CELLBOOSTER® GLOW", "bullets": ["Deeply hydrates dry, tired-looking skin", "Improves radiance and uneven tone", "Supports healthier-looking skin against oxidative stress"], "image": CB + "cellbooster-glow-750x725-1.jpg"},
            {"name": "CELLBOOSTER® LIFT", "bullets": ["Improves skin hydration and firmness", "Softens the appearance of fine lines and skin laxity", "Supports collagen production and skin density"], "image": CB + "cellbooster-lift-750x725-1 (1).jpg"},
            {"name": "CELLBOOSTER® SHAPE", "bullets": ["Targets localised fat deposits", "Helps reduce fluid retention and puffiness", "Supports improved microcirculation and contour definition"], "image": CB + "cellbooster-shape-1-750x725-1.jpg"},
            {"name": "CELLBOOSTER® HAIR", "bullets": ["Supports hair follicle strength", "Promotes healthier hair growth and density", "Improves scalp microcirculation and hair fibre quality"], "image": CB + "cellbooster-hair-980x947.jpg"},
        ], None),
    ], cta="Book a Consultation")

NC = "Skin Booster/NCTF® 135 HA/"
T["nctf-135-ha"] = dict(
    name="NCTF", h1="NCTF® 135 HA", cat="skin-boosters",
    lead="A revitalising skin booster for fresher, brighter and more youthful-looking skin.",
    hero=NC + "NCTF135HA-Hero-Banner-Square-1024x956.png", thumb=(NC + "4ae2e431-26e5-4cdd-acfa-142b36cc032b.webp", "45", (0.45, 0.5)),
    blocks=[
        ("about", "What Is NCTF® 135 HA?", ["NCTF® 135 HA combines free hyaluronic acid with 60 skin-supporting ingredients, including vitamins, amino acids, minerals and co-enzymes, to revitalise tired or ageing skin."], NC + "nctf2.jpg"),
        ("acc", [(HOW, "Small amounts are injected into the skin to deliver hyaluronic acid and revitalising nutrients directly where they are needed, supporting hydration, skin density and a fresher-looking complexion."),
                 (COMFORT, "Downtime is generally minimal. Small bumps, redness, tenderness or mild bruising can occur temporarily after injection."),
                 (RESULTS, "Skin improvement develops progressively over a treatment course. The official protocol commonly uses 3 sessions around 3 weeks apart, with maintenance according to individual needs. After treatment, keep skincare gentle and use daily sun protection.")],
         NC + "nctf 1.jpg"),
        ("benefits", "Benefits", ["Improves skin hydration", "Restores radiance", "Softens fine lines", "Supports better skin firmness and density", "Improves overall skin quality"], NC + "nctf 3.jpg"),
        ("who", "What Skin Concerns Can It Treat?", [("Dehydrated Skin", None), ("Dull Skin", None), ("Fine Lines", None), ("Loss of Firmness", None), ("Tired or Ageing Skin", None)]),
    ])

RV = "Skin Booster/Restylane Skinboosters Vital Light/"
T["restylane-vital-light"] = dict(
    name="Restylane Skinboosters Vital Light", cat="skin-boosters",
    lead="Restylane Vital Light is a skin booster made with stabilised hyaluronic acid designed to improve skin hydration, elasticity and smoothness.",
    hero=RV + "Restylane Skinboosters Vital Light 2.png", thumb=(RV + "Restylane Skinboosters Vital Light 1.png", "45"),
    blocks=[
        ("acc", [(HOW, "Hyaluronic acid is injected into the skin where it binds water and helps improve hydration and skin elasticity from within.")], RV + "Restylane Skinboosters Vital Light 3.png"),
        ("benefits", "Benefits", ["Improves skin hydration", "Supports better skin elasticity", "Smooths rough skin texture", "Softens the appearance of fine lines", "Restores a fresher, healthier-looking complexion"], RV + "Restylane Skinboosters Vital Light 1.png"),
        ("who", "What Skin Concerns Can It Treat?", [("Dehydrated Skin", None), ("Fine Lines", None), ("Rough Skin Texture", None), ("Loss of Elasticity", None), ("Dull, Tired-Looking Skin", None)]),
    ])

NV = "Skin Booster/Neauvia Hydro Deluxe/"
T["neauvia-hydro-deluxe"] = dict(
    name="Neauvia Hydro Deluxe", cat="skin-boosters",
    lead="Deep hydration with a smoother, more refined skin finish.",
    hero=NV + "neuvia 2.png", thumb=(NV + "neuvia 1.png", "45"),
    blocks=[
        ("about", "What Is Neauvia Hydro Deluxe?", ["Neauvia Hydro Deluxe is an injectable skin booster formulated with hyaluronic acid and skin-supporting ingredients to improve hydration, elasticity and overall skin quality."], NV + "neuvia 3.png"),
        ("acc", [(HOW, "The treatment delivers hyaluronic acid directly into the skin to help attract and retain moisture while supporting a smoother, more supple appearance."),
                 (COMFORT, "Mild redness, swelling, tenderness, bruising or small injection bumps may occur temporarily after treatment. Downtime is generally minimal."),
                 (RESULTS, "Skin may appear more hydrated, smoother and more refreshed as results develop. Maintain gentle skincare, hydration and daily sun protection.")],
         NV + "neuvia 4.png"),
        ("benefits", "5 Key Benefits", ["Improves deep hydration", "Supports better skin elasticity", "Refines skin texture", "Softens the appearance of fine lines", "Restores a fresher, healthier-looking complexion"], NV + "neuvia 1.png"),
        ("who", "What Skin Concerns Can It Treat?", [("Dry Skin", NV + "dry skin.jpg"), ("Fine Lines", NV + "fine line.jpg"), ("Rough Skin Texture", NV + "Rough Skin texture.jpg"), ("Loss of Elasticity", NV + " Loss of Elasticity.png"), ("Dull Skin", NV + "dull skin.jpg")]),
    ])

RK = "Skin Booster/RevoK50/"
T["revok50"] = dict(
    name="RevoK50", cat="skin-boosters",
    lead="Revive tired skin with hydration, smoothness and renewed radiance.",
    hero=RK + "REVOK50 1.png", thumb=(RK + "revok50 3.png", "45"),
    blocks=[
        ("about", "What Is RevoK50?", ["RevoK50 is an injectable skin booster designed to improve hydration, skin texture and overall skin quality, helping tired-looking skin appear fresher, smoother and more luminous."], None),
        ("acc", [(HOW, "RevoK50 delivers hyaluronic acid and amino acids directly into the skin, helping restore moisture while supporting the skin’s natural collagen and renewal processes for a smoother, firmer and healthier-looking complexion.")], RK + "revok50 2.png"),
        ("benefits", "Benefits", ["Deep Hydration", "Smoother Lines", "Firmer Skin", "Brighter Complexion", "Skin Repair"], RK + "revok50 3.png"),
        ("figure", "Treatment Areas", RK + "revok50 inject zone.jpg", None),
    ])

RJ = "Skin Booster/Rejuran HB Plus/"
RH = "Skin Booster/Rejuran Healer/"
T["rejuran"] = dict(
    name="REJURAN", h1="Rejuran", cat="skin-boosters", hero_mode="banner",
    lead="Rejuran is a skin-healing treatment using polynucleotides from salmon DNA to rejuvenate and repair the skin.",
    hero=RJ + "banner rejuran.png", thumb=(RH + "rejuran-healer-2.jpg", "45"),
    blocks=[
        ("about", "About Rejuran", ["Originating from South Korea, it contains PN (polynucleotide), extracted from salmon, as the main active ingredient.",
                                    "Salmon DNA was chosen because scientists found that it can accelerate the healing processes of skin cells, boosting collagen production, improving the skin barrier and enhancing wound healing. Salmon DNA is also similar to human DNA, ensuring there is little risk of an immune response when it is injected into the body."],
         RJ + "Rejuran-PN-768x235-1.png"),
        ("cards", None, [
            {"name": "Specialised DNA for Skin", "text": "PDRN, a raw material reborn as an ingredient for cosmetics products.", "image": RJ + "specialised-dna-min_540x.webp"},
            {"name": "Skin Improvement Activator", "text": "REJURAN Cosmetics is proven to be the most compatible with human skin.", "image": RJ + "skinactivator-min_540x.webp"},
            {"name": "Fundamental Change in Skin", "text": "Promoting the secretion of collagen, restoring thin and damaged skin.", "image": RJ + "fundamental-change-skin-min_540x.webp"},
            {"name": "Enhanced Skin Absorption", "text": "670 times smaller than skin pores, allowing effective skin penetration and helping to reinforce the skin barrier.", "image": RJ + "enhanced-skin-absorption-min_540x.webp"},
        ], None),
        ("about", "How REJURAN Works", ["REJURAN delivers polynucleotides (PN) into the skin to support its natural repair and renewal processes. Over time, this helps improve texture, elasticity, hydration and overall skin quality."], None),
        ("variants", "Which REJURAN Is Right for You?", [
            {"id": "healer", "name": "REJURAN HEALER", "text": "Rejuran Healer repairs and rejuvenates aging or damaged skin. Unlike hyaluronic acid skinboosters, Rejuran Healer consists of biologically active molecules that stimulate regenerative processes and reduce inflammation.",
             "bullets": ["Reduction in pore size", "Increased skin elasticity and firmness", "Increased skin hydration", "Improvement acne scars", "Increase regeneration of skin cells"],
             "suit": "For those in their 30s and above, with dry skin and frequent skin problems. It is also indicated in those with wrinkles on the neck, around the eyes, and have stretch marks which are difficult to treat with other options.",
             "image": (RH + "rejuran healer 1.webp", "43")},
            {"id": "hb-plus", "name": "REJURAN HB PLUS", "text": "Rejuran HB is mainly used to strengthen the skin’s regenerative ability whilst providing an intense hydration effect on dehydrated areas.",
             "bullets": ["Strengthens skin regenerative ability", "Provide intense skin hydration", "Improves skin elasticity", "Softens fine lines & wrinkles", "Improve overall skin texture"],
             "suit": "This treatment is suitable for individuals with dry skin looking for an overall intense skin hydration instead of healing for skin repair, achieving that Korean ‘Glass Skin’ look.",
             "image": (RJ + "rejuran hb 2.jpg", "43")},
        ]),
        ("about", "What to Expect", ["Results develop gradually as the skin undergoes renewal. Skin may appear smoother, firmer and healthier-looking over time. Mild redness, swelling or small injection bumps may occur temporarily after treatment."], None),
        ("figure", "What Can Rejuran Treat?", RJ + "what can rejuran treats.png", None),
    ], cta="Book a Consultation")

PN = "Skin Booster/Plinest & Newest/"
T["plinest-newest"] = dict(
    name="PLINEST® & NEWEST®", cat="skin-boosters",
    lead="Italian-made polynucleotide treatments powered by PN-HPT™, the original PN technology from Italy with more than 100 published clinical studies. Designed to support skin repair, collagen production and elasticity for healthier, revitalised skin.",
    hero=PN + "plinest and newest_.png", thumb=(PN + "PLINEST.png", "45"),
    blocks=[
        ("figure", None, PN + "Italian-made polynucleotide.png", None),
        ("cards", None, [
            {"name": "PLINEST®", "text": "A PN-HPT™ treatment focused on skin biorevitalisation and regeneration, helping improve ageing or damaged skin from within.", "image": PN + "PLINEST.png"},
            {"name": "NEWEST®", "text": "Combines PN-HPT™ with Hyaluronic Acid and Mannitol, providing regenerative support together with enhanced hydration, elasticity and radiance.", "image": PN + "NEWEST.png"},
        ], None),
        ("benefits", "Benefits", ["Supports Skin Regeneration", "Improves Firmness & Elasticity", "Supports Collagen Production", "Refines Fine Lines & Skin Texture", "Improves Hydration & Radiance"], None),
        ("who", "Suitable For", [("Ageing Skin", PN + "aging skin.jpg"), ("Dry Skin", PN + "dry skin.jpg"), ("Loss of Firmness", PN + "loss of firmness.png"), ("Wrinkles & Fine Lines", PN + "wrinkles & fine line.jpg")]),
        ("timeline", "What to Expect", [
            ("After First Session", "Skin may feel more hydrated, refreshed and supple, with an early improvement in overall firmness."),
            ("After Second Session", "As skin renewal progresses, texture, fine lines and overall smoothness may begin to improve, with a healthier-looking radiance."),
            ("After Third Session", "Continued treatment supports firmer, more resilient and revitalised-looking skin, with progressive improvement in overall skin quality.")]),
    ], cta="Book a Consultation")

PF = "Skin Booster/Profhilo/"
T["profhilo"] = dict(
    name="Profhilo", cat="skin-boosters",
    lead="Profhilo is an injectable hyaluronic acid bioremodelling treatment designed to improve hydration, firmness and overall skin quality without traditional volumising filler effects.",
    hero=PF + "Profhilo 2.jpg", thumb=(PF + "Profhilo 2.jpg", "45"),
    blocks=[
        ("acc", [(HOW, "Highly concentrated hyaluronic acid is injected at selected points, where it spreads through the tissue to support hydration and skin remodelling."),
                 (COMFORT, "Small injection bumps may appear temporarily after treatment and usually settle. Downtime is generally minimal."),
                 (RESULTS, "Skin may progressively appear more hydrated, smoother and firmer following treatment.")],
         PF + "Profhilo 1.png"),
        ("benefits", "Benefits", ["Provides deep hydration", "Supports firmer-looking skin", "Improves skin elasticity", "Softens fine lines", "Improves overall skin quality"], None),
        ("who", "What Skin Concerns Can It Treat?", [("Dehydrated Skin", None), ("Skin Laxity", None), ("Fine Lines", None), ("Loss of Elasticity", None), ("Crepey or Ageing Skin", None)]),
    ])

NX = "Skin Booster/NXO Exosome/"
T["nxo-exosome"] = dict(
    name="NXO Exosome", cat="skin-boosters",
    lead="Support recovery. Renew from within.",
    hero=NX + "NXO 1.png", thumb=(NX + "NXO 2.png", "45"),
    blocks=[
        ("about", "What Is Exosome Therapy?", ["Exosomes are tiny extracellular vesicles involved in cell-to-cell communication. In aesthetic regenerative treatments, exosome-based formulations are used to support the skin or scalp environment during recovery and renewal.",
                                               "At ÉTERNA, NXO Exosome protocols are available for both facial skin rejuvenation and scalp/hair care."], None),
        ("benefits", "Benefits", ["Supports Recovery & Regeneration", "Helps improve Skin & Scalp Condition", "Supports a healthier renewal environment", "Helps revitalise tired or stressed tissue", "Complements skin and hair rejuvenation programmes"], NX + "NXO 2.png"),
        ("cards", "Treatment Areas", [
            {"name": "FACE", "text": "For dullness, dehydration, rough texture and stressed-looking skin, supporting a fresher and healthier-looking complexion.", "image": (NX + "exosome face.webp", "43")},
            {"name": "HAIR & SCALP", "text": "For weakened hair, thinning concerns and scalp rejuvenation, supporting a healthier scalp environment as part of a hair-care programme.", "image": (NX + "exosome hair.jpg", "43")},
        ], None),
    ], cta="Book a Consultation")

ND = "Skin Booster/NADRx Skinbooster/"
T["nadrx-skinbooster"] = dict(
    name="NADRx Skinbooster", cat="skin-boosters",
    lead="Recharge tired-looking skin with hydration and renewed vitality.",
    hero=ND + "NADRX 1.jpg", thumb=(ND + "NADRX 1.jpg", "45"),
    blocks=[
        ("about", "What Is NADRx Skinbooster?", ["NADRx is a regenerative skin booster designed to support hydration, skin conditioning and a fresher, healthier-looking complexion."], None),
        ("acc", [(HOW, "The formulation is delivered into the skin as part of a regenerative skin protocol, supporting hydration and overall skin quality."),
                 (RESULTS, "Skin may gradually appear more hydrated, refreshed and luminous.")], None),
        ("benefits", "Benefits", ["Improves hydration", "Revives tired-looking skin", "Supports smoother texture", "Enhances radiance", "Improves overall skin quality"], None),
        ("who", "What Skin Concerns Can It Treat?", [("Dry Skin", ND + "dry skin.jpg"), ("Tired-Looking Skin", ND + "tired looking skin.png"), ("Rough Skin Texture", ND + "Rough Skin texture.jpg"), ("Early Ageing Skin", ND + "Early Ageing Skin.jpg")]),
    ])

EL = "Skin Booster/Elesome Skinbooster/"
T["elesome-skinbooster"] = dict(
    name="Elesome Skinbooster", cat="skin-boosters",
    lead="Elesome is a regenerative skin booster designed to support hydration, skin recovery and overall skin quality.",
    hero=EL + "elesome skinbooster.webp", thumb=(EL + "elesome skinbooster.webp", "45", (0.62, 0.5)),
    blocks=[
        ("acc", [(HOW, "The treatment delivers selected skin-conditioning ingredients directly into the skin to support hydration and progressive rejuvenation."),
                 (RESULTS, "Skin may progressively appear smoother, fresher and better hydrated.")], None),
        ("benefits", "5 Key Benefits", ["Improves hydration", "Supports skin recovery", "Refines skin texture", "Enhances radiance", "Supports healthier-looking skin"], None),
        ("who", "What Skin Concerns Can It Treat?", [("Dry Skin", EL + "dry skin.jpg"), ("Dull Skin", EL + "dull skin.jpg"), ("Rough Skin Texture", EL + "Rough Skin texture.jpg"), ("Early Ageing Skin", EL + "aging skin.jpg")]),
    ])

PR = "Skin Booster/PRP Face/"
T["prp-face"] = dict(
    name="PRP Face", cat="skin-boosters", hero_mode="text", hero=None,
    lead="PRP uses platelet-rich plasma prepared from your own blood as part of a regenerative treatment that supports skin renewal and overall skin quality.",
    thumb=(PR + "PRP-Skin-Treatment.webp", "45"),
    blocks=[
        ("steps", HOW, [("Blood drawn", "A small amount of your blood is drawn.", (PR + "Blood Draw.webp", "43")),
                        ("Centrifugation", "The blood is spun in a centrifuge to separate the platelet-rich plasma.", (PR + "PRP Centrifugation.jpg", "43")),
                        ("PRP skin treatment", "The PRP is applied to your skin via micro-needling or injections, targeting specific areas for rejuvenation.", (PR + "PRP-Skin-Treatment.webp", "43"))],
         "A small amount of blood is collected and processed to concentrate the platelet-rich plasma, which is then used in the treatment area to support the skin’s natural repair response."),
        ("benefits", "Benefits", ["Supports natural skin renewal", "Downtime is usually minimal to mild", "Supports smoother texture", "Helps improve fine lines", "Supports healthier-looking radiance"], None),
        ("about", RESULTS, ["Results develop gradually as the skin’s regenerative response continues. Follow post-treatment skincare and sun-protection advice."], None),
    ])

# ---------- Lifting, rejuvenation, contouring
DN = "Density Noir/"
T["density"] = dict(
    name="DENSITY RF", h1="DENSITY", cat="face-lifting", hero_mode="banner",
    lead="DENSITY is an advanced radiofrequency treatment combining Monopolar and Bipolar RF energy to deliver controlled heating at different skin depths. By stimulating collagen and elastin remodelling, DENSITY helps improve skin firmness, smoothness and facial definition with no needles and minimal downtime.",
    hero=DN + "DENSITY RF 1.png", thumb=(DN + "DENSITY RF 1.png", "45", (0.66, 0.5)),
    blocks=[
        ("figure", "How Does It Work?", DN + "how does density work.png", None),
        ("figure", "Patented Sequential Heating Technology", DN + "density rf 2.png", None),
        ("split", "Smooth & Adjustable Cooling with 5 Levels", ["DENSITY uses a gas-spraying cooling system adjustable across five levels to help protect the skin during RF energy delivery.",
                                                               "Cooling can be customised according to skin condition, treatment area and treatment intensity, allowing a more precise and comfortable treatment experience."],
         DN + "Smooth & Adjustable Cooling with 5 Levels.png"),
        ("figure", "Handpieces & Tips", DN + "handpiece and tips.png", None),
        ("pair", "Real Result", [DN + "before and after 1.png", DN + "before and after 2.png"]),
        ("benefits", "Benefits", ["Tighten loose skin", "Improves facial and jawline definition", "Supports new collagen and elastin", "Immediate tightening with progressive improvement", "Results may last up to 12 months"], None),
        ("acc", [(COMFORT, "Integrated cooling keeps treatment comfortable with no downtime. Most patients can return to normal activities after treatment."),
                 (RESULTS, "Some tightening may be seen early, with progressive improvement over 4–6 months as collagen remodelling continues. Maintain good hydration, gentle skincare and daily sun protection.")], None),
        ("who", "Who Is It For?", [("Sagging Cheeks", DN + "Sagging Cheeks.jpg"), ("Loose Jawline", DN + "Loose Jawline.jpg"), ("Jowls", DN + "Jowls.jpg"), ("Fine Lines & Wrinkles", DN + "Fine Lines & Wrinkles.jpg"), ("Loose Skin Around the Eyes", DN + "Loose Skin Around the Eyes.jpg")]),
    ])

BX = "botox/"
T["botox"] = dict(
    name="Botox", cat="botox",
    lead="Soften lines. Preserve expression.",
    hero=BX + "botox 1.jpg", thumb=("BOTOX COVER.jpg", "45"),
    blocks=[
        ("about", "What Is Botox?", ["A targeted botulinum toxin treatment designed to relax selected facial muscles and soften the appearance of dynamic expression lines."], None),
        ("acc", [(HOW, "Botox temporarily reduces excessive muscle activity in selected areas, helping expression lines appear smoother while maintaining a natural-looking result."),
                 (COMFORT, "Treatment is quick with minimal downtime. Small injection marks, mild redness or bruising may occur temporarily."),
                 (RESULTS, "Results develop gradually over several days. Avoid rubbing the treated areas and follow the practitioner’s aftercare advice.")],
         BX + "before and after botox.jpg"),
        ("benefits", "Benefits", ["Wrinkle Smoothing", "Features Contouring", "Minimized Fine Lines", "Non-Surgical Solution"], None),
        ("who", "Who Is It For?", [("Forehead Lines", BX + "Forehead Lines.jpg"), ("Frown Lines", BX + "Frown Lines.jpg"), ("Crow’s Feet", BX + "Crow’s Feet.jpg")]),
    ])

FF = "Premium Facial Fillers/"
T["premium-facial-fillers"] = dict(
    name="Premium Facial Fillers", cat="face-eye-rejuvenation",
    lead="Facial fillers are injectable treatments used to restore lost volume, structural support and facial balance in selected areas of the face.",
    hero=FF + "facial filler 3.jpg", thumb=(FF + "facial filler 2.jpeg", "45", (0.55, 0.5)),
    blocks=[
        ("acc", [(HOW, "A carefully selected filler is placed beneath the skin to support areas affected by volume loss or reduced structural support, helping improve contour and facial proportions."),
                 (RESULTS, "Results are usually visible immediately, with the final appearance settling as swelling reduces. Avoid unnecessary pressure on treated areas and follow the practitioner’s aftercare advice.")],
         FF + "facial filler 1.jpg"),
        ("benefits", "5 Key Benefits", ["Restores lost facial volume", "Improves facial contour", "Supports better facial balance", "Softens the appearance of hollows and folds", "Creates a more refreshed, structured appearance"], FF + "facial filler 2.jpeg"),
        ("who", "Who Is It For?", [("Facial Volume Loss", None), ("Sunken Cheeks", None), ("Nasolabial Folds", None), ("Weak Chin Definition", None), ("Loss of Facial Contour", None)]),
    ])

FB = "Facial Biostimulators/"
T["facial-biostimulators"] = dict(
    name="Facial Biostimulators", cat="face-lifting",
    lead="Collagen biostimulators are injectable treatments designed to stimulate the skin’s own collagen production, helping improve firmness, support and overall skin quality over time.",
    hero=FB + "Biostimulators 1.png", thumb=(FB + "Biostimulators 1.png", "45", (0.72, 0.5)),
    blocks=[
        ("figure", HOW, FB + "how Biostimulators works.png", ["The treatment is placed in selected areas of the face to trigger a gradual regenerative response, supporting collagen formation and tissue renewal rather than simply adding immediate volume."]),
        ("benefits", "Benefits", ["Supports natural collagen production", "Improves skin firmness", "Helps reduce skin laxity", "Enhances facial support", "Improves overall skin quality"], FB + "Biostimulator before and after.jpg"),
        ("who", "Who Is It For?", [("Loss of Firmness", None), ("Skin Laxity", None), ("Reduced Facial Support", None), ("Early Sagging", None), ("Ageing Skin", None)]),
        ("about", RESULTS, ["Results develop gradually over the following weeks to months as collagen production increases. Follow the practitioner’s aftercare advice and avoid unnecessary pressure on treated areas."], None),
    ])

EY = "Eye Rejuvenation/"
T["eye-rejuvenation"] = dict(
    name="Eye Rejuvenation", cat="face-eye-rejuvenation",
    lead="Restore support. Refresh tired-looking eyes.",
    hero=EY + "eye 2.jpg", thumb=(EY + "eye 3.jpg", "45"),
    blocks=[
        ("about", "What Is Eye Rejuvenation?", ["Eye rejuvenation is a personalised treatment approach designed to improve under-eye hollowness, dark circles, fine lines and loss of support around the eye area."], EY + "eye 1.jpg"),
        ("acc", [(HOW, "Treatment is customised according to the main cause of the concern and may combine eye skinboosters, scaffold threads, collagen-supporting injectables or energy-based treatments."),
                 (COMFORT, "Downtime depends on the treatment combination used. Mild swelling, tenderness, bruising or redness may occur temporarily."),
                 (RESULTS, "Results develop according to the treatment selected. Some improvements may be visible early, while regenerative treatments continue to improve progressively. Follow the practitioner’s aftercare advice and use gentle skincare around the eye area.")],
         EY + "eye 3.jpg"),
        ("benefits", "5 Key Benefits", ["Improves under-eye hollowness", "Helps soften dark circles", "Supports smoother fine lines", "Restores structural support", "Refreshes the overall eye area"], None),
    ])

PB = "PB Serum/"
T["pb-serum"] = dict(
    name="PB Serum", cat="face-contouring",
    lead="PB Serum is an injectable treatment range designed to address selected facial contour, localised fat, cellulite, scar and fibrosis concerns.",
    hero=PB + "pb serum 2.png", thumb=(PB + "pb serum 1.png", "45", (0.55, 0.5)),
    blocks=[
        ("cards", "3 Targeted Formulations", [
            {"name": "PB SERUM LOW", "bullets": ["Face Reshaping"], "image": (PB + "pb serum low.png", "45")},
            {"name": "PB SERUM MEDIUM", "bullets": ["Double Chin", "Localised Fat", "Cellulite"], "image": (PB + "pb serum medium.png", "45")},
            {"name": "PB SERUM HIGH", "bullets": ["Scars", "Post-Surgical Fibrosis", "Fibrotic Tissue"], "image": (PB + "PB SERUM HIGH.png", "45")},
        ], None),
        ("acc", [(HOW, "The appropriate PB Serum formulation is selected according to the treatment area, tissue condition and individual treatment goals."),
                 (COMFORT, "Mild swelling, tenderness or bruising may occur after treatment. Downtime varies depending on the area treated."),
                 (RESULTS, "Results develop progressively, and the number of sessions required depends on the treatment area and individual response.")], None),
    ], cta="Book a Consultation")

# ---------- Wellness
HD = "Hydrogen Drip/"
T["hydrogen-drip"] = dict(
    name="Hydrogen Drip", cat="wellness",
    lead="Recharge from within with a wellness infusion designed to support recovery, balance and overall vitality.",
    hero=HD + "hydrogen drip 2.jpg", thumb=(HD + "hydrogen drip 1.png", "45"),
    blocks=[
        ("about", "What Is Hydrogen Drip?", ["Hydrogen Drip is an intravenous wellness treatment designed to support overall wellbeing, recovery and oxidative balance as part of a personalised wellness programme."], None),
        ("acc", [(HOW, "The infusion is administered intravenously, allowing the selected formulation to enter the bloodstream directly as part of a doctor-guided wellness protocol.")], HD + "hydrogen drip 1.png"),
        ("benefits", "Benefits", ["Supports overall recovery", "Helps promote a sense of wellbeing", "Supports the body’s oxidative balance", "Complements a healthy lifestyle and wellness routine", "Suitable for ongoing wellness maintenance"], None),
        ("who", "Who Is It For?", [("Low Energy Days", None), ("Late Nights", None), ("Frequent Travel", None), ("Busy Schedules", None), ("Wellness Maintenance", None)]),
    ])

T["nmn-drip"] = dict(
    name="NMN Drip", cat="wellness",
    lead="NMN Drip is an intravenous wellness treatment designed to support cellular energy, vitality and healthy ageing as part of a personalised longevity programme.",
    hero="NMN Drip/NMN drip.png", thumb=("NMN Drip/NMN drip.png", "45"),
    blocks=[
        ("acc", [(HOW, "NMN is administered intravenously as part of a doctor-guided wellness protocol, allowing it to enter the bloodstream directly without relying on digestive absorption."),
                 ("What to Expect", "Some patients choose NMN Drip as part of a regular energy, recovery and longevity routine. Individual experience and response may vary.")], None),
        ("benefits", "5 Key Benefits", ["Supports cellular energy", "Promotes overall vitality", "Supports healthy ageing", "Helps support recovery during demanding periods", "Complements an ongoing longevity programme"], None),
        ("who", "Who Is It For?", [("Low Energy Days", None), ("Busy Schedules", None), ("Frequent Travel", None), ("Ageing Support", None), ("Longevity Maintenance", None)]),
    ])

GI = "ÉTERNA Glow Infusion Drip/ÉTERNA Glow Infusion Drip.png"
T["glow-infusion-drip"] = dict(
    name="ÉTERNA Glow Infusion Drip", cat="wellness",
    lead="ÉTERNA Glow Infusion is an intravenous wellness treatment designed to support skin radiance, hydration and overall wellness as part of a personalised beauty-from-within programme.",
    hero=GI, thumb=(GI, "45"),
    blocks=[
        ("acc", [(HOW, "The infusion delivers selected nutrients intravenously, allowing direct bloodstream delivery as part of a doctor-guided wellness protocol focused on radiance and skin support."),
                 ("What to Expect", "Some patients choose Glow Infusion as part of a regular beauty and wellness routine, especially when skin looks tired, dull or lacking radiance.")], None),
        ("benefits", "Benefits", ["Supports a brighter-looking complexion", "Promotes overall skin radiance", "Supports hydration and skin freshness", "Complements aesthetic and facial treatments", "Suitable for ongoing beauty maintenance"], None),
        ("who", "Who Is It For?", [("Dull-Looking Skin", None), ("Tired Complexion", None), ("Busy Schedules", None), ("Pre-Event Glow", None), ("Beauty Maintenance", None)]),
    ])

SS = "Signature Secretome/"
T["signature-secretome"] = dict(
    name="Signature Secretome", cat="wellness",
    lead="Secretome is a cell-free mixture of bioactive signals released by cells, including exosomes, growth factors, cytokines and proteins.",
    hero=SS + "secretome 4.jpg", thumb=(SS + "secretome 2.jpg", "45"),
    blocks=[
        ("about", "What Is Signature Secretome?", ["Rather than introducing living cells, secretome therapy uses these signalling molecules to support the body’s natural repair and regenerative processes."], SS + "secretome 3.png"),
        ("acc", [(HOW, "Secretome acts like a biological communication system, delivering signals that may help support tissue repair, regulate inflammation and encourage a healthier regenerative environment."),
                 ("Treatment Experience", "Treatment is provided in a private clinical setting after medical assessment and suitability review."),
                 ("What to Expect", "Signature Secretome is positioned as part of a broader regenerative wellness programme, with treatment planning based on individual goals and medical assessment.")],
         SS + "secretome 1.jpg"),
        ("figure", "5 Key Benefits", SS + "benefits for secretome.png", None),
        ("who", "Who Is It For?", [("Recovery Support", None), ("High-Demand Lifestyles", None), ("Healthy-Ageing Support", None), ("Regenerative Wellness", None), ("Long-Term Wellness Maintenance", None)]),
    ], cta="Book Signature Secretome")

XS = "Exosome/"
T["exosome-therapy"] = dict(
    name="Exosome Therapy", cat="wellness",
    lead="Cell-to-cell signalling support for recovery, vitality and regenerative wellness.",
    hero=XS + "exosome 4.jpg", thumb=(XS + "exosome 3.jpg", "45"),
    blocks=[
        ("about", "What Is Exosome Therapy?", ["Exosomes are microscopic signalling particles released by cells. They carry biological messages that support cell communication, tissue recovery and regenerative processes.",
                                               "At ÉTERNA, we offer Exosome Therapy as part of a personalised regenerative wellness programme following a medical assessment."], XS + "exosome 1.png"),
        ("acc", [(HOW, "Exosomes act as cell-to-cell messengers, carrying signalling molecules that may support the body’s natural repair environment and cellular communication. Treatment planning is personalised according to individual wellness goals and medical suitability."),
                 ("What to Expect", "Exosome Therapy is intended as part of a broader regenerative and longevity strategy, rather than a quick one-off wellness treatment. Individual response and recommended treatment frequency may vary.")],
         XS + "exosome 2.jpg"),
        ("benefits", "5 Key Benefits", ["Supports regenerative wellness", "Supports overall recovery", "Supports healthy cell communication", "Complements healthy-ageing goals", "Can be tailored according to individual wellness needs"], None),
        ("tiles", "Treatment Options", [("Exosome 50B", "A 50 billion exosome formulation positioned for general regenerative wellness, recovery and ongoing wellness support."),
                                        ("Supreme Exosome 500B", "Contains mesenchymal stem cell-derived extracellular vesicles, delivering 500 billion exosome particles in 100 mL of saline. A Certificate of Analysis (COA) will be provided for the treatment.")]),
        ("figure", "Who Is It For?", XS + "benefits exosome.png", None),
    ], cta="Book Exosome Therapy")

HR = "HerRestore Signature/"
T["herrestore-signature"] = dict(
    name="HerRestore Signature", cat="wellness",
    lead="HerRestore Signature is ÉTERNA’s non-surgical women’s core and pelvic wellness programme combining two complementary treatment components.",
    hero=HR + "herrestore 1.png", thumb=(HR + "pelvic core.png", "45", (0.42, 0.5)),
    blocks=[
        ("about", HOW, ["HerRestore Signature works on both the core muscles and pelvic floor muscles to provide a more complete approach to women’s functional strength and support."], None),
        ("tiles", None, [("CoreLift™", "CoreLift™ focuses on core strength, posture and stability."),
                         ("PelviLift™", "PelviLift™ focuses on pelvic floor strengthening, bladder support and feminine wellbeing.")]),
        ("figure", "Key Benefits", HR + "benefits herrestore.png", None),
        ("acc", [("Treatment Experience", "A non-surgical, comfortable treatment performed in a private clinical environment with no downtime."),
                 ("What to Expect", "Improvement is progressive over the treatment programme. The recommended number of sessions depends on individual assessment and goals.")],
         HR + "Paintech.png"),
        ("who", "Who Is It For?", [("Urinary Leakage", None), ("Frequent Night-Time Urination", None), ("Pelvic Floor Laxity", None), ("Menstrual Irregularities", None)]),
    ], cta="Book HerRestore Signature")

EM = "Emsella Chair/"
T["emsella"] = dict(
    name="EMSELLA", h1="EMSELLA®", cat="wellness", hero_mode="banner",
    lead="EMSELLA® is a non-invasive pelvic floor treatment designed to support intimate health and improve weakened pelvic floor function in both women and men.",
    hero=EM + "EMSELLA 1.png", thumb=(EM + "EMSELLA 1.png", "45", (0.6, 0.5)),
    blocks=[
        ("about", "What Is EMSELLA?", ["Using HIFEM® electromagnetic technology, treatment is performed comfortably while seated and fully clothed, making pelvic floor strengthening simple and convenient."], None),
        ("split", "Why Pelvic Floor Health Matters?", ["The pelvic floor supports the pelvic organs and plays an important role in bladder control, core stability, movement and intimate wellbeing. When these muscles become weakened, it may contribute to urinary leakage, reduced pelvic support and loss of confidence."], EM + "EMSELLA 2.png"),
        ("about", "How Does EMSELLA Work?", ["EMSELLA uses electromagnetic energy to stimulate thousands of powerful pelvic floor muscle contractions during a single session. This stimulation re-educates and strengthens weakened muscles, restores neuromuscular control, improves intimate wellbeing, and helps reduce urinary incontinence."], None),
        ("figure", "EMSELLA Benefits", EM + "EMSELLA BENEFITS.png", None),
        ("figure", "Result", EM + "Result EMSELLA.png", None),
    ], cta="Book EMSELLA")

# ---------------------------------------------------------------- home / about
HOME = {
    "hero_title": "Eternal Beauty,<br>Crafted for You.",
    "hero_text": "We believe beauty is not about changing who you are. It is about returning to your best self. From consultation to aftercare, every treatment at ÉTERNA is planned around one face: yours.",
    "made_title": "Beauty, Made Personal.",
    "made_text": "We help you return to your best state through bespoke treatment plans that combine medical expertise with a refined sense of beauty.",
    "made_cn": "美，不是改变自己，而是回到最好的状态。",
    "approach": [
        ("Consultation", "专业咨询", "Understand your concerns, goals and suitability.", ("HOME PAGE/consulation.png", "43")),
        ("Personalised Planning", "个性化方案", "Select treatments according to your individual condition and priorities.", ("HOME PAGE/Personalised Planning.png", "43")),
        ("Precise Treatment", "专业治疗", "Deliver care with attention to safety, comfort and natural-looking outcomes.", ("HOME PAGE/Precise Treatment.jpg", "43", (0.5, 0.42))),
        ("Ongoing Aftercare", "术后关怀", "Support recovery, maintenance and long-term treatment planning.", ("HOME PAGE/Ongoing Aftercare.jpg", "43", (0.5, 0.0))),
    ],
}

ABOUT = {
    "philosophy_title": "Beauty, Treated with Intention.",
    "philosophy": ["At ÉTERNA, we believe beauty is not about changing who you are, but helping you return to your best, most confident state.",
                   "From consultation to treatment and aftercare, we combine clinical precision, aesthetic judgement and personalised attention to create a bespoke beauty experience made just for you."],
    "philosophy_cn": "我们相信，真正的美不是改变自己，而是让你以更自然、更自信的状态呈现最好的自己。",
    "what_we_do": [
        ("Aesthetic Medicine", "医美美容", "Personalised treatments focused on skin quality, facial rejuvenation and natural-looking enhancement.", "以自然、精致为核心，改善肤质与面部年轻化。", "ABOUT US/Aesthetic Medicine.png"),
        ("Regenerative & Longevity Care", "再生医学与长寿管理", "Doctor-guided therapies designed to support recovery, vitality, healthy ageing and long-term wellness.", "从恢复活力到健康老化，打造长期健康管理。", "ABOUT US/Regenerative & Longevity Care.png"),
        ("Personalised Wellness", "个性化健康管理", "Integrated wellness solutions tailored according to individual lifestyle, health goals and clinical assessment.", "结合个人生活方式与健康目标，制定专属健康方案。", "ABOUT US/Personalised Wellness.png"),
    ],
    "vision": "To be a trusted leader in aesthetic, longevity and regenerative care, delivering safe, effective treatments with an exceptional client experience.",
    "vision_cn": "成为值得信赖的医美、长寿与再生医学品牌，以安全、有效的治疗与卓越体验，陪伴每个人实现健康与美丽。",
    "mission": [
        ("Clinical Excellence", "卓越的医疗品质", "Deliver high-quality aesthetic, wellness and regenerative treatments with consistent standards of care."),
        ("Safety & Comfort", "安全与舒适", "Prioritise client safety, comfort and satisfaction throughout every stage of the treatment journey."),
        ("Ethical Practice", "专业与诚信", "Uphold the highest standards of ethics, professionalism and responsible clinical practice."),
    ],
    "why": [
        ("Personalised Treatment Planning", "个性化治疗方案", "No one-size-fits-all protocols. Treatments are selected around your individual needs."),
        ("Doctor-Guided Care", "医生主导治疗", "Clinical assessment and treatment planning according to suitability."),
        ("Advanced Technology", "先进的医疗科技", "Selected technologies chosen for safety, treatment relevance and clinical application."),
        ("Refined Client Experience", "高品质客户体验", "From consultation to aftercare, every detail is designed around comfort and trust."),
    ],
    "cta_title": "Your Journey, Thoughtfully Designed.",
    "cta_text": "Discover personalised aesthetic, regenerative and wellness care at ÉTERNA.",
}
