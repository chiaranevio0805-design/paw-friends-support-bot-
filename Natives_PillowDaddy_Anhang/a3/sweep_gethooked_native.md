# Agent 3 – Sweep GetHooked (Native-/Advertorial-Filter): weitere Native-Vorbilder in Schlaf / Bettwaren / Haushalt / Allergie / Wechseljahre / Hygiene

Stand: 08.10.2026, ca. 11:05 Uhr · Quelle: GetHookd MCP (`search_ads`, `aggregate_ads`, `get_domain_advertisers`, `get_ad`) + Playwright-Abruf der Landingpages (mobil, Texte unter `a3/lp/*.txt`, Screenshots `a3/lp/*.png`).
PillowDaddy und seine Persona-Seiten sind bewusst **nicht** enthalten (Agent 1).

**Definition „erfolgreich" (wie im Auftrag):** Laufzeit ≥ 30 Tage, viele aktive Ads/Varianten, Spend-Bucket, mehrere Persona-/Advertiser-Seiten auf derselben Domain. Laufzeit = `days_active` aus GetHookd (bei aktiven Ads „start_to_today"). Zeitfenster laut Konventionen: Ads mit Ende ≥ 08.04.2026 oder heute aktiv.

---

## 0. Kurzfazit (für Agent 4)

1. **Es gibt einen direkten Kategorie-Vorreiter: MagicSplashy (DE, „EasySleep" Decke + Bezug in einem).** Die Marke fährt ihre Decke ohne Bezug über ein ganzes Presell-System: Redakteur-Ich-Story („Ich habe 15 Jahre lang jede Woche Bettwäsche gewechselt…"), Kundenumfrage-Advertorial („Das Bettbeziehen war eine Qual…"), Wechseljahre-Listicle im Look eines Frauenmagazins („7 Gründe, warum Frauen in den Wechseljahren jetzt ihre Bettdecke tauschen!") und eine Sommer-Hitze-Presell-Seite. Die stärkste Ad dazu ist eine UGC-Ich-Story mit **Spend $10.001–20.000, „Winning", 83 Tage aktiv** → das ist die nächstliegende Vorlage für unsere Angles B und C (und teilweise A).
2. **Hygiene-Angle A ist in UK bewiesen:** UVLizer/„Clairu" (UK-Klon von Clarifion) fährt Milben-Advertorials mit **489 / 436 / 246 / 245 Tagen Laufzeit** in GB, und zwar über mehrere Persona-Seiten (DetoxSpa UK, Families vs. Dust Mites, By Clairu). Mechanismus: „Der p 1" in Milbenkot, „84% of British people…", Geschichten von „Grandma Carol, 76" und „Mom Lisa, 37, Manchester". Dazu „Miracle Sheets" (US) über *The Granny Blog* mit rund 2.400 aktiven Ads auf 8 Personas: Bakterien im Kissenbezug („more than a toilet seat", „ICU nurse swabbed my son's pillowcase").
3. **Wechseljahre-Angle B wird in den USA mit Bettwaren groß gefahren:** Plufl Hugl (Night-Sweats-Advertorial, Creator-Netz mit 17 Seiten, Ads bis **309 Tage** aktiv), Eight Sleep über Publisher-Advertorial (*The Get Well*: „Hot Flashes on My Side, Freezing on His…"), GroundingWell („10 Reasons Why Women Over 50…", 46 Advertiser-Seiten), Silvery Cooling Comforter („Doctor tested Top 5").
4. **Angle D (Tochter/Mutter)** gibt es nicht als eigenes Format im Bettwaren-Markt. Die nächsten Vorlagen sind Gründer-Story „why I quit cycling for my mum" (Down To Ground), Ich-Story „Tochter wäscht bei Mama" (X-All Waschmaschinenreiniger, 235 Tage) und die Altersgeruch-Scham „your children, your grandchildren — they notice" (Swarva).
5. **Wiederkehrende Formate:** (a) Persona-Seiten mit Vornamen + Nachnamen oder „Community/Insider/Today"-Namen, die alle auf **dieselbe** Presell-Domain zeigen; (b) Listicle „X Reasons Why [Zielgruppe] Are Switching to…"; (c) Ich-Story-Advertorial mit Tiefpunkt-Szene (Krankenhaus, Chef, 3 Uhr nachts); (d) „We tested 5 …" Vergleichs-Listicle mit Arzt/Experte; (e) UGC-/Creator-Video, das auf ein Advertorial statt auf die PDP zeigt.

---

## 1. Suchprotokoll (was gesucht wurde, Treffer)

| # | Suche | Filter | Treffer (brand-capped) | Ergebnis |
|---|---|---|---|---|
| 1 | duvet | page_type adv/list, geo GB | 1 | nichts Relevantes (Avalaine Nervenpflaster) |
| 2 | duvet | page_type adv/list | 5 | Moodie (Kissen), Avalaine |
| 3 | pillow | page_type adv/list | 332 | Mellow Sleep-Netz, Blissy, Nourial, The Pillow Home, Moodie |
| 4 | menopause night sweats | page_type adv/list | 11 | Plufl, GroundingWell, Bloomin, Wilderglow, Camille Rhodes |
| 5 | blanket | page_type adv/list | 78 | Splash Blanket, Fine Foams, The Get Well/Eight Sleep |
| 6 | sheets | page_type adv/list | 133 | GroundingWell-Netz, Healthy Essential (Waschmittelblätter), Miracle/Granny Blog, VegOut/Eucalypso |
| 7 | mattress | page_type adv/list | 102 | Down To Ground, Home & Garden Trend, Top 5 Best Mattresses UK (Emma), FluffCo, Eight Sleep |
| 8 | dust mites | page_type adv/list | 20 | **UVLizer/Clairu UK**, Clarifion, AeroPure, Swissker |
| 9 | sleep / menopause | native_ads=true | 5 / 1 | Uk Sleep Forum (Airvex), Helen Glover (Sleepsake UK) |
| 10 | (ohne Query) | native_ads=true, geo GB, sort days_active | 13 | Facet deckt nur Ads seit ca. 26.08.2026 ab → für Langläufer ungeeignet |
| 11 | night sweats | page_type adv/list | 38 | **Plufl-Creator-Netz** (bis 309 Tage) |
| 12 | hot flashes | page_type adv/list | 36 | Eight Sleep, Vono Labs, Bloom & Bond, SP Nutrition |
| 13 | allergy | page_type adv/list | 82 | überwiegend Haustier; AeroPure |
| 14 | mould | page_type adv/list | 13 | AeroPure |
| 15 | washing machine | page_type adv/list | 28 | X-All (235 Tage), Uproot Clean, Swarva, Gohomie UK, PrimeDrum |
| 16 | comforter | page_type adv/list | 4 | **The Sleep Edit / Silvery** |
| 17 | silver sheets bacteria | page_type adv/list | 11 | Miracle/Granny Blog, Down To Ground (Gründer) |
| 18 | weighted blanket | page_type adv/list | 27 | fast nur Supplements |
| 19 | Bettdecke | language de | 954 (Obergrenze) | **MagicSplashy**, HappyBed, OhMySwiss, Paradies, Anfaru, Zelesta (DE-Wettbewerb Decke ohne Bezug) |
| 20 | Milben | language de | 76 | **Ryer + provergleich.com** (8 Seiten), elsa Schweiz |
| 21 | Wechseljahre | language de, sort days_active | 182 | Supplements; „Wechseljahre und Ich" (225 Tage) |
| 22 | Nachtschweiß | language de | 602 (Obergrenze) | Yasuxi, Cozy Heaven, Cellumove (alle PDP) |
| 23 | what's living in your bed | page_type adv/list | 56 | nichts aus Bettwaren |
| 24 | women over 50 sleep | page_type adv/list, geo GB | 17 | GroundingWell, Vitalisys (Schlafpflaster) |
| 25 | (ohne Query) | page_type adv/list, geo GB, aktiv, sort days_active | 972 | UK-Langläufer: DetoxSpa UK (UVLizer-Domain, 518 Tage Katzen-Listicle), sonst fachfremd |
| 26 | sleep | page_type adv/list, geo GB | 259 | Top 5 Best Mattresses UK, Nourial, GroundingWell |

Zusätzlich `aggregate_ads(group_by=page_type)` für 18 Domains, `get_domain_advertisers` für 15 Domains, Brand-Listen (`brand_id`) für FluffCo, MagicSplashy, HappyBed, MarshMellow Comforter, Mark Davis (Granny Blog) sowie `get_ad` für zwei MagicSplashy-Winner.

---

## 2. Kandidaten (sortiert nach Score für unsere Angles)

Legende LP-Typ: Advertorial / Listicle / Presell (Landing mit Story/Reviews vor der PDP) / PDP / Vergleichsseite. Hooks wörtlich (GetHookd kürzt Hooks nach ca. 125 Zeichen, „…" = Kürzung durch GetHookd).

### K1 · MagicSplashy „EasySleep" (Decke + Bezug in einem) · Score 10
- **brand_id** 88310 · **Domain** magicsplashy.de (.ch) · **Kategorie** Schlaf/Bettwaren · **Markt** DE/AT
- **Native-Formate:** Redakteur-Ich-Story-Advertorial (`/pages/gesund-schlafen`: „Ich habe 15 Jahre lang jede Woche Bettwäsche gewechselt. Bis ich verstanden habe, dass das Problem die Decke war." – Daniel K., „Haushalts- & Alltagsredakteur", Punkt 02 „Hygienischer als jede normale Bettwäsche"), Kundenumfrage-Advertorial (`/pages/umfrage`: „Was die Menschen über unsere Decke denken. Das Ergebnis hat selbst uns aus der Bahn geworfen." – Punkt 01 „Das Bettbeziehen war eine Qual für Kopf und Geist, ich konnte es nicht mehr."), Wechseljahre-Listicle im Frauenmagazin-Stil (`/pages/frauen-magazin`: „Die Decke, unter der du seit Jahren schläfst, ist in den Wechseljahren dein größter Gegner. / 7 Gründe, warum Frauen in den Wechseljahren jetzt ihre Bettdecke tauschen!"), Presell-Seiten (`/pages/schlafen-im-sommer`: „Die Decke, die dich bei 30 Grad schlafen lässt wie bei 20. Warum sie ständig ausverkauft ist:"; `/pages/easysleep`: „Ich hab mein Bett seit einem Jahr nicht mehr bezogen. Und es ist sauberer als je zuvor."; `/pages/gut-schlafen`: „"Nie wieder Bettwäsche wechseln am Sonntag" / Wie 17.000+ Deutsche dem Betten-Beziehen ade sagten…", „Bekannt aus Bild der Frau, Focus Online, Stern, WELT"), UGC-Ich-Story-Video.
- **Erfolgssignale:** 177 Ads gesamt / 146 aktiv; Presell-Ads mit Spend $10.001–20.000 und Performance „Winning"; PDP-Langläufer 202 Tage.
- **Belege:**
  | Ad-ID | Status | Laufzeit | Format | LP / Typ | Hook bzw. Bildtext wörtlich |
  |---|---|---|---|---|---|
  | [126012757](https://app.gethookd.ai/share/ad/126012757?signature=4aa5cf75157a813c3daede61927240a452d4bf09046a0feee9ae288bd457658f) | aktiv | 83 T (seit 18.07.) · Spend $10.001–20.000 · „Winning" · EU-Reichweite 1,3 Mio | Video 57 s, UGC-Ich-Story | magicsplashy.de/pages/schlafen-im-sommer · Presell | „Ich habe die Easy-Sleep-Decke bestellt, weil ich einfach keinen Bock mehr hatte, jede Woche mit der Bettwäsche zu kämpfen." · Overlay „DAS WARS MIT BETTWÄSCHE WECHSELN!" |
  | [148248622](https://app.gethookd.ai/share/ad/148248622?signature=84d901c24974a36d3944f48f20a4e49c67491a96f0afc5eac2f108a8698f93ac) | aktiv | 53 T · Spend $2.001–5.000 · „Winning" | Bild | /pages/umfrage · Umfrage-Advertorial | Bild: „“Ich hab Bettwäsche gestrichen.” Decke + Bezug in EINEM." · Text: „Decke + Bezug in einem 🌙 Die EasySleep Bettdecke macht Bettmachen endlich einfach…" |
  | [125662155](https://app.gethookd.ai/share/ad/125662155?signature=58704b1448c83dbd30e5cb1d8fd3327deff8aa407978d23dc3eaad4c5b389a11) | aktiv | 84 T | – | /pages/gesund-schlafen · Redakteur-Advertorial | Titel „Nie wieder Bettwäsche wechseln 🛏️" (Hook nicht einzeln abgerufen) |
  | [196672570](https://app.gethookd.ai/share/ad/196672570?signature=25fdd89bbee9e2fe42c316af211c2cca53a5142c9af403d5f8406c8a0fe30b20) | aktiv | 6 T (Test) | – | /pages/frauen-magazin · Listicle (Wechseljahre) | „Nie wieder Bettbezug wechseln 🌙 Die EasySleep Bettdecke macht Bettmachen endlich einfach…" |
  | [112079858](https://app.gethookd.ai/share/ad/112079858?signature=d437bb1ca539176a632abb07f1c15432d04d11076276d79c6ca87de68d650db6) | aktiv | 202 T · Spend $5.001–10.000 | – | /products/easysleep-decke · PDP | Titel „Bett machen im Handumdrehen 👋"; Bildtext der Serie: „Nie wieder Bettwäsche wechseln. Decke + Bezug in EINEM. Komplett waschbar / Schnell trocken" |
- **Warum:** Gleiches Produkt wie unseres, gleiche Probleme (Beziehen, Hygiene, Nachtschweiß in den Wechseljahren). Die Marke hat schon geklärt, welche Presell-Seiten tragen. Die Seiten lassen sich fast 1:1 ins Englische (UK) übertragen. Lücke: Die Frauenmagazin-Seite ist erst seit 6 Tagen aktiv und deshalb noch nicht belegt; belegt sind die Seiten schlafen-im-sommer, umfrage und gesund-schlafen.

### K2 · UVLizer / „Clairu" (UK-Klon des Clarifion-Playbooks) · Score 9
- **brand_ids** DetoxSpa UK 70309 (183 aktive Ads auf der Domain), Families vs. Dust Mites 197491 (22), By Clairu 126532 (27), dazu auf derselben Domain Better Home Habits 279134 (201, anderes Gerät „fridgie"), Dogs Are Family 197494, Fresh Cat Home 281364 → **6 Advertiser-Seiten**
- **Domain** getuvlizer.co.uk (leitet heute auf **tryclairo.co.uk** um) · **Kategorie** Allergie/Hygiene (Milben in Bett, Kissen, Sofa) · **Markt** GB
- **Native-Formate:** Ich-Story-Advertorial einer Persona („By Lisa Morgan, Retired Nurse": „How This Grandma Effortlessly Cleared Dust Mites from Her Home in Just 30 Minutes", Carol F., 76), Familien-Story-Advertorial („How This Mom Saved Her Family From A Mysterious Dust Mite Invasion With a Quick Trick", Lisa C., 37, Manchester), Listicle („🏠 10 Reasons Why Thousands Are Switching to Clairu…", „Health insider", By Jessica M.). Mechanismus: Milbenkot mit dem Allergen „Der p 1"; Statistik „84% of British people suffer from allergy symptoms inside their own homes"; Angebot £19.99, bis 46 % Rabatt, „LIMITED STOCK OFFER", 30-day money back guarantee.
- **Seitenstruktur laut aggregate:** listicle 93, advertorial 20, product_page 9 (aktive Ads)
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | LP / Typ | Hook wörtlich |
  |---|---|---|---|---|---|
  | [80269727](https://app.gethookd.ai/share/ad/80269727?signature=275f24a45e105ebc7d27ead2e15742ba603a98d219aec0dcc4a0d7580466ec2c) | DetoxSpa UK | aktiv | **489 T** (seit 07.06.2025) | getuvlizer.co.uk/pages/adv-dust-mites · Advertorial | Titel „Eliminates Dust Mites In Your Home? (MUST READ)" · „Do You Have Dust Mites in Your House? Try This Simple Solution." |
  | [80270006](https://app.gethookd.ai/share/ad/80270006?signature=20213f2ee6b41377ee81640500cf7374b279c71704ec04b071a25a801fe48783) | DetoxSpa UK | aktiv | **436 T** (Video) | dto. · Advertorial | dto. |
  | [77369458](https://app.gethookd.ai/share/ad/77369458?signature=61d29ab41b5b2da978ab945b1b0d18128bf6a766575735c3cf143e969d987c4e) | Families vs. Dust Mites | aktiv | 246 T (Bild) | /pages/dust-mite-invasion · Advertorial | „Do You Have Dust Mites in Your House? Try This Simple Solution." · Bild: „Easy Trick to Protect Your Family From Dust Mites (They Can't Stand This)… more / Microscopic Poop / You can't see them. But you're breathing them in. Every night." |
  | [77486364](https://app.gethookd.ai/share/ad/77486364?signature=08c6c0a6320dee63e33e114d90951096dfcf25fad932db586688d978bd8df5bd) | By Clairu | aktiv | 245 T | /pages/dust-mites · Listicle | „⚠️ 84% of homes have dust mite allergens in the air — most people never realize *until they get sick*." |
  | [98699538](https://app.gethookd.ai/share/ad/98699538?signature=f5b56ac0c5087bcdf0a9ea67d9725b0f2b79f842390d7114883755788ae8d7c3) | Families vs. Dust Mites | aktiv | 152 T (Video) | /pages/dust-mite-invasion · Advertorial | „Do You Have Dust Mites in Your House? Try This Simple Solution." |
- **Warum:** In GB nachweislich jahrelang profitabel. Beweist, dass UK-Käufer auf „unsichtbare Milben in Bettzeug + Ich-Story einer älteren Frau" reagieren. Das ist genau unser Angle A, nur mit einem anderen Produkt. Die Erzählperspektive „Retired Nurse erzählt Grandma-Story" passt auch zu Angle D.

### K3 · Miracle Sheets über „The Granny Blog" (Fake-Magazin + Ich-Story-Personas) · Score 9
- **brand_ids (Personas auf thegrannyblog.com):** Mark Davis 13039094 (760 aktive Ads), Lifed 88032 (463), Rachel Monroe 14234590 (447), Cammy Bennett 15227765 (403), Julia Dawson 19855729 (148), Olivia Taylor 17346087 (91), Melissa Taylor 1286792 (81), Sophia Miller (1), früher James Moore 4554328 → **8 Personas, ~2.390 aktive Ads**
- **Domain** thegrannyblog.com (`/miracle-gma/`, `/miraclefbv2-get/`), gogrannyblog.com · Produkt: Silber-Bettwäsche „Miracle Sheets" · **Kategorie** Hygiene/Bettwaren · **Markt** US
- **Native-Formate:** Fake-Magazin-Advertorial („✦ The Granny Blog / ADVERTORIAL / Good Morning America Features The Sheet Set That's Changing How America Sleeps — And We Tested It For 30 Days", „Special editorial by Sarah Johnson, Senior Editor"; Mechanismus: „the average pillowcase contains over 3 million bacteria per square inch — more than a toilet seat") + Ich-Story-Ads im Stil „Ich darf das eigentlich nicht posten".
- **Belege:**
  | Ad-ID | Persona | Status | Laufzeit | LP / Typ | Hook wörtlich |
  |---|---|---|---|---|---|
  | [99445068](https://app.gethookd.ai/share/ad/99445068?signature=7d374440e76d412b469cac680610215a7e93e19bb4fbdb167786e870655278ea) | James Moore | inaktiv | 43 T (02.05.–13.06.) | thegrannyblog.com/miracle-gma/ · Advertorial | Titel „These New Silver-Infused Sheets Kill 99.7% of Bacteria While You Sleep" · „My wife is going to kill me for posting this. She made me promise I wouldn't. I'm doing it anyway because I almost lost her t…" |
  | [98842631](https://app.gethookd.ai/share/ad/98842631?signature=8628a81dca2c4c422fd78fab6cfa1be55d1e2b62226e767416cc759c7e97a658) | Melissa Taylor | inaktiv | 19 T | dto. | Titel „"Wrinkle-Free" Sheets Right Out The Dryer" · „My dad would probably be furious if he knew I was posting about this. But if his accident can help prevent even just ONE fami[ly]…" |
  | [198629101](https://app.gethookd.ai/share/ad/198629101?signature=4aea0ba899ae2b074395d19a924fa3c33e96c33e78d690093c20ec36d62612fe) | Mark Davis | aktiv | 4 T (Test, Teil einer ~760er-Welle) | dto. | „Ive been an ICU nurse for 14 years. Last month I swabbed my sons pillowcase as a joke to win an argument with my wife. Nobody…" |
- **Warum:** Exakt unser Hygiene-Mechanismus (Bakterien im Bettzeug), aber für Bettwäsche. Der Erfolg zeigt sich hier in der **Masse** (8 Personas, ~2.400 aktive Ads, rotierende Kurzläufer), nicht in der Laufzeit einzelner Ads. Einschränkung: Die einzelnen Ads laufen kurz (ältere Belege 19–43 T); Spend-Daten fehlen.

### K4 · Plufl „Hugl" Self-Cooling Body Pillow (Night-Sweats-Advertorial + Creator-Netz) · Score 9
- **brand_ids** Plufl 116814 (131 aktiv auf Domain), Plufl 7705, Hannah Houg 351627, Shay 7488236, Gen X Jess 344266, Noah S. 508882, Victoria Roberts 11396607, Yuki K. 7154072, Mammaboomboom, Perfectly Kelsey 28432, Ashley Faith, Stacey's 7154074, Linzy Taylor Shop 16716 u. a. → **17 Advertiser-Seiten**
- **Domain** weareplufl.com · **Kategorie** Wechseljahre/Schlaf · **Markt** US
- **Native-Format:** Alle 198 aktiven Ads führen auf **ein** Advertorial (`/pages/hugl-sleep-system-advertorial`): „How 40,000+ Hot Sleepers Are Finally Sleeping Through the Night — No Medications, No Pillow Flipping, Just NASA-Inspired Cooling" („For women over 45…", „women 45-65 account for 78% of temperature-related sleep disruption cases", „As Seen on Shark Tank", Countdown + 2 Gratis-Geschenke). Zulieferer: UGC-Creator-Videos (Whitelisting) mit Kommentar-Overlay.
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | Typ | Hook wörtlich |
  |---|---|---|---|---|---|
  | [121399208](https://app.gethookd.ai/share/ad/121399208?signature=a7525a95abd29dcb4a1de055c7ca72296aaa71af4bd20a5eb1f544e781a7eff9) | Perfectly Kelsey | aktiv | **309 T** | UGC-Video → Advertorial | „Watch me cut my sleep expenses in half. Yeah, that's a huggle. It's a cooling body pillow that has literally saved me money." |
  | [108743671](https://app.gethookd.ai/share/ad/108743671?signature=b0000a7c59c2ee58d28ba481695e1924deb9fa9708315307a2566b8d3366184a) | Hannah Houg | aktiv | 176 T | Video → Advertorial | „Tired of waking up drenched? 🌡️ 😫 Say goodbye to night sweats with the Hugl Self-Cooling Body Pillow trusted by 21,346+ hot…" |
  | [156685182](https://app.gethookd.ai/share/ad/156685182?signature=3f819bd7d341758781d6980209495cce9d85d37b496e66da36a01b02eaf94f90) | Yuki K. | aktiv | 145 T | Video → Advertorial | dto. |
  | [117887406](https://app.gethookd.ai/share/ad/117887406?signature=a3f51209716548557e8683ad380c293cac78c5896d26fb0bc72a4b42f6800c82) | Plufl | aktiv | 130 T | Video → Advertorial | „My night sweats were constant. I felt miserable. 3 a.m. wake-ups, drenched sheets, multiple fans. Sound familiar?" · Overlay: „Anyone else's husband sleeping in the guest room because of their sweating? 😔" |
  | [117887399](https://app.gethookd.ai/share/ad/117887399?signature=b724667b3a212141ffb5dcab59d3c1e24445eafae4ed4e4203243819d1281c63) | Plufl | aktiv | 130 T | Video → Advertorial | „I still see a ton of people commenting that they think this is just a regular body pillow with a $189 price tag, so I wanted…" · Overlay „I ain't paying $189 for a body pillow." |
- **Warum:** Die beste belegte Vorlage für Angle B (Nachtschweiß, Ehemann im Gästezimmer, Frauen 45+) mit einem Bettwaren-Produkt. Das System „viele Creator-Seiten → ein Advertorial" lässt sich direkt übernehmen.

### K5 · Eight Sleep Pod über Publisher-Advertorial „The Get Well" · Score 8
- **brand_ids** The Suite 6005158 (19 aktiv), The Get Well 8071 (3), kellysomers 515674 (3), Noah Vale 247022, Jasper Wythe 6161906, Abby Power 6975644 → 6 Seiten
- **Domain** i.eightsleep.com (Redirect) → thegetwell.co/brands/eight-sleep-couples/ · **Kategorie** Wechseljahre/Schlaf (temperierte Matratzenauflage) · **Markt** US
- **Native-Format:** Publisher-Advertorial „Hot Flashes on My Side, Freezing on His: How One Sleep Upgrade Ended Our Blanket Wars for Good" (THE GET WELL STAFF, „Sponsored"; Entdeckung über einen Reddit-Thread zur Menopause; Preis $2,899 wird offen genannt). Ad-Bild: Reddit-Kommentar-Screenshot („my wife (also perimenopausal and experiencing hot flashes overnight)…") + „HER SIDE 86° / HIS SIDE 67°".
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | Hook wörtlich |
  |---|---|---|---|---|
  | [150166895](https://app.gethookd.ai/share/ad/150166895?signature=036356691a32567027bb0c9bfe0b90058d72fa211f5ff02cc29688018566fcd5) | kellysomers | aktiv | 52 T | Titel „Hot Flash at 2AM? The Pod 5 Cools Me Down Automatically. 😮‍💨❄️" · „We tried Eight Sleep's temp-regulating mattress cover on a whim, and it's the best thing that has ever happened to our sleep:" |
  | [150166893](https://app.gethookd.ai/share/ad/150166893?signature=67f736dbfed3d22823db96bd295ed3c1d3a477243aa3a9fb2532f2916ba8ae84) | kellysomers | aktiv | 52 T | Titel „This Temp-Regulating Mattress Cover Saved My Sleep (+ My Marriage) 😅" · „After months of waking up sweaty while my husband froze under 3 blankets… we found the Pod 5." |
  | [150331872](https://app.gethookd.ai/share/ad/150331872?signature=cfb06d44ca463e36501ccf428fd3c7debdfdc1edf28704785e56da52f279c9aa) | The Get Well | aktiv | 52 T | Titel „The Sleep Tech That Ended Blanket Wars (and Boosts Deep Sleep by up to 34%) 🔥" |
  | [150166898](https://app.gethookd.ai/share/ad/150166898?signature=45565c82f30910ae608a5eb5f07e15ce2d5af39a9f371922e4283203b2d56706) | kellysomers | aktiv | 52 T | Titel „Eight Sleep's Pod 5 Saved My Sleep, My Sanity, and My Marriage. 😅" · „If there's one thing they don't tell you about relationships, it's how hard it can be to share a bed." |
  | [181990936](https://app.gethookd.ai/share/ad/181990936?signature=c422c63c86b743e243607e9292df37c88576ce28cdd53f47473e742475a345d3) | The Get Well | aktiv | 16 T | Titel „Blanket Fights? Over. Night Sweats? Gone. Couples Are Obsessed With This Sleep Tech. 👉" |
- **Warum:** Zeigt, wie eine Premium-Bettwarenmarke Wechseljahre und „Decken-Krieg im Paar" über einen Fremd-Publisher erzählt. Die Paar-Perspektive ist für Angle B wichtig: Nicht nur die Frau leidet, auch der Partner.

### K6 · GroundingWell (Grounding-Bettlaken) · Score 8
- **brand_ids** GroundingWell 697 (623 aktiv auf Domain), Wellness Today 689 (156), Grounding Health Benefits 698 (65), Cynthia Roberts 7011057 (56), Charlotte Miller 2741196 (41), Amber Hayes 306559 (30), Elizabeth Porter 4296525, Kirsty Phillips 2112042, „The Honest Mama", „Nerve Support Community" … → **46 Advertiser-Seiten** auf groundingwell.com, 7 auf journal.groundingwell.com
- **Domains** groundingwell.com (`/pages/special-sheet-listicle`, `/pages/special-sheet-listicle-sleep-aid`), journal.groundingwell.com (`/pages/bed-sheet`, `/pages/o4`), article.groundingwell.com (`/b09`) · **Kategorie** Bettwaren/Wechseljahre · **Markt** US, GB, EU
- **Native-Formate:** Listicle „10 Reasons Why Women Over 50 Are Switching to this "Special Sheet" to Wake Up Refreshed And Pain-Free in 2026" (By Linda L., „Read this BEFORE you take one more sleep/pain pill!"); Ich-Story-Advertorial „This "Weird" Sheet Finally Fixed My 3-Year Sleep Problem" (by Emma Richardson: im Auto eingeschlafen, 17 verpasste Anrufe vom Chef); Airbnb-Gastgeber-Story; Animations-Video „this is grace she's 49…". Auf groundingwell.com: product_page 931, listicle 56; journal: advertorial 21.
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | LP / Typ | Hook wörtlich |
  |---|---|---|---|---|---|
  | [89809570](https://app.gethookd.ai/share/ad/89809570?signature=a594daabb56da2a6e21f0132ef0d21f1489618e1ca4e90dcb7b80db526cd31a2) | Wellness Today | inaktiv | 157 T (bis 08.09.) | special-sheet-listicle · Listicle | „If you're thinking about buying a Grounding Well bed sheet, stop. There's something that I should have told you but I didn't…" |
  | [87653051](https://app.gethookd.ai/share/ad/87653051?signature=a9b8c433898921321593a0f1db5b39ad47230b7d10422ffee811a568bcfdf21b) | Wellness Today | inaktiv | 127 T (bis 30.07.) | dto. | „💛 UP TO 67% OFF + FREE GIFT 💛 If you're a woman over 50 who's tired of waking up exhausted, stiff, and in pain - read this b[efore]…" |
  | [102834602](https://app.gethookd.ai/share/ad/102834602?signature=9c8b44383ab0135a4a6de55c19f68e2f22d1b7857055c639215d87c4e7c13afd) | GroundingWell | inaktiv | 108 T (bis 08.09.) | special-sheet-listicle (v2) · Listicle | „this is grace she's 49 she slept eight hours last night and woke up more tired than before she doesn't know this exhausted wo[man]…" (3D-Animation, Overlay „THIS IS GRACE") |
  | [174085195](https://app.gethookd.ai/share/ad/174085195?signature=7e38f85035ad1ae57d8bdd275358b2d0a45c4450809b83e04fd24c31be2a434c) | Amber Hayes | aktiv | 30 T | journal…/pages/bed-sheet · Advertorial | „I heard about grounding sheets through social media, did some research on it, and decided that it would be worth my time to g[ive]…" |
  | [176347757](https://app.gethookd.ai/share/ad/176347757?signature=57d95409652460dc005e44b87150c3daf95c995f805d8fb7740558704b0a9854) | Grounding Health Benefits | aktiv | 27 T | special-sheet-listicle · Listicle | „✨ 5 Reasons why grounding is a solution for hot flashes and night sweats 👉 Effective for hot flashes, night sweats & broken…" |
- **Warum:** Bettwaren, Zielgruppe „Frauen über 50", Wechseljahre-Begriffe, sehr breites Persona-Netz. Sehr gute Listicle-Vorlage für Angle B. Der Mechanismus (Erdung) ist für uns nicht übertragbar, die Struktur aber schon.

### K7 · Down To Ground (Grounding-Matratzenbezug) · Score 7
- **brand_ids** Down To Ground 36329 (1.095 aktiv auf Domain), Frazer 7049265 (161, Gründer-Persona), Biggest Grounding Sale 7049260 (119), Down To Ground Learning 3414031 (48), DTG 7049262 (27), Benefits of Grounding 805589 (19), averysgroundingjourney 5386203, Sandy Thompson, James Corbin → 9 Seiten
- **Domain** downtoground.co (`/pages/article-listicle`) · **Kategorie** Bettwaren · **Markt** US, GB
- **Native-Formate:** Gründer-Listicle „8 Reasons Why Everyone Is Replacing Their Old Bedding with This Grounding Mattress Cover" (By Frazer C.); Gründer-Story-Ads (auch über die Mutter); Fake-Beschwerde-Hook. Laut aggregate: listicle 433, product 109, advertorial 32.
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | Typ | Hook wörtlich |
  |---|---|---|---|---|---|
  | [124903647](https://app.gethookd.ai/share/ad/124903647?signature=81bb58a967f0181cebd34f76a72667fb6b9f14faca207a0687d87c41fbfbdc7c) | Down To Ground | aktiv | 86 T | Video → Listicle | „Yes, our mattress cover is expensive. Here's why that's a good thing. My name's Fraser. I'm the founder of Down to Ground. I…" |
  | [150220474](https://app.gethookd.ai/share/ad/150220474?signature=e7cbe035100f1d921db5924fb1933f21766ec742a359fdf1aadbaa69193f17a4) | DTG | aktiv | 75 T | Bild → Listicle | „You went to bed on time…so why do you still feel off? If your sleep feels light, it might be time to try something different…" |
  | [130630996](https://app.gethookd.ai/share/ad/130630996?signature=705626133e6c03915f14a82675bd6194c5ef8c9c093a98c6191275a7a14464bb) | Down To Ground Learning | aktiv (GB) | 75 T | Video → Listicle | dto. |
  | [169458382](https://app.gethookd.ai/share/ad/169458382?signature=494aacfa3cc49cf887f0e6f5926cb7fe3ff27d6cc24010e8248fa43a43bb4a7b) | Frazer | aktiv | 46 T | Bild → Listicle | Titel „why I quit cycling for my mum" · „People ask me why I quit professional cycling to make mattress covers. The honest answer is my mum…" |
  | [115569935](https://app.gethookd.ai/share/ad/115569935?signature=03885f66fb7e75db0034ba3e27da23926b5208ea54929db09d51590e75e3dc28) | Down To Ground Learning | inaktiv | 37 T | Video → Listicle | „I'm so frustrated. I bought this down-to-ground mattress cover and now I'm considering a refund…" |
- **Warum:** Bettwaren-Listicle, läuft auch in GB. Liefert die einzige echte „für meine Mutter"-Erzählung (Angle D) und das Muster „Gründer erklärt den hohen Preis".

### K8 · Mellow Sleep (Cloud-Align-Kissen + MarshMellow Comforter) · Score 7
- **brand_ids** u. a. VictorGonzalez 11368761 (940), Mellow Cloud Pillow 1329122 (899), Mellow Cloud Align Pillow 4398848 (690), Mellow Sleeping Company 4398847 (640), Mellow Bedding 2359895 (508), Dr. Ralph Napolitano 2755134 (482, Chiropraktiker-Persona), MarshMellow Comforter 4398840 (397), Mellow Comforters 356060 (106), Mellow Hotel Collection 11369172 (118), Anthony Moll 2519277 (270), Jess's Favorite Finds 2748629 (237), Heim Health 227026 (228) … → **≥ 50 Advertiser** (Liste bei 50 abgeschnitten)
- **Domain** mellowsleep.com · **Kategorie** Bettwaren (Kissen, Bettdecke) · **Markt** US
- **Native-Formate:** Ich-Story-Advertorial `/pages/wp-adv-2` („My Chiropractor Told Me to Stop Wasting Money on Pillows. Then She Showed Me This One." – By Jackie S), Listicle `/pages/solvi-list-1` („10 Reasons Chiropractors Are Recommending This Pillow For Neck Pain, Stiffness & Poor Sleep"), Experten-Persona-Videos (Chiropraktiker), UGC. Hinweis: `/pages/rp-001` leitet heute auf `/pages/gu-ad-1` um (Verkaufsseite statt Listicle). Laut aggregate: landing 1.564, product 1.167, listicle 939, advertorial 473.
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | LP / Typ | Hook wörtlich |
  |---|---|---|---|---|---|
  | [95218705](https://app.gethookd.ai/share/ad/95218705?signature=cf1770991bf3d70d33a96540e7561a30f12f348a42b7ae16ae3ba44c17f16a2d) | Dr. Ralph Napolitano | aktiv | 168 T | solvi-list-1 · Listicle | „Stop folding your pillow in half and sticking it under your head and neck. This is causing you a lot of pressure, tension, an[d]…" |
  | [100378666](https://app.gethookd.ai/share/ad/100378666?signature=1747f116d702c6e1c8a457bbacee28529e40415ea455710daf7cad9cd3e56ddc) | Anthony Moll | aktiv | 148 T | rp-001 · (heute Redirect auf Landing) | „Oh Hear that most side sleepers don't realize what they're doing to their shoulder when they're sleeping for 10 hours or more…" |
  | [74769954](https://app.gethookd.ai/share/ad/74769954?signature=77a2349873b6915e3d645ecbbe463e01f205ccd4c3ed14d127c477b14ec6fb98) | Heim Health | inaktiv | 139 T (bis 01.06.) | solvi-list-1 · Listicle | „spot the difference with a cervical pillow? It might be decent for sleeping on your back, but look at this cap when you're on…" |
  | [172504962](https://app.gethookd.ai/share/ad/172504962?signature=7ab505d2988071e368122f61c4ee5c248006f0c2b441198cbaac7bc8fd52807e) | Mellow Sleep Cloud Pillow | aktiv | 34 T | wp-adv-2 · Advertorial | Titel „Pillow That Ends Side Sleep Strain" · „Built for real people, not perfect sleepers…" |
  | [107155630](https://app.gethookd.ai/share/ad/107155630?signature=6686b28ae04cdf7abea5fe0755fd871810d08627f77a2d44560242265d3e6314) | MarshMellow Comforter | aktiv | 118 T | products/marshmellow-comforter · PDP | Titel „The World's Fluffiest Comforter" · „People can't believe how thick this comforter is. It's literally double-stuffed and looks unreal in person…" |
- **Warum:** Größtes Persona-Netz im Bettwaren-Bereich, Experten- und Ich-Story-Muster. Die Bettdecke (MarshMellow) fährt Mellow allerdings nur über PDP bzw. eine Landing ohne Native-Story. Für Kissen sehr nah an PillowDaddy, für unsere Angles nur bedingt neu.

### K9 · FluffCo (Hotel-Kissen und -Bettwaren) · Score 7
- **brand_ids** FluffCo 47695 (951 aktive Ads auf try.fluff.co, gesamt 961), Molly Simpson 6971966 (104), Sharon Rossi 10010233 (77), The Sleep Lab 6971968 (32), Daily Culture Trends 11282084 (29), Airbnb Host Community 11282082 (27) → 6 Seiten
- **Domain** try.fluff.co (`/adv-8-reasons-v2c`) · **Kategorie** Bettwaren · **Markt** US
- **Native-Format:** Listicle-Advertorial „8 Ways This Award Winning Pillow Helped +1 Million People To Fix Their Sleep" („I'm 58. My old pillow felt fine at bedtime and flat by 3AM…" – Jennifer Hayes; „Same suppliers as luxury hotels"; 66 % OFF; 30-Day Money Back). Laut aggregate: advertorial 804, landing 44.
- **Belege:**
  | Ad-ID | Status | Laufzeit | Typ | Hook wörtlich |
  |---|---|---|---|---|
  | [120530139](https://app.gethookd.ai/share/ad/120530139?signature=ef502e12f0ee6fa1da90f716307cb623a60e017b449cf4785aa25eba04a16da5) | aktiv | 91 T, 5 Varianten | DCO → Advertorial | Titel „Wake Up Without The Crick" · „Snoring isn't just annoying. It's separating couples into different bedrooms. The fix isn't a mouth guard or surgery. It's pi[llows]…" · Bild „4 FOR THE PRICE OF 1 / Same supplier as the Four Seasons / NOW $69 / ENDS TODAY!" |
  | [120530182](https://app.gethookd.ai/share/ad/120530182?signature=90311b25cb19fe29dcd4b9f832558bbba7f99531f19212f8e148334af1a62e79) | aktiv | 90 T | Bild → Advertorial | Titel „Why Your Pillows Keep Failing You" · „You've bought every pillow Target sells. Memory foam, cooling gel, bamboo. They all go flat. They all betray your neck eventu[ally]…" |
  | [129326906](https://app.gethookd.ai/share/ad/129326906?signature=762055a5e6783b94cf46499ccc725faba06a5e6868d41a928e7a60bd89ccb872) | inaktiv | 54 T | Bild → Advertorial | Titel „8 Reasons For Luxury Sleep \| FluffCo" · „I stole a pillow from a hotel in Maui last summer. I'm not proud of it. The general manager wrote me a letter three weeks lat[er]…" |
  | [170560325](https://app.gethookd.ai/share/ad/170560325?signature=99da0aa70ad4650d4913cda6a5e98d8cf76ebfbf0aaa25303831ea8553b3600c) | aktiv | 37 T | Bild → Advertorial | Titel „Sleep Like A Five Star Hotel For $69" · „The pillow you sleep on at five star hotels has a $200 price tag in the gift shop. We went directly to the same suppliers and…" |
- **Warum:** Ein Advertorial trägt fast das ganze Konto. „Hotel-Qualität" und „Hotel-Diebstahl-Story" lassen sich gut auf eine Decke übertragen (Hotel = frisch gewaschen, kein Bezug-Gefummel).

### K10 · Ryer (DE, Polster-/Matratzen-Nassreiniger) + provergleich.com · Score 7
- **brand_ids** Reinigungstipps für Zuhause 7199496 (140 aktiv auf provergleich.com), Anika Schmidt 7199495 (132), Ryer 5345283 (125; gesamt 917 aktiv), Angebote für Mamas 7199497 (123), Daniel Weber 7526090 (50), Auto Hacks & Pflege 7526091 (36), Ryer Deutschland 7526084 (25), RYER Germany 7526085 (18) → **8 Seiten, ~650 aktive Ads** auf der Advertorial-Domain
- **Domain** ryer.de + provergleich.com (`/adv1`, `/adv2`, `/adv3`, `/adv5`, `/adv13-b`, `/adv-test-1`, `/5-gruende-wassermechanism`) · **Kategorie** Haushalt/Allergie (Milben in Matratze und Sofa) · **Markt** DE/AT
- **Native-Formate:** Mama-Ich-Story-Advertorial („Gesponserter Beitrag … Der schockierende Moment, als dieses günstige Gerät jahrealten Dreck aus meinem Sofa geholt hat" – Von Marta Löffel, Mama von zwei; „In einer durchschnittlichen Matratze leben zwischen 100.000 und 10 Millionen Hausstaubmilben"), Listicle „5 Gründe, warum 50.000 Deutsche auf Nassreinigung umsteigen." (mit eingebauten Fake-Social-Kommentaren), animierte Milben-Videos.
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | LP / Typ | Hook wörtlich |
  |---|---|---|---|---|---|
  | [111737379](https://app.gethookd.ai/share/ad/111737379?signature=4d616e456c750e2c496f4e36fc21ac8884d77c1ac0729da6b9febd18f237de15) | Ryer | aktiv | 124 T | ryer.de/products/plus · PDP | Titel „Milben fressen dich jede Nacht – ekelhaft!" · „Wir sind Millionen Milben. Und dein Bett ist unser Zuhause! Wir fressen deine Hautschuppen – jede Nacht. Und wir werden imme[r mehr]…" (sprechende 3D-Milben) |
  | [145503635](https://app.gethookd.ai/share/ad/145503635?signature=cba4b57aea9d8b9c26f49594d9a0f6313b7d280099feecaa5b1a8ef7dca5e436) | Anika Schmidt | aktiv | 55 T · 9 Varianten | provergleich.com/adv13-b · Advertorial | Titel „Seit Jahren schlecht geschlafen" · „Ich schlafe seit Jahren schlecht, bis das bei mir angekommen ist. Morgens unausgeruht aufwachen. Ich dachte einfach, das gehö[rt]…" |
  | [185267659](https://app.gethookd.ai/share/ad/185267659?signature=84fccf12e06f13adfa6cfedbe06d5b635365aa7a067fedcbabf62070ee3395dd) | Auto Hacks & Pflege | aktiv | 11 T | provergleich.com/5-gruende-wassermechanism · Listicle | „Sorry an alle, die den RYER vor dem Herbst-Sale gekauft haben. Ja, es stimmt: Der RYER Plus holt Milben, Schimmel und Bakter[ien]…" |
  | [200979074](https://app.gethookd.ai/share/ad/200979074?signature=13fc270eb733ee56b804a8456de0c40464b5199fa7e9492b1f50de772356e448) | Ryer | aktiv | 3 T, 6 Varianten | provergleich.com/adv2 · Advertorial | „Dieses Teil hat mir gezeigt, welchen tiefen Dreck mein 600-€-Staubsauger jahrelang übersehen hat…" |
- **Warum:** Deutsche Vorlage für Angle A (Milben fressen Hautschuppen im Bett), mit einer eigenen „Vergleichs"-Domain als Advertorial-Host. Die Ad mit den sprechenden Milben ist ein sehr starker Hygiene-Hook für Video.

### K11 · The Sleep Edit → Silvery Restcool Cooling Comforter · Score 7
- **brand_id** The Sleep Edit Guide 7531501 (95 aktiv) · **Domain** thesleepedit.co (`/pages/best-cooling-comforter-2026-3822`) → mysilvery.com · **Kategorie** Bettwaren (Bettdecke)/Wechseljahre · **Markt** US
- **Native-Format:** Vergleichs-Advertorial mit Arzt („Sponsored Content … We Tested the 5 Most-Hyped Cooling Comforters of 2026. Only One Was Still Working by 4am." – Dr. Christian Fernandez, MD, Sleep & Wellness Expert; Mechanismus: Körperkerntemperatur muss um 1–3°F sinken, „hormonal changes that turn your internal thermostat into a wildfire"). Laut aggregate: advertorial 11.
- **Belege:**
  | Ad-ID | Status | Laufzeit | Hook / Bildtext wörtlich |
  |---|---|---|---|
  | [185341953](https://app.gethookd.ai/share/ad/185341953?signature=16fdb248195b961f8f7705f48469e902e4a3293dcb77edd055151962b12851ac) | aktiv | 22 T | Titel „🏆 Top 5 Cooling Comforters of 2026 Tested" · „🚨 Read this before you buy a cooling comforter. A sleep expert just tested the top 5 cooling comforter brands of 2026, and t[he]…" · Bild „PRODUCT TEST / Waking Up Drenched In Sweat? We tested 5 cooling comforters, and the cheapest one won." |
  | [200147638](https://app.gethookd.ai/share/ad/200147638?signature=4b119cd6f7a9902fd736fc4fca8e3e7b65ecc370b3388527d6b3dc33880dcd8e) | aktiv | 6 T | Bild „We put 5 cooling comforters to the test. The cheapest one beat every $200+ brand on the list. … Tap here to find out which won." |
- **Warum:** Einziges Vergleichs-Advertorial („Top 5") im Bettdecken-Bereich mit Wechseljahre-Begründung. Einordnung „Kandidat", weil die Laufzeit erst 22 Tage beträgt.

### K12 · Clarifion (US-Original des Milben-Ionisator-Playbooks) · Score 7
- **brand_ids** Clarifion 3202 (60 aktiv auf Domain), Homeowners vs. Dust Mites 44651 (44), Air Quality Secrets 44656 (8), The Home Guru 3204 (6), Home Diva 52824 (6), Homeowners vs. Mold 44658 (2) → 6 Seiten
- **Domain** about.clarifion.com · **Kategorie** Allergie · **Markt** US · Laut aggregate: advertorial 70
- **Native-Format:** News-Advertorial („Advertorial – How This Innovative Device Is Helping Thousands with Airborne Dust, Particulates, etc." – „A small genius startup in California called Clarifion quietly built a breakthrough alternative") plus Persona-Seiten im Stil „Homeowners vs. …".
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | Hook / Bildtext wörtlich |
  |---|---|---|---|---|
  | [92196867](https://app.gethookd.ai/share/ad/92196867?signature=0a7064a7721e4fdeb097843a9ae0431ab1918bf40e797e58112daaeb43debf29) | Homeowners vs. Dust Mites | inaktiv | 93 T (bis 16.07.) | Titel „Eliminates Dust Mites In Your Home? (MUST READ)" · „2 Years of Dust Mites… GONE IN DAYS??" · Bild: Gummiwürmer mit Milben „Most people don't know this trick keeps dust mites away, but did you know… more" |
  | [167852423](https://app.gethookd.ai/share/ad/167852423?signature=551c51e0227c1a58725de12d2707566b0393a1379cd8228305bb9616e43e1f18) | Homeowners vs. Dust Mites | aktiv | 42 T | Titel „Clears Dust Mites - Save 46% OFF with Bundle" · „🍃 Discover how this smart device turned a dust mite-filled room into a fresh air paradise without any hassle in almost days!" · Overlay „This is how I got rid of my dust mite allergy symptoms" |
  | [149611857](https://app.gethookd.ai/share/ad/149611857?signature=250d1afa36834d1456d8daa5984dac473696d1457300c7faa7a4f37db683c1d2) | The Home Guru | inaktiv | 50 T | „Say goodbye to dust mites and hello to fresher air with Clarifion™ Air Ionizer 🌬️" |
- **Warum:** Die Vorlage hinter K2. Zum Vergleich US gegen UK nützlich; für uns ist K2 (UK) wichtiger.

### K13 · AeroPure (AU, Milben-Ionisator) · Score 6
- **brand_ids** AeroPure 1511778 (244 aktiv), Fresh Air Finds 1987586 (97), Dust Mite Solutions 11131855 (21) · **Domain** aeropure.com.au · **Kategorie** Allergie · **Markt** AU (englisch) · Laut aggregate: advertorial 216, listicle 7
- **Native-Formate:** Experten-Listicle („Home Health Insider – 10 Reasons Why Homeowners Are Switching to AeroPure to Eliminate Dust & Dust Mites" bzw. „Why Thousands of Australian Homeowners are Switching…" – By Dr. Emily Carter, Clinical Allergy Researcher & Indoor Air Quality Specialist; „Every dust mite produces around 20 fecal pellets per day… Der p1… you're inhaling these particles all night long").
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | LP / Typ | Hook / Bildtext wörtlich |
  |---|---|---|---|---|---|
  | [80217310](https://app.gethookd.ai/share/ad/80217310?signature=11ebd6dc888cedd13fc1c745ec2b898040284a5bfe5988ba23b8eda8911d4359) | Fresh Air Finds | inaktiv | **230 T** (bis 07.10.) | /pages/10-reasons · Listicle | Titel „Dust Mites in Your Home?" · „🏠 8 out of 10 of homes have dust mite waste floating in the air, most people never realize *until they get sick*" |
  | [115020517](https://app.gethookd.ai/share/ad/115020517?signature=076393e95d779585040dc9dc71b8ac98d6de9b97135dc94416820f249a505b7c) | AeroPure | inaktiv | 88 T | /pages/particles-adv1 · Advertorial | Titel „Clean air. Clean home." · „Most people are solving dust the wrong way…" |
  | [142759176](https://app.gethookd.ai/share/ad/142759176?signature=6ffda3c58132d237899a2f014e440fd19879a0e36f47c433e46f60a5bf7fb69e) | AeroPure | aktiv | 60 T | /pages/particles-adv1 · Advertorial | Titel „Reduces Dust - Save 45% OFF with Bundle" · „Dust back on your shelves the morning after you cleaned them?" |
  | [174476297](https://app.gethookd.ai/share/ad/174476297?signature=169190f8f4f079c670ea28a14810c79a97f92fb19c62afb8232acc7c4f5d1579) | Fresh Air Finds | aktiv | 30 T | /pages/particles-adv1 · Advertorial | „🏠 You keep your home spotless. So why do you still wake up congested, sneezy, and exhausted every morning?" · Bild „YOUR BEDROOM AIR HAS MILLIONS OF INVISIBLE MOULD SPORES … Clinicians' Choice - Verified / Over 25,000+ Homes Trust AeroPure" |
- **Warum:** Gleiches Playbook wie K2/K12, mit dem stärksten Bezug auf Matratze und Kissen und einer Arzt-Persona als Autorin.

### K14 · Healthy Essential (Waschmittelblätter-Vergleichs-Listicle) · Score 6
- **brand_ids** The Healthy Cleaning Mom 81274 (52 aktiv), Healthy Cleaning Reviews 272689 (50), früher Health Essential Reviews 2569 · **Domain** healthy-essential.co (`/pages/he-article-laundry-topfive-researcher-uk|-ca|-usa`) · **Kategorie** Haushalt · **Markt** US, CA, **GB** · Laut aggregate: listicle 86
- **Native-Format:** „Sponsored Advertising Post – 2026's Top 4 Eco-Friendly Laundry Detergent Sheets, Available in the UK" (Redaktion hat „18 different laundry detergent sheets from 14 different brands" getestet).
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | Hook wörtlich |
  |---|---|---|---|---|
  | [75702](https://app.gethookd.ai/share/ad/75702?signature=11199bd438844b59c155b25fd546ae8e95c10ccc5e9b0747611a1d28f9239ef5) | Health Essential Reviews | inaktiv | **954 T** (27.09.2023–07.05.2026) | Titel „Top 5 Laundry Detergent Sheets of 2023 Revealed" · „Top five laundry detergent sheets of 2023, tested and ranked. Red wine stains are a nightmare…" |
  | [162394458](https://app.gethookd.ai/share/ad/162394458?signature=9a4c4c925961c890cdeacc3618652cb24e956742c5c64451057a6bbb71042ea3) | Healthy Cleaning Reviews | aktiv (GB) | 44 T | Titel „The Dirty Truth About Laundry Sheets" · „Created for convenience, these detergent sheets remove stains and odors without the usual mess or measuring." |
  | [162394748](https://app.gethookd.ai/share/ad/162394748?signature=40de2e1f5a15a97c2288f56d90e7dd72242e470995f9089dd34da0e45dd2dcc2) | Healthy Cleaning Reviews | aktiv | 43 T | dto. (CA-Seite) |
- **Warum:** Das langlebigste Vergleichs-Listicle-Format im Haushaltsbereich, mit eigener UK-Version. Vorlage für eine „Best coverless/washable duvets UK 2026 – we tested 5"-Seite.

### K15 · Fine Foams (AU, Musselin-Decke) · Score 6
- **brand_id** 7210101 (175 aktiv) · **Domain** finefoams.com.au (`/pages/5-reason-why-soothing-muslin-blanket`) · **Kategorie** Bettwaren · **Markt** AU · Laut aggregate: listicle 40
- **Native-Format:** Gründer-Listicle „5 ways this muslin blanket will upgrade your sleep." (Dhiren · Fine Foams founder), Vergleichstabelle „A DOONA / A SHEET ALONE / [Muslin]" („At 2am: Too hot, it gets kicked off / Not warm enough"; „Sharing the bed: Tug of war / Everyone loses"); Ad-Bild in Native-Typo „Two people. One doona. Nobody wins."
- **Belege:**
  | Ad-ID | Status | Laufzeit | Hook wörtlich |
  |---|---|---|---|
  | [170770704](https://app.gethookd.ai/share/ad/170770704?signature=6bf3c5fb5089dda1549fac65e68c2062dce326c55e97df6ea248fb0b1095176a) | aktiv | 41 T | Titel „The nightly blanket war" · „One of you runs hot. One of you runs cold. And every night the same silent negotiation: doona on, doona off, one leg out, cov[ers]…" |
  | [184419371](https://app.gethookd.ai/share/ad/184419371?signature=8f04834d589a0fe790a987d374621370eb235efa8fe17cb017e6c0b1ab358346) | aktiv | 14 T | Titel „Not a Sheet. Not a Doona." · „If a sheet's never enough but a doona's always too hot, this is for you. Doonas overheat. Sheets underdeliver…" |
  | [188063413](https://app.gethookd.ai/share/ad/188063413?signature=91aabd892814a3949d1796fa24268a668b82014d791fab400d0acbedeb7a6bd5) | aktiv | 9 T | Titel „A sheet's not enough. A doona's too much" · „Same night, three beds. The bed with just a sheet is cold by 4am…" |
- **Warum:** Spricht im Commonwealth-Wortschatz („doona" in AU entspricht „duvet" in UK) über Bettdecken-Frust und Temperatur. Native-Typo-Bilder sind leicht nachzubauen. Einordnung „Kandidat" (41 Tage).

### K16 · X-All Waschmaschinenreiniger („Home Cleaning Pros") · Score 6
- **brand_id** Home Cleaning Pros 4465551 (222 aktiv) · **Domain** xwm.x-all.com (`/xwm-sick-vl-t5`) · **Kategorie** Haushalt/Hygiene · **Markt** US
- **Native-Format:** Ich-Story-Advertorial im News-Look mit Aufrufzähler („Is Your Washing Machine Making You Sick? … HALEY WILLIAMS · 290,153 views · ◉693 Live Viewers": „I'm a 39 year old woman, and I do laundry at my mom's house…" → **Tochter-Mutter-Konstellation**).
- **Belege:**
  | Ad-ID | Status | Laufzeit | Hook wörtlich |
  |---|---|---|---|
  | [94819002](https://app.gethookd.ai/share/ad/94819002?signature=11f034106ae0cb060df83d138b009d675d079c45f418949e3a0b6ae26957e502) | inaktiv | **235 T** (22.12.2025–13.08.2026) | Titel „How to Clean a Washing Machine" · „Did you know washing machines need to be cleaned every 3 months or they can build up with toxic mold, and bacteria's like E.C[oli]…" |
  | [94819000](https://app.gethookd.ai/share/ad/94819000?signature=b74f9e6e09ff83e3bd6e64beb5b3ae80da0ad33a1f5d940921dd02a213089401) | inaktiv | 224 T | dto. |
- **Warum:** Langläufer mit Hygiene-Mechanismus (Schimmel/Bakterien in Wäsche) und einer Tochter-Mutter-Szene als Rahmen. Brauchbar für Angle A + D.

### K17 · Swarva (Altersgeruch / „Nonenal") · Score 6
- **brand_id** 197895 (67 aktiv) · **Domain** swarva.com (`/pages/5-reaons-why-1`) · **Kategorie** Hygiene · **Markt** US, GB
- **Native-Format:** Arzt-Advertorial („Advertorial – 5 Reasons This Japanese Secret Eliminates Aging Body Odor (Before Anyone Notices)" – By Dr. James Mitchell; „After age 40, your body begins producing a compound called nonenal… you cannot smell it on yourself… your friends, your children, your grandchildren — they notice. And almost none of them will tell you.").
- **Belege:**
  | Ad-ID | Status | Laufzeit | Hook wörtlich |
  |---|---|---|---|
  | [76171252](https://app.gethookd.ai/share/ad/76171252?signature=8408f3922a511841796045ccac4b4baffed888478e1c8539474566672c451fb7) | inaktiv | **165 T** (01.02.–15.07.) | Titel „What Ages Us More Than Sun Damage" · „There's something that happens typically after 70 where no matter how much you wash your clothes, they start to carry this sm[ell]…" |
  | [184315039](https://app.gethookd.ai/share/ad/184315039?signature=765f78659c702aab202cfb76e7c3d67639355bc88a85412fb3fd97fc9abde846) | aktiv (GB) | 14 T | dto. |
- **Warum:** Hygiene-Scham bei Älteren, die die Kinder bemerken („they notice"). Das ist die emotionale Brücke für Angle D (Tochter merkt, dass Mutters Bettzeug nicht mehr frisch ist), wird aber nur vorsichtig einsetzbar sein.

### K18 · Uproot Clean (Waschmaschinenreiniger) · Score 5
- **brand_id** 631 (1.914 aktiv) · **Domain** uprootclean.com (`/pages/washing-machine-cleaner-pro-wmt007-l3-3`) · **Kategorie** Haushalt · **Markt** US
- **Native-Format:** Ich-Story-Advertorial („Is Pet Hair And Bacteria Destroying Your Washing Machine - Here's How You Can Tell" – Posted By Mary Lee, Opa als Experte).
- **Beleg:** [85841180](https://app.gethookd.ai/share/ad/85841180?signature=99a36356c0ca7e1c835e523b1b8e0e635ab12f9f915f5f14c1e0b5a349104650) · inaktiv · 120 T (18.03.–15.07.) · „This one trick from my grandpa made my washer smell brand new. For months, I couldn't figure out why everything, towels, t-sh[irts]…"
- **Warum:** Großvater-als-Experte-Muster, Hygiene beim Waschen. Nur Nebenvorlage.

### K19 · Splash Blanket (wasserdichte Decke) · Score 5
- **brand_id** 28278 · **Domain** splashblanket.com (+ .co.uk) · **Kategorie** Bettwaren · **Markt** US/UK
- **Native-Format:** Listicle „7 Reasons People Are Switching to This Blanket." („150,000+ Customers").
- **Belege:** [117142108](https://app.gethookd.ai/share/ad/117142108?signature=26fe307e87e0c1615b00b3fa078b2e92d0d85bee9a2369d3229c005caf717c99) inaktiv 74 T „“This blanket changed my life.” Join thousands who have ditched towels and protectors for something that actually works." · [167390963](https://app.gethookd.ai/share/ad/167390963?signature=53b584fef29c76477c38812751c6c4d1b8034ef4f240ce5dcf7446d7544c5b5b) aktiv 42 T „Goodbye wet patch 💦 Keep your bed dry and fun flowing with Splash Blanket™"
- **Warum:** Decken-Listicle mit UK-Domain. Die Positionierung (Intimität) passt nicht zu uns, die Listicle-Struktur schon.

### K20 · Home & Garden Trend (Matratzentopper) · Score 5
- **brand_id** 2090 (304 aktiv) · **Domain** garden-trend.store (`/pages/5-ways-your-old-mattress-is-destroying-your-sleep`, `/pages/sleep-scientists-reveal-why-you-have-back-pain-every-morning`) · **Kategorie** Bettwaren · **Markt** US
- **Beleg:** [119287941](https://app.gethookd.ai/share/ad/119287941?signature=40c1f60e24058d0af86c0b4eb84c6bbd181111bfefd6929e04da94cd35fbbb6c) · aktiv · 89 T · Advertorial · Titel „50% OFF + Free Shipping" · „If you struggle with any sort of lower back pain, spine pain, pressure point pain, hip pain, anything like that, definitely g[et]…"
- **Warum:** Schlagzeilen-Muster „5 Ways Your Old Mattress Is Destroying Your Sleep" lässt sich direkt auf „5 Ways Your Old Duvet…" übertragen.

### K21 · Top 5 Best Mattresses UK (Vergleichsseite von Emma Sleep) · Score 5
- **brand_id** 504951 · **Domain** top5bestmattress.co.uk · **Kategorie** Bettwaren · **Markt** GB
- **Format:** Marken-eigene Vergleichsseite („This comparison website … is operated by DIBmat GmbH, a wholly owned subsidiary of Emma Sleep GmbH").
- **Belege:** [127296495](https://app.gethookd.ai/share/ad/127296495?signature=2228420e0d4302766eeb3920df769d579fe8473fda025bfcbfaf115d4fb24273) inaktiv (Ende 08.08.) „Tired of overthinking every purchase? Top 5 by Emma does the hard work for you. No endless research…" · [123223120](https://app.gethookd.ai/share/ad/123223120?signature=e284f016e43573af82caceec240803bbaed2b4aa3faa53519a877d6480831496) inaktiv „Sleep better and save bigger.Plus an extra 5% off with code TOP5UK…" (GetHookd zeigt 82–94 „days_active", das Ende-Datum 08.08. ergibt aber nur ca. 20–32 Tage → Laufzeit unsicher)
- **Warum:** Zeigt, dass der größte UK-Bettwarenanbieter Native über eine eigene Vergleichsseite fährt (Offenlegung im Footer).

### K22 · Uk Sleep Forum (Airvex, Schnarchen/Apnoe) · Score 4
- **brand_id** 11235315 (616 aktiv) · **Domain** airvex.shop (PDP) · **Kategorie** Schlaf · **Markt** GB
- **Format:** Lange Native-Text-Story-Ads mit „echten" Handyfotos (dreckige CPAP-Maske, fleckige Matratze), Link aber direkt auf die PDP.
- **Belege:** [178964742](https://app.gethookd.ai/share/ad/178964742?signature=f9370713da94347904bc2404f61d1e2a28ba61b2a40c83364772bc9db8faeec1) aktiv 33 T „My wife's snoring started in menopause. I haven't slept a full night in 4 years. Her GP said it would settle." · [178964447](https://app.gethookd.ai/share/ad/178964447?signature=7b48bb1db1b2b785a3f3ca56cfe44cc14eab52bddee07b4c22992885cf202b1a) aktiv 44 T „I'm an HGV driver with sleep apnoea. I couldn't wear the CPAP mask. The DVLA took my licence."
- **Warum:** UK-typische Native-Text-Ads (GP, DVLA, Boots-Kassenzettel im Bild). Die LP ist aber eine PDP, deshalb nur als Vorlage für den Ad-Stil brauchbar.

### Weitere geprüfte, aber schwächere Fundstellen (nicht als Kandidat gewertet)
- **Blissy** (7085041): „🚨 Is Your Pillow Making You Sick?" ([168753041](https://app.gethookd.ai/share/ad/168753041?signature=d34fc84258d46be2fc6482bb0462ddf63a2166e8e9c5768a2f69f882f5a913f1), aktiv 39 T, Hook „Did you know most memory foam pillows are made from the same chemicals as gasoline? 😱…"). Die LP `latest.blissy.com/pillow-reasons` leitet heute auf eine Checkout-Verkaufsseite um, nicht mehr auf ein Listicle.
- **Nourial** (5539254, 674 aktiv): Knie-Kissen-Advertorials (115280781 121 T, 103916523 130 T), Hook „If you're a side sleeper who wakes up every single night grabbing your hip, flips from side to side like a rotisserie chicken…". Seitenschläfer-Kissen, für unsere Angles kaum relevant.
- **Wechseljahre und Ich** (4411451, DE): Kollagen-Advertorial `myhealth-lifestyle.com/5-gruende-warum-250000-frauen-in-der-menopause…`, [93282658](https://app.gethookd.ai/share/ad/93282658?signature=a05fc8962ad6c4621ba3fb0860c52622422c8d11883e7f733ddacb8e7dcbd4fe) aktiv 225 T, Spend $2.001–5.000. DE-Beleg dafür, dass Wechseljahre-Listicles laufen, aber kein Bettwarenprodukt.
- **Wilderglow / Kelly's Menopause Blog** (4479958): 98407829, 119 T, „Please STOP increasing your HRT dose…" (Supplement).
- **VegOut Magazine** (50402): Eucalypso-Laken-Review „I Tried Eucalypso Sheets – Are They Worth the Hype?" (127754306); die Laufzeit ist unklar, GetHookd zeigt „inaktiv" mit Ende 09.08.
- **Gohomie UK** (38904): News-Funnel für Waschmaschinentabs (`funnel.gohomie.co.uk/funnel/news-washing-machine-cleaning-tablets`), nur 33–36 Tage und schon im März beendet → vor dem Zeitfenster.
- **Direkter DE-Wettbewerb ohne Natives (wichtig als Kontrast):** HappyBed/thehappybed.com (5350729, 338 Ads): ausschließlich PDP/Collection mit 2-für-1-Angeboten; OhMySwiss/Swiss Deals (7563513): PDP („Nie wieder am Bettbezug ziehen, wenden oder damit kämpfen.", 100–115 T); Paradies (7148697), Anfaru (5346835), Zelesta (5189960): PDP/Collection. → In DE setzt **nur MagicSplashy** Natives für die Decke ohne Bezug ein.

---

## 3. Wiederkehrende Muster über alle Kandidaten (für Agent 4)

1. **Persona-Netz → eine Presell-Domain.** UVLizer (6 Seiten), Plufl (17), GroundingWell (46), Mellow (≥ 50), Granny Blog (8), Ryer/provergleich (8), FluffCo (6), Clarifion (6), Eight Sleep (6). Die Seiten heißen entweder wie Menschen (Hannah Houg, Anika Schmidt, Mark Davis), wie Communities („Families vs. Dust Mites", „Homeowners vs. Mold", „Reinigungstipps für Zuhause", „Angebote für Mamas") oder wie Magazine („Wellness Today", „The Get Well", „Health insider").
2. **Drei Seitentypen dominieren:** (a) Listicle „X Reasons Why [Zielgruppe] Are Switching to…" (Clairu, AeroPure, GroundingWell, Down To Ground, FluffCo, Splash, Fine Foams, MagicSplashy-Frauenmagazin); (b) Ich-Story-Advertorial mit Tiefpunkt und Autor-Persona (Retired Nurse, Mama von zwei, Redakteur Daniel K., Emma Richardson); (c) Vergleichs-Listicle „We tested 5…" mit Arzt bzw. Redaktion (Silvery, Healthy Essential, Top 5 by Emma).
3. **Hygiene-Mechanismus ist immer gleich gebaut:** unsichtbar + Zahl + Ekel-Bild + „Every night": „Microscopic Poop / You can't see them. But you're breathing them in. Every night." · „Der p 1" · „3 million bacteria per square inch — more than a toilet seat" · „Wir fressen deine Hautschuppen – jede Nacht" · „100.000 und 10 Millionen Hausstaubmilben" in einer Matratze.
4. **Wechseljahre-Mechanismus:** Thermostat/Temperatur („drop its core temperature by 1 to 3°F", „thermostat into a wildfire", „Your Hot Flashes Aren't A Hormone Problem. They're A Thermostat Problem.") plus Paar-Konflikt („husband sleeping in the guest room", „Hot Flashes on My Side, Freezing on His", „Blanket Wars", „Two people. One doona. Nobody wins.").
5. **Beziehen-Mechanismus (bisher nur MagicSplashy):** Ritual-Beschreibung „Bezug ab, neuen drauf, Ecken suchen, alles verrutscht, nochmal von vorne. Jeden zweiten Sonntag dasselbe Ritual." plus Umdeutung „Es war nie normal. Es war nur Gewohnheit." plus Beweis „Das Beziehen war die häufigste Antwort" aus der Kundenumfrage.
6. **Belege und Angebote in den Seiten:** „As seen on/Bekannt aus" (Shark Tank, GMA, Bild der Frau, Focus, Stern, WELT), Zahlen-Social-Proof (17.000+, 40,000+, 150,000+, 1 Million), Countdown-Timer, „Limited stock", Bundle-Rabatt 45–66 %, Gratis-Zugabe (Kissenbezüge, Grounding-Matte), Garantie 30/40/100 Tage.
7. **Videos fürs Advertorial sind UGC, keine Studio-Produktion:** Plufl (Kommentar-Reply-Overlay), MagicSplashy (Ich-Story 57 s, Overlay „DAS WARS MIT BETTWÄSCHE WECHSELN!"), Down To Ground (Gründer), Ryer (animierte Milben).

---

## 4. Lücken / Einschränkungen (ehrlich)

- **`native_ads=true` taugt hier kaum:** Das Facet deckt nur frisch klassifizierte Ads ab (in GB 13 Treffer, die älteste mit 44 Tagen). Langläufer findet es nicht. Haupt-Suchweg war deshalb `page_type=advertorial,listicle`.
- **DE-Ads haben meist `page_type = null`.** Auch für provergleich.com und magicsplashy.de liefert `aggregate_ads` keine Buckets. Die DE-Kandidaten wurden deshalb über `language=de` + Query gefunden und die LP-Typen per Abruf der Seiten bestimmt.
- **Domain-Suche mit `sort_column=days_active` wird von GetHookd nicht unterstützt** („mixed_runtime_sort_unsupported"). Ersatz: Suche per `brand_id`.
- **Spend-Daten fehlen bei den meisten US-Ads** (`ad_spend_range_score_title = null`). Spend-Belege gibt es v. a. für EU-Ads (MagicSplashy, Wechseljahre und Ich).
- **Redirects ändern den LP-Typ:** getuvlizer.co.uk → tryclairo.co.uk; mellowsleep.com/pages/rp-001 → /pages/gu-ad-1 (Landing statt Listicle); latest.blissy.com/pillow-reasons → Checkout-Seite. Der in GetHookd gespeicherte `page_type` gilt für den Zeitpunkt der Indexierung.
- **Granny Blog / Mark Davis:** Mit `status=active` + Sortierung wurden alle Ads zurückgehalten (fehlender Brand-Sweep). Die Ads wurden deshalb ohne Statusfilter abgerufen. Die genaue Laufzeit der 760 Ads ist nicht belegt (Start ab 29.09.).
- **Transkripte:** In diesem Sweep wurde nur das MagicSplashy-Video 126012757 per `get_ad` transkribiert (liegt vollständig vor). Die übrigen Video-Hooks sind die von GetHookd gelieferten ersten ca. 125 Zeichen. Volle Transkripte der Top-3 je Marke sind Aufgabe des Transkript-Schritts von Agent 3.
- Die abgerufenen LP-Texte (mobil) liegen unter `/tmp/claude-0/-home-user-paw-friends-support-bot-/42d75a1d-7d37-5001-977b-a9dade5cafb7/scratchpad/natives/a3/lp/` (z. B. `uvlizer_adv.txt`, `magicsplashy_frauen.txt`, `magicsplashy_umfrage.txt`, `magicsplashy_gesund.txt`, `plufl_adv.txt`, `grannyblog.txt`, `getwell_8s.txt`, `sleepedit.txt`, `provergleich13.txt`, `xwm.txt`, `swarva.txt`), daneben Screenshots (`*.png`) und Linklisten.
