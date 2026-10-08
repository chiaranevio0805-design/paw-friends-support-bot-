# Marken-Deep-Dive: Rest – Evercool® Cooling Comforter (Kühl-Bettdecke, ohne Bezug nutzbar)

Stand: 08.10.2026, ca. 17:10 Uhr (UTC), Agent 3, zweiter Lauf. Quellen: GetHookd (`get_domain_advertisers`, `search_ads` aktiv/inaktiv/Query, `get_ad`, `transcribe_ads`/`get_transcription_status`) sowie die mobilen Seitenabrufe `a3/pages/rest_pdp.*` und `a3/pages/rest_meno6.*`. Zitate stehen wörtlich in der Originalsprache. Rohnotizen liegen in `a3/deep3/_notes.md`, der Volltext der Story-Ad in `a3/deep3/body_182116197.txt`.

| Feld | Wert |
|---|---|
| Produkt | Evercool® Cooling Comforter: eine Kühl-Bettdecke. **Wichtig für uns:** Laut PDP-FAQ ist sie ausdrücklich für die Nutzung **ohne Bezug** gedacht: „Do I need a duvet cover with the Evercool® Cooling Comforter? No. The Evercool® Cooling Comforter is designed to be used on its own, so the cool touch fabric rests directly against your skin, and it is machine washable so it does not need a protective cover.“ Das ist also dieselbe Produktgattung wie unsere. |
| Preis (PDP 08.10.) | Twin $199 → $139 („PRIME TIME SALE“, „30% OFF“, „Valid Until 10/11“), 4.8 Sterne aus 8,445 Bewertungen, „HSA/FSA Eligible with Truemed“ |
| Meta-Seiten (Domain-Advertiser rest.com, 08.10., 16:48) | **Rest** 28140 (589 aktive Ads auf der Domain, first_seen 07.05.), **Hot Sleeper Journal** 7097606 (11, seit 04.09.; Persona-/Magazin-Seite), Creator-Seiten **emmvuu** 10993508 (2), **Laura On A Mission** 11625816 (1), **AJ Core Performance** 28387891 (1), **Caroline Zawadzki** 28387893 (1). 6 Seiten, keine Kappung (`truncated: false`). |
| Domains | rest.com, restduvet.com, au.rest.com |
| Markt / Sprache | USA (alle geprüften Ads `countries: US`), Englisch. Laut Domains auch Australien. **Kein UK-Shop gefunden.** |
| Native-/Story-Nachweis | **Ja, aber schmal.** Es gibt nur eine Persona-Magazin-Seite („Hot Sleeper Journal“, 11 Ads, alle eine Story) und einige Creator-Whitelisting-Seiten. Die Markenseite fährt überwiegend PDP-Werbung (Rabatt, Awards, UGC-Testimonials). Die Wechseljahre-Listicles (`/pages/menopause-science-v6`, `/pages/menopause-proof-v7/v8`) existieren im Web, sind in GetHookd aber **nicht als Ad-Ziel** belegt (siehe `sweep_web.md`). |

## 1. Inventar und Erfolgssignale

- **Rest aktiv (586 Treffer, sortiert nach Laufzeit, collapse):** 97674605 Bild 155 T „Up to 40% Off + Free Gifts“ (Black-Friday-Text, Winning, 6 Varianten), 106946437 Karussell 120 T (Winning), 163683600 Video 51 T „The Cooling Sheet Set That Sold Out 5x This Year“ (Winning, 3 Varianten). Alle führen auf PDPs. Achtung: Der Index hielt bei dieser Abfrage 30 Zeilen zurück („withheld“), die Liste ist also unvollständig.
- **Rest inaktiv (ab 06/2025, 6.953 Treffer):** sehr lange DCO-/UGC-Läufer: 23146918 DCO 315 T (05.06.2025–15.04.2026), 23650843 DCO 312 T (18 Varianten), 26502459 DCO 303 T. Dazu eine ganze Welle von **Creator-Whitelisting-Videos** 30297003–30297046, alle vom 11.07.2025 bis 21.04.2026 (285 T), mit den Titeln „The "Cooling Comforter" That Sold Out 4x Last Year“ bzw. „94% Sleep Better With This "Cooling Comforter"“. Deren Hooks reichen von „Have hot flashes? Just a hot sleep…“ (30297024) über „as a new mom…“ bis „Especially if you’re pregnant“.
- **Wechseljahre (strenge Suche „menopause“ in Rest):** 8 Treffer. Aktiv ist nur 175766490 (Winning). Der Langläufer 30297004 (278 T) ist über das Sweep-Ergebnis belegt.
- **Spend:** GetHookd liefert für alle geprüften Rest-Ads keinen Spend-Bucket (US, keine EU-Transparenz).

## 2. Auswahl der 3 stärksten Native-/Story-Ads

| Rang | Ad | Begründung |
|---|---|---|
| 1 | **182116197** Hot Sleeper Journal – Ich-Story „I stole a comforter from a hotel…“ | Einzige echte Persona-/Magazin-Seite der Marke. **11 Ads = 1 Story-Cluster** (`variant_count` 11), aktiv seit 04.09. (35 T), Performance „Growing“. Langes Story-Native (7.252 Zeichen) mit der Erzählerin „Marina, 46, Texas“ und einem verdeckten Wechseljahre-Rahmen („before I turned 40-something… hot sweaty mess… up by 3:47am“). Dieselbe Hotel-Diebstahl-Schablone nutzt auch FluffCo, sie ist also bewährt. |
| 2 | **30297004** Creator-Video „Let's talk about sleep… woman in menopause like I am“ | **278 T** Laufzeit (11.07.2025–14.04.2026; endete im 6-Monats-Fenster), 3 Media-Varianten. Ich-Story-UGC mit explizitem Wechseljahre-Angle. Längster Wechseljahre-Läufer einer Bettdecken-Marke im Datensatz. |
| 3 | **175766490** Testimonial-Video „Good morning. So there is this thing… it's called menopause.“ | Aktiv (seit 11.09., 28 T), **„Winning“**, die einzige aktive Ad mit „menopause“ im Text. Gekennzeichnete Partner-Ad („#MeNoPause with @rest #ad“). Ich-Perspektive im Bett, humorvoll. |

---

## Ad 1 · 182116197 – Hot Sleeper Journal: „I stole a comforter from a hotel in Charleston…“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/182116197?signature=f72aa798b79363f7f2b6fc3e17ab0d03ac0423b9e87c9bee5948803db09de37d |
| Seite/Persona | Hot Sleeper Journal (7097606), eine Magazin-artige Seite. Die Ad-Headline ist der Seitenname. |
| Status | aktiv (letzte Sichtung 06.10.) |
| Start / Ende / Laufzeit | 04.09.2026 / – / 35 T |
| Format | Bild · facebook, instagram, messenger, threads |
| CTA | SHOP_NOW · link_description – |
| Spend / Score / Varianten | kein Spend · 66 „Growing“ · 11 Ads mit identischem Text (alle 11 aktiven Ads der Seite) |
| LP | https://rest.com/products/evercool-comforter (PDP) |

**Headline:** „Hot Sleeper Journal“

**Text im Bild:** kein Text. Amateurhaftes, dunkles Handyfoto: Eine Frau schläft unter einer hellblauen Steppdecke, daneben ein Nachttisch mit Lampe. Das Bild wirkt wie ein privates Foto, nicht wie Werbung.

**Primärtext (wörtlich, vollständig; 7.252 Zeichen / 1.352 Wörter; die Marke „Rest“ fällt erst nach 794 Wörtern):**
> I stole a comforter from a hotel in Charleston while I was in town for my niece’s wedding last spring. I'm not proud of it.
>
> The general manager emailed me three days after we checked out.
>
> It was the third night of the trip. We had been at the hotel for three nights and I was sleeping the way people sleep in commercials.
>
> Out cold. Not a single wake-up, not one leg kicked out from under the comforter looking for cool air.
>
> The kind of sleep I used to have before I turned 40-something and my nights turned into a hot sweaty mess— at home I'm 46, I sleep on my side, and most nights I'm up by 3:47am peeling the comforter off, then pulling it back on, then off again, already doing the math on how wrecked I'm going to be tomorrow.
>
> On the first night, I thought it was the mattress.
>
> On the second night, I thought it was the wine.
>
> On the third night, I lay there at 7:30am, having slept eight hours uninterrupted, and I thought: it's the comforter.
>
> I never woke up too hot. I needed this comforter.
>
> No 2am wake-up, kicking the comforter off and pulling it back on.
>
> No lying there doing math about how many hours of sleep I had left.
>
> I've been what I'd call a hot sleeper for a while now — I run warm, especially at night, for reasons I've mostly stopped trying to diagnose — and this was the first time in longer than I want to admit that I hadn't woken up hot.
>
> I checked for the tag. There wasn't one. I called the front desk.
>
> "Hi, I'm in 214 — can you tell me what brand your comforters are? I'd love to get one."
>
> Long pause.
>
> "I'm so sorry, that's actually one of our proprietary amenities, we're not able to share the supplier."
>
> I asked if they sold them in the gift shop. They didn't.
>
> I asked if there was a way to be notified if they ever did. There wasn't.
>
> I hung up and told my husband. He didn't even look up from his book.
>
> "You're gonna take it, aren't you?"
>
> "I am absolutely going to take it."
>
> "You know they're gonna know it was you."
>
> "They can keep the incidentals deposit or something"
>
> That morning, after breakfast, I rolled the comforter up small, and stuffed it into the bottom of my suitcase under my shoes.
>
> My heart was racing.
>
> My husband watched the entire operation from the bed, laughing, occasionally offering unhelpful commentary like "maybe use the laundry bag, it's more discreet" and "I want it on record I said this was a bad idea."
>
> We checked out by 11am. Flew back home. Unpacked the next day at 2pm.
>
> I put the comforter on my bed.
>
> I slept perfectly for another 2 nights.
>
> Then on the third day, an email showed up. Subject line: "A Small Matter From Your Recent Stay."
>
> It was from the general manager. Polite. Almost amused, honestly.
>
> Dear Mrs. Santana,
>
> Our housekeeping team flagged, during checkout inventory for room 214, that the comforter was unaccounted for. I want to be clear that we're not assuming anything by writing — items get left behind, packed by accident, or simply misplaced more often than guests realize. That said, if it is the case that you wanted to take it home with you, we would like the opportunity to offer it to you formally.
>
> For what it's worth, that particular comforter is custom-made for us by a supplier we work with exclusively, so it isn't something we're able to offer for purchase through the hotel. If you're willing to let me know either way, I can close this out on my side with no issue at all.
>
> Warmly,
>
> Carolyn, General Manager
>
> I'd been sleeping like a different person on a comforter I'd stuffed in my suitcase, and now the general manager of a hotel I'd stayed at for one weekend had emailed me — not with a bill, not with a warning, just genuinely and kindly asking whether I'd taken it.
>
> I showed my husband. He read it twice and then laughed so hard he had to sit down.
>
> "You got caught."
>
> I wrote back and confessed. I offered to pay for it.
>
> They said not to worry about it, called it a parting gift, and even refunded the incidentals deposit. They really wanted that five-star review.
>
> Then in July, at a dinner with my girl friends, the hotel story came up — because at this point it's the only genuinely interesting thing I've ever done — and my friend Jen who's an interior designer, said "I think I know the mystery brand of your stolen comforter. Look up Rest, they make the Evercool Cooling Comforter. Tell me if I'm right."
>
> I looked it up. Read the description.
>
> It wasn't just "cooling" in the vague way everything claims to be cooling — it actually explained why: the fibers are ultr-thin and made for pulling heat away from your body heat instead of just trapping it under the covers.
>
> A lab test found Evercool to be cooler than silk, cotton, or bamboo.
>
> I didn't know that was something you could actually put a number on.
>
> "You could be right, Jen."
>
> I wasn't sure if it was the same one but I ordered it because I wasn't thrilled about sleeping with a stolen hotel comforter.
>
> It arrived on a Tuesday. I put it on the bed that night.
>
> It was cold, even cooler than my precious stolen comforter, and it was still cold when I woke up at 7am for work.
>
> I slept through the whole night without a drop of sweat.
>
> Without waking up hot once. Only turned a few times as I was falling asleep, then out like a light until I got up for work.
>
> About two weeks in, my husband rolled over one morning and said, "You've stopped doing the thing."
>
> "What thing?"
>
> "The 3am huffing and kicking thing."
>
> "Yea I sleep like a baby now that all your body heat isn't getting trapped under the covers" which I was just teasing him about, but it's true I sleep like an angel now.
>
> I'm less anxious when I wake up knowing I'm full rested and I'm in a way better mood when I get good sleep.
>
> I can't believe I went so long waking up cranky everyday when this comforter was just out there existing without me knowing.
>
> It's also machine washable, which matters, because I am not about to hand-wash a comforter for the rest of my life the way I apparently would have for a stolen hotel one if I'd never found anything better.
>
> I still think about that hotel sometimes. I hope whoever's in 214 is sleeping okay.
>
> If you are reading this and you're the kind of person who wakes up hot, or sweaty, tosses and turns, sticks out limbs from the covers… I understand you completely, and I'd like to save you the email from the general manager of a hotel.
>
> It's Rest. It ships free, machine washable, and comes with a 1 year warranty.
>
> Right now they're running an end of summer sale and it's the biggest sale I've seen from them yet.
>
> I just grabbed another set for the guest room. Sometimes I go to sleep there when I'm sick so it'll be nice to have.
>
> — Marina, 46, Texas
>
> P.S. — My husband still brings up the hotel story at dinner parties. He now also brings up that I "finally parted with it and just bought the real thing," which is true, but it was an easy choice.
>
> P.P.S. — Get the bundle with the comforter and sheet set together. A lot of heat can get released through the comforter but when I got the sheet set I could feel the difference in how much cooler I was underneath too.
>
> P.P.P.S — I have not been back to that hotel. I want to. But I'm sure my picture is taped to the back of the front desk so the staff can see who to call security on.

**Story-Muster:** **Geständnis-Hook mit kleinem Verbrechen** („I stole a comforter… I'm not proud of it.“), dann ein Spannungsversprechen („The general manager emailed me…“), dann ein **Ausschluss-Dreischritt** („first night… mattress / second night… wine / third night… it's the comforter“), dann das Geheimnis (Hotel nennt den Lieferanten nicht), dann Diebstahl-Szene mit Ehemann als komischem Sidekick, dann der Brief des Managers (wörtlich zitiert, wirkt glaubwürdig), dann **Auflösung durch eine Freundin mit Fachwissen** („Jen who's an interior designer“), dann Mechanismus und Laborbeleg in 3 Sätzen, dann Ergebnis aus Partnersicht („You've stopped doing the thing.“ – „The 3am huffing and kicking thing.“), dann Waschbarkeit als Nebensatz, dann Angebot, dann Signatur mit Name/Alter/Ort und **drei P.S.** (Bundle-Upsell im P.P.S.). Wechseljahre werden nie genannt („40-something… for reasons I've mostly stopped trying to diagnose“). Die Zielgruppe erkennt sich, ohne dass ein Gesundheitsversprechen gemacht wird.

**Landingpage:** PDP `https://rest.com/products/evercool-comforter`, siehe LP-Analyse unten. Es gibt keine eigene Story-LP: Die Story steckt komplett im Ad-Text.

---

## Ad 2 · 30297004 – Creator-Video „woman in menopause like I am“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/30297004?signature=9c76a6aae73a1520cfb85e881230dfdc0c0927e2bcdf2b22f13fdbccfd335bc1 |
| Seite/Persona | Rest (28140). Die Ad läuft auf der Markenseite, der Text ist aber in Creator-Ich-Form geschrieben („@rest.bedding“). |
| Status | inaktiv |
| Start / Ende / Laufzeit | 11.07.2025 / 14.04.2026 / **278 T** |
| Format | Video 69 s (3 Media-Varianten mit identischem Ton) · facebook, instagram, audience_network, messenger, threads |
| CTA | LEARN_MORE „Learn more“ |
| Spend / Score | – / – (alte Ad, keine Scores) |
| LP | https://rest.com/products/evercool-comforter (PDP) |

**Headline:** „94% Sleep Better With This "Cooling Comforter"“

**Primärtext (wörtlich, vollständig):**
> For women navigating menopause, I know what a challenge restful sleep can be! Even with the A/C set to “snowing” 😆 , it’s never quite cool enough to keep the hot flashes away! That’s why I wanted to share this cooling comforter from @rest.bedding —it’s made with breathable, moisture-wicking fabric that is so soft and can help regulate body temperature and keep you comfortable and cool through the night.
>
> It’s been such a simple way to support better sleep, even during those tough nights. If you’ve been struggling with hot flashes or night sweats, this might be worth exploring. 💕

**Bild/Video:** Talking-Head einer blonden Frau in kariertem Flanellhemd. Sie sitzt vor einem Bücherregal auf Bett bzw. Boden, eine graue Steppdecke liegt im Schoß, sie trägt zwischendurch eine Schlafmaske. Weiße Untertitel-Box im Wort-für-Wort-Stil (Still: „I wish I could wear this all“).

**Transkript (vollständig):**
```
[00:00] Let's talk about sleep for a minute because if you're a woman in menopause like I am,
[00:04] I know that sleep does not come easy and the hot flashes and the night sweats don't make it any easier,
[00:11] but I have recently discovered something
[00:14] that has helped me tremendously. It is this cooling comforter from Rest.
[00:22] First of all, it is the softest thing I've ever felt. I wish you could feel it through the screen. And
[00:27] secondly, it is literally like cold. Like I have it on my legs. It feels like I have a cold
[00:35] pack on my legs. It keeps you cool.
[00:39] It really is incredibly helpful. In fact, both of my teenagers are
[00:45] wanting to steal it and asking for them. I also got this cooling mask.
[00:51] Oh my gosh, I wish I could wear this all the time like in public because it's so soothing on the eyes.
[01:01] But you have to check this out. And if you comment down below with sleep,
[01:06] I will send you more info.
```

**Story-Muster:** **Selbst-Identifikation als Peer** („a woman in menopause like I am“), dann Problem (hot flashes/night sweats), dann Entdeckung („recently discovered something“), dann zwei Sinneseindrücke („softest thing I've ever felt“, „like I have a cold pack on my legs“), dann **sozialer Beweis aus der Familie** („both of my teenagers are wanting to steal it“), dann Cross-Sell (Schlafmaske), dann eine organische CTA („comment down below with sleep“), die erkennbar aus dem Original-Creator-Post übernommen ist.

---

## Ad 3 · 175766490 – „#MeNoPause with @rest“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/175766490?signature=53c2958ed27005a27439cfd8fcce153ed15d3c046df4e52dc85cc82432724af0 |
| Seite/Persona | Rest (28140). Gekennzeichnete Partner-Ad einer Frau („#ad“). Ihre Identität wurde nicht verifiziert. |
| Status | aktiv |
| Start / Ende / Laufzeit | 11.09.2026 / – / 28 T |
| Format | Video ca. 46 s · facebook, instagram, threads |
| CTA | SHOP_NOW „Shop now“ |
| Spend / Score | – / **Winning** · 1 Variante |
| LP | https://rest.com/products/evercool-comforter (PDP) |

**Headline:** – (leer)

**Primärtext (wörtlich, vollständig):**
> Menopause can be a wild ride and everybody’s experience is different.
>
> Because menopause is part of life. And there’s no reason we can’t talk about it, laugh about it, support each other through it. And keep going.
>
> Better sleep isn’t a luxury during menopause; it’s a necessity. Trust me, @rest evercool bedding will change your life. It’s my magic solution.
>
> #MeNoPause with @rest #ad

**Bild/Video:** Ein Selfie-Video im Bett: Die Frau liegt auf einem weißen Kissen, an der Wand hängen gerahmte Herbarium-Drucke. Die Hook-Stills (0/1/3 s) zeigen kein Text-Overlay.

**Transkript (vollständig):**
```
[00:00] Good morning.
[00:01] So there is this thing, you might have heard about it,
[00:05] it's called menopause.
[00:06] There's like a movement wanting to happen called menopause,
[00:10] which means like, I don't have time for you menopause.
[00:13] Oh, it sounds like a really good goal.
[00:15] One of the hardest things about not sleeping
[00:20] is not sleeping.
[00:22] Well, I have a solution for you.
[00:26] Rest bedding.
[00:27] One thing that I do is I cool myself down with rest bedding.
[00:32] If you want a really good night's sleep,
[00:35] you wanna stay cool, you wanna be cool, rest bedding.
[00:40] Everyone in my house fights over the rest bedding.
[00:43] There really is nothing like a good night's sleep.
```

**Story-Muster:** „Morgen-im-Bett“-Selfie-Testimonial: Enttabuisierung mit Humor („Me-No-Pause… I don't have time for you menopause“) statt Leidensgeschichte. Die Lösung wird früh genannt (0:26), gefolgt von **sozialem Beweis im Haushalt** („Everyone in my house fights over the rest bedding“). Story-Tiefe ist gering, der Ton aber nah und nicht werblich.

---

## LP-Analyse

### PDP `rest.com/products/evercool-comforter` (Ziel aller drei Ads; `shot.js` mobil 16:50, 2.447 Wörter)
- **Typ:** PDP (Produktseite), keine Fake-Magazin-Optik.
- **H1 (wörtlich):** „Evercool® Cooling Comforter“ · **Sub:** „Award-Winning Comforter for Hot Sleepers“ · Badges „PRIME TIME SALE“, „#1 BEST SELLER“, „4.8 (8,445)“
- **Abschnitts-Überschriften (wörtlich):** SleepScore™ Labs Validated · 4x Good Housekeeping Award Winner · OEKO-TEX® Standard 100 Certified · What people are feeling · What people are saying · Proprietary Evercool® Cooling Fabric · See It In Action: · Scientifically Proven, Third-Party Tested* · The Science of Evercool® · Rest® Labs · How Evercool® Compares (Evercool®/Silk/Bamboo/Cotton) · Sleep Expert Approved · Frequently Asked Questions · Explore Evercool® Bedding · Transform Your Sleep · dazu ein Abschnitt zu einer prominenten Markenpartnerin (Überschrift mit Vornamen).
- **Produkt-Einführung:** sofort (PDP). „Menopause“ taucht erst nach 1.019 Wörtern auf (Award „Menopause O-wards 2025“, Oprah Daily), „night sweats and hot flashes“ nach 1.755 Wörtern in der FAQ.
- **Mechanismus (wörtlich):** „The Evercool® Cooling Comforter cools through the structure of the fabric itself, not through chemical coatings or cooling additives, so the effect does not wash out or fade.“ und „The Evercool® fabric pulls moisture away from your skin and dries quickly, while the cool touch surface helps take the edge off the temperature spikes that wake hot sleepers.“
- **Beweise:** „97% found the cooling sensation better compared to a regular comforter / 94% reported that the comforter helped improve their overall sleep quality / 88% experienced better temperature regulation“ („*SleepScore Labs conducted a scientific study which analyzed over 1000 nights of sleep.“) · SGS-Qmax „0.433 watts per square centimeter, compared to 0.19 for silk, 0.15 for bamboo, and 0.11 for cotton“ · „Good Housekeeping Bedding Award four years in a row, from 2023 through 2026“ · OEKO-TEX Class I, „no detectable PFAS and no detectable BPA“ · KI-Zusammenfassung der Bewertungen.
- **Angebot/Knappheit/Garantie:** „Prime Time Sale | Up to 30% Off… Limited Time. Valid Until 10/11.“ · Gratis-Geschenk-Stufen ($99 Free Shipping / $199 Free Express Shipping / $299 Free Eyemask) · „4 payments of $34.75“ · „30-NIGHT RETURNS“ (Erstattung mit „10 dollar flat fee“) · „1-YEAR WARRANTY“ · „HSA/FSA ELIGIBLE“.
- **Waschen und Bezug (FAQ, wörtlich):** „The Evercool® Cooling Comforter is fully machine washable at home. Machine wash cold, then tumble dry on low heat or drip dry.“ sowie „Do I need a duvet cover…? No. … designed to be used on its own… machine washable so it does not need a protective cover.“

### Bonus: Wechseljahre-Listicle `rest.com/pages/menopause-science-v6` (kein belegtes Ad-Ziel; 1.187 Wörter)
- **Typ:** Marken-Listicle (Rest-Layout, Countdown-Timer „:07:55“ oben), keine Fake-Magazin-Optik, „wir“-Perspektive.
- **H1 (wörtlich):** „6 Reasons Women In Menopause Are Switching To The Evercool® Comforter“
- **Sub (wörtlich):** „To fall and stay asleep, your core temperature has to drop. Down and microfiber comforters hold warmth in, so the heat has nowhere to go and you're soaked at 3AM. Not the Evercool® Cooling Comforter.“
- **H2 (wörtlich):** THE PROBLEM „It's not just you, it's also your bedding.“ · 01 „You stay cool at 3AM, not just at lights-out“ · 02 „It's measurably cool to the touch“ · 03 „You don't wake up damp“ · 04 „Tested with women who actually have night sweats“ · 05 „Nothing in it you'd worry about“ · 06 „Thirty nights to decide“ · „What women with night sweats say“ · „After six weeks with Evercool®, here’s what real women said:“
- **Produkt** im ersten Absatz (Marken-Listicle). **Beweis:** „The study followed 40 women, ages 40 to 60, all dealing with night sweats or hot flashes“, „97% of the women said it felt cooler“, „100% enjoyed using it / 97% planned to keep using it… / 78% would not go back to traditional bedding“. Testimonials: „At 53, I have hot flashes and night sweats. Although this comforter can’t completely stop them from happening, it can make me a whole lot more comfortable when they do happen.“ (Marietta F.) und „When having multiple hot flashes at night, I just rotate comforter to a cooler side…“ (Donna W.).
- Problem-Satz (wörtlich): „You've assumed the problem is your body. It isn't just your body. Cotton and down comforters are insulators. They trap the heat you're trying to shed and hold it against your skin until you wake up and push everything off.“

---

## 5. Was wir für Decken ohne Bezug (UK) übernehmen

**Angle B – Wechseljahre (Hauptlehre):**
- **Die Hotel-Diebstahl-Story als Schablone** (Ad 1) übernehmen, mit UK-Setting: eine Hochzeit in den Cotswolds, ein Hotel in Edinburgh. Die Struktur bleibt: Geständnis, Ausschluss-Dreischritt (Matratze? Wein? Nein, die Decke), Geheimnis, Brief des Managers, Freundin löst auf, Partner bemerkt „You've stopped doing the thing.“, Signatur „— Name, 52, Surrey“, P.S.-Kaskade. Wichtig ist die indirekte Wechseljahre-Ansprache („before I turned 40-something… for reasons I've mostly stopped trying to diagnose“), weil sie keinen Gesundheits-Claim braucht (ASA-sicherer).
- Problem-Reframe aus der Listicle: „It's not just you, it's also your bedding.“ bzw. „Cotton and down comforters are insulators. They trap the heat…“. Bei uns kommt ein zusätzlicher Hebel dazu: **Decke plus Bezug sind zwei Schichten, die Wärme stauen.** Daraus wird: *„A duvet inside a cover is two layers of insulation. No wonder you're soaked at 3am.“*
- Konkrete Uhrzeiten („3:47am“, „3AM“) und Partner-Zitate („The 3am huffing and kicking thing“) bringen Glaubwürdigkeit. UK-Begriff: „hot flushes“.

**Angle A – Hygiene:**
- Rest nutzt Hygiene kaum. Waschbarkeit kommt nur als Nebensatz vor („It's also machine washable, which matters…“). Das ist unsere Lücke: Dieselbe Story-Form, aber mit Waschbarkeit als Wendepunkt. Rests eigene FAQ liefert das Argument: „machine washable so it does not need a protective cover“, also *„no cover needed because you wash the duvet itself“*.

**Angle C – Beziehen:**
- Rest verkauft dieselbe Gattung („designed to be used on its own“), wirbt aber nicht damit. Wir können als erste das Story-Motiv „Ich musste nicht mal einen Bezug draufziehen“ besetzen. Passende Szene in der Hotel-Story wäre: „It arrived on a Tuesday. I put it on the bed that night.“, bei uns ergänzt um *„– no cover, no wrestling, straight on the bed.“*

**Angle D – Tochter kauft für Mutter:**
- Rest nutzt Familien-Begehrlichkeit: „both of my teenagers are wanting to steal it“ (Ad 2), „Everyone in my house fights over the rest bedding“ (Ad 3), „I just grabbed another set for the guest room“ (Ad 1). Daraus wird eine Diebstahl-Variante für D: *„My mum stayed in our guest room for a week. When she left, so did the duvet.“* Die Tochter kauft daraufhin der Mutter eine eigene. Das ist dieselbe komische Fallhöhe wie im Hotel-Original.

**Formales:** Eine Persona-Seite mit Magazin-Namen (bei Rest „Hot Sleeper Journal“), die Seitenname als Headline nutzt und ein privates, unperfektes Handyfoto ohne Text zeigt. Mit 11 identischen Ads wird eine Story breit getestet. Rest leitet trotzdem auf die PDP. Wir sollten das A/B testen: Story-Ad → PDP gegen Story-Ad → Listicle.

## Lücken
- Für keine Rest-Ad liegt Spend oder Reichweite vor (US, keine EU-Transparenz).
- Die Wechseljahre-Listicles `/pages/menopause-*` sind nur im Web belegt. Eine Meta-Ad mit diesem Ziel wurde nicht gefunden (Abfragen dazu in `sweep_web.md`).
- Bei der Abfrage aktiver Rest-Ads hielt GetHookd 30 Zeilen zurück. Die Liste der aktiven Langläufer ist daher unvollständig.
- Die Creator-Seiten (emmvuu, Laura On A Mission, AJ Core Performance, Caroline Zawadzki; je 1–2 Ads seit September) wurden nicht einzeln gesichtet.
- Für Ad 1 und Ad 3 wurde kein separater `get_ad_media`-Batch abgerufen. Die Bilder bzw. Hook-Stills kamen mit `get_ad`/`search_ads` (Ad 1: Foto ohne Text; Ad 3: drei Hook-Stills ohne Overlay; Ad 2: drei Poster-Frames mit Untertitel).
