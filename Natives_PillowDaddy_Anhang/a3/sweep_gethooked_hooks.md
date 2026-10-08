# Agent 3 – Sweep "Hook-/Story-Suchbegriffe" (GetHooked) – Native-Vorbilder Schlaf / Bettwaren / Haushalt / Allergie / Wechseljahre / Hygiene

Stand: 08.10.2026, ca. 10:41–11:10 UTC. Quelle: GetHooked `search_ads` (Hook-/Story-Begriffe, z. T. mit `page_type=advertorial,listicle`, `sort_column=days_active` strikt), Brand-Abfragen per `brand_id`, Landingpages per curl (mobile UA) geprüft, Transkripte per `transcribe_ads`.
PillowDaddy und seine Persona-Seiten sind bewusst ausgeschlossen (Agent 1).
Rohdaten/Volltexte: `a3/_notes_hooks_raw.md` (alle Treffer je Suche), `a3/transcripts/batch1_dedup.md` (Transkripte), `a3/lp_hooks/*.html` (LP-Snapshots).

Erfolgs-Kriterien für die Einstufung: Laufzeit ≥ 30 Tage, mehrere aktive Varianten/Persona-Seiten, Spend-Bucket (wo vorhanden), Anzahl aktiver Ads der Marke. Spend-Range ist bei den meisten US/UK-Ads in GetHooked leer (null) – das ist keine Aussage über niedrigen Spend.

---

## 1. Kurzfazit (für Agent 4)

1. **Die stärksten, direkt übertragbaren Vorbilder** sind Bettwaren- bzw. Schlafzimmer-Hygiene-Marken, die (a) ein unsichtbares Problem im Bett "aufdecken" (Milben/Schweiß/Hautschuppen) oder (b) Nachtschweiß in den Wechseljahren lösen – und das über **Persona-/Creator-Seiten + Advertorial/Listicle** tun:
   - **Plufl/Hugl** (Kühl-Körperkissen, US): 4 Creator-Seiten, Ads 207–309 Tage aktiv, LP = Magazin-Advertorial "How 40,000+ Hot Sleepers…", inkl. Ad **"Want Mom to Sleep Better? 👩 💤"** (Angle B + D in einem).
   - **UVlizer/Clairu** (Ionisator gegen Milben, **UK**): 3 Persona-Seiten ("Families vs. Dust Mites" …), Ads 187–424 Tage aktiv, Listicle + 2 Advertorials; Hook "If you sneeze within the first 10 minutes of waking up every single morning, your pillow is the problem."
   - **GroundingWell** (Erdungs-**Bettlaken**, US/UK/EU): 4+ Persona-Seiten, Ads 108–226 Tage, Arzt-Advertorial, Wechseljahre-Advertorial, Listicle "10 Reasons Why Women Over 50…".
   - **The Natural Household / TrueClean** (CaptureCards gegen Milben in der Matratze, US): 268 Ads, Matratzen-Hygiene-Ads 70–106 Tage, 6+ Listicle/Advertorial-Varianten, neue Native-Text-Bild-Tests ("My house is spotless. This came out of my mattress anyway…").
   - **Ryer** (DE, Nasssauger, Milben in Matratze): 4 Persona-Seiten, Advertorials auf neutraler Vergleichsdomain provergleich.com; "Hör auf, in deinem eigenen Dreck zu schlafen. Milben, Schweiß, Hautschuppen…".
2. **Wiederkehrendes Story-Muster "Tochter bringt Mutter die Lösung"** in 4 unabhängigen Marken (UVlizer, SP Nutrition, GroundingWell, Calmhaven) – plus "Daughter sent me this" (Kolnar-Staubsauger) und "Want Mom to Sleep Better?" (Plufl). Direkt nutzbar für Angle D.
3. **Der Decke-/Bettdecken-Markt selbst nutzt praktisch keine Natives**: Suche "duvet" (US/UK) und "Bettdecke" (DE) liefert fast nur Homepage/PDP/DPA (Bedfolk, Linenbundle, Soak and Sleep, MagicSplashy, Ynot, Zelesta, Pleene). Einzige Story-Elemente dort: UGC-Ich-Storys zum Beziehen (Zelesta DE, Doze US). → Bestätigt die Chance.
4. **Direkte Wettbewerber "Decke ohne Bezug"** gefunden (ohne Natives): Pleene (pleene.com/pleene.uk, "No stuffing. No tying. No adjusting a separate cover."), MagicSplashy EasySleep (DE), Ynot-dreambig (DE, "bettdecke-ohne-bezug"). Siehe Abschnitt 5.

---

## 2. Kandidaten-Übersicht (Rang nach Score = Stärke als Vorbild für UNSERE Angles)

| # | Marke | GetHooked brand_id(s) | Domain | Kategorie | Markt | Native-Formate | Längste Laufzeit (im Fenster) | Score |
|---|---|---|---|---|---|---|---|---|
| 1 | Plufl / Hugl | 116814 (Plufl), 28432 Perfectly Kelsey, 508882 Noah S., 344266 Gen X Jess, 351627 Hannah Houg | weareplufl.com | schlaf_bettwaren | US | Creator-UGC-Ich-Story, Kommentar-Antwort, Magazin-Advertorial | 309 d (aktiv) | 10 |
| 2 | UVlizer / Clairu | 197491 Families vs. Dust Mites, 70309 DetoxSpa UK, 126532 By Clairu | getuvlizer.co.uk → tryclairo.co.uk | hygiene (Milben/Allergie) | **UK** | Ich-Story (Video + Bild), Listicle, 2 Advertorials (Grandma/Mom), "Read if…"-Bild | 424 d (aktiv) | 10 |
| 3 | GroundingWell | 697, 306559 Amber Hayes, 2741196 Charlotte Miller, 689 Wellness Today, 7011057 Cynthia Roberts | groundingwell.com / journal.groundingwell.com | schlaf_bettwaren (Bettlaken) + Wechseljahre | US/UK/EU | Arzt-Advertorial, Ich-Story-Advertorial, Wechseljahre-Advertorial, Listicle, Animations-Story | 226 d | 9 |
| 4 | The Natural Household / TrueClean (CaptureCards) | 7566011, 7635423 True Clean Home | truecleanhome.com / thenaturalhousehold.co | hygiene (Milben Matratze) | US | Listicle, Ich-Story-Advertorial, Native-Text-Bild ("Read more"), Problem-Benennung ("Mattress Face") | 106 d (aktiv) | 9 |
| 5 | Ryer | 5345283, 7199495 Anika Schmidt, 7199496 Reinigungstipps für Zuhause, 7526090 Daniel Weber, 7526091 Auto Hacks & Pflege | ryer.de / provergleich.com | haushalt_home (Milben/Matratze) | **DE** | Ich-Story-Video, Advertorial auf Vergleichsdomain, Charakter-Ad (sprechende Milben), "Sorry an alle…" | 124 d (aktiv) | 9 |
| 6 | Down To Ground | 36329, 7049265 Frazer | downtoground.co | schlaf_bettwaren (Matratzenauflage) | US/UK | Listicle, Gründer-Story, Advertorial | 187 d (aktiv) | 8 |
| 7 | Cosy House Collection | 5995 | cosyhousecollection.com (+ .co.uk) | schlaf_bettwaren (Bettwäsche) | US | Listicle (2 Varianten), Ich-Story-Video ("I was a housekeeper") | 115 d (aktiv) | 8 |
| 8 | Aeyla | 4518428 Susan Collins – The Neck & Shoulder Pain Community | aeyla.co.uk | schlaf_bettwaren (Kissen) | **UK** | Community-Persona, Ich-Story-Bild (61-Jährige, Hygiene), Listicle, Ärztin-Video | 98 d (aktiv) | 8 |
| 9 | Kaori | 4486124 Grandma's Care Journal, 4451068 Grandma's Glow | try-kaori.com | hygiene (Körpergeruch 50+) | US | Ich-Story (Oma/Enkel), Listicle "7 Reasons…" | 203 d (aktiv) | 8 |
| 10 | Mellow Sleep | 4398848, 1329122, 3873187, 4398854, 7071687 Mellow Pillowcases | mellowsleep.com | schlaf_bettwaren (Kissen) | US | Advertorial (Chiropraktiker-Ich-Story), Listicles, Multi-Page | 41 d (aktiv) | 7 |
| 11 | SP Nutrition | 4755341 Deborah Rustad, 1798132 Wellness Tips, 1897875 Welcome to 3 AM Wake Up Club, 4311878 Alice Williams | spnutrition-us.com | wechseljahre | US/UK | Gynäkologen-Advertorial, Ich-Story mit Tochter, Arzt-bewertet-Video | 186 d | 7 |
| 12 | Earthbound Co. | 15669 | tryearthbound.com / thelongevitybrief.com | schlaf_bettwaren | US | UGC-Review → Advertorial auf Fake-Magazin "The Longevity Brief" | 366 d (aktiv) | 7 |
| 13 | Home & Garden Trend (OrthoBed / Matratzensauger) | 2090 | garden-trend.store / homegardentrend.com | haushalt_home / schlaf | US | Listicle-Advertorial "5 Ways Your Old Mattress…", Ekel-UGC | 128 d (aktiv) | 7 |
| 14 | Clarifion | 3202, 44651 Homeowners vs. Dust Mites, 3204 The Home Guru | clarifion.com / about.clarifion.com | allergie / haushalt | US | Magazin-Advertorial, Native-Text-Bild "(MUST READ)" | 50 d (im Fenster) | 7 |
| 15 | twentythree.de | 5346201 | twentythree.de | schlaf_bettwaren (Bettwäsche) | **DE** | Listicle "8 Gründe…" | 130 d (aktiv) | 7 |
| 16 | Pridola | 15934 | pridola.co.uk | schlaf_bettwaren (Musselin-Decke) | **UK** | Story-Hooks (Frauen 50+, "undercover"), Charakter-Animation – LP aber PDP | 41 d (aktiv) | 6 |
| 17 | Blissy | 7085041 Blissy Pillow (389 Blissy) | blissy.com | schlaf_bettwaren | US | "Is Your Pillow Making You Sick?" → Listicle/Salespage | 54 d | 6 |
| 18 | TRAVLR | 4088306, 4088304 Brenda Burke | shoptravlr.com | sonstiges (Reisekissen) | US | Ich-Story Oma/Tochter, Experten-Exposé-Advertorial | 268 d (aktiv) | 6 |
| 19 | Zelesta.de | 5189960 | zelesta.de | schlaf_bettwaren (Bettdecke) | **DE** | UGC-Ich-Story "Bett beziehen" (Homepage) | 129 d (aktiv), Spend $2.001–5.000 | 6 |
| 20 | NYVEN / Kolnar | 7449265 | kolnarhome.com / nyvenshop.com | haushalt_home | US | "My Daughter Sent Me This…" Ich-Story 58-Jährige (PDP) | 45 d (aktiv) | 6 |
| 21 | Top 5 Best Mattresses UK (Emma) | 504951 | top5bestmattress.co.uk | schlaf_bettwaren | **UK** | Vergleichs-Listicle-Seite | 149 d | 6 |
| 22 | Vitalisys | 1591367 Emma McCarthy | vitalisys.co | wechseljahre | **UK** | Ich-Story-Advertorial | 97 d | 6 |
| 23 | Doze Bedding | 7224019 | dozebedding.com | schlaf_bettwaren (Bettbezug) | US | UGC-Ich-Story "household battles" (Homepage) | 225 d (aktiv) | 5 |
| 24 | Rest (Evercool Comforter) | 28140 | rest.com | schlaf_bettwaren (Bettdecke) | US | UGC-Story Wechseljahre (PDP) | 278 d (bis 14.04.) | 5 |
| 25 | Unikor NightGuard | 59081 | unikor.shop | hygiene (Bettnässen) | US/UK | Listicle, Ich-Story | 187 d (aktiv) | 5 |
| 26 | Lovy (UroControl) | 4444041 Unstoppable After 50 | trylovy.com | hygiene (Inkontinenz 50+) | US | Experten-Beichte-Advertorial | 80 d | 5 |
| 27 | Pestlab Co | 41923 | pestlab.co | haushalt_home (Bettwanzen) | US | Charakter-Ad (Bettwanze spricht), Advertorial | 22 d im Fenster (ältere 207–216 d vor Fenster) | 5 |
| 28 | wellbe ("Wechseljahre und Ich") | 4411451 | myhealth-lifestyle.com | wechseljahre | DE | Listicle auf Magazin-Domain | 225 d, Spend $2.001–5.000 | 5 |
| 29 | Vision Beam (Schlaf-Earbuds) | 42070 | vionb.com | schlaf | US/UK | Listicle/Advertorial | 218 d (aktiv) | 5 |
| 30 | PurePath | 536540 | purepathshop.co | haushalt_home | US/UK | Fake-Tweet-Bild, "professional house cleaner"-Story, Listicle | 39 d | 5 |

---

## 3. Kandidaten im Detail (Belege: Ad-ID · share_url · Laufzeit · Status · LP · LP-Typ · Hook wörtlich)

### 3.1 Plufl / Hugl Self-Cooling Body Pillow – Score 10
- Domain weareplufl.com · Kategorie schlaf_bettwaren · Markt US · Plufl 160 aktive Ads; Creator-Seiten Perfectly Kelsey (8 aktiv), Noah S. (18), Gen X Jess (23), Hannah Houg (34).
- LP verifiziert: `weareplufl.com/pages/hugl-sleep-system-advertorial` = **Advertorial im Magazin-Stil** (Datum, "Reading Time: 3 min"), Headline "How 40,000+ Hot Sleepers Are Finally Sleeping Through the Night — No Medications, No Pillow Flipping, Just NASA-Inspired Cooling", Sub "A NASA-developed cooling technology is helping women sleep through the night, restoring energy and wellness without hormone therapy or sleep aids.", Einstieg "For women over 45, sleepless nights can feel like an inevitable part of aging." Weitere LPs: `/pages/hugl-advertorial-page`, `/pages/hugl-cooling-support`.
- Belege:
  1. 121399208 · https://app.gethookd.ai/share/ad/121399208?signature=a7525a95abd29dcb4a1de055c7ca72296aaa71af4bd20a5eb1f544e781a7eff9 · 309 d · aktiv · Advertorial · Hook (Transkript): "Watch me cut my sleep expenses in half. Yeah, that's a huggle. It's a cooling body pillow that has literally saved me money." (weiter: "I stopped waking up in pools of my own sweat … instead of buying a new mattress, I got a $180 huggle")
  2. 122685364 · https://app.gethookd.ai/share/ad/122685364?signature=9094b1343988fe1dff3a1468928c7f64672a193a52751b956916f003d9c222cc · 309 d · aktiv · Advertorial · Titel "Want Mom to Sleep Better? 👩 💤" · Text "If your mom sleeps on her side you NEED to get her this! <3" (Schwester-Ad 122685383 gleiche Laufzeit, Transkript "Not hype, here's exactly how it works…", Overlay "Reply to james's comment: Will this actually help my back pain or is it just hype?")
  3. 121930625 · https://app.gethookd.ai/share/ad/121930625?signature=a9d341607b4629b5bbabf28419bd469a33e9d0f489ec0b656298a0705f2d22cf · 274 d · aktiv · Advertorial · "This body pillow is the best mom purchase I've made in a long time." (Transkript-Ende: "If you're a tired mom who's still waking up exhausted, Huggle has been the one upgrade that's actually helped.")
  4. 108743598 · https://app.gethookd.ai/share/ad/108743598?signature=ed127f44ecd7dcf40f95c377dcb3b3bfc8837f24116e4235d7ccb60be8d91ebd · 242 d · aktiv · Advertorial · "Tired of waking up drenched? 🌡️ 😫 Say goodbye to night sweats with the Hugl Self-Cooling Body Pillow trusted by 21,346+ hot…"
  5. 81163839 · https://app.gethookd.ai/share/ad/81163839?signature=9564460c0c9fb5c78003c8b1d69c472e44f36af03e219894516a934b9fab41fe · 226 d · aktiv · Advertorial · Titel "Say Goodbye to Night Sweats 👋💧" (Markenseite, Bild)
- Begründung: Bettwaren-Produkt, Nachtschweiß/Frauen 45+ (Angle B), "für Mama kaufen" (Angle D), Creator-Persona-System + Magazin-Advertorial, extrem lange Laufzeiten mit vielen Seiten. Vorlage für unser B- und D-Native.

### 3.2 UVlizer / Clairu (Ionisator gegen Milbenkot) – Score 10 – UK
- Domain getuvlizer.co.uk (leitet heute auf tryclairo.co.uk, Produkt "Clairu") · Kategorie hygiene/allergie · Markt GB · Persona-Seiten: "Families vs. Dust Mites" (22 aktiv), "DetoxSpa UK" (183 aktiv), "By Clairu" (27 aktiv).
- LPs verifiziert: `/pages/dust-mites` = **Listicle** "🏠 10 Reasons Why Thousands Are Switching to Clairu to Eliminate Dust & Dust Mites at Home" (By Jessica M.); `/pages/adv-dust-mites` = **Advertorial** "How This Grandma Effortlessly Cleared Dust Mites from Her Home in Just 30 Minutes" ("I tested Clairu myself, and here's what I found:" / "MY FINAL THOUGHTS"); `/pages/dust-mite-invasion` = **Advertorial** "How This Mom Saved Her Family From A Mysterious Dust Mite Invasion With a Quick Trick" (Testerin "SHARON ARCHER", WEEK 1/2/3).
- Belege:
  1. 35831986 · https://app.gethookd.ai/share/ad/35831986?signature=de97fb0901ee6b6f257263d7ca29f4b3001bed8512db1c71ef0bc894abaefdd5 · 424 d · aktiv · Listicle · "If you live in a dusty house, and no matter how much you clean, you still wake up sick, watch this." (Transkript: "…the problem was never just the dust, it's what's in the dust. Microscopic poop particles from dust mites. Tiny creatures that live in your bedding, your pillow, and your furniture.")
  2. 89834921 · https://app.gethookd.ai/share/ad/89834921?signature=cbc7273ea2192cf8807a41cd6c8a4525c69bdd3704e6f16f118abdbeb57a5270 · 187 d · aktiv · Listicle · "If you sneeze within the first 10 minutes of waking up every single morning, your pillow is the problem." (Transkript: "Here's what nobody told me. Dust mites, the ones living in your pillow right now … A brand new pillow has them within weeks." … "I was skeptical." … "60 days, money back if it doesn't work.")
  3. 77601762 · https://app.gethookd.ai/share/ad/77601762?signature=7e3eb6b58db706cf098c8d1731f1d4e1d2435f06efa79717b2efce0e6e4b5618 · 218 d · inaktiv (bis 11.09.) · Listicle · Titel "Read if you wake up coughing in the middle of the night 👆" · Text "My husband moved to the guest room on a Wednesday night. After I woke him up coughing for the fourth time that week."
  4. 77369446 · https://app.gethookd.ai/share/ad/77369446?signature=c6a8c6df387f389f6cc555b32e26e3f33308169d27af094b07b4af5eb4be8cf6 · 246 d · aktiv · Advertorial (adv-dust-mites) · Titel "Eliminates Dust Mites In Your Home?" · "Do You Have Dust Mites in Your House? Try This Simple Solution."
  5. 77884660 · https://app.gethookd.ai/share/ad/77884660?signature=ddcf0c0923c1a7d5a8e0fcc3e3a736d555afbba0366478240e5a921ee84e3abd · 243 d · aktiv · Listicle · "🏠 8 out of 10 of homes have dust mite poop floating in the air, most people never realize *until they get sick*"
- Zusatz (Transkript, Ad vor Fenster beendet): 27829534 Grandma-Story "Then my daughter came over one day, saw how congested I was, and said, Mom, why haven't you tried Kleru yet?"
- Begründung: UK-Markt, Bett/Kissen als Problemort (Angle A), Persona-Seiten + Listicle + 2 Advertorials, Laufzeiten bis 424 Tage. Bestes UK-Vorbild für Angle A.

### 3.3 GroundingWell (Erdungs-Bettlaken) – Score 9
- Domains groundingwell.com, journal.groundingwell.com, article.groundingwell.com · Kategorie schlaf_bettwaren (+ Wechseljahre) · Markt US, GB, EU · GroundingWell 701 aktiv; Personas Amber Hayes (34), Charlotte Miller (41), Wellness Today (160), Cynthia Roberts (57).
- LPs verifiziert: `journal.groundingwell.com/pages/bed-sheet` = **Advertorial** (Label "ADVERTORIAL"), Headline "This “Weird” Sheet Finally Fixed My 3-Year Sleep Problem", "by Emma Richardson", Einstieg "I'll never forget waking up in my car at 4 PM to 17 missed calls from my boss."; `/pages/menopause-advertorial` = **Advertorial** "Sleepless, Sweaty Nights? Menopausal Women Say This Bedsheet Finally Let Them Sleep Again"; `groundingwell.com/pages/special-sheet-listicle` = **Listicle** "10 Reasons Why Women Over 50 Are Switching to this "Special Sheet" to Wake Up Refreshed And Pain-Free in 2026".
- Belege:
  1. 75250601 · https://app.gethookd.ai/share/ad/75250601?signature=6073c8a1db81dd0fcab4101b2f3db56fe0638d3050be7f26ce3b6a8b73684eeb · 226 d · inaktiv (bis 08.09.) · Advertorial (bed-sheet) · "Don't waste your money on grounding sheets until you see what it did for my 94-year-old patient. Look, I'm a doctor with thr[ee]…"
  2. 102834602 · https://app.gethookd.ai/share/ad/102834602?signature=9c8b44383ab0135a4a6de55c19f68e2f22d1b7857055c639215d87c4e7c13afd · 108 d · inaktiv · Listicle · Animations-Story (Transkript): "this is grace she's 49 she slept eight hours last night and woke up more tired than before … her daughter says at dinner mom it's nice to see you smile again"
  3. 89809570 · https://app.gethookd.ai/share/ad/89809570?signature=a594daabb56da2a6e21f0132ef0d21f1489618e1ca4e90dcb7b80db526cd31a2 · 157 d · inaktiv · Listicle · "If you're thinking about buying a Grounding Well bed sheet, stop. There's something that I should have told you but I didn't and it's kind of a big deal."
  4. 83898286 · https://app.gethookd.ai/share/ad/83898286?signature=7ca3be9f80207f1dd52cc1a47728ca42c5c54451be4a5ebf8688c3e8d8171369 · 41 d · inaktiv (bis 14.04.) · Advertorial (menopause) · Titel "Menopause Stole My Sleep. This Helped." · "I debated posting this but honestly I wish someone had told me sooner."
  5. 87656553 · https://app.gethookd.ai/share/ad/87656553?signature=7ae0906deea9a327531c5cfddc0f0ff1f80a7e85072925530d6beac481311f94 · 128 d · inaktiv · Listicle · "If you're a woman over 50 who's tired of waking up exhausted, stiff, and in pain - read this b[efore]…"
- Begründung: Bettlaken = Bettwaren; deckt Arzt-Format, Ich-Story, Wechseljahre, Frauen 50+ und Tochter-Moment ab. Klares Vorbild für B und für Experten-Advertorial.

### 3.4 The Natural Household / TrueClean – CaptureCards – Score 9
- Domains truecleanhome.com, thenaturalhousehold.co (Vergleichsseite cleaningmadesimple.us) · Kategorie hygiene · Markt US · 268 Ads im Index (+ 2. Seite "True Clean Home", 84 aktiv).
- LPs verifiziert: `/pages/household-report` = **Ich-Story-Advertorial** "Why You Can Sleep 8 Hours and Still Wake Up Like the Night Never Counted" (H2 "The Spot Your Face Presses Into for 7,000 Breaths a Night", "Introducing the Card That Goes Where Laundry Cannot"); `/pages/mites-capturecards` = Advertorial-Listicle-Hybrid "Why You Wake Up Stuffy, Even After Washing Your Sheets" / "You Don't Have an Allergy Problem. You Have a Mattress Problem." / "6 Reasons People Are Switching to CaptureCards".
- Belege:
  1. 127732600 · https://app.gethookd.ai/share/ad/127732600?signature=afa84150b7971449d34bc3e756184af0f9c28f93b8213a649bdc4b29039e2f33 · 106 d · aktiv · Listicle (capturecards-listicle-airpurifier) · Titel "Covers, Sprays, A $200 Purifier, Hot Washes — The First Thing That Actually Pulled Anything Out Of My Bed." · "I've spent more money trying to get dust mites out of my bed than I'd like to admit."
  2. 127732615 · https://app.gethookd.ai/share/ad/127732615?signature=1c2daa6dab3ece7f5a9388e7beaa035f7c50268cc5efef8230051ae4eb064011 · 105 d · aktiv · Advertorial-Listicle (mites-capturecards) · Titel "You Can't Wash A Mattress. You Can Empty It." · "You wash the sheets in hot water every week. The mattress just refills them."
  3. 127732656 · https://app.gethookd.ai/share/ad/127732656?signature=0452299123cea85a26ed11fb06930539f681630d86ed19e498d7d58327d30901 · 98 d · aktiv · Listicle (capturecards-listicle-sleep) · "You can't see them, but your mattress and pillow are home to millions of dust mites — and you breathe them in all night."
  4. 201100978 · https://app.gethookd.ai/share/ad/201100978?signature=601b94e5286fea7e8016796619291ed524d9ebf8676f95000dc0fe754bb34656 · 3 d · aktiv (Test) · Advertorial-Listicle · Native-Text-Bild: "My house is spotless. This came out of my mattress anyway. My niece, who studies insects, explained... Read more" (Schwester 201100987: "I iron my pillowcases. So when the allergist asked how often I dust, I nearly walked out... Read more")
  5. 201100958 · https://app.gethookd.ai/share/ad/201100958?signature=39c2e92c0f728b9f3ba21ae8ccf15c82d30050b2b779da3f7ac2e3a56b922a4e · 3 d · aktiv · Ich-Story-Advertorial (household-report) · "You'd choose your own bed 10/10 times…"
- Begründung: Exakt Angle A (Matratze/Kissen/Bettwäsche als Ekel-Ort, Waschen reicht nicht), Beweis-Ritual ("hold it up to your phone light"), viele LP-Varianten mit 70–106 Tagen. Gutes Vorbild für Hygiene-Listicle + Native-Text-Bild.

### 3.5 Ryer (DE) – Score 9
- Domains ryer.de, ryershop.de, Advertorials auf provergleich.com · Kategorie haushalt_home (Hygiene Matratze) · Markt DE/AT · Ryer 917 aktiv; Personas Anika Schmidt (179), Reinigungstipps für Zuhause (193), Daniel Weber (75), Auto Hacks & Pflege (57).
- LP verifiziert: `provergleich.com/adv13-b` = **Ich-Story-Advertorial** "Der schockierende Moment, als dieses günstige Gerät jahrealten Dreck aus meinem Sofa geholt hat", Sub "Was wirklich in deiner Couch, Matratze und im Teppich steckt – und warum dein Staubsauger nichts davon mitbekommt. Spoiler: Ich hab geweint…", Abschnitt "Was ich gelernt habe: Polster sind Schwämme. Und sie speichern alles.", Angebot "56% Rabatt + 30€ Gratis Gutschein".
- Belege:
  1. 111737379 · https://app.gethookd.ai/share/ad/111737379?signature=4d616e456c750e2c496f4e36fc21ac8884d77c1ac0729da6b9febd18f237de15 · 124 d · aktiv · PDP · Titel "Milben fressen dich jede Nacht – ekelhaft!" · "Wir sind Millionen Milben. Und dein Bett ist unser Zuhause! Wir fressen deine Hautschuppen – jede Nacht."
  2. 145503635 · https://app.gethookd.ai/share/ad/145503635?signature=cba4b57aea9d8b9c26f49594d9a0f6313b7d280099feecaa5b1a8ef7dca5e436 · 55 d · aktiv · 9 Varianten · Advertorial (adv13-b) · "Ich schlafe seit Jahren schlecht, bis das bei mir angekommen ist." (Transkript: "Was da rauskam, war krass. Braune Brühe, Milben, Hautschuppen, jahrelanger Schweiß." … "Ich habe jede Nacht meinen eigenen Dreck eingeatmet.")
  3. 151964563 · https://app.gethookd.ai/share/ad/151964563?signature=eead42585b6cb10d2ad46f6a2c2558ab9a8ede084fb0e10d6880c2cc8c5b5964 · 49 d · aktiv · Advertorial (adv13-b) · Titel "In deinem eigenen Dreck schlafen" · "Hör auf, in deinem eigenen Dreck zu schlafen. Milben, Schweiß, Hautschuppen – genau das sammelt sich in jeder Matratze, die …"
  4. 185267664 · https://app.gethookd.ai/share/ad/185267664?signature=9f4825b629ec1f37f6e81ed51f8b89eb86825ae97383d7aa766d85195d1bfb5a · 12 d · aktiv · 8 Varianten · PDP/Advertorial · "Sorry an alle, die den RYER vor dem Herbst-Sale gekauft haben."
- Begründung: Unsere Angle-A-Worte (Milben, Schweiß, Hautschuppen) 1:1 im Einsatz, Persona-Netz + neutrale Vergleichsdomain. Bestes DE-Vorbild.

### 3.6 Down To Ground (Erdungs-Matratzenauflage) – Score 8
- Domain downtoground.co · Kategorie schlaf_bettwaren · Markt US + GB · 1113 aktive Ads; 345 Ads mit Advertorial/Listicle-LP; Gründer-Persona "Frazer" (161 aktiv).
- LP verifiziert: `/pages/article-listicle` = **Listicle** "8 Reasons Why Everyone Is Replacing Their Old Bedding with This Grounding Mattress Cover"; zusätzlich Advertorial `/pages/article-a00-gen-v3-mc`.
- Belege:
  1. 89820013 · https://app.gethookd.ai/share/ad/89820013?signature=69fd14f697cdf6cbe147774e88a6aedd0dcf6660dbaf5ed2634a7e6f8bf602c9 · 187 d · aktiv · Listicle · "Better health with Nature's electrons. Try grounding today 👇"
  2. 133588846 · https://app.gethookd.ai/share/ad/133588846?signature=729c3b4e8b89df28d427972549fa70e77844e9e007be318edb03e8bf96e2b328 · 74 d · aktiv · Listicle · "Hot nights, restless sleep, and feeling out of balance? During menopause, many women look for simple ways to support their we[ll-being]…"
  3. 169458382 · https://app.gethookd.ai/share/ad/169458382?signature=494aacfa3cc49cf887f0e6f5926cb7fe3ff27d6cc24010e8248fa43a43bb4a7b · 46 d · aktiv · Listicle · Titel "why I quit cycling for my mum" · "People ask me why I quit professional cycling to make mattress covers. The honest answer is my mum."
  4. 124903647 · https://app.gethookd.ai/share/ad/124903647?signature=81bb58a967f0181cebd34f76a72667fb6b9f14faca207a0687d87c41fbfbdc7c · 86 d · aktiv · Listicle · "Yes, our mattress cover is expensive. Here's why that's a good thing. My name's Fraser. I'm the founder of Down to Ground."
  5. 132146301 · https://app.gethookd.ai/share/ad/132146301?signature=bcb7de87b41b0e8e6e20c62bbf6a73f5b385775f1093f02ee563d4c21b037703 · 75 d · aktiv · GB · Listicle · "You went to bed on time…so why do you still feel off?"
- Begründung: Bettwaren-Listicle mit enormem Volumen, Gründer-Story mit Mutter-Motiv (Angle D-nah), läuft auch in GB.

### 3.7 Cosy House Collection (Bambus-Bettwäsche) – Score 8
- Domain cosyhousecollection.com (+ cosyhousecollection.co.uk) · Kategorie schlaf_bettwaren · Markt US (im Index) · 117 aktiv.
- LPs verifiziert: `try.cosyhousecollection.com/7-reasons-you-need-to-upgrade-to-100-bamboo-bed-sheets-cooling` = **Listicle** "Still Waking Up Hot at 3 A.M.? Your Cotton Sheets Could Be Why." (1. It's Not the Heat. It's the Sheets. … 7. 90-Night Risk-Free Trial); `…-sleep` = **Listicle** "You Spend 25 Years of Your Life in Bed. Why Skimp Out On Your Bedding?"
- Belege:
  1. 107610652 · https://app.gethookd.ai/share/ad/107610652?signature=6640df54d74502335a81fa1c3fa74900d36d23717cf0e4f4672e4264e052e96f · 115 d · aktiv · Listicle · "The answer to night sweats & hot flashes is here!"
  2. 107610671 · https://app.gethookd.ai/share/ad/107610671?signature=9712a950d62212e292716703aeaae7a5e8eb70e86d5d9150e29adecf0564df9a · 115 d · aktiv · Listicle · "You'll spend 25 years of your life in bed. Why are you skimping on the sheets?" (Video-Overlay "I was a housekeeper")
  3. 111090841 · https://app.gethookd.ai/share/ad/111090841?signature=5c369f8bb74c2c778b1491df5acc8bf266f5231b88a818d85a725173b5df0e4c · 108 d · aktiv · Listicle · "Wake up drenched? Your sheets are the problem. 🥵"
  4. 107610669 · https://app.gethookd.ai/share/ad/107610669?signature=4be694a255d6af29296a604186d5ecf562c01d1edcb08f9f0dfa21e517f38d24 · 115 d · aktiv · PDP · "The answer to Bad-skin, Night sweats & Dirty bedding is here!"
  5. 115193823 · https://app.gethookd.ai/share/ad/115193823?signature=336f0163e33ba70982b0b25ad02d7afbb0ba19fc010520fb80e3d96d4d1522c9 · 81 d · inaktiv · PDP · Transkript: "This is why your sheets are making you sweat all night. For years I thought waking up sweaty was just how I slept. Then I changed my sheets…"
- Begründung: Bettwäsche + Nachtschweiß + "Dirty bedding" = A und B, kurze Listicles (~600 Wörter) als leicht kopierbare Vorlage.

### 3.8 Aeyla (UK-Kissen) – Score 8 – UK
- Domain aeyla.co.uk · Kategorie schlaf_bettwaren · Markt GB · Persona-Seite "Susan Collins - The Neck & Shoulder Pain Community" (19 aktiv, 24 Ads im Index).
- LP: meist `aeyla.co.uk/products/the-dual-pillow` (PDP); Listicle `/pages/best-hotel-pillows-uk-2026` heute 404.
- Belege:
  1. 97025036 · https://app.gethookd.ai/share/ad/97025036?signature=de5b8f729a3ac81a3bb0f6b01c7c03536fffda676fb2e9082733e8e350ebdb6f · 33 d · inaktiv · PDP · Titel "I can’t believe I was sleeping on that" · "That pillow in the photo is mine. I had been sleeping on it for three years. I am 61 years old. I have kept a clean house m[y whole life]…"
  2. 97025542 · https://app.gethookd.ai/share/ad/97025542?signature=29f4623e73efb05caf48f8c4e9925f2af609c223512e5a8d89a4a3d0d9c14b8a · 33 d · inaktiv · Listicle (404) · Titel "Read my story, so this doesn't happen to you." · "I went to the doctor because I couldn't turn my head. She asked me one question I wasn't expecting."
  3. 117258077 · https://app.gethookd.ai/share/ad/117258077?signature=f7f787c496f3b8cd7779f20cad99249cd268ed1a35d8621af62459c11ef1af07 · 98 d · aktiv · PDP · Titel "☁️ The Pillow Taking Over UK" · "Your pillow is doing half the job."
  4. 160591716 · https://app.gethookd.ai/share/ad/160591716?signature=a76ca98d4262e556ccdeab57fdd565078e62ad2bde6c57d30c451c04c96145f7 · 44 d · aktiv (9 Varianten) · PDP · "You've tried everything. Switching to different mattresses. Buying pillow after pillow hoping this would be the one."
- Begründung: Einzige UK-Bettwarenmarke mit Community-Persona + Ich-Story einer 61-Jährigen zum Hygiene-Schock ("I can't believe I was sleeping on that") – fast wörtlich unser Angle A für UK-Frauen 55+. Abzug: Story-Ads liefen nur 33 Tage, aktuelle Langläufer gehen auf PDP.

### 3.9 Kaori (Körpergeruch 50+) – Score 8
- Domain try-kaori.com (+ try-lunera.com) · Kategorie hygiene · Markt US · Personas "Grandma's Care Journal" (24 aktiv), "Grandma's Glow" (113 aktiv).
- LP verifiziert: `/pages/7-reasons-why` = **Listicle** "7 Reasons Why Seniors Are Using This Japanese Secret To Be Close To Family Again" (By Jade M.; "3. Your Grandkids Will Actually Want to Hug You Again").
- Belege:
  1. 95842126 · https://app.gethookd.ai/share/ad/95842126?signature=f8f290640067d6ced02b3cdd16c040124c28c875b8837c28208a39f3be292282 · 203 d · aktiv · Listicle · Titel "The Japanese Secret to Staying Fresh After 50" · "My grandson was at my house every afternoon. He was everything to me. Then one day he was gone."
  2. 94387808 · https://app.gethookd.ai/share/ad/94387808?signature=eb787cb82e8a7a4ce6e5defb491245971015716566c9631e8cf3e998d3962334 · 189 d · aktiv · Listicle · "My husband told me I smell like a nursing home. No amount of showering fixed it, until a nurse finally told me why."
  3. 94387965 · https://app.gethookd.ai/share/ad/94387965?signature=af429cd2a04ccbc288a24e263bd049a2b786b0f02b891bcae3f519dfb148db2f · 184 d · aktiv · Listicle · gleiche Copy
- Begründung: Hygiene-Scham bei 50+ und Familien-Nähe (Enkel/Ehemann) als emotionaler Treiber – übertragbar auf "Mama, dein Bett riecht" (A + D). Keine Bettwaren, daher 8.

### 3.10 Mellow Sleep (Kissen) – Score 7
- Domain mellowsleep.com · schlaf_bettwaren · US · 5 Seiten: Mellow Cloud Align Pillow (690 aktiv), Mellow Cloud Pillow (899), Mellow Sleep Cloud Pillow (439), Mellow Sleep Co. (92), Mellow Pillowcases (97).
- LPs verifiziert: `/pages/wp-adv-2` = **Advertorial (Ich-Story)** "My Chiropractor Told Me to Stop Wasting Money on Pillows. Then She Showed Me This One."; `/pages/rp-001` → `/pages/gu-ad-1` Sales-/Listicle-Hybrid "Wake Up Without Shoulder Pain, Neck Pain or Stiffness".
- Belege:
  1. 172323615 · https://app.gethookd.ai/share/ad/172323615?signature=de33298a0424d5fc0a3fad046fe54aba115e0b3a8147fce31ea34092b2f64b3c · 38 d · aktiv · Advertorial · Titel "The Pillow That Helps You Show Up" · "You don’t need to sleep perfectly, you just need a pillow that meets you halfway."
  2. 168185448 · https://app.gethookd.ai/share/ad/168185448?signature=0b5bbc372d75dd497686b37c4f61c19d854a7548a61656f70df9e062ddfc1fd4 · 41 d · aktiv · Advertorial (adv-flex-whiplash) · "Stop buying new pillows."
  3. 172038823 · https://app.gethookd.ai/share/ad/172038823?signature=b6620ee9644bc90e9fdb04da20386a0c93611209d7dbc9368b09caafa6a4d47a · 35 d · aktiv · Listicle (solvi-list-1) · "Built for real people, not perfect sleepers."
  4. 176715736 · https://app.gethookd.ai/share/ad/176715736?signature=f46fc1c21f4227baa7a40e218ada934d1276f1ea61c49d755e19169a75c9153a · 31 d · aktiv · LP lst-cp-night-sweat-fix · Titel "Menopause Relief: The Cooling Pillowcase" · "Hot flashes shouldn't ruin your night."
- Begründung: Riesiges Multi-Page-Native-System in Bettwaren, aber Laufzeiten nur 30–41 Tage (rotiert stark) → 7.

### 3.11 SP Nutrition (Magnesium, Wechseljahre) – Score 7
- Domain spnutrition-us.com · wechseljahre · US/GB · Personas Deborah Rustad (1458 aktiv), Wellness Tips (959), Welcome to 3 AM Wake Up Club (4), Alice Williams (65).
- LP verifiziert: `/pages/advertorial-menopause-new` = **Experten-Advertorial** "Leading Gynecologist: The #1 Reason Menopause Feels This Brutal Has Nothing To Do With Your Hormones" (H2 u. a. "First — You Are Not Crazy. You Are Not Alone. And You Have Not Been Told The Truth." / "The Patient Who Finally Made Me Look Deeper" / "If You Are Already On HRT And Still Not Sleeping, This Is Why" / "Real Women. Real Words.").
- Belege:
  1. 101624013 · https://app.gethookd.ai/share/ad/101624013?signature=06fb2c84e91653471c74fe657a9747dcc8199b63b0c06d71d00e049baa3fe13a · 139 d · inaktiv (bis 06.10.) · Advertorial · Transkript: "When menopause hit, I don't feel like myself anymore. Soaked sheets every night. … My husband sleeps in the guest room. … Then my daughter sat me down and showed me an article from a gynecologist. She said, mom, please just read this. … Dry sheets, clear head … Read the article below. It is the same one my daughter showed me."
  2. 104320503 · https://app.gethookd.ai/share/ad/104320503?signature=60ee510227499d81456d8e3b206b9b880290ff1c5c9aa8cc9dce4cc18faacc82 · 186 d · inaktiv (bis 07.10.) · GB · Advertorial (advertorial-magnesium) · Titel "I was shocked by the findings" · "My husband bought me a $2,200 cooling mattress for our anniversary. And honestly? The thing that fixed my sleep was something…"
  3. 96618779 · https://app.gethookd.ai/share/ad/96618779?signature=998aa855743070858eac00651a6c8e5516b2f50fe3765b0d36aa9a6bbbc5249c · 156 d · inaktiv · Advertorial · "So, your anxiety spiked during perimenopause and menopause? Let me explain."
  4. 75017229 · https://app.gethookd.ai/share/ad/75017229?signature=ce9110c76ec45b09502afc57ff8d91288fa2035926360bef728a3f7e42085ffc · 117 d · inaktiv (bis 19.05.) · Advertorial (adv1) · "I Need to Tell You Something That Might Piss You Off About Your Doctor. My name is Karen. I'm 52 years old."
- Begründung: Kein Bettwaren-Produkt, aber das stärkste Wechseljahre-Story-Gerüst ("Soaked sheets" → Tochter → Artikel → "Dry sheets") – Skript fast 1:1 auf Decke übertragbar.

### 3.12 Earthbound Co. – Score 7
- Domains tryearthbound.com, Advertorial auf **Fake-Magazin** thelongevitybrief.com · schlaf_bettwaren · US · 284 aktiv.
- LP verifiziert: `thelongevitybrief.com/review-1` = **Advertorial** "This New "Grounding Mattress Cover" Is Helping Thousands of Americans Sleep Deeply Again" (Science Reveals Why… / Users Share Their Amazing Results / Why Earthbound Is Better Than Other Options / Try … Risk-Free (Before Supplies Run Out) / References).
- Beleg: 46362941 · https://app.gethookd.ai/share/ad/46362941?signature=ed7def77d6c5bdaef72798a308284341cf6f93707a58df7e2839cfc97b77efc9 · 366 d · aktiv · Advertorial · Transkript: "You guys I want to do a quick review on this … grounding mat So this is the king size and you can see it fits our bed" … "my husband would be like, hey, can I use it?"
- Begründung: 1 Jahr Laufzeit mit simplem UGC-Review → Magazin-Advertorial; Struktur-Vorlage.

### 3.13 Home & Garden Trend (OrthoBed-Topper / Matratzensauger) – Score 7
- Domains garden-trend.store → homegardentrend.com · haushalt_home/schlaf · US · 304 aktiv.
- LP verifiziert: `/pages/5-ways-your-old-mattress-is-destroying-your-sleep` = **Listicle-Advertorial** "5 Ways Your Old Mattress Is Destroying Your Sleep (And the Simple Fix That Works Better Than a New Mattress)" ("That's Why 47,000+ Adults Are Switching to OrthoBed").
- Belege:
  1. 104756839 · https://app.gethookd.ai/share/ad/104756839?signature=5bdcf1018bbd9c59588873cc7daa02e1bd4bebc2b7efb54a1df9626272947cc6 · 128 d · aktiv · Listicle-Advertorial · Titel "Why Smart Sleepers Are NOT Buying New Mattresses" · "⚠️ If your back, hips, or shoulders hurt every morning — this is for you."
  2. 104756778 · https://app.gethookd.ai/share/ad/104756778?signature=51f52efc58c8bfe058b257194c6c225e14f8dd3292f877b158bfee304f4a4080 · 128 d · aktiv · Video, gleiche LP
  3. 105886924 · https://app.gethookd.ai/share/ad/105886924?signature=78d67e906d1031250ad2c695637a10ee4ac90a7df0ceddb19de8f2f1dd3ec0d9 · 123 d · aktiv · PDP · Transkript: "Trigger warning do not get this if you do not want to be disgusted with yourself You thought your mattress was clean"
- Begründung: "Nicht neu kaufen, sondern X" – Listicle-Muster + Ekel-UGC, beides Angle-A-tauglich.

### 3.14 Clarifion – Score 7
- Domain clarifion.com / about.clarifion.com · allergie/haushalt · US · Seiten Clarifion (63 aktiv), Homeowners vs. Dust Mites (47), The Home Guru (6).
- LP verifiziert: `about.clarifion.com/ionizer/meta/s41/lp2/` = **Advertorial** (Label "Advertorial", "December 9th, 2025 Lifestyle & Tech") "How This Innovative Device Is Helping Thousands with Airborne Dust, Particulates, etc."
- Belege:
  1. 174677165 · https://app.gethookd.ai/share/ad/174677165?signature=f57c6b10957a9d68c61ac7806157ed1de5655df332d8e258c6880b364b6085b4 · 29 d · aktiv · Advertorial · Titel "Eliminates Dust Mites In Your Home? (MUST READ)" · "Do You Have Dust Mites in Your House? Try This Simple Solution."
  2. 149611857 · https://app.gethookd.ai/share/ad/149611857?signature=250d1afa36834d1456d8daa5984dac473696d1457300c7faa7a4f37db683c1d2 · 50 d · inaktiv · Advertorial · "Say goodbye to dust mites and hello to fresher air with Clarifion™ Air Ionizer 🌬️"
  3. 187235247 · https://app.gethookd.ai/share/ad/187235247?signature=f2e02328aeaadfd3d53cf5d4ed601853805ba3db4b1977cc164a154e1897d629 · 9 d · aktiv · Advertorial · Native-Text-Bild "Most people don't know this trick keeps dust mites away, but did you know… more"
- Begründung: Klassisches "(MUST READ)"-Native mit Persona-Seite; dieselbe Bildsprache übernahm UVlizer/TrueClean.

### 3.15 twentythree.de (Bettwäsche, DE) – Score 7
- Domain twentythree.de · schlaf_bettwaren · DE · 549 aktiv.
- LP verifiziert: `/pages/tof-ls4` = **Listicle** "8 Gründe, warum über 85.296 Menschen diese Bettwäsche statt Baumwolle benutzen ☁️" (1. Spürbar weniger Schwitzen beim Schlafen / 3. Mega sanft zur reifer werdenden Haut / 7. Top Bewertungen und 100 Tage Probeschlafen).
- Beleg: 111961242 · https://app.gethookd.ai/share/ad/111961242?signature=ad5cde84976749f387dbb9c8aac0f3db960e07cbbd33a35729c2d7d7cc64d7e0 · 130 d · aktiv · Listicle · Titel "Zu heiß zum Schlafen?" · "Wenn du nachts schwitzt, die Bettdecke wegkickst und trotzdem nicht zur Ruhe kommst, liegt es oft an d[er Bettwäsche]…"
- Begründung: Einziger DE-Bettwäsche-Listicle-Langläufer; Schwitzen + reife Haut = Angle B.

### 3.16 Weitere (Score ≤ 6) – Kurzbelege
- **Pridola (UK, Musselin-Decke)** – 178483534 https://app.gethookd.ai/share/ad/178483534?signature=1f3dc9a0cb84144d9f003396a2412c4f764930a475565b492dd494acb5ed2325 · 23 d aktiv · PDP · "If your body could talk, it would be SCREAMING for help 🥵 For years, women over 50 have been making 4 sleep mistakes that le[ad]…"; 181319442 https://app.gethookd.ai/share/ad/181319442?signature=bb50f3a6be561eaad519c76597ae6a0bc99c8834c7deb633f5206e9539e3eb50 · 18 d · "I went undercover at Bloomingdale’s to see what they really sell women over 50."; 168477031 https://app.gethookd.ai/share/ad/168477031?signature=a0080a4ba910574e0f0c459fbfb8fb0be4f856ce76257cd3ad881ccb91fc8ed8 · 41 d · Overlay "IF YOUR BLANKET'S LABEL SAYS POLYESTER / THROW IT AWAY NOW". UK-Decke mit Story-Hooks, aber ohne Native-LP (635 aktive Ads).
- **Blissy** – 168753041 https://app.gethookd.ai/share/ad/168753041?signature=d34fc84258d46be2fc6482bb0462ddf63a2166e8e9c5768a2f69f882f5a913f1 · 39 d aktiv · latest.blissy.com/pillow-reasons (GetHooked: Listicle; heute Redirect auf Salespage "Sleep Better & Wake Up Totally Ache-Free!") · "🚨 Is Your Pillow Making You Sick?" "Did you know most memory foam pillows are made from the same chemicals as gasoline? 😱"; 149328356 https://app.gethookd.ai/share/ad/149328356?signature=c29cdb7c24102c04c19a1d499dd67dd2538de2a3de3a5885395b07682389e157 · 54 d · "\"Designed by chiropractors. Not marketers.\""
- **TRAVLR / Brenda Burke** – 85720667 https://app.gethookd.ai/share/ad/85720667?signature=324dc6777331bb6a9fe467f515aa9ec092182f63eb22eadd4f677cfb67ef43c5 · 268 d aktiv · Advertorial `shoptravlr.com/pages/advert-v1` ("A Retired Pilot Exposes What Airlines Deliberately Did to Economy Seats 15 Years Ago") · "Last week, my daughter offered to fly to me instead, and I realized I'd become the grandmother who is \"too old to travel anymore\""
- **Zelesta.de** – 108558235 https://app.gethookd.ai/share/ad/108558235?signature=823f5e0a02bd7b22e2d162ddf63f0af3ee22a6c5bb569453d45d2ccd37a5f125 · 129 d aktiv · Spend $2.001–5.000 · Homepage · "|anzeige| ✨ okay aber… können wir kurz darüber reden, wie nervig bett beziehen eigentlich ist? dieses gefummel, alles verrut[scht]…" (Angle C)
- **NYVEN / Kolnar** – 154291037 https://app.gethookd.ai/share/ad/154291037?signature=3967595eff96090ffd817b25da956d379eddc24ea5f007f9cf1ea5da7893e189 · 45 d aktiv · PDP · Titel "My Daughter Sent Me This. I Should Have Found It Years Ago." · "Oh, I'm 58 years old and this $130 vacuum changed how I clean my house. My back can't handle the heavy vacuums anymore." (Angle D/C-Muster)
- **Top 5 Best Mattresses UK** – 123222968 https://app.gethookd.ai/share/ad/123222968?signature=061d59d55532a23ddb3a114503226641100388498f33de12166ead9e3e0f9f3b · 149 d (bis 08.08.) · Vergleichs-Listicle top5bestmattress.co.uk ("Top 5 Best Mattresses 2026", Platz 1 Emma) · "Tired of overthinking every purchase? Top 5 by Emma does the hard work for you."
- **Vitalisys / Emma McCarthy (UK)** – 91584388 https://app.gethookd.ai/share/ad/91584388?signature=10c45dc556ad1bab43380cd25b8801992e6268742f09c59a44ccdde41c85275b · 97 d (bis 17.07.) · Advertorial vitalisys.co/pages/menopause-insomnia (heute 404) · "Here's Why You Can't Sleep During Menopause" "I was lying on the bathroom floor at 3:42 AM when I realized this couldn't be my life anymore."
- **Doze Bedding** – 132509372 https://app.gethookd.ai/share/ad/132509372?signature=02b54bef5fe390dfd677ebe66409058a36add761c4a783cf602b59134a467bd6 · 225 d aktiv · Homepage · "Duvet the Right Way" "Between work, family, errands, and everything else we do in a day, I don’t have the energy for household battles, especially…" (Angle C)
- **Rest (Evercool Comforter)** – 30297004 https://app.gethookd.ai/share/ad/30297004?signature=9c76a6aae73a1520cfb85e881230dfdc0c0927e2bcdf2b22f13fdbccfd335bc1 · 278 d (bis 14.04.) · PDP · "94% Sleep Better With This \"Cooling Comforter\"" "For women navigating menopause, I know what a challenge restful sleep can be!"
- **Unikor NightGuard** – 89826614 https://app.gethookd.ai/share/ad/89826614?signature=bda8a350fcb8e2f6562dd7fa3c5458ffcd3fb410af918b6ee32685e486359d75 · 187 d aktiv · unikor.shop/pages/listicle-1b · "Finally, a Peaceful Night Without Pull-Ups or Pee-Stained Bedding" "Every night you wait = another load of laundry. 🧺"
- **Lovy / Unstoppable After 50** – 93897339 https://app.gethookd.ai/share/ad/93897339?signature=77c1df9ae1831ac819619b39d75b066b54061ee426b501b31f7624386613a588 · 80 d · Advertorial "I Spent 20 Years Telling Post-Hysterectomy Women Their Bladder Problems Were \"Just Aging.\" I Was Wrong." · Hook "I'm a urogynecologist, and last week one of my patients told me something I had never heard in 31 years of practice."
- **Pestlab Co** – 89056069 https://app.gethookd.ai/share/ad/89056069?signature=03e4b698dab0cfc014a2345060345694747024fd269e7bc0d0a7660663169adc · 22 d (bis 23.04.) · PDP · Charakter-Ad, Overlay "WHY YOU KEEP WAKING UP EXHAUSTED NO MATTER HOW MUCH YOU SLEEP", Transkript "I'm the bed bug living in your mattress, and I've been ruining your life from the inside out! That itchy patch on your arm … Me."
- **wellbe ("Wechseljahre und Ich", DE)** – 93282658 https://app.gethookd.ai/share/ad/93282658?signature=a05fc8962ad6c4621ba3fb0860c52622422c8d11883e7f733ddacb8e7dcbd4fe · 225 d aktiv · Spend $2.001–5.000 · Listicle auf Magazin-Domain myhealth-lifestyle.com "5 Gründe warum 250.000+ Frauen in der Menopause auf DIESES Kollagenpulver schwören…" · "Nicht jede Veränderung ist einfach nur das Älterwerden."
- **Vision Beam** – 83070525 https://app.gethookd.ai/share/ad/83070525?signature=fea1823c2dfe17ec63e200334e0e373e79f3eb677181705ce9bf09e72575b6fd · 218 d aktiv · Listicle "5 Reasons These Earbuds Are Going Viral (Especially With Side Sleepers)" · "She read every book on sleep. Tried every trick. Then she found the one thing that actually worked."
- **PurePath** – 192686369 https://app.gethookd.ai/share/ad/192686369?signature=d480381dddf157ec4096374d4ba02215ebf47c4826c50e459945e1c11f5aaa9e · 8 d · Fake-Tweet-Bild "was today years old when i ran this over the bed just to see. wasn't ready for what came off." · 168968334 https://app.gethookd.ai/share/ad/168968334?signature=3cc56664da40f34b533081c287fdfa031cd3024fb3534d1acd1589358b153fce · 39 d GB · "I'm a professional house cleaner…"

---

## 4. Wiederkehrende Muster (aus Hooks, Transkripten, LPs)

1. **"Tochter bringt Mutter die Lösung"** (UVlizer 27829534, SP Nutrition 101624013, GroundingWell 102834602, Calmhaven 93024586; Varianten: Plufl "Want Mom to Sleep Better?", Kolnar "My Daughter Sent Me This", TRAVLR "my daughter offered to fly to me", Down To Ground "why I quit cycling for my mum"). Dramaturgie: Mutter leidet still → Tochter bemerkt es/schickt Artikel → Mutter testet skeptisch → "Mom, you sound like you again".
2. **Unsichtbares Problem im eigenen Bett** ("what's in the dust", "your pillow is the problem", "The mattress just refills them", "Diese Brühe war unter mir. Jede Nacht.") + **Beweis-Ritual** (CaptureCard ans Handylicht, braune Brühe aus Nasssauger, EMF-Messgerät).
3. **"Ich habe alles versucht"-Liste** vor der Lösung (HEPA, Hot Washes, Covers, Sprays, Pillen) und **"Waschen reicht nicht"** – direkt anschlussfähig an "Decke ohne Bezug, komplett waschbar".
4. **Persona-Netz statt Markenseite**: 3–5 Seiten pro Marke (Personennamen, "Families vs. Dust Mites", "Grandma's Glow", "Reinigungstipps für Zuhause", Community-Seiten). Advertorials teils auf neutralen/Magazin-Domains (provergleich.com, thelongevitybrief.com, myhealth-lifestyle.com, journal.groundingwell.com).
5. **Titel-Formeln mit Langläufer-Beleg**: "Read if … 👆" / "Read this if …" (UVlizer 218 d); "(MUST READ)" (Clarifion, TrueClean 72 d); "If you're thinking about buying X, stop." (GroundingWell 157 d); "Don't waste your money on X until you see…" (GroundingWell 226 d); "This is why your sheets are making you sweat all night." (Cosy House 81 d); "Why Smart Sleepers Are NOT Buying New Mattresses" (128 d); "Wake up drenched? Your sheets are the problem." (108 d).
6. **Wechseljahre-Gerüst**: Nachtschweiß-Szene ("Soaked sheets every night", "pools of my own sweat") → Partner zieht ins Gästezimmer → Arzt/Gynäkologin/Artikel → "Dry sheets". Zielgruppe explizit "women over 45/50".
7. **Listicle-Aufbau Bettwaren** (Cosy House, GroundingWell, Down To Ground, twentythree): 7–10 nummerierte Gründe, Punkt 1 = Problem-Umdeutung ("It's Not the Heat. It's the Sheets."), Mitte = Mechanismus + Studien-/Kundenzahl, letzter Punkt = Risiko-frei-Testen (90/100 Nächte).

---

## 5. Kontext: Decke-ohne-Bezug-/Bettdecken-Markt (keine Native-Vorbilder, aber relevant)
- **Pleene** (brand 7553008, 145 aktiv, pleene.com + **pleene.uk**) – direkter Wettbewerber (waschbare Bettdecke ohne separaten Bezug): 182988038 https://app.gethookd.ai/share/ad/182988038?signature=3b83966def7d239d3f8f898327a0d424f41581509f344934902a9eaf4f852074 · 16 d · PDP · "No stuffing. No tying. No adjusting a separate cover. EasyRest™ goes straight back on the bed…"; 182988034 https://app.gethookd.ai/share/ad/182988034?signature=14dbc2129486bcabd193e665ddf4838458be05e7bf9dce3dfc69bf4aacede6cc · 15 d · "Clean bedding doesn’t need a complicated routine."
- **MagicSplashy EasySleep** (DE, 88310) 112080468 https://app.gethookd.ai/share/ad/112080468?signature=c6da45b72cea09eb8259e61d7eefacb44689fda59d198412a00972678b5aad00 · 202 d aktiv · PDP · "Decke + Bezug in einem 🌙"
- **Ynot-dreambig** (DE, 5346316) 131050756 https://app.gethookd.ai/share/ad/131050756?signature=34e463604904b888ab398ad947ed261791a912d99886ce964b084ebc47acb9fe · 72 d · Kollektion "bettdecke-ohne-bezug" · "Kein mühsames Beziehen mehr."
- **COZY HEAVEN** (DE, 89277) 106859899 https://app.gethookd.ai/share/ad/106859899?signature=6654ecba38e358dbcd55523058516409b7aa2514e1b28959f71aff5d4e9882dc · 119 d · PDP · "Wann hast du deine Bettdecke das letzte Mal gewechselt? Vor 3 Jahren? Vor 5? Nie? Dann hat sie Jahre von Schweiß, Hautzelle[n]…"
- UK-Bettwaren ohne Natives (Homepage/Kollektion/DPA): Bedfolk (466 d DPA), Linenbundle (389 d), Soak and Sleep (214 d), Woolroom ("Stuffy mornings? It might be your bedding." 14 d), Panda London ("Hot sleeper? Try switching your bedding." 37 d).

---

## 6. Lücken / Einschränkungen
- Transkripte: 15 Video-Ads vollständig transkribiert (siehe `transcripts/batch1_dedup.md`). Weitere ~30 Video-IDs (u. a. Plufl 122685364/121930642/108743598, Ryer 111737379/151964563, Down To Ground 133588846, Home&Garden 104756778, Blissy 168753041, SP Nutrition 142761054, Doze 132509372, Zelesta 108558235, Aeyla 117258077, Cosy House 107610671, Rest 30297004, Pridola 168477031/178483534) standen bei Abgabe noch auf "processing" (GetHooked-Queue); Hooks liegen als Ad-Text vor. Nachtrag erfolgt unten, falls fertig.
- Spend-Range ist bei fast allen US/UK-Ads null; Einstufung stützt sich daher auf Laufzeit, Varianten- und Seitenzahl.
- Geo-Filter blendet Ads ohne Länderdaten aus (GetHooked `excluded_no_geo`); UK-Abdeckung ist dadurch evtl. unvollständig.
- `native_ads=true`-Filter lieferte mit Niche/Geo 0 Treffer – nicht nutzbar.
- Einige LPs inzwischen offline/umgeleitet: aeyla best-hotel-pillows-uk-2026 (404), vitalisys menopause-insomnia (404), getuvlizer → tryclairo, latest.blissy.com/pillow-reasons → Salespage, unikor listicle-1b (nur JS-Shell, Inhalt nicht prüfbar).
- Generische Hooks ("doctor reveals", "nobody tells you", "the real reason", "women over 50") liefern überwiegend Supplements/Gelenk-/Haut-Themen; Bettwaren-Treffer kamen v. a. über Produkt-/Problemwörter (dust mites, night sweats, pillow, sheets, mattress, hot flashes, Milben, Bettdecke).
