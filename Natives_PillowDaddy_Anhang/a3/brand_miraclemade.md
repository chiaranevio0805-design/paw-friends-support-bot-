# Marken-Deep-Dive: Miracle Made / Miracle Brand (Silber-Bettwäsche) inkl. Persona-Netze „try.miraclebrand.co“ und „The Granny Blog“

Stand: 08.10.2026, ca. 17:15 Uhr (UTC), Agent 3, zweiter Lauf. Er baut auf dem ersten Lauf auf (`a3/deep_mir/_notes.md`, LP-Abrufe 11:53). Quellen: GetHookd (`get_domain_advertisers`, `search_ads`, `get_ad`, `transcribe_ads`) und mobile Seitenabrufe mit `tools/shot.js` (`a3/pages/mir_*`). Zitate stehen wörtlich in der Originalsprache. Volltexte liegen in `a3/deep3/body_147817064.txt`, `a3/deep_mir/body_99445068.txt` und `a3/deep_mir/body_190372791.txt`.

| Feld | Wert |
|---|---|
| Produkt | „Miracle Made® Sheets“ (früher „Miracle Sheets“): silberbehandelte Baumwoll-Bettwäsche (Spannbettlaken, Laken, 2 Kissenbezüge) plus „free 3-piece towel set“. Versprechen: „Helps prevent up to 99.7% of bacteria growth“, „Self-cleaning: Fewer odors. Up to 3x less laundry.“, „Advanced temperature regulation“. **Keine Bettdecke**, aber das gleiche Hygiene-/Schwitz-Problem wie bei uns. |
| Firma | „PATTERN BRANDS LLC“, Jersey City (LP-Footer) |
| Preis (LP `/sheets/ksp`, 08.10.) | Queen „$224 → $149“, Full „$214 → $139 · 35% OFF - YOU SAVE $75“; Banner „UP TO 46% OFF AUTO-APPLIED“ |
| Domains | miraclebrand.co, miraclemade.co, restmiracle.com, **try.miraclebrand.co** (LPs); Affiliate-Presell: **thegrannyblog.com** (`/miracle-gma/`, `/miraclefbv2-get/`) |
| Markt / Sprache | USA, Englisch |
| Native-Nachweis A – eigenes Persona-Netz (Domain-Advertiser `try.miraclebrand.co`, 08.10., 16:48) | Miracle Brand 3177 (275), **Chelsea Turano** 26340610 (71, neu seit 05.10.), **The Savvy Neighbor** 8456 (45, seit 30.06.), **All things beautiful by Janelle** 26340617 (39, 05.10.), **Meredith Little** 26340606 (32, 05.10.), **Sarah Thompson** 7103244 (20, seit 29.06.), **Bedroom Insider** 7494139 (19, seit 20.07.), **Offline Granny** 7103253 (9, seit 29.06.), Life of Chef Mom 104009 (4), Healthy Living 7494142 (2), The Daily Comfort Guide 11330499 (1). Das sind **10 Persona-/Magazin-Seiten** plus Markenseite. Die Seiten heißen wie Menschen („Sarah Thompson“), Nachbarn („The Savvy Neighbor“), Oma-Blogs („Offline Granny“) oder Magazine („Bedroom Insider“, „The Daily Comfort Guide“). |
| Native-Nachweis B – Affiliate-Netz The Granny Blog (Domain-Advertiser `thegrannyblog.com`, 08.10., 11:55, erster Lauf) | Mark Davis 13039094 (760 aktive Ads), Lifed 88032 (463), Rachel Monroe 14234590 (447), Cammy Bennett 15227765 (403), Julia Dawson 19855729 (148), Olivia Taylor 17346087 (91), Melissa Taylor 1286792 (81), Sophia Miller 15172500 (1), zusammen **~2.394 aktive Ads auf 8 Personas**. Früher kam James Moore 4554328 dazu (4.458 inaktive Ads). Die Links laufen über `sub1/sub2/sub3` und k34mtrk.com, es handelt sich also um ein **Affiliate-Media-Buyer-Netz**. Dieselben Personas bewerben auch fremde Produkte (Neuropathie, Kollagen, Alarm-Gadgets). Typisch: sehr viele Ads mit kurzer Lebensdauer (längste Granny-Blog-Miracle-Ad: 43 T). |

## 1. Erfolgssignale

- **Markenseite 3177:** 357 aktive Ads (erster Lauf). Die Top 40 nach Laufzeit laufen alle 93–102 T und führen alle auf das Listicle `try.miraclebrand.co/a/s6-reasons`. Typisch sind Marken-/DR-Copy und UGC, z. B. 115189525 „Self Cleaning: Fewer Odors, 3x Less Laundry!“ (Gründer-Talking-Head, 102 T). Die Markenseite selbst fährt kaum Storys.
- **Eigenes Persona-Netz (die eigentlichen Natives):** Die Ads laufen seit dem 29./30.06. ununterbrochen, also **101–102 T**, mehrere davon „Winning“ mit Performance-Score 100:
  - Sarah Thompson 152620723 „Self Cleaning: Fewer Odors, 3x Less Laundry!“: 102 T, **Winning (100)**, 6 Varianten, used_count 4, Nachbarin-Knappheits-Story
  - Sarah Thompson 152620790 „Sleeping with pets? Read this“: 102 T, Optimized, 2 Varianten, Ich-Story Geruch vom Hund → `/sheets/ksp`
  - The Savvy Neighbor 115254854 „Say Goodbye to Musty, Smelly Bedding“: 101 T, **Winning (100)**, Hygiene-Ich-Text
  - Offline Granny 147817064 „The Splurge You’ll Wish You Made Years Ago“: 102 T, Growing (74), 2 Varianten, **Nachtschweiß-Ich-Story** → `/sheets/ksp`
  - Offline Granny 147817078: 101 T, Hook „At 73, are you tired of waking up multiple times a night—hot, uncomfortable…“, Video mit älterem Paar
  - Bedroom Insider 157635028 „A Simple Bedding Upgrade for Hot Sleepers“: 81 T, Winning → `/a/dermatologist-approved-sheets`
  - Neue Welle seit 05.10. (Chelsea Turano, Janelle, Meredith Little: 142 Ads), hier nicht gesichtet.
- **Granny Blog:** Masse statt Laufzeit. Die aktuelle Welle (Start 29.09.) kommt auf ca. 2.370 Ads mit dem URL-Keyword `thegrannyblog.com/miracle`. Die längste aktuelle Ad läuft 10 T. Die längste Ad in der Historie ist 99445068 (43 T).
- **Spend:** Für keine Miracle-Ad liefert GetHookd einen Spend-Bucket (US).

## 2. Auswahl der 3 stärksten Native-/Story-Ads (plus 1 Bonus für Angle B)

| Rang | Ad | Begründung |
|---|---|---|
| 1 | **152620723** Sarah Thompson – „My neighbor works in logistics…“ | Höchster Score (Winning 100), 102 T aktiv, **6 Varianten**, used_count 4. Persona-Ich-Post im Facebook-Freundinnen-Ton mit Knappheits-Story. Führt auf das Listicle. |
| 2 | **115254854** The Savvy Neighbor – „I had no idea how gross sheets get…“ | Winning 100, 101 T aktiv, Persona-Seite. Reiner **Hygiene-Angle**, das Bild zeigt eine zerwühlte weiße Bettdecke mit „Clean Body. Dirty Sheets. Lets fix that.“. Führt auf das Listicle. |
| 3 | **99445068** James Moore (Granny Blog) – „My wife is going to kill me for posting this.“ | Längste Granny-Blog-Miracle-Ad (43 T, 02.05.–13.06., im Fenster). Extrem langes Ich-Story-Native (20.423 Zeichen) mit Fake-Magazin-Advertorial als LP. Das Granny-Blog-Netz hat aktuell ~2.390 aktive Ads, das System ist also bewährt. Viele Signale für Wechseljahre und Familie (Linda 58, nass geschwitzt, die Tochter zahlt das Resort). |
| Bonus | **147817064** Offline Granny – „3:12 in the morning… soaked again“ | 102 T aktiv, 2 Varianten, nur „Growing“. Aber es ist die **beste Wechseljahre-Story** der Marke, deshalb vollständig dokumentiert. |

---

## Ad 1 · 152620723 – Sarah Thompson: „My neighbor works in logistics…“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/152620723?signature=845a8d91362e718406965af22357efa08b72211e6fbd577694c47cd0d13cffc3 |
| Seite/Persona | Sarah Thompson (7103244), Persona-Seite mit Frauennamen (31 Ads im Index) |
| Status | aktiv (letzte Sichtung 02.10.) |
| Start / Ende / Laufzeit | 29.06.2026 / – / 102 T |
| Format | DCO (2 Bilder, 4 Karten mit identischem Text) · facebook, instagram, audience_network, messenger, threads |
| CTA | SHOP_NOW „Shop now“ · link_description „{{product.description}}“ (nicht ersetzter Template-Platzhalter) |
| Score / Varianten | Performance 100 „Winning“ · 6 Varianten (collapse) · used_count 4 |
| LP | https://try.miraclebrand.co/a/s6-reasons (Listicle) |

**Headline:** „Self Cleaning: Fewer Odors, 3x Less Laundry!“

**Primärtext (wörtlich, vollständig):**
> My neighbor works in logistics and she told me something crazy - apparently Miracle Made had to halt all their sheet sales last month because of some tariff issues, and EVERYTHING sold out within days. People were literally calling asking when they'd be back!
>
> Well, she just texted me this morning that they finally got their bestsellers back in stock! - and they're doing a "we're sorry we were out of stock" sale for 46% off to make up for the shortage.
>
> I've been sleeping on these silver-treated sheets for 8 months now and I was panicking thinking I wouldn't be able to get a second set for our guest room. Just ordered the ivory ones for $129 instead of the usual $224!
> Sarah said they're only doing this sale until they clear the inventory that came in, so it could end any day. I know a bunch of you have been asking me about these sheets since I posted about how much better I've been sleeping - now's your chance to try them without the full investment!
>
> Linking below if you want to check it out. And yes, they still have that 30-night trial so there's literally no risk. Sweet dreams!

**Text im Bild:** kein Overlay-Text außer „+3“ bzw. „+4“ (Facebook-Album-Optik). Die Bilder sind Collagen aus Kundenfotos: eine Hand auf einer Packung „MIRACLE SHEETS / Self-Cooling & Self-Cleaning Bed Sheets“ auf einer bunten Tagesdecke, ein Bett mit blauer Tagesdecke vor einem Kopfteil mit Plüschtieren, blaue Kissen, Packungen „MIRACLE TOWELS“. Absichtlich unprofessionell, wirkt wie ein privater Facebook-Post.

**Story-Muster:** **Insider-Tipp aus dem Nachbarschaftsnetz** („My neighbor works in logistics“), dann eine Knappheits-Erzählung mit plausiblem Grund („tariff issues… EVERYTHING sold out within days“), dann eine Entschuldigungs-Aktion als Rabattgrund („"we're sorry we were out of stock" sale“), dann die Ich-Erzählerin als langjährige Nutzerin („for 8 months now“) und konkreter Preisanker („$129 instead of the usual $224“), dann das Gefühl einer Community („I know a bunch of you have been asking me…“), dann Risikoumkehr („30-night trial“). Das Produkt bleibt Nebensache. Verkauft wird die Gelegenheit.

---

## Ad 2 · 115254854 – The Savvy Neighbor: „I had no idea how gross sheets get…“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/115254854?signature=945dede758f97c4f06e4007b33ccad81816482037b98f84ee05a4adeaf0e8c37 |
| Seite/Persona | The Savvy Neighbor (8456), eine „Nachbarin mit Spartipps“-Seite (49 aktive Ads) |
| Status | aktiv |
| Start / Ende / Laufzeit | 30.06.2026 / – / 101 T |
| Format | DCO (4 Bilder, 4 Karten mit identischem Text) · facebook, instagram, audience_network, messenger, threads |
| CTA | LEARN_MORE „Learn more“ |
| Score | Performance 100 „Winning“ · 1 Variante |
| LP | https://try.miraclebrand.co/a/s6-reasons (Listicle) |

**Headline:** „Say Goodbye to Musty, Smelly Bedding“

**Primärtext (wörtlich, vollständig):**
> I had no idea how gross sheets get until I started researching this. Heat, sweat, dead skin cells, oils—it all builds up in your bedding faster than you think. Even if you shower before bed.
> Most sheets? You can smell it by day 5. That stale, not-quite-clean feeling.
> But I just tried Miracle Made sheets and I'm honestly shocked at the difference. They're silver-infused to help limit odor-causing bacteria on the fabric, so they actually stay fresh between washes. Like genuinely fresh, not just "good enough."
> They're also cooling (which is perfect for me because I'm always hot at night), 100% cotton, and they have this smooth, luxe feel that reminds me of high-end hotels.
> They're doing up to 46% off right now. I grabbed two sets—one for us, one for the guest room—and I'm already telling everyone about them.
> Link below if you want to try them. Seriously one of my better finds this year.
> Antimicrobial finish helps protect the fabric from odor-causing bacteria. Does not protect users against bacteria or other disease organisms.

**Text im Bild (wörtlich, alle 4 Formate gleich):** „Clean Body. / Dirty Sheets. / Lets fix that.“ („Dirty Sheets.“ in Gold), darunter das Logo „MIRACLE MADE“. Das Motiv ist eine zerwühlte weiße **Bettdecke** auf einem Bett im Dämmerlicht. Die Bildsprache ist ruhig und wirkt nicht reißerisch.

**Story-Muster:** **Recherche-Ich** („I had no idea… until I started researching this“), dann eine Ekel-Aufzählung („Heat, sweat, dead skin cells, oils“) und ein Einwand-Konter („Even if you shower before bed.“), dann ein Sinnes-Beweis („You can smell it by day 5“), dann Produkt und Mechanismus in einem Satz, dann Zusatznutzen Kühlung, dann „two sets—one for us, one for the guest room“, dann Empfehlung. Wichtig: Der **rechtliche Disclaimer steht im Ad-Text** („Does not protect users against bacteria…“). Die Formulierung ist vorsichtig: „help limit odor-causing bacteria on the fabric“.

---

## Ad 3 · 99445068 – The Granny Blog / James Moore: „My wife is going to kill me for posting this.“

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/99445068?signature=7d374440e76d412b469cac680610215a7e93e19bb4fbdb167786e870655278ea |
| Seite/Persona | James Moore (4554328), Persona im Granny-Blog-Affiliate-Netz |
| Status | inaktiv |
| Start / Ende / Laufzeit | 02.05.2026 / 13.06.2026 / 43 T |
| Format | Bild (2 Media) · facebook, instagram · US |
| CTA | LEARN_MORE · link_description „Click Here To Get 46% OFF Miracle Sheets Today“ |
| Score | – (keine Werte) |
| LP | https://thegrannyblog.com/miracle-gma/ (mit Affiliate-Parametern `?sub1=…`), Fake-Magazin-Advertorial |

**Headline:** „These New Silver-Infused Sheets Kill 99.7% of Bacteria While You Sleep“

**Primärtext:** 20.423 Zeichen / ca. 3.600 Wörter. Der **vollständige Wortlaut** steht in der Anhangdatei `a3/deep_mir/body_99445068.txt`. Die ersten Absätze wörtlich:
> My wife is going to kill me for posting this. She made me promise I wouldn't. I'm doing it anyway because I almost lost her this year and if even one husband reads this and pays attention to what I missed for 14 months, then she can be mad at me forever.
>
> My wife Linda is 58. Elementary school librarian for 31 years. The kind of person who organizes our spice rack alphabetically and remembers every kid's birthday on her block. She has run the show in our house since the day we got married — meals, schedules, holidays, our daughters' weddings, the family Christmas card every December.
>
> She has never once in 34 years of marriage said the words "I'm too tired."
>
> That's how I knew something was wrong.

Weitere Schlüsselstellen (wörtlich): „I'd wake up at 2 AM and the bed beside me would be empty.“ · „She woke up to her car in a culvert off I-890. Front bumper crushed against a guardrail. Airbag deployed.“ · „We bought a $2,400 mattress… Linda lay on it for three nights, sweat through it just like the old one“ · „Three weeks later, our daughter flew us out to a resort in Sedona, Arizona.“ · Hotel-Auflösung: „"Sir, all our linens are antimicrobial silver-thread. Most upper-tier hotels switched over the last decade…"“ · Mechanismus: „Your skin sheds approximately 500 million dead cells every 24 hours… Standard laundering does NOT eliminate the bacteria embedded in cotton fibers. It washes the surface.“ und „BIOGENIC AMINES… create the sour, metallic smell“ · Ergebnis: „Night three. Six hours and 51 minutes. No sweating. No sour smell in the morning.“ · Kaskade aus P.S. bis P.P.P.P.S.: Warnung vor Amazon-Fälschungen „sprayed silver coating that washes off completely after 4 to 6 wash cycles“, Abschluss „She said "if it saves one woman, post it."“. „Miracle“ fällt erst nach **2.360 Wörtern**.

**Text im Bild:** kein Text. Das Foto im Nachrichtenstil zeigt eine verunglückte graue Limousine an einer Leitplanke mit ausgelöstem Airbag, dahinter ein Streifenwagen mit Blaulicht im Schnee. Es illustriert die Unfall-Szene der Story und passt nicht zur Produktkategorie. Das ist Absicht (Neugier, „News“-Gefühl).

**Story-Muster:** **Ehemann-Geständnis gegen den Willen der Frau** („She made me promise I wouldn't“), dann Verfall der Ehefrau über 14 Monate, dann **Beinahe-Katastrophe** (Sekundenschlaf-Unfall), dann gescheiterte Lösungen (Ärzte, „$2,400 mattress“), dann **Urlaubs-Kontrast** (im Resort schläft sie, zu Hause nicht), dann Hotel-Personal verrät das Geheimnis (Silberfäden), dann pseudowissenschaftlicher Mechanismus (Hautschuppen, Bakterien im Gewebe, „biogenic amines“), dann Test-Tagebuch, dann Familie rüstet alle Betten um, dann P.S.-Kaskade gegen Fälschungen. Template-Fehler: Die Frau sagt einmal „Mark“ statt „James“, die Persona-Texte werden also zwischen Seiten recycelt (Mark Davis ist die aktuelle Haupt-Persona).

**Aktuelle Granny-Blog-Welle (nur zum Vergleich):** Mark Davis 190372791 (aktiv seit 29.09., 10 T, Testing; share_url in diesem Lauf nicht abgefragt), Variante 198629101 https://app.gethookd.ai/share/ad/198629101?signature=4aea0ba899ae2b074395d19a924fa3c33e96c33e78d690093c20ec36d62612fe, Titel „Mark Davis“, Hook: „Ive been an ICU nurse for 14 years. Last month I swabbed my sons bedsheets as a joke to win an argument with my wife. Nobody's laughing now.“ Volltext in `a3/deep_mir/body_190372791.txt`. Die Variante 198629101 sagt „pillowcase“ statt „bedsheets“.

---

## Bonus-Ad 4 · 147817064 – Offline Granny: „3:12 in the morning… soaked again“ (Angle B)

| Feld | Wert |
|---|---|
| Link | https://app.gethookd.ai/share/ad/147817064?signature=495693eb53ff3ec74fc61a2bb10a54cfa8d3fdb9e880a5a9c2609f7376e2730e |
| Seite/Persona | Offline Granny (7103253), eine „Oma ohne Internet“-Persona (9 Ads) |
| Status | aktiv |
| Start / Ende / Laufzeit | 29.06.2026 / – / 102 T |
| Format | Bild · facebook, instagram, audience_network, messenger, threads |
| CTA | SHOP_NOW „Shop now“ |
| Score | 74 „Growing“ · 2 Varianten |
| LP | https://try.miraclebrand.co/sheets/ksp (PDP) |

**Headline:** „The Splurge You’ll Wish You Made Years Ago“

**Text im Bild:** kein Text außer „+4“. Facebook-Album-Collage aus vier Handyfotos eines Schlafzimmers: weiße Steppdecke, olivgrüne Kissen, Nachttisch mit Lampe, Blumen und Büchern, Fenster mit Stadtblick im Sonnenuntergang.

**Primärtext (wörtlich, vollständig; 3.992 Zeichen / 723 Wörter; die Marke fällt nach 590 Wörtern; Datei `a3/deep3/body_147817064.txt`):**
> I was sitting on the edge of my bed at 3:12 in the morning, trying not to cry because I was soaked again.
>
> It had been like that for almost two years.
>
> Wake up hot. Throw the covers off. Get cold. Pull them back on. Then just lie there.
>
> Wide awake.
>
> I started dreading going to bed.
>
> I used to love it. Clean sheets, quiet house, lights out.
>
> Now it felt like something I had to manage.
>
> Every night.
>
> I tried everything I could think of.
>
> I bought new sheets. The ones that said they were cooling. They felt nice for a few nights.
>
> Then they didn’t.
>
> I bought lighter ones. Heavier ones. Softer ones.
>
> I opened the window. I used a fan.
>
> I even changed what I wore to bed.
>
> Nothing fixed it.
>
> I would wake up at 3am, soaked, then freezing, and then just… stuck there.
>
> Thinking about how tired I was going to feel the next day.
>
> Thinking about how this might just be my life now.
>
> I stopped talking about it.
>
> My husband slept fine.
>
> I didn’t want to keep saying the same thing over and over.
>
> So I just dealt with it.
>
> Quietly.
>
> And the sheets didn’t help.
>
> By the third or fourth night, they felt off.
>
> Not dirty exactly.
>
> Just… not fresh.
>
> Like they were holding onto something.
>
> I started washing them twice a week.
>
> It felt ridiculous.
>
> But I couldn’t stand the feeling.
>
> One Sunday, I was at my sister’s house.
>
> We were sitting at her kitchen counter, drinking coffee.
>
> I told her I hadn’t slept through the night in months.
>
> She looked at me and said, “I was the same.”
>
> That got my attention.
>
> She said she used to wake up soaked too.
>
> Same time. Same cycle.
>
> Then she said something I hadn’t heard before.
>
> “It wasn’t just me. It was my sheets.”
>
> I remember thinking that sounded like marketing.
>
> She laughed and said she thought the same thing.
>
> Regular sheets can trap heat and moisture.
>
> And over a few nights, they can start holding onto sweat and body oils.
>
> So even if they look clean, they don’t always feel fresh.
>
> They can feel warmer. Heavier.
>
> That’s what can start to smell.
>
> That’s what sits against your skin.
>
> I remember asking her, “Does it actually make a difference?”
>
> She said, “I stopped thinking about my sheets.”
>
> That was the first thing that sounded real to me.
>
> Not “best sleep ever.”
>
> Not “life changing.”
>
> Just… she stopped thinking about it.
>
> She sent me the link that afternoon.
>
> I almost didn’t order them.
>
> I’ve spent enough money on things that didn’t work.
>
> But there was a 30 night trial.
>
> So I figured I’d know pretty quickly.
>
> The first week, I noticed something small.
>
> I wasn’t flipping the pillow over as much.
>
> The sheets felt the same when I woke up as when I fell asleep.
>
> Week two was different.
>
> I still woke up once or twice. But I felt more comfortable, and I fell back asleep faster.
>
> By week three, I realized something.
>
> It was Wednesday.
>
> And my sheets still felt clean.
>
> That had not happened in years.
>
> By week four, I had a night where I didn’t wake up at all.
>
> I opened my eyes in the morning and just stayed there for a second.
>
> Quiet. Still. Rested.
>
> I hadn’t felt that in a long time. That’s when I knew it was different.
>
> I was ready to pick up my activities again! Bridge, pickleball, zumba, it was unheard of.
>
> The brand is called Miracle Made.
>
> They make sheets with that silver infused fabric.
>
> The part that mattered to me was simple.
>
> They stayed comfortable longer.
>
> They stayed fresh longer.
>
> And I stopped thinking about them.
>
> That was the whole point. Right now, they’re offering up to 46% off.
>
> They also include three free towels, which I didn’t expect but ended up liking.
>
> There’s a 30 night trial.
>
> If it doesn’t help, you can send them back.
>
> Nothing to lose, just make sure you buy the real ones, not those fakes https://tinyurl.com/3etdb2pe
>
> No complicated process. Just try them and see.
>
> If you’ve been dealing with this for a while, you already know.
>
> You don’t need perfect sleep. You just want one good night.
>
> Then another.
>
> Then maybe, eventually, it stops being something you think about at all.

**Story-Muster:** **Tiefpunkt mit Uhrzeit** („3:12 in the morning, trying not to cry“), dann der Zyklus („Wake up hot. Throw the covers off. Get cold. Pull them back on.“), dann Isolation („My husband slept fine… So I just dealt with it. Quietly.“), dann der **Hygiene-Dreh** („By the third or fourth night, they felt off… I started washing them twice a week.“), dann die **Schwester als Vertraute** („It wasn’t just me. It was my sheets.“), dann bewusst unaufgeregte Versprechen („Not “best sleep ever.” Not “life changing.” Just… she stopped thinking about it.“), dann ein Wochen-Zeitstrahl, dann das Comeback ins Leben („Bridge, pickleball, zumba“), dann Marke, Angebot und eine Warnung vor Fälschungen. Die Wechseljahre werden **nie genannt**, die Leserin erkennt sich aber sofort.

---

## LP-Analysen

### A · `try.miraclebrand.co/a/s6-reasons` (Ziel von Ad 1 und 2; abgerufen 11:53 und 17:03 mobil, 845 Wörter)
- **Typ:** **Listicle** im Marken-Layout (Miracle-Made-Logo). Keine Fake-Magazin-Optik, aber ein Advertorial-Disclaimer am Fuß: „Disclaimer: this is an advertisement, using a fictional customer but discussing experiences that are common to real customers of miracle brand.“ / „This is an advertisement and not an actual news article, blog, or consumer protection update“.
- **H1 (wörtlich):** „6 Reasons Americans are Switching to these NASA-Inspired Sheets“ · **Sub:** „Combining comfort with breathability and softness.“ · Top-Bar: „⏰ PRIME TIME SALE! 🛍️ UP TO 46% OFF AUTO-APPLIED / OFFER VALID FOR 15:00“ (Countdown, 17:03 bei „14:44“, also neu startend)
- **Abschnitte (wörtlich):** „1. Temperature-Regulating Comfort“ · „2. Up to 3x Less Laundry And Big Savings“ · „3. Your Sheets Are Damaging Your Skin“ · „4. Odor Fighting“ · „5. Luxury Comfort Without The Price Tag“ · „6. Try it 100% Risk Free!“ · „GET UP TO 46% OFF FOR A LIMITED TIME ONLY!“. Neu seit 17:03: „LIMITED-TIME SWEEPSTAKES / Win a Dream Home Makeover or $100,000 Cash … Every $1 spent = 1 entry.“
- **Produkt-Einführung:** nach **81 Wörtern** (in Punkt 1).
- **Mechanismus (wörtlich):** „Miracle Made® Sheets help prevent up to 99.7% of bacteria growth due to their unique silver-infused fiber technology.“ und „infused with silver and made with NASA-inspired temperature-regulating fabrics“.
- **Problem-/Beweis-Sätze (wörtlich):** „Night sweats are the absolute worst! Especially if you are waking up next to a significant other, it can be really embarrassing. Waking up feeling like you just wet the bed makes everything such a hassle.“ · „According to research by Amerisleep, after just one week of use, bedsheets had more bacteria than a bathroom doorknob. After just two weeks, that number multiplied to have more bacteria than a pet toy.“ · „your bed could be harboring more bacteria than a toilet seat“ · „Humans shed around 15 million skin cells each night.“
- **Angebot/Knappheit/Garantie:** „This limited-time deal is in high demand and stock keeps selling out.“ · „Hurry! Last chance for this offer!“ · „Sell-Out Risk: High“ · „FREE SHIPPING“ · „if you aren't 100% satisfied with your purchase in the first 100 days, we will refund all of your money“.

### B · `thegrannyblog.com/miracle-gma/` (Ziel von Ad 3; abgerufen 11:53 mobil, 1.976 Wörter)
- **Typ:** **Fake-Magazin-Advertorial** (Masthead „✦ The Granny Blog“, Label „ADVERTORIAL“, Serif-H1, Byline mit Foto).
- **H1 (wörtlich):** „Good Morning America Features The Sheet Set That's Changing How America Sleeps — And We Tested It For 30 Days“ · **Byline:** „Feb 21, 2026 · Special editorial by Sarah Johnson, Senior Editor“ · Banner „⭐ DEALS & STEALS — FEATURED PRODUCT OF THE WEEK“
- **Lead (wörtlich):** „"If you could put on sheets every night that killed 99.7% of bacteria, kept you cool all night, and made your skin look better — would you ever go back to regular bedding?"“ · „What about sleeping on sheets so naturally clean, so temperature-regulating, that you stopped waking up at 3am drenched in sweat?“ · „Research shows that after just one week of use, the average pillowcase contains over 3 million bacteria per square inch — more than a toilet seat.“ · „As we get older, the constant battle we all face is how to protect our sleep, our skin, and our wellbeing.“
- **H2 (wörtlich):** „Silver — The 'Holy Grail Ingredient' For Bedding“ · „Let Me Tell You About Miracle Sheets' Breakthrough Discovery“ · „Is Miracle Sheets' Extra Luxe Set Really The Best?“ · „(STORY UPDATE: October 1, 2026) Miracle Sheets Has Taken The Sleep Industry By Storm…“ · „Miracle Sheets Independent Clinical Study Results:“ · „We Tested It Ourselves — Did It Live Up To The Hype?“ (Night 1 / Day 7 / Day 20 / Day 30 / Sandra's Thoughts) · „If You Can Get Your Hands On A Set — Do It Now“ · „Comments“
- **Produkt-Einführung:** „Miracle“ im Bildtext nach 46 Wörtern, „Meet Miracle Sheets.“ nach ca. 287 Wörtern.
- **Mechanismus (wörtlich):** „Silver works by disrupting the cell walls of bacteria, preventing them from growing or reproducing. When silver is infused directly into fabric at the thread level — not sprayed on as a coating that washes away — it retains its antibacterial power wash after wash, permanently.“
- **Beweise:** Medien-Logo-Wand (GMA, QVC, The View usw.; unbelegte Behauptungen) · „Eliminates 99.7% of bacteria growth — permanently, wash after wash“ · „100% of users reported sleeping cooler…“ · Testtagebuch (Day 7: „Seven consecutive nights — not once have I woken up sweating. My husband noticed too…“) · Kommentarbereich, darin Margaret R.: „I'm 62 and have been dealing with night sweats for four years. Hot flashes during the day, drenched at night… Third night in on these sheets, I slept straight through without waking up once. I actually cried that morning.“ und Robert W.: „Bought these for my wife as a gift after she'd been complaining about waking up hot for years.“ Familien-Kauf: „I ordered 3 sets so my mother and my sister could try them too.“ (Sandra) und „a set for my daughter“ (Day 30).
- **Angebot/Knappheit/Garantie:** „Last time we checked, they were running a 25% Discount (TODAY ONLY)“ · „Update: Only 22 Sets Left. Promotion Ends: October 8, 2026“ (das Datum ist dynamisch und entspricht dem Abruftag) · 100-day money-back. Der Footer-Disclaimer lautet „This is a sponsored advertorial. Results may vary.“. Die CTA-Links gehen über den Tracker k34mtrk.com.

### C · `try.miraclebrand.co/sheets/ksp` (Ziel von Bonus-Ad 4; abgerufen 17:03 mobil, 1.419 Wörter)
- **Typ:** **PDP/Sales-Seite** im Marken-Layout. H1 (wörtlich): „Temp-regulating and self-cleaning sheets. Hotel-quality sleep, every night.“ · Sub: „Infused with silver that helps prevent up to 99.7% of bacteria growth and helps keep you at the perfect temperature all night long.“
- **H3-Nutzen (wörtlich):** „Advanced temperature regulation. Wake up refreshed, not sweaty.“ · „Helps prevent up to 99.7% of bacteria growth, naturally.“ · „Self-cleaning: Fewer odors. Up to 3x less laundry.“ · „Goodbye morning stuffiness.“ · „87% of surveyed customers report better rest.*“ · „100-Nights Money Back Guarantee“
- **Angebot:** „UP TO 46% OFF AUTO-APPLIED“, „HURRY! LAST CHANCE!“, „SHOP TO WIN: Every order today enters you to win a Dream Home Makeover or $100,000 cash.“, „24,078+ FIVE-STAR REVIEWS“, „427,873+ Miracles Delivered“, Bundle-Upsell „Add 2x EXTRA Pillowcases“.

---

## 5. Was wir für Decken ohne Bezug (UK) übernehmen

**Angle A – Hygiene:**
- Die Bild-Headline „Clean Body. Dirty Sheets. Lets fix that.“ (Winning, 101 T, zerwühlte **Bettdecke** im Bild) lässt sich fast wörtlich übertragen: *„Clean body. Dirty duvet.“* Die Steigerung für uns: *„You wash the cover. Nobody washes the duvet.“*
- Die Sinnes-Beweise statt Laborzahlen funktionieren: „You can smell it by day 5. That stale, not-quite-clean feeling.“ sowie „Not dirty exactly. Just… not fresh. Like they were holding onto something.“ Bei uns geht es um den Geruch der Bettdecke selbst, „the duvet you've had since…“.
- Die Mechanik der Granny-Blog-Story passt sehr gut: „Standard laundering… washes the surface. The deeper colonies survive in the weave.“ Für uns gilt: *Der Bezug wird gewaschen, die Füllung nie.* **Wichtig:** Die Granny-Blog-Behauptungen (biogenic amines, 3 Mio. Bakterien, „more than a toilet seat“) wären in UK nach ASA-Regeln heikel. Für uns gilt deshalb „Sinnes-Beweis plus vorsichtige Formulierung“ wie bei Ad 2 („help limit odor-causing bacteria on the fabric“), Disclaimer inklusive.

**Angle B – Wechseljahre:**
- Die Offline-Granny-Story (Bonus-Ad) ist die beste Vorlage: Tiefpunkt mit Uhrzeit, der Zyklus Decke weg/Decke drauf, „My husband slept fine“, die Schwester als Auslöser, unaufgeregte Versprechen, ein Wochen-Zeitstrahl, die Rückkehr zu Hobbys. Die Wechseljahre werden nie benannt. Bei uns wird aus „It wasn’t just me. It was my sheets.“ dann *„It wasn't just me. It was my duvet – and the cover I'd zipped it into.“*
- Der Kommentar-Typ „I'm 62 and have been dealing with night sweats for four years…“ eignet sich für die Kommentar-Sektion unseres Advertorials.

**Angle C – Beziehen:**
- Miracle nutzt „Up to 3x less laundry“ und „washing them twice a week. It felt ridiculous.“ Bei uns wird daraus die Kombination aus weniger Waschaufwand und **kein Beziehen mehr**: *„I was stripping and re-covering the duvet twice a week. At 3am. Soaked.“*

**Angle D – Tochter kauft für Mutter:**
- Das Granny-Blog-System zeigt, wie man ältere Frauen und ihre Familien erreicht: Persona-Namen wie „Offline Granny“, „Sarah Thompson“, „The Savvy Neighbor“, die Tochter zahlt das Resort, „a set for my daughter“, „3 sets so my mother and my sister could try them too“, „Bought these for my wife as a gift“. Bei uns kann eine Ehemann- oder Tochter-Ich-Story nach dem Muster „My wife is going to kill me for posting this“ werden zu *„My mum is going to kill me for posting this.“*: Die Tochter sieht, wie die Mutter mit dem Bettbezug kämpft bzw. nass aufwacht, und kauft die Decke.
- Die Insider-Knappheits-Story von Ad 1 („My neighbor works in logistics…“) taugt als Rabatt-Grund im UK-Kontext (z. B. Lieferengpass, „back in stock“-Aktion). Das funktioniert aber nur, wenn es wahr ist.

**Formales:** (1) Ein eigenes Netz aus 5–10 Persona-Seiten mit Alltagsnamen (Nachbarin, Oma, Magazin), die alle auf **eine** Listicle-LP zeigen und dort 100+ Tage laufen. Das ist für eine Marke unserer Größe realistischer als ein Affiliate-Netz mit 2.400 Ads. (2) Facebook-Album-Collagen aus „Kundenfotos“ mit „+3/+4“ als Bild. (3) Listicle mit Advertorial-Disclaimer am Fuß. (4) Nicht übernehmen: nicht ersetzte Platzhalter („{{product.description}}“), dynamische Fake-Deadlines, unbelegte Medien-Logos.

## Lücken
- Für keine Miracle-Ad liegt Spend vor (US).
- Die neue Persona-Welle seit 05.10. (Chelsea Turano 71, All things beautiful by Janelle 39, Meredith Little 32) wurde nicht gesichtet.
- Zu 99445068 liegen nur die Daten aus dem ersten Lauf vor (`get_ad` 11:58), die Bilder wurden damals angesehen. Im zweiten Lauf gab es keinen neuen `get_ad_media`-Batch. Die Bilder von Ad 1, 2 und 4 kamen mit `get_ad`.
- Die Granny-Blog-LP stammt vom Abruf um 11:53. Die LP `/a/dermatologist-approved-sheets` (Bedroom Insider, Winning 81 T) wurde nicht abgerufen.
- Den share_url für 190372791 hat dieser Lauf nicht neu abgefragt. Ersatzweise ist die textgleiche Variante 198629101 verlinkt (Volltext und Metadaten siehe `a3/deep_mir/_notes.md`).
- Nicht prüfbar sind die Medienbehauptungen der Granny-Blog-Seite (GMA, QVC, The View) und die Studienzahlen.
