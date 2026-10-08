# Marken-Deep-Dive: MagicSplashy „EasySleep" (Decke + Bezug in einem)

Stand: 08.10.2026, Agent 3. Quellen: GetHookd (search_ads, get_ad, get_ad_media, transcribe_ads), Seitenabrufe mit `tools/shot.js` (mobil). Zitate wörtlich in Originalsprache. Links sind GetHookd-`share_url`s oder echte LP-URLs.

| Feld | Wert |
|---|---|
| Marke / Meta-Seite | MagicSplashy (eine einzige Seite, keine Persona-Seiten; laut `get_domain_advertisers(magicsplashy.de)` wirbt nur MagicSplashy auf die Domain) |
| GetHookd brand_id | **88310** (external_id 106221409129856) |
| Domain | magicsplashy.de (auch magicsplashy.ch), Shopify, shop_id 12609 |
| Kategorie | schlaf_bettwaren (Decke ohne Bezug, also exakt unser Produkt) |
| Markt / Sprache | DE + AT (alle geprüften Ads `countries: AT, DE`), Deutsch |
| Native-/Story-Formate | UGC-Ich-Story-Video, Problem-Agitation-Voiceover mit Mini-Fallgeschichten, Zitat-Bild („“Ich hab Bettwäsche gestrichen.”"), Kundenumfrage-Advertorial (10 Punkte), Redakteur-Ich-Story-Advertorial (10 Punkte), Wechseljahre-Listicle (7 Gründe), Presell-Sales-Letter-Seiten |
| is_real_native_player | **ja**, mit einer Einschränkung: Alle Natives laufen über die eigene Markenseite und eigene `/pages/…`-URLs, nicht über Fremd-Publisher oder Personas. Die zwei Videos mit dem höchsten Spend ($10.001–20.000) führen zum Teil direkt auf die Produktseite (PDP). |
| Score als Vorbild für uns | **10/10** |

## 1. Erfolgssignale und Inventar

- **Volumen:** GetHookd zählt 146 aktive Ads (get_brand, 08.10.). `search_ads(status=active)` meldet total 169 (Obergrenze). Gesichtet wurden die Seiten 1–3 (117 Zeilen, sortiert nach Laufzeit). Seite 4 enthält nur Ads, die höchstens 3 Tage alt sind, und wurde nicht gesichtet. Die inaktive Historie meldet total 5.706 (darunter viele DCO-Varianten); gesichtet wurden die 40 längsten.
- **Langläufer:** PDP-Bild „Bett machen im Handumdrehen 👋" seit 21.03.2026 (**202 T**, aktiv; 112079858 Spend $5.001–10.000, Winning).
- **Spend-Spitze (EU-Transparenzdaten):** 3 aktive Ads im Bucket **$10.001–20.000**, alle „Winning": das UGC-Ich-Story-Video 126012757 (→ Presell) und die zwei Problem-Story-Voiceover-Videos 125662052 und 129130363 (→ PDP). Darunter liegen im Bucket $5.001–10.000 die inaktive Vorgängerversion des UGC-Skripts 112079893 (→ PDP, 86 T) sowie die Bild-Ads 112079858, 125661811, 112079871 und 112079907.
- **Native-Landingpages (eigene Domain), aktiv belegt:**

| LP | Typ | aktive Ads (gesichtet) | ältester Start / Laufzeit |
|---|---|---|---|
| /pages/schlafen-im-sommer | Presell-Sales-Letter (Sommer/Schwitzen) | 126012757, 130714467, 126013293 | 18.07. / 83 T |
| /pages/gesund-schlafen | Redakteur-Ich-Story-Advertorial, 10 Punkte | 125662155 | 17.07. / 84 T |
| /pages/umfrage | Kundenumfrage-Advertorial, 10 Punkte | 148248622, 201264494 | 17.08. / 53 T |
| /pages/gut-schlafen | Presell-Bridge („"Nie wieder Bettwäsche wechseln am Sonntag"") | 177828057, 200300803, 200300922 | 15.09. / 24 T |
| /pages/frauen-magazin | Wechseljahre-Listicle, 7 Gründe | 196672418, 196670945, 196672570, 196672112, 196671707, 196671531, 199242833 | 03.10. / 6 T (Test) |
| /pages/easysleep (inaktiv) | Presell „Ich hab mein Bett seit einem Jahr nicht mehr bezogen." | 112081235, 112080628 (98 T), 112083483, 112083327 (86 T), 114949876 (81 T) | 11.06.–16.09. |

- **Produktseiten:** /products/easysleep-decke (leitet heute auf /products/easysleep-ganzjahresdecke um; neue Herbstwelle ab 15.09.), /products/magicsleep (Kühldecke „Eisdecke statt Schwitzdecke!", 112080045 138 T, $2.001–5.000).
- **Systematisches Hook-Testing:** gleicher 93-s-Body mit 4 verschiedenen Hooks, alle am 17.07. gestartet (siehe Ad 3). Die neue Herbstwelle (02.–06.10.) testet weitere Hooks: Wechseljahre, Gelenke/ältere Menschen, Zeitumstellung, Hund, „5 Gründe", „Nur 44 % der Kunden…".

## 2. Auswahl der 3 stärksten Native-/Story-Ads (Begründung)

| Rang | Ad | Warum |
|---|---|---|
| 1 | **126012757** UGC-Ich-Story-Video → Presell /schlafen-im-sommer | Höchster Spend-Bucket ($10.001–20.000), „Winning", 83 T aktiv, EU-Reichweite 1.315.088. Klares Story-Format (Ich-Erzähler, Einwand-Vorwegnahme). Das Skript läuft als Cluster mit mindestens 6 weiteren IDs auf 3 LPs. |
| 2 | **148248622** Zitat-Bild „“Ich hab Bettwäsche gestrichen.”" → Umfrage-Advertorial /umfrage | Einzige Bild-Ad mit Native-LP und „Winning" plus Spend $2.001–5.000. 53 T aktiv, EU-Reichweite 374.878, used_count 3. Am 06.10. kam mit 201264494 eine neue Ad auf dieselbe LP hinzu (die LP wird also weiter genutzt). |
| 3 | **125662052** (+ Zwilling **129130363**) Problem-Agitation-Voiceover mit Fallgeschichten „Werner, über 80, Witwer" / „Sabine, Allergien" → PDP | Höchster Spend ($10.001–20.000, beide IDs „Winning"), 84 bzw. 73 T, EU-Reichweite 1.343.347. Story-nah (Ritual-Schilderung, Fallgeschichten, Zeitstrahl „erste Nacht / erste Woche / ein Monat"). Deckt A, C und D in einem Skript ab. Einschränkung: Die LP ist die PDP. Den passenden Advertorial-Text liefert /pages/gesund-schlafen (Ad 125662155, gleiche Story „15 Jahre"). |

Verworfen als Top 3: **125662155** → /gesund-schlafen. Sie läuft zwar 84 T auf einer Native-LP, ist aber „Testing", hat Spend $0–500 und nur 1.157 EU-Reichweite, und ihr Bild ist eine reine Angebotsgrafik. Die LP wird unten trotzdem zerlegt.

---

## 3. Ad-Raster

### Ad 1 · 126012757 · UGC-Ich-Story „Ich habe die Easy-Sleep-Decke bestellt, weil ich einfach keinen Bock mehr hatte…"
| Spalte | Inhalt |
|---|---|
| Link | https://app.gethookd.ai/share/ad/126012757?signature=4aa5cf75157a813c3daede61927240a452d4bf09046a0feee9ae288bd457658f |
| Seite | MagicSplashy |
| Markt/Sprache | AT, DE · de |
| Status | aktiv |
| Start / Ende / Laufzeit | 18.07.2026 / läuft / **83 T** |
| Format | Video 57 s (720×1280, 9:16), 2 Medien (identisches Transkript) |
| Plattformen | facebook, instagram, audience_network, messenger, threads |
| Zielgruppe (EU) | 18–65, alle Geschlechter, EU-Reichweite 1.315.088 |
| Headline | Nie wieder Bettwäsche wechseln 🛏️ |
| Primärtext (vollständig) | Decke + Bezug in einem 🌙<br><br>Die EasySleep Bettdecke macht Bettmachen endlich einfach. Waschen, trocknen und wieder aufs Bett legen.<br><br>✓ Nie wieder Ärger mit Überzügen <br>✓ Angenehm kühl im Sommer, wohlig warm im Winter <br>✓ Hypoallergen und antibakteriell<br><br>Heute 2 SoftCloud Kissenbezüge gratis (49,99€ Wert) sichern.<br><br>40 Tage risikofrei probeschlafen.<br><br>Genieße endlich ein Bett, das immer frisch ist. |
| Text im Video | Kopf-Overlay 0–6 s: „DAS WARS MIT BETTWÄSCHE WECHSELN!" Danach Untertitel-Boxen, die dem gesprochenen Text folgen, z. B. „Ich hab die EasySleep Decke bestellt", „Die ist nämlich Decke und Bettwäsche in EINEM", „An der Luft 2 bis 3 Stunden", „schlaf ich nicht mehr wie in der Sauna", „und nein das ist keine Faulheit", „Kein "Ich müsste mal wieder wechseln"", „Softcloud Kissenbezügen im Wert von 49,99 €", „und mit 40 Tage probeschlafen", „Link ist unten" (Kontaktabzug alle 2 s geprüft) |
| Bildfolge | Mann um die 35–40 wirft die Decke aufs Bett → liegt darunter → Waschmaschine im Keller → Decke an der Wäschespinne im Garten → Hand auf der Decke („Klimafasern") → streckt sich im Bett, Daumen hoch → Kontrast: alter blau karierter Bezug zerknüllt, Mann wischt sich die Stirn → wirft die EasySleep drüber → zeigt die Kissenbezüge. Handy-UGC-Optik. |
| CTA | ORDER_NOW („Order now") |
| Landingpage | https://magicsplashy.de/pages/schlafen-im-sommer → **Presell / Long-Form-Sales-Letter** (siehe LP 1) |
| Hook | gesprochen: „Ich habe die Easy-Sleep-Decke bestellt, weil ich einfach keinen Bock mehr hatte, jede Woche mit der Bettwäsche zu kämpfen." · Overlay: „DAS WARS MIT BETTWÄSCHE WECHSELN!" |
| Angle | C Beziehen (Hauptthema), dazu Sommer-Schwitzen („wie in der Sauna") und Frische/Hygiene („wie frisch geduscht ins Bett") |
| Story-Muster | **Ich-Story Käufer (UGC)**: Kaufgrund → Mechanismus → Einwand-Vorwegnahme („Und bevor du sagst, die wird doch nie trocken…", „Und nein, das ist keine Faulheit.") → Überraschungs-Benefit („Was mich aber echt überrascht hat, die Klimafasern.") → Angebot |
| Angebot | 2 gratis SoftCloud-Kissenbezüge (49,99 € Wert), 40 Tage Probeschlafen |
| Spend / Performance | **$10.001–20.000** · **Winning** (Score 100) |
| Varianten (Skript-Cluster) | 130714467 (01.08., 69 T, aktiv, → schlafen-im-sommer, $0–500) · 177828057 (15.09., 24 T, → /gut-schlafen, $501–2.000, Optimized) · 200300803, 200300922 (06.10., → /gut-schlafen) · 196672482 (DCO, 04.10., → PDP) · **112079893** (14.05.–07.08., 86 T, inaktiv, → PDP, **$5.001–10.000**) · Hook-Varianten desselben Skripts: **196670581** „Ich hab mir die EasySleep bestellt, weil ich mit meinen Gelenken keine Kraft hatte, jede Woche mit der Bettwäsche zu kämpfen." (02.10.) und 196672076 „Am 25. Oktober wird die Uhr zurückgestellt und ich habe mir die EasySleep bestellt, weil ich einfach keinen Bock mehr hatte, …" (02.10.). Transkript-Ähnlichkeit zu 126012757: 130714467 1,00 · 112079893 0,998 · 177828057 0,982 · 196670581 0,841 |
| Einordnung | **Winner** (≥ 60 T, aktiv, höchster Spend). Das Skript trägt seit Mai (112079893) und wird inzwischen auf drei LPs verteilt. |

Transkript: siehe Anhang A1.

### Ad 2 · 148248622 · Zitat-Bild „“Ich hab Bettwäsche gestrichen.”" → Kundenumfrage-Advertorial
| Spalte | Inhalt |
|---|---|
| Link | https://app.gethookd.ai/share/ad/148248622?signature=84d901c24974a36d3944f48f20a4e49c67491a96f0afc5eac2f108a8698f93ac |
| Seite | MagicSplashy |
| Markt/Sprache | AT, DE · de |
| Status | aktiv |
| Start / Ende / Laufzeit | 17.08.2026 / läuft / **53 T** |
| Format | Bild (1 Medium) |
| Plattformen | facebook, instagram, audience_network, messenger, threads |
| Zielgruppe (EU) | 18–65, alle, EU-Reichweite 374.878 |
| Headline | Nie wieder Bettwäsche wechseln 🛏️ |
| Primärtext (vollständig, = Standard-Body) | Decke + Bezug in einem 🌙<br><br>Die EasySleep Bettdecke macht Bettmachen endlich einfach. Waschen, trocknen und wieder aufs Bett legen.<br><br>✓ Nie wieder Ärger mit Überzügen <br>✓ Angenehm kühl im Sommer, wohlig warm im Winter <br>✓ Hypoallergen und antibakteriell<br><br>Heute 2 SoftCloud Kissenbezüge gratis (49,99€ Wert) sichern.<br><br>40 Tage risikofrei probeschlafen.<br><br>Genieße endlich ein Bett, das immer frisch ist. |
| Text im Bild | „“Ich hab Bettwäsche gestrichen.”" (große schwarze Schrift, Zitat) / „Decke + Bezug in EINEM." / Häkchen-Chips „komplett waschbar" · „schnell trocknend". Motiv: schwarze Steppdecke mit 2 Kissen in Draufsicht auf hellem Grund. |
| CTA | SEE_DETAILS („See details") · Link-Beschreibung „Das Original- MagicSplashy" |
| Landingpage | https://magicsplashy.de/pages/umfrage → **Advertorial (Kundenumfrage-Auswertung, Listicle mit 10 Punkten)** (siehe LP 2) |
| Hook | Bild: „“Ich hab Bettwäsche gestrichen.”" · Text: „Decke + Bezug in einem 🌙" |
| Angle | C Beziehen |
| Story-Muster | **Kundenzitat als Native-Statement (Ich-Satz im Bild)** → Umfrage-Advertorial „Kundenbetreuer wertet 2.000 Antworten aus" |
| Angebot | wie Ad 1; auf der LP zusätzlich „Spare heute 30%" |
| Spend / Performance | **$2.001–5.000** · **Winning** (100) |
| Varianten | used_count 3 (dasselbe Bild in 3 Ads); 201264494 (06.10., → /umfrage, neu) |
| Einordnung | **Winner** (≥ 30 T, aktiv, ≥ 3 Verwendungen). Es ist die einzige Bild-Ad mit Native-LP und Winning-Status. |

### Ad 3 · 125662052 (+ 129130363) · Problem-Agitation-Voiceover mit Fallgeschichten
| Spalte | Inhalt |
|---|---|
| Link | https://app.gethookd.ai/share/ad/125662052?signature=afca98f12b6dd400226ecbd2adcf32983adb04f2c06b179d502bd583a5f9a763 · Zwilling https://app.gethookd.ai/share/ad/129130363?signature=2280883cdc1b06d68811f8455bca14dbebe3878407f4246090cb2afb6c5c467c |
| Seite | MagicSplashy |
| Markt/Sprache | AT, DE · de |
| Status | aktiv (beide) |
| Start / Ende / Laufzeit | 125662052: 17.07.2026 / läuft / **84 T** · 129130363: 28.07.2026 / läuft / **73 T** |
| Format | Video 93 s (720×1280), 2 Medien je Ad |
| Plattformen | facebook, instagram, audience_network, messenger, threads |
| Zielgruppe (EU) | 18–65, alle, EU-Reichweite 1.343.347 (125662052) |
| Headline | Nie wieder Bettwäsche wechseln 🛏️ |
| Primärtext (vollständig, = Standard-Body) | Decke + Bezug in einem 🌙<br><br>Die EasySleep Bettdecke macht Bettmachen endlich einfach. Waschen, trocknen und wieder aufs Bett legen.<br><br>✓ Nie wieder Ärger mit Überzügen <br>✓ Angenehm kühl im Sommer, wohlig warm im Winter <br>✓ Hypoallergen und antibakteriell<br><br>Heute 2 SoftCloud Kissenbezüge gratis (49,99€ Wert) sichern.<br><br>40 Tage risikofrei probeschlafen.<br><br>Genieße endlich ein Bett, das immer frisch ist. |
| Text im Video | Kopf-Overlay „Nie wieder Bettbeziehen ❌" (0–6 s) · Untertitel-Boxen zum Sprechtext · Feature-Overlays „100% WASCHBAR 🧼", „SCHNELL TROCKNEND ⏰", „TEMPERATUR REGULIEREND 🌡" · OEKO-TEX-Siegel · Balken „★★★★★ 17.000+ zufriedene Kunden, 5 Sterne" · eingeblendete Bewertungskarten „Werner ✓ ★★★★★" und „Sabine ✓ ★★★★★" · Sticker „Gratis KISSEN BEZÜGE" (Kontaktabzug alle 3 s) |
| Bildfolge | Montage aus mehreren UGC-Creators (mindestens 6 verschiedene Männer). Kampf mit dem Bezug (Blattmuster), Waschkeller mit Trockner und Waschmaschine, Wäschespinne, Schläfer im Bett, Vorher-Nachher. |
| CTA | ORDER_NOW |
| Landingpage | https://magicsplashy.de/products/easysleep-decke → **PDP** (leitet heute auf /products/easysleep-ganzjahresdecke um) |
| Hook | gesprochen: „Bettbeziehen ist einer der sinnlosesten Zeitfresser im Haushalt. Und trotzdem machst du es jede Woche, bis jetzt." · Overlay „Nie wieder Bettbeziehen ❌" |
| Angle | C Beziehen + A Hygiene („Wann hast du deine Bettdecke zuletzt wirklich gewaschen? Nicht den Bezug, die Decke selbst." / „Schweiß, Milben, Hautpartikel.") + D Ältere („Werner ist über 80. Witwer, das Bett alleine machen war immer ein Kraftakt.") + Allergie („Sabine … wegen ihrer Allergien") |
| Story-Muster | **Problem-Agitation-Voiceover + Mini-Fallgeschichten (Kunden-Testimonials) + Zeitstrahl** („Deine erste Nacht … Nach der ersten Woche … Nach einem Monat …"), Umdeutung „Das Problem ist nicht deine Bettwäsche, das Problem ist deine Decke." |
| Angebot | 40 Nächte Probeschlaf mit Geld-zurück-Garantie, 2 gratis SoftCloud-Kissenbezüge (49,99 €) |
| Spend / Performance | 125662052 **$10.001–20.000 · Winning** · 129130363 **$10.001–20.000 · Winning** (used_count 6) |
| Hook-Varianten (gleicher Body, alle 17.07., 84 T, aktiv, → PDP, $0–500) | **125662166** „Deine Bettdecke ist wahrscheinlich ekliger als deine Toilette. Klingt drastisch, ist aber so." (Testing) · **125661961** „Wann hast du deine Bettdecke zuletzt wirklich gewaschen? Nicht den Bezug, die Decke selbst." (Growing) · **125661932** „Über 15 Jahre lang jede Woche das Bett frisch beziehen und trotzdem nie unter einer wirklich sauberen Decke schlafen." (Growing) · DCO 196670519 (04.10.) |
| Einordnung | **Winner** (≥ 60 T, aktiv, höchster Spend). Ergebnis des Hook-Tests: Der Beziehen-Hook (C) hat den meisten Spend bekommen. Die Hygiene-Hooks (A) laufen weiter, aber mit wenig Budget. |

Transkript: Anhang A2 (Haupt-Ad) sowie A3 (Hook-Varianten).

### Weitere Story-Ads (Belege für B und D, noch zu jung für ein Urteil)
| Ad | Start / Laufzeit | LP | Hook wörtlich | Einordnung |
|---|---|---|---|---|
| [196670813](https://app.gethookd.ai/share/ad/196670813?signature=18c04d33e4f05286ddb4bfdab9774e13d7241a51984b8736c07555d2620be093) Video 32 s | 02.10. / 7 T | PDP Ganzjahresdecke | „Guter Schlaf in den Wechseljahren ist kein Zufall. Der fängt schon bei der richtigen Decke an. Eine Decke ohne Bezug. Wie soll das funktionieren?" | Test (Scaling) |
| [196670581](https://app.gethookd.ai/share/ad/196670581?signature=e5a96a5e315b625f975238b8a61f8c6c33672b8b2180347f4772d5f22026f3f8) Video 62 s | 02.10. / 7 T | PDP Ganzjahresdecke | „Ich hab mir die EasySleep bestellt, weil ich mit meinen Gelenken keine Kraft hatte, jede Woche mit der Bettwäsche zu kämpfen." | Test (Scaling) |
| [196672570](https://app.gethookd.ai/share/ad/196672570?signature=25fdd89bbee9e2fe42c316af211c2cca53a5142c9af403d5f8406c8a0fe30b20) DCO | 03.10. / 6 T | /pages/frauen-magazin | Titel „Frischer Schlafkomfort 💤" · „Nie wieder Bettbezug wechseln 🌙 Die EasySleep Bettdecke macht Bettmachen endlich einfach…" | Test |
| [199242833](https://app.gethookd.ai/share/ad/199242833?signature=c2c64fcf7462685c73857f0c7e57a8cb2f24b34e4be11ba708d5d460747472c9) Bild | 04.10. / 5 T | /pages/frauen-magazin | „Für alle, die keine Lust mehr haben, Bettwäsche zu beziehen aber trotzdem hygienisch schlafen wollen. 🌙 Die EasySleep Decke:" | Test |
| [112081287](https://app.gethookd.ai/share/ad/112081287?signature=1ca5bb5015a714bea59c41e4d0ddced6db782e5af5cbcd952a78eb9512d15313) Video 51 s | 14.05. / 148 T | PDP | „Viele schreiben, Bettbeziehen dauert doch nur zwei Minuten. Was für eine faule Generation. Und genau darum geht es eigentlich gar nicht." (Antwort auf Kommentare) | Winner nach Laufzeit (Spend $0–500, Growing) |
| [139047107](https://app.gethookd.ai/share/ad/139047107?signature=d92f3d774a51e16a6300c97ac99e88544f9fc74fb903be25e3686750f39f55f4) Video 39 s | 07.08. / 63 T | PDP | „Ich weiß nicht, wie die Decke das macht, aber egal, ob heiße Sommernacht oder plötzlicher Wetterumschwung. Ich schlafe einfach durch." | Winner nach Laufzeit (Optimized) |

Transkripte: Anhang A4.

---

## 4. Landingpages – Kurzzerlegung

Abgerufen am 08.10. mit `shot.js … mobile`. Dateien: `a3/pages/ms_<slug>.txt/.html/.png`. Die PNGs von gut-schlafen, frauen-magazin und schlafen-im-sommer stammen aus dem Lauf um 10:56 Uhr (`a3/lp/`), weil `networkidle` im neuen Lauf in den Timeout lief. Die Textlänge ist in beiden Läufen identisch. Wortzählung mit `scripts/wordpos.py`.

### LP 1 · /pages/schlafen-im-sommer (Ad 1) · Presell / Long-Form-Sales-Letter
- **Headline:** „Die Decke, die dich bei 30 Grad schlafen lässt wie bei 20. Warum sie ständig ausverkauft ist:"
- **Subheadline:** „Die EasySleep® 2-in-1 Decke – leicht, luftig und aus Klimafasern, die die Wärme rauslassen statt zu stauen."
- **Perspektive/Autor:** Markenstimme („Wir"). Am Ende stellen sich „Laureen Bimczok, Gründerin" und „Tobie Fallschmidt, MA, Leiter Produktentwicklung" (Textiltechnologie) vor.
- **Fake-Magazin-Optik:** nein (Shop-Optik). Unter dem CTA steht der Logo-Streifen „Bekannt aus": DER SPIEGEL, FOCUS Gesundheit, fit for fun, Apotheken Umschau, Men'sHealth.
- **Abschnitts-Überschriften:** „WIR HABEN BEREITS 17.000+ MENSCHEN GEHOLFEN, NIE WIEDER SCHWEISSGEBADET AUFZUWACHEN" · „EINE NORMALE DECKE IST IM SOMMER NICHTS ANDERES ALS EINE SAUNA, DIE DU DIR ÜBERZIEHST." · „Die Lösung" · „Wie es funktioniert / Die 5 Gründe, warum niemand mehr schwitzend aufwacht, und warum das kein Zufall ist" (1 „Kühl, auch wenn's draußen nicht abkühlt" · 2 „Komplett waschbar – Decke + Bezug in einem" · 3 „Leicht und luftig" · 4 „In 2 Stunden trocken – an der Luft" · 5 „Kühl im Sommer, warm im Winter – eine Decke für alles") · „97.3% wollen nach 40 Nächten nicht mehr zurück / UNBESTREITBARE ERGEBNISSE" · „Der neue No-Stress-Schlafplan: Einfach umsteigen und zusehen wie sich alles verändert" (Erste Nacht / Nach einer Woche / Nach zwei Wochen / Nach einem Monat) · „Funktioniert für Menschen jeden Alters, egal wie hitzeempfindlich sie sind" · „Mehr als nur eine Decke" · „Probiere unsere Decke noch heute aus" · „Dein Kauf ist geschützt durch unsere 40 Nächte 100% Geld-zurück-Garantie" · „Unsere Mission: …" · „Noch Fragen? Hier sind die häufigsten"
- **Produkt-Einführung:** nach **18 Wörtern** (Subheadline), 2.036 Wörter gesamt
- **Mechanismus:** „Eine normale Bettdecke hält die Wärme am Körper fest, statt sie rauszulassen. Die dicke Füllung staut die Hitze." Die „Klimafasern" leiten die Wärme ab. Weil Decke und Bezug eins sind, wird alles gewaschen.
- **Beweise:** „17.000+" Kunden; vier „Verifizierter Kauf"-Reviews (Frank M., Sabine W., Maria K., Werner H.: „Wer auch im Dachgeschoss schläft, weiß wovon ich rede."); „97.3%" aus der Kundenbefragung; Medienlogos; Experte für Textiltechnologie; Oeko-Tex.
- **Angebot/Knappheit/Garantie:** „79,99€ STATT 129,99€ mit gratis Kissenbezügen im Wert von 49,99€"; Knappheit schon in der Headline („Warum sie ständig ausverkauft ist"); 40 Nächte 100 % Geld zurück. Zusatz: „Wir waschen jede zurückgeschickte Decke und spenden sie anschließend an soziale Einrichtungen und Pflegeheime."
- **Für B und D relevant:** „✅ Perfekt für Menschen ab 55 – das Bett machen wird zum Kinderspiel, auch alleine" · „✅ Ideal bei Hitzewallungen – gerade wer nachts schneller ins Schwitzen kommt, schläft endlich wieder durch" · FAQ „Ist die Decke auch für ältere Menschen geeignet? Besonders gut. … Viele unserer Kunden über 70 schreiben, dass das Bettmachen zum ersten Mal wirklich einfach ist."
- **Für A relevant (FAQ):** „Ist es ohne Bezug nicht unhygienisch? Das Gegenteil ist der Fall. Weil du die gesamte Decke regelmäßig wäschst – nicht nur eine Hülle – ist sie hygienischer als jede normale Bettwäsche. Milben, Schweiß, Hautpartikel – alles wird gewaschen."

### LP 2 · /pages/umfrage (Ad 2) · Advertorial „Kundenumfrage", Listicle mit 10 Punkten
- **Headline:** „Was die Menschen über unsere Decke denken. Das Ergebnis hat selbst uns aus der Bahn geworfen."
- **Subheadline:** keine eigene. Darüber steht die Rubrikzeile „ALLES RUND UM DEN HAUSHALT".
- **Perspektive/Autor:** „Daniel K. / Kundenbetreuer MagicSplashy" mit Avatar, Ich-/Wir-Stimme
- **Fake-Magazin-Optik:** teilweise. Redaktionelle Optik mit Rubrik, Serif-Headlines (Playfair-Stil), Autorenzeile und Trennornamenten, aber offen als Markenseite gekennzeichnet (kein erfundener Publisher).
- **Abschnitts-Überschriften:** 01 „„Das Bettbeziehen war eine Qual für Kopf und Geist, ich konnte es nicht mehr."" · 02 „„Leicht" ist das Wort, das am häufigsten fiel" · 03 „„Keine Ahnung wie, aber sie wärmt und kühlt."" · 04 „„90% von Insta-Produkten sind ihr Geld nicht wert."" · [AKTUELLES ANGEBOT] · 05 „„Als Allergiker ein Segen, merke ich täglich."" · 06 „„Keine Waschtage mehr blocken, unfassbar wie genial!"" · 07 „„Ich schlafe endlich wieder durch, obwohl ich nur die Decke gewechselt habe."" · 08 „„Papa, damit er weniger Aufwand hat in seinem Alter."" · 09 „„Ich liebe sie, mehr Farben wären schön."" · 10 „„Warum gibt es das erst jetzt?""
- **Produkt-Einführung:** nach **90 Wörtern**, 1.309 Wörter gesamt
- **Mechanismus:** „Decke und Bezug sind eins. Runter vom Bett, in die Maschine, fertig." Dazu „ThermoBalance® Klimafaser" (leicht, wärmt und kühlt). Hygiene: „Normale Bettwäsche schützt die Decke nur oberflächlich. Schweiß, Hautschuppen und Milben sammeln sich trotzdem, Jahr für Jahr, unbemerkt."
- **Beweise:** „Über 2.000 Menschen haben geantwortet", „2.114 Kunden haben uns ihre ehrliche Meinung geschrieben", wörtliche Kundenzitate. Punkt 04 nimmt Skepsis offen auf: „„90% von Insta-Produkten sind ihr Geld nicht wert."" → 40 Tage Probeschlafen. Punkt 09 enthält ehrliche Kritik („mehr Farben").
- **Angebot:** „AKTUELLES ANGEBOT / Spare heute 30% + erhalte 2 SoftCloud Kissenbezüge gratis" · „HOHE NACHFRAGE" · „GRATIS VERSAND AB 150€" · „40 TAGE RISIKOFREI TESTEN". Alle 12 CTAs führen auf /products/easysleep-decke. Die CTAs sind thematisch beschriftet („Mehr zur Hygiene erfahren", „Als Geschenk bestellen", „Farben ansehen").
- **Kernpassagen wörtlich:** „Bezug ab, neuen drauf, Ecken suchen, alles verrutscht, nochmal von vorne. Jeden zweiten Sonntag dasselbe Ritual. Und irgendwann macht man es einfach, ohne es noch zu hinterfragen. Bis man merkt: Es war nie normal. Es war nur Gewohnheit." · Punkt 08: „Eine schwere Winterdecke ist für die eigenen Eltern oft mehr Last als Komfort. Beziehen, Waschen, Tragen, alles wird mit den Jahren beschwerlicher, aber selten spricht man offen darüber. … sehr oft die eigenen Eltern, wegen des geringeren Gewichts und der einfachen Handhabung. … Mehrere Kunden erzählten, dass sie zuerst für sich selbst bestellt und danach gleich nochmal für die Familie nachbestellt haben."

### LP 3 · /pages/gesund-schlafen (Ad 125662155; gleiche Story wie Hook-Variante 125661932) · Ich-Story-Advertorial eines Redakteurs, 10 Punkte
- **Headline:** „Ich habe 15 Jahre lang jede Woche Bettwäsche gewechselt."
- **Subheadline:** „Bis ich verstanden habe, dass das Problem die Decke war."
- **Perspektive/Autor:** Ich-Erzähler „Daniel K. / Haushalts- & Alltagsredakteur". Dasselbe Foto und derselbe Name erscheinen auf /umfrage als „Kundenbetreuer", die Persona ist also nicht konsistent.
- **Fake-Magazin-Optik:** teilweise. Gleiches Template wie /umfrage (Rubrik „ALLES RUND UM DEN HAUSHALT", Serif, Autor-Avatar).
- **Einstieg:** „Jeden zweiten Sonntag dasselbe Spiel: Bezug abziehen, Decke reinfummeln, Ecken suchen, fluchen. Ein Kreislauf, den ich nie hinterfragt habe. / „Warum wäschst du eigentlich nicht einfach die Decke selbst?" / Meine Antwort: „Passt nicht in die Maschine. Trocknet ewig." Ich lag falsch. Bei beidem."
- **Abschnitts-Überschriften:** 01 „Nie wieder Bettwäsche wechseln" („Das nervigste Ritual im Haushalt – einfach gestrichen") · 02 „Hygienischer als jede normale Bettwäsche" („Was die meisten nicht über ihre Decke wissen") · 03 „In 2–3 Stunden trocken" · 04 „Ganzjährig – eine Decke für jede Nacht" · 05 „Leicht genug für jede Waschmaschine" · [SOMMERANGEBOT] · 06 „Ideal für Allergiker" („Komplettreinigung statt Oberflächenschutz") · 07 „Weniger mentale Last" · 08 „Weniger Zeug, mehr Ordnung" · 09 „Das Geschenk, das wirklich benutzt wird" · 10 „Tausende, die nicht mehr zurück wollen"
- **Produkt-Einführung:** nach **117 Wörtern**, 897 Wörter gesamt
- **Mechanismus/Hygiene wörtlich:** „Normale Bettwäsche schützt die Decke nur oberflächlich. Schweiß, Hautpartikel und Milben gelangen trotzdem durch. Und die Decke? Wird quasi nie gewaschen, weil sie zu groß, zu schwer, zu unpraktisch ist. … Das ist nicht weniger hygienisch, sondern das Gegenteil: Es ist die sauberste Lösung, die du haben kannst."
- **Angebot:** „SOMMERANGEBOT / Spare heute 30% + erhalte 2 SoftCloud Kissenbezüge gratis / Ich war selbst skeptisch. Aber mit 40 Tagen Probeschlafen gibt es nichts zu verlieren." · „HOHE NACHFRAGE"
- **Für D relevant:** Punkt 09: „Viele Kunden bestellen EasySleep® zuerst für sich und dann nochmal für die Eltern, den Partner oder die Kinder."

### LP 4 · /pages/frauen-magazin (seit 03.10., 7 Ads, Test) · Wechseljahre-Listicle „7 Gründe"
- **Headline:** „Die Decke, unter der du seit Jahren schläfst, ist in den Wechseljahren dein größter Gegner."
- **Subheadline:** „7 Gründe, warum Frauen in den Wechseljahren jetzt ihre Bettdecke tauschen!"
- **Perspektive/Autor:** Du-Ansprache, kein Autor, keine Publisher-Marke sichtbar
- **Fake-Magazin-Optik:** nur ansatzweise: Blog- bzw. Ratgeber-Look mit großem Foto (Frau liegt nachts wach, Wecker „3:21"). Trotz des Slugs „frauen-magazin" gibt es kein Magazin-Logo.
- **Einstieg:** „Nachts um drei. Die Decke fliegt zur Seite. Fünf Minuten später ist dir kalt. Und dann geht das Gedankenkarussell los. Kennst du das? Dann bist du nicht allein."
- **Abschnitts-Überschriften:** „Grund 1: Schluss mit dem nächtlichen Schweißbad." · „Grund 2: Erst zu heiß, dann zu kalt. Eine Decke für beides." · „Grund 3: Leicht statt schwer und erdrückend." · „Grund 4: Nie wieder Bettbeziehen" · „Grund 5: Komplett waschbar und in 2 Stunden wieder trocken." · „Grund 6: Weil wenigstens das Bett easy sein darf" · „Grund 7: 17.000 Schläfer. Und du testest 40 Nächte ohne Risiko." · „DER EHRLICHE VERGLEICH / EasySleep im direkten Vergleich" · „HERBSTANGEBOT / 40 Nächte risikofrei testen" · „ECHTE ERFAHRUNGEN / So verändert EasySleep den Schlafalltag" · „Die häufigsten Fragen zur EasySleep" · „ECHTE ERFAHRUNGEN / Über 17.000 Kunden schlafen bereits ohne Bettbezug"
- **Produkt-Einführung:** nach **88 Wörtern**, 1.428 Wörter gesamt
- **Mechanismus:** „Herkömmliche Decken stauen die Wärme. Genau dann, wenn dein Körper sie loswerden will.." → „ThermoBalance® Klimafasern … Wärme kann entweichen". Wer nachts schwitzt, will öfter waschen, und das geht nur, wenn die ganze Decke in die Maschine passt (Grund 5).
- **Beweise:** 4,8 Sterne (Schlafkomfort 4,9/5 · Pflegeleichtigkeit 4,8/5 · Alltagserleichterung 4,9/5); Reviews mit Alter und Stadt, z. B. „Petra K., 49 – München: „Ich schlafe wieder wie vor den Wechseljahren"", „Ursula R., 58 – Hamburg: „Ich muss nachts nicht mehr aufstehen"". **Paar-Review:** „Sabine K., 55 – Bern: „Wir schlafen beide deutlich ruhiger" Seit den Wechseljahren ist mir nachts ständig heiß, mein Mann friert dagegen schnell. Früher gab's jede Nacht Deckengezerre. Mit EasySleep wird mir nicht mehr zu warm, und er friert trotzdem nicht. Klingt nach Werbung, ich weiß. Aber wir schlafen beide seitdem durch." Dazu eine Vergleichstabelle.
- **Angebot:** „HERBSTANGEBOT", 40 Nächte risikofrei, „Gratis Versand ab 150€"
- **Status:** erst 6 Tage alt, Wirkung nicht belegt (alle zugehörigen Ads: Testing/Scaling, Spend $0–500)

### LP 5 · /pages/gut-schlafen (177828057, 200300803, 200300922) · Presell-Bridge
- **Headline:** „"Nie wieder Bettwäsche wechseln am Sonntag"" · **Subheadline:** „Wie 17.000+ Deutsche dem Betten-Beziehen ade sagten - mit einer maschinenwaschbaren 2in1 Decke, bei der Bezug und Decke in einem sind"
- **Optik:** Shop-Presell mit „Bekannt aus Bild der Frau · Focus Online · Stern · WELT", „Das Original aus NRW" und einem Vorher-Nachher-Bild („VORHER: 2 TEILE" / „NACHHER: 1 TEIL")
- **Abschnitte:** „EasySleep Ganzjahresdecke: Bezug und Decke werden eins" · „DER EASYSLEEP UNTERSCHIED / Was sich für dich im Alltag ändert" (01 Kein Beziehen mehr · 02 Kein Verrutschen mehr · 03 Ganzjährig nutzbar · 04 Komplett waschbar · 05 Schnelltrocknend) · „DER EHRLICHE VERGLEICH" · „ECHTE ERFAHRUNGEN" · „HEUTIGES HERBSTANGEBOT / Heute 2 passende Kissenbezüge gratis sichern"
- **Produkt-Einführung:** nach 74 Wörtern, 1.310 Wörter gesamt

### Inaktive Vorgänger-LP · /pages/easysleep (11.06.–16.09., bis 98 T)
Headline „Ich hab mein Bett seit einem Jahr nicht mehr bezogen. / Und es ist sauberer als je zuvor." Der Hygiene-Block lautet „MIT JEDER NORMALEN DECKE SAMMELN SICH JAHRELANG MILBEN, SCHWEISS UND BAKTERIEN AN – UND DU KANNST NICHTS DAGEGEN TUN." Review „Werner H.: Ich bin Witwer und über 80 Jahre alt. Das Bett alleine machen war immer ein Kraftakt. Ecken suchen, Decke reinquetschen, alles verrutscht. Das jede Woche. Jetzt ist es einfach. Ich hab mir gleich eine zweite bestellt." Text: `a3/pages/ms_easysleep_inaktiv.txt`.

---

## 5. Was wir für Decken ohne Bezug in UK übernehmen

1. **C Beziehen (am besten belegt): das UGC-Ich-Story-Skript von Ad 1 fast 1:1 auf UK-Englisch übertragen.** Ablauf: Kaufgrund („I ordered it because I was sick of wrestling with the duvet cover every week") → Mechanismus „duvet and cover in one, the whole thing goes in the machine" → Einwand vorwegnehmen („Before you say it'll never dry…") → „And no, it's not laziness" → überraschender Zusatznutzen → Angebot. Overlay als Kampfansage („THAT'S IT FOR CHANGING DUVET COVERS!"). Laufen sollte es auf einer Presell-Seite und nicht nur auf der PDP: Die Presell-Version (schlafen-im-sommer) hat denselben Spend-Bucket wie die PDP-Versionen erreicht.
2. **Das Hook-Matrix-Prinzip von Ad 3:** Ein 90-s-Body bekommt 4–5 austauschbare Hooks, je einen pro Angle (C „pointless chore", A „Your duvet is probably dirtier than your toilet seat", A „When did you last actually wash your duvet – not the cover, the duvet itself?", D „Over 80, widowed, making the bed alone was a struggle"). MagicSplashy hat damit gelernt, dass C am meisten Spend trägt. Für den UK-Markt ist das noch offen und muss selbst getestet werden.
3. **A Hygiene:** die Umdeutung „The problem isn't your bedding – it's your duvet." Dazu das Argument „Normal bedding only protects the duvet on the surface. Sweat, skin flakes and dust mites still get through – and the duvet itself almost never gets washed." Den FAQ-Einwand „Isn't it unhygienic without a cover? The opposite…" auf jede LP setzen. Die inaktive Seite /easysleep zeigt einen guten Ich-Satz für A: „I haven't put a cover on my bed for a year – and it's cleaner than ever."
4. **B Wechseljahre:** Die Struktur der Frauenmagazin-Seite übernehmen: Szene „3 a.m., duvet off, five minutes later you're cold", dann „7 reasons why women going through the menopause are swapping their duvet now". Dazu kommen das Paar-Review („I'm too hot, my husband's always cold – no more tug of war") und das Argument „Wer nachts schwitzt, will öfter waschen". Wichtig: Bei MagicSplashy ist das noch ein Test (6 T). Den belegten Teil für B liefern Eight Sleep und Plufl, siehe dort.
5. **D Tochter kauft für Mutter:** MagicSplashy hat das Motiv nur in Bausteinen, nämlich Punkt 08 der Umfrage („„Papa, damit er weniger Aufwand hat in seinem Alter."" + CTA „Als Geschenk bestellen"), den Werner-Fall im Video, den Gelenke-Hook (196670581) und die FAQ für Ältere. **Ein eigenes Advertorial aus Sicht der Tochter fehlt dort.** Das ist eine echte Lücke, die wir in UK füllen können: „I bought one for my mum after watching her struggle with the duvet cover."
6. **LP-Bausteine, die wir übernehmen:** redaktionelles Template mit Rubrik und Autor (wie bei umfrage und gesund-schlafen); nummerierte Punkte mit Zitat als Zwischenüberschrift; nach jedem Punkt ein CTA mit Thema („Read more about hygiene", „Order as a gift"); Kundenumfrage als Beweisformat („We asked 2,000 customers…"); Zeitstrahl „first night / first week / after a month"; Bundle-Angebot (2 Kissenbezüge gratis) statt nur Rabatt.
7. **Vorsicht (Compliance UK/ASA):** Medienlogos („Bekannt aus"), „Verifizierter Kauf"-Reviews, „97,3 %" und die Spende an Pflegeheime nur mit echten Belegen verwenden. Gesundheitsaussagen (Allergie, Wechseljahre) vorsichtig formulieren.

## 6. Lücken
- Spend-Buckets sind EU-Schätzungen von GetHookd und keine echten Umsätze. Die Performance-Scores sind GetHookd-intern.
- Seite 4 der aktiven Ads (≤ 3 T alt) wurde nicht gesichtet. Bei den inaktiven Ads wurden nur die 40 längsten gesichtet (total 5.706, vermutlich viele DCO-Varianten).
- Musik und Tonspur der Videos wurden nicht analysiert; ausgewertet wurden nur Sprache (Transkript) und Overlays (Kontaktabzug).
- Ob die Bewertungen und Medienlogos auf den LPs echt sind, lässt sich nicht prüfen.
- Die PDP wurde nicht neu erfasst: /products/easysleep-decke leitet auf /products/easysleep-ganzjahresdecke um, und der Abruf lieferte nur 27 Zeichen. Der Preis (79,99 € statt 129,99 €) stammt von /schlafen-im-sommer.

---

## Anhang · Vollständige Transkripte (GetHookd/Whisper, Segmente [mm:ss])

Hinweis: Jede Ad hat 2 Medien (Formate) mit identischem Transkript; Status je Medium `completed`. Varianten 130714467, 112079893, 177828057 haben das Transkript von A1 (Ähnlichkeit ≥ 0,98).


### A1 · Ad 126012757 (UGC-Ich-Story, 57 s)
- Länge Sprache bis 56.6s
[00:00] Ich habe die Easy-Sleep-Decke bestellt, weil ich einfach keinen Bock mehr hatte,
[00:03] jede Woche mit der Bettwäsche zu kämpfen.
[00:05] Die ist nämlich Decke und Bettwäsche in einem.
[00:08] Heißt, du brauchst keine Bettwäsche mehr.
[00:09] Einfach die komplette Decke in die Waschmaschine und alles wird gewaschen.
[00:13] Nicht nur der Bezug wie bei normaler Bettwäsche, sondern wirklich alles.
[00:16] Und bevor du sagst, die wird doch nie trocken, die ist schnell trocknend.
[00:20] An der Luft zwei bis drei Stunden, im Trockner noch schneller.
[00:22] Passt locker in jede normale Waschmaschine, weil sie leicht und kompakt ist.
[00:26] Was mich aber echt überrascht hat, die Klimafasern.
[00:29] Im Sommer schlafe ich nicht mehr wie in der Sauna und schwitze nicht mehr.
[00:31] Mein Bett fühlt sich jetzt einfach jede Nacht frisch an, wie frisch geduscht ins Bett.
[00:35] Und nein, das ist keine Faulheit.
[00:37] Das ist einfach weniger Stress für den Alltag.
[00:39] Kein Gefungel mehr mit Ecken, kein Verrutschen, kein Ich-müsste-mal-wieder-wechseln.
[00:43] Einfach rein in die Maschine und fertig.
[00:45] Gerade gibt es die Easy-Sleep-Decke sogar im Angebot.
[00:48] Mit zwei gratis Soft-Cloud-Kissenbezügen im Wert von 49,99 Euro.
[00:52] Und mit 40 Tage Probeschlafen kannst du sie einfach selbst testen.
[00:55] Link ist unten.

### A1b · Ad 196670581 (Hook-Variante „Gelenke“, 62 s)
- Länge Sprache bis 62.4s
[00:00] Ich hab mir die EasySleep bestellt, weil ich mit meinen Gelenken keine Kraft hatte, jede Woche mit der Bettwäsche zu kämpfen.
[00:05] Ich hab die EasySleep-Decke bestellt, weil ich einfach keinen Bock mehr hatte, jede Woche mit der Bettwäsche zu kämpfen.
[00:11] Die ist nämlich Decke und Bettwäsche in einem. Heißt, du brauchst keine Bettwäsche mehr.
[00:15] Einfach die komplette Decke in die Waschmaschine und alles wird gewaschen.
[00:18] Nicht nur der Bezug wie bei normaler Bettwäsche, sondern wirklich alles.
[00:22] Und bevor du sagst, die wird doch nie trocken, die ist schnell trocknend.
[00:25] An der Luft zwei bis drei Stunden, im Trockner noch schneller.
[00:28] Passt locker in jede normale Waschmaschine, weil sie leicht und kompakt ist.
[00:32] Was mich aber echt überrascht hat, die Klimafasern.
[00:34] Im Sommer schlafe ich nicht mehr wie in der Sauna und schwitze nicht mehr.
[00:37] Mein Bett fühlt sich jetzt einfach jede Nacht frisch an, wie frisch geduscht ins Bett.
[00:41] Und nein, das ist keine Faulheit. Das ist einfach weniger Stress für den Alltag.
[00:45] Kein Gefummel mehr mit Ecken, kein Verrutschen, kein, ich müsste mal wieder wechseln.
[00:49] Einfach rein in die Maschine und fertig.
[00:51] Gerade gibt's die EasySleep-Decke sogar im Angebot.
[00:53] Mit zwei gratis SoftCloud-Kissenbezügen im Wert von 49,99 Euro.
[00:58] Und mit 40 Tagen Probeschlafen kannst du sie einfach selbst testen.
[01:01] Link ist unten.

### A2 · Ad 125662052 (Problem-Voiceover + Fallgeschichten, 93 s; Zwilling 129130363 identisch)
- Länge Sprache bis 93.2s
[00:00] Bettbeziehen ist einer der sinnlosesten Zeitfresser im Haushalt.
[00:03] Und trotzdem machst du es jede Woche, bis jetzt.
[00:05] Stell dir kurz eine Frage.
[00:06] Wann hast du deine Bettdecke zuletzt wirklich gewaschen?
[00:08] Nicht den Bezug, die Decke selbst.
[00:10] Die meisten waschen sie nie, weil sie nicht in eine normale Waschmaschine passt.
[00:13] Und selbst wenn. Trocknen dauert ewig.
[00:15] Schweiß, Milben, Hautpartikel.
[00:17] Alles sammelt sich an, während du dir selbst vormachst, dass nur den Bezugtauschen ausreicht.
[00:21] Und dann das wöchentliche Ritual.
[00:22] Alten Bezug abziehen, Ecken suchen, umständlich die Füllung reinquetschen, alles verrutscht.
[00:27] Und das immer wieder von vorne. Jede Woche.
[00:29] Für den Rest deines Lebens.
[00:30] Das Problem ist nicht deine Bettwäsche, das Problem ist deine Decke.
[00:32] Die EasySleep ist die erste Decke, die Decke und Bezug in einem ist.
[00:36] Nichts zum Beziehen, keine Ecken, kein Gefummeln.
[00:38] Einfach auflegen, fertig.
[00:39] So läuft der Waschtag. Einfach komplett rein.
[00:41] Passt in jede handelsübliche Waschmaschine.
[00:43] Die ganze Decke. Alles wird rausgewaschen.
[00:45] Und trocken ist sie in zwei Stunden, auch ohne Trockner.
[00:47] Morgens rein, abends frisch drauf.
[00:49] Dazu passen sich die Klimafasern automatisch deiner Körpertemperatur an.
[00:52] Kühl, wenn es warm ist, warm, wenn es kühler wird.
[00:54] Im Sommer schwitzt du nicht mehr, im Winter frierst du nicht.
[00:57] Decke das ganze Jahr. Öko-Text zertifiziert, Hypoallergen.
[01:00] Über 17.000 Menschen haben umgestellt.
[01:02] 97,3% wollen nach 40 Nächten nicht mehr zurück.
[01:05] Werner ist über 80.
[01:07] Witwer, das Bett alleine machen war immer ein Kraftakt.
[01:09] Jetzt ist es einfach.
[01:10] Und Sabine? Für sie ist das wöchentliche Decke waschen zur Routine geworden.
[01:13] Besonders wegen ihrer Allergien.
[01:15] Deine erste Nacht. Du fühlst dich leichter, frischer, anders.
[01:18] Nach der ersten Woche, Waschtag in zwei Stunden erledigt.
[01:20] Nach einem Monat, das nagende, ich müsste mal wieder wechseln, ist einfach weg.
[01:23] 40 Nächte Probeschlaf.
[01:25] Wenn du nicht begeistert bist, gibst das Geld einfach zurück.
[01:27] Gerade gibt es dazu noch zwei gratis Soft-Cloud-Kissenbezüge im Wert von 49,99 Euro.
[01:32] Link ist unten.

### A3a · Ad 125662166 (Hook-Variante Hygiene „ekliger als deine Toilette“, 92 s)
- Länge Sprache bis 92.2s
[00:00] Deine Bettdecke ist wahrscheinlich ekliger als deine Toilette.
[00:02] Klingt drastisch, ist aber so.
[00:04] Stell dir kurz eine Frage.
[00:05] Wann hast du deine Bettdecke zuletzt wirklich gewaschen?
[00:07] Nicht den Bezug, die Decke selbst.
[00:09] Die meisten waschen sie nie,
[00:10] weil sie nicht in eine normale Waschmaschine passt.
[00:12] Und selbst wenn.
[00:12] Trocknen dauert ewig.
[00:14] Schweiß, Milben, Hautpartikel.
[00:16] Alles sammelt sich an, während du dir selbst vormachst,
[00:18] dass nur den Bezugtauschen ausreicht.
[00:20] Und dann das wöchentliche Ritual.
[00:21] Alten Bezug abziehen, Ecken suchen,
[00:23] umständlich die Füllung reinquetschen, alles verrutscht.
[00:25] Und das immer wieder von vorne.
[00:27] Jede Woche, für den Rest deines Lebens.
[00:28] Das Problem ist nicht deine Bettwäsche.
[00:30] Das Problem ist deine Decke.
[00:31] Die EasySleep ist die erste Decke,
[00:33] die Decke und Bezug in einem ist.
[00:34] Nichts zum Beziehen, keine Ecken, kein Gefummeln.
[00:36] Einfach auflegen, fertig.
[00:38] So läuft der Waschtag.
[00:39] Einfach komplett rein.
[00:40] Passt in jede handelsübliche Waschmaschine.
[00:42] Die ganze Decke.
[00:42] Alles wird rausgewaschen.
[00:43] Und trocken ist sie in zwei Stunden.
[00:45] Auch ohne Trockner.
[00:46] Morgens rein, abends frisch drauf.
[00:47] Dazu passen sich die Klimafasern
[00:49] automatisch deiner Körpertemperatur an.
[00:51] Kühl, wenn es warm ist.
[00:52] Warm, wenn es kühler wird.
[00:53] Im Sommer schwitzt du nicht mehr.
[00:54] Im Winter frierst du nicht.
[00:55] Eine Decke das ganze Jahr.
[00:56] Öko-Text zertifiziert.
[00:58] Hypoallergen.
[00:58] Über 17.000 Menschen haben umgestellt.
[01:00] 97,3% wollen nach 40 Nächten nicht mehr zurück.
[01:04] Werner ist über 80.
[01:05] Witwer, das Bett alleine machen,
[01:07] war immer ein Kraftakt.
[01:08] Jetzt ist es einfach.
[01:09] Und Sabine?
[01:09] Für sie ist das wöchentliche Deckewaschen
[01:11] zur Routine geworden.
[01:12] Besonders wegen ihrer Allergien.
[01:13] Deine erste Nacht.
[01:14] Du fühlst dich leichter, frischer, anders.
[01:16] Nach der ersten Woche.
[01:17] Waschtag in zwei Stunden erledigt.
[01:19] Nach einem Monat.
[01:19] Das nagende, ich müsste mal wieder wechseln,
[01:21] ist einfach weg.
[01:22] 40 Nächte Probeschlaf.
[01:23] Wenn du nicht begeistert bist,
[01:24] gibt's das Geld einfach zurück.
[01:26] Gerade gibt es dazu noch zwei
[01:27] gratis Soft-Cloud-Kissenbezüge
[01:28] im Wert von 49,99 Euro.
[01:31] Link ist unten.

### A3b · Ad 125661961 (Hook-Variante „Wann hast du deine Bettdecke zuletzt wirklich gewaschen?“, 92 s) – nur Abweichung im Hook, Rest wie A3a
- Länge Sprache bis 92.0s
[00:00] Wann hast du deine Bettdecke zuletzt wirklich gewaschen?
[00:02] Nicht den Bezug, die Decke selbst.
[00:04] Stell dir kurz eine Frage.
[00:05] Wann hast du deine Bettdecke zuletzt wirklich gewaschen?
[00:07] Nicht den Bezug, die Decke selbst.
[00:09] Die meisten waschen sie nie,
[00:10] weil sie nicht in eine normale Waschmaschine passt.
[00:12] Und selbst wenn.
[00:13] Trocknen dauert ewig.
[00:14] Schweiß, Milben, Hautpartikel.
[00:16] Alles sammelt sich an, während du dir selbst vormachst,
[00:18] dass nur den Bezugtauschen ausreicht.
[00:20] Und dann das wöchentliche Ritual.
[00:21] Alten Bezug abziehen, Ecken suchen,
[00:23] umständlich die Füllung reinquetschen, alles verrutscht.
[00:25] Und das immer wieder von vorne.
[00:27] Jede Woche, für den Rest deines Lebens.
[00:29] Das Problem ist nicht deine Bettwäsche.
[00:30] Das Problem ist deine Decke.
[00:31] Die EasySleep ist die erste Decke,
[00:33] die Decke und Bezug in einem ist.
[00:35] Nichts zum Beziehen, keine Ecken, kein Gefummel.
[00:37] Einfach auflegen, fertig.
[00:38] So läuft der Waschtag.
[00:39] Einfach komplett rein.
[00:40] Passt in jede handelsübliche Waschmaschine.
[00:42] Die ganze Decke.
[00:43] Alles wird rausgewaschen.
[00:44] Und trocken ist sie in zwei Stunden.
[00:45] Auch ohne Trockner.
[00:46] Morgens rein, abends frisch drauf.
[00:47] Dazu passen sich die Klimafasern automatisch deiner Körpertemperatur an.
[00:51] Kühl, wenn es warm ist.
[00:52] Warm, wenn es kühler wird.
[00:53] Im Sommer schwitzt du nicht mehr.
[00:54] Im Winter frierst du nicht.
[00:55] Eine Decke das ganze Jahr.
[00:56] Öko-Text zertifiziert.
[00:57] Hypoallergen.
[00:58] Über 17.000 Menschen haben umgestellt.
[01:00] 97,3% wollen nach 40 Nächten nicht mehr zurück.
[01:04] Werner ist über 80.
[01:05] Witwer.
[01:06] Das Bett alleine machen war immer ein Kraftakt.
[01:08] Jetzt ist es einfach.
[01:09] Und Sabine?
[01:10] Für sie ist das wöchentliche Deckewaschen zur Routine geworden.
[01:12] Besonders wegen ihrer Allergien.
[01:13] Deine erste Nacht.
[01:14] Du fühlst dich leichter, frischer, anders.
[01:16] Nach der ersten Woche.
[01:17] Waschtag in zwei Stunden erledigt.
[01:18] Nach einem Monat.
[01:19] Das nagende, ich müsste mal wieder wechseln, ist einfach weg.
[01:22] 40 Nächte Probeschlaf.
[01:23] Wenn du nicht begeistert bist, gibst das Geld einfach zurück.
[01:26] Gerade gibt es dazu noch zwei gratis Softcloud-Kissenbezüge im Wert von 49,99 Euro.
[01:31] Link ist unten.

### A3c · Ad 125661932 (Hook-Variante „Über 15 Jahre…“, 93 s)
- Länge Sprache bis 93.2s
[00:00] Über 15 Jahre lang jede Woche das Bett frisch beziehen und trotzdem nie unter einer wirklich
[00:04] sauberen Decke schlafen.
[00:05] Stell dir kurz eine Frage.
[00:06] Wann hast du deine Bettdecke zuletzt wirklich gewaschen?
[00:09] Nicht den Bezug, die Decke selbst.
[00:10] Die meisten waschen sie nie, weil sie nicht in eine normale Waschmaschine passt.
[00:13] Und selbst wenn.
[00:14] Trocknen dauert ewig.
[00:15] Schweiß, Milben, Hautpartikel.
[00:17] Alles sammelt sich an, während du dir selbst vormachst, dass nur den Bezugtauschen ausreicht.
[00:21] Und dann das wöchentliche Ritual.
[00:23] Alten Bezug abziehen, Ecken suchen, umständlich die Füllung reinquetschen, alles verrutscht.
[00:27] Und das immer wieder von vorne.
[00:28] Jede Woche.
[00:29] Für den Rest deines Lebens.
[00:30] Das Problem ist nicht deine Bettwäsche.
[00:31] Das Problem ist deine Decke.
[00:32] Die EasySleep ist die erste Decke, die Decke und Bezug in einem ist.
[00:36] Nichts zum Beziehen, keine Ecken, kein Gefummel.
[00:38] Einfach auflegen, fertig.
[00:39] So läuft der Waschtag.
[00:40] Einfach komplett rein.
[00:41] Passt in jede handelsübliche Waschmaschine.
[00:43] Die ganze Decke.
[00:44] Alles wird rausgewaschen.
[00:45] Und trocken ist sie in zwei Stunden.
[00:46] Auch ohne Trockner.
[00:47] Morgens rein, abends frisch drauf.
[00:49] Dazu passen sich die Klimafasern automatisch deiner Körpertemperatur an.
[00:52] Kühl, wenn es warm ist.
[00:53] Warm, wenn es kühler wird.
[00:54] Im Sommer schwitzt du nicht mehr.
[00:55] Im Winter frierst du nicht.
[01:00] Über 17.000 Menschen haben umgestellt.
[01:02] 97,3 Prozent wollen nach 40 Nächten nicht mehr zurück.
[01:06] Werner ist über 80.
[01:07] Witwer, das Bett alleine machen war immer ein Kraftakt.
[01:09] Jetzt ist es einfacher.
[01:10] Und Sabine?
[01:11] Für sie ist das wöchentliche Deckewaschen zur Routine geworden.
[01:14] Besonders wegen ihrer Allergie.
[01:15] Deine erste Nacht.
[01:16] Du fühlst dich leichter, frischer, anders.
[01:18] Nach der ersten Woche, Waschtag in zwei Stunden erledigt.
[01:20] Nach einem Monat, das nagende, ich müsste mal wieder wechseln, ist einfach weg.
[01:24] 40 Nächte Probeschlaf.
[01:25] Wenn du nicht begeistert bist, gibst das Geld einfach zurück.
[01:27] Gerade gibt es dazu noch zwei gratis Soft-Cloud-Kissenbezüge im Wert von 49,99 Euro.
[01:32] Link ist unten.

### A4a · Ad 196670813 (Wechseljahre, 32 s)
- Länge Sprache bis 32.3s
[00:00] Guter Schlaf in den Wechseljahren ist kein Zufall.
[00:02] Der fängt schon bei der richtigen Decke an.
[00:04] Eine Decke ohne Bezug.
[00:05] Wie soll das funktionieren?
[00:06] Einfach drüberwerfen.
[00:07] Fertig und der Haushalt fühlt sich plötzlich viel leichter an.
[00:10] Wenn Waschtag ist, alles zusammen rein, Decke und Kissenbezüge.
[00:13] Zwei Stunden später trocken und alles fühlt sich so leicht und hochwertig an.
[00:17] Die Klimafasern sorgen dafür, dass du bei Hitzewallungen nicht schwitzt,
[00:20] aber im Winter trotzdem nicht drehst.
[00:21] Endlich wieder eine Nacht ohne ständiges Aufwachen.
[00:24] Warum hat das nicht schon früher jemand erfunden?
[00:26] Nur noch heute im Angebot.
[00:27] Plus zwei gratis Softcloud-Kissenbezüge und 40 Tage Probeschlaf.
[00:31] Ohne Risiko.

### A4b · Ad 112081287 (Antwort auf Kommentare „faule Generation“, 51 s)
- Länge Sprache bis 51.1s
[00:00] Viele schreiben, Bettbeziehen dauert doch nur zwei Minuten.
[00:02] Was für eine faule Generation.
[00:04] Und genau darum geht es eigentlich gar nicht.
[00:05] Es geht nicht nur ums Beziehen,
[00:07] sondern darum, dass alles in einem Schritt gewaschen wird.
[00:09] Die EasySleep ist Decke und Bezug in einem.
[00:12] Komplett waschbar.
[00:12] Das heißt, einfach in die Waschmaschine und alles ist sauber.
[00:15] Viele waschen aktuell nur den Bezug,
[00:17] aber die Decke selbst viel seltener.
[00:19] Hier wäscht du einfach alles auf einmal.
[00:20] Und keine Sorge, sie ist leichter als klassische Decken,
[00:23] passt in normale Maschinen,
[00:24] untrocknet an der Luft oft in zwei bis drei Stunden
[00:26] und trockner noch schneller.
[00:28] Durch die Klimafasern bleibt sie trotzdem angenehm warm
[00:30] und fühlt sich weich auf der Haut an.
[00:32] Am Ende ist es nicht weniger hygienisch,
[00:33] sondern sogar einfacher und sauberer.
[00:35] Wenn du dir das ganze Beziehen sparen willst,
[00:37] schau sie dir einfach mal an.
[00:39] Du bekommst 40 Tage Zeit, sie in deinem Alltag auszuprobieren,
[00:42] risikolos.
[00:42] Heute geben wir dir sogar unsere Softcloth Kissenbezüge
[00:45] gratis im Wert von 49,99 Euro dazu,
[00:48] damit du ein komplett neues Schlafgefühl genießen kannst.

### A4c · Ad 139047107 (Sommer/Durchschlafen, 39 s)
- Länge Sprache bis 39.3s
[00:00] Ich weiß nicht, wie die Decke das macht, aber egal, ob heiße Sommernacht oder plötzlicher Wetterumschwung.
[00:04] Ich schlafe einfach durch.
[00:05] Die Easy Sleep hat Klimafasern, die sich an deine Körpertemperatur antasten.
[00:08] Im Sommer bleibst du kühl, ohne zu frieren.
[00:10] Seit ich die hab, wache ich nicht mehr schweißgewadet auf.
[00:13] Ich schlafe einfach durch wie ein Baby.
[00:14] Das kannte ich im Sommer gar nicht mehr.
[00:16] Und das Beste, die ist Decke und Bettwäsche in einem.
[00:18] Einfach komplett in die Waschmaschine, in zwei Stunden trocken an der Luft.
[00:21] Nicht nur der Bezug, alles wird gewascht.
[00:23] Kein Gefummel mehr mit Bettwäsche, kein Verrutschen, kein Ich-müsste-mal-wieder-wechseln.
[00:27] Einfach rein in die Maschine und fertig.
[00:29] Gerade gibt's die Easy Sleep Decke im Angebot.
[00:31] Mit zwei gratis Softcloud-Kissenbezügen im Wert von 49,99 Euro.
[00:35] Und mit 40 Tage Probeschlafen kannst du sie einfach selbst testen.
[00:38] Link ist unten.

### A4d · Ad 196670101 („Nur 44 %…“ Herbst/Zeitumstellung, 81 s)
- Länge Sprache bis 81.4s
[00:00] Nur 44% der Easy-Sleep-Kunden waren sich vorher sicher, dass die Decke auch in kalten, dunklen
[00:05] Herbst- und Winternächten warm genug ist.
[00:07] Trotzdem würden die meisten sie gerade jetzt, kurz vor der Zeitumstellung, wieder kaufen.
[00:11] Die Easy-Sleep ist nämlich Decke und Bettwäsche in einem, heißt, du brauchst keine Bettwäsche
[00:16] mehr.
[00:17] Einfach die komplette Decke in die Waschmaschine und alles wird gewaschen.
[00:19] Nicht nur der Bezug wie bei normaler Bettwäsche, sondern wirklich alles.
[00:23] An der Luft 2-3 Stunden trocken, auch jetzt im Herbst und Winter, wenn du sie drinnen
[00:27] trocknen musst.
[00:28] Und sie passt locker in jede normale Waschmaschine.
[00:31] Was mich aber wirklich überzeugt hat, die Thermobalance-Klimafasern.
[00:34] Ich hab mich nämlich gefragt, hält die auch warm, wenn's draußen richtig kalt wird?
[00:38] Ja, ist mir kalt, wärmen die dünnen Fasern von Natur aus, ganz ohne dickes Material.
[00:44] Fang ich dagegen an zu schwitzen, leiten sie die Feuchtigkeit sofort ab, statt sie zu staunen.
[00:48] Kurz, wenn du schwitzt, kühlt sie, wenn du frierst, wärmt sie.
[00:51] Und du brauchst dafür keine extra Winterdecke, eine Decke für 365 Nächte im Jahr und nie
[00:57] wieder Bett beziehen.
[00:58] Und nein, das ist keine Faulheit, das ist einfach weniger Stress im Alltag, gerade jetzt
[01:02] in der dunklen Jahreszeit.
[01:03] Kein Gefummel mehr mit Ecken, kein Verrutschen, kein Ich-müsste-mal-wieder-Wechseln.
[01:07] Gerade jetzt, rechtzeitig vor der Zeitumstellung, gibt's die Easy Sleep im Angebot.
[01:12] Mit zwei gratis Soft-Cloud-Kissenbezügen im Wert von 49,99 Euro.
[01:16] Und mit 40 Tagen Probeschlaf kannst du sie einfach selbst testen.
[01:20] Link ist unten.
