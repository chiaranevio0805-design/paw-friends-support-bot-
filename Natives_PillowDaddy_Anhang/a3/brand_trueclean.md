# Marken-Deep-Dive: TrueClean / The Natural Household – CaptureCards (Milbenfalle für die Matratze)

Stand: 08.10.2026, ca. 17:00 Uhr (UTC), Agent 3, zweiter Lauf. Quellen: GetHookd (`get_domain_advertisers`, `search_ads`, `get_ad`, `get_ad_media`, `transcribe_ads`/`get_transcription_status`) und mobile Seitenabrufe mit `tools/shot.js` (`a3/pages/tc_*`). Zitate stehen wörtlich in der Originalsprache. Links sind GetHookd-`share_url`s oder echte LP-URLs. Rohnotizen liegen in `a3/deep3/_notes.md`, Volltexte in `a3/deep3/body_*.txt`.

| Feld | Wert |
|---|---|
| Produkt | „CaptureCard™ Dust Mite Traps“: eine Stoffkarte mit Lockstoff und Klebefläche, die unter die Matratze bzw. in den Kissenbereich gelegt wird. Laufzeit 1 Karte = 3 Monate. Daneben verkauft dieselbe Firma einen Toiletten-Reiniger (TrueClean „Swoosh n Shine“). |
| Firma (laut LP-Footer) | „Brandlab Ventures LLC, 412 W 7th St, Clovis New Mexico“ |
| Domains | truecleanhome.com (Haupt-LPs), thenaturalhousehold.co (zweite LP-Domain), cleaningmadesimple.us (Vergleichs-„Review“-Seite, nur Toilette) |
| Meta-Seiten (Domain-Advertiser 08.10., 16:48) | truecleanhome.com: **The Natural Household** 7566011 (250 aktive Ads auf der Domain, seit 01.04.), **True Clean Home** 7635423 (84, seit 20.04.), **Clean Home Review** 7635424 (18, seit 06.08.). thenaturalhousehold.co: nur The Natural Household (10). |
| Markt / Sprache | USA, Englisch (alle geprüften Ads `countries: US`) |
| Native-/Story-Nachweis | **Ja.** (1) Drei Seiten mit neutral-redaktionellen Namen („The Natural Household“, „True Clean Home“, „Clean Home Review“) statt Markenname. (2) Lange Ich-Story-Texte mit Native-Post-Bild („… Read more“). (3) Alle CaptureCards-LPs sind Advertorial-Listicle-Hybride („Why You Wake Up Stuffy…“, „6 Reasons People Are Switching to CaptureCards“). Einschränkung: Es gibt keine Fake-Magazin-Optik, denn die LPs tragen oben das TrueClean-Logo. |
| Zielgruppe (aus Bildern/Texten) | Frauen um 50+ (Before/After-Foto einer Frau ~50 auf allen LPs; „At my age, I just don't have the energy…“; „By our age, who has the energy to strip the bed…“; „Everyone keeps telling women over 50 the same thing… Menopause“) |

## 1. Inventar und Erfolgssignale (CaptureCards, 08.10.)

- **The Natural Household (7566011):** Im Index stehen 268 aktive Ads. Die Langläufer sind Toiletten-Ads (191, 186 und 122 Tage). Die CaptureCards-Langläufer: 127732600 (106 T), 127732615 (105 T), 127732656 (98 T, 2 Varianten), 127732679 (86 T), 132827480 „The Mattress Trick For Dust Mites? (MUST READ)“ (72 T, **Winning**), 135447800 „What Would Your Mattress Reveal?“ (70 T, 6 Varianten), 143765162 „A Different Dust-Mite Fix“ (58 T, 3 Varianten).
- **True Clean Home (7635423):** 81 Ads im Index. Die CaptureCards-Ads starteten alle am 25./26.06. und laufen damit seit **105–106 T**: 132882815 (**Winning**), 132882900 „Sneezing Every Morning? It’s Probably Not Pollen. Check Your Mattress.“ (**Winning**), 132882997 (**Optimized**, 3 Varianten), 132884643 „The Allergy Test You Can Do With Your Phone Flashlight.“ (3 Varianten), 135489754 „No sprays, no scrubbing — up to 35% off today.“ (Hook: „By our age, who has the energy to strip the bed, haul the matt…“).
- **Clean Home Review (7635424):** 155122137 Video (64 T, **Winning**, 7 Varianten). Dazu der **Wechseljahre-Test** 155122378 „Hormones fine. Mornings still wrecked?“ (55 T, Testing, 2 Varianten) mit eigener LP `/pages/capturecards-menovsmite`.
- **Spend:** GetHookd liefert für alle CaptureCards-Ads **keinen** Spend-Bucket (`ad_spend_range_score_title: null`, US-Ads ohne EU-Transparenzdaten). Die Stärke wird deshalb an Laufzeit, Performance-Score und Varianten gemessen.
- **Neue Tests (06.10., 3 T):** Native-Text-Bilder im Facebook-Post-Stil. Beispiel 201101007 „30 Years Of Hot Washes Didn’t Work“ mit Tochter-über-Mutter-Rahmen: „My mom washed sheets the way her mom taught her: hot water, every week, no shortcuts. And for years she still woke up stuffy.“ (Angle D!). Weitere Beispiele siehe `sweep_gethooked_hooks.md`: „My Allergist Asked How Often I Dust…“, „My house is spotless. This came out of my mattress anyway…“.

## 2. Auswahl der 3 stärksten Native-/Story-Ads

| Rang | Ad | Begründung |
|---|---|---|
| 1 | **132882997** (Cluster „You Can't Wash A Mattress. You Can Empty It.“, True Clean Home) | Größter Cluster der Marke: 33 Treffer auf der Seite True Clean Home, dazu ein gleich betiteltes Video 127732615 auf The Natural Household (105 T). Die Vertreter laufen 106 T aktiv: 132882997 „Optimized“ (3 Varianten), 132882815 „Winning“. Der Text ist ein Problem-Aufklärungs-Native (Mechanismus statt Produktfoto) und führt auf die Listicle-LP. Das ist **die direkteste Vorlage für unseren Hygiene-Angle**, denn der Satz lässt sich 1:1 auf Bettdecken übertragen: Die Decke im Bezug wird nie gewaschen. |
| 2 | **127732600** (Ich-Story „Covers, Sprays, A $200 Purifier, Hot Washes…“, The Natural Household) | Reine Ich-Story mit 5.201 Zeichen, Native-Post-Bild („My electric bill noticed the purifier. My nose never did… Read more“), 106 T aktiv. Klassischer Erzählbogen: alles probiert, ein Mentor („a guy… in hotel housekeeping and pest control“), Aha-Frage, Produkt, sichtbarer Beweis. Die Ich-Erzählerin ist älter („At my age…“). Führt auf das Listicle-Advertorial `capturecards-listicle-airpurifier`. |
| 3 | **155122137** (Video „You Don't Have An Allergy Problem. You Have A Mattress Problem.“, Clean Home Review) | „Winning“, 7 Varianten, 64 T aktiv. Läuft über die dritte Persona-Seite. Format: Zeitstrahl-Beweis „Week 1 vs Week 12“ mit eingeblendeten Wochen-Labels. Führt auf `capturecards-proof`. Das ist das stärkste Video-Native der Marke. |

Nicht gewählt, aber notiert: 132827480 „(MUST READ)“ (Winning, 72 T, Bild → `capturecards-not-a-cold`) und 155122378 „Hormones fine. Mornings still wrecked?“ (Wechseljahre-Angle, nur Testing).

---

## Ad 1 · 132882997 – „You Can't Wash A Mattress. You Can Empty It.“ (Cluster)

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/132882997?signature=4a74d8199d2725ff56ae882f8f65eb500764073b358d210fc61c662b79d5a72b |
| Cluster | 132882997 (Optimized, 3 Varianten), 135489776, 135489793, 135489763 (alle → `/pages/capturecards-listicle`); 132882815 (Winning → `/pages/mites-capturecards`) https://app.gethookd.ai/share/ad/132882815?signature=e665384ea5092161c4dd3f7d57a09b61befc703179f19ccb140858d0b656fade ; Video-Schwester 127732615 (The Natural Household, 105 T) https://app.gethookd.ai/share/ad/127732615?signature=1c2daa6dab3ece7f5a9388e7beaa035f7c50268cc5efef8230051ae4eb064011 |
| Seite/Persona | True Clean Home (7635423) |
| Status | aktiv |
| Start / Ende / Laufzeit | 25.06.2026 / – / 106 T |
| Format | Bild · Plattformen facebook, instagram, audience_network, messenger, threads |
| CTA | SHOP_NOW „Shop now“ · link_description „True Clean“ |
| Spend / Score | kein Spend-Bucket · Optimized (132882815: Winning) |

**Headline:** „You Can't Wash A Mattress. You Can Empty It.“

**Primärtext (wörtlich, vollständig):**
> You wash the sheets in hot water every week. The mattress just refills them.
>
> Here's the truth no one selling you sprays and covers wants to say out loud: you don't have an allergy problem. You have a mattress problem. And you can't wash a mattress.
>
> Hot washes clean fabric. Encasements seal the problem in — under you. Sprays kill a few mites on the surface and leave every dropping (the actual allergen) right where it was. Air purifiers clean the air, not the bed. A brand-new mattress just gets colonized again in weeks. None of them REMOVE anything from inside the mattress, where the colony actually lives.
>
> You can't wash a mattress. But you can empty it.
>
> CaptureCards take the opposite approach:
>
> 🟢 A plant-derived scent lures mites out of the mattress layers
> 🟢 An adhesive traps them for good — mites AND droppings
> 🟢 Nothing sprayed, nothing sealed, nothing left behind in your bed
> 🟢 Cut the card open after a few weeks and see what it caught with your phone light
>
> 10-second install. Works 24/7 for 3 months per card. No fumes, no chemicals — safe for kids' beds and pet beds.
>
> 90-day money-back guarantee — full refund, no return needed. Tap below to get up to 35% off.
> 👉 https://truecleanhome.com/pages/capturecards-listicle

**Text im Bild (wörtlich):** „YOU CAN’T WASH / A MATTRESS. / YOU CAN EMPTY IT.“ (die letzte Zeile in Petrol). Darunter eine gerollte weiße Matratze, die in einer Frontlader-Waschmaschine steckt, Schaum läuft heraus. Die Bildsprache wirkt KI-generiert, die Kartenaufschrift ist verzerrt („True Clean / MITE CAPTURE CARD“). Unten rechts eine Button-Grafik „SEE HOW“.

**Video-Schwester 127732615, Transkript (93 s, vollständig):**
```
[00:00] I saw something that honestly made my own bed feel gross.
[00:03] Your mattress can hold millions of dust mites and they are the main reason you wake up stuffy,
[00:08] sneezing, or groggy every morning. So I did what everyone does. I washed my sheets on hot,
[00:14] I washed my pillows, I even bought an air purifier, and it helped for a night or two.
[00:18] Then the stuffy mornings came right back because the problem was never really the sheets or the
[00:23] air. It was what was hiding deeper down in the mattress and the pillow where none of that ever
[00:28] reaches. That's why I tried capture cards. Instead of spraying your bed and trying to repel them,
[00:33] these cards do the opposite. They lure the dust mites out of hiding. Each card uses an attractant
[00:38] that pulls the mites toward the trap. And once they crawl on, the adhesive holds them there for
[00:42] good. So you're not just hoping it's working. After a few weeks, you check the card and actually
[00:47] see what it pulled out of your bed. And here's the part that got me. Dust mites are basically
[00:52] invisible. Way too small to see with your eyes. But the lure inside the card has a dye in it.
[00:57] So the moment a mite feeds, it turns visible. Hold the card up to your phone light and you can
[01:02] actually see the catch. Using it couldn't be simpler. You slide one under your mattress,
[01:07] place one near your pillow, and that's it. No spray, no fumes, nothing to plug in, no filters
[01:12] to replace, and one card lasts for months. In lab testing, capture cards trapped up to 99.9%
[01:19] of dust mites. It even comes with a 90-day money-back guarantee. If you don't see it work,
[01:23] you get a full refund. No return needed. So if waking up clear actually matters to you,
[01:27] I can't recommend this enough. Tap below to pull the dust mites out of your bed,
[01:31] risk-free, while supplies last.
```

**Story-Muster:** Reframe-Native („You don't have an allergy problem. You have a mattress problem.“): Zuerst wird der Feind entlarvt, dann folgt die Liste der gescheiterten Lösungen (hot washes, encasements, sprays, purifiers, neue Matratze), dann der Satz-Twist „You can't wash a mattress. But you can empty it.“, dann der Mechanismus in vier grünen Punkten, dann Selbstbeweis („phone light“) und Risikoumkehr. Das Video erzählt dieselbe Abfolge als Ich-Erzählung („I did what everyone does…“).

**Landingpage:** `https://truecleanhome.com/pages/capturecards-listicle`. Die Seite liefert textgleich dieselbe Seite wie `/pages/mites-capturecards` (md5 der Textfassung identisch), siehe LP-Analyse A unten.

---

## Ad 2 · 127732600 – Ich-Story „Covers, Sprays, A $200 Purifier, Hot Washes …“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/127732600?signature=afa84150b7971449d34bc3e756184af0f9c28f93b8213a649bdc4b29039e2f33 |
| Seite/Persona | The Natural Household (7566011) |
| Status | aktiv |
| Start / Ende / Laufzeit | 25.06.2026 / – / 106 T |
| Format | Bild (2 Media; per `get_ad_media` nur 1 Bild darstellbar) · facebook, instagram, audience_network, messenger, threads |
| CTA | SEE_DETAILS „See details“ · link_description „True Clean“ |
| Spend / Score | kein Spend-Bucket · Performance 61 „Growing“ · 1 Variante |

**Headline:** „Covers, Sprays, A $200 Purifier, Hot Washes — The First Thing That Actually Pulled Anything Out Of My Bed.“

**Text im Bild (wörtlich):** Ein weißer Balken im Facebook-Post-Stil mit schwarzer Schrift: „My electric bill noticed the purifier. My nose never did…“, gefolgt von „Read more“ in Grau. Darunter ein Amateur-Handyfoto: schwarzer Luftreiniger neben einem Bett, eine Stromrechnung auf dem Nachttisch, abgenutzter Holzboden.

**Primärtext (wörtlich, vollständig, 5.201 Zeichen; Datei `a3/deep3/body_127732600.txt`):**
> I've spent more money trying to get dust mites out of my bed than I'd like to admit.
>
> Covers, sprays, a $200 purifier, years of hot washes.
>
> The first thing that ever pulled anything actually out of the mattress cost less than any of them.
>
> This one's for the people who already know it's dust mites.
>
> You're not confused about the cause. You've read the articles. You've tried the fixes.
>
> And you've quietly started to believe there's just nothing you can really do about what's living in your mattress.
>
> I believed that for a long time.
>
> I'd known for years it was dust mites — the morning congestion, the sneezing, the watery eyes.
>
> I'm not someone who ignores a problem. I went after it. Hard.
>
> I started with the encasements — the zip-up covers that promise to seal in the mattress and pillows.
>
> And they did work… for a few days.
>
> But to keep it that way you have to strip the bed and wash everything constantly. At my age, I just don't have the energy to keep that up.
>
> Then the anti-mite sprays. I did the whole mattress, gagging on the smell.
>
> It killed a few on the surface — but more just crawled right back within days.
>
> Then a $200 HEPA air purifier, running every night. My electric bill noticed. My nose never did.
>
> And the honest truth? Keeping all of it up — the washing, the spraying, the constant upkeep — for results that small… I got tired of it. I let it slide.
>
> And the stuffy mornings never went anywhere.
>
> What finally made it click was a guy I met through work.
>
> He'd spent years in hotel housekeeping and pest control.
>
> He didn't tell me anything I didn't already know deep down — he just finally put it into words.
>
> The reason they always come back, he said, is you.
>
> Your body heat and the moisture you give off every night is exactly what dust mites are drawn to.
>
> They migrate toward your pillow and the spot where you sleep — because that's where the warmth, the humidity, and the skin to feed on all are.
>
> You're never going to "stop" that. As long as you sleep there, they keep coming back to it.
>
> Then he asked me one simple question:
>
> "Did any of the stuff you tried actually remove anything from inside the mattress? Or did it just sit on top — or just clean the air?"
>
> I thought about it.
>
> The covers just sealed them in — under me.
>
> The spray killed a few on the surface, but more crawled right back.
>
> The purifier cleaned the air, not the bed.
>
> And the washing only cleaned the sheets — while the colony sat in the fibers underneath, refilling the surface within days.
>
> He was right.
>
> In all those years, and all that money, not one thing I tried had removed a single mite from where they actually live.
>
> I'd cleaned around the problem. Sealed it in. Chased it through the air. Never once emptied the bed.
>
> "That's the whole game," he said. "Stop trying to kill them or seal them in. Pull them out instead."
>
> That's how I found CaptureCards.
>
> And yes — I was skeptical. I'd been skeptical about the last four things too.
>
> It's a flat fabric card. You slide it under the mattress and tuck one near the pillows.
>
> It doesn't seal, spray, or filter. It removes.
>
> Here's how it actually works:
>
> The card is loaded with the same scent dust mites use to gather — their own aggregation pheromone — plus the kind of food they're always hunting for.
>
> To a dust mite, that makes the card a far more tempting place to be than your mattress or your pillow.
>
> So they do the one thing they're wired to do — they crawl toward it. Off the bed. Off your pillow. Onto the card.
>
> And that changes two things.
>
> First, they're no longer crawling toward you — not feeding on your skin, not getting stirred into the air you breathe all night.
>
> Second, the moment they settle onto the card, the adhesive locks them in. They don't crawl back out.
>
> One card runs about three months.
>
> But here's the part I still can't get over.
>
> A few weeks in, you can cut the card open and hold your phone flashlight behind the inner pad.
>
> And you see them.
>
> A scatter of tiny dark specks all through the fabric — the actual mites it pulled out of your bed.
>
> Not a number on a box. Not a promise. The real thing, out of your own mattress, right there in the light.
>
> There were far more than I ever wanted to think about.
>
> After years of products I had to take on faith, this was the first one that showed me — in my own hands — that it had done something.
>
> The mornings finally eased.
>
> But the thing I keep coming back to isn't even that. It's that I could finally see it working.
>
> If you've tried everything and quietly given up — that part matters more than I can explain.
>
> If you already know it's dust mites, and you've done the covers, the sprays, the purifiers and lost faith — read this.
>
> It breaks down exactly why each of those leaves the mites in your bed… and why pulling them out is the one thing none of them do.
>
> 👉 https://thenaturalhousehold.co/pages/capturecards-listicle-airpurifier
>
> P.S. Here's the test for anything you've ever tried:
>
> Did it actually remove something from inside the mattress? Or did it just sit on top, or clean the air?
>
> If the honest answer is no… that's not bad luck. That's the reason it didn't work.
>
> None of them were built to pull the mites out. This one is.

**Story-Muster:** „Ich habe alles probiert“ (die Ich-Erzählerin ist älter und gibt aus Erschöpfung auf), dann ein **zufälliger Mentor/Experte** („hotel housekeeping and pest control“), dann **eine entlarvende Frage** („Did any of the stuff you tried actually remove anything…?“), dann eine Rückblende auf alle gescheiterten Mittel, dann das Produkt (nach 534 Wörtern), dann der Mechanismus (Pheromon und Klebefläche), dann der **sichtbare Selbstbeweis** („phone flashlight… tiny dark specks“), dann der Verweis auf den Artikel („read this“), dann ein P.S. mit Prüffrage. Der Text ist nicht an einen Namen gebunden und hat keine Signatur.

**Landingpage:** `https://thenaturalhousehold.co/pages/capturecards-listicle-airpurifier`, siehe LP-Analyse B.

---

## Ad 3 · 155122137 – Video „You Don't Have An Allergy Problem. You Have A Mattress Problem.“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/155122137?signature=72b4af3c33f341b58dd8831ec6df8c34315d4876921fb04484c2c11fb6ce9195 |
| Seite/Persona | Clean Home Review (7635424) |
| Status | aktiv (letzte Sichtung 06.10.) |
| Start / Ende / Laufzeit | 06.08.2026 / – / 64 T |
| Format | Video ca. 56 s |
| Spend / Score | kein Spend-Bucket · **Winning** · 7 Varianten (`collapse_variants`); weitere Kopien 155122245 und 155122220 (beide 15.08., 55 T, Optimized), CTA LEARN_MORE „Learn more“ |

**Headline:** „You Don't Have An Allergy Problem. You Have A Mattress Problem.“

**Primärtext (wörtlich, aus den textgleichen Cluster-Varianten 155122245/155122220; über `collapse_variants` mit 155122137 gruppiert):**
> This is what happens when you slide one Capture Card under your mattress and just… leave it. Week 1, your mornings start clearing. By week two you're sleeping through more and waking less puffy. By month 3 — cut the card open, hold it to your phone light, and see exactly what came out of your bed. No spraying, no plugs, no laundry. 90-day money-back guarantee. 👉

**Text im Video (Stills 0 s/25 %/50 %):** In den ersten Sekunden ein Split-Screen: oben „WEEK 1“ (petrolfarbenes Label, saubere Netzkarte in der Hand), unten „WEEK 12 🤮“ (gelbes Label, aufgeschnittene Karte vor dem Handylicht mit dunklen Punkten). Bei 25 % das Label „END OF WEEK 1“ (Karte „TrueClean / MITE-CAPTURE CARD / EFFECTIVE · SAFE · NON-TOXIC“ auf weißem Laken), bei 50 % „WEEK 4“ (Netzkarte in der Hand, Verpackungen im Hintergrund). Der Sprecher ist nicht zu sehen, es läuft nur Voiceover.

**Transkript (vollständig):**
```
[00:00] Week one versus week 12.
[00:01] What a single card pulls out of a clean mattress.
[00:03] Day one, you lift the mattress,
[00:05] lay the card flat underneath, drop it back down.
[00:07] That's the whole job.
[00:08] No spray, no plugs, no laundry.
[00:10] The lure's already working,
[00:12] drawing what's living in the foam up toward the card.
[00:14] End of week one.
[00:15] You won't see much yet, but you might notice the mornings.
[00:17] Not reaching for a tissue the second you sit up.
[00:19] The first clear breath before you're even out of bed.
[00:22] Week two, the card's been pulling quietly
[00:24] every night you slept.
[00:24] You're waking less blocked, sleeping through more.
[00:26] You stop wondering if you're coming down with something.
[00:29] Week four, this is where people text me.
[00:31] They pull the card out, hold it to the phone light,
[00:33] and there it is.
[00:33] Dark specks across a card that started clean.
[00:36] That came out of a bed you thought was fine.
[00:37] By month three, the card's done its run.
[00:39] The mattress finally feels clean at the source.
[00:42] Not for one day after laundry, for the whole stretch.
[00:45] You drop a fresh one in and forget about it again.
[00:47] No spraying, no washing.
[00:48] Just slide it in, leave it, and see what it caught.
[00:51] 30,000 plus homes, 90-day money-back guarantee,
[00:54] no return needed.
```

**Story-Muster:** **Zeitstrahl-Beweis** („Day one → End of week one → Week two → Week four → Month three“): Der Ekel-Moment kommt als Vorher/Nachher schon in Sekunde 0 („WEEK 12 🤮“). Danach folgt jede Etappe mit einem körperlichen Morgen-Signal („Not reaching for a tissue the second you sit up“). Der Erzähler tritt als Vermittler auf („this is where people text me“). Die Struktur entspricht dem MagicSplashy-Muster „erste Nacht / erste Woche / ein Monat“.

**Landingpage:** `https://truecleanhome.com/pages/capturecards-proof`, siehe LP-Analyse C.

---

## LP-Analysen (alle `shot.js` mobil, 08.10. 16:52; Dateien `a3/pages/tc_*.txt/.png/.html`)

**Gemeinsamer Befund:** Alle CaptureCards-LPs nutzen **ein Template**. Pro Angle werden nur H1, Intro und der erste Erklärabschnitt ausgetauscht, ab „Every Fix You’ve Tried Works On The Wrong Thing“ sind die Seiten identisch. Typ: **Advertorial-Listicle-Hybrid** (Problem-Advertorial plus „6 Reasons“-Liste plus Sales-Box). Die Perspektive ist „du/wir“, es gibt keinen Autor und keine Byline. **Fake-Magazin-Optik: nein.** Oben steht das TrueClean-Logo, darunter ein Before/After-Foto einer Frau um 50 (mit Taschentuch im Bett bzw. sich streckend) und eine gelbe ❌-Box mit den gescheiterten Mitteln.

### A · /pages/mites-capturecards (= /pages/capturecards-listicle) – zu Ad 1
- **H1 (wörtlich):** „Why You Wake Up Stuffy, Even After Washing Your Sheets“
- **Sub (wörtlich):** „If you spend your nights stuffed up and wake up unable to breathe through your nose... you’re not alone.“
- **Abschnitts-Überschriften (wörtlich):** Join 30,000+ Homes Sleeping Cleaner · THE REAL CAUSE „You Don’t Have an Allergy Problem. You Have a Mattress Problem.“ · WHY IT KEEPS FAILING „Every Fix You’ve Tried Works On The Wrong Thing“ · THE FIX „How One Card Draws the Mites Out and Shows You“ · WHY IT WORKS „6 Reasons People Are Switching to CaptureCards“ (1 It pulls mites out of hiding · 2 You can actually see it work · 3 No sprays, powders, or fumes · 4 Safe around kids and pets · 5 10 seconds to set up · 6 One card lasts 3 months) · THE PROOF „Proof You Can See. Results You Can Feel.“ · WHY WE BUILT IT „“With So Many Dust Mite Products Out There, We Knew Ours Had To Prove Itself.”“ · More Reasons People Won’t Sleep Without One · HOW TO USE IT „Takes 10 Seconds. No Spray. No Smell.“ · Everything you need. Nothing you don't. · REVIEWS „Don’t Take Our Word For It“ · RISK-FREE „90 Nights. See It Or Your Money Back.“ · CaptureCard™ Dust Mite Traps · Questions? Quick Answers.
- **Produkt-Einführung:** „CaptureCards“ fällt nach **383 Wörtern** (von 1.701).
- **Mechanismus:** „A hidden scent-lure draws mites off your mattress and onto the card... because mites move toward warmth and food, not away from it. They settle on the trap surface. And they can’t get back.“ Die Ursache wird so erklärt: „Dust mites live deep inside the foam and fibers, not on the surface… Washing and vacuuming never reach where they actually live“.
- **Beweise:** „In a controlled lab test, 1,206 of 1,210 mites collected on the card. That's a 99.9% capture rate.“ · Umfrage „92% Reported sleeping deeply / 95% Reported breathing better / 89% Reported waking clear-headed“ („*From our post-purchase survey“) · Bewertungen „4.8 / 5 from 5,247 verified reviews“ (in der Kaufbox dagegen „4.8 (2,100+ Reviews)“, also widersprüchlich) · 6 Kurz-Testimonials mit Vorname und Initial („My son stopped wheezing“ – David R.) · „Join 30,000+ Homes Sleeping Cleaner“.
- **Angebot/Knappheit/Garantie:** Mengenstaffel 4/8/12/20 Karten ($7.49 → $4.49 pro Karte, „MOST POPULAR“ 8, „BEST VALUE“ 12), Streichpreis „$155.88 → $59.99 · You're Saving $95.89“ · „⚠️ Capture Cards are NOT available on Amazon.“ · „AVAILABILITY NOTICE · JUNE 13, 2026 … certain batches can sell out from time to time“ · „Warning: Dust mites multiply fast in a warm, humid bedroom. Every week you wait can mean more buildup…“ · „90-Day Money Back. No Return Needed“.

### B · /pages/capturecards-listicle-airpurifier (thenaturalhousehold.co) – zu Ad 2
- **H1:** „You Already Know It’s Dust Mites — And You’ve Tried Everything.“
- **Sub:** „You’re not confused about the cause. You know it’s dust mites. You’ve read the articles, and you’ve done the covers, the sprays, the $200 purifier, the endless hot washes...“ und dann „There’s one thing none of those ever did — the one thing that actually empties the bed instead of cleaning around it. And it’s the first one you can actually see working.“
- **Abweichende H2:** „How One Card Draws the Mites Out — And Shows You“ · „You Won’t Have to Guess. You’ll See It Yourself.“ (statt „Proof You Can See…“). Alle übrigen Abschnitte sind identisch mit A.
- **Produkt-Einführung** nach **431 Wörtern** (von 1.624). Die LP **spiegelt Wort für Wort die Sprache der Ad** („the covers, the sprays, the $200 purifier, the endless hot washes“), das sorgt für Message-Match.
- Angebot und Garantie wie A.

### C · /pages/capturecards-proof – zu Ad 3
- **H1:** „You Washed These Sheets This Morning. Explain This.“
- **Sub:** „Hold the card to your phone light and see what came out of a bed you thought was clean.“ und „That stuffy nose you wake up with, the one you blame on a cold or allergies? It was never a cold.“
- **Abweichende H2:** „Two Parts: A Lure That Draws Them Out, and a Trap They Cannot Leave.“ (statt „You Don’t Have an Allergy Problem…“). Rest wie B.
- **Produkt-Einführung** nach **441 Wörtern** (von 1.634). Mechanismus wie A: „It is dust mites, buried deep in the mattress foam. Washing only touches the surface… where hot water and suction physically cannot reach.“ Angebot wie A.

### Bonus D · /pages/capturecards-menovsmite – Wechseljahre-Version (Ad 155122378, Testing)
- **H1:** „Menopause Didn't Suddenly Give You Allergies. It Made You More Sensitive To What's Living In Your Bed.“
- **Sub:** „You go to bed on time. You sleep seven, even eight hours. And you still wake up blocked, puffy, and drained. Your hormones are real. So is what's in your mattress. Only one of them has never been checked.“
- **H2:** „While Your Sensitivity Went Up, The Colony In Your Mattress Kept Growing.“ · „One Card Pulls Them Out Of The Bed. Then Shows You What It Caught.“ · „90 Nights to Finally Wake Up Rested. Or Your Money Back.“
- Der Text im Bild der Ad lautet „MENO-NOSE? / IT MIGHT BE YOUR MATTRESS. / At 3am / When you roll over / On vacation / SPECIAL DEAL / UP TO 65% OFF / THIS WEEK ONLY“. Die Ad öffnet mit: „Everyone keeps telling women over 50 the same thing. Blocked mornings? Menopause. Tired face? Menopause. Bad sleep? Menopau…“

---

## 5. Was wir für Decken ohne Bezug (UK) übernehmen

**Angle A – Hygiene (stärkste Übertragung):**
- Der Kernsatz lässt sich direkt übertragen. Aus „You wash the sheets in hot water every week. The mattress just refills them.“ wird für uns: *„You wash the duvet cover every week. The duvet inside it never gets washed.“* Aus „You can't wash a mattress. You can empty it.“ wird bei uns die umgekehrte Pointe: *„You can't really wash a duvet that lives inside a cover. You can wash ours – the whole thing.“*
- Reframe-Formel „You don't have an allergy problem. You have a mattress problem.“ übernehmen als *„You don't have a sweating problem. You have a duvet problem.“* bzw. *„…a duvet-cover problem.“*
- Die Prüffrage aus dem P.S. als Story-Wendepunkt nutzen: „Did it actually remove something from inside…?“, bei uns *„When was the last time you washed the duvet – not the cover?“*. Dazu wie in Ad 2 einen Mentor aus „hotel housekeeping“ einsetzen (in UK z. B. ein ehemaliger Hotel-Housekeeper).
- Den sichtbaren Selbstbeweis ersetzen. TrueClean hat „hold it to your phone light“, wir brauchen ein vergleichbares Ritual, z. B. das **graue Waschwasser der ersten Wäsche** oder ein Vorher/Nachher-Foto, als Zeitstrahl „Night 1 / Week 1 / Week 12 🤮“ wie in Ad 3.
- Die LP-Mechanik übernehmen: ein Template mit austauschbarer H1 je Angle, ❌-Box „you've probably tried everything“ (Bezug heiß waschen, Topper, Allergy Covers, Sprays), danach „6 Reasons People Are Switching to …“.

**Angle B – Wechseljahre:**
- TrueClean testet „Menopause Didn't Suddenly Give You Allergies. It Made You More Sensitive To What's Living In Your Bed.“ / „Your hormones are real. So is what's in your mattress. Only one of them has never been checked.“ Diese Kombination aus A und B passt sehr gut zu uns: *„Your hot flushes are real. So is what's soaking into your duvet every night. Only one of them goes in the wash.“* (UK: „hot flushes“ statt „hot flashes“).
- Die Ad-Formel „Everyone keeps telling women over 50 the same thing… Menopause.“ funktioniert als Hook für Frauen, die alles auf die Hormone schieben.

**Angle C – Beziehen:**
- TrueClean begründet die Kaufentscheidung mit Erschöpfung: „to keep it that way you have to strip the bed and wash everything constantly. At my age, I just don't have the energy to keep that up.“ sowie „By our age, who has the energy to strip the bed, haul the matt…“ (135489754). Daraus wird bei uns: *„At my age I don't have the energy to wrestle a king-size duvet back into its cover every week – so I stopped washing it.“* Das verbindet C mit A, denn die Bettdecke wird nicht gewaschen, weil das Beziehen so mühsam ist.

**Angle D – Tochter kauft für Mutter:**
- Der neue Test 201101007 nutzt den Rahmen „My mom washed sheets the way her mom taught her: hot water, every week, no shortcuts. And for years she still woke up stuffy.“ und erzählt dabei als Tochter über die Mutter. Die Gewohnheit wird nicht kritisiert („Sometimes the habit isn’t wrong. It’s just missing the one layer nobody told you about.“). Daraus wird bei uns: *„My mum has washed her duvet cover every Sunday for 40 years. The duvet inside? Never.“* Die Tochter entdeckt das Problem, die Mutter bekommt die Lösung, und die Sprache bleibt respektvoll.
- In 15 Sekunden einsatzbereit, nichts muss nachgekauft werden: Die Botschaft „10 seconds to set up“ entspricht bei uns *„no cover, nothing to wrestle“*. Das ist ein Kaufgrund für die Tochter, die ihrer Mutter Arbeit abnehmen will.

**Formales für UK:** Persona-Seiten mit neutral-redaktionellen Namen (vgl. „The Natural Household“, „Clean Home Review“) und Native-Post-Bilder mit „… Read more“-Balken auf Amateurfoto lassen sich übertragen. **Nicht übernehmen:** widersprüchliche Bewertungszahlen (5,247 vs. 2,100+), das starre Datum der „Availability Notice“ sowie Labor-Behauptungen ohne Beleg. Für UK gelten die ASA/CAP-Regeln (Substantiierung von Claims, Advertorial-Kennzeichnung).

## Lücken
- Für keine der drei Ads gibt es Spend- oder Reichweitendaten (US, ohne EU-Transparenz). Die Stärke ist nur über Laufzeit, Performance-Score und Varianten belegt.
- Der Primärtext von 155122137 stammt aus den textgleichen Cluster-Varianten 155122245/155122220. Die ID selbst wurde nicht einzeln per `get_ad` abgefragt.
- Ad 127732600 hat 2 Media, `get_ad_media` lieferte aber nur 1 Bild. Das zweite Medium ist nicht gesichtet.
- Das Ich-Story-Advertorial `truecleanhome.com/pages/household-report` (H1 „Why You Can Sleep 8 Hours and Still Wake Up Like the Night Never Counted“, siehe `sweep_gethooked_hooks.md`) gehört zu keiner der drei Top-Ads und wurde hier nicht neu zerlegt.
- Die inaktive Historie (`status=inactive`) der drei Seiten wurde aus Zeitgründen nicht gesichtet. Die Marke ist seit April 2026 aktiv, die CaptureCards-Ads seit Juni.
