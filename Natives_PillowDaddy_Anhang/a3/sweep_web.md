# Agent 3 – Sweep "Web / Google" + Zusammenführung aller drei Suchwege

Stand: 08.10.2026, ca. 11:20–11:40 UTC (Wiederaufnahme nach Abbruch durch Nutzungslimit).
Quellen: WebSearch (Google-Index, US), Seitenabruf per curl (mobiler User-Agent; Rohdateien `a3/web/raw/*.html`), Gegenprüfung in GetHooked (`get_domain_advertisers`, `aggregate_ads(page_type)`, `search_ads(brand_id|landing_page_domain)`).
Rohnotizen: `a3/_notes_web.md`. Die beiden anderen Suchwege: `a3/sweep_gethooked_native.md` (Native-Filter) und `a3/sweep_gethooked_hooks.md` (Hook-Begriffe).
PillowDaddy und seine Persona-Seiten sind bewusst ausgeschlossen (Agent 1).

---

## 0. Kurzfazit Web-Suchweg

1. **Google findet Advertorials kaum.** Presell-Seiten sind fast immer `noindex`. 12 gezielte Abfragen (u. a. „advertorial“ / „reasons why … switching“ kombiniert mit duvet, comforter, sheets, pillow, menopause, night sweats, dust mites, laundry; DE: „Anzeige“ + Milben/Bettdecke/Wechseljahre) brachten nur zwei echte Treffer: **rest.com/pages/menopause-*** und **thebreeze.earthbreeze.com/pages/***. Der Rest waren Ratgeber, Testberichte, Hersteller-Blogs und Spam-Listen.
2. **Neu aus diesem Suchweg (verifiziert):**
   - **Rest / Evercool Comforter (US):** eine *Bettdecke* mit eigenen Wechseljahre-Listicles („6 Reasons Women In Menopause Are Switching To The Evercool® Comforter“, „10 Reasons Women Over 40 with Night Sweats Switched…“). Dazu kommen eine Persona-Seite „Hot Sleeper Journal“ (Hotel-Diebstahl-Ich-Story) und eine UGC-Wechseljahre-Ad mit **278 Tagen** Laufzeit. Das ist die nächstliegende US-Vorlage für Angle B mit genau unserer Produktgattung.
   - **Miracle Made (US, Silber-Bettwäsche):** Listicle „6 Reasons Americans are Switching to these NASA-Inspired Sheets“ mit Nachtschweiß- und Bakterien-Mechanismus („more bacteria than a toilet seat“). Mehrere DCO-Varianten sind **102 Tage** aktiv. Zusammen mit dem Persona-Netz *The Granny Blog* (~2.390 Ads) ist das das stärkste Hygiene-Vorbild bei Bettwäsche.
   - **Earth Breeze (US, Waschmittelblätter):** Advertorial-Subdomain mit 4 Seiten und ~326 aktiven Ads, darunter die Ich-Story „I stopped washing my bed sheets and my life is so much better. Here’s why:“ (Hygiene im Bettlaken, Schwarzlicht-Beweis).
   - **Clean People (US, Waschmittel):** Fake-Blog „Women's Fitness & Style“ mit 10 Persona-Seiten (Dr. Rose MD, Nontoxic Mom …) und ~723 aktiven Ads. Das Format ist ein Vergleichs-Listicle „5 Best Laundry Detergents … According to a Dermatologist“, die Laufzeiten liegen bei 114–169 Tagen.
3. **Kontrollgruppe bestätigt die Chance:** 17 bekannte Bettwaren-/Schlafmarken (Buffy, Slumber Cloud, Woolroom, Beddy's, BedJet, Simba, Panda, Fine Bedding, Hush, Dagsmejan, Cozy Earth, Manta, Tru Earth, Kally, Promeed, Brolly, Calming Blankets) fahren laut GetHooked **keine** Advertorials oder Listicles, nur Homepage, Collection oder PDP. Auch der direkte UK-Wettbewerber **Night Lark Coverless Duvet** (Fine Bedding Co., 56 aktive Ads) wirbt nur mit PDP/Collection und einer Kinder-Kampagne („BEDDING MADE EASY“). Die Suche „hot flushes“ (UK-Schreibweise) mit Advertorial/Listicle-Filter in GB ergab keinen einzigen Bettwaren-Treffer.

---

## 1. Suchprotokoll Web

| # | Abfrage (Google) | Ergebnis |
|---|---|---|
| 1 | "advertorial" coverless duvet washable "reasons why" | nur Ratgeber (Homes & Gardens, Ideal Home, Mumsnet, Fine Bedding Blog) |
| 2 | "reasons why" women switching cooling comforter menopause | **rest.com/pages/menopause-science-v4/v6, menopause-proof-v4/v7/v8** → Treffer W1 |
| 3 | "advertorial" menopause cooling sheets "hot flashes" | Hersteller-Blogs (Bedgear, Sheex), Spam-Listen |
| 4 | "reasons why" thousands switching pillow dust mites UK | Presse/Umfragen (Allergy UK, Silentnight), kein Advertorial |
| 5 | "reasons why" switching duvet night sweats/hot flushes UK | Händler-Blogs |
| 6 | "Advertorial" sheets night sweats "I tried" | kein Advertorial |
| 7 | "advertorial" "dust mites" "your mattress" reasons | Ratgeber |
| 8 | DE: "Warum" Frauen Bettdecke Wechseljahre Advertorial | Ratgeber, alte Apotheken-Anzeige (2013) |
| 9 | "Brits are" switching duvet hotel quality | Presse |
| 10 | "is your pillow making you sick" / "your duvet is dirtier" | Ratgeber (goodtoknow, AOL) |
| 11 | Chillow menopause cooling pillow advertorial | Forum/Hersteller |
| 12 | "advertorial" laundry sheets "reasons why" earth breeze/tru earth | **thebreeze.earthbreeze.com/pages/…** → Treffer W2 |
| 13 | weighted/cooling blanket, menopause pajamas, silk/copper pillowcase, DE "Anzeige" Milben, "reasons hot sleepers are switching", "women over 50", allergy sufferers switching, Top-5-Duvet-UK-Vergleichsseiten, adlibrary/motionapp | keine weiteren Advertorial-URLs |

Danach habe ich nach Marken gesucht: bekannte Marken in GetHooked nachgeschlagen (`search_brands` → `aggregate_ads(page_type)` je Domain), siehe Abschnitt 3. Daraus kam Treffer W3 (Miracle Brand). Treffer W4 (Clean People) fiel bei der Gegenprüfung an (Persona-Ad „Dr. Rose, MD“ in der Abfrage „pillowcase“ mit Filter advertorial/listicle). Danach habe ich die Landingpage abgerufen und die Advertiser der Domain abgefragt.

---

## 2. Neue Kandidaten aus dem Web-Suchweg (Belege)

### W1 · Rest – Evercool® Cooling Comforter · Score 8 · schlaf_bettwaren / wechseljahre · US
- **brand_ids:** Rest 28140 (589 aktive Ads auf rest.com), **Hot Sleeper Journal 7097606** (11, Persona-Seite seit 04.09.), Creator-Seiten emmvuu 10993508, Laura On A Mission 11625816, AJ Core Performance 28387891, Caroline Zawadzki 28387893 → 6 Seiten; Domain gesamt 656 Ads (568 aktiv). Domains rest.com, restduvet.com, au.rest.com.
- **Web-verifizierte Listicles (curl 11:24):**
  - `rest.com/pages/menopause-science-v6`: H1 „6 Reasons Women In Menopause Are Switching To The Evercool® Comforter“. H2: „It's not just you, it's also your bedding.“ · „You stay cool at 3AM, not just at lights-out“ · „It's measurably cool to the touch“ · „You don't wake up damp“ · „Tested with women who actually have night sweats“ · „Nothing in it you'd worry about“ · „Thirty nights to decide“ · „What women with night sweats say“.
  - `rest.com/pages/menopause-proof-v7` / `-v8`: H1 „10 Reasons Women Over 40 with Night Sweats Switched To The Evercool® Comforter“. Weitere H2: „Both sides stay cool, so there's no cold side to hunt for“ · „It works even when the person next to you runs hot“ · „No fuss — it goes in the washing machine“ · „SleepScore™ Labs Validated“.
  - Google zeigt zusätzlich die Varianten v4. Es gibt also mehrere Iterationen, die Seiten werden offenbar systematisch getestet.
- **Lücke:** GetHooked ordnet bei rest.com nur `product_page` zu (197). Eine erfasste Ad mit Ziel `/pages/menopause-*` wurde **nicht** gefunden. Die Listicles könnten über andere Kanäle laufen oder (noch) nicht indexiert sein.
- **Belege (GetHooked):**
  | Ad-ID | Seite | Status | Laufzeit | LP | Hook wörtlich |
  |---|---|---|---|---|---|
  | [30297004](https://app.gethookd.ai/share/ad/30297004?signature=9c76a6aae73a1520cfb85e881230dfdc0c0927e2bcdf2b22f13fdbccfd335bc1) | Rest | inaktiv | **278 T** (11.07.2025–14.04.2026, im Fenster) | rest.com/products/evercool-comforter · PDP | Titel „94% Sleep Better With This "Cooling Comforter"“ · „For women navigating menopause, I know what a challenge restful sleep can be! Even with the A/C set to “snowing” 😆 , it’s nev[er]…“ |
  | [175766490](https://app.gethookd.ai/share/ad/175766490?signature=53c2958ed27005a27439cfd8fcce153ed15d3c046df4e52dc85cc82432724af0) | Rest | aktiv | 28 T · Performance „Winning“ | PDP | „Menopause can be a wild ride and everybody’s experience is different.“ |
  | [199556307](https://app.gethookd.ai/share/ad/199556307?signature=cfc6be959f09fc3da5fd6942044a4b649a5aca3ade314469ea41f26d625df5ab) | Hot Sleeper Journal | aktiv | 8 T (Welle mit 5 IDs: 199555950, 199555937, 200077705, 197997776) | PDP | „I stole a comforter from a hotel in Charleston while I was in town for my niece’s wedding last spring. I'm not proud of it.“ |
  | [81436242](https://app.gethookd.ai/share/ad/81436242?signature=ef35049a6575f8f95d2912d91a394d44103832d1fed958407c4a427ea593f79a) | Rest | inaktiv (bis 30.03., vor Fenster) | 33 T | PDP | „This is the fastest and easiest fix for menopause night sweats. During menopause, your body's temperature control system beco[mes]…“ · Bild „This is the FASTEST AND EASIEST FIX for menopause night sweats.“ (Wärmebild einer Frau unter der Decke) |
- **Warum:** Das gleiche Produkt-Genre wie unseres (Bettdecke statt Laken/Kissen). Rest baut Wechseljahre-Listicles genau mit unseren Begründungen: „it's also your bedding“, 3 Uhr nachts, nicht feucht aufwachen, Partner schläft wärmer, waschmaschinenfest. Die Hotel-Diebstahl-Story der Persona-Seite deckt sich wörtlich mit FluffCo („I stole a pillow from a hotel in Maui…“). Das ist offenbar eine Schablone, die zwischen Bettwaren-Marken wandert. Abzug: Die Listicles sind in GetHooked nicht als Ziel-LP belegt.

### W2 · Earth Breeze (Waschmittelblätter) · Score 6 · haushalt_home / hygiene · US
- **brand_ids:** Earth Breeze 27455 (203 aktive Ads auf der Advertorial-Subdomain), **Laundry Tips Daily 27470** (119), Healthy Home Advocates 4088765 (2), Eco-Friendly Living Daily 4088782 (2) → 4 Seiten, ~326 aktive Ads auf `thebreeze.earthbreeze.com`
- **Web-verifizierte Seiten (Label „ADVERTORIAL“):**
  - `/pages/q-bedsheets`: „I stopped washing my bed sheets and my life is so much better. Here’s why:“ (Ich-Story: optische Aufheller im Laken, Schwarzlicht-Test, „we spend approximately one-third of our lives in bed, in direct contact with these chemicals every night of our lives“)
  - `/pages/american-laundry-sheet`: „Finally! THEY'RE Making Laundry Sheets Right Here in America - And They're Flying Off the Shelves!“ · „WARNING: This story will change the way you do laundry forever!“
  - `/pages/p-lis-free-sample`: Listicle „No matter what, DO NOT PAY for laundry detergent this month!“ („Here are 5 reasons why you shouldn't miss this free sample offer“)
  - `/pages/a-free-sample`, `/pages/stain-l1`
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | LP | Hook wörtlich |
  |---|---|---|---|---|---|
  | [110263351](https://app.gethookd.ai/share/ad/110263351?signature=6716f021b4572cd255c822b81144aa223486baed235796e528fabf450d9e8c34) | Laundry Tips Daily | aktiv | 111 T (6 DCO-Varianten: 110263343/328/310/299/295) | thebreeze…/pages/stain-l1 | Titel „NEW: Miracle Stain Remover Spray ✨“ · „Meet the NEW Miracle Stain Remover Spray ✨ Our formula is designed to help tackle set-in stains fast.“ |
  | [112398178](https://app.gethookd.ai/share/ad/112398178?signature=abbdf8cc3cdcfad6becd06c4166caaf7959146b60f445e20c02a90545293f346) | Earth Breeze | inaktiv (bis 13.08.) | 51 T | earthbreeze.com/scratcher | „I stopped washing my bedsheets and my life is so much better. Here's why…“ (Schwarzlicht-Demo) |
  | [131670779](https://app.gethookd.ai/share/ad/131670779?signature=2fd07f058c9acf0f13fd6aa573bec131d6fc14ac887bb146793f2f89d33242ec) | Earth Breeze | aktiv | 68 T | /scratcher | Titel „Everyone Should Know This“ · „My honest thoughts on Earth Breeze sheets...“ (Overlay „I've worked at Earth Breeze“) |
- **Warum:** Der Bettlaken-Hygiene-Hook „I stopped washing my bed sheets…“ passt als Muster direkt zu Angle A („Ich habe meine Bettdecke seit … nicht mehr bezogen“ wie bei MagicSplashy). Dazu kommen das Schwarzlicht als Beweis-Ritual und eine eigene Advertorial-Subdomain mit Persona-Seite „Laundry Tips Daily“.

### W3 · Miracle Made / Miracle Brand (Silber-Bettwäsche) · Score 9 · hygiene / schlaf_bettwaren · US
- **brand_ids:** Miracle Brand 3177 (357 aktiv; Domains miraclebrand.co, miraclemade.co, restmiracle.com, try.miraclebrand.co; aggregate: landing_page 200, product_page 28) + Persona-Netz auf thegrannyblog.com (Mark Davis 13039094, Lifed 88032, Rachel Monroe 14234590, Cammy Bennett 15227765, Julia Dawson 19855729, Olivia Taylor 17346087, Melissa Taylor 1286792 … ~2.390 aktive Ads, siehe `sweep_gethooked_native.md` K3)
- **Web-verifiziertes Listicle (curl 11:35):** `try.miraclebrand.co/a/s6-reasons`: H1 „6 Reasons Americans are Switching to these NASA-Inspired Sheets“ (Title „6 Reasons Why Americans Are Ditching Their Traditional Sheets“, Countdown „PRIME TIME SALE! … UP TO 46% OFF … VALID FOR 15:00“). Punkte: „1. Temperature-Regulating Comfort“ („Night sweats are the absolute worst! Especially if you are waking up next to a significant other, it can be really embarrassing. Waking up feeling like you just wet the bed makes everything such a hassle.“), „2. Up to 3x Less Laundry And Big Savings“ („after just one week of use, bedsheets had more bacteria than a bathroom doorknob“), „3. Your Sheets Are Damaging Your Skin“ („Do you know what's living in your sheets with you? … more bacteria than a toilet seat“), „4. Odor Fighting“, „5. Luxury Comfort Without The Price Tag“, „6. Try it 100% Risk Free!“
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | LP | Hook wörtlich |
  |---|---|---|---|---|---|
  | [115189525](https://app.gethookd.ai/share/ad/115189525?signature=d8cb4987d48c9a9c9197a8df81f9f0f3505857e55df524290dcf34c99c9b477d) | Miracle Brand | aktiv | **102 T** (seit 29.06.) | try.miraclebrand.co/a/s6-reasons · Listicle | Titel „Self Cleaning: Fewer Odors, 3x Less Laundry!“ · „You probably need some new sheets, let's be honest.“ |
  | [115189367](https://app.gethookd.ai/share/ad/115189367?signature=437a0a94ec27d6892ccee094fa2cdd63ba7db3d3897583867559d199a97134fd) | Miracle Brand | aktiv | 102 T (weitere Varianten 115189412/403/393/354) | dto. | „"I wish I would have upgraded sooner!"It’s never too late to invest in better sleep. Upgrade to Miracle’s NASA-inspired, temp[erature-regulating]…“ |
  | [99445068](https://app.gethookd.ai/share/ad/99445068?signature=7d374440e76d412b469cac680610215a7e93e19bb4fbdb167786e870655278ea) | James Moore (Granny Blog) | inaktiv | 43 T | thegrannyblog.com/miracle-gma/ · Advertorial | „My wife is going to kill me for posting this. She made me promise I wouldn't. I'm doing it anyway because I almost lost her t[o]…“ |
  | [198629101](https://app.gethookd.ai/share/ad/198629101?signature=4aea0ba899ae2b074395d19a924fa3c33e96c33e78d690093c20ec36d62612fe) | Mark Davis (Granny Blog) | aktiv | 4 T (Welle ~760 Ads) | dto. | „Ive been an ICU nurse for 14 years. Last month I swabbed my sons pillowcase as a joke to win an argument with my wife. Nobody…“ |
  | [80214546](https://app.gethookd.ai/share/ad/80214546?signature=c9269390cb7382e27a8ad919c2f31d97846c1be3d0d21f0e73627a00de4ac6c6) | Melissa Taylor (Granny Blog) | inaktiv (Feb., vor Fenster) | 5 T | thegrannyblog.com/miracle-pets/ | Titel „If Your Cat Or Dog Sleeps On Your Bed, Check Your Pillowcase“ · „I knew something was really wrong with my mom when she didn't come to Thanksgiving.“ (Tochter-Mutter-Rahmen) |
- **Warum:** Hygiene (Bakterien, Geruch, Haut) und Nachtschweiß in einer Bettwaren-Story, dazu ein eigenes Listicle mit 102 Tagen Laufzeit und ein riesiges Persona-Advertorial-Netz. Das ist fast 1:1 auf eine waschbare Decke übertragbar („Up to 3x Less Laundry“ entspricht bei uns „kein Bezug mehr“).

### W4 · Clean People (Waschmittel/Spülmittel) über Fake-Blog „Women's Fitness & Style“ · Score 6 · haushalt_home · US
- **brand_ids (Personas auf womensfitnessandstyle.com):** Women's Wellness 301530 (364 aktiv), Women into Wellness 261911 (162), Dr. Rose, MD 11831258 (90), Dr. Gabriela, Dermatologist 7091070 (34), Natural Living Tips 7091065 (28), Nontoxic Mom 1083672 (25), Clean American Mom 7091063 (10), Nontoxic Home Guy 7091064 (7), Dermatologist Reviews 20215704 (2), The Clean Label Woman 11831220 (1) → **10 Persona-Seiten, ~723 aktive Ads**
- **Web-verifizierte LP (curl 11:36):** `womensfitnessandstyle.com/5-best-laundry-detergents-avoid-harsh-chemicals/` (Redirect von `…-according-dermatologist/`) = Vergleichs-Listicle „5 Best Laundry Detergents to Avoid Toxic Ingredients According to a Dermatologist“ (Blog „by Nicole“, Rubrik „Life Changes“; „TLDR: CLEAN PEOPLE Laundry Detergent came in #1…“; „And The Winner Is…“). Zweite Seite: `/5-best-dishwasher-detergents-avoid-gut-health-issues/`.
- **Belege:**
  | Ad-ID | Seite | Status | Laufzeit | Hook / Bildtext wörtlich |
  |---|---|---|---|---|
  | [100927762](https://app.gethookd.ai/share/ad/100927762?signature=8a69520a16760aa81c512ed13deb0bc02949891082ce5e6b3d771f940a644508) | Women's Wellness | inaktiv (bis 09.09.) | **115 T** | Titel „You'll want to change your laundry detergent after reading this“ · „We tried dozen of laundry detergents to identify the 5 best laundry detergents to avoid harsh chemicals like 1,4 dioxane, SLS…“ · Bild „YOUR LAUNDRY DETERGENT COULD BE CAUSING YOUR HEADACHES / Read to reveal the 5 best safer alternatives👇👇👇“ |
  | [100927511](https://app.gethookd.ai/share/ad/100927511?signature=42e4c381d22d3648a229ac94d726206f0cb4a66c4293cdb8abb5bb7bde4cca8e) | Women's Wellness | inaktiv | 115 T (used_count 6) | „Whoever made this billboard might be getting sued. Which is wild… because I’m pretty sure the brand people are thinking of i[s]…“ · Bild: Fake-Plakat „Experts urge families to switch detergents after ingredient officially linked to CANCER“ |
  | [87297559](https://app.gethookd.ai/share/ad/87297559?signature=6fd590560dbe512abd8bbd87fee7357a7fb5f755a8ceb720908b5330ca58baca) | Women's Wellness | inaktiv | 169 T (25.03.–09.09.) | „I don't trust clean people dishwasher pods. Here's why. I tried 10 dishwasher pod brands. One of them cost just 29 cents per…“ (Fake-Skepsis) |
  | [191741416](https://app.gethookd.ai/share/ad/191741416?signature=74e92c7a10db15b1b5c8898408b9db3c405a9bd5ca8e59ab634646fb6f0e1d49) | Dr. Rose, MD | aktiv | 29 T | „I didn’t want to share this because it’s pretty personal... but maybe this can help one of you. Last month, I started waking…“ |
- **Warum:** Kein Bettwarenprodukt. Es ist aber die sauberste Vorlage für ein **Experten-Vergleichs-Listicle auf einer neutralen Blog-Domain** („We tested 5 … According to a Dermatologist“) mit vielen Experten- und Mama-Personas. Das lässt sich direkt auf „5 Best Washable Duvets for Allergy Sufferers – tested by a nurse“ übertragen.

---

## 3. Kontrollgruppe (Marken ohne Natives) – GetHooked `aggregate_ads(page_type)` auf Domain, aktive Ads

| Marke / Domain | page_type-Verteilung | Bemerkung |
|---|---|---|
| Buffy (buffy.co) | PDP 10, Collection 4, Homepage 2 | US-Bettdecken-Marke |
| Slumber Cloud (slumbercloud.com) | Homepage 78, PDP 3 | Kühl-Bettwaren |
| Woolroom (thewoolroom.com) | Collection 99, Homepage 53 | UK-Wollbettwaren, Allergie-Claims |
| Beddy's (beddys.com) | Homepage 82, Collection 11 | Reißverschluss-Bettwäsche (Angle C!) |
| BedJet, Kally Sleep, Promeed, Brolly Sheets, Calming Blankets, trymiracle.com | keine Buckets | – |
| Simba (simbasleep.com) | Collection 16, PDP 2 | UK |
| Panda London | Collection 5 | UK |
| Fine Bedding Co. (finebedding.co.uk) | PDP 5 | UK, Night-Lark-Decke ohne Bezug |
| Hush Blankets | PDP 2 | – |
| Dagsmejan | Collection 21 | Wechseljahre-Schlafwäsche |
| Cozy Earth | Collection 171, Homepage 164, PDP 69 | – |
| Manta Sleep | PDP 78, Landing 53 | – |
| Tru Earth | Collection 38 | – |
| **Night Lark Coverless Duvet** (brand 7106888, 56 aktiv, GB) | alle Ads → PDP/Collection | z. B. [153477576](https://app.gethookd.ai/share/ad/153477576?signature=488f48c6e8b485e729c0c1b4a310661b3984c54efaf841544b00cd06c9a8bfbc) aktiv 52 T „Refresh your little cub’s bedroom and say goodnight to duvet changing faff with our Junior Leopard Family Coverless Duvet.“ → **direkter UK-Wettbewerber ohne Native-Ansatz** |

---

## 4. Lücken / Einschränkungen (ehrlich)
- Der WebSearch-Index ist US-zentriert und zeigt Presell-Seiten selten. Ein „kein Treffer“ heißt deshalb nicht, dass es keine Advertorials gibt.
- Rest: Die Wechseljahre-Listicles sind im Web nachgewiesen, nicht aber als Ziel einer erfassten Meta-Ad. Mögliche Gründe: Traffic über andere Kanäle (z. B. Native-Netzwerke, Google) oder fehlende Indexierung.
- GetHooked `days_active` bei aktiven Ads ist „start_to_today“. Bei Clean People sind alle Langläufer seit 09.09. inaktiv; eine Abfrage mit `status=active` lieferte 0 Zeilen, weil der Index sie als veraltet zurückhielt.
- Die Meta-Ad-Library (META_ADS-Tool) habe ich bewusst nicht genutzt. GetHooked deckt die Belege ab.
- Zwei GetHooked-Abfragen liefen in ein Timeout („pillowcase bacteria“, Domain-Suche „sheets bed“) und wurden vereinfacht wiederholt.

---

## 5. ZUSAMMENGEFÜHRTE Kandidatenliste (alle drei Suchwege, jede Marke einmal)

Score = Stärke als Vorbild für UNSERE Angles (A Hygiene, B Wechseljahre, C Beziehen, D Tochter kauft für Mutter). „Quelle“: N = Native-Sweep, H = Hook-Sweep, W = Web-Sweep. Volle Belege in der jeweiligen Datei.

| # | Marke | brand_id(s) | Domain | Kategorie | Markt | Native-Formate | Bester Laufzeit-Beleg | Angles | Score | Quelle |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MagicSplashy EasySleep | 88310 | magicsplashy.de | schlaf_bettwaren | DE | Redakteur-Ich-Story-Adv., Umfrage-Adv., Wechseljahre-Listicle (Frauenmagazin), Presell, UGC-Ich-Story | 126012757 · 83 T · $10–20k · Winning | C, B, A | 10 | N, H |
| 2 | Plufl / Hugl | 116814, 7705, 28432, 351627 … (17 Seiten) | weareplufl.com | schlaf_bettwaren | US | Creator-UGC → Magazin-Advertorial | 121399208 · 309 T aktiv; 122685364 „Want Mom to Sleep Better?“ 309 T | B, D | 10 | N, H |
| 3 | UVlizer / Clairu | 70309, 197491, 126532 | getuvlizer.co.uk → tryclairo.co.uk | allergie | **UK** | Grandma-/Mom-Advertorial, Listicle, Ich-Story-Video | 80269727 · 489 T; 35831986 · 424 T | A, (D) | 10 | N, H |
| 4 | Miracle Made + The Granny Blog | 3177 + 13039094, 88032, 14234590 … | try.miraclebrand.co, thegrannyblog.com | hygiene | US | Listicle „6 Reasons…“, Fake-Magazin-Advertorial, Ich-Story-Personas | 115189525 · 102 T aktiv | A, B | 9 | N, W |
| 5 | GroundingWell | 697, 689, 306559, 2741196 … (46 Seiten) | groundingwell.com, journal.… | schlaf_bettwaren | US/UK/EU | Arzt-Adv., Ich-Story-Adv., Wechseljahre-Adv., Listicle „Women Over 50“ | 75250601 · 226 T; 89809570 · 157 T | B, D | 9 | N, H |
| 6 | TrueClean / The Natural Household (CaptureCards) | 7566011, 7635423 | truecleanhome.com, thenaturalhousehold.co | hygiene | US | Listicle, Ich-Story-Adv., Native-Text-Bild | 127732600 · 106 T aktiv | A | 9 | H |
| 7 | Rest – Evercool Comforter | 28140, 7097606 | rest.com | schlaf_bettwaren | US | Wechseljahre-Listicles (Web), Persona-Ich-Story, UGC | 30297004 · 278 T (PDP) | B, A | 8 | W, H |
| 8 | Ryer + provergleich.com | 5345283, 7199495, 7199496 … (8 Seiten) | ryer.de, provergleich.com | haushalt_home | DE | Mama-Ich-Story-Adv., Listicle, sprechende Milben | 111737379 · 124 T; 145503635 · 55 T · 9 Var. | A | 8 | N, H |
| 9 | Eight Sleep über „The Get Well“ | 6005158, 8071, 515674 … (6 Seiten) | i.eightsleep.com → thegetwell.co | wechseljahre | US | Publisher-Advertorial, Reddit-Screenshot, Paar-Story | 150166895 · 52 T aktiv | B | 8 | N |
| 10 | Cosy House Collection | 5995 | try.cosyhousecollection.com | schlaf_bettwaren | US | Listicles (2), Ich-Story-Video | 107610652 · 115 T aktiv | B, A | 8 | H |
| 11 | Down To Ground | 36329, 7049265 … (9 Seiten) | downtoground.co | schlaf_bettwaren | US/UK | Gründer-Listicle, Gründer-Story („for my mum“), Menopause-Ad | 89820013 · 187 T aktiv | D, B | 7 | N, H |
| 12 | Aeyla | 4518428 | aeyla.co.uk | schlaf_bettwaren | **UK** | Community-Persona, Ich-Story 61-Jährige (Hygiene-Schock) | 97025036 · 33 T; 117258077 · 98 T (PDP) | A, D | 7 | H |
| 13 | Kaori (Grandma's Glow / Care Journal) | 4451068, 4486124 | try-kaori.com | hygiene | US | Ich-Story Oma/Enkel, Listicle „7 Reasons…“ | 95842126 · 203 T aktiv | A, D | 7 | H |
| 14 | SP Nutrition | 4755341, 1798132 … | spnutrition-us.com | wechseljahre | US/UK | Gynäkologen-Adv., Tochter-zeigt-Artikel-Story | 104320503 · 186 T; 101624013 · 139 T | B, D | 7 | N, H |
| 15 | FluffCo | 47695, 6971966 … (6 Seiten) | try.fluff.co | schlaf_bettwaren | US | Listicle-Advertorial „8 Ways…“, Hotel-Story | 120530139 · 91 T · 5 Var. | (C), A | 7 | N |
| 16 | The Sleep Edit → Silvery Cooling Comforter | 7531501 | thesleepedit.co | schlaf_bettwaren | US | Arzt-Vergleichs-Advertorial „Top 5“ | 185341953 · 22 T | B | 7 | N |
| 17 | Mellow Sleep | 4398848, 1329122, 2755134 … (≥50) | mellowsleep.com | schlaf_bettwaren | US | Chiropraktiker-Ich-Story-Adv., Listicles, Kühl-Kissenbezug Menopause | 95218705 · 168 T | (B) | 6 | N, H |
| 18 | twentythree.de | 5346201 | twentythree.de | schlaf_bettwaren | DE | Listicle „8 Gründe…“ (Schwitzen, reife Haut) | 111961242 · 130 T aktiv | B | 6 | H |
| 19 | Earth Breeze | 27455, 27470 … (4 Seiten) | thebreeze.earthbreeze.com | haushalt_home | US | Ich-Story-Adv. „I stopped washing my bed sheets…“, Listicle | 110263351 · 111 T aktiv | A | 6 | W |
| 20 | Clean People (Women's Fitness & Style) | 301530, 261911, 11831258 … (10 Seiten) | womensfitnessandstyle.com | haushalt_home | US | Dermatologen-Vergleichs-Listicle auf Fake-Blog | 87297559 · 169 T; 100927762 · 115 T | A | 6 | W |
| 21 | Clarifion | 3202, 44651, 3204 … (6 Seiten) | about.clarifion.com | allergie | US | News-Advertorial, „(MUST READ)“-Native | 92196867 · 93 T | A | 6 | N, H |
| 22 | AeroPure | 1511778, 1987586, 11131855 | aeropure.com.au | allergie | AU | Arzt-Listicle, Advertorial | 80217310 · 230 T | A | 6 | N |
| 23 | Healthy Essential | 81274, 272689, 2569 | healthy-essential.co | haushalt_home | US/**UK** | Vergleichs-Listicle „Top 4 … Available in the UK“ | 75702 · 954 T | A | 6 | N |
| 24 | X-All Waschmaschinenreiniger | 4465551 | xwm.x-all.com | hygiene | US | News-Ich-Story (Tochter wäscht bei Mama) | 94819002 · 235 T | A, D | 6 | N |
| 25 | Home & Garden Trend (OrthoBed) | 2090 | garden-trend.store | schlaf_bettwaren | US | Listicle-Advertorial „5 Ways Your Old Mattress…“, Ekel-UGC | 104756839 · 128 T aktiv | A | 6 | N, H |
| 26 | Fine Foams | 7210101 | finefoams.com.au | schlaf_bettwaren | AU | Gründer-Listicle, Native-Typo-Bild „Two people. One doona.“ | 170770704 · 41 T | B | 6 | N |
| 27 | Swarva | 197895 | swarva.com | hygiene | US/UK | Arzt-Advertorial (Altersgeruch) | 76171252 · 165 T | A, D | 5 | N |
| 28 | Top 5 Best Mattresses UK (Emma) | 504951 | top5bestmattress.co.uk | schlaf_bettwaren | **UK** | Marken-eigene Vergleichsseite | 123222968 · 149 T (unsicher) | – | 5 | N, H |
| 29 | Earthbound Co. | 15669 | thelongevitybrief.com | schlaf_bettwaren | US | UGC → Fake-Magazin-Advertorial | 46362941 · 366 T aktiv | – | 5 | H |
| 30 | Zelesta.de | 5189960 | zelesta.de | schlaf_bettwaren | DE | UGC-Ich-Story „Bett beziehen“ (Homepage) | 108558235 · 129 T · $2–5k | C | 5 | H |
| 31 | Pridola | 15934 | pridola.co.uk | schlaf_bettwaren | **UK** | Story-Hooks Frauen 50+, Animation (LP = PDP) | 168477031 · 41 T | B | 5 | H |
| 32 | Uk Sleep Forum (Airvex) | 11235315 | airvex.shop | schlaf | **UK** | Native-Text-Story (LP = PDP) | 178964447 · 44 T | B | 4 | N |

Nicht als Kandidat gewertet (Kontext): direkte Wettbewerber „Decke ohne Bezug“ ohne Natives: Night Lark (UK), Pleene (US/UK), HappyBed, OhMySwiss, Ynot, Anfaru, Paradies (DE).
