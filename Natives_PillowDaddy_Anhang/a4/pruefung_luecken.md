# Pflichtlisten-Prüfung und offene Lücken (Schlussrunde Agent 4)

Stand 08.10.2026, 17:30 UTC. Geprüft wurden die Ergebnis-Dateien in `a1/`, `a2/`, `a3/` und `a4/` gegen den Auftrag. Die Lücken stammen aus den Abschnitten „Lücken“, „Methodik“ und „gaps“ der `grid_`-, `lp_`- und `brand_`-Dateien sowie aus eigenen Nachzählungen per Python. Bewertung: **erfüllt** / **teilweise** / **nicht erfüllt**.

---

## Agent 1 – PillowDaddy-Ads

| Pflichtpunkt | Status | Beleg | Offene Lücke (Grund) |
|---|---|---|---|
| Alle aktiven und inaktiven Ads der letzten 6 Monate | **erfüllt** | 6 Lanes, `ads_*.json`. Im Fenster liegen **4.472 IDs** auf den 10 PillowDaddy-Seiten, dazu Discovery (Brielle Grace 25 PillowDaddy- und 84 Fremd-Ads, Sofía 58). Jede Lane ist gegen GetHooked `meta.total` abgeglichen, inklusive Langläufer-Checks. | Zurückgehaltene aktive Ads sind nicht abrufbar: US 18 (DH 4, SR 1, GK 1, RF 12), CR 2, DK 3, GLJ 1. Grund: Index-Verzug bei GetHooked. Inaktive Persona-Seiten, die vor dem 12.06. endeten, sind nicht auffindbar (Restrisiko). |
| Volles Raster je Ad | **teilweise** | Einzelzeilen pro Ad: GLJ/Brandt 493, Marke 207, Discovery 167. Zeilen pro Copy-Cluster mit allen IDs im Anhang: US 346 Cluster (2.632 IDs), DE-Frauen 99 Cluster (1.140 IDs). | Spend fehlt für alle US-Ads (null). DE-Spend ist dünn: 92 % liegen im Bucket „0–$500“. Länder sind nur bei 115 von 493 GLJ-Ads abgefragt. Text im Bild: Bei 140 von 452 US-Mediengruppen nur per Tesseract-OCR erfasst, bei DE-Frauen nur die 3 häufigsten Motive je Cluster. Eingeblendeter Video-Text nur aus Start- bzw. Poster-Frame (US, GLJ). Grund jeweils: Zeit- und Kontextbudget. |
| **Jede** Video-Ad transkribiert | **teilweise** | US: 646 von 652 Medien `completed`, 2 `no_speech`. Marke, Discovery: keine Lücke vermerkt. DE-Frauen: keine Videos im Fenster. | **GLJ: 37 von 181 Video-Clustern haben nur die ersten 40 s** (lokal transkribiert), weil GetHooked bei Redaktionsschluss noch „processing“ meldete. US: 4 Medien `failed` (u. a. 117914555, 126713042), auch nach erneutem Anstoß. Whisper-Fehler bewusst nicht korrigiert. |
| Top 15 heruntergeladen, Aufbau in Sekunden | **erfüllt** | `a1/top15.md`: alle 15 IDs als mp4 lokal, 15 Sekunden-Tabellen (184 Zeitzeilen), Querschnitt mit Master-Dramaturgie. Nr. 13–15 sind inzwischen fertig. | Die Szenen-Spalte stützt sich auf je 20 Frames, nicht auf alle 100–200 Schnitte. Bei den Knete-Videos sind die Schnitte geschätzt. US-Ranking ohne Spend. |
| Advertorial/Listicle vs. Produktseite | **erfüllt** | LP-Typ steht in allen Grids. `a2/lp_inventar.json`: 4.206 von 4.533 IDs Native (92 %), 327 PDP. | 5 Native-LPs sind heute 404 (153 Ads). Ihr Typ ist nur vermutet. |
| Einordnung Winner/Kandidat/Test/Verlierer | **erfüllt** (mit Einschränkung) | Winner/Kandidat/Test/Verlierer je Grid: US 106/86/0/211 · DE-Frauen 63/47/0/70 · GLJ/Brandt 33/56/12/235 · Marke bis Juli 13/6/0/28 · Marke ab Aug. 6/40/0/32 · Discovery 10/26/28/26 | Die Einordnung beruht auf Laufzeit und Varianten, nicht auf Umsatz. „Test“ nutzen nur 2 Lanes, die anderen führen junge Ads als „Kandidat“. |

### Zahlen-Abgleich: Ads im Fenster je Seite, `a1/ads_*.json` vs. `a2/lp_inventar.json`

| Seite | Agent 1 (aktiv) | Inventar Agent 2 (aktiv) | Differenz |
|---|---|---|---|
| Claudia Reichardt | 634 (55) | 634 (55) | 0 |
| Daniela Koch | 342 (24) | 342 (24) | 0 |
| Karin Zimmermann | 164 (18) | 163 (18) | −1 (nicht aufgeklärt) |
| Gesund Leben Journal | 483 (74) | 483 (74) | 0 |
| Thomas Brandt | 10 (8) | 10 (8) | 0 |
| PillowDaddy (Marke, 2 Dateien, keine Überschneidung) | 207 (16) | 207 (16) | 0 |
| The Daily Health | 606 (30) | 606 (30) | 0 |
| Stephanie Robertson | 277 (16) | 317 (16) | **+40** |
| Gary Kuhlman | 299 (6) | 306 (6) | +7 |
| Rebecca Fitzgerald | 1.450 (5) | 1.465 (5) | +15 |
| **Summe** | **4.472 (252)** | **4.533 (252)** | **+61 (+1,4 %)** |

Die Aktivzahlen stimmen überall überein. Die Differenz entsteht fast vollständig bei den US-Personas (+62). Laut eigener Gap-Notiz zählt das Inventar diese Seiten über `collapse_variants` (Summe `variant_count`, „Näherung ±5 %“). Agent 1 hat dieselben Seiten einzeln aufgezählt und gegen `meta.total` geprüft. **Agent 1 ist deshalb die belastbarere Zahl.** Für den Bauplan heißt das: Die Kennzahl „92 % Native von 4.533“ ändert sich in der Größenordnung nicht, die Basis sollte aber 4.472 sein. Außerdem bezog sich „487 von 493“ auf GLJ und Brandt zusammen; GLJ allein hat 477 Native-Ads von 483 (im Bauplan korrigiert). Brielle Grace (UK) und Sofía (ES) fehlen im Inventar, weil sie über andere Domains laufen.

---

## Agent 2 – Native-Seiten

| Pflichtpunkt | Status | Beleg | Offene Lücke (Grund) |
|---|---|---|---|
| **Jede** Native-Seite erfasst | **teilweise** | 33 Seiten in `muster.md` §1 und `lp_struktur_alle.md` (33 Zeilen). `lp_analysen_alle.md` hat 34 Abschnitte, dazu kommen die Tiefenanalysen advert-6 und advert-7. | **5 Seiten sind 404** (us headaches-r-1 110 Ads, neck-pain-r-4 31, neck-pain-r-1 8, DE-t-2 3, anti-snoring 1). Inhalt nicht rekonstruierbar, weil Wayback mit 429 antwortet. Unverlinkte Slugs mit Zufallscode (Muster `-A391`) bleiben unentdeckt. |
| Perspektive/Autor, Fake-Magazin-Optik | **erfüllt** | Spalten in `muster.md` §1, Abschnitt 2.3 | Die Optik ist nur bei 18 Seiten per Screenshot geprüft, bei den übrigen aus HTML-Merkmalen abgeleitet. |
| Headline und Sub wörtlich | **erfüllt** | `lp_analysen_alle.md`, Sub-Formeln in `muster.md` 2.2 | Bei de_test_bauarten fehlt die Sub. |
| Aufbau mit Überschriften und Länge | **erfüllt** | `lp_struktur_alle.md`/`.json` (Mobile 390 px) | Abschnittsgrenzen sind heuristisch (±einige %). Manuell zerlegt sind nur advert-6 und advert-7. Text in Bildern ist nicht mitgezählt. |
| Produkt-Einführung nach X Wörtern | **erfüllt** | Spalte „Produkt nach“ in `muster.md` §1 (z. B. 848 W bzw. 24 %, T4 64 %) | fehlt bei den 404-Seiten |
| Mechanismus, Beweise, Angebot, Knappheit, Garantie, Übergang | **weitgehend erfüllt** | `lp_analysen_alle.md`, je Seite mit Zitaten | Ableger-Seiten (#14 Schulter, #16 Hände, #17 Migräne, #28–#32) sind nur verkürzt beschrieben („wie #13“). Bei einigen fehlen Angebot oder Übergang ausdrücklich. Der UK-Checkout `zifarra.com` wurde nicht abgerufen, Post-Purchase-Upsells sind unbekannt. |
| Wiederkehrende Muster | **erfüllt** | `muster.md` §2 (2.1–2.10) und §3 Schablone | Erfolg ist nur indirekt gemessen (Ad-Zahl, Laufzeit). Die 10–12 Video-Loops pro Seite sind nicht transkribiert. Google- und Taboola-Traffic ist mit GetHooked nicht messbar. |

---

## Agent 3 – weitere Native-Vorbilder

| Pflichtpunkt | Status | Beleg | Offene Lücke (Grund) |
|---|---|---|---|
| ≥ 8 Marken | **erfüllt** | 8 `brand_*.md`: MagicSplashy, UVlizer/Clairu, Plufl, Miracle Made, TrueClean, Rest, Eight Sleep/The Get Well, Cosy House. Dazu die Synthese `vorbilder_uebersicht.md` (erst 17:20 erschienen). | Ryer, GroundingWell, Aeyla (UK) und Pridola (UK) liegen nur als Sweep vor. Unter den 8 vertieften Marken läuft nur UVlizer in UK. |
| je 3 stärkste Native-/Story-Ads | **erfüllt** | je 3 Ads, teils mit Bonus-Ad (Miracle 4, Eight Sleep 4, UVlizer 3 + 3), mit `share_url` | Fehlende `share_url`s: UVlizer 27829561/27829534, Calmhaven 93024586, TrueClean 155122378/201101007, MagicSplashy-Hook-Varianten. Bei TrueClean 127732600 und Cosy Ad 2 wurde jeweils das zweite Medium nicht gesichtet. |
| Transkript | **erfüllt** (für alle Video-Ads) | Transkript-Anhänge bei Plufl, Cosy House, MagicSplashy, UVlizer; Rest 2 Videos, TrueClean 1 Video plus Schwester | Eight Sleep und Miracle haben nur Bild-Ads, dort liegen stattdessen die vollständigen Primärtexte vor. Musik und Ton sind nicht analysiert. Die Creator-Seiten von Cosy, Plufl und Rest wurden nicht transkribiert. |
| LP-Typ | **erfüllt** | LP-Zerlegung je Marke (Advertorial/Listicle/PDP/Publisher) | Nicht abgerufen wurden die MagicSplashy-PDP (Abruf leer), die Miracle-LP `/a/dermatologist-approved-sheets` und die TrueClean-LP `household-report`. Bei Plufl ist die gewinnende Headline-Variante unklar (Timeout). |
| Spend | – (kein Pflichtpunkt) | – | Spend gibt es nur bei MagicSplashy (EU). Für alle anderen Marken ist der Erfolg nur über Laufzeit und Score belegt. |

---

## Agent 4 – Bauplan (`a4/bauplan.md`)

| Pflichtpunkt | Status | Beleg | Offene Lücke |
|---|---|---|---|
| Je Angle Native-Format mit Begründung | **erfüllt** | A–D a), seit der Schlussrunde mit PillowDaddy-eigenen Belegen (Tochter-Winner, Ekelbilder, Wechseljahre als Einwand) | – |
| Story-Gerüst 8–10 Schritte | **erfüllt** | A 10, B 10, C 9, D 10. Für D gibt es zusätzlich den Abgleich mit dem Winner SR-K05 (Positionen in %). | Platzhalter (`[N]`, `[£XX]`, Gewicht, Trockenzeit) brauchen echte Produktdaten. |
| 3 Headline-Muster | **erfüllt** | Muster mit wörtlichem Original und Link: A 7, B 8, C 3, D 6 | C liegt genau am Minimum. |
| Vorlage mit Link | **erfüllt** | d)-Tabellen: A 9 Zeilen/13 Links, B 8/10, C 6/6, D 6/11. Neu: Seiten-Schablone (Kap. 1.5) und Video-Sekunden-Anker (Kap. 1.6). | Keine UK-Rechtsprüfung (Kap. 4 ist nur eine Leitplanke). Claims-Belege (Waschtest, Umfrage) fehlen noch. |

---

## Wichtigste offene Lücken (Priorität)

1. **GLJ-Transkripte:** 37 Video-Cluster haben nur den 40-s-Hook. Nachholen per `get_transcription_status`; betroffen sind vor allem K01- und K02-Hook-Varianten.
2. **Zählbasis:** Das Inventar liegt bei den US-Personas um 62 IDs über der Einzelzählung. Kennzahlen sollten auf 4.472 IDs (Agent 1) beruhen.
3. **5 Native-LPs sind 404 (153 Ads)**, darunter US headaches-r-1 mit 110 Ads. Aufbau und Mechanismus fehlen.
4. **Kein Spend für US/UK.** Winner-Urteile außerhalb von DE/AT beruhen nur auf Laufzeit und Varianten.
5. **PillowDaddy UK (Brielle Grace)** läuft erst seit 06.10. Der Erfolg ist offen; in 2–4 Wochen erneut prüfen.
6. **Eingeblendeter Video-Text** ist nur aus Startframes erfasst, Text in Bildern teils nur per OCR.
7. Für **Angle D** hat keine der 8 Vorbild-Marken ein vollständiges Tochter-Advertorial. Das beste Vorbild ist PillowDaddys eigene Long-Copy SR-K05/KZ-01. Das ist eine Lücke im Markt, keine Lücke der Research.
