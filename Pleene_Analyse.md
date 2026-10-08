# Pleene – Vollanalyse (ZWISCHENSTAND, Stand 2026-10-08)
> Zwischenstand: Inventar, Funnel, Reviews und Video-Batches 1–3 (21 von 63 Videos) sind fertig. Video-Batches 4–9, alle Statics, die Musteranalyse, die Chrome-/Nevio-Listen und die Angriffsfläche folgen.


## Teil 1 – Ads-Inventar

Stand: 2026-10-08 · Quelle: GetHooked (brand_id 7553008, „Pleene“), Abruf 2026-10-08 ca. 10:30–10:34 UTC · Analyse auf Deutsch, Anzeigentexte wörtlich im englischen Original.

### Zusammenfassung

- **Datenbasis:** 137 aktive Ads + 555 inaktive Ads mit Start ab 2026-04-08 (frühester gefundener Start: 2026-06-01) = **692 Ads**, jede einzeln im Vollinventar.
- **Aktive Ads nach Block:** Winner 20, Starker Kandidat 7, Neuer Test 94, Beobachten 16.
- **Inaktive Ads nach Block:** Verlierer (<7 T.) 202, Inaktiv (7–29 T.) 258, Inaktiv, lang gelaufen (≥30 T.) 95 → 36 % der inaktiven Ads liefen weniger als 7 Tage.
- **Formate aktiv:** Bild 73, Video 63, DCO 1. **Formate inaktiv:** Video 347, Bild 192, DPA (Katalog-Karussell) 8, DCO 7, Karussell 1.
- **Videolängen aktiv** (63 von 63 Videos mit Wert): min 9 s, Median 29 s, max 93 s. **Inaktiv** (347 von 347): min 9 s, Median 36 s, max 98 s.
- **Haupt-Angles aktiv:** C 60, A 22, B 14, F-Knappheit/Farbe 13, F-Selbstständigkeit im Alter 11, F-Einwand/Kaufhilfe 7, F-Social-Proof 6, D 1, n/a (kein Text) 1, F-Neuheit/Größe 1, F-Angebot 1.
- **Haupt-Angles der Winner:** C 7, F-Knappheit/Farbe 5, B 3, F-Social-Proof 3, F-Einwand/Kaufhilfe 2. Winner-Headlines: „No More Fighting With Duvet Covers“ ×7; „Properly Warm, Never Heavy“ ×3; „Everyone said it. They were right.“ ×3; „Mint Green is almost gone.“ ×2; „Check This Before You Buy“ ×2; „Everyone's buying the blue one.“ ×2; „Hearth Red. Nearly gone.“ ×1.
- **Landingpages aktiv:** pleene.com/products/easyrest 83, pleene.com/products/easyrest-comforter 40, pleene.com/pages/tb-6 8, pleene.com/products/easyrest-duvet 6. Alle aktiven Ads verlinken auf pleene.com (keine aktive Ad auf pleene.uk).
- **Nicht-EasyRest:** 76 inaktive Ads bewerben das Produkt „ZipSheet“ (LP pleene.com/products/zipsheet-us), Start 2026-08-03 bis 2026-09-02; aktuell keine aktive ZipSheet-Ad. Sie sind im Inventar enthalten und mit „Produkt: ZipSheet“ markiert.
- **Neue Tests (Start ≥ 2026-09-24, aktiv):** 94 Ads; davon mit frühem Signal (Score ≥ 41): 13.
- **Reichweite/Spend:** n/a – GetHooked liefert für GB keine Reichweite und keinen Spend. Ersatzsignale: days_active, performance_score (nur aktive Ads), used_count.

### Regeln & Datenbasis

**Abfragen (GetHooked MCP):**

| Abfrage | Parameter | Geliefert | meta / Einschränkungen |
|---|---|---|---|
| search_ads aktiv | brand_id=7553008, status=active, limit=100, page 1–2, sort start_date desc | 137 Zeilen (100 + 37) | meta.total=145 (total_is_exact=True, aber library_presence_coverage.total_is_upper_bound=true); withheld_this_page=8 auf Seite 2 → 8 Ads wurden zurückgehalten, weil sie im Index als „nicht mehr laufend“ erscheinen oder kein aktueller Brand-Sweep-Nachweis vorlag. Diese 8 sind nicht identifizierbar (nicht verifiziert, ob sie in der Inaktiv-Liste auftauchen). |
| search_ads inaktiv | brand_id=7553008, status=inactive, started_after=2026-04-08, limit=100, page 1–6 (+ limit=25 page 20 als Nachholabruf) | 555 eindeutige Zeilen | meta.total=555, total_is_exact=True, enumeration_incomplete=False → vollständig. Für **alle** inaktiven Ads ist performance_score = null (GetHooked bewertet beendete Ads nicht) → Score „n/a“. days_active_basis = start_to_end_date (Start bis letzte bestätigte Sichtung, inklusive). |
| Abgleich | agent1_enriched.json (137 aktive Ads) vs. frischer Abruf | 137 = 137 | keine neuen, keine fehlenden aktiven Ads; 0 Feldabweichungen bei Titel, Text, LP, CTA, Start, Tagen, Score, used_count, Plattformen, Format. |
| Videolängen | öffentlicher GetHooked-Share-Endpunkt `/api/get-shared-ad/<id>?signature=…` (dieselbe Signatur wie die share_url; liefert media[].video_length wie get_ad) | 427 von 427 Nicht-Bild-Ads | Validiert gegen search_ads(compact=false): 5 Stichproben identisch (28/51/23/23/44 s). Statt ~430 Einzelaufrufen von get_ad per Skript abgerufen (Kontextbudget). 3 Videos hatten bei GetHooked video_length 0 (136390115, 136390079, 133365161) → per ffprobe auf die GetHooked-Medien-URL gemessen (47 / 25 / 23 s). 22 Video-Ads haben 2 Medienvarianten (Platzierungen) mit jeweils gleicher Länge → ein Wert. DPA/DCO/Karussell: Anzahl Videos/Bilder laut Share-JSON. |

- Aktive Ads: end_date = letzte Sichtung (2026-10-07), days_active zählt bis heute (start_to_today). In den Tabellen steht bei aktiven Ads „aktiv“ statt Enddatum.
- Technischer Hinweis: Die Antwort von Seite 5 (inaktiv) wurde vom Tool bei 25 000 Tokens abgeschnitten; 99 von 100 Zeilen waren vollständig, die fehlende Zeile wurde über limit=25/page=20 (Zeilen 476–500) nachgeholt. Ergebnis: 555 eindeutige IDs = meta.total.
- Kosten: ca. 7,3 Credits (search_ads-Zeilen); get_user_profile kostenlos.

**Block-Regeln (verbindlich, mit dokumentierter Anpassung):**

| Block | Regel | Anzahl |
|---|---|---|
| Neuer Test | aktiv und Start ≥ 2026-09-24 (Vorrang vor allen anderen aktiven Blöcken) | 94 |
| Winner | aktiv, days_active ≥ 30 und Score ≥ 61 | 20 |
| Starker Kandidat | aktiv, 15–29 Tage mit Score ≥ 61 **oder** ≥ 30 Tage mit Score 41–60 | 7 |
| Beobachten | aktiv, ohne obiges Signal (z. B. lange Laufzeit, aber Score < 41) | 16 |
| Verlierer (<7 T.) | inaktiv und Laufzeit < 7 Tage | 202 |
| Inaktiv (7–29 T.) | inaktiv, 7–29 Tage gelaufen | 258 |
| Inaktiv, lang gelaufen (≥30 T.) | inaktiv, ≥ 30 Tage gelaufen („aufgegeben nach langer Laufzeit“) | 95 |

Anpassung: Der Vorgabe-Block „Inaktiv (≥ 7 Tage gelaufen)“ wurde in 7–29 T. und ≥ 30 T. geteilt, weil beendete Langläufer (z. B. die Juni-Ads mit 60–97 Tagen) ein anderes Signal sind als kurz getestete Ads. Zusammen ergeben beide den Vorgabe-Block. Neue Tests mit Score ≥ 41 werden in der Test-Liste als „frühes Signal“ markiert, bleiben aber Neuer Test.

**Weitere Regeln:**

- Ranking = days_active × max(used_count, 1) × max(performance_score, 1). Inaktive Ads haben keinen Score (→ Faktor 1).
- Angle-Codes (A Hygiene, B Wechseljahre/Temperatur, C Beziehen, D Geschenk, E körperliche Beschwerden, F-… weitere) wurden je Primärtext (bei identischem Text mit unterschiedlicher Headline zusätzlich nach Headline) vergeben; Haupt-Code zuerst. F-Codes: F-Knappheit/Farbe, F-Angebot, F-Social-Proof, F-Selbstständigkeit im Alter, F-Einwand/Kaufhilfe, F-Neuheit/Größe, F-Haustier, F-Gäste. Ads ohne Text: „n/a (kein Text)“, DCO mit Platzhalter `{{product.brand}}`: „n/a (Platzhalter-Text)“. Grundlage nur Headline + Primärtext (nicht Bild/Video-Inhalt).
- D (Geschenk) wird nur einmal vergeben: „Take the duvet-cover chore out of their routine.“ – Käufer ≠ Nutzer ist im Text impliziert, das Wort „gift“ kommt nicht vor (nicht verifiziert als Geschenk-Kampagne).
- Landingpage-Gruppierung nach Host + Pfad ohne Query (z. B. `?trybe=…`); im Vollinventar steht die komplette URL.
- Headline-Familie = gleiche Headline nach Normalisierung (Groß/Klein ignoriert, Mehrfach-Leerzeichen zusammengefasst, Schlusspunkt entfernt). „Pleene“ ist der Seitenname, der bei einigen Ads als Headline geliefert wird.
- Primärtexte stehen wörtlich; Zeilenumbrüche sind in Tabellen als `<br>` dargestellt, `|` maskiert. Texte, die ≥ 2 Ads nutzen, stehen einmal wörtlich im Anhang (T01 …) und werden in den Tabellen referenziert.
- Links: Ad Library `https://www.facebook.com/ads/library/?id=<Meta-ID>` und GetHooked-share_url (signierte Medien-URLs laufen nach 24 h ab und werden nicht verlinkt).

### Gruppierungen

#### (a) nach Landingpage

**Aktiv**

| Gruppe | Ads | Formate | Winner | Winner-Anteil | Starke Kand. | Neue Tests | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|---|
| pleene.com/products/easyrest | 83 | Video 46, Bild 37 | 20 | 24 % | 2 | 48 | 23.7 | 33.3 |
| pleene.com/products/easyrest-comforter | 40 | Bild 31, Video 8, DCO 1 | 0 | 0 % | 0 | 38 | 10.6 | 5.4 |
| pleene.com/pages/tb-6 | 8 | Video 6, Bild 2 | 0 | 0 % | 0 | 8 | 7.9 | 25.5 |
| pleene.com/products/easyrest-duvet | 6 | Bild 3, Video 3 | 0 | 0 % | 5 | 0 | 22.2 | 70.7 |

**Inaktiv**

| Gruppe | Ads | Formate | Verlierer (<7 T.) | Verlierer-Anteil | ≥30 T. gelaufen | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|
| pleene.com/products/easyrest | 407 | Video 262, Bild 138, DPA (Katalog-Karussell) 7 | 152 | 37 % | 71 | 17.2 | n/a |
| pleene.com/products/zipsheet-us | 76 | Video 46, Bild 29, Karussell 1 | 18 | 24 % | 4 | 13.5 | n/a |
| pleene.com/pages/duvet-10r | 19 | Video 15, Bild 4 | 19 | 100 % | 0 | 3.6 | n/a |
| pleene.com/products/easyrest-duvet | 15 | Bild 11, Video 4 | 8 | 53 % | 0 | 7.8 | n/a |
| pleene.com/products/easyrest-pdp | 14 | Video 9, Bild 3, DCO 2 | 1 | 7 % | 12 | 45.8 | n/a |
| pleene.com/products/pleene-easyrest-duvet-2in1 | 14 | Video 7, DCO 4, Bild 3 | 2 | 14 % | 7 | 31.7 | n/a |
| pleene.com/products/easyrest-everyday-duvet | 9 | Video 4, Bild 3, DPA (Katalog-Karussell) 1, DCO 1 | 1 | 11 % | 1 | 14.1 | n/a |
| pleene.com/products/easyrest-comforter | 1 | Bild 1 | 1 | 100 % | 0 | 4.0 | n/a |

#### (b) nach Angle

Haupt-Code (erster Code je Ad):

**Aktiv – Haupt-Code**

| Gruppe | Ads | Formate | Winner | Winner-Anteil | Starke Kand. | Neue Tests | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|---|
| C | 60 | Bild 37, Video 23 | 7 | 12 % | 2 | 43 | 21.9 | 21.6 |
| A | 22 | Video 15, Bild 7 | 0 | 0 % | 1 | 19 | 9.4 | 17.2 |
| B | 14 | Bild 8, Video 6 | 3 | 21 % | 4 | 5 | 19.4 | 49.5 |
| F-Knappheit/Farbe | 13 | Video 8, Bild 5 | 5 | 38 % | 0 | 7 | 27.3 | 47.7 |
| F-Selbstständigkeit im Alter | 11 | Bild 9, Video 2 | 0 | 0 % | 0 | 11 | 7.3 | 1.0 |
| F-Einwand/Kaufhilfe | 7 | Video 4, Bild 3 | 2 | 29 % | 0 | 2 | 20.7 | 34.6 |
| F-Social-Proof | 6 | Video 5, Bild 1 | 3 | 50 % | 0 | 3 | 30.2 | 54.7 |
| D | 1 | Bild 1 | 0 | 0 % | 0 | 1 | 2.0 | 1.0 |
| F-Angebot | 1 | Bild 1 | 0 | 0 % | 0 | 1 | 14.0 | 41.0 |
| F-Neuheit/Größe | 1 | Bild 1 | 0 | 0 % | 0 | 1 | 12.0 | 1.0 |
| n/a (kein Text) | 1 | DCO 1 | 0 | 0 % | 0 | 1 | 10.0 | 1.0 |

**Inaktiv – Haupt-Code**

| Gruppe | Ads | Formate | Verlierer (<7 T.) | Verlierer-Anteil | ≥30 T. gelaufen | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|
| C | 266 | Video 162, Bild 99, DPA (Katalog-Karussell) 5 | 70 | 26 % | 79 | 23.6 | n/a |
| A | 107 | Video 77, Bild 28, DPA (Katalog-Karussell) 2 | 60 | 56 % | 0 | 7.7 | n/a |
| F-Knappheit/Farbe | 56 | Video 34, Bild 22 | 23 | 41 % | 7 | 13.5 | n/a |
| F-Social-Proof | 51 | Video 46, Bild 4, Karussell 1 | 22 | 43 % | 1 | 9.8 | n/a |
| F-Angebot | 26 | Bild 14, Video 12 | 15 | 58 % | 0 | 8.6 | n/a |
| E | 18 | Video 11, Bild 6, DPA (Katalog-Karussell) 1 | 6 | 33 % | 0 | 11.2 | n/a |
| F-Einwand/Kaufhilfe | 8 | Bild 7, Video 1 | 0 | 0 % | 2 | 22.9 | n/a |
| n/a (Platzhalter-Text) | 6 | DCO 6 | 0 | 0 % | 3 | 33.0 | n/a |
| n/a (kein Text) | 5 | Video 4, DCO 1 | 3 | 60 % | 0 | 9.4 | n/a |
| B | 4 | Bild 4 | 0 | 0 % | 0 | 15.5 | n/a |
| F-Neuheit/Größe | 4 | Bild 4 | 1 | 25 % | 3 | 27.2 | n/a |
| F-Selbstständigkeit im Alter | 4 | Bild 4 | 2 | 50 % | 0 | 6.0 | n/a |

Alle Nennungen (Haupt- und Nebencodes; eine Ad zählt in mehreren Zeilen):

**Aktiv – alle Codes**

| Gruppe | Ads | Formate | Winner | Winner-Anteil | Starke Kand. | Neue Tests | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|---|
| C | 80 | Bild 49, Video 31 | 10 | 12 % | 2 | 59 | 20.2 | 20.6 |
| A | 53 | Video 36, Bild 17 | 7 | 13 % | 5 | 36 | 14.8 | 30.7 |
| F-Angebot | 42 | Video 23, Bild 19 | 9 | 21 % | 3 | 23 | 29.4 | 42.5 |
| B | 38 | Bild 22, Video 16 | 10 | 26 % | 7 | 14 | 32.2 | 47.5 |
| F-Knappheit/Farbe | 20 | Video 13, Bild 7 | 5 | 25 % | 0 | 12 | 22.5 | 39.2 |
| F-Selbstständigkeit im Alter | 14 | Bild 12, Video 2 | 0 | 0 % | 0 | 14 | 7.4 | 1.0 |
| F-Social-Proof | 8 | Video 6, Bild 2 | 5 | 62 % | 0 | 3 | 36.8 | 59.4 |
| F-Einwand/Kaufhilfe | 7 | Video 4, Bild 3 | 2 | 29 % | 0 | 2 | 20.7 | 34.6 |
| F-Gäste | 3 | Video 3 | 0 | 0 % | 0 | 3 | 4.0 | 15.0 |
| F-Haustier | 3 | Video 3 | 0 | 0 % | 0 | 3 | 4.0 | 15.0 |
| D | 1 | Bild 1 | 0 | 0 % | 0 | 1 | 2.0 | 1.0 |
| E | 1 | Bild 1 | 0 | 0 % | 0 | 1 | 15.0 | 1.0 |
| F-Neuheit/Größe | 1 | Bild 1 | 0 | 0 % | 0 | 1 | 12.0 | 1.0 |
| n/a (kein Text) | 1 | DCO 1 | 0 | 0 % | 0 | 1 | 10.0 | 1.0 |

**Inaktiv – alle Codes**

| Gruppe | Ads | Formate | Verlierer (<7 T.) | Verlierer-Anteil | ≥30 T. gelaufen | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|
| C | 362 | Video 230, Bild 126, DPA (Katalog-Karussell) 6 | 109 | 30 % | 82 | 20.3 | n/a |
| F-Angebot | 279 | Video 162, Bild 113, DPA (Katalog-Karussell) 4 | 94 | 34 % | 77 | 22.0 | n/a |
| B | 175 | Video 99, Bild 73, DPA (Katalog-Karussell) 3 | 39 | 22 % | 74 | 29.9 | n/a |
| A | 150 | Video 100, Bild 47, DPA (Katalog-Karussell) 3 | 76 | 51 % | 5 | 9.3 | n/a |
| F-Knappheit/Farbe | 115 | Video 86, Bild 29 | 59 | 51 % | 7 | 10.7 | n/a |
| E | 77 | Video 50, Bild 26, DPA (Katalog-Karussell) 1 | 20 | 26 % | 4 | 12.6 | n/a |
| F-Social-Proof | 68 | Video 59, Bild 8, Karussell 1 | 35 | 51 % | 1 | 9.1 | n/a |
| F-Einwand/Kaufhilfe | 22 | Video 13, Bild 7, DPA (Katalog-Karussell) 2 | 7 | 32 % | 2 | 12.4 | n/a |
| n/a (Platzhalter-Text) | 6 | DCO 6 | 0 | 0 % | 3 | 33.0 | n/a |
| n/a (kein Text) | 5 | Video 4, DCO 1 | 3 | 60 % | 0 | 9.4 | n/a |
| F-Neuheit/Größe | 4 | Bild 4 | 1 | 25 % | 3 | 27.2 | n/a |
| F-Selbstständigkeit im Alter | 4 | Bild 4 | 2 | 50 % | 0 | 6.0 | n/a |

#### (c) nach Format

**Aktiv**

| Gruppe | Ads | Formate | Winner | Winner-Anteil | Starke Kand. | Neue Tests | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|---|
| Bild | 73 | Bild 73 | 9 | 12 % | 3 | 49 | 20.3 | 23.4 |
| Video | 63 | Video 63 | 11 | 17 % | 4 | 44 | 17.4 | 30.2 |
| DCO | 1 | DCO 1 | 0 | 0 % | 0 | 1 | 10.0 | 1.0 |

**Inaktiv**

| Gruppe | Ads | Formate | Verlierer (<7 T.) | Verlierer-Anteil | ≥30 T. gelaufen | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|
| Video | 347 | Video 347 | 141 | 41 % | 45 | 15.3 | n/a |
| Bild | 192 | Bild 192 | 56 | 29 % | 47 | 20.0 | n/a |
| DPA (Katalog-Karussell) | 8 | DPA (Katalog-Karussell) 8 | 5 | 62 % | 0 | 6.9 | n/a |
| DCO | 7 | DCO 7 | 0 | 0 % | 3 | 30.4 | n/a |
| Karussell | 1 | Karussell 1 | 0 | 0 % | 0 | 8.0 | n/a |

#### (d) nach Startmonat

**Aktiv**

| Gruppe | Ads | Formate | Winner | Winner-Anteil | Starke Kand. | Neue Tests | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|---|
| 2026-06 | 5 | Bild 4, Video 1 | 3 | 60 % | 0 | 0 | 119.2 | 52.6 |
| 2026-08 | 12 | Video 10, Bild 2 | 12 | 100 % | 0 | 0 | 52.5 | 88.9 |
| 2026-09 | 73 | Bild 55, Video 17, DCO 1 | 5 | 7 % | 7 | 47 | 15.9 | 22.5 |
| 2026-10 | 47 | Video 35, Bild 12 | 0 | 0 % | 0 | 47 | 4.3 | 13.5 |

**Inaktiv**

| Gruppe | Ads | Formate | Verlierer (<7 T.) | Verlierer-Anteil | ≥30 T. gelaufen | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|
| 2026-06 | 23 | Video 16, Bild 7 | 0 | 0 % | 23 | 82.5 | n/a |
| 2026-07 | 48 | Bild 28, Video 20 | 0 | 0 % | 35 | 38.8 | n/a |
| 2026-08 | 257 | Video 163, Bild 83, DCO 6, DPA (Katalog-Karussell) 4, Karussell 1 | 60 | 23 % | 34 | 15.5 | n/a |
| 2026-09 | 225 | Video 148, Bild 72, DPA (Katalog-Karussell) 4, DCO 1 | 140 | 62 % | 3 | 7.4 | n/a |
| 2026-10 | 2 | Bild 2 | 2 | 100 % | 0 | 5.0 | n/a |

#### Produkt

**Aktiv**

| Gruppe | Ads | Formate | Winner | Winner-Anteil | Starke Kand. | Neue Tests | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|---|
| EasyRest | 137 | Bild 73, Video 63, DCO 1 | 20 | 15 % | 7 | 94 | 18.9 | 26.4 |

**Inaktiv**

| Gruppe | Ads | Formate | Verlierer (<7 T.) | Verlierer-Anteil | ≥30 T. gelaufen | Ø Tage | Ø Score |
|---|---|---|---|---|---|---|---|
| EasyRest | 479 | Video 301, Bild 163, DPA (Katalog-Karussell) 8, DCO 7 | 184 | 38 % | 91 | 17.5 | n/a |
| ZipSheet | 76 | Video 46, Bild 29, Karussell 1 | 18 | 24 % | 4 | 13.5 | n/a |

### Zeitachse

**Neue Ads pro Kalenderwoche (ISO-KW, letzte 8 Wochen, aktive + inaktive Ads nach Startdatum):**

| KW | Zeitraum | Neue Ads | davon aktiv / inaktiv | Video | Bild | DCO/DPA/Karussell | Haupt-Angles | neue Headline-Familien |
|---|---|---|---|---|---|---|---|---|
| 34 | 2026-08-17 – 2026-08-23 | 37 | 2 / 35 | 26 | 11 | 0 | C 24, F-Knappheit/Farbe 5, F-Social-Proof 4, A 3, E 1 | 3 |
| 35 | 2026-08-24 – 2026-08-30 | 91 | 3 / 88 | 68 | 21 | 2 | C 41, F-Social-Proof 19, F-Angebot 10, F-Knappheit/Farbe 9, A 6, F-Einwand/Kaufhilfe 3, F-Neuheit/Größe 3 | 10 |
| 36 | 2026-08-31 – 2026-09-06 | 73 | 4 / 69 | 56 | 15 | 2 | C 26, F-Knappheit/Farbe 20, A 16, F-Social-Proof 5, B 4, F-Angebot 1, n/a (kein Text) 1 | 7 |
| 37 | 2026-09-07 – 2026-09-13 | 81 | 3 / 78 | 60 | 19 | 2 | A 35, C 14, F-Social-Proof 13, F-Angebot 7, F-Knappheit/Farbe 5, B 3, n/a (kein Text) 3, F-Einwand/Kaufhilfe 1 | 1 |
| 38 | 2026-09-14 – 2026-09-20 | 46 | 10 / 36 | 22 | 24 | 0 | A 25, B 6, C 4, F-Knappheit/Farbe 4, F-Social-Proof 4, F-Angebot 3 | 5 |
| 39 | 2026-09-21 – 2026-09-27 | 76 | 37 / 39 | 32 | 43 | 1 | C 28, A 22, F-Knappheit/Farbe 6, F-Angebot 6, E 6, F-Einwand/Kaufhilfe 4, B 2, F-Neuheit/Größe 2 | 21 |
| 40 | 2026-09-28 – 2026-10-04 | 45 | 30 / 15 | 10 | 32 | 3 | C 16, F-Selbstständigkeit im Alter 11, A 9, F-Knappheit/Farbe 3, F-Social-Proof 3, E 2, n/a (kein Text) 1 | 16 |
| 41 | 2026-10-05 – 2026-10-11 (laufend) | 37 | 37 / 0 | 28 | 9 | 0 | C 15, A 10, F-Selbstständigkeit im Alter 4, F-Knappheit/Farbe 3, B 3, D 1, F-Einwand/Kaufhilfe 1 | 9 |

**Landingpages im Zeitverlauf:**

| Landingpage | erste Ad (Start · ID) | letzte neue Ad (Start) | Ads gesamt | aktiv | Produkt |
|---|---|---|---|---|---|
| pleene.com/products/easyrest | 2026-06-01 · 136388705 | 2026-10-06 | 490 | 83 | EasyRest |
| pleene.com/products/easyrest-pdp | 2026-07-14 · 133364629 | 2026-08-27 | 14 | 0 | EasyRest |
| pleene.com/products/zipsheet-us | 2026-08-03 · 133365264 | 2026-09-02 | 76 | 0 | ZipSheet |
| pleene.com/products/pleene-easyrest-duvet-2in1 | 2026-08-05 · 136389704 | 2026-09-12 | 14 | 0 | EasyRest |
| pleene.com/products/easyrest-everyday-duvet | 2026-08-20 · 151024464 | 2026-09-23 | 9 | 0 | EasyRest |
| pleene.com/pages/duvet-10r | 2026-08-25 · 157492467 | 2026-08-27 | 19 | 0 | EasyRest |
| pleene.com/products/easyrest-duvet | 2026-09-16 · 178749241 | 2026-09-28 | 21 | 6 | EasyRest |
| pleene.com/products/easyrest-comforter | 2026-09-23 · 182988038 | 2026-10-07 | 41 | 40 | EasyRest |
| pleene.com/pages/tb-6 | 2026-10-01 · 193234214 | 2026-10-02 | 8 | 8 | EasyRest |

**Auffälligkeiten (aus den Zahlen oben abgeleitet):**

- Höchster Start-Ausstoß in KW 35 (91 neue Ads). In den letzten 3 KW (39–41) 158 neue Ads, Bildanteil 53 % (KW 34–38: 27 %).
- Neue LP-Linie „easyrest-comforter“ (Wording „comforter“) ab 2026-09-23: 41 Ads, davon 40 aktiv; dort bislang kein Winner (Ø Score aktiv 5.4).
- Angle „F-Selbstständigkeit im Alter“ erscheint erst ab 2026-09-29 (18 Ads; aktiv 14, inaktiv 4); D (Geschenk/„their routine“) erstmals 2026-10-07.
- ZipSheet-Tests (US-LP) liefen 2026-08-03 bis 2026-09-07 (letzte Sichtung) und sind komplett beendet.

Vor KW 34 gestartet (im Datenfenster ab 2026-04-08): 206 Ads (11 davon noch aktiv).

**Erstes Auftreten je Angle (im Datenfenster; frühester Start, bei Gleichstand niedrigste ID):**

| Angle | Erste Ad als Haupt-Code | Erste Ad mit Code (Haupt- oder Nebencode) | Erste EasyRest-Ad als Haupt-Code | Ads gesamt (Haupt) | davon aktiv (Haupt) |
|---|---|---|---|---|---|
| A | 2026-08-14 · 145443310 („When Did You Last Wash Your Duvet?“, inactive) | 2026-08-07 · 139561410 („Mint Green is almost gone.“) | 2026-08-14 · 145443310 („When Did You Last Wash Your Duvet?“, inactive) | 129 | 22 |
| B | 2026-09-05 · 172403388 („Properly Warm, Never Heavy“, inactive) | 2026-06-01 · 136388705 („No More Fighting With Duvet Covers“) | 2026-09-05 · 172403388 („Properly Warm, Never Heavy“, inactive) | 18 | 14 |
| C | 2026-06-01 · 136388705 („No More Fighting With Duvet Covers“, inactive) | 2026-06-01 · 136388705 („No More Fighting With Duvet Covers“) | 2026-06-01 · 136388705 („No More Fighting With Duvet Covers“, inactive) | 326 | 60 |
| D | 2026-10-07 · 200490661 („Skip The  Duvet Cover“, active) | 2026-10-07 · 200490661 („Skip The  Duvet Cover“) | 2026-10-07 · 200490661 („Skip The  Duvet Cover“, active) | 1 | 1 |
| E | 2026-08-03 · 133365991 („Made for hands that hurt“, inactive) | 2026-08-03 · 133365264 („Never lift your mattress again.“) | 2026-09-25 · 184134594 („Change Your Bed Without The Pain After“, inactive) | 18 | 0 |
| F-Angebot | 2026-08-25 · 157492457 („End Of Season Sale“, inactive) | 2026-06-01 · 136388705 („No More Fighting With Duvet Covers“) | 2026-08-25 · 157492457 („End Of Season Sale“, inactive) | 27 | 1 |
| F-Einwand/Kaufhilfe | 2026-08-13 · 144538441 („Never lift your mattress again“, inactive) | 2026-08-13 · 144538441 („Never lift your mattress again“) | 2026-08-14 · 145443282 („What bed have you got?“, inactive) | 15 | 7 |
| F-Gäste | – | 2026-10-05 · 200037047 („The Spare Bed, Fresh For Every Guest“) | – | 0 | 0 |
| F-Haustier | – | 2026-10-05 · 200037045 („The Dog Can Stay On The Bed“) | – | 0 | 0 |
| F-Knappheit/Farbe | 2026-08-07 · 139561388 („Pick a colour. Watch.“, inactive) | 2026-08-07 · 139561388 („Pick a colour. Watch.“) | 2026-08-07 · 139561388 („Pick a colour. Watch.“, inactive) | 69 | 13 |
| F-Neuheit/Größe | 2026-08-25 · 157492463 („Now In Super King“, inactive) | 2026-08-25 · 157492463 („Now In Super King“) | 2026-08-25 · 157492463 („Now In Super King“, inactive) | 5 | 1 |
| F-Selbstständigkeit im Alter | 2026-09-29 · 186893837 („Keep Making Your Own Bed“, active) | 2026-09-29 · 186893814 („Your Routine, Made Simpler“) | 2026-09-29 · 186893837 („Keep Making Your Own Bed“, active) | 15 | 11 |
| F-Social-Proof | 2026-08-07 · 139561349 („Best decision I ever made.“, inactive) | 2026-08-07 · 139561349 („Best decision I ever made.“) | 2026-08-07 · 139561349 („Best decision I ever made.“, inactive) | 57 | 6 |
| n/a (Platzhalter-Text) | 2026-08-02 · 136388788 („–“, inactive) | 2026-08-02 · 136388788 („–“) | 2026-08-02 · 136388788 („–“, inactive) | 6 | 0 |
| n/a (kein Text) | 2026-08-07 · 139561473 („–“, inactive) | 2026-08-07 · 139561473 („–“) | 2026-08-07 · 139561473 („–“, inactive) | 6 | 1 |

**Headline-Familien (gleiche Headline = eine Familie), sortiert nach erstem Start:**

| # | Headline (Original) | Ads | aktiv | inaktiv | erster Start | letzter Start | Formate | Haupt-Angle(s) | Landingpages | Winner | Starke Kand. | bester Score (aktiv) | Verlierer |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | „No More Fighting With Duvet Covers“ | 175 | 20 | 155 | 2026-06-01 | 2026-10-06 | Video 98, Bild 77 | C | /pages/duvet-10r, /pages/tb-6, /products/easyrest, /products/easyrest-everyday-duvet, /products/easyrest-pdp, /products/pleene-easyrest-duvet-2in1 | 7 | 2 | 100 | 25 |
| 2 | „(ohne Headline)“ | 12 | 1 | 11 | 2026-08-02 | 2026-09-29 | DCO 8, Video 4 | n/a (Platzhalter-Text), n/a (kein Text) | /products/easyrest, /products/easyrest-comforter, /products/easyrest-everyday-duvet, /products/easyrest-pdp, /products/pleene-easyrest-duvet-2in1 | 0 | 0 | 1 | 3 |
| 3 | „Made for hands that hurt“ | 6 | 0 | 6 | 2026-08-03 | 2026-08-13 | Bild 6 | E | /products/zipsheet-us | 0 | 0 | n/a | 0 |
| 4 | „Never lift your mattress again.“ / „Never lift your mattress again“ | 66 | 0 | 66 | 2026-08-03 | 2026-09-02 | Video 42, Bild 23, Karussell 1 | C, E, F-Einwand/Kaufhilfe, F-Social-Proof | /products/zipsheet-us | 0 | 0 | n/a | 14 |
| 5 | „"Best thing I got for years."“ | 3 | 0 | 3 | 2026-08-07 | 2026-08-25 | Bild 3 | F-Social-Proof | /products/easyrest | 0 | 0 | n/a | 0 |
| 6 | „Best decision I ever made.“ | 12 | 0 | 12 | 2026-08-07 | 2026-09-08 | Video 12 | F-Social-Proof | /products/easyrest, /products/easyrest-everyday-duvet | 0 | 0 | n/a | 7 |
| 7 | „Everyone's buying the blue one.“ | 6 | 2 | 4 | 2026-08-07 | 2026-09-12 | Video 5, Bild 1 | F-Knappheit/Farbe | /pages/duvet-10r, /products/easyrest | 2 | 0 | 86 | 3 |
| 8 | „Hearth Red. Nearly gone.“ | 5 | 1 | 4 | 2026-08-07 | 2026-09-12 | Video 5 | F-Knappheit/Farbe | /pages/duvet-10r, /products/easyrest | 1 | 0 | 100 | 3 |
| 9 | „Mint Green is almost gone.“ / „Mint Green Is Almost Gone“ | 16 | 5 | 11 | 2026-08-07 | 2026-10-06 | Video 12, Bild 4 | F-Angebot, F-Knappheit/Farbe | /pages/duvet-10r, /products/easyrest, /products/easyrest-everyday-duvet | 2 | 0 | 100 | 6 |
| 10 | „Pick a colour. Watch.“ | 15 | 3 | 12 | 2026-08-07 | 2026-10-06 | Video 14, Bild 1 | F-Knappheit/Farbe | /products/easyrest | 0 | 0 | 12 | 3 |
| 11 | „Why people are switching.“ | 1 | 0 | 1 | 2026-08-07 | 2026-08-07 | Bild 1 | F-Social-Proof | /products/easyrest | 0 | 0 | n/a | 0 |
| 12 | „Not your normal fitted sheet“ | 4 | 0 | 4 | 2026-08-13 | 2026-08-14 | Video 4 | C | /products/zipsheet-us | 0 | 0 | n/a | 4 |
| 13 | „Duvet & Cover In One“ | 11 | 0 | 11 | 2026-08-14 | 2026-09-23 | Video 11 | C | /products/easyrest, /products/easyrest-everyday-duvet | 0 | 0 | n/a | 6 |
| 14 | „Everyone said it. They were right.“ | 20 | 5 | 15 | 2026-08-14 | 2026-10-01 | Video 20 | F-Social-Proof | /pages/duvet-10r, /pages/tb-6, /products/easyrest | 3 | 0 | 100 | 6 |
| 15 | „What bed have you got?“ | 7 | 3 | 4 | 2026-08-14 | 2026-09-23 | Bild 7 | F-Einwand/Kaufhilfe | /products/easyrest | 0 | 0 | 41 | 0 |
| 16 | „When Did You Last Wash Your Duvet?“ | 9 | 3 | 6 | 2026-08-14 | 2026-10-05 | Bild 6, Video 3 | A | /products/easyrest | 0 | 0 | 22 | 3 |
| 17 | „Which Colour Survives?“ | 3 | 0 | 3 | 2026-08-14 | 2026-08-14 | Bild 3 | F-Knappheit/Farbe | /products/easyrest | 0 | 0 | n/a | 0 |
| 18 | „Who Wins In Your House?“ | 5 | 0 | 5 | 2026-08-14 | 2026-08-25 | Bild 5 | F-Knappheit/Farbe | /pages/duvet-10r, /products/easyrest | 0 | 0 | n/a | 2 |
| 19 | „The Cover Is Sewn In“ | 12 | 0 | 12 | 2026-08-20 | 2026-09-08 | Video 9, Bild 3 | C | /products/easyrest | 0 | 0 | n/a | 6 |
| 20 | „The Duvet You Can Actually Wash“ | 20 | 1 | 19 | 2026-08-20 | 2026-10-01 | Video 19, Bild 1 | A | /pages/tb-6, /products/easyrest | 0 | 0 | 1 | 10 |
| 21 | „Which One Is Our Bestseller?“ | 3 | 0 | 3 | 2026-08-20 | 2026-08-20 | Video 3 | F-Knappheit/Farbe | /products/easyrest | 0 | 0 | n/a | 0 |
| 22 | „A Duvet With No Cover?“ | 15 | 0 | 15 | 2026-08-25 | 2026-09-08 | Video 15 | F-Social-Proof | /pages/duvet-10r, /products/easyrest | 0 | 0 | n/a | 7 |
| 23 | „End Of Season Sale“ | 12 | 0 | 12 | 2026-08-25 | 2026-09-08 | Video 12 | F-Angebot | /pages/duvet-10r, /products/easyrest | 0 | 0 | n/a | 7 |
| 24 | „I've Quit Bed Linen“ | 4 | 0 | 4 | 2026-08-25 | 2026-08-26 | Bild 4 | C | /products/easyrest | 0 | 0 | n/a | 4 |
| 25 | „Now In Super King“ | 5 | 1 | 4 | 2026-08-25 | 2026-09-27 | Bild 5 | F-Neuheit/Größe | /products/easyrest | 0 | 0 | 1 | 1 |
| 26 | „Pleene“ | 11 | 4 | 7 | 2026-08-26 | 2026-09-30 | Bild 5, DPA (Katalog-Karussell) 5, Video 1 | A, C, E, F-Selbstständigkeit im Alter | /products/easyrest, /products/easyrest-comforter, /products/easyrest-everyday-duvet | 0 | 0 | 1 | 4 |
| 27 | „2 Free Pillow Cases 🎁“ | 12 | 0 | 12 | 2026-08-29 | 2026-09-23 | Bild 12 | F-Angebot | /products/easyrest | 0 | 0 | n/a | 6 |
| 28 | „Check This Before You Buy“ | 5 | 4 | 1 | 2026-08-29 | 2026-10-06 | Video 5 | F-Einwand/Kaufhilfe | /products/easyrest | 2 | 0 | 100 | 0 |
| 29 | „Myth vs Truth 🛏️“ | 6 | 1 | 5 | 2026-08-29 | 2026-09-11 | Bild 6 | C | /products/easyrest | 0 | 0 | 1 | 1 |
| 30 | „The Duvet That Goes In The Wash“ | 12 | 0 | 12 | 2026-08-29 | 2026-09-08 | Video 12 | A | /products/easyrest | 0 | 0 | n/a | 6 |
| 31 | „Why This Duvet Needs No Cover“ | 4 | 0 | 4 | 2026-08-29 | 2026-08-29 | Video 4 | C | /products/easyrest | 0 | 0 | n/a | 0 |
| 32 | „Pleene EasyRest™ 2in1 Duvet“ | 1 | 0 | 1 | 2026-08-31 | 2026-08-31 | DPA (Katalog-Karussell) 1 | C | /products/easyrest | 0 | 0 | n/a | 0 |
| 33 | „Be honest. When did you last wash it?“ | 51 | 6 | 45 | 2026-09-05 | 2026-10-02 | Video 45, Bild 6 | A | /pages/tb-6, /products/easyrest | 0 | 0 | 60 | 27 |
| 34 | „Done fighting with bed linen.“ | 6 | 0 | 6 | 2026-09-05 | 2026-09-06 | Video 6 | C | /products/easyrest | 0 | 0 | n/a | 6 |
| 35 | „NEW: Lavender Mist“ | 7 | 3 | 4 | 2026-09-05 | 2026-10-06 | Bild 7 | F-Knappheit/Farbe | /products/easyrest | 0 | 0 | 60 | 1 |
| 36 | „Only 26 Left In Hearth Red“ | 3 | 0 | 3 | 2026-09-05 | 2026-09-05 | Bild 3 | F-Knappheit/Farbe | /products/easyrest | 0 | 0 | n/a | 3 |
| 37 | „Properly Warm, Never Heavy“ | 9 | 5 | 4 | 2026-09-05 | 2026-09-27 | Bild 9 | B | /products/easyrest | 3 | 0 | 100 | 0 |
| 38 | „Ready for the colder nights.“ | 4 | 0 | 4 | 2026-09-05 | 2026-09-06 | Video 3, Bild 1 | F-Knappheit/Farbe | /products/easyrest | 0 | 0 | n/a | 4 |
| 39 | „Pleene EasyRest™ Quilt“ | 1 | 0 | 1 | 2026-09-07 | 2026-09-07 | DPA (Katalog-Karussell) 1 | A | /products/easyrest | 0 | 0 | n/a | 1 |
| 40 | „"You'll Never Wash That." Watch Us.“ | 3 | 0 | 3 | 2026-09-16 | 2026-09-16 | Bild 3 | A | /products/easyrest-duvet | 0 | 0 | n/a | 3 |
| 41 | „No Launderette Needed. Ever.“ | 4 | 1 | 3 | 2026-09-16 | 2026-09-17 | Bild 4 | A | /products/easyrest-duvet | 0 | 1 | 81 | 3 |
| 42 | „The Duvet With No Cover To Change“ | 4 | 0 | 4 | 2026-09-16 | 2026-09-17 | Video 4 | F-Social-Proof | /products/easyrest-duvet | 0 | 0 | n/a | 2 |
| 43 | „Warm Enough For A British Winter“ | 5 | 5 | 0 | 2026-09-16 | 2026-09-20 | Video 3, Bild 2 | B | /products/easyrest-duvet | 0 | 4 | 81 | 0 |
| 44 | „Which Colour? Comment 1-9“ | 5 | 0 | 5 | 2026-09-16 | 2026-09-28 | Bild 5 | F-Knappheit/Farbe | /products/easyrest-duvet | 0 | 0 | n/a | 0 |
| 45 | „Simplify Your Bedding Routine“ | 2 | 2 | 0 | 2026-09-23 | 2026-09-24 | Bild 2 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 46 | „The Comforter That Does It All“ | 2 | 2 | 0 | 2026-09-23 | 2026-10-06 | Bild 2 | C | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 41 | 0 |
| 47 | „Clean Bedding, Made Easier“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | A | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 48 | „Fewer Steps. Fresher Bed.“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 49 | „Fresh Bedding Made Easy“ | 3 | 2 | 1 | 2026-09-24 | 2026-10-06 | Bild 3 | C | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 41 | 1 |
| 50 | „No Assembly Required“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 51 | „Skip the Cover“ | 2 | 2 | 0 | 2026-09-24 | 2026-09-24 | Bild 2 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 52 | „Skip The  Duvet Cover“ / „Skip The Duvet Cover“ | 2 | 2 | 0 | 2026-09-24 | 2026-10-07 | Bild 2 | C, D | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 53 | „Straight Back On The Bed“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 54 | „Take The Work Out Of Bedding“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 55 | „Warmth Without The Weight“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | B | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 56 | „Wash More Than The Sheets“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | A | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 57 | „Wash The Whole Comforter“ | 2 | 2 | 0 | 2026-09-24 | 2026-10-06 | Bild 2 | A | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 54 | 0 |
| 58 | „Wash. Dry. Done.“ | 1 | 1 | 0 | 2026-09-24 | 2026-09-24 | Bild 1 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 59 | „A Winter Duvet You Can Actually Lift“ | 3 | 0 | 3 | 2026-09-25 | 2026-09-25 | Video 3 | E | /products/easyrest | 0 | 0 | n/a | 3 |
| 60 | „Change Your Bed Without The Pain After“ | 4 | 0 | 4 | 2026-09-25 | 2026-09-30 | Video 4 | E | /products/easyrest | 0 | 0 | n/a | 1 |
| 61 | „Never Wrestle A Duvet Cover Again“ | 4 | 4 | 0 | 2026-09-25 | 2026-10-01 | Video 4 | C | /products/easyrest | 0 | 0 | 52 | 0 |
| 62 | „When Did You Last Wash The Duvet?“ | 5 | 0 | 5 | 2026-09-25 | 2026-10-01 | Bild 5 | A | /products/easyrest | 0 | 0 | n/a | 4 |
| 63 | „Winter-Ready In One Wash“ | 3 | 0 | 3 | 2026-09-25 | 2026-09-25 | Video 3 | A | /products/easyrest | 0 | 0 | n/a | 2 |
| 64 | „Yes, It Fits Your Machine“ | 5 | 0 | 5 | 2026-09-25 | 2026-09-30 | Bild 5 | A | /products/easyrest | 0 | 0 | n/a | 1 |
| 65 | „You Never Actually Wash Your Duvet“ | 4 | 0 | 4 | 2026-09-25 | 2026-09-29 | Video 4 | A | /products/easyrest | 0 | 0 | n/a | 0 |
| 66 | „A Duvet That Works For You“ | 1 | 1 | 0 | 2026-09-29 | 2026-09-29 | Bild 1 | F-Selbstständigkeit im Alter | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 67 | „Bedding Made For Your Routine“ | 1 | 1 | 0 | 2026-09-29 | 2026-09-29 | Bild 1 | F-Selbstständigkeit im Alter | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 68 | „Bedding That Fits Your Schedule“ | 1 | 1 | 0 | 2026-09-29 | 2026-09-29 | Bild 1 | A | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 69 | „Bedding Without The Struggle“ | 3 | 3 | 0 | 2026-09-29 | 2026-09-30 | Bild 3 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 70 | „Fresh Bed, Fewer Steps“ | 1 | 1 | 0 | 2026-09-29 | 2026-09-29 | Bild 1 | F-Selbstständigkeit im Alter | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 71 | „Keep Making Your Own Bed“ | 2 | 2 | 0 | 2026-09-29 | 2026-10-06 | Bild 2 | F-Selbstständigkeit im Alter | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 72 | „Meet The One-Piece Comforter“ | 1 | 1 | 0 | 2026-09-29 | 2026-09-29 | Bild 1 | F-Social-Proof | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 73 | „One Piece. Less To Handle.“ | 1 | 1 | 0 | 2026-09-29 | 2026-09-29 | Bild 1 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 74 | „Pleene EasyRest™ Duvet“ | 1 | 0 | 1 | 2026-09-29 | 2026-09-29 | DPA (Katalog-Karussell) 1 | C | /products/easyrest | 0 | 0 | n/a | 1 |
| 75 | „Skip The Cover. Keep The Comfort.“ | 2 | 2 | 0 | 2026-09-29 | 2026-09-29 | Bild 2 | C | /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 76 | „Your Bed. Your Way.“ | 2 | 2 | 0 | 2026-09-29 | 2026-10-06 | Bild 2 | F-Selbstständigkeit im Alter | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 77 | „Your Routine, Made Simpler“ | 2 | 2 | 0 | 2026-09-29 | 2026-10-06 | Bild 2 | C | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 78 | „A Simpler Way To Change The Bed“ | 1 | 1 | 0 | 2026-09-30 | 2026-09-30 | Bild 1 | C | /products/easyrest | 0 | 0 | 1 | 0 |
| 79 | „Fewer Steps To A Fresh Bed“ | 1 | 0 | 1 | 2026-09-30 | 2026-09-30 | Bild 1 | C | /products/easyrest | 0 | 0 | n/a | 1 |
| 80 | „Less To Handle. More Independence.“ | 1 | 0 | 1 | 2026-09-30 | 2026-09-30 | Bild 1 | F-Selbstständigkeit im Alter | /products/easyrest | 0 | 0 | n/a | 1 |
| 81 | „Skip The Duvet Cover Fuss“ | 1 | 0 | 1 | 2026-09-30 | 2026-09-30 | Bild 1 | F-Selbstständigkeit im Alter | /products/easyrest | 0 | 0 | n/a | 0 |
| 82 | „The Dog Can Stay On The Bed“ | 3 | 3 | 0 | 2026-10-05 | 2026-10-05 | Video 3 | A | /products/easyrest | 0 | 0 | 22 | 0 |
| 83 | „The Spare Bed, Fresh For Every Guest“ | 3 | 3 | 0 | 2026-10-05 | 2026-10-05 | Video 3 | A | /products/easyrest | 0 | 0 | 22 | 0 |
| 84 | „Too Thin For Winter? Look Closer.“ | 3 | 3 | 0 | 2026-10-05 | 2026-10-05 | Video 3 | B | /products/easyrest | 0 | 0 | 22 | 0 |
| 85 | „A Smarter Way To Do Bedding“ | 2 | 2 | 0 | 2026-10-06 | 2026-10-06 | Video 2 | C | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 86 | „Bedding Made for Independence“ | 2 | 2 | 0 | 2026-10-06 | 2026-10-06 | Video 2 | F-Selbstständigkeit im Alter | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 1 | 0 |
| 87 | „Ditch The Duvet Cover“ | 2 | 2 | 0 | 2026-10-06 | 2026-10-06 | Video 2 | C | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 12 | 0 |
| 88 | „Say Goodbye to Duvet Cover Hassle“ | 3 | 3 | 0 | 2026-10-06 | 2026-10-06 | Video 3 | C | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 12 | 0 |
| 89 | „The Bedding Upgrade Is Here“ | 2 | 2 | 0 | 2026-10-06 | 2026-10-06 | Video 2 | C | /products/easyrest, /products/easyrest-comforter | 0 | 0 | 12 | 0 |
| 90 | „The Easiest Bed Upgrade“ | 1 | 1 | 0 | 2026-10-06 | 2026-10-06 | Video 1 | C | /products/easyrest-comforter | 0 | 0 | 12 | 0 |

### Top 20 nach Ranking

Ranking = days_active × max(used_count,1) × max(Score,1), über alle 692 Ads (inaktive Ads haben keinen Score und landen dadurch nicht in den Top 20).

| Rang | GetHooked-ID | Meta-ID | Block | Start | Tage | used | Score | Ranking-Wert | Format | Länge | Headline | Angle | Landingpage | Links |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 136388964 | 884267707299487 | Winner | 2026-06-11 | 120 | 1 | 100 (Winning) | 12000 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=884267707299487) · [share](https://app.gethookd.ai/share/ad/136388964?signature=d0ff0d2a2536e91cfc3dacb7f3b055bf680241a71e3d485ea8d2c98436047966) |
| 2 | 136388847 | 1583232786477915 | Winner | 2026-06-11 | 120 | 1 | 100 (Winning) | 12000 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1583232786477915) · [share](https://app.gethookd.ai/share/ad/136388847?signature=422777a4ae4663b915702dc330ccb3f999733ab57559e373f53beb6af24567f7) |
| 3 | 145443331 | 1440933327878495 | Winner | 2026-08-14 | 56 | 2 | 100 (Winning) | 11200 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1440933327878495) · [share](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) |
| 4 | 136389861 | 1642037860240117 | Winner | 2026-06-11 | 120 | 1 | 61 (Growing) | 7320 | Video | 38 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1642037860240117) · [share](https://app.gethookd.ai/share/ad/136389861?signature=52dff4dac27abf45e6f9b062724b0d38f817b3ddcd8939d92684a863d31faaf8) |
| 5 | 133366534 | 1372761711494763 | Winner | 2026-08-03 | 67 | 1 | 100 (Winning) | 6700 | Video | 93 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1372761711494763) · [share](https://app.gethookd.ai/share/ad/133366534?signature=ec7e21facd4f53244e7aacaf8002b409a7803a538b1d302bb66be766c52ef924) |
| 6 | 139561428 | 1034362836068724 | Winner | 2026-08-07 | 63 | 1 | 100 (Winning) | 6300 | Video | 16 s | Hearth Red. Nearly gone. | F-Knappheit/Farbe | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1034362836068724) · [share](https://app.gethookd.ai/share/ad/139561428?signature=1eb14bdf7f1f4b278f8b5996d37204958181d02f07e10262e225457c7f9a49fd) |
| 7 | 139561410 | 1355121136744622 | Winner | 2026-08-07 | 63 | 1 | 100 (Winning) | 6300 | Video | 16 s | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1355121136744622) · [share](https://app.gethookd.ai/share/ad/139561410?signature=8993cc76f99c424613789bd7c6c9a9248d166b223587f503929e5077c7a435b2) |
| 8 | 139561491 | 1526037445508180 | Winner | 2026-08-07 | 63 | 1 | 86 (Optimized) | 5418 | Video | 16 s | Everyone's buying the blue one. | F-Knappheit/Farbe, F-Social-Proof | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1526037445508180) · [share](https://app.gethookd.ai/share/ad/139561491?signature=5cbb3a8ead3ed2e5b41ef6ef544d7498f90d8427b339e0ba7304f344c120fb43) |
| 9 | 163921089 | 1609110380938946 | Winner | 2026-08-27 | 43 | 1 | 100 (Winning) | 4300 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1609110380938946) · [share](https://app.gethookd.ai/share/ad/163921089?signature=18918dab03620f19a44f0f4ae4aabab8d5f163dfaa3984dcc8e6e691c7301c1d) |
| 10 | 145443318 | 1474663121347221 | Winner | 2026-08-14 | 56 | 1 | 74 (Growing) | 4144 | Video | 50 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1474663121347221) · [share](https://app.gethookd.ai/share/ad/145443318?signature=be73a154548ac1fdbbec6cdf47867c12c72f8b288e40c2faaa6b1db18c69b49b) |
| 11 | 151025063 | 1369166828764339 | Winner | 2026-08-22 | 48 | 1 | 86 (Optimized) | 4128 | Video | 29 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1369166828764339) · [share](https://app.gethookd.ai/share/ad/151025063?signature=6a64477f3dd49f4b0e862e714a6a052a0839cfe3382654d8e4902e827f95d481) |
| 12 | 168246678 | 1607904514111212 | Winner | 2026-08-29 | 41 | 1 | 100 (Winning) | 4100 | Video | 27 s | Check This Before You Buy | F-Einwand/Kaufhilfe, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1607904514111212) · [share](https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59) |
| 13 | 171191667 | 1583757549405276 | Winner | 2026-09-03 | 36 | 1 | 100 (Winning) | 3600 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1583757549405276) · [share](https://app.gethookd.ai/share/ad/171191667?signature=b03cc4b1b86af6280d5edfa0028fe241e19fd20d3b3592e580dd3f576a92669d) |
| 14 | 168246686 | 2035183934551496 | Winner | 2026-08-29 | 41 | 1 | 86 (Optimized) | 3526 | Video | 27 s | Check This Before You Buy | F-Einwand/Kaufhilfe, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2035183934551496) · [share](https://app.gethookd.ai/share/ad/168246686?signature=a360c60671d85ebeec646d4238239e0ec57ba2d7b037d0bb4c8888b606378db0) |
| 15 | 172403389 | 1725326416267519 | Winner | 2026-09-05 | 34 | 1 | 100 (Winning) | 3400 | Bild | – | Properly Warm, Never Heavy | B, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1725326416267519) · [share](https://app.gethookd.ai/share/ad/172403389?signature=fc57a29e066c788034eca64a557143f0c3e0b71232ea5868d51df06e7536000f) |
| 16 | 172760571 | 1415553300514250 | Winner | 2026-09-06 | 33 | 1 | 100 (Winning) | 3300 | Bild | – | Properly Warm, Never Heavy | B, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1415553300514250) · [share](https://app.gethookd.ai/share/ad/172760571?signature=82cd0a698c2d4720c44c69a474abfa9e4e1f24189f59d7dd6d1f216aaf8e25b8) |
| 17 | 151025052 | 1363184622691769 | Winner | 2026-08-20 | 50 | 1 | 61 (Growing) | 3050 | Bild | – | Everyone's buying the blue one. | F-Knappheit/Farbe, F-Social-Proof | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1363184622691769) · [share](https://app.gethookd.ai/share/ad/151025052?signature=fa0ac684d0e23c918a286f4c72318a4110a6ecece18af70548ebdfc97ba1bc3e) |
| 18 | 169082912 | 2192690231462965 | Winner | 2026-08-31 | 39 | 1 | 74 (Growing) | 2886 | Bild | – | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2192690231462965) · [share](https://app.gethookd.ai/share/ad/169082912?signature=4ab996ca26c1daf73d6ef9a482fc283fbce80f5ccef0bc6ead1abbcdb159c5e0) |
| 19 | 173307160 | 1770207397626174 | Winner | 2026-09-07 | 32 | 1 | 81 (Optimized) | 2592 | Bild | – | Properly Warm, Never Heavy | B, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1770207397626174) · [share](https://app.gethookd.ai/share/ad/173307160?signature=20a01e20e8d0bc5720968b8ee00d824e45a8e18af15aa506b60fd22b7789241f) |
| 20 | 174599778 | 2301727147248244 | Winner | 2026-09-09 | 30 | 1 | 74 (Growing) | 2220 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2301727147248244) · [share](https://app.gethookd.ai/share/ad/174599778?signature=0f3b267681520755857f3c8967162b7f9b49eb9f935ce9ac83a4c94572252bc1) |

### Neue Tests (aktiv, Start ≥ 2026-09-24)

94 Ads. Frühes Signal = Score ≥ 41 bereits jetzt.

| # | GetHooked-ID | Meta-ID | Start | Tage | Format | Länge | Headline | Angle | Landingpage | CTA | Score | used | frühes Signal | Links |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 200490661 | 2272066053740371 | 2026-10-07 | 2 | Bild | – | Skip The  Duvet Cover | D, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2272066053740371) · [share](https://app.gethookd.ai/share/ad/200490661?signature=114722e2aec9d0a68a974913b4cf9f5a2ba74b9f5bf1d0b762ad013438a493dc) |
| 2 | 200490726 | 2479370542555841 | 2026-10-06 | 3 | Bild | – | Fresh Bedding Made Easy | C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2479370542555841) · [share](https://app.gethookd.ai/share/ad/200490726?signature=115b524a7494fc7321eeae317f8c27392d4975dd61a417a7abb8ca8b737a684c) |
| 3 | 200490725 | 1598917498396809 | 2026-10-06 | 3 | Bild | – | Wash The Whole Comforter | A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1598917498396809) · [share](https://app.gethookd.ai/share/ad/200490725?signature=67a10c5447fc7a3f8b569d83dfdc87c2601d377c0332e160872fa4f4e059ff1f) |
| 4 | 200490724 | 1488098906488814 | 2026-10-06 | 3 | Bild | – | Your Routine, Made Simpler | C, F-Selbstständigkeit im Alter | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1488098906488814) · [share](https://app.gethookd.ai/share/ad/200490724?signature=1567b21782ab0caddb1ff07fb11120d7672fb131b518752e7470ef2b72b7247f) |
| 5 | 200490723 | 1478232800908923 | 2026-10-06 | 3 | Bild | – | The Comforter That Does It All | C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1478232800908923) · [share](https://app.gethookd.ai/share/ad/200490723?signature=2e878d2a1eb5ff26136f4a2e83dcb09f424a5e3d8b59e961f3a1802dbbd9232b) |
| 6 | 200490722 | 1103563399362311 | 2026-10-06 | 3 | Video | 28 s | A Smarter Way To Do Bedding | C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1103563399362311) · [share](https://app.gethookd.ai/share/ad/200490722?signature=dd70cdeb1b3f44685b65dd999b089fa20ba19c1b6db90d019468210a9539d0a1) |
| 7 | 200490721 | 2373725086706676 | 2026-10-06 | 3 | Video | 51 s | The Bedding Upgrade Is Here | C, B | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2373725086706676) · [share](https://app.gethookd.ai/share/ad/200490721?signature=8697f9fa84603c6c5fe39198bba6510a3c6efe060e8c12de0cac95d04e13450e) |
| 8 | 200490720 | 1660322526104618 | 2026-10-06 | 3 | Bild | – | Your Bed. Your Way. | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1660322526104618) · [share](https://app.gethookd.ai/share/ad/200490720?signature=ba2af6dc6e4e320ef5b15b27078c4635dda547216aef3cdbec06294ee1c182e7) |
| 9 | 200490719 | 1099152986192830 | 2026-10-06 | 3 | Video | 23 s | Ditch The Duvet Cover | C, A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1099152986192830) · [share](https://app.gethookd.ai/share/ad/200490719?signature=02b20c37beecbaad1d44b7e74cd81762006aa203ca85a92692a4fce5b3aa9e84) |
| 10 | 200490718 | 969394622234742 | 2026-10-06 | 3 | Video | 23 s | Bedding Made for Independence | F-Selbstständigkeit im Alter, A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=969394622234742) · [share](https://app.gethookd.ai/share/ad/200490718?signature=38b5623f18087b0df4c2c1716eb5005dc8644f32545bafb73badcec66bf77774) |
| 11 | 200490716 | 2233952628001235 | 2026-10-06 | 3 | Video | 44 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | SEE_DETAILS („See details“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2233952628001235) · [share](https://app.gethookd.ai/share/ad/200490716?signature=f9af223b680c0ee04bd5687c44ba0fd8ca69eace21b5373ed6b6f893022689ff) |
| 12 | 200490714 | 2178788646402978 | 2026-10-06 | 3 | Video | 30 s | Say Goodbye to Duvet Cover Hassle | C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2178788646402978) · [share](https://app.gethookd.ai/share/ad/200490714?signature=627ca4dcd8cf81ffbbe8928084c30d078545b5271aa95e2c5093eb36261092a5) |
| 13 | 200490712 | 1570785790996577 | 2026-10-06 | 3 | Video | 27 s | Check This Before You Buy | F-Einwand/Kaufhilfe, A | https://pleene.com/products/easyrest | ORDER_NOW („Order now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1570785790996577) · [share](https://app.gethookd.ai/share/ad/200490712?signature=5ca96434dc1391452bf61216cdc94bffb3d3b8ab283563c1354672fbd689d547) |
| 14 | 200490709 | 965754332621763 | 2026-10-06 | 3 | Bild | – | Keep Making Your Own Bed | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=965754332621763) · [share](https://app.gethookd.ai/share/ad/200490709?signature=2d7f89c9b03596be2e52285bbb9a8d93f265460fdb50363beccf2776ff75a276) |
| 15 | 200490708 | 1410624373895542 | 2026-10-06 | 3 | Video | 15 s | Pick a colour. Watch. | F-Knappheit/Farbe, C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1410624373895542) · [share](https://app.gethookd.ai/share/ad/200490708?signature=c478fee5f2f2b1906248ac292415fd4e4fb6b49899a564cd74f30be3cf28ac09) |
| 16 | 200490706 | 3697076843791050 | 2026-10-06 | 3 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=3697076843791050) · [share](https://app.gethookd.ai/share/ad/200490706?signature=bf8fb3d07c078c72fd1dd3c635f84c09d6efe02037bea42b6f0c348469448635) |
| 17 | 200490701 | 2558876794610991 | 2026-10-06 | 3 | Video | 16 s | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2558876794610991) · [share](https://app.gethookd.ai/share/ad/200490701?signature=af04268440606b4ede2605c8f08f88b62eaaee7acf8bbd6c6b33990e392b96e2) |
| 18 | 200490698 | 4427668754123793 | 2026-10-06 | 3 | Bild | – | NEW: Lavender Mist | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 13 (Testing) | 2 | – | [Meta](https://www.facebook.com/ads/library/?id=4427668754123793) · [share](https://app.gethookd.ai/share/ad/200490698?signature=545ba781a548a5c01d329f2fd0013f8c17445f4fe55be65e34bbea4cb49766dc) |
| 19 | 200490660 | 2352066545542430 | 2026-10-06 | 3 | Video | 23 s | Bedding Made for Independence | F-Selbstständigkeit im Alter, A | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2352066545542430) · [share](https://app.gethookd.ai/share/ad/200490660?signature=2bdf462077564f674b5c865f99ba0e9e930f29ccb8d973a094d72ef52a3ed322) |
| 20 | 200490658 | 4710162855976658 | 2026-10-06 | 3 | Video | 28 s | A Smarter Way To Do Bedding | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=4710162855976658) · [share](https://app.gethookd.ai/share/ad/200490658?signature=c8f37e5af06714882e4c6e6120919336cdce17ce51bcf0f206bbd74faf16c421) |
| 21 | 200490657 | 1088262300260108 | 2026-10-06 | 3 | Video | 30 s | Say Goodbye to Duvet Cover Hassle | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1088262300260108) · [share](https://app.gethookd.ai/share/ad/200490657?signature=14e9cab282a8e5334823ebd0fe803836a252fcd8cf045e8e22111a5867c33ff8) |
| 22 | 200490656 | 941633032037665 | 2026-10-06 | 3 | Video | 13 s | The Easiest Bed Upgrade | C | https://pleene.com/products/easyrest-comforter?trybe=532dbd48 | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=941633032037665) · [share](https://app.gethookd.ai/share/ad/200490656?signature=9b9fd72ba4d964a239aa279407b823b1686d57f783845a835d07793d5157d2b6) |
| 23 | 200490655 | 4392590044384955 | 2026-10-06 | 3 | Video | 51 s | The Bedding Upgrade Is Here | C, B | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=4392590044384955) · [share](https://app.gethookd.ai/share/ad/200490655?signature=7d24527061b5c2c8f21d9243b2a93c078b438788a757590a49fc3e5bc7294145) |
| 24 | 200490654 | 1704721577299375 | 2026-10-06 | 3 | Video | 25 s | Say Goodbye to Duvet Cover Hassle | C | https://pleene.com/products/easyrest-comforter?trybe=769e7716 | SEE_DETAILS („See details“) | 12 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1704721577299375) · [share](https://app.gethookd.ai/share/ad/200490654?signature=47a2ea43f6061e1680dc6c3acfbfbfe49dda22c6028484f0a15fd6b2c5413750) |
| 25 | 200036996 | 38866239393024310 | 2026-10-06 | 3 | Video | 23 s | Ditch The Duvet Cover | C, A | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=38866239393024310) · [share](https://app.gethookd.ai/share/ad/200036996?signature=945bd160e24141ec27cd570f40308c72484012330c424f8889416548c509a965) |
| 26 | 200037063 | 1667265245004008 | 2026-10-05 | 4 | Video | 82 s | The Dog Can Stay On The Bed | A, F-Haustier | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1667265245004008) · [share](https://app.gethookd.ai/share/ad/200037063?signature=59e1350bb940afa8ce2ef4db6bc9f0dc9c3d58b5363f4541de87c32b08c94beb) |
| 27 | 200037062 | 1426769122930670 | 2026-10-05 | 4 | Video | 46 s | When Did You Last Wash Your Duvet? | A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1426769122930670) · [share](https://app.gethookd.ai/share/ad/200037062?signature=cda1bc0bd9028c69d9fba9351c6e6030713ed82bd1d77fc8a1574dafccc5ec75) |
| 28 | 200037061 | 1056794434059905 | 2026-10-05 | 4 | Video | 46 s | When Did You Last Wash Your Duvet? | A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1056794434059905) · [share](https://app.gethookd.ai/share/ad/200037061?signature=0567af9a9eaa403fac9aabda031e164b44e4c540386667d1dc31c6c13838d758) |
| 29 | 200037059 | 1762566964862159 | 2026-10-05 | 4 | Video | 74 s | The Spare Bed, Fresh For Every Guest | A, F-Gäste | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1762566964862159) · [share](https://app.gethookd.ai/share/ad/200037059?signature=59009cf51aaea1c606c359bf3dde2a7411fd0a4e972af70643b9fad86da60902) |
| 30 | 200037058 | 2388197505255466 | 2026-10-05 | 4 | Video | 16 s | Too Thin For Winter? Look Closer. | B, A, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2388197505255466) · [share](https://app.gethookd.ai/share/ad/200037058?signature=8b9260efa8d3e451a50636127320d32fc1789291c109321c5b496c3192bfb0e4) |
| 31 | 200037053 | 1833362664327699 | 2026-10-05 | 4 | Video | 16 s | Too Thin For Winter? Look Closer. | B, A, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1833362664327699) · [share](https://app.gethookd.ai/share/ad/200037053?signature=a89d0ec9b5b673f5988345a774bf4a4f858e1b8996f1952670685df5ce8f602c) |
| 32 | 200037052 | 961172106430872 | 2026-10-05 | 4 | Video | 73 s | The Spare Bed, Fresh For Every Guest | A, F-Gäste | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=961172106430872) · [share](https://app.gethookd.ai/share/ad/200037052?signature=ab0ea3d22bfd746992e616204067846b3fc4ad0b9794701144978049c326996a) |
| 33 | 200037051 | 2176522276563795 | 2026-10-05 | 4 | Video | 16 s | Too Thin For Winter? Look Closer. | B, A, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2176522276563795) · [share](https://app.gethookd.ai/share/ad/200037051?signature=1f846d614d7ded11dca1363417ba6340f5e6bb0229af8a271a5f50fea944c262) |
| 34 | 200037049 | 4571329826520060 | 2026-10-05 | 4 | Video | 80 s | The Dog Can Stay On The Bed | A, F-Haustier | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=4571329826520060) · [share](https://app.gethookd.ai/share/ad/200037049?signature=5045ba37ea51c2cd64846ac6342c368334f1f1b19a0b44769b33ca1012550c40) |
| 35 | 200037047 | 1818573935991907 | 2026-10-05 | 4 | Video | 73 s | The Spare Bed, Fresh For Every Guest | A, F-Gäste | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1818573935991907) · [share](https://app.gethookd.ai/share/ad/200037047?signature=17fe05b65ba5af7f7b6a0e07d401ba8e36e2ca9af6ea7f68938dcf67525578db) |
| 36 | 200037045 | 1251620417158236 | 2026-10-05 | 4 | Video | 80 s | The Dog Can Stay On The Bed | A, F-Haustier | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1251620417158236) · [share](https://app.gethookd.ai/share/ad/200037045?signature=9dbc6af8a2932afed3e5a991ab6f9ad12e1fef2910914283018eeff2b95baea8) |
| 37 | 200037044 | 2217517888813082 | 2026-10-05 | 4 | Video | 47 s | When Did You Last Wash Your Duvet? | A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 22 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2217517888813082) · [share](https://app.gethookd.ai/share/ad/200037044?signature=a19c242b496cbc5e92ce74a3a3303e782e4f5f6f23b854194823c49f93fb0260) |
| 38 | 193234216 | 1078627058473158 | 2026-10-02 | 7 | Video | 16 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/pages/tb-6 | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1078627058473158) · [share](https://app.gethookd.ai/share/ad/193234216?signature=60e2dc530fac13782e5f82c44abb08606f4acb8db2a48f6580a4f67b8d2e303d) |
| 39 | 193234279 | 28476177958733795 | 2026-10-01 | 8 | Video | 93 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/tb-6 | SHOP_NOW („Shop now“) | 44 (Scaling) | 2 | ja | [Meta](https://www.facebook.com/ads/library/?id=28476177958733795) · [share](https://app.gethookd.ai/share/ad/193234279?signature=13f6122c0c5d22eb8c8b6141c88c013e8051538391bd99bbd1f57e3f4702f207) |
| 40 | 193234278 | 1103531258742413 | 2026-10-01 | 8 | Bild | – | NEW: Lavender Mist | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 40 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1103531258742413) · [share](https://app.gethookd.ai/share/ad/193234278?signature=2acfe25ae18b9ee3fd409e989a071bce595dea12e1dca232a03824238d38b557) |
| 41 | 193234275 | 931889339640196 | 2026-10-01 | 8 | Video | 93 s | Never Wrestle A Duvet Cover Again | C, A, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 52 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=931889339640196) · [share](https://app.gethookd.ai/share/ad/193234275?signature=ffce5170bcd8108ccef8ec8fa356ebe88ee4788757813cf94c27b340e5ff2e63) |
| 42 | 193234224 | 1614086653522933 | 2026-10-01 | 8 | Video | 49 s | The Duvet You Can Actually Wash | A | https://pleene.com/pages/tb-6 | ORDER_NOW („Order now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1614086653522933) · [share](https://app.gethookd.ai/share/ad/193234224?signature=e67f0112dff4be83367fd2663a38a3c667a76a33044371dae7cb5e0307b1035b) |
| 43 | 193234221 | 2325762131511604 | 2026-10-01 | 8 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/pages/tb-6 | ORDER_NOW („Order now“) | 52 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=2325762131511604) · [share](https://app.gethookd.ai/share/ad/193234221?signature=34d449a91191d816e5a91f7d690e2d93f52044d2af092704c3b3dece336abb59) |
| 44 | 193234219 | 4170969413201905 | 2026-10-01 | 8 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/pages/tb-6 | ORDER_NOW („Order now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=4170969413201905) · [share](https://app.gethookd.ai/share/ad/193234219?signature=0cb8964e6ba84cfd7298793d4bb26527250a2d845375dcbc5de0b9fc4c82562e) |
| 45 | 193234218 | 1114220797783359 | 2026-10-01 | 8 | Video | 29 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/pages/tb-6 | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1114220797783359) · [share](https://app.gethookd.ai/share/ad/193234218?signature=3870fec0fed270d728da178501d4d67c9e13c536497ef821674e8f3e9c30953b) |
| 46 | 193234215 | 1068343922634373 | 2026-10-01 | 8 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/tb-6 | SHOP_NOW („Shop now“) | 52 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=1068343922634373) · [share](https://app.gethookd.ai/share/ad/193234215?signature=92968440b95005fe0fc1bf85409c9b3366e3ae8f6dbf240ce5448a242e85affb) |
| 47 | 193234214 | 2366124124211597 | 2026-10-01 | 8 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/tb-6 | SHOP_NOW („Shop now“) | 52 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=2366124124211597) · [share](https://app.gethookd.ai/share/ad/193234214?signature=4c554cee5f2b53ee0a1c202d4fe10ee2f6cfb8b5f6e3a6b4936aab8a10f4eec3) |
| 48 | 190288319 | 1650102630028747 | 2026-09-30 | 9 | Bild | – | A Simpler Way To Change The Bed | C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1650102630028747) · [share](https://app.gethookd.ai/share/ad/190288319?signature=729f0bc268e9a52e0c55703bcfd9467503c62b1ee1d8fcb35f0a6610a2f3db7f) |
| 49 | 190288311 | 28870324805925641 | 2026-09-30 | 9 | Bild | – | Bedding Without The Struggle | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=28870324805925641) · [share](https://app.gethookd.ai/share/ad/190288311?signature=516e1093da353991ffedcb490ec607edb228c6ef1f12611c429fc7f6c0a744c5) |
| 50 | 189550275 | 1697353005429136 | 2026-09-30 | 9 | Bild | – | Pleene | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest | SHOP_NOW (Text n/a) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1697353005429136) · [share](https://app.gethookd.ai/share/ad/189550275?signature=e2841af4c3309f1f54a47962f542b0d928f5b10afef23bdb312b9555f7e1f404) |
| 51 | 189550269 | 2239984750193672 | 2026-09-30 | 9 | Bild | – | Pleene | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest | SHOP_NOW (Text n/a) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2239984750193672) · [share](https://app.gethookd.ai/share/ad/189550269?signature=f3ebac77a9aabd296cb1e960812c63aa60881f30e0da69bded7fc73cec4371e1) |
| 52 | 189550267 | 1845735359934868 | 2026-09-30 | 9 | Bild | – | Pleene | C | https://pleene.com/products/easyrest | SHOP_NOW (Text n/a) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1845735359934868) · [share](https://app.gethookd.ai/share/ad/189550267?signature=0ae93d7c42293d935614c14ae39cce8ebc82b4d76b07db17850a7cfb68f38e5f) |
| 53 | 186893878 | 28612939431667546 | 2026-09-29 | 10 | Bild | – | Bedding Made For Your Routine | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=28612939431667546) · [share](https://app.gethookd.ai/share/ad/186893878?signature=f232a426903d049b7b06b46c06d250fb7eea59242595dbbbfb87042d99c66827) |
| 54 | 186893875 | 2350297945720190 | 2026-09-29 | 10 | Bild | – | Your Bed. Your Way. | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2350297945720190) · [share](https://app.gethookd.ai/share/ad/186893875?signature=eb76cbb5770c4d86cb5e4bb7bf79451829587405bd54863dd53422787d2c7971) |
| 55 | 186893873 | 1400490411791512 | 2026-09-29 | 10 | Bild | – | Meet The One-Piece Comforter | F-Social-Proof, F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1400490411791512) · [share](https://app.gethookd.ai/share/ad/186893873?signature=6e5233b7a44d6f4c0b6241fe5a5dfd8bc67078473f1ca4dfa8733b675916b722) |
| 56 | 186893869 | 1096087780074941 | 2026-09-29 | 10 | Bild | – | Fresh Bed, Fewer Steps | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1096087780074941) · [share](https://app.gethookd.ai/share/ad/186893869?signature=b35e84823f3c3e06bdd64e526557f5aa8adc0cf618dd1681d566efefe923a169) |
| 57 | 186893867 | 1744189879967996 | 2026-09-29 | 10 | Bild | – | A Duvet That Works For You | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1744189879967996) · [share](https://app.gethookd.ai/share/ad/186893867?signature=427fec70c06030c12582ea7afc5367a9381e9977011adcea03ef8367788f4ba2) |
| 58 | 186893864 | 1196771192793545 | 2026-09-29 | 10 | DCO | 3 Bild(er) | n/a | n/a (kein Text) | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1196771192793545) · [share](https://app.gethookd.ai/share/ad/186893864?signature=c4d30ed8926495e9042192d8622fb23ae265cf0b993d757bbe63f57af5595106) |
| 59 | 186893862 | 1122560766807410 | 2026-09-29 | 10 | Bild | – | Bedding Without The Struggle | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1122560766807410) · [share](https://app.gethookd.ai/share/ad/186893862?signature=a82b35565236b229024dfb64fb1fb681e1e300d1decba6dac35e25bd8dafacf4) |
| 60 | 186893861 | 1108416845124866 | 2026-09-29 | 10 | Bild | – | One Piece. Less To Handle. | C, B | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1108416845124866) · [share](https://app.gethookd.ai/share/ad/186893861?signature=1c5e7c9a1a97f705b6efeb5f2fe85bde75fd83702387d3c01f9eae4b94e2b14d) |
| 61 | 186893859 | 1740917367195794 | 2026-09-29 | 10 | Bild | – | Bedding That Fits Your Schedule | A, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1740917367195794) · [share](https://app.gethookd.ai/share/ad/186893859?signature=b98601908ab59abfba07fc1c1081e6a491558c128c090114c0218409fb4dceea) |
| 62 | 186893846 | 1092854683130854 | 2026-09-29 | 10 | Bild | – | Skip The Cover. Keep The Comfort. | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1092854683130854) · [share](https://app.gethookd.ai/share/ad/186893846?signature=caad060c8e8ab36651b2536e28a6cef64fce2c0c70b442162689b11ac79d0ef1) |
| 63 | 186893844 | 2052923595354457 | 2026-09-29 | 10 | Bild | – | Bedding Without The Struggle | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 2 | – | [Meta](https://www.facebook.com/ads/library/?id=2052923595354457) · [share](https://app.gethookd.ai/share/ad/186893844?signature=f56cef38bdf4271c06d03206fdc5607e7f702ce5a602485401736777e23c53de) |
| 64 | 186893837 | 28819204317704017 | 2026-09-29 | 10 | Bild | – | Keep Making Your Own Bed | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=28819204317704017) · [share](https://app.gethookd.ai/share/ad/186893837?signature=296de22f294544b5a6e1de4329a707b9ab8c8d754343b48b762174f85a621bcb) |
| 65 | 186893831 | 4537475009834373 | 2026-09-29 | 10 | Bild | – | Skip The Cover. Keep The Comfort. | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=4537475009834373) · [share](https://app.gethookd.ai/share/ad/186893831?signature=7a72439f549f6691a92e5c861625f174cc926bc15ca0e02bd6d03876a27cc6b9) |
| 66 | 186893814 | 1759745871934283 | 2026-09-29 | 10 | Bild | – | Your Routine, Made Simpler | C, F-Selbstständigkeit im Alter | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1759745871934283) · [share](https://app.gethookd.ai/share/ad/186893814?signature=8bd9162f3bfd33faf85979f4605208fc571e1affbdb578c78e5e8cac4f9df0ee) |
| 67 | 185395501 | 4386478151596961 | 2026-09-28 | 11 | Video | 9 s | Pleene | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW (Text n/a) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=4386478151596961) · [share](https://app.gethookd.ai/share/ad/185395501?signature=015f1978dac5f9d276bb167b0564e2fe687605d8c9ad005f1b15479977650936) |
| 68 | 185228774 | 850494884758362 | 2026-09-27 | 12 | Bild | – | Properly Warm, Never Heavy | B, A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=850494884758362) · [share](https://app.gethookd.ai/share/ad/185228774?signature=6459312b29b8e015b00623a9c8704115adbc89d90290a12a406708f7e07ceba3) |
| 69 | 185228773 | 2789047968155632 | 2026-09-27 | 12 | Video | 15 s | Pick a colour. Watch. | F-Knappheit/Farbe, C | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2789047968155632) · [share](https://app.gethookd.ai/share/ad/185228773?signature=a25a1c0dc9c693ccb2b54cced73f43f031683b0b29560a7a1a6bae916c224838) |
| 70 | 185228772 | 1609404564015528 | 2026-09-27 | 12 | Video | 29 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 2 | – | [Meta](https://www.facebook.com/ads/library/?id=1609404564015528) · [share](https://app.gethookd.ai/share/ad/185228772?signature=b8b59977a1223802de6aa2310ed361654df4253dc41d5ac727fe2d89dc343ef4) |
| 71 | 185228767 | 947904747867427 | 2026-09-27 | 12 | Video | 16 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 60 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=947904747867427) · [share](https://app.gethookd.ai/share/ad/185228767?signature=d4a01baf409b9ddc41f60bfabb36d11b1b0037cf0db9af90a7ff2251278f24be) |
| 72 | 185228766 | 1401480008764681 | 2026-09-27 | 12 | Bild | – | NEW: Lavender Mist | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 60 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=1401480008764681) · [share](https://app.gethookd.ai/share/ad/185228766?signature=f4be2b097e5b58bb0f5013dc8e461a8cea74051b0e8dfd5a28059f540eaf99fb) |
| 73 | 185228765 | 1107581421667412 | 2026-09-27 | 12 | Bild | – | Now In Super King | F-Neuheit/Größe, A | https://pleene.com/products/easyrest | ORDER_NOW („Order now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1107581421667412) · [share](https://app.gethookd.ai/share/ad/185228765?signature=fdc1176605c0f19ad51f2626b448a5fdfb307d0143360d07311941417feb5d0b) |
| 74 | 185228764 | 3754498381550275 | 2026-09-27 | 12 | Video | 27 s | Check This Before You Buy | F-Einwand/Kaufhilfe, A | https://pleene.com/products/easyrest | ORDER_NOW („Order now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=3754498381550275) · [share](https://app.gethookd.ai/share/ad/185228764?signature=c703896014750ef26ae392d8460d22d78a412a986b4bb954473b7a82371145bf) |
| 75 | 185228755 | 1858016975363264 | 2026-09-27 | 12 | Video | 16 s | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 60 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=1858016975363264) · [share](https://app.gethookd.ai/share/ad/185228755?signature=25ebc63a662bfe1309283139b99531554229712ec743d75253367e8f2956578d) |
| 76 | 184134616 | 4380603895511872 | 2026-09-25 | 14 | Video | 48 s | Never Wrestle A Duvet Cover Again | C, A, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=4380603895511872) · [share](https://app.gethookd.ai/share/ad/184134616?signature=30d5fa9687840e415704fb7e19f5a1ef4dd204c7e06fbb62833ac631d02fe94a) |
| 77 | 184134607 | 2292800994824018 | 2026-09-25 | 14 | Video | 48 s | Never Wrestle A Duvet Cover Again | C, A, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2292800994824018) · [share](https://app.gethookd.ai/share/ad/184134607?signature=19e12d9ef3e8461ef2c7fa995df7cd451f2608fc590135b4f248dc4336d2e56d) |
| 78 | 184134598 | 1772685790545501 | 2026-09-25 | 14 | Bild | – | Mint Green Is Almost Gone | F-Angebot, F-Knappheit/Farbe | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 41 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=1772685790545501) · [share](https://app.gethookd.ai/share/ad/184134598?signature=74028bdc9398943d1fa7b8f9149049962318fe3ebdf4bcecd5c613ee3875d422) |
| 79 | 184134597 | 4249373995353335 | 2026-09-25 | 14 | Video | 47 s | Never Wrestle A Duvet Cover Again | C, A, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 41 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=4249373995353335) · [share](https://app.gethookd.ai/share/ad/184134597?signature=2b680d992f53e9489bd001330a9e608908df3f009b371ab2cf0e14275970f411) |
| 80 | 183445651 | 1640984024127964 | 2026-09-24 | 15 | Bild | – | Skip the Cover | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 2 | – | [Meta](https://www.facebook.com/ads/library/?id=1640984024127964) · [share](https://app.gethookd.ai/share/ad/183445651?signature=3af2be1a313fcc4887a0cd71ed59cf6121bb5f75f33757760103514ce37b379e) |
| 81 | 182988114 | 1426446732803436 | 2026-09-24 | 15 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | SHOP_NOW („Shop now“) | 41 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=1426446732803436) · [share](https://app.gethookd.ai/share/ad/182988114?signature=45373dfa7ccdf466516a711b6593e9207307858450c4d58f1857ebd0d9c95216) |
| 82 | 182988043 | 29208178135432493 | 2026-09-24 | 15 | Bild | – | Wash The Whole Comforter | A | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 54 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=29208178135432493) · [share](https://app.gethookd.ai/share/ad/182988043?signature=474ac523034272536a305779503c22ea294092cc8bd3cc7b069288c8fe337071) |
| 83 | 182988042 | 28437506889250706 | 2026-09-24 | 15 | Bild | – | No Assembly Required | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=28437506889250706) · [share](https://app.gethookd.ai/share/ad/182988042?signature=e713dbcee072e6217acb230e04b0dfb8c7114c149d8c98626c040da7bef3f891) |
| 84 | 182988040 | 2515261675637941 | 2026-09-24 | 15 | Bild | – | Clean Bedding, Made Easier | A | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2515261675637941) · [share](https://app.gethookd.ai/share/ad/182988040?signature=70c523c1f926d7fd461c615515849a5b4da5e7a7cd0b682c0335da480ffd657a) |
| 85 | 182988039 | 2506169333225327 | 2026-09-24 | 15 | Bild | – | Fewer Steps. Fresher Bed. | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2506169333225327) · [share](https://app.gethookd.ai/share/ad/182988039?signature=527dd4c916d39ab9e6336ae3da5dfb03d8f6e255525d6dcab66494f2f427a37d) |
| 86 | 182988037 | 1640153464440559 | 2026-09-24 | 15 | Bild | – | Skip the Cover | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1640153464440559) · [share](https://app.gethookd.ai/share/ad/182988037?signature=b7d4bc753ea2e96af174d564c3492d5adf7a481ed1267e58644c73a559c03796) |
| 87 | 182988035 | 2320911822014129 | 2026-09-24 | 15 | Bild | – | Fresh Bedding Made Easy | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 41 (Scaling) | 1 | ja | [Meta](https://www.facebook.com/ads/library/?id=2320911822014129) · [share](https://app.gethookd.ai/share/ad/182988035?signature=7092f978c95adda0f69e7d8ee25f7a28d421bd5b83e9ec632c18a18ed9941b58) |
| 88 | 182988034 | 1509916224516076 | 2026-09-24 | 15 | Bild | – | Simplify Your Bedding Routine | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1509916224516076) · [share](https://app.gethookd.ai/share/ad/182988034?signature=14dbc2129486bcabd193e665ddf4838458be05e7bf9dce3dfc69bf4aacede6cc) |
| 89 | 182988033 | 1974838589853602 | 2026-09-24 | 15 | Bild | – | Skip The Duvet Cover | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1974838589853602) · [share](https://app.gethookd.ai/share/ad/182988033?signature=02e7cdc360791bd35b8ddcd944fe2a094efad14b6918e50c6eab16a385c9fc59) |
| 90 | 182988032 | 1109103628745298 | 2026-09-24 | 15 | Bild | – | Wash. Dry. Done. | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1109103628745298) · [share](https://app.gethookd.ai/share/ad/182988032?signature=fbd107f7a97ed551302eb2de90f0c8a58bf341d7335b7f01b6a069b61410c80b) |
| 91 | 182988031 | 2312946976208616 | 2026-09-24 | 15 | Bild | – | Straight Back On The Bed | C | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=2312946976208616) · [share](https://app.gethookd.ai/share/ad/182988031?signature=929ab2700d8d2ff4c55371cf11ebef82c019bb414b81a2990302dfd8d9efd784) |
| 92 | 182988029 | 956768364140489 | 2026-09-24 | 15 | Bild | – | Take The Work Out Of Bedding | C, E | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=956768364140489) · [share](https://app.gethookd.ai/share/ad/182988029?signature=7000d6337b257185b3d04740a740841f3c2734266cacfabe1aaee79e136c9e57) |
| 93 | 182988027 | 1789453228862663 | 2026-09-24 | 15 | Bild | – | Warmth Without The Weight | B | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1789453228862663) · [share](https://app.gethookd.ai/share/ad/182988027?signature=9321cc0e170e1a68f3b963e4904fb45eec5f2859a60a5d4abc63285b6a3fcde3) |
| 94 | 182988024 | 1104976622267074 | 2026-09-24 | 15 | Bild | – | Wash More Than The Sheets | A | https://pleene.com/products/easyrest-comforter | SHOP_NOW („Shop now“) | 1 (Testing) | 1 | – | [Meta](https://www.facebook.com/ads/library/?id=1104976622267074) · [share](https://app.gethookd.ai/share/ad/182988024?signature=eabd40dff7802187b5f63741ae4ea3e7cc7a4cd1ac89cf64689be1a3177bdf9f) |

Neue Tests nach Headline-Familie: „No More Fighting With Duvet Covers“ ×6; „Be honest. When did you last wash it?“ ×4; „Never Wrestle A Duvet Cover Again“ ×4; „Pleene“ ×4; „Say Goodbye to Duvet Cover Hassle“ ×3; „Mint Green is almost gone.“ ×3; „NEW: Lavender Mist“ ×3; „The Dog Can Stay On The Bed“ ×3; „When Did You Last Wash Your Duvet?“ ×3; „The Spare Bed, Fresh For Every Guest“ ×3; „Too Thin For Winter? Look Closer.“ ×3; „Bedding Without The Struggle“ ×3; „Skip The  Duvet Cover“ ×2; „Fresh Bedding Made Easy“ ×2; „Wash The Whole Comforter“ ×2; „Your Routine, Made Simpler“ ×2; „A Smarter Way To Do Bedding“ ×2; „The Bedding Upgrade Is Here“ ×2; „Your Bed. Your Way.“ ×2; „Ditch The Duvet Cover“ ×2; „Bedding Made for Independence“ ×2; „Check This Before You Buy“ ×2; „Keep Making Your Own Bed“ ×2; „Pick a colour. Watch.“ ×2; „Everyone said it. They were right.“ ×2; „Skip The Cover. Keep The Comfort.“ ×2; „Skip the Cover“ ×2; „The Comforter That Does It All“ ×1; „The Easiest Bed Upgrade“ ×1; „The Duvet You Can Actually Wash“ ×1; „A Simpler Way To Change The Bed“ ×1; „Bedding Made For Your Routine“ ×1; „Meet The One-Piece Comforter“ ×1; „Fresh Bed, Fewer Steps“ ×1; „A Duvet That Works For You“ ×1; „(ohne Headline)“ ×1; „One Piece. Less To Handle.“ ×1; „Bedding That Fits Your Schedule“ ×1; „Properly Warm, Never Heavy“ ×1; „Now In Super King“ ×1; „No Assembly Required“ ×1; „Clean Bedding, Made Easier“ ×1; „Fewer Steps. Fresher Bed.“ ×1; „Simplify Your Bedding Routine“ ×1; „Wash. Dry. Done.“ ×1; „Straight Back On The Bed“ ×1; „Take The Work Out Of Bedding“ ×1; „Warmth Without The Weight“ ×1; „Wash More Than The Sheets“ ×1.

### Verlierer / Aufgegeben

**Verlierer = inaktiv mit Laufzeit < 7 Tage: 202 Ads.** Zusammenfassung nach Headline-Familie (Verlierer / alle Ads der Familie im Datenfenster):

| Headline-Familie | Verlierer | Ads in Familie gesamt | davon heute aktiv | Verlierer-Quote |
|---|---|---|---|---|
| „Be honest. When did you last wash it?“ | 27 | 51 | 6 | 53 % |
| „No More Fighting With Duvet Covers“ | 25 | 175 | 20 | 14 % |
| „Never lift your mattress again.“ | 14 | 66 | 0 | 21 % |
| „The Duvet You Can Actually Wash“ | 10 | 20 | 1 | 50 % |
| „A Duvet With No Cover?“ | 7 | 15 | 0 | 47 % |
| „Best decision I ever made.“ | 7 | 12 | 0 | 58 % |
| „End Of Season Sale“ | 7 | 12 | 0 | 58 % |
| „Mint Green is almost gone.“ | 6 | 16 | 5 | 38 % |
| „Duvet & Cover In One“ | 6 | 11 | 0 | 55 % |
| „2 Free Pillow Cases 🎁“ | 6 | 12 | 0 | 50 % |
| „Everyone said it. They were right.“ | 6 | 20 | 5 | 30 % |
| „The Cover Is Sewn In“ | 6 | 12 | 0 | 50 % |
| „The Duvet That Goes In The Wash“ | 6 | 12 | 0 | 50 % |
| „Done fighting with bed linen.“ | 6 | 6 | 0 | 100 % |
| „When Did You Last Wash The Duvet?“ | 4 | 5 | 0 | 80 % |
| „Pleene“ | 4 | 11 | 4 | 36 % |
| „Ready for the colder nights.“ | 4 | 4 | 0 | 100 % |
| „I've Quit Bed Linen“ | 4 | 4 | 0 | 100 % |
| „Not your normal fitted sheet“ | 4 | 4 | 0 | 100 % |
| „Pick a colour. Watch.“ | 3 | 15 | 3 | 20 % |
| „A Winter Duvet You Can Actually Lift“ | 3 | 3 | 0 | 100 % |
| „No Launderette Needed. Ever.“ | 3 | 4 | 1 | 75 % |
| „"You'll Never Wash That." Watch Us.“ | 3 | 3 | 0 | 100 % |
| „When Did You Last Wash Your Duvet?“ | 3 | 9 | 3 | 33 % |
| „Everyone's buying the blue one.“ | 3 | 6 | 2 | 50 % |
| „Hearth Red. Nearly gone.“ | 3 | 5 | 1 | 60 % |
| „(ohne Headline)“ | 3 | 12 | 1 | 25 % |
| „Only 26 Left In Hearth Red“ | 3 | 3 | 0 | 100 % |
| „Winter-Ready In One Wash“ | 2 | 3 | 0 | 67 % |
| „The Duvet With No Cover To Change“ | 2 | 4 | 0 | 50 % |
| „Who Wins In Your House?“ | 2 | 5 | 0 | 40 % |
| „NEW: Lavender Mist“ | 1 | 7 | 3 | 14 % |
| „Fewer Steps To A Fresh Bed“ | 1 | 1 | 0 | 100 % |
| „Less To Handle. More Independence.“ | 1 | 1 | 0 | 100 % |
| „Yes, It Fits Your Machine“ | 1 | 5 | 0 | 20 % |
| „Change Your Bed Without The Pain After“ | 1 | 4 | 0 | 25 % |
| „Pleene EasyRest™ Duvet“ | 1 | 1 | 0 | 100 % |
| „Now In Super King“ | 1 | 5 | 1 | 20 % |
| „Fresh Bedding Made Easy“ | 1 | 3 | 2 | 33 % |
| „Myth vs Truth 🛏️“ | 1 | 6 | 1 | 17 % |
| „Pleene EasyRest™ Quilt“ | 1 | 1 | 0 | 100 % |

Alle Verlierer einzeln (Details inkl. Primärtext, CTA, Plattformen im Vollinventar inaktiv):

| # | GetHooked-ID | Meta-ID | Start | Ende | Tage | Format | Länge | Headline | Angle | Landingpage | Produkt | Links |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 193234277 | 943243035064922 | 2026-10-01 | 2026-10-04 | 4 | Bild | – | When Did You Last Wash The Duvet? | A, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=943243035064922) · [share](https://app.gethookd.ai/share/ad/193234277?signature=77ae63f144efe3984006b368cc0904cd9c41e7a7c6e5d22091a64ab95d8f32af) |
| 2 | 193234273 | 2100922640555492 | 2026-10-01 | 2026-10-06 | 6 | Bild | – | NEW: Lavender Mist | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2100922640555492) · [share](https://app.gethookd.ai/share/ad/193234273?signature=0ba2f670cf75a2cea80f69a0f1d518096f384fc05de8fe37422c55254a2856d1) |
| 3 | 190288325 | 1348489960694867 | 2026-09-30 | 2026-10-05 | 6 | Bild | – | Fewer Steps To A Fresh Bed | C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1348489960694867) · [share](https://app.gethookd.ai/share/ad/190288325?signature=5fb631c87cf69dc85e89d8b703b981cd94e212c894b87ecb72970ca5523d2b38) |
| 4 | 190288318 | 1067252816111108 | 2026-09-30 | 2026-10-04 | 5 | Bild | – | Less To Handle. More Independence. | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1067252816111108) · [share](https://app.gethookd.ai/share/ad/190288318?signature=4b7f8a3d253d34ff53a70de87acb2846ec4495551f4ab28bebaa04b1289d150a) |
| 5 | 190288250 | 977688892023326 | 2026-09-30 | 2026-10-04 | 5 | Bild | – | Yes, It Fits Your Machine | A, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=977688892023326) · [share](https://app.gethookd.ai/share/ad/190288250?signature=ab039581e4288805e3058d4430104d7505f2a62784a0d55a714226526b00cbd8) |
| 6 | 189550279 | 947126441804190 | 2026-09-30 | 2026-10-04 | 5 | Bild | – | Pleene | F-Selbstständigkeit im Alter, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=947126441804190) · [share](https://app.gethookd.ai/share/ad/189550279?signature=e531d4180cb84f6914c0848fce5d8471ae2f19ca3576ce52a18cbae0568a4aea) |
| 7 | 186894303 | 1890941582288574 | 2026-09-30 | 2026-10-01 | 2 | Video | 29 s | Change Your Bed Without The Pain After | E, C, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1890941582288574) · [share](https://app.gethookd.ai/share/ad/186894303?signature=f24378a86b717ac22da1b3e91dd742d6e26bf6dd5cd89506ff6bd5a6e1a9d07d) |
| 8 | 186894314 | 1824185538588533 | 2026-09-29 | 2026-10-04 | 6 | DPA (Katalog-Karussell) | 6 Bild(er) | Pleene EasyRest™ Duvet | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1824185538588533) · [share](https://app.gethookd.ai/share/ad/186894314?signature=7bdbabfdbbbe2383748e19b6dad0d11cdfcc162c80d898188e955339901be34c) |
| 9 | 186000741 | 2094126661191928 | 2026-09-29 | 2026-10-01 | 3 | DPA (Katalog-Karussell) | 1 Video(s): 41 s; 7 Bild(er) | Pleene | E, C, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2094126661191928) · [share](https://app.gethookd.ai/share/ad/186000741?signature=6738884412d512024ad69d3116f5823f1082695bf006ebf4cc69595eb5ec6b8d) |
| 10 | 186000736 | 4319008731578321 | 2026-09-28 | 2026-09-29 | 2 | Bild | – | When Did You Last Wash The Duvet? | A, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4319008731578321) · [share](https://app.gethookd.ai/share/ad/186000736?signature=1452f241e18da47fde78b934850d8cd904275ba1e5c5ece021cc18729e9d1c9c) |
| 11 | 185228757 | 1702834305187116 | 2026-09-27 | 2026-09-30 | 4 | Video | 15 s | Pick a colour. Watch. | F-Knappheit/Farbe, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1702834305187116) · [share](https://app.gethookd.ai/share/ad/185228757?signature=1dfd2f4531667bf568420272cb6c94e3a909cb4fcffb421662b836ba4399b731) |
| 12 | 185228754 | 1410164930583069 | 2026-09-27 | 2026-09-30 | 4 | Video | 16 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1410164930583069) · [share](https://app.gethookd.ai/share/ad/185228754?signature=5987f7828c48ebe4b1dba09dde3f65d4de768d7044d5eba18781273d14192008) |
| 13 | 185228753 | 1407444221500652 | 2026-09-27 | 2026-09-30 | 4 | Video | 16 s | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1407444221500652) · [share](https://app.gethookd.ai/share/ad/185228753?signature=d53dccb8597c8bb1de574f968d58d3edab599dc5cdc83f40af3bc2c1640722f0) |
| 14 | 185228748 | 1433462792232813 | 2026-09-27 | 2026-09-30 | 4 | Bild | – | Now In Super King | F-Neuheit/Größe, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1433462792232813) · [share](https://app.gethookd.ai/share/ad/185228748?signature=5ae20f134bb97857c1a962310cd9f5342d933e3ff0f7883488da80ca47b665ea) |
| 15 | 184134615 | 975825245551246 | 2026-09-25 | 2026-09-28 | 4 | Video | 32 s | Winter-Ready In One Wash | A, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=975825245551246) · [share](https://app.gethookd.ai/share/ad/184134615?signature=774ef2ce0f1f441165f2fc0b8a1cf8db0cf68ac2251544099acb001a51c92b56) |
| 16 | 184134614 | 2476447719512704 | 2026-09-25 | 2026-09-28 | 4 | Bild | – | Mint Green Is Almost Gone | F-Angebot, F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2476447719512704) · [share](https://app.gethookd.ai/share/ad/184134614?signature=3cf132e830abc320de3ba32af3792dcc31ccb92aba762db10afb6e5270455dca) |
| 17 | 184134613 | 1634367715003367 | 2026-09-25 | 2026-09-30 | 6 | Video | 45 s | A Winter Duvet You Can Actually Lift | E, C, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1634367715003367) · [share](https://app.gethookd.ai/share/ad/184134613?signature=39df81a972221b2ebeef9200328c1d2c127109519697b53bd7096a482ce50025) |
| 18 | 184134611 | 1608059824115796 | 2026-09-25 | 2026-09-30 | 6 | Video | 45 s | A Winter Duvet You Can Actually Lift | E, C, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1608059824115796) · [share](https://app.gethookd.ai/share/ad/184134611?signature=b4867beeb53616de91f8f5f592335b29311e07fd2e62a99a20e1aa581c601e23) |
| 19 | 184134605 | 2529410374194727 | 2026-09-25 | 2026-09-30 | 6 | Bild | – | When Did You Last Wash The Duvet? | A, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2529410374194727) · [share](https://app.gethookd.ai/share/ad/184134605?signature=12406f14ac37ae38da8bd1321f87e6637d86669b5c9aa934278fe1f6e05b2983) |
| 20 | 184134602 | 1153825353859983 | 2026-09-25 | 2026-09-30 | 6 | Video | 45 s | A Winter Duvet You Can Actually Lift | E, C, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1153825353859983) · [share](https://app.gethookd.ai/share/ad/184134602?signature=d2740a7f2a1172b621d9dfe802a913d4a649abb13541a1a7a0b6034cfa223dfc) |
| 21 | 184134596 | 1844350933397173 | 2026-09-25 | 2026-09-29 | 5 | Bild | – | When Did You Last Wash The Duvet? | A, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1844350933397173) · [share](https://app.gethookd.ai/share/ad/184134596?signature=a4195f16ec3a5a353e03ee2a4c3f1b6bce8ce4c15e281538b19b5e45849f727b) |
| 22 | 184134595 | 28232197259777711 | 2026-09-25 | 2026-09-28 | 4 | Bild | – | Mint Green Is Almost Gone | F-Angebot, F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28232197259777711) · [share](https://app.gethookd.ai/share/ad/184134595?signature=92121d7b03b2744d38fcd3c1ff304d545ba85ca9d2d1d3ca7e1be636cd4c7914) |
| 23 | 184134591 | 1770358953887705 | 2026-09-25 | 2026-09-28 | 4 | Video | 33 s | Winter-Ready In One Wash | A, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1770358953887705) · [share](https://app.gethookd.ai/share/ad/184134591?signature=41d5a47e03e241f311fadc2e5d097841a6aa5db17f9e6004ad112392d6bb080c) |
| 24 | 182988113 | 2467224973688738 | 2026-09-24 | 2026-09-28 | 5 | Video | 49 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2467224973688738) · [share](https://app.gethookd.ai/share/ad/182988113?signature=90ab157bcb1732d5b60d0b117ac08f6d95d7c324c7ae50841f8e39776bbb8993) |
| 25 | 182988036 | 1406063364236210 | 2026-09-24 | 2026-09-27 | 4 | Bild | – | Fresh Bedding Made Easy | C | https://pleene.com/products/easyrest-comforter | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1406063364236210) · [share](https://app.gethookd.ai/share/ad/182988036?signature=2f1743c2b27c60670ab677c5a3f4907398217e0d9c20f7c63ac7b72315e3e61a) |
| 26 | 182988116 | 1867690807533357 | 2026-09-23 | 2026-09-26 | 4 | DPA (Katalog-Karussell) | 1 Video(s): 26 s; 7 Bild(er) | Pleene | C | https://pleene.com/products/easyrest-everyday-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1867690807533357) · [share](https://app.gethookd.ai/share/ad/182988116?signature=38a4687f57e9750bde85aca915009010d1778e7fc9d63cb1eeb9e0bbc4750ca6) |
| 27 | 182988106 | 1737210887558001 | 2026-09-23 | 2026-09-28 | 6 | Video | 49 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1737210887558001) · [share](https://app.gethookd.ai/share/ad/182988106?signature=0d75a6fb63b6ad6e31a3d662ee78759e6f1cabcaa4955b8fa579302f16fb2f12) |
| 28 | 182988102 | 2033750387344906 | 2026-09-23 | 2026-09-28 | 6 | Video | 26 s | Duvet & Cover In One | C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2033750387344906) · [share](https://app.gethookd.ai/share/ad/182988102?signature=d7b28853d86506804b089084340f29f08f1d1d635e12481ba44d484d6fb80a2a) |
| 29 | 182988101 | 1427987919549105 | 2026-09-23 | 2026-09-28 | 6 | Video | 26 s | Duvet & Cover In One | C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1427987919549105) · [share](https://app.gethookd.ai/share/ad/182988101?signature=36749826f681f3817a1fe74b7ed0f7cc03ebc504c51bee13b89d5a9fe17ec22d) |
| 30 | 182988098 | 1559161055536548 | 2026-09-23 | 2026-09-28 | 6 | Video | 26 s | Duvet & Cover In One | C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1559161055536548) · [share](https://app.gethookd.ai/share/ad/182988098?signature=a21e32f4ad60b396b82ad788c498d9859003d18503d1cc5efd6f35801f0e6e0d) |
| 31 | 182988096 | 1102669162216252 | 2026-09-23 | 2026-09-28 | 6 | Video | 49 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1102669162216252) · [share](https://app.gethookd.ai/share/ad/182988096?signature=1a11212bc1d4f8d66b1431a4a4c84f65c4fa8a5353f603685de5b89ca9b9a748) |
| 32 | 179476351 | 2322836645140315 | 2026-09-17 | 2026-09-19 | 3 | Bild | – | No Launderette Needed. Ever. | A, B, F-Angebot | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2322836645140315) · [share](https://app.gethookd.ai/share/ad/179476351?signature=53587ea7f0871be857c471ca560da21e0722799d9c3c617ed054a176562302b0) |
| 33 | 178749264 | 832047280000629 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | "You'll Never Wash That." Watch Us. | A, F-Angebot | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=832047280000629) · [share](https://app.gethookd.ai/share/ad/178749264?signature=d8e08fd7024ff622ab3eacbab2d56418953b6cce8719c355c54bb885d2941843) |
| 34 | 178749263 | 1559934122048335 | 2026-09-16 | 2026-09-19 | 4 | Video | 60 s | The Duvet With No Cover To Change | F-Social-Proof, C, A | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1559934122048335) · [share](https://app.gethookd.ai/share/ad/178749263?signature=28c598109f6505dfc77225878d4dfaac7f1f9c557ec2ca81d2b65a272e654513) |
| 35 | 178749262 | 1433020452362661 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | "You'll Never Wash That." Watch Us. | A, F-Angebot | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1433020452362661) · [share](https://app.gethookd.ai/share/ad/178749262?signature=6ceea2df765c2665f061bdb2643d632d74e795a39fedbd69227e229ab47471de) |
| 36 | 178749253 | 1605124007665486 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | "You'll Never Wash That." Watch Us. | A, F-Angebot | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1605124007665486) · [share](https://app.gethookd.ai/share/ad/178749253?signature=bb402c29283429757519bab449ec29d3ee59c6746076b55220cae39f880c0375) |
| 37 | 178749250 | 1600246531600764 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | No Launderette Needed. Ever. | A, B, F-Angebot | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1600246531600764) · [share](https://app.gethookd.ai/share/ad/178749250?signature=fc6d5d6a0b6751501b08c46781636fc56679a17751a11b9a753d14e1d0cb4edc) |
| 38 | 178749244 | 1554811692528015 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | No Launderette Needed. Ever. | A, B, F-Angebot | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1554811692528015) · [share](https://app.gethookd.ai/share/ad/178749244?signature=e82eedb3d5627dfcb853ac65f9f4001d15d3830da366355715ee051dfd039d1d) |
| 39 | 178749241 | 986052237841995 | 2026-09-16 | 2026-09-19 | 4 | Video | 60 s | The Duvet With No Cover To Change | F-Social-Proof, C, A | https://pleene.com/products/easyrest-duvet | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=986052237841995) · [share](https://app.gethookd.ai/share/ad/178749241?signature=6aeed07ee78eed5e22d99bb8187bd9d3d5d945249cf272ee3c10935ee517f838) |
| 40 | 177443601 | 1081218440981332 | 2026-09-15 | 2026-09-16 | 2 | Video | 98 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1081218440981332) · [share](https://app.gethookd.ai/share/ad/177443601?signature=0e69fdceabad477dafabf63d8a3c28b2d86db1d8e7fcdd8418ceefca00ef2163) |
| 41 | 177443530 | 2946532112392018 | 2026-09-15 | 2026-09-17 | 3 | Video | 35 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2946532112392018) · [share](https://app.gethookd.ai/share/ad/177443530?signature=12e7365a3613a67379a7167323d2c57539c53d9fcf100e93e6ece743c14230a9) |
| 42 | 177443602 | 2073792263526938 | 2026-09-14 | 2026-09-17 | 4 | Video | 98 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2073792263526938) · [share](https://app.gethookd.ai/share/ad/177443602?signature=c7b285afffca47f2dae3a4244736d275d94880a7f74338e78ee9a246ee829c87) |
| 43 | 177443600 | 2513290722497605 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2513290722497605) · [share](https://app.gethookd.ai/share/ad/177443600?signature=ddcd685a91abfe87049a8b15bca3ec2472427e8c95a15dc7762f54cad2ab1642) |
| 44 | 177443599 | 1133395249149782 | 2026-09-14 | 2026-09-17 | 4 | Video | 34 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1133395249149782) · [share](https://app.gethookd.ai/share/ad/177443599?signature=0b63f79b5e22ad95e72fbe0283b5b2f29c287ad0b413acc81da374bdc52d329a) |
| 45 | 177443598 | 3670824246413927 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | F-Angebot, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3670824246413927) · [share](https://app.gethookd.ai/share/ad/177443598?signature=41f2961d627967c40ecc3e207c46b8000fba2b2ca4a1bfc74abca492b5051d44) |
| 46 | 177443597 | 1753919435864474 | 2026-09-14 | 2026-09-19 | 6 | Bild | – | When Did You Last Wash Your Duvet? | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1753919435864474) · [share](https://app.gethookd.ai/share/ad/177443597?signature=1fd330417eda40b19982750d960267251b300d61d02f19ef774729067d903643) |
| 47 | 177443596 | 1068339942444828 | 2026-09-14 | 2026-09-19 | 6 | Bild | – | When Did You Last Wash Your Duvet? | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1068339942444828) · [share](https://app.gethookd.ai/share/ad/177443596?signature=97e9107b8d99f64129bf266ca55bc9a87a40b954190972d55be43bccd790d2d3) |
| 48 | 177443595 | 840757192396215 | 2026-09-14 | 2026-09-17 | 4 | Video | 34 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=840757192396215) · [share](https://app.gethookd.ai/share/ad/177443595?signature=fb3ec8d47cec9e5c384e6557da566e2a7167bc1dcce9ad6004cb0fadaea8b19a) |
| 49 | 177443594 | 2260760481446549 | 2026-09-14 | 2026-09-16 | 3 | Video | 29 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2260760481446549) · [share](https://app.gethookd.ai/share/ad/177443594?signature=32aab5c3e8c051a3e77000b5faed05d22088822596bdbc6d2464e22a702afab0) |
| 50 | 177443593 | 1665100558534130 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1665100558534130) · [share](https://app.gethookd.ai/share/ad/177443593?signature=f4deccae206a80e28326e74d23f2ecf1d936137255cea305f49342ebc1c0329f) |
| 51 | 177443592 | 1650813800086569 | 2026-09-14 | 2026-09-17 | 4 | Video | 94 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1650813800086569) · [share](https://app.gethookd.ai/share/ad/177443592?signature=0e39df1674b5bdab377169a5bff27662dab3d2399075ef2b9c93febd70e5ffdf) |
| 52 | 177443591 | 1807950816883747 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | F-Angebot, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1807950816883747) · [share](https://app.gethookd.ai/share/ad/177443591?signature=9b1b5962bd37b35bf32147c23dcf7b76b29224049049ea1392a465cbd8d4837e) |
| 53 | 177443590 | 1637789308019060 | 2026-09-14 | 2026-09-19 | 6 | Bild | – | When Did You Last Wash Your Duvet? | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1637789308019060) · [share](https://app.gethookd.ai/share/ad/177443590?signature=7d0804fe474cc900241867e4c4480513626ee440e521d3331542bd7436ee44d3) |
| 54 | 177443589 | 1062087943363494 | 2026-09-14 | 2026-09-16 | 3 | Video | 29 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1062087943363494) · [share](https://app.gethookd.ai/share/ad/177443589?signature=34b1701e868065679c26dc7306ed31ec7fd1e1118a2660e1307008ad2c28bb94) |
| 55 | 177443587 | 1365365102252559 | 2026-09-14 | 2026-09-17 | 4 | Video | 96 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1365365102252559) · [share](https://app.gethookd.ai/share/ad/177443587?signature=bde276edcdaf9c768e65fad707576046f8bbeee5604da6892f4e33cd78891e00) |
| 56 | 177443586 | 1115745250806662 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | F-Angebot, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1115745250806662) · [share](https://app.gethookd.ai/share/ad/177443586?signature=c3e170e663b3af9badf9153a8841dec1bcdee31483cc400b0085be8e43e6dacd) |
| 57 | 177443585 | 2112997812629345 | 2026-09-14 | 2026-09-16 | 3 | Video | 28 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2112997812629345) · [share](https://app.gethookd.ai/share/ad/177443585?signature=8248c0424dbc7287f602f53e57dcea576f5d035db1e239f473058c840cc22143) |
| 58 | 177443584 | 1420035363429161 | 2026-09-14 | 2026-09-16 | 3 | Video | 94 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1420035363429161) · [share](https://app.gethookd.ai/share/ad/177443584?signature=c3f292e4706e8da618c9951485184c115181b432b831b8812581f5b1b75695c0) |
| 59 | 177443583 | 1062322340039317 | 2026-09-14 | 2026-09-16 | 3 | Video | 96 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1062322340039317) · [share](https://app.gethookd.ai/share/ad/177443583?signature=45b8176c4e4d2e8be24aaaec3f22cf0c39a8ebfbd522a251950a00136b5cc3e5) |
| 60 | 177443582 | 4749659575356689 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4749659575356689) · [share](https://app.gethookd.ai/share/ad/177443582?signature=f1e9e6b8ee11393bac575639d0d9bda72b44a6d5afb364f18abe37c6133b1c89) |
| 61 | 177443581 | 3596849097145294 | 2026-09-14 | 2026-09-17 | 4 | Video | 35 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3596849097145294) · [share](https://app.gethookd.ai/share/ad/177443581?signature=8770a3816223f407aae0a981fbc60cd93879455c620054d8123dc4d98e2fca93) |
| 62 | 176509047 | 28114479864874336 | 2026-09-13 | 2026-09-15 | 3 | Video | 48 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28114479864874336) · [share](https://app.gethookd.ai/share/ad/176509047?signature=0ed329f327631ee51b9fa3aa0b71e1e0be1602dcbe46c162d9159fe929a4868f) |
| 63 | 176509066 | 1405795578348773 | 2026-09-12 | 2026-09-16 | 5 | Video | 16 s | Everyone's buying the blue one. | F-Knappheit/Farbe, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1405795578348773) · [share](https://app.gethookd.ai/share/ad/176509066?signature=0cb321d47a6685ad62cd128e9ee362e51677b6599206c7e668b97a96d75c7851) |
| 64 | 176509065 | 1071333062193488 | 2026-09-12 | 2026-09-14 | 3 | Video | 50 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1071333062193488) · [share](https://app.gethookd.ai/share/ad/176509065?signature=9669db0b0e00ec60e30cd5e73327896e4fe5ab061380a0920d7e7711fd988983) |
| 65 | 176509063 | 944582731412393 | 2026-09-12 | 2026-09-14 | 3 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=944582731412393) · [share](https://app.gethookd.ai/share/ad/176509063?signature=a372ddfb0b0807ae92f022d8cc6fa0a81d70ca62bcdca550c9416bbb2c4548a3) |
| 66 | 176509060 | 1621625339576154 | 2026-09-12 | 2026-09-16 | 5 | Video | 16 s | Hearth Red. Nearly gone. | F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1621625339576154) · [share](https://app.gethookd.ai/share/ad/176509060?signature=1f30a265e865968ab41ca2a354333e4d0ec4219f106c9ec7e8dc5af322ee855b) |
| 67 | 176509056 | 2186278792248538 | 2026-09-12 | 2026-09-14 | 3 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2186278792248538) · [share](https://app.gethookd.ai/share/ad/176509056?signature=41b0a4df7dfb88f17041680c5f8ce936c5e84ba419882f3cf2337cec316a8d41) |
| 68 | 176509055 | 2180767429991145 | 2026-09-12 | 2026-09-16 | 5 | Video | 16 s | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2180767429991145) · [share](https://app.gethookd.ai/share/ad/176509055?signature=9bbc5a4d046b3f673950a2c443b8c2250709e70b6922df7aedffef37cee09762) |
| 69 | 176509054 | 1962643637741789 | 2026-09-12 | 2026-09-15 | 4 | Video | 47 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/pleene-easyrest-duvet-2in1 | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1962643637741789) · [share](https://app.gethookd.ai/share/ad/176509054?signature=a554e25219cba3cad17680d784564316a99593283fd9e7c47ee843bcdd6b0ff8) |
| 70 | 176509052 | 1075991888730769 | 2026-09-12 | 2026-09-15 | 4 | Video | 59 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1075991888730769) · [share](https://app.gethookd.ai/share/ad/176509052?signature=896d11ba94d11972dd88fa29f17ac77f4adb7408f9f4b75b25c6c150f6378832) |
| 71 | 176508991 | 28255297224133462 | 2026-09-12 | 2026-09-17 | 6 | Video | 49 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28255297224133462) · [share](https://app.gethookd.ai/share/ad/176508991?signature=586e9db7e5756e56bb6246fa38aac1efc1a1c4b7985fd977a3fbf683aa5cd96d) |
| 72 | 176508990 | 1602884004557852 | 2026-09-12 | 2026-09-15 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | F-Angebot, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1602884004557852) · [share](https://app.gethookd.ai/share/ad/176508990?signature=d207586659ddf999ec302f11b69d22ab150bf1b051cb74e3d4cad1f60fd6eeb4) |
| 73 | 176508987 | 1655941279573927 | 2026-09-12 | 2026-09-15 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | F-Angebot, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1655941279573927) · [share](https://app.gethookd.ai/share/ad/176508987?signature=a5a4925a2adf37d5f1657d14b913c939ad83a050c2c9046ea3cf7cd31ee716c0) |
| 74 | 176508986 | 1408102604752995 | 2026-09-12 | 2026-09-17 | 6 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1408102604752995) · [share](https://app.gethookd.ai/share/ad/176508986?signature=fbfc27e40214d569d214e7c2b70c3ad3f278b49b575449f2721aeac1687986e9) |
| 75 | 176508985 | 1088698223613178 | 2026-09-12 | 2026-09-17 | 6 | Video | 49 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1088698223613178) · [share](https://app.gethookd.ai/share/ad/176508985?signature=6304303116b7f7aeac0486e46e80a748f30d7fb74bf5a9f2bd33aecc7691acb6) |
| 76 | 176508984 | 2175136563403655 | 2026-09-12 | 2026-09-17 | 6 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2175136563403655) · [share](https://app.gethookd.ai/share/ad/176508984?signature=93c729a3da289d837a0fee102bd899171882ab546b646c6b03bf4b6365a628c2) |
| 77 | 176508983 | 1221511333504674 | 2026-09-12 | 2026-09-17 | 6 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1221511333504674) · [share](https://app.gethookd.ai/share/ad/176508983?signature=41ed18628405ec73ab4ef2f7fb6acfec16d000796546d4d2056005fe640b2f80) |
| 78 | 176508981 | 28145093718480500 | 2026-09-12 | 2026-09-17 | 6 | Video | 49 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28145093718480500) · [share](https://app.gethookd.ai/share/ad/176508981?signature=75b467bb3b5270538bcb911fab12096c89c9fc3c447d73da3723172fc6dd54aa) |
| 79 | 176508979 | 1864835554677337 | 2026-09-12 | 2026-09-15 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | F-Angebot, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1864835554677337) · [share](https://app.gethookd.ai/share/ad/176508979?signature=2fc8ca3d7826e750f2ea7707646e09fbf894beb019a090d6c13353b375110b13) |
| 80 | 176019259 | 4515497522038458 | 2026-09-11 | 2026-09-13 | 3 | Video | 44 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4515497522038458) · [share](https://app.gethookd.ai/share/ad/176019259?signature=4c1250bb64d20097e0fb4f3dbbed33facd04cf96980b19ab734e383fcdfeab3e) |
| 81 | 176019255 | 1790894445237675 | 2026-09-11 | 2026-09-15 | 5 | Video | 98 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1790894445237675) · [share](https://app.gethookd.ai/share/ad/176019255?signature=2e89903b8b91d86f9c011c63bad07d35fbfaf757dc7689c7a65bb9b594b24d35) |
| 82 | 176019250 | 1048588144808991 | 2026-09-11 | 2026-09-15 | 5 | Video | 94 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1048588144808991) · [share](https://app.gethookd.ai/share/ad/176019250?signature=bb2fa23857f95c8fbbd4470ca26afe8c50a2a3a53440cb713b252b0dc726ec46) |
| 83 | 176019246 | 1418934120178412 | 2026-09-11 | 2026-09-13 | 3 | Bild | – | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1418934120178412) · [share](https://app.gethookd.ai/share/ad/176019246?signature=9cf50967f51ccc7b3b630db5181aa3835ea34294e36ffe4506e3208334d0a204) |
| 84 | 176019241 | 1066337919529975 | 2026-09-11 | 2026-09-13 | 3 | Bild | – | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1066337919529975) · [share](https://app.gethookd.ai/share/ad/176019241?signature=e9afb4b06e132db07ad4314245fa57cfad5b59eb748875f2fbfb802e422f2171) |
| 85 | 176019239 | 1732152891324106 | 2026-09-11 | 2026-09-15 | 5 | Video | 96 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1732152891324106) · [share](https://app.gethookd.ai/share/ad/176019239?signature=83dfcb5761b42b60b24ebb97d6b9a921b39d571f76ecc67849fef22b1a7271ae) |
| 86 | 176019233 | 1094931049641062 | 2026-09-11 | 2026-09-13 | 3 | Video | 45 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1094931049641062) · [share](https://app.gethookd.ai/share/ad/176019233?signature=6d58a91fd822d4c14be82b878e67a2a26a0770681ec6646e160d6cb372d52349) |
| 87 | 176019230 | 1591747636063500 | 2026-09-11 | 2026-09-13 | 3 | Video | 44 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1591747636063500) · [share](https://app.gethookd.ai/share/ad/176019230?signature=3465221580679edd49ba19eea71bbfa2387d65e2b5a77bc56c9e3d45159d232c) |
| 88 | 176019196 | 3314026992102951 | 2026-09-11 | 2026-09-13 | 3 | Bild | – | Myth vs Truth 🛏️ | C, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3314026992102951) · [share](https://app.gethookd.ai/share/ad/176019196?signature=eaf5d1c9d6ecc47321dbf0e0ced67e3a27bef8126d5147b1a411c0dc85c2517c) |
| 89 | 175318057 | 1460580929454191 | 2026-09-10 | 2026-09-13 | 4 | Bild | – | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1460580929454191) · [share](https://app.gethookd.ai/share/ad/175318057?signature=5a6e702b890f12853a1485a0260e2e074a6255554b3f255ec399ef702c22f153) |
| 90 | 173929467 | 4742524499401363 | 2026-09-08 | 2026-09-12 | 5 | Video | 48 s | The Cover Is Sewn In | C, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4742524499401363) · [share](https://app.gethookd.ai/share/ad/173929467?signature=83c55cebe89c1e13d336e356bead6be7c22e066e8a9394b241287ef7b99960a8) |
| 91 | 173929464 | 2866592690402716 | 2026-09-08 | 2026-09-10 | 3 | Video | 38 s | The Duvet That Goes In The Wash | A, F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2866592690402716) · [share](https://app.gethookd.ai/share/ad/173929464?signature=6231ce8c4f192970af0163c675f3b104590c25633eedf10ca198bcf8d1afebeb) |
| 92 | 173929458 | 1396594501799516 | 2026-09-08 | 2026-09-10 | 3 | Video | 23 s | A Duvet With No Cover? | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1396594501799516) · [share](https://app.gethookd.ai/share/ad/173929458?signature=919bfcf3c06976a17855b18a9eae3584ab808496c40dc2ce4c6d3b096eb6183b) |
| 93 | 173929457 | 1313740154015262 | 2026-09-08 | 2026-09-12 | 5 | Video | 54 s | Best decision I ever made. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1313740154015262) · [share](https://app.gethookd.ai/share/ad/173929457?signature=318a10de4d807a3da3f6df6c1924f11fad80c243fad2ddaae94e437fb6da92ac) |
| 94 | 173929454 | 2124006455660892 | 2026-09-08 | 2026-09-10 | 3 | Video | 23 s | A Duvet With No Cover? | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2124006455660892) · [share](https://app.gethookd.ai/share/ad/173929454?signature=82f3602f981c8ded46f205e02da5111dfe758e2f5f5acd66eaced5e190f97564) |
| 95 | 173929453 | 1775756157097634 | 2026-09-08 | 2026-09-12 | 5 | Video | 56 s | n/a | n/a (kein Text) | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1775756157097634) · [share](https://app.gethookd.ai/share/ad/173929453?signature=363c943770a6eac005ea84e110a874267a0f34c2e9f66aad7f390776989f17d9) |
| 96 | 173929450 | 1611973930463209 | 2026-09-08 | 2026-09-12 | 5 | Video | 48 s | The Cover Is Sewn In | C, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1611973930463209) · [share](https://app.gethookd.ai/share/ad/173929450?signature=a80523029cf057265338cb0d1b380c6bd6c6ca060c8e7df907815edcb06c42e0) |
| 97 | 173929447 | 1084752110635145 | 2026-09-08 | 2026-09-12 | 5 | Video | 55 s | Best decision I ever made. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1084752110635145) · [share](https://app.gethookd.ai/share/ad/173929447?signature=23d52a022f8b0892cfbd6432d1ef38943fb354ae201d74571083262155450522) |
| 98 | 173929446 | 1747135706520938 | 2026-09-08 | 2026-09-10 | 3 | Video | 39 s | The Duvet That Goes In The Wash | A, F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1747135706520938) · [share](https://app.gethookd.ai/share/ad/173929446?signature=41103af45d64edffdebf55011b080c0021547475e50f3fe39ac2e2d924c6eccc) |
| 99 | 173929444 | 1610741237372540 | 2026-09-08 | 2026-09-10 | 3 | Video | 24 s | A Duvet With No Cover? | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1610741237372540) · [share](https://app.gethookd.ai/share/ad/173929444?signature=96dc06e86ed7d0fad83c789b40f870e1252e6d0fb43cec8a62cdc3c8ef37bc70) |
| 100 | 173929442 | 1505795144878605 | 2026-09-08 | 2026-09-10 | 3 | Video | 38 s | The Duvet That Goes In The Wash | A, F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1505795144878605) · [share](https://app.gethookd.ai/share/ad/173929442?signature=65e304c9da2cca6468717d25a3b74600f2a206eabae99575b026fe93f26595b4) |
| 101 | 173929439 | 1106556025275590 | 2026-09-08 | 2026-09-12 | 5 | Video | 50 s | The Cover Is Sewn In | C, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1106556025275590) · [share](https://app.gethookd.ai/share/ad/173929439?signature=a267e12b5f45bf7184dc01d32db6e869ee78491d64604eafaf0be77449dbdc50) |
| 102 | 173929435 | 2919028021772107 | 2026-09-08 | 2026-09-12 | 5 | Video | 47 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/pleene-easyrest-duvet-2in1 | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2919028021772107) · [share](https://app.gethookd.ai/share/ad/173929435?signature=c50016d9643bf4d37e1afa6b14ad6930ef119939dc611c4f14a8543e4298f9cf) |
| 103 | 173307153 | 1791848022151143 | 2026-09-07 | 2026-09-08 | 2 | DPA (Katalog-Karussell) | 6 Bild(er) | Pleene EasyRest™ Quilt | A, F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1791848022151143) · [share](https://app.gethookd.ai/share/ad/173307153?signature=c316a45d4dc935a7f05a32666c8d157f3c1816aa64c4607768db951b292a7815) |
| 104 | 173307006 | 1000819466312449 | 2026-09-07 | 2026-09-12 | 6 | Video | 38 s | The Duvet That Goes In The Wash | A, F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1000819466312449) · [share](https://app.gethookd.ai/share/ad/173307006?signature=6a3facb6e15dea5163f1c82f08c104d1aef6c96ea8688ec8bea2a6b5746e0553) |
| 105 | 173307005 | 1727217541693945 | 2026-09-07 | 2026-09-11 | 5 | Video | 56 s | n/a | n/a (kein Text) | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1727217541693945) · [share](https://app.gethookd.ai/share/ad/173307005?signature=e955c720ed02764a12620677fab430c40c3a1302ba1074ff6cbb6fb4feea2a6f) |
| 106 | 173307004 | 1750365589627986 | 2026-09-07 | 2026-09-11 | 5 | Video | 54 s | Best decision I ever made. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1750365589627986) · [share](https://app.gethookd.ai/share/ad/173307004?signature=ba8f780802160b23c82b13adf941ab4fe94b5d5de7ed58620b8c2308a5b1f268) |
| 107 | 173307003 | 1551454820113864 | 2026-09-07 | 2026-09-12 | 6 | Video | 15 s | End Of Season Sale | F-Angebot, F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1551454820113864) · [share](https://app.gethookd.ai/share/ad/173307003?signature=7d90d90ea9416ce04b33ce21489d3bedbb0cdbf29bfe65acfd480939c61bbaea) |
| 108 | 173307002 | 1408393734570917 | 2026-09-07 | 2026-09-12 | 6 | Video | 48 s | The Cover Is Sewn In | C, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1408393734570917) · [share](https://app.gethookd.ai/share/ad/173307002?signature=90c2c08116708120d27bfc2e8580872008f442c0f3e95ccbb3cc6fc9b55e5e28) |
| 109 | 173307001 | 2019851816071206 | 2026-09-07 | 2026-09-12 | 6 | Video | 39 s | The Duvet That Goes In The Wash | A, F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2019851816071206) · [share](https://app.gethookd.ai/share/ad/173307001?signature=41c3897aadcad08aca61bc702885f8d3be00532d8544ef94b04666894383e743) |
| 110 | 173306995 | 1773663007005034 | 2026-09-07 | 2026-09-12 | 6 | Video | 15 s | End Of Season Sale | F-Angebot, F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1773663007005034) · [share](https://app.gethookd.ai/share/ad/173306995?signature=140a8ebf96325d786b4b3c419967f9d1ec43bb5dfa1319fce5a79b8f7b7b1b75) |
| 111 | 173306993 | 892043567122512 | 2026-09-07 | 2026-09-12 | 6 | Video | 50 s | The Cover Is Sewn In | C, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=892043567122512) · [share](https://app.gethookd.ai/share/ad/173306993?signature=ca830277dd3a0fba7588d3ebb8dd729b43dc82c336a8c1b2908c7757831e5801) |
| 112 | 173306992 | 1353734010076648 | 2026-09-07 | 2026-09-12 | 6 | Video | 15 s | End Of Season Sale | F-Angebot, F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1353734010076648) · [share](https://app.gethookd.ai/share/ad/173306992?signature=02b4684000d99e4cd4849b9fb8fbd1e96290019bcdb22cc4b9ec3c68f424d7ec) |
| 113 | 173306991 | 1813978556714586 | 2026-09-07 | 2026-09-12 | 6 | Video | 48 s | The Cover Is Sewn In | C, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1813978556714586) · [share](https://app.gethookd.ai/share/ad/173306991?signature=45f76ead5c2e625579dd0e46616f9d32b7701a8d6aa00098f07f5ef595ee8a94) |
| 114 | 173306989 | 1415692010491060 | 2026-09-07 | 2026-09-12 | 6 | Video | 38 s | The Duvet That Goes In The Wash | A, F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1415692010491060) · [share](https://app.gethookd.ai/share/ad/173306989?signature=dfaaa21c2a8eb9d0a0d154f9428d5549072fbdee069a0a84ca508b6fa9e441dc) |
| 115 | 173306987 | 1649586253355020 | 2026-09-07 | 2026-09-11 | 5 | Video | 55 s | Best decision I ever made. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1649586253355020) · [share](https://app.gethookd.ai/share/ad/173306987?signature=245c4c09deb9406cdfbd1eadba71da357fbac13cc785b382d6894b5c87f12b7e) |
| 116 | 172760592 | 1473559164549663 | 2026-09-06 | 2026-09-10 | 5 | Video | 59 s | Done fighting with bed linen. | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1473559164549663) · [share](https://app.gethookd.ai/share/ad/172760592?signature=34ef3733de3b00b2d39bfd544a65d6e7be2a30c2d6ce23b73830cfb80bbd9e85) |
| 117 | 172760591 | 2155825362011800 | 2026-09-06 | 2026-09-08 | 3 | Video | 59 s | Done fighting with bed linen. | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2155825362011800) · [share](https://app.gethookd.ai/share/ad/172760591?signature=f234261cbd623d574d2b1b896e8b26322b56b0add0f9778861b0b1f32cd1213f) |
| 118 | 172760590 | 2154817405448722 | 2026-09-06 | 2026-09-10 | 5 | Video | 16 s | Everyone's buying the blue one. | F-Knappheit/Farbe, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2154817405448722) · [share](https://app.gethookd.ai/share/ad/172760590?signature=51d9c5f51a7ff752d4fb0266db56db7490e25422000ee88f65127a396c3fa683) |
| 119 | 172760589 | 4080616435408881 | 2026-09-06 | 2026-09-10 | 5 | Video | 29 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4080616435408881) · [share](https://app.gethookd.ai/share/ad/172760589?signature=c67cec1fd4b8eda7027c98101f3f4c4e9d8301a9275d5de37d0e02f056ff4133) |
| 120 | 172760587 | 1822169385440820 | 2026-09-06 | 2026-09-10 | 5 | Video | 16 s | Hearth Red. Nearly gone. | F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1822169385440820) · [share](https://app.gethookd.ai/share/ad/172760587?signature=2b4e810a164a060bd1eb662fffa47f884bbbdb856d88f7878267826394bc65f9) |
| 121 | 172760586 | 2224833071629221 | 2026-09-06 | 2026-09-10 | 5 | Bild | – | Ready for the colder nights. | F-Knappheit/Farbe, F-Angebot, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2224833071629221) · [share](https://app.gethookd.ai/share/ad/172760586?signature=a28d96cdbad6739f0e66379d1579f0d4d173c3222c592ba1a3f285b1591d3eea) |
| 122 | 172760585 | 1383471107298030 | 2026-09-06 | 2026-09-10 | 5 | Video | 28 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1383471107298030) · [share](https://app.gethookd.ai/share/ad/172760585?signature=614d76db8b735b3e0b425eedb0f17da8c7aa491d9d269cb296a85e2445b0bd12) |
| 123 | 172760584 | 5071189629774111 | 2026-09-06 | 2026-09-08 | 3 | Video | 59 s | Done fighting with bed linen. | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=5071189629774111) · [share](https://app.gethookd.ai/share/ad/172760584?signature=89ad43600d35883c4c875291e49e0af48c19c42995b4872e2f077785bdf5281d) |
| 124 | 172760582 | 1566620011909494 | 2026-09-06 | 2026-09-10 | 5 | Video | 29 s | Be honest. When did you last wash it? | A, F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1566620011909494) · [share](https://app.gethookd.ai/share/ad/172760582?signature=4653e55e292e27bc8ba412a6127af6ffce2dbf2cb58e7d36d4b2e49bfb749e9b) |
| 125 | 172760581 | 2064941720817246 | 2026-09-06 | 2026-09-09 | 4 | Video | 50 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2064941720817246) · [share](https://app.gethookd.ai/share/ad/172760581?signature=62b824fc009ef8712321fb6207ee1cca8499f004aadca0a232a67120956316d9) |
| 126 | 172760577 | 1546680813321412 | 2026-09-06 | 2026-09-09 | 4 | Video | 50 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1546680813321412) · [share](https://app.gethookd.ai/share/ad/172760577?signature=c6010cabb389b06207f0b7b85de3e14580452be3b3a3f25d86fe96c841362540) |
| 127 | 172760575 | 2062520128474003 | 2026-09-06 | 2026-09-09 | 4 | Video | 50 s | The Duvet You Can Actually Wash | A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2062520128474003) · [share](https://app.gethookd.ai/share/ad/172760575?signature=368770e1ba104e2cddba7d32d17ff4cca0f40d232c2e1f0b1b693a1380b131a5) |
| 128 | 172760574 | 1125246056730912 | 2026-09-06 | 2026-09-10 | 5 | Video | 16 s | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1125246056730912) · [share](https://app.gethookd.ai/share/ad/172760574?signature=a265429009c433a43bccd6e62f08bc60d973eb49316be71d4228add1a0e97c2f) |
| 129 | 172760572 | 2197532430803188 | 2026-09-06 | 2026-09-08 | 3 | Video | 59 s | Done fighting with bed linen. | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2197532430803188) · [share](https://app.gethookd.ai/share/ad/172760572?signature=fc3725255d53d3a4bc819d5488413d1c65ccaa3d1eaa465504e0a845605c2457) |
| 130 | 172760562 | 2737528016642337 | 2026-09-06 | 2026-09-10 | 5 | Video | 49 s | End Of Season Sale | F-Angebot, F-Knappheit/Farbe | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2737528016642337) · [share](https://app.gethookd.ai/share/ad/172760562?signature=60a829ad071ce22be7d44e89c70ee87a884b0496c6e5517e26cd454eeb63d64e) |
| 131 | 172403416 | 1495174535679772 | 2026-09-05 | 2026-09-10 | 6 | Video | 59 s | Done fighting with bed linen. | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1495174535679772) · [share](https://app.gethookd.ai/share/ad/172403416?signature=04c920975df7291f74c0d3a215cd8c7b45527ffbed620639c9e6ee522e908b59) |
| 132 | 172403414 | 1359950386127722 | 2026-09-05 | 2026-09-09 | 5 | Bild | – | Only 26 Left In Hearth Red | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1359950386127722) · [share](https://app.gethookd.ai/share/ad/172403414?signature=7ce3efc089cae8465e763a3a2833d4818d13f53f6721553419bc34fcc87ee561) |
| 133 | 172403410 | 1011734415282335 | 2026-09-05 | 2026-09-07 | 3 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1011734415282335) · [share](https://app.gethookd.ai/share/ad/172403410?signature=c031a6d42aa9bec274935ec2721365081180a4163a81544118fdfb0c0a89e13b) |
| 134 | 172403408 | 1903265557302675 | 2026-09-05 | 2026-09-10 | 6 | Video | 15 s | Ready for the colder nights. | F-Knappheit/Farbe, F-Angebot, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1903265557302675) · [share](https://app.gethookd.ai/share/ad/172403408?signature=bfb0af5a1e4e5a82f16edd5b86f44ebbb56dc5556a1863f47a4d1e371b532065) |
| 135 | 172403405 | 2993343241057795 | 2026-09-05 | 2026-09-09 | 5 | Bild | – | Only 26 Left In Hearth Red | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2993343241057795) · [share](https://app.gethookd.ai/share/ad/172403405?signature=3cb40faac6160592ee39229aa9835e5dd359fd87160be63d99143151d82788e4) |
| 136 | 172403404 | 1100457982933062 | 2026-09-05 | 2026-09-10 | 6 | Video | 15 s | Ready for the colder nights. | F-Knappheit/Farbe, F-Angebot, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1100457982933062) · [share](https://app.gethookd.ai/share/ad/172403404?signature=43077be1c9f75c9211e6b7ddbdb399536420b1e69fa246418be2a5485a3f4be1) |
| 137 | 172403397 | 2575860129544226 | 2026-09-05 | 2026-09-10 | 6 | Video | 15 s | Ready for the colder nights. | F-Knappheit/Farbe, F-Angebot, B | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2575860129544226) · [share](https://app.gethookd.ai/share/ad/172403397?signature=754de3445e3d24f94af983df44f76271cbe1cc6e05c68be95a1c34ae33aaf2c2) |
| 138 | 172403392 | 894822553505355 | 2026-09-05 | 2026-09-09 | 5 | Bild | – | Only 26 Left In Hearth Red | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=894822553505355) · [share](https://app.gethookd.ai/share/ad/172403392?signature=4842e5be2a38754fb19073aeb84a99fc495ccf5b401752fa9480fab1b39c82bd) |
| 139 | 172403382 | 1043368568571207 | 2026-09-05 | 2026-09-10 | 6 | Video | 59 s | Done fighting with bed linen. | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1043368568571207) · [share](https://app.gethookd.ai/share/ad/172403382?signature=455f14c32c51aa4eeba91c1d7b0a1d4ac2faf012615529cf6ff4d1db370fd2c7) |
| 140 | 172403290 | 28510580475296819 | 2026-09-05 | 2026-09-09 | 5 | Video | 96 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28510580475296819) · [share](https://app.gethookd.ai/share/ad/172403290?signature=fd3527a1f12be055e344574cbb88297284557047fbbd326bffb5bd2e13a5ed2e) |
| 141 | 170468005 | 1373362798113475 | 2026-09-02 | 2026-09-07 | 6 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1373362798113475) · [share](https://app.gethookd.ai/share/ad/170468005?signature=2671a74f597c9c31a930449c59dd7dbd8953fb2f5b329ee5e4870ef5233d1ec9) |
| 142 | 169784535 | 1103610958669062 | 2026-09-02 | 2026-09-05 | 4 | Video | 9 s | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1103610958669062) · [share](https://app.gethookd.ai/share/ad/169784535?signature=27cd42a1c461e7a06f38d8a43b3e8cb8e5901bc5b85d0f2091b087bd17e6e379) |
| 143 | 169082944 | 1063281430012872 | 2026-08-31 | 2026-09-03 | 4 | Video | 56 s | n/a | n/a (kein Text) | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1063281430012872) · [share](https://app.gethookd.ai/share/ad/169082944?signature=ccd7617745b1f844aa56ce5e2dd9e9fa2679a8a215c40a8d23d579a61d411b87) |
| 144 | 169082943 | 1057947053611731 | 2026-08-31 | 2026-09-03 | 4 | Video | 54 s | Best decision I ever made. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1057947053611731) · [share](https://app.gethookd.ai/share/ad/169082943?signature=9979b60a88acad2dd355eeef2ae2180bb2e3c9a47f8341d67043a650d5c3faa2) |
| 145 | 169082939 | 1595930678671246 | 2026-08-31 | 2026-09-03 | 4 | Video | 55 s | Best decision I ever made. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1595930678671246) · [share](https://app.gethookd.ai/share/ad/169082939?signature=29f934e432f4b95834b38de07164974e9dbe13400caa5b8c32a13a26df89bbab) |
| 146 | 169082930 | 39017574957841998 | 2026-08-31 | 2026-09-05 | 6 | Video | 44 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=39017574957841998) · [share](https://app.gethookd.ai/share/ad/169082930?signature=ef1a6f899fad7115e11af44db3bd5fe068648a8b8124165c663ffeb9787ea290) |
| 147 | 168246691 | 2293103338097014 | 2026-08-29 | 2026-09-03 | 6 | Video | 15 s | Pick a colour. Watch. | F-Knappheit/Farbe, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2293103338097014) · [share](https://app.gethookd.ai/share/ad/168246691?signature=620d8944f6dc8b4f894c4b8f9f8c219cbfb636dce8b2119a47556cfb9ceceee1) |
| 148 | 168246687 | 1681661857299597 | 2026-08-29 | 2026-09-03 | 6 | Video | 15 s | Pick a colour. Watch. | F-Knappheit/Farbe, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1681661857299597) · [share](https://app.gethookd.ai/share/ad/168246687?signature=833e484afb7dc3d2e8ecd7003188a3c257bdf388e3b9a5dfdb54ec0d8846f130) |
| 149 | 168246683 | 1429155502643651 | 2026-08-29 | 2026-09-03 | 6 | Video | 26 s | Duvet & Cover In One | C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1429155502643651) · [share](https://app.gethookd.ai/share/ad/168246683?signature=a8dff647e7084fb9044b563b677037a9c4fc8447b41b9d1faf660409e9b5f565) |
| 150 | 168246681 | 1579804513380981 | 2026-08-29 | 2026-09-02 | 5 | Video | 26 s | Duvet & Cover In One | C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1579804513380981) · [share](https://app.gethookd.ai/share/ad/168246681?signature=4686c482a3fa397ba50b0180aca04fea349cbaa88edad17ca8e51c77da27a514) |
| 151 | 168246677 | 1399976375399987 | 2026-08-29 | 2026-09-03 | 6 | Video | 26 s | Duvet & Cover In One | C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1399976375399987) · [share](https://app.gethookd.ai/share/ad/168246677?signature=91765c1d883833146b2b1499d6f27f94ac51aa2dcb7f2dde3ba5828511ffec14) |
| 152 | 163921090 | 1507951734683814 | 2026-08-27 | 2026-08-28 | 2 | Video | 42 s | A Duvet With No Cover? | F-Social-Proof, C | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1507951734683814) · [share](https://app.gethookd.ai/share/ad/163921090?signature=0a9f0705447563d2bc2177c2ef0c5eb4427695d95aa5f4933f6fac4b281d4e57) |
| 153 | 163921087 | 944463371282198 | 2026-08-27 | 2026-08-29 | 3 | Video | 15 s | End Of Season Sale | F-Angebot, F-Knappheit/Farbe | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=944463371282198) · [share](https://app.gethookd.ai/share/ad/163921087?signature=dbabf958912509934002176b25730135248f1ecd65d749a25059ec39fdb9b45b) |
| 154 | 163921086 | 969450709504445 | 2026-08-27 | 2026-08-28 | 2 | Video | 42 s | A Duvet With No Cover? | F-Social-Proof, C | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=969450709504445) · [share](https://app.gethookd.ai/share/ad/163921086?signature=e9ed3f6703cd1c492a7d61853dd650776b4ca3f78e3ae8547d769f242f0b8ce0) |
| 155 | 163921085 | 2182897075602948 | 2026-08-27 | 2026-08-29 | 3 | Video | 15 s | End Of Season Sale | F-Angebot, F-Knappheit/Farbe | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2182897075602948) · [share](https://app.gethookd.ai/share/ad/163921085?signature=d7e7da488a277dd0f3997c646f89861fc931e9e1eca511ce1973f354d35573b4) |
| 156 | 163921083 | 2301951323952231 | 2026-08-27 | 2026-08-29 | 3 | Video | 15 s | End Of Season Sale | F-Angebot, F-Knappheit/Farbe | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2301951323952231) · [share](https://app.gethookd.ai/share/ad/163921083?signature=e0031e10058b5b97b0b4dc7a368cd8967c194eb7d5489070ae8d3c4cf6ccb60b) |
| 157 | 163921080 | 1795527678139092 | 2026-08-27 | 2026-08-29 | 3 | Video | 23 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1795527678139092) · [share](https://app.gethookd.ai/share/ad/163921080?signature=4cf9442d2d597ea0f9fabb4b8dacfa2fb7d10c45fa0ee79d35d827fb1d72aa24) |
| 158 | 163921076 | 2109383479965541 | 2026-08-27 | 2026-08-28 | 2 | Video | 42 s | A Duvet With No Cover? | F-Social-Proof, C | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2109383479965541) · [share](https://app.gethookd.ai/share/ad/163921076?signature=d3129746960cf7fcc05bcf84f40bd1869c96a2c74d50077f8522b2ee71d2cbbe) |
| 159 | 163921068 | 1774397390382079 | 2026-08-27 | 2026-08-29 | 3 | Video | 47 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1774397390382079) · [share](https://app.gethookd.ai/share/ad/163921068?signature=6ced84e543db34204bd831a6a201cebb6682f5b08dfeec641a2590c492396e82) |
| 160 | 160709948 | 1081193501126219 | 2026-08-26 | 2026-08-29 | 4 | Bild | – | I've Quit Bed Linen | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1081193501126219) · [share](https://app.gethookd.ai/share/ad/160709948?signature=fefd44f7dfc20214ab3cce5a784f38b0c6b310e30d37054382a620e06b075a11) |
| 161 | 160709944 | 2266305264227781 | 2026-08-26 | 2026-08-30 | 5 | DPA (Katalog-Karussell) | 1 Video(s): 36 s; 7 Bild(er) | Pleene | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2266305264227781) · [share](https://app.gethookd.ai/share/ad/160709944?signature=b577fde27437ee2aba50500c9cc66e49cad0330bf8e4242078c369a37dc6c3ed) |
| 162 | 160709929 | 28109977455334741 | 2026-08-26 | 2026-08-29 | 4 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28109977455334741) · [share](https://app.gethookd.ai/share/ad/160709929?signature=8d8e9f4864b97a6d285e9eaca6eb5a9285a9b4fd475c300c2eea14cea90fb4d7) |
| 163 | 160709927 | 2572930263145430 | 2026-08-26 | 2026-08-29 | 4 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2572930263145430) · [share](https://app.gethookd.ai/share/ad/160709927?signature=54fd2107141c3e5974e184f88822d706e0f74aa091ee8750549f4b084315b807) |
| 164 | 160709926 | 1085517767464996 | 2026-08-26 | 2026-08-28 | 3 | Video | 50 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1085517767464996) · [share](https://app.gethookd.ai/share/ad/160709926?signature=00bc45001dd9357fa7743ead4ef9c6238748a40fa26a3ab56ecb401684def44b) |
| 165 | 160709961 | 2260628194476786 | 2026-08-25 | 2026-08-30 | 6 | Video | 47 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2260628194476786) · [share](https://app.gethookd.ai/share/ad/160709961?signature=5122603c55275ec13f2871e574ec497fa1b5e466631f8f664bbec4b3b173e376) |
| 166 | 160709957 | 2064399717496829 | 2026-08-25 | 2026-08-27 | 3 | Video | 23 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2064399717496829) · [share](https://app.gethookd.ai/share/ad/160709957?signature=f5d8aa1fec83bd858da01a57694b65ffcec54c1ab083c537269b941b93e4c855) |
| 167 | 160709955 | 1100389765715214 | 2026-08-25 | 2026-08-30 | 6 | Video | 36 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1100389765715214) · [share](https://app.gethookd.ai/share/ad/160709955?signature=88f3b14e1120d2e8115efb28054f6c32a658c3261927fdeeab4000ef943fd10d) |
| 168 | 160709950 | 2301207490642262 | 2026-08-25 | 2026-08-29 | 5 | Video | 40 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2301207490642262) · [share](https://app.gethookd.ai/share/ad/160709950?signature=0cf51dc6d7c6ea9a72a0ae0b325005fe89c4bc74e4652784fc66d0d5b281d072) |
| 169 | 160709949 | 1221049120196497 | 2026-08-25 | 2026-08-30 | 6 | Video | 41 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1221049120196497) · [share](https://app.gethookd.ai/share/ad/160709949?signature=a992fc436e5986a18614d58c34bd9a20bdf5b690dc2474acbfdd6ea0489f204c) |
| 170 | 157492489 | 1081653717937889 | 2026-08-25 | 2026-08-28 | 4 | Video | 16 s | Everyone's buying the blue one. | F-Knappheit/Farbe, F-Social-Proof | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1081653717937889) · [share](https://app.gethookd.ai/share/ad/157492489?signature=b976a10a18bd562b4bc73ecd5dca2c86cbc8747232f337b62e0c19473584ed69) |
| 171 | 157492488 | 1612940290484916 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1612940290484916) · [share](https://app.gethookd.ai/share/ad/157492488?signature=002bbb0caed63fc997b3cc1e258264245d1be199739b1a0f38f9c4b37f14463a) |
| 172 | 157492485 | 2191503985130597 | 2026-08-25 | 2026-08-28 | 4 | Video | 16 s | Mint Green is almost gone. | F-Knappheit/Farbe, F-Angebot, A | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2191503985130597) · [share](https://app.gethookd.ai/share/ad/157492485?signature=5f17c96390d02ec4e058bf835dca1895b32c0cd6161baf821d2bd4646b1b834d) |
| 173 | 157492484 | 1068419246180894 | 2026-08-25 | 2026-08-28 | 4 | Bild | – | Who Wins In Your House? | F-Knappheit/Farbe, A | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1068419246180894) · [share](https://app.gethookd.ai/share/ad/157492484?signature=2cca06d67ac0d22467469bed203baabc91303161e4978d73d36db1b726396560) |
| 174 | 157492482 | 29044842228452116 | 2026-08-25 | 2026-08-28 | 4 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=29044842228452116) · [share](https://app.gethookd.ai/share/ad/157492482?signature=60f5f8823b70421f9e7a0e68b1f2cebd7c6a28ab6ecc58b0720954319d9f999c) |
| 175 | 157492478 | 2420769561780009 | 2026-08-25 | 2026-08-28 | 4 | Bild | – | Who Wins In Your House? | F-Knappheit/Farbe, A | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2420769561780009) · [share](https://app.gethookd.ai/share/ad/157492478?signature=33b0dee5afdb8c8e537404fa06fe93e4a7be923e15f2364042c4869e0cb58983) |
| 176 | 157492475 | 28310942411851184 | 2026-08-25 | 2026-08-28 | 4 | Video | 16 s | Hearth Red. Nearly gone. | F-Knappheit/Farbe | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28310942411851184) · [share](https://app.gethookd.ai/share/ad/157492475?signature=5eb2d7f117c2b9294d3bb589fbaabf079f80f1faeade780115f4d8c9295cc156) |
| 177 | 157492473 | 4546369339018467 | 2026-08-25 | 2026-08-29 | 5 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4546369339018467) · [share](https://app.gethookd.ai/share/ad/157492473?signature=3eaaac535b9780fa955d0915458de135634fc22a69ebcc784f9e461f46503df6) |
| 178 | 157492472 | 1825439511773317 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | I've Quit Bed Linen | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1825439511773317) · [share](https://app.gethookd.ai/share/ad/157492472?signature=5b71cd123544e758cf706a1b48078891c4fc64e6687cc4f3247833117d7a5c9f) |
| 179 | 157492471 | 2112919846285525 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | I've Quit Bed Linen | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2112919846285525) · [share](https://app.gethookd.ai/share/ad/157492471?signature=1fcc0b6e3f899dbfb6d7112768569574a3134c8a7685ab9e6af35cac7c818564) |
| 180 | 157492470 | 1705539210556149 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1705539210556149) · [share](https://app.gethookd.ai/share/ad/157492470?signature=145b0f5a9287037aa2910c3574c8e9c26286d5813a25ea7cb3fbcb5915e088f6) |
| 181 | 157492467 | 1078897054604867 | 2026-08-25 | 2026-08-28 | 4 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/pages/duvet-10r | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1078897054604867) · [share](https://app.gethookd.ai/share/ad/157492467?signature=3cf62701e1d688a71248fdf97c0c8ef346e1e0a23509bef2fa349d64780f97d3) |
| 182 | 157492466 | 1015702894758175 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | I've Quit Bed Linen | C, F-Social-Proof | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1015702894758175) · [share](https://app.gethookd.ai/share/ad/157492466?signature=0773a1845fc8aca226fffc23042104b3df58e724899d6427ee7f03af8bc9b7a0) |
| 183 | 157492462 | 1748296249698720 | 2026-08-25 | 2026-08-29 | 5 | Video | 23 s | A Duvet With No Cover? | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1748296249698720) · [share](https://app.gethookd.ai/share/ad/157492462?signature=7bed1c94429100715f4f68291026c8adf46a9151be06eb875931d38a281fd7bd) |
| 184 | 151025048 | 3301904860149799 | 2026-08-22 | 2026-08-24 | 3 | Video | 23 s | Best decision I ever made. | F-Social-Proof, C | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3301904860149799) · [share](https://app.gethookd.ai/share/ad/151025048?signature=d07f71e93c7157b05227904578990a9b3cfdb976353663f49e73088bc69ae70f) |
| 185 | 148470070 | 2301093177301755 | 2026-08-17 | 2026-08-21 | 5 | Video | 40 s | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2301093177301755) · [share](https://app.gethookd.ai/share/ad/148470070?signature=1494deb455ef2f7af2394ffaefdffbbc74a8a0f5fc2dc4965debd2bf1bd1c3e4) |
| 186 | 148470066 | 1064404466239652 | 2026-08-17 | 2026-08-21 | 5 | Video | 39 s | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1064404466239652) · [share](https://app.gethookd.ai/share/ad/148470066?signature=8b45b88137ac4ce24c7f74dc339f2ec4496d5f8363a509deaf2c6af4033164c8) |
| 187 | 148470063 | 1318852313660983 | 2026-08-17 | 2026-08-21 | 5 | Video | 38 s | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1318852313660983) · [share](https://app.gethookd.ai/share/ad/148470063?signature=6b3c52d047a550d932f8ab20edb45e47ed8178c847592cd16498849cd72454e4) |
| 188 | 148470052 | 2034537413848091 | 2026-08-17 | 2026-08-21 | 5 | Video | 38 s | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2034537413848091) · [share](https://app.gethookd.ai/share/ad/148470052?signature=07eda101a2d1fc014b6521fc78879fe5233a0d079e31aaa14a732c8d68d88223) |
| 189 | 148470051 | 2089139941674812 | 2026-08-17 | 2026-08-21 | 5 | Video | 30 s | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2089139941674812) · [share](https://app.gethookd.ai/share/ad/148470051?signature=e93174c6e0855912b409f45a0e286bd763cb40328817e95af679f2dc6bdb0472) |
| 190 | 148470050 | 1378606943654097 | 2026-08-17 | 2026-08-21 | 5 | Video | 20 s | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1378606943654097) · [share](https://app.gethookd.ai/share/ad/148470050?signature=dfabf2d52d1fa7ff51d748fdb2763651614908eb9df5d6eca8295b86e1111704) |
| 191 | 148470048 | 1821943842572215 | 2026-08-17 | 2026-08-21 | 5 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1821943842572215) · [share](https://app.gethookd.ai/share/ad/148470048?signature=1021f57230380bffc5d59e5cc238361f76f8b38e1abd5b369ba33f3ef17e631c) |
| 192 | 148470042 | 1892456801721570 | 2026-08-17 | 2026-08-21 | 5 | Video | 63 s | Never lift your mattress again. | E, C | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1892456801721570) · [share](https://app.gethookd.ai/share/ad/148470042?signature=bdfcef67290d2b2bf252d3115a52a178b8704cf7988e66e90a388feb1571b6ff) |
| 193 | 145443344 | 1039722162271817 | 2026-08-14 | 2026-08-18 | 5 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1039722162271817) · [share](https://app.gethookd.ai/share/ad/145443344?signature=61d373a6271fbf33568a0c96f34c3f204bd461bbfea756103ed87d4696e860d5) |
| 194 | 144538448 | 1958958918100454 | 2026-08-14 | 2026-08-18 | 5 | Video | 29 s | Not your normal fitted sheet | C | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1958958918100454) · [share](https://app.gethookd.ai/share/ad/144538448?signature=883dc6c733e047737588261bec31c92b182852ddc445b2570c0be9a6ec527ed8) |
| 195 | 144538461 | 1358924786406826 | 2026-08-13 | 2026-08-18 | 6 | Video | 29 s | Not your normal fitted sheet | C | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1358924786406826) · [share](https://app.gethookd.ai/share/ad/144538461?signature=47130893fdf6bcc9c0a56ab8393eb4c52bdb0390703525e7426479561565cf0d) |
| 196 | 144538443 | 1621543769568759 | 2026-08-13 | 2026-08-18 | 6 | Video | 29 s | Not your normal fitted sheet | C | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1621543769568759) · [share](https://app.gethookd.ai/share/ad/144538443?signature=5f8d34f70af38a48dfbdd164ad91af739f281193ec367232f43ffc5006bf22f7) |
| 197 | 144538440 | 2324305058330745 | 2026-08-13 | 2026-08-18 | 6 | Video | 21 s | Not your normal fitted sheet | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2324305058330745) · [share](https://app.gethookd.ai/share/ad/144538440?signature=9d832ad98d6ba8a4a8277766ba915987fcbefcc53c49818951433b388d556daa) |
| 198 | 141368443 | 1692150768534132 | 2026-08-10 | 2026-08-13 | 4 | Video | 50 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1692150768534132) · [share](https://app.gethookd.ai/share/ad/141368443?signature=04dbd77de5710410c7b1387ea3344ba8ef4858efeea984e553dde807972befab) |
| 199 | 139561358 | 2250098979162898 | 2026-08-08 | 2026-08-11 | 4 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2250098979162898) · [share](https://app.gethookd.ai/share/ad/139561358?signature=123c971ebdbc3bae64dcd1cbfcfbb1450fb929337c689910be60ebc3d17d1594) |
| 200 | 139561003 | 1061887276489463 | 2026-08-08 | 2026-08-11 | 4 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1061887276489463) · [share](https://app.gethookd.ai/share/ad/139561003?signature=4ab2075d47422e21e9a812d8cc824d54ff8fb77fab21099ff8a40537904a638b) |
| 201 | 139560993 | 1974393473279543 | 2026-08-08 | 2026-08-11 | 4 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1974393473279543) · [share](https://app.gethookd.ai/share/ad/139560993?signature=c7b89329aa0b82bfc06195199fe13c8b7930cdcc641789f6ecae964f17432854) |
| 202 | 139560971 | 1370133432000783 | 2026-08-07 | 2026-08-11 | 5 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1370133432000783) · [share](https://app.gethookd.ai/share/ad/139560971?signature=7a43bdcc08a37246b998394ba04a7def356b6a68ac7349874b912c21d0eb0326) |

**Aufgegeben nach langer Laufzeit (inaktiv, ≥ 30 Tage gelaufen): 95 Ads**

| # | GetHooked-ID | Meta-ID | Start | Ende | Tage | used | Format | Länge | Headline | Angle | Landingpage | Links |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 133364681 | 1332402255676454 | 2026-06-02 | 2026-09-06 | 97 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1332402255676454) · [share](https://app.gethookd.ai/share/ad/133364681?signature=1f697d19a3e48473cc48ee7242eb827b0144b438577de47455947de87e8ab6aa) |
| 2 | 136389548 | 2264705503936499 | 2026-06-01 | 2026-08-28 | 89 | 1 | Video | 15 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2264705503936499) · [share](https://app.gethookd.ai/share/ad/136389548?signature=04225e5f98e694f2d087aa884a689ec9ce7fa7995bfdc206597109cd1b3a02da) |
| 3 | 136389371 | 1666885827896282 | 2026-06-01 | 2026-08-28 | 89 | 1 | Video | 39 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1666885827896282) · [share](https://app.gethookd.ai/share/ad/136389371?signature=a95032fa92b4fbf0d5f4b9744b87351beafdad9634c50e8b0ae18de242b06cd6) |
| 4 | 136388705 | 2167721337409320 | 2026-06-01 | 2026-08-28 | 89 | 1 | Video | 48 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2167721337409320) · [share](https://app.gethookd.ai/share/ad/136388705?signature=59cb41d55414e96286187aee0b49252cfc352ad2e8b678704364f32e28cbf745) |
| 5 | 136389047 | 27141063635550818 | 2026-06-11 | 2026-09-07 | 89 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=27141063635550818) · [share](https://app.gethookd.ai/share/ad/136389047?signature=f407409921a12b77f620caee522c9e9b4d3114be6a4666a155f82a55a607beed) |
| 6 | 136389753 | 1496288965315983 | 2026-06-02 | 2026-08-28 | 88 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1496288965315983) · [share](https://app.gethookd.ai/share/ad/136389753?signature=c11710ed0494a2be2e0de04459119cb94adb1abe7eb43daeb71696d9f786eaca) |
| 7 | 136389610 | 1342423427761201 | 2026-06-02 | 2026-08-28 | 88 | 1 | Video | 28 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1342423427761201) · [share](https://app.gethookd.ai/share/ad/136389610?signature=56c0541108d5e5623da5490c5b074c2aa092c14d809ace13e980d09dec4e096b) |
| 8 | 136389489 | 1968037894586095 | 2026-06-02 | 2026-08-28 | 88 | 1 | Video | 33 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1968037894586095) · [share](https://app.gethookd.ai/share/ad/136389489?signature=ac4e07d23ab6dc2de08fdcd8da355a2f3a89b1cd771ba96003bc6ab12216f95f) |
| 9 | 136389222 | 973168308972800 | 2026-06-02 | 2026-08-28 | 88 | 1 | Video | 29 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=973168308972800) · [share](https://app.gethookd.ai/share/ad/136389222?signature=aec00b54d808b9636318d04258bc56d5564a596abc9743d8147da2428469d16b) |
| 10 | 133365908 | 1512627093723201 | 2026-06-02 | 2026-08-28 | 88 | 2 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1512627093723201) · [share](https://app.gethookd.ai/share/ad/133365908?signature=9dcf1b20c00296daa11240385f0e80116a4a46d480544bdc39348bff2de48080) |
| 11 | 133366209 | 1299502702267336 | 2026-06-02 | 2026-08-28 | 88 | 1 | Video | 58 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1299502702267336) · [share](https://app.gethookd.ai/share/ad/133366209?signature=0ca5e0fa91b3c32b412e2c5f223fc1b3f00404d25f776aa4b1263d2d5aae2fce) |
| 12 | 136388830 | 4632064777027243 | 2026-06-11 | 2026-09-05 | 87 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=4632064777027243) · [share](https://app.gethookd.ai/share/ad/136388830?signature=0a77fef64e45b6d4ac4246726ac7cc62af7116ef20fd7376a56385dc6e44ce49) |
| 13 | 133364769 | 993861203283367 | 2026-06-02 | 2026-08-25 | 85 | 2 | Video | 28 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=993861203283367) · [share](https://app.gethookd.ai/share/ad/133364769?signature=a283a599732fc527e7395c8730a00d8dfe95a8bf92b57ae53b10033b2e921989) |
| 14 | 136389438 | 2804497349943273 | 2026-06-11 | 2026-09-01 | 83 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2804497349943273) · [share](https://app.gethookd.ai/share/ad/136389438?signature=5c304e8ba36424a23d89f3d6006dbc4d4b4df49870ba1eb414dd7788768c1d49) |
| 15 | 136389687 | 1581020036920692 | 2026-06-11 | 2026-08-29 | 80 | 1 | Video | 31 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1581020036920692) · [share](https://app.gethookd.ai/share/ad/136389687?signature=c4bb5359676c09c0fecb5d53654ff09439ab842da4d61b30364ab8523e2bb228) |
| 16 | 136389533 | 930528683362670 | 2026-06-11 | 2026-08-29 | 80 | 1 | Video | 35 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=930528683362670) · [share](https://app.gethookd.ai/share/ad/136389533?signature=098116e8bc41e977e86da0a4f671318187afb182da5c3aa7d227a3f14f716296) |
| 17 | 136389068 | 872796652569192 | 2026-06-11 | 2026-08-29 | 80 | 1 | Video | 34 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=872796652569192) · [share](https://app.gethookd.ai/share/ad/136389068?signature=f32a83a0e9ded3693b704eaeafe4400277060e3c0fea4c000fbc52df28441b07) |
| 18 | 136388894 | 1521797796024377 | 2026-06-11 | 2026-08-29 | 80 | 1 | Video | 37 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1521797796024377) · [share](https://app.gethookd.ai/share/ad/136388894?signature=46517ce85e33409baa60557815e288889bfda8f6760ac9e2f2776fa956cbd167) |
| 19 | 133365701 | 1010280781725300 | 2026-06-19 | 2026-08-28 | 71 | 1 | Video | 55 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1010280781725300) · [share](https://app.gethookd.ai/share/ad/133365701?signature=cd14a4f1ee52ab596fe2b659af29e0e62a9f3cf1cacc838a5c3b2738945fc55e) |
| 20 | 136389340 | 1318752613771504 | 2026-06-11 | 2026-08-18 | 69 | 1 | Video | 20 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1318752613771504) · [share](https://app.gethookd.ai/share/ad/136389340?signature=b82275ea25b1cf5ec9480291b359002737514826365b9a62e39d68bbeb5b8aad) |
| 21 | 136388877 | 994215023537195 | 2026-06-11 | 2026-08-18 | 69 | 1 | Video | 28 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=994215023537195) · [share](https://app.gethookd.ai/share/ad/136388877?signature=a1045f9e95cb8ba5ce31f522148a1cf95c52adca92abb15182a51b2a446ce79d) |
| 22 | 133364552 | 1543010393881104 | 2026-06-11 | 2026-08-18 | 69 | 1 | Video | 44 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1543010393881104) · [share](https://app.gethookd.ai/share/ad/133364552?signature=c9276584f76e85d70ed7c0097d31c2b7869af1231c40c0badc3e55f6fb5c3420) |
| 23 | 133365600 | 1766472621172612 | 2026-06-24 | 2026-08-25 | 63 | 3 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1766472621172612) · [share](https://app.gethookd.ai/share/ad/133365600?signature=bb14f9662c96dca701e442e18fa35b03c166c12048a54f7031a467ed15e17746) |
| 24 | 136389591 | 1066970162680624 | 2026-07-14 | 2026-09-13 | 62 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=1066970162680624) · [share](https://app.gethookd.ai/share/ad/136389591?signature=128cd56fd17e7e8a903e836c0cf0b5c189b3741af4552317c8634e5e4f5b99d3) |
| 25 | 136389420 | 1691830705272900 | 2026-07-14 | 2026-09-13 | 62 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=1691830705272900) · [share](https://app.gethookd.ai/share/ad/136389420?signature=b4bd0943bb42dadf73930e0adc9471cce81ae2ebae200c824951393d5ebb7fef) |
| 26 | 133365473 | 999736119482810 | 2026-07-08 | 2026-09-06 | 61 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=999736119482810) · [share](https://app.gethookd.ai/share/ad/133365473?signature=7b9c1794fd12ce5847523511908d34956487944e2bc88b1ce295d96cd6d4e4b4) |
| 27 | 136390020 | 2077394283142508 | 2026-07-15 | 2026-09-13 | 61 | 1 | Video | 44 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=2077394283142508) · [share](https://app.gethookd.ai/share/ad/136390020?signature=43bb77aaa3c476ecf22789be539884c3fee2eddcb6c104f3548e5ea8d2d92c24) |
| 28 | 136389104 | 1676213717010450 | 2026-07-14 | 2026-09-11 | 60 | 1 | Video | 35 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=1676213717010450) · [share](https://app.gethookd.ai/share/ad/136389104?signature=1ecadaac32b0bdd55b98ec59ff226bbe5c93891e210e84c5b55b8f89b64c7940) |
| 29 | 133364629 | 2001712173822376 | 2026-07-14 | 2026-09-08 | 57 | 1 | Video | 23 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=2001712173822376) · [share](https://app.gethookd.ai/share/ad/133364629?signature=0530d830f92dffb62a94265dd10345ea5918f64fae33b78cb05a491ae0aa5869) |
| 30 | 133367207 | 1594458228914070 | 2026-07-15 | 2026-09-08 | 56 | 1 | Video | 28 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=1594458228914070) · [share](https://app.gethookd.ai/share/ad/133367207?signature=b47c01bfa1259f78870365b6b958cd4a043befa65cda3a07e49dcb169288e357) |
| 31 | 139561518 | 1579050700440920 | 2026-08-07 | 2026-09-30 | 55 | 1 | Video | 15 s | Pick a colour. Watch. | F-Knappheit/Farbe, C | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1579050700440920) · [share](https://app.gethookd.ai/share/ad/139561518?signature=d72502de7ed81824137c8820524649b47c851f8f179ee0259df83195cfb82f6a) |
| 32 | 145443324 | 1580155590567953 | 2026-08-14 | 2026-10-06 | 54 | 1 | Bild | – | Who Wins In Your House? | F-Knappheit/Farbe, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1580155590567953) · [share](https://app.gethookd.ai/share/ad/145443324?signature=dcc958d471b824d4955e38f9f510a978f9185438d4c38c0fa24d621c143bc2c1) |
| 33 | 136390163 | 1403615265199738 | 2026-08-05 | 2026-09-26 | 53 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/pleene-easyrest-duvet-2in1 | [Meta](https://www.facebook.com/ads/library/?id=1403615265199738) · [share](https://app.gethookd.ai/share/ad/136390163?signature=ff1ff4abc16e413a14c23bb444456994041fa290e32bddbe607ea607fab00b7a) |
| 34 | 136390181 | 1063023972882365 | 2026-08-05 | 2026-09-26 | 53 | 1 | Video | 14 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/pleene-easyrest-duvet-2in1 | [Meta](https://www.facebook.com/ads/library/?id=1063023972882365) · [share](https://app.gethookd.ai/share/ad/136390181?signature=2fdc26262981f9072ba82f5682e47a5620d78569385993916b71e885a5d79578) |
| 35 | 136390102 | 2895295140832235 | 2026-08-05 | 2026-09-26 | 53 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/pleene-easyrest-duvet-2in1 | [Meta](https://www.facebook.com/ads/library/?id=2895295140832235) · [share](https://app.gethookd.ai/share/ad/136390102?signature=78f1f5aadcae3c3d74e711f9e7ca88c0d5b4d6230c9e5a41c0f4575ef345eb7e) |
| 36 | 136390115 | 1327742962471077 | 2026-08-05 | 2026-09-26 | 53 | 1 | Video | 47 s (ffprobe; GetHooked-Wert 0) | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/pleene-easyrest-duvet-2in1 | [Meta](https://www.facebook.com/ads/library/?id=1327742962471077) · [share](https://app.gethookd.ai/share/ad/136390115?signature=91338eddf0fd7c5c6e99bec2de2d2d10580cee04e026d1bfc549387830c039f2) |
| 37 | 139561522 | 1690354895371776 | 2026-08-07 | 2026-09-28 | 53 | 1 | Video | 15 s | Pick a colour. Watch. | F-Knappheit/Farbe, C | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1690354895371776) · [share](https://app.gethookd.ai/share/ad/139561522?signature=f7641e4d380301b573b3c68bc2dcbeb4e08fda6c51cf27cdc64e0e30b9bc690c) |
| 38 | 133364652 | 1717741949560876 | 2026-07-19 | 2026-09-06 | 50 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1717741949560876) · [share](https://app.gethookd.ai/share/ad/133364652?signature=3bce78c603fdc40bc2f876d127c117f6e3ecefc1b2029c7d164e965d7787b99a) |
| 39 | 141368634 | 1738762820597769 | 2026-08-09 | 2026-09-26 | 49 | 1 | DCO | 2 Bild(er) | n/a | n/a (Platzhalter-Text) | https://pleene.com/products/pleene-easyrest-duvet-2in1 | [Meta](https://www.facebook.com/ads/library/?id=1738762820597769) · [share](https://app.gethookd.ai/share/ad/141368634?signature=c2c7bf617728ea211ec7f459a13c57ebc1141d48f5378fe963924cde98ed3845) |
| 40 | 141368639 | 1830971708059484 | 2026-08-09 | 2026-09-26 | 49 | 1 | DCO | 2 Bild(er) | n/a | n/a (Platzhalter-Text) | https://pleene.com/products/pleene-easyrest-duvet-2in1 | [Meta](https://www.facebook.com/ads/library/?id=1830971708059484) · [share](https://app.gethookd.ai/share/ad/141368639?signature=1b542dbd1ba1767b702af28724d05557991cf43421578ccfd2210617ecbd9f30) |
| 41 | 136389628 | 2289223651817793 | 2026-07-14 | 2026-08-29 | 47 | 1 | Video | 36 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=2289223651817793) · [share](https://app.gethookd.ai/share/ad/136389628?signature=08211bdb4738a024f9e37e390f2a7ec81628596d83a49d7959b936cbb2851ba5) |
| 42 | 136389475 | 1665276507873808 | 2026-07-14 | 2026-08-29 | 47 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=1665276507873808) · [share](https://app.gethookd.ai/share/ad/136389475?signature=cdc7d706bda49dc938b2a6871442b97f2e3a1f120750351323d137c356bdfcd7) |
| 43 | 133364874 | 1512948843284329 | 2026-07-14 | 2026-08-29 | 47 | 1 | Video | 28 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=1512948843284329) · [share](https://app.gethookd.ai/share/ad/133364874?signature=5b1bb0e877a87a848e1f50f7bcbe7c11e488ca10bae121b3901685104e3a4848) |
| 44 | 136389963 | 1975714743107781 | 2026-07-24 | 2026-09-07 | 46 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1975714743107781) · [share](https://app.gethookd.ai/share/ad/136389963?signature=ece4db923d57198a5151d1cd2e21396c13ec79db716555abe397462ef8962a5f) |
| 45 | 136389207 | 1360910075371475 | 2026-07-24 | 2026-09-07 | 46 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1360910075371475) · [share](https://app.gethookd.ai/share/ad/136389207?signature=844180bb66aa9304988005e499dddccd67e0d85c2b7582d0562f417acd761e43) |
| 46 | 133365601 | 2152532702347311 | 2026-07-24 | 2026-09-07 | 46 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2152532702347311) · [share](https://app.gethookd.ai/share/ad/133365601?signature=ec205502f9e72e259496ee70ddd78e15ba076201839bbf0eff5d26c0b231c300) |
| 47 | 145443328 | 1073865045064863 | 2026-08-14 | 2026-09-28 | 46 | 1 | Bild | – | Who Wins In Your House? | F-Knappheit/Farbe, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1073865045064863) · [share](https://app.gethookd.ai/share/ad/145443328?signature=21756bad808a39b6810c19993600f40703e80b8975676dee769dc8dbcec4b43d) |
| 48 | 136389776 | 1740546437293601 | 2026-07-25 | 2026-09-07 | 45 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1740546437293601) · [share](https://app.gethookd.ai/share/ad/136389776?signature=9158f77f53ff8622fe97eab093e2545056713d85ba1de6a8ee4fa03606e2c18a) |
| 49 | 133366096 | 1414405543861664 | 2026-07-25 | 2026-09-07 | 45 | 2 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1414405543861664) · [share](https://app.gethookd.ai/share/ad/133366096?signature=c06237ca01ee6ed72a16462ff01cac43005a1ab4f89eeaed96142109f0fc9a18) |
| 50 | 136389520 | 1015735761224024 | 2026-07-31 | 2026-09-13 | 45 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1015735761224024) · [share](https://app.gethookd.ai/share/ad/136389520?signature=2b4c313c9f13dbf9db2e95adb3a2da0887210aa0b619f76ff9b15da4a26c64c9) |
| 51 | 136389084 | 1080197727891601 | 2026-07-31 | 2026-09-13 | 45 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1080197727891601) · [share](https://app.gethookd.ai/share/ad/136389084?signature=1b273f39ab752ca515108c16cac3b68b295aeed37552af28ba5905b0d7fc9549) |
| 52 | 136388548 | 2500141900410353 | 2026-07-31 | 2026-09-13 | 45 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2500141900410353) · [share](https://app.gethookd.ai/share/ad/136388548?signature=915e7379c59ae4aac6fb8723801e6d65bcd7b8c06c6512e771c9c31053c7c0be) |
| 53 | 136390051 | 1334119675550930 | 2026-08-03 | 2026-09-14 | 43 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1334119675550930) · [share](https://app.gethookd.ai/share/ad/136390051?signature=1c30cec8be3c15a4acdf04695ce040044adb2b36e8f1bbc11f1078e6518bcbce) |
| 54 | 136389942 | 2123958901533050 | 2026-07-31 | 2026-09-10 | 42 | 1 | Video | 96 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2123958901533050) · [share](https://app.gethookd.ai/share/ad/136389942?signature=5b0ab8b6147634fe5ba59e7d5acd104c90c5e8bdab91aa519a0d58a56b44bc1f) |
| 55 | 133366390 | 3601686853322008 | 2026-07-31 | 2026-09-10 | 42 | 1 | Video | 93 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=3601686853322008) · [share](https://app.gethookd.ai/share/ad/133366390?signature=ecde9e74513dad2031f2bd469a99705a6d0f2ce5a80fa2dd87e5dd32826c96ea) |
| 56 | 133365906 | 27620340294226557 | 2026-07-07 | 2026-08-16 | 41 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=27620340294226557) · [share](https://app.gethookd.ai/share/ad/133365906?signature=c64065035922fdd423ddd8b5b0cd60cabc90f8d129fba4b4fc62789e15402034) |
| 57 | 136389304 | 1050230747984526 | 2026-08-02 | 2026-09-11 | 41 | 1 | DCO | 2 Bild(er) | n/a | n/a (Platzhalter-Text) | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=1050230747984526) · [share](https://app.gethookd.ai/share/ad/136389304?signature=b65c9eed879926d0c738c75b1397f3abf138f2f88244e3ad04e8c099a6c2ba36) |
| 58 | 136389919 | 1972881356696916 | 2026-07-31 | 2026-09-08 | 40 | 1 | Video | 96 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1972881356696916) · [share](https://app.gethookd.ai/share/ad/136389919?signature=9a8734e956cb63dc41f673a79fcee27d00ef4625977c1ffbcc195f753d9ed381) |
| 59 | 136389274 | 1736838194026177 | 2026-07-11 | 2026-08-18 | 39 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1736838194026177) · [share](https://app.gethookd.ai/share/ad/136389274?signature=70a971cce68498575e6e1dd4bf2c9438b78aca76dd8f51d77e5f6a2763236aef) |
| 60 | 133365808 | 1303214664920128 | 2026-07-11 | 2026-08-18 | 39 | 1 | Video | 47 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1303214664920128) · [share](https://app.gethookd.ai/share/ad/133365808?signature=15b6e1a3c8a418beb25d32067334e8d8d264d18ae4837cfeac4cc0f12daa9478) |
| 61 | 133365161 | 2227307328108597 | 2026-07-11 | 2026-08-18 | 39 | 1 | Video | 23 s (ffprobe; GetHooked-Wert 0) | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2227307328108597) · [share](https://app.gethookd.ai/share/ad/133365161?signature=b75ad7165b9d660353b9df4605d37bde235366e4db54a92fdd9d707d0b779873) |
| 62 | 136389325 | 1560968608716430 | 2026-08-01 | 2026-09-08 | 39 | 1 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1560968608716430) · [share](https://app.gethookd.ai/share/ad/136389325?signature=dccb7cf41edcf7a89b6a48af5d49b9018e32ca1ac99139c5fae285acf9999ad5) |
| 63 | 136389356 | 1023198490702848 | 2026-08-01 | 2026-09-08 | 39 | 1 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1023198490702848) · [share](https://app.gethookd.ai/share/ad/136389356?signature=8d74e7d04420262d8389ac1b419eb51d321f8faf45b361282d6e91c56851d7a4) |
| 64 | 136388564 | 1023015420539475 | 2026-08-01 | 2026-09-08 | 39 | 1 | Video | 25 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1023015420539475) · [share](https://app.gethookd.ai/share/ad/136388564?signature=67f01175964a40230987822c9e1161e3beb456135bcec1b0fa6158d754646ec1) |
| 65 | 145443340 | 937322868660942 | 2026-08-14 | 2026-09-19 | 37 | 1 | Bild | – | What bed have you got? | F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=937322868660942) · [share](https://app.gethookd.ai/share/ad/145443340?signature=16e5742c4db77b5e7bba52412bce46bd9e1b48b5cf894d96de978e05ba364722) |
| 66 | 145443282 | 1642682714085833 | 2026-08-14 | 2026-09-19 | 37 | 1 | Bild | – | What bed have you got? | F-Einwand/Kaufhilfe | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1642682714085833) · [share](https://app.gethookd.ai/share/ad/145443282?signature=45cc510ddcc3d6aac86f8012d62c00861c0c39924b6db4256e8aefcf120c073d) |
| 67 | 133364609 | 1345015433804123 | 2026-07-14 | 2026-08-18 | 36 | 1 | Video | 28 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1345015433804123) · [share](https://app.gethookd.ai/share/ad/133364609?signature=ab9f5717822ef51de1bf47331063c1ff48f5072af4e439017ae53e09ab7a1e93) |
| 68 | 136389504 | 1671870660573049 | 2026-07-24 | 2026-08-27 | 35 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1671870660573049) · [share](https://app.gethookd.ai/share/ad/136389504?signature=122cdd016c5d7113a18e33863d11a6c5a561d599760c2923a75e2fbf80f5f729) |
| 69 | 136388826 | 954938290974827 | 2026-08-05 | 2026-09-08 | 35 | 1 | Video | 40 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=954938290974827) · [share](https://app.gethookd.ai/share/ad/136388826?signature=c6b6f69a3cae71df05f6bd6578441137c72b3bf2fcb32cfc0023e4065e1fe099) |
| 70 | 133365812 | 3016531412024707 | 2026-08-05 | 2026-09-08 | 35 | 1 | Video | 34 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest-pdp | [Meta](https://www.facebook.com/ads/library/?id=3016531412024707) · [share](https://app.gethookd.ai/share/ad/133365812?signature=1b4a3e59dcdfc2b084e49e2b79fa8a8a684927eaa3616f9b93ce7e7617dd4e35) |
| 71 | 157492487 | 1040663415485965 | 2026-08-25 | 2026-09-28 | 35 | 1 | Bild | – | Now In Super King | F-Neuheit/Größe, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1040663415485965) · [share](https://app.gethookd.ai/share/ad/157492487?signature=a83fedfddd2d15a5863f04bfae129c9d383a04bbb8cc7f316e48cbdfd42fdf1a) |
| 72 | 157492481 | 1078447658460536 | 2026-08-25 | 2026-09-28 | 35 | 1 | Bild | – | Now In Super King | F-Neuheit/Größe, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1078447658460536) · [share](https://app.gethookd.ai/share/ad/157492481?signature=a79cf57b76a32952a090c568ce8b11f833b15216715725029ac7b78610ea41fa) |
| 73 | 157492463 | 1368027478281052 | 2026-08-25 | 2026-09-28 | 35 | 1 | Bild | – | Now In Super King | F-Neuheit/Größe, A | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1368027478281052) · [share](https://app.gethookd.ai/share/ad/157492463?signature=bad25402e96a220a3d79c6ce2124749d566abc055806c41e318d90758916a5cc) |
| 74 | 136388767 | 1949202019085906 | 2026-07-30 | 2026-09-01 | 34 | 2 | Video | 14 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1949202019085906) · [share](https://app.gethookd.ai/share/ad/136388767?signature=97d96f2921c1b25152af4dc91ed46fccf9a1c70124de90538c0526f62e51bd04) |
| 75 | 133366194 | 1063953986594114 | 2026-07-30 | 2026-09-01 | 34 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1063953986594114) · [share](https://app.gethookd.ai/share/ad/133366194?signature=44ce7b40d4f15dbede03f2cbe1531d66548ea6cff76058b79d13941cc4a75800) |
| 76 | 136387989 | 1585337489714739 | 2026-08-03 | 2026-09-05 | 34 | 1 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | [Meta](https://www.facebook.com/ads/library/?id=1585337489714739) · [share](https://app.gethookd.ai/share/ad/136387989?signature=96d70f22ff88d4436342e04a314e5522779b9537036dc9784053c5073265e14a) |
| 77 | 136387870 | 2279493866157814 | 2026-08-03 | 2026-09-05 | 34 | 1 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | [Meta](https://www.facebook.com/ads/library/?id=2279493866157814) · [share](https://app.gethookd.ai/share/ad/136387870?signature=6eece85a7ee2f1ac893e2ee6f6a7821b78b760cb0ca81c8f3de60313718e0f3f) |
| 78 | 136387930 | 1047129641511978 | 2026-08-03 | 2026-09-05 | 34 | 1 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | [Meta](https://www.facebook.com/ads/library/?id=1047129641511978) · [share](https://app.gethookd.ai/share/ad/136387930?signature=a6099e0ba62a4f57b7350400fcb0630471569e598bd3ee0c21cf0b4fa1d96cdd) |
| 79 | 133365157 | 1080490354405286 | 2026-08-03 | 2026-09-05 | 34 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1080490354405286) · [share](https://app.gethookd.ai/share/ad/133365157?signature=157666fe61e360203be9f6cc0683d39ec77be4c1ca4e52f0d891a5c4cae5ec3e) |
| 80 | 136388113 | 2125708415039670 | 2026-08-04 | 2026-09-05 | 33 | 1 | Bild | – | Never lift your mattress again. | C, E | https://pleene.com/products/zipsheet-us | [Meta](https://www.facebook.com/ads/library/?id=2125708415039670) · [share](https://app.gethookd.ai/share/ad/136388113?signature=179aca7330eb6a46cdc54004783388cca0f21913a8e5335a00daaf97ab73c374) |
| 81 | 136390079 | 1003603455838091 | 2026-08-05 | 2026-09-06 | 33 | 1 | Video | 25 s (ffprobe; GetHooked-Wert 0) | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/pleene-easyrest-duvet-2in1 | [Meta](https://www.facebook.com/ads/library/?id=1003603455838091) · [share](https://app.gethookd.ai/share/ad/136390079?signature=17415b51b507421e4c28adf740d08df6eec086a70b1f87cb81fd8ffad8e7e640) |
| 82 | 136388651 | 1054588847286173 | 2026-08-01 | 2026-09-01 | 32 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1054588847286173) · [share](https://app.gethookd.ai/share/ad/136388651?signature=4ebe96e56befc58754e6608f4bdfab7a20edb8e890144bc65078bef00d687a90) |
| 83 | 133364896 | 1444482834179132 | 2026-08-04 | 2026-09-04 | 32 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1444482834179132) · [share](https://app.gethookd.ai/share/ad/133364896?signature=583a168fd68c4b76cd60ac6c5d5bb931332ffdbecbf3b418d515d4251dacc8be) |
| 84 | 172403395 | 1047122204596890 | 2026-09-05 | 2026-10-06 | 32 | 1 | Bild | – | NEW: Lavender Mist | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1047122204596890) · [share](https://app.gethookd.ai/share/ad/172403395?signature=32a90ebdcc05f257ecbde618aaae2b4b213c2b141a11e1c2568016a6d04c2153) |
| 85 | 172403399 | 1806555340498784 | 2026-09-05 | 2026-10-06 | 32 | 1 | Bild | – | NEW: Lavender Mist | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1806555340498784) · [share](https://app.gethookd.ai/share/ad/172403399?signature=633b9ced144a1ca4578a840282486695db353cfc109f6057fde09722940b670f) |
| 86 | 172403406 | 4500708943408046 | 2026-09-05 | 2026-10-06 | 32 | 1 | Bild | – | NEW: Lavender Mist | F-Knappheit/Farbe, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=4500708943408046) · [share](https://app.gethookd.ai/share/ad/172403406?signature=f03bfb314ad32fbcd30c11226ecdd5a1135ab35973faad99f4d19ed963db5cc1) |
| 87 | 133365280 | 27290663163969275 | 2026-07-19 | 2026-08-18 | 31 | 2 | Video | 40 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=27290663163969275) · [share](https://app.gethookd.ai/share/ad/133365280?signature=c2da9ec475935c65e23c4fbd9828a4f00840d7b9b26a82da67bacdc00af36186) |
| 88 | 136388605 | 1950197182309185 | 2026-07-30 | 2026-08-29 | 31 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1950197182309185) · [share](https://app.gethookd.ai/share/ad/136388605?signature=72d097c2019296b44f39542fc1be022f42d698c4c1717e91e841f297d6e7f257) |
| 89 | 136389732 | 2178372706066416 | 2026-07-31 | 2026-08-30 | 31 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2178372706066416) · [share](https://app.gethookd.ai/share/ad/136389732?signature=aa518563a2b7058ff8552d02be7e6408c2663474b3f57d2ad93d9cdbabc3057a) |
| 90 | 133366463 | 1746200703394058 | 2026-07-31 | 2026-08-30 | 31 | 1 | Bild | – | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1746200703394058) · [share](https://app.gethookd.ai/share/ad/133366463?signature=f560dc070fda4555f91beb8709864f8de605524cc88255a830124b9bbea9fcdf) |
| 91 | 145443320 | 1027409520213921 | 2026-08-14 | 2026-09-13 | 31 | 1 | Video | 47 s | Everyone said it. They were right. | F-Social-Proof, C | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1027409520213921) · [share](https://app.gethookd.ai/share/ad/145443320?signature=439640c36173f599b8515b7d30d7e8e4325c232d122781f0cd60a580062dd92d) |
| 92 | 163921094 | 2004939896876500 | 2026-08-27 | 2026-09-26 | 31 | 1 | Video | 26 s | Duvet & Cover In One | C | https://pleene.com/products/easyrest-everyday-duvet | [Meta](https://www.facebook.com/ads/library/?id=2004939896876500) · [share](https://app.gethookd.ai/share/ad/163921094?signature=a39f561bd389718001fe0486d7cc002b947dc3a469485419fdc85afb04a22171) |
| 93 | 133365704 | 2067781017145122 | 2026-07-24 | 2026-08-22 | 30 | 1 | Video | 14 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=2067781017145122) · [share](https://app.gethookd.ai/share/ad/133365704?signature=7d062de9aef165bead173b001df38d45bcc1cf0e0147afb5b9e065296a3f00d5) |
| 94 | 136389122 | 1560449009073304 | 2026-08-01 | 2026-08-30 | 30 | 1 | Video | 37 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1560449009073304) · [share](https://app.gethookd.ai/share/ad/136389122?signature=4c42c52810755c53ec9a838078ba5c71b2c7f36c17312550bcd6e0a64b71e00d) |
| 95 | 136388680 | 1630436858419591 | 2026-08-01 | 2026-08-30 | 30 | 1 | Video | 37 s | No More Fighting With Duvet Covers | C, B, F-Angebot | https://pleene.com/products/easyrest | [Meta](https://www.facebook.com/ads/library/?id=1630436858419591) · [share](https://app.gethookd.ai/share/ad/136388680?signature=c4d82b859d1af3f95383c02c86d66b0bf832dcdc94321bf6dd977737bb9ed251) |

Häufigste Enddaten (Abschalt-Wellen) inaktiver Ads: 2026-08-21 (34), 2026-09-17 (31), 2026-08-29 (31), 2026-08-28 (31), 2026-09-10 (28), 2026-08-18 (26), 2026-09-13 (25), 2026-09-19 (23).

### Vollinventar aktiv (137 Ads)

Sortierung: Block (Winner → Starker Kandidat → Neuer Test → Beobachten), dann Ranking-Wert absteigend.

| # | GetHooked-ID | Meta-ID | Start | Ende | Tage | Format | Länge | Headline | Primärtext | CTA | Plattformen | Landingpage | Score | used | Block | Angle | Produkt | Links |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 136388964 | 884267707299487 | 2026-06-11 | aktiv | 120 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=884267707299487) · [share](https://app.gethookd.ai/share/ad/136388964?signature=d0ff0d2a2536e91cfc3dacb7f3b055bf680241a71e3d485ea8d2c98436047966) |
| 2 | 136388847 | 1583232786477915 | 2026-06-11 | aktiv | 120 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1583232786477915) · [share](https://app.gethookd.ai/share/ad/136388847?signature=422777a4ae4663b915702dc330ccb3f999733ab57559e373f53beb6af24567f7) |
| 3 | 145443331 | 1440933327878495 | 2026-08-14 | aktiv | 56 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 2 | Winner | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1440933327878495) · [share](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) |
| 4 | 136389861 | 1642037860240117 | 2026-06-11 | aktiv | 120 | Video | 38 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 61 (Growing) | 1 | Winner | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1642037860240117) · [share](https://app.gethookd.ai/share/ad/136389861?signature=52dff4dac27abf45e6f9b062724b0d38f817b3ddcd8939d92684a863d31faaf8) |
| 5 | 133366534 | 1372761711494763 | 2026-08-03 | aktiv | 67 | Video | 93 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1372761711494763) · [share](https://app.gethookd.ai/share/ad/133366534?signature=ec7e21facd4f53244e7aacaf8002b409a7803a538b1d302bb66be766c52ef924) |
| 6 | 139561428 | 1034362836068724 | 2026-08-07 | aktiv | 63 | Video | 16 s | Hearth Red. Nearly gone. | → **T26** (Anhang) „Hearth Red is nearly sold out — and unlike most 'selling fast' claims,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1034362836068724) · [share](https://app.gethookd.ai/share/ad/139561428?signature=1eb14bdf7f1f4b278f8b5996d37204958181d02f07e10262e225457c7f9a49fd) |
| 7 | 139561410 | 1355121136744622 | 2026-08-07 | aktiv | 63 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1355121136744622) · [share](https://app.gethookd.ai/share/ad/139561410?signature=8993cc76f99c424613789bd7c6c9a9248d166b223587f503929e5077c7a435b2) |
| 8 | 139561491 | 1526037445508180 | 2026-08-07 | aktiv | 63 | Video | 16 s | Everyone's buying the blue one. | → **T19** (Anhang) „Everyone's buying it in Coastal Blue — and stock is running low. The E…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 86 (Optimized) | 1 | Winner | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1526037445508180) · [share](https://app.gethookd.ai/share/ad/139561491?signature=5cbb3a8ead3ed2e5b41ef6ef544d7498f90d8427b339e0ba7304f344c120fb43) |
| 9 | 163921089 | 1609110380938946 | 2026-08-27 | aktiv | 43 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1609110380938946) · [share](https://app.gethookd.ai/share/ad/163921089?signature=18918dab03620f19a44f0f4ae4aabab8d5f163dfaa3984dcc8e6e691c7301c1d) |
| 10 | 145443318 | 1474663121347221 | 2026-08-14 | aktiv | 56 | Video | 50 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 74 (Growing) | 1 | Winner | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1474663121347221) · [share](https://app.gethookd.ai/share/ad/145443318?signature=be73a154548ac1fdbbec6cdf47867c12c72f8b288e40c2faaa6b1db18c69b49b) |
| 11 | 151025063 | 1369166828764339 | 2026-08-22 | aktiv | 48 | Video | 29 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 86 (Optimized) | 1 | Winner | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1369166828764339) · [share](https://app.gethookd.ai/share/ad/151025063?signature=6a64477f3dd49f4b0e862e714a6a052a0839cfe3382654d8e4902e827f95d481) |
| 12 | 168246678 | 1607904514111212 | 2026-08-29 | aktiv | 41 | Video | 27 s | Check This Before You Buy | → **T25** (Anhang) „Before you buy a coverless duvet, check three things: ✅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | F-Einwand/Kaufhilfe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1607904514111212) · [share](https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59) |
| 13 | 171191667 | 1583757549405276 | 2026-09-03 | aktiv | 36 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1583757549405276) · [share](https://app.gethookd.ai/share/ad/171191667?signature=b03cc4b1b86af6280d5edfa0028fe241e19fd20d3b3592e580dd3f576a92669d) |
| 14 | 168246686 | 2035183934551496 | 2026-08-29 | aktiv | 41 | Video | 27 s | Check This Before You Buy | → **T25** (Anhang) „Before you buy a coverless duvet, check three things: ✅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 86 (Optimized) | 1 | Winner | F-Einwand/Kaufhilfe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2035183934551496) · [share](https://app.gethookd.ai/share/ad/168246686?signature=a360c60671d85ebeec646d4238239e0ec57ba2d7b037d0bb4c8888b606378db0) |
| 15 | 172403389 | 1725326416267519 | 2026-09-05 | aktiv | 34 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1725326416267519) · [share](https://app.gethookd.ai/share/ad/172403389?signature=fc57a29e066c788034eca64a557143f0c3e0b71232ea5868d51df06e7536000f) |
| 16 | 172760571 | 1415553300514250 | 2026-09-06 | aktiv | 33 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 100 (Winning) | 1 | Winner | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1415553300514250) · [share](https://app.gethookd.ai/share/ad/172760571?signature=82cd0a698c2d4720c44c69a474abfa9e4e1f24189f59d7dd6d1f216aaf8e25b8) |
| 17 | 151025052 | 1363184622691769 | 2026-08-20 | aktiv | 50 | Bild | – | Everyone's buying the blue one. | → **T19** (Anhang) „Everyone's buying it in Coastal Blue — and stock is running low. The E…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 61 (Growing) | 1 | Winner | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1363184622691769) · [share](https://app.gethookd.ai/share/ad/151025052?signature=fa0ac684d0e23c918a286f4c72318a4110a6ecece18af70548ebdfc97ba1bc3e) |
| 18 | 169082912 | 2192690231462965 | 2026-08-31 | aktiv | 39 | Bild | – | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 74 (Growing) | 1 | Winner | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2192690231462965) · [share](https://app.gethookd.ai/share/ad/169082912?signature=4ab996ca26c1daf73d6ef9a482fc283fbce80f5ccef0bc6ead1abbcdb159c5e0) |
| 19 | 173307160 | 1770207397626174 | 2026-09-07 | aktiv | 32 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 81 (Optimized) | 1 | Winner | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1770207397626174) · [share](https://app.gethookd.ai/share/ad/173307160?signature=20a01e20e8d0bc5720968b8ee00d824e45a8e18af15aa506b60fd22b7789241f) |
| 20 | 174599778 | 2301727147248244 | 2026-09-09 | aktiv | 30 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 74 (Growing) | 1 | Winner | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2301727147248244) · [share](https://app.gethookd.ai/share/ad/174599778?signature=0f3b267681520755857f3c8967162b7f9b49eb9f935ce9ac83a4c94572252bc1) |
| 21 | 178749258 | 1750276626195989 | 2026-09-16 | aktiv | 23 | Bild | – | No Launderette Needed. Ever. | → **T38** (Anhang) „❄️ Your winter duvet shouldn't need a launderette.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | 81 (Optimized) | 1 | Starker Kandidat | A, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1750276626195989) · [share](https://app.gethookd.ai/share/ad/178749258?signature=26142585e8a79bd682cbb72cd7ae73d46e39dc00bb8ff65b79f19d32e5e4e2cb) |
| 22 | 178749251 | 1792003651846452 | 2026-09-16 | aktiv | 23 | Video | 34 s | Warm Enough For A British Winter | → **T29** (Anhang) „❄️ "You'll freeze under that in winter." Here's the honest answer: the…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | 81 (Optimized) | 1 | Starker Kandidat | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1792003651846452) · [share](https://app.gethookd.ai/share/ad/178749251?signature=f7a95b97af4df738359f0bc0b4a21bbd6f5508efef5391e097423762a823afc1) |
| 23 | 179476350 | 935523852471023 | 2026-09-17 | aktiv | 22 | Bild | – | Warm Enough For A British Winter | → **T29** (Anhang) „❄️ "You'll freeze under that in winter." Here's the honest answer: the…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | 81 (Optimized) | 1 | Starker Kandidat | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=935523852471023) · [share](https://app.gethookd.ai/share/ad/179476350?signature=929eaf7be4e50da7829743ff0e7ad0be30111ad47d7408608f8bb7fc89e7de17) |
| 24 | 178749254 | 1632682334866450 | 2026-09-16 | aktiv | 23 | Video | 35 s | Warm Enough For A British Winter | → **T29** (Anhang) „❄️ "You'll freeze under that in winter." Here's the honest answer: the…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | 70 (Growing) | 1 | Starker Kandidat | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1632682334866450) · [share](https://app.gethookd.ai/share/ad/178749254?signature=83a5eb4a50bf72fe2effb4d2ccd1e63703dc4357bed313215787c0765ffb300a) |
| 25 | 178749247 | 1337076731626722 | 2026-09-16 | aktiv | 23 | Video | 34 s | Warm Enough For A British Winter | → **T29** (Anhang) „❄️ "You'll freeze under that in winter." Here's the honest answer: the…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | 70 (Growing) | 1 | Starker Kandidat | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1337076731626722) · [share](https://app.gethookd.ai/share/ad/178749247?signature=ead4e820d252fbf4cb5f6f4bdc9ff97c3172308e95f7a04f5dde33677b0f12e5) |
| 26 | 180153186 | 1115810910797427 | 2026-09-18 | aktiv | 21 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 66 (Growing) | 1 | Starker Kandidat | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1115810910797427) · [share](https://app.gethookd.ai/share/ad/180153186?signature=3d665d4929718403a6c75e93b2efcb58f4e2d3ef6f4708e6759b79e45f7b2aa7) |
| 27 | 182988073 | 1307634398016532 | 2026-09-21 | aktiv | 18 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 72 (Growing) | 1 | Starker Kandidat | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1307634398016532) · [share](https://app.gethookd.ai/share/ad/182988073?signature=18244261546a933ac17b6d832e4abb5f9491a76500ae006902ed5c113947df05) |
| 28 | 182988043 | 29208178135432493 | 2026-09-24 | aktiv | 15 | Bild | – | Wash The Whole Comforter | → **T72** (Anhang) „Yes, the whole comforter goes right in the wash! The Pleene EasyRest™ …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 54 (Scaling) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=29208178135432493) · [share](https://app.gethookd.ai/share/ad/182988043?signature=474ac523034272536a305779503c22ea294092cc8bd3cc7b069288c8fe337071) |
| 29 | 185228767 | 947904747867427 | 2026-09-27 | aktiv | 12 | Video | 16 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 60 (Scaling) | 1 | Neuer Test | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=947904747867427) · [share](https://app.gethookd.ai/share/ad/185228767?signature=d4a01baf409b9ddc41f60bfabb36d11b1b0037cf0db9af90a7ff2251278f24be) |
| 30 | 185228766 | 1401480008764681 | 2026-09-27 | aktiv | 12 | Bild | – | NEW: Lavender Mist | → **T16** (Anhang) „NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyR…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 60 (Scaling) | 1 | Neuer Test | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1401480008764681) · [share](https://app.gethookd.ai/share/ad/185228766?signature=f4be2b097e5b58bb0f5013dc8e461a8cea74051b0e8dfd5a28059f540eaf99fb) |
| 31 | 185228755 | 1858016975363264 | 2026-09-27 | aktiv | 12 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 60 (Scaling) | 1 | Neuer Test | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1858016975363264) · [share](https://app.gethookd.ai/share/ad/185228755?signature=25ebc63a662bfe1309283139b99531554229712ec743d75253367e8f2956578d) |
| 32 | 193234279 | 28476177958733795 | 2026-10-01 | aktiv | 8 | Video | 93 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 44 (Scaling) | 2 | Neuer Test | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28476177958733795) · [share](https://app.gethookd.ai/share/ad/193234279?signature=13f6122c0c5d22eb8c8b6141c88c013e8051538391bd99bbd1f57e3f4702f207) |
| 33 | 182988114 | 1426446732803436 | 2026-09-24 | aktiv | 15 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 41 (Scaling) | 1 | Neuer Test | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1426446732803436) · [share](https://app.gethookd.ai/share/ad/182988114?signature=45373dfa7ccdf466516a711b6593e9207307858450c4d58f1857ebd0d9c95216) |
| 34 | 182988035 | 2320911822014129 | 2026-09-24 | aktiv | 15 | Bild | – | Fresh Bedding Made Easy | → **T37** (Anhang) „Nothing beats getting into a freshly made bed. Pleene EasyRest™ makes …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 41 (Scaling) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2320911822014129) · [share](https://app.gethookd.ai/share/ad/182988035?signature=7092f978c95adda0f69e7d8ee25f7a28d421bd5b83e9ec632c18a18ed9941b58) |
| 35 | 184134597 | 4249373995353335 | 2026-09-25 | aktiv | 14 | Video | 47 s | Never Wrestle A Duvet Cover Again | → **T39** (Anhang) „🐙 Every wash day, my duvet cover turns into an angry octopus. Eight co…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 41 (Scaling) | 1 | Neuer Test | C, A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4249373995353335) · [share](https://app.gethookd.ai/share/ad/184134597?signature=2b680d992f53e9489bd001330a9e608908df3f009b371ab2cf0e14275970f411) |
| 36 | 184134598 | 1772685790545501 | 2026-09-25 | aktiv | 14 | Bild | – | Mint Green Is Almost Gone | → **T54** (Anhang) „🎁 30% off + 2 FREE matching pillow cases. And Mint Green is almost gon…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 41 (Scaling) | 1 | Neuer Test | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1772685790545501) · [share](https://app.gethookd.ai/share/ad/184134598?signature=74028bdc9398943d1fa7b8f9149049962318fe3ebdf4bcecd5c613ee3875d422) |
| 37 | 193234275 | 931889339640196 | 2026-10-01 | aktiv | 8 | Video | 93 s | Never Wrestle A Duvet Cover Again | → **T39** (Anhang) „🐙 Every wash day, my duvet cover turns into an angry octopus. Eight co…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 52 (Scaling) | 1 | Neuer Test | C, A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=931889339640196) · [share](https://app.gethookd.ai/share/ad/193234275?signature=ffce5170bcd8108ccef8ec8fa356ebe88ee4788757813cf94c27b340e5ff2e63) |
| 38 | 193234221 | 2325762131511604 | 2026-10-01 | aktiv | 8 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 52 (Scaling) | 1 | Neuer Test | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2325762131511604) · [share](https://app.gethookd.ai/share/ad/193234221?signature=34d449a91191d816e5a91f7d690e2d93f52044d2af092704c3b3dece336abb59) |
| 39 | 193234215 | 1068343922634373 | 2026-10-01 | aktiv | 8 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 52 (Scaling) | 1 | Neuer Test | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1068343922634373) · [share](https://app.gethookd.ai/share/ad/193234215?signature=92968440b95005fe0fc1bf85409c9b3366e3ae8f6dbf240ce5448a242e85affb) |
| 40 | 193234214 | 2366124124211597 | 2026-10-01 | aktiv | 8 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 52 (Scaling) | 1 | Neuer Test | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2366124124211597) · [share](https://app.gethookd.ai/share/ad/193234214?signature=4c554cee5f2b53ee0a1c202d4fe10ee2f6cfb8b5f6e3a6b4936aab8a10f4eec3) |
| 41 | 193234278 | 1103531258742413 | 2026-10-01 | aktiv | 8 | Bild | – | NEW: Lavender Mist | → **T16** (Anhang) „NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyR…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 40 (Testing) | 1 | Neuer Test | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1103531258742413) · [share](https://app.gethookd.ai/share/ad/193234278?signature=2acfe25ae18b9ee3fd409e989a071bce595dea12e1dca232a03824238d38b557) |
| 42 | 200037058 | 2388197505255466 | 2026-10-05 | aktiv | 4 | Video | 16 s | Too Thin For Winter? Look Closer. | → **T53** (Anhang) „❄️ Too thin for winter? Look closer.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | B, A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2388197505255466) · [share](https://app.gethookd.ai/share/ad/200037058?signature=8b9260efa8d3e451a50636127320d32fc1789291c109321c5b496c3192bfb0e4) |
| 43 | 200037053 | 1833362664327699 | 2026-10-05 | aktiv | 4 | Video | 16 s | Too Thin For Winter? Look Closer. | → **T53** (Anhang) „❄️ Too thin for winter? Look closer.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | B, A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1833362664327699) · [share](https://app.gethookd.ai/share/ad/200037053?signature=a89d0ec9b5b673f5988345a774bf4a4f858e1b8996f1952670685df5ce8f602c) |
| 44 | 200037052 | 961172106430872 | 2026-10-05 | aktiv | 4 | Video | 73 s | The Spare Bed, Fresh For Every Guest | → **T57** (Anhang) „🛏️ The grandchildren are coming to stay this weekend, and the spare be…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | A, F-Gäste | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=961172106430872) · [share](https://app.gethookd.ai/share/ad/200037052?signature=ab0ea3d22bfd746992e616204067846b3fc4ad0b9794701144978049c326996a) |
| 45 | 200037051 | 2176522276563795 | 2026-10-05 | aktiv | 4 | Video | 16 s | Too Thin For Winter? Look Closer. | → **T53** (Anhang) „❄️ Too thin for winter? Look closer.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | B, A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2176522276563795) · [share](https://app.gethookd.ai/share/ad/200037051?signature=1f846d614d7ded11dca1363417ba6340f5e6bb0229af8a271a5f50fea944c262) |
| 46 | 200037049 | 4571329826520060 | 2026-10-05 | aktiv | 4 | Video | 80 s | The Dog Can Stay On The Bed | → **T55** (Anhang) „🐾 Bella sleeps on our bed every night. And nobody worries about it, be…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | A, F-Haustier | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4571329826520060) · [share](https://app.gethookd.ai/share/ad/200037049?signature=5045ba37ea51c2cd64846ac6342c368334f1f1b19a0b44769b33ca1012550c40) |
| 47 | 200037047 | 1818573935991907 | 2026-10-05 | aktiv | 4 | Video | 73 s | The Spare Bed, Fresh For Every Guest | → **T57** (Anhang) „🛏️ The grandchildren are coming to stay this weekend, and the spare be…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | A, F-Gäste | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1818573935991907) · [share](https://app.gethookd.ai/share/ad/200037047?signature=17fe05b65ba5af7f7b6a0e07d401ba8e36e2ca9af6ea7f68938dcf67525578db) |
| 48 | 200037045 | 1251620417158236 | 2026-10-05 | aktiv | 4 | Video | 80 s | The Dog Can Stay On The Bed | → **T55** (Anhang) „🐾 Bella sleeps on our bed every night. And nobody worries about it, be…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | A, F-Haustier | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1251620417158236) · [share](https://app.gethookd.ai/share/ad/200037045?signature=9dbc6af8a2932afed3e5a991ab6f9ad12e1fef2910914283018eeff2b95baea8) |
| 49 | 200037044 | 2217517888813082 | 2026-10-05 | aktiv | 4 | Video | 47 s | When Did You Last Wash Your Duvet? | → **T56** (Anhang) „🛏️ If a guest asked you when you last washed your duvet, not the cover…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 22 (Testing) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2217517888813082) · [share](https://app.gethookd.ai/share/ad/200037044?signature=a19c242b496cbc5e92ce74a3a3303e782e4f5f6f23b854194823c49f93fb0260) |
| 50 | 200490698 | 4427668754123793 | 2026-10-06 | aktiv | 3 | Bild | – | NEW: Lavender Mist | → **T16** (Anhang) „NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyR…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 13 (Testing) | 2 | Neuer Test | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4427668754123793) · [share](https://app.gethookd.ai/share/ad/200490698?signature=545ba781a548a5c01d329f2fd0013f8c17445f4fe55be65e34bbea4cb49766dc) |
| 51 | 200490726 | 2479370542555841 | 2026-10-06 | aktiv | 3 | Bild | – | Fresh Bedding Made Easy | → **T37** (Anhang) „Nothing beats getting into a freshly made bed. Pleene EasyRest™ makes …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 12 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2479370542555841) · [share](https://app.gethookd.ai/share/ad/200490726?signature=115b524a7494fc7321eeae317f8c27392d4975dd61a417a7abb8ca8b737a684c) |
| 52 | 200490719 | 1099152986192830 | 2026-10-06 | aktiv | 3 | Video | 23 s | Ditch The Duvet Cover | → **T69** (Anhang) „Still using a separate duvet cover? There’s another way. Pleene EasyRe…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 12 (Testing) | 1 | Neuer Test | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1099152986192830) · [share](https://app.gethookd.ai/share/ad/200490719?signature=02b20c37beecbaad1d44b7e74cd81762006aa203ca85a92692a4fce5b3aa9e84) |
| 53 | 200490716 | 2233952628001235 | 2026-10-06 | aktiv | 3 | Video | 44 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 12 (Testing) | 1 | Neuer Test | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2233952628001235) · [share](https://app.gethookd.ai/share/ad/200490716?signature=f9af223b680c0ee04bd5687c44ba0fd8ca69eace21b5373ed6b6f893022689ff) |
| 54 | 200490712 | 1570785790996577 | 2026-10-06 | aktiv | 3 | Video | 27 s | Check This Before You Buy | → **T25** (Anhang) „Before you buy a coverless duvet, check three things: ✅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 12 (Testing) | 1 | Neuer Test | F-Einwand/Kaufhilfe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1570785790996577) · [share](https://app.gethookd.ai/share/ad/200490712?signature=5ca96434dc1391452bf61216cdc94bffb3d3b8ab283563c1354672fbd689d547) |
| 55 | 200490708 | 1410624373895542 | 2026-10-06 | aktiv | 3 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 12 (Testing) | 1 | Neuer Test | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1410624373895542) · [share](https://app.gethookd.ai/share/ad/200490708?signature=c478fee5f2f2b1906248ac292415fd4e4fb6b49899a564cd74f30be3cf28ac09) |
| 56 | 200490706 | 3697076843791050 | 2026-10-06 | aktiv | 3 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 12 (Testing) | 1 | Neuer Test | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3697076843791050) · [share](https://app.gethookd.ai/share/ad/200490706?signature=bf8fb3d07c078c72fd1dd3c635f84c09d6efe02037bea42b6f0c348469448635) |
| 57 | 200490701 | 2558876794610991 | 2026-10-06 | aktiv | 3 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 12 (Testing) | 1 | Neuer Test | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2558876794610991) · [share](https://app.gethookd.ai/share/ad/200490701?signature=af04268440606b4ede2605c8f08f88b62eaaee7acf8bbd6c6b33990e392b96e2) |
| 58 | 200490657 | 1088262300260108 | 2026-10-06 | aktiv | 3 | Video | 30 s | Say Goodbye to Duvet Cover Hassle | → **T45** (Anhang) „No more stuffing, buttoning or fighting with duvet cover corners. Plee…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 12 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1088262300260108) · [share](https://app.gethookd.ai/share/ad/200490657?signature=14e9cab282a8e5334823ebd0fe803836a252fcd8cf045e8e22111a5867c33ff8) |
| 59 | 200490656 | 941633032037665 | 2026-10-06 | aktiv | 3 | Video | 13 s | The Easiest Bed Upgrade | Pleene's EasyRest™ Comforter is one fluffy piece: no duvet cover to wrestle on, easily washable, and feels amazing. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter?trybe=532dbd48 | 12 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=941633032037665) · [share](https://app.gethookd.ai/share/ad/200490656?signature=9b9fd72ba4d964a239aa279407b823b1686d57f783845a835d07793d5157d2b6) |
| 60 | 200490655 | 4392590044384955 | 2026-10-06 | aktiv | 3 | Video | 51 s | The Bedding Upgrade Is Here | → **T67** (Anhang) „Still doing bedding the old-fashioned way? Pleene EasyRest™ makes fres…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 12 (Testing) | 1 | Neuer Test | C, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4392590044384955) · [share](https://app.gethookd.ai/share/ad/200490655?signature=7d24527061b5c2c8f21d9243b2a93c078b438788a757590a49fc3e5bc7294145) |
| 61 | 200490654 | 1704721577299375 | 2026-10-06 | aktiv | 3 | Video | 25 s | Say Goodbye to Duvet Cover Hassle | → **T45** (Anhang) „No more stuffing, buttoning or fighting with duvet cover corners. Plee…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter?trybe=769e7716 | 12 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1704721577299375) · [share](https://app.gethookd.ai/share/ad/200490654?signature=47a2ea43f6061e1680dc6c3acfbfbfe49dda22c6028484f0a15fd6b2c5413750) |
| 62 | 183445651 | 1640984024127964 | 2026-09-24 | aktiv | 15 | Bild | – | Skip the Cover | → **T62** (Anhang) „Clean bedding shouldn't feel like a wrestling match. Pleene EasyRest™ …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 2 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1640984024127964) · [share](https://app.gethookd.ai/share/ad/183445651?signature=3af2be1a313fcc4887a0cd71ed59cf6121bb5f75f33757760103514ce37b379e) |
| 63 | 185228772 | 1609404564015528 | 2026-09-27 | aktiv | 12 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 2 | Neuer Test | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1609404564015528) · [share](https://app.gethookd.ai/share/ad/185228772?signature=b8b59977a1223802de6aa2310ed361654df4253dc41d5ac727fe2d89dc343ef4) |
| 64 | 186893844 | 2052923595354457 | 2026-09-29 | aktiv | 10 | Bild | – | Bedding Without The Struggle | → **T44** (Anhang) „No more hunting for corners or wrestling fabric into place. Pleene Eas…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 2 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2052923595354457) · [share](https://app.gethookd.ai/share/ad/186893844?signature=f56cef38bdf4271c06d03206fdc5607e7f702ce5a602485401736777e23c53de) |
| 65 | 182988042 | 28437506889250706 | 2026-09-24 | aktiv | 15 | Bild | – | No Assembly Required | Skip the stuffing, shaking and corner hunting. Pleene EasyRest™ is a machine-washable comforter with no separate cover to wrestle with. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28437506889250706) · [share](https://app.gethookd.ai/share/ad/182988042?signature=e713dbcee072e6217acb230e04b0dfb8c7114c149d8c98626c040da7bef3f891) |
| 66 | 182988040 | 2515261675637941 | 2026-09-24 | aktiv | 15 | Bild | – | Clean Bedding, Made Easier | kip the laundromat and dry cleaner. EasyRest™ is fully machine washable and designed to wash right at home, so keeping your whole comforter fresh is simpler. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2515261675637941) · [share](https://app.gethookd.ai/share/ad/182988040?signature=70c523c1f926d7fd461c615515849a5b4da5e7a7cd0b682c0335da480ffd657a) |
| 67 | 182988039 | 2506169333225327 | 2026-09-24 | aktiv | 15 | Bild | – | Fewer Steps. Fresher Bed. | Wash. Dry. Back on the bed. EasyRest™ cuts out the extra steps of traditional bedding with one machine-washable comforter and built-in cover. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2506169333225327) · [share](https://app.gethookd.ai/share/ad/182988039?signature=527dd4c916d39ab9e6336ae3da5dfb03d8f6e255525d6dcab66494f2f427a37d) |
| 68 | 182988037 | 1640153464440559 | 2026-09-24 | aktiv | 15 | Bild | – | Skip the Cover | → **T62** (Anhang) „Clean bedding shouldn't feel like a wrestling match. Pleene EasyRest™ …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1640153464440559) · [share](https://app.gethookd.ai/share/ad/182988037?signature=b7d4bc753ea2e96af174d564c3492d5adf7a481ed1267e58644c73a559c03796) |
| 69 | 182988034 | 1509916224516076 | 2026-09-24 | aktiv | 15 | Bild | – | Simplify Your Bedding Routine | Clean bedding doesn’t need a complicated routine. Pleene EasyRest™ is a machine-washable comforter you can wash, dry and put straight back on. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1509916224516076) · [share](https://app.gethookd.ai/share/ad/182988034?signature=14dbc2129486bcabd193e665ddf4838458be05e7bf9dce3dfc69bf4aacede6cc) |
| 70 | 182988033 | 1974838589853602 | 2026-09-24 | aktiv | 15 | Bild | – | Skip The Duvet Cover | A duvet cover means more stuffing, tying and wrestling every time you change the bed. EasyRest™ combines the comforter and cover into one washable piece. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1974838589853602) · [share](https://app.gethookd.ai/share/ad/182988033?signature=02e7cdc360791bd35b8ddcd944fe2a094efad14b6918e50c6eab16a385c9fc59) |
| 71 | 182988032 | 1109103628745298 | 2026-09-24 | aktiv | 15 | Bild | – | Wash. Dry. Done. | Why spend laundry day stuffing a comforter back into its cover? The Pleene EasyRest™ Comforter gives you an all-in-one, machine-washable routine. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1109103628745298) · [share](https://app.gethookd.ai/share/ad/182988032?signature=fbd107f7a97ed551302eb2de90f0c8a58bf341d7335b7f01b6a069b61410c80b) |
| 72 | 182988031 | 2312946976208616 | 2026-09-24 | aktiv | 15 | Bild | – | Straight Back On The Bed | Get to the best part of laundry day faster. Wash your Pleene EasyRest™ Comforter, dry it fast, and lay it straight back on the bed to enjoy that fresh-bed feeling. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2312946976208616) · [share](https://app.gethookd.ai/share/ad/182988031?signature=929ab2700d8d2ff4c55371cf11ebef82c019bb414b81a2990302dfd8d9efd784) |
| 73 | 182988029 | 956768364140489 | 2026-09-24 | aktiv | 15 | Bild | – | Take The Work Out Of Bedding | Clean bedding shouldn’t feel like a workout. Pleene EasyRest™ is machine washable, with no separate cover to stuff, shake, or zip. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C, E | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=956768364140489) · [share](https://app.gethookd.ai/share/ad/182988029?signature=7000d6337b257185b3d04740a740841f3c2734266cacfabe1aaee79e136c9e57) |
| 74 | 182988027 | 1789453228862663 | 2026-09-24 | aktiv | 15 | Bild | – | Warmth Without The Weight | Cozy doesn’t have to mean heavy. EasyRest™ combines lightweight comfort with temperature regulation to keep you comfortable through every season. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1789453228862663) · [share](https://app.gethookd.ai/share/ad/182988027?signature=9321cc0e170e1a68f3b963e4904fb45eec5f2859a60a5d4abc63285b6a3fcde3) |
| 75 | 182988024 | 1104976622267074 | 2026-09-24 | aktiv | 15 | Bild | – | Wash More Than The Sheets | You wash your sheets when they need a refresh. Why not your comforter too? Pleene EasyRest™ is fully machine washable, with no separate cover needed. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1104976622267074) · [share](https://app.gethookd.ai/share/ad/182988024?signature=eabd40dff7802187b5f63741ae4ea3e7cc7a4cd1ac89cf64689be1a3177bdf9f) |
| 76 | 184134616 | 4380603895511872 | 2026-09-25 | aktiv | 14 | Video | 48 s | Never Wrestle A Duvet Cover Again | → **T39** (Anhang) „🐙 Every wash day, my duvet cover turns into an angry octopus. Eight co…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C, A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4380603895511872) · [share](https://app.gethookd.ai/share/ad/184134616?signature=30d5fa9687840e415704fb7e19f5a1ef4dd204c7e06fbb62833ac631d02fe94a) |
| 77 | 184134607 | 2292800994824018 | 2026-09-25 | aktiv | 14 | Video | 48 s | Never Wrestle A Duvet Cover Again | → **T39** (Anhang) „🐙 Every wash day, my duvet cover turns into an angry octopus. Eight co…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C, A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2292800994824018) · [share](https://app.gethookd.ai/share/ad/184134607?signature=19e12d9ef3e8461ef2c7fa995df7cd451f2608fc590135b4f248dc4336d2e56d) |
| 78 | 185228774 | 850494884758362 | 2026-09-27 | aktiv | 12 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=850494884758362) · [share](https://app.gethookd.ai/share/ad/185228774?signature=6459312b29b8e015b00623a9c8704115adbc89d90290a12a406708f7e07ceba3) |
| 79 | 185228773 | 2789047968155632 | 2026-09-27 | aktiv | 12 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2789047968155632) · [share](https://app.gethookd.ai/share/ad/185228773?signature=a25a1c0dc9c693ccb2b54cced73f43f031683b0b29560a7a1a6bae916c224838) |
| 80 | 185228765 | 1107581421667412 | 2026-09-27 | aktiv | 12 | Bild | – | Now In Super King | → **T27** (Anhang) „Our most requested size is finally here: the Pleene EasyRest in Super …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Neuheit/Größe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1107581421667412) · [share](https://app.gethookd.ai/share/ad/185228765?signature=fdc1176605c0f19ad51f2626b448a5fdfb307d0143360d07311941417feb5d0b) |
| 81 | 185228764 | 3754498381550275 | 2026-09-27 | aktiv | 12 | Video | 27 s | Check This Before You Buy | → **T25** (Anhang) „Before you buy a coverless duvet, check three things: ✅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Einwand/Kaufhilfe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3754498381550275) · [share](https://app.gethookd.ai/share/ad/185228764?signature=c703896014750ef26ae392d8460d22d78a412a986b4bb954473b7a82371145bf) |
| 82 | 185395501 | 4386478151596961 | 2026-09-28 | aktiv | 11 | Video | 9 s | Pleene | → **T37** (Anhang) „Nothing beats getting into a freshly made bed. Pleene EasyRest™ makes …“ | SHOP_NOW (Text n/a) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4386478151596961) · [share](https://app.gethookd.ai/share/ad/185395501?signature=015f1978dac5f9d276bb167b0564e2fe687605d8c9ad005f1b15479977650936) |
| 83 | 186893864 | 1196771192793545 | 2026-09-29 | aktiv | 10 | DCO | 3 Bild(er) | n/a | n/a (leer) | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | n/a (kein Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1196771192793545) · [share](https://app.gethookd.ai/share/ad/186893864?signature=c4d30ed8926495e9042192d8622fb23ae265cf0b993d757bbe63f57af5595106) |
| 84 | 186893878 | 28612939431667546 | 2026-09-29 | aktiv | 10 | Bild | – | Bedding Made For Your Routine | A fresh bed shouldn’t mean waiting for a helping hand. Pleene EasyRest™ combines the duvet and cover into one lightweight, machine-washable piece, so you can change your bed all by yourself. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28612939431667546) · [share](https://app.gethookd.ai/share/ad/186893878?signature=f232a426903d049b7b06b46c06d250fb7eea59242595dbbbfb87042d99c66827) |
| 85 | 186893875 | 2350297945720190 | 2026-09-29 | aktiv | 10 | Bild | – | Your Bed. Your Way. | → **T68** (Anhang) „Still doing things your way? Pleene EasyRest™ makes it easier to keep …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2350297945720190) · [share](https://app.gethookd.ai/share/ad/186893875?signature=eb76cbb5770c4d86cb5e4bb7bf79451829587405bd54863dd53422787d2c7971) |
| 86 | 186893873 | 1400490411791512 | 2026-09-29 | aktiv | 10 | Bild | – | Meet The One-Piece Comforter | Tried, trusted, and loved by hundreds of customers, Pleene makes changing the bed alone simpler. With a lightweight, machine-washable duvet and built-in cover, you can leave the bedding struggle behind. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | F-Social-Proof, F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1400490411791512) · [share](https://app.gethookd.ai/share/ad/186893873?signature=6e5233b7a44d6f4c0b6241fe5a5dfd8bc67078473f1ca4dfa8733b675916b722) |
| 87 | 186893869 | 1096087780074941 | 2026-09-29 | aktiv | 10 | Bild | – | Fresh Bed, Fewer Steps | Still want to make your own bed? Pleene EasyRest™ keeps the duvet and cover together in one lightweight piece, so there’s less to handle when it’s time to wash and remake your bed. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1096087780074941) · [share](https://app.gethookd.ai/share/ad/186893869?signature=b35e84823f3c3e06bdd64e526557f5aa8adc0cf618dd1681d566efefe923a169) |
| 88 | 186893867 | 1744189879967996 | 2026-09-29 | aktiv | 10 | Bild | – | A Duvet That Works For You | Keep changing your bedding by yourself, without the extra fuss. Pleene EasyRest™ combines the duvet and cover into one simple piece that’s easy to fit and care for. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1744189879967996) · [share](https://app.gethookd.ai/share/ad/186893867?signature=427fec70c06030c12582ea7afc5367a9381e9977011adcea03ef8367788f4ba2) |
| 89 | 186893862 | 1122560766807410 | 2026-09-29 | aktiv | 10 | Bild | – | Bedding Without The Struggle | → **T44** (Anhang) „No more hunting for corners or wrestling fabric into place. Pleene Eas…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1122560766807410) · [share](https://app.gethookd.ai/share/ad/186893862?signature=a82b35565236b229024dfb64fb1fb681e1e300d1decba6dac35e25bd8dafacf4) |
| 90 | 186893861 | 1108416845124866 | 2026-09-29 | aktiv | 10 | Bild | – | One Piece. Less To Handle. | What if your bedding could do more, with less to handle? Pleene EasyRest™ combines the duvet and cover into one lightweight piece, delivering temperature-regulating comfort with less fuss. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1108416845124866) · [share](https://app.gethookd.ai/share/ad/186893861?signature=1c5e7c9a1a97f705b6efeb5f2fe85bde75fd83702387d3c01f9eae4b94e2b14d) |
| 91 | 186893859 | 1740917367195794 | 2026-09-29 | aktiv | 10 | Bild | – | Bedding That Fits Your Schedule | Clean bedding shouldn’t have to wait. Pleene EasyRest™ lets you wash the whole comforter at home, air dry it in 2 hours, and put it back on when you’re ready. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | A, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1740917367195794) · [share](https://app.gethookd.ai/share/ad/186893859?signature=b98601908ab59abfba07fc1c1081e6a491558c128c090114c0218409fb4dceea) |
| 92 | 186893846 | 1092854683130854 | 2026-09-29 | aktiv | 10 | Bild | – | Skip The Cover. Keep The Comfort. | → **T66** (Anhang) „No more finding corners. No more fighting fabric. Pleene EasyRest™ com…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1092854683130854) · [share](https://app.gethookd.ai/share/ad/186893846?signature=caad060c8e8ab36651b2536e28a6cef64fce2c0c70b442162689b11ac79d0ef1) |
| 93 | 186893837 | 28819204317704017 | 2026-09-29 | aktiv | 10 | Bild | – | Keep Making Your Own Bed | → **T60** (Anhang) „A fresh bed can still be part of your own routine. Pleene EasyRest™ co…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28819204317704017) · [share](https://app.gethookd.ai/share/ad/186893837?signature=296de22f294544b5a6e1de4329a707b9ab8c8d754343b48b762174f85a621bcb) |
| 94 | 186893831 | 4537475009834373 | 2026-09-29 | aktiv | 10 | Bild | – | Skip The Cover. Keep The Comfort. | → **T66** (Anhang) „No more finding corners. No more fighting fabric. Pleene EasyRest™ com…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4537475009834373) · [share](https://app.gethookd.ai/share/ad/186893831?signature=7a72439f549f6691a92e5c861625f174cc926bc15ca0e02bd6d03876a27cc6b9) |
| 95 | 186893814 | 1759745871934283 | 2026-09-29 | aktiv | 10 | Bild | – | Your Routine, Made Simpler | → **T64** (Anhang) „Keep your routine. Skip the duvet cover struggle. Pleene EasyRest™ tak…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C, F-Selbstständigkeit im Alter | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1759745871934283) · [share](https://app.gethookd.ai/share/ad/186893814?signature=8bd9162f3bfd33faf85979f4605208fc571e1affbdb578c78e5e8cac4f9df0ee) |
| 96 | 190288319 | 1650102630028747 | 2026-09-30 | aktiv | 9 | Bild | – | A Simpler Way To Change The Bed | → **T71** (Anhang) „Why wrestle with a separate duvet cover? Pleene EasyRest™ keeps the du…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1650102630028747) · [share](https://app.gethookd.ai/share/ad/190288319?signature=729f0bc268e9a52e0c55703bcfd9467503c62b1ee1d8fcb35f0a6610a2f3db7f) |
| 97 | 190288311 | 28870324805925641 | 2026-09-30 | aktiv | 9 | Bild | – | Bedding Without The Struggle | → **T44** (Anhang) „No more hunting for corners or wrestling fabric into place. Pleene Eas…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28870324805925641) · [share](https://app.gethookd.ai/share/ad/190288311?signature=516e1093da353991ffedcb490ec607edb228c6ef1f12611c429fc7f6c0a744c5) |
| 98 | 189550275 | 1697353005429136 | 2026-09-30 | aktiv | 9 | Bild | – | Pleene | Keep your bedding routine in your own hands. Pleene EasyRest™ is one lightweight, machine-washable piece, ready to go from wash to bed. | SHOP_NOW (Text n/a) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1697353005429136) · [share](https://app.gethookd.ai/share/ad/189550275?signature=e2841af4c3309f1f54a47962f542b0d928f5b10afef23bdb312b9555f7e1f404) |
| 99 | 189550269 | 2239984750193672 | 2026-09-30 | aktiv | 9 | Bild | – | Pleene | You can still take care of your own bed. Pleene EasyRest™ makes the job simpler with one easy-to-handle piece that goes straight from the wash back to bed in just 2 hours. | SHOP_NOW (Text n/a) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2239984750193672) · [share](https://app.gethookd.ai/share/ad/189550269?signature=f3ebac77a9aabd296cb1e960812c63aa60881f30e0da69bded7fc73cec4371e1) |
| 100 | 189550267 | 1845735359934868 | 2026-09-30 | aktiv | 9 | Bild | – | Pleene | → **T71** (Anhang) „Why wrestle with a separate duvet cover? Pleene EasyRest™ keeps the du…“ | SHOP_NOW (Text n/a) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1845735359934868) · [share](https://app.gethookd.ai/share/ad/189550267?signature=0ae93d7c42293d935614c14ae39cce8ebc82b4d76b07db17850a7cfb68f38e5f) |
| 101 | 193234224 | 1614086653522933 | 2026-10-01 | aktiv | 8 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 1 (Testing) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1614086653522933) · [share](https://app.gethookd.ai/share/ad/193234224?signature=e67f0112dff4be83367fd2663a38a3c667a76a33044371dae7cb5e0307b1035b) |
| 102 | 193234219 | 4170969413201905 | 2026-10-01 | aktiv | 8 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 1 (Testing) | 1 | Neuer Test | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4170969413201905) · [share](https://app.gethookd.ai/share/ad/193234219?signature=0cb8964e6ba84cfd7298793d4bb26527250a2d845375dcbc5de0b9fc4c82562e) |
| 103 | 193234218 | 1114220797783359 | 2026-10-01 | aktiv | 8 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 1 (Testing) | 1 | Neuer Test | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1114220797783359) · [share](https://app.gethookd.ai/share/ad/193234218?signature=3870fec0fed270d728da178501d4d67c9e13c536497ef821674e8f3e9c30953b) |
| 104 | 193234216 | 1078627058473158 | 2026-10-02 | aktiv | 7 | Video | 16 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/pages/tb-6 | 1 (Testing) | 1 | Neuer Test | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1078627058473158) · [share](https://app.gethookd.ai/share/ad/193234216?signature=60e2dc530fac13782e5f82c44abb08606f4acb8db2a48f6580a4f67b8d2e303d) |
| 105 | 200037063 | 1667265245004008 | 2026-10-05 | aktiv | 4 | Video | 82 s | The Dog Can Stay On The Bed | → **T55** (Anhang) „🐾 Bella sleeps on our bed every night. And nobody worries about it, be…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | A, F-Haustier | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1667265245004008) · [share](https://app.gethookd.ai/share/ad/200037063?signature=59e1350bb940afa8ce2ef4db6bc9f0dc9c3d58b5363f4541de87c32b08c94beb) |
| 106 | 200037062 | 1426769122930670 | 2026-10-05 | aktiv | 4 | Video | 46 s | When Did You Last Wash Your Duvet? | → **T56** (Anhang) „🛏️ If a guest asked you when you last washed your duvet, not the cover…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1426769122930670) · [share](https://app.gethookd.ai/share/ad/200037062?signature=cda1bc0bd9028c69d9fba9351c6e6030713ed82bd1d77fc8a1574dafccc5ec75) |
| 107 | 200037061 | 1056794434059905 | 2026-10-05 | aktiv | 4 | Video | 46 s | When Did You Last Wash Your Duvet? | → **T56** (Anhang) „🛏️ If a guest asked you when you last washed your duvet, not the cover…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1056794434059905) · [share](https://app.gethookd.ai/share/ad/200037061?signature=0567af9a9eaa403fac9aabda031e164b44e4c540386667d1dc31c6c13838d758) |
| 108 | 200037059 | 1762566964862159 | 2026-10-05 | aktiv | 4 | Video | 74 s | The Spare Bed, Fresh For Every Guest | → **T57** (Anhang) „🛏️ The grandchildren are coming to stay this weekend, and the spare be…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | A, F-Gäste | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1762566964862159) · [share](https://app.gethookd.ai/share/ad/200037059?signature=59009cf51aaea1c606c359bf3dde2a7411fd0a4e972af70643b9fad86da60902) |
| 109 | 200490725 | 1598917498396809 | 2026-10-06 | aktiv | 3 | Bild | – | Wash The Whole Comforter | → **T72** (Anhang) „Yes, the whole comforter goes right in the wash! The Pleene EasyRest™ …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1598917498396809) · [share](https://app.gethookd.ai/share/ad/200490725?signature=67a10c5447fc7a3f8b569d83dfdc87c2601d377c0332e160872fa4f4e059ff1f) |
| 110 | 200490724 | 1488098906488814 | 2026-10-06 | aktiv | 3 | Bild | – | Your Routine, Made Simpler | → **T64** (Anhang) „Keep your routine. Skip the duvet cover struggle. Pleene EasyRest™ tak…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C, F-Selbstständigkeit im Alter | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1488098906488814) · [share](https://app.gethookd.ai/share/ad/200490724?signature=1567b21782ab0caddb1ff07fb11120d7672fb131b518752e7470ef2b72b7247f) |
| 111 | 200490723 | 1478232800908923 | 2026-10-06 | aktiv | 3 | Bild | – | The Comforter That Does It All | → **T65** (Anhang) „No cover. No corners to find. No stuffing required. Pleene EasyRest™ C…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1478232800908923) · [share](https://app.gethookd.ai/share/ad/200490723?signature=2e878d2a1eb5ff26136f4a2e83dcb09f424a5e3d8b59e961f3a1802dbbd9232b) |
| 112 | 200490722 | 1103563399362311 | 2026-10-06 | aktiv | 3 | Video | 28 s | A Smarter Way To Do Bedding | → **T61** (Anhang) „Bedding shouldn't be harder than it needs to be. Pleene EasyRest™ comb…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1103563399362311) · [share](https://app.gethookd.ai/share/ad/200490722?signature=dd70cdeb1b3f44685b65dd999b089fa20ba19c1b6db90d019468210a9539d0a1) |
| 113 | 200490721 | 2373725086706676 | 2026-10-06 | aktiv | 3 | Video | 51 s | The Bedding Upgrade Is Here | → **T67** (Anhang) „Still doing bedding the old-fashioned way? Pleene EasyRest™ makes fres…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2373725086706676) · [share](https://app.gethookd.ai/share/ad/200490721?signature=8697f9fa84603c6c5fe39198bba6510a3c6efe060e8c12de0cac95d04e13450e) |
| 114 | 200490720 | 1660322526104618 | 2026-10-06 | aktiv | 3 | Bild | – | Your Bed. Your Way. | → **T68** (Anhang) „Still doing things your way? Pleene EasyRest™ makes it easier to keep …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1660322526104618) · [share](https://app.gethookd.ai/share/ad/200490720?signature=ba2af6dc6e4e320ef5b15b27078c4635dda547216aef3cdbec06294ee1c182e7) |
| 115 | 200490718 | 969394622234742 | 2026-10-06 | aktiv | 3 | Video | 23 s | Bedding Made for Independence | → **T70** (Anhang) „Why wait for someone else to help with your bedding? Pleene EasyRest™ …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=969394622234742) · [share](https://app.gethookd.ai/share/ad/200490718?signature=38b5623f18087b0df4c2c1716eb5005dc8644f32545bafb73badcec66bf77774) |
| 116 | 200490714 | 2178788646402978 | 2026-10-06 | aktiv | 3 | Video | 30 s | Say Goodbye to Duvet Cover Hassle | → **T45** (Anhang) „No more stuffing, buttoning or fighting with duvet cover corners. Plee…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2178788646402978) · [share](https://app.gethookd.ai/share/ad/200490714?signature=627ca4dcd8cf81ffbbe8928084c30d078545b5271aa95e2c5093eb36261092a5) |
| 117 | 200490709 | 965754332621763 | 2026-10-06 | aktiv | 3 | Bild | – | Keep Making Your Own Bed | → **T60** (Anhang) „A fresh bed can still be part of your own routine. Pleene EasyRest™ co…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=965754332621763) · [share](https://app.gethookd.ai/share/ad/200490709?signature=2d7f89c9b03596be2e52285bbb9a8d93f265460fdb50363beccf2776ff75a276) |
| 118 | 200490660 | 2352066545542430 | 2026-10-06 | aktiv | 3 | Video | 23 s | Bedding Made for Independence | → **T70** (Anhang) „Why wait for someone else to help with your bedding? Pleene EasyRest™ …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | F-Selbstständigkeit im Alter, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2352066545542430) · [share](https://app.gethookd.ai/share/ad/200490660?signature=2bdf462077564f674b5c865f99ba0e9e930f29ccb8d973a094d72ef52a3ed322) |
| 119 | 200490658 | 4710162855976658 | 2026-10-06 | aktiv | 3 | Video | 28 s | A Smarter Way To Do Bedding | → **T61** (Anhang) „Bedding shouldn't be harder than it needs to be. Pleene EasyRest™ comb…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4710162855976658) · [share](https://app.gethookd.ai/share/ad/200490658?signature=c8f37e5af06714882e4c6e6120919336cdce17ce51bcf0f206bbd74faf16c421) |
| 120 | 200036996 | 38866239393024310 | 2026-10-06 | aktiv | 3 | Video | 23 s | Ditch The Duvet Cover | → **T69** (Anhang) „Still using a separate duvet cover? There’s another way. Pleene EasyRe…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=38866239393024310) · [share](https://app.gethookd.ai/share/ad/200036996?signature=945bd160e24141ec27cd570f40308c72484012330c424f8889416548c509a965) |
| 121 | 200490661 | 2272066053740371 | 2026-10-07 | aktiv | 2 | Bild | – | Skip The  Duvet Cover | Take the duvet-cover chore out of their routine. Pleene EasyRest™ combines the duvet and cover in one, so there’s no separate cover to iron, wrestle into place or fasten. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Neuer Test | D, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2272066053740371) · [share](https://app.gethookd.ai/share/ad/200490661?signature=114722e2aec9d0a68a974913b4cf9f5a2ba74b9f5bf1d0b762ad013438a493dc) |
| 122 | 182988115 | 1611031707100333 | 2026-09-22 | aktiv | 17 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 41 (Scaling) | 2 | Beobachten | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1611031707100333) · [share](https://app.gethookd.ai/share/ad/182988115?signature=c904e1bd40a381849b8f0118dd2be30ffc212b955d2b15bfb326e5c357b2996f) |
| 123 | 182988119 | 2366375294199061 | 2026-09-21 | aktiv | 18 | Bild | – | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 60 (Scaling) | 1 | Beobachten | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2366375294199061) · [share](https://app.gethookd.ai/share/ad/182988119?signature=21211ffe2868f914fece4b782664bd0021c0949ff05775c0fd48c6017351de06) |
| 124 | 180646058 | 1579069737037989 | 2026-09-20 | aktiv | 19 | Bild | – | Warm Enough For A British Winter | → **T29** (Anhang) „❄️ "You'll freeze under that in winter." Here's the honest answer: the…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | 41 (Scaling) | 1 | Beobachten | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1579069737037989) · [share](https://app.gethookd.ai/share/ad/180646058?signature=88fbfe70a305d101d6f1ae039dd8bb482d03568d53926741876d8462e5ca3355) |
| 125 | 182988091 | 1562707309236010 | 2026-09-23 | aktiv | 16 | Bild | – | What bed have you got? | → **T17** (Anhang) „Not sure which size? It's easier than duvet shopping usually is: Singl…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 41 (Scaling) | 1 | Beobachten | F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1562707309236010) · [share](https://app.gethookd.ai/share/ad/182988091?signature=d38f60d9788af1b85ef236ca2bc85df5cb3de0c4ac38b8240791e6ace576727a) |
| 126 | 182988041 | 27616218781386469 | 2026-09-23 | aktiv | 16 | Bild | – | The Comforter That Does It All | → **T65** (Anhang) „No cover. No corners to find. No stuffing required. Pleene EasyRest™ C…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 41 (Scaling) | 1 | Beobachten | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=27616218781386469) · [share](https://app.gethookd.ai/share/ad/182988041?signature=656021e045b4ec00d24fe1a994c294542e9ff36636166d025b70fab06f7efb14) |
| 127 | 136390001 | 2687410064986677 | 2026-06-11 | aktiv | 120 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2687410064986677) · [share](https://app.gethookd.ai/share/ad/136390001?signature=1765b0a55cd4792881cb510eac2152901fc1b2187c69ce5fdd22929e5f2e6553) |
| 128 | 133366116 | 1687513282572901 | 2026-06-15 | aktiv | 116 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1687513282572901) · [share](https://app.gethookd.ai/share/ad/133366116?signature=a2afe366ec4a13b6ab93d2e4edce9c7275c8292acd57172af7d5455a8b4dc87d) |
| 129 | 177443533 | 1025780787101985 | 2026-09-15 | aktiv | 24 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 1 (Testing) | 2 | Beobachten | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1025780787101985) · [share](https://app.gethookd.ai/share/ad/177443533?signature=b49e6756d0f788df305d7d64b0ecdf567538d748bde051b17a21130afda3e2c3) |
| 130 | 173929415 | 1080653068157794 | 2026-09-08 | aktiv | 31 | Bild | – | Myth vs Truth 🛏️ | → **T22** (Anhang) „Myth: Changing the bed has to be a struggle. 🛏️…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1080653068157794) · [share](https://app.gethookd.ai/share/ad/173929415?signature=f0e1ccce27a60346510cf79fea8c03c205a409770a77094a35c9f7a4e9a2b927) |
| 131 | 178011633 | 1098100946061801 | 2026-09-15 | aktiv | 24 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1098100946061801) · [share](https://app.gethookd.ai/share/ad/178011633?signature=48c8e7e35f6375127cf561739916180953154da9ef203df6bb5f45775709f748) |
| 132 | 177443532 | 2894384197604810 | 2026-09-15 | aktiv | 24 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2894384197604810) · [share](https://app.gethookd.ai/share/ad/177443532?signature=0e0c69630ceb34cd905e1db339879cccd638942624cbd67020f4cfb3c8937ccb) |
| 133 | 182988111 | 1084737137379454 | 2026-09-21 | aktiv | 18 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1084737137379454) · [share](https://app.gethookd.ai/share/ad/182988111?signature=3946cc0bedfae59cd046d6e8d5c8ada264c91345b8d4ccb1192ee02716cb1b00) |
| 134 | 182988108 | 1224279553236944 | 2026-09-21 | aktiv | 18 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1224279553236944) · [share](https://app.gethookd.ai/share/ad/182988108?signature=c18f0e428c7a9f0555d06c32f36d4378439a94eaa30173163756f73045560493) |
| 135 | 182988112 | 2138510413448166 | 2026-09-23 | aktiv | 16 | Bild | – | What bed have you got? | → **T17** (Anhang) „Not sure which size? It's easier than duvet shopping usually is: Singl…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2138510413448166) · [share](https://app.gethookd.ai/share/ad/182988112?signature=e637d1aa88032bb3e6f40a107860add2023c5f81431ec94ddb40f889cad2579f) |
| 136 | 182988109 | 1650784179985323 | 2026-09-23 | aktiv | 16 | Bild | – | What bed have you got? | → **T17** (Anhang) „Not sure which size? It's easier than duvet shopping usually is: Singl…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | 1 (Testing) | 1 | Beobachten | F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1650784179985323) · [share](https://app.gethookd.ai/share/ad/182988109?signature=8a1a3bb47f8f0c47a3b8176d48503e7b6803273f62a7295f1b74fe1848bd06f2) |
| 137 | 182988038 | 2162602794330262 | 2026-09-23 | aktiv | 16 | Bild | – | Simplify Your Bedding Routine | No stuffing. No tying. No adjusting a separate cover. EasyRest™ goes straight back on the bed, making bed-making feel less like a project. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | 1 (Testing) | 1 | Beobachten | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2162602794330262) · [share](https://app.gethookd.ai/share/ad/182988038?signature=3b83966def7d239d3f8f898327a0d424f41581509f344934902a9eaf4f852074) |

### Vollinventar inaktiv (555 Ads, Start ab 2026-04-08)

Sortierung: Startdatum absteigend. Score bei allen inaktiven Ads n/a (von GetHooked nicht geliefert).

| # | GetHooked-ID | Meta-ID | Start | Ende | Tage | Format | Länge | Headline | Primärtext | CTA | Plattformen | Landingpage | Score | used | Block | Angle | Produkt | Links |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 193234277 | 943243035064922 | 2026-10-01 | 2026-10-04 | 4 | Bild | – | When Did You Last Wash The Duvet? | → **T33** (Anhang) „🧺 Be honest: when did you last wash the duvet you're about to spend al…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=943243035064922) · [share](https://app.gethookd.ai/share/ad/193234277?signature=77ae63f144efe3984006b368cc0904cd9c41e7a7c6e5d22091a64ab95d8f32af) |
| 2 | 193234273 | 2100922640555492 | 2026-10-01 | 2026-10-06 | 6 | Bild | – | NEW: Lavender Mist | → **T16** (Anhang) „NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyR…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2100922640555492) · [share](https://app.gethookd.ai/share/ad/193234273?signature=0ba2f670cf75a2cea80f69a0f1d518096f384fc05de8fe37422c55254a2856d1) |
| 3 | 190288325 | 1348489960694867 | 2026-09-30 | 2026-10-05 | 6 | Bild | – | Fewer Steps To A Fresh Bed | No stuffing, shaking or wrestling with a separate cover. Pleene EasyRest™ combines the duvet and cover into one machine-washable piece. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1348489960694867) · [share](https://app.gethookd.ai/share/ad/190288325?signature=5fb631c87cf69dc85e89d8b703b981cd94e212c894b87ecb72970ca5523d2b38) |
| 4 | 190288324 | 1124276960537017 | 2026-09-30 | 2026-10-06 | 7 | Bild | – | Skip The Duvet Cover Fuss | Skip the fiddly bits and keep your bedding routine in your own hands. Pleene EasyRest™ combines the duvet and cover into one lightweight, machine-washable piece, so there’s less to handle on wash day. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1124276960537017) · [share](https://app.gethookd.ai/share/ad/190288324?signature=48aa562c5319cf72520957009999b67df783221b6bb58928f7e9f3e92219e0b3) |
| 5 | 190288318 | 1067252816111108 | 2026-09-30 | 2026-10-04 | 5 | Bild | – | Less To Handle. More Independence. | → **T63** (Anhang) „Keep the routine, just make it simpler. Pleene EasyRest™ combines the …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1067252816111108) · [share](https://app.gethookd.ai/share/ad/190288318?signature=4b7f8a3d253d34ff53a70de87acb2846ec4495551f4ab28bebaa04b1289d150a) |
| 6 | 190288250 | 977688892023326 | 2026-09-30 | 2026-10-04 | 5 | Bild | – | Yes, It Fits Your Machine | → **T32** (Anhang) „🧺 "Does a Double REALLY fit in a normal 7kg washing machine?"…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=977688892023326) · [share](https://app.gethookd.ai/share/ad/190288250?signature=ab039581e4288805e3058d4430104d7505f2a62784a0d55a714226526b00cbd8) |
| 7 | 189550279 | 947126441804190 | 2026-09-30 | 2026-10-04 | 5 | Bild | – | Pleene | → **T63** (Anhang) „Keep the routine, just make it simpler. Pleene EasyRest™ combines the …“ | SHOP_NOW (Text n/a) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=947126441804190) · [share](https://app.gethookd.ai/share/ad/189550279?signature=e531d4180cb84f6914c0848fce5d8471ae2f19ca3576ce52a18cbae0568a4aea) |
| 8 | 189550274 | 1111778964682657 | 2026-09-30 | 2026-10-06 | 7 | Bild | – | Pleene | Keep the fresh-bed feeling without waiting for a helping hand. Pleene EasyRest™ combines the duvet and cover into one lightweight piece, so there’s less to handle on wash day. | SHOP_NOW (Text n/a) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Selbstständigkeit im Alter, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1111778964682657) · [share](https://app.gethookd.ai/share/ad/189550274?signature=d9914bd38c801d34f0c4d58ee9084802ec8a0d73ed8f4e8ebda0324819bada4a) |
| 9 | 186894303 | 1890941582288574 | 2026-09-30 | 2026-10-01 | 2 | Video | 29 s | Change Your Bed Without The Pain After | → **T31** (Anhang) „🖐️ "Arthritis in my fingers, wrists and prolapsed discs in my back. It…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | E, C, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1890941582288574) · [share](https://app.gethookd.ai/share/ad/186894303?signature=f24378a86b717ac22da1b3e91dd742d6e26bf6dd5cd89506ff6bd5a6e1a9d07d) |
| 10 | 186894314 | 1824185538588533 | 2026-09-29 | 2026-10-04 | 6 | DPA (Katalog-Karussell) | 6 Bild(er) | Pleene EasyRest™ Duvet | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1824185538588533) · [share](https://app.gethookd.ai/share/ad/186894314?signature=7bdbabfdbbbe2383748e19b6dad0d11cdfcc162c80d898188e955339901be34c) |
| 11 | 186894309 | 915791224700196 | 2026-09-29 | 2026-10-06 | 8 | Video | 55 s | You Never Actually Wash Your Duvet | → **T41** (Anhang) „🧺 Did you know you probably never actually wash your duvet?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=915791224700196) · [share](https://app.gethookd.ai/share/ad/186894309?signature=715b75dc25f81dc2bf7ec290648cca49c830ad1645ebb0a089931528978a7fa4) |
| 12 | 186000741 | 2094126661191928 | 2026-09-29 | 2026-10-01 | 3 | DPA (Katalog-Karussell) | 1 Video(s): 41 s; 7 Bild(er) | Pleene | → **T31** (Anhang) „🖐️ "Arthritis in my fingers, wrists and prolapsed discs in my back. It…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | E, C, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2094126661191928) · [share](https://app.gethookd.ai/share/ad/186000741?signature=6738884412d512024ad69d3116f5823f1082695bf006ebf4cc69595eb5ec6b8d) |
| 13 | 186000740 | 1654541439598610 | 2026-09-28 | 2026-10-04 | 7 | Bild | – | Yes, It Fits Your Machine | → **T32** (Anhang) „🧺 "Does a Double REALLY fit in a normal 7kg washing machine?"…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1654541439598610) · [share](https://app.gethookd.ai/share/ad/186000740?signature=99fc4675117114ba5b482e8e3cc8d825fc4b7b859b5d70faabdc388f566d64dd) |
| 14 | 186000736 | 4319008731578321 | 2026-09-28 | 2026-09-29 | 2 | Bild | – | When Did You Last Wash The Duvet? | → **T33** (Anhang) „🧺 Be honest: when did you last wash the duvet you're about to spend al…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4319008731578321) · [share](https://app.gethookd.ai/share/ad/186000736?signature=1452f241e18da47fde78b934850d8cd904275ba1e5c5ece021cc18729e9d1c9c) |
| 15 | 186000729 | 28683433151294400 | 2026-09-28 | 2026-10-06 | 9 | Bild | – | Which Colour? Comment 1-9 | → **T30** (Anhang) „❄️ Which colour is getting you through winter?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28683433151294400) · [share](https://app.gethookd.ai/share/ad/186000729?signature=8ba95535eebdf9b6842922c24fb07aa44c47d3c4d2ff69945060bde006efccf6) |
| 16 | 185228757 | 1702834305187116 | 2026-09-27 | 2026-09-30 | 4 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 3 | Verlierer (<7 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1702834305187116) · [share](https://app.gethookd.ai/share/ad/185228757?signature=1dfd2f4531667bf568420272cb6c94e3a909cb4fcffb421662b836ba4399b731) |
| 17 | 185228754 | 1410164930583069 | 2026-09-27 | 2026-09-30 | 4 | Video | 16 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 3 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1410164930583069) · [share](https://app.gethookd.ai/share/ad/185228754?signature=5987f7828c48ebe4b1dba09dde3f65d4de768d7044d5eba18781273d14192008) |
| 18 | 185228753 | 1407444221500652 | 2026-09-27 | 2026-09-30 | 4 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1407444221500652) · [share](https://app.gethookd.ai/share/ad/185228753?signature=d53dccb8597c8bb1de574f968d58d3edab599dc5cdc83f40af3bc2c1640722f0) |
| 19 | 185228748 | 1433462792232813 | 2026-09-27 | 2026-09-30 | 4 | Bild | – | Now In Super King | → **T27** (Anhang) „Our most requested size is finally here: the Pleene EasyRest in Super …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | F-Neuheit/Größe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1433462792232813) · [share](https://app.gethookd.ai/share/ad/185228748?signature=5ae20f134bb97857c1a962310cd9f5342d933e3ff0f7883488da80ca47b665ea) |
| 20 | 184134615 | 975825245551246 | 2026-09-25 | 2026-09-28 | 4 | Video | 32 s | Winter-Ready In One Wash | → **T52** (Anhang) „❄️ Cold nights are coming, and your duvet isn't ready.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=975825245551246) · [share](https://app.gethookd.ai/share/ad/184134615?signature=774ef2ce0f1f441165f2fc0b8a1cf8db0cf68ac2251544099acb001a51c92b56) |
| 21 | 184134614 | 2476447719512704 | 2026-09-25 | 2026-09-28 | 4 | Bild | – | Mint Green Is Almost Gone | → **T54** (Anhang) „🎁 30% off + 2 FREE matching pillow cases. And Mint Green is almost gon…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2476447719512704) · [share](https://app.gethookd.ai/share/ad/184134614?signature=3cf132e830abc320de3ba32af3792dcc31ccb92aba762db10afb6e5270455dca) |
| 22 | 184134613 | 1634367715003367 | 2026-09-25 | 2026-09-30 | 6 | Video | 45 s | A Winter Duvet You Can Actually Lift | → **T59** (Anhang) „🪶 "I'm 78 and only four foot nine. Putting a cover on a heavy winter d…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | E, C, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1634367715003367) · [share](https://app.gethookd.ai/share/ad/184134613?signature=39df81a972221b2ebeef9200328c1d2c127109519697b53bd7096a482ce50025) |
| 23 | 184134612 | 1607849677547918 | 2026-09-25 | 2026-10-06 | 12 | Video | 41 s | You Never Actually Wash Your Duvet | → **T41** (Anhang) „🧺 Did you know you probably never actually wash your duvet?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1607849677547918) · [share](https://app.gethookd.ai/share/ad/184134612?signature=9a873a8ff404e24cef3cde0b41912ee190d55637d8bf0057b1316dec5cc6804d) |
| 24 | 184134611 | 1608059824115796 | 2026-09-25 | 2026-09-30 | 6 | Video | 45 s | A Winter Duvet You Can Actually Lift | → **T59** (Anhang) „🪶 "I'm 78 and only four foot nine. Putting a cover on a heavy winter d…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | E, C, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1608059824115796) · [share](https://app.gethookd.ai/share/ad/184134611?signature=b4867beeb53616de91f8f5f592335b29311e07fd2e62a99a20e1aa581c601e23) |
| 25 | 184134610 | 28565120193099791 | 2026-09-25 | 2026-10-06 | 12 | Video | 40 s | You Never Actually Wash Your Duvet | → **T41** (Anhang) „🧺 Did you know you probably never actually wash your duvet?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28565120193099791) · [share](https://app.gethookd.ai/share/ad/184134610?signature=cb856b5ff34530fd68a6dc1c2e2d92bc1f08bf2315a0c7e98efec6551db0a57b) |
| 26 | 184134609 | 1952981572049664 | 2026-09-25 | 2026-10-04 | 10 | Bild | – | When Did You Last Wash The Duvet? | → **T33** (Anhang) „🧺 Be honest: when did you last wash the duvet you're about to spend al…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1952981572049664) · [share](https://app.gethookd.ai/share/ad/184134609?signature=0bbe48a4857636000ab46b4034e0195acaa42a3f818ab5fafd1d8d4f371dc9c4) |
| 27 | 184134608 | 1613161157111198 | 2026-09-25 | 2026-10-04 | 10 | Bild | – | Yes, It Fits Your Machine | → **T32** (Anhang) „🧺 "Does a Double REALLY fit in a normal 7kg washing machine?"…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1613161157111198) · [share](https://app.gethookd.ai/share/ad/184134608?signature=af18a3f11f7ccbe073c637b31beee14d41600fcc75130ac42db447333a74289e) |
| 28 | 184134606 | 975374475578218 | 2026-09-25 | 2026-10-01 | 7 | Video | 37 s | Winter-Ready In One Wash | → **T52** (Anhang) „❄️ Cold nights are coming, and your duvet isn't ready.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=975374475578218) · [share](https://app.gethookd.ai/share/ad/184134606?signature=13c94c9f91be02b7fc4f03c99c2fde7e6ceb36f23613d2d7d30bfaa54762d054) |
| 29 | 184134605 | 2529410374194727 | 2026-09-25 | 2026-09-30 | 6 | Bild | – | When Did You Last Wash The Duvet? | → **T33** (Anhang) „🧺 Be honest: when did you last wash the duvet you're about to spend al…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2529410374194727) · [share](https://app.gethookd.ai/share/ad/184134605?signature=12406f14ac37ae38da8bd1321f87e6637d86669b5c9aa934278fe1f6e05b2983) |
| 30 | 184134604 | 1386126253692718 | 2026-09-25 | 2026-10-06 | 12 | Video | 42 s | You Never Actually Wash Your Duvet | → **T41** (Anhang) „🧺 Did you know you probably never actually wash your duvet?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1386126253692718) · [share](https://app.gethookd.ai/share/ad/184134604?signature=4826825961750bcb5b926b6f776b2310b64a712fecc8d975d983bd3ddf00aff2) |
| 31 | 184134603 | 1597178745488191 | 2026-09-25 | 2026-10-04 | 10 | Bild | – | Yes, It Fits Your Machine | → **T32** (Anhang) „🧺 "Does a Double REALLY fit in a normal 7kg washing machine?"…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1597178745488191) · [share](https://app.gethookd.ai/share/ad/184134603?signature=04b974bad08fcb96f3f92cbac23fbe1adcf3ad40c7f37386edc5739c4519b6a2) |
| 32 | 184134602 | 1153825353859983 | 2026-09-25 | 2026-09-30 | 6 | Video | 45 s | A Winter Duvet You Can Actually Lift | → **T59** (Anhang) „🪶 "I'm 78 and only four foot nine. Putting a cover on a heavy winter d…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | E, C, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1153825353859983) · [share](https://app.gethookd.ai/share/ad/184134602?signature=d2740a7f2a1172b621d9dfe802a913d4a649abb13541a1a7a0b6034cfa223dfc) |
| 33 | 184134601 | 1094904756318997 | 2026-09-25 | 2026-10-01 | 7 | Video | 43 s | Change Your Bed Without The Pain After | → **T31** (Anhang) „🖐️ "Arthritis in my fingers, wrists and prolapsed discs in my back. It…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | E, C, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1094904756318997) · [share](https://app.gethookd.ai/share/ad/184134601?signature=f324617c96ac3410786e53ebffab6b89603f171280b705764cbded88f0d71dad) |
| 34 | 184134600 | 1589300952684868 | 2026-09-25 | 2026-10-04 | 10 | Bild | – | Yes, It Fits Your Machine | → **T32** (Anhang) „🧺 "Does a Double REALLY fit in a normal 7kg washing machine?"…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1589300952684868) · [share](https://app.gethookd.ai/share/ad/184134600?signature=04ee6c267f6a31a698efb1c88ef9ba2178569827b363fe364b197d8d0ad5fc41) |
| 35 | 184134599 | 1100256319606441 | 2026-09-25 | 2026-10-01 | 7 | Video | 41 s | Change Your Bed Without The Pain After | → **T31** (Anhang) „🖐️ "Arthritis in my fingers, wrists and prolapsed discs in my back. It…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | E, C, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1100256319606441) · [share](https://app.gethookd.ai/share/ad/184134599?signature=c5bc84b6a7aa534ebd0bb0d738ac661a9bc3836413ea507246076f1684b115a4) |
| 36 | 184134596 | 1844350933397173 | 2026-09-25 | 2026-09-29 | 5 | Bild | – | When Did You Last Wash The Duvet? | → **T33** (Anhang) „🧺 Be honest: when did you last wash the duvet you're about to spend al…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1844350933397173) · [share](https://app.gethookd.ai/share/ad/184134596?signature=a4195f16ec3a5a353e03ee2a4c3f1b6bce8ce4c15e281538b19b5e45849f727b) |
| 37 | 184134595 | 28232197259777711 | 2026-09-25 | 2026-09-28 | 4 | Bild | – | Mint Green Is Almost Gone | → **T54** (Anhang) „🎁 30% off + 2 FREE matching pillow cases. And Mint Green is almost gon…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28232197259777711) · [share](https://app.gethookd.ai/share/ad/184134595?signature=92121d7b03b2744d38fcd3c1ff304d545ba85ca9d2d1d3ca7e1be636cd4c7914) |
| 38 | 184134594 | 1429473512608237 | 2026-09-25 | 2026-10-01 | 7 | Video | 41 s | Change Your Bed Without The Pain After | → **T31** (Anhang) „🖐️ "Arthritis in my fingers, wrists and prolapsed discs in my back. It…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | E, C, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1429473512608237) · [share](https://app.gethookd.ai/share/ad/184134594?signature=399d61817499ac305e62c268595c4733c74c033fb1dfdb8ba480e27b6059fd24) |
| 39 | 184134591 | 1770358953887705 | 2026-09-25 | 2026-09-28 | 4 | Video | 33 s | Winter-Ready In One Wash | → **T52** (Anhang) „❄️ Cold nights are coming, and your duvet isn't ready.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1770358953887705) · [share](https://app.gethookd.ai/share/ad/184134591?signature=41d5a47e03e241f311fadc2e5d097841a6aa5db17f9e6004ad112392d6bb080c) |
| 40 | 183445647 | 1568449991144068 | 2026-09-25 | 2026-10-06 | 12 | Bild | – | Which Colour? Comment 1-9 | → **T30** (Anhang) „❄️ Which colour is getting you through winter?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1568449991144068) · [share](https://app.gethookd.ai/share/ad/183445647?signature=685c637db0097e2ad41b55cff5b262eb14d488aac73b6256853d287c4cbb09dd) |
| 41 | 182988113 | 2467224973688738 | 2026-09-24 | 2026-09-28 | 5 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2467224973688738) · [share](https://app.gethookd.ai/share/ad/182988113?signature=90ab157bcb1732d5b60d0b117ac08f6d95d7c324c7ae50841f8e39776bbb8993) |
| 42 | 182988036 | 1406063364236210 | 2026-09-24 | 2026-09-27 | 4 | Bild | – | Fresh Bedding Made Easy | → **T37** (Anhang) „Nothing beats getting into a freshly made bed. Pleene EasyRest™ makes …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest-comforter | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1406063364236210) · [share](https://app.gethookd.ai/share/ad/182988036?signature=2f1743c2b27c60670ab677c5a3f4907398217e0d9c20f7c63ac7b72315e3e61a) |
| 43 | 182988118 | 2239010486832594 | 2026-09-23 | 2026-10-04 | 12 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2239010486832594) · [share](https://app.gethookd.ai/share/ad/182988118?signature=8664479c40d1bc89165689674718420bff11317b83b06be41a6d3c284d45a68e) |
| 44 | 182988116 | 1867690807533357 | 2026-09-23 | 2026-09-26 | 4 | DPA (Katalog-Karussell) | 1 Video(s): 26 s; 7 Bild(er) | Pleene | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1867690807533357) · [share](https://app.gethookd.ai/share/ad/182988116?signature=38a4687f57e9750bde85aca915009010d1778e7fc9d63cb1eeb9e0bbc4750ca6) |
| 45 | 182988106 | 1737210887558001 | 2026-09-23 | 2026-09-28 | 6 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1737210887558001) · [share](https://app.gethookd.ai/share/ad/182988106?signature=0d75a6fb63b6ad6e31a3d662ee78759e6f1cabcaa4955b8fa579302f16fb2f12) |
| 46 | 182988104 | 1076654141840560 | 2026-09-23 | 2026-10-01 | 9 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1076654141840560) · [share](https://app.gethookd.ai/share/ad/182988104?signature=9b4a4cb15a6b1319762c593f01610e29c6fe56c9fb5a73913ada5869a389a472) |
| 47 | 182988102 | 2033750387344906 | 2026-09-23 | 2026-09-28 | 6 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2033750387344906) · [share](https://app.gethookd.ai/share/ad/182988102?signature=d7b28853d86506804b089084340f29f08f1d1d635e12481ba44d484d6fb80a2a) |
| 48 | 182988101 | 1427987919549105 | 2026-09-23 | 2026-09-28 | 6 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1427987919549105) · [share](https://app.gethookd.ai/share/ad/182988101?signature=36749826f681f3817a1fe74b7ed0f7cc03ebc504c51bee13b89d5a9fe17ec22d) |
| 49 | 182988100 | 4654579761443720 | 2026-09-23 | 2026-10-01 | 9 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4654579761443720) · [share](https://app.gethookd.ai/share/ad/182988100?signature=d7256224990ef89b05f6d35d739d2e4eb471b9d67ad304aa0f49403f9b1a8357) |
| 50 | 182988098 | 1559161055536548 | 2026-09-23 | 2026-09-28 | 6 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1559161055536548) · [share](https://app.gethookd.ai/share/ad/182988098?signature=a21e32f4ad60b396b82ad788c498d9859003d18503d1cc5efd6f35801f0e6e0d) |
| 51 | 182988096 | 1102669162216252 | 2026-09-23 | 2026-09-28 | 6 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1102669162216252) · [share](https://app.gethookd.ai/share/ad/182988096?signature=1a11212bc1d4f8d66b1431a4a4c84f65c4fa8a5353f603685de5b89ca9b9a748) |
| 52 | 182988094 | 1113558567904611 | 2026-09-23 | 2026-10-01 | 9 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1113558567904611) · [share](https://app.gethookd.ai/share/ad/182988094?signature=cf9de6e9349690594ca466d531d17d18d829c9c3906caa277d86782f5211b71c) |
| 53 | 182988087 | 4506106302995779 | 2026-09-21 | 2026-10-04 | 14 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4506106302995779) · [share](https://app.gethookd.ai/share/ad/182988087?signature=0e7974c6a1c6659c7b622a412d5108c5914d70378f01869d6c324b8968e7000f) |
| 54 | 182988085 | 2805172383218328 | 2026-09-21 | 2026-10-04 | 14 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2805172383218328) · [share](https://app.gethookd.ai/share/ad/182988085?signature=6621233799270b7ad2ad1ad8e2abcf574d73253cb843bb17315d222a094d07ae) |
| 55 | 180646060 | 909825758588041 | 2026-09-18 | 2026-09-26 | 9 | Bild | – | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=909825758588041) · [share](https://app.gethookd.ai/share/ad/180646060?signature=55c093ab1f9428f2d3cb0aaabc7de50412eca27f2fd7c27f62d23720cc00ee34) |
| 56 | 179476353 | 1129938659563410 | 2026-09-17 | 2026-09-23 | 7 | Video | 34 s | The Duvet With No Cover To Change | → **T40** (Anhang) „🛏️ I've spent over £300 on duvets, trying to find one that's actually …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1129938659563410) · [share](https://app.gethookd.ai/share/ad/179476353?signature=7940b29bf34bb5a96817e6dcde0bf749ff1a3cf7bf6343254ff0f505d95aed11) |
| 57 | 179476351 | 2322836645140315 | 2026-09-17 | 2026-09-19 | 3 | Bild | – | No Launderette Needed. Ever. | → **T38** (Anhang) „❄️ Your winter duvet shouldn't need a launderette.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | A, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2322836645140315) · [share](https://app.gethookd.ai/share/ad/179476351?signature=53587ea7f0871be857c471ca560da21e0722799d9c3c617ed054a176562302b0) |
| 58 | 178749264 | 832047280000629 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | "You'll Never Wash That." Watch Us. | → **T58** (Anhang) „🧺 "You'll never get that in a washing machine."…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=832047280000629) · [share](https://app.gethookd.ai/share/ad/178749264?signature=d8e08fd7024ff622ab3eacbab2d56418953b6cce8719c355c54bb885d2941843) |
| 59 | 178749263 | 1559934122048335 | 2026-09-16 | 2026-09-19 | 4 | Video | 60 s | The Duvet With No Cover To Change | → **T40** (Anhang) „🛏️ I've spent over £300 on duvets, trying to find one that's actually …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1559934122048335) · [share](https://app.gethookd.ai/share/ad/178749263?signature=28c598109f6505dfc77225878d4dfaac7f1f9c557ec2ca81d2b65a272e654513) |
| 60 | 178749262 | 1433020452362661 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | "You'll Never Wash That." Watch Us. | → **T58** (Anhang) „🧺 "You'll never get that in a washing machine."…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1433020452362661) · [share](https://app.gethookd.ai/share/ad/178749262?signature=6ceea2df765c2665f061bdb2643d632d74e795a39fedbd69227e229ab47471de) |
| 61 | 178749261 | 1910433766990430 | 2026-09-16 | 2026-09-23 | 8 | Video | 60 s | The Duvet With No Cover To Change | → **T40** (Anhang) „🛏️ I've spent over £300 on duvets, trying to find one that's actually …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1910433766990430) · [share](https://app.gethookd.ai/share/ad/178749261?signature=b3eb7a286e139adc9f17b32d765192b1abe27b7d39d5fe58d1f09cfcb2ff1289) |
| 62 | 178749256 | 1755623602431430 | 2026-09-16 | 2026-10-06 | 21 | Bild | – | Which Colour? Comment 1-9 | → **T30** (Anhang) „❄️ Which colour is getting you through winter?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1755623602431430) · [share](https://app.gethookd.ai/share/ad/178749256?signature=7ef8ca1e01e282413805d7e06ea684d3fb86dc2b3e7d113f11d549c6e121e016) |
| 63 | 178749253 | 1605124007665486 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | "You'll Never Wash That." Watch Us. | → **T58** (Anhang) „🧺 "You'll never get that in a washing machine."…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | A, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1605124007665486) · [share](https://app.gethookd.ai/share/ad/178749253?signature=bb402c29283429757519bab449ec29d3ee59c6746076b55220cae39f880c0375) |
| 64 | 178749250 | 1600246531600764 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | No Launderette Needed. Ever. | → **T38** (Anhang) „❄️ Your winter duvet shouldn't need a launderette.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | A, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1600246531600764) · [share](https://app.gethookd.ai/share/ad/178749250?signature=fc6d5d6a0b6751501b08c46781636fc56679a17751a11b9a753d14e1d0cb4edc) |
| 65 | 178749248 | 39521808590751389 | 2026-09-16 | 2026-09-23 | 8 | Bild | – | Which Colour? Comment 1-9 | → **T30** (Anhang) „❄️ Which colour is getting you through winter?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=39521808590751389) · [share](https://app.gethookd.ai/share/ad/178749248?signature=0412d7ece242d3435fb53b3a43e70c16d737aee591e13371a10a92aa4a647cf3) |
| 66 | 178749246 | 1940045106690283 | 2026-09-16 | 2026-10-06 | 21 | Bild | – | Which Colour? Comment 1-9 | → **T30** (Anhang) „❄️ Which colour is getting you through winter?…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1940045106690283) · [share](https://app.gethookd.ai/share/ad/178749246?signature=b56865ebc78f16250b8cbd28c54179f6839f72542e1c273bd2c8af04495a5e78) |
| 67 | 178749244 | 1554811692528015 | 2026-09-16 | 2026-09-19 | 4 | Bild | – | No Launderette Needed. Ever. | → **T38** (Anhang) „❄️ Your winter duvet shouldn't need a launderette.…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | A, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1554811692528015) · [share](https://app.gethookd.ai/share/ad/178749244?signature=e82eedb3d5627dfcb853ac65f9f4001d15d3830da366355715ee051dfd039d1d) |
| 68 | 178749241 | 986052237841995 | 2026-09-16 | 2026-09-19 | 4 | Video | 60 s | The Duvet With No Cover To Change | → **T40** (Anhang) „🛏️ I've spent over £300 on duvets, trying to find one that's actually …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest-duvet | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=986052237841995) · [share](https://app.gethookd.ai/share/ad/178749241?signature=6aeed07ee78eed5e22d99bb8187bd9d3d5d945249cf272ee3c10935ee517f838) |
| 69 | 177443601 | 1081218440981332 | 2026-09-15 | 2026-09-16 | 2 | Video | 98 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1081218440981332) · [share](https://app.gethookd.ai/share/ad/177443601?signature=0e69fdceabad477dafabf63d8a3c28b2d86db1d8e7fcdd8418ceefca00ef2163) |
| 70 | 177443530 | 2946532112392018 | 2026-09-15 | 2026-09-17 | 3 | Video | 35 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2946532112392018) · [share](https://app.gethookd.ai/share/ad/177443530?signature=12e7365a3613a67379a7167323d2c57539c53d9fcf100e93e6ece743c14230a9) |
| 71 | 177443602 | 2073792263526938 | 2026-09-14 | 2026-09-17 | 4 | Video | 98 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2073792263526938) · [share](https://app.gethookd.ai/share/ad/177443602?signature=c7b285afffca47f2dae3a4244736d275d94880a7f74338e78ee9a246ee829c87) |
| 72 | 177443600 | 2513290722497605 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2513290722497605) · [share](https://app.gethookd.ai/share/ad/177443600?signature=ddcd685a91abfe87049a8b15bca3ec2472427e8c95a15dc7762f54cad2ab1642) |
| 73 | 177443599 | 1133395249149782 | 2026-09-14 | 2026-09-17 | 4 | Video | 34 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1133395249149782) · [share](https://app.gethookd.ai/share/ad/177443599?signature=0b63f79b5e22ad95e72fbe0283b5b2f29c287ad0b413acc81da374bdc52d329a) |
| 74 | 177443598 | 3670824246413927 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3670824246413927) · [share](https://app.gethookd.ai/share/ad/177443598?signature=41f2961d627967c40ecc3e207c46b8000fba2b2ca4a1bfc74abca492b5051d44) |
| 75 | 177443597 | 1753919435864474 | 2026-09-14 | 2026-09-19 | 6 | Bild | – | When Did You Last Wash Your Duvet? | → **T23** (Anhang) „When did you last wash your duvet? Not the cover — the duvet. If you c…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1753919435864474) · [share](https://app.gethookd.ai/share/ad/177443597?signature=1fd330417eda40b19982750d960267251b300d61d02f19ef774729067d903643) |
| 76 | 177443596 | 1068339942444828 | 2026-09-14 | 2026-09-19 | 6 | Bild | – | When Did You Last Wash Your Duvet? | → **T23** (Anhang) „When did you last wash your duvet? Not the cover — the duvet. If you c…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1068339942444828) · [share](https://app.gethookd.ai/share/ad/177443596?signature=97e9107b8d99f64129bf266ca55bc9a87a40b954190972d55be43bccd790d2d3) |
| 77 | 177443595 | 840757192396215 | 2026-09-14 | 2026-09-17 | 4 | Video | 34 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=840757192396215) · [share](https://app.gethookd.ai/share/ad/177443595?signature=fb3ec8d47cec9e5c384e6557da566e2a7167bc1dcce9ad6004cb0fadaea8b19a) |
| 78 | 177443594 | 2260760481446549 | 2026-09-14 | 2026-09-16 | 3 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2260760481446549) · [share](https://app.gethookd.ai/share/ad/177443594?signature=32aab5c3e8c051a3e77000b5faed05d22088822596bdbc6d2464e22a702afab0) |
| 79 | 177443593 | 1665100558534130 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1665100558534130) · [share](https://app.gethookd.ai/share/ad/177443593?signature=f4deccae206a80e28326e74d23f2ecf1d936137255cea305f49342ebc1c0329f) |
| 80 | 177443592 | 1650813800086569 | 2026-09-14 | 2026-09-17 | 4 | Video | 94 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1650813800086569) · [share](https://app.gethookd.ai/share/ad/177443592?signature=0e39df1674b5bdab377169a5bff27662dab3d2399075ef2b9c93febd70e5ffdf) |
| 81 | 177443591 | 1807950816883747 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1807950816883747) · [share](https://app.gethookd.ai/share/ad/177443591?signature=9b1b5962bd37b35bf32147c23dcf7b76b29224049049ea1392a465cbd8d4837e) |
| 82 | 177443590 | 1637789308019060 | 2026-09-14 | 2026-09-19 | 6 | Bild | – | When Did You Last Wash Your Duvet? | → **T23** (Anhang) „When did you last wash your duvet? Not the cover — the duvet. If you c…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1637789308019060) · [share](https://app.gethookd.ai/share/ad/177443590?signature=7d0804fe474cc900241867e4c4480513626ee440e521d3331542bd7436ee44d3) |
| 83 | 177443589 | 1062087943363494 | 2026-09-14 | 2026-09-16 | 3 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1062087943363494) · [share](https://app.gethookd.ai/share/ad/177443589?signature=34b1701e868065679c26dc7306ed31ec7fd1e1118a2660e1307008ad2c28bb94) |
| 84 | 177443587 | 1365365102252559 | 2026-09-14 | 2026-09-17 | 4 | Video | 96 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1365365102252559) · [share](https://app.gethookd.ai/share/ad/177443587?signature=bde276edcdaf9c768e65fad707576046f8bbeee5604da6892f4e33cd78891e00) |
| 85 | 177443586 | 1115745250806662 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1115745250806662) · [share](https://app.gethookd.ai/share/ad/177443586?signature=c3e170e663b3af9badf9153a8841dec1bcdee31483cc400b0085be8e43e6dacd) |
| 86 | 177443585 | 2112997812629345 | 2026-09-14 | 2026-09-16 | 3 | Video | 28 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2112997812629345) · [share](https://app.gethookd.ai/share/ad/177443585?signature=8248c0424dbc7287f602f53e57dcea576f5d035db1e239f473058c840cc22143) |
| 87 | 177443584 | 1420035363429161 | 2026-09-14 | 2026-09-16 | 3 | Video | 94 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1420035363429161) · [share](https://app.gethookd.ai/share/ad/177443584?signature=c3f292e4706e8da618c9951485184c115181b432b831b8812581f5b1b75695c0) |
| 88 | 177443583 | 1062322340039317 | 2026-09-14 | 2026-09-16 | 3 | Video | 96 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1062322340039317) · [share](https://app.gethookd.ai/share/ad/177443583?signature=45b8176c4e4d2e8be24aaaec3f22cf0c39a8ebfbd522a251950a00136b5cc3e5) |
| 89 | 177443582 | 4749659575356689 | 2026-09-14 | 2026-09-17 | 4 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4749659575356689) · [share](https://app.gethookd.ai/share/ad/177443582?signature=f1e9e6b8ee11393bac575639d0d9bda72b44a6d5afb364f18abe37c6133b1c89) |
| 90 | 177443581 | 3596849097145294 | 2026-09-14 | 2026-09-17 | 4 | Video | 35 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3596849097145294) · [share](https://app.gethookd.ai/share/ad/177443581?signature=8770a3816223f407aae0a981fbc60cd93879455c620054d8123dc4d98e2fca93) |
| 91 | 176509047 | 28114479864874336 | 2026-09-13 | 2026-09-15 | 3 | Video | 48 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28114479864874336) · [share](https://app.gethookd.ai/share/ad/176509047?signature=0ed329f327631ee51b9fa3aa0b71e1e0be1602dcbe46c162d9159fe929a4868f) |
| 92 | 176509066 | 1405795578348773 | 2026-09-12 | 2026-09-16 | 5 | Video | 16 s | Everyone's buying the blue one. | → **T19** (Anhang) „Everyone's buying it in Coastal Blue — and stock is running low. The E…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1405795578348773) · [share](https://app.gethookd.ai/share/ad/176509066?signature=0cb321d47a6685ad62cd128e9ee362e51677b6599206c7e668b97a96d75c7851) |
| 93 | 176509065 | 1071333062193488 | 2026-09-12 | 2026-09-14 | 3 | Video | 50 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1071333062193488) · [share](https://app.gethookd.ai/share/ad/176509065?signature=9669db0b0e00ec60e30cd5e73327896e4fe5ab061380a0920d7e7711fd988983) |
| 94 | 176509063 | 944582731412393 | 2026-09-12 | 2026-09-14 | 3 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=944582731412393) · [share](https://app.gethookd.ai/share/ad/176509063?signature=a372ddfb0b0807ae92f022d8cc6fa0a81d70ca62bcdca550c9416bbb2c4548a3) |
| 95 | 176509060 | 1621625339576154 | 2026-09-12 | 2026-09-16 | 5 | Video | 16 s | Hearth Red. Nearly gone. | → **T26** (Anhang) „Hearth Red is nearly sold out — and unlike most 'selling fast' claims,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1621625339576154) · [share](https://app.gethookd.ai/share/ad/176509060?signature=1f30a265e865968ab41ca2a354333e4d0ec4219f106c9ec7e8dc5af322ee855b) |
| 96 | 176509056 | 2186278792248538 | 2026-09-12 | 2026-09-14 | 3 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2186278792248538) · [share](https://app.gethookd.ai/share/ad/176509056?signature=41b0a4df7dfb88f17041680c5f8ce936c5e84ba419882f3cf2337cec316a8d41) |
| 97 | 176509055 | 2180767429991145 | 2026-09-12 | 2026-09-16 | 5 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2180767429991145) · [share](https://app.gethookd.ai/share/ad/176509055?signature=9bbc5a4d046b3f673950a2c443b8c2250709e70b6922df7aedffef37cee09762) |
| 98 | 176509054 | 1962643637741789 | 2026-09-12 | 2026-09-15 | 4 | Video | 47 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 2 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1962643637741789) · [share](https://app.gethookd.ai/share/ad/176509054?signature=a554e25219cba3cad17680d784564316a99593283fd9e7c47ee843bcdd6b0ff8) |
| 99 | 176509052 | 1075991888730769 | 2026-09-12 | 2026-09-15 | 4 | Video | 59 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1075991888730769) · [share](https://app.gethookd.ai/share/ad/176509052?signature=896d11ba94d11972dd88fa29f17ac77f4adb7408f9f4b75b25c6c150f6378832) |
| 100 | 176509041 | 1021959167506701 | 2026-09-12 | 2026-09-26 | 15 | DCO | 2 Video(s): 47 s, 47 s | n/a | n/a (leer) | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Inaktiv (7–29 T.) | n/a (kein Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1021959167506701) · [share](https://app.gethookd.ai/share/ad/176509041?signature=b9739d4c6dafacc2711d845206535a5f5dce38e9e19ec0065c24778448068fef) |
| 101 | 176508993 | 29273650882225118 | 2026-09-12 | 2026-09-19 | 8 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=29273650882225118) · [share](https://app.gethookd.ai/share/ad/176508993?signature=2caada086021dd3c9911715419c8e047223a3cddf95dd7a9e09ee43b46ec4195) |
| 102 | 176508992 | 4521407554737304 | 2026-09-12 | 2026-09-19 | 8 | Video | 98 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4521407554737304) · [share](https://app.gethookd.ai/share/ad/176508992?signature=af45c0cd620aa0a401a22ca15f4987b69eecbcbe935a564f83bb999a3df5228f) |
| 103 | 176508991 | 28255297224133462 | 2026-09-12 | 2026-09-17 | 6 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28255297224133462) · [share](https://app.gethookd.ai/share/ad/176508991?signature=586e9db7e5756e56bb6246fa38aac1efc1a1c4b7985fd977a3fbf683aa5cd96d) |
| 104 | 176508990 | 1602884004557852 | 2026-09-12 | 2026-09-15 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1602884004557852) · [share](https://app.gethookd.ai/share/ad/176508990?signature=d207586659ddf999ec302f11b69d22ab150bf1b051cb74e3d4cad1f60fd6eeb4) |
| 105 | 176508989 | 1562959005608743 | 2026-09-12 | 2026-09-19 | 8 | Video | 94 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1562959005608743) · [share](https://app.gethookd.ai/share/ad/176508989?signature=8e2bc9471a003d18c4a332d7d06e3ae828a8bbf18822fccd716f30ac3943212b) |
| 106 | 176508988 | 2301773750360881 | 2026-09-12 | 2026-09-19 | 8 | Video | 28 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2301773750360881) · [share](https://app.gethookd.ai/share/ad/176508988?signature=71118fd9fa564a03e99f3b12f1cc48886d8a99e73132d5a8ab4b2565e7ec88c8) |
| 107 | 176508987 | 1655941279573927 | 2026-09-12 | 2026-09-15 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1655941279573927) · [share](https://app.gethookd.ai/share/ad/176508987?signature=a5a4925a2adf37d5f1657d14b913c939ad83a050c2c9046ea3cf7cd31ee716c0) |
| 108 | 176508986 | 1408102604752995 | 2026-09-12 | 2026-09-17 | 6 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1408102604752995) · [share](https://app.gethookd.ai/share/ad/176508986?signature=fbfc27e40214d569d214e7c2b70c3ad3f278b49b575449f2721aeac1687986e9) |
| 109 | 176508985 | 1088698223613178 | 2026-09-12 | 2026-09-17 | 6 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1088698223613178) · [share](https://app.gethookd.ai/share/ad/176508985?signature=6304303116b7f7aeac0486e46e80a748f30d7fb74bf5a9f2bd33aecc7691acb6) |
| 110 | 176508984 | 2175136563403655 | 2026-09-12 | 2026-09-17 | 6 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2175136563403655) · [share](https://app.gethookd.ai/share/ad/176508984?signature=93c729a3da289d837a0fee102bd899171882ab546b646c6b03bf4b6365a628c2) |
| 111 | 176508983 | 1221511333504674 | 2026-09-12 | 2026-09-17 | 6 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1221511333504674) · [share](https://app.gethookd.ai/share/ad/176508983?signature=41ed18628405ec73ab4ef2f7fb6acfec16d000796546d4d2056005fe640b2f80) |
| 112 | 176508982 | 2524514124713738 | 2026-09-12 | 2026-09-19 | 8 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2524514124713738) · [share](https://app.gethookd.ai/share/ad/176508982?signature=78880ad8a2e009df9edd4e8401ecd5f9b3d3bffc61f3a36ce7604b5606d2358c) |
| 113 | 176508981 | 28145093718480500 | 2026-09-12 | 2026-09-17 | 6 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28145093718480500) · [share](https://app.gethookd.ai/share/ad/176508981?signature=75b467bb3b5270538bcb911fab12096c89c9fc3c447d73da3723172fc6dd54aa) |
| 114 | 176508980 | 2313969162736198 | 2026-09-12 | 2026-09-19 | 8 | Video | 96 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2313969162736198) · [share](https://app.gethookd.ai/share/ad/176508980?signature=8c22b6bccd6cc6f785622e46083bf0a4b50f329f3ff402228831d1fcdc4e7df4) |
| 115 | 176508979 | 1864835554677337 | 2026-09-12 | 2026-09-15 | 4 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1864835554677337) · [share](https://app.gethookd.ai/share/ad/176508979?signature=2fc8ca3d7826e750f2ea7707646e09fbf894beb019a090d6c13353b375110b13) |
| 116 | 176019259 | 4515497522038458 | 2026-09-11 | 2026-09-13 | 3 | Video | 44 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4515497522038458) · [share](https://app.gethookd.ai/share/ad/176019259?signature=4c1250bb64d20097e0fb4f3dbbed33facd04cf96980b19ab734e383fcdfeab3e) |
| 117 | 176019258 | 1091844320013799 | 2026-09-11 | 2026-10-04 | 24 | Video | 16 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1091844320013799) · [share](https://app.gethookd.ai/share/ad/176019258?signature=877d121b02bf3d985b6df42cb1d5483f438f879c7c995c6795926b1b29414348) |
| 118 | 176019255 | 1790894445237675 | 2026-09-11 | 2026-09-15 | 5 | Video | 98 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1790894445237675) · [share](https://app.gethookd.ai/share/ad/176019255?signature=2e89903b8b91d86f9c011c63bad07d35fbfaf757dc7689c7a65bb9b594b24d35) |
| 119 | 176019254 | 1575463634269025 | 2026-09-11 | 2026-10-04 | 24 | Video | 16 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1575463634269025) · [share](https://app.gethookd.ai/share/ad/176019254?signature=bb33383c5e78af0d24dfcea0f10a8ec6ebc1eba275ddb8841b2dec6acb95abee) |
| 120 | 176019253 | 3973545856286426 | 2026-09-11 | 2026-09-17 | 7 | Video | 34 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3973545856286426) · [share](https://app.gethookd.ai/share/ad/176019253?signature=dbd4d6716615d9b91a68b18a99df1974752bee5358829d2b60eb285cc48a902e) |
| 121 | 176019252 | 1080291597819859 | 2026-09-11 | 2026-09-17 | 7 | Video | 35 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1080291597819859) · [share](https://app.gethookd.ai/share/ad/176019252?signature=db3a8cf6c471e5f0f0b8a399c64dfafba0a7f063bc3204acdaa873cd81f1c9e2) |
| 122 | 176019250 | 1048588144808991 | 2026-09-11 | 2026-09-15 | 5 | Video | 94 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1048588144808991) · [share](https://app.gethookd.ai/share/ad/176019250?signature=bb2fa23857f95c8fbbd4470ca26afe8c50a2a3a53440cb713b252b0dc726ec46) |
| 123 | 176019248 | 1739499207100992 | 2026-09-11 | 2026-09-26 | 16 | Bild | – | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1739499207100992) · [share](https://app.gethookd.ai/share/ad/176019248?signature=57e50378386295bdacdb4ca47cb13b1a8f787eafd84f3dfde113e2cc58d53569) |
| 124 | 176019246 | 1418934120178412 | 2026-09-11 | 2026-09-13 | 3 | Bild | – | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1418934120178412) · [share](https://app.gethookd.ai/share/ad/176019246?signature=9cf50967f51ccc7b3b630db5181aa3835ea34294e36ffe4506e3208334d0a204) |
| 125 | 176019245 | 2045770659638142 | 2026-09-11 | 2026-10-04 | 24 | Video | 16 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2045770659638142) · [share](https://app.gethookd.ai/share/ad/176019245?signature=08786d0c3c199a5e92351131085260291bf0b0d8ccc8ace96ea5380e4f80a8cc) |
| 126 | 176019241 | 1066337919529975 | 2026-09-11 | 2026-09-13 | 3 | Bild | – | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1066337919529975) · [share](https://app.gethookd.ai/share/ad/176019241?signature=e9afb4b06e132db07ad4314245fa57cfad5b59eb748875f2fbfb802e422f2171) |
| 127 | 176019240 | 1573597270304264 | 2026-09-11 | 2026-09-17 | 7 | Video | 34 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1573597270304264) · [share](https://app.gethookd.ai/share/ad/176019240?signature=2339b54ce2b22f2d4def404031dc8ecab0f652a77350e6103276e8ab326267bc) |
| 128 | 176019239 | 1732152891324106 | 2026-09-11 | 2026-09-15 | 5 | Video | 96 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1732152891324106) · [share](https://app.gethookd.ai/share/ad/176019239?signature=83dfcb5761b42b60b24ebb97d6b9a921b39d571f76ecc67849fef22b1a7271ae) |
| 129 | 176019233 | 1094931049641062 | 2026-09-11 | 2026-09-13 | 3 | Video | 45 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1094931049641062) · [share](https://app.gethookd.ai/share/ad/176019233?signature=6d58a91fd822d4c14be82b878e67a2a26a0770681ec6646e160d6cb372d52349) |
| 130 | 176019230 | 1591747636063500 | 2026-09-11 | 2026-09-13 | 3 | Video | 44 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1591747636063500) · [share](https://app.gethookd.ai/share/ad/176019230?signature=3465221580679edd49ba19eea71bbfa2387d65e2b5a77bc56c9e3d45159d232c) |
| 131 | 176019196 | 3314026992102951 | 2026-09-11 | 2026-09-13 | 3 | Bild | – | Myth vs Truth 🛏️ | → **T22** (Anhang) „Myth: Changing the bed has to be a struggle. 🛏️…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3314026992102951) · [share](https://app.gethookd.ai/share/ad/176019196?signature=eaf5d1c9d6ecc47321dbf0e0ced67e3a27bef8126d5147b1a411c0dc85c2517c) |
| 132 | 175318060 | 1058340253859638 | 2026-09-10 | 2026-09-28 | 19 | Bild | – | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1058340253859638) · [share](https://app.gethookd.ai/share/ad/175318060?signature=13d8f1a7d44e7b1e3e4cf23b72b91c34921ea34c8d7bf50234640d8503d23c99) |
| 133 | 175318057 | 1460580929454191 | 2026-09-10 | 2026-09-13 | 4 | Bild | – | The Duvet You Can Actually Wash | → **T18** (Anhang) „You think your bed is clean? Underneath that fresh cover is a duvet th…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1460580929454191) · [share](https://app.gethookd.ai/share/ad/175318057?signature=5a6e702b890f12853a1485a0260e2e074a6255554b3f255ec399ef702c22f153) |
| 134 | 175318052 | 2285022788925371 | 2026-09-10 | 2026-09-28 | 19 | Bild | – | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2285022788925371) · [share](https://app.gethookd.ai/share/ad/175318052?signature=28530bd54680e04220625e7a7ce35670298de4de88f19142f63a0af51aafaf27) |
| 135 | 174599748 | 1633029611773061 | 2026-09-09 | 2026-09-19 | 11 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1633029611773061) · [share](https://app.gethookd.ai/share/ad/174599748?signature=5103ae44bd483e3c3b7858b09dea61dd063a5ccb9ca1abf8616d60f4956b81e5) |
| 136 | 174599757 | 2279080359522397 | 2026-09-08 | 2026-09-19 | 12 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2279080359522397) · [share](https://app.gethookd.ai/share/ad/174599757?signature=e1fed6927c9dccb1ae2a8244f19403432b86f1e08214bc19ef56436cd50271b5) |
| 137 | 173929467 | 4742524499401363 | 2026-09-08 | 2026-09-12 | 5 | Video | 48 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4742524499401363) · [share](https://app.gethookd.ai/share/ad/173929467?signature=83c55cebe89c1e13d336e356bead6be7c22e066e8a9394b241287ef7b99960a8) |
| 138 | 173929464 | 2866592690402716 | 2026-09-08 | 2026-09-10 | 3 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2866592690402716) · [share](https://app.gethookd.ai/share/ad/173929464?signature=6231ce8c4f192970af0163c675f3b104590c25633eedf10ca198bcf8d1afebeb) |
| 139 | 173929458 | 1396594501799516 | 2026-09-08 | 2026-09-10 | 3 | Video | 23 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1396594501799516) · [share](https://app.gethookd.ai/share/ad/173929458?signature=919bfcf3c06976a17855b18a9eae3584ab808496c40dc2ce4c6d3b096eb6183b) |
| 140 | 173929457 | 1313740154015262 | 2026-09-08 | 2026-09-12 | 5 | Video | 54 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1313740154015262) · [share](https://app.gethookd.ai/share/ad/173929457?signature=318a10de4d807a3da3f6df6c1924f11fad80c243fad2ddaae94e437fb6da92ac) |
| 141 | 173929454 | 2124006455660892 | 2026-09-08 | 2026-09-10 | 3 | Video | 23 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2124006455660892) · [share](https://app.gethookd.ai/share/ad/173929454?signature=82f3602f981c8ded46f205e02da5111dfe758e2f5f5acd66eaced5e190f97564) |
| 142 | 173929453 | 1775756157097634 | 2026-09-08 | 2026-09-12 | 5 | Video | 56 s | n/a | n/a (leer) | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | n/a (kein Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1775756157097634) · [share](https://app.gethookd.ai/share/ad/173929453?signature=363c943770a6eac005ea84e110a874267a0f34c2e9f66aad7f390776989f17d9) |
| 143 | 173929450 | 1611973930463209 | 2026-09-08 | 2026-09-12 | 5 | Video | 48 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1611973930463209) · [share](https://app.gethookd.ai/share/ad/173929450?signature=a80523029cf057265338cb0d1b380c6bd6c6ca060c8e7df907815edcb06c42e0) |
| 144 | 173929447 | 1084752110635145 | 2026-09-08 | 2026-09-12 | 5 | Video | 55 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1084752110635145) · [share](https://app.gethookd.ai/share/ad/173929447?signature=23d52a022f8b0892cfbd6432d1ef38943fb354ae201d74571083262155450522) |
| 145 | 173929446 | 1747135706520938 | 2026-09-08 | 2026-09-10 | 3 | Video | 39 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1747135706520938) · [share](https://app.gethookd.ai/share/ad/173929446?signature=41103af45d64edffdebf55011b080c0021547475e50f3fe39ac2e2d924c6eccc) |
| 146 | 173929444 | 1610741237372540 | 2026-09-08 | 2026-09-10 | 3 | Video | 24 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1610741237372540) · [share](https://app.gethookd.ai/share/ad/173929444?signature=96dc06e86ed7d0fad83c789b40f870e1252e6d0fb43cec8a62cdc3c8ef37bc70) |
| 147 | 173929442 | 1505795144878605 | 2026-09-08 | 2026-09-10 | 3 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1505795144878605) · [share](https://app.gethookd.ai/share/ad/173929442?signature=65e304c9da2cca6468717d25a3b74600f2a206eabae99575b026fe93f26595b4) |
| 148 | 173929439 | 1106556025275590 | 2026-09-08 | 2026-09-12 | 5 | Video | 50 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1106556025275590) · [share](https://app.gethookd.ai/share/ad/173929439?signature=a267e12b5f45bf7184dc01d32db6e869ee78491d64604eafaf0be77449dbdc50) |
| 149 | 173929435 | 2919028021772107 | 2026-09-08 | 2026-09-12 | 5 | Video | 47 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2919028021772107) · [share](https://app.gethookd.ai/share/ad/173929435?signature=c50016d9643bf4d37e1afa6b14ad6930ef119939dc611c4f14a8543e4298f9cf) |
| 150 | 173929420 | 1484474786770328 | 2026-09-08 | 2026-09-14 | 7 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1484474786770328) · [share](https://app.gethookd.ai/share/ad/173929420?signature=6ee8e18aed443e7bb57a524f264fcb2cdcba91b00a566ff4f88886078407f91a) |
| 151 | 173929418 | 1073463711711279 | 2026-09-08 | 2026-09-23 | 16 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1073463711711279) · [share](https://app.gethookd.ai/share/ad/173929418?signature=af19810988ed88d51a91c0287e9cebf9b8981aa2a23e6505dcdd4a611e512ebb) |
| 152 | 173929409 | 4486713028269098 | 2026-09-08 | 2026-09-14 | 7 | Bild | – | What bed have you got? | → **T17** (Anhang) „Not sure which size? It's easier than duvet shopping usually is: Singl…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4486713028269098) · [share](https://app.gethookd.ai/share/ad/173929409?signature=b8a51aa95323f61b6e70a6a8e6a0aecc896fd10099238aabd06c28766a3c6940) |
| 153 | 173307153 | 1791848022151143 | 2026-09-07 | 2026-09-08 | 2 | DPA (Katalog-Karussell) | 6 Bild(er) | Pleene EasyRest™ Quilt | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1791848022151143) · [share](https://app.gethookd.ai/share/ad/173307153?signature=c316a45d4dc935a7f05a32666c8d157f3c1816aa64c4607768db951b292a7815) |
| 154 | 173307006 | 1000819466312449 | 2026-09-07 | 2026-09-12 | 6 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1000819466312449) · [share](https://app.gethookd.ai/share/ad/173307006?signature=6a3facb6e15dea5163f1c82f08c104d1aef6c96ea8688ec8bea2a6b5746e0553) |
| 155 | 173307005 | 1727217541693945 | 2026-09-07 | 2026-09-11 | 5 | Video | 56 s | n/a | n/a (leer) | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | n/a (kein Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1727217541693945) · [share](https://app.gethookd.ai/share/ad/173307005?signature=e955c720ed02764a12620677fab430c40c3a1302ba1074ff6cbb6fb4feea2a6f) |
| 156 | 173307004 | 1750365589627986 | 2026-09-07 | 2026-09-11 | 5 | Video | 54 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1750365589627986) · [share](https://app.gethookd.ai/share/ad/173307004?signature=ba8f780802160b23c82b13adf941ab4fe94b5d5de7ed58620b8c2308a5b1f268) |
| 157 | 173307003 | 1551454820113864 | 2026-09-07 | 2026-09-12 | 6 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1551454820113864) · [share](https://app.gethookd.ai/share/ad/173307003?signature=7d90d90ea9416ce04b33ce21489d3bedbb0cdbf29bfe65acfd480939c61bbaea) |
| 158 | 173307002 | 1408393734570917 | 2026-09-07 | 2026-09-12 | 6 | Video | 48 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1408393734570917) · [share](https://app.gethookd.ai/share/ad/173307002?signature=90c2c08116708120d27bfc2e8580872008f442c0f3e95ccbb3cc6fc9b55e5e28) |
| 159 | 173307001 | 2019851816071206 | 2026-09-07 | 2026-09-12 | 6 | Video | 39 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2019851816071206) · [share](https://app.gethookd.ai/share/ad/173307001?signature=41c3897aadcad08aca61bc702885f8d3be00532d8544ef94b04666894383e743) |
| 160 | 173307000 | 1992364828132659 | 2026-09-07 | 2026-09-17 | 11 | Video | 23 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1992364828132659) · [share](https://app.gethookd.ai/share/ad/173307000?signature=4591be66cf1294ac7b9b7c10baa7494974338f5e9f9fa283af2b614b16929972) |
| 161 | 173306996 | 3194755530721425 | 2026-09-07 | 2026-09-17 | 11 | Video | 23 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3194755530721425) · [share](https://app.gethookd.ai/share/ad/173306996?signature=ad19816d535260e2704b4044c8732c933236cec185d6acab3c6748aac20b33b4) |
| 162 | 173306995 | 1773663007005034 | 2026-09-07 | 2026-09-12 | 6 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1773663007005034) · [share](https://app.gethookd.ai/share/ad/173306995?signature=140a8ebf96325d786b4b3c419967f9d1ec43bb5dfa1319fce5a79b8f7b7b1b75) |
| 163 | 173306993 | 892043567122512 | 2026-09-07 | 2026-09-12 | 6 | Video | 50 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=892043567122512) · [share](https://app.gethookd.ai/share/ad/173306993?signature=ca830277dd3a0fba7588d3ebb8dd729b43dc82c336a8c1b2908c7757831e5801) |
| 164 | 173306992 | 1353734010076648 | 2026-09-07 | 2026-09-12 | 6 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1353734010076648) · [share](https://app.gethookd.ai/share/ad/173306992?signature=02b4684000d99e4cd4849b9fb8fbd1e96290019bcdb22cc4b9ec3c68f424d7ec) |
| 165 | 173306991 | 1813978556714586 | 2026-09-07 | 2026-09-12 | 6 | Video | 48 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1813978556714586) · [share](https://app.gethookd.ai/share/ad/173306991?signature=45f76ead5c2e625579dd0e46616f9d32b7701a8d6aa00098f07f5ef595ee8a94) |
| 166 | 173306990 | 3137854586414565 | 2026-09-07 | 2026-09-17 | 11 | Video | 24 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3137854586414565) · [share](https://app.gethookd.ai/share/ad/173306990?signature=e86abbaec05a56eec8618735a0357c52a90ea08707e30727f8b66d94c7c11bea) |
| 167 | 173306989 | 1415692010491060 | 2026-09-07 | 2026-09-12 | 6 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1415692010491060) · [share](https://app.gethookd.ai/share/ad/173306989?signature=dfaaa21c2a8eb9d0a0d154f9428d5549072fbdee069a0a84ca508b6fa9e441dc) |
| 168 | 173306987 | 1649586253355020 | 2026-09-07 | 2026-09-11 | 5 | Video | 55 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1649586253355020) · [share](https://app.gethookd.ai/share/ad/173306987?signature=245c4c09deb9406cdfbd1eadba71da357fbac13cc785b382d6894b5c87f12b7e) |
| 169 | 172760592 | 1473559164549663 | 2026-09-06 | 2026-09-10 | 5 | Video | 59 s | Done fighting with bed linen. | → **T20** (Anhang) „I ordered it because I was done fighting with bed linen every single w…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1473559164549663) · [share](https://app.gethookd.ai/share/ad/172760592?signature=34ef3733de3b00b2d39bfd544a65d6e7be2a30c2d6ce23b73830cfb80bbd9e85) |
| 170 | 172760591 | 2155825362011800 | 2026-09-06 | 2026-09-08 | 3 | Video | 59 s | Done fighting with bed linen. | → **T20** (Anhang) „I ordered it because I was done fighting with bed linen every single w…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2155825362011800) · [share](https://app.gethookd.ai/share/ad/172760591?signature=f234261cbd623d574d2b1b896e8b26322b56b0add0f9778861b0b1f32cd1213f) |
| 171 | 172760590 | 2154817405448722 | 2026-09-06 | 2026-09-10 | 5 | Video | 16 s | Everyone's buying the blue one. | → **T19** (Anhang) „Everyone's buying it in Coastal Blue — and stock is running low. The E…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2154817405448722) · [share](https://app.gethookd.ai/share/ad/172760590?signature=51d9c5f51a7ff752d4fb0266db56db7490e25422000ee88f65127a396c3fa683) |
| 172 | 172760589 | 4080616435408881 | 2026-09-06 | 2026-09-10 | 5 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4080616435408881) · [share](https://app.gethookd.ai/share/ad/172760589?signature=c67cec1fd4b8eda7027c98101f3f4c4e9d8301a9275d5de37d0e02f056ff4133) |
| 173 | 172760587 | 1822169385440820 | 2026-09-06 | 2026-09-10 | 5 | Video | 16 s | Hearth Red. Nearly gone. | → **T26** (Anhang) „Hearth Red is nearly sold out — and unlike most 'selling fast' claims,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1822169385440820) · [share](https://app.gethookd.ai/share/ad/172760587?signature=2b4e810a164a060bd1eb662fffa47f884bbbdb856d88f7878267826394bc65f9) |
| 174 | 172760586 | 2224833071629221 | 2026-09-06 | 2026-09-10 | 5 | Bild | – | Ready for the colder nights. | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2224833071629221) · [share](https://app.gethookd.ai/share/ad/172760586?signature=a28d96cdbad6739f0e66379d1579f0d4d173c3222c592ba1a3f285b1591d3eea) |
| 175 | 172760585 | 1383471107298030 | 2026-09-06 | 2026-09-10 | 5 | Video | 28 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1383471107298030) · [share](https://app.gethookd.ai/share/ad/172760585?signature=614d76db8b735b3e0b425eedb0f17da8c7aa491d9d269cb296a85e2445b0bd12) |
| 176 | 172760584 | 5071189629774111 | 2026-09-06 | 2026-09-08 | 3 | Video | 59 s | Done fighting with bed linen. | → **T20** (Anhang) „I ordered it because I was done fighting with bed linen every single w…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=5071189629774111) · [share](https://app.gethookd.ai/share/ad/172760584?signature=89ad43600d35883c4c875291e49e0af48c19c42995b4872e2f077785bdf5281d) |
| 177 | 172760582 | 1566620011909494 | 2026-09-06 | 2026-09-10 | 5 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1566620011909494) · [share](https://app.gethookd.ai/share/ad/172760582?signature=4653e55e292e27bc8ba412a6127af6ffce2dbf2cb58e7d36d4b2e49bfb749e9b) |
| 178 | 172760581 | 2064941720817246 | 2026-09-06 | 2026-09-09 | 4 | Video | 50 s | The Duvet You Can Actually Wash | → **T18** (Anhang) „You think your bed is clean? Underneath that fresh cover is a duvet th…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2064941720817246) · [share](https://app.gethookd.ai/share/ad/172760581?signature=62b824fc009ef8712321fb6207ee1cca8499f004aadca0a232a67120956316d9) |
| 179 | 172760580 | 1427738612589068 | 2026-09-06 | 2026-09-12 | 7 | Video | 50 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1427738612589068) · [share](https://app.gethookd.ai/share/ad/172760580?signature=af8d335f16d5cec35b62ba7617f38335df1b0ddcad5344c0dec47cf16cfb3218) |
| 180 | 172760579 | 2314424596030860 | 2026-09-06 | 2026-09-12 | 7 | Video | 37 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2314424596030860) · [share](https://app.gethookd.ai/share/ad/172760579?signature=20dd80ee314f804135267319113d5458f91d54c5ea2e7e8df40838a3d204111a) |
| 181 | 172760578 | 1084719370703887 | 2026-09-06 | 2026-09-12 | 7 | Video | 33 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1084719370703887) · [share](https://app.gethookd.ai/share/ad/172760578?signature=6ef0e999afcb1d26d0534b0fc1035ed3677738ced7fb5d99da87a9a29a1d30b3) |
| 182 | 172760577 | 1546680813321412 | 2026-09-06 | 2026-09-09 | 4 | Video | 50 s | The Duvet You Can Actually Wash | → **T18** (Anhang) „You think your bed is clean? Underneath that fresh cover is a duvet th…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1546680813321412) · [share](https://app.gethookd.ai/share/ad/172760577?signature=c6010cabb389b06207f0b7b85de3e14580452be3b3a3f25d86fe96c841362540) |
| 183 | 172760575 | 2062520128474003 | 2026-09-06 | 2026-09-09 | 4 | Video | 50 s | The Duvet You Can Actually Wash | → **T18** (Anhang) „You think your bed is clean? Underneath that fresh cover is a duvet th…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2062520128474003) · [share](https://app.gethookd.ai/share/ad/172760575?signature=368770e1ba104e2cddba7d32d17ff4cca0f40d232c2e1f0b1b693a1380b131a5) |
| 184 | 172760574 | 1125246056730912 | 2026-09-06 | 2026-09-10 | 5 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1125246056730912) · [share](https://app.gethookd.ai/share/ad/172760574?signature=a265429009c433a43bccd6e62f08bc60d973eb49316be71d4228add1a0e97c2f) |
| 185 | 172760572 | 2197532430803188 | 2026-09-06 | 2026-09-08 | 3 | Video | 59 s | Done fighting with bed linen. | → **T20** (Anhang) „I ordered it because I was done fighting with bed linen every single w…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2197532430803188) · [share](https://app.gethookd.ai/share/ad/172760572?signature=fc3725255d53d3a4bc819d5488413d1c65ccaa3d1eaa465504e0a845605c2457) |
| 186 | 172760562 | 2737528016642337 | 2026-09-06 | 2026-09-10 | 5 | Video | 49 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2737528016642337) · [share](https://app.gethookd.ai/share/ad/172760562?signature=60a829ad071ce22be7d44e89c70ee87a884b0496c6e5517e26cd454eeb63d64e) |
| 187 | 172403416 | 1495174535679772 | 2026-09-05 | 2026-09-10 | 6 | Video | 59 s | Done fighting with bed linen. | → **T20** (Anhang) „I ordered it because I was done fighting with bed linen every single w…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1495174535679772) · [share](https://app.gethookd.ai/share/ad/172403416?signature=04c920975df7291f74c0d3a215cd8c7b45527ffbed620639c9e6ee522e908b59) |
| 188 | 172403414 | 1359950386127722 | 2026-09-05 | 2026-09-09 | 5 | Bild | – | Only 26 Left In Hearth Red | → **T47** (Anhang) „Only 26 left in Hearth Red. The EasyRest is duvet and cover in one: no…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1359950386127722) · [share](https://app.gethookd.ai/share/ad/172403414?signature=7ce3efc089cae8465e763a3a2833d4818d13f53f6721553419bc34fcc87ee561) |
| 189 | 172403413 | 1589327685966822 | 2026-09-05 | 2026-09-28 | 24 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1589327685966822) · [share](https://app.gethookd.ai/share/ad/172403413?signature=4616717edd72d4e38c72d57f4d73ba1b0882bc18c37c295c883f6dfcde3d0ded) |
| 190 | 172403411 | 2831253467259319 | 2026-09-05 | 2026-09-13 | 9 | Video | 50 s | The Duvet You Can Actually Wash | → **T18** (Anhang) „You think your bed is clean? Underneath that fresh cover is a duvet th…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2831253467259319) · [share](https://app.gethookd.ai/share/ad/172403411?signature=5ad5eaebd840020d23e6872fb149a7b83e76348bc2b826a8e1b4fae3a5f87730) |
| 191 | 172403410 | 1011734415282335 | 2026-09-05 | 2026-09-07 | 3 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1011734415282335) · [share](https://app.gethookd.ai/share/ad/172403410?signature=c031a6d42aa9bec274935ec2721365081180a4163a81544118fdfb0c0a89e13b) |
| 192 | 172403408 | 1903265557302675 | 2026-09-05 | 2026-09-10 | 6 | Video | 15 s | Ready for the colder nights. | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1903265557302675) · [share](https://app.gethookd.ai/share/ad/172403408?signature=bfb0af5a1e4e5a82f16edd5b86f44ebbb56dc5556a1863f47a4d1e371b532065) |
| 193 | 172403407 | 1555774002992737 | 2026-09-05 | 2026-09-28 | 24 | Video | 29 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1555774002992737) · [share](https://app.gethookd.ai/share/ad/172403407?signature=969611d54898a7f52e40bf7f507004ac4141b671dcb7194d78381054efb280b6) |
| 194 | 172403406 | 4500708943408046 | 2026-09-05 | 2026-10-06 | 32 | Bild | – | NEW: Lavender Mist | → **T16** (Anhang) „NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyR…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4500708943408046) · [share](https://app.gethookd.ai/share/ad/172403406?signature=f03bfb314ad32fbcd30c11226ecdd5a1135ab35973faad99f4d19ed963db5cc1) |
| 195 | 172403405 | 2993343241057795 | 2026-09-05 | 2026-09-09 | 5 | Bild | – | Only 26 Left In Hearth Red | → **T47** (Anhang) „Only 26 left in Hearth Red. The EasyRest is duvet and cover in one: no…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2993343241057795) · [share](https://app.gethookd.ai/share/ad/172403405?signature=3cb40faac6160592ee39229aa9835e5dd359fd87160be63d99143151d82788e4) |
| 196 | 172403404 | 1100457982933062 | 2026-09-05 | 2026-09-10 | 6 | Video | 15 s | Ready for the colder nights. | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1100457982933062) · [share](https://app.gethookd.ai/share/ad/172403404?signature=43077be1c9f75c9211e6b7ddbdb399536420b1e69fa246418be2a5485a3f4be1) |
| 197 | 172403403 | 1576109840662015 | 2026-09-05 | 2026-09-19 | 15 | Video | 28 s | Be honest. When did you last wash it? | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1576109840662015) · [share](https://app.gethookd.ai/share/ad/172403403?signature=0e67b173a03d83deab9dbd5249852dd27ba752cbe7d72d8838d616e34e1f4e7b) |
| 198 | 172403399 | 1806555340498784 | 2026-09-05 | 2026-10-06 | 32 | Bild | – | NEW: Lavender Mist | → **T16** (Anhang) „NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyR…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1806555340498784) · [share](https://app.gethookd.ai/share/ad/172403399?signature=633b9ced144a1ca4578a840282486695db353cfc109f6057fde09722940b670f) |
| 199 | 172403397 | 2575860129544226 | 2026-09-05 | 2026-09-10 | 6 | Video | 15 s | Ready for the colder nights. | → **T02** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, B | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2575860129544226) · [share](https://app.gethookd.ai/share/ad/172403397?signature=754de3445e3d24f94af983df44f76271cbe1cc6e05c68be95a1c34ae33aaf2c2) |
| 200 | 172403395 | 1047122204596890 | 2026-09-05 | 2026-10-06 | 32 | Bild | – | NEW: Lavender Mist | → **T16** (Anhang) „NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyR…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1047122204596890) · [share](https://app.gethookd.ai/share/ad/172403395?signature=32a90ebdcc05f257ecbde618aaae2b4b213c2b141a11e1c2568016a6d04c2153) |
| 201 | 172403394 | 1949307619048060 | 2026-09-05 | 2026-09-19 | 15 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1949307619048060) · [share](https://app.gethookd.ai/share/ad/172403394?signature=49f5bfb34175c8dc3e3ead1b370df4c278544e19823f0e68a98659d230834a31) |
| 202 | 172403392 | 894822553505355 | 2026-09-05 | 2026-09-09 | 5 | Bild | – | Only 26 Left In Hearth Red | → **T47** (Anhang) „Only 26 left in Hearth Red. The EasyRest is duvet and cover in one: no…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=894822553505355) · [share](https://app.gethookd.ai/share/ad/172403392?signature=4842e5be2a38754fb19073aeb84a99fc495ccf5b401752fa9480fab1b39c82bd) |
| 203 | 172403391 | 1475931497627107 | 2026-09-05 | 2026-09-13 | 9 | Video | 50 s | The Duvet You Can Actually Wash | → **T18** (Anhang) „You think your bed is clean? Underneath that fresh cover is a duvet th…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1475931497627107) · [share](https://app.gethookd.ai/share/ad/172403391?signature=3d90b8ceaafb6f699b6a275d0cedce828afb1a6a3d146eabcd61d4e274c12b2e) |
| 204 | 172403390 | 1062571513142195 | 2026-09-05 | 2026-09-13 | 9 | Video | 50 s | The Duvet You Can Actually Wash | → **T18** (Anhang) „You think your bed is clean? Underneath that fresh cover is a duvet th…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1062571513142195) · [share](https://app.gethookd.ai/share/ad/172403390?signature=6a43282ebc53b3aa01bbf83327b992b079851aafd7c043664c5a5d31b870883e) |
| 205 | 172403388 | 1612120560527748 | 2026-09-05 | 2026-09-28 | 24 | Bild | – | Properly Warm, Never Heavy | → **T15** (Anhang) „A light duvet can't keep you warm in winter." We hear it every autumn,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | B, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1612120560527748) · [share](https://app.gethookd.ai/share/ad/172403388?signature=3eb0c5363f97560fcf9894889022c33b7f7225e518d551b73a8a701f7e38d591) |
| 206 | 172403382 | 1043368568571207 | 2026-09-05 | 2026-09-10 | 6 | Video | 59 s | Done fighting with bed linen. | → **T20** (Anhang) „I ordered it because I was done fighting with bed linen every single w…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1043368568571207) · [share](https://app.gethookd.ai/share/ad/172403382?signature=455f14c32c51aa4eeba91c1d7b0a1d4ac2faf012615529cf6ff4d1db370fd2c7) |
| 207 | 172403290 | 28510580475296819 | 2026-09-05 | 2026-09-09 | 5 | Video | 96 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28510580475296819) · [share](https://app.gethookd.ai/share/ad/172403290?signature=fd3527a1f12be055e344574cbb88297284557047fbbd326bffb5bd2e13a5ed2e) |
| 208 | 171870422 | 1418532113677425 | 2026-09-04 | 2026-09-15 | 12 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1418532113677425) · [share](https://app.gethookd.ai/share/ad/171870422?signature=b9a1116c859c220adb712d7e199249d7b9ad0a4530aceb13fbaa1fa651ec2b87) |
| 209 | 171870396 | 895462430311508 | 2026-09-03 | 2026-09-13 | 11 | Bild | – | Myth vs Truth 🛏️ | → **T22** (Anhang) „Myth: Changing the bed has to be a struggle. 🛏️…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=895462430311508) · [share](https://app.gethookd.ai/share/ad/171870396?signature=be59938e647deee51a0ca00a63c7bc5ac0bd2527706e5763601feee142ce34a5) |
| 210 | 171191701 | 1628220762425725 | 2026-09-03 | 2026-09-09 | 7 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1628220762425725) · [share](https://app.gethookd.ai/share/ad/171191701?signature=e6ba97534895541942d2c660e5bbe65499cafaf9b4157baff6c7e65522993040) |
| 211 | 171191699 | 1388798466011501 | 2026-09-03 | 2026-09-15 | 13 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1388798466011501) · [share](https://app.gethookd.ai/share/ad/171191699?signature=ca8be45af4ab0c11e54293520c00fcd9dfffa7b207d5a644a74b5144931637f3) |
| 212 | 171191582 | 3041704462827410 | 2026-09-03 | 2026-09-17 | 15 | Video | 16 s | Everyone's buying the blue one. | → **T19** (Anhang) „Everyone's buying it in Coastal Blue — and stock is running low. The E…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3041704462827410) · [share](https://app.gethookd.ai/share/ad/171191582?signature=00f4fa882f6a2be7ba87570ff6dd2b8bf13dd8fbee7e17ba86d7941bb61340ce) |
| 213 | 171191579 | 1099598952476064 | 2026-09-03 | 2026-09-09 | 7 | Video | 96 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1099598952476064) · [share](https://app.gethookd.ai/share/ad/171191579?signature=df04eb95e699cc53100a3d4c6ffd20b8a0f31d5b769658907d5c826458b54039) |
| 214 | 171191578 | 1402957108651054 | 2026-09-03 | 2026-09-17 | 15 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1402957108651054) · [share](https://app.gethookd.ai/share/ad/171191578?signature=45afedabff81abb452f2ae4cdc936adb05b652b3b898517f91fa8b5831886863) |
| 215 | 171191577 | 953775363762625 | 2026-09-03 | 2026-09-17 | 15 | Video | 50 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=953775363762625) · [share](https://app.gethookd.ai/share/ad/171191577?signature=ec038e63954b500349a98dfbf8ce8616d211fe2be068b31a83f4bd23615be7fb) |
| 216 | 171191574 | 1783899642622192 | 2026-09-03 | 2026-09-09 | 7 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1783899642622192) · [share](https://app.gethookd.ai/share/ad/171191574?signature=96b814e48551e425a2ba4b314fe061cbb7ca7ea1143290f0733cac277a92f63c) |
| 217 | 171191569 | 1610826870566611 | 2026-09-03 | 2026-09-17 | 15 | Video | 16 s | Hearth Red. Nearly gone. | → **T26** (Anhang) „Hearth Red is nearly sold out — and unlike most 'selling fast' claims,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1610826870566611) · [share](https://app.gethookd.ai/share/ad/171191569?signature=276c65d91aa86495698e416020c4262afd91bff3c353a12d96347bcbdad72525) |
| 218 | 171191568 | 1901757394542231 | 2026-09-03 | 2026-09-17 | 15 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1901757394542231) · [share](https://app.gethookd.ai/share/ad/171191568?signature=b863eaac50d47a23ab3a3609204e018eb92eaab16fe7f3ea5a2f93e6ad50f790) |
| 219 | 171191565 | 1874287520217800 | 2026-09-03 | 2026-09-09 | 7 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1874287520217800) · [share](https://app.gethookd.ai/share/ad/171191565?signature=3dbc3a5b754e8ce0b3354b8d5c9cdf8cc4fa63071f0cc7c4456602127d80a172) |
| 220 | 171191563 | 1079490754725153 | 2026-09-03 | 2026-09-15 | 13 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1079490754725153) · [share](https://app.gethookd.ai/share/ad/171191563?signature=8d294969356e6da3d92c37cf4628d104ef3c0c6d3266de0608244f7929518942) |
| 221 | 171191562 | 1047859684781075 | 2026-09-03 | 2026-09-17 | 15 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1047859684781075) · [share](https://app.gethookd.ai/share/ad/171191562?signature=1ea0ee52edf17f5556ea47cebb78b616250f4d7ec42422fa433693319b6ae0e7) |
| 222 | 171191560 | 1594830955384046 | 2026-09-03 | 2026-09-13 | 11 | Video | 47 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1594830955384046) · [share](https://app.gethookd.ai/share/ad/171191560?signature=a7bf3c8ec8581a1e31d0dec3b7721ef075b4d164739ff7e738332a559a2e4758) |
| 223 | 171191559 | 1623641532608382 | 2026-09-03 | 2026-09-09 | 7 | Video | 93 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1623641532608382) · [share](https://app.gethookd.ai/share/ad/171191559?signature=dee1e7be84469060645f7cd0746a7c86c5ea84190023fc0dfb3588f0663f2315) |
| 224 | 170468009 | 1853044069012295 | 2026-09-02 | 2026-09-08 | 7 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1853044069012295) · [share](https://app.gethookd.ai/share/ad/170468009?signature=1c20bafd5e8d6194c082aa09d482b9115e6cab387fd2e983cfe91335034475a1) |
| 225 | 170468005 | 1373362798113475 | 2026-09-02 | 2026-09-07 | 6 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1373362798113475) · [share](https://app.gethookd.ai/share/ad/170468005?signature=2671a74f597c9c31a930449c59dd7dbd8953fb2f5b329ee5e4870ef5233d1ec9) |
| 226 | 170468002 | 2023598331621501 | 2026-09-02 | 2026-09-08 | 7 | Video | 93 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, whatsapp, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2023598331621501) · [share](https://app.gethookd.ai/share/ad/170468002?signature=3539ba2e84e2aa8c885137fc4ba813fd127c9af2a5c236eca74c01c0922de21b) |
| 227 | 169784535 | 1103610958669062 | 2026-09-02 | 2026-09-05 | 4 | Video | 9 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1103610958669062) · [share](https://app.gethookd.ai/share/ad/169784535?signature=27cd42a1c461e7a06f38d8a43b3e8cb8e5901bc5b85d0f2091b087bd17e6e379) |
| 228 | 169082944 | 1063281430012872 | 2026-08-31 | 2026-09-03 | 4 | Video | 56 s | n/a | n/a (leer) | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | n/a (kein Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1063281430012872) · [share](https://app.gethookd.ai/share/ad/169082944?signature=ccd7617745b1f844aa56ce5e2dd9e9fa2679a8a215c40a8d23d579a61d411b87) |
| 229 | 169082943 | 1057947053611731 | 2026-08-31 | 2026-09-03 | 4 | Video | 54 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1057947053611731) · [share](https://app.gethookd.ai/share/ad/169082943?signature=9979b60a88acad2dd355eeef2ae2180bb2e3c9a47f8341d67043a650d5c3faa2) |
| 230 | 169082940 | 2161962311364685 | 2026-08-31 | 2026-09-08 | 9 | DPA (Katalog-Karussell) | 1 Video(s): 38 s; 7 Bild(er) | Pleene | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2161962311364685) · [share](https://app.gethookd.ai/share/ad/169082940?signature=0257b3488765dede9886989f81511db7ae3c42f1581bdeb289f1411b81fbceda) |
| 231 | 169082939 | 1595930678671246 | 2026-08-31 | 2026-09-03 | 4 | Video | 55 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1595930678671246) · [share](https://app.gethookd.ai/share/ad/169082939?signature=29f934e432f4b95834b38de07164974e9dbe13400caa5b8c32a13a26df89bbab) |
| 232 | 169082937 | 1626369158830578 | 2026-08-31 | 2026-09-08 | 9 | Video | 39 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1626369158830578) · [share](https://app.gethookd.ai/share/ad/169082937?signature=ad90315ed07068ea21d9ed773f130ae05875a2564b2d60e1ccc97d2d6b327793) |
| 233 | 169082936 | 1403346028405151 | 2026-08-31 | 2026-09-08 | 9 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1403346028405151) · [share](https://app.gethookd.ai/share/ad/169082936?signature=3fc943823fe63b987d5bbedae0519a360c2b37140ce39fb729bcd9e379af0519) |
| 234 | 169082934 | 1840411663595618 | 2026-08-31 | 2026-09-06 | 7 | Video | 46 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1840411663595618) · [share](https://app.gethookd.ai/share/ad/169082934?signature=bca93a838da2594c98f7d89377847673ff7a320dc652525bb77db73dc535155d) |
| 235 | 169082930 | 39017574957841998 | 2026-08-31 | 2026-09-05 | 6 | Video | 44 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=39017574957841998) · [share](https://app.gethookd.ai/share/ad/169082930?signature=ef1a6f899fad7115e11af44db3bd5fe068648a8b8124165c663ffeb9787ea290) |
| 236 | 169082928 | 1630900805110061 | 2026-08-31 | 2026-09-08 | 9 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1630900805110061) · [share](https://app.gethookd.ai/share/ad/169082928?signature=f81494fd3aa682a935722cc950975f59fab4da7c43415a28ec9eb5eacb3adc84) |
| 237 | 169082901 | 1780533559636125 | 2026-08-31 | 2026-09-09 | 10 | DPA (Katalog-Karussell) | 6 Bild(er) | Pleene EasyRest™ 2in1 Duvet | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1780533559636125) · [share](https://app.gethookd.ai/share/ad/169082901?signature=6e5e293c8ce1eaf0f67c0953b750499eb652578ace81d836b78dbc87bb8c61fb) |
| 238 | 168246696 | 1390324605820571 | 2026-08-29 | 2026-09-06 | 9 | Video | 33 s | Why This Duvet Needs No Cover | → **T34** (Anhang) „A duvet with no cover? Here's why that works. 👀…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1390324605820571) · [share](https://app.gethookd.ai/share/ad/168246696?signature=4a721d77d921d1a8b3e02559e61bc26d95b7d023dd9e574b4147d04a7ab0ad58) |
| 239 | 168246695 | 1661145052255141 | 2026-08-29 | 2026-09-05 | 8 | Video | 39 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1661145052255141) · [share](https://app.gethookd.ai/share/ad/168246695?signature=ba5cef8cff4c48877dd068a8a65031659a40e722956230dc64cd3267a353a224) |
| 240 | 168246693 | 28131939953139657 | 2026-08-29 | 2026-09-06 | 9 | Video | 33 s | Why This Duvet Needs No Cover | → **T34** (Anhang) „A duvet with no cover? Here's why that works. 👀…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28131939953139657) · [share](https://app.gethookd.ai/share/ad/168246693?signature=300efd2b7ed8575c14952b880f5b46ea536847bc73d2c3a9446d02c06315eb67) |
| 241 | 168246692 | 1756490415659312 | 2026-08-29 | 2026-09-06 | 9 | Video | 33 s | Why This Duvet Needs No Cover | → **T34** (Anhang) „A duvet with no cover? Here's why that works. 👀…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1756490415659312) · [share](https://app.gethookd.ai/share/ad/168246692?signature=f03510f37c63c63227cc6c7b9bcbfb12ca721122ed05696848d5d63914814a5f) |
| 242 | 168246691 | 2293103338097014 | 2026-08-29 | 2026-09-03 | 6 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2293103338097014) · [share](https://app.gethookd.ai/share/ad/168246691?signature=620d8944f6dc8b4f894c4b8f9f8c219cbfb636dce8b2119a47556cfb9ceceee1) |
| 243 | 168246690 | 1085479163954702 | 2026-08-29 | 2026-09-13 | 16 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1085479163954702) · [share](https://app.gethookd.ai/share/ad/168246690?signature=06e7966d22e7bf8e9641038471d7d2acf83497a5f6c7b0a6c2667aa7e9e9e12e) |
| 244 | 168246689 | 2552139308542869 | 2026-08-29 | 2026-09-05 | 8 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2552139308542869) · [share](https://app.gethookd.ai/share/ad/168246689?signature=5e2460275321ab2d6bf23838617642be82612cee9bcd3850162a5b9363130757) |
| 245 | 168246688 | 934156075782137 | 2026-08-29 | 2026-09-05 | 8 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=934156075782137) · [share](https://app.gethookd.ai/share/ad/168246688?signature=eef9cd013e3f37963f7867568afd8f220c81b1a2f8c00b524bafb16378ad48f0) |
| 246 | 168246687 | 1681661857299597 | 2026-08-29 | 2026-09-03 | 6 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1681661857299597) · [share](https://app.gethookd.ai/share/ad/168246687?signature=833e484afb7dc3d2e8ecd7003188a3c257bdf388e3b9a5dfdb54ec0d8846f130) |
| 247 | 168246685 | 1761675601627408 | 2026-08-29 | 2026-09-09 | 12 | Video | 50 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1761675601627408) · [share](https://app.gethookd.ai/share/ad/168246685?signature=5211f757478b9997975f63fb11ac4260d43b8522bec781185e798e2531405690) |
| 248 | 168246684 | 1276548054508945 | 2026-08-29 | 2026-09-10 | 13 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1276548054508945) · [share](https://app.gethookd.ai/share/ad/168246684?signature=2d9919418e3ff6df2f21e3f33e7d8db9a845a95ec80463e7aad18b1eada17ee2) |
| 249 | 168246683 | 1429155502643651 | 2026-08-29 | 2026-09-03 | 6 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1429155502643651) · [share](https://app.gethookd.ai/share/ad/168246683?signature=a8dff647e7084fb9044b563b677037a9c4fc8447b41b9d1faf660409e9b5f565) |
| 250 | 168246681 | 1579804513380981 | 2026-08-29 | 2026-09-02 | 5 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1579804513380981) · [share](https://app.gethookd.ai/share/ad/168246681?signature=4686c482a3fa397ba50b0180aca04fea349cbaa88edad17ca8e51c77da27a514) |
| 251 | 168246680 | 1419441456832154 | 2026-08-29 | 2026-09-09 | 12 | Video | 48 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1419441456832154) · [share](https://app.gethookd.ai/share/ad/168246680?signature=d4d43fd58fa3d3aedb70fe7c47bd56bb80ea89c01f2c3db39cf9a12d2f704605) |
| 252 | 168246679 | 1882195236549647 | 2026-08-29 | 2026-09-13 | 16 | Bild | – | Myth vs Truth 🛏️ | → **T22** (Anhang) „Myth: Changing the bed has to be a struggle. 🛏️…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1882195236549647) · [share](https://app.gethookd.ai/share/ad/168246679?signature=c325194f9d01b91c1830675c97d0f98797424df05a27f6b5fa8f3a76f6f702d2) |
| 253 | 168246677 | 1399976375399987 | 2026-08-29 | 2026-09-03 | 6 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1399976375399987) · [share](https://app.gethookd.ai/share/ad/168246677?signature=91765c1d883833146b2b1499d6f27f94ac51aa2dcb7f2dde3ba5828511ffec14) |
| 254 | 168246676 | 3154796451577249 | 2026-08-29 | 2026-09-09 | 12 | Video | 48 s | The Cover Is Sewn In | → **T14** (Anhang) „For 40 years, wash day in our house meant one thing: fighting a duvet …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3154796451577249) · [share](https://app.gethookd.ai/share/ad/168246676?signature=8868845356466469475202630e999966b097f08fbc5ea2b067b6f9852d797b63) |
| 255 | 168246674 | 1778366989841923 | 2026-08-29 | 2026-09-13 | 16 | Bild | – | Myth vs Truth 🛏️ | → **T22** (Anhang) „Myth: Changing the bed has to be a struggle. 🛏️…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1778366989841923) · [share](https://app.gethookd.ai/share/ad/168246674?signature=f22886d86d88e4ad775b22d5791ecc09b0eedfee5f87b1ab41fa261167f9a4d6) |
| 256 | 168246672 | 3417215361792397 | 2026-08-29 | 2026-09-13 | 16 | Video | 27 s | Check This Before You Buy | → **T25** (Anhang) „Before you buy a coverless duvet, check three things: ✅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Einwand/Kaufhilfe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3417215361792397) · [share](https://app.gethookd.ai/share/ad/168246672?signature=2630c6a030465ae3342d93ea6e5d39b36463f202fc714c4bdbab208dbbef1c8b) |
| 257 | 168246671 | 1745625510080286 | 2026-08-29 | 2026-09-14 | 17 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1745625510080286) · [share](https://app.gethookd.ai/share/ad/168246671?signature=b9d423b091340bc8f67820b401d12d77133ea5456e66dd06b1a6f408c9aad76c) |
| 258 | 168246668 | 3269980339876399 | 2026-08-29 | 2026-09-13 | 16 | Bild | – | Myth vs Truth 🛏️ | → **T22** (Anhang) „Myth: Changing the bed has to be a struggle. 🛏️…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3269980339876399) · [share](https://app.gethookd.ai/share/ad/168246668?signature=873648a58bc1055a141c8108f14ab68b94c8192ed86fdb2630cda3c79f57fa8d) |
| 259 | 168246667 | 1772539527099238 | 2026-08-29 | 2026-09-05 | 8 | Video | 38 s | The Duvet That Goes In The Wash | → **T07** (Anhang) „"You'd need an enormous washing machine for that." 😅…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A, F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1772539527099238) · [share](https://app.gethookd.ai/share/ad/168246667?signature=2910fcb35b400d6a681632c4175a78eec867d3d7da565dcb3f257926330cf1fe) |
| 260 | 168246665 | 1349363223849405 | 2026-08-29 | 2026-09-14 | 17 | Bild | – | 2 Free Pillow Cases 🎁 | → **T12** (Anhang) „This week only 🎁…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1349363223849405) · [share](https://app.gethookd.ai/share/ad/168246665?signature=dc33b546d3bb0ae6f9596c58a23eb8457824803d3557b5c3b6d7b17cc4872cc6) |
| 261 | 168246664 | 1346057280616402 | 2026-08-29 | 2026-09-06 | 9 | Video | 33 s | Why This Duvet Needs No Cover | → **T34** (Anhang) „A duvet with no cover? Here's why that works. 👀…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1346057280616402) · [share](https://app.gethookd.ai/share/ad/168246664?signature=eb8a3845b674a444cc9a1304bd72588ca50d1e9ea34b325534f32cfb27895985) |
| 262 | 168246660 | 1625011942569991 | 2026-08-29 | 2026-09-13 | 16 | DPA (Katalog-Karussell) | 6 Bild(er) | Pleene | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1625011942569991) · [share](https://app.gethookd.ai/share/ad/168246660?signature=8a3f4e11088acfaf0c959abc38664a0e14ab303be1d870369977f1f8011331cc) |
| 263 | 163921092 | 1058378360424550 | 2026-08-28 | 2026-09-23 | 27 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1058378360424550) · [share](https://app.gethookd.ai/share/ad/163921092?signature=b5e611e6e903a1b87b3bb69a34aba3421ac405393588d11f1d5ffc47ad9624de) |
| 264 | 163921094 | 2004939896876500 | 2026-08-27 | 2026-09-26 | 31 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2004939896876500) · [share](https://app.gethookd.ai/share/ad/163921094?signature=a39f561bd389718001fe0486d7cc002b947dc3a469485419fdc85afb04a22171) |
| 265 | 163921093 | 1418435773513243 | 2026-08-27 | 2026-09-14 | 19 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1418435773513243) · [share](https://app.gethookd.ai/share/ad/163921093?signature=fbcaf4b8f5ad6cea8f74218d9c700e42d6722192fb8de2ba37a598d82faafbd0) |
| 266 | 163921090 | 1507951734683814 | 2026-08-27 | 2026-08-28 | 2 | Video | 42 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1507951734683814) · [share](https://app.gethookd.ai/share/ad/163921090?signature=0a9f0705447563d2bc2177c2ef0c5eb4427695d95aa5f4933f6fac4b281d4e57) |
| 267 | 163921087 | 944463371282198 | 2026-08-27 | 2026-08-29 | 3 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=944463371282198) · [share](https://app.gethookd.ai/share/ad/163921087?signature=dbabf958912509934002176b25730135248f1ecd65d749a25059ec39fdb9b45b) |
| 268 | 163921086 | 969450709504445 | 2026-08-27 | 2026-08-28 | 2 | Video | 42 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=969450709504445) · [share](https://app.gethookd.ai/share/ad/163921086?signature=e9ed3f6703cd1c492a7d61853dd650776b4ca3f78e3ae8547d769f242f0b8ce0) |
| 269 | 163921085 | 2182897075602948 | 2026-08-27 | 2026-08-29 | 3 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2182897075602948) · [share](https://app.gethookd.ai/share/ad/163921085?signature=d7e7da488a277dd0f3997c646f89861fc931e9e1eca511ce1973f354d35573b4) |
| 270 | 163921083 | 2301951323952231 | 2026-08-27 | 2026-08-29 | 3 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2301951323952231) · [share](https://app.gethookd.ai/share/ad/163921083?signature=e0031e10058b5b97b0b4dc7a368cd8967c194eb7d5489070ae8d3c4cf6ccb60b) |
| 271 | 163921080 | 1795527678139092 | 2026-08-27 | 2026-08-29 | 3 | Video | 23 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1795527678139092) · [share](https://app.gethookd.ai/share/ad/163921080?signature=4cf9442d2d597ea0f9fabb4b8dacfa2fb7d10c45fa0ee79d35d827fb1d72aa24) |
| 272 | 163921079 | 1728762728359986 | 2026-08-27 | 2026-09-06 | 11 | Video | 96 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1728762728359986) · [share](https://app.gethookd.ai/share/ad/163921079?signature=dbba0887ebed7dd446620490e04222290f9e2b3dcbca28ac4be40102e8a8e849) |
| 273 | 163921077 | 1370482488044030 | 2026-08-27 | 2026-09-06 | 11 | Video | 96 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1370482488044030) · [share](https://app.gethookd.ai/share/ad/163921077?signature=f900f538973d396e346fa0fdc9b75047728b7fa851109f8251d33022fbf89933) |
| 274 | 163921076 | 2109383479965541 | 2026-08-27 | 2026-08-28 | 2 | Video | 42 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2109383479965541) · [share](https://app.gethookd.ai/share/ad/163921076?signature=d3129746960cf7fcc05bcf84f40bd1869c96a2c74d50077f8522b2ee71d2cbbe) |
| 275 | 163921073 | 1412790744070211 | 2026-08-27 | 2026-09-07 | 12 | Video | 55 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1412790744070211) · [share](https://app.gethookd.ai/share/ad/163921073?signature=fd1156b865162f2928e0d3008db154dfb46d4a6d68bcf138d0e8a10ce9d7a932) |
| 276 | 163921072 | 1061170520166635 | 2026-08-27 | 2026-09-07 | 12 | Video | 14 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1061170520166635) · [share](https://app.gethookd.ai/share/ad/163921072?signature=7591a13e8e00576e212778cf1b761b444e2c7c38cd3062f535b9f0bef6562586) |
| 277 | 163921071 | 1053872310871368 | 2026-08-27 | 2026-09-07 | 12 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1053872310871368) · [share](https://app.gethookd.ai/share/ad/163921071?signature=785b33469c7abd08a1569b0920a17b6b9f4bfbb08ca28099ca78b84422f549da) |
| 278 | 163921070 | 1178371524845767 | 2026-08-27 | 2026-09-06 | 11 | Video | 93 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1178371524845767) · [share](https://app.gethookd.ai/share/ad/163921070?signature=6049305db6840dacb7ced4fa96fed53d89741c6efad53a4f806df206ed6571ff) |
| 279 | 163921068 | 1774397390382079 | 2026-08-27 | 2026-08-29 | 3 | Video | 47 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1774397390382079) · [share](https://app.gethookd.ai/share/ad/163921068?signature=6ced84e543db34204bd831a6a201cebb6682f5b08dfeec641a2590c492396e82) |
| 280 | 160709948 | 1081193501126219 | 2026-08-26 | 2026-08-29 | 4 | Bild | – | I've Quit Bed Linen | → **T36** (Anhang) „I've quit bed linen. Completely. The Pleene EasyRest is duvet and cove…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1081193501126219) · [share](https://app.gethookd.ai/share/ad/160709948?signature=fefd44f7dfc20214ab3cce5a784f38b0c6b310e30d37054382a620e06b075a11) |
| 281 | 160709944 | 2266305264227781 | 2026-08-26 | 2026-08-30 | 5 | DPA (Katalog-Karussell) | 1 Video(s): 36 s; 7 Bild(er) | Pleene | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2266305264227781) · [share](https://app.gethookd.ai/share/ad/160709944?signature=b577fde27437ee2aba50500c9cc66e49cad0330bf8e4242078c369a37dc6c3ed) |
| 282 | 160709941 | 1576220147073129 | 2026-08-26 | 2026-09-10 | 16 | Video | 50 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1576220147073129) · [share](https://app.gethookd.ai/share/ad/160709941?signature=095fb25269f7342801cf8dcfaac1b708ecd3c507257b215674431c6a813d0019) |
| 283 | 160709929 | 28109977455334741 | 2026-08-26 | 2026-08-29 | 4 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28109977455334741) · [share](https://app.gethookd.ai/share/ad/160709929?signature=8d8e9f4864b97a6d285e9eaca6eb5a9285a9b4fd475c300c2eea14cea90fb4d7) |
| 284 | 160709927 | 2572930263145430 | 2026-08-26 | 2026-08-29 | 4 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2572930263145430) · [share](https://app.gethookd.ai/share/ad/160709927?signature=54fd2107141c3e5974e184f88822d706e0f74aa091ee8750549f4b084315b807) |
| 285 | 160709926 | 1085517767464996 | 2026-08-26 | 2026-08-28 | 3 | Video | 50 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1085517767464996) · [share](https://app.gethookd.ai/share/ad/160709926?signature=00bc45001dd9357fa7743ead4ef9c6238748a40fa26a3ab56ecb401684def44b) |
| 286 | 160709967 | 1540905524455176 | 2026-08-25 | 2026-09-06 | 13 | Video | 50 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1540905524455176) · [share](https://app.gethookd.ai/share/ad/160709967?signature=8522221c85aab2a963bfee562d179490c44a0230ceaa99d3ad2f0ec4bff6a4ae) |
| 287 | 160709966 | 1530826575397557 | 2026-08-25 | 2026-09-06 | 13 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1530826575397557) · [share](https://app.gethookd.ai/share/ad/160709966?signature=9575017d8b0627a970dd1d7664714212835abb83142cb2c0c2eacaa1731ff618) |
| 288 | 160709965 | 1372039134492690 | 2026-08-25 | 2026-09-08 | 15 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1372039134492690) · [share](https://app.gethookd.ai/share/ad/160709965?signature=a8f3f2406fc0ad1a007069b6dc7bd9211b99debd654cb77e100d726efd4a1401) |
| 289 | 160709963 | 1964455347562823 | 2026-08-25 | 2026-09-08 | 15 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1964455347562823) · [share](https://app.gethookd.ai/share/ad/160709963?signature=b0a558b6c640dc1ff83f3e164cf5e4b841bb981fffecf5dd24fb85f9bcb737e0) |
| 290 | 160709961 | 2260628194476786 | 2026-08-25 | 2026-08-30 | 6 | Video | 47 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2260628194476786) · [share](https://app.gethookd.ai/share/ad/160709961?signature=5122603c55275ec13f2871e574ec497fa1b5e466631f8f664bbec4b3b173e376) |
| 291 | 160709959 | 1330349489174807 | 2026-08-25 | 2026-09-08 | 15 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1330349489174807) · [share](https://app.gethookd.ai/share/ad/160709959?signature=63dfbaf234edf2381440e0a51477875fdee054d15daa0c3c7bc6f979a42ffd9e) |
| 292 | 160709957 | 2064399717496829 | 2026-08-25 | 2026-08-27 | 3 | Video | 23 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2064399717496829) · [share](https://app.gethookd.ai/share/ad/160709957?signature=f5d8aa1fec83bd858da01a57694b65ffcec54c1ab083c537269b941b93e4c855) |
| 293 | 160709955 | 1100389765715214 | 2026-08-25 | 2026-08-30 | 6 | Video | 36 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1100389765715214) · [share](https://app.gethookd.ai/share/ad/160709955?signature=88f3b14e1120d2e8115efb28054f6c32a658c3261927fdeeab4000ef943fd10d) |
| 294 | 160709953 | 1428614925830931 | 2026-08-25 | 2026-09-06 | 13 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1428614925830931) · [share](https://app.gethookd.ai/share/ad/160709953?signature=654aaa9ca5b533ca0c47df8b85f895de8c5e3abefb1d8aa16f2ae9e6cad19f0d) |
| 295 | 160709950 | 2301207490642262 | 2026-08-25 | 2026-08-29 | 5 | Video | 40 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2301207490642262) · [share](https://app.gethookd.ai/share/ad/160709950?signature=0cf51dc6d7c6ea9a72a0ae0b325005fe89c4bc74e4652784fc66d0d5b281d072) |
| 296 | 160709949 | 1221049120196497 | 2026-08-25 | 2026-08-30 | 6 | Video | 41 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1221049120196497) · [share](https://app.gethookd.ai/share/ad/160709949?signature=a992fc436e5986a18614d58c34bd9a20bdf5b690dc2474acbfdd6ea0489f204c) |
| 297 | 160709947 | 1388363746835507 | 2026-08-25 | 2026-09-12 | 19 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1388363746835507) · [share](https://app.gethookd.ai/share/ad/160709947?signature=f90fb9a5645c554ee88ba39eefd54178bb13cef0b9794641c37fe6a48e401c2e) |
| 298 | 160709946 | 1640468797597252 | 2026-08-25 | 2026-09-12 | 19 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1640468797597252) · [share](https://app.gethookd.ai/share/ad/160709946?signature=cbfcddf6816b003d565c3c2b6a8e8e062debb43c861a5a54f4bd993f2cb55026) |
| 299 | 160709942 | 1879644266746711 | 2026-08-25 | 2026-09-10 | 17 | Bild | – | "Best thing I got for years." | → **T42** (Anhang) „"Best thing I got for years." — six words from a real customer, and ho…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1879644266746711) · [share](https://app.gethookd.ai/share/ad/160709942?signature=f6784c59d93e62e2b4c886b44ec2108e3b9830642a104b75a9811c4b4be14541) |
| 300 | 157492489 | 1081653717937889 | 2026-08-25 | 2026-08-28 | 4 | Video | 16 s | Everyone's buying the blue one. | → **T19** (Anhang) „Everyone's buying it in Coastal Blue — and stock is running low. The E…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1081653717937889) · [share](https://app.gethookd.ai/share/ad/157492489?signature=b976a10a18bd562b4bc73ecd5dca2c86cbc8747232f337b62e0c19473584ed69) |
| 301 | 157492488 | 1612940290484916 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1612940290484916) · [share](https://app.gethookd.ai/share/ad/157492488?signature=002bbb0caed63fc997b3cc1e258264245d1be199739b1a0f38f9c4b37f14463a) |
| 302 | 157492487 | 1040663415485965 | 2026-08-25 | 2026-09-28 | 35 | Bild | – | Now In Super King | → **T27** (Anhang) „Our most requested size is finally here: the Pleene EasyRest in Super …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Neuheit/Größe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1040663415485965) · [share](https://app.gethookd.ai/share/ad/157492487?signature=a83fedfddd2d15a5863f04bfae129c9d383a04bbb8cc7f316e48cbdfd42fdf1a) |
| 303 | 157492485 | 2191503985130597 | 2026-08-25 | 2026-08-28 | 4 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2191503985130597) · [share](https://app.gethookd.ai/share/ad/157492485?signature=5f17c96390d02ec4e058bf835dca1895b32c0cd6161baf821d2bd4646b1b834d) |
| 304 | 157492484 | 1068419246180894 | 2026-08-25 | 2026-08-28 | 4 | Bild | – | Who Wins In Your House? | → **T28** (Anhang) „You want this one. Your partner wants that one. The great bedroom deba…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1068419246180894) · [share](https://app.gethookd.ai/share/ad/157492484?signature=2cca06d67ac0d22467469bed203baabc91303161e4978d73d36db1b726396560) |
| 305 | 157492483 | 1789447299065374 | 2026-08-25 | 2026-09-03 | 10 | Video | 23 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1789447299065374) · [share](https://app.gethookd.ai/share/ad/157492483?signature=c4b50c236e2d00a999958d39ca05bd33f4cf8da6fa45de77761fd2e8cac2f580) |
| 306 | 157492482 | 29044842228452116 | 2026-08-25 | 2026-08-28 | 4 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=29044842228452116) · [share](https://app.gethookd.ai/share/ad/157492482?signature=60f5f8823b70421f9e7a0e68b1f2cebd7c6a28ab6ecc58b0720954319d9f999c) |
| 307 | 157492481 | 1078447658460536 | 2026-08-25 | 2026-09-28 | 35 | Bild | – | Now In Super King | → **T27** (Anhang) „Our most requested size is finally here: the Pleene EasyRest in Super …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Neuheit/Größe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1078447658460536) · [share](https://app.gethookd.ai/share/ad/157492481?signature=a79cf57b76a32952a090c568ce8b11f833b15216715725029ac7b78610ea41fa) |
| 308 | 157492479 | 903208642489850 | 2026-08-25 | 2026-09-09 | 16 | Video | 42 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=903208642489850) · [share](https://app.gethookd.ai/share/ad/157492479?signature=68087b0d31abe2c31f607af0d6707cc5ebbc66e277a2dbe5c90d079cac29a4b7) |
| 309 | 157492478 | 2420769561780009 | 2026-08-25 | 2026-08-28 | 4 | Bild | – | Who Wins In Your House? | → **T28** (Anhang) „You want this one. Your partner wants that one. The great bedroom deba…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2420769561780009) · [share](https://app.gethookd.ai/share/ad/157492478?signature=33b0dee5afdb8c8e537404fa06fe93e4a7be923e15f2364042c4869e0cb58983) |
| 310 | 157492477 | 1962491847730660 | 2026-08-25 | 2026-09-10 | 17 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1962491847730660) · [share](https://app.gethookd.ai/share/ad/157492477?signature=18355d8f25762b105a0929b1b0bc652cc0348e7d048693619c2ef1e21d28ec4e) |
| 311 | 157492475 | 28310942411851184 | 2026-08-25 | 2026-08-28 | 4 | Video | 16 s | Hearth Red. Nearly gone. | → **T26** (Anhang) „Hearth Red is nearly sold out — and unlike most 'selling fast' claims,…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28310942411851184) · [share](https://app.gethookd.ai/share/ad/157492475?signature=5eb2d7f117c2b9294d3bb589fbaabf079f80f1faeade780115f4d8c9295cc156) |
| 312 | 157492474 | 1276406671182644 | 2026-08-25 | 2026-09-10 | 17 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1276406671182644) · [share](https://app.gethookd.ai/share/ad/157492474?signature=35a369839bdacf2e5f7a8333b7a5832d227e9d3445e7053ef4bbe19f3e9842f4) |
| 313 | 157492473 | 4546369339018467 | 2026-08-25 | 2026-08-29 | 5 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4546369339018467) · [share](https://app.gethookd.ai/share/ad/157492473?signature=3eaaac535b9780fa955d0915458de135634fc22a69ebcc784f9e461f46503df6) |
| 314 | 157492472 | 1825439511773317 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | I've Quit Bed Linen | → **T36** (Anhang) „I've quit bed linen. Completely. The Pleene EasyRest is duvet and cove…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1825439511773317) · [share](https://app.gethookd.ai/share/ad/157492472?signature=5b71cd123544e758cf706a1b48078891c4fc64e6687cc4f3247833117d7a5c9f) |
| 315 | 157492471 | 2112919846285525 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | I've Quit Bed Linen | → **T36** (Anhang) „I've quit bed linen. Completely. The Pleene EasyRest is duvet and cove…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2112919846285525) · [share](https://app.gethookd.ai/share/ad/157492471?signature=1fcc0b6e3f899dbfb6d7112768569574a3134c8a7685ab9e6af35cac7c818564) |
| 316 | 157492470 | 1705539210556149 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1705539210556149) · [share](https://app.gethookd.ai/share/ad/157492470?signature=145b0f5a9287037aa2910c3574c8e9c26286d5813a25ea7cb3fbcb5915e088f6) |
| 317 | 157492469 | 1633189931734399 | 2026-08-25 | 2026-09-09 | 16 | Video | 42 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1633189931734399) · [share](https://app.gethookd.ai/share/ad/157492469?signature=2ab48ef2e310e3e5f5b8d8b0cf1d9d0fa044931f396a5c67cb7692e07186451e) |
| 318 | 157492467 | 1078897054604867 | 2026-08-25 | 2026-08-28 | 4 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/pages/duvet-10r | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1078897054604867) · [share](https://app.gethookd.ai/share/ad/157492467?signature=3cf62701e1d688a71248fdf97c0c8ef346e1e0a23509bef2fa349d64780f97d3) |
| 319 | 157492466 | 1015702894758175 | 2026-08-25 | 2026-08-29 | 5 | Bild | – | I've Quit Bed Linen | → **T36** (Anhang) „I've quit bed linen. Completely. The Pleene EasyRest is duvet and cove…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | C, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1015702894758175) · [share](https://app.gethookd.ai/share/ad/157492466?signature=0773a1845fc8aca226fffc23042104b3df58e724899d6427ee7f03af8bc9b7a0) |
| 320 | 157492463 | 1368027478281052 | 2026-08-25 | 2026-09-28 | 35 | Bild | – | Now In Super King | → **T27** (Anhang) „Our most requested size is finally here: the Pleene EasyRest in Super …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Neuheit/Größe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1368027478281052) · [share](https://app.gethookd.ai/share/ad/157492463?signature=bad25402e96a220a3d79c6ce2124749d566abc055806c41e318d90758916a5cc) |
| 321 | 157492462 | 1748296249698720 | 2026-08-25 | 2026-08-29 | 5 | Video | 23 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1748296249698720) · [share](https://app.gethookd.ai/share/ad/157492462?signature=7bed1c94429100715f4f68291026c8adf46a9151be06eb875931d38a281fd7bd) |
| 322 | 157492461 | 1781304766393797 | 2026-08-25 | 2026-09-03 | 10 | Video | 24 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1781304766393797) · [share](https://app.gethookd.ai/share/ad/157492461?signature=6e1f515e391589eb7f883acac1309df6a90a1a79af527ccb467f5b7b150c8e9d) |
| 323 | 157492460 | 1361807279498461 | 2026-08-25 | 2026-09-09 | 16 | Video | 42 s | A Duvet With No Cover? | → **T05** (Anhang) „I only ordered it because the concept made me so curious. A duvet with…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1361807279498461) · [share](https://app.gethookd.ai/share/ad/157492460?signature=46cb95d3b92ff086d3f989881742367ec3f6f1806deb3a0b410f1c4fce0ee5cf) |
| 324 | 157492457 | 1923898135682926 | 2026-08-25 | 2026-09-10 | 17 | Video | 15 s | End Of Season Sale | → **T10** (Anhang) „End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Angebot, F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1923898135682926) · [share](https://app.gethookd.ai/share/ad/157492457?signature=bb080cf328e87d290b45ad859710ef65f3bd80ac7ba9f1cf5bdbb55a89f0f865) |
| 325 | 153409676 | 1569268328002827 | 2026-08-25 | 2026-09-05 | 12 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1569268328002827) · [share](https://app.gethookd.ai/share/ad/153409676?signature=0fbb52ca95460e169235e1af5b66b2ab13cbf3e41c07f92d200d1c2b0fa995ce) |
| 326 | 151454666 | 1054169594195589 | 2026-08-22 | 2026-09-01 | 11 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1054169594195589) · [share](https://app.gethookd.ai/share/ad/151454666?signature=b5b022b7178e6f18ca90d8a8264c96aaeb9dfd21e875426c288315c6d6ba1ab7) |
| 327 | 151025048 | 3301904860149799 | 2026-08-22 | 2026-08-24 | 3 | Video | 23 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Verlierer (<7 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3301904860149799) · [share](https://app.gethookd.ai/share/ad/151025048?signature=d07f71e93c7157b05227904578990a9b3cfdb976353663f49e73088bc69ae70f) |
| 328 | 151025064 | 2048346635781281 | 2026-08-20 | 2026-08-29 | 10 | Video | 29 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2048346635781281) · [share](https://app.gethookd.ai/share/ad/151025064?signature=eb694fd9122fc08f794241cadc7deb80a7ca245de812ee0ab6a87e52f386ce48) |
| 329 | 151025058 | 1603065724564054 | 2026-08-20 | 2026-08-28 | 9 | Video | 48 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 3 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1603065724564054) · [share](https://app.gethookd.ai/share/ad/151025058?signature=b76afbe777d30e880b15c86b9b676cbe87edba96db5c102dfd113f9141818b01) |
| 330 | 151024484 | 27652164324465851 | 2026-08-20 | 2026-09-06 | 18 | Video | 55 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=27652164324465851) · [share](https://app.gethookd.ai/share/ad/151024484?signature=5555cc7d70e4f43233475c24da1f7755ab20bc1e40acccc9504a37d536f9d34a) |
| 331 | 151024482 | 1046838818139502 | 2026-08-20 | 2026-08-26 | 7 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1046838818139502) · [share](https://app.gethookd.ai/share/ad/151024482?signature=6852e7e4c90a71c65762cc476ead0b4e6abfb8a59062fa34636ab0bbbb46a231) |
| 332 | 151024481 | 1040113395446847 | 2026-08-20 | 2026-08-29 | 10 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1040113395446847) · [share](https://app.gethookd.ai/share/ad/151024481?signature=3d8038b1a16ad1b2b582a12187bb46bfbd51109c504daf1d68525015f706d632) |
| 333 | 151024479 | 1869751867765792 | 2026-08-20 | 2026-09-06 | 18 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1869751867765792) · [share](https://app.gethookd.ai/share/ad/151024479?signature=98bbeb24e713532b65db7e743e09d13356e4e343bd9eb192581facc90ce307b4) |
| 334 | 151024477 | 1563180478681583 | 2026-08-20 | 2026-08-26 | 7 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1563180478681583) · [share](https://app.gethookd.ai/share/ad/151024477?signature=11c89d9b7522a8acf6f47f2babc07505ae3c83ae3d2923ee1e1a29baf493cd46) |
| 335 | 151024469 | 2914506212243187 | 2026-08-20 | 2026-09-06 | 18 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2914506212243187) · [share](https://app.gethookd.ai/share/ad/151024469?signature=a53d3634c865af4af3c9e6dde45fa3eeabc6611f4ec67feaba0d4d09013a9591) |
| 336 | 151024468 | 1786479932794070 | 2026-08-20 | 2026-08-26 | 7 | Bild | – | The Cover Is Sewn In | → **T48** (Anhang) „The cover is sewn in. That is the whole idea. No changing, no wrestlin…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1786479932794070) · [share](https://app.gethookd.ai/share/ad/151024468?signature=b326bc87aa1da49925d0994b4c87ed11bdcd1d5ebc9a71550df4964d4c26eb23) |
| 337 | 151024466 | 1619394593087784 | 2026-08-20 | 2026-09-03 | 15 | Video | 20 s | Which One Is Our Bestseller? | → **T46** (Anhang) „One of these nine is our bestseller — and it's nearly sold out again. …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1619394593087784) · [share](https://app.gethookd.ai/share/ad/151024466?signature=7c615a4cfb715cbe81f4b3f8f3c73f928eacf946544ae62eb914a39d175ef166) |
| 338 | 151024464 | 1774506470235275 | 2026-08-20 | 2026-09-05 | 17 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-everyday-duvet | n/a | 2 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1774506470235275) · [share](https://app.gethookd.ai/share/ad/151024464?signature=bbcbe6dcf2a580fd9c61363c517f3da3cbb9cd95012ada272ea74a7e2b8b3a08) |
| 339 | 151024462 | 1748314246205468 | 2026-08-20 | 2026-09-03 | 15 | Video | 20 s | Which One Is Our Bestseller? | → **T46** (Anhang) „One of these nine is our bestseller — and it's nearly sold out again. …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1748314246205468) · [share](https://app.gethookd.ai/share/ad/151024462?signature=996a47930b9026c22888463cf46885483c90ab77aaa663a1fb41b30c0608f155) |
| 340 | 151024458 | 2326706541470957 | 2026-08-20 | 2026-08-26 | 7 | Bild | – | The Cover Is Sewn In | → **T48** (Anhang) „The cover is sewn in. That is the whole idea. No changing, no wrestlin…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2326706541470957) · [share](https://app.gethookd.ai/share/ad/151024458?signature=fa6095d3df2d4b2199fe27bfb0d1fc3be2e8d23a258edd2baf66f7e388e7f36a) |
| 341 | 151024448 | 1412875314079376 | 2026-08-20 | 2026-09-06 | 18 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1412875314079376) · [share](https://app.gethookd.ai/share/ad/151024448?signature=b72edcca53634369e895e5d6809e3b855f7f12dc859e3175d07ec712cb9a8b15) |
| 342 | 151024446 | 1096349936261560 | 2026-08-20 | 2026-08-26 | 7 | Bild | – | The Cover Is Sewn In | → **T48** (Anhang) „The cover is sewn in. That is the whole idea. No changing, no wrestlin…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1096349936261560) · [share](https://app.gethookd.ai/share/ad/151024446?signature=56b889037aca7d8aff1f246f1142aee9caa2a0f8538bf3af48efd028c8450c8f) |
| 343 | 151024439 | 1087187533876380 | 2026-08-20 | 2026-09-03 | 15 | Video | 20 s | Which One Is Our Bestseller? | → **T46** (Anhang) „One of these nine is our bestseller — and it's nearly sold out again. …“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1087187533876380) · [share](https://app.gethookd.ai/share/ad/151024439?signature=cf1fe5b8587fb26511de3798ebd8e6a4e5e07cc30fb1ebe8830d013bd3cfb6b9) |
| 344 | 151024437 | 1984809562359390 | 2026-08-20 | 2026-09-06 | 18 | Video | 49 s | The Duvet You Can Actually Wash | → **T09** (Anhang) „You shower every night — then sleep under a duvet that's never been wa…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1984809562359390) · [share](https://app.gethookd.ai/share/ad/151024437?signature=b7277e42ba999fb844faeb98ffa00492a4f81126f4e9aef374a376d3be23e904) |
| 345 | 151025056 | 1065365702538507 | 2026-08-19 | 2026-09-01 | 14 | Video | 48 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1065365702538507) · [share](https://app.gethookd.ai/share/ad/151025056?signature=0f66fe8183ca7bc51921273343ace78d5db0829da205dedcc0f4fe1cf66abd78) |
| 346 | 148470055 | 1044423091779881 | 2026-08-18 | 2026-08-24 | 7 | Video | 40 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1044423091779881) · [share](https://app.gethookd.ai/share/ad/148470055?signature=74af97946434ea4cf5e606ef1839b04f8026938f14d18f22075465e487a7e0fb) |
| 347 | 148470084 | 1629563352178769 | 2026-08-17 | 2026-08-28 | 12 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1629563352178769) · [share](https://app.gethookd.ai/share/ad/148470084?signature=84bcfb60bb6282987d2f3a92dca22064c8d27361465bd07db7e76c7522647458) |
| 348 | 148470083 | 1596291422164585 | 2026-08-17 | 2026-08-28 | 12 | Video | 37 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1596291422164585) · [share](https://app.gethookd.ai/share/ad/148470083?signature=7b0f0498accdefa57b2109b9dd44fb6a2cdd5079954052f8e7f9594bc27fb580) |
| 349 | 148470082 | 1060411050313798 | 2026-08-17 | 2026-08-28 | 12 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1060411050313798) · [share](https://app.gethookd.ai/share/ad/148470082?signature=be9091c219c91afdca393345c4e68bea81dafed3a19ca5425378181efe902587) |
| 350 | 148470081 | 1371005181233258 | 2026-08-17 | 2026-08-27 | 11 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1371005181233258) · [share](https://app.gethookd.ai/share/ad/148470081?signature=9952b80e2f0b3921965ec9dd918d14f7ec4d2efcf51487b8b68bbf6d695aa295) |
| 351 | 148470080 | 1056968210311063 | 2026-08-17 | 2026-08-28 | 12 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1056968210311063) · [share](https://app.gethookd.ai/share/ad/148470080?signature=59beea508aa3ba02974db19c590993ff5478b366c7690889d1c4ed8d55a79a1f) |
| 352 | 148470070 | 2301093177301755 | 2026-08-17 | 2026-08-21 | 5 | Video | 40 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2301093177301755) · [share](https://app.gethookd.ai/share/ad/148470070?signature=1494deb455ef2f7af2394ffaefdffbbc74a8a0f5fc2dc4965debd2bf1bd1c3e4) |
| 353 | 148470066 | 1064404466239652 | 2026-08-17 | 2026-08-21 | 5 | Video | 39 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1064404466239652) · [share](https://app.gethookd.ai/share/ad/148470066?signature=8b45b88137ac4ce24c7f74dc339f2ec4496d5f8363a509deaf2c6af4033164c8) |
| 354 | 148470063 | 1318852313660983 | 2026-08-17 | 2026-08-21 | 5 | Video | 38 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1318852313660983) · [share](https://app.gethookd.ai/share/ad/148470063?signature=6b3c52d047a550d932f8ab20edb45e47ed8178c847592cd16498849cd72454e4) |
| 355 | 148470057 | 1036133439179976 | 2026-08-17 | 2026-08-27 | 11 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1036133439179976) · [share](https://app.gethookd.ai/share/ad/148470057?signature=a6280b140a84258a5ef9b160857d5b4143026e7ef2efca8579ca96b463b0f887) |
| 356 | 148470052 | 2034537413848091 | 2026-08-17 | 2026-08-21 | 5 | Video | 38 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2034537413848091) · [share](https://app.gethookd.ai/share/ad/148470052?signature=07eda101a2d1fc014b6521fc78879fe5233a0d079e31aaa14a732c8d68d88223) |
| 357 | 148470051 | 2089139941674812 | 2026-08-17 | 2026-08-21 | 5 | Video | 30 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2089139941674812) · [share](https://app.gethookd.ai/share/ad/148470051?signature=e93174c6e0855912b409f45a0e286bd763cb40328817e95af679f2dc6bdb0472) |
| 358 | 148470050 | 1378606943654097 | 2026-08-17 | 2026-08-21 | 5 | Video | 20 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1378606943654097) · [share](https://app.gethookd.ai/share/ad/148470050?signature=dfabf2d52d1fa7ff51d748fdb2763651614908eb9df5d6eca8295b86e1111704) |
| 359 | 148470048 | 1821943842572215 | 2026-08-17 | 2026-08-21 | 5 | Bild | – | Never lift your mattress again. | → **T51** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1821943842572215) · [share](https://app.gethookd.ai/share/ad/148470048?signature=1021f57230380bffc5d59e5cc238361f76f8b38e1abd5b369ba33f3ef17e631c) |
| 360 | 148470042 | 1892456801721570 | 2026-08-17 | 2026-08-21 | 5 | Video | 63 s | Never lift your mattress again. | → **T35** (Anhang) „I just didn't have the strength — or the patience — to lift my mattres…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1892456801721570) · [share](https://app.gethookd.ai/share/ad/148470042?signature=bdfcef67290d2b2bf252d3115a52a178b8704cf7988e66e90a388feb1571b6ff) |
| 361 | 145704163 | 1390280413109522 | 2026-08-15 | 2026-08-21 | 7 | Video | 18 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1390280413109522) · [share](https://app.gethookd.ai/share/ad/145704163?signature=81c86b66323e4b4e64b59d5f492311bfd8d68b2e3843610cf1dfa5fe7ac3269d) |
| 362 | 145704161 | 1385864409628179 | 2026-08-15 | 2026-08-21 | 7 | Video | 18 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1385864409628179) · [share](https://app.gethookd.ai/share/ad/145704161?signature=b08605adbb99efa510a5b77141adb3705ef1b90b0e4a110fe5f60d1a1dce5ba7) |
| 363 | 145704160 | 1526918582090276 | 2026-08-15 | 2026-08-21 | 7 | Video | 20 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1526918582090276) · [share](https://app.gethookd.ai/share/ad/145704160?signature=382c8d478364e22c04d6c323df8705a0b3c639885a34cbc44926dd624a0fbdf6) |
| 364 | 145443338 | 1074630778843581 | 2026-08-15 | 2026-09-07 | 24 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1074630778843581) · [share](https://app.gethookd.ai/share/ad/145443338?signature=8ac29f47b1fd0547ab037cbf9f8820e7a3fb58e2a1847da482684362cfe8bdb3) |
| 365 | 145443315 | 2700523520343460 | 2026-08-15 | 2026-09-01 | 18 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2700523520343460) · [share](https://app.gethookd.ai/share/ad/145443315?signature=d3b29f7cc8330c998a5334081fdd27c65a0a96554f7532805d328b59ec8cd902) |
| 366 | 145443350 | 2378264689411105 | 2026-08-14 | 2026-09-07 | 25 | Video | 16 s | Mint Green is almost gone. | → **T08** (Anhang) „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if y…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, F-Angebot, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2378264689411105) · [share](https://app.gethookd.ai/share/ad/145443350?signature=c2a3da465bdab55bf0d2de761984f9338ab07ee6b3f8986fa5b8818406fffbff) |
| 367 | 145443347 | 1738067994284895 | 2026-08-14 | 2026-09-07 | 25 | Video | 37 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1738067994284895) · [share](https://app.gethookd.ai/share/ad/145443347?signature=0f4db10cea223c1dcc650cac2574481cbbf9b3e86128e4b0c71f41b9cfc31a62) |
| 368 | 145443344 | 1039722162271817 | 2026-08-14 | 2026-08-18 | 5 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Verlierer (<7 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1039722162271817) · [share](https://app.gethookd.ai/share/ad/145443344?signature=61d373a6271fbf33568a0c96f34c3f204bd461bbfea756103ed87d4696e860d5) |
| 369 | 145443342 | 3432447646935956 | 2026-08-14 | 2026-09-01 | 19 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3432447646935956) · [share](https://app.gethookd.ai/share/ad/145443342?signature=03e75839e950bceb44d7edc2e360100bbb743dbfcbab8328d00ecce9a0add795) |
| 370 | 145443340 | 937322868660942 | 2026-08-14 | 2026-09-19 | 37 | Bild | – | What bed have you got? | → **T17** (Anhang) „Not sure which size? It's easier than duvet shopping usually is: Singl…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=937322868660942) · [share](https://app.gethookd.ai/share/ad/145443340?signature=16e5742c4db77b5e7bba52412bce46bd9e1b48b5cf894d96de978e05ba364722) |
| 371 | 145443335 | 1394373306132074 | 2026-08-14 | 2026-08-21 | 8 | Bild | – | What bed have you got? | → **T17** (Anhang) „Not sure which size? It's easier than duvet shopping usually is: Singl…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1394373306132074) · [share](https://app.gethookd.ai/share/ad/145443335?signature=f9e5498211890da025149ba3284c3b116e038312dcfd65fd963d54774b879187) |
| 372 | 145443333 | 1546588980558663 | 2026-08-14 | 2026-08-26 | 13 | Bild | – | When Did You Last Wash Your Duvet? | → **T23** (Anhang) „When did you last wash your duvet? Not the cover — the duvet. If you c…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1546588980558663) · [share](https://app.gethookd.ai/share/ad/145443333?signature=c0f3b18dfe3dafbfba72368d137068bdbc949ae670fa98e2eae0df6a275292ac) |
| 373 | 145443332 | 1047080881057215 | 2026-08-14 | 2026-08-26 | 13 | Bild | – | When Did You Last Wash Your Duvet? | → **T23** (Anhang) „When did you last wash your duvet? Not the cover — the duvet. If you c…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1047080881057215) · [share](https://app.gethookd.ai/share/ad/145443332?signature=dde91ae1b473828547686e690328735c85d5a955677b88431737cb7d4250a080) |
| 374 | 145443329 | 1369083151996528 | 2026-08-14 | 2026-08-22 | 9 | Bild | – | Which Colour Survives? | → **T43** (Anhang) „Nine colours. One has to go forever — which number gets deleted? Choos…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1369083151996528) · [share](https://app.gethookd.ai/share/ad/145443329?signature=a5852ae097a6e201e07acebdbc11efb1eed2af23b6b9900cce7d0f6194070f11) |
| 375 | 145443328 | 1073865045064863 | 2026-08-14 | 2026-09-28 | 46 | Bild | – | Who Wins In Your House? | → **T28** (Anhang) „You want this one. Your partner wants that one. The great bedroom deba…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Knappheit/Farbe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1073865045064863) · [share](https://app.gethookd.ai/share/ad/145443328?signature=21756bad808a39b6810c19993600f40703e80b8975676dee769dc8dbcec4b43d) |
| 376 | 145443324 | 1580155590567953 | 2026-08-14 | 2026-10-06 | 54 | Bild | – | Who Wins In Your House? | → **T28** (Anhang) „You want this one. Your partner wants that one. The great bedroom deba…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Knappheit/Farbe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1580155590567953) · [share](https://app.gethookd.ai/share/ad/145443324?signature=dcc958d471b824d4955e38f9f510a978f9185438d4c38c0fa24d621c143bc2c1) |
| 377 | 145443321 | 27941822298789563 | 2026-08-14 | 2026-08-22 | 9 | Bild | – | Which Colour Survives? | → **T43** (Anhang) „Nine colours. One has to go forever — which number gets deleted? Choos…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=27941822298789563) · [share](https://app.gethookd.ai/share/ad/145443321?signature=f239acab718a0c9260c3da075652628b9a1fff2c67a0bcb7d0627b1d8da48b5f) |
| 378 | 145443320 | 1027409520213921 | 2026-08-14 | 2026-09-13 | 31 | Video | 47 s | Everyone said it. They were right. | → **T04** (Anhang) „I only ordered it because everyone said you never have to change the b…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1027409520213921) · [share](https://app.gethookd.ai/share/ad/145443320?signature=439640c36173f599b8515b7d30d7e8e4325c232d122781f0cd60a580062dd92d) |
| 379 | 145443319 | 1549185346074210 | 2026-08-14 | 2026-08-21 | 8 | Karussell | 1 Video(s): 30 s; 2 Bild(er) | Never lift your mattress again. | ⭐️⭐️⭐️⭐️⭐️ Over 10,000 happy customers | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1549185346074210) · [share](https://app.gethookd.ai/share/ad/145443319?signature=266e5c411eaf9edd0769382a3fd5d845e5a499af363067ced0b822d0a4d3aef4) |
| 380 | 145443312 | 1587079409878071 | 2026-08-14 | 2026-08-22 | 9 | Bild | – | Who Wins In Your House? | → **T28** (Anhang) „You want this one. Your partner wants that one. The great bedroom deba…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1587079409878071) · [share](https://app.gethookd.ai/share/ad/145443312?signature=ef15113dd67d09346bfd4e23359a8d65c81fbcb4d3a79ebb3880be8c88f2887d) |
| 381 | 145443310 | 1062448459632194 | 2026-08-14 | 2026-08-22 | 9 | Bild | – | When Did You Last Wash Your Duvet? | → **T23** (Anhang) „When did you last wash your duvet? Not the cover — the duvet. If you c…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1062448459632194) · [share](https://app.gethookd.ai/share/ad/145443310?signature=fb744b25934468ff367f23feb3fd05c4f2a3b0dabfd7246a3dc074535174e1ed) |
| 382 | 145443298 | 1668586550892687 | 2026-08-14 | 2026-09-01 | 19 | Video | 26 s | Duvet & Cover In One | → **T13** (Anhang) „Throw it on. Done. The Pleene EasyRest is duvet and cover in one — mak…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1668586550892687) · [share](https://app.gethookd.ai/share/ad/145443298?signature=4f60a9373b11bdea350a6c4926484ae80a8c5824573fec3bf984aaf9a1bee3fe) |
| 383 | 145443292 | 1893990084896632 | 2026-08-14 | 2026-08-22 | 9 | Bild | – | Which Colour Survives? | → **T43** (Anhang) „Nine colours. One has to go forever — which number gets deleted? Choos…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1893990084896632) · [share](https://app.gethookd.ai/share/ad/145443292?signature=23dcde615b82b02fb5a0556efe313a0dd827552789981b61c5b4231451bfa9b9) |
| 384 | 145443282 | 1642682714085833 | 2026-08-14 | 2026-09-19 | 37 | Bild | – | What bed have you got? | → **T17** (Anhang) „Not sure which size? It's easier than duvet shopping usually is: Singl…“ | ORDER_NOW („Order now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Einwand/Kaufhilfe | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1642682714085833) · [share](https://app.gethookd.ai/share/ad/145443282?signature=45cc510ddcc3d6aac86f8012d62c00861c0c39924b6db4256e8aefcf120c073d) |
| 385 | 144538448 | 1958958918100454 | 2026-08-14 | 2026-08-18 | 5 | Video | 29 s | Not your normal fitted sheet | → **T50** (Anhang) „This is not your normal fitted sheet: the base stays on your mattress …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1958958918100454) · [share](https://app.gethookd.ai/share/ad/144538448?signature=883dc6c733e047737588261bec31c92b182852ddc445b2570c0be9a6ec527ed8) |
| 386 | 144538678 | 1376656558001397 | 2026-08-13 | 2026-09-07 | 26 | Bild | – | Made for hands that hurt | → **T21** (Anhang) „My hands decide what I can do these days. Changing the bed used to be …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1376656558001397) · [share](https://app.gethookd.ai/share/ad/144538678?signature=aff9915d3fc3a02d22fe3ca82e30d610ec2cee0b116a9013d0e35e9a4dbee535) |
| 387 | 144538462 | 903629772362028 | 2026-08-13 | 2026-08-21 | 9 | Video | 60 s | Never lift your mattress again. | → **T35** (Anhang) „I just didn't have the strength — or the patience — to lift my mattres…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=903629772362028) · [share](https://app.gethookd.ai/share/ad/144538462?signature=f2514f09568f711656ab1d9013183c30a7c6dcb1a1b81e3d1f4d97e2dfe00710) |
| 388 | 144538461 | 1358924786406826 | 2026-08-13 | 2026-08-18 | 6 | Video | 29 s | Not your normal fitted sheet | → **T50** (Anhang) „This is not your normal fitted sheet: the base stays on your mattress …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1358924786406826) · [share](https://app.gethookd.ai/share/ad/144538461?signature=47130893fdf6bcc9c0a56ab8393eb4c52bdb0390703525e7426479561565cf0d) |
| 389 | 144538460 | 1106183011734357 | 2026-08-13 | 2026-09-07 | 26 | Bild | – | Never lift your mattress again | → **T49** (Anhang) „The number one question we get: "How does the base get on the mattress…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | F-Einwand/Kaufhilfe, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1106183011734357) · [share](https://app.gethookd.ai/share/ad/144538460?signature=6be2d3f8c47cb73a3b6468828f1e9b577ad6149414b85b542dcddb6554416f69) |
| 390 | 144538456 | 1742083596707903 | 2026-08-13 | 2026-09-07 | 26 | Bild | – | Made for hands that hurt | → **T21** (Anhang) „My hands decide what I can do these days. Changing the bed used to be …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1742083596707903) · [share](https://app.gethookd.ai/share/ad/144538456?signature=0d15b9e9a3724915145f94500bf0d3a7b47dcd6a98adff6794aacb9e6a8c8f93) |
| 391 | 144538454 | 4420119828248164 | 2026-08-13 | 2026-08-21 | 9 | Video | 60 s | Never lift your mattress again. | → **T35** (Anhang) „I just didn't have the strength — or the patience — to lift my mattres…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=4420119828248164) · [share](https://app.gethookd.ai/share/ad/144538454?signature=cd730f055f4ab266aef01e80925ab7d947238867ea684cfc48be516350c9187c) |
| 392 | 144538452 | 1349792887223259 | 2026-08-13 | 2026-09-07 | 26 | Bild | – | Never lift your mattress again | → **T49** (Anhang) „The number one question we get: "How does the base get on the mattress…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | F-Einwand/Kaufhilfe, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1349792887223259) · [share](https://app.gethookd.ai/share/ad/144538452?signature=4c5acd074377887c8407db64e781529076f73ff0e5e82f5d91666acbb1c7b1e4) |
| 393 | 144538445 | 1049450258054308 | 2026-08-13 | 2026-09-07 | 26 | Bild | – | Made for hands that hurt | → **T21** (Anhang) „My hands decide what I can do these days. Changing the bed used to be …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1049450258054308) · [share](https://app.gethookd.ai/share/ad/144538445?signature=70dee626d8286f7fec7218efa55e2e8d60dcfb11e66afbb421b54ed16c3781a2) |
| 394 | 144538444 | 1720203672386621 | 2026-08-13 | 2026-08-21 | 9 | Video | 63 s | Never lift your mattress again. | → **T35** (Anhang) „I just didn't have the strength — or the patience — to lift my mattres…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1720203672386621) · [share](https://app.gethookd.ai/share/ad/144538444?signature=aec3041e3dbff451d15f613f0f35fa9a0bcdd3af5aadf13dbf1dbd7ae62c51be) |
| 395 | 144538443 | 1621543769568759 | 2026-08-13 | 2026-08-18 | 6 | Video | 29 s | Not your normal fitted sheet | → **T50** (Anhang) „This is not your normal fitted sheet: the base stays on your mattress …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1621543769568759) · [share](https://app.gethookd.ai/share/ad/144538443?signature=5f8d34f70af38a48dfbdd164ad91af739f281193ec367232f43ffc5006bf22f7) |
| 396 | 144538441 | 1605504207829012 | 2026-08-13 | 2026-09-07 | 26 | Bild | – | Never lift your mattress again | → **T49** (Anhang) „The number one question we get: "How does the base get on the mattress…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 3 | Inaktiv (7–29 T.) | F-Einwand/Kaufhilfe, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1605504207829012) · [share](https://app.gethookd.ai/share/ad/144538441?signature=1bf67239300f5554ae1b06fc0edee2951957868b3665043ab467e734a8b75b76) |
| 397 | 144538440 | 2324305058330745 | 2026-08-13 | 2026-08-18 | 6 | Video | 21 s | Not your normal fitted sheet | Never lift your mattress again: only the top sheet comes off — the base stays on your mattress forever. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2324305058330745) · [share](https://app.gethookd.ai/share/ad/144538440?signature=9d832ad98d6ba8a4a8277766ba915987fcbefcc53c49818951433b388d556daa) |
| 398 | 144538679 | 1100906412446119 | 2026-08-12 | 2026-08-22 | 11 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 3 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1100906412446119) · [share](https://app.gethookd.ai/share/ad/144538679?signature=58eb77e1328855120e815ac20b2268df01d826d18641cd7d0d6523d8e9b2d959) |
| 399 | 143044543 | 2009665866382873 | 2026-08-12 | 2026-08-22 | 11 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2009665866382873) · [share](https://app.gethookd.ai/share/ad/143044543?signature=c612ad2aab81ded9655c31fc52ba660724258297e0aae00799e17df4fb79cc8d) |
| 400 | 143044541 | 2269761180455210 | 2026-08-12 | 2026-08-22 | 11 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2269761180455210) · [share](https://app.gethookd.ai/share/ad/143044541?signature=8d7ffac013d9e4cc9a20c218a7838e1529c1321d1ab87d78cbdd2ba9042ab4f6) |
| 401 | 143044538 | 1043168664973988 | 2026-08-12 | 2026-08-21 | 10 | Video | 33 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1043168664973988) · [share](https://app.gethookd.ai/share/ad/143044538?signature=406cc846ccca7a28e4595161465c5e54ac5ac460cc7a85aa3d0b1ffa3d0dca6f) |
| 402 | 143044532 | 1580460996817349 | 2026-08-12 | 2026-08-21 | 10 | Video | 29 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1580460996817349) · [share](https://app.gethookd.ai/share/ad/143044532?signature=00bbb804f343ce6e86af31661e74dba9e06fa4b6138e386ce2d2434b8cb45c50) |
| 403 | 143044483 | 1349516040673176 | 2026-08-12 | 2026-08-21 | 10 | Video | 29 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1349516040673176) · [share](https://app.gethookd.ai/share/ad/143044483?signature=52ab25b54730dfdd11a647d217eebfc59330b60e3cd1cebca740029cbadd3375) |
| 404 | 143044458 | 1592936229030823 | 2026-08-12 | 2026-08-28 | 17 | Video | 27 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1592936229030823) · [share](https://app.gethookd.ai/share/ad/143044458?signature=26b33dd319fc8b3356378f2082c0b8734a83f01eeab896716469ef2024030bc0) |
| 405 | 143044453 | 2119297005668572 | 2026-08-12 | 2026-08-28 | 17 | Video | 29 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2119297005668572) · [share](https://app.gethookd.ai/share/ad/143044453?signature=4dc89ba060d70e6e9402d258035de9f81d7ad2aa2ac5b59e93b2a1222d0ac7fd) |
| 406 | 143044452 | 2051427139079670 | 2026-08-12 | 2026-08-22 | 11 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 3 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2051427139079670) · [share](https://app.gethookd.ai/share/ad/143044452?signature=b47768d0d99c4ca2a39d0c63fe3d2cfbd31f953cac7d5a64233cee8a1053effc) |
| 407 | 143044440 | 2241138083306217 | 2026-08-12 | 2026-08-28 | 17 | Video | 30 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2241138083306217) · [share](https://app.gethookd.ai/share/ad/143044440?signature=e44dd30792a2c353ed5fac127373274d9d3b051e50f504717650d4d68e059125) |
| 408 | 143044433 | 1527062372030147 | 2026-08-12 | 2026-08-22 | 11 | Bild | – | Never lift your mattress again. | → **T51** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1527062372030147) · [share](https://app.gethookd.ai/share/ad/143044433?signature=826148b4724730fcb265efd296df7066cf13396d549613b9aecd597b6603d822) |
| 409 | 141368548 | 1380666784199574 | 2026-08-10 | 2026-09-07 | 29 | Video | 40 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1380666784199574) · [share](https://app.gethookd.ai/share/ad/141368548?signature=2bfe7f20c8aa72c329906b72c9d95eeeaca517e5723ebd70a73d893b6666a601) |
| 410 | 141368443 | 1692150768534132 | 2026-08-10 | 2026-08-13 | 4 | Video | 50 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1692150768534132) · [share](https://app.gethookd.ai/share/ad/141368443?signature=04dbd77de5710410c7b1387ea3344ba8ef4858efeea984e553dde807972befab) |
| 411 | 141368434 | 3581013772056531 | 2026-08-10 | 2026-08-16 | 7 | Video | 25 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=3581013772056531) · [share](https://app.gethookd.ai/share/ad/141368434?signature=2283c3d792f4580fcbf5ccf70733ca46ab130385ed972199839fbedf554f2c31) |
| 412 | 141368431 | 1475185867961398 | 2026-08-10 | 2026-09-07 | 29 | Video | 38 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1475185867961398) · [share](https://app.gethookd.ai/share/ad/141368431?signature=56d6510d29f8ae744ea3a6d2d5d6b9044a945d7193afc3d9a523dd461864dc12) |
| 413 | 141368423 | 1743555873642452 | 2026-08-10 | 2026-09-07 | 29 | Video | 39 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1743555873642452) · [share](https://app.gethookd.ai/share/ad/141368423?signature=9c46a4f772467785e3b5dcd9e9c4bf3fcc80670de7e8d4becbabdd03e4aee73e) |
| 414 | 141368643 | 4606822172882382 | 2026-08-09 | 2026-08-29 | 21 | DCO | 2 Bild(er) | n/a | → **T24** (Anhang) „{{product.brand}}…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv (7–29 T.) | n/a (Platzhalter-Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4606822172882382) · [share](https://app.gethookd.ai/share/ad/141368643?signature=d9cb1c458e98f7b2672e51755bbbf5b0e4c5eab8e8ee87c4d702e9034cda0c12) |
| 415 | 141368639 | 1830971708059484 | 2026-08-09 | 2026-09-26 | 49 | DCO | 2 Bild(er) | n/a | → **T24** (Anhang) „{{product.brand}}…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | n/a (Platzhalter-Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1830971708059484) · [share](https://app.gethookd.ai/share/ad/141368639?signature=1b542dbd1ba1767b702af28724d05557991cf43421578ccfd2210617ecbd9f30) |
| 416 | 141368634 | 1738762820597769 | 2026-08-09 | 2026-09-26 | 49 | DCO | 2 Bild(er) | n/a | → **T24** (Anhang) „{{product.brand}}…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | n/a (Platzhalter-Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1738762820597769) · [share](https://app.gethookd.ai/share/ad/141368634?signature=c2c7bf617728ea211ec7f459a13c57ebc1141d48f5378fe963924cde98ed3845) |
| 417 | 141368619 | 844560458740490 | 2026-08-09 | 2026-08-18 | 10 | DCO | 2 Bild(er) | n/a | → **T24** (Anhang) „{{product.brand}}…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv (7–29 T.) | n/a (Platzhalter-Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=844560458740490) · [share](https://app.gethookd.ai/share/ad/141368619?signature=9c777c0d2fdff1cf14ba25db3cc17a1ad35509b5e4f66852983fbc326f9e65ca) |
| 418 | 141368543 | 27392633277085803 | 2026-08-09 | 2026-08-16 | 8 | Video | 19 s | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=27392633277085803) · [share](https://app.gethookd.ai/share/ad/141368543?signature=59461ea698f5c3bb9296e2eb098ae6d655258b0dd9d3a3d752a48dba84f02ab6) |
| 419 | 141368447 | 1969587817077218 | 2026-08-09 | 2026-08-16 | 8 | Video | 25 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1969587817077218) · [share](https://app.gethookd.ai/share/ad/141368447?signature=0e50d20959be385edd193c6d8aa7cb7de6790a22de7e80ba22908dd2a9c41b95) |
| 420 | 141368437 | 1372413497637661 | 2026-08-09 | 2026-08-16 | 8 | Video | 19 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1372413497637661) · [share](https://app.gethookd.ai/share/ad/141368437?signature=c69bd49b2c5a55ecfe4912d3e81e9f6d5e4ca2a8dad3f17fe24fe1711303668d) |
| 421 | 141368436 | 1605124174624622 | 2026-08-09 | 2026-08-16 | 8 | Video | 19 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1605124174624622) · [share](https://app.gethookd.ai/share/ad/141368436?signature=63e08212648aebb843f0fa21a23890fb40c14a404a30139ad49839103984c125) |
| 422 | 141368428 | 1760374211782557 | 2026-08-09 | 2026-08-27 | 19 | Video | 37 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1760374211782557) · [share](https://app.gethookd.ai/share/ad/141368428?signature=d554ce01dcdd5555015817ca9af5fa41b18fac8f9c36fb641deb5033e7ca22da) |
| 423 | 141368420 | 1087597353603207 | 2026-08-09 | 2026-08-27 | 19 | Video | 39 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1087597353603207) · [share](https://app.gethookd.ai/share/ad/141368420?signature=b104e9ac8e99a1c044186013abd94d9df7acb50f41b578423d5c6d656ca359ad) |
| 424 | 141368416 | 1625178769163998 | 2026-08-09 | 2026-08-16 | 8 | Video | 25 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1625178769163998) · [share](https://app.gethookd.ai/share/ad/141368416?signature=25bb457002b6667bae64fefc42b08de1a4d31a9d6044996cb17f16e781ba95d5) |
| 425 | 141368410 | 1040621305378136 | 2026-08-09 | 2026-08-27 | 19 | Video | 40 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1040621305378136) · [share](https://app.gethookd.ai/share/ad/141368410?signature=de0b2d716c3494788a99c030f085d4e0fd922a085970664b3ad3e894bbcdb8f9) |
| 426 | 139561401 | 1374570724806646 | 2026-08-08 | 2026-08-21 | 14 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1374570724806646) · [share](https://app.gethookd.ai/share/ad/139561401?signature=624671e71c929fcbb32236377299451718adb3a4a7e588704ca68374d3fa74d7) |
| 427 | 139561358 | 2250098979162898 | 2026-08-08 | 2026-08-11 | 4 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2250098979162898) · [share](https://app.gethookd.ai/share/ad/139561358?signature=123c971ebdbc3bae64dcd1cbfcfbb1450fb929337c689910be60ebc3d17d1594) |
| 428 | 139561003 | 1061887276489463 | 2026-08-08 | 2026-08-11 | 4 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1061887276489463) · [share](https://app.gethookd.ai/share/ad/139561003?signature=4ab2075d47422e21e9a812d8cc824d54ff8fb77fab21099ff8a40537904a638b) |
| 429 | 139560997 | 1044318828574742 | 2026-08-08 | 2026-08-21 | 14 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1044318828574742) · [share](https://app.gethookd.ai/share/ad/139560997?signature=a1205f0e4b0b2fd9c7c97a9cec4855337c0653a4ad136059288c60f178e4c15d) |
| 430 | 139560993 | 1974393473279543 | 2026-08-08 | 2026-08-11 | 4 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1974393473279543) · [share](https://app.gethookd.ai/share/ad/139560993?signature=c7b89329aa0b82bfc06195199fe13c8b7930cdcc641789f6ecae964f17432854) |
| 431 | 139561522 | 1690354895371776 | 2026-08-07 | 2026-09-28 | 53 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1690354895371776) · [share](https://app.gethookd.ai/share/ad/139561522?signature=f7641e4d380301b573b3c68bc2dcbeb4e08fda6c51cf27cdc64e0e30b9bc690c) |
| 432 | 139561518 | 1579050700440920 | 2026-08-07 | 2026-09-30 | 55 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1579050700440920) · [share](https://app.gethookd.ai/share/ad/139561518?signature=d72502de7ed81824137c8820524649b47c851f8f179ee0259df83195cfb82f6a) |
| 433 | 139561478 | 1682646723035195 | 2026-08-07 | 2026-08-28 | 22 | Bild | – | "Best thing I got for years." | → **T42** (Anhang) „"Best thing I got for years." — six words from a real customer, and ho…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1682646723035195) · [share](https://app.gethookd.ai/share/ad/139561478?signature=74f86b7d1229ce9918c96bfbc75d322669fa731af3432a01c91d6c83fa35d45e) |
| 434 | 139561473 | 1016454404593766 | 2026-08-07 | 2026-08-24 | 18 | Video | 56 s | n/a | n/a (leer) | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | n/a (kein Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1016454404593766) · [share](https://app.gethookd.ai/share/ad/139561473?signature=ccdf4921400e16be0e60389d128505ac99cdb1f32de06177562758d2b8ad29f5) |
| 435 | 139561448 | 1743141450271267 | 2026-08-07 | 2026-08-28 | 22 | Bild | – | "Best thing I got for years." | → **T42** (Anhang) „"Best thing I got for years." — six words from a real customer, and ho…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1743141450271267) · [share](https://app.gethookd.ai/share/ad/139561448?signature=4872a37679894c373114ab20741c1094a54c83fd6012717d74939937e2d8cf4c) |
| 436 | 139561419 | 2127706218160118 | 2026-08-07 | 2026-08-21 | 15 | Bild | – | Why people are switching. | There's a quiet switch happening in British bedrooms: out with the cover, in with the Pleene EasyRest™ — a duvet and cover in one. No wrestling, no separate bed linen, and the whole thing washes in a normal machine. | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C, A | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2127706218160118) · [share](https://app.gethookd.ai/share/ad/139561419?signature=0b980cd5b2d3a6806a8bf5bc77efb23c3402b9f2d9f794b5614c69b22efa301a) |
| 437 | 139561388 | 1007459772279636 | 2026-08-07 | 2026-08-21 | 15 | Video | 15 s | Pick a colour. Watch. | → **T06** (Anhang) „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Knappheit/Farbe, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1007459772279636) · [share](https://app.gethookd.ai/share/ad/139561388?signature=6f6e0916dfd15d8a8680849f0935eb3e752e19fc298fc7837daaa535df218eb0) |
| 438 | 139561387 | 1022624587205120 | 2026-08-07 | 2026-08-21 | 15 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1022624587205120) · [share](https://app.gethookd.ai/share/ad/139561387?signature=a3e4bf5c3ac64c4e4a8c34e0461f95b4921f5e9462415c4258baf0c23c2b1e1d) |
| 439 | 139561360 | 1366082289066214 | 2026-08-07 | 2026-08-24 | 18 | Video | 54 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1366082289066214) · [share](https://app.gethookd.ai/share/ad/139561360?signature=49c3565f980b1ec6b6d312c50a646529eb07a2332ad2449a96ab95b96f5f8c62) |
| 440 | 139561349 | 1077106241638635 | 2026-08-07 | 2026-08-24 | 18 | Video | 55 s | Best decision I ever made. | → **T11** (Anhang) „I don't have a duvet cover anymore — and it was honestly the best deci…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | F-Social-Proof, C | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1077106241638635) · [share](https://app.gethookd.ai/share/ad/139561349?signature=59d5270b25111911923164c3fcdab3c595dce7b497d6c7e89090c7e3e7ab9076) |
| 441 | 139561007 | 1613752890320348 | 2026-08-07 | 2026-08-21 | 15 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1613752890320348) · [share](https://app.gethookd.ai/share/ad/139561007?signature=9d5237cf63a81f6bbed58fd418b33f09a23f19bba0f834f7cec55ee6773f4351) |
| 442 | 139560990 | 1712037746699179 | 2026-08-07 | 2026-08-18 | 12 | Video | 18 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1712037746699179) · [share](https://app.gethookd.ai/share/ad/139560990?signature=7a7dbd16e32d72d761f33c9ec70875ffe00d4e9abce2dc2fa8321e023e3e6bda) |
| 443 | 139560984 | 2048119069141581 | 2026-08-07 | 2026-08-18 | 12 | Video | 20 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2048119069141581) · [share](https://app.gethookd.ai/share/ad/139560984?signature=19febae34852f3901ba92a01f3499af973c58962333d02483983cbbe9bd0d16b) |
| 444 | 139560976 | 1609013710575999 | 2026-08-07 | 2026-08-18 | 12 | Video | 18 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1609013710575999) · [share](https://app.gethookd.ai/share/ad/139560976?signature=5803680704d20849315029c62e0f9c66ecbc71fd67a9dfb11cd73698ead168c9) |
| 445 | 139560971 | 1370133432000783 | 2026-08-07 | 2026-08-11 | 5 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Verlierer (<7 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1370133432000783) · [share](https://app.gethookd.ai/share/ad/139560971?signature=7a43bdcc08a37246b998394ba04a7def356b6a68ac7349874b912c21d0eb0326) |
| 446 | 139560968 | 1372402600939624 | 2026-08-07 | 2026-08-21 | 15 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 4 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1372402600939624) · [share](https://app.gethookd.ai/share/ad/139560968?signature=94b442b2c400ee8f13e29316e01f950a72f11f84beb1835a22c3b8a3cca25e2e) |
| 447 | 136390198 | 2357310554802037 | 2026-08-05 | 2026-08-29 | 25 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2357310554802037) · [share](https://app.gethookd.ai/share/ad/136390198?signature=391e44c6ce58455322b55ca9aa76be8f5933fd9639609e8eeaa5ddc701ac3286) |
| 448 | 136390181 | 1063023972882365 | 2026-08-05 | 2026-09-26 | 53 | Video | 14 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1063023972882365) · [share](https://app.gethookd.ai/share/ad/136390181?signature=2fdc26262981f9072ba82f5682e47a5620d78569385993916b71e885a5d79578) |
| 449 | 136390163 | 1403615265199738 | 2026-08-05 | 2026-09-26 | 53 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1403615265199738) · [share](https://app.gethookd.ai/share/ad/136390163?signature=ff1ff4abc16e413a14c23bb444456994041fa290e32bddbe607ea607fab00b7a) |
| 450 | 136390115 | 1327742962471077 | 2026-08-05 | 2026-09-26 | 53 | Video | 47 s (ffprobe; GetHooked-Wert 0) | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1327742962471077) · [share](https://app.gethookd.ai/share/ad/136390115?signature=91338eddf0fd7c5c6e99bec2de2d2d10580cee04e026d1bfc549387830c039f2) |
| 451 | 136390102 | 2895295140832235 | 2026-08-05 | 2026-09-26 | 53 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2895295140832235) · [share](https://app.gethookd.ai/share/ad/136390102?signature=78f1f5aadcae3c3d74e711f9e7ca88c0d5b4d6230c9e5a41c0f4575ef345eb7e) |
| 452 | 136390079 | 1003603455838091 | 2026-08-05 | 2026-09-06 | 33 | Video | 25 s (ffprobe; GetHooked-Wert 0) | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1003603455838091) · [share](https://app.gethookd.ai/share/ad/136390079?signature=17415b51b507421e4c28adf740d08df6eec086a70b1f87cb81fd8ffad8e7e640) |
| 453 | 136389704 | 2488164531666082 | 2026-08-05 | 2026-08-29 | 25 | Video | 93 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/pleene-easyrest-duvet-2in1 | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2488164531666082) · [share](https://app.gethookd.ai/share/ad/136389704?signature=01891762a17993119970f8af162cf3da3745243142410cce61c4718eb87ee18d) |
| 454 | 136388826 | 954938290974827 | 2026-08-05 | 2026-09-08 | 35 | Video | 40 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=954938290974827) · [share](https://app.gethookd.ai/share/ad/136388826?signature=c6b6f69a3cae71df05f6bd6578441137c72b3bf2fcb32cfc0023e4065e1fe099) |
| 455 | 133365812 | 3016531412024707 | 2026-08-05 | 2026-09-08 | 35 | Video | 34 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3016531412024707) · [share](https://app.gethookd.ai/share/ad/133365812?signature=1b4a3e59dcdfc2b084e49e2b79fa8a8a684927eaa3616f9b93ce7e7617dd4e35) |
| 456 | 136388113 | 2125708415039670 | 2026-08-04 | 2026-09-05 | 33 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2125708415039670) · [share](https://app.gethookd.ai/share/ad/136388113?signature=179aca7330eb6a46cdc54004783388cca0f21913a8e5335a00daaf97ab73c374) |
| 457 | 133364896 | 1444482834179132 | 2026-08-04 | 2026-09-04 | 32 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1444482834179132) · [share](https://app.gethookd.ai/share/ad/133364896?signature=583a168fd68c4b76cd60ac6c5d5bb931332ffdbecbf3b418d515d4251dacc8be) |
| 458 | 136390051 | 1334119675550930 | 2026-08-03 | 2026-09-14 | 43 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1334119675550930) · [share](https://app.gethookd.ai/share/ad/136390051?signature=1c30cec8be3c15a4acdf04695ce040044adb2b36e8f1bbc11f1078e6518bcbce) |
| 459 | 136389982 | 2051183155490325 | 2026-08-03 | 2026-08-29 | 27 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2051183155490325) · [share](https://app.gethookd.ai/share/ad/136389982?signature=65c7b6fe8757a2a2e16401f04cc665f18ba3496596acb6f6079be97704bef42c) |
| 460 | 136388087 | 1722622828790660 | 2026-08-03 | 2026-08-13 | 11 | Video | 29 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1722622828790660) · [share](https://app.gethookd.ai/share/ad/136388087?signature=b7dac6a88f894389daf9c0064a4c918f6b9b67055c90939c49f4356cf6231d9f) |
| 461 | 136388066 | 1482965057198773 | 2026-08-03 | 2026-08-13 | 11 | Video | 33 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1482965057198773) · [share](https://app.gethookd.ai/share/ad/136388066?signature=8a12107b9dd720a6efc7250b55cbbaf58d1cd204ce05549a83b02c8e5e1c7caf) |
| 462 | 136388032 | 1036825899085653 | 2026-08-03 | 2026-08-21 | 19 | Video | 29 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1036825899085653) · [share](https://app.gethookd.ai/share/ad/136388032?signature=a07f2e94af61536db8fefd462f99a9d403e391a2671795e09fbfd1d332114355) |
| 463 | 136388014 | 1385528472912281 | 2026-08-03 | 2026-08-18 | 16 | Bild | – | Made for hands that hurt | → **T21** (Anhang) „My hands decide what I can do these days. Changing the bed used to be …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1385528472912281) · [share](https://app.gethookd.ai/share/ad/136388014?signature=04af3d67e5ea16e3172756667b216d1adbd843dbc19d4f833c81e255c9a7c0c7) |
| 464 | 136387989 | 1585337489714739 | 2026-08-03 | 2026-09-05 | 34 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1585337489714739) · [share](https://app.gethookd.ai/share/ad/136387989?signature=96d70f22ff88d4436342e04a314e5522779b9537036dc9784053c5073265e14a) |
| 465 | 136387930 | 1047129641511978 | 2026-08-03 | 2026-09-05 | 34 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1047129641511978) · [share](https://app.gethookd.ai/share/ad/136387930?signature=a6099e0ba62a4f57b7350400fcb0630471569e598bd3ee0c21cf0b4fa1d96cdd) |
| 466 | 136387870 | 2279493866157814 | 2026-08-03 | 2026-09-05 | 34 | Bild | – | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2279493866157814) · [share](https://app.gethookd.ai/share/ad/136387870?signature=6eece85a7ee2f1ac893e2ee6f6a7821b78b760cb0ca81c8f3de60313718e0f3f) |
| 467 | 133366473 | 1077293534856067 | 2026-08-03 | 2026-08-21 | 19 | Video | 27 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1077293534856067) · [share](https://app.gethookd.ai/share/ad/133366473?signature=4963289d1d8c71fbbd7971b31f043a8e3e3a7886697288429da07e32faade587) |
| 468 | 133366274 | 28264929783194204 | 2026-08-03 | 2026-08-18 | 16 | Bild | – | Made for hands that hurt | → **T21** (Anhang) „My hands decide what I can do these days. Changing the bed used to be …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=28264929783194204) · [share](https://app.gethookd.ai/share/ad/133366274?signature=a4f91f4b424a28f2cc29ac8bc4220dee0d2aa541888c23d120f2ab7a18130970) |
| 469 | 133366022 | 2504271366724256 | 2026-08-03 | 2026-08-18 | 16 | Video | 46 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2504271366724256) · [share](https://app.gethookd.ai/share/ad/133366022?signature=7325105534b1addf4c44318b6ccaebab1d38048906c3bc8f142af9e6e9393f1e) |
| 470 | 133365991 | 2462111157644122 | 2026-08-03 | 2026-08-18 | 16 | Bild | – | Made for hands that hurt | → **T21** (Anhang) „My hands decide what I can do these days. Changing the bed used to be …“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | E, C | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2462111157644122) · [share](https://app.gethookd.ai/share/ad/133365991?signature=a0ea695155a8f9ad9c379fcdb085c775181329db18dab58cfd7e9bc3d1e83d3e) |
| 471 | 133365890 | 2135568750706017 | 2026-08-03 | 2026-08-21 | 19 | Video | 30 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2135568750706017) · [share](https://app.gethookd.ai/share/ad/133365890?signature=c37f660528d9ef3fb1cec405ced5bfd740ccd31abee0f01d4fbe63d9f32d8228) |
| 472 | 133365588 | 1791074972341344 | 2026-08-03 | 2026-08-22 | 20 | Bild | – | Never lift your mattress again. | → **T51** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=1791074972341344) · [share](https://app.gethookd.ai/share/ad/133365588?signature=12358fc1c5bc24008b65dbcf19405465d2791c434e11cf0bfb47dc2e80ad12a4) |
| 473 | 133365264 | 2609327512865792 | 2026-08-03 | 2026-08-13 | 11 | Video | 29 s (2 Medienvarianten, gleiche Länge) | Never lift your mattress again. | → **T03** (Anhang) „Zippered fitted sheet 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/zipsheet-us | n/a | 1 | Inaktiv (7–29 T.) | C, E | ZipSheet | [Meta](https://www.facebook.com/ads/library/?id=2609327512865792) · [share](https://app.gethookd.ai/share/ad/133365264?signature=8140168147be9fdd9b2fb57681ed398d7971d94c0752869ec3e35329c9a676d2) |
| 474 | 133365157 | 1080490354405286 | 2026-08-03 | 2026-09-05 | 34 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1080490354405286) · [share](https://app.gethookd.ai/share/ad/133365157?signature=157666fe61e360203be9f6cc0683d39ec77be4c1ca4e52f0d891a5c4cae5ec3e) |
| 475 | 136389304 | 1050230747984526 | 2026-08-02 | 2026-09-11 | 41 | DCO | 2 Bild(er) | n/a | → **T24** (Anhang) „{{product.brand}}…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | n/a (Platzhalter-Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1050230747984526) · [share](https://app.gethookd.ai/share/ad/136389304?signature=b65c9eed879926d0c738c75b1397f3abf138f2f88244e3ad04e8c099a6c2ba36) |
| 476 | 136388788 | 888568524320369 | 2026-08-02 | 2026-08-29 | 28 | DCO | 2 Video(s): 28 s, 28 s | n/a | → **T24** (Anhang) „{{product.brand}}…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv (7–29 T.) | n/a (Platzhalter-Text) | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=888568524320369) · [share](https://app.gethookd.ai/share/ad/136388788?signature=cb53d372923937d47475e0fe70f69aa9cdc24efe0bc7d8a27fa2311d87e5689b) |
| 477 | 136389573 | 3674032809410886 | 2026-08-01 | 2026-08-18 | 18 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3674032809410886) · [share](https://app.gethookd.ai/share/ad/136389573?signature=8bdb055e7b80a4a47435f00e1de661864b28c50feb801f953b968db4c60e2db7) |
| 478 | 136389356 | 1023198490702848 | 2026-08-01 | 2026-09-08 | 39 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1023198490702848) · [share](https://app.gethookd.ai/share/ad/136389356?signature=8d74e7d04420262d8389ac1b419eb51d321f8faf45b361282d6e91c56851d7a4) |
| 479 | 136389325 | 1560968608716430 | 2026-08-01 | 2026-09-08 | 39 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1560968608716430) · [share](https://app.gethookd.ai/share/ad/136389325?signature=dccb7cf41edcf7a89b6a48af5d49b9018e32ca1ac99139c5fae285acf9999ad5) |
| 480 | 136389155 | 1548901663534152 | 2026-08-01 | 2026-08-27 | 27 | Video | 37 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1548901663534152) · [share](https://app.gethookd.ai/share/ad/136389155?signature=092d35315d1890920e425248586f183f2a8b89a76cf526b80538ab357c24c1ae) |
| 481 | 136389122 | 1560449009073304 | 2026-08-01 | 2026-08-30 | 30 | Video | 37 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1560449009073304) · [share](https://app.gethookd.ai/share/ad/136389122?signature=4c42c52810755c53ec9a838078ba5c71b2c7f36c17312550bcd6e0a64b71e00d) |
| 482 | 136388680 | 1630436858419591 | 2026-08-01 | 2026-08-30 | 30 | Video | 37 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1630436858419591) · [share](https://app.gethookd.ai/share/ad/136388680?signature=c4d82b859d1af3f95383c02c86d66b0bf832dcdc94321bf6dd977737bb9ed251) |
| 483 | 136388651 | 1054588847286173 | 2026-08-01 | 2026-09-01 | 32 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1054588847286173) · [share](https://app.gethookd.ai/share/ad/136388651?signature=4ebe96e56befc58754e6608f4bdfab7a20edb8e890144bc65078bef00d687a90) |
| 484 | 136388564 | 1023015420539475 | 2026-08-01 | 2026-09-08 | 39 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1023015420539475) · [share](https://app.gethookd.ai/share/ad/136388564?signature=67f01175964a40230987822c9e1161e3beb456135bcec1b0fa6158d754646ec1) |
| 485 | 136389942 | 2123958901533050 | 2026-07-31 | 2026-09-10 | 42 | Video | 96 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2123958901533050) · [share](https://app.gethookd.ai/share/ad/136389942?signature=5b0ab8b6147634fe5ba59e7d5acd104c90c5e8bdab91aa519a0d58a56b44bc1f) |
| 486 | 136389919 | 1972881356696916 | 2026-07-31 | 2026-09-08 | 40 | Video | 96 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1972881356696916) · [share](https://app.gethookd.ai/share/ad/136389919?signature=9a8734e956cb63dc41f673a79fcee27d00ef4625977c1ffbcc195f753d9ed381) |
| 487 | 136389732 | 2178372706066416 | 2026-07-31 | 2026-08-30 | 31 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2178372706066416) · [share](https://app.gethookd.ai/share/ad/136389732?signature=aa518563a2b7058ff8552d02be7e6408c2663474b3f57d2ad93d9cdbabc3057a) |
| 488 | 136389666 | 1360335088916893 | 2026-07-31 | 2026-08-22 | 23 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1360335088916893) · [share](https://app.gethookd.ai/share/ad/136389666?signature=cf6c5d2b147b3d892bbb49fcee7ec98d02460bddfea6aa9cdae8ff764dca699f) |
| 489 | 136389520 | 1015735761224024 | 2026-07-31 | 2026-09-13 | 45 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1015735761224024) · [share](https://app.gethookd.ai/share/ad/136389520?signature=2b4c313c9f13dbf9db2e95adb3a2da0887210aa0b619f76ff9b15da4a26c64c9) |
| 490 | 136389238 | 1432881185324334 | 2026-07-31 | 2026-08-21 | 22 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1432881185324334) · [share](https://app.gethookd.ai/share/ad/136389238?signature=912b8449e2902130290a516ef9e86528645a741a264469bbe49f431f9793a758) |
| 491 | 136389084 | 1080197727891601 | 2026-07-31 | 2026-09-13 | 45 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1080197727891601) · [share](https://app.gethookd.ai/share/ad/136389084?signature=1b273f39ab752ca515108c16cac3b68b295aeed37552af28ba5905b0d7fc9549) |
| 492 | 136388811 | 28128993223455056 | 2026-07-31 | 2026-08-22 | 23 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=28128993223455056) · [share](https://app.gethookd.ai/share/ad/136388811?signature=87c3856ef767df563629bb70660fdabc0828a636fee33d6efb2d69d8f82ea81e) |
| 493 | 136388548 | 2500141900410353 | 2026-07-31 | 2026-09-13 | 45 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2500141900410353) · [share](https://app.gethookd.ai/share/ad/136388548?signature=915e7379c59ae4aac6fb8723801e6d65bcd7b8c06c6512e771c9c31053c7c0be) |
| 494 | 133366463 | 1746200703394058 | 2026-07-31 | 2026-08-30 | 31 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1746200703394058) · [share](https://app.gethookd.ai/share/ad/133366463?signature=f560dc070fda4555f91beb8709864f8de605524cc88255a830124b9bbea9fcdf) |
| 495 | 133366390 | 3601686853322008 | 2026-07-31 | 2026-09-10 | 42 | Video | 93 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=3601686853322008) · [share](https://app.gethookd.ai/share/ad/133366390?signature=ecde9e74513dad2031f2bd469a99705a6d0f2ce5a80fa2dd87e5dd32826c96ea) |
| 496 | 133364751 | 1592381502536133 | 2026-07-31 | 2026-08-21 | 22 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1592381502536133) · [share](https://app.gethookd.ai/share/ad/133364751?signature=35875198cf14ac161d74a054e7801c1499800fcb3760f0c2c97516de4d27a57f) |
| 497 | 136388767 | 1949202019085906 | 2026-07-30 | 2026-09-01 | 34 | Video | 14 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1949202019085906) · [share](https://app.gethookd.ai/share/ad/136388767?signature=97d96f2921c1b25152af4dc91ed46fccf9a1c70124de90538c0526f62e51bd04) |
| 498 | 136388605 | 1950197182309185 | 2026-07-30 | 2026-08-29 | 31 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1950197182309185) · [share](https://app.gethookd.ai/share/ad/136388605?signature=72d097c2019296b44f39542fc1be022f42d698c4c1717e91e841f297d6e7f257) |
| 499 | 133366194 | 1063953986594114 | 2026-07-30 | 2026-09-01 | 34 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1063953986594114) · [share](https://app.gethookd.ai/share/ad/133366194?signature=44ce7b40d4f15dbede03f2cbe1531d66548ea6cff76058b79d13941cc4a75800) |
| 500 | 133364702 | 2092959514955978 | 2026-07-30 | 2026-08-16 | 18 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2092959514955978) · [share](https://app.gethookd.ai/share/ad/133364702?signature=bba3a1f9c97453867b4fdd8e73e63d31293cb9be1f5348814e10303500110f66) |
| 501 | 133364798 | 1347588606950021 | 2026-07-29 | 2026-08-16 | 19 | Video | 48 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1347588606950021) · [share](https://app.gethookd.ai/share/ad/133364798?signature=5aba192a4305308f9d412303fdfaf1ec52413482963c1f25652b361c40e3babb) |
| 502 | 133366283 | 1405919834710614 | 2026-07-26 | 2026-08-18 | 24 | Video | 46 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1405919834710614) · [share](https://app.gethookd.ai/share/ad/133366283?signature=bb31ac51f1a33b78fa710ce7c8dc77550fa0869aa0596dc71e952496e654c982) |
| 503 | 136389776 | 1740546437293601 | 2026-07-25 | 2026-09-07 | 45 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1740546437293601) · [share](https://app.gethookd.ai/share/ad/136389776?signature=9158f77f53ff8622fe97eab093e2545056713d85ba1de6a8ee4fa03606e2c18a) |
| 504 | 133366096 | 1414405543861664 | 2026-07-25 | 2026-09-07 | 45 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1414405543861664) · [share](https://app.gethookd.ai/share/ad/133366096?signature=c06237ca01ee6ed72a16462ff01cac43005a1ab4f89eeaed96142109f0fc9a18) |
| 505 | 136389963 | 1975714743107781 | 2026-07-24 | 2026-09-07 | 46 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1975714743107781) · [share](https://app.gethookd.ai/share/ad/136389963?signature=ece4db923d57198a5151d1cd2e21396c13ec79db716555abe397462ef8962a5f) |
| 506 | 136389902 | 1016719314582911 | 2026-07-24 | 2026-08-18 | 26 | Video | 25 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1016719314582911) · [share](https://app.gethookd.ai/share/ad/136389902?signature=9c355c235cd77c3669bab615e03a4c3408fc2da34981416e5c17804543e01515) |
| 507 | 136389882 | 1153681931170777 | 2026-07-24 | 2026-08-18 | 26 | Video | 26 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1153681931170777) · [share](https://app.gethookd.ai/share/ad/136389882?signature=e9c9c295ab730fbdeb8da901048ce90f5d1603f3c0ac3db49c8809a320403891) |
| 508 | 136389840 | 1416104743678164 | 2026-07-24 | 2026-08-21 | 29 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1416104743678164) · [share](https://app.gethookd.ai/share/ad/136389840?signature=fb87ad0a34a42172248f6ec7ccf099e3e811fd2d7672786ad8de22c84a7b8e41) |
| 509 | 136389650 | 4400055180215149 | 2026-07-24 | 2026-08-21 | 29 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4400055180215149) · [share](https://app.gethookd.ai/share/ad/136389650?signature=3fd8b9b5b797c4f9b214886b8735220ec2f893cdb51d6a13ceb6c00f59e6dc84) |
| 510 | 136389504 | 1671870660573049 | 2026-07-24 | 2026-08-27 | 35 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1671870660573049) · [share](https://app.gethookd.ai/share/ad/136389504?signature=122cdd016c5d7113a18e33863d11a6c5a561d599760c2923a75e2fbf80f5f729) |
| 511 | 136389207 | 1360910075371475 | 2026-07-24 | 2026-09-07 | 46 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1360910075371475) · [share](https://app.gethookd.ai/share/ad/136389207?signature=844180bb66aa9304988005e499dddccd67e0d85c2b7582d0562f417acd761e43) |
| 512 | 133365704 | 2067781017145122 | 2026-07-24 | 2026-08-22 | 30 | Video | 14 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2067781017145122) · [share](https://app.gethookd.ai/share/ad/133365704?signature=7d062de9aef165bead173b001df38d45bcc1cf0e0147afb5b9e065296a3f00d5) |
| 513 | 133365601 | 2152532702347311 | 2026-07-24 | 2026-09-07 | 46 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2152532702347311) · [share](https://app.gethookd.ai/share/ad/133365601?signature=ec205502f9e72e259496ee70ddd78e15ba076201839bbf0eff5d26c0b231c300) |
| 514 | 133365486 | 4505768623074624 | 2026-07-24 | 2026-08-21 | 29 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4505768623074624) · [share](https://app.gethookd.ai/share/ad/133365486?signature=a6f90bc8f0a2e3c1ec76d0d068940d2b9e7363478983c4848238f7a0b667d7ab) |
| 515 | 133365279 | 1039326638747579 | 2026-07-24 | 2026-08-18 | 26 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv (7–29 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1039326638747579) · [share](https://app.gethookd.ai/share/ad/133365279?signature=b509f3d1fa09175576676ba08520ec8513d346e41c4d7c8e35b335ae11e83685) |
| 516 | 133365280 | 27290663163969275 | 2026-07-19 | 2026-08-18 | 31 | Video | 40 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=27290663163969275) · [share](https://app.gethookd.ai/share/ad/133365280?signature=c2da9ec475935c65e23c4fbd9828a4f00840d7b9b26a82da67bacdc00af36186) |
| 517 | 133364652 | 1717741949560876 | 2026-07-19 | 2026-09-06 | 50 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1717741949560876) · [share](https://app.gethookd.ai/share/ad/133364652?signature=3bce78c603fdc40bc2f876d127c117f6e3ecefc1b2029c7d164e965d7787b99a) |
| 518 | 136390020 | 2077394283142508 | 2026-07-15 | 2026-09-13 | 61 | Video | 44 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2077394283142508) · [share](https://app.gethookd.ai/share/ad/136390020?signature=43bb77aaa3c476ecf22789be539884c3fee2eddcb6c104f3548e5ea8d2d92c24) |
| 519 | 133367207 | 1594458228914070 | 2026-07-15 | 2026-09-08 | 56 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1594458228914070) · [share](https://app.gethookd.ai/share/ad/133367207?signature=b47c01bfa1259f78870365b6b958cd4a043befa65cda3a07e49dcb169288e357) |
| 520 | 136389628 | 2289223651817793 | 2026-07-14 | 2026-08-29 | 47 | Video | 36 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2289223651817793) · [share](https://app.gethookd.ai/share/ad/136389628?signature=08211bdb4738a024f9e37e390f2a7ec81628596d83a49d7959b936cbb2851ba5) |
| 521 | 136389591 | 1066970162680624 | 2026-07-14 | 2026-09-13 | 62 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1066970162680624) · [share](https://app.gethookd.ai/share/ad/136389591?signature=128cd56fd17e7e8a903e836c0cf0b5c189b3741af4552317c8634e5e4f5b99d3) |
| 522 | 136389475 | 1665276507873808 | 2026-07-14 | 2026-08-29 | 47 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1665276507873808) · [share](https://app.gethookd.ai/share/ad/136389475?signature=cdc7d706bda49dc938b2a6871442b97f2e3a1f120750351323d137c356bdfcd7) |
| 523 | 136389420 | 1691830705272900 | 2026-07-14 | 2026-09-13 | 62 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1691830705272900) · [share](https://app.gethookd.ai/share/ad/136389420?signature=b4bd0943bb42dadf73930e0adc9471cce81ae2ebae200c824951393d5ebb7fef) |
| 524 | 136389104 | 1676213717010450 | 2026-07-14 | 2026-09-11 | 60 | Video | 35 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1676213717010450) · [share](https://app.gethookd.ai/share/ad/136389104?signature=1ecadaac32b0bdd55b98ec59ff226bbe5c93891e210e84c5b55b8f89b64c7940) |
| 525 | 133364874 | 1512948843284329 | 2026-07-14 | 2026-08-29 | 47 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1512948843284329) · [share](https://app.gethookd.ai/share/ad/133364874?signature=5b1bb0e877a87a848e1f50f7bcbe7c11e488ca10bae121b3901685104e3a4848) |
| 526 | 133364629 | 2001712173822376 | 2026-07-14 | 2026-09-08 | 57 | Video | 23 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest-pdp | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2001712173822376) · [share](https://app.gethookd.ai/share/ad/133364629?signature=0530d830f92dffb62a94265dd10345ea5918f64fae33b78cb05a491ae0aa5869) |
| 527 | 133364609 | 1345015433804123 | 2026-07-14 | 2026-08-18 | 36 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1345015433804123) · [share](https://app.gethookd.ai/share/ad/133364609?signature=ab9f5717822ef51de1bf47331063c1ff48f5072af4e439017ae53e09ab7a1e93) |
| 528 | 136389274 | 1736838194026177 | 2026-07-11 | 2026-08-18 | 39 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1736838194026177) · [share](https://app.gethookd.ai/share/ad/136389274?signature=70a971cce68498575e6e1dd4bf2c9438b78aca76dd8f51d77e5f6a2763236aef) |
| 529 | 133365808 | 1303214664920128 | 2026-07-11 | 2026-08-18 | 39 | Video | 47 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1303214664920128) · [share](https://app.gethookd.ai/share/ad/133365808?signature=15b6e1a3c8a418beb25d32067334e8d8d264d18ae4837cfeac4cc0f12daa9478) |
| 530 | 133365161 | 2227307328108597 | 2026-07-11 | 2026-08-18 | 39 | Video | 23 s (ffprobe; GetHooked-Wert 0) | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2227307328108597) · [share](https://app.gethookd.ai/share/ad/133365161?signature=b75ad7165b9d660353b9df4605d37bde235366e4db54a92fdd9d707d0b779873) |
| 531 | 133365473 | 999736119482810 | 2026-07-08 | 2026-09-06 | 61 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=999736119482810) · [share](https://app.gethookd.ai/share/ad/133365473?signature=7b9c1794fd12ce5847523511908d34956487944e2bc88b1ce295d96cd6d4e4b4) |
| 532 | 133365906 | 27620340294226557 | 2026-07-07 | 2026-08-16 | 41 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=27620340294226557) · [share](https://app.gethookd.ai/share/ad/133365906?signature=c64065035922fdd423ddd8b5b0cd60cabc90f8d129fba4b4fc62789e15402034) |
| 533 | 133365600 | 1766472621172612 | 2026-06-24 | 2026-08-25 | 63 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 3 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1766472621172612) · [share](https://app.gethookd.ai/share/ad/133365600?signature=bb14f9662c96dca701e442e18fa35b03c166c12048a54f7031a467ed15e17746) |
| 534 | 133365701 | 1010280781725300 | 2026-06-19 | 2026-08-28 | 71 | Video | 55 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1010280781725300) · [share](https://app.gethookd.ai/share/ad/133365701?signature=cd14a4f1ee52ab596fe2b659af29e0e62a9f3cf1cacc838a5c3b2738945fc55e) |
| 535 | 136389687 | 1581020036920692 | 2026-06-11 | 2026-08-29 | 80 | Video | 31 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1581020036920692) · [share](https://app.gethookd.ai/share/ad/136389687?signature=c4bb5359676c09c0fecb5d53654ff09439ab842da4d61b30364ab8523e2bb228) |
| 536 | 136389533 | 930528683362670 | 2026-06-11 | 2026-08-29 | 80 | Video | 35 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=930528683362670) · [share](https://app.gethookd.ai/share/ad/136389533?signature=098116e8bc41e977e86da0a4f671318187afb182da5c3aa7d227a3f14f716296) |
| 537 | 136389438 | 2804497349943273 | 2026-06-11 | 2026-09-01 | 83 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2804497349943273) · [share](https://app.gethookd.ai/share/ad/136389438?signature=5c304e8ba36424a23d89f3d6006dbc4d4b4df49870ba1eb414dd7788768c1d49) |
| 538 | 136389340 | 1318752613771504 | 2026-06-11 | 2026-08-18 | 69 | Video | 20 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1318752613771504) · [share](https://app.gethookd.ai/share/ad/136389340?signature=b82275ea25b1cf5ec9480291b359002737514826365b9a62e39d68bbeb5b8aad) |
| 539 | 136389068 | 872796652569192 | 2026-06-11 | 2026-08-29 | 80 | Video | 34 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=872796652569192) · [share](https://app.gethookd.ai/share/ad/136389068?signature=f32a83a0e9ded3693b704eaeafe4400277060e3c0fea4c000fbc52df28441b07) |
| 540 | 136389047 | 27141063635550818 | 2026-06-11 | 2026-09-07 | 89 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=27141063635550818) · [share](https://app.gethookd.ai/share/ad/136389047?signature=f407409921a12b77f620caee522c9e9b4d3114be6a4666a155f82a55a607beed) |
| 541 | 136388894 | 1521797796024377 | 2026-06-11 | 2026-08-29 | 80 | Video | 37 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1521797796024377) · [share](https://app.gethookd.ai/share/ad/136388894?signature=46517ce85e33409baa60557815e288889bfda8f6760ac9e2f2776fa956cbd167) |
| 542 | 136388877 | 994215023537195 | 2026-06-11 | 2026-08-18 | 69 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=994215023537195) · [share](https://app.gethookd.ai/share/ad/136388877?signature=a1045f9e95cb8ba5ce31f522148a1cf95c52adca92abb15182a51b2a446ce79d) |
| 543 | 136388830 | 4632064777027243 | 2026-06-11 | 2026-09-05 | 87 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=4632064777027243) · [share](https://app.gethookd.ai/share/ad/136388830?signature=0a77fef64e45b6d4ac4246726ac7cc62af7116ef20fd7376a56385dc6e44ce49) |
| 544 | 133364552 | 1543010393881104 | 2026-06-11 | 2026-08-18 | 69 | Video | 44 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SEE_DETAILS („See details“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1543010393881104) · [share](https://app.gethookd.ai/share/ad/133364552?signature=c9276584f76e85d70ed7c0097d31c2b7869af1231c40c0badc3e55f6fb5c3420) |
| 545 | 136389753 | 1496288965315983 | 2026-06-02 | 2026-08-28 | 88 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1496288965315983) · [share](https://app.gethookd.ai/share/ad/136389753?signature=c11710ed0494a2be2e0de04459119cb94adb1abe7eb43daeb71696d9f786eaca) |
| 546 | 136389610 | 1342423427761201 | 2026-06-02 | 2026-08-28 | 88 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1342423427761201) · [share](https://app.gethookd.ai/share/ad/136389610?signature=56c0541108d5e5623da5490c5b074c2aa092c14d809ace13e980d09dec4e096b) |
| 547 | 136389489 | 1968037894586095 | 2026-06-02 | 2026-08-28 | 88 | Video | 33 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1968037894586095) · [share](https://app.gethookd.ai/share/ad/136389489?signature=ac4e07d23ab6dc2de08fdcd8da355a2f3a89b1cd771ba96003bc6ab12216f95f) |
| 548 | 136389222 | 973168308972800 | 2026-06-02 | 2026-08-28 | 88 | Video | 29 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=973168308972800) · [share](https://app.gethookd.ai/share/ad/136389222?signature=aec00b54d808b9636318d04258bc56d5564a596abc9743d8147da2428469d16b) |
| 549 | 133366209 | 1299502702267336 | 2026-06-02 | 2026-08-28 | 88 | Video | 58 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1299502702267336) · [share](https://app.gethookd.ai/share/ad/133366209?signature=0ca5e0fa91b3c32b412e2c5f223fc1b3f00404d25f776aa4b1263d2d5aae2fce) |
| 550 | 133365908 | 1512627093723201 | 2026-06-02 | 2026-08-28 | 88 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1512627093723201) · [share](https://app.gethookd.ai/share/ad/133365908?signature=9dcf1b20c00296daa11240385f0e80116a4a46d480544bdc39348bff2de48080) |
| 551 | 133364769 | 993861203283367 | 2026-06-02 | 2026-08-25 | 85 | Video | 28 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 2 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=993861203283367) · [share](https://app.gethookd.ai/share/ad/133364769?signature=a283a599732fc527e7395c8730a00d8dfe95a8bf92b57ae53b10033b2e921989) |
| 552 | 133364681 | 1332402255676454 | 2026-06-02 | 2026-09-06 | 97 | Bild | – | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1332402255676454) · [share](https://app.gethookd.ai/share/ad/133364681?signature=1f697d19a3e48473cc48ee7242eb827b0144b438577de47455947de87e8ab6aa) |
| 553 | 136389548 | 2264705503936499 | 2026-06-01 | 2026-08-28 | 89 | Video | 15 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2264705503936499) · [share](https://app.gethookd.ai/share/ad/136389548?signature=04225e5f98e694f2d087aa884a689ec9ce7fa7995bfdc206597109cd1b3a02da) |
| 554 | 136389371 | 1666885827896282 | 2026-06-01 | 2026-08-28 | 89 | Video | 39 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=1666885827896282) · [share](https://app.gethookd.ai/share/ad/136389371?signature=a95032fa92b4fbf0d5f4b9744b87351beafdad9634c50e8b0ae18de242b06cd6) |
| 555 | 136388705 | 2167721337409320 | 2026-06-01 | 2026-08-28 | 89 | Video | 48 s | No More Fighting With Duvet Covers | → **T01** (Anhang) „Duvet + Cover in One 🌙…“ | SHOP_NOW („Shop now“) | facebook, instagram, audience_network, messenger, threads | https://pleene.com/products/easyrest | n/a | 1 | Inaktiv, lang gelaufen (≥30 T.) | C, B, F-Angebot | EasyRest | [Meta](https://www.facebook.com/ads/library/?id=2167721337409320) · [share](https://app.gethookd.ai/share/ad/136388705?signature=59cb41d55414e96286187aee0b49252cfc352ad2e8b678704364f32e28cbf745) |

### Primärtext-Anhang

72 Primärtexte werden von ≥ 2 Ads genutzt. Jeder steht hier einmal wörtlich (englisches Original), darunter alle GetHooked-IDs, die ihn verwenden. Texte, die nur eine Ad nutzt, stehen direkt im Vollinventar.

#### T01 – 178 Ads (20 aktiv, 158 inaktiv) · Angle: C, B, F-Angebot

```text
Duvet + Cover in One 🌙

The Pleene EasyRest™ makes changing the bed finally simple. Wash it, dry it, and lay it back on — that's it.

✓ No more wrestling with a separate duvet cover
✓ Pleasantly cool in summer, cosily warm in winter
✓ Hypoallergenic and kind to sensitive skin

Get 2 free Pleene™ Pillow Cases today (worth £39.99).

90 nights to try it risk-free.

Enjoy a bed that always feels fresh.
```

Headlines dazu: „No More Fighting With Duvet Covers“ ×175; „Pleene“ ×2; „Pleene EasyRest™ Duvet“ ×1

- aktiv: 133366116, 133366534, 136388847, 136388964, 136389861, 136390001, 151025063, 171191667, 174599778, 180153186, 182988073, 182988108, 182988111, 182988114, 182988115, 193234214, 193234215, 193234279, 200490706, 200490716
- inaktiv: 133364552, 133364609, 133364629, 133364652, 133364681, 133364702, 133364751, 133364769, 133364798, 133364874, 133364896, 133365157, 133365161, 133365279, 133365280, 133365473, 133365486, 133365600, 133365601, 133365701, 133365704, 133365808, 133365812, 133365906, 133365908, 133366022, 133366096, 133366194, 133366209, 133366283, 133366390, 133366463, 133367207, 136388548, 136388564, 136388605, 136388651, 136388680, 136388705, 136388767, 136388811, 136388826, 136388830, 136388877, 136388894, 136389047, 136389068, 136389084, 136389104, 136389122, 136389155, 136389207, 136389222, 136389238, 136389274, 136389325, 136389340, 136389356, 136389371, 136389420, 136389438, 136389475, 136389489, 136389504, 136389520, 136389533, 136389548, 136389573, 136389591, 136389610, 136389628, 136389650, 136389666, 136389687, 136389704, 136389732, 136389753, 136389776, 136389840, 136389882, 136389902, 136389919, 136389942, 136389963, 136389982, 136390020, 136390051, 136390079, 136390102, 136390115, 136390163, 136390181, 136390198, 145443344, 145443347, 148470057, 148470081, 148470082, 148470083, 151024464, 151024477, 151024479, 151024481, 151025056, 151025058, 151025064, 151454666, 153409676, 157492470, 157492473, 157492488, 160709927, 160709929, 160709944, 160709946, 160709947, 160709949, 160709950, 160709955, 160709957, 160709959, 160709961, 163921068, 163921070, 163921071, 163921072, 163921077, 163921079, 163921080, 168246660, 169082930, 169082934, 170468002, 170468005, 170468009, 171191559, 171191560, 171191563, 171191579, 171191699, 171870422, 172403290, 172403410, 172760578, 172760579, 172760580, 173929435, 176508983, 176508984, 176508986, 176509054, 177443582, 177443593, 177443600, 182988085, 182988087, 182988118, 186894314

#### T02 – 55 Ads (6 aktiv, 49 inaktiv) · Angle: „Be honest. When did you last wash it?“: A, F-Knappheit/Farbe, F-Angebot | „Ready for the colder nights.“: F-Knappheit/Farbe, F-Angebot, B

```text
This week only: 2 free Pleene™ Pillow Cases with every duvet. And if you want the bedroom ready for the colder nights, Hearth Red is the one everyone picks, and it's almost gone. The EasyRest™ is duvet and cover in one: wash it whole, dry in 2 hours.
```

Headlines dazu: „Be honest. When did you last wash it?“ ×51; „Ready for the colder nights.“ ×4

- aktiv: 177443532, 182988119, 185228767, 185228772, 193234216, 193234218
- inaktiv: 172403397, 172403403, 172403404, 172403407, 172403408, 172403413, 172760582, 172760585, 172760586, 172760589, 175318060, 176019230, 176019233, 176019239, 176019240, 176019241, 176019245, 176019246, 176019248, 176019250, 176019252, 176019253, 176019254, 176019255, 176019258, 176019259, 176508980, 176508982, 176508988, 176508989, 176508992, 176508993, 176509047, 176509052, 177443530, 177443581, 177443583, 177443584, 177443585, 177443587, 177443589, 177443592, 177443594, 177443595, 177443599, 177443601, 177443602, 180646060, 185228754

#### T03 – 55 Ads (0 aktiv, 55 inaktiv) · Angle: C, E

```text
Zippered fitted sheet 🌙

The ZipSheet™ finally makes changing your bed easy. Unzip the zip-on sheet, wash it, dry it, and zip a fresh one back on — done.

✓ Never lift the heavy mattress again
✓ Cool in summer, cozy in winter
✓ Hypoallergenic and gentle on sensitive skin

Enjoy a bed that always feels fresh.

Try it risk-free for 90 nights.
👉 https://pleene.com/products/zipsheet-us
```

Headlines dazu: „Never lift your mattress again.“ ×55

- aktiv: –
- inaktiv: 133365264, 133365890, 133366473, 136387870, 136387930, 136387989, 136388032, 136388066, 136388087, 136388113, 139560968, 139560971, 139560976, 139560984, 139560990, 139560993, 139560997, 139561003, 139561007, 139561358, 139561387, 139561401, 141368410, 141368416, 141368420, 141368423, 141368428, 141368431, 141368434, 141368436, 141368437, 141368443, 141368447, 141368543, 141368548, 143044440, 143044452, 143044453, 143044458, 143044483, 143044532, 143044538, 143044541, 143044543, 144538679, 145704160, 145704161, 145704163, 148470050, 148470051, 148470052, 148470063, 148470066, 148470070, 169784535

#### T04 – 20 Ads (5 aktiv, 15 inaktiv) · Angle: F-Social-Proof, C

```text
I only ordered it because everyone said you never have to change the bed linen again. Annoyingly, they were right. The Pleene EasyRest™ is a duvet and cover in one — wash it whole, dry in 2 hours, throw it back on.
```

Headlines dazu: „Everyone said it. They were right.“ ×20

- aktiv: 145443318, 145443331, 163921089, 193234219, 193234221
- inaktiv: 145443320, 148470080, 157492467, 157492482, 160709926, 160709953, 160709966, 160709967, 163921093, 171191562, 171191577, 171191578, 176509056, 176509063, 176509065

#### T05 – 15 Ads (0 aktiv, 15 inaktiv) · Angle: F-Social-Proof, C

```text
I only ordered it because the concept made me so curious. A duvet with no cover — how is that even supposed to work? Turns out: it works. Throw it on — done.
```

Headlines dazu: „A Duvet With No Cover?“ ×15

- aktiv: –
- inaktiv: 157492460, 157492461, 157492462, 157492469, 157492479, 157492483, 163921076, 163921086, 163921090, 173306990, 173306996, 173307000, 173929444, 173929454, 173929458

#### T06 – 15 Ads (3 aktiv, 12 inaktiv) · Angle: F-Knappheit/Farbe, C

```text
Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed, and the fastest bed-making you'll see today — because the Pleene EasyRest™ needs no cover. One throw, done.
```

Headlines dazu: „Pick a colour. Watch.“ ×15

- aktiv: 177443533, 185228773, 200490708
- inaktiv: 139561388, 139561518, 139561522, 145443338, 168246687, 168246689, 168246691, 171191565, 171191574, 171191701, 175318052, 185228757

#### T07 – 14 Ads (0 aktiv, 14 inaktiv) · Angle: A, F-Einwand/Kaufhilfe

```text
"You'd need an enormous washing machine for that." 😅

That's what everyone thinks, until they watch it go in. The Pleene EasyRest™ is deliberately lightweight. It fits the machine you already have.

✓ Whole duvet in your normal machine
✓ Dry in 2 hours, no launderette trip
```

Headlines dazu: „The Duvet That Goes In The Wash“ ×12; „Pleene EasyRest™ Quilt“ ×1; „Pleene“ ×1

- aktiv: –
- inaktiv: 168246667, 168246688, 168246695, 169082928, 169082936, 169082937, 169082940, 173306989, 173307001, 173307006, 173307153, 173929442, 173929446, 173929464

#### T08 – 13 Ads (4 aktiv, 9 inaktiv) · Angle: F-Knappheit/Farbe, F-Angebot, A

```text
This week only: 2 free Pleene™ Pillow Cases with every duvet. And if you've been eyeing Mint Green — it's almost gone. The EasyRest™ is duvet and cover in one: wash it whole, dry in 2 hours.
```

Headlines dazu: „Mint Green is almost gone.“ ×13

- aktiv: 139561410, 169082912, 185228755, 200490701
- inaktiv: 145443350, 151024482, 157492485, 160709965, 171191568, 172760574, 173929420, 176509055, 185228753

#### T09 – 13 Ads (1 aktiv, 12 inaktiv) · Angle: A

```text
You shower every night — then sleep under a duvet that's never been washed. Not because you're lazy: normal duvets don't fit normal machines. Ours does. And it's dry in 2 hours.
```

Headlines dazu: „The Duvet You Can Actually Wash“ ×13

- aktiv: 193234224
- inaktiv: 151024437, 151024448, 151024469, 160709963, 163921092, 168246684, 176508981, 176508985, 176508991, 182988096, 182988106, 182988113

#### T10 – 12 Ads (0 aktiv, 12 inaktiv) · Angle: F-Angebot, F-Knappheit/Farbe

```text
End of season sale: 2 free Pleene™ Pillow Cases with every duvet — and the popular colours are almost gone. The EasyRest is duvet and cover in one: wash it whole, dry in 2 hours.
```

Headlines dazu: „End Of Season Sale“ ×12

- aktiv: –
- inaktiv: 157492457, 157492474, 157492477, 160709941, 163921083, 163921085, 163921087, 172760562, 173306992, 173306995, 173307003, 173929418

#### T11 – 12 Ads (0 aktiv, 12 inaktiv) · Angle: F-Social-Proof, C

```text
I don't have a duvet cover anymore — and it was honestly the best decision I ever made. The Pleene EasyRest™ is a duvet and cover in one: the whole thing goes in a normal washing machine and it's dry in 2 hours.
```

Headlines dazu: „Best decision I ever made.“ ×12

- aktiv: –
- inaktiv: 139561349, 139561360, 148470055, 151024484, 151025048, 163921073, 169082939, 169082943, 173306987, 173307004, 173929447, 173929457

#### T12 – 12 Ads (0 aktiv, 12 inaktiv) · Angle: F-Angebot, C

```text
This week only 🎁

Order any Pleene EasyRest™ duvet and get 2 free matching pillow cases with it.

✓ Duvet + cover in one, nothing to change
✓ Dry in 2 hours, no tumble dryer
✓ 90-night sleep trial
```

Headlines dazu: „2 Free Pillow Cases 🎁“ ×12

- aktiv: –
- inaktiv: 168246665, 168246671, 168246690, 176508979, 176508987, 176508990, 177443586, 177443591, 177443598, 182988094, 182988100, 182988104

#### T13 – 12 Ads (0 aktiv, 12 inaktiv) · Angle: C

```text
Throw it on. Done. The Pleene EasyRest is duvet and cover in one — making the bed takes seconds, not a wrestling match. Fully machine washable and dry in 2 hours. Try it at home for 90 nights.
```

Headlines dazu: „Duvet & Cover In One“ ×11; „Pleene“ ×1

- aktiv: –
- inaktiv: 145443298, 145443315, 145443342, 148470084, 163921094, 168246677, 168246681, 168246683, 182988098, 182988101, 182988102, 182988116

#### T14 – 10 Ads (0 aktiv, 10 inaktiv) · Angle: C, A

```text
For 40 years, wash day in our house meant one thing: fighting a duvet into its cover. 🛏️

Not anymore. The Pleene EasyRest™ is duvet and cover in one. The cover is sewn in. Nothing to change. Ever.

2 – Machine:
The whole duvet goes into a normal washing machine 🌀

And it's dry in 2 hours, no tumble dryer needed.

✓ Duvet + cover in one
✓ 90-night sleep trial
```

Headlines dazu: „The Cover Is Sewn In“ ×9; „Pleene EasyRest™ 2in1 Duvet“ ×1

- aktiv: –
- inaktiv: 168246676, 168246680, 168246685, 169082901, 173306991, 173306993, 173307002, 173929439, 173929450, 173929467

#### T15 – 9 Ads (5 aktiv, 4 inaktiv) · Angle: B, A

```text
A light duvet can't keep you warm in winter." We hear it every autumn, and it's wrong. Climate-regulating fibres keep you properly warm without the heavy feeling, and the whole duvet still goes in your washing machine, dry in 2 hours.
```

Headlines dazu: „Properly Warm, Never Heavy“ ×9

- aktiv: 172403389, 172760571, 173307160, 178011633, 185228774
- inaktiv: 172403388, 172403394, 174599748, 174599757

#### T16 – 7 Ads (3 aktiv, 4 inaktiv) · Angle: F-Knappheit/Farbe, F-Angebot

```text
NEW: Lavender Mist. Our newest colour, as a limited edition. The EasyRest is duvet and cover in one: no cover changing, fully machine washable, dry in 2 hours. With 2 free pillow cases and a 90-night trial.
```

Headlines dazu: „NEW: Lavender Mist“ ×7

- aktiv: 185228766, 193234278, 200490698
- inaktiv: 172403395, 172403399, 172403406, 193234273

#### T17 – 7 Ads (3 aktiv, 4 inaktiv) · Angle: F-Einwand/Kaufhilfe

```text
Not sure which size? It's easier than duvet shopping usually is: Single bed (3ft) → Single. Double bed (4ft6) → Double. King bed (5ft) → King. Same name as your bed — that's it.
```

Headlines dazu: „What bed have you got?“ ×7

- aktiv: 182988091, 182988109, 182988112
- inaktiv: 145443282, 145443335, 145443340, 173929409

#### T18 – 7 Ads (0 aktiv, 7 inaktiv) · Angle: A

```text
You think your bed is clean? Underneath that fresh cover is a duvet that has never been washed. Not because you're lazy: normal duvets don't fit normal machines. Ours does. And it's dry in 2 hours.
```

Headlines dazu: „The Duvet You Can Actually Wash“ ×7

- aktiv: –
- inaktiv: 172403390, 172403391, 172403411, 172760575, 172760577, 172760581, 175318057

#### T19 – 6 Ads (2 aktiv, 4 inaktiv) · Angle: F-Knappheit/Farbe, F-Social-Proof

```text
Everyone's buying it in Coastal Blue — and stock is running low. The EasyRest™ is duvet and cover in one: wash the whole thing, dry in 2 hours, bed made in one throw.
```

Headlines dazu: „Everyone's buying the blue one.“ ×6

- aktiv: 139561491, 151025052
- inaktiv: 157492489, 171191582, 172760590, 176509066

#### T20 – 6 Ads (0 aktiv, 6 inaktiv) · Angle: C, F-Social-Proof

```text
I ordered it because I was done fighting with bed linen every single week. The Pleene EasyRest™ is a duvet and cover in one. The whole thing goes in a normal washing machine, everything gets washed, and it air-dries in 2 hours.
```

Headlines dazu: „Done fighting with bed linen.“ ×6

- aktiv: –
- inaktiv: 172403382, 172403416, 172760572, 172760584, 172760591, 172760592

#### T21 – 6 Ads (0 aktiv, 6 inaktiv) · Angle: E, C

```text
My hands decide what I can do these days. Changing the bed used to be the worst of it — gripping the elastic, forcing the corners under the mattress. This sheet took all of that away: the base stays on the mattress, and the top just zips off and on. Two fingers.
```

Headlines dazu: „Made for hands that hurt“ ×6

- aktiv: –
- inaktiv: 133365991, 133366274, 136388014, 144538445, 144538456, 144538678

#### T22 – 6 Ads (1 aktiv, 5 inaktiv) · Angle: C, A

```text
Myth: Changing the bed has to be a struggle. 🛏️

Truth: With the Pleene EasyRest™ there's nothing to change. The cover is sewn in.

✓ The whole duvet goes in your normal washing machine
✓ Dry in 2 hours, no tumble dryer
✓ 90-night sleep trial
```

Headlines dazu: „Myth vs Truth 🛏️“ ×6

- aktiv: 173929415
- inaktiv: 168246668, 168246674, 168246679, 171870396, 176019196

#### T23 – 6 Ads (0 aktiv, 6 inaktiv) · Angle: A

```text
When did you last wash your duvet? Not the cover — the duvet. If you can't remember, it's not your fault: normal duvets don't fit normal machines. This one does. And it's dry in 2 hours.
```

Headlines dazu: „When Did You Last Wash Your Duvet?“ ×6

- aktiv: –
- inaktiv: 145443310, 145443332, 145443333, 177443590, 177443596, 177443597

#### T24 – 6 Ads (0 aktiv, 6 inaktiv) · Angle: n/a (Platzhalter-Text)

```text
{{product.brand}}
```

Headlines dazu: „(ohne Headline)“ ×6

- aktiv: –
- inaktiv: 136388788, 136389304, 141368619, 141368634, 141368639, 141368643

#### T25 – 5 Ads (4 aktiv, 1 inaktiv) · Angle: F-Einwand/Kaufhilfe, A

```text
Before you buy a coverless duvet, check three things: ✅

✓ Does the WHOLE thing fit a normal washing machine?
✓ Is it dry in 2 hours without a tumble dryer?
✓ Can you test it at home for 90 nights?

The Pleene EasyRest™: yes, yes and yes.
```

Headlines dazu: „Check This Before You Buy“ ×5

- aktiv: 168246678, 168246686, 185228764, 200490712
- inaktiv: 168246672

#### T26 – 5 Ads (1 aktiv, 4 inaktiv) · Angle: F-Knappheit/Farbe

```text
Hearth Red is nearly sold out — and unlike most 'selling fast' claims, this one's just true. If deep red is your bedroom, this is the week to move. Duvet and cover in one, fully washable, dry in 2 hours.
```

Headlines dazu: „Hearth Red. Nearly gone.“ ×5

- aktiv: 139561428
- inaktiv: 157492475, 171191569, 172760587, 176509060

#### T27 – 5 Ads (1 aktiv, 4 inaktiv) · Angle: F-Neuheit/Größe, A

```text
Our most requested size is finally here: the Pleene EasyRest in Super King (260 × 220 cm). Duvet and cover in one — and yes, even this one fits a normal washing machine.
```

Headlines dazu: „Now In Super King“ ×5

- aktiv: 185228765
- inaktiv: 157492463, 157492481, 157492487, 185228748

#### T28 – 5 Ads (0 aktiv, 5 inaktiv) · Angle: F-Knappheit/Farbe, A

```text
You want this one. Your partner wants that one. The great bedroom debate — settled, as always, by whoever does the washing. Either way: duvet and cover in one, fully washable, dry in 2 hours.
```

Headlines dazu: „Who Wins In Your House?“ ×5

- aktiv: –
- inaktiv: 145443312, 145443324, 145443328, 157492478, 157492484

#### T29 – 5 Ads (5 aktiv, 0 inaktiv) · Angle: B, A

```text
❄️ "You'll freeze under that in winter." Here's the honest answer: the Pleene EasyRest™ is rated 10.5 tog, a proper autumn and winter weight, and the whole thing still goes in your washing machine.
```

Headlines dazu: „Warm Enough For A British Winter“ ×5

- aktiv: 178749247, 178749251, 178749254, 179476350, 180646058
- inaktiv: –

#### T30 – 5 Ads (0 aktiv, 5 inaktiv) · Angle: F-Knappheit/Farbe, F-Angebot

```text
❄️ Which colour is getting you through winter?

Comment 1-9 👇

And yes, every single one:

✓ Cover sewn in, one piece
✓ Washes whole in your machine at home 🧺
✓ Matching pillow cases included

🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „Which Colour? Comment 1-9“ ×5

- aktiv: –
- inaktiv: 178749246, 178749248, 178749256, 183445647, 186000729

#### T31 – 5 Ads (0 aktiv, 5 inaktiv) · Angle: E, C, F-Angebot

```text
🖐️ "Arthritis in my fingers, wrists and prolapsed discs in my back. It took nearly all day to change my bed, and I was in terrible pain afterwards." Real customer.
✓ EasyRest: the movement that hurts doesn't exist any more
✓ Cover sewn in: no gripping, no stuffing, no reaching overhead
✓ Whole duvet in your machine at home, dry in 2 hours 🧺
✓ 10.5 tog, warm all winter, without the weight
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „Change Your Bed Without The Pain After“ ×4; „Pleene“ ×1

- aktiv: –
- inaktiv: 184134594, 184134599, 184134601, 186000741, 186894303

#### T32 – 5 Ads (0 aktiv, 5 inaktiv) · Angle: A, F-Angebot

```text
🧺 "Does a Double REALLY fit in a normal 7kg washing machine?"
Yes. The whole duvet, room to spare.
✓ Cover sewn in, so there's nothing to take off first
✓ Wash it whole at home, dry in about 2 hours
✓ Back on the bed the same day ✨
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „Yes, It Fits Your Machine“ ×5

- aktiv: –
- inaktiv: 184134600, 184134603, 184134608, 186000740, 190288250

#### T33 – 5 Ads (0 aktiv, 5 inaktiv) · Angle: A, F-Angebot

```text
🧺 Be honest: when did you last wash the duvet you're about to spend all winter under?
Not the cover. The duvet inside it.
✓ The EasyRest has the cover sewn in, one piece
✓ So you wash the WHOLE duvet, in your machine at home
✓ Dry again in about 2 hours
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „When Did You Last Wash The Duvet?“ ×5

- aktiv: –
- inaktiv: 184134596, 184134605, 184134609, 186000736, 193234277

#### T34 – 4 Ads (0 aktiv, 4 inaktiv) · Angle: C

```text
A duvet with no cover? Here's why that works. 👀

The outer layer IS the cover. Sewn in, fully washable, dry in 2 hours.
```

Headlines dazu: „Why This Duvet Needs No Cover“ ×4

- aktiv: –
- inaktiv: 168246664, 168246692, 168246693, 168246696

#### T35 – 4 Ads (0 aktiv, 4 inaktiv) · Angle: E, C

```text
I just didn't have the strength — or the patience — to lift my mattress and force the corners under it every time I changed my bed. Then I found this sheet with a zipper.
P2: It's a 2-in-1 fitted sheet: the base goes on once and stays on for good. After that, only the zip-on sheet comes off — with a zipper. See how it works on the page, step by step.
```

Headlines dazu: „Never lift your mattress again.“ ×4

- aktiv: –
- inaktiv: 144538444, 144538454, 144538462, 148470042

#### T36 – 4 Ads (0 aktiv, 4 inaktiv) · Angle: C, F-Social-Proof

```text
I've quit bed linen. Completely. The Pleene EasyRest is duvet and cover in one — nothing to change, nothing to wrestle, nothing to iron.
```

Headlines dazu: „I've Quit Bed Linen“ ×4

- aktiv: –
- inaktiv: 157492466, 157492471, 157492472, 160709948

#### T37 – 4 Ads (3 aktiv, 1 inaktiv) · Angle: C

```text
Nothing beats getting into a freshly made bed. Pleene EasyRest™ makes it easier with an all-in-one, machine-washable comforter and no separate cover to change.
```

Headlines dazu: „Fresh Bedding Made Easy“ ×3; „Pleene“ ×1

- aktiv: 182988035, 185395501, 200490726
- inaktiv: 182988036

#### T38 – 4 Ads (1 aktiv, 3 inaktiv) · Angle: A, B, F-Angebot

```text
❄️ Your winter duvet shouldn't need a launderette.
The Pleene EasyRest washes whole, at home:

✓ Cover sewn in, nothing to strip off
✓ Fits a normal washing machine 🧺
✓ Filling quilted in place, no cold spots
✓ Dry again in about 2 hours

🎁 Right now: 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „No Launderette Needed. Ever.“ ×4

- aktiv: 178749258
- inaktiv: 178749244, 178749250, 179476351

#### T39 – 4 Ads (4 aktiv, 0 inaktiv) · Angle: C, A, F-Angebot

```text
🐙 Every wash day, my duvet cover turns into an angry octopus. Eight corners, none of them where they should be.
Then I got the Pleene EasyRest, and the cover just disappeared.
✓ Cover sewn in, one piece, nothing to wrestle
✓ Lay it on the bed and the bed is made
✓ Washes whole in your machine at home, dry in 2 hours 🧺
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „Never Wrestle A Duvet Cover Again“ ×4

- aktiv: 184134597, 184134607, 184134616, 193234275
- inaktiv: –

#### T40 – 4 Ads (0 aktiv, 4 inaktiv) · Angle: F-Social-Proof, C, A

```text
🛏️ I've spent over £300 on duvets, trying to find one that's actually right.

The one that finally ended the search works completely differently:

✓ No duvet cover, it's sewn in. One piece.
✓ The whole duvet washes in your machine at home
✓ Dry again in about 2 hours 🧺
✓ Filling quilted in place, no clumping, no cold spots

❄️ Made for cold nights, without being heavy.
🎁 Right now: 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „The Duvet With No Cover To Change“ ×4

- aktiv: –
- inaktiv: 178749241, 178749261, 178749263, 179476353

#### T41 – 4 Ads (0 aktiv, 4 inaktiv) · Angle: A, F-Angebot

```text
🧺 Did you know you probably never actually wash your duvet?
You wash the cover. The duvet inside? Hardly ever.
✓ EasyRest: cover sewn in, so you wash the WHOLE duvet
✓ In your machine at home, dry in 2 hours
✓ 10.5 tog, warm all winter
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „You Never Actually Wash Your Duvet“ ×4

- aktiv: –
- inaktiv: 184134604, 184134610, 184134612, 186894309

#### T42 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: F-Social-Proof

```text
"Best thing I got for years." — six words from a real customer, and honestly the whole pitch. The Pleene EasyRest™ is a duvet and cover in one: wash it whole, dry in 2 hours, throw it on. Done.
```

Headlines dazu: „"Best thing I got for years."“ ×3

- aktiv: –
- inaktiv: 139561448, 139561478, 160709942

#### T43 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: F-Knappheit/Farbe

```text
Nine colours. One has to go forever — which number gets deleted? Choose carefully: every single one is a full duvet and cover in one, fully washable and dry in 2 hours.
```

Headlines dazu: „Which Colour Survives?“ ×3

- aktiv: –
- inaktiv: 145443292, 145443321, 145443329

#### T44 – 3 Ads (3 aktiv, 0 inaktiv) · Angle: C

```text
No more hunting for corners or wrestling fabric into place. Pleene EasyRest™ keeps the duvet and cover together, making bedding simpler from wash to bed.
```

Headlines dazu: „Bedding Without The Struggle“ ×3

- aktiv: 186893844, 186893862, 190288311
- inaktiv: –

#### T45 – 3 Ads (3 aktiv, 0 inaktiv) · Angle: C

```text
No more stuffing, buttoning or fighting with duvet cover corners. Pleene EasyRest™ combines a duvet and cover in one, so fresh bedding is simpler from start to finish.
```

Headlines dazu: „Say Goodbye to Duvet Cover Hassle“ ×3

- aktiv: 200490654, 200490657, 200490714
- inaktiv: –

#### T46 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: F-Knappheit/Farbe, F-Social-Proof

```text
One of these nine is our bestseller — and it's nearly sold out again. Watch the reveal. Every one of them is a duvet and cover in one, fully washable, dry in 2 hours.
```

Headlines dazu: „Which One Is Our Bestseller?“ ×3

- aktiv: –
- inaktiv: 151024439, 151024462, 151024466

#### T47 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: F-Knappheit/Farbe, F-Angebot

```text
Only 26 left in Hearth Red. The EasyRest is duvet and cover in one: no cover changing, fully machine washable, dry in 2 hours. Right now with 2 free pillow cases and a 90-night trial.
```

Headlines dazu: „Only 26 Left In Hearth Red“ ×3

- aktiv: –
- inaktiv: 172403392, 172403405, 172403414

#### T48 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: C

```text
The cover is sewn in. That is the whole idea. No changing, no wrestling, no separate bed linen — one duvet that IS the cover. Fully machine washable, dry in 2 hours.
```

Headlines dazu: „The Cover Is Sewn In“ ×3

- aktiv: –
- inaktiv: 151024446, 151024458, 151024468

#### T49 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: F-Einwand/Kaufhilfe, C

```text
The number one question we get: "How does the base get on the mattress?" Simple — it goes on ONCE, exactly like a normal fitted sheet. One corner at a time. After that, you never take it off again.
```

Headlines dazu: „Never lift your mattress again“ ×3

- aktiv: –
- inaktiv: 144538441, 144538452, 144538460

#### T50 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: C

```text
This is not your normal fitted sheet: the base stays on your mattress forever — you only zip the top sheet off and on. In any color.
```

Headlines dazu: „Not your normal fitted sheet“ ×3

- aktiv: –
- inaktiv: 144538443, 144538448, 144538461

#### T51 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: C, E

```text
Zippered fitted sheet 🌙

The ZipSheet™ finally makes changing your bed easy. Unzip the zip-on sheet, wash it, dry it, and zip a fresh one back on — done.

✓ Never lift the heavy mattress again
✓ Cool in summer, cozy in winter
✓ Hypoallergenic and gentle on sensitive skin

Enjoy a bed that always feels fresh.

Try it risk-free for 90 nights.
👉
```

Headlines dazu: „Never lift your mattress again.“ ×3

- aktiv: –
- inaktiv: 133365588, 143044433, 148470048

#### T52 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: A, B

```text
❄️ Cold nights are coming, and your duvet isn't ready.
Most people head into winter with a duvet that hasn't been washed since spring.
✓ EasyRest: cover sewn in, one piece, nothing to strip off
✓ The whole duvet goes in your machine at home, dry in 2 hours 🧺
✓ 10.5 tog, warm all winter
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „Winter-Ready In One Wash“ ×3

- aktiv: –
- inaktiv: 184134591, 184134606, 184134615

#### T53 – 3 Ads (3 aktiv, 0 inaktiv) · Angle: B, A, F-Angebot

```text
❄️ Too thin for winter? Look closer.
✓ Quilted in place, no cold spots
✓ Warm all night, still washes whole 🧺
✓ Still fits a normal washing machine
✓ Dry again in about 2 hours
🎁 Right now: 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „Too Thin For Winter? Look Closer.“ ×3

- aktiv: 200037051, 200037053, 200037058
- inaktiv: –

#### T54 – 3 Ads (1 aktiv, 2 inaktiv) · Angle: F-Angebot, F-Knappheit/Farbe

```text
🎁 30% off + 2 FREE matching pillow cases. And Mint Green is almost gone.
✓ Cover sewn in, one piece, nothing to change
✓ Washes whole in your machine at home 🧺
✓ 10.5 tog, properly warm, without the weight
Link below.
```

Headlines dazu: „Mint Green Is Almost Gone“ ×3

- aktiv: 184134598
- inaktiv: 184134595, 184134614

#### T55 – 3 Ads (3 aktiv, 0 inaktiv) · Angle: A, F-Haustier

```text
🐾 Bella sleeps on our bed every night. And nobody worries about it, because the WHOLE duvet goes in the wash, not just the cover.
✓ Pleene EasyRest: cover sewn in, duvet and cover in one
✓ Fits your normal 7kg washing machine, dry in 2 hours 🧺
✓ 10.5 tog, every bit as warm as a winter duvet, just without the weight
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „The Dog Can Stay On The Bed“ ×3

- aktiv: 200037045, 200037049, 200037063
- inaktiv: –

#### T56 – 3 Ads (3 aktiv, 0 inaktiv) · Angle: A

```text
🛏️ If a guest asked you when you last washed your duvet, not the cover, the duvet, what would you say?
For a lot of us the honest answer is never, because it doesn't fit in the machine.
✓ Pleene EasyRest: cover sewn in, you wash the WHOLE duvet
✓ Normal 7kg machine, then the tumble dryer, dry in 2 hours 🧺
✓ 10.5 tog, every bit as warm as a winter duvet, just without the weight
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „When Did You Last Wash Your Duvet?“ ×3

- aktiv: 200037044, 200037061, 200037062
- inaktiv: –

#### T57 – 3 Ads (3 aktiv, 0 inaktiv) · Angle: A, F-Gäste

```text
🛏️ The grandchildren are coming to stay this weekend, and the spare bed is already done: whole duvet washed this morning, not just the cover.
✓ Pleene EasyRest: cover sewn in, duvet and cover in one
✓ The whole duvet goes in your normal 7kg washing machine, dry in 2 hours 🧺
✓ 10.5 tog, every bit as warm as a winter duvet, just without the weight (yes, even in the cold spare room)
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „The Spare Bed, Fresh For Every Guest“ ×3

- aktiv: 200037047, 200037052, 200037059
- inaktiv: –

#### T58 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: A, F-Angebot

```text
🧺 "You'll never get that in a washing machine."
We get this comment a lot. So here's the answer:

✓ The WHOLE duvet goes in a normal machine at home
✓ Cover sewn in, nothing to strip off first
✓ Dry again in about 2 hours
✓ Back on the bed the same day ✨

🎁 Right now: 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „"You'll Never Wash That." Watch Us.“ ×3

- aktiv: –
- inaktiv: 178749253, 178749262, 178749264

#### T59 – 3 Ads (0 aktiv, 3 inaktiv) · Angle: E, C, B

```text
🪶 "I'm 78 and only four foot nine. Putting a cover on a heavy winter duvet is an absolute workout." Real customer.
✓ EasyRest: so light you can lift it with one hand
✓ 10.5 tog, every bit as warm as a winter duvet, just without the weight
✓ Cover sewn in, washes whole in your machine at home, dry in 2 hours 🧺
🎁 30% off + 2 FREE matching pillow cases.
```

Headlines dazu: „A Winter Duvet You Can Actually Lift“ ×3

- aktiv: –
- inaktiv: 184134602, 184134611, 184134613

#### T60 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: F-Selbstständigkeit im Alter, C

```text
A fresh bed can still be part of your own routine. Pleene EasyRest™ combines the duvet and cover into one lightweight piece, so there’s less to manage from wash to bed.
```

Headlines dazu: „Keep Making Your Own Bed“ ×2

- aktiv: 186893837, 200490709
- inaktiv: –

#### T61 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C

```text
Bedding shouldn't be harder than it needs to be. Pleene EasyRest™ combines the duvet and cover in one, so there’s nothing separate to change, stuff or wrestle with.
```

Headlines dazu: „A Smarter Way To Do Bedding“ ×2

- aktiv: 200490658, 200490722
- inaktiv: –

#### T62 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C

```text
Clean bedding shouldn't feel like a wrestling match. Pleene EasyRest™ has no separate cover to stuff, shake or fasten back into place.
```

Headlines dazu: „Skip the Cover“ ×2

- aktiv: 182988037, 183445651
- inaktiv: –

#### T63 – 2 Ads (0 aktiv, 2 inaktiv) · Angle: F-Selbstständigkeit im Alter, C

```text
Keep the routine, just make it simpler. Pleene EasyRest™ combines the duvet and cover into one lightweight piece, so there’s nothing separate to fit or wrestle with.
```

Headlines dazu: „Less To Handle. More Independence.“ ×1; „Pleene“ ×1

- aktiv: –
- inaktiv: 189550279, 190288318

#### T64 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C, F-Selbstständigkeit im Alter

```text
Keep your routine. Skip the duvet cover struggle. Pleene EasyRest™ takes the separate duvet cover out of the equation, so there’s less stuffing, tying and managing.
```

Headlines dazu: „Your Routine, Made Simpler“ ×2

- aktiv: 186893814, 200490724
- inaktiv: –

#### T65 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C

```text
No cover. No corners to find. No stuffing required. Pleene EasyRest™ Comforter is an all-in-one machine-washable comforter designed to make bedding simpler.
```

Headlines dazu: „The Comforter That Does It All“ ×2

- aktiv: 182988041, 200490723
- inaktiv: –

#### T66 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C

```text
No more finding corners. No more fighting fabric. Pleene EasyRest™ combines the duvet and cover into one simple piece, so you can skip the struggle from wash day to bedtime.
```

Headlines dazu: „Skip The Cover. Keep The Comfort.“ ×2

- aktiv: 186893831, 186893846
- inaktiv: –

#### T67 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C, B

```text
Still doing bedding the old-fashioned way? Pleene EasyRest™ makes fresh-bed days simpler, with a duvet and cover in one, made for year-round comfort.
```

Headlines dazu: „The Bedding Upgrade Is Here“ ×2

- aktiv: 200490655, 200490721
- inaktiv: –

#### T68 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: F-Selbstständigkeit im Alter, C

```text
Still doing things your way? Pleene EasyRest™ makes it easier to keep your bedding routine yours, with a duvet and cover in one simple, machine-washable piece.
```

Headlines dazu: „Your Bed. Your Way.“ ×2

- aktiv: 186893875, 200490720
- inaktiv: –

#### T69 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C, A

```text
Still using a separate duvet cover? There’s another way. Pleene EasyRest™ combines the duvet and cover in one, so the whole thing goes into the wash and dries in 2 hours.
```

Headlines dazu: „Ditch The Duvet Cover“ ×2

- aktiv: 200036996, 200490719
- inaktiv: –

#### T70 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: F-Selbstständigkeit im Alter, A

```text
Why wait for someone else to help with your bedding? Pleene EasyRest™ washes whole at home, air dries in 2 hours, and goes straight back on the bed.
```

Headlines dazu: „Bedding Made for Independence“ ×2

- aktiv: 200490660, 200490718
- inaktiv: –

#### T71 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: C

```text
Why wrestle with a separate duvet cover? Pleene EasyRest™ keeps the duvet and cover together in one lightweight piece, making wash day a little simpler.
```

Headlines dazu: „A Simpler Way To Change The Bed“ ×1; „Pleene“ ×1

- aktiv: 189550267, 190288319
- inaktiv: –

#### T72 – 2 Ads (2 aktiv, 0 inaktiv) · Angle: A

```text
Yes, the whole comforter goes right in the wash! The Pleene EasyRest™ Comforter fits standard home washers, making fresh, clean bedding refreshingly simple.
```

Headlines dazu: „Wash The Whole Comforter“ ×2

- aktiv: 182988043, 200490725
- inaktiv: –



### S2 – Creative-Tiefenanalyse, Video-Batch 1 (Agent 2)

Stand: 2026-10-08 · Marke Pleene (UK) · Produkt EasyRest · 7 Video-Ads: 136389861, 133366534, 139561428, 139561410, 145443331, 139561491, 163921089 (alle 7 gehören zur Top-20-Liste und haben deshalb die Keyframe-Tiefenanalyse bekommen).

**Methodik und Quellen**
- Metadaten und Transkripte stammen aus GetHooked (`get_ad`, `get_transcription_status`, abgerufen am 2026-10-08). Alle 7 Transkripte hatten den Status „completed“. Ein `transcribe_ads` war nicht nötig.
- Videos liegen unter `wf/vid/<id>.mp4`. Mit ffprobe geprüft: alle 720×1280 (9:16), H.264 + AAC Stereo 44,1 kHz.
- Schnitte habe ich mit `ffmpeg select='gt(scene,0.3)',showinfo` gezählt. Bei den drei 16-Sekunden-Farbvarianten habe ich zusätzlich mit Schwelle 0,12 geprüft, weil weiche Schnitte bei 0,3 nicht erkannt wurden.
- Frames liegen unter `wf/frames/<id>/`: Stills bei 0/1/2/3 s, danach alle 5 s, plus ein Frame je erkanntem Schnitt (+0,2 s). Bei 133366534 waren das 26 von 51 Schnitten gleichmäßig verteilt plus 18 Zusatz-Frames. Dazu kommen 1-Sekunden-Streifen des oberen Bildbereichs, um die Badges zu erfassen. Alle Frames wurden als Kontaktbögen (`wf/s2b1_sheets/`) angesehen.
- Audio-Check: `volumedetect` und `silencedetect` (−40 dB / 0,4 s), dazu Spektrogramme (`wf/s2b1_audio/*.png`), Kreuzkorrelation der Tonspuren und eine grobe Grundfrequenz-Schätzung (f0, Autokorrelation; nur Indiz für die Stimmlage, **nicht verifiziert**).
- ElevenLabs habe ich **nicht** eingesetzt. Kein Transkript dieses Batches ist „falsch erkannte Sprache“. Die drei Platzhalter-Transkripte („the next, video!!“) sind per Audio-Check eindeutig reine Musik.
- Die Markenschreibweise im Whisper-Transkript schwankt („Plein“, „Pleen“, „plean“). Laut Untertiteln heißt es „Pleene“. Die Transkripte sind unten trotzdem **wörtlich** wiedergegeben, Korrekturen nach Untertitel stehen separat.
- GetHooked meldet für GB **keine Reichweite und keinen Spend**. Ersatzsignale sind Tage aktiv, performance_score und used_count. `ai_badge` ist bei allen 7 Ads `null`. Das heißt laut GetHooked ausdrücklich **nicht** „von Menschen gemacht“. `script_anatomy` lautet bei allen „not_analysed“.
- Alle 7 Ads: Länder [GB], Sprache en, Plattformen facebook, instagram, audience_network, messenger, threads. Landingpage `https://pleene.com/products/easyrest` (shop_id 47758). Link-Beschreibung: „⭐️⭐️⭐️⭐️⭐️ – Over 10,000 Happy Customers“.

**Wichtigste Querbefunde des Batches**
1. **145443331 und 163921089 sind byte-identisch** (MP4-md5 `a22e6497e1155287fea63fd80477ee89`): dasselbe Video unter zwei Ad-IDs (Start 2026-08-14 bzw. 2026-08-27). Beide haben Score 100.
2. **139561428, 139561410 und 139561491 sind ein KI-Template mit Farbtausch** (Hearth Red / Mint Green / Coastal Blue): identische Kamerafahrt und Handbewegung, identische Musikspur (Tonspur 428 = 491 bitgleich als PCM, 410 korreliert zu 0,99999). Nur die Hook-Texte und die Restmenge („Only 17/26/19 left“) unterscheiden sich.
3. Zwei Produktionswelten: (a) **UGC-Kompilation bzw. echter Creator** (133366534, 145443331/163921089) und (b) **KI-generierte Visuals** (KI-Presenter-Hook in 136389861, KI-Schlafzimmer-Template 1395614xx). Die Template-Angebotskarte („This week only: 2 FREE Pillow Cases with every DUVET“, „£39.99“ durchgestrichen) wird auch im Creator-Video 145443331 ab ca. 41 s eingeblendet.
4. Hygiene (Angle A) ist **nur in 133366534 Haupt-Angle**: Milben, Schweiß, Hautpartikel, Mikroskop-Einblendung, „dirtiest thing in your bedroom“. In allen anderen Ads dieses Batches taucht Hygiene nur als Waschbarkeit auf („Wash the whole thing“, „washing machine … tumble dryer“, „Dry in 2 hours“).

---

#### Video 136389861 – No More Fighting With Duvet Covers

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 136389861 |
| Meta-ID | 1642037860240117 |
| Ad Library | https://www.facebook.com/ads/library/?id=1642037860240117 |
| share_url | https://app.gethookd.ai/share/ad/136389861?signature=52dff4dac27abf45e6f9b062724b0d38f817b3ddcd8939d92684a863d31faaf8 |
| Start / Tage aktiv | 2026-06-11 / 120 (start_to_today, Status active) |
| performance_score / used_count | 61 („Growing“) / 1 |
| CTA | SEE_DETAILS – „See details“ |
| Landingpage | https://pleene.com/products/easyrest |
| Länge / Format | 38,0 s · 720×1280 · 25 fps |
| Schnitte (0,3) | 21 gesamt = **5,5 pro 10 s** (0–10 s: 8 · 10–20 s: 6 · 20–30 s: 5 · 30–38 s: 2) |

**Primärtext (wörtlich):** „Duvet + Cover in One 🌙 / The Pleene EasyRest™ makes changing the bed finally simple. Wash it, dry it, and lay it back on — that's it. / ✓ No more wrestling with a separate duvet cover / ✓ Pleasantly cool in summer, cosily warm in winter / ✓ Hypoallergenic and kind to sensitive skin / Get 2 free Pleene™ Pillow Cases today (worth £39.99). / 90 nights to try it risk-free. / Enjoy a bed that always feels fresh.“

**Transkript (GetHooked/Whisper, vollständig, wörtlich)**
| Sek. | Text |
|---|---|
| 0–2 | If your shoulders ache, don't do this. |
| 2–7 | And if your back is sore, definitely don't do this. |
| 7–10 | As we get older, making the bed shouldn't be this hard. |
| 10–12 | So here's the smarter way to do it instead. |
| 12–14 | All you need is the Plein EasyRest duvet. |
| 14–16 | It's a duvet and cover in one. No more separate bed linen. |
| 16–19 | You just put it straight in the washing machine and then in the tumble dryer. |
| 19–22 | And the best thing is, the breathable fibres adapt to your temperature. |
| 22–24 | Nice and warm in winter, cool and comfortable in summer. |
| 24–26 | I swear to you, my bed always feels fresh. |
| 26–28 | And the Plein pillowcases really feel super soft. |
| 28–34 | Right now, the Plein EasyRest duvet even comes with two free Plein pillowcases worth £39.99. |
| 34–37 | And with a 90-night trial sleep guarantee, you can simply test it yourself. |

Transkript-Qualität: plausibel und deckt sich mit den Untertiteln. „Plein“ steht laut Untertitel für „Pleene™“. Audio: mean −16,6 dB, keine Stille ≥ 0,4 s.

**Hook (0–3 s)**
- Gesprochen: „If your shoulders ache, don't do this.“ (0–2 s) → „And if your back is sore, definitely don't do this.“ (ab 2 s)
- Eingeblendet (Untertitel): „If your shoulders ache don't do this“ (0–2,9 s), dann „and if your back is sore definitely don't do this“.
- Bild: Ein KI-Presenter (älterer „Heiler/Lehrer“) steht in einem Apotheken- bzw. Heilkunde-Raum mit Anatomie-Postern, Kräutergläsern und Union-Jack-Tischfahne. Ab 1,28 s steht er im Klassenzimmer und zeigt mit einem Holzstock auf eine Bleistift-Cartoonzeichnung: ein schwitzender Mann kämpft mit dem Bettbezug. Das Muster ist ein Verbots-Hook („don't do this“) mit Autoritätsfigur.

**Szenenliste (alle 21 Schnitte angesehen)**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,00–1,28 | KI-Presenter im Apothekenraum, Hand auf Bauch | „If your shoulders ache don't do this“ |
| 1,28–1,88 | Klassenzimmer, Presenter zeigt mit Stock auf Cartoon an der Tafel | dto. |
| 1,88–2,88 | Close-up Cartoon (Mann zerrt am Bezug, Schweißtropfen) + Zeigestock | dto. |
| 2,88–4,32 | Presenter im Apothekenraum | „and if your back is sore definitely don't do this“ |
| 4,32–5,08 | Cartoon + Zeigestock | dto. |
| 5,08–7,08 | Cartoon nah, ohne Stock | dto. |
| 7,08–7,96 | Presenter | „As we get older making the bed shouldn't be this hard“ |
| 7,96–9,80 | Klassenzimmer, Presenter neben Cartoon | dto. |
| 9,80–11,80 | Presenter | „So here's the smarter way to do it instead“ |
| 11,80–13,80 | Realer Mann (Glatze, grauer Bart, ca. 45–55) liegt unter beiger Decke, Draufsicht | „All you need is the Pleene EasyRest™ Duvet“ |
| 13,80–16,28 | Hand streicht über beige Steppdecke | „is a duvet and cover in one“ |
| 16,28–17,92 | Arm (blaues Shirt) stopft beige Decke in Frontlader-Waschmaschine | „You just put it straight in the washing machine“ |
| 17,92–18,96 | Decke in Trockner | „and then in the tumble dryer“ |
| 18,96–19,76 | Junger Mann mit nacktem Oberkörper in mintgrüner Decke (glatter Render-Look) | „And the best thing is,“ |
| 19,76–21,72 | Junger Mann im Bett, Nachttischlampe, mintgrün | „the breathable fibres adapt to your temperature“ |
| 21,72–22,84 | Mann im blauen T-Shirt unter beiger Decke | „Nice and warm in winter, cool and comfortable in summer“ |
| 22,84–25,88 | Hand drückt in beige Decke (Füllung) | dto. / „I swear to you, my bed always feels fresh“ |
| 25,88–28,44 | Hand auf schwarzem Kissen | „And the Pleene™ Pillow Cases really feel super soft“ |
| 28,44–29,56 | Mann sitzt auf mintgrüner Decke, Kissen fliegt ins Bild | „Right now, the Pleene EasyRest™ Duvet“ |
| 29,56–32,16 | Zwei Hände drücken mintgrünes Kissen | dto. |
| 32,16–34,08 | Glatzkopf-Mann legt mintgrünes Kissen ans Kopfende | „even comes with two free Pleene™ Pillow Cases worth £39.99“ |
| 34,08–38,0 | Derselbe Mann im Bett, schüttelt mintgrüne Decke auf, am Ende glättet er stehend | „And with a 90-night trial sleep guarantee,“ → „you can simply test it yourself“ |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–7 | Verbot plus körperlicher Schmerz (Schulter → Rücken), Steigerung „definitely“ |
| Problem | 7–10 | „As we get older, making the bed shouldn't be this hard.“ |
| Verstärkung | 2–7 (Teil des Hooks) | Steigerung Schulter → Rücken. Eine eigene Agitation fehlt, also **fehlt weitgehend** |
| Lösung | 10–14 | „So here's the smarter way…“, „All you need is the … EasyRest duvet.“ |
| Mechanismus | 14–24 | duvet and cover in one, Waschmaschine + Trockner, „breathable fibres adapt to your temperature“ |
| Beweis | 24–28 | nur subjektives Testimonial („I swear to you…“, „super soft“). Keine Zahlen, keine Reviews, **schwach** |
| Angebot | 28–37 | 2 gratis Kissenbezüge „worth £39.99“ + „90-night trial sleep guarantee“ |
| CTA | – | gesprochener CTA **fehlt**, nur weich „you can simply test it yourself“. Button „See details“ |

**Personen und Sprecher**
- Hook-Presenter: männlich, geschätzt 70+, ostasiatisch wirkend, langer weißer Bart, runde Brille, Leinentunika. Rolle: weiser Heiler bzw. Lehrer (Autorität). Einschätzung: **sehr wahrscheinlich KI-generiert** (nicht verifiziert). Gründe: inszeniertes Archetyp-Setting mit britischer Tischfahne in einer „TCM“-Apotheke, dieselbe Figur springt ohne Übergang ins Klassenzimmer, glatter Render-Look. Lippen bewegen sich synchron zur Sprache (Frames 1 s/3 s), Artefakte sind bei der Frame-Auflösung nicht eindeutig.
- B-Roll: (a) realer Mann, ca. 45–55, Glatze und grauer Bart, mehrere UGC-Clips, derselbe Mann erscheint auch in 133366534. (b) Junge Männer (ca. 25–35) in Bettszenen bei 18,96–22,84 s. Sie wirken glatt und studiohaft, also **möglicherweise KI-generiert (nicht verifiziert)**. (c) Hände und Waschmaschinen-Close-ups.
- Stimme: Off- bzw. Presenter-Stimme. Der f0-Median liegt bei 0–11 s um 168 Hz und bei 12–38 s um 124 Hz, also männlich klingend. Ob es eine oder zwei Stimmen sind und ob es eine KI-Stimme ist: **nicht verifiziert**. Musik unter der VO: nicht verifiziert.

**Setting:** Heilkunde-Raum bzw. Klassenzimmer (KI), danach Schlafzimmer und Waschküche (UGC).
**Avatar / Angle:** Ältere Menschen (ca. 60+) und Menschen mit Schulter- oder Rückenbeschwerden, für die Bettenmachen körperlich anstrengend ist. **Angle E** (primär) + C (kein Bezug-Wechsel) + B (warm/kühl) + F-Angebot. Die vorläufige Einstufung „Wärme/Winter (Tog-Einwand)“ aus agent1 überschreibe ich: Der Hook ist eindeutig E.
**Haupt-Emotion:** Mitgefühl/Frust über die körperliche Mühsal, danach Erleichterung („smarter way“).
**Schnitttempo / Untertitel / Ton:** 5,5 Schnitte pro 10 s. Untertitel ja: weiße Box, schwarze kursive Sans, satzweise, Bildmitte. Ton: VO durchgehend (im Hook lippensynchron), Musik nicht verifiziert.

**Zahlen und Behauptungen (wörtlich):** „two free Plein pillowcases worth £39.99“ · „90-night trial sleep guarantee“ · „breathable fibres adapt to your temperature“ · „Nice and warm in winter, cool and comfortable in summer“ · „duvet and cover in one“ · Primärtext: „Hypoallergenic and kind to sensitive skin“, „(worth £39.99)“, „90 nights to try it risk-free“. Keine Milben-, Tog- oder Trocknungszeit-Angaben im Video.
**Angebotspräsentation:** gesprochen und als Untertitel „even comes with two free Pleene™ Pillow Cases worth £39.99“ (32–34 s) sowie „90-night trial sleep guarantee“. Keine Knappheit, keine Farbangebote, kein Preis der Decke.
**Varianten-Hinweis:** Der Primärtext ist identisch mit der Copy-Familie „No More Fighting With Duvet Covers“ (u. a. 133366534, 151025063, 182988073, 182988108, 182988111, 193234279, 200490716 sowie Bild-Ads). Skript-Verwandtschaft per Transkriptvergleich: 151025063 hat einen anderen Hook („I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“), der Body ist fast wortgleich, inkl. „worth £39.99“ und „90 night trial“. 200490716 hat dasselbe Thema (Alter, Schultern, Rücken) mit eigenem Skript. Die Satzbausteine „I swear to you, my bed always feels fresh“, „pillowcases really feel super soft“ und „you can simply test it yourself“ kommen auch in 145443331/163921089 vor. Eine Envelope-Korrelation ergab dort aber eine **andere Aufnahme** (r ≈ 0,39).

---

#### Video 133366534 – No More Fighting With Duvet Covers

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 133366534 |
| Meta-ID | 1372761711494763 |
| Ad Library | https://www.facebook.com/ads/library/?id=1372761711494763 |
| share_url | https://app.gethookd.ai/share/ad/133366534?signature=ec7e21facd4f53244e7aacaf8002b409a7803a538b1d302bb66be766c52ef924 |
| Start / Tage aktiv | 2026-08-03 / 67 (active) |
| performance_score / used_count | 100 („Winning“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Länge / Format | 92,7 s · 720×1280 · 25 fps |
| Schnitte (0,3) | 51 gesamt = **5,5 pro 10 s** (0–10: 5 · 10–20: 5 · 20–30: 5 · 30–40: 10 · 40–50: 5 · 50–60: 6 · 60–70: 4 · 70–80: 6 · 80–90: 5 · 90–92,7: 0) |

**Primärtext:** identisch mit 136389861 (siehe oben).

**Transkript (GetHooked/Whisper, vollständig, wörtlich)**
| Sek. | Text |
|---|---|
| 0,00–4,00 | Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it. When did |
| 4,00–8,40 | you last actually wash it? Not the cover, the duvet itself. Most people never do, |
| 8,40–13,36 | because it doesn't fit in a normal washing machine. And even if it does, drying takes forever. Sweat, |
| 13,36–18,00 | dust mites, skin particles. It all builds up, while you tell yourself that swapping the cover |
| 18,00–22,00 | is enough. And then there's the weekly ritual. Strip the old cover, hunt for the corners, |
| 22,00–26,48 | stuff the duvet back in, everything slips. And then all over again. Every week. For the |
| 27,04–31,68 | of your life. The problem isn't your bed linen. The problem is your duvet. The plean easy rest |
| 31,68–36,64 | is a duvet and cover in one. Nothing to stuff, no corners, no fiddling, just throw it on. Done. |
| 36,64–41,28 | And this is wash day. The whole thing goes straight in. It fits in any normal household |
| 41,28–46,16 | washing machine. The entire duvet. Everything gets washed out. And it's dry in two hours. |
| 46,16–49,92 | Even without a dryer. In the machine in the morning. Fresh on the bed by evening. The |
| 49,92–54,88 | breathable fibres adapt to your body temperature. Cool when it's warm. Warm when it turns cold. No |
| 54,88–59,84 | more sweating in summer. No more freezing in winter. One duvet all year round. Hypoallergenic. |
| 59,84–65,84 | Over 10,000 sleepers have already switched. And 96% never want to go back after their 90 night |
| 65,84–70,80 | trial. George is over 80. A widower. Making the bed alone was always a struggle. Now it's easy. |
| 70,80–75,52 | And Sarah. Washing her whole duvet has become a weekly routine. Especially because of her allergies. |
| 75,52–79,92 | Your first night. You feel lighter, fresher, different. After the first week, wash day done |
| 79,92–84,72 | in two hours. After a month, that nagging, I really should change the bedding, is simply gone. |
| 84,72–88,56 | 90 nights to sleep on it. If you're not convinced, you simply get your money back. |
| 88,56–92,32 | Right now it comes with two free Pleen pillowcases. Tap the link below. |

Transkript-Qualität: gut. Korrekturen laut Untertitel: „For the of your life“ heißt „For the rest of your life“ (Untertitel 24,3–26,2 s), „plean easy rest“ heißt „Pleene EasyRest™“. Audio: mean −16,6 dB, keine Stille ≥ 0,4 s.

**Hook (0–3 s)**
- Gesprochen: „Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it.“
- Eingeblendet: Top-Badge „No more bed changing ❌“ (0–7 s) und Untertitel „Sorry, but your duvet is probably the dirtiest thing in your bedroom“ (0–3,1 s), danach „Think about it“.
- Bild: Mann im weißen T-Shirt bezieht eine weiße Decke (Zimmer mit Holzbalken). Ab 1,8 s schüttelt eine junge Frau eine weiße Decke auf. Hook-Typ: Ekel- bzw. Schock-Behauptung mit „Sorry, but…“-Entschuldigung als Pattern Interrupt.

**Szenenliste** (Schnittzeiten aus der Szenenerkennung, Bildinhalt aus 44 + 18 angesehenen Frames und 1-s-Badge-Streifen. Mit * markierte Schnitte wurden nicht einzeln angesehen, ihr Inhalt ist aus Nachbarframes oder Streifen abgeleitet.)
| Sek. (Schnitt) | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,00 | Mann (ca. 30–40, weißes T-Shirt) zieht weiße Decke ab, Holzbalken-Zimmer | Badge „No more bed changing ❌“ · „Sorry, but your duvet is probably the dirtiest thing in your bedroom“ |
| 1,80 | Junge Frau (ca. 20–30) schüttelt weiße Decke auf dem Bett | dto. |
| 3,08 | Frau verschwindet im gemusterten Bettbezug | „Think about it“ → „When did you last actually wash it? Not the cover. The duvet itself“ |
| 5,40 | Frau (ca. 25–35) stopft weiße Decke in Frontlader. **Kreis-Einschub: Mikroskopbild länglicher, wurmartiger Organismen** (soll offenbar Milben zeigen, Art nicht verifiziert) | dto. |
| 7,32 | Mann mit Brille (ca. 30–40) kämpft mit Decke | „Most people never do,“ |
| 8,52 | Weiße Decke wird in Waschmaschine gedrückt, **großes rotes X** über der Maschine | „because it doesn't fit in a normal washing machine“ |
| 10,84 | Mann (graues T-Shirt) zieht Decke aus dem Trockner (Keller) | „And even if it does, drying takes forever“ |
| 13,00 | Mann mit Brille (wie 7,32) | dto. / „Sweat, dust mites, skin particles. It all builds up,“ |
| 14,12 | Hände kneten weiße Decke + **Mikroskop-Kreis mit Pfeil auf die Decke** | „Sweat, dust mites, skin particles. It all builds up,“ |
| 16,04 | Mann (rotes Shirt) mit grauer Decke | „while you tell yourself that swapping the cover is enough“ |
| 18,60 | Frau (dunkles Top) kämpft auf dem Bett mit Decke | „And then there's the weekly ritual“ |
| 20,12 | Blonde Frau (ca. 35–45) zieht Bezug ab | „Strip the old cover, hunt for the corners,“ |
| 24,28 | Split-Screen: derselbe tätowierte Mann zweimal beim Beziehen | „And then all over again. Every week. For the rest of your life“ |
| 26,20 | Mann weißes T-Shirt (wie 0,00) | dto. |
| 28,64 | Frau mit weißer Decke | „The problem isn't your bed linen“ |
| 29,36* / 30,0 | Frau mit gemustertem Bezug | „The problem is your duvet“ |
| 30,76 | **Produkt-Reveal**: mintgrüne EasyRest-Steppdecke wird aufs Bett geworfen | „The Pleene EasyRest™ is a duvet and cover in one“ |
| 32,04* / 33,68 / 34,60* | Junge Frau (ca. 20–30, Blumen-Pyjama) schläft unter mintgrüner Decke, Daumen hoch (35 s) | „Nothing to stuff, no corners, no fiddling. Just throw it on. Done“ |
| 35,80 | Frau zieht Decke über den Kopf | dto. |
| 36,76 / 37,88* / 38,92* | Mintgrüne Decke in Frontlader, Waschmittelflaschen | „And this is wash day / The whole thing goes straight in“ |
| 39,48* / 39,76 | Waschmaschine/Trockner-Turm, tätowierter Arm | Badge „✅ Fits any washing machine“ (40–42 s) · „It fits in any normal household washing machine“ |
| 42,12 | Blick aus der Trommel, graue Decke | „The entire duvet. Everything gets washed out“ |
| 43,08 | **Außen**: Frau hängt dunkle Decke im Garten über ein Fußballtor (Sonne) | dto. |
| 44,84 | Hand auf anthrazitfarbener Decke | Badge „✅ Quick-drying“ (45–47 s) · „And it's dry in two hours. Even without a dryer“ |
| 47,24 | Frau (gestreiftes Top) an Waschmaschine/Trockner-Turm | „In the machine in the morning, fresh on the bed by evening“ |
| 48,48 | Dieselbe Frau auf Bett mit navyblauer Decke | dto. / Badge „✅ Temperature-regulating“ (50–52 s) · „The breathable fibres adapt to your body temperature“ |
| 52,44 | Frau macht Bett (navy) | „Cool when it's warm. Warm when it turns cold“ |
| 53,52 | **CGI-Animation**: orange (warm) und blau (kalt) leuchtende Faserlinien über der Matratze | dto. |
| 54,88 | Mann (ca. 30, Bart) schläft unter anthrazitfarbener Decke | „No more sweating in summer. No more freezing in winter“ |
| 56,24* | Hände mit Decke | dto. |
| 57,56 | Mann schaut hinter hochgehaltener Decke hervor | „One duvet, all year round. Hypoallergenic.“ |
| 58,96 | Frau (gestreift) faltet navyblaue Decke | dto. / Badge „✅ 10,000+ happy customers“ (60–62 s) |
| 61,60 | Frau sitzt auf Bett | „Over 10,000 sleepers have already switched“ |
| 64,84 | Frau (ca. 30–40, Pferdeschwanz) sitzt auf Bett | „And 96% never want to go back after their 90-night trial“ |
| 66,32 | Mann macht Bett (mintgrün) + **Review-Karte** | „George is over 80. A widower“ · Karte: „★★★★★ “Since my wife passed, making the bed was the job I dreaded most. This duvet has made it easy again.” George, 82 · Verified buyer“ (mit Foto: blaue Decke) |
| 69,80 / 70,36 | Glatzkopf-Mann (ca. 45–55, derselbe wie in 136389861) streckt sich und schüttelt Decke auf | „Making the bed alone was always a struggle“ → „Now it's easy“ (Karte bleibt) |
| 72,12 | Toplader mit weißer Decke + **Review-Karte** | „Washing her whole duvet has become a weekly routine“ · Karte: „★★★★★ I'm allergic to dust and pollen, so being able to wash the entire duvet, not just the cover, is exactly what I needed. Sarah — Verified buyer“ (Foto: mintgrünes Schlafzimmer) |
| 73,96* / 75,08 | Frau (ca. 35–45, graues T-Shirt) mit weißer Decke | „Especially because of her allergies“ (Karte bleibt) |
| 75,68 | Frau (ca. 35–45, schwarze Strickjacke) mit grauer Decke im Bett | „Your first night: you feel lighter, fresher, different.“ |
| 78,40 | Frau macht graues Bett | „After the first week: wash day done in two hours“ |
| 80,36 / 80,72 | Graue Decke in Frontlader | „After a month, that nagging“ |
| 83,60* / 84,72 | Frau sitzt in grauer Decke | „90 nights to sleep on it“ |
| 87,20 | Frau liegt lächelnd unter grauer Decke | „you simply get your money back“ |
| ~89–92,7 | Frau mit grauer Decke/Kissen | „Right now it comes with two free Pleene™ Pillow Cases“ → „Tap the link below“ |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–4 | „dirtiest thing in your bedroom“ + Badge „No more bed changing ❌“ |
| Problem | 4–18 | Decke wird nie gewaschen (passt nicht, Trocknung dauert ewig), Schweiß, Milben, Hautpartikel sammeln sich |
| Verstärkung | 18–31 | „weekly ritual“, „Every week. For the rest of your life“, Reframe „The problem isn't your bed linen. The problem is your duvet.“ |
| Lösung | 30,8–36,6 | Reveal: „duvet and cover in one … just throw it on. Done.“ |
| Mechanismus | 36,6–59,8 | Ganze Decke in normale Waschmaschine, „dry in two hours. Even without a dryer“, „breathable fibres adapt to your body temperature“ (CGI), „Hypoallergenic“ |
| Beweis | 59,8–75,5 | „Over 10,000 sleepers“, „96%“, Review-Karten George (82) und Sarah (Allergie), Badge „10,000+ happy customers“. Danach Future Pacing 75,5–84,7 (erste Nacht, Woche, Monat) |
| Angebot | 84,7–92,3 | 90 Nächte mit Geld-zurück, „two free Pleene™ Pillow Cases“ (im Video ohne £-Wert) |
| CTA | 90,6–92,7 | „Tap the link below.“ + Button „Shop now“ |

**Personen und Sprecher:** Kompilation aus mindestens 15 verschiedenen realen UGC- bzw. Stock-artigen Clips (Frauen ca. 20–45, Männer ca. 25–55). Die Gesichter wirken natürlich, Handyvideo-Ästhetik, wechselnde Wohnungen. Einschätzung: **echte Personen, UGC-/Lizenzmaterial** (Herkunft nicht verifiziert). Einzige CGI-Einlage ist die Faser-Animation bei 53,5 s. Niemand spricht im Bild: **Off-Voiceover**, f0-Median ca. 139 Hz, also vermutlich männlich (nicht verifiziert). Ob die Stimme KI-generiert ist: nicht verifiziert. Auffällig: Zur Review „George, 82“ wird ein Mann gezeigt, der visuell auf ca. 45–55 geschätzt wird. Bild und Review-Zuordnung sind nicht stimmig (Schätzung).
**Setting:** Schlafzimmer (diverse), Waschküche/Keller, Küche, ein Außenclip (Garten, Decke auf Fußballtor).
**Avatar / Angle:** Hygienebewusste Haushalte und „Bettwäsche-Wechsler“ (30–65), zusätzlich Allergiker und alleinstehende Senioren (George). **Angle A** (primär) + C (Wochenritual Beziehen) + B (Temperatur) + E (George, über 80) + F-Social-Proof (10,000 / 96 % / Reviews) + F-Angebot.
**Haupt-Emotion:** Ekel und Scham (Hook und Problem), dann Frust (Wochenritual), dann Erleichterung (Future Pacing).
**Schnitttempo / Untertitel / Ton:** 5,5 Schnitte pro 10 s, Spitze 10 Schnitte bei 30–40 s rund um den Reveal. Untertitel ja: weiße Box, schwarze fette Sans (Poppins-artig), Bildmitte. Zusätzlich Top-Badges mit ✅/❌ und Review-Karten. Ton: Off-VO durchgehend, Musik nicht verifiziert.

**Zahlen und Behauptungen (wörtlich):** „probably the dirtiest thing in your bedroom“ · „Sweat, dust mites, skin particles. It all builds up“ · „It fits in any normal household washing machine“ · „And it's dry in two hours. Even without a dryer.“ · „In the machine in the morning. Fresh on the bed by evening.“ · „Cool when it's warm. Warm when it turns cold.“ · „No more sweating in summer. No more freezing in winter.“ · „Hypoallergenic.“ · „Over 10,000 sleepers have already switched.“ · „96% never want to go back after their 90 night trial“ · „George is over 80“ / Karte „George, 82“ · „wash day done in two hours“ · „90 nights to sleep on it. If you're not convinced, you simply get your money back.“ · Badges „✅ Fits any washing machine“, „✅ Quick-drying“, „✅ Temperature-regulating“, „✅ 10,000+ happy customers“. Keine Tog-Angabe, keine Temperaturwerte in °C, kein Preis.
**Angebotspräsentation:** am Ende gesprochen und eingeblendet: „Right now it comes with two free Pleene™ Pillow Cases“ (kein £-Wert im Video, im Primärtext „worth £39.99“). Risikoumkehr: „90 nights … money back“. Keine Knappheit, keine Farben.
**Varianten-Hinweis:** **193234279** (Start 2026-10-01) hat ein **wortgleiches Transkript mit identischen Segment-Zeitstempeln**. Wahrscheinlich ist es dasselbe Video oder ein Re-Upload (visuell nicht verifiziert). Primärtext-Familie wie bei 136389861.

---

#### Video 139561428 – Hearth Red. Nearly gone.

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 139561428 |
| Meta-ID | 1034362836068724 |
| Ad Library | https://www.facebook.com/ads/library/?id=1034362836068724 |
| share_url | https://app.gethookd.ai/share/ad/139561428?signature=1eb14bdf7f1f4b278f8b5996d37204958181d02f07e10262e225457c7f9a49fd |
| Start / Tage aktiv | 2026-08-07 / 63 (active) |
| performance_score / used_count | 100 („Winning“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Länge / Format | 16,5 s · 720×1280 · 30 fps |
| Schnitte | bei 0,3: 1 (10,83 s) = 0,6 pro 10 s. Bei 0,12 erkennbare harte Schnitte bei 3,0 / 7,0 / 10,83 s, also **3 Schnitte = 1,8 pro 10 s** (4 Szenen) |

**Primärtext (wörtlich):** „Hearth Red is nearly sold out — and unlike most 'selling fast' claims, this one's just true. If deep red is your bedroom, this is the week to move. Duvet and cover in one, fully washable, dry in 2 hours.“

**Transkript:** GetHooked meldet „the next, video!!“ (0,00–15,16 s). **Das ist ein Platzhalter bzw. eine Whisper-Halluzination, keine Sprache.**
Audio-Check: mean −15,0 dB, max −4,0 dB, keine Stille ≥ 0,4 s. Das Spektrogramm (`wf/s2b1_audio/139561428_spec.png`) zeigt regelmäßige breitbandige Perkussions-Transienten und tonale Akkordblöcke unter ca. 1,2 kHz, **keine Sprach-Formantstruktur**. Die Tonspur ist bit-identisch mit 139561491 und korreliert mit 139561410 zu 0,99999. **Ergebnis: eindeutig nur Musik, kein Voiceover.** Deshalb keine Neutranskription.

**Hook (0–3 s)**
- Gesprochen: keiner (nur Musik).
- Eingeblendet: „Only 17 left in Hearth Red“ (weiße Schrift mit Schatten, oben).
- Bild: Kamerafahrt durch einen Türrahmen in ein dunkles, holzvertäfeltes Luxus-Schlafzimmer mit tiefroter Steppdecke (Rautensteppung), passenden Kissen, Messing-Wandleuchten und Hochflor-Teppich.

**Szenenliste**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,0–3,0 | Kamerafahrt durch Türrahmen, Totale rotes Bett | „Only 17 left in Hearth Red“ |
| 3,0–7,0 | POV: Hand (weißer Strickärmel) hebt Deckenkante an, darunter Spannbettlaken (zeigt: kein Bezug) | „The duvet with no cover / Wash the whole thing“ |
| 7,0–10,83 | Hand streicht über Decke, Nahaufnahme | „Dry in 2 hours / Back on the bed“ |
| 10,83–16,5 | Totale; Typewriter-Text, Produktkarte Kissenbezüge, Fade to Black | „2 FREE Pillow Cases / with every DUVET / Only 17 left in Hearth Red“ · Badge (schwarzer Kreis) „FREE this week only“ · „~~£39.99~~“ (durchgestrichen) |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–3 | Knappheit „Only 17 left in Hearth Red“ |
| Problem | – | **fehlt** |
| Verstärkung | – | **fehlt** |
| Mechanismus | 3–10,8 | „The duvet with no cover / Wash the whole thing“, „Dry in 2 hours / Back on the bed“ |
| Lösung | 0–16 | Produkt durchgehend im Bild |
| Beweis | – | **fehlt** |
| Angebot | 10,8–16,5 | „2 FREE Pillow Cases with every DUVET“, „FREE this week only“, Wert „£39.99“ durchgestrichen, Knappheit „Only 17 left“ |
| CTA | – | im Video **fehlt**. Button „Shop now“ |

**Personen und Sprecher:** keine Person, nur Hand und Unterarm (weißer Strickärmel, vermutlich weiblich). **KI-generiert (Einschätzung).** Gründe: identische Kamerafahrt und **identische Handbewegung Frame für Frame** in drei Farbvarianten (139561410, 139561491), was auf eingefärbten bzw. generierten Content hindeutet. Dazu kommt der hochglatte Render-Look. Kein Sprecher, nur Musik.
**Setting:** Schlafzimmer, dunkles Holz, Luxus-Hotel-Look (KI).
**Avatar / Angle:** Ästhetik- und farbbewusste Käufer, die ihr Schlafzimmer in Rot einrichten („If deep red is your bedroom“). Vermutlich warmes bzw. Retargeting-Publikum (nicht verifiziert). **Angle F-Knappheit/Farbe** (primär) + F-Angebot + A sekundär („Wash the whole thing“).
**Haupt-Emotion:** Dringlichkeit/FOMO und Begehren (Ästhetik).
**Schnitttempo / Untertitel / Ton:** effektiv 1,8 Schnitte pro 10 s (0,6 bei Schwelle 0,3). Keine Untertitel, nur Text-Einblendungen (weiße Sans mit Schatten, oben, Typewriter-Effekt). Ton: nur Musik.

**Zahlen und Behauptungen (wörtlich):** „Only 17 left in Hearth Red“ · „Wash the whole thing“ · „Dry in 2 hours“ · „2 FREE Pillow Cases with every DUVET“ · „FREE this week only“ · „£39.99“ (durchgestrichen) · Primärtext: „nearly sold out“, „unlike most 'selling fast' claims, this one's just true“, „fully washable, dry in 2 hours“.
**Angebotspräsentation:** Endkarte mit Gratis-Kissenbezügen (Wert £39.99 durchgestrichen), zeitlich begrenzt („this week only“), plus Restmenge in der Farbe.
**Varianten-Hinweis:** Farbvariante von **139561410** (Mint Green) und **139561491** (Coastal Blue), gleiches Template, gleiche Musik, gleiche Schnitte. Weitere aktive Hearth-Red-Ads finden sich in agent1_enriched nicht.

---

#### Video 139561410 – Mint Green is almost gone.

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 139561410 |
| Meta-ID | 1355121136744622 |
| Ad Library | https://www.facebook.com/ads/library/?id=1355121136744622 |
| share_url | https://app.gethookd.ai/share/ad/139561410?signature=8993cc76f99c424613789bd7c6c9a9248d166b223587f503929e5077c7a435b2 |
| Start / Tage aktiv | 2026-08-07 / 63 (active) |
| performance_score / used_count | 100 („Winning“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Länge / Format | 16,4 s · 720×1280 · 30 fps |
| Schnitte | bei 0,3: 2 (3,0 / 10,7 s) = 1,2 pro 10 s. Bei 0,12 zusätzlich 7,0 s, also **3 harte Schnitte = 1,8 pro 10 s** |

**Primärtext (wörtlich):** „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if you've been eyeing Mint Green — it's almost gone. The EasyRest™ is duvet and cover in one: wash it whole, dry in 2 hours.“

**Transkript:** GetHooked meldet „the next, video!!“ (0,00–15,16 s), also Platzhalter. Audio-Check: mean −15,0 dB, max −4,0 dB, keine Stille, Tonspur korreliert mit 139561428 zu 0,99999 (dieselbe Musik). **Ergebnis: nur Musik, keine Sprache.**

**Hook (0–3 s)**
- Gesprochen: keiner.
- Eingeblendet: „This week only: / 2 FREE Pillow Cases / with every DUVET / Only 26 left in Mint Green“.
- Bild: dieselbe Türrahmen-Kamerafahrt wie 139561428, Decke in Mintgrün. Die Kissen im Hintergrund sind beige.

**Szenenliste**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,0–3,0 | Kamerafahrt durch Türrahmen, Totale mintgrünes Bett | „This week only: 2 FREE Pillow Cases with every DUVET / Only 26 left in Mint Green“ |
| 3,0–7,0 | POV-Hand hebt Deckenkante | „The duvet with no cover / Wash the whole thing“ |
| 7,0–10,7 | Hand streicht über Decke | „Dry in 2 hours / Back on the bed“ |
| 10,7–16,4 | Totale + Typewriter-Text + Kissenbezug-Karte, Fade to Black | „2 FREE Pillow Cases / with every DUVET / Only 26 left in Mint Green“ · „FREE this week only“ · „~~£39.99~~“ |

**Aufbau:** Hook 0–3 (Angebot + Knappheit, das Angebot steht hier schon im Hook) · Problem **fehlt** · Verstärkung **fehlt** · Mechanismus 3–10,7 („Wash the whole thing“, „Dry in 2 hours“) · Lösung = Produkt durchgehend · Beweis **fehlt** · Angebot 0–3 und 10,7–16,4 · CTA im Video **fehlt** (Button „Shop now“).
**Personen und Sprecher:** keine Person, nur Hand (weißer Strickärmel). **KI-generiert (Einschätzung, Begründung wie 139561428).** Kein Sprecher, nur Musik.
**Setting:** KI-Luxus-Schlafzimmer, dunkles Holz.
**Avatar / Angle:** Schnäppchen- und farborientierte Käufer, die Mintgrün bereits „im Auge haben“ („if you've been eyeing Mint Green“, deutet auf Retargeting hin, nicht verifiziert). **Angle F-Angebot + F-Knappheit/Farbe** (gleichrangig, das Angebot steht im Hook) + A sekundär.
**Haupt-Emotion:** Dringlichkeit (Wochenfrist + Restmenge).
**Schnitttempo / Untertitel / Ton:** 1,8 Schnitte pro 10 s effektiv. Keine Untertitel, nur Text-Einblendungen. Nur Musik.
**Zahlen und Behauptungen (wörtlich):** „This week only“ · „2 FREE Pillow Cases with every DUVET“ · „Only 26 left in Mint Green“ · „Wash the whole thing“ · „Dry in 2 hours“ · „FREE this week only“ · „£39.99“ (durchgestrichen) · Primärtext: „it's almost gone“, „wash it whole, dry in 2 hours“.
**Angebotspräsentation:** Angebot schon im Hook und noch einmal als Endkarte mit Wert £39.99 durchgestrichen, „this week only“, Restmenge.
**Varianten-Hinweis:** Farbvariante von 139561428 und 139561491. Weitere aktive Ads mit gleicher Headline „Mint Green is almost gone.“: **200490701** (Video, Start 2026-10-06) und **185228755** (Video, Start 2026-09-27). Beide haben dasselbe Platzhalter-Transkript „the next, video!!“ (0–15,16 s), sind also wahrscheinlich dasselbe oder ein sehr ähnliches Template (visuell nicht verifiziert). Bild-Ads: 169082912 (gleiche Headline) und 184134598 („Mint Green Is Almost Gone“, Primärtext mit „30% off + 2 FREE matching pillow cases“, also ein anderes Angebot).

---

#### Video 145443331 – Everyone said it. They were right.

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 145443331 |
| Meta-ID | 1440933327878495 |
| Ad Library | https://www.facebook.com/ads/library/?id=1440933327878495 |
| share_url | https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660 |
| Start / Tage aktiv | 2026-08-14 / 56 (active) |
| performance_score / used_count | 100 („Winning“) / **2** |
| CTA | ORDER_NOW – „Order now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Länge / Format | 47,0 s · 720×1280 · 25 fps |
| Schnitte (0,3) | 7 (3,8 / 11,2 / 19,6 / 25,32 / 27,84 / 31,08 / 37,56 s) = **1,5 pro 10 s** (0–10: 1 · 10–20: 2 · 20–30: 2 · 30–40: 2 · 40–47: 0) |

**Primärtext (wörtlich):** „I only ordered it because everyone said you never have to change the bed linen again. Annoyingly, they were right. The Pleene EasyRest™ is a duvet and cover in one — wash it whole, dry in 2 hours, throw it back on.“

**Transkript (GetHooked/Whisper, vollständig, wörtlich)**
| Sek. | Text |
|---|---|
| 0,00–3,76 | I haven't changed my bed linen in three months and it's never felt fresher. |
| 3,76–8,40 | The Pleen Easy Rest Duvet is a duvet and covering one, so no more separate bed linen. |
| 12,56–15,12 | Just put it in the washing machine and then in the tumble dryer. |
| 19,36–22,72 | And the best thing is the breathable fibres adapt to your body, |
| 22,72–25,20 | nice and warm in the winter, comfortable and cool in the summer. |
| 25,20–27,76 | I swear to you, my bed always feels fresh. |
| 27,76–31,04 | And the Pleen Pillow Cases really feel super soft. |
| 31,04–35,44 | And the Pleen Easy Rest comes in loads of limited colours and all different sizes. |
| 35,44–37,52 | Honestly, the hardest part was picking one. |
| 37,52–42,80 | At the moment, the Pleen Easy Rest Duvet is even on offer with two free Pleen Pillow Cases |
| 42,80–45,04 | and a 90-night trial sleep guarantee. |
| 45,04–46,64 | You can simply test it yourself. |

Transkript-Qualität: gut. Korrekturen laut Untertitel: „covering one“ heißt „cover in one“, „Pleen“ heißt „Pleene™“. Der Untertitel bei 3,0 s lautet „— and my bed has never felt fresher“, gesprochen wurde laut Whisper „and it's never felt fresher“. Sprechpausen 8,4–12,6 s und 15,1–19,4 s: Pegel −30,3 bzw. −32,1 dB (gegenüber ca. −15 dB beim Sprechen), nur leiser Hintergrund (Musik oder Raumton, nicht verifiziert), keine Sprache.

**Hook (0–3 s)**
- Gesprochen: „I haven't changed my bed linen in three months and it's never felt fresher.“
- Eingeblendet: „I haven't changed my bed linen in three months“ (0–3 s), dann „— and my bed has never felt fresher“.
- Bild: Totale von oben. Ein Mann liegt entspannt (Arm ausgestreckt) unter einer grauen Steppdecke in einem britischen Schlafzimmer mit grüner Wand, Holzbett und Hängelampe. Hook-Typ: kontraintuitive bzw. provokante Ich-Aussage (scheinbarer Hygiene-Tabubruch, der positiv aufgelöst wird).

**Szenenliste (alle 7 Schnitte angesehen, plus 20 Zusatz-Frames)**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,00–3,80 | Mann liegt im Bett, Totale von oben | „I haven't changed my bed linen in three months“ → „— and my bed has never felt fresher“ |
| 3,80–11,20 | Mann steht am Bett, hebt graue Decke an, schüttelt sie auf, legt sie zurück, Blick in die Kamera | „The Pleene EasyRest™ Duvet is a duvet and cover in one“ → „So no more separate bed linen“ |
| 11,20–19,60 | Küche mit Fliesenboden: Mann stopft Decke in Frontlader, öffnet Trockner bzw. Maschine | „Just put it in the washing machine“ → „and then in the tumble dryer“ |
| 19,60–25,32 | Mann liegt im Bett, Selfie-Perspektive, spricht in die Kamera | „And the best thing is,“ → „the breathable fibres adapt to your body“ → „Nice and warm in the winter,“ → „Comfortable and cool in the summer“ |
| 25,32–27,84 | Mann sitzt auf der Bettkante (Totale) | „I swear to you, my bed always feels fresh“ |
| 27,84–31,08 | Mann macht das Bett, Kissen | „And the Pleene™ Pillow Cases really feel super soft“ |
| 31,08–37,56 | Mann hinter dem Bett mit Decke, **eingeblendete Produktbilder wechseln** (blau, schwarz, mintgrün, anthrazit, weiß) | „And the Pleene EasyRest™ comes in loads of limited colours“ → „and all different sizes“ → „— honestly, the hardest part was picking one“ |
| 37,56–47,0 | Mann sitzt frontal auf der Bettkante und spricht. Ab ca. 41 s **Overlay-Karte** aus dem KI-Template (mintgrünes Schlafzimmer) | „At the moment, the Pleene EasyRest™ Duvet is even on offer“ → (oben) „with two free Pleene™ Pillow Cases“ → „And a 90-night trial sleep guarantee,“ → „you can simply test it yourself“ · Karte: „This week only: 2 FREE Pillow Cases with every DUVET ⏱“ · „FREE this week only“ · „~~£39.99~~“ |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–3,8 | „haven't changed my bed linen in three months … never felt fresher“ |
| Problem | – | **fehlt explizit**, nur implizit (Bettwäsche wechseln) |
| Verstärkung | – | **fehlt** |
| Lösung | 3,8–8,4 | „duvet and cover in one, so no more separate bed linen“ |
| Mechanismus | 11,2–25,3 | Waschmaschine + Trockner, „breathable fibres adapt to your body“, warm/kühl |
| Beweis | 25,3–31,1 | nur persönliches Testimonial des Creators („I swear to you…“, „super soft“). Keine Zahlen |
| (Auswahl/Knappheit-light) | 31,1–37,6 | „loads of limited colours and all different sizes“, „the hardest part was picking one“ |
| Angebot | 37,6–46,6 | 2 gratis Kissenbezüge (Overlay „£39.99“ durchgestrichen, „This week only“) + 90-Nächte-Test |
| CTA | 45–46,6 | weich: „You can simply test it yourself.“ Button „Order now“ |

**Personen und Sprecher:** Ein **echter UGC-Creator**: Mann, geschätzt 30–40, dunkle kurze Haare, Bart, graues Tanktop, Smartwatch, in einem britisch wirkenden Zuhause. Er spricht teils lippensynchron in die Kamera (19,6–25 s und 37,6–47 s), sonst als VO über seinen eigenen Handlungsszenen. Hinweise auf KI-Generierung sind nicht erkennbar. f0-Median ca. 148 Hz (männlich). KI-Stimme: nicht verifiziert, wirkt bildlich lippensynchron.
**Setting:** Schlafzimmer (grüne Wand) und Küche mit Waschmaschine.
**Avatar / Angle:** Pragmatiker, die Bettwäschewechsel hassen (Männer und junge Haushalte, ca. 25–45, Komfort-Suchende). **Angle C** (primär) + B (warm/kühl) + F-Farbauswahl/limitiert + F-Angebot. A nur indirekt („never felt fresher“, Waschmaschine).
**Haupt-Emotion:** Neugier bzw. Irritation (provokanter Hook), dann Erleichterung und Bequemlichkeit.
**Schnitttempo / Untertitel / Ton:** 1,5 Schnitte pro 10 s, ruhig mit langen Einstellungen. Untertitel ja: weiße Box, schwarze fett-kursive Sans, satzweise. Ton: Creator-O-Ton bzw. VO, in den Pausen leiser Hintergrund.
**Zahlen und Behauptungen (wörtlich):** „I haven't changed my bed linen in three months“ · „duvet and cover in one“ · „washing machine and then in the tumble dryer“ · „breathable fibres adapt to your body, nice and warm in the winter, comfortable and cool in the summer“ · „loads of limited colours and all different sizes“ · „two free Pleen Pillow Cases“ · „90-night trial sleep guarantee“ · Overlay: „This week only“, „£39.99“ (durchgestrichen), „FREE this week only“. Primärtext: „dry in 2 hours“.
**Angebotspräsentation:** gesprochen „even on offer with two free … Pillow Cases and a 90-night trial sleep guarantee“. Visuell die Template-Angebotskarte mit Wert £39.99 durchgestrichen und „This week only“. Farbauswahl als leichte Knappheit („limited colours“).
**Varianten-Hinweis:** **163921089 ist byte-identisch** (gleiche MP4). **193234221** (Start 2026-10-01) hat ein wortgleiches Transkript mit identischen Segment-Zeitstempeln, also wahrscheinlich dasselbe Video (nicht visuell verifiziert). **145443318** und **193234219** haben dieselbe Headline und denselben Primärtext, ihr GetHooked-Transkript ist **fälschlich Walisisch** erkannt. Die Struktur (Duvet, „twmble dryer“, „90“, gleiche Pausenlage um 10–15 s) deutet auf dasselbe Skript mit anderem gesprochenem Hook hin. Laut walisischer Rohfassung geht er sinngemäß Richtung „when everyone said you don't need to change your bed linen again, I ordered one“, was zum Primärtext passt (**nicht verifiziert**, gehört in den Batch eines anderen Agenten).

---

#### Video 139561491 – Everyone's buying the blue one.

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 139561491 |
| Meta-ID | 1526037445508180 |
| Ad Library | https://www.facebook.com/ads/library/?id=1526037445508180 |
| share_url | https://app.gethookd.ai/share/ad/139561491?signature=5cbb3a8ead3ed2e5b41ef6ef544d7498f90d8427b339e0ba7304f344c120fb43 |
| Start / Tage aktiv | 2026-08-07 / 63 (active) |
| performance_score / used_count | 86 („Optimized“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Länge / Format | 16,5 s · 720×1280 · 30 fps |
| Schnitte (0,3) | 3 (3,0 / 7,0 / 10,83 s) = **1,8 pro 10 s** |

**Primärtext (wörtlich):** „Everyone's buying it in Coastal Blue — and stock is running low. The EasyRest™ is duvet and cover in one: wash the whole thing, dry in 2 hours, bed made in one throw.“

**Transkript:** GetHooked meldet „the next, video!!“ (0,00–15,16 s), also Platzhalter. Audio-Check: Die Tonspur ist **bit-identisch** mit 139561428 (PCM-md5 `672fa0f2…`), mean −15,0 dB, keine Stille, Musik-Spektrum wie dort. **Ergebnis: nur Musik, keine Sprache.**

**Hook (0–3 s)**
- Gesprochen: keiner.
- Eingeblendet: „Everyone's / buying it in Coastal Blue / Only 19 left“.
- Bild: Türrahmen-Kamerafahrt, Steppdecke in Coastal Blue (Petrolblau).

**Szenenliste**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,0–3,0 | Kamerafahrt, Totale blaues Bett | „Everyone's buying it in Coastal Blue / Only 19 left“ |
| 3,0–7,0 | POV-Hand hebt Deckenkante | „The duvet with no cover / Wash the whole thing“ |
| 7,0–10,83 | Hand streicht über Decke | „Dry in 2 hours / Back on the bed“ |
| 10,83–16,5 | Totale + Typewriter + Kissenbezug-Karte, Fade to Black | „2 FREE Pillow Cases / with every DUVET / Only 19 left in Coastal Blue“ · „FREE this week only“ · „~~£39.99~~“ |

**Aufbau:** Hook 0–3 (Social Proof + Knappheit) · Problem **fehlt** · Verstärkung **fehlt** · Mechanismus 3–10,8 · Lösung = Produkt durchgehend · Beweis: nur die unbelegte Behauptung „Everyone's buying it“, sonst **fehlt** · Angebot 10,8–16,5 · CTA im Video **fehlt** (Button „Shop now“).
**Personen und Sprecher:** keine Person, nur Hand. **KI-generiert (Einschätzung, wie 139561428).** Nur Musik.
**Setting:** KI-Luxus-Schlafzimmer.
**Avatar / Angle:** Trendorientierte, farbbewusste Käufer (Bandwagon). **Angle F-Social-Proof + F-Knappheit/Farbe** + F-Angebot + A sekundär.
**Haupt-Emotion:** FOMO/Dringlichkeit (Herdeneffekt).
**Schnitttempo / Untertitel / Ton:** 1,8 Schnitte pro 10 s. Keine Untertitel, nur Text-Einblendungen. Nur Musik.
**Zahlen und Behauptungen (wörtlich):** „Everyone's buying it in Coastal Blue“ · „Only 19 left“ / „Only 19 left in Coastal Blue“ · „Wash the whole thing“ · „Dry in 2 hours“ · „2 FREE Pillow Cases with every DUVET“ · „FREE this week only“ · „£39.99“ (durchgestrichen) · Primärtext: „stock is running low“, „dry in 2 hours, bed made in one throw“.
**Angebotspräsentation:** wie 139561428 (Endkarte, £39.99 durchgestrichen, „this week only“, Restmenge).
**Varianten-Hinweis:** Farbvariante von 139561428 und 139561410 (identische Musik und Schnitte). Bild-Ad mit gleicher Headline: **151025052**.

---

#### Video 163921089 – Everyone said it. They were right.

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 163921089 |
| Meta-ID | 1609110380938946 |
| Ad Library | https://www.facebook.com/ads/library/?id=1609110380938946 |
| share_url | https://app.gethookd.ai/share/ad/163921089?signature=18918dab03620f19a44f0f4ae4aabab8d5f163dfaa3984dcc8e6e691c7301c1d |
| Start / Tage aktiv | 2026-08-27 / 43 (active) |
| performance_score / used_count | 100 („Winning“) / 1 |
| CTA | ORDER_NOW – „Order now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Länge / Format | 47,0 s · 720×1280 · 25 fps |
| Schnitte (0,3) | 7 (3,8 / 11,2 / 19,6 / 25,32 / 27,84 / 31,08 / 37,56 s) = **1,5 pro 10 s** |

**Identität:** Die MP4 ist **byte-identisch mit 145443331** (`cmp` ohne Abweichung, md5 `a22e6497e1155287fea63fd80477ee89`). Die extrahierten Frames (`wf/frames/163921089/`) sind bitgleich mit denen von 145443331, der Kontaktbogen wurde zusätzlich angesehen. Primärtext, Headline, CTA (ORDER_NOW) und Landingpage sind identisch. Es unterscheiden sich nur Ad-ID, Meta-ID, Startdatum (13 Tage später) und used_count (1 statt 2).

**Transkript (GetHooked, vollständig, wörtlich, identisch mit 145443331)**
| Sek. | Text |
|---|---|
| 0,00–3,76 | I haven't changed my bed linen in three months and it's never felt fresher. |
| 3,76–8,40 | The Pleen Easy Rest Duvet is a duvet and covering one, so no more separate bed linen. |
| 12,56–15,12 | Just put it in the washing machine and then in the tumble dryer. |
| 19,36–22,72 | And the best thing is the breathable fibres adapt to your body, |
| 22,72–25,20 | nice and warm in the winter, comfortable and cool in the summer. |
| 25,20–27,76 | I swear to you, my bed always feels fresh. |
| 27,76–31,04 | And the Pleen Pillow Cases really feel super soft. |
| 31,04–35,44 | And the Pleen Easy Rest comes in loads of limited colours and all different sizes. |
| 35,44–37,52 | Honestly, the hardest part was picking one. |
| 37,52–42,80 | At the moment, the Pleen Easy Rest Duvet is even on offer with two free Pleen Pillow Cases |
| 42,80–45,04 | and a 90-night trial sleep guarantee. |
| 45,04–46,64 | You can simply test it yourself. |

**Hook, Szenenliste, Aufbau, Personen, Setting, Avatar/Angle, Emotion, Schnitttempo, Untertitel, Ton, Zahlen und Angebot:** **exakt wie 145443331** (siehe dort, gleiche Datei). Kurzfassung:
- Hook gesprochen: „I haven't changed my bed linen in three months and it's never felt fresher.“ Eingeblendet: „I haven't changed my bed linen in three months“ / „— and my bed has never felt fresher“.
- Aufbau: Hook 0–3,8 · Problem fehlt · Verstärkung fehlt · Lösung 3,8–8,4 · Mechanismus 11,2–25,3 · Beweis 25,3–31,1 (nur persönlich) · Angebot 37,6–46,6 · CTA weich 45–46,6 („You can simply test it yourself.“), Button „Order now“.
- Person: echter UGC-Creator, Mann ca. 30–40. Setting: Schlafzimmer und Küche. **Angle C** + B + F-Farbauswahl + F-Angebot. Emotion: Neugier, dann Erleichterung. 1,5 Schnitte pro 10 s. Untertitel ja (weiße Box, fett-kursiv). Creator-O-Ton.

**Varianten-Hinweis:** byte-identische Dublette von **145443331**. Dieselbe Familie wie 193234221 (wortgleiches Transkript) sowie 145443318 und 193234219 (gleiche Copy, Transkript fälschlich Walisisch, nicht verifiziert). Dass Pleene denselben Clip als zweite Ad (13 Tage später) mit Score 100 laufen lässt, spricht für Skalierung über Duplikate (Interpretation, nicht verifiziert).

---

##### Hygiene-Zitate Batch 1

Gesammelt sind alle Stellen zu Milben, Bakterien, Schweiß, Waschen, Trocknen oder Temperatur (dazu Allergie und „fresh/Frische“ als verwandte Hygiene-Signale). Quelle: VO = gesprochen (GetHooked-Segment), UT = Untertitel, Badge/Grafik/Karte = sonstige Einblendung. **Bakterien kommen in keiner Ad dieses Batches vor.** Tog-Werte und Temperaturen in °C ebenfalls nicht.

| Ad-ID | Sek. | Quelle | Zitat (wörtlich) | Kategorie |
|---|---|---|---|---|
| 136389861 | 16–19 | VO | „You just put it straight in the washing machine and then in the tumble dryer.“ | Waschen/Trocknen |
| 136389861 | 16,3–17,9 | UT | „You just put it straight in the washing machine“ | Waschen |
| 136389861 | 17,9–19,0 | UT | „and then in the tumble dryer“ | Trocknen |
| 136389861 | 19–22 | VO | „And the best thing is, the breathable fibres adapt to your temperature.“ | Temperatur |
| 136389861 | 19,8–21,7 | UT | „the breathable fibres adapt to your temperature“ | Temperatur |
| 136389861 | 22–24 (UT 21,7–22,8+) | VO + UT | „Nice and warm in winter, cool and comfortable in summer.“ | Temperatur |
| 136389861 | 24–26 | VO + UT | „I swear to you, my bed always feels fresh.“ | Frische |
| 133366534 | 0–4 | VO + UT | „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ | Schmutz/Hygiene |
| 133366534 | 0–7 | Badge | „No more bed changing ❌“ | (Beziehen, Kontext) |
| 133366534 | 4–8,4 (UT 5–7,3) | VO + UT | „When did you last actually wash it? Not the cover, the duvet itself.“ | Waschen |
| 133366534 | 5,4–7,3 | Grafik | Kreis-Einschub mit Mikroskopbild länglicher Organismen (soll offenbar Milben darstellen, nicht verifiziert) | Milben (visuell) |
| 133366534 | 8,4–10,8 | VO + UT | „Most people never do, because it doesn't fit in a normal washing machine.“ | Waschen |
| 133366534 | 8,5–10,8 | Grafik | Großes rotes X über Waschmaschine mit Decke | Waschen (visuell) |
| 133366534 | 10,8–13,4 | VO + UT | „And even if it does, drying takes forever.“ | Trocknen |
| 133366534 | 13,4–16,0 | VO + UT | „Sweat, dust mites, skin particles. It all builds up,“ | Schweiß/Milben |
| 133366534 | 14,1–16,0 | Grafik | Mikroskop-Kreis mit Pfeil auf die Decke | Milben (visuell) |
| 133366534 | 16,0–18,6 | VO + UT | „while you tell yourself that swapping the cover is enough“ | Hygiene (Bezug ≠ Decke) |
| 133366534 | 36,6–39,8 | VO + UT | „And this is wash day. The whole thing goes straight in.“ | Waschen |
| 133366534 | 39,8–42,1 | VO + UT | „It fits in any normal household washing machine.“ | Waschen |
| 133366534 | 40–42 | Badge | „✅ Fits any washing machine“ | Waschen |
| 133366534 | 42,1–44,8 | VO + UT | „The entire duvet. Everything gets washed out.“ | Waschen |
| 133366534 | 43,1–44,8 | Bild | Decke trocknet draußen in der Sonne (über Fußballtor) | Trocknen (visuell) |
| 133366534 | 44,8–47,2 | VO + UT | „And it's dry in two hours. Even without a dryer.“ | Trocknen |
| 133366534 | 45–47 | Badge | „✅ Quick-drying“ | Trocknen |
| 133366534 | 47,2–49,9 | VO + UT | „In the machine in the morning, fresh on the bed by evening.“ | Waschen/Trocknen |
| 133366534 | 49,9–52,4 | VO + UT | „The breathable fibres adapt to your body temperature.“ | Temperatur |
| 133366534 | 50–52 | Badge | „✅ Temperature-regulating“ | Temperatur |
| 133366534 | 52,4–54,9 | VO + UT | „Cool when it's warm. Warm when it turns cold.“ | Temperatur |
| 133366534 | 53,5–54,9 | Grafik | CGI-Faseranimation orange (warm) / blau (kalt) | Temperatur (visuell) |
| 133366534 | 54,9–57,6 | VO + UT | „No more sweating in summer. No more freezing in winter.“ | Schweiß/Temperatur |
| 133366534 | 57,6–59,8 | VO + UT | „One duvet, all year round. Hypoallergenic.“ | Allergie/Temperatur |
| 133366534 | 70,8–75,5 | VO | „And Sarah. Washing her whole duvet has become a weekly routine. Especially because of her allergies.“ | Waschen/Allergie |
| 133366534 | 72,1–75,7 | UT | „Washing her whole duvet has become a weekly routine“ / „Especially because of her allergies“ | Waschen/Allergie |
| 133366534 | 72,1–75,7 | Review-Karte | „I'm allergic to dust and pollen, so being able to wash the entire duvet, not just the cover, is exactly what I needed.“ (Sarah — Verified buyer) | Waschen/Allergie |
| 133366534 | 75,5–79,9 | VO + UT | „Your first night. You feel lighter, fresher, different.“ | Frische |
| 133366534 | 78,4–80,4 (VO 79–84,7) | VO + UT | „After the first week, wash day done in two hours.“ | Waschen/Trocknen |
| 133366534 | 80,4–84,7 | VO (UT: „After a month, that nagging“) | „After a month, that nagging, I really should change the bedding, is simply gone.“ | Hygiene-Routine |
| 139561428 | 3,0–7,0 | Einblendung | „The duvet with no cover / Wash the whole thing“ | Waschen |
| 139561428 | 7,0–10,8 | Einblendung | „Dry in 2 hours / Back on the bed“ | Trocknen |
| 139561410 | 3,0–7,0 | Einblendung | „The duvet with no cover / Wash the whole thing“ | Waschen |
| 139561410 | 7,0–10,7 | Einblendung | „Dry in 2 hours / Back on the bed“ | Trocknen |
| 139561491 | 3,0–7,0 | Einblendung | „The duvet with no cover / Wash the whole thing“ | Waschen |
| 139561491 | 7,0–10,8 | Einblendung | „Dry in 2 hours / Back on the bed“ | Trocknen |
| 145443331 | 0–3,76 | VO | „I haven't changed my bed linen in three months and it's never felt fresher.“ | Frische (Hygiene-Tabu als Hook) |
| 145443331 | 3,0–3,8 | UT | „— and my bed has never felt fresher“ | Frische |
| 145443331 | 12,56–15,12 | VO | „Just put it in the washing machine and then in the tumble dryer.“ | Waschen/Trocknen |
| 145443331 | 11,2–ca. 15 | UT | „Just put it in the washing machine“ | Waschen |
| 145443331 | ca. 15–19,6 | UT | „and then in the tumble dryer“ | Trocknen |
| 145443331 | 19,36–22,72 | VO + UT | „And the best thing is the breathable fibres adapt to your body,“ | Temperatur |
| 145443331 | 22,72–25,20 | VO | „nice and warm in the winter, comfortable and cool in the summer.“ | Temperatur |
| 145443331 | ca. 23–25,3 | UT | „Nice and warm in the winter,“ / „Comfortable and cool in the summer“ | Temperatur |
| 145443331 | 25,2–27,8 | VO + UT | „I swear to you, my bed always feels fresh.“ | Frische |
| 163921089 | wie 145443331 | VO + UT | identisch mit allen Zeilen zu 145443331 (byte-identische Datei) | – |

Ergänzend die Hygiene-Aussagen in den **Primärtexten** (kein Video-Inhalt):
- 136389861 / 133366534: „Wash it, dry it, and lay it back on — that's it.“ · „Pleasantly cool in summer, cosily warm in winter“ · „Hypoallergenic and kind to sensitive skin“ · „Enjoy a bed that always feels fresh.“
- 139561428: „Duvet and cover in one, fully washable, dry in 2 hours.“
- 139561410: „wash it whole, dry in 2 hours.“
- 139561491: „wash the whole thing, dry in 2 hours, bed made in one throw.“
- 145443331 / 163921089: „wash it whole, dry in 2 hours, throw it back on.“

---

##### Kurz-Tabelle Batch 1

| ID | Länge | Hook (wörtlich, 0–3 s) | Angle | Avatar | Sprecher-Typ | Schnitte/10 s | Emotion |
|---|---|---|---|---|---|---|---|
| 136389861 | 38,0 s | VO: „If your shoulders ache, don't do this.“ / UT: „If your shoulders ache don't do this“ | **E** (+C, B, F-Angebot) | Ältere (60+), Schulter- und Rückenbeschwerden | KI-Presenter (älterer „Heiler“), danach Off-VO über UGC- und teils KI-B-Roll | 5,5 | Mitgefühl/Frust → Erleichterung |
| 133366534 | 92,7 s | VO+UT: „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ + Badge „No more bed changing ❌“ | **A** (+C, B, E, F-Social-Proof, F-Angebot) | Hygienebewusste Haushalte 30–65, Allergiker, alleinstehende Senioren | Off-VO (männlich, nicht verifiziert) über UGC-Kompilation echter Personen | 5,5 | Ekel/Scham → Frust → Erleichterung |
| 139561428 | 16,5 s | Text: „Only 17 left in Hearth Red“ (keine Sprache) | **F-Knappheit/Farbe** (+F-Angebot, A sek.) | Ästhetik- und farbbewusste Käufer (Rot), vermutlich warm/Retargeting | keiner, nur Musik; KI-Visual (nur Hand) | 1,8 effektiv (0,6 bei 0,3) | Dringlichkeit/FOMO |
| 139561410 | 16,4 s | Text: „This week only: 2 FREE Pillow Cases with every DUVET / Only 26 left in Mint Green“ | **F-Angebot + F-Knappheit/Farbe** (A sek.) | Schnäppchen- und farborientierte Interessenten („eyeing Mint Green“) | keiner, nur Musik; KI-Visual | 1,8 effektiv (1,2 bei 0,3) | Dringlichkeit |
| 145443331 | 47,0 s | VO: „I haven't changed my bed linen in three months and it's never felt fresher.“ / UT: „I haven't changed my bed linen in three months“ | **C** (+B, F-Farbauswahl, F-Angebot) | Pragmatiker 25–45, die Bettwäschewechsel hassen | Echter UGC-Creator (Mann ca. 30–40), O-Ton/VO, teils on-camera | 1,5 | Neugier → Erleichterung |
| 139561491 | 16,5 s | Text: „Everyone's buying it in Coastal Blue / Only 19 left“ | **F-Social-Proof + F-Knappheit/Farbe** (+F-Angebot, A sek.) | Trendorientierte, farbbewusste Käufer | keiner, nur Musik; KI-Visual | 1,8 | FOMO (Herdeneffekt) |
| 163921089 | 47,0 s | = 145443331 (byte-identisch) | **C** (+B, F-Farbauswahl, F-Angebot) | = 145443331 | = 145443331 | 1,5 | Neugier → Erleichterung |

---

##### Prüfung der Pflichtliste (Batch 1)

| Ad | Transkript | Hook | Aufbau | Personen | Setting | Avatar/Angle | Emotion | Tempo/UT/Ton | Zahlen | Angebot | Varianten | Metadaten | Szenenliste (Top-20) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 136389861 | ✔ vollständig | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ alle 21 Schnitte |
| 133366534 | ✔ vollständig (+Korrektur) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ 51 Schnitte; ca. 40 per Frame angesehen, Rest (*) aus Nachbarframes und Streifen |
| 139561428 | ✔ begründeter Vermerk: nur Musik (Audio-Check) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 139561410 | ✔ begründeter Vermerk: nur Musik | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 145443331 | ✔ vollständig (+Pausen geprüft) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ alle 7 Schnitte + 20 Zusatz-Frames |
| 139561491 | ✔ begründeter Vermerk: nur Musik | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 163921089 | ✔ vollständig (identisch 145443331) | ✔ | ✔ (= 145443331) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ (byte-identisch, Frames bitgleich, Kontaktbogen angesehen) |

Offen bzw. nicht verifiziert (bewusst so markiert): ob Stimmen KI-generiert sind; ob unter den VOs von 136389861 und 133366534 Musik liegt; die Organismen-Art im Mikroskop-Einschub; die Herkunft der UGC-Clips (lizenziert oder eigen); ob 193234279 / 193234221 / 200490701 / 185228755 visuell identische Videos sind (nur Transkript- bzw. Titelvergleich); die Hook-Wortlaute von 145443318 / 193234219 (Walisisch-Fehltranskript, anderer Batch).


### Agent 2 – Creative-Tiefenanalyse, Video-Batch 2 (Pleene EasyRest, UK)

Stand: 2026-10-08. Ads: 145443318, 151025063, 168246678, 168246686, 178749251, 178749254, 178749247.
Top-20-Tiefenanalyse (Frame an jedem Schnitt): 145443318, 151025063, 168246678, 168246686. Die drei 178749xxx-Ads sind nicht in der Top-20-Liste; trotzdem wurde an jedem erkannten Schnitt ein Frame angesehen.

**Methodik und Datenbasis**
- Metadaten: `get_ad` (frisch am 2026-10-08) plus `agent1_enriched.json` / `s1_inventar.md` (Stand des früheren Laufs). Abweichungen sind ausgewiesen.
- Transkripte: `get_transcription_status` (alle 7 terminal: 5× `completed`, 2× `no_speech`). `transcribe_ads` war nicht nötig.
- Videos: `/wf/vid/<id>.mp4` (alle 720×1280). ffprobe; Schnitte mit `select='gt(scene,0.3)'` (Hauptwert) und zusätzlich mit 0.15 (Feinwert; Doppeltreffer < 0,1 s zusammengefasst).
- Frames: `/wf/frames/<id>/` (0/1/2/3 s, dann alle 5 s, dazu je Schnitt +0,2 s). Für die Untertitel wurden alle 0,5 s Streifen aufgenommen (`/wf/frames/<id>/cap/`), bei 168246678/686 alle 0,25 bis 0,5 s Vollbilder. Alle Kontaktbögen liegen in `/wf/s2b2_sheets/`, Skripte in `/wf/s2b2_scripts/`.
- Audio: volumedetect, silencedetect, Spektrogramme (`/wf/s2b2_audio/`), Grundfrequenz-Schätzung (f0, Autokorrelation), Audio-Kreuzkorrelation und Frame-Differenz zwischen Varianten.
- Emojis in Zitaten sind als [Emoji: …] wiedergegeben. Gesprochenes steht so, wie GetHooked/Whisper es geschrieben hat (z. B. „Pleen“, „Plein“); in den Untertiteln steht korrekt „Pleene“.
- Hinweis zu Reichweite/Spend: GetHooked liefert für GB keine Werte. Ersatzsignale sind days_active, performance_score und used_count.

---

#### Video 145443318 – Everyone said it. They were right.

**Metadaten**
| Feld | Wert |
|---|---|
| Meta-ID | 1474663121347221 |
| Start / Status | 2026-08-14 / aktiv (get_ad: end_date 2026-10-08, days_active_basis start_to_today) |
| Tage aktiv | 56 |
| performance_score | **61 (Growing)** laut get_ad vom 2026-10-08. Im früheren Lauf (agent1/s1) stand **74 (Growing)**. Der Score ist also gesunken. |
| used_count | 1 |
| Block (s1) | Winner (Top-20-Rang 10) |
| Landingpage | https://pleene.com/products/easyrest |
| CTA | ORDER_NOW („Order now“) |
| Plattformen | facebook, instagram, audience_network, messenger, threads; Land GB |
| Primärtext (T04) | „I only ordered it because everyone said you never have to change the bed linen again. Annoyingly, they were right. The Pleene EasyRest™ is a duvet and cover in one — wash it whole, dry in 2 hours, throw it back on.“ |
| Link-Beschreibung | „[5 Stern-Emojis] – Over 10,000 Happy Customers“ |
| share_url | https://app.gethookd.ai/share/ad/145443318?signature=be73a154548ac1fdbbec6cdf47867c12c72f8b288e40c2faaa6b1db18c69b49b |
| Ad Library | https://www.facebook.com/ads/library/?id=1474663121347221 |
| Technik | 49,53 s, 720×1280, 25 fps |

**Transkript**
- **GetHooked-Transkript ist fehlerhaft:** Es wurde als Walisisch erkannt (bekanntes Fehlerbild). Auch das `hook`-Feld von get_ad ist walisisch. Die gespeicherten Segmente werden hier vollständig dokumentiert, sind aber inhaltlich wertlos:
  - [0.00–5.04] „Oh, rydw i wedi gwneud newid i'r byd. Pan roedd pawb yn dweud nad oes angen newid eich llinyn y byd eto,“
  - [5.04–10.88] „rydw i'n gofyn un ar y ffwrdd. Mae'r Duvet Easy Rest Plain yn duvet a chyflawni, felly dim llinyn y byd arall.“
  - [15.04–17.60] „Mae'n dod i mewn i'r wasanaeth a'n dod i mewn i'r twmble dryer.“
  - [21.92–25.28] „Ac mae'r peth gorau yw bod y ffibrau allweddol yn cyfathrebu ag eich byd.“
  - [25.44–27.64] „Syfio am y gei'r ffibrau allweddol a'r llaeth yn ddiweddar ac annergyfwng y fano.“
  - [27.64–31.36] „Rydw i'n gofyn i chi fod cymaint yn rydw i'n byw yn ddarllen ac mae'r ddau dufrealion plem“
  - [31.36–37.38] „yn di. Marwch wrth gael eu toriadu ac yn clathro'n dda a'n hollbubyn.“
  - [37.38–39.36] „Dylid y byd ar safonau unraig.“
  - [39.36–44.26] „Mae'rcelyn ddufrayn Lleithi Angen Plain FM yna wrth ddadleu'r dau dduferealion plem“
  - [44.26–48.40] „rhyf disgybl tadiau o ran fry Điogel Cymdeithaeth. Gwella i'ch DUVET.“
- **ElevenLabs-Versuch (1×, wie vorgegeben):** Ich habe einen Flow angelegt (ID JLJvQAcJPDNthDtuQpu4) und das MP4 per `creative_attach_reference_file` angehängt (Asset lAnpLqbptdSxqBmhwk8s). Der Speech-to-Text-Knoten nimmt aber nur Audio an. Der Testaufruf mit `estimate_only` scheiterte deshalb mit „no input on node … accepts modality 'video'“. Die Upload-Tools für eine lokale Audiodatei (`creative_create_asset_upload` / `creative_finalize_asset_upload`) gibt es in dieser Session nicht (ToolSearch: „No matching deferred tools found“). **Eine ElevenLabs-Transkription wurde daher nicht gestartet.** Ob das Anhängen selbst Credits gekostet hat: nicht verifiziert.
- **Ersatz:** lokales faster-whisper (Modell small.en, Englisch erzwungen, Datei `/wf/s2b2_meta/asr_small_en.json`). Gegengeprüft wurde Zeile für Zeile mit den eingeblendeten Untertiteln (0,5-s-Streifen). Ein zweiter Beleg: Ab 6,32 s ist die Tonspur identisch mit 145443331 (Kreuzkorrelation 0,995, Versatz 2,52 s), deren Transkript englisch ist.
- **Korrigiertes Transkript** (Zeiten aus Whisper, Wortlaut nach den Untertiteln; in Klammern steht, wo Whisper abweicht):
  - [0.68–6.26] „I bloody hate changing the bed. When everyone kept saying you never have to change your bed linen again, I ordered one straight away.“
  - [6.50–10.84] „The Pleene EasyRest™ Duvet is a duvet and cover in one. So no more separate bed linen.“ (Whisper: „The plain easy rest duvet is a duvet and covering one.“)
  - [10.84–14.96] keine Sprache
  - [14.96–17.82] „Just put it in the washing machine and then in the tumble dryer.“
  - [17.82–21.76] keine Sprache
  - [21.76–26.38] „And the best thing is, the breathable fibres adapt to your body. Nice and warm in the winter,“
  - [26.38–30.62] „comfortable and cool in the summer. I swear to you, my bed always feels fresh“
  - [30.62–36.10] „and the Pleene™ Pillow Cases really feel super soft. And the Pleene EasyRest™ comes in loads of limited colours“ (Whisper: „clean pillowcases“, „clean easy rest“)
  - [36.10–40.68] „and all different sizes — honestly, the hardest part was picking one. At the moment,“
  - [40.68–46.48] „the Pleene EasyRest™ Duvet is even on offer with two free Pleene™ Pillow Cases and a 90-night trial sleep guarantee,“
  - [46.48–48.96] „you can simply test it yourself.“
- **Audio-Check:** Mittelwert −17,2 dB, Spitze −5,3 dB, keine Stille unter −35 dB. In den Sprechpausen (11–14,5 s und 18,2–21,5 s) liegt der Pegel bei −29 / −32 dB, und das Spektrogramm zeigt tonale Linien. Das spricht für leise Hintergrundmusik, ist aber nicht verifiziert.

**Einblendungen (wörtlich, mit Sekunden)**
- Untertitel (weiße Box, schwarze fett-kursive Sans, satzweise, unteres Drittel; ab 43,3 s oben):
  - 0.0–2.9 „I bloody hate changing the bed“
  - 3.0 „— When everyone kept saying“
  - 3.5–5.0 „you never have to change your bed linen again,“
  - 5.5–6.0 „I ordered one straight away“
  - 6.5–9.5 „The Pleene EasyRest™ Duvet is a duvet and cover in one“
  - 10.0–13.5 „So no more separate bed linen“
  - 14.0–16.5 „Just put it in the washing machine“
  - 17.0–22.0 „and then in the tumble dryer“
  - 22.5–23.0 „And the best thing is,“
  - 23.5–25.0 „the breathable fibres adapt to your body“
  - 25.5–26.5 „Nice and warm in the winter,“
  - 27.0–27.5 „Comfortable and cool in the summer“
  - 28.0–30.0 „I swear to you, my bed always feels fresh“
  - 30.5–33.5 „And the Pleene™ Pillow Cases really feel super soft“
  - 34.0–36.5 „And the Pleene EasyRest™ comes in loads of limited colours“
  - 37.0–38.0 „and all different sizes“
  - 38.5–40.0 „— honestly, the hardest part was picking one“
  - 40.5–43.0 „At the moment, the Pleene EasyRest™ Duvet is even on offer“
  - 43.5–45.0 „with two free Pleene™ Pillow Cases“
  - 45.5–47.5 „And a 90-night trial sleep guarantee,“
  - 48.0–49.5 „you can simply test it yourself“
- Produktbild-Einsätze 33,8–37,1 s (wechselnde Farben, ohne Farbnamen): Blau, Bordeaux, Schwarz, Koralle, Mintgrün, Beige/Sand, Anthrazit, Braun.
- Angebotskarte 43,3–49,5 s (KI-Schlafzimmerbild mit mintgrüner Decke): „This week only: 2 FREE Pillow Cases with every DUVET“ [Uhr-Icon], runder Badge „FREE this week only“, „£39.99“ durchgestrichen, daneben ein Kissenbezug.

**Hook (0–3 s)**
- Gesprochen: „I bloody hate changing the bed. When everyone kept saying …“
- Eingeblendet: „I bloody hate changing the bed“, ab 3,0 s „— When everyone kept saying“
- Bild: Totale eines britischen Schlafzimmers. Ein Mann zerrt eine weiße Decke aus einem grün gemusterten Bezug und gestikuliert genervt zur Kamera.

**Aufbau**
| Teil | Sekunden | Inhalt |
|---|---|---|
| Hook | 0–2,9 | „I bloody hate changing the bed“ (Frust-Statement) |
| Problem | 0–6,3 | Bettbeziehen nervt. Dazu Social-Proof-Auslöser „everyone kept saying you never have to change your bed linen again“ → „I ordered one straight away“ |
| Verstärkung | **fehlt** | keine weitere Problemvertiefung |
| Mechanismus | 6,5–10,8; 21,8–27,5 | „duvet and cover in one“ / „no more separate bed linen“; „breathable fibres adapt to your body. Nice and warm in the winter, comfortable and cool in the summer“ |
| Lösung/Demo | 6,3–22,1 | graue Decke aufs Bett, dann Waschmaschine (14–17,8) und „tumble dryer“ (17–22) |
| Beweis | 28–33,5 | nur persönliches Testimonial: „I swear to you, my bed always feels fresh“, „Pillow Cases really feel super soft“. Keine Zahlen im Video; „Over 10,000 Happy Customers“ steht nur in der Link-Beschreibung |
| (Auswahl/Knappheit) | 33,6–40,1 | „loads of limited colours“, „all different sizes“, Farb-Einsätze |
| Angebot | 40,5–49,5 | „on offer with two free Pleene™ Pillow Cases and a 90-night trial sleep guarantee“ plus Karte „This week only …“, „£39.99“ durchgestrichen |
| CTA | 48–49,5 | nur weich: „you can simply test it yourself“. Ein expliziter Link-CTA fehlt im Video; der Button lautet „Order now“ |

**Szenenliste (Schnitte 0.3: 6.32, 13.72, 22.12, 27.84, 30.36, 33.60, 40.08; zusätzlich 0.15: 19.40, 43.28)**
| s | Szene |
|---|---|
| 0–6.32 | Totale Schlafzimmer (grüne Wand, Erkerfenster, Lampenschirm im Marokko-Muster, Holzbett mit Regal-Kopfteil, Teppichboden). Mann zieht alte Decke und Bezug ab und spricht zur Kamera. |
| 6.32–13.72 | Mann am Bett mit grauer EasyRest, Blick und Sprechen in die Kamera, hebt die Decke an |
| 13.72–19.40 | Küche: Mann hockt vor silbernem Frontlader, stopft graue Decke hinein (blau-weiße Musterfliesen, Waschmittelflasche) |
| 19.40–22.12 | dieselbe Küche, Jump-Cut: Mann beugt sich zur Maschinentür („tumble dryer“). Gezeigt wird dieselbe Maschine; ein separater Trockner ist nicht zu sehen (nicht verifiziert) |
| 22.12–27.84 | Mann liegt unter grauer Decke im Bett und spricht in die Kamera (Selfie, von oben) |
| 27.84–30.36 | Mann sitzt auf der Bettkante (graue Decke, Holz-Kleiderschrank) und spricht |
| 30.36–33.60 | Totale: Mann breitet die graue Decke aus |
| 33.60–40.08 | Mann hinter dem Bett, hebt die Decke; 33,8–37,1 Produkt-Einsätze in 8 Farben |
| 40.08–43.28 | Mann sitzt frontal auf der Bettkante und spricht |
| 43.28–49.53 | wie zuvor, dazu Angebotskarte als Overlay, Untertitel oben |

**Personen / Sprecher**
- Ein Mann, geschätzt 30–40 Jahre, sportlich, kurze dunkle Haare, Vollbart, graues ärmelloses Shirt, schwarze Shorts, Smartwatch. Rolle: UGC-Creator bzw. Kunden-Persona.
- **Echte Person.** Begründung: lippensynchrones Sprechen in die Kamera (22–28 s, 40–49 s), natürliche Bewegungen, echtes Zuhause mit konsistenten Details über mehrere Räume, O-Ton mit f0-Median ca. 151 Hz (männlich). Ob er echter Kunde oder bezahlter Creator ist: nicht verifiziert.
- Spricht selbst (O-Ton, teils als Off über B-Roll).

**Setting:** privates britisches Schlafzimmer (grüne Wand, Erker) und Küche mit Waschmaschine.

**Avatar / Angle**
- Avatar: Erwachsene (auch Männer, ca. 25–55), die das Bettbeziehen hassen und durch Mundpropaganda neugierig sind. Altersangabe ist geschätzt.
- Angle: **C** (Beziehen), dazu F-Social-Proof („everyone kept saying“), B (warm/kühl), A-nah (Waschmaschine/Trockner), F-Knappheit/Farbe („limited colours“), F-Angebot.

**Haupt-Emotion:** Frust („bloody hate“), dann Erleichterung und Begeisterung.

**Tempo / Untertitel / Audio:** 7 Schnitte (0.3) → **1,41 pro 10 s** (pro 10-s-Block: 1/1/2/2/1). Feinwert 9 Schnitte → 1,82 pro 10 s. Untertitel ja (weiße Box, schwarze fett-kursive Schrift). O-Ton, vermutlich leise Musik (nicht verifiziert).

**Zahlen und Behauptungen (wörtlich):** „two free Pleene™ Pillow Cases“; „a 90-night trial sleep guarantee“; Karte: „This week only: 2 FREE Pillow Cases with every DUVET“, „FREE this week only“, „£39.99“ (durchgestrichen); „loads of limited colours“, „all different sizes“; „Nice and warm in the winter, comfortable and cool in the summer“. Nur im Anzeigentext: „dry in 2 hours“, „Over 10,000 Happy Customers“.

**Angebot:** 2 Kissenbezüge gratis, Wert über das durchgestrichene „£39.99“, zeitlich knapp („This week only“), 90 Nächte Probeschlafen. Farbknappheit wird nur als „limited colours“ angedeutet, ohne Stückzahl.

**Varianten (verifiziert):**
- **145443331 und 163921089** (laut Batch 1 byte-identisch): Ab dem ersten Schnitt identischer Body. Tonspur-Korrelation 0,995 bei 2,52 s Versatz, Schnittmuster deckungsgleich (+2,52 s). Nur der Hook ist ausgetauscht: hier 0–6,32 s „I bloody hate changing the bed …“, dort 0–3,8 s „I haven't changed my bed linen in three months“.
- Derselbe Primärtext T04 läuft aktiv auch bei 193234219 und 193234221 (Inhalt nicht geprüft). Inaktive 50-s-Versionen mit T04: 176509065, 171191577, 160709926, 160709967 (nicht verifiziert).
- Footage desselben Creators steckt auch in 178749251/254/247 (identische Einstellung bei 13,1 s dort = 22,3 s hier).

---

#### Video 151025063 – No More Fighting With Duvet Covers

**Metadaten**
| Feld | Wert |
|---|---|
| Meta-ID | 1369166828764339 |
| Start / Status | 2026-08-22 / aktiv |
| Tage aktiv | 48 |
| performance_score | 86 (Optimized), in get_ad und s1 gleich |
| used_count | 1 |
| Block (s1) | Winner (Top-20-Rang 11) |
| Landingpage | https://pleene.com/products/easyrest |
| CTA | SHOP_NOW („Shop now“) |
| Plattformen | facebook, instagram, audience_network, messenger, threads; get_ad.countries = [] (leer, abweichend von den anderen Ads) |
| Primärtext (T01) | „Duvet + Cover in One [Emoji: Mond]<br>The Pleene EasyRest™ makes changing the bed finally simple. Wash it, dry it, and lay it back on — that's it.<br>✓ No more wrestling with a separate duvet cover<br>✓ Pleasantly cool in summer, cosily warm in winter<br>✓ Hypoallergenic and kind to sensitive skin<br>Get 2 free Pleene™ Pillow Cases today (worth £39.99).<br>90 nights to try it risk-free.<br>Enjoy a bed that always feels fresh.“ |
| Link-Beschreibung | „[5 Stern-Emojis] – Over 10,000 Happy Customers“ |
| share_url | https://app.gethookd.ai/share/ad/151025063?signature=6a64477f3dd49f4b0e862e714a6a052a0839cfe3382654d8e4902e827f95d481 |
| Ad Library | https://www.facebook.com/ads/library/?id=1369166828764339 |
| Technik | 29,39 s, 720×1280, 25 fps |

**Transkript (GetHooked, vollständig, korrekt; mit den Untertiteln abgeglichen)**
- [0.00–4.24] „I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“
- [4.24–8.32] „The Pleen Easy Rest Duvet is a duvet and cover in one. No more separate bed linen,“
- [8.32–11.44] „just put it in the washing machine and then in the tumble dryer. And the best thing is,“
- [11.44–14.64] „the breathable fibres adapt to your temperature. Nice and warm in winter,“
- [14.64–17.76] „and comfortable and cool in summer. I swear to you, my bed always feels fresh.“
- [17.76–22.00] „And the Pleen Pillow Cases really feel super soft. At the moment, the Pleen Easy Rest Duvet“
- [22.00–27.36] „is even on offer with two free Pleen Pillow Cases worth £39.99. And with a 90 night trial sleep“
- [27.36–29.28] „guarantee, you can simply test it yourself.“
- Audio-Check: Mittelwert −17,0 dB, Spitze −2,2 dB, durchgehend Sprache. Unter der Stimme liegt eine konstante tonale Linie bei ca. 600 Hz, also vermutlich ein Musikbett.
- Stimme: Off-Sprecherin. f0-Median 193 Hz (P25 182, P75 217) liegt im typischen Frauenbereich → vermutlich weiblich. Ob KI-Stimme (TTS) oder Mensch: nicht verifiziert. Keine Person auf dem Bild spricht lippensynchron.

**Einblendungen (Untertitel: schwarze Box, weiße fette Sans, Poppins-artig, mittig, zweizeilig)**
- 0.0–2.4 „I only ordered it because changing the bed linen“
- 2.5–4.4 „every time gave me pain in my shoulders and back“
- 4.5–7.0 „The Pleene EasyRest™ Duvet is a duvet and cover in one“
- 7.5–8.0 „No more separate bed linen“
- 8.5–9.5 „Just put it in the washing machine“
- 10.0–10.5 „and then in the tumble dryer.“
- 11.0–11.5 „And the best thing is,“
- 12.0–13.5 „the breathable fibres adapt to your temperature“
- 14.0–15.5 „Nice and warm in winter and comfortable and cool in summer“
- 16.0–17.5 „I swear to you, my bed always feels fresh“
- 18.0–20.0 „And the Pleene™ Pillow Cases really feel super soft“
- 20.5–22.0 „At the moment, the Pleene EasyRest™ Duvet“
- 22.5–26.0 „is even on offer with two free Pleene™ Pillow Cases worth £39.99“
- 26.5–27.5 „And with a 90-night trial sleep guarantee“
- 28.0–29.4 „you can simply test it yourself“
- Grafik: roter Schmerz-Glow auf Rücken- und Hüfthöhe (1,2–3,1 s). 3D-Anatomie-Render der Schulter mit den Beschriftungen „TRAPEZIUS [UPPER]“, „TRAPEZIUS [MIDDLE]“, „SCAPULA“ und Pfeilen (3,1–4,4 s).

**Hook (0–3 s):** gesprochen „I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“ Eingeblendet: „I only ordered it because changing the bed linen“, ab 2,5 s „every time gave me pain in my shoulders and back“. Bild: Frau macht das Bett, dann rotes Schmerz-Overlay am Rücken, dann Kampf mit dem Bezug.

**Aufbau**
| Teil | Sekunden | Inhalt |
|---|---|---|
| Hook | 0–4,2 | Kaufgrund Schulter- und Rückenschmerz |
| Problem | 0–4,4 | Kampf mit dem Bezug, rotes Schmerz-Overlay |
| Verstärkung | 3,1–4,4 | nur visuell: 3D-Trapezius-Render (medizinische Anmutung); keine verbale Vertiefung |
| Mechanismus | 4,2–8,3; 11,4–17,8 | „duvet and cover in one“, „breathable fibres adapt to your temperature“ |
| Lösung/Demo | 8,3–11,4 | Waschmaschine, dann Trockner |
| Beweis | 14,6–20,4 | nur Ich-Testimonial („I swear to you, my bed always feels fresh“, „super soft“). Keine Zahlen; „Over 10,000 Happy Customers“ nur in der Link-Beschreibung |
| Angebot | 20,4–27,4 | „two free Pleen Pillow Cases worth £39.99“, „90 night trial sleep guarantee“ |
| CTA | 27,4–29,3 | weich: „you can simply test it yourself“. Expliziter Link-CTA fehlt; Button „Shop now“ |

**Szenenliste (alle 22 Schnitte bei 0.15; 0.3: 1.88, 2.56, 3.08, 4.40, 7.08, 8.40, 9.72, 10.80, 12.64, 14.60, 16.00, 17.88, 18.64, 19.72, 20.44, 22.76, 26.16)**
| s | Szene |
|---|---|
| 0–1.24 | Frau (ca. 25–35, gestreifte Bluse, weiße Hose) richtet Kissen auf einem Bett mit taupefarbener Steppdecke; weißes Schlafzimmer |
| 1.24–1.88 | dieselbe Frau neben einem Bett mit weißer Decke, roter Glow auf Rückenhöhe |
| 1.88–2.56 | Frau schüttelt weiße Decke vor einem Dünengras-Bild, roter Glow |
| 2.56–3.08 | Frau kämpft seitlich am Bett mit grau-weißem Bezug, roter Glow |
| 3.08–4.40 | 3D-Anatomie-Render der Schulter (Trapezius/Scapula) |
| 4.40–5.84 | Hand (gestreifter Ärmel) streicht über die taupe Steppdecke |
| 5.84–7.08 | blonde Frau sitzt im Bett unter der taupe Decke |
| 7.08–8.40 | Frau zieht die taupe Decke über sich |
| 8.40–9.72 | Männerarm (blaues T-Shirt, Uhr) befüllt einen weißen Frontlader |
| 9.72–10.80 | Arm legt dunkle Decke in eine Trockner-/Waschtrommel |
| 10.80–11.56 | muskulöser Mann mit nacktem Oberkörper von oben in mintgrüner Decke (KI-Optik) |
| 11.56–12.64 | taupe Steppdecke in Nahaufnahme mit Kamerafahrt |
| 12.64–14.60 | Mann mit Glatze und grauem Bart liegt unter beiger Decke, schwarzes Kissen |
| 14.60–16.00 | Hand drückt auf die taupe Decke |
| 16.00–17.88 | KI-Mann mit nacktem Oberkörper im Bett, mintgrüne Decke, Nachttischlampe |
| 17.88–18.64 | junge Frau (ca. 20–30, Streifenshirt) hält ein beiges Kissen hoch und lächelt in die Kamera |
| 18.64–19.72 | Kissen in Nahaufnahme, Hände |
| 19.72–20.44 | Frau umarmt das Kissen |
| 20.44–21.60 | mintgrüne Decke auf dem Bett, Hand hebt die Kante |
| 21.60–22.76 | Hände heben die mintgrüne Decke |
| 22.76–26.16 | Hände tätscheln mintgrüne Kissen |
| 26.16–27.52 | mintgrüne Decke im Sonnenlicht, Hand glättet |
| 27.52–29.39 | Arm im grauen Ärmel glättet die mintgrüne Decke |

**Personen / Sprecher**
- Mehrere Personen, Collage-Schnitt:
  - Frau in Streifenbluse: echte Aufnahme (natürliche Bewegung); ob Stock oder UGC: nicht verifiziert.
  - Muskulöser Mann mit nacktem Oberkörper (10,8 und 16,0 s): **KI-generiert, wahrscheinlich.** Begründung: glatte Plastik-Haut, generisches Model-Gesicht, gerenderte Lichtstimmung; Batch 1 sah dieselbe Figur in 136389861.
  - Mann mit Glatze und grauem Bart (ca. 50–60): echte Aufnahme.
  - Junge Frau mit Kissen: wirkt echt (natürliche Haut und Mimik), nicht verifiziert.
  - 3D-Render: Grafik bzw. Stock.
- Gesprochen wird von einer weiblichen Off-Stimme (siehe oben). Die Person im Bild ist nicht die Sprecherin.

**Setting:** weiße, minimalistische Schlafzimmer, Waschmaschine, ein Studio mit 3D-Grafik.

**Avatar / Angle:** Avatar sind Menschen mit Schulter- und Rückenschmerzen beim Bettbeziehen; die Ausrichtung auf ältere Menschen ist eine Annahme, nicht verifiziert. Angle: **E** (körperliche Beschwerden), dazu C, B und F-Angebot.

**Haupt-Emotion:** Schmerz und Frust, dann Erleichterung.

**Tempo / Untertitel / Audio:** 17 Schnitte (0.3) → **5,78 pro 10 s** (Blöcke 7/7/3). Feinwert 22 → 7,48 pro 10 s. Das ist das schnellste Video im Batch. Untertitel ja (schwarze Box, weiße Schrift). Weibliche Off-Stimme plus vermutlich Musikbett.

**Zahlen und Behauptungen (wörtlich):** „gave me pain in my shoulders and back“; „two free Pleen Pillow Cases worth £39.99“; „90 night trial sleep guarantee“; „the breathable fibres adapt to your temperature. Nice and warm in winter, and comfortable and cool in summer“. Nur im Anzeigentext: „Hypoallergenic and kind to sensitive skin“, „90 nights to try it risk-free“, „(worth £39.99)“, „Over 10,000 Happy Customers“.

**Angebot:** 2 Kissenbezüge gratis mit Wertangabe „worth £39.99“, gesprochen und im Untertitel. 90 Nächte. Keine Zeit- oder Farbknappheit.

**Varianten:**
- **136389861** (Batch 1): gleicher Skript-Body ab „The Pleene EasyRest™ Duvet is a duvet and cover in one“ bis „test it yourself“, gleicher Primärtext T01, teils gleiches Footage (KI-Mann in Mintgrün, Glatzkopf mit beiger Decke, Arm im blauen Shirt an der Waschmaschine). Unterschiede: anderer Hook (dort KI-Presenter „If your shoulders ache don't do this“) und **andere Stimme**. 136389861 liegt bei f0 ca. 131 Hz (männlich), 151025063 bei ca. 193 Hz; die Audio-Korrelation beträgt 0,05.
- Die Headline-Familie „No More Fighting With Duvet Covers“ umfasst 175 Ads (s1); die Inhaltsgleichheit mit weiteren Ads ist nicht verifiziert.

---

#### Video 168246678 – Check This Before You Buy

**Metadaten**
| Feld | Wert |
|---|---|
| Meta-ID | 1607904514111212 |
| Start / Status | 2026-08-29 / aktiv |
| Tage aktiv | 41 |
| performance_score | **100 (Winning)**, in get_ad und s1 gleich |
| used_count | 1 |
| Block (s1) | Winner (Top-20-Rang 12) |
| Landingpage | https://pleene.com/products/easyrest |
| CTA | ORDER_NOW („Order now“) |
| Plattformen | facebook, instagram, audience_network, messenger, threads; GB |
| Primärtext (T25) | „Before you buy a coverless duvet, check three things: [Emoji: Häkchen]<br>✓ Does the WHOLE thing fit a normal washing machine?<br>✓ Is it dry in 2 hours without a tumble dryer?<br>✓ Can you test it at home for 90 nights?<br>The Pleene EasyRest™: yes, yes and yes.“ |
| Link-Beschreibung | „[5 Stern-Emojis] – Over 10,000 Happy Customers“ |
| share_url | https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59 |
| Ad Library | https://www.facebook.com/ads/library/?id=1607904514111212 |
| Technik | 27,12 s, 720×1280, 30 fps |

**Transkript:** GetHooked meldet `no_speech`, das Transkript ist leer. **Audio-Check bestätigt: nur Musik.**
- Mittelwert −16,2 dB, Spitze −0,9 dB, keine Stille.
- Spektrogramm: stabile tonale Akkordblöcke unter ca. 1,9 kHz und regelmäßige breitbandige Perkussions-Transienten; keine Sprachformanten.
- Ein Gegentest mit lokalem Whisper (small.en) halluzinierte „Thanks for watching, see you next time.“ (6,86–26,52 s, no_speech_prob 0,67, avg_logprob −0,97). Das ist das bekannte Platzhalter-Fehlerbild.

**Einblendungen (weiße Schrift mit Schatten, mittig; grüne Häkchen-Emojis)**
- 0.0–3.7 „Before you buy a coverless duvet check 3 things“
- 3.7–9.87 „1. Does the WHOLE thing fit a normal washing machine?“, ab ca. 6,5 s zusätzlich „Ours does. [Emoji: Häkchen]“
- 9.87–16.1 „2. Is it dry in 2 hours without a tumble dryer?“, ab ca. 12,5 s (Zoom-Animation) „2 hours. No dryer. [Emoji: Häkchen]“
- 16.1–21.53 „3. Can you test it at home for 90 nights?“, ab ca. 18,0 s (Zoom-Animation) „90 nights. Zero risk. [Emoji: Häkchen]“
- 21.53–ca. 23.3 „The Pleene EasyRest: yes, yes and yes.“
- ca. 23.5–25.07 „On offer now — with 2 free pillow cases.“
- 25.07–27.12 Endkarte: „Pleene“ / „THE ORIGINAL“ / „2× Pleene™ Pillow Cases FREE“ / „Value £39.99“ / „90-Night Trial“

**Hook (0–3 s):** gesprochen: keiner (nur Musik). Eingeblendet: „Before you buy a coverless duvet check 3 things“. Bild: Draufsicht auf ein Bett mit salbeigrüner Steppdecke, langsamer Push-in.

**Aufbau**
| Teil | Sekunden | Inhalt |
|---|---|---|
| Hook | 0–3,7 | Kaufcheckliste als Einwand-Vorwegnahme |
| Problem | **fehlt** (nur implizit) | Angst vor einer Decke, die nicht in die Maschine passt oder nicht trocknet |
| Verstärkung | **fehlt** | |
| Mechanismus | 3,7–21,5 | drei Prüfkriterien, jeweils mit „Ours does“ / „2 hours. No dryer.“ / „90 nights. Zero risk.“ |
| Lösung | 21,5–23,3 | „The Pleene EasyRest: yes, yes and yes.“ |
| Beweis | **fehlt** | nur Behauptungen mit Häkchen und gerenderte Demo; keine Testimonials, keine Zahlen außer 2 h und 90 Nächte |
| Angebot | 23,5–27,1 | „On offer now — with 2 free pillow cases.“ und Endkarte „2× … FREE / Value £39.99 / 90-Night Trial“ |
| CTA | **fehlt im Video** | Button „Order now“ |

**Szenenliste (0.3: 3.70, 4.37, 9.87, 16.10, 21.53; 0.15 zusätzlich: 7.53, 18.77, 25.07)**
| s | Szene |
|---|---|
| 0–3.70 | Draufsicht Bett: salbeigrüne Steppdecke und Kissen, Jute-Teppich, Blumen auf dem Nachttisch |
| 3.70–4.37 | Waschküche (weiße Schränke, Fenster, Korb); Decke quillt aus offenem Frontlader |
| 4.37–7.53 | Nahaufnahme: Faust und Arm stopfen die Decke in die Trommel; 7,0–7,5 Tür wird geschlossen |
| 7.53–9.87 | geschlossene Tür, Decke in der Trommel sichtbar |
| 9.87–16.10 | heller Raum, Holz-Wäscheständer; Hand legt die Decke darüber und streicht sie glatt |
| 16.10–18.77 | abendliches Schlafzimmer mit Lampe, Bett mit grüner Decke (Push-in) |
| 18.77–21.53 | Deckentextur in Nahaufnahme, Lampen-Bokeh |
| 21.53–25.07 | helles Schlafzimmer, Bett mit grüner Decke (Push-in) |
| 25.07–27.12 | Endkarte auf beige strukturiertem Hintergrund |

**Personen / Sprecher:** keine Person, nur Hand und Arm, kein Sprecher. Bildmaterial **vermutlich KI-generiert** (nicht verifiziert). Begründung: glatte fotoreale Render-Optik, generische und makellose Interieurs, keine Gesichter, identische Decke in allen Räumen, weiche synthetische Kamerafahrten.

**Setting:** Schlafzimmer (Draufsicht), Waschküche, Raum mit Wäscheständer, Schlafzimmer am Abend; dazu die Endkarte.

**Avatar / Angle:** Avatar sind lösungsbewusste, skeptische Vergleichskäufer, die „coverless duvets“ schon kennen. Angle: **F-Einwand/Kaufhilfe (Checkliste)** mit **A** (ganze Decke waschen, trocknen) und F-Angebot. Positionierung „THE ORIGINAL“ gegen Nachahmer.

**Haupt-Emotion:** Neugier und Skepsis, dann Sicherheit und Vertrauen. Ruhige Tonalität.

**Tempo / Untertitel / Audio:** 5 Schnitte (0.3) → **1,84 pro 10 s** (Blöcke 3/1/1). Feinwert 8 → 2,95 pro 10 s. Keine Untertitel (keine Sprache), nur Text-Overlays. Nur Musik.

**Zahlen und Behauptungen (wörtlich):** „check 3 things“; „fit a normal washing machine“; „Is it dry in 2 hours without a tumble dryer?“; „2 hours. No dryer.“; „90 nights. Zero risk.“; „On offer now — with 2 free pillow cases.“; „2× Pleene™ Pillow Cases FREE“; „Value £39.99“; „90-Night Trial“; „THE ORIGINAL“.

**Angebot:** 2 Kissenbezüge gratis, als Wert „Value £39.99“ auf der Endkarte, dazu „90-Night Trial“ und „Zero risk“. Keine Zeit- oder Farbknappheit.

**Varianten (verifiziert):**
- **168246686**: Bild nach 3,7 s identisch (Frame-Differenz ab 3,7 s nur Kodierrauschen 0,2–0,8, davor ca. 1,0). Tonspur PCM-identisch (md5 gleich). Nur der Hook-Text unterscheidet sich.
- Gleicher Primärtext T25: aktiv 185228764 und 200490712 (je 27 s), inaktiv 168246672. Deren Bildinhalt ist nicht verifiziert.

---

#### Video 168246686 – Check This Before You Buy

**Metadaten**
| Feld | Wert |
|---|---|
| Meta-ID | 2035183934551496 |
| Start / Status | 2026-08-29 / aktiv |
| Tage aktiv | 41 |
| performance_score | 86 (Optimized), in get_ad und s1 gleich |
| used_count | 1 |
| Block (s1) | Winner (Top-20-Rang 14) |
| Landingpage | https://pleene.com/products/easyrest |
| CTA | ORDER_NOW („Order now“) |
| Plattformen | facebook, instagram, audience_network, messenger, threads; GB |
| Primärtext | T25, identisch mit 168246678 |
| Link-Beschreibung | „[5 Stern-Emojis] – Over 10,000 Happy Customers“ |
| share_url | https://app.gethookd.ai/share/ad/168246686?signature=a360c60671d85ebeec646d4238239e0ec57ba2d7b037d0bb4c8888b606378db0 |
| Ad Library | https://www.facebook.com/ads/library/?id=2035183934551496 |
| Technik | 27,12 s, 720×1280, 30 fps |

**Transkript:** `no_speech`. **Nur Musik**: Die Tonspur ist PCM-identisch mit 168246678 (dort per Spektrogramm geprüft). Whisper halluziniert auch hier „Thanks for watching, see you next time.“ (no_speech_prob 0,67).

**Einblendungen:** abweichend nur der Hook:
- 0.0–ca. 1.9 „Seen coverless duvets all over your feed?“
- ca. 2.0–3.7 „Check these 3 things before you buy.“
- Ab 3,7 s alles identisch mit 168246678 (Checkliste, „Ours does.“, „2 hours. No dryer.“, „90 nights. Zero risk.“, „The Pleene EasyRest: yes, yes and yes.“, „On offer now — with 2 free pillow cases.“, Endkarte „Pleene / THE ORIGINAL / 2× Pleene™ Pillow Cases FREE / Value £39.99 / 90-Night Trial“).

**Hook (0–3 s):** gesprochen: keiner. Eingeblendet: „Seen coverless duvets all over your feed?“, dann „Check these 3 things before you buy.“ Der Hook greift ein Trend- bzw. Feed-Phänomen auf (Pattern-Recognition beim Zuschauer), statt direkt mit der Checkliste zu starten.

**Aufbau:** wie 168246678. Hook 0–3,7; Problem **fehlt** (implizit); Verstärkung **fehlt**; Mechanismus 3,7–21,5; Lösung 21,5–23,3; Beweis **fehlt**; Angebot 23,5–27,1; CTA **fehlt im Video**.

**Szenenliste:** identisch mit 168246678 (Schnitte 3.70, 4.37, 9.87, 16.10, 21.53; fein 7.53, 18.77, 25.07). An jedem Schnitt wurde ein Frame angesehen (3.90, 4.57, 7.73, 10.07, 16.30, 18.97, 21.73, 25.27); Inhalte wie oben.

**Personen / Sprecher:** keine Person, nur Hand und Arm; vermutlich KI-generiert (Begründung wie 168246678, nicht verifiziert). **Setting:** wie 168246678.

**Avatar / Angle:** Avatar sind Menschen, denen „coverless duvets“ im Feed begegnet sind (Trend-aware, Vergleichskäufer). Angle: **F-Einwand/Kaufhilfe** mit **A**, F-Angebot; im Hook zusätzlich Trend- bzw. Social-Proof-Anklang („all over your feed“).

**Haupt-Emotion:** Neugier und Wiedererkennung, dann Sicherheit.

**Tempo / Untertitel / Audio:** **1,84 Schnitte pro 10 s** (Feinwert 2,95). Keine Untertitel, Text-Overlays. Nur Musik.

**Zahlen und Behauptungen:** wie 168246678 („2 hours. No dryer.“, „90 nights. Zero risk.“, „Value £39.99“, „2× Pleene™ Pillow Cases FREE“, „90-Night Trial“).

**Angebot:** wie 168246678.

**Varianten:** **168246678** (verifiziert identisch bis auf den Hook-Text 0–3,7 s). Damit eignet sich das Paar als sauberer Hook-A/B-Test: Score 100 bei 168246678 („Before you buy …“) gegenüber 86 bei 168246686 („Seen coverless duvets …“), beide 41 Tage, used_count 1. Weitere T25-Ads: 185228764, 200490712, 168246672 (nicht verifiziert).

---

#### Video 178749251 – Warm Enough For A British Winter

**Metadaten**
| Feld | Wert |
|---|---|
| Meta-ID | 1792003651846452 |
| Start / Status | 2026-09-16 / **inaktiv laut get_ad vom 2026-10-08** (end_date 2026-10-07, active_in_library 0). Im früheren Lauf (agent1/s1) noch aktiv. |
| Tage aktiv | 22 (start_to_end_date); s1 nannte 23 |
| performance_score | **n/a** (get_ad: null, weil GetHooked inaktive Ads nicht bewertet). Im früheren Lauf: 81 (Optimized) |
| used_count | 1 |
| Block (s1) | Starker Kandidat (zum Zeitpunkt des früheren Laufs) |
| Landingpage | https://pleene.com/products/easyrest-duvet |
| CTA | SHOP_NOW („Shop now“) |
| Plattformen | facebook, instagram, audience_network, threads; GB |
| Primärtext (T29) | „[Emoji: Schneeflocke] "You'll freeze under that in winter." Here's the honest answer: the Pleene EasyRest™ is rated 10.5 tog, a proper autumn and winter weight, and the whole thing still goes in your washing machine.“ |
| Link-Beschreibung | „10.5 TOG winter warmth · Washes whole · 90-night trial“ |
| share_url | https://app.gethookd.ai/share/ad/178749251?signature=f7a95b97af4df738359f0bc0b4a21bbd6f5508efef5391e097423762a823afc1 |
| Ad Library | https://www.facebook.com/ads/library/?id=1792003651846452 |
| Technik | 34,43 s, 720×1280, 25 fps |

**Transkript (GetHooked, vollständig, korrekt; mit den Untertiteln abgeglichen)**
- [0.00–2.48] „Looks lovely, but you'll freeze under that in winter.“
- [2.48–3.64] „You won't freeze under this.“
- [3.64–5.56] „The Plein EasyRest is made for cold nights.“
- [5.56–7.40] „It's duvet and cover in one, and warmth“
- [7.40–8.48] „doesn't come from bulk.“
- [8.48–10.60] „It comes from the air held between the fibers.“
- [10.60–12.92] „The climate fibers keep your body heat in on cold nights,“
- [12.92–13.68] „but they breathe.“
- [13.68–15.92] „So you're warm all night, and you don't wake up sweating“
- [15.92–17.12] „at 3 AM with the heating on.“
- [17.12–19.46] „And when it needs washing, you don't fight with a cover,“
- [19.46–21.12] „because the cover is already sewn in.“
- [21.12–23.54] „The whole Plein duvet goes in the machine in one piece.“
- [23.54–25.50] „And don't worry, because it's not a heavy duvet,“
- [25.50–27.80] „it still fits easily into a normal washing machine.“
- [27.80–29.08] „Dry again in two hours.“
- [29.08–31.32] „The Plein duvet comes with a 90-night sleep trial,“
- [31.32–33.48] „and right now with two free matching pillowcases.“
- [33.48–35.36] „Link is below.“
- Audio-Check: Mittelwert −16,4 dB, Spitze −2,1 dB, durchgehend Sprache. Unter der Stimme eine konstante tonale Linie bei ca. 700 Hz, also vermutlich ein Musikbett.
- Stimmen: Der Hook-Satz (0–2,5 s) hat f0-Median 170 Hz und eine andere Stimme als der Rest; das Geschlecht ist bei 170 Hz nicht eindeutig. Der Body ab 2,5 s ist eine männliche Off-Stimme mit f0-Median 123 Hz. Das ist tiefer als der O-Ton des Creators in 145443318 (ca. 151 Hz), also vermutlich ein anderer Sprecher oder eine synthetische Stimme (nicht verifiziert). Nicht lippensynchron: Bei 13,1 s ist eine Einstellung aus 145443318 eingeschnitten, in der der Mann einen anderen Satz spricht.

**Einblendungen (Untertitel: weiße Box, schwarze fett-kursive Sans wie bei 145443318; dazu ein Kommentar-Overlay)**
- 0.0–2.48 Kommentar-Karte im Facebook-Stil, oben: „Janet Whitfield [Verifiziert-Haken] Looks lovely but you'll freeze under that in winter[Emoji: frierendes Gesicht]“ · „Like · Reply · 1h“ · Reaktionen [Like/Herz/traurig] „18“. Ob der Kommentar echt ist: nicht verifiziert.
- 2.5–3.5 „You won't freeze under this“
- 4.0–5.5 „The Pleene EasyRest is made for cold nights“
- 6.0–6.5 „It's duvet and cover in one“
- 7.0–8.0 „And warmth doesn't come from bulk“
- 8.5–10.5 „It comes from the air held between the fibres“
- 11.0–12.5 „The climate fibres keep your body heat in on cold nights,“
- 13.0–13.5 „but they breathe“
- 14.0–14.5 „So you're warm all night,“
- 15.0–17.0 „and you don't wake up sweating at 3am with the heating on“
- 17.5–18.0 „And when it needs washing,“
- 18.5–19.0 „you don't fight with a cover,“
- 19.5–21.0 „because the cover is already sewn in“
- 21.5–23.0 „The whole Pleene duvet goes in the machine in one piece“
- 23.5–25.0 „And don't worry: because it's not a heavy duvet,“
- 25.5–27.5 „it still fits easily into a normal washing machine“
- 28.0–29.0 „Dry again in two hours“
- 29.5–31.0 „The Pleene duvet comes with a 90-night sleep trial“
- 31.5–33.0 „And right now with two free matching pillow cases“
- 33.5–34.4 „Link is below“

**Hook (0–3 s):** gesprochen „Looks lovely, but you'll freeze under that in winter.“ und ab 2,48 s „You won't freeze under this.“ Eingeblendet: Kommentar-Karte (Janet Whitfield, siehe oben), ab 2,5 s „You won't freeze under this“. Bild: Männerhand drückt auf eine hochgehaltene mintgrüne Decke vor grüner Wand (Format „Reply to comment“).

**Aufbau**
| Teil | Sekunden | Inhalt |
|---|---|---|
| Hook | 0–2,5 | Einwand-Kommentar „you'll freeze under that in winter“ |
| Problem | 0–2,5 | Angst vor Kälte bzw. zu dünner Decke |
| Verstärkung | 13,7–17,1 | Gegenproblem Überhitzung: „you don't wake up sweating at 3 AM with the heating on“ |
| Mechanismus | 2,5–17,1 | „warmth doesn't come from bulk … air held between the fibres“; „climate fibres keep your body heat in … but they breathe“ |
| Lösung/Demo | 17,1–29,1 | Waschen ohne Bezugskampf („cover is already sewn in“), ganze Decke in die Maschine, „not a heavy duvet“, „Dry again in two hours“ |
| Beweis | **fehlt im Video** | keine Testimonials oder Zahlen; „10.5 tog“ nur im Anzeigentext und in der Link-Beschreibung |
| Angebot | 29,1–33,5 | „90-night sleep trial“, „two free matching pillowcases“ (ohne £-Wert) |
| CTA | 33,5–35,4 | „Link is below.“ (explizit) |

**Szenenliste (0.3: 2.48, 3.64, 6.96, 10.60, 13.12, 14.84, 17.32, 23.52, 26.08, 29.08, 31.28; fein zusätzlich 8.48, 28.36)**
| s | Szene |
|---|---|
| 0–2.48 | Hand drückt auf hochgehaltene mintgrüne Decke (grüne Wand, Holzschrank) plus Kommentar-Karte |
| 2.48–3.64 | Mann (ca. 35–45, graues T-Shirt, dunkle Haare, Bart) hält die mintgrüne Decke hoch und befühlt sie |
| 3.64–6.96 | Mann sitzt im Bett und umarmt die mintgrüne Decke (Spiegelschrank) |
| 6.96–8.48 | Hand auf navyblauer Decke an der Bettkante; oranger Streifenteppich, weiße Fliesen |
| 8.48–10.60 | Hand hebt die Ecke der navy Decke |
| 10.60–13.12 | älterer Mann mit Glatze liegt im Bett unter dunkler Decke (Selfie) |
| 13.12–14.84 | Mann aus 145443318 (Tanktop) liegt unter grauer Decke (wiederverwendete Einstellung) |
| 14.84–17.32 | Totale: Mann schläft unter grauer Decke (grüne Wand, Marokko-Lampe) |
| 17.32–23.52 | silberne Waschmaschine: Hand stopft graue Decke hinein, schließt die Tür (blau-weiße Fliesen) |
| 23.52–26.08 | Mann (weißes T-Shirt) breitet mintgrüne Decke auf dem Bett aus |
| 26.08–28.36 | mintgrüne Decke wird in die silberne Maschine gestopft |
| 28.36–29.08 | Hand schließt die Tür, mintgrüne Decke in der Trommel |
| 29.08–31.28 | Mann lugt unter der mintgrünen Decke hervor und liegt dann entspannt |
| 31.28–34.43 | älterer Mann mit Glatze (ca. 60+, Waffel-Bademantel) sitzt auf dem Bett mit schwarzer Decke, hält zwei schwarze Kissenbezüge hoch und lacht (Terrakottafliesen, Klimagerät) |

**Personen / Sprecher**
- Zwei echte Personen (natürliche Mimik und Bewegung, reale Wohnungen):
  - Mann ca. 35–45: derselbe Creator wie 145443318/145443331. Gleiche Wohnung, gleiche Lampe, gleiche Waschmaschine und Fliesen, eine identische Einstellung.
  - Älterer Mann mit Glatze, ca. 60+: anderes Zuhause.
- Sprecher: männliche Off-Stimme, nicht lippensynchron; KI oder Mensch nicht verifiziert. Der Hook-Satz wird von einer anderen Stimme gesprochen (Kommentatorin), ebenfalls nicht verifiziert.

**Setting:** Schlafzimmer mit grüner Wand, Küche mit Waschmaschine, ein zweites Schlafzimmer (Terrakotta) und ein Raum mit orangem Teppich.

**Avatar / Angle:** Avatar sind britische Käufer, die im Winter frieren und heizbewusst sind („with the heating on“) und zweifeln, ob eine bezugslose Decke warm genug ist. Angle: **B** (Temperatur/Wärme, Tog), dazu F-Einwand (Kommentar), A/C (ganze Decke waschen, kein Bezugskampf), F-Angebot.

**Haupt-Emotion:** Zweifel und Kälte-Sorge, dann Beruhigung und Gemütlichkeit.

**Tempo / Untertitel / Audio:** 11 Schnitte (0.3) → **3,19 pro 10 s** (Blöcke 3/4/3/1). Feinwert 13 → 3,78 pro 10 s. Untertitel ja. Off-Stimme (Hook-Stimme plus männlicher Body), vermutlich Musikbett.

**Zahlen und Behauptungen (wörtlich):** „at 3 AM with the heating on“; „Dry again in two hours.“; „a 90-night sleep trial“; „two free matching pillowcases“; „it's not a heavy duvet, it still fits easily into a normal washing machine“; Kommentar-Reaktionen „18“, „1h“. Nur im Anzeigentext: „rated 10.5 tog, a proper autumn and winter weight“, „10.5 TOG winter warmth · Washes whole · 90-night trial“.

**Angebot:** nur gesprochen und im Untertitel: 90 Nächte und „two free matching pillowcases“. Kein £-Wert, keine Knappheit, keine Angebotskarte. Expliziter CTA „Link is below“.

**Varianten (verifiziert):**
- **178749254 und 178749247**: gleicher Body mit gleicher Off-Stimme (Audio-Korrelation 0,93–0,95 bei +0,24 s bzw. −0,58 s Versatz) und gleichem Schnittmuster. Das Bild von 251 und 254 ist nach dem Hook identisch (Frame-Differenz ab 2,5 s im Median 0,70). Unterschiedlich sind Hook-Clip, Kommentar und Hook-Stimme.
- Zum Primärtext T29 gehören laut s1 außerdem 179476350 und 180646058 (laut s1 vermutlich die 2 Bild-Ads der Familie; nicht verifiziert).
- Footage-Überschneidung mit 145443318/145443331 (derselbe Creator).

---

#### Video 178749254 – Warm Enough For A British Winter

**Metadaten**
| Feld | Wert |
|---|---|
| Meta-ID | 1632682334866450 |
| Start / Status | 2026-09-16 / **inaktiv laut get_ad** (end_date 2026-10-07); im früheren Lauf aktiv |
| Tage aktiv | 22 (start_to_end_date); s1: 23 |
| performance_score | **n/a** (null, inaktiv). Im früheren Lauf: 70 (Growing) |
| used_count | 1 |
| Landingpage | https://pleene.com/products/easyrest-duvet |
| CTA | SHOP_NOW („Shop now“) |
| Plattformen | facebook, instagram, audience_network, threads; GB |
| Primärtext / Link-Beschreibung | T29 bzw. „10.5 TOG winter warmth · Washes whole · 90-night trial“ (wie 178749251) |
| share_url | https://app.gethookd.ai/share/ad/178749254?signature=83a5eb4a50bf72fe2effb4d2ccd1e63703dc4357bed313215787c0765ffb300a |
| Ad Library | https://www.facebook.com/ads/library/?id=1632682334866450 |
| Technik | 34,66 s, 720×1280, 25 fps |

**Transkript (GetHooked, vollständig, korrekt)**
- [0.00–2.56] „No way that keeps you warm in a Scottish winter.“
- [2.56–6.80] „You won't freeze under this. The Plein EasyRest is made for cold nights. It's duvet and cover in“
- [6.80–10.64] „one, and warmth doesn't come from bulk, it comes from the air held between the fibres.“
- [10.64–13.76] „The climate fibres keep your body heat in on cold nights, but they breathe.“
- [13.76–17.36] „So you're warm all night, and you don't wake up sweating at 3am with the heating on.“
- [17.36–21.20] „And when it needs washing, you don't fight with a cover, because the cover is already sewn in.“
- [21.20–24.24] „The whole Plein duvet goes in the machine in one piece. And don't worry,“
- [24.24–27.92] „because it's not a heavy duvet, it still fits easily into a normal washing machine.“
- [27.92–31.44] „Dry again in two hours. The Plein duvet comes with a 90 night sleep trial,“
- [31.44–34.24] „and right now with two free matching pillowcases. Link is below.“
- Audio: Mittelwert −16,4 dB, Spitze −2,5 dB. Hook-Stimme f0-Median 222 Hz (Frauenbereich, vermutlich weiblich). Ein schottischer Akzent ist nicht verifiziert. Body-Stimme 124 Hz (männlich, dieselbe wie 178749251).

**Einblendungen:**
- 0.0–2.72 Kommentar-Karte: „Moira McAllister [Verifiziert-Haken] No way that keeps you warm in a Scottish winter[Emoji: gelbes Gesicht, vermutlich verunsichert/skeptisch – nicht eindeutig lesbar]“ · „Like · Reply · 1h“ · Reaktionen „19“.
- Danach dieselben Untertitel wie 178749251, um ca. +0,24 s verschoben (geprüft bei 3,0 / 4,0 / … / 34,0 s): „You won't freeze under this“ … „Link is below“.

**Hook (0–3 s):** gesprochen „No way that keeps you warm in a Scottish winter.“, ab 2,56 s „You won't freeze under this.“ Eingeblendet: Moira-McAllister-Kommentar, ab ca. 2,7 s „You won't freeze under this“. Bild: Der Mann schläft in der grünen Schlafzimmer-Szene unter der mintgrünen Decke, reckt sich und wacht gemütlich auf.

**Aufbau:** wie 178749251, nur um ca. +0,24 s verschoben: Hook 0–2,7; Problem 0–2,7 (Kälte, regional zugespitzt: Schottland); Verstärkung ca. 13,9–17,4 (Schwitzen um 3 Uhr); Mechanismus 2,7–17,4; Lösung/Demo 17,4–29,3; Beweis **fehlt im Video**; Angebot 29,3–33,7; CTA 33,7–34,7 „Link is below.“

**Szenenliste (0.3: 2.72, 3.88, 7.20, 10.84, 13.36, 15.08, 17.56, 23.76, 26.32, 29.32, 31.52):** 0–2.72 Hook-Clip (Mann schläft und wacht unter mintgrüner Decke auf, grüne Wand, Regal-Kopfteil mit Kerze und Duftlampe). Ab 2.72 identisch mit 178749251 (Bild-Body deckungsgleich, Frame-Differenz geprüft).

**Personen / Sprecher:** wie 178749251. Im Hook der Creator (ca. 35–45, echt). Hook-Stimme vermutlich weiblich, Body männlich (Off, nicht lippensynchron; KI oder Mensch nicht verifiziert).

**Setting:** wie 178749251.

**Avatar / Angle:** Avatar mit regionaler Zuspitzung: Käufer in Schottland bzw. im kalten Norden. Angle: **B**, dazu F-Einwand, A/C, F-Angebot.

**Haupt-Emotion:** Skepsis und Kälte-Sorge, dann Beruhigung.

**Tempo / Untertitel / Audio:** 11 Schnitte → **3,17 pro 10 s** (Feinwert 3,75). Untertitel ja. Off-Stimmen, vermutlich Musikbett.

**Zahlen und Behauptungen (wörtlich):** „Scottish winter“; „3am with the heating on“; „Dry again in two hours.“; „90 night sleep trial“; „two free matching pillowcases“; Reaktionen „19“. Im Anzeigentext: „rated 10.5 tog“.

**Angebot:** wie 178749251 (90 Nächte, 2 Kissenbezüge gratis, ohne £-Wert).

**Varianten:** 178749251 und 178749247 (verifiziert, siehe 178749251).

---

#### Video 178749247 – Warm Enough For A British Winter

**Metadaten**
| Feld | Wert |
|---|---|
| Meta-ID | 1337076731626722 |
| Start / Status | 2026-09-16 / **inaktiv laut get_ad** (end_date 2026-10-07); im früheren Lauf aktiv |
| Tage aktiv | 22 (start_to_end_date); s1: 23 |
| performance_score | **n/a** (null, inaktiv). Im früheren Lauf: 70 (Growing) |
| used_count | 1 |
| Landingpage | https://pleene.com/products/easyrest-duvet |
| CTA | SHOP_NOW („Shop now“) |
| Plattformen | facebook, instagram, audience_network, threads; GB |
| Primärtext / Link-Beschreibung | T29 bzw. „10.5 TOG winter warmth · Washes whole · 90-night trial“ |
| share_url | https://app.gethookd.ai/share/ad/178749247?signature=ead4e820d252fbf4cb5f6f4bdc9ff97c3172308e95f7a04f5dde33677b0f12e5 |
| Ad Library | https://www.facebook.com/ads/library/?id=1337076731626722 |
| Technik | 33,85 s, 720×1280, 25 fps |

**Transkript (GetHooked, vollständig, korrekt)**
- [0.00–1.84] „Is it actually warm enough for winter?“
- [1.84–3.04] „You won't freeze under this.“
- [3.04–4.96] „The Plein EasyRest is made for cold nights.“
- [4.96–7.88] „It's duvet and cover in one, and warmth doesn't come from bulk.“
- [7.88–10.00] „It comes from the air held between the fibers.“
- [10.00–12.32] „The climate fibers keep your body heat in on cold nights,“
- [12.32–13.08] „but they breathe.“
- [13.08–15.32] „So you're warm all night, and you don't wake up sweating“
- [15.32–16.74] „at 3 AM with the heating on.“
- [16.74–19.08] „And when it needs washing, you don't fight with a cover,“
- [19.08–20.62] „because the cover is already sewn in.“
- [20.62–22.96] „The whole Plein duvet goes in the machine in one piece.“
- [22.96–24.92] „And don't worry, because it's not a heavy duvet,“
- [24.92–27.20] „it still fits easily into a normal washing machine.“
- [27.20–28.48] „Dry again in two hours.“
- [28.48–30.72] „The Plein duvet comes with a 90-night sleep trial,“
- [30.72–32.88] „and right now with two free matching pillowcases.“
- [32.88–34.72] „Link is below.“
- Audio: Mittelwert −16,5 dB, Spitze −1,8 dB. Hook-Stimme f0-Median 281 Hz (Frauenbereich, vermutlich weiblich). Body männlich mit 124 Hz, dieselbe VO wie 251 und 254 (Korrelation 0,94–0,95 bei −0,58 s).

**Einblendungen:**
- 0.0–1.88 Kommentar-Karte (diesmal mittig unten): „Susan Hargreaves [Verifiziert-Haken] Is it actually warm enough for winter??“ · „Like · Reply · 1h“ · Reaktionen „22“.
- Danach dieselben Untertitel wie 178749251, um ca. −0,58 s verschoben (geprüft im 1-s-Raster): „You won't freeze under this“ (2,0–3,0) … „It's duvet and cover in one“ (5,0–6,0) … „Link is below“ (33,0).

**Hook (0–3 s):** gesprochen „Is it actually warm enough for winter?“, ab 1,84 s „You won't freeze under this.“ Eingeblendet: Kommentar von Susan Hargreaves, ab ca. 1,9 s „You won't freeze under this“. Bild: Der Mann liegt von oben gefilmt unter einer **grauen** Decke (Regal-Kopfteil) und lächelt zufrieden mit der Hand auf der Brust.

**Aufbau:** wie 178749251, nur um ca. −0,58 s verschoben: Hook 0–1,9; Problem 0–1,9 (Frage statt Behauptung, weicherer Einwand); Verstärkung ca. 13,1–16,7; Mechanismus 1,9–16,7; Lösung/Demo 16,7–28,5; Beweis **fehlt im Video**; Angebot 28,5–32,9; CTA 32,9–33,9 „Link is below.“

**Szenenliste (0.3: 1.88, 3.08, 6.40, 10.04, 12.56, 14.24, 16.72, 22.96, 25.52, 28.52, 30.72; fein zusätzlich 7.88, 27.76):** 0–1.88 Hook-Clip (Mann unter grauer Decke, Draufsicht). Ab 1.88 dieselbe Szenenfolge wie 178749251. Die Bilddifferenz bleibt wegen des halben Frame-Versatzes (−0,58 s = 14,5 Frames) moderat; die Szeneninhalte an allen Schnitten wurden geprüft und sind gleich.

**Personen / Sprecher:** wie 178749251. Hook-Clip: der Creator (echt). Hook-Stimme vermutlich weiblich, Body männlich (Off; KI oder Mensch nicht verifiziert).

**Setting:** wie 178749251.

**Avatar / Angle:** Avatar sind vorsichtige Interessenten mit offener Frage („Is it actually warm enough …?“). Angle: **B**, dazu F-Einwand, A/C, F-Angebot.

**Haupt-Emotion:** Zweifel bzw. Neugier, dann Beruhigung und Gemütlichkeit.

**Tempo / Untertitel / Audio:** 11 Schnitte → **3,25 pro 10 s** (Feinwert 3,84). Untertitel ja. Off-Stimmen, vermutlich Musikbett.

**Zahlen und Behauptungen (wörtlich):** „3 AM with the heating on“; „Dry again in two hours.“; „90-night sleep trial“; „two free matching pillowcases“; Reaktionen „22“. Im Anzeigentext: „rated 10.5 tog“.

**Angebot:** wie 178749251.

**Varianten:** 178749251 und 178749254 (verifiziert).

---

##### Hygiene-Zitate Batch 2

Gesucht wurde nach Milben, Bakterien, Schweiß, Waschen, Trocknen und Temperatur in Transkripten (T) und Einblendungen (E). Ergebnis vorab: **Milben und Bakterien kommen in keiner der 7 Ads vor**, weder gesprochen noch eingeblendet. „Hypoallergenic“ steht nur im Anzeigentext von 151025063.

| Ad | Sek. | Quelle | Zitat (wörtlich) | Thema |
|---|---|---|---|---|
| 145443318 | 14.96–17.82 | T | „Just put it in the washing machine and then in the tumble dryer.“ | Waschen/Trocknen |
| 145443318 | 14.0–16.5 | E | „Just put it in the washing machine“ | Waschen |
| 145443318 | 17.0–22.0 | E | „and then in the tumble dryer“ | Trocknen |
| 145443318 | 21.76–27.5 | T | „And the best thing is, the breathable fibres adapt to your body. Nice and warm in the winter, comfortable and cool in the summer.“ | Temperatur |
| 145443318 | 23.5–25.0 | E | „the breathable fibres adapt to your body“ | Temperatur |
| 145443318 | 25.5–26.5 | E | „Nice and warm in the winter,“ | Temperatur |
| 145443318 | 27.0–27.5 | E | „Comfortable and cool in the summer“ | Temperatur |
| 145443318 | 28.0–30.0 | T/E | „I swear to you, my bed always feels fresh“ | Frische |
| 151025063 | 8.32–11.44 | T | „just put it in the washing machine and then in the tumble dryer.“ | Waschen/Trocknen |
| 151025063 | 8.5–9.5 | E | „Just put it in the washing machine“ | Waschen |
| 151025063 | 10.0–10.5 | E | „and then in the tumble dryer.“ | Trocknen |
| 151025063 | 11.44–17.76 | T | „the breathable fibres adapt to your temperature. Nice and warm in winter, and comfortable and cool in summer.“ | Temperatur |
| 151025063 | 12.0–13.5 | E | „the breathable fibres adapt to your temperature“ | Temperatur |
| 151025063 | 14.0–15.5 | E | „Nice and warm in winter and comfortable and cool in summer“ | Temperatur |
| 151025063 | 14.64–17.76 / 16.0–17.5 | T/E | „I swear to you, my bed always feels fresh“ | Frische |
| 168246678 | 3.7–9.87 | E | „1. Does the WHOLE thing fit a normal washing machine?“ | ganze Decke waschen |
| 168246678 | ca. 6.5–9.87 | E | „Ours does. [Emoji: Häkchen]“ | Waschen |
| 168246678 | 9.87–16.1 | E | „2. Is it dry in 2 hours without a tumble dryer?“ | Trocknen |
| 168246678 | ca. 12.5–16.1 | E | „2 hours. No dryer. [Emoji: Häkchen]“ | Trocknen |
| 168246686 | 3.7–9.87 | E | „1. Does the WHOLE thing fit a normal washing machine?“ | ganze Decke waschen |
| 168246686 | ca. 6.5–9.87 | E | „Ours does. [Emoji: Häkchen]“ | Waschen |
| 168246686 | 9.87–16.1 | E | „2. Is it dry in 2 hours without a tumble dryer?“ | Trocknen |
| 168246686 | ca. 12.5–16.1 | E | „2 hours. No dryer. [Emoji: Häkchen]“ | Trocknen |
| 178749251 | 0.00–2.48 | T | „Looks lovely, but you'll freeze under that in winter.“ | Temperatur (Kälte) |
| 178749251 | 0.0–2.48 | E | „Looks lovely but you'll freeze under that in winter[Emoji: frierendes Gesicht]“ (Kommentar Janet Whitfield) | Temperatur |
| 178749251 | 2.48–3.64 / 2.5–3.5 | T/E | „You won't freeze under this.“ | Temperatur |
| 178749251 | 3.64–5.56 / 4.0–5.5 | T/E | „The Plein EasyRest is made for cold nights.“ (E: „The Pleene EasyRest is made for cold nights“) | Temperatur |
| 178749251 | 5.56–10.60 | T | „and warmth doesn't come from bulk. It comes from the air held between the fibers.“ | Temperatur |
| 178749251 | 7.0–10.5 | E | „And warmth doesn't come from bulk“ / „It comes from the air held between the fibres“ | Temperatur |
| 178749251 | 10.60–13.68 / 11.0–13.5 | T/E | „The climate fibers keep your body heat in on cold nights, but they breathe.“ | Temperatur |
| 178749251 | 13.68–17.12 | T | „So you're warm all night, and you don't wake up sweating at 3 AM with the heating on.“ | Schweiß/Temperatur |
| 178749251 | 15.0–17.0 | E | „and you don't wake up sweating at 3am with the heating on“ | Schweiß/Temperatur |
| 178749251 | 17.12–21.12 | T | „And when it needs washing, you don't fight with a cover, because the cover is already sewn in.“ | Waschen |
| 178749251 | 17.5–21.0 | E | „And when it needs washing,“ / „you don't fight with a cover,“ / „because the cover is already sewn in“ | Waschen |
| 178749251 | 21.12–23.54 / 21.5–23.0 | T/E | „The whole Plein duvet goes in the machine in one piece.“ (E: „The whole Pleene duvet goes in the machine in one piece“) | ganze Decke waschen |
| 178749251 | 23.54–27.80 | T | „And don't worry, because it's not a heavy duvet, it still fits easily into a normal washing machine.“ | Waschen |
| 178749251 | 23.5–27.5 | E | „And don't worry: because it's not a heavy duvet,“ / „it still fits easily into a normal washing machine“ | Waschen |
| 178749251 | 27.80–29.08 / 28.0–29.0 | T/E | „Dry again in two hours.“ | Trocknen |
| 178749254 | 0.00–2.56 | T | „No way that keeps you warm in a Scottish winter.“ | Temperatur (Kälte) |
| 178749254 | 0.0–2.72 | E | „No way that keeps you warm in a Scottish winter[Emoji]“ (Kommentar Moira McAllister) | Temperatur |
| 178749254 | 2.56–6.80 | T | „You won't freeze under this. The Plein EasyRest is made for cold nights.“ | Temperatur |
| 178749254 | 6.80–10.64 | T | „and warmth doesn't come from bulk, it comes from the air held between the fibres.“ | Temperatur |
| 178749254 | 10.64–13.76 | T | „The climate fibres keep your body heat in on cold nights, but they breathe.“ | Temperatur |
| 178749254 | 13.76–17.36 | T | „So you're warm all night, and you don't wake up sweating at 3am with the heating on.“ | Schweiß/Temperatur |
| 178749254 | 17.36–21.20 | T | „And when it needs washing, you don't fight with a cover, because the cover is already sewn in.“ | Waschen |
| 178749254 | 21.20–27.92 | T | „The whole Plein duvet goes in the machine in one piece. And don't worry, because it's not a heavy duvet, it still fits easily into a normal washing machine.“ | Waschen |
| 178749254 | 27.92–29.4 | T | „Dry again in two hours.“ | Trocknen |
| 178749254 | ca. 3–29 | E | dieselben Untertitel wie 178749251, ca. +0,24 s (z. B. 16–17 „and you don't wake up sweating at 3am with the heating on“, 29 „Dry again in two hours“) | alle oben |
| 178749247 | 0.00–1.84 | T | „Is it actually warm enough for winter?“ | Temperatur |
| 178749247 | 0.0–1.88 | E | „Is it actually warm enough for winter??“ (Kommentar Susan Hargreaves) | Temperatur |
| 178749247 | 1.84–4.96 | T | „You won't freeze under this. The Plein EasyRest is made for cold nights.“ | Temperatur |
| 178749247 | 4.96–10.00 | T | „It's duvet and cover in one, and warmth doesn't come from bulk. It comes from the air held between the fibers.“ | Temperatur |
| 178749247 | 10.00–13.08 | T | „The climate fibers keep your body heat in on cold nights, but they breathe.“ | Temperatur |
| 178749247 | 13.08–16.74 | T | „So you're warm all night, and you don't wake up sweating at 3 AM with the heating on.“ | Schweiß/Temperatur |
| 178749247 | 16.74–20.62 | T | „And when it needs washing, you don't fight with a cover, because the cover is already sewn in.“ | Waschen |
| 178749247 | 20.62–27.20 | T | „The whole Plein duvet goes in the machine in one piece. And don't worry, because it's not a heavy duvet, it still fits easily into a normal washing machine.“ | Waschen |
| 178749247 | 27.20–28.48 | T | „Dry again in two hours.“ | Trocknen |
| 178749247 | ca. 2–28 | E | dieselben Untertitel wie 178749251, ca. −0,58 s (z. B. 15–16 „… sweating at 3am with the heating on“, 28 „Dry again in two hours“) | alle oben |

Nur im Anzeigentext (nicht im Video), zur Vollständigkeit:
- 145443318: „wash it whole, dry in 2 hours“
- 151025063: „Wash it, dry it, and lay it back on“, „Pleasantly cool in summer, cosily warm in winter“, „Hypoallergenic and kind to sensitive skin“, „Enjoy a bed that always feels fresh.“
- 168246678/686: „Does the WHOLE thing fit a normal washing machine?“, „Is it dry in 2 hours without a tumble dryer?“
- 178749251/254/247: „rated 10.5 tog, a proper autumn and winter weight, and the whole thing still goes in your washing machine“, Link-Beschreibung „10.5 TOG winter warmth · Washes whole · 90-night trial“

---

##### Kurz-Tabelle Batch 2

| ID | Länge | Hook (0–3 s) | Angle | Avatar | Sprecher-Typ | Schnitte/10 s (0.3) | Emotion |
|---|---|---|---|---|---|---|---|
| 145443318 | 49,5 s | „I bloody hate changing the bed“ (gesprochen und Untertitel) | C (+F-Social-Proof, B, F-Knappheit, F-Angebot) | Erwachsene 25–55 (auch Männer), die das Beziehen hassen | echter UGC-Creator, Mann ca. 30–40, O-Ton | 1,41 | Frust → Erleichterung |
| 151025063 | 29,4 s | „I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“ | E (+C, B, F-Angebot) | Menschen mit Schulter-/Rückenschmerz beim Beziehen | Off-Stimme weiblich (f0 193 Hz); Footage gemischt: echt, Stock-3D und KI-Mann | 5,78 | Schmerz/Frust → Erleichterung |
| 168246678 | 27,1 s | Text: „Before you buy a coverless duvet check 3 things“ (ohne Sprache) | F-Einwand/Kaufhilfe + A (+F-Angebot) | skeptische Vergleichskäufer | kein Sprecher, nur Musik; Bild vermutlich KI | 1,84 | Neugier/Skepsis → Sicherheit |
| 168246686 | 27,1 s | Text: „Seen coverless duvets all over your feed?“ → „Check these 3 things before you buy.“ | F-Einwand/Kaufhilfe + A (+Trend-Anklang) | Trend-aware Vergleichskäufer | kein Sprecher, nur Musik; Bild vermutlich KI | 1,84 | Neugier/Wiedererkennung → Sicherheit |
| 178749251 | 34,4 s | gesprochen „Looks lovely, but you'll freeze under that in winter.“ + Kommentar-Karte | B (+F-Einwand, A/C, F-Angebot) | frierende, heizbewusste Briten | Off-VO männlich (124 Hz) + andere Hook-Stimme; echte Personen im Bild | 3,19 | Zweifel/Kälte → Beruhigung |
| 178749254 | 34,7 s | gesprochen „No way that keeps you warm in a Scottish winter.“ + Kommentar-Karte | B (+F-Einwand, A/C, F-Angebot; regional) | Schottland/kalter Norden | wie 251; Hook-Stimme vermutlich weiblich (222 Hz) | 3,17 | Skepsis/Kälte → Beruhigung |
| 178749247 | 33,9 s | gesprochen „Is it actually warm enough for winter?“ + Kommentar-Karte | B (+F-Einwand, A/C, F-Angebot) | vorsichtige Frager | wie 251; Hook-Stimme vermutlich weiblich (281 Hz) | 3,25 | Zweifel/Neugier → Beruhigung |

**Kurzbefunde für die Synthese**
- Drei der sieben Ads sind reine **Hook-Tests auf identischem Body** (178749251/254/247). Zwei weitere bilden ein **Text-Hook-A/B** (168246678 mit Score 100 gegenüber 168246686 mit Score 86, bei gleicher Laufzeit). 145443318 ist ein Hook-Swap von 145443331/163921089.
- Hygiene wird in Batch 2 **nur über Waschbarkeit, Trocknung und Frische** gespielt. Milben, Bakterien und Schweiß als Ekel-Trigger fehlen; Schweiß kommt nur als Temperatur-Argument vor („you don't wake up sweating at 3 AM“).
- Das Angebot ist durchgehend „2 free pillow cases“ + 90 Nächte. Ein £-Wert wird nur in 145443318 (£39.99 durchgestrichen), 151025063 („worth £39.99“) und 1682466xx („Value £39.99“) genannt, nicht in den Winter-Ads. Echte Knappheit („This week only“) zeigt nur 145443318.
- Die Winter-Familie (178749xxx) ist laut get_ad seit 2026-10-07 inaktiv, nach 22 Tagen und mit früheren Scores 81/70/70.

**Prüfliste (je Ad)**
| ID | Transkript bzw. Vermerk | Hook | Aufbau | Szenen | Personen | Setting | Avatar/Angle | Emotion | Tempo/UT/Audio | Zahlen | Angebot | Varianten | Metadaten |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 145443318 | ja (GetHooked walisisch, Fehler dokumentiert; ElevenLabs technisch nicht möglich, begründet; korrigiert per lokalem Whisper + Untertiteln) | ja | ja | ja (alle Schnitte) | ja | ja | ja | ja | ja | ja | ja | ja (verifiziert) | ja |
| 151025063 | ja | ja | ja | ja (alle 22 Schnitte) | ja | ja | ja | ja | ja | ja | ja | ja | ja |
| 168246678 | `no_speech`, per Audio-Check bestätigt: nur Musik | ja | ja | ja (alle Schnitte) | ja | ja | ja | ja | ja | ja | ja | ja (verifiziert) | ja |
| 168246686 | `no_speech`, Tonspur PCM-identisch mit 168246678: nur Musik | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja (verifiziert) | ja |
| 178749251 | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja (verifiziert) | ja (Score n/a, inaktiv, alter Wert genannt) |
| 178749254 | ja | ja | ja | ja (Hook + Verweis, Body verifiziert identisch) | ja | ja | ja | ja | ja | ja | ja | ja | ja (Score n/a, alter Wert genannt) |
| 178749247 | ja | ja | ja | ja (Hook + Verweis, Szenen an allen Schnitten geprüft) | ja | ja | ja | ja | ja | ja | ja | ja | ja (Score n/a, alter Wert genannt) |

**Offene bzw. nicht verifizierte Punkte**
- ElevenLabs-Neutranskription von 145443318 war nicht möglich: Die Audio-Upload-Tools fehlen in dieser Session, und der Video-Knoten lässt sich nicht an Speech-to-Text anschließen. Ersatz: lokales Whisper plus Untertitel-Abgleich.
- Die Unterscheidung KI-Stimme gegenüber menschlicher Stimme (alle Off-Stimmen) ist nicht verifiziert.
- Ob Musik unter dem O-Ton von 145443318 liegt, ist nicht verifiziert.
- Das Emoji im Moira-Kommentar (178749254) ist nicht eindeutig lesbar.
- Echtheit der eingeblendeten Kommentare ist nicht verifiziert.
- Inhaltliche Gleichheit weiterer Ads gleicher Primärtexte (193234219/221, 185228764, 200490712, 168246672, 179476350, 180646058) ist nicht geprüft.


### S2 – Creative-Tiefenanalyse, Video-Batch 3 (Agent 2)

Stand: 2026-10-08 · Marke Pleene (UK) · Produkt EasyRest · 7 Video-Ads: 182988073, 185228767, 185228755, 184134597, 193234275, 193234221, 193234279. Keine dieser Ads gehört zur Top-20-Liste. Deshalb gilt für alle die Standardanalyse 3a, die Keyframe-Tiefenanalyse 3b entfällt. Die drei inhaltlich neuen Videos (182988073, 185228767, 184134597) habe ich trotzdem an jedem erkannten Schnitt angesehen.

**Methodik und Quellen**
- Metadaten stammen aus GetHooked `get_ad` (abgerufen am 2026-10-08). Wo sie von `agent1_enriched.json` abweichen, ist das unten vermerkt. Transkripte stammen aus `get_transcription_status`. Alle 7 Ads waren „complete“: 182988073 hat „no_speech“, die anderen sechs „completed“. `transcribe_ads` war nicht nötig.
- Videos liegen unter `wf/vid/<id>.mp4`. ffprobe: alle 720×1280 (9:16), H.264 + AAC Stereo 44,1 kHz. Die Bildrate liegt bei 30 fps (182988073, 185228767, 185228755, 184134597) bzw. 25 fps (193234275, 193234221, 193234279).
- **MD5 aller Videos** (gegen alle 21 Dateien in `wf/vid/` verglichen):
  - 193234275 = 193234279 = **133366534** (Batch 1, Top-20, Score 100), md5 `9877275e5c9724bee5a00be00da2fb3f`
  - 193234221 = **145443331** = **163921089** (Batch 1, Score 100), md5 `a22e6497e1155287fea63fd80477ee89`
  - 185228755 = **139561410** (Batch 1, Score 100), md5 `b98b8b49e94b01d46d71c5e548dfca4b`
  - Eigenständig sind nur 182988073 (`77017b3e…`), 185228767 (`a3d7617b…`) und 184134597 (`f5e6f83f…`).
- Schnitte habe ich mit `ffmpeg select='gt(scene,0.3)',showinfo` gezählt, zusätzlich mit Schwelle 0,15 und bei 184134597 mit `signalstats` (Ein-Frame-Schwarzblitze) und Szenen-Scores (Überblendungen). Rohdaten: `wf/s2b3_meta/<id>.scenes03.txt`, `.scenes015.txt`.
- Frames liegen unter `wf/frames/<id>/`: bei 0/1/2/3 s, danach alle 5 s (bei 16–47-s-Videos dichter, 1–2,5 s), dazu ein Frame je erkanntem Schnitt (+0,1–0,2 s). Alle wurden als Kontaktbögen (`wf/s2b3_sheets/`) mit dem Read-Tool angesehen. Insgesamt sind es 49 Frames (182988073), 75 (184134597), 20 (185228767), 14 (185228755), 23 (193234275), 23 (193234279; per md5 bitgleich mit 193234275) und 14 (193234221).
- Audio-Checks:
  - `volumedetect` und `silencedetect` (−40 dB / 0,4 s), Rohdaten in `wf/s2b3_meta/<id>.volume.txt` / `.silence.txt`.
  - Spektrogramme liegen in `wf/s2b3_audio/*_spec*.png`.
  - Kreuzkorrelation der Tonspuren (`wf/s2b3_scripts/xcorr.py`).
  - Grundfrequenz-Schätzung (f0 per Autokorrelation; nur ein Indiz, **nicht verifiziert**).
  - Als **lokale Whisper-Gegenprobe** lief faster-whisper `small.en` offline auf 182988073, 185228767, 185228755 und 184134597 (`wf/s2b3_meta/asr_small_en.txt`).
- **ElevenLabs wurde nicht eingesetzt**, weil kein Transkript dieses Batches falsch erkannte Sprache enthält. Die zwei Platzhalter-Transkripte („the next, video!!“) und der „no_speech“-Fall sind per Audio-Check eindeutig reine Musik.
- Die Markenschreibweise in den Whisper-Transkripten schwankt („Pleen“, „plean“). Laut Untertiteln heißt es „Pleene“. Die Transkripte sind trotzdem **wörtlich** wiedergegeben.
- GetHooked meldet für GB **keine Reichweite und keinen Spend**. `ai_badge` ist bei allen 7 Ads `null` (das ist laut GetHooked ausdrücklich kein „human-made“), `script_anatomy` lautet überall „not_analysed“, `creative_insights` ist `null`.
- Plattformen bei allen 7: facebook, instagram, audience_network, threads. Sprache en. Länder: [GB], außer bei 193234275 und 193234279. Dort liefert `get_ad` eine **leere Länderliste** (n/a).

**Abweichungen zu `agent1_enriched.json` (Live-Wert `get_ad` vom 08.10. hat Vorrang)**
| Ad | Feld | enriched | get_ad 08.10. |
|---|---|---|---|
| 182988073 | performance_score | 72 („Growing“) | **61** („Growing“) |
| 193234279 | performance_score / used_count | 44 / 2 | **41 / 1** |
| 193234221 | Status / Score / Tage | active / 52 / 8 | **inactive**, end_date 2026-10-07, **Score null (n/a)**, 7 Tage (start_to_end_date) |
| 193234275, 193234279 | Länder | – | `countries: []` (n/a) |

**Wichtigste Querbefunde des Batches**
1. **Nur 3 der 7 IDs sind neue Creatives.** 4 IDs sind byte-identische Kopien von Top-Videos aus Batch 1. Pleene lässt dieselbe Datei mit neuer Headline, neuem Primärtext oder neuer Landingpage (Advertorial `/pages/tb-6`) erneut laufen:
   - **193234275** ist das Hygiene-Video 133366534, jetzt mit der „Octopus“-Copy (Angle C).
   - **193234279** ist dasselbe Video mit Original-Copy, aber auf tb-6.
   - **193234221** ist das Creator-Video 145443331, jetzt auf tb-6. Es ist laut GetHooked seit 2026-10-07 inaktiv.
   - **185228755** ist die Mint-Green-Template-Ad 139561410.
2. **185228767 ist ein Neuschnitt des KI-Templates.** Musik und Eröffnung (Türrahmen-Fahrt, Coastal Blue) sind identisch mit 139561491, aber der Hook ist neu: B/Tog („One duvet that handles a British winter / 10.5 TOG · warm, never sweaty“). **Headline („Be honest. When did you last wash it?“) und Primärtext („Hearth Red … almost gone“) passen nicht zum Video.**
3. **184134597 gehört zu einem Hook-Test.** Drei Videos starteten am 2026-09-25 mit identischem Körper-Skript und drei verschiedenen gesprochenen Hooks: 184134597 „I bloody hate changing the bed“, 184134616 „demented octopus“ und 184134607 „work of the devil“ (laut GetHooked-Transkripten). Neu in diesem Skript sind die Spezifikationen „normal 7kg washing machine“, „10.5 tog“ und das Angebot „30% off“.
4. **182988073 ist ein stummer Farb-Karussell-Clip** (7 Farben, nur Musik). Er endet auf einer Endkarte „7 colours · 2× Pleene™ Pillow Cases FREE · Value £39.99 · 90-Night Trial Sleep Guarantee“.
5. **Hygiene (Angle A) ist nur in 193234275 und 193234279 Haupt-Angle**, also in der Kopie von 133366534: Milben, Schweiß, Hautpartikel, Mikroskop-Einblendung. In allen anderen Ads tauchen Waschen und Trocknen nur als Produkteigenschaft auf („Wash the whole thing“, „dry in 2 hours“, „7kg washing machine“, „fully washable“). Temperatur taucht als Tog- bzw. Winter-Argument auf (185228767, 184134597).
6. Das Angebot wird uneinheitlich kommuniziert:
   - Template- und Creator-Videos: „2 FREE Pillow Cases … this week only“ mit **£39.99 durchgestrichen**.
   - 182988073: „Value £39.99“, nicht durchgestrichen.
   - 184134597 und die Copy von 193234275: „**30% off** + 2 free pillow cases“. Das Video von 193234275 nennt die 30 % aber gar nicht.

---

#### Video 182988073 – No More Fighting With Duvet Covers

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 182988073 |
| Meta-ID | 1307634398016532 |
| Ad Library | https://www.facebook.com/ads/library/?id=1307634398016532 |
| share_url | https://app.gethookd.ai/share/ad/182988073?signature=18244261546a933ac17b6d832e4abb5f9491a76500ae006902ed5c113947df05 |
| Start / Tage aktiv | 2026-09-21 / 18 (start_to_today, Status active) |
| performance_score / used_count | 61 („Growing“; enriched: 72) / 1 |
| CTA | SEE_DETAILS – „See details“ |
| Landingpage | https://pleene.com/products/easyrest |
| Link-Beschreibung | „⭐️⭐️⭐️⭐️⭐️ – Over 10,000 Happy Customers“ |
| Länge / Format | 25,1 s · 720×1280 · 30 fps |
| Schnitte | bei 0,3: 7 (3,53 / 9,20 / 11,93 / 14,67 / 17,40 / 20,10 / 22,23 s). Bei 0,15 zusätzlich 6,37 s (Farbwechsel Beige → Blau). **8 Schnitte = 3,2 pro 10 s** (0–10 s: 3 · 10–20 s: 3 · 20–25 s: 2) |

**Primärtext (wörtlich):** „Duvet + Cover in One 🌙 / The Pleene EasyRest™ makes changing the bed finally simple. Wash it, dry it, and lay it back on — that's it. / ✓ No more wrestling with a separate duvet cover / ✓ Pleasantly cool in summer, cosily warm in winter / ✓ Hypoallergenic and kind to sensitive skin / Get 2 free Pleene™ Pillow Cases today (worth £39.99). / 90 nights to try it risk-free. / Enjoy a bed that always feels fresh.“

**Transkript:** GetHooked meldet `transcript_status: no_speech`. Ein Transkript gibt es nicht. **Audio-Check:**
- Pegel: mean −16,4 dB, max −0,7 dB. Keine Stille ≥ 0,4 s bei −40 dB.
- Spektrogramm (`wf/s2b3_audio/182988073_spec.png`): stehende Akkordtöne unter ca. 1,3 kHz mit regelmäßigen Perkussions-Transienten, keine Sprach-Formantverläufe.
- Die lokale Whisper-Gegenprobe liefert **0 Segmente**.
- Die Musik ist **nicht** die Template-Musik der 1395614xx-Ads (Korrelation 0,06).

**Ergebnis: eindeutig nur Musik, kein Voiceover.**

**Hook (0–3 s)**
- Gesprochen: keiner (nur Musik).
- Eingeblendet: „Best thing I got for years.“ (graue, halbtransparente Box, 0–3,5 s). Ab ca. 2 s steht darunter „NEW: Mint Green“.
- Bild: Draufsicht auf ein leeres Bett (weißes Spannlaken, helles Holzbett, Pflanze, Nachttischlampe, Sonnenstreifen). Ab 1 s fliegt eine mintgrüne Steppdecke von links ins Bild und landet samt Kissen fertig gemacht auf dem Bett.
- Hook-Typ: Testimonial-Satz plus Neuheit/Farbe als „Satisfying Reveal“.

**Szenenliste (alle 8 Schnitte angesehen, plus 1-Sekunden-Frames)**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,00–3,53 | Leeres Bett → mintgrüne Decke + Kissen landen | „Best thing I got for years.“ · „NEW: Mint Green“ |
| 3,53–6,37 | Leeres Bett → Decke in Cream Beige wird von links geworfen | „No cover. No bed linen.“ · „Cream Beige“ |
| 6,37–9,20 | Leeres Bett → Coastal Blue | „Never change bed linen again.“ · „Coastal Blue“ |
| 9,20–11,93 | Leeres Bett → Hearth Red (bei 10,5 s schweben die Kissen gleichzeitig mit der Decke ins Bild) | „Hearth Red“ |
| 11,93–14,67 | Leeres Bett → Orange | „Orange“ |
| 14,67–17,40 | Leeres Bett → Moonstone Grey | „Moonstone Grey“ |
| 17,40–20,10 | Leeres Bett → Midnight Black | „Duvet + cover in one, fully washable.“ · „Midnight Black“ |
| 20,10–22,23 | Nahaufnahme: Hand drückt schwarze Steppdecke (Textur, Seitenlicht) | „Which colour is yours?“ |
| 22,23–25,12 | Endkarte auf grauem Verlauf | „Pleene“ / „7 colours“ / „2× Pleene™ Pillow Cases FREE“ / „Value £39.99“ / „90-Night Trial Sleep Guarantee“ |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–3,5 | „Best thing I got for years.“ + Reveal Mint Green („NEW“) |
| Problem | – | **fehlt** |
| Verstärkung | – | **fehlt** |
| Mechanismus | 3,5–20,1 | nur als Text: „No cover. No bed linen.“, „Never change bed linen again.“, „Duvet + cover in one, fully washable.“ Visuell: Decke drauf werfen = Bett gemacht |
| Lösung | 0–20,1 | Produkt durchgehend, in 7 Farben |
| Beweis | 0–3,5 | nur das unbelegte Zitat „Best thing I got for years.“, sonst **fehlt** |
| Angebot | 22,2–25,1 | Endkarte: 2 Gratis-Kissenbezüge „Value £39.99“ + „90-Night Trial Sleep Guarantee“ |
| CTA | 20,1–22,2 | weich: „Which colour is yours?“. Ein expliziter Handlungsaufruf **fehlt**. Button „See details“ |

**Wer ist zu sehen / wer spricht:** keine Person, nur nackte Arme bzw. Hände, die die Decke von links ins Bild werfen, gelegentlich Füße am Bildrand. Niemand spricht.
**Einschätzung: KI-generiert bzw. synthetisch (nicht verifiziert).** Gründe:
- Szene, Licht und Schatten sind in allen 7 Farbdurchgängen identisch.
- Bei 10,5 s schweben die Kissen gleichzeitig mit der Decke ins Bild, ohne dass jemand sie wirft.
- Der Look ist glatt und gerendert.
- Rechts unten sieht man nur Fußspitzen, nie eine ganze Person.

**Setting:** helles, minimalistisches Schlafzimmer in Draufsicht (Holzbett, Teppich, Monstera, Lampe).
**Avatar / Angle:** design- und farborientierte Käufer, die den Bettwäsche-Wechsel loswerden wollen. Die Kombination „NEW“ + Farbe deutet auch auf Bestandskunden bzw. Retargeting hin (nicht verifiziert). **Angle C** (primär: „No cover. No bed linen.“, „Never change bed linen again.“) + **F-Farbe/Auswahl** („7 colours“, „NEW: Mint Green“, „Which colour is yours?“) + F-Angebot. A nur am Rand („fully washable“).
**Haupt-Emotion:** Neugier bzw. Begehren (befriedigender Reveal-Loop), Leichtigkeit.
**Schnitttempo / Untertitel / Ton:**
- 3,2 Schnitte pro 10 s, rhythmisch: alle ca. 2,7 s eine neue Farbe.
- Keine Untertitel (kein Ton zu untertiteln). Texteinblendungen in grauer halbtransparenter Box (Sans), darunter der Farbname in weißer Schrift.
- Ton: nur Musik.

**Konkrete Zahlen und Behauptungen (wörtlich):**
- Im Video: „Best thing I got for years.“ · „No cover. No bed linen.“ · „Never change bed linen again.“ · „Duvet + cover in one, fully washable.“ · „7 colours“ · „2× Pleene™ Pillow Cases FREE“ · „Value £39.99“ · „90-Night Trial Sleep Guarantee“.
- Farbnamen: „NEW: Mint Green“, „Cream Beige“, „Coastal Blue“, „Hearth Red“, „Orange“, „Moonstone Grey“, „Midnight Black“.
- Primärtext zusätzlich: „Pleasantly cool in summer, cosily warm in winter“, „Hypoallergenic and kind to sensitive skin“, „worth £39.99“, „90 nights to try it risk-free“.
- Keine Tog-Angabe, keine Trocknungszeit, kein Preis.

**Angebotspräsentation:** nur auf der Endkarte. Gratis-Kissenbezüge mit Wert „£39.99“ (nicht durchgestrichen) und 90-Nächte-Garantie. Keine Frist, keine Restmenge, kein Rabatt.
**Varianten-Hinweis:**
- Copy-Familie: Headline und Primärtext sind identisch mit 136389861, 133366534, 151025063, 193234279, 200490716 und mehreren Bild-Ads.
- Wahrscheinliche Kreativ-Geschwister: **182988108** und **182988111**. Beide haben denselben Starttag (2026-09-21), je 25 s und laut GetHooked „no_speech“. Visuell nicht verifiziert.

---

#### Video 185228767 – Be honest. When did you last wash it?

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 185228767 |
| Meta-ID | 947904747867427 |
| Ad Library | https://www.facebook.com/ads/library/?id=947904747867427 |
| share_url | https://app.gethookd.ai/share/ad/185228767?signature=d4a01baf409b9ddc41f60bfabb36d11b1b0037cf0db9af90a7ff2251278f24be |
| Start / Tage aktiv | 2026-09-27 / 12 (start_to_today, active) |
| performance_score / used_count | 60 („Scaling“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Link-Beschreibung | „⭐️⭐️⭐️⭐️⭐️ – Over 10,000 Happy Customers“ |
| Länge / Format | 15,9 s · 720×1280 · 30 fps |
| Schnitte | bei 0,3: 3 (3,00 / 6,40 / 10,23 s) = **1,9 pro 10 s** (0–10 s: 2 · 10–15,9 s: 1). Bei 0,15 kommt nur 0,77 s hinzu, das ist Kamerafahrt und kein Schnitt |

**Primärtext (wörtlich):** „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if you want the bedroom ready for the colder nights, Hearth Red is the one everyone picks, and it's almost gone. The EasyRest™ is duvet and cover in one: wash it whole, dry in 2 hours.“

**Transkript:** GetHooked meldet „the next, video!!“ (0,00–15,16 s). **Das ist ein Platzhalter bzw. eine Whisper-Halluzination.** Audio-Check:
- Pegel: mean −15,0 dB, max −4,0 dB, keine Stille.
- Spektrogramm (`wf/s2b3_audio/185228767_spec.png`): regelmäßige Perkussions-Transienten und tonale Blöcke unter ca. 1 kHz, keine Formanten.
- Die Tonspur korreliert mit der Template-Musik von 139561428 und 139561491 zu ≈ 1,0 bei Versatz 0, ist also dieselbe Musik.
- Die lokale Whisper-Gegenprobe liefert nur die typische Musik-Halluzination „Thanks for watching guys!“ mit no_speech_prob 0,54.

**Ergebnis: nur Musik, keine Sprache.** Deshalb keine Neutranskription.

**Hook (0–3 s)**
- Gesprochen: keiner.
- Eingeblendet: „One duvet that handles a British winter“ (weiß) und darunter „10.5 TOG · warm, never sweaty“ (orange).
- Bild: Kamerafahrt durch einen Türrahmen in ein dunkles, holzvertäfeltes Schlafzimmer mit Steppdecke in Coastal Blue. Die Bildfolge in 0–3 s ist nahezu identisch mit 139561491 (Graustufen-Bilddifferenz 5–6 von 255, danach 23–55).
- Hook-Typ: Einwandbehandlung (reicht die Wärme im britischen Winter?) plus Spezifikation (Tog).

**Szenenliste (alle 3 Schnitte und 1-Sekunden-Frames angesehen)**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,00–3,00 | Türrahmen-Kamerafahrt, Totale blaues Bett, Messing-Wandleuchte | „One duvet that handles a British winter“ · „10.5 TOG · warm, never sweaty“ |
| 3,00–6,40 | POV-Hand (weißer Strickärmel) hebt die Deckenkante, darunter Spannbettlaken (zeigt: kein separater Bezug) | „Duvet and cover in one. Sewn in“ |
| 6,40–10,23 | Hand drückt bzw. streicht über die Decke, Nahaufnahme Kissen | „Washes whole, fits any / Washing machine, dry in 2 hours“ |
| 10,23–15,86 | Totale mit langsamem Push-in, ab ca. 11 s Kissenbezug-Produktkarte. Bis 15,7 s kein Fade-to-black sichtbar | „2 FREE Matching Pillow Cases / with every DUVET“ · Badge (schwarzer Kreis) „FREE this week only“ · „~~£39.99~~“ (durchgestrichen) |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–3 | Winter- bzw. Tog-Einwand: „One duvet that handles a British winter / 10.5 TOG · warm, never sweaty“ |
| Problem | – | **fehlt** (nur implizit: kalter Winter, Schwitzen) |
| Verstärkung | – | **fehlt** |
| Mechanismus | 3–10,2 | „Duvet and cover in one. Sewn in“, „Washes whole, fits any Washing machine, dry in 2 hours“ |
| Lösung | 0–15,9 | Produkt durchgehend im Bild |
| Beweis | – | **fehlt** |
| Angebot | 10,2–15,9 | „2 FREE Matching Pillow Cases with every DUVET“, „FREE this week only“, Wert £39.99 durchgestrichen |
| CTA | – | im Video **fehlt**. Button „Shop now“ |

**Wer ist zu sehen / wer spricht:** keine Person, nur Hand und Unterarm (weißer Strickärmel). **KI-generiert (Einschätzung).** Gründe: dieselbe synthetische Template-Szene wie 139561428/410/491 (identische Kamerafahrt in 0–3 s) und hochglatter Render-Look. Kein Sprecher, nur Musik.
**Setting:** KI-Luxus-Schlafzimmer (dunkles Holz, Messingleuchten, Hochflor-Teppich).
**Avatar / Angle:** UK-Käufer vor der kalten Jahreszeit, die bezweifeln, dass eine „Ganzjahres“-Decke warm genug ist, oder nachts schwitzen. **Angle B** (primär) + C („Sewn in“) + A sekundär (ganz waschen, 2 h trocken) + F-Angebot.
**Copy-Bruch:** Die Headline ist eine Hygiene-Frage (Angle A), der Primärtext setzt auf Knappheit in Hearth Red (Angle F). Das Video zeigt Coastal Blue mit Tog-Hook (Angle B).
**Haupt-Emotion:** Beruhigung bzw. Sicherheit (Einwand „zu kalt / zu verschwitzt“), danach Dringlichkeit („this week only“).
**Schnitttempo / Untertitel / Ton:** 1,9 Schnitte pro 10 s. Keine Untertitel, nur Texteinblendungen oben (weiße Sans mit Schatten, die Tog-Zeile orange). Ton: nur Musik (Template-Track).

**Konkrete Zahlen und Behauptungen (wörtlich):**
- Im Video: „One duvet that handles a British winter“ · „10.5 TOG · warm, never sweaty“ · „Duvet and cover in one. Sewn in“ · „Washes whole, fits any Washing machine, dry in 2 hours“ · „2 FREE Matching Pillow Cases with every DUVET“ · „FREE this week only“ · „£39.99“ (durchgestrichen).
- Primärtext: „This week only“, „ready for the colder nights“, „Hearth Red is the one everyone picks, and it's almost gone“, „wash it whole, dry in 2 hours“.

**Angebotspräsentation:**
- Endkarte mit Gratis-Kissenbezügen („Matching“), Wert £39.99 durchgestrichen, Wochenfrist.
- **Keine Restmenge im Video**, anders als bei 1395614xx und 185228755. Knappheit steht nur im Primärtext (Hearth Red).

**Varianten-Hinweis:**
- Neuschnitt des KI-Templates **139561428 / 139561410 / 139561491**: gleiche Musik, gleiche Eröffnung wie 139561491 (Coastal Blue). Anders sind die Texte, die Schnittzeiten (3,0 / 6,4 / 10,23 statt 3,0 / 7,0 / 10,8) und das fehlende Fade-to-black.
- Headline-Geschwister (nicht visuell verifiziert):
  - **185228772**, **193234218** und **177443532**: je 29 s, GetHooked-Transkript „Thanks for watching!“, vermutlich also ebenfalls nur Musik.
  - **193234216**: 16 s, „the next, video!!“.
  - Bild-Ad **182988119**.

---

#### Video 185228755 – Mint Green is almost gone.

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 185228755 |
| Meta-ID | 1858016975363264 |
| Ad Library | https://www.facebook.com/ads/library/?id=1858016975363264 |
| share_url | https://app.gethookd.ai/share/ad/185228755?signature=25ebc63a662bfe1309283139b99531554229712ec743d75253367e8f2956578d |
| Start / Tage aktiv | 2026-09-27 / 12 (start_to_today, active) |
| performance_score / used_count | 60 („Scaling“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Link-Beschreibung | „⭐️⭐️⭐️⭐️⭐️ – Over 10,000 Happy Customers“ |
| Länge / Format | 16,4 s · 720×1280 · 30 fps |
| Schnitte | bei 0,3: 2 (3,0 / 10,7 s). Bei 0,15 zusätzlich 7,0 s (und 0,67 s Kamerafahrt). **3 harte Schnitte = 1,8 pro 10 s** (0–10 s: 2 · 10–16,4 s: 1) |

**Identität:** Die MP4 ist **byte-identisch mit 139561410** (Batch 1, Start 2026-08-07, Score 100), md5 `b98b8b49e94b01d46d71c5e548dfca4b`. Headline, Primärtext, CTA und Landingpage sind ebenfalls identisch. Es unterscheiden sich nur Ad-ID, Meta-ID und Startdatum (51 Tage später).

**Primärtext (wörtlich):** „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if you've been eyeing Mint Green — it's almost gone. The EasyRest™ is duvet and cover in one: wash it whole, dry in 2 hours.“

**Transkript:** GetHooked meldet „the next, video!!“ (0,00–15,16 s), also einen Platzhalter. Audio-Check:
- Pegel: mean −15,0 dB, max −4,0 dB, keine Stille.
- Die Tonspur korreliert mit 185228767 und dem Template zu ≈ 1,0.
- Die lokale Whisper-Gegenprobe liefert nur die Halluzination „Thanks for watching, and I'll see you next time.“ (no_speech_prob 0,52).

**Ergebnis: nur Musik, keine Sprache.**

**Hook (0–3 s)**
- Gesprochen: keiner.
- Eingeblendet: „This week only: / 2 FREE Pillow Cases / with every DUVET / Only 26 left in Mint Green“.
- Bild: Türrahmen-Kamerafahrt, mintgrüne Steppdecke, beige Kissen im Hintergrund. Hook-Typ: Angebot + Knappheit.

**Szenenliste (alle Schnitte angesehen)**
| Sek. | Szene | Einblendung (wörtlich) |
|---|---|---|
| 0,0–3,0 | Kamerafahrt durch den Türrahmen, Totale mintgrünes Bett | „This week only: / 2 FREE Pillow Cases / with every DUVET“ · „Only 26 left in Mint Green“ |
| 3,0–7,0 | POV-Hand (weißer Strickärmel) hebt die Deckenkante, Spannbettlaken sichtbar | „The duvet with no cover / Wash the whole thing“ |
| 7,0–10,7 | Hand streicht über die Decke, Nahaufnahme | „Dry in 2 hours / Back on the bed“ |
| 10,7–16,4 | Totale, Typewriter-Text, ab ca. 11,5 s Kissenbezug-Karte, Fade-to-black ab ca. 15,5 s | „2 FREE Pillow Cases / with every DUVET / Only 26 left in Mint Green“ · „FREE this week only“ · „~~£39.99~~“ |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–3 | Angebot + Knappheit (das Angebot steht schon im Hook) |
| Problem | – | **fehlt** |
| Verstärkung | – | **fehlt** |
| Mechanismus | 3–10,7 | „The duvet with no cover / Wash the whole thing“, „Dry in 2 hours / Back on the bed“ |
| Lösung | 0–16,4 | Produkt durchgehend |
| Beweis | – | **fehlt** |
| Angebot | 0–3 und 10,7–16,4 | 2 Gratis-Kissenbezüge, £39.99 durchgestrichen, „this week only“, „Only 26 left“ |
| CTA | – | im Video **fehlt**. Button „Shop now“ |

**Wer ist zu sehen / wer spricht:** keine Person, nur Hand und Unterarm. **KI-generiert (Einschätzung, Begründung wie bei 185228767 und Batch 1: Farbtausch eines synthetischen Clips, identische Hand- und Kamerabewegung in drei Farben).** Kein Sprecher.
**Setting:** KI-Luxus-Schlafzimmer, dunkles Holz.
**Avatar / Angle:** schnäppchen- und farborientierte Käufer, die Mint Green „im Auge haben“ („if you've been eyeing Mint Green“, deutet auf Retargeting hin, nicht verifiziert). **Angle F-Angebot + F-Knappheit/Farbe** (gleichrangig) + A sekundär („Wash the whole thing“).
**Haupt-Emotion:** Dringlichkeit (Wochenfrist + Restmenge).
**Schnitttempo / Untertitel / Ton:** 1,8 Schnitte pro 10 s. Keine Untertitel, nur Texteinblendungen (weiße Sans mit Schatten, oben, Typewriter-Effekt). Nur Musik.

**Konkrete Zahlen und Behauptungen (wörtlich):**
- Im Video: „This week only“ · „2 FREE Pillow Cases with every DUVET“ · „Only 26 left in Mint Green“ · „Wash the whole thing“ · „Dry in 2 hours“ · „FREE this week only“ · „£39.99“ (durchgestrichen).
- Primärtext: „it's almost gone“, „wash it whole, dry in 2 hours“.

**Angebotspräsentation:** Das Angebot steht schon im Hook und noch einmal auf der Endkarte, mit Wert £39.99 durchgestrichen, Wochenfrist und Restmenge „26“. Dieselbe Zahl „26“ steht auch in 139561410 (seit 2026-08-07) – die Restmenge ist also seit mindestens 51 Tagen unverändert (statische Angabe, Interpretation).
**Varianten-Hinweis:**
- Byte-identisch mit **139561410**.
- Weitere Ad mit gleicher Headline: **200490701** (Start 2026-10-06, 16 s, gleicher Platzhalter „the next, video!!“; nicht visuell verifiziert).
- Farbgeschwister: **139561428** (Hearth Red) und **139561491** (Coastal Blue). Neuschnitt mit Tog-Hook: **185228767**. Bild-Ad: 169082912.

---

#### Video 184134597 – Never Wrestle A Duvet Cover Again

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 184134597 |
| Meta-ID | 4249373995353335 |
| Ad Library | https://www.facebook.com/ads/library/?id=4249373995353335 |
| share_url | https://app.gethookd.ai/share/ad/184134597?signature=2b680d992f53e9489bd001330a9e608908df3f009b371ab2cf0e14275970f411 |
| Start / Tage aktiv | 2026-09-25 / 14 (start_to_today, active) |
| performance_score / used_count | 41 („Scaling“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Link-Beschreibung | „Coverless duvet · Nothing to wrestle · 30% off + 2 free pillow cases“ |
| Länge / Format | 47,3 s · 720×1280 · 30 fps |
| Schnitte | Der Detektor findet bei 0,3 nur 2 Schnitte (9,77 / 11,00 s), also 0,4 pro 10 s. Das ist **zu niedrig**, weil die meisten Übergänge Ein-Frame-Schwarzblitze (6,37 / 16,20 / 25,10 / 41,20 s, Y-Mittel ≈ 16) oder Überblendungen (≈ 21,7 / 27,0 / 35,2 s) sind. **Visuell gezählt: 11 Szenenwechsel = 2,3 pro 10 s** (0–10 s: 4 · 10–20 s: 2 · 20–30 s: 3 · 30–40 s: 1 · 40–47 s: 1) |

**Primärtext (wörtlich):** „🐙 Every wash day, my duvet cover turns into an angry octopus. Eight corners, none of them where they should be. / Then I got the Pleene EasyRest, and the cover just disappeared. / ✓ Cover sewn in, one piece, nothing to wrestle / ✓ Lay it on the bed and the bed is made / ✓ Washes whole in your machine at home, dry in 2 hours 🧺 / 🎁 30% off + 2 FREE matching pillow cases.“

**Transkript (GetHooked/Whisper, vollständig, wörtlich)**
| Sek. | Text |
|---|---|
| 0,00–6,40 | I bloody hate changing the bed, not the sheets, that bit, the bit where the cover fights back. |
| 6,40–9,84 | Then I got the Pleen EasyRest and the cover just disappeared. |
| 9,84–13,44 | It's a duvet and cover in one, so there's nothing to wrestle. |
| 13,44–17,60 | You lay it on the bed, and the bed is made, that's it. |
| 17,60–22,48 | When it needs washing, the whole thing goes into your normal 7kg washing machine, then |
| 22,48–25,92 | the tumble dryer, and it's dry in two hours. |
| 25,92–31,12 | It's 10.5 tog, so it's every bit as warm as a winter duvet, just without the weight, |
| 31,12–34,60 | and the breathable fibres mean it never feels stuffy on you. |
| 34,60–37,96 | I swear to you, my bed always feels fresh. |
| 37,96–41,68 | And the Pleen pillowcases really do feel super soft. |
| 41,68–46,76 | Right now, the EasyRest is on offer with 30% off, plus two free Pleen pillowcases. |

Transkript-Qualität: gut. Die lokale Whisper-Gegenprobe ist inhaltlich deckungsgleich („seven kilogram washing machine“, „10.5 Tog“, „30% off“). Korrekturen laut Untertitel: „Pleen“ heißt „PLEENE“. Die Untertitel schreiben „7 KILOGRAM WASHING MACHINE“ und „BREATHABLE FIBERS“ (US-Schreibweise). Die Sprechpausen sind digital still (z. B. 16,6–17,5 s: −67 dBFS), **es gibt also kein Musikbett**.

**Hook (0–3 s)**
- Gesprochen: „I bloody hate changing the bed, not the sheets, that bit, …“ (der Satz läuft bis 6,4 s weiter: „… the bit where the cover fights back.“).
- Eingeblendet: „I BLOODY HATE CHANGING THE BED“ (0–ca. 2,5 s), dann „NOT THE SHEETS THAT BIT“.
- Bild: POV, zwei schlanke Hände (vermutlich weiblich) zerren an einem rostroten Damast-Bettbezug auf einem Bett in hellem Schlafzimmer (Lampe, Pflanze, Holzkopfteil).
- Hook-Typ: emotionaler Frust-Ausruf in der Ich-Form mit britischem Slang („bloody“).

**Szenenliste (alle 11 Übergänge und 2,5-Sekunden-Raster angesehen)**
| Sek. | Szene | Einblendung (wörtlich, Untertitel) |
|---|---|---|
| 0,00–3,70 | POV-Hände greifen den rostroten, gemusterten Bettbezug | „I BLOODY HATE CHANGING THE BED“ → „NOT THE SHEETS THAT BIT“ |
| 3,70–6,37 | Hände heben bzw. zerren den Bezug (Matratze sichtbar), Totale rostrotes Bett mit Händen | „NOT THE SHEETS THAT BIT“ → „THE BIT WHERE THE COVER FIGHTS“ |
| 6,37 (Schwarzblitz) –8,50 | **Produkt-Reveal**: mintgrüne EasyRest liegt gefaltet auf weißem Bett, Hände öffnen sie | „THEN I GOT THE PLEENE EASY“ → „AND THE COVER JUST DISAPPEARED“ |
| 8,50–9,77 | Hand schlägt die Decke auf dem Bett zurück | „AND THE COVER JUST DISAPPEARED“ |
| 9,77–11,00 | Zwei Hände heben die Deckenkante, Matratze und Bettrahmen sichtbar | „IT'S A DUVET AND COVER IN“ |
| 11,00–16,20 | Hand glättet die Decke, langsame Rückfahrt zur Totale (mintgrünes Schlafzimmer mit Pflanzen) | „ONE“ → „SO THERE'S NOTHING TO WRESTLE“ → „YOU LAY IT ON THE BED“ → „AND THE BED IS MADE“ → „THAT'S IT“ |
| 16,20 (Schwarzblitz) –ca. 21,7 | Waschküche: Hände stopfen die Decke in einen Frontlader, Hand am Programmwahlschalter | „THAT'S IT“ → „WHEN IT NEEDS WASHING“ → „THE WHOLE THING GOES INTO YOUR“ → „NORMAL“ → „7 KILOGRAM WASHING MACHINE“ |
| ca. 21,7 (Überblendung) –25,0 | POV: Hände halten die gefaltete Decke vor einem offenen Frontlader (als Trockner gemeint) | „THEN THE TUMBLE DRYER AND IT'S“ → „DRY IN TWO HOURS“ |
| 25,10 (Schwarzblitz) –ca. 27,0 | Gefaltete Decke auf dem Bett, Hände klappen sie auf | „IT'S 10.5 TOG“ |
| ca. 27,0 (Überblendung) –ca. 35,2 | POV aus dem Bett: Hand drückt auf die Steppdecke, Fenster im Hintergrund. Bei ca. 30 s halbtransparente „Geisterhand“ (Überblendungs-Artefakt) | „SO IT'S EVERY BIT AS WARM“ → „AS A WINTER DUVET“ → „JUST WITHOUT“ → „THE WEIGHT AND THE BREATHABLE FIBERS“ → „MEAN IT NEVER FEELS STUFFY ON“ → „YOU“ → „I SWEAR TO YOU MY BED“ |
| ca. 35,2 (Überblendung) –41,20 | Hand tätschelt ein mintgrünes Kissen | „ALWAYS FEELS FRESH“ → „AND THE PLEENE PILLOW CASES REALLY“ → „DO FEEL SUPER SOFT“ |
| 41,20 (Schwarzblitz) –47,32 | Totale mintgrünes Schlafzimmer, langsame Kamerafahrt, Abblende ab ca. 46,5 s | „RIGHT NOW THE EASY REST IS“ → „ON OFFER WITH 30% OFF“ → „PLUS TWO FREE PLEENE PILLOW CASES“ |

**Aufbau**
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–3 | Frust-Ausruf „I bloody hate changing the bed“ |
| Problem | 0–6,4 | „the bit where the cover fights back“ (Kampf mit dem Bezug) |
| Verstärkung | – | **fehlt** (keine Eskalation, kein Wiederholungs- oder Zeit-Argument) |
| Lösung | 6,4–17,6 | Reveal „the cover just disappeared“, „duvet and cover in one“, „the bed is made, that's it“ |
| Mechanismus | 17,6–34,6 | „normal 7kg washing machine“, „tumble dryer“, „dry in two hours“, „10.5 tog“, „breathable fibres … never feels stuffy“ |
| Beweis | 34,6–41,7 | nur persönliches Testimonial („I swear to you, my bed always feels fresh“, „super soft“). Zahlen, Reviews und Kundenzahl **fehlen** |
| Angebot | 41,7–46,8 | „30% off, plus two free Pleen pillowcases“ |
| CTA | – | im Video **fehlt** (kein Handlungsaufruf). Button „Shop now“ |

**Wer ist zu sehen / wer spricht:**
- Zu sehen ist keine Person, nur Hände und Unterarme (schlank, vermutlich weiblich) in POV-Perspektive.
- Es spricht ein **Off-Voiceover**. f0-Median ca. 193 Hz (p25 167 / p75 235 Hz), also vermutlich eine **Frauenstimme** (nicht verifiziert). Britische Wortwahl („bloody“, „tog“, „tumble dryer“). Ob es eine KI-Stimme ist: nicht verifiziert.
- **Visuals: KI-generiert (Einschätzung).** Gründe:
  - durchgehend glatte Render-Optik, Hände ohne Hautdetails;
  - Raumdetails (Kopfteil, Regale, Pflanzen) wechseln zwischen Einstellungen, die dasselbe Zimmer zeigen sollen;
  - keine einzige Einstellung mit ganzer Person;
  - Stil wie bei generierten Produkt-Clips.

**Setting:** helles Schlafzimmer (Holz, Pflanzen) und Waschküche mit Frontlader.
**Avatar / Angle:** britische Frauen, geschätzt 35–65, die das Beziehen hassen; Komfortsucher. **Angle C** (primär) + B („10.5 tog“, „every bit as warm as a winter duvet“, „never feels stuffy“) + A sekundär (ganze Decke in die normale Maschine, 2 h trocken) + F-Angebot (30 %).
**Haupt-Emotion:** Frust bzw. Ärger (Hook, Problem), danach Erleichterung („that's it“).
**Schnitttempo / Untertitel / Ton:**
- 2,3 Szenenwechsel pro 10 s (visuell; der Detektor bei 0,3 findet nur 0,4).
- Untertitel ja: Großbuchstaben, weiß, fett, mit schwarzer Kontur, Bildmitte bis unteres Drittel, 1–6 Wörter pro Einblendung, wortgenau zum VO (TikTok-Stil).
- Ton: nur VO, **keine Musik**.

**Konkrete Zahlen und Behauptungen (wörtlich):**
- Im Video: „normal 7kg washing machine“ (UT „7 KILOGRAM WASHING MACHINE“) · „dry in two hours“ · „It's 10.5 tog“ · „every bit as warm as a winter duvet, just without the weight“ · „breathable fibres mean it never feels stuffy on you“ · „my bed always feels fresh“ · „30% off“ · „two free Pleen pillowcases“.
- Primärtext: „Eight corners“, „Washes whole in your machine at home, dry in 2 hours“, „30% off + 2 FREE matching pillow cases“.
- **Nicht im Video:** £-Werte, 90-Nächte-Test, Kundenzahl.

**Angebotspräsentation:** am Ende gesprochen und eingeblendet: 30 % Rabatt plus 2 Gratis-Kissenbezüge. Keine Frist, keine Knappheit, kein £-Wert, kein Testversprechen.
**Varianten-Hinweis:**
- **Hook-Test.** Drei Videos starteten am 2026-09-25 mit identischem Körper-Skript ab „Then I got the Pleen EasyRest and the cover just disappeared …“ bis „… plus two free Pleen pillowcases“ (laut GetHooked-Transkripten; visuell nicht verifiziert):
  - **184134597**: „I bloody hate changing the bed, not the sheets, that bit, the bit where the cover fights back.“ (47 s)
  - **184134616**: „Every wash day, my duvet cover turns into a demented octopus. Eight corners, none of them where they should be.“ (48 s)
  - **184134607**: „Changing a duvet cover is the work of the devil. Whoever invented it never had to do it on a Sunday night.“ (48 s)
- Der Primärtext von 184134597 („angry octopus“) gehört inhaltlich zum Hook von 184134616.
- **193234275** trägt dieselbe Headline und denselben Primärtext, ist aber ein ganz anderes Video (Kopie von 133366534).
- Die Körper-Formeln „I swear to you, my bed always feels fresh“ und „pillowcases really … feel super soft“ stammen aus dem Skript von 136389861 und 145443331.

---

#### Video 193234275 – Never Wrestle A Duvet Cover Again

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 193234275 |
| Meta-ID | 931889339640196 |
| Ad Library | https://www.facebook.com/ads/library/?id=931889339640196 |
| share_url | https://app.gethookd.ai/share/ad/193234275?signature=ffce5170bcd8108ccef8ec8fa356ebe88ee4788757813cf94c27b340e5ff2e63 |
| Start / Tage aktiv | 2026-10-01 / 8 (start_to_today, active) |
| performance_score / used_count | 52 („Scaling“) / 1 |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/products/easyrest |
| Link-Beschreibung | „Coverless duvet · Nothing to wrestle · 30% off + 2 free pillow cases“ |
| Länder | `countries: []` in get_ad (n/a) |
| Länge / Format | 92,7 s · 720×1280 · 25 fps |
| Schnitte (0,3) | 51 gesamt = **5,5 pro 10 s** (0–10: 5 · 10–20: 5 · 20–30: 5 · 30–40: 10 · 40–50: 5 · 50–60: 6 · 60–70: 4 · 70–80: 6 · 80–90: 5 · 90–92,7: 0) |

**Identität:** Die MP4 ist **byte-identisch mit 133366534** (Batch 1, Top-20, Score 100, Start 2026-08-03) und mit **193234279**, md5 `9877275e5c9724bee5a00be00da2fb3f`. Die 23 extrahierten Frames von 193234275 und 193234279 sind per md5 bitgleich. Die vollständige Szenenliste mit 44 + 18 Frames steht in Batch 1 unter 133366534 und gilt unverändert. Anders sind hier nur die **Copy** (Octopus-Primärtext und Headline aus der 184134xxx-Familie) und die Link-Beschreibung mit „30% off“.

**Primärtext (wörtlich):** „🐙 Every wash day, my duvet cover turns into an angry octopus. Eight corners, none of them where they should be. / Then I got the Pleene EasyRest, and the cover just disappeared. / ✓ Cover sewn in, one piece, nothing to wrestle / ✓ Lay it on the bed and the bed is made / ✓ Washes whole in your machine at home, dry in 2 hours 🧺 / 🎁 30% off + 2 FREE matching pillow cases.“

**Transkript (GetHooked/Whisper, vollständig, wörtlich)**
| Sek. | Text |
|---|---|
| 0,00–4,00 | Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it. When did |
| 4,00–8,40 | you last actually wash it? Not the cover. The duvet itself. Most people never do, |
| 8,40–13,36 | because it doesn't fit in a normal washing machine. And even if it does, drying takes forever. Sweat, |
| 13,36–18,00 | dust mites, skin particles. It all builds up, while you tell yourself that swapping the cover |
| 18,00–22,00 | is enough. And then there's the weekly ritual. Strip the old cover, hunt for the corners, |
| 22,00–26,48 | stuff the duvet back in, everything slips. And then all over again. Every week. For the |
| 27,04–31,68 | of your life. The problem isn't your bed linen. The problem is your duvet. The plean easy rest |
| 31,68–36,64 | is a duvet and cover in one. Nothing to stuff, no corners, no fiddling, just throw it on. Done. |
| 36,64–41,28 | And this is wash day. The whole thing goes straight in. It fits in any normal household |
| 41,28–46,16 | washing machine. The entire duvet. Everything gets washed out. And it's dry in two hours. |
| 46,16–49,92 | Even without a dryer. In the machine in the morning. Fresh on the bed by evening. The |
| 49,92–54,88 | breathable fibres adapt to your body temperature. Cool when it's warm. Warm when it turns cold. No |
| 54,88–59,84 | more sweating in summer. No more freezing in winter. One duvet all year round. Hypoallergenic. |
| 59,84–65,84 | Over 10,000 sleepers have already switched. And 96% never want to go back after their 90 night |
| 65,84–70,80 | trial. George is over 80. A widower. Making the bed alone was always a struggle. Now it's easy. |
| 70,80–75,52 | And Sarah. Washing her whole duvet has become a weekly routine. Especially because of her allergies. |
| 75,52–79,92 | Your first night. You feel lighter, fresher, different. After the first week, wash day done |
| 79,92–84,72 | in two hours. After a month, that nagging, I really should change the bedding, is simply gone. |
| 84,72–88,56 | 90 nights to sleep on it. If you're not convinced, you simply get your money back. |
| 88,56–92,32 | Right now it comes with two free Pleen pillowcases. Tap the link below. |

Transkript-Qualität: gut. Korrektur laut Untertitel: „For the of your life“ heißt „For the rest of your life“ (UT bei 25 s angesehen). In der Lücke 26,48–27,04 s liegt der Pegel bei −19,8 dBFS, dort wird also gesprochen (das von Whisper ausgelassene „rest“). „plean easy rest“ heißt „Pleene EasyRest™“. Audio: mean −16,6 dB, keine Stille ≥ 0,4 s. Nach dem VO-Ende (92,35–92,7 s) bleiben −29,9 dBFS. Das deutet auf ein leises Musikbett hin (nicht verifiziert).

**Hook (0–3 s)**
- Gesprochen: „Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it.“
- Eingeblendet: Top-Badge „No more bed changing ❌“ und Untertitel „Sorry, but your duvet is probably the dirtiest thing in your bedroom“.
- Bild: 0–1,8 s ein Mann (ca. 30–40, weißes T-Shirt) zieht eine weiße Decke ab, Zimmer mit Holzbalken. Ab 1,8 s schüttelt eine junge Frau (ca. 20–30, dunkle Haare) eine weiße Decke auf dem Bett auf.
- Hook-Typ: Ekel- bzw. Schock-Behauptung mit „Sorry, but…“-Pattern-Interrupt.

**Gesehene Frames (Raster 0/1/2/3 s, dann alle 5 s; Einblendungen wörtlich)**
| Sek. | Bild | Einblendung |
|---|---|---|
| 0 / 1 | Mann weißes T-Shirt, weiße Decke, Holzbalken-Zimmer | Badge „No more bed changing ❌“ · UT „Sorry, but your duvet is probably the dirtiest thing in your bedroom“ |
| 2 / 3 | Junge Frau mit weißer Decke auf dem Bett | dto. |
| 5 | Frau verschwindet im gemusterten Bezug | Badge dto. · UT „When did you last actually wash it? Not the cover. The duvet itself“ |
| 10 | Weiße Decke wird in Waschmaschine/Trockner-Turm gedrückt | UT „because it doesn't fit in a normal washing machine“ |
| 15 | Männerhände an weißer Decke + **Kreis-Einschub mit Mikroskopbild länglicher brauner Organismen**, Pfeil auf die Decke | UT „Sweat, dust mites, skin particles. It all builds up,“ |
| 20 | Frau (schwarzes Top) wirft sich mit weißer Decke aufs Bett | UT „And then there's the weekly ritual“ |
| 25 | Split-Screen: tätowierter Mann zweimal beim Beziehen | UT „And then all over again. Every week. For the rest of your life“ |
| 30 | Frau schüttelt hellen, gemusterten Bezug | UT „The problem is your duvet“ |
| 35 | Junge Frau (Blumen-Pyjama) unter mintgrüner EasyRest, Daumen hoch | UT „Nothing to stuff, no corners, no fiddling. Just throw it on. Done“ |
| 40 | Waschturm, tätowierter Arm stopft dunkle Decke hinein | Badge „✅ Fits any washing machine“ · UT „It fits in any normal household washing machine“ |
| 45 | Hand auf anthrazitfarbener Decke | Badge „✅ Quick-drying“ · UT „And it's dry in two hours. Even without a dryer“ |
| 50 | Frau liegt unter navyblauer Decke | Badge „✅ Temperature-regulating“ · UT „The breathable fibres adapt to your body temperature“ |
| 55 | Mann (Bart, ca. 30) liegt unter anthrazitfarbener Decke | UT „No more sweating in summer. No more freezing in winter“ |
| 60 | Hände falten navyblaue Decke | Badge „✅ 10,000+ happy customers“ · UT „Over 10,000 sleepers have already switched“ |
| 65 | Frau (Pferdeschwanz) sitzt auf dem Bett | UT „And 96% never want to go back after their 90-night trial“ |
| 70 | Glatzkopf-Mann streckt sich in mintgrünem Bett + Review-Karte | UT „Making the bed alone was always a struggle“ · Karte „★★★★★ “Since my wife passed, making the bed was the job I dreaded most. This duvet has made it easy again.” George, 82 · Verified buyer“ |
| 75 | Frau (graues T-Shirt) mit weißer Decke + Review-Karte | UT „Especially because of her allergies“ · Karte „★★★★★ I'm allergic to dust and pollen, so being able to wash the entire duvet, not just the cover, is exactly what I needed. Sarah — Verified buyer“ |
| 80 | Graues Bett | UT „After the first week: wash day done in two hours“ |
| 85 | Hände in grauer Decke | UT „90 nights to sleep on it“ |
| 90 | Frau (schwarze Strickjacke) mit grauem Kissen | UT „Right now it comes with two free Pleene™ Pillow Cases“ |
| 92,4 | dto. | „Tap the link below“ |

**Aufbau** (identisch mit 133366534)
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–4 | „dirtiest thing in your bedroom“ + Badge „No more bed changing ❌“ |
| Problem | 4–18 | Die Decke wird nie gewaschen (passt nicht in die Maschine, Trocknung dauert ewig). Schweiß, Milben und Hautpartikel sammeln sich |
| Verstärkung | 18–31 | „weekly ritual“, „Every week. For the rest of your life“, Reframe „The problem isn't your bed linen. The problem is your duvet.“ |
| Lösung | 30,8–36,6 | Reveal (mintgrün): „duvet and cover in one … just throw it on. Done.“ |
| Mechanismus | 36,6–59,8 | ganze Decke in die normale Waschmaschine, „dry in two hours. Even without a dryer“, „breathable fibres adapt to your body temperature“ (CGI-Fasern laut Batch 1), „Hypoallergenic“ |
| Beweis | 59,8–75,5 | „Over 10,000 sleepers“, „96%“, Review-Karten George (82) und Sarah (Allergie). Danach Future Pacing 75,5–84,7 |
| Angebot | 84,7–92,3 | 90 Nächte mit Geld-zurück, „two free Pleene™ Pillow Cases“ (im Video ohne £-Wert und **ohne die 30 % aus dem Primärtext**) |
| CTA | 90,6–92,7 | „Tap the link below.“ + Button „Shop now“ |

**Wer ist zu sehen / wer spricht:** Kompilation aus mindestens 15 verschiedenen UGC- bzw. stockartigen Clips (Frauen ca. 20–45, Männer ca. 25–55). Handy-Ästhetik, wechselnde Wohnungen, natürliche Gesichter. Einschätzung: **echte Personen, UGC- bzw. Lizenzmaterial** (Herkunft nicht verifiziert). Einzige CGI-Einlage ist die Faser-Animation bei ca. 53,5 s (laut Batch 1). Niemand spricht im Bild: **Off-Voiceover**, f0-Median ca. 139 Hz, also vermutlich männlich (nicht verifiziert). Ob die Stimme KI-generiert ist: nicht verifiziert. Wie in Batch 1 gilt: Zur Karte „George, 82“ wird ein Mann gezeigt, den man visuell auf ca. 45–55 schätzt. Bild und Review passen nicht zusammen (Schätzung).
**Setting:** diverse Schlafzimmer, Waschküche bzw. Keller, Küche, ein Außenclip (Garten, laut Batch 1).
**Avatar / Angle:** hygienebewusste Haushalte und Bettwäsche-Wechsler (30–65), zusätzlich Allergiker und alleinstehende Senioren (George). **Angle A** (primär) + C (Wochenritual) + B (Temperatur) + E (George „over 80“) + F-Social-Proof + F-Angebot. **Copy-Bruch:** Headline, Primärtext und Link-Beschreibung bewerben Angle C mit „30% off“, das Video führt mit Angle A und nennt keine 30 %.
**Haupt-Emotion:** Ekel und Scham (Hook, Problem), dann Frust (Wochenritual), dann Erleichterung (Future Pacing).
**Schnitttempo / Untertitel / Ton:** 5,5 Schnitte pro 10 s, Spitze 10 Schnitte bei 30–40 s. Untertitel ja: weiße Box, schwarze fette Sans (Poppins-artig), Bildmitte. Dazu Top-Badges mit ✅/❌ und Review-Karten. Ton: durchgehend Off-VO, ein leises Musikbett ist möglich (nicht verifiziert).

**Konkrete Zahlen und Behauptungen (wörtlich):** „probably the dirtiest thing in your bedroom“ · „Sweat, dust mites, skin particles. It all builds up“ · „It fits in any normal household washing machine“ · „And it's dry in two hours. Even without a dryer.“ · „In the machine in the morning. Fresh on the bed by evening.“ · „Cool when it's warm. Warm when it turns cold.“ · „No more sweating in summer. No more freezing in winter.“ · „Hypoallergenic.“ · „Over 10,000 sleepers have already switched.“ · „96% never want to go back after their 90 night trial“ · „George is over 80“ / Karte „George, 82“ · „wash day done in two hours“ · „90 nights to sleep on it. If you're not convinced, you simply get your money back.“ · Badges „✅ Fits any washing machine“, „✅ Quick-drying“, „✅ Temperature-regulating“, „✅ 10,000+ happy customers“. Keine Tog-Angabe, kein Preis, kein £-Wert.
**Angebotspräsentation:** am Ende gesprochen und eingeblendet: „Right now it comes with two free Pleene™ Pillow Cases“ plus Risikoumkehr „90 nights … money back“. Die im Primärtext und in der Link-Beschreibung versprochenen „30% off“ kommen im Video nicht vor.
**Varianten-Hinweis:** byte-identisch mit **133366534** (Original, `/products/easyrest`, Original-Copy) und **193234279** (Original-Copy, LP `/pages/tb-6`). Pleene testet hier dasselbe Gewinner-Video mit der Copy der Hook-Test-Familie 184134597 / 184134616 / 184134607 (Interpretation).

---

#### Video 193234221 – Everyone said it. They were right.

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 193234221 |
| Meta-ID | 2325762131511604 |
| Ad Library | https://www.facebook.com/ads/library/?id=2325762131511604 |
| share_url | https://app.gethookd.ai/share/ad/193234221?signature=34d449a91191d816e5a91f7d690e2d93f52044d2af092704c3b3dece336abb59 |
| Start / Ende / Tage aktiv | 2026-10-01 / **2026-10-07** / 7 (start_to_end_date). **Status laut get_ad am 08.10.: inactive** (enriched: active, 8 Tage) |
| performance_score / used_count | **n/a** (get_ad: null; enriched: 52 „Scaling“) / 1 |
| CTA | ORDER_NOW – „Order now“ |
| Landingpage | https://pleene.com/pages/tb-6 (Advertorial bzw. Pre-Lander, siehe s3_funnel.md) |
| Link-Beschreibung | „⭐️⭐️⭐️⭐️⭐️ – Over 10,000 Happy Customers“ |
| Länge / Format | 47,0 s · 720×1280 · 25 fps |
| Schnitte (0,3) | 7 (3,8 / 11,2 / 19,6 / 25,32 / 27,84 / 31,08 / 37,56 s) = **1,5 pro 10 s** (0–10: 1 · 10–20: 2 · 20–30: 2 · 30–40: 2 · 40–47: 0) |

**Identität:** Die MP4 ist **byte-identisch mit 145443331 und 163921089** (Batch 1, beide Score 100), md5 `a22e6497e1155287fea63fd80477ee89`. Headline, Primärtext und CTA sind identisch, **neu ist die Landingpage tb-6**.

**Primärtext (wörtlich):** „I only ordered it because everyone said you never have to change the bed linen again. Annoyingly, they were right. The Pleene EasyRest™ is a duvet and cover in one — wash it whole, dry in 2 hours, throw it back on.“

**Transkript (GetHooked/Whisper, vollständig, wörtlich)**
| Sek. | Text |
|---|---|
| 0,00–3,76 | I haven't changed my bed linen in three months and it's never felt fresher. |
| 3,76–8,40 | The Pleen Easy Rest Duvet is a duvet and covering one, so no more separate bed linen. |
| 12,56–15,12 | Just put it in the washing machine and then in the tumble dryer. |
| 19,36–22,72 | And the best thing is the breathable fibres adapt to your body, |
| 22,72–25,20 | nice and warm in the winter, comfortable and cool in the summer. |
| 25,20–27,76 | I swear to you, my bed always feels fresh. |
| 27,76–31,04 | And the Pleen Pillow Cases really feel super soft. |
| 31,04–35,44 | And the Pleen Easy Rest comes in loads of limited colours and all different sizes. |
| 35,44–37,52 | Honestly, the hardest part was picking one. |
| 37,52–42,80 | At the moment, the Pleen Easy Rest Duvet is even on offer with two free Pleen Pillow Cases |
| 42,80–45,04 | and a 90-night trial sleep guarantee. |
| 45,04–46,64 | You can simply test it yourself. |

Transkript-Qualität: gut. Korrekturen laut Untertitel: „covering one“ heißt „cover in one“ (UT bei 5 s: „is a duvet and cover in one“), „Pleen“ heißt „Pleene™“. Der UT bei 3 s lautet „— and my bed has never felt fresher“. In den Sprechpausen 8,4–12,6 s und 15,1–19,4 s liegt der Pegel bei −30,0 bzw. −32,1 dBFS. Das Spektrogramm (`wf/s2b3_audio/193234221_spec_8_20.png`) zeigt dort rhythmische Transienten und stehende Töne. Das spricht für ein **leises Musikbett** (Einschätzung), Sprache ist dort keine.

**Hook (0–3 s)**
- Gesprochen: „I haven't changed my bed linen in three months and it's never felt fresher.“
- Eingeblendet: „I haven't changed my bed linen in three months“ (0–3 s), dann „— and my bed has never felt fresher“.
- Bild: Totale schräg von oben. Ein Mann liegt mit ausgestrecktem Arm unter einer grauen Steppdecke, das Zimmer hat eine grüne Wand, Holzbett und eine Hängelampe mit Kupfermuster.
- Hook-Typ: provokante Ich-Aussage (scheinbarer Hygiene-Tabubruch, der positiv aufgelöst wird).

**Gesehene Frames (Raster 0/1/2/3 s, dann alle 5 s; Einblendungen wörtlich)**
| Sek. | Bild | Einblendung |
|---|---|---|
| 0–2 | Mann liegt im Bett unter grauer Decke | „I haven't changed my bed linen in three months“ |
| 3 | dto. | „— and my bed has never felt fresher“ |
| 5 | Mann steht am Bett und hebt die graue Decke an, Blick in die Kamera | „The Pleene EasyRest™ Duvet is a duvet and cover in one“ |
| 10 | Mann legt die Decke zurück | „So no more separate bed linen“ |
| 15 | Küche mit Fliesenboden, Mann hockt vor dem Frontlader | „and then in the tumble dryer“ |
| 20 | Mann liegt im Bett, Selfie-Perspektive, spricht | „And the best thing is,“ |
| 25 | dto. | „Comfortable and cool in the summer“ |
| 30 | Mann hinter dem Bett mit Decke (Totale) | „And the Pleene™ Pillow Cases really feel super soft“ |
| 35 | Mann am Bett + eingeblendetes Produktbild (weiße Decke) | „and all different sizes“ |
| 40 | Mann sitzt frontal auf der Bettkante und spricht | „At the moment, the Pleene EasyRest™ Duvet is even on offer“ |
| 45 | dto. + **Overlay-Karte** aus dem KI-Template (mintgrünes Schlafzimmer) | „And a 90-night trial sleep guarantee,“ · Karte „This week only: 2 FREE Pillow Cases with every DUVET ⏱“ · Badge „FREE this week only“ · „~~£39.99~~“ |
| 46,8 | dto. | „you can simply test it yourself“ |

**Aufbau** (identisch mit 145443331)
| Baustein | Sek. | Inhalt |
|---|---|---|
| Hook | 0–3,8 | „haven't changed my bed linen in three months … never felt fresher“ |
| Problem | – | **fehlt explizit**, nur implizit (Bettwäsche wechseln) |
| Verstärkung | – | **fehlt** |
| Lösung | 3,8–8,4 | „duvet and cover in one, so no more separate bed linen“ |
| Mechanismus | 11,2–25,3 | Waschmaschine + Trockner, „breathable fibres adapt to your body“, warm/kühl |
| Beweis | 25,3–31,1 | nur persönliches Testimonial („I swear to you…“, „super soft“). Keine Zahlen |
| (Auswahl / leichte Knappheit) | 31,1–37,6 | „loads of limited colours and all different sizes“, „the hardest part was picking one“ |
| Angebot | 37,6–46,6 | 2 Gratis-Kissenbezüge (Overlay £39.99 durchgestrichen, „This week only“) + 90-Nächte-Test |
| CTA | 45–46,6 | weich: „You can simply test it yourself.“ Button „Order now“ |

**Wer ist zu sehen / wer spricht:** ein **echter UGC-Creator**: Mann, geschätzt 30–40, kurze dunkle Haare, Bart, graues Tanktop, Smartwatch, britisch wirkendes Zuhause (Erkerfenster, grüne Wand). Er spricht teils lippensynchron in die Kamera (ca. 19,6–25 s und 37,6–47 s), sonst als VO über eigenen Handlungsszenen. Kein Hinweis auf KI-Generierung erkennbar. f0-Median ca. 148 Hz (männlich). Ob die Stimme KI ist: nicht verifiziert, sie wirkt bildlich lippensynchron.
**Setting:** Schlafzimmer (grüne Wand) und Küche mit Waschmaschine.
**Avatar / Angle:** Pragmatiker, die Bettwäschewechsel hassen (Männer und junge Haushalte, ca. 25–45). **Angle C** (primär) + B (warm/kühl) + F-Farbauswahl/limitiert + F-Angebot. A nur indirekt („never felt fresher“, Waschmaschine).
**Haupt-Emotion:** Neugier bzw. Irritation (provokanter Hook), dann Erleichterung und Bequemlichkeit.
**Schnitttempo / Untertitel / Ton:** 1,5 Schnitte pro 10 s, ruhig, lange Einstellungen. Untertitel ja: weiße Box, schwarze fett-kursive Sans, satzweise, Bildmitte. Ton: Creator-O-Ton bzw. VO, leises Musikbett (Einschätzung).

**Konkrete Zahlen und Behauptungen (wörtlich):** „I haven't changed my bed linen in three months“ · „duvet and cover in one“ · „washing machine and then in the tumble dryer“ · „breathable fibres adapt to your body, nice and warm in the winter, comfortable and cool in the summer“ · „loads of limited colours and all different sizes“ · „two free Pleen Pillow Cases“ · „90-night trial sleep guarantee“ · Overlay: „This week only“, „£39.99“ (durchgestrichen), „FREE this week only“. Primärtext: „dry in 2 hours“.
**Angebotspräsentation:** gesprochen: „even on offer with two free … Pillow Cases and a 90-night trial sleep guarantee“. Visuell die Template-Angebotskarte mit Wert £39.99 durchgestrichen und „This week only“. Farbauswahl als leichte Knappheit („limited colours“).
**Varianten-Hinweis:** byte-identisch mit **145443331** und **163921089** (beide `/products/easyrest`). Dieselbe Copy und LP tb-6 hat auch **193234219** (Start 2026-10-01). Dessen Transkript ist laut Batch 1 fälschlich als Walisisch erkannt, gehört nicht zu diesem Batch und ist nicht verifiziert. Dass 193234221 nach 7 Tagen auf tb-6 endete, während die Kopien auf der Produktseite mit Score 100 laufen, ist ein möglicher Hinweis auf schwächere Performance des Advertorial-Pfads (Interpretation, nicht verifiziert).

---

#### Video 193234279 – No More Fighting With Duvet Covers

**Metadaten**
| Feld | Wert |
|---|---|
| GetHooked-ID | 193234279 |
| Meta-ID | 28476177958733795 |
| Ad Library | https://www.facebook.com/ads/library/?id=28476177958733795 |
| share_url | https://app.gethookd.ai/share/ad/193234279?signature=13f6122c0c5d22eb8c8b6141c88c013e8051538391bd99bbd1f57e3f4702f207 |
| Start / Tage aktiv | 2026-10-01 / 8 (start_to_today, active) |
| performance_score / used_count | 41 („Scaling“; enriched: 44) / 1 (enriched: 2) |
| CTA | SHOP_NOW – „Shop now“ |
| Landingpage | https://pleene.com/pages/tb-6 (page_type in get_ad: null) |
| Link-Beschreibung | „⭐️⭐️⭐️⭐️⭐️ – Over 10,000 Happy Customers“ |
| Länder | `countries: []` in get_ad (n/a) |
| Länge / Format | 92,7 s · 720×1280 · 25 fps |
| Schnitte (0,3) | 51 = **5,5 pro 10 s** (Verteilung wie bei 193234275) |

**Identität:** Die MP4 ist **byte-identisch mit 133366534 und 193234275** (md5 `9877275e5c9724bee5a00be00da2fb3f`). Die 23 Frames unter `wf/frames/193234279/` sind per md5 bitgleich mit denen von 193234275. Gegenüber 133366534 sind Headline und Primärtext gleich, **neu ist die Landingpage tb-6**. In Batch 1 war die Identität nur über das Transkript vermutet, **jetzt ist sie per md5 verifiziert**.

**Primärtext (wörtlich):** „Duvet + Cover in One 🌙 / The Pleene EasyRest™ makes changing the bed finally simple. Wash it, dry it, and lay it back on — that's it. / ✓ No more wrestling with a separate duvet cover / ✓ Pleasantly cool in summer, cosily warm in winter / ✓ Hypoallergenic and kind to sensitive skin / Get 2 free Pleene™ Pillow Cases today (worth £39.99). / 90 nights to try it risk-free. / Enjoy a bed that always feels fresh.“

**Transkript (GetHooked/Whisper, vollständig, wörtlich)**
| Sek. | Text |
|---|---|
| 0,00–4,00 | Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it. When did |
| 4,00–8,40 | you last actually wash it? Not the cover, the duvet itself. Most people never do, |
| 8,40–13,36 | because it doesn't fit in a normal washing machine. And even if it does, drying takes forever. Sweat, |
| 13,36–18,00 | dust mites, skin particles. It all builds up, while you tell yourself that swapping the cover |
| 18,00–22,00 | is enough. And then there's the weekly ritual. Strip the old cover, hunt for the corners, |
| 22,00–26,48 | stuff the duvet back in, everything slips. And then all over again. Every week. For the |
| 27,04–31,68 | of your life. The problem isn't your bed linen. The problem is your duvet. The plean easy rest |
| 31,68–36,64 | is a duvet and cover in one. Nothing to stuff, no corners, no fiddling, just throw it on. Done. |
| 36,64–41,28 | And this is wash day. The whole thing goes straight in. It fits in any normal household |
| 41,28–46,16 | washing machine. The entire duvet. Everything gets washed out. And it's dry in two hours. |
| 46,16–49,92 | Even without a dryer. In the machine in the morning. Fresh on the bed by evening. The |
| 49,92–54,88 | breathable fibres adapt to your body temperature. Cool when it's warm. Warm when it turns cold. No |
| 54,88–59,84 | more sweating in summer. No more freezing in winter. One duvet all year round. Hypoallergenic. |
| 59,84–65,84 | Over 10,000 sleepers have already switched. And 96% never want to go back after their 90 night |
| 65,84–70,80 | trial. George is over 80. A widower. Making the bed alone was always a struggle. Now it's easy. |
| 70,80–75,52 | And Sarah. Washing her whole duvet has become a weekly routine. Especially because of her allergies. |
| 75,52–79,92 | Your first night. You feel lighter, fresher, different. After the first week, wash day done |
| 79,92–84,72 | in two hours. After a month, that nagging, I really should change the bedding, is simply gone. |
| 84,72–88,56 | 90 nights to sleep on it. If you're not convinced, you simply get your money back. |
| 88,56–92,32 | Right now it comes with two free Pleen pillowcases. Tap the link below. |

Gleiche Tonspur wie 193234275. Die Transkripte unterscheiden sich nur in der Interpunktion bei 4–8,4 s („Not the cover, the duvet itself.“ statt „Not the cover. The duvet itself.“). Korrekturen wie dort: „For the rest of your life“, „Pleene EasyRest™“.

**Hook (0–3 s), gesehene Frames, Aufbau, Personen, Setting, Emotion, Schnitttempo, Untertitel, Ton, Zahlen und Angebot:** **exakt wie 193234275 bzw. 133366534** (gleiche Datei, siehe oben). Kurzfassung:
- Hook gesprochen: „Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it.“ Eingeblendet: Badge „No more bed changing ❌“ und UT „Sorry, but your duvet is probably the dirtiest thing in your bedroom“.
- Aufbau: Hook 0–4 · Problem 4–18 · Verstärkung 18–31 · Lösung 30,8–36,6 · Mechanismus 36,6–59,8 · Beweis 59,8–75,5 (+ Future Pacing bis 84,7) · Angebot 84,7–92,3 · CTA „Tap the link below.“ 90,6–92,7 + Button „Shop now“.
- Personen: UGC- bzw. Lizenz-Kompilation mit echten Personen (≥ 15 Clips), Off-VO vermutlich männlich (f0 ca. 139 Hz, nicht verifiziert). Setting: diverse Schlafzimmer, Waschküche.
- Avatar: Hygienebewusste, Allergiker, Senioren. **Angle A** (primär) + C + B + E + F-Social-Proof + F-Angebot. Emotion: Ekel und Scham, dann Erleichterung.
- 5,5 Schnitte pro 10 s. Untertitel ja (weiße Box, fette Sans). Off-VO.
- Angebot: „two free Pleene™ Pillow Cases“ + „90 nights … money back“. Der Primärtext ergänzt „(worth £39.99)“.

**Copy-Fit:** Hier passen Primärtext und Video zusammen (Original-Copy von 133366534). Laut s3_funnel.md ist Hygiene auf tb-6 aber nur ein Randthema. Video (Angle A) und Landingpage (C/Social Proof) passen also schlechter zusammen als beim Original auf `/products/easyrest`.
**Varianten-Hinweis:** byte-identisch mit **133366534** (Score 100, seit 2026-08-03) und **193234275** (Octopus-Copy). Copy-Familie: siehe 182988073.

---

##### Hygiene-Zitate Batch 3

Gesammelt sind alle Stellen zu Milben, Bakterien, Schweiß, Waschen, Trocknen oder Temperatur, dazu Allergie und „fresh/Frische“ als verwandte Hygiene-Signale. Quelle: VO = gesprochen (GetHooked-Segment), UT = Untertitel, Text = Texteinblendung ohne Ton, Badge/Grafik/Karte = sonstige Einblendung. **Bakterien kommen in keiner Ad dieses Batches vor.** Temperaturen in °C ebenfalls nicht. Eine Tog-Angabe gibt es nur in 185228767 und 184134597 („10.5“). 193234275 und 193234279 sind dieselbe Datei, die Zitate gelten für beide IDs. Ihre Sekundenangaben bei Badges und Grafiken stammen aus der Szenenliste von Batch 1 (identische Datei 133366534) und wurden an den 5-Sekunden-Frames gegengeprüft.

| Ad-ID | Sek. | Quelle | Zitat (wörtlich) | Kategorie |
|---|---|---|---|---|
| 182988073 | 17,4–20,1 | Text | „Duvet + cover in one, fully washable.“ | Waschen |
| 185228767 | 0,0–3,0 | Text | „One duvet that handles a British winter“ / „10.5 TOG · warm, never sweaty“ | Temperatur/Tog/Schweiß |
| 185228767 | 6,4–10,2 | Text | „Washes whole, fits any / Washing machine, dry in 2 hours“ | Waschen/Trocknen |
| 185228755 | 3,0–7,0 | Text | „The duvet with no cover / Wash the whole thing“ | Waschen |
| 185228755 | 7,0–10,7 | Text | „Dry in 2 hours / Back on the bed“ | Trocknen |
| 184134597 | 17,60–22,48 | VO | „When it needs washing, the whole thing goes into your normal 7kg washing machine, then“ | Waschen |
| 184134597 | ca. 18–21,7 | UT | „WHEN IT NEEDS WASHING“ → „THE WHOLE THING GOES INTO YOUR“ → „NORMAL“ → „7 KILOGRAM WASHING MACHINE“ | Waschen |
| 184134597 | 22,48–25,92 | VO | „the tumble dryer, and it's dry in two hours.“ | Trocknen |
| 184134597 | ca. 22–25 | UT | „THEN THE TUMBLE DRYER AND IT'S“ → „DRY IN TWO HOURS“ | Trocknen |
| 184134597 | 25,92–31,12 | VO | „It's 10.5 tog, so it's every bit as warm as a winter duvet, just without the weight,“ | Temperatur/Tog |
| 184134597 | ca. 26–30 | UT | „IT'S 10.5 TOG“ → „SO IT'S EVERY BIT AS WARM“ → „AS A WINTER DUVET“ → „JUST WITHOUT“ | Temperatur/Tog |
| 184134597 | 31,12–34,60 | VO | „and the breathable fibres mean it never feels stuffy on you.“ | Temperatur |
| 184134597 | ca. 31–34 | UT | „THE WEIGHT AND THE BREATHABLE FIBERS“ → „MEAN IT NEVER FEELS STUFFY ON“ → „YOU“ | Temperatur |
| 184134597 | 34,60–37,96 | VO + UT | „I swear to you, my bed always feels fresh.“ (UT „I SWEAR TO YOU MY BED“ / „ALWAYS FEELS FRESH“) | Frische |
| 193234275 / 193234279 | 0–4 | VO + UT | „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ | Schmutz/Hygiene |
| 193234275 / 193234279 | 4,0–8,4 (UT bei 5 s) | VO + UT | „When did you last actually wash it? Not the cover. The duvet itself.“ | Waschen |
| 193234275 / 193234279 | ca. 5,4–7,3 | Grafik | Kreis-Einschub mit Mikroskopbild länglicher Organismen (soll offenbar Milben zeigen, nicht verifiziert) | Milben (visuell) |
| 193234275 / 193234279 | 8,4–10,8 (UT bei 10 s) | VO + UT | „Most people never do, because it doesn't fit in a normal washing machine.“ | Waschen |
| 193234275 / 193234279 | ca. 8,5–10,8 | Grafik | großes rotes X über der Waschmaschine mit Decke (laut Batch 1) | Waschen (visuell) |
| 193234275 / 193234279 | 10,8–13,4 | VO + UT | „And even if it does, drying takes forever.“ | Trocknen |
| 193234275 / 193234279 | 13,4–16,0 (UT bei 15 s) | VO + UT | „Sweat, dust mites, skin particles. It all builds up,“ | Schweiß/Milben |
| 193234275 / 193234279 | 14,1–16,0 (Frame 15 s) | Grafik | Mikroskop-Kreis (längliche braune Organismen) mit Pfeil auf die Decke | Milben (visuell) |
| 193234275 / 193234279 | 16,0–18,6 | VO + UT | „while you tell yourself that swapping the cover is enough“ | Hygiene (Bezug ≠ Decke) |
| 193234275 / 193234279 | 36,6–39,8 | VO + UT | „And this is wash day. The whole thing goes straight in.“ | Waschen |
| 193234275 / 193234279 | 39,8–42,1 (Frame 40 s) | VO + UT | „It fits in any normal household washing machine.“ | Waschen |
| 193234275 / 193234279 | 40–42 (Frame 40 s) | Badge | „✅ Fits any washing machine“ | Waschen |
| 193234275 / 193234279 | 42,1–44,8 | VO + UT | „The entire duvet. Everything gets washed out.“ | Waschen |
| 193234275 / 193234279 | 43,1–44,8 | Bild | Decke trocknet draußen in der Sonne (laut Batch 1) | Trocknen (visuell) |
| 193234275 / 193234279 | 44,8–47,2 (Frame 45 s) | VO + UT | „And it's dry in two hours. Even without a dryer.“ | Trocknen |
| 193234275 / 193234279 | 45–47 (Frame 45 s) | Badge | „✅ Quick-drying“ | Trocknen |
| 193234275 / 193234279 | 47,2–49,9 | VO + UT | „In the machine in the morning. Fresh on the bed by evening.“ | Waschen/Trocknen |
| 193234275 / 193234279 | 49,9–52,4 (Frame 50 s) | VO + UT | „The breathable fibres adapt to your body temperature.“ | Temperatur |
| 193234275 / 193234279 | 50–52 (Frame 50 s) | Badge | „✅ Temperature-regulating“ | Temperatur |
| 193234275 / 193234279 | 52,4–54,9 | VO + UT | „Cool when it's warm. Warm when it turns cold.“ | Temperatur |
| 193234275 / 193234279 | ca. 53,5–54,9 | Grafik | CGI-Faseranimation orange (warm) / blau (kalt) (laut Batch 1) | Temperatur (visuell) |
| 193234275 / 193234279 | 54,9–57,6 (Frame 55 s) | VO + UT | „No more sweating in summer. No more freezing in winter.“ | Schweiß/Temperatur |
| 193234275 / 193234279 | 57,6–59,8 | VO + UT | „One duvet all year round. Hypoallergenic.“ | Allergie/Temperatur |
| 193234275 / 193234279 | 70,8–75,5 (Frame 75 s) | VO + UT | „And Sarah. Washing her whole duvet has become a weekly routine. Especially because of her allergies.“ | Waschen/Allergie |
| 193234275 / 193234279 | ca. 72–75,7 (Frame 75 s) | Review-Karte | „I'm allergic to dust and pollen, so being able to wash the entire duvet, not just the cover, is exactly what I needed.“ (Sarah — Verified buyer) | Waschen/Allergie |
| 193234275 / 193234279 | 75,5–79,9 | VO | „Your first night. You feel lighter, fresher, different.“ | Frische |
| 193234275 / 193234279 | 79,9–84,7 (Frame 80 s) | VO + UT | „After the first week, wash day done in two hours.“ (UT „After the first week: wash day done in two hours“) | Waschen/Trocknen |
| 193234221 | 0,00–3,76 | VO + UT | „I haven't changed my bed linen in three months and it's never felt fresher.“ (UT ab 3 s: „— and my bed has never felt fresher“) | Frische (impliziter Hygiene-Tabubruch) |
| 193234221 | 12,56–15,12 | VO | „Just put it in the washing machine and then in the tumble dryer.“ | Waschen/Trocknen |
| 193234221 | ca. 11–19 (Frame 15 s) | UT | „Just put it in the washing machine“ → „and then in the tumble dryer“ | Waschen/Trocknen |
| 193234221 | 19,36–22,72 | VO + UT | „And the best thing is the breathable fibres adapt to your body,“ | Temperatur |
| 193234221 | 22,72–25,20 (Frame 25 s) | VO + UT | „nice and warm in the winter, comfortable and cool in the summer.“ (UT „Nice and warm in the winter,“ / „Comfortable and cool in the summer“) | Temperatur |
| 193234221 | 25,20–27,76 | VO + UT | „I swear to you, my bed always feels fresh.“ | Frische |

Nicht im Video, nur im Primärtext (zur Vollständigkeit):
- 182988073 und 193234279: „Wash it, dry it, and lay it back on“, „Pleasantly cool in summer, cosily warm in winter“, „Hypoallergenic and kind to sensitive skin“.
- 185228767 und 185228755: „wash it whole, dry in 2 hours“. 185228767 zusätzlich „ready for the colder nights“.
- 184134597 und 193234275: „Washes whole in your machine at home, dry in 2 hours 🧺“.
- 193234221: „wash it whole, dry in 2 hours“.

---

##### Kurz-Tabelle Batch 3

| ID | Länge | Hook (0–3 s, wörtlich) | Angle | Avatar | Sprecher-Typ | Schnitte/10 s | Emotion |
|---|---|---|---|---|---|---|---|
| 182988073 | 25,1 s | Text: „Best thing I got for years.“ / „NEW: Mint Green“ (kein Ton außer Musik) | C + F-Farbe/Auswahl + F-Angebot (A am Rand) | Design- und farborientierte Käufer, Bettwäsche-Wechsel-Müde | keiner; nur Arme/Hände, KI-generiert (Einschätzung); nur Musik | 3,2 | Neugier/Begehren, Leichtigkeit |
| 185228767 | 15,9 s | Text: „One duvet that handles a British winter“ / „10.5 TOG · warm, never sweaty“ | B + C + A sek. + F-Angebot | UK-Käufer vor dem Winter mit Wärme- bzw. Schwitz-Einwand | keiner; KI-Template-Hand; nur Musik | 1,9 | Beruhigung, dann Dringlichkeit |
| 185228755 | 16,4 s | Text: „This week only: 2 FREE Pillow Cases with every DUVET / Only 26 left in Mint Green“ | F-Angebot + F-Knappheit/Farbe + A sek. | Schnäppchen- und Farbkäufer (Retargeting, nicht verifiziert) | keiner; KI-Template-Hand; nur Musik | 1,8 | Dringlichkeit/FOMO |
| 184134597 | 47,3 s | VO: „I bloody hate changing the bed, not the sheets, that bit, …“ · UT: „I BLOODY HATE CHANGING THE BED“ / „NOT THE SHEETS THAT BIT“ | C + B + A sek. + F-Angebot (30 %) | UK-Frauen ca. 35–65, genervt vom Beziehen | Off-VO vermutlich weiblich (f0 ca. 193 Hz, nicht verifiziert); KI-POV-Visuals (Einschätzung); keine Musik | 2,3 (visuell; Detektor 0,4) | Frust → Erleichterung |
| 193234275 | 92,7 s | VO + UT: „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ · Badge „No more bed changing ❌“ | A + C + B + E + F-Social-Proof + F-Angebot (Copy: C + 30 %) | Hygienebewusste 30–65, Allergiker, Senioren | Off-VO vermutlich männlich (f0 ca. 139 Hz); echte UGC-/Lizenz-Clips | 5,5 | Ekel/Scham → Frust → Erleichterung |
| 193234221 | 47,0 s | VO: „I haven't changed my bed linen in three months and it's never felt fresher.“ · UT: „I haven't changed my bed linen in three months“ | C + B + F-Farbauswahl + F-Angebot | Pragmatiker ca. 25–45 (v. a. Männer), Komfort-Suchende | echter UGC-Creator (Mann ca. 30–40), O-Ton/VO, leises Musikbett (Einschätzung) | 1,5 | Neugier/Irritation → Erleichterung |
| 193234279 | 92,7 s | wie 193234275 (gleiche Datei) | A + C + B + E + F-Social-Proof + F-Angebot | wie 193234275 | wie 193234275 | 5,5 | wie 193234275 |

---

##### Prüfung der Pflichtliste (Batch 3)

| Pflichtfeld | 182988073 | 185228767 | 185228755 | 184134597 | 193234275 | 193234221 | 193234279 |
|---|---|---|---|---|---|---|---|
| get_ad + Transkriptionsstatus | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Transkript vollständig oder begründeter Vermerk | ✔ Vermerk „no_speech“, Audio-Check = nur Musik | ✔ Platzhalter, Audio-Check = nur Musik | ✔ Platzhalter, Audio-Check = nur Musik | ✔ 11 Segmente + lokale Gegenprobe | ✔ 20 Segmente | ✔ 12 Segmente | ✔ 20 Segmente |
| ElevenLabs nötig? | nein | nein | nein | nein | nein | nein | nein |
| Video geladen + ffprobe | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Schnitte gesamt und pro 10 s | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Frames 0/1/2/3/alle ~5 s angesehen | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ (md5-gleich mit 193234275) |
| Hook gesprochen + eingeblendet | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Aufbau mit Sekunden, fehlende Teile markiert | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Personen/Sprecher, echt/KI/Stock mit Begründung | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Setting | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Avatar + Angle-Code | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Haupt-Emotion | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Schnitttempo / Untertitel / Ton | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Zahlen/Behauptungen wörtlich | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Angebotspräsentation | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Varianten-Hinweis | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Metadaten (Meta-ID, Start, Tage, Score, used_count, LP, share_url, Ad Library) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ (Score n/a, inaktiv) | ✔ |

Offen bzw. nicht verifiziert:
- Ob die Stimmen in 184134597, 193234275 und 193234279 KI-generiert sind.
- Das Geschlecht der Sprecher (nur f0-Indiz).
- Ob unter dem VO von 193234275 und 193234279 ein Musikbett liegt.
- Die visuelle Identität der Geschwister-Ads 182988108, 182988111, 184134616, 184134607, 185228772, 193234216, 193234218, 177443532 und 200490701 (nur über Transkript bzw. Länge abgeleitet).
- Die Herkunft der UGC-Clips.

Arbeitsdateien:
- Skripte: `wf/s2b3_scripts/`
- Rohdaten: `wf/s2b3_meta/`
- Audio und Spektrogramme: `wf/s2b3_audio/`
- Kontaktbögen: `wf/s2b3_sheets/`
- Frames: `wf/frames/<id>/`
- Videos: `wf/vid/<id>.mp4`


## Teil 3 – Funnel und Landingpages

Stand: 2026-10-08. Quellen: Live-Abrufe von pleene.com und pleene.uk (curl und Playwright/Chromium, mobil 390×844 und Desktop 1440×900, Locale en-GB, Cookies `localization=GB` und `cart_currency=GBP`; für die US-Seite zusätzlich `localization=US` und `cart_currency=USD`), Shopify-Produkt-JSON (`/products/<handle>.js`), Policy-Seiten, Klaviyo-Formular-JSON, Elevate-A/B-Konfiguration im Seitenquelltext sowie GetHooked (get_shop_landing_pages, search_ads mit `countries`, get_shop, get_ad_technologies). Die Bewertungsdaten stammen aus `wf/reviews_all.json` (Agent 4). Es wurde nichts gekauft. Bis zur Warenkorbseite wurde getestet, Checkout-Requests wurden im Browser blockiert, und in kein Checkout-Formular wurden Daten eingegeben. Texte von Seiten und Ads sind wörtlich auf Englisch zitiert, die Analyse ist auf Deutsch.

---

### 3.0 Zusammenfassung

1. **Vier Landingpages, alle auf pleene.com.** Keine einzige aktive Ad verlinkt auf pleene.uk. Die 137 Ads aus dem Inventar verteilen sich so:

   | Landingpage | Ads | davon Land laut GetHooked |
   |---|---|---|
   | `/products/easyrest` | 83 | 52 GB, 31 ohne Länderdaten |
   | `/products/easyrest-comforter` | 40 | 37 US, 3 ohne |
   | `/pages/tb-6` | 8 | 7 GB, 1 ohne |
   | `/products/easyrest-duvet` | 6 | 4 GB, 2 ohne |

   GetHooked (`get_shop_landing_pages`, shop 47758, Publikation vom 05.10.) zählt 70 / 32 / 10 / 8 = 120 Ads. Shop 47737 (pleene.uk) hat genau 1 Ad, und auch die zeigt auf `pleene.com/products/easyrest`. `search_ads` meldet am 08.10. bereits 153 aktive Ads. Darunter sind 20 neue vom 07.10.: 13 davon GB auf `/products/easyrest`, 7 davon US auf `/products/easyrest-comforter`.

2. **Wichtigste Korrektur zur Ausgangsannahme:** Die Comforter-Seite ist **die US/CA-Produktseite** (Zoll-Größen, °F, „comforter", „top sheet", „laundromat", „Value: $39.99"). Die 40 Ads, die dorthin führen, sind laut GetHooked-Feld `countries` **US-Ads** und keine GB-Ads. Im Quelltext steht dazu ein Elevate-A/B-Test mit dem Namen "Duvet UK PDP Weiterleitung an USCA PDP" (`isLive: true`). Er soll US/CA-Besucher von `/products/easyrest` auf `/products/easyrest-comforter` umleiten. In unserem Headless-Test mit US-IP hat diese Weiterleitung nicht ausgelöst. Die Wirkung ist deshalb nicht verifiziert.

3. **Der GB-Funnel besteht aus drei Seiten.**
   - Die Produktseite `/products/easyrest` ist um Angle **B (Wärme/Tog)** gebaut: "10.5 TOG — proper winter warmth".
   - `/products/easyrest-duvet` ist ein fast identischer Klon davon. Das Produkt ist versteckt (Tags `hidden-search`), wurde am 09.09.2026 angelegt und hat die eigene Vorlage `easyrest-duvet-winter26-2`. Alle 6 Ads dorthin sind Tog-/Winter-Ads.
   - Das Advertorial `/pages/tb-6` ist ein Pre-Lander für Angle **C (Bezug/Beziehen)** und **F-Social-Proof**. Alle CTAs führen auf `/products/easyrest`.

4. **Angebot UK:**
   - Preise von £74.99 (Narrow 90×200) bis £129.99 (Super King 260×220), Vergleichspreise £114.99–£169.99 ("SAVE 23–35 %").
   - Mengenstaffel über die App Kaching: 2 Stück −10 % "Couple-Bundle" (vorausgewählt), 3 Stück −15 % "Family-Bundle".
   - Gratis sollen 2 Kissenbezüge je Decke dazukommen ("Value: £39.99"). In der Kaching-Konfiguration ist dafür aber `freeGifts: []` hinterlegt, und im Warenkorb erscheinen keine Kissenbezüge als Position. Ob sie tatsächlich mitgeliefert werden, ist nicht verifiziert.
   - **Kein Countdown** auf irgendeiner Seite. Die einzige Knappheitsangabe ist der statische Text "Ready to Ship – Limited Stock" (fest im HTML, für jede Größe und Farbe gleich) sowie auf tb-6 "while stocks last".

5. **Preiswelten:**
   - Die Basiswährung des Shops ist GBP (`Shopify.currency rate 1.0`).
   - UK-Besucher sehen auf pleene.com wie auf pleene.uk dieselben GBP-Preise. Es ist derselbe Shopify-Shop `sq48au-70.myshopify.com`, und der Text ist identisch.
   - Der US-Markt hat eigene, deutlich höhere Festpreise. Beispiele: Duvet Narrow $109.99 statt £74.99. Comforter Single $139.99, in der GBP-Ansicht £69.99.
   - Ein Browser mit US-IP wird von pleene.uk auf pleene.com mit USD umgeleitet (`?shpxid=`). Ob ein GB-Besucher von pleene.com auf pleene.uk umgeleitet wird, ist mangels GB-IP nicht verifiziert.

6. **Warenkorb (Cart-Drawer):**
   - Fortschrittsbalken bis zum Gratisversand ab £100.
   - "↓ ADD ONE-TIME CART DEALS 🛒" mit drei Upsells, standardmäßig aus: Pillow-Cases £19.99, Pillow £39.99, FluffBalls £14.99.
   - "Package Protection (Recommended)" für £2.99, standardmäßig aus.
   - Die /cart-Seite cross-sellt zusätzlich ein **"180-Day Return Policy – Upgrade" für £2.99**, einen digitalen Service, der das Rückgabefenster verlängert.
   - Auf der US-Seite sind die Upsells andere: ZipLift™ Mattress Lifter, FluffBalls, Package Protection.

7. **Garantie:**
   - Werbeversprechen: "90-Night Free Trial. Money back, no questions asked." (Galeriebild).
   - Die Policy sagt etwas anderes: 90 Tage ab Lieferung, **Rücksendekosten trägt der Kunde**, die ursprünglichen Versandkosten werden nicht erstattet, und man soll zuerst den Support kontaktieren.
   - Versand UK: £4.95 unter £100, ab £100 gratis, "Priority Handling" £7.95, Lieferung in 5–8 Werktagen.

8. **Bewertungen:**
   - Judge.me zeigt "4.8 · 172 reviews" auf allen drei Produktseiten. Auf der Comforter-Seite sind das Bewertungen des Duvet-Produkts (171 von 172 gehören zum Duvet).
   - 154 von 172 Judge.me-Texten sind textgleich mit Trustpilot-Bewertungen, also Importe. Nur 4 tragen "verified buyer".
   - tb-6 nennt "Excellent 4.7/5 · 250 reviews on Trustpilot". Agent 4 hat am 08.10. 291 Trustpilot-Bewertungen erfasst.
   - Die "✓ Verified"-Testimonial-Karten der Produktseiten (Margaret 67, James 55 usw.) und die Galerie-Zitate (Robert 61, Susan 62) **kommen in keiner der 463 erfassten Bewertungen vor**. Ihre Herkunft ist nicht verifiziert.
   - "Robert, 61" sagt auf der UK-Seite etwas völlig anderes als auf der US-Seite. In der US-Version sagt er "I've had the comforter for a year", obwohl das Comforter-Produkt erst am 25.06.2026 angelegt wurde und laut About-Seite "Founded 2026" gilt.

9. **Widersprüche in den Produktaussagen** (Details in 3.5 bis 3.8):
   - Waschmaschine: Das Bullet sagt "Fits in every washing machine", die eigene Größentabelle verlangt dagegen eine Trommel ab 6–8 kg.
   - Trocknen: "about 2 hours" gegenüber "2–3 hours".
   - Wärme: Die Produktseite sagt "10.5 TOG — proper winter warmth", die Home-Page sagt "mid-weight, all-season duvet".
   - Kundenzahl: "Over 10,000 customers" auf der Produktseite gegenüber "7,000+" auf tb-6.
   - Farben: "Six colourways" auf der Home-Page, aber 10 Farben im Shop.

10. **Technik:**
    - Shopify-Theme "Shrine PRO" 1.8.0 (Theme-Name "working of shrine-theme-pro").
    - Apps: Kaching Bundles, Judge.me, Elevate A/B Testing, HeyMerch Sales Stock Counter, Klaviyo, ParcelPanel, Zigpoll, Lucky Orange, Triple Whale, Google Ads Pixel by Nabu.
    - Meta Pixel 2174873679968281, Google Ads AW-18246939242.
    - Kein TikTok-Pixel gefunden.
    - Interne Namen sind auf Deutsch ("Weiterleitung", "AKTUELL", Canva-Datei "Design_ohne_Titel", Bild "…_Kopie.png"). Das ist ein Indiz für deutschsprachige Betreiber (nicht verifiziert).
    - Impressum: One Way Ecom Limited, Hongkong, Telefon +1 (205). Laut Footer betreut 21Commerce Limited die Werbung.

---

### 3.1 Vergleichstabelle der Landingpages

| Merkmal | `/products/easyrest` | `/products/easyrest-comforter` | `/pages/tb-6` | `/products/easyrest-duvet` |
|---|---|---|---|---|
| Ads (Inventar 137) | 83 | 40 | 8 | 6 |
| Ads (GetHooked-Publikation 05.10., 120) | 70 | 32 | 8 | 10 |
| Zielland der Ads (GetHooked `countries`) | GB (52), ohne Angabe (31) | **US** (37), ohne Angabe (3) | GB (7), ohne (1) | GB (4), ohne (2) |
| Typ | Produktseite (Long-Form-PDP mit Sales-Sections) | Produktseite, **US-lokalisiert** | **Advertorial**, als "ADVERTISEMENT" markiert, Pre-Lander mit nummerierten Benefit-Karten (01–05) und Vergleichstabelle | Produktseite (Klon von `/products/easyrest`) |
| Shopify-Template | `product.easyrest-duvet-winter26` | `product.easyrest-duvet-usa230926` | `page.tabeasyrest-tb6` | `product.easyrest-duvet-winter26-2` |
| Shop-Header/Navigation | ja | ja | **nein** (eigenständige Seite ohne Menü) | ja |
| Haupt-Angle | **B** (Tog/Winterwärme) | **A + B** (ganz waschbar/hygienisch, "One comforter, every season", Schwitzen) | **C** (nie wieder Bezug aufziehen) + **F-Social-Proof** | **B** (identisch mit easyrest) |
| Neben-Angles | C, A, F-Angebot, F-Social-Proof, E (Testimonial "Margaret, 67") | C ("skip the top sheet"), E ("Margaret, 67"), F-Angebot | A (Hygiene-Vergleich), F-Angebot ("Autumn offer") | wie easyrest |
| H1 | "Pleene EasyRest™ Duvet" | "Pleene EasyRest™ Comforter" | "How 7,000+ people said goodbye to putting duvet covers on – with a machine-washable 2-in-1 duvet" | "Pleene EasyRest™ Duvet" |
| ATF-Bullets | "10.5 TOG — proper winter warmth" / "Warm without overheating" / "Never change bedding again" / "Fits in every washing machine" | "Warm in winter, cool in summer" / "No cover to change" / "Hygienic & allergy-friendly" / "Fits in any washing machine" | "No more putting covers on" / "Not too warm, not too cold" / "Fits any washing machine" / "Dry in about 2 hours" | wie easyrest |
| Wärmeangabe | 10.5 TOG | "300 GSM fill", kein Tog | "climate fibres", kein Tog | 10.5 TOG |
| Einstiegspreis | £74.99 (statt £114.99) | GBP-Ansicht £69.99 (statt £119.99); USD-Ansicht $139.99 (statt $199.99) | keine Preise auf der Seite | £74.99 (statt £114.99) |
| Bundles | Kaching 1 / 2 (−10 %) / 3 (−15 %) | gleich | keine (Link zur PDP) | gleich |
| Gratisbeigabe | "2 Pleene™ Pillow Cases (Value: £39.99)" | "2 Pleene™ Pillowcases (Value: $39.99)", auch in der GBP-Ansicht | "2 matching pillowcases free … Worth £39.99 – while stocks last." | wie easyrest |
| Social-Proof-Zahl | "Over 10,000 customers" | "Over 10,000 customers" | "7,000+ customers" | "Over 10,000 customers" |
| Bewertungsanzeige | Judge.me ★ "172 reviews", Widget "4.8" | Judge.me "172 reviews" (Bewertungen des Duvet) | Trustpilot "Excellent 4.7/5 · 250 reviews" | Judge.me "172 reviews" (als "Review for Pleene EasyRest™ Duvet" verknüpft) |
| Testimonial-Videos | ja ("Peter", "Brian", "Dave") | nein | nein | ja |
| Cross-Sell-Sektion auf der Seite | "The Cosy Bundle" (+ CosyRest™ Sherpa Throw) | "The Full Sleep Set:" (+ ZipSheet™ US + EasyStore™) und "You may also like" | – | "The Cosy Bundle" |
| Laufband oben | 3 rotierende Texte (s. u.) | keines | "ADVERTISEMENT" | keines |
| E-Mail-Pop-up | ja (sofort und bei Exit-Intent) | ja | **nein** (URL-Muster `*tb*` ausgeschlossen) | ja |
| pleene.uk-Entsprechung | Text identisch (gleicher Shop) | identisch | identisch | identisch |

**Wo sich die Seiten genau unterscheiden:**

- **easyrest gegenüber easyrest-duvet:**
  - Nur `/products/easyrest` hat das rotierende Laufband (Section `custom_liquid_ge9Xt4`).
  - Das Duvet-Produkt ist ein separates, verstecktes Produkt (ID 16081090838860) mit eigener Vorlage `…-winter26-2`.
  - Sein Bewertungs-Widget kennzeichnet die Bewertungen als "Review for Pleene EasyRest™ Duvet", sie werden also vom Hauptprodukt übernommen.
  - Bei der Farbe Lavender Mist unterscheiden sich die Vergleichspreise (s. 3.4).
  - Alle Texte, FAQs, Sections und die Bildgalerie sind sonst identisch (Textvergleich der vollständigen Seiten ohne weitere Unterschiede).
  - Wahrscheinlich dient die Seite als separater Test- oder Kampagnen-Endpunkt für die Tog-Ads. Das ist nicht verifiziert.
- **easyrest gegenüber comforter:**
  - Komplett anderes Copy-Set für den US-Markt: "comforter", Zoll-Größen, °F, "top sheet", "laundromat".
  - Andere Galerie (eigene "Comforter"-Bilder).
  - Keine Tog-Angabe.
  - FAQ mit Größentabelle als **unausgefülltem Platzhalter** ("Twin __ × __ in").
  - Andere Cross-Sells.
- **tb-6 gegenüber den Produktseiten:**
  - Keine Preise, keine Variantenauswahl, kein Warenkorb.
  - Stattdessen Story-Hook, "AS FEATURED IN"-Logos, Vergleichstabelle, Trustpilot-Zitate und ein Angebotskasten "Autumn offer".
  - 5 CTAs, alle auf `https://pleene.com/products/easyrest`.

---

### 3.2 Preiswelten GBP und USD

**Was UK-Besucher sehen:**

- Bei curl ohne Cookie liefern pleene.com und pleene.uk `Shopify.country = "GB"` und `Shopify.currency = {"active":"GBP","rate":"1.0"}` und setzen die Cookies `localization=GB` und `cart_currency=GBP`.
- Ein frischer Browser über den Proxy (US-IP) bekommt dagegen auf pleene.com `USD rate 1.3465326`. pleene.uk leitet ihn per JavaScript auf `pleene.com/products/easyrest?shpxid=…` in USD um. Das ist die Markt- bzw. Geo-Weiterleitung von Shopify.
- Mit dem Cookie `localization=GB` zeigt pleene.com GBP. Ein UK-Besucher sieht also GBP.
- Ob pleene.com GB-IPs auf pleene.uk umleitet, ist nicht verifiziert, da keine GB-IP verfügbar war. Für den Preis spielt das keine Rolle, weil beide Domains denselben Shop und dieselben GBP-Preise ausliefern.

**`/products/easyrest` und `/products/easyrest-duvet`, GBP** (Kaching-Bundle-Preise mit Playwright je Größe ausgelesen):

| Größe | 1 Stück | Vergleichspreis | 2er "Couple-Bundle" −10 % | Vergleich | 3er "Family-Bundle" −15 % | Vergleich |
|---|---|---|---|---|---|---|
| 90 × 200 cm (Narrow) | £74.99 | £114.99 | £135.00 | £229.98 | £191.25 | £344.97 |
| 140 × 200 cm (Single) | £79.99 | £119.99 | £144.00 | £239.98 | £204.00 | £359.97 |
| 160 × 210 cm (Single XL) | £84.99 | £129.99 | £153.00 | £259.98 | £216.75 | £389.97 |
| 200 × 200 cm (Double) | £89.99 | £139.99 | £162.00 | £279.98 | £229.50 | £419.97 |
| 230 × 230 cm (King) | £119.99 | £159.99 | £216.00 | £319.98 | £306.00 | £479.97 |
| 260 × 220 cm (Super King) | £129.99 | £169.99 | £234.00 | £339.98 | £331.50 | £509.97 |

- Das Badge zeigt je nach Größe "SAVE 34 %", "33 %", "34 %", "35 %", "25 %" oder "23 %".
- **Lavender Mist** hat auf `/products/easyrest` keinen Vergleichspreis. Es gibt dann kein Streichpreis- und kein SAVE-Badge, und der Kaching-Balken zeigt "You're saving £0.00".
- Auf `/products/easyrest-duvet` hat Lavender Mist für alle Größen den Vergleichspreis £114.99. Bei King (£119.99) und Super King (£129.99) liegt der Vergleichspreis damit **unter** dem Verkaufspreis. Das ist ein Datenfehler.
- Alle 60 Varianten sind verfügbar (`available: true`).

**USD-Preise derselben Seite** (US-Preisliste, `/products/easyrest.js` mit USD; US-Besucher sollen laut Elevate-Konfiguration eigentlich auf die Comforter-Seite umgeleitet werden):

| Größe | Preis | Vergleichspreis |
|---|---|---|
| Narrow | $109.99 | $149.99 |
| Single | $119.99 | $159.99 |
| Single XL | $129.99 | $169.99 |
| Double | $149.99 | $199.99 |
| King | $179.99 | $229.99 |
| Super King | $194.99 | $244.99 |

Das sind Festpreise und keine Umrechnung: £74.99 × 1.3465 = $100.97, verlangt werden $109.99.

**`/products/easyrest-comforter`, beide Preiswelten:**

| Größe | GBP 1 Stück (Vergleich) | GBP 2er | GBP 3er | **USD 1 Stück (Vergleich)** | **USD 2er (Vergleich)** | **USD 3er (Vergleich)** |
|---|---|---|---|---|---|---|
| Single (55 × 79 in) | £69.99 (£119.99) | £126.00 (£239.98) | £178.50 (£359.97) | $139.99 ($199.99) | $252.00 ($399.98) | $357.00 ($599.97) |
| Twin (63 × 83 in) | £74.99 (£129.99) | £135.00 (£259.98) | £191.25 (£389.97) | $159.99 ($219.99) | $288.00 ($439.98) | $408.00 ($659.97) |
| Full (79 × 79 in) | £79.99 (£139.99) | £144.00 (£279.98) | £204.00 (£419.97) | $169.99 ($229.99) | $306.00 ($459.98) | $433.50 ($689.97) |
| Queen (91 × 91 in) | £109.99 (£169.99) | £198.00 (£339.98) | £280.50 (£509.97) | $199.99 ($259.99) | $360.00 ($519.98) | $510.00 ($779.97) |
| King (102 × 86 in) | £119.99 (Vergleich = Preis, kein Rabatt) | £216.00 (£239.98) | £306.00 (£359.97) | $219.99 ($279.99) | $396.00 ($559.98) | $561.00 ($839.97) |

- In der GBP-Ansicht hat Comforter King keinen Rabatt, da der Vergleichspreis dem Preis entspricht. Lavender Mist hat in den Größen Single bis Queen keinen Vergleichspreis.
- Die Zielgruppe dieser Seite (US-Ads) sieht die USD-Spalte. Die GBP-Werte zeigen nur, was ein UK-Besucher dort sehen würde.

---

### 3.3 Seite 1: `pleene.com/products/easyrest` (83 Ads, GB) — Produktseite

**Above the Fold, mobil** (Screenshot `render/com_products_easyrest_mobile_atf_clean.png`):

- Header: Burger-Menü, Logo "Pleene.", UK-Flagge, Suche, Warenkorb.
- Braunes Laufband mit drei Slides, die alle 3,5 s rotieren (aus dem HTML): "Cosy Season Is Here — **Sleep Warm All Winter**" / "Free Shipping On Orders Over £100" / "90 Nights Risk-Free — Try It In Your Own Bed".
- Hauptbild: blaue EasyRest™-Decke ("Coastal Blue") von oben auf einem Doppelbett mit zwei Kissen und Holz-Nachttischen. Das Bild ist KI-typisch glatt; der Dateiname `hf_20260914_…` deutet auf Higgsfield-Generierung hin (nicht verifiziert).
- Darunter 17 Galerie-Thumbnails.
- H1 "Pleene EasyRest™ Duvet", fünf gelbe Sterne, "172 reviews".
- Preis "£74.99 ~~£114.99~~", Badge "SAVE 34%".
- Bullets: "✔️ **10.5 TOG — proper winter warmth**", "✔️ Warm without overheating", "✔️ Never change bedding again", "✔️ Fits in every washing machine".
- Am Fold-Rand beginnt der blaue Badge-Kasten "🎁 Free with every duvet today".
- **Pop-up:** Bereits nach 4 s liegt das Klaviyo-Pop-up über der Seite (Screenshot `render/com_products_easyrest_mobile_atf_t4.png`). Motiv: ein lachendes Senioren-Paar, das gefaltete Decken in Mint und Blau hält. Text: "Win a free Duvet" / "One subscriber wins a duvet of their choice every month. Any size, any colour." / "Your email address" / Button "Enter the giveaway".

**Above the Fold, Desktop** (`render/com_products_easyrest_desktop_atf_clean.png`):

- Navigation: "Home", "EasyRest™ Duvet" (hervorgehoben), "All Products", "Track Your Order", "About Us", "Contact", dazu der Länderwähler "United Kingdom | GBP £", Login und Warenkorb.
- Laufband.
- Links das Galerie-Bild, rechts H1, Sterne, Preis, Bullets und der Geschenk-Kasten "🎁 Free with every duvet today / 2 Pleene™ Pillow Cases **(Value: £39.99)**".
- Darunter "STOCK UP & SAVE" mit drei Kaching-Balken:
  - "Buy 1, Get 2 Pillow Cases FREE / You're saving £40.00 / £74.99 ~~£114.99~~"
  - **vorausgewählt** "Couple-Bundle" "Buy 2, Get 4 Pillow Cases FREE" "10% OFF" "You're saving £94.98" "£135.00 ~~£229.98~~", mit zwei Farb- und Größen-Dropdowns
  - "Family-Bundle" "Buy 3, Get 6 Pillow Cases FREE" "15% OFF" "£191.25"
- Badges: "SAVE 34%", "Couple-Bundle", "Family-Bundle", "10% OFF", "15% OFF". Unter dem Fold folgen "Ready to Ship – Limited Stock" mit grünem Punkt und die Zahlungs-Icons Mastercard, Visa, PayPal, Amex, Apple Pay, Google Pay und Klarna.

**Seitenaufbau, Abschnitt für Abschnitt** (Überschriften wörtlich):

1. Header und Laufband (siehe oben).
2. Hauptbereich:
   - Galerie mit 17 Bildern. Bildtexte, die gelesen werden konnten:
     - "90 Night Free Trial / FREE today: 2x EasyRest™ Pillowcases / Value £39.99"
     - "Duvet + Cover in one. / Completely washable." mit "Dries indoors in hours", "Wash as often as your sheets", "Fits a standard washing machine"
     - "10.5 TOG. Built for British winters. / Pleene™ Microfibre Technology" mit "The standard UK winter weight", "Warmth without the weight", "Never clammy, never cold"
     - Testimonial-Bild "Robert, 61: "I nearly didn't order this. A whole duvet in the washing machine? And it felt so light I thought I'd freeze in winter. Wrong on both. Fits my 7kg machine easily, and we've had frost all week without me needing the spare blanket. Should have bought it years ago."" mit dem Zusatz "10,000+ people enjoy sleeping with the Pleene™ Duvet"
     - "Susan, 62: „I'm always the cold one in our house, but under some duvets I'd still wake up boiling at 3am. With this one, neither happens. Not cold, not sweating. No idea how it does that, but it does. Couldn't recommend it more.😍""
     - Collage "10,000+ people already sleep with the Pleene™ Duvet. / 90-Night Free Trial. Money back, no questions asked."
     - dazu Farbbilder
   - H1, Preis, Bullets, Geschenk-Kasten, "STOCK UP & SAVE" (Kaching).
   - "What size do I need?" öffnet die Größentabelle mit "Sizing Chart" / "Between two sizes? Go bigger — especially if you share a bed or move a lot in your sleep." und zwei Tabellenbildern (s. u.).
   - "Ready to Ship – Limited Stock", "ADD TO CART", Zahlungs-Icons.
   - 4 Akkordeons: "What is the TOG rating?" / "How do I wash and dry the Pleene™ duvet?" / "Does the Pleene™ duvet fit in my washing machine?" / "It looks thin — is it really warm enough?"
3. "★★★★★ **Real customers, real results**" / "Tap a clip to hear what they have to say": drei Hochkant-UGC-Videos mit den Namen "Peter", "Brian" und "Dave" (101 s, 42 s, 53 s). Auf den Standbildern sind ältere Männer in britischen Wohnungen zu sehen, einer sitzt auf einer hellblauen EasyRest. Ton nicht transkribiert, siehe 3.13.
4. "**10.5 TOG. Built for cold nights.**" / "On the UK scale, 10.5 TOG is the standard winter weight — what most households sleep under from autumn through to spring." / "10.5 TOG / Full winter warmth, in a duvet that still goes in your washing machine." / "✓ Warm in winter, cool in summer" "✓ Temperature regulating, all year round" "✓ Not sure? 90 nights to change your mind"
5. "**Feels weightless. Sleeps warm.**" / "No heavy duvet pressing down on your chest. The EasyRest™ rests lightly on you and still carries a full 10.5 TOG of winter warmth." / "That's because warmth comes from the air held between the fibres, not from weight. You get the heat without the load — and it still fits in your washing machine." / "✓ All the warmth, none of the weight" "✓ Temperature regulating — warm, never clammy"
6. "**Never make the bed the hard way again**" / "No more duvet covers. No more wrestling. No more effort." / "We know how frustrating it is to fight with a separate cover every time — especially on a cold morning." / "The Pleene EasyRest™ combines duvet and cover in one." / "✓ No separate cover needed" "✓ A fresh bed in seconds"
7. "**Washable like bed linen**" / "The Pleene EasyRest™ fits in any normal washing machine." / "Winter bedding usually goes months without a proper wash, because the duvet itself never goes in. Only the cover does." / "With Pleene EasyRest™, everything goes in. One wash. All clean." / "Air dries in 2 hours — or even faster in the dryer."
8. "★★★★★ Over 10,000 customers now sleep more comfortably with Pleene EasyRest™" / "**Try Pleene EasyRest™ 90 nights risk-free**", dazu 5 Karten mit "✓ Verified":
   - "Margaret, 67": "At my age, wrestling a duvet into its cover was such a struggle. This is an absolute godsend — I can make my bed on my own again."
   - "James, 55": "Looks far too thin to work in January. It absolutely does — not once been cold."
   - "Sarah, 41": "Changing the bed used to be my most dreaded chore. Now the whole thing just goes in the wash — honestly a game changer."
   - "Robert, 50": "Straight in the machine and done. This is how bedding should be."
   - "David, 58": "My wife runs cold and I run hot. First winter duvet we've agreed on in years."
   - Keines dieser Zitate kommt in den 291 Trustpilot- oder 172 Judge.me-Bewertungen vor. Das "Verified" ist nicht verifizierbar.
9. "**Frequently Asked Questions**": 8 Fragen, wörtlich unten.
10. "**The Cosy Bundle**" / "The EasyRest™ keeps you warm at 10.5 TOG. The CosyRest™ throw goes over the top for the nights when that isn't quite enough — and lives on the sofa the rest of the time. Your whole winter bed, in one order." Angeboten werden EasyRest £74.99 ~~£114.99~~ und "Pleene CosyRest™ — Reversible Sherpa Throw" £59.99 ~~£77.99~~, "Total Price: £134.98 ~~£192.98~~", "Add selected to cart". Einen Extra-Rabatt auf das Bundle gibt es nicht.
11. "Customer Reviews" (Judge.me): "4.8", "172 reviews", "Write a review", Sortierung, 35 Seiten.
12. Newsletter: "**Join the hassle-free bedding movement**" / "Early access, restock alerts and the occasional bed-making tip you'll actually use."
13. Footer: "The #1 for Hassle-Free Bedding" / "Pleene is more than just an online shop — it's a movement to free people from the endless struggle of changing bed linen, through clever, high-quality bedding." Darunter das Impressum (One Way Ecom Limited, Hongkong, "Tel.: +1 (205) 360-5811", "pleene.com is operated by One Way Ecom Limited. Advertising for this store is managed on our behalf by 21Commerce Limited, registered at the same address.") und die Länderwahl "United Kingdom (GBP £)".

**Akkordeons im Hauptbereich (wörtlich):**

- "What is the TOG rating?" — "10.5 TOG — the standard UK winter weight, warmer than the 9.0 TOG duvets sold as year-round."
- "How do I wash and dry the Pleene™ duvet?" — "Yes, the Pleene™ duvet is fully washable and can be cleaned easily in your washing machine. We recommend washing it at 40°C on a spin cycle of around 800 rpm. / Pleene™ is designed to absorb far less sweat and dirt than traditional bedding, so 40°C is perfectly sufficient for everyday washing while protecting the material and extending its lifespan. / If you ever want a deeper clean, you can occasionally wash it at 60°C. After washing, you can dry the Pleene™ duvet in the dryer or let it air dry. Air-dried, it is usually completely dry in about 2 hours."
- "Does the Pleene™ duvet fit in my washing machine?" — "Yes — a normal household machine is enough. A feather-filled king duvet weighs 4–6 kg and fills the whole drum. Ours weighs 3.12 kg and compresses flat instead."
- "It looks thin — is it really warm enough?" — "Warmth comes from air trapped between the fibres, not from bulk. A heavier fill would only stop it fitting in your washing machine."

**FAQ "Frequently Asked Questions" (wörtlich, Frage und Antwort):**

1. "What is the TOG rating?" — "10.5 TOG. On the UK scale that is the standard winter and all-year weight — warmer than the 9.0 TOG duvets commonly sold as year-round, and the rating most households sleep under from autumn through to spring. Only the coldest unheated bedrooms call for more."
2. "Is it warm in winter and cool in summer?" — "Yes. At 10.5 TOG it carries the standard UK winter rating, so it holds your body heat through the coldest months. The microfibre is temperature regulating: it lets moisture and excess heat escape instead of trapping them, so it stays comfortable as the seasons turn rather than leaving you clammy."
3. "It looks thin. How can it be that warm?" — "Thickness and warmth are not the same thing. What insulates you is the air trapped between the fibres, not the bulk of the filling — the same reason a thin technical jacket beats a heavy wool coat. Our fill is engineered to hold that air, which is how it reaches 10.5 TOG while staying light enough to wash at home."
4. "What if I am still cold?" — "Sleep under it for 90 nights. If it is not warm enough for you, send it back for a full refund — no explanation needed. Return postage is paid by the customer and we ask that it comes back clean and resaleable. This sits alongside your statutory rights, not instead of them."
5. "Why is the Pleene EasyRest™ more hygienic than a normal duvet?" — "With the Pleene EasyRest™, you can wash the entire duvet — not just a cover. With traditional duvets, usually only the cover is washed while the duvet itself is rarely cleaned, so over time sweat, dust and allergens can build up. With Pleene EasyRest™, your bed stays regularly fresh and hygienically clean."
6. "What is the Pleene EasyRest™ made of?" — "Soft, breathable microfibre with a lightweight high-loft fill. It feels gentle against the skin, holds its warmth, and is free from feathers and down — making it suitable for allergy sufferers."
7. "Is it suitable for allergy sufferers?" — "Yes. Because you can wash the whole duvet regularly and it contains no feathers or down, it is well suited to allergy sufferers. Regular washing helps keep dust and allergens to a minimum."
8. "Do I really not need a duvet cover anymore?" — "That's right. The Pleene EasyRest™ is a duvet and cover in one, so there is no separate cover to put on or take off. You simply wash the whole thing and lay it back on the bed — that's it."

**Welche Einwände beantwortet werden:**

- zu dünn bzw. nicht warm genug (5 von 12 Fragen inklusive Akkordeons)
- Waschen und Trocknen
- passt es in die Waschmaschine
- Hygiene
- Material und Allergie
- braucht man noch einen Bezug
- Rückgabe, falls zu kalt

Nicht beantwortet werden: Lieferzeit, Versandkosten, Pflegeetikett, genaue Materialzusammensetzung in Prozent und Füllgewicht pro m² (beides n/a auf der Seite).

**Größentabelle (Bilder im Größen-Modal, wörtlich abgelesen):**

- Tabelle 1 "Size / Fits / Sleeps":
  - "90×200 cm / 35×79 in – Narrow – Caravan, cabin & bunk beds – 1 person, sits flat, no overhang"
  - "140×200 cm – Single – 90–140 cm / 35–55 in wide – 1 person"
  - "160×210 cm – Single XL – 1 person, extra length"
  - "200×200 cm – Double – 140–160 cm – 2 people"
  - "230×230 cm – King – 180–200 cm – 2 people, plenty of room"
  - "260×220 cm – Super King – 180–200 cm – 2 people, extra drop each side"
- Tabelle 2 "Size / Weight / Fits a drum from":
  - "Narrow 90 × 200 cm – approx. 1.2 kg – 6 kg"
  - "Single 140 × 200 cm · fits 3'0" beds – 1.78 kg – 6 kg"
  - "Single XL – 2.06 kg – 7 kg"
  - "Double 200 × 200 cm · fits 4'6" beds – 2.32 kg – 7 kg"
  - "King 230 × 230 cm · fits 5'0" beds – 2.88 kg – 8 kg"
  - "Super King 260 × 220 cm · fits 6'0" beds – 3.12 kg – 8 kg"
- Widerspruch: Bullet "Fits in every washing machine" und Abschnitt "fits in any normal washing machine" gegen die eigene Mindest-Trommel von 6–8 kg. Die Trustpilot-Bewertung von Rona Dixon sagt im Original "although it is a tight fit in my washing machine".

**Alle Aussagen zu Waschen, Temperatur, Tog, Material und Trocknen auf dieser Seite (wörtlich):**

- "10.5 TOG — proper winter warmth"
- "Warm without overheating"
- "Fits in every washing machine"
- "We recommend washing it at 40°C on a spin cycle of around 800 rpm"
- "occasionally wash it at 60°C"
- "dry the Pleene™ duvet in the dryer or let it air dry. Air-dried, it is usually completely dry in about 2 hours"
- "Ours weighs 3.12 kg and compresses flat"
- "Air dries in 2 hours — or even faster in the dryer"
- "Soft, breathable microfibre with a lightweight high-loft fill … free from feathers and down"
- Galerie: "Dries indoors in hours", "Pleene™ Microfibre Technology", "Never clammy, never cold"

Die Produktbeschreibung im Produkt-JSON wird auf der Seite **nicht angezeigt**. Sie enthält zusätzlich Aussagen zu Angle E: "Change your bed in one move with no sore arms, shoulders or back", "a full body workout on your arms, shoulders and back", "Breathable and temperature regulating, so no sweating even in summer", "Care: machine washable, quick-drying".

**Bewertungen auf der Seite:**

- App: Judge.me. Anzeige "4.8", "172 reviews", standardmäßig nach "Most Recent" sortiert.
- Die ersten 5 Bewertungen (alle Duvet, laut Agent-4-Daten alle textgleich mit Trustpilot und vom 11./12.09.2026):
  - Robin Lewis ★5, "I have battled with a duvet and separate cover for years": "I have battled with a duvet and separate cover for years and not least at the oresent time coping with injuries received in a car accident. I have though that there has to be a better way when I discovered the Pleene way. My order took a little while to be delivered but once it arrived it ha been on my bed, now coming up to it's first wash. If that works I will be ordering another set"
  - Ros Leftley ★4, "Very good": "Very good. Just took longer to deliver than I expected"
  - Louise ★5, "Great": "Well, I ordered 2 Pleene quilts. One each for my husband and me. I feel it is light, but I don't feel cold at night. My husband likes a heavy quilt, but he hasn't complained, so I think we are on a winner. However, we have not washed them yet! So if I have any issues, I will update it."
  - blacky ★5, "Excellent product": "Excellent product. Light but very warm and comfortable"
  - Anne ★5, "Excellent quality - better than expected.": "Even though the order took a little longer to reach me than expected, the communication was excellent throughout. I am delighted with my duvet! It is a lovely colour, soft and cosy, yet light and cool in warmer weather."
- Auffällig: Drei der fünf sichtbaren Bewertungen erwähnen eine verzögerte Lieferung.

---

### 3.4 Seite 2: `pleene.com/products/easyrest-comforter` (40 Ads, US) — Produktseite (US-PDP)

**Rolle im Funnel:**

- Die Vorlage heißt `easyrest-duvet-usa230926`, also "USA", 23.09.26.
- Laut Elevate-Konfiguration ist "Duvet UK PDP Weiterleitung an USCA PDP" live (SPLIT_URL, 100 % auf die Variante). Bedingungen: Land US oder CA, Quelle facebook, instagram, google, direct, tiktok oder pinterest. Wirkung: von `/products/easyrest` auf `/products/easyrest-comforter`.
- In unserem Test hat das nicht ausgelöst (US-IP, Headless, mit fbclid und Facebook-Referrer). Nicht verifiziert.
- Laut GetHooked `countries` sind die direkt verlinkenden Ads US-Ads.
- Ein analoger Live-Test leitet AU auf `/products/pleene-easyrest-quilt`. Diese Seite hat im Inventar keine Ads und wurde nicht analysiert.

**Above the Fold, mobil (GBP-Ansicht)** (`render/com_products_easyrest-comforter_mobile_atf_clean.png`):

- Kein Laufband.
- Hauptbild: blaue Comforter-Decke von oben auf beigem Teppich mit zwei Kissen.
- H1 "Pleene EasyRest™ Comforter", ★★★★★ "172 reviews".
- "£69.99 ~~£119.99~~ SAVE 41%".
- Bullets "✔️ Warm in winter, cool in summer", "✔️ No cover to change", "✔️ Hygienic & allergy-friendly", "✔️ Fits in any washing machine".
- "🎁 Free with every comforter today / 2 Pleene™ Pillowcases (Value: **$39.99**)". Der Dollarwert steht auch in der GBP-Ansicht.
- Pop-up wie auf Seite 1.

**USD-Ansicht** (`cart/us_comforter_atf.png`): "$139.99 ~~$199.99~~ SAVE 30%", Couple-Bundle "$252.00 ~~$399.98~~", Family-Bundle "$357.00 ~~$599.97~~".

**Desktop** (`render/com_products_easyrest-comforter_desktop_atf_clean.png`): Navigation wie auf Seite 1, aber ohne braunes Laufband. Links das Bild, rechts die Kaufbox, Couple-Bundle mit "Single (55 × 79 in)" vorausgewählt.

**Seitenaufbau (Überschriften wörtlich):**

1. Hauptbereich:
   - Galerie mit eigenen Comforter-Bildern:
     - "90-Night Free Trial" / "FREE TODAY 2× Pleene™ Pillow Cases Value $39.99"
     - "Comforter + cover in one. Completely washable." mit "Air dries in about 2 hours", "**No chance for dust mites & bacteria**", "Fits any washing machine"
     - "Always the right temperature. Pleene™ Microfiber Technology" mit "Cool in summer", "Warm in winter", "No sweating. No freezing."
     - "Susan, 62: "I was skeptical about the hygiene at first, but here everything gets clean in one wash. Climbing into a fresh, clean comforter straight after a shower — absolutely amazing😍"" mit "10,000+ people love sleeping under the Pleene™ Comforter"
     - "Robert, 61: "No idea how it does it, but I've had the comforter for a year and I don't sweat at night anymore. In summer I wake up dry — that used to be unthinkable.""
     - Collage "10,000+ people already sleep under the Pleene™ Comforter. 90-Night Free Trial. Money back, no questions asked."
   - Kaching-Box, "What size do I need?" (Bild `pleene-size-chart-us.png`), "Ready to Ship – Limited Stock", "ADD TO CART".
   - 4 Akkordeons: "Will I be warm enough in winter?" / "How do I wash and dry the Pleene™ Comforter?" / "Does the Pleene™ Comforter fit in my washing machine?" / "How long does a Pleene™ Comforter last?"
2. "**Washable like your sheets**" / "Most comforters never see a washing machine. They're too bulky for the drum, or the care label says dry clean only." / "The Pleene EasyRest™ fits in a standard home washer. The whole thing goes in — not a cover, the comforter itself. One wash. All clean." / "Air-dries in 2 hours — faster in the dryer." / "✓ Wash it as often as your sheets" "✓ No dry cleaning, no trip to the laundromat"
3. "**You can skip the top sheet**" / "The top sheet exists for one reason: to keep you off a comforter that hardly ever gets washed." / "Take that reason away and the layer stops earning its place on your bed." / "The Pleene EasyRest™ is comforter and cover in one piece — and it goes straight in the wash." / "✓ No cover and no top sheet" "✓ A made bed in seconds"
4. "**One comforter, every season**" / "Most people own two: a heavy one for winter and a thin one for summer. The Pleene EasyRest™ replaces both." / "A 300 GSM fill holds your body heat in, and breathable microfiber lets moisture move out instead of trapping it. That combination is what keeps the same comforter comfortable in January and in July." / H3 "Cold nights": "Traps your body heat and holds it, so the bed is warm within minutes of getting in." / H3 "Warm nights": "Lets heat and moisture escape, so you don't wake up damp or kick it off at 3am." / "✓ No overheating, no waking up cold" "✓ Nothing to swap out when the season turns"
5. "**Feels like a freshly made bed**" / "Soft against the skin. Light, but never thin." / "Not too thick, not too heavy." / "Right for every night of the year — the coldest ones and the warmest."
6. "★★★★★ Over 10,000 customers now sleep more comfortably with Pleene EasyRest™" / "**Try Pleene EasyRest™ risk-free for 90 nights**", dazu 5 "✓ Verified"-Karten:
   - Margaret, 67: "At my age, wrestling a comforter into its cover was such a struggle. This is an absolute godsend — I can make my bed on my own again."
   - James, 55: "Saves me so much time, no more changing covers, and it still feels great. I sweat a lot less at night now, too."
   - Sarah, 41: wie auf Seite 1.
   - Robert, 50: "I expected something this light to leave me cold in winter. It doesn't — and it goes straight into the machine. This is how bedding should be."
   - David, 58: "Honestly, I'm lazy when it comes to changing bedding — and that's exactly why Pleene EasyRest™ is perfect for me."
   - Bei gleichen Namen und gleichem Alter weichen die Zitate teilweise von Seite 1 ab.
7. "**Frequently Asked Questions**": 8 Fragen, wörtlich unten.
8. "**The Full Sleep Set:**" mit Comforter £69.99 ~~£119.99~~, "ZipSheet™ — Zip-On Bed Sheet Set" £59.99 ~~£79.99~~ (US-Größen Twin bis Cal King, "Dusty Purple - Unavailable") und "EasyStore™ - Duvet & Bedding Storage Bag" £19.99 ~~£34.99~~. "Total Price: £149.97 ~~£234.97~~".
9. Judge.me "Customer Reviews 4.8 · 172 reviews". Jede Bewertung ist mit "Review for Pleene EasyRest™ Duvet" gekennzeichnet, es sind also Bewertungen des UK-Duvet.
10. "**You may also like**": FluffBalls™ £14.99, EasyStore™ from £19.99, "Pleene RestEasy™ 3-in-1 Support Cushion" £99.99 ~~£149.99~~.
11. Footer. Ein Newsletter-Block fehlt hier.

**Akkordeons (wörtlich):**

- "Will I be warm enough in winter?" — "Yes. Warmth comes from trapped air, not from bulk — the 300 GSM fill holds your body heat instead of letting it escape. It's lighter than the oversized comforters most people are used to, which is why customers are often surprised by how warm it is the first cold night. / If your bedroom runs unusually cold, a throw over the top handles the deepest part of winter."
- "How do I wash and dry the Pleene™ Comforter?" — "Yes, the Pleene™ Comforter is fully washable and cleans up easily in your washing machine. We recommend washing it on a warm cycle (around 105°F) with a gentle to medium spin. / Pleene™ is designed to absorb far less sweat and dirt than traditional bedding, so a warm wash is perfectly sufficient for everyday cleaning while protecting the material and extending its lifespan. / If you ever want a deeper clean, you can occasionally wash it on a hot cycle (around 140°F). After washing, you can tumble dry the Pleene™ Comforter or let it air dry. Air-dried, it's usually completely dry in about 2 hours."
- "Does the Pleene™ Comforter fit in my washing machine?" — "Yes, with no trouble at all. Pleene™ is intentionally designed so it isn't unnecessarily thick or bulky like traditional comforters. / 👉 What that means for you: you can easily wash it yourself in a regular household washing machine — no stuffing, no cramming. Many customers are surprised at first by how light and compact it is, but that's exactly the advantage: / ✔️ Fits easily in your washing machine / ✔️ Dries significantly faster / ✔️ More hygienic than a traditional comforter / So you don't need an oversized machine or a trip to the laundromat."
- "How long does a Pleene™ Comforter last?" — "The Pleene™ Comforter is built to be washed regularly without losing quality. Even after many wash cycles, it stays shape-stable, soft and functional. With normal use, it'll be part of your bedroom for years."

**FAQ (wörtlich):**

1. "What size should I get?" — eine Tabelle "Size / Comforter / Fits" mit den Zeilen "Twin __ × __ in – Twin and Twin XL beds", "Full / Queen __ × __ in – Full and Queen beds", "King __ × __ in – King and Cal King beds". **Die Platzhalter sind nicht ausgefüllt.** Danach: "If you sleep with a partner and like some overhang, size up. Most couples on a Queen bed are happiest with the King."
2. "Will I be warm enough in winter?" — wie das Akkordeon, in einem Absatz.
3. "Will I get too hot in summer?" — "The fabric lets heat and moisture move through instead of trapping them, so it stays comfortable on warm nights. Customers who tend to sleep hot are usually the ones who notice the difference first — it's the same comforter they use through winter, not a second one they swap in."
4. "Do I need a cover or a top sheet?" — "Neither. The Pleene EasyRest™ is the comforter and the cover in one piece, so there's nothing to put on and nothing to take off. And because the whole thing is machine washable, you don't need a top sheet to keep it clean — you wash it and lay it back on the bed."
5. "Why is the Pleene EasyRest™ cleaner than a regular comforter?" — "Because you can wash the whole thing, not just a cover. With regular bedding, the cover goes in the laundry while the comforter itself often sits unwashed for years. The Pleene EasyRest™ goes in the machine as one piece, so the part you actually sleep under gets washed as often as your sheets do."
6. "What if I don't like it?" — "Sleep under it for 90 nights. If it isn't right for you, tell us and we'll take it back. That covers a full change of season, so you can try it on cold nights and warm ones before you decide."
7. "What is the Pleene EasyRest™ made of?" — "Soft, breathable microfiber with a 300 GSM fill. It's gentle against the skin, holds its warmth, and has no feathers or down."
8. "Is it a good choice if feathers and down bother me?" — "The fill is microfiber, so there are no feathers and no down. Because the whole comforter is machine washable, you can also wash it as often as you like instead of leaving it unwashed between cover changes."

**Einwände:** warm genug, zu heiß im Sommer, Größe, Bezug bzw. Top Sheet, Sauberkeit, Rückgabe, Material, Federallergie, Waschmaschine, Haltbarkeit. Keine Tog-Angabe; die Wärme wird über "300 GSM fill" erklärt.

**Unstimmigkeiten auf dieser Seite:**

- "Value: $39.99" erscheint auch für GBP-Besucher.
- Die FAQ-Größentabelle besteht aus Platzhaltern.
- Die Bewertungen stammen vom UK-Duvet (britische Namen, "quilt", "colour").
- "Robert, 61" sagt "had the comforter for a year", das Produkt existiert seit 25.06.2026.
- Die Produktbeschreibung nennt "Sizes: Twin, Full, Queen, King, Split Comfort Size", die Varianten sind aber Single, Twin, Full, Queen und King.
- Bei gleicher Breite (140 cm bzw. 55 in) kostet der Comforter in GBP £69.99, das Duvet £79.99.

---

### 3.5 Seite 3: `pleene.com/pages/tb-6` (8 Ads, GB) — Advertorial (Pre-Lander)

Typ: Advertorial im Stil einer redaktionellen Landingpage. Oben steht klein "ADVERTISEMENT". Es gibt keinen Shop-Header, keine Preise und keinen Warenkorb. Elemente einer Listicle sind eingebaut (nummerierte Vorteile 01–05). Vorlage: `page.tabeasyrest-tb6`. Alle 5 CTAs führen auf `https://pleene.com/products/easyrest`, der Text "Claim my free pillowcases" ebenfalls. Kein E-Mail-Pop-up (Klaviyo-Ausschluss `*tb*`).

**Above the Fold, mobil** (`render/com_pages_tb-6_mobile_atf_clean.png`):

- "ADVERTISEMENT"
- Kicker in Blau: '"Never change your bed linen on a Sunday again"'
- H1: "How 7,000+ people said goodbye to putting duvet covers on – with a **machine-washable 2-in-1 duvet**"
- fünf grüne Sterne im Trustpilot-Stil: "**Excellent 4.7/5** on Trustpilot · 7,000+ customers"
- Bild "THE OLD WAY" vs. "THE EASYREST WAY":
  - links Hände, die eine weiße Decke in einen Bezug stopfen, mit den Labels "Cover has to be put on" und "Filling slips into corners"
  - rechts eine graue EasyRest auf einem Bett in einem hellen Zimmer mit "Cover and duvet in one" und "Machine-washable in one go"
  - orangefarbenes "VS"
- Die Checkmarks beginnen am Fold-Rand.

**Desktop** (`render/com_pages_tb-6_desktop_atf_clean.png`):

- Links Kicker, H1, Sterne und die 4 Checks: "No more putting covers on", "Not too warm, not too cold", "Fits any washing machine", "Dry in about 2 hours".
- Orangefarbener Button "**Try EasyRest risk-free now**", dazu drei Trust-Kästen: "Free shipping / UK orders over £100", "90 nights / risk-free trial", "Secure / checkout".
- Rechts das Vergleichsbild.
- Darunter der Streifen "AS FEATURED IN" mit den Logos STARTUPS (Magazine), "new!", THE TIMES und "Fabulous". Es gibt keine Links zu Artikeln. Die Dateinamen lauten `Design_ohne_Titel.png`, `Design_ohne_Titel_1.png`, `Design_ohne_Titel_2.png` und `3-removebg-preview.png`. Presseerwähnungen sind nicht verifiziert.

**Seitenaufbau (Überschriften wörtlich):**

1. "ADVERTISEMENT", Hero (s. o.).
2. "AS FEATURED IN".
3. "THE EASYREST DIFFERENCE" / "**Cover and duvet become one**":
   - "Duvet and cover are permanently joined – nothing to stuff in, nothing to straighten out after washing. You use it like any normal duvet: spread it out, snuggle in, done."
   - Checks: "Built-in cover – nothing to put on", "Whole duvet machine-washable at 40°", "Filling never slips into corners", "Air-dries in 2–3 hours", "One duvet for all seasons", "Back on the bed straight after washing".
   - Karten "01 No more putting covers on", "02 No more slipping", "03 All-year use", "04 Fully washable", "05 Quick-drying".
   - CTA, darunter "90-night trial · Free UK shipping over £100 · Secure checkout".
4. "THE HONEST COMPARISON" / "**EasyRest vs. classic bed linen**", Tabelle "EasyRest | Classic":

   | Merkmal | EasyRest | Classic |
   |---|---|---|
   | "Cover needs putting on" | "No" | "Yes, every time" |
   | "Slips inside the cover" | "No" | "Yes" |
   | "Fully washable" | "Yes, at 40°" | "Usually only the cover" |
   | "Drying time" | "2–3 hours" | "Often overnight" |
   | "Suitable all year" | "Yes, thanks to climate fibres" | "Usually seasonal" |
   | "Hygiene" | "Whole duvet washable" | "Duvet rarely washed" |
   | "Effort when changing" | "No cover to put on" | "Join duvet and cover" |

   Danach ein CTA.
5. "REAL EXPERIENCES" / "**Over 7,000 people already sleep without a duvet cover**": Bewertung '"Why has no one done this before?"' / '"This Pleene duvet is light, sumptuously soft and easier to live with. Love it!"' / "Glyn F. · Review from Trustpilot", dazu "★★★★★ Excellent 4.7/5 · 250 reviews on Trustpilot".
6. Angebotskasten: "**Autumn offer**" / "**2 matching pillowcases free with your EasyRest**" / "Worth £39.99 – while stocks last." / Button "Claim my free pillowcases" / "✓ 90-night trial ✓ Free UK shipping over £100 ✓ Secure checkout".
7. "REAL EXPERIENCES" / "**What 7,000+ customers say about EasyRest**" / "4.7" / 'Rated "Excellent" on Trustpilot · 250 reviews' / "Photos sent in by EasyRest customers" (Judge.me-Fotos), dazu 6 Karten:
   - "Glyn F. – Why has no one done this before? – "No heavy duvet putting pressure on your feet and being too hot or too cold. This Pleene duvet is light, sumptuously soft and easier to live with. Love it!""
   - "Andrew B. – I was wrong – "I must admit I was sceptical about the claims for the duvet, but I was wrong. Very comfortable, easy to wash and dries quickly. Good quality material.""
   - "Rona D. – No more getting twisted up – "I bought a king size and it washed well and dried quickly. I especially like the ease with which I can now change bedding and the fact I no longer get twisted up in duvet covers.""
   - "Mr Mayes – It has made life easier – "Very pleased with the product – it has certainly made life easier! With a duvet and cover I always ended up with too much duvet at the feet end and not enough at the head end.""
   - "Kathryn – The whole household sleeps better – "I ordered two doubles and a single so our whole household could try them. After a week we have all been sleeping better due to a more comfortable temperature in bed.""
   - "Moira L. – No faffing about – "Straight on to the bed. No faffing about. It's warm and comfortable. What more could I ask.""
   - Link "Read all 250 reviews on Trustpilot →".
   - **Abgleich mit Trustpilot:** Alle 6 Bewertungen existieren auf Trustpilot (Glyn Fletcher, Andrew Byrne, Rona Dixon, Mr Mayes, Kathryn, MOIRA LOW, 01.–04.09.2026). Sie wurden gekürzt, was die Seite selbst offenlegt. Bei **Rona Dixon fehlt dadurch der Nachteil**. Original: "I bought a king size and **although it is a tight fit in my washing machine** it washed well and dried quickly." Bei Moira Low fehlt "Haven't washed it yet but expect no issues."
8. "90 NIGHTS" / "**Test it risk-free for 90 nights**" / "Sleep on it in your own bed. If it doesn't convince you, send it back and get your money refunded – no complicated explanation needed."
9. "STILL HAVE QUESTIONS?" / "**Frequently asked questions**": 7 Fragen, wörtlich unten.
10. CTA, dann der Disclaimer (wörtlich):
    - "Advertisement. This page is an advertisement for the Pleene EasyRest™ Duvet and is published by Pleene (One Way Ecom Limited, …). It is not a news article or independent editorial content."
    - "Images: Some images on this page were created or edited with the help of AI and are for illustration only. Colours and details of the actual product may vary slightly."
    - "Reviews & results: Customer photos were sent in by EasyRest customers via our review app. Customer reviews are taken from Pleene's public Trustpilot profile and partly shortened; reviewer names are abbreviated. The 4.7/5 TrustScore is based on 250 reviews as of October 2026. Individual experiences vary and the results described are not guaranteed. Customer numbers refer to total orders placed with Pleene. Drying times depend on room temperature, airflow and spin speed."
    - "Health: The EasyRest™ is a bedding product, not a medical device. Statements about allergies and sleep are general information and do not replace medical advice."
    - "Offer & guarantee: Prices and the free pillowcase offer are valid while stocks last and may change at any time. The 90-night trial and money-back guarantee are subject to our returns policy. Free UK shipping applies to orders over £100. All brand names and logos shown belong to their respective owners."

**FAQ (wörtlich, Antworten aus dem HTML, da auf der Seite eingeklappt):**

1. "Do I really not need a duvet cover any more?" — "No. The EasyRest combines duvet and cover in one product. After washing you simply put it back on the bed."
2. "Does it keep me warm in winter – and will I sweat?" — "The breathable EasyRest climate fibres regulate temperature in both directions and wick moisture away, so it stays cool in summer and warm in winter without feeling clammy."
3. "Does it fit in a normal washing machine?" — "Yes. The EasyRest is light and compact, so it fits in any standard household machine – no laundrette needed."
4. "How long does it take to dry?" — "Around 2 hours in the air, faster in a tumble dryer."
5. "Why is it more hygienic than a normal duvet?" — "With ordinary bedding only the cover gets washed. With the EasyRest the whole duvet goes in the wash every time, so you can clean it as often as normal bed linen."
6. "How long does the EasyRest last?" — "It keeps its shape and softness wash after wash, with no clumping or flattening even after 50 washes."
7. "What if I don't like it?" — "You have 90 nights to try it in your own bed. If it's not for you, contact our customer service and you'll get your money back."

**Einwände:** Bezug, Wärme bzw. Schwitzen, Waschmaschine, Trocknungszeit, Hygiene, Haltbarkeit ("50 washes"), Rückgabe. Kein Tog, keine Preise. Die Trocknungszeit ist auf derselben Seite widersprüchlich: "Dry in about 2 hours" und "Around 2 hours" gegen "Air-dries in 2–3 hours" und "2–3 hours".

---

### 3.6 Seite 4: `pleene.com/products/easyrest-duvet` (6 Ads, GB) — Produktseite (Klon)

- **Above the Fold, mobil und Desktop:** Der Textvergleich mit Seite 1 ergibt nur einen Unterschied: Das Laufband "Free Shipping On Orders Over £100 / …" fehlt. Gleiches Hauptbild, gleiche H1 "Pleene EasyRest™ Duvet", "172 reviews", "£74.99 ~~£114.99~~ SAVE 34%", gleiche 4 Bullets, gleicher Geschenk-Kasten "2 Pleene™ Pillow Cases (Value: £39.99)", gleiche Kaching-Box. Screenshots: `render/com_products_easyrest-duvet_mobile_atf_clean.png` und `…_desktop_atf_clean.png`.
- **Seitenaufbau, FAQ und Aussagen:** identisch mit Seite 1. Gleiche Sections (`main`, `custom_liquid_UaiXN9`, `bundle_deals_EQzQcN`, Judge.me, Newsletter) und gleiche Texte. Der Diff der vollständigen Seitentexte zeigt nur das fehlende Laufband und die Kennzeichnung "Review for Pleene EasyRest™ Duvet" im Bewertungs-Widget.
- **Unterschiede in den Daten:**
  - Eigenes Produkt (Handle `easyrest-duvet`, angelegt am 09.09.2026, veröffentlicht am 10.09.2026, Tags `hidden-search`, `search-hidden`).
  - Vorlage `easyrest-duvet-winter26-2`.
  - Lavender Mist hat für alle Größen den Vergleichspreis £114.99, bei King und Super King also **unter** dem Preis.
- **Angle:** B. Alle 6 Ads sind Tog- bzw. Winter-Ads, z. B. "Warm Enough For A British Winter" und "No Launderette Needed. Ever.".

---

### 3.7 Garantie, Probeschlafen, Rückgabe und Versand (für alle Seiten)

**Versprechen auf den Seiten (wörtlich):**

- Laufband und Galerie: "90 Nights Risk-Free — Try It In Your Own Bed", "90 Night Free Trial", "90-Night Free Trial. Money back, no questions asked."
- Produktseite, FAQ: "Return postage is paid by the customer and we ask that it comes back clean and resaleable."
- Comforter: "tell us and we'll take it back"
- tb-6: "send it back and get your money refunded – no complicated explanation needed"
- Warenkorb: "90-Night Home Trial", "Money Back Guarantee"

**Refund Policy** (`/policies/refund-policy`, "Last updated: September 04, 2026"), wörtliche Eckpunkte:

- "We accept returns of both defective and non-defective products within 90 days of delivery."
- Tabelle: "Return window 90 days from delivery" / "Accepted condition New or slightly used, including opened packaging" / "Return method By mail" / "Return shipping Paid by the customer, unless the return is due to an error on our side" / "Restocking fee None" / "Refund processing time Up to 10 days after we receive and inspect your return" / "Exchanges Available on request"
- "90-Day Guarantee … If you are not satisfied with your purchase for any reason, you may request a return, exchange, or refund within 90 days of receiving your order. No questions asked."
- "That is why we invite you to contact us first before sending anything back. In many cases, we can help with guidance, a replacement, or a refund without requiring a physical return. This is an invitation, not a condition"
- "Please wait for these instructions before shipping anything back"
- "We are unable to accept items that are soiled, contaminated, or damaged in a way that makes them unsafe or unhygienic to handle"
- "Original shipping fees are non-refundable unless the return is due to an error on our side."

Bewertung: "Money back, no questions asked" und "Free Trial" klingen kostenlos. Tatsächlich trägt der Kunde Rücksende- und Hinversandkosten, und die Rücksendeadresse gibt es nur auf E-Mail-Anfrage.

**Zusatzprodukt "180-Day Return Policy – Upgrade"** (£2.99 bzw. $2.99, Cross-Sell auf der /cart-Seite), Beschreibung wörtlich: "With this upgrade, you receive a voluntarily extended return window of 180 days in total from the date you receive your order. Your statutory rights, in particular the legal 14-day right of withdrawal, naturally remain unaffected. The upgrade is a digital service and applies to your entire order, not to individual items. There are no further obligations or costs – just a longer, hassle-free return window for you."

**Shipping Policy** (`/policies/shipping-policy`, "Last updated: September 04, 2026"):

- UK: "£0.00–£99.99 Royal Mail® — tracked, insured £4.95 GBP" / "£100.00 and up … Free" / "Royal Mail® — tracked, insured, with Priority Handling £7.95 GBP"
- Bearbeitung: "Orders placed before 2:00 PM (GMT) on a business day are processed the same day." / "Orders are typically processed within 1–2 business days"
- Lieferzeit UK: "1–2 business days / 4–6 business days / 5–8 business days". Ebenso für die USA. Kanada 7–12, Australien 8–14 Werktage.
- Zu "Priority Handling": "It shortens the processing window only. It does not speed up the carrier".
- Ausgeliefert wird nach UK, USA, Kanada und Australien.
- Home-Page: "Dispatched in 1–2 Days / From our nearest warehouse". Lagerstandort n/a.

Folge für das Angebot: Ein einzelnes Duvet bis Double (£74.99–£89.99) liegt unter der Gratisversand-Schwelle, dazu kommen £4.95. Das vorausgewählte Couple-Bundle (ab £135) ist versandkostenfrei.

---

### 3.8 Bewertungs-Apps und -Zahlen

| Quelle | Wo angezeigt | Angabe auf der Seite | Erfasster Stand (Agent 4, 08.10.) |
|---|---|---|---|
| Judge.me | alle 3 Produktseiten (Badge und Widget) | "4.8", "172 reviews" | 172 Bewertungen (171 Duvet, 1 Comforter), Mittel 4.82, Sterne 5×142 / 4×29 / 3×1. **154 textgleich mit Trustpilot** (Import), 4 "verified buyer", 8 mit Foto, 0 Video. Neueste vom 12.09.2026 |
| Trustpilot | nur tb-6 (Zitate und Links) | "Excellent 4.7/5", "250 reviews … as of October 2026" | 291 Bewertungen, alle aus dem Zeitraum 01.08.–08.10.2026 (Mittel der Sterne 4.8; der TrustScore selbst n/a) |
| Eigene Testimonials | Produktseiten-Karten "✓ Verified", Galeriebilder | Margaret 67, James 55, Sarah 41, Robert 50, David 58; Robert 61, Susan 62 | **in keiner erfassten Bewertung gefunden**, nicht verifiziert |
| UGC-Videos | /products/easyrest, /products/easyrest-duvet | "Peter", "Brian", "Dave" | nicht transkribiert |

GetHooked meldet für die Technik zusätzlich Loox und Yotpo. Im HTML stehen dazu nur leere Theme-Variablen (`MetafieldLooxRating = null`, `okendoProduct = null`). Das sind falsch-positive Treffer; es ist keine aktive App erkennbar.

---

### 3.9 Warenkorb, Upsells und Cross-Sells (bis vor den Checkout)

**Testablauf** (Skripte `a3scripts/cart_test.js`, `a3scripts/cart_bars.js`, `a3scripts2/us_comforter.js`):

- Für alle 3 Produktseiten: GB-Kontext, mobil 390 px. Alle 10 Farben und 6 bzw. 5 Größen im "Buy 1"-Balken durchgeschaltet.
- Jeden Kaching-Balken (1/2/3) in den Warenkorb gelegt, Cart-Drawer und /cart angesehen.
- `/products/easyrest` zusätzlich auf Desktop.
- Comforter zusätzlich in USD.
- Checkout-URLs per Request-Blocker gesperrt, der Warenkorb nach jedem Lauf per `/cart/clear.js` geleert.

**Varianten und Lager:**

- Alle Farben (Coastal Blue, Soft Mint Green, Moonstone Grey/Gray, Cream Beige, Midnight Black, Hearth Red, Cloud White, Cocoa Brown, Sunset Glow, Lavender Mist) und alle Größen sind wählbar und kaufbar. Keine ist "Sold out".
- Bei jeder Variante steht derselbe statische Text "Ready to Ship – Limited Stock".
- Lagerbestände sind öffentlich nicht abrufbar (`inventory_quantity: null`).
- Die Ad-Aussagen "Hearth Red is nearly sold out" und "Mint Green is almost gone" haben auf der Seite keine Entsprechung (kein Farb-Lagerhinweis). Den tatsächlichen Bestand konnten wir nicht prüfen.

**Cart-Drawer, GB** (Screenshots `cart/bars_easyrest_mobile_9177_drawer.png` und `cart/bars_easyrest_desktop_9177_drawer.png`; Texte in `cart/*_drawer.txt`):

- Kopf "Cart • 2 item".
- Fortschrittsbalken: bei 1× Narrow (£74.99) "Only £25.01 more to get FREE Shipping!", ab £100 "Congrats! You get FREE shipping!".
- Zeile: Bild, "Pleene EasyRest™ Duvet", "~~£114.99~~ £67.50", Tag "Buy 2, Get 4 Pillow Cases FREE", Variante, Mengenwähler, "~~£229.98~~ £135.00 (You're saving £94.98)".
- "↓ **ADD ONE-TIME CART DEALS** 🛒", Toggles standardmäßig **aus**:
  - "Pleene EasyRest™ Pillow-Cases" £19.99 ~~£29.99~~ (Farbe, "51 x 76cm")
  - "EasyRest™ Pillow – Hypoallergenic Premium-Comfort Pillow" £39.99 ~~£59.99~~ ("1 Pillow" oder "2 Pillows", "48 x 74cm")
  - "FluffBalls™ – Reusable Tumble Dryer Balls (Set of 4)" £14.99 (White oder Blue)
- **Versandschutz:** "Package Protection (Recommended)" £2.99, "FREE Replacements in case of Package Loss, Theft or Damage during Shipping." Toggle standardmäßig **aus**, also nicht vorausgewählt.
- Summen: "Discount −£94.98", "Subtotal £135.00", "Discounts: £-67.50)" (Darstellungsfehler).
- Der Rabatt laut Shopify-`cart.js` beträgt nur £14.98 (10 % auf 2 × £74.99). Die "−£94.98" schließen die Differenz zum Vergleichspreis ein.
- Button "Secure Checkout", darunter "90-Night Home Trial" und "Money Back Guarantee".
- **Gratisbeigaben:** Die versprochenen 2, 4 bzw. 6 Kissenbezüge erscheinen **nicht als Warenkorbposition**, sondern nur als Rabatt- bzw. Tagname "Buy 2, Get 4 Pillow Cases FREE". `cart.js` enthält nur die Decken. In der Kaching-Konfiguration ist `freeGifts: []` für alle drei Balken eingetragen. Ob die Bezüge im Checkout oder beim Versand dazukommen, ist **nicht verifiziert**.
- Wertangabe: Die Gratis-Bezüge werden mit "Value: £39.99" beworben. Das gleiche Produkt "Pillow-Cases" kostet im Drawer £19.99 (statt £29.99). Ob das ein Paar ist, ist auf der Karte nicht angegeben; die Home-Collection nennt "EasyRest™ Pillow Cases / Set of two". Ob der Wert damit überhöht ist, ist nicht verifiziert.
- Der Drawer ist für `/products/easyrest`, `/products/easyrest-duvet` und `/products/easyrest-comforter` (GBP) identisch.

**/cart-Seite, GB** (`cart/bars_easyrest_mobile_9177_cartpage.png`):

- "Your cart", Zeile mit "~~£74.99~~ £67.50". Hier wird der normale Preis als Streichpreis verwendet, im Drawer dagegen £114.99.
- "Subtotal £135.00 GBP", "Secure Checkout", Express-Buttons **Shop Pay, PayPal, Google Pay**.
- "**You may also like**":
  - "180-Day Return Policy – Upgrade" £2.99
  - "BreatheEasy™ Nasal Strips (30pcs)" £14.99 ~~£19.99~~
  - "CoolRest™ - Cooling Ice Duvet for Hot Summer Nights" from £69.99 ~~£99.99~~
  - "EasyRest™ Fitted Sheet – Soft, Hypoallergenic & Perfectly Fitting" from £24.99 ~~£39.99~~
- Newsletter "Subscribe to our emails".
- Es gibt keine Gratisgeschenk-Stufen und keine Mengen-Upsell-Pop-ups. Kaching hat `progressiveGifts: null` und `timer: null`.

**Cross-Sell auf den Produktseiten:** "The Cosy Bundle" (+ CosyRest™ Throw) bzw. auf der US-Seite "The Full Sleep Set:" (+ ZipSheet™ und EasyStore™). Gekauft wird über "Add selected to cart", ohne Extra-Rabatt.

**USD, Comforter** (`cart/us_comforter_9177_drawer.png`, `cart/us_comforter_9177_cartpage.png`):

- Drawer: "Congrats! You get FREE shipping!", Zeile "~~$199.99~~ $126.00", "~~$399.98~~ $252.00 (You're saving $147.98)".
- Upsells:
  - "ZipLift™ – Mattress Lifter" $19.99 ~~$29.99~~
  - "FluffBalls™ … (Set of 4)" $14.99 ~~$19.99~~
  - "Package Protection (Recommended)" $2.99
- /cart: "You may also like" mit "180-Day Return Policy – Upgrade" $2.99, "BreatheEasy™ Nasal Strips (30pcs)" $14.99, "EasyRest™ Pillow – Hypoallergenic Premium Comfort Pillow" from $49.99 und "EasyStore™" from $29.99.

---

### 3.10 Kongruenz: Ad und Landingpage

Links: Ad Library `https://www.facebook.com/ads/library/?id=<external_id>`; GetHooked über die share_url (die Signatur ist kein ablaufender Media-Link).

**`/products/easyrest`:**

| Ad | Hook und Versprechen (wörtlich) | Fortsetzung auf der Seite | Bewertung |
|---|---|---|---|
| 136388964, Bild, 120 Tage aktiv, Perf. 100. [Ad Library](https://www.facebook.com/ads/library/?id=884267707299487), [GetHooked](https://app.gethookd.ai/share/ad/136388964?signature=d0ff0d2a2536e91cfc3dacb7f3b055bf680241a71e3d485ea8d2c98436047966) | Titel "No More Fighting With Duvet Covers". Text: "Duvet + Cover in One 🌙 … ✓ No more wrestling with a separate duvet cover ✓ Pleasantly cool in summer, cosily warm in winter ✓ Hypoallergenic and kind to sensitive skin / Get 2 free Pleene™ Pillow Cases today (worth £39.99). / 90 nights to try it risk-free." | Gratisbezüge "(Value: £39.99)" stehen direkt im ATF, "90 Nights Risk-Free" im Laufband. Der Kampf mit dem Bezug kommt erst in Section 6 ("Never make the bed the hard way again"). Das ATF führt mit "10.5 TOG — proper winter warmth" | **Teilweise kongruent.** Angebot und Garantie passen 1:1. Der Bezug-Hook (C) wird above the fold nur über "Never change bedding again" aufgegriffen, die Seite führt stattdessen mit Wärme (B). "Hypoallergenic" steht erst in der FAQ |
| 139561428, Video, 63 Tage, Perf. 100. [Ad Library](https://www.facebook.com/ads/library/?id=1034362836068724), [GetHooked](https://app.gethookd.ai/share/ad/139561428?signature=1eb14bdf7f1f4b278f8b5996d37204958181d02f07e10262e225457c7f9a49fd) | "Hearth Red. Nearly gone." / "Hearth Red is nearly sold out — and unlike most 'selling fast' claims, this one's just true. If deep red is your bedroom, this is the week to move. Duvet and cover in one, fully washable, dry in 2 hours." | Es gibt keinen Farb-Lagerhinweis. Hearth Red ist normal wählbar, als Standardfarbe ist Coastal Blue vorausgewählt. Nur der generische Text "Ready to Ship – Limited Stock" ist sichtbar. "dry in 2 hours" wird bestätigt | **Bruch** beim Knappheitsversprechen. Die Seite setzt die Dringlichkeit nicht fort, und das Ad-Motiv (Rot) ist nicht vorausgewählt |
| 168246678, Video, 41 Tage, Perf. 100. [Ad Library](https://www.facebook.com/ads/library/?id=1607904514111212), [GetHooked](https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59) | "Check This Before You Buy" / "✓ Does the WHOLE thing fit a normal washing machine? ✓ Is it dry in 2 hours without a tumble dryer? ✓ Can you test it at home for 90 nights? The Pleene EasyRest™: yes, yes and yes." | "Fits in every washing machine" (ATF), FAQ "a normal household machine is enough", "Air-dried … about 2 hours", "90 nights" | **Kongruent** in den drei Punkten. Die eigene Größentabelle ("Fits a drum from 6–8 kg") schränkt das "yes" zur Waschmaschine aber ein |
| Ergänzend: 145443331, Video, 56 Tage. [Ad Library](https://www.facebook.com/ads/library/?id=1440933327878495) | "Everyone said it. They were right." / "…you never have to change the bed linen again…" | ATF-Bullet "Never change bedding again" | kongruent |

**`/products/easyrest-comforter` (US-Ads):**

| Ad | Hook und Versprechen (wörtlich) | Fortsetzung auf der Seite | Bewertung |
|---|---|---|---|
| 182988043, Bild, 15 Tage, Perf. 54. [Ad Library](https://www.facebook.com/ads/library/?id=29208178135432493), [GetHooked](https://app.gethookd.ai/share/ad/182988043?signature=474ac523034272536a305779503c22ea294092cc8bd3cc7b069288c8fe337071) | "Wash The Whole Comforter" / "Yes, the whole comforter goes right in the wash! The Pleene EasyRest™ Comforter fits standard home washers, making fresh, clean bedding refreshingly simple." | Erste Section "Washable like your sheets": "The whole thing goes in — not a cover, the comforter itself." Bullet "Fits in any washing machine" | **Stark kongruent** (Angle A, gleiche Wortwahl "comforter", "standard home washer") |
| 182988041, Bild, 16 Tage, Perf. 41. [Ad Library](https://www.facebook.com/ads/library/?id=27616218781386469), [GetHooked](https://app.gethookd.ai/share/ad/182988041?signature=656021e045b4ec00d24fe1a994c294542e9ff36636166d025b70fab06f7efb14) | "The Comforter That Does It All" / "No cover. No corners to find. No stuffing required. … all-in-one machine-washable comforter" | "No cover to change" (ATF), "You can skip the top sheet", "comforter and cover in one piece" | **Kongruent** |
| 200490657, Video, 3 Tage, Perf. 12. [Ad Library](https://www.facebook.com/ads/library/?id=1088262300260108), [GetHooked](https://app.gethookd.ai/share/ad/200490657?signature=14e9cab282a8e5334823ebd0fe803836a252fcd8cf045e8e22111a5867c33ff8) | "Say Goodbye to Duvet Cover Hassle" / "No more stuffing, buttoning or fighting with duvet cover corners. Pleene EasyRest™ combines a duvet and cover in one…" | Die Seite spricht durchgehend von "comforter". Das Wort "duvet" kommt nur in der Beschreibung und in den (britischen) Bewertungen vor. Der Kampf mit dem Bezug wird in "No cover to change" und "You can skip the top sheet" aufgegriffen | **Teilweise kongruent.** Das Versprechen passt, aber die Terminologie der Ad ("duvet") wechselt auf der Seite zu "comforter" |

**`/pages/tb-6`:**

| Ad | Hook und Versprechen (wörtlich) | Fortsetzung auf der Seite | Bewertung |
|---|---|---|---|
| 193234221, Video, 8 Tage, Perf. 52. [Ad Library](https://www.facebook.com/ads/library/?id=2325762131511604), [GetHooked](https://app.gethookd.ai/share/ad/193234221?signature=34d449a91191d816e5a91f7d690e2d93f52044d2af092704c3b3dece336abb59) | "Everyone said it. They were right." / "I only ordered it because everyone said you never have to change the bed linen again. Annoyingly, they were right. … wash it whole, dry in 2 hours, throw it back on." | Kicker '"Never change your bed linen on a Sunday again"', H1 "How 7,000+ people said goodbye to putting duvet covers on", Social Proof von 7,000+ Kunden und Trustpilot, "Dry in about 2 hours" | **Stark kongruent.** Testimonial-Hook trifft auf eine Social-Proof-Seite, fast wortgleich ("never change your bed linen") |
| 193234215, Bild, 8 Tage, Perf. 52. [Ad Library](https://www.facebook.com/ads/library/?id=1068343922634373), [GetHooked](https://app.gethookd.ai/share/ad/193234215?signature=92968440b95005fe0fc1bf85409c9b3366e3ae8f6dbf240ce5448a242e85affb) | "No More Fighting With Duvet Covers" (gleicher Text wie 136388964, inkl. "Get 2 free Pleene™ Pillow Cases today (worth £39.99). / 90 nights to try it risk-free.") | Hero "No more putting covers on", Kasten "2 matching pillowcases free … Worth £39.99", "90 nights risk-free trial" | **Kongruent** (Bezug, Angebot, Garantie) |
| 193234218, Video, 8 Tage, Perf. 1. [Ad Library](https://www.facebook.com/ads/library/?id=1114220797783359), [GetHooked](https://app.gethookd.ai/share/ad/193234218?signature=3870fec0fed270d728da178501d4d67c9e13c536497ef821674e8f3e9c30953b) | "Be honest. When did you last wash it?" / "This week only: 2 free Pleene™ Pillow Cases with every duvet. And if you want the bedroom ready for the colder nights, Hearth Red is the one everyone picks, and it's almost gone. …" | Hygiene nur in der Vergleichstabelle ("Duvet rarely washed") und in der FAQ. Das Angebot heißt "Autumn offer … while stocks last" statt "This week only". Hearth Red und Farbknappheit kommen nicht vor | **Schwach.** Der Hygiene-Hook (A) wird nicht prominent fortgesetzt. Die Dringlichkeit "This week only" bzw. Farbe fehlt |

**`/products/easyrest-duvet`:**

| Ad | Hook und Versprechen (wörtlich) | Fortsetzung auf der Seite | Bewertung |
|---|---|---|---|
| 178749258, Bild, 23 Tage, Perf. 81. [Ad Library](https://www.facebook.com/ads/library/?id=1750276626195989), [GetHooked](https://app.gethookd.ai/share/ad/178749258?signature=26142585e8a79bd682cbb72cd7ae73d46e39dc00bb8ff65b79f19d32e5e4e2cb) | "No Launderette Needed. Ever." / "❄️ Your winter duvet shouldn't need a launderette. … ✓ Cover sewn in, nothing to strip off ✓ Fits a normal washing machine 🧺 ✓ Filling quilted in place, no cold spots ✓ Dry again in about 2 hours / 🎁 Right now: 30% off + 2 FREE matching pillow cases." | "10.5 TOG — proper winter warmth", "Fits in every washing machine", Geschenk-Kasten, "SAVE 34%" (Narrow; 23–35 % je nach Größe) | **Kongruent** (Winter, Waschmaschine, Angebot). Die "30% off" der Ad entsprechen 23–35 % auf der Seite. "launderette" kommt auf der Seite nicht vor |
| 178749251, Video, 23 Tage, Perf. 81. [Ad Library](https://www.facebook.com/ads/library/?id=1792003651846452), [GetHooked](https://app.gethookd.ai/share/ad/178749251?signature=f7a95b97af4df738359f0bc0b4a21bbd6f5508efef5391e097423762a823afc1) | "Warm Enough For A British Winter" / '❄️ "You'll freeze under that in winter." Here's the honest answer: the Pleene EasyRest™ is rated 10.5 tog, a proper autumn and winter weight, and the whole thing still goes in your washing machine.' | ATF-Bullet "10.5 TOG — proper winter warmth", Galerie "10.5 TOG. Built for British winters.", Section "10.5 TOG. Built for cold nights.", FAQ "It looks thin…" | **Sehr stark kongruent.** Die Seite ist für genau diesen Einwand gebaut |
| 179476350, Bild, 22 Tage, Perf. 81. [Ad Library](https://www.facebook.com/ads/library/?id=935523852471023), [GetHooked](https://app.gethookd.ai/share/ad/179476350?signature=929eaf7be4e50da7829743ff0e7ad0be30111ad47d7408608f8bb7fc89e7de17) | gleicher Text wie 178749251 | wie oben | **Sehr stark kongruent** |

**Fazit Kongruenz:**

- Am besten passen die **Tog-Ads auf die easyrest- und easyrest-duvet-Seite** (B auf B), die **Testimonial- und Bezug-Ads auf tb-6** und die **Wasch-Ads auf die US-Comforter-Seite**.
- Brüche entstehen bei Knappheits-Ads (Farbe "nearly gone", "This week only"), weil die Seiten dazu nichts zeigen.
- Ein weiterer Bruch: Hygiene-Hooks wie "When did you last wash it?" laufen auf tb-6, wo Hygiene nur am Rand vorkommt.

---

### 3.11 Technik

**Shopify-Theme:** `Shopify.theme = {"name":"working of shrine-theme-pro","id":203880759628,"schema_name":"Shrine PRO","schema_version":"1.8.0","theme_store_id":null}`. Shrine PRO kommt nicht aus dem Theme Store und lädt `js.shrinetheme.com`. Die Section `global-music-player` ist vorhanden. Der Shopify-Store heißt `sq48au-70.myshopify.com`, die Shop-ID ist 106066411852.

**Apps (im HTML nachgewiesen über App-Embeds bzw. Extensions):**

| App | Funktion im Funnel | Nachweis |
|---|---|---|
| Kaching Bundles (`kaching-bundles-2039`) | Mengenstaffel 1/2/3 mit "Couple-Bundle"/"Family-Bundle", Cart-Rabatte | Extension, `kaching-bundles-deal`-Inputs, `apps/kaching-bundles` |
| Judge.me (`judgeme-774`) | Sterne-Badge und Bewertungs-Widget, Bild-Reviews (auch auf tb-6) | Extension, Web-Pixel "Judge.me" |
| Elevate A/B Testing (`elevate-ab-testing-201`, `apps/elevateab`) | Preis-, Template- und Split-URL-Tests, Geo-Weiterleitungen | `window.eab_data` mit 12 Tests (s. u.) |
| HeyMerch Sales Stock Counter (`heymerch-sales-stock-counter-51`) | Lager- bzw. Verkaufszähler. Geladen, aber im Test **nicht sichtbar**; die Knappheitszeile ist fest im Theme | Extension-Skripte |
| Klaviyo (`apps/klaviyo-email-marketing-sms`) | Pop-up "Welcome Pop Up - Email" (Gewinnspiel), Newsletter | `static.klaviyo.com`, Formular RJktrA |
| ParcelPanel (`apps/parcelpanel`, Pixel-Endpunkt `api.parcelwill.com`) | "Track Your Order" | Seite `/apps/parcelpanel` |
| Zigpoll | Umfragen (z. B. Post-Purchase; nicht verifiziert, welche) | `cdn.zigpoll.com` |
| Lucky Orange | Session-Recording und Heatmaps | `tools.luckyorange.com`, `apps/lucky-orange` |
| Triple Whale | Attribution | `apps/triplewhale`, `TriplePixel` |
| Google Ads Pixel by Nabu | Google-Ads-Conversion | `apps/google-ads-pixel-by-nabu`; Web-Pixel mit `AW-18246939242` |
| Shopify Bundle-Deals-Section des Themes | "The Cosy Bundle" / "The Full Sleep Set:" | Section `bundle_deals_EQzQcN` |

**Web-Pixel (`webPixelsConfigList`), 13 Einträge:**

- **Meta Pixel** `pixel_id 2174873679968281` (facebook_pixel)
- **Google Ads** `AW-18246939242`
- Judge.me
- ParcelPanel (`api.parcelwill.com`)
- Shopify Standard- und Custom-Pixel
- Weitere App-Pixel mit Konfigurationen `siteId`, `storeId`, `accountID 1880964 / spfy-pxl.archive-digger.com`, `marketerIds` (Format passt zu Outbrain) und `shopifyDomain`. Ihre Zuordnung ist nicht verifiziert.
- **Kein TikTok-, Pinterest- oder Snapchat-Pixel** gefunden.

**GetHooked** (`get_shop` 47758 / `get_ad_technologies`; für alle 4 Seiten identisch):

- Pixel: Microsoft Clarity (93), Google Analytics (88), Meta Pixel (88)
- Apps: Judge.me, Klaviyo, Loox, Shop Pay, Yotpo, Trustpilot, Kaching Bundle Quantity Breaks
- Theme "working of shrine-theme-pro"
- Clarity wird in der Elevate-Konfiguration über `hasClarityEnabled` angesprochen; ein eigenes Clarity-Tag im HTML wurde nicht gefunden.
- Loox, Yotpo und Okendo sind im HTML nur Null-Variablen des Themes, also wahrscheinlich falsch-positiv.
- GetHooked schätzt den Shop als "US" (`country_kind: likely`) mit Währung "USD" (inferred). Das widerspricht der Basiswährung GBP.
- monthly_visits 29,356, 29 Produkte.

**Elevate-A/B-Tests (aus `window.eab_data.allTests`, Namen wörtlich):**

| Test | Typ | Live | Bedingungen | Inhalt |
|---|---|---|---|---|
| "Duvet UK PDP Weiterleitung an USCA PDP" | SPLIT_URL | **true** | US, CA; Quelle facebook, instagram, google, direct, tiktok, pinterest | 100 % von `/products/easyrest` auf `/products/easyrest-comforter` |
| "Duvet UK PDP Weiterleitung an AUS PDP" | SPLIT_URL | **true** (2. Kopie false) | AU | auf `/products/pleene-easyrest-quilt` |
| "ZipSheet UK PDP Weiterleitung an USCA PDP" / "…an AUS PDP" | SPLIT_URL | true | US, CA bzw. AU | `/products/zipsheet` auf `-us` bzw. `-aus` |
| "ZipSheet US PDP1 Weiterleitung an AUS PDP" | PRODUCT | true | AU | Produkttausch |
| "Duplicated 07-28-2026 - EasyRest - 10 Pounds Split Test" (3×) | PRICE_PLUS | false | GB, facebook/instagram, nur Erstbesucher | Variante mit höheren GBP-Preisen (79.99 / 84.99 / 89.99 / 119.99, Vergleich 119.99–159.99) für `easyrest` und `easyrest-pdp` |
| "UK DUVET PDP - AKTUELL vs. easyrest-pdp-04-08-26" | PAGE | false | GB | Template-Test |
| "USCA DUVET PDP - easyrest-duvet-usa vs. easyrest-duvet-winter26 different tog rate" | PAGE | false | US, CA; facebook/instagram | Template-Test auf der Comforter-Seite ("different tog rate") |
| "ZipSheet US PDP1 vs ZipSheet US PDP2" | PAGE | false | US | Template-Test |

Elevate-Einstellungen: `"inTrial":true`, `"useShopifyGeolocation":true`, `"excludeGoogleTraffic":true`. Daraus geht hervor, dass Pleene Preispunkte (+£5/£10) und Templates systematisch testet und die Länder-Funnel über die Weiterleitungen trennt.

**URL-Parameter:** Zwei Comforter-Ads verlinken mit `?trybe=532dbd48` bzw. `?trybe=769e7716`. Im Seitencode gibt es keine Referenz auf "trybe"; Zweck und Tool sind nicht verifiziert.

---

### 3.12 Home-Page und weitere Funnel-Elemente

**Home-Page** (`/`, `render/com__mobile_full.txt`):

- Laufband "🚚 Free shipping on orders over £100 · 90-day home trial".
- Hero "THE EASYREST™ DUVET" / "**Make your bed in 10 seconds.**" / "A coverless, machine-washable duvet designed for how you actually live. No wrestling. No cover fights. Just fresh sheets, fast." / Buttons "SHOP EASYREST™" und "SEE HOW IT WORKS" / Leiste "NO DUVET COVER · WASHES AT 40°C · TUMBLE-DRYER SAFE".
- Das hervorgehobene Produkt auf der Home-Page ist überraschend **ZipSheet™ - Zippered Fitted Sheet** (£59.99 ~~£79.99~~).
- Weitere Sections:
  - "HOW EASYREST™ WORKS / Bedding, reimagined." mit 3 Schritten
  - "THE OLD WAY VS THE NEW WAY / Why we skipped the duvet cover."
  - "BUILT FOR REAL LIFE / Every detail, rethought." ("Quick-drying fibre … Typically ready again in about 2 hours", "All-season weight / A mid-weight fill designed to work through spring, autumn and most winters. One duvet, all year.", "Six colourways")
  - "THE FULL COLLECTION / The collection."
  - "CARE & SIZING / Simple to live with." ("40°C, normal cycle / Wash the duvet on its own with a mild detergent. Skip fabric softener and bleach — both reduce the loft of the fill over time.", "Tumble-dry on low, ideally with dryer balls to keep the fill even.")
  - "THE HONEST COMPARISON / Pleene vs a regular duvet."
  - FAQ "QUESTIONS, ANSWERED / Everything you might wonder about." mit u. a. "Is it warm enough for winter?" — "It's a mid-weight, all-season duvet that suits most bedrooms from spring through winter."
  - "90 nights to decide — or your money back."
- **Widerspruch** zur Produktseite: "mid-weight, all-season" gegen "10.5 TOG — proper winter warmth"; "Six colourways" gegen 10 Farben.

**E-Mail-Pop-up bzw. Gewinnspiel** (Klaviyo-Formular `RJktrA`, "Welcome Pop Up - Email", Typ POPUP, Allocation 100 %):

- Trigger: `DELAY 0` (sofort), `EXIT_INTENT true`, `COOKIE_TIMEOUT 5` (Tage), `EXISTING_USER` und `SUPPRESS_SUCCESS_FORM`.
- Ausgeschlossen auf `duvet-10r`, `pages/easyrest-duvet`, `easyrest-lp`, `pages/easyrest-tb`, `pages/adv10r-2`, `pages/adv-9r`, `*tb*` und `pages/tb-5`.
- Text: "Win a free Duvet" / "One subscriber wins a duvet of their choice every month. Any size, any colour." / "Your email address" / "Enter the giveaway".
- Erfolgsmeldung: "You're in." / "We draw on the 1st and email the winner. Until then — have a look around."
- Es gibt keinen Rabattcode. **Teilnahmebedingungen fehlen**: `/pages/giveaway`, `/pages/competition` und `/pages/win` liefern 404, und weder Terms noch Privacy Policy erwähnen ein Gewinnspiel.
- Motiv: lachendes Senioren-Paar mit Decken (Zielgruppe 55+).

**Track Your Order:** Der Menüpunkt führt auf `/apps/parcelpanel` (ParcelPanel) mit den Feldern "Order Number" und "Email or Phone Number" sowie "Track". `/pages/track-your-order` liefert 404.

**About Us** (`/pages/about-us`):

- "We got rid of the duvet cover."
- "The chore nobody redesigned" mit dem Satz "So we built the duvet and the cover as one piece. Wash the whole thing at 40°C in a normal machine, tumble-dry it on low, put it back."
- Zitat "Good bedding shouldn't need a technique. If it takes practice, we designed it wrong. — Founder of Pleene". Es gibt **keine Gründer-Story mit Namen oder Gesicht**.
- "How we decide things" ("Fewer steps wins", "Numbers, not adjectives", "Say what it isn't") und "Ninety nights to disagree with us".
- "The short version: Founded 2026 · Ships to UK, US, Canada, Australia · Home trial 90 nights · Dispatch 1–2 business days · Support reply Within one working day · Team 12 people".

**Kontakt:** Kontaktformular, "support@pleene.com", "Tel.: +1 (205) 360-5811" (US-Vorwahl), Servicezeiten "Monday through Friday, 9:00 a.m. to 5:00 p.m. (GMT)".

**Weitere, derzeit nicht beworbene Funnel-Seiten** (existieren, aber keine aktive Ad im Inventar):

- `/pages/adv-9r` ("Pleene EasyRest™ Duvet - 10 Reasons TB1")
- `/pages/adv10r-2` ("10 Reasons TB2")
- `/pages/easyrest-tb` (TB3)
- `/pages/tb-5` (TB5)
- `/pages/easyrest-duvet`
- `/products/easyrest-pdp` ("Pleene EasyRest™ 2in1 Duvet")
- `/products/easyrest-everyday-duvet`
- `/products/pleene-easyrest-duvet-2in1`
- `/pages/tb-1` bis `tb-4` und `tb-7` liefern 404.

Daraus folgt, dass Listicles ("10 Reasons") und mehrere Advertorial-Iterationen getestet wurden; tb-6 ist die aktuell aktive.

---

### 3.13 Offene Punkte (n/a bzw. nicht verifiziert)

- **Checkout-Inhalte** wurden bewusst nicht geöffnet: Versandoptionen, Steuern, Post-Purchase-Upsells, ob Package Protection im Checkout vorausgewählt ist und ob die Gratis-Kissenbezüge erscheinen. Alles n/a.
- **Geo-Weiterleitungen** (Elevate US/CA auf Comforter; pleene.com auf pleene.uk für GB-IPs) haben im Test nicht ausgelöst bzw. waren mangels GB-IP nicht prüfbar. Nicht verifiziert.
- **UGC-Videos "Peter", "Brian", "Dave"** wurden nicht transkribiert: Es gibt keine lokale Speech-to-Text-Software und keine Transkripte im Inventar. Die Dauern sind bekannt (101 s / 42 s / 53 s). Die Zuordnung der Namen zu den Dateien ist nicht verifiziert.
- **Tatsächliche Lagerbestände** (z. B. Hearth Red) sind öffentlich nicht verfügbar.
- **"As featured in"** (STARTUPS, new!, The Times, Fabulous): keine Belege auf der Seite, nicht verifiziert.
- **Herkunft der "✓ Verified"-Testimonials und Galerie-Zitate:** nicht in Trustpilot oder Judge.me auffindbar, nicht verifiziert.
- **Zuordnung mehrerer Web-Pixel** (siteId, storeId, archive-digger, marketerIds): nicht verifiziert.
- **AU-Seite `/products/pleene-easyrest-quilt`:** Ziel der AU-Weiterleitung, nicht analysiert, da keine Ad im Inventar dorthin führt.

---

### 3.14 Dateien

Alle Pfade relativ zu `/tmp/claude-0/-home-user-paw-friends-support-bot-/fdae0922-7feb-5884-bf18-6d4ea4ec6336/scratchpad/`.

- Screenshots Above the Fold und ganze Seite, mobil und Desktop: `wf/funnel/render/com_products_easyrest_*`, `com_products_easyrest-comforter_*`, `com_products_easyrest-duvet_*`, `com_pages_tb-6_*`, `com__*` (Home), `misc_about_mobile.png`, `misc_track_mobile.png`, `misc_contact_mobile.png`
  - Dateien `_atf_t4.png` zeigen den Zustand nach 4 s mit Pop-up, `_atf_clean.png` den Zustand ohne Pop-up.
  - Texte: `_full.txt`, Überschriften: `_outline.json`, Sections: `_sections.json`.
- Kontaktbögen: `wf/funnel/sheets/` (Seiten, Galerien `gallery_er.png` und `gallery_cf.png`, `testimonial_videos.png`).
- Warenkorb: `wf/funnel/cart/` (`bars_*_drawer.png|txt`, `*_cartpage.png|txt`, `cart_*_variantscan.png`, Logs `cart_*.log` und `bars_*.log`, `bundle_prices.txt`, USD: `us_comforter_*.png|txt|log`).
- Detailbilder: `wf/funnel/gallery_view/` (Testimonial-Texte, `size_table.jpg`, `wm_table.jpg`, `cartpage_top.png`).
- Währungsprobe: `wf/funnel/probe_currency.log`.
- Roh-HTML und JSON: `a3dl_html/` (inkl. Policies, Produkt-JSON GB/US, `elevate_block.txt`), Klaviyo: `a3dl_klaviyo/forms_v7.json`.


## Teil 4 – Bewertungen und Einwände

Stand: 08.10.2026. Quellen: Trustpilot `uk.trustpilot.com/review/pleene.com` (der Aufruf von `/review/pleene.uk` liefert dieselbe Business Unit, Canonical-URL pleene.com), Judge.me-Widget der Produktseite (Shop `sq48au-70.myshopify.com`, Produkt-IDs 15775652118860, 15843626418508, 16081090838860). Rohdaten aller Bewertungen: `wf/reviews_all.json` (Trustpilot 291, Judge.me 172 plus 6 shopweite Zusatzbewertungen). Referenzen: T001–T291 = Trustpilot, J001–J172 = Judge.me, jeweils aufsteigend nach Datum. Zitate wörtlich im Original (inklusive Tippfehlern).

### 4.1 Zusammenfassung

- **Bewertungsbasis ist dünn, aber sehr positiv:** Trustpilot 291 Bewertungen (TrustScore 4,8; 86 % 5★, 2,7 % 1–3★), alle seit dem 01.08.2026. Das Judge.me-Widget auf der Produktseite („172 reviews“, Ø 4,82) besteht zu 154 von 172 aus **wörtlich von Trustpilot importierten** Texten; nur 18 Judge.me-Bewertungen sind eigenständig.
- **Der Import ist kuratiert (starkes Muster, Mechanismus nicht verifiziert):** Von den 168 Trustpilot-Bewertungen bis zum letzten Import (12.09.2026, T001–T168) wurden 154 von 162 positiven übernommen, aber **0 von 6 negativen** und **0 von 7 Bewertungen, die „China“ erwähnen**; ebenso nicht T143 (Amazon-Preisvergleich). Auf der Produktseite gibt es deshalb **keine einzige 1- oder 2-Sterne-Bewertung**.
- **Einwand Nr. 1 ist die Lieferzeit, nicht das Produkt:** 51 Trustpilot-Bewertungen (17,5 %) nennen lange oder verzögerte Lieferung, davon 46 trotzdem mit 4–5★. Im September lag der Anteil bei 26 % (34 von 133). 11 Bewertungen thematisieren Versand aus China/USA bzw. die intransparente Herkunft trotz „London“-Adresse.
- **Produktprobleme sind selten und mild:** Knitterfalten durch Vakuumverpackung (7), Größe (10, gemischt: zu knapp vs. sehr großzügig, Fehlbestellungen), Verarbeitung (5, darunter 1★ „unfinished“), Farbe (3). **Kein einziger Bericht über tatsächliches Verklumpen oder schlechten Geruch.** Wärme: nur 3 negative Erfahrungen (2× zu warm, 1× zu dünn), aber 14 Käufer schreiben ausdrücklich, dass der Winter noch nicht getestet ist; das ist der größte offene Produkteinwand im Oktober.
- **Häufigster Vorab-Einwand der Käufer: „zu dünn/zu leicht, um warm zu halten“** (14 Bewertungen, die diese Skepsis nennen und auflösen). Pleene adressiert diesen Einwand in den Ads bereits („Too Thin For Winter? Look Closer.“, „Warm Enough For A British Winter“).
- **Rückgabeversprechen vs. Realität:** Die Ads werben mit „90 nights to try it risk-free“. Zwei Käufer berichten, dass eine Rücksendung nach China „really expensive“ bzw. „too much“ sei und stattdessen Teilerstattung/Rabatt angeboten wurde (T055, T119: "They say a free return - no they don’t").
- **Lob-Lücken (oft gelobt, in Ads nicht genutzt):** Weichheit/Haptik (46 Bewertungen vs. 1 Ad), Qualität/Verarbeitung (55 vs. 0 echte Qualitätsaussage), besserer Schlaf (28 vs. 0), großzügige Größe/bleibt auf dem Bett/Füße bedeckt (24 vs. 0), Service/Kommunikation (28 vs. 0), Preis-Leistung (21 vs. 0, Ads nur mit Rabatt), konkrete Lebenslagen wie Arthritis, Witwer, Chemo, Mobilität (42 vs. 9 abstrakte „Independence“-Varianten).
- **Umgekehrt nutzen die Ads Themen, die Käufer kaum nennen:** Hygiene/Allergie/Frische steckt in 59 von 137 Ads (22 von 61 Textvarianten), aber nur in 8 von 283 positiven Bewertungen (3 %); das Versprechen „Hypoallergenic and kind to sensitive skin“ bestätigt keine einzige Bewertung. Wechseljahre/Nachtschweiß: 0 Ads, 3 Bewertungen (alle von Männern).
- **Käuferprofil:** überwiegend ältere Briten (91,8 % GB), viele Senioren und Menschen mit körperlichen Einschränkungen (Arthritis, Rücken, Beine, Herz, Krebs/Chemo, Mobilität), Witwer und Alleinlebende, Paare. Nach Vornamen sind **56 % der Bewerterkonten männlich** (157 von 280), 31 % weiblich. Mehrfachkäufe sind häufig (Gästezimmer, weitere Betten).
- **Auffälligkeiten:** (1) Start mit 37 Bewertungen in gut 5 Stunden am 01.08.2026 (erster Tag des Profils) plus 13 am 02.08.; (2) die einzigen 8 Foto-Bewertungen auf Judge.me entstanden am 06.06.2026 innerhalb von 3 Minuten 23 Sekunden, keine davon verifiziert; die Fotos deuten auf kontinentaleuropäische Schlafzimmer hin (Bildeindruck, nicht verifiziert); (3) 3 Judge.me-Bewertungen mit Datum 2025-08 bis 2026-04, also vor allen echten Käuferbelegen; (4) **Pleene antwortet öffentlich auf keine einzige Bewertung** (0/291 Trustpilot, 0/172 Judge.me), obwohl ein bezahltes Trustpilot-Abo aktiv ist; (5) seit September wachsen Bewertungen aus Australien/Kanada/USA (Oktober: 13 von 44), teils zum zweiten Produkt ZipSheet.

### 4.2 Zahlen

**Plattformen im Überblick**

| Kennzahl | Trustpilot (pleene.com = pleene.uk) | Judge.me Produktseite EasyRest |
|---|---|---|
| Angezeigte Gesamtzahl | 291 (Kopfzeile); Sternfilter 8 + 32 + 251 = 291 | „Based on 172 reviews“ |
| Erfasst | 291 (Abgleich: identisch) | 172 (Abgleich: identisch) |
| Ø Sterne | 4,80 (angezeigter TrustScore 4,8) | 4,82 (Widget) |
| 5★ / 4★ / 3★ / 2★ / 1★ | 251 / 32 / 2 / 1 / 5 | 142 / 29 / 1 / 0 / 0 |
| Anteil 1–3★ | 8 = 2,7 % | 1 = 0,6 % |
| Zeitraum | 01.08.2026 – 08.10.2026 | 03.08.2025 – 12.09.2026 |
| Label „Invited“ | 2 (0,7 %; T050, T109, Quelle „BasicLink“) | n/a (Judge.me-Badges siehe unten) |
| „Verified“ | 0 | „verified_buyer“: 4 (2,3 %) |
| Öffentliche Antworten von Pleene | 0 von 291 (Trustpilot: replyPercentage 0, 6 negative Bewertungen, 0 beantwortet) | 0 von 172 |
| Fotos / Videos | Trustpilot zeigt keine Bewertungsfotos (n/a) | 8 Bewertungen mit Foto (4,7 %), 0 Videos |
| Herkunft der Bewertungen | 289 „Organic“, 2 „BasicLink“ | 154 textgleich mit Trustpilot (Import), 18 eigenständig |

**Trustpilot-Profil (Business-Unit-Daten aus `__NEXT_DATA__`):** Kategorie „Bedding Shop“; `countryCode: HK`, Kontakt `support@pleene.com`, Land HK; `claimedDate` 20.08.2026; `isMerged: true`, `hasBusinessUnitMergeHistory: true` (pleene.uk wurde offenbar in pleene.com zusammengeführt; die ID der Business Unit codiert als Erstellungszeit den 19.08.2026, abgeleitet, nicht verifiziert); `verifiedPaymentMethod: true`; `isUsingPaidFeatures: true`, `hasSubscription: true`; `isCollectingReviews: false`, `hasRecentlyInvitedUsers: false`; `hasCollectedIncentivisedReviews: false`. Die Standardansicht ohne Filter listet 280 statt 291 Bewertungen (Trustpilot-interne Ansicht, Grund n/a); über Sternfilter und Zeitraumfilter „last12months“ sind alle 291 erreichbar.

Trustpilot-KI-Zusammenfassung (wörtlich): "Looking at 271 reviews, reviewers overwhelmingly had a great experience with this company. [...] However, some people mentioned that delivery times took longer than expected to arrive at their homes. A few customers also noted that the items arrived heavily creased because of the tight vacuum packaging, requiring some extra patience to smooth out."

**Trustpilot nach Land:** GB 267, AU 12, CA 6, US 3, CY 1, JE 1, FR 1 (GB = 91,8 %).

**Trustpilot-Bewerter:** 291 Bewertungen von 280 Konten; 10 Konten schrieben 2–3 Bewertungen (zusammen 21). Median der Trustpilot-Bewertungen pro Konto: 10; Konten mit nur dieser einen Bewertung: 28. Ø Textlänge (Median) 198 Zeichen. 5 Bewertungen wurden nachträglich aktualisiert (T143, T177, T185, T194, T244).

**Judge.me im Detail:** Anbieter der Bewertungs-App ist Judge.me (Produktseiten-HTML enthält 1.259 `jdgm`-Verweise; Daten vollständig über die Judge.me-Widget-API `reviews_for_widget`, 6 Seiten à 30, sowie das shopweite Widget abgerufen). Dieselben 172 Bewertungen erscheinen auf allen drei Produkt-IDs („Pleene EasyRest™ Duvet“ zweimal, „Pleene EasyRest™ Comforter“). Badges: `review_collected_from_another_provider` 158, `review_collected_from_store_visitor` 11, `review_collected_via_store_invitation` 3. Von den 154 Trustpilot-Importen tragen 147 die Uhrzeit 10:00 (nur Datum übernommen). Bei 20 importierten Texten weicht die Sternzahl von Trustpilot ab (14× Trustpilot 5★ → Judge.me 4★, 5× 4★ → 5★, 1× 5★ → 3★: T109/J121); Ursache n/a. Shopweit zeigt Judge.me 176 Produktbewertungen (172 EasyRest + 4 ZipSheet™ vom 12./13.07.2026, alle 5★, nicht verifiziert) und 2 Shop-Bewertungen (21./22.06.2026).

**Judge.me 1–3★ (wörtlich, vollständig):** Es gibt genau eine:
- J121 · 2026-08-30 · 3★ · Norman Walton · Land n/a · verified_buyer: nein · Antwort Pleene: keine · Titel: "Ok but too much security checks" · Text: "Ok but too much security checks from email and face book" – identisch mit Trustpilot T109, dort aber **5★**.

**Kuratierter Import (Detail):** Trustpilot T001–T168 (bis 12.09.2026) = 168 Bewertungen. Importiert: 154. Nicht importiert: alle 6 mit 1–3★ (T036, T059, T094, T115, T119, T127) sowie 8 positive: T044, T055, T069, T107, T124, T150 (alle erwähnen „China“), T143 (Amazon-Vergleich, „very expensive“) und T158 (ZipSheet). Die einzige weitere China-Erwähnung (T278) stammt von nach dem Import. Zufällig wäre ein solches Muster sehr unwahrscheinlich; ob manuell oder per Filter ausgewählt wurde, ist nicht verifiziert. Seit dem 12.09.2026 kamen keine neuen Judge.me-Bewertungen hinzu, während Trustpilot 123 neue erhielt.

### 4.3 Kategorien: Probleme und Einwände

Basis: alle 291 Trustpilot-Bewertungen, also auch Kritik innerhalb von 4–5★-Bewertungen (die meisten Einwände stehen dort). Zählung = Anzahl Bewertungen mit Erwähnung, manuell codiert, Mehrfachzuordnung möglich. Die 18 eigenständigen Judge.me-Bewertungen enthalten nur drei kritische Punkte (J051, J110 Lieferdauer; J015 Wunsch nach Weiß).

**Produkt**

| Kategorie | n | Sterne (5/4/3/2/1) | Referenzen |
|---|---|---|---|
| W1 Wärme: zu warm | 2 | 0/2/0/0/0 | T056, T170 |
| W2 Wärme: zu kalt / zu dünn | 1 | 0/0/0/1/0 | T127 |
| W3 Wärme: Wunsch nach wärmerer Version / Zusatzdecke im Winter | 3 | 3/0/0/0/0 | T015, T233, T260 |
| W4 Wärme: Winter noch ungetestet (Vorbehalt in positiver Bewertung) | 14 | 9/5/0/0/0 | T026, T057, T088, T107, T124, T125, T146, T149, T173, T179, T188, T194, T218, T232 |
| G Größe (zu knapp, sehr großzügig, falsch bestellt, falsch geliefert) | 10 | 7/2/1/0/0 | T022, T035, T055, T119, T146, T153, T232, T239, T250, T270 |
| M Material/Verarbeitung (offene Naht, loser Faden, Füllung tritt aus, "unfinished", Reißverschluss) | 5 | 0/3/1/0/1 | T028, T119, T180, T217, T277 |
| Wa Waschen (knapp in der Maschine, Restwasser, Sorge vor Verklumpen) | 4 | 4/0/0/0/0 | T103, T126, T141, T270 |
| Tr Trocknen (länger als 2 Std.) | 2 | 2/0/0/0/0 | T019, T262 |
| K Knittern durch Vakuumverpackung | 7 | 2/4/0/0/1 | T008, T014, T042, T094, T118, T139, T239 |
| V Verklumpen (tatsächlich aufgetreten) | 0 | 0/0/0/0/0 | – |
| Ge Geruch (negativ) | 0 | 0/0/0/0/0 | – |
| F Farbe (zu grell, weicht von Website ab, Verwechslung) | 3 | 2/1/0/0/0 | T068, T198, T282 |
| S Sonstiges/Wünsche (Muster, Weiß, mehr Farben, Top Sheet, Treuerabatt) | 8 | 7/1/0/0/0 | T043, T051, T054, T146, T189, T226, T237, T264 + Judge.me eigen: J015 |
| P Preis hoch | 3 | 1/2/0/0/0 | T008, T097, T143 |

**Lieferung**

| Kategorie | n | Sterne (5/4/3/2/1) | Referenzen |
|---|---|---|---|
| L1 Lieferdauer lang/verzögert | 51 | 31/15/1/1/3 | T016, T020, T028, T044, T054, T056, T067, T070, T094, T104, T107, T115, T119, T124, T125, T127, T132, T134, T136, T139, T143, T150, T152, T156, T159, T162, T167, T168, T174, T180, T183, T187, T190, T191, T193, T194, T198, T202, T204, T205, T208, T216, T218, T226, T240, T248, T256, T261, T273, T279, T287 + Judge.me eigen: J110, J051 |
| L2 Zustellproblem (beschädigt, falsche Adresse, nicht angekommen, falsche Ware, Kurieranweisung) | 9 | 3/4/0/0/2 | T021, T060, T115, T125, T138, T153, T162, T240, T291 |
| L3 Versand aus China/USA bzw. Herkunft intransparent | 11 | 6/3/1/0/1 | T044, T055, T059, T069, T107, T119, T124, T132, T150, T175, T278 |
| L4 Lieferung positiv (schnell, pünktlich, gut verpackt, Tracking) | 33 | 32/1/0/0/0 | T007, T011, T015, T019, T023, T050, T051, T069, T077, T089, T106, T110, T116, T122, T128, T131, T147, T160, T172, T182, T196, T206, T207, T212, T213, T214, T234, T235, T239, T252, T267, T278, T283 |

**Kundenservice**

| Kategorie | n | Sterne (5/4/3/2/1) | Referenzen |
|---|---|---|---|
| K1 Service negativ (keine/späte Antwort, Erstattung zäh) | 5 | 1/0/0/1/3 | T115, T127, T185, T240, T277 |
| K2 Rückgabe/Umtausch (Rücksendung nach China zu teuer, Teilerstattung statt Retoure) | 3 | 2/0/1/0/0 | T055, T119, T270 |
| K3 Bestellprozess/Angebot (Upsell-Seite, Gratis-Kissen, Sicherheitschecks, Aktion verpasst, versehentliche Zusatzbestellung) | 5 | 3/0/1/0/1 | T036, T059, T109, T113, T114 |
| K4 Service positiv (Ersatz, Erstattung, schnelle Antwort, Kommunikation) | 22 | 18/4/0/0/0 | T020, T021, T055, T075, T077, T082, T089, T141, T143, T153, T164, T174, T185, T213, T231, T232, T244, T270, T272, T273, T282, T291 |
| K5 Erstattung/Gutschrift erwähnt | 6 | 1/3/1/0/1 | T020, T055, T119, T143, T244, T277 |

**Erwartung vs. Realität**

| Kategorie | n | Sterne (5/4/3/2/1) | Referenzen |
|---|---|---|---|
| E1 Erwartung enttäuscht / Versprechen nicht gehalten | 10 | 1/4/1/1/3 | T059, T094, T107, T119, T127, T170, T198, T226, T250, T277 |
| E2 Vertrauen/Scam-Angst vor oder nach dem Kauf | 11 | 7/1/0/0/3 | T020, T052, T059, T076, T098, T115, T192, T240, T270, T276, T283 |
| E3 Erwartung übertroffen nach Skepsis | 32 | 31/1/0/0/0 | T005, T016, T040, T042, T047, T051, T052, T054, T063, T076, T098, T099, T108, T120, T122, T126, T146, T150, T192, T223, T229, T241, T246, T261, T262, T269, T270, T276, T284, T288, T289, T290 |

**Belegzitate Produkt**

- Wärme zu warm: "Got rather hot but light weight allows for it to be thrown off easily." (T056, 4★); "still felt hot sometimes and had to throw the Pleene EasyRest duvet off myself on some occasions" (T170, 4★)
- Zu dünn: "Its not warm too thin, waste of money" (T127, 2★)
- Wärmere Version gewünscht: "do you make heavier one for the winter." (T233, 5★); "Will probably add a weighted blanket in mid winter" (T260, 5★); "in winter, if it is cold, I will use two at once" (T015, 5★)
- Winter-Vorbehalt: "As it is still summer, I cannot say how warm it will be for winter nights. It is claimed that the duvet will be like a 10 tog in winter. I will have to wait and see." (T107, 4★); "I am waiting to see how I cope with it during the winter months." (T179, 5★)
- Größe: "I bought a double sized which is a little undersized." (T035, 5★); "One king size quilt would be far too small." (T239, 5★); "I like a king size, but it is so generous I think a double would have been ok!" (T146, 5★); "It seems much bigger than a regular “Flat”, doesn’t fit as nicely as the shown in the advertisement." (T250, 4★) (ZipSheet)
- Verarbeitung: "Regretably the duvet arrived unfinished and very poor quality." (T277, 1★); "was clearly ‘bubbled’ with lining coming out through a series of minute minute punctures in the surface" (T119, 3★); "I did notice that there was a lone loose thread in the middle of a line of stitch." (T180, 4★); "the only thing was the pillow case seam was open" (T028, 4★)
- Waschen: "had a little problem on the wash for the double as it retained abit of water" (T141, 5★); "although it is a tight fit in my washing machine it washed well" (T126, 5★); "My biggest concern is, will the filling bunch up during washing?" (T103, 5★)
- Trocknen: "Drying takes about 4hours but all good." (T019, 5★); "dried inside within 1 day" (T262, 5★)
- Knittern: "it was so tightly vacuum packed, thousands of tiny creases still remain even after a wash and a week’s use." (T118, 4★); "the pillowcases are still very creased, and I feel loathe to iron them in case I spoil them" (T008, 4★); "Item is very creased" (T094, 1★)
- Verklumpen: kein Fall; Gegenbeleg "after the first wash no "bunching" or lumpiness to the filling (unlike my last quilt)" (T270, 5★)
- Geruch: kein negativer Fall; Gegenbeleg "no unpleasant odour as with some ordinary duvets" (T067, 5★)
- Farbe: "sunset red .much too bright,husband says its like having an RAF life raft on the bed" (T068, 4★); "I think the colour looks different than it appeared on the website" (T198, 5★)
- Wünsche: "Only thought I had is that they do not do patterened ones" (T043, 5★); "I just wish you also did it in white" (T051, 5★); "you need to have a matching top sheet" (T264, 5★); "I would have appreciated a loyalty discount for being a returning customer." (T054, 5★)
- Preis: "very expensive compared with buying from the likes of Amazon" (T143, 4★); "A bit pricey but worth having." (T097, 5★)

**Belegzitate Lieferung**

- Dauer: "Took 13 days instead of 6 day advertised" (T094, 1★); "Took over 3 weeks to be delivered" (T143, 4★); "my order took a long time to be delivered so please evaluate your logistical processes." (T054, 5★)
- Zustellung: "They than claimed that Evri had the parcel in thier london hub days ago you Evri have no record of the tracking numbers given" (T240, 1★); "being delivered to a similar sounding wrong address" (T060, 5★); "our original order was damaged in transit, they promptly sent a replacement" (T021, 5★)
- Herkunft: "despite the company being based in London, the product actually has to travel all the way from China" (T107, 4★); "The address 128 City Road, London (EC1V 2NX) is a well-known mass-registration office" (T059, 1★); "Then when the parcel arrived in UK it went Stansted, Braintree, Midlands, Cardiff (?), before getting delivered to us in East Anglia." (T044, 4★)
- Positiv: "I was able to follow my parcels voyage on its complete journey until it arrived which took a week." (T278, 5★); "Prior to ordering, I read quite a few reviews saying that the delivery time was quite long.  I didn’t find that" (T196, 5★)

**Belegzitate Kundenservice**

- Negativ: "Customer support has taken 5 days to respond and then didn’t help just said out for delivery." (T115, 1★); "no reply to email" (T127, 2★); "I am now trying to be reimbursed, to which there seems to be reluctance. I have been offered a free one, but it would not be free as I have already paid for unusable goods." (T277, 1★)
- Rückgabe: "A lovely customer service lady explained that it would be really expensive to return the item as the company was based in China." (T055, 5★); "They say a free return - no they don’t I was told my miss-order would cost me too much to return to China so they offered me a percentage off another order which I accepted." (T119, 3★)
- Bestellprozess/Upsell: "I made the purchase, and got another page asking me to confirm an order. I thought I was just confirming the purchase I'd made (probably wasn't concentrating) but it added a second Duvet, that I didn't want) to the order at a discount." (T036, 3★); "Luckily I mistakenly ordered an extra one" (T114, 5★); "Ok but too much security checks from email and face book" (T109, 5★); "it offers two free pillow cases but no indication of this when you come to pay" (T059, 1★)
- Positiv: "The company have been in contact and I am very happy with the outcome" (T185, 5★) (nach "Avoid this company like the plague."); "found Amelia quick to respond with here advice" (T270, 5★); "Updated, I have had a £25 refund from the company with this message." (T143, 4★)

**Belegzitate Erwartung vs. Realität**

- Enttäuscht: "waste of money" (T127, 2★); "Though they did not fully work in the way they described" (T170, 4★); "Thought I’d ordered a top sheet but no." (T226, 4★)
- Vertrauen: "i only saw the advert on facebook and wasn't sure if this would be a scam" (T098, 5★); "pleene has a low security rating" (T020, 4★); "this seems to be a scam" (T115, 1★); "NO STARS CON" (T240, 1★)
- Übertroffen: "THIS IS NOT THE CASE WITH PLEENE." (T076, 5★); "So okay, I admit it, I was completely wrong" (T192, 5★); "I must admit I was sceptical about the claims for the duvet, but I was wrong." (T122, 5★)

**Vorab-Einwände, die Käufer vor dem Kauf hatten (aus positiven Bewertungen)**

| Einwand vor dem Kauf | n | Referenzen | Beleg |
|---|---|---|---|
| Zu dünn/leicht, um warm zu halten | 14 | T005, T016, T150, T159, T173, T229, T232, T237, T241, T245, T246, T262, T288, T289 | "I thought it wouldn't be warm enough being quite thin, but it's lovely and warm." (T241, 5★) |
| Online-/Facebook-Kauf, Angst vor Betrug | 8 | T052, T076, T098, T099, T192, T270, T276, T283 | "I, like you, am somewhat suspicious of claims by companies on FB etc" (T192, 5★) |
| Passt nicht in die Waschmaschine | 4 | T107, T146, T157, T270 | "I did not believe the duvet would fit into the washing machine" (T146, 5★) |
| Trocknet im Winter nicht schnell genug | 2 | T043, T146 | "I ordered two duvets as I was worried about getting it dry in the winter." (T043, 5★) |
| Füllung verklumpt beim Waschen | 1 | T103 | "will the filling bunch up during washing?" (T103, 5★) |

### 4.4 Lob-Lücken: Was Käufer loben und die Ads nicht nutzen

Methode: Themen-Suchmuster über alle 283 Trustpilot-Bewertungen mit 4–5★ (Judge.me nicht separat gezählt, da 154 von 172 Kopien sind) und über Titel+Text aller 137 aktiven Ads aus `agent1_enriched.json` (61 unterschiedliche Titel-Text-Kombinationen). Treffer wurden manuell gesichtet und offensichtliche Fehltreffer entfernt; Toleranz etwa ±2–3. Angle-Codes nach Vorgabe (A–F).

| Thema (Angle) | Bewertungen 4–5★ (n von 283) | Ads (n von 137) | Ad-Varianten (n von 61) | Einordnung |
|---|---|---|---|---|
| Weich / Haptik / Stoff (F) | 46 (16 %) | 1 | 1 | große Lücke: nur „fluffy … feels amazing“ in 1 Ad |
| Qualität / Verarbeitung (F) | 55 (19 %) | 4 | 2 | große Lücke: Ads sagen nur „Quilted in place, no cold spots“ |
| Besserer Schlaf (explizit) (F) | 28 (10 %) | 0 | 0 | Lücke: keine Ad verspricht besseren Schlaf |
| Bleibt auf dem Bett / großzügige Größe / Füße bedeckt (F) | 24 (8 %) | 0 | 0 | Lücke: Größe nur als Größen-Erklärung („What bed have you got?“) |
| Service / Kommunikation / Tracking (F) | 28 (10 %) | 0 | 0 | Lücke (und Gegengewicht zum Lieferzeit-Einwand) |
| Preis-Leistung (F) | 21 (7 %) | 0 | 0 | Lücke: Ads nutzen nur Rabatt („30% off + 2 FREE“), kein „worth it“ |
| Optik / Farbe / Schlafzimmer aufgewertet (F) | 52 (18 %) | 13 | 4 | teilweise: Farbe nur als Knappheit/Neuheit, nie „sieht toll aus/Zimmer aufgewertet“ |
| Wiederkauf / weitere Betten / Gäste (F) | 50 (18 %) | 8 | 3 | teilweise: nur „Spare Bed“-Story |
| Körperliche Erleichterung / Alter / Gesundheit / allein (E) | 42 (15 %) | 13 | 9 | teilweise: Ads abstrakt („Independence“, „by yourself“), keine konkreten Beschwerden |
| Empfehlung / Familie und Freunde (F) | 39 (14 %) | 14 | 4 | teilweise: „Everyone said it“, „loved by hundreds“ |
| Leicht / nicht schwer (B) | 72 (25 %) | 25 | 14 | genutzt („without the weight“), aber unterrepräsentiert |
| Temperatur (warm/kühl/regulierend) (B) | 105 (37 %) | 46 | 11 | genutzt (Winter-Wärme), Sommer-Kühle kaum |
| Bequem / komfortabel (F) | 72 (25 %) | 24 | 19 | genutzt |
| Skepsis überwunden (F) | 34 (12 %) | 26 | 7 | genutzt (Einwandbehandlung „Too Thin For Winter?“, „Check This Before You Buy“) |
| Kein Bezug mehr / Kampf mit dem Bezug (C) | 83 (29 %) | 108 | 46 | Kernbotschaft, deckungsgleich |
| Ganze Decke in der Waschmaschine (A/C) | 111 (39 %) | 114 | 48 | Kernbotschaft, deckungsgleich |
| Schnell trocken (C) | 50 (18 %) | 79 | 25 | in Ads stärker als in Bewertungen |
| Bett schnell gemacht / Bettwechsel leicht (C) | 30 (11 %) | 41 | 11 | in Ads stärker als in Bewertungen |
| Kissenbezüge (F-Angebot) | 16 (6 %) | 51 | 11 | Ads stark (Gratis-Kissen), Käufer erwähnen sie als „bonus“ |
| Hygiene / Allergie / Frische / Geruch (A) | 8 (3 %) | 59 | 22 | **umgekehrte Lücke:** Ads stark, Käufer kaum |
| Nachtschweiß / Schwitzen (B) | 3 (1 %) | 0 | 0 | beide schwach; Wechseljahre nie erwähnt |
| Paar mit unterschiedlichem Wärmeempfinden (B) | 2 (1 %) | 0 | 0 | Lücke (klein): Paare mit unterschiedlichem Wärmeempfinden |
| Haustiere (F) | 2 (1 %) | 3 | 1 | beide schwach |
| Kein Bügeln (F) | 2 (1 %) | 1 | 1 | beide schwach |

Geschenk (Angle D): Kauf für andere oder als Geschenk in 7 Bewertungen (T133 an sich selbst zum 84. Geburtstag, T171 Mutter, T196 Sohn zu Weihnachten, T200 Sohn, T252 Freund, T289 Sohn, T283 ZipSheet für die Mutter); in den Ads 0 Geschenk-Erwähnungen.

**Belegzitate zu den wichtigsten Lücken**

- Weichheit/Haptik: "Soft as a baby’s tush" (T217, 4★); "It is like lying asleep in a floating  cloud." (T133, 5★); "This Pleene duvet is light, sumptuously soft and easier to live with." (T117, 5★); "It seems to hug every part of your body" (T113, 5★); "Crisp yet soft." (T273, 5★)
- Qualität/Verarbeitung: "Good quality materials and well sewn." (T077, 5★); "So quality first rate and item well worth the money." (T040, 5★); "Excellent quality - better than expected." (T164, 5★); "I'm very happy with the colour, quality, stitch and warmth." (T248, 5★)
- Besserer Schlaf: "First night on I had a comfortable complete nights sleep.  I was suffering from broken nights previously." (T192, 5★); "I generally don’t sleep more than 4/5 hours at a time but with my pleene I’m getting up to 7 hours" (T212, 5★); "I have never had so many nights of uninterrupted sleep" (T133, 5★); "So far after a week we have all been sleeping better due to feeling a more comfortable temperature in bed." (T123, 5★)
- Größe/bleibt liegen/Füße: "I liked the idea that I could get a long cover that would cover my feet perfectly." (T066, 5★); "The sizing is also very generous and there is plenty of overhang which I like." (T203, 5★); "doesn't slip off the bed during the night" (T103, 5★); "With a duvet and cover I always ended up with too much duvet at the feet end and not enough at the head end!!" (T120, 5★); "I got a super king for a king size bed as both of us are quilt hoggers" (T202, 5★)
- Service/Kommunikation: "Even though the order took a little longer to reach me than expected, the communication was excellent throughout." (T164, 5★); "Although delivery took a little while  I was kept up to date throughout" (T174, 5★)
- Preis-Leistung: "real value for money in todays climate" (T037, 5★); "Definitely value for money." (T091, 5★)
- Optik/Schlafzimmer: "my bedroom has been transformed into an amazing  bedroom" (T009, 5★); "It looks great on the bed it really smarten the bed up" (T096, 5★); "The spring green is a lovely restful colour that provides a calm atmosphere for my bedroom." (T181, 5★); "as the bedroom now looks like a bedroom" (T251, 5★)
- Wiederkauf/weitere Betten: "In fact we have just ordered our 3rd set" (T140, 5★); "have ordered another 2 for  my son and will be replacing all the bedding in the house." (T289, 5★); "Having friends to stay the night will now be quick and easy to prepare and quick and easy to wash afterwards." (T175, 5★)
- Paare: "I like to be warm and cosy whereas my husband wants to be cool and unrestricted by quilts and additional quilt covers. The Pleene coverless duvet delivers for both of us!" (T054, 5★)
- Nachtschweiß: "Overall it did stop my night sweats and waking up to wet sheets so they did work." (T170, 4★); "it has been very hot at night but have not  had any perspirationover the night time" (T057, 5★); "no sweating overheating under it" (T105, 5★)
- Zum Vergleich Hygiene (umgekehrte Lücke), die einzigen konkreten Käufer-Belege: "having a quilt I can wash I no longer wake up with a bunged up nose" (T202, 5★); "so no guilt for us or short stay visitors!! ( don’t tell’em!)" (T027, 5★)

**Ad-Versprechen, die Bewertungen relativieren:** „90 nights to try it risk-free“ vs. T055/T119 (Rücksendung nach China zu teuer); „dry in 2 hours“ bestätigt von T140 ("in 2hrs"), J011 ("dry in about 2 hours"), aber T019 ("about 4hours") und T262 ("within 1 day"); „10.5 tog, every bit as warm as a winter duvet“ wird im Oktober von 14 Käufern noch als ungetestet markiert; „Hypoallergenic and kind to sensitive skin“ ohne Käuferbeleg; Lieferzeit: T094 nennt "6 day advertised".

### 4.5 Voice of Customer: das alte Problem in Käuferworten

**Bettbezug: Kampf, Wrestling, Erschöpfung** (18 Belege)

- "Absolute magic just helped an old man to enjoy his duvet without the continuous fight." (T001, 5★)
- "My wife always looked forward to changing our duvet cover (not really!) . . . bought these. . . now i dont hear any more cursing and frustration venting!" (T140, 5★)
- "I no longer end up inside the duvet covet when I'm changing it, because there isn't a cover!" (T276, 5★)
- "No more wrestling and disappearing in duvet cover" (T265, 5★)
- "I no longer get twisted up in duvet covers" (T126, 5★)
- "the thought of arguing with a duvet has lost its attraction" (T175, 5★)
- "if you have ever struggled to get your quilt into the cover then you'll what a nightmare it can be" (T163, 4★)
- "the duvet cover nightmare is a thing of the past!" (T203, 5★)
- "Life's too short to fight with duvet covers!" (T260, 5★)
- "the putting of a quilt into a cover could be exhausting!" (T257, 5★)
- "I got so exhausted changing the bed, with the duvet" (T095, 5★)
- "changing the bed is no longer the horrendous chore it used to be" (T108, 5★)
- "Changing the bedding, especially on your own with a traditional king size duvet, is a painful chore." (T268, 5★)
- "where i used to struggle to shake out a king size quilt with cover" (T289, 5★)
- "I have battled with a duvet and separate cover for years" (T168, 5★)
- "I had trouble fitting the old style quilts and separate covers" (T030, 5★)
- "without the usual duvet faff" (T038, 5★)
- "trying to change the duvet cover is a job that was almost impossible without doing myself serious injury" (T072, 5★)

**Bezug verrutscht, Füße, Druckknöpfe** (4 Belege)

- "With a duvet and cover I always ended up with too much duvet at the feet end and not enough at the head end!!" (T120, 5★)
- "At last my feet are comfortable and no longer get caught up in a quilt cover's poppers." (T194, 4★)
- "i got feed up that my doona would always slip down to the feet area" (T254, 5★)
- "at no time have I had to flip it to one side and sleep with no cover" (T040, 5★)

**Waschen: die Decke selbst wurde nie oder umständlich gewaschen** (6 Belege)

- "no stripping it down for the washer just shove it all in the washer and it comes out perfect." (T006, 5★)
- "Oh….. and my actual duvet gets washed regularly too!" (T268, 5★)
- "have used a sleeping bag more than once on a clean fitted sheet, whilst waiting for a duvet cover to dry and the duvet itself being returned from the cleaners." (T175, 5★)
- "being able to put them in the washing machine in one piece without having to take covers off and put them back on is a life saver." (T003, 5★)
- "I did not believe the duvet would fit into the washing machine" (T146, 5★)
- "especially if you’ve got a lot of people coming and going as washing is so easy" (T058, 5★)

**Allergie, Frische, Geruch (selten)** (3 Belege)

- "having a quilt I can wash I no longer wake up with a bunged up nose." (T202, 5★)
- "no unpleasant odour as with some ordinary duvets" (T067, 5★)
- "And it fits in the washing machine so no guilt for us or short stay visitors!!" (T027, 5★)

**Hitze, Kälte, Gewicht der alten Decke** (9 Belege)

- "heavy duvets hampered my sleep as I turned over in bed" (T126, 5★)
- "No heavy duvet putting pressure on your feet and being too hot or too cold." (T117, 5★)
- "it's great not have to much weight pressing down on me" (T096, 5★)
- "no longer feel restricted in bed" (T037, 5★)
- "so much better than our bulky old ones" (T044, 4★)
- "Cosy without restrictive weight." (T023, 5★)
- "I am always cold and have the heaviest quilt i can find to keep me warm at night." (T289, 5★)
- "Overall it did stop my night sweats and waking up to wet sheets" (T170, 4★)
- "I like to be warm and cosy whereas my husband wants to be cool and unrestricted by quilts and additional quilt covers." (T054, 5★)

**Alter, Gesundheit, allein leben** (23 Belege)

- "My wife and I are in our 80's and need all the help we can get" (T003, 5★)
- "I am in my late 70s and even though I have changed quilt covers all my life I am now finding it very difficult." (T066, 5★)
- "has eliminated my ongoing worries as to how I shall cope with my bedding as old age advances." (T103, 5★)
- "having limited mobility, it’s a real dream not having to change duvet covers any more." (T025, 5★)
- "With declining mobility I have struggled to change even a single duvet cover." (T290, 5★)
- "I am so pleased that I do not have to change the duvet cover now as I have a bad heart and it takes a lot out of me." (T043, 5★)
- "chemo makes me very fatigued so the fact there is no messing about getting my duvet in a cover is an absolute god send" (T070, 5★)
- "My strength and enery are low." (T231, 5★)
- "This is ideal as couldn’t change the dooner cover." (T231, 5★)
- "I live on my own and have struggled with changing quilt covers for at least 4 years providing me with anxiety and affecting my diabetes." (T079, 5★)
- "The wifes hands are quite bad with Athritis" (T064, 5★)
- "esp if you have arthritus in hands" (T074, 5★)
- "So easy to use, to wash and replace, despite age and arthritis," (T249, 5★)
- "making it more comfortable for my joints" (T047, 5★)
- "Back operation .no more struggling with quilt covers." (T046, 5★)
- "I am elderly, not too fit & am now a widower, so making up the new bed system alone was a joy." (T177, 5★)
- "As a widower living on my own changing the king size  duvet cover on my own was struggle" (T236, 5★)
- "I ordered these after my wife passed away" (T029, 5★)
- "I hadn’t even put the quilt cover on…just pulled it over me in the sheer exhaustion of grief." (T251, 5★)
- "coping with injuries received in a car accident" (T168, 5★)
- "Being 66 with a bad back, changing sheets became a daunting task which I’m sure I put off way too long many times." (T274, 5★)
- "I no longer have to worry about hurting my lower back whilst making the bed" (T284, 5★)
- "She wants to remain independent" (T283, 5★)

**Skepsis gegenüber dem Kauf (Sprache des Einwands)** (6 Belege)

- "I was dubious when I saw how lightweight this quilt was." (T016, 5★)
- "The only thing I worried about were the claims it was warm for such a thin material." (T150, 5★)
- "thought it was too light to be warm" (T288, 5★)
- "Too often you are taken in by amazing ads you see online." (T076, 5★)
- "I've been caught out before with internet orders" (T270, 5★)
- "I didn’t think you could have a quilt all in one that you could put in a washing machine and dry it quickly then put it back on the bed……it’s a miracle." (T269, 5★)

Auffällig: In keiner einzigen Bewertung (0 von 291 Trustpilot, 0 von 172 Judge.me) kommen die Wörter „hygiene“, „mites“, „bacteria“, „germs“, „dust“, „allergy“ oder „sensitive skin“ vor. Ihr Vokabular ist „fight“, „wrestle“, „struggle“, „battle“, „faff“, „nightmare“, „chore“, „exhausting“. Die Lösung beschreiben sie als „game changer“, „life saver“, „god send“, „miracle“, „does what it says on the tin“.

### 4.6 Tempo

**Neue Bewertungen pro Monat (April–Oktober 2026)**

| Monat | Trustpilot neu | TP 5/4/3/2/1★ | TP Ø | TP „Invited“ | TP Antworten Pleene | TP Lieferzeit-Kritik (L1) | TP außerhalb GB | Judge.me neu | davon TP-Import / eigen | JM 5/4/3/2/1★ |
|---|---|---|---|---|---|---|---|---|---|---|
| Apr | 0 | 0/0/0/0/0 | – | 0 | 0 | 0 | 0 | 1 | 0 / 1 | 1/0/0/0/0 |
| Mai | 0 | 0/0/0/0/0 | – | 0 | 0 | 0 | 0 | 0 | 0 / 0 | 0/0/0/0/0 |
| Jun | 0 | 0/0/0/0/0 | – | 0 | 0 | 0 | 0 | 11 | 0 / 11 | 9/2/0/0/0 |
| Jul | 0 | 0/0/0/0/0 | – | 0 | 0 | 0 | 0 | 1 | 0 / 1 | 0/1/0/0/0 |
| Aug | 114 | 103/8/1/0/2 | 4,84 | 2 | 0 | 11 (10 %) | 0 | 110 | 107 / 3 | 93/16/1/0/0 |
| Sep | 133 | 108/21/1/1/2 | 4,74 | 0 | 0 | 34 (26 %) | 11 | 47 | 47 / 0 | 37/10/0/0/0 |
| Okt (1.–8.) | 44 | 40/3/0/0/1 | 4,84 | 0 | 0 | 6 (14 %) | 13 | 0 | 0 / 0 | 0/0/0/0/0 |

Vor April 2026: Trustpilot 0; Judge.me je 1 Bewertung im August 2025 (J001) und November 2025 (J002). Erste Bewertung überhaupt: Judge.me J001 (03.08.2025); erste Trustpilot-Bewertung T001 (01.08.2026, 18:11 UTC). ZipSheet-Bewertungen auf Judge.me (nicht in der Tabelle): 4 im Juli 2026.

Trustpilot pro Tag: August 3,7 (ohne die ersten beiden Tage 64 in 29 Tagen = 2,2), September 4,4, Oktober bisher 5,5. Kalenderwochen: KW31 50, KW32 11, KW33 12, KW34 26, KW35 13, KW36 32, KW37 36, KW38 19, KW39 31, KW40 39, KW41 (05.–08.10.) 22. Spitzentage: 01.08. 37, 02.08. 13, 12.09. 10, 04.10. 10, 05.10. 10, 11.09. 9, 06.10. 9. Wochentage: Samstag 69, Sonntag 54, Montag 45, Dienstag 39, Freitag 38, Mittwoch 24, Donnerstag 22. Uhrzeit (UTC): Schwerpunkt 18–23 Uhr (133 von 291).

Anteil „Invited“: 2 von 291 (0,7 %). Antwortquote Pleene: 0 % auf beiden Plattformen. Private Kontakte gibt es nachweislich (T141 "problem solved as you replied with the satisfied explanation", T143 Erstattung mit Nachricht, T185 Kontaktaufnahme, T277 Angebot eines kostenlosen Ersatzes).

**Auffälligkeiten**

1. **Start-Welle 01.08.2026:** 37 Bewertungen zwischen 18:11 und 23:14 UTC als allererste Bewertungen des Profils (33× 5★, 3× 4★, 1× 3★), dazu 13 am 02.08. = 50 Bewertungen (17 % aller) in zwei Tagen. Erlebnisdaten 26.06.–01.08.2026. Die Konten sind etablierte Trustpilot-Nutzer (Median 9 Bewertungen, nur 2 Erstbewerter), Texte individuell mit Details und Kritik (z. B. T008 Knitterfalten, T036 Upsell-Ärger). Das Muster passt zu einer einmaligen Aufforderung an Bestandskunden per E-Mail/Link (Quelle „Organic“, nicht „Invited“); nicht verifiziert. Hinweise auf gefälschte Inhalte: keine.
2. **Judge.me-Foto-Serie 06.06.2026:** J004–J011 entstanden zwischen 07:36:42 und 07:40:05 UTC (8 Bewertungen in 3 Min. 23 Sek.), alle mit genau 1 Foto, alle „review_collected_from_store_visitor“, keine verifiziert, Namen im Format „Vorname + Initial“ („Emma T.“, „Payton R.“ …). Sie sind **die einzigen Foto-Bewertungen** und bilden die Foto-Galerie des Widgets. Die Fotos (gesichtet, 8 Bilder) zeigen Schlafzimmer mit Merkmalen, die eher auf kontinentaleuropäische Wohnungen hindeuten (u. a. Dreh-Kipp-Fenster, zwei getrennte Decken bzw. Matratzen im Doppelbett, Heizkörper unter dem Fenster; Bildeindruck, nicht verifiziert), während ein Text "Best wishes from Birmingham" sagt. Verdacht auf hinterlegte Startbewertungen, nicht verifiziert. Texte: J004 "Lovely bedding — washes and dries in no time, and so comfy to sleep under. Top marks 👍"; J005 "Washed it once at 30° on a 400 spin: colour and texture completely unchanged. Really impressed"; J006 "Just brilliant, this duvet. Sleeping really well and it matches the room nicely too. No more faffing about changing covers!"; J007 "Sooo good. Absolutely over the moon with it and I've been telling all my friends."; J008 "We're really pleased with it. I've already got one for my kids too, and I'll be ordering another for the little ones soon. Have a lovely evening 🤗 Best wishes from Birmingham."; J009 "Lovely."; J010 "Really good — so lovely and soothing to sleep under."; J011 "Gorgeous duvet. It really was dry in about 2 hours after washing."
3. **Judge.me-Bewertungen vor dem Shop-Start:** J001 (2025-08-03, Badge „another provider“, "totally transformed my mornings": "the bed takes 90 seconds now. my morning is completely different. better."); J002 (2025-11-15, Badge „another provider“, "quiet life improvement": "not dramatic but real. my life is just a little bit better because of this. that adds up."); J003 (2026-04-28, Badge „another provider“, "so glad i took the plunge": "ummed and ahhed for ages. so glad i finally bought it."). Sie liegen vor den ersten verifizierten Käufern (J012–J014, 21.–23.06.2026) und vor dem Trustpilot-Profil, sind kleingeschrieben und generisch; Herkunft n/a, nicht verifiziert.
4. **Kuratierter Trustpilot-Import** (siehe 4.2): 0 von 6 negativen und 0 von 7 China-Erwähnungen übernommen; 20 Sternwerte beim Import verändert; seit 12.09. kein Import mehr.
5. **Internationalisierung ab September:** Außerhalb GB im August 0, im September 11 von 133, im Oktober 13 von 44 (30 %): AU 12, CA 6, US 3, CY 1, JE 1, FR 1. 10 Trustpilot-Bewertungen betreffen das zweite Produkt ZipSheet (T158, T169, T217, T224, T226, T250, T264, T274, T283, T284), alle aus AU/US/CA.
6. **Lieferzeit-Kritik im September:** 34 von 133 (26 %) gegenüber 11 von 114 (10 %) im August und 6 von 44 (14 %) im Oktober.
7. **Mehrfach-Bewerter und Dubletten:** 10 Konten mit 2–3 Bewertungen (z. B. „Andrea“ T215, T247, T290; „Robin Lewis“ T168, T285 nach Zweitkauf). Zwei verschiedene Konten „Herbert Lawrence“ (T063, 2 Bewertungen gesamt) und „HERBERT LAWRENCE“ (T065, 32 Bewertungen) schrieben im Abstand eines Tages fast denselben Inhalt: "I immediately noticed the difference in weight from my old duvet with the cover." (T063, 5★) / "I immediately felt the weight difference between my old duvet and the Pleene, so much lighter." (T065, 5★). Bedeutung nicht verifiziert.
8. **Inhalte, die nicht zum Produkt passen:** ZipSheet-Bewertungen auf demselben Profil (s. o.); T220 "Such lovely good quality clothing"; Konto „Stanton Approved vehicles“ (T073); Markenname falsch geschrieben („Preene“ T009/T158, „Plebe“ T139, „Plein/Plien“ T256), was eher für echte Kunden spricht.
9. **Gewinnspiel-Hinweis:** T177 schreibt "I would really welcome winning another quilt". Die Produktseite bewirbt ein Newsletter-Gewinnspiel ("Win a free Duvet … One subscriber wins a duvet of their choice every month."). Ein Zusammenhang mit Bewertungen ist nicht verifiziert; Trustpilot meldet `hasCollectedIncentivisedReviews: false`. T290 erwähnt einen "friends discount" (Empfehlungsrabatt).
10. **Nachträgliche Änderungen:** T185 (5★) beginnt mit "Avoid this company like the plague." und endet nach Kontakt durch Pleene mit Empfehlung (aktualisiert 07.10.); T244 (4★) besteht nur aus "Refunded in full" (aktualisiert 07.10.).

### 4.7 Käuferprofil

**Geografie:** 267 von 291 Trustpilot-Bewertungen aus GB (91,8 %), dazu AU 12, CA 6, US 3, CY, JE, FR je 1. Judge.me zeigt kein Land (n/a).

**Geschlecht (Schätzung über Vornamen/Anrede der 280 Trustpilot-Konten, nicht verifiziert):** männlich 157 (56 %), weiblich 88 (31 %), unklar 35 (13 %). Anreden: „Mr“ 20, „Mrs/Miss/Ms“ 10. Einschränkung: Der Kontoinhaber ist nicht unbedingt der Nutzer; mehrere Männer schreiben für Paare oder die Ehefrau (T003, T064, T140), Frauen für Paare (T054, T166).

**Alter:** Ausdrückliche Altersangaben oder Seniorenhinweise in 16 Bewertungen, keine einzige deutet auf jüngere Käufer hin:
- "My wife and I are in our 80's" (T003, 5★)
- "the duvet arrived the day before my 84th!" (T133, 5★)
- "I am in my late 70s" (T066, 5★)
- "I’m a 77 years old disabled woman" (T269, 5★)
- "I am 72 years old" (T284, 5★)
- "Being 66 with a bad back" (T274, 5★)
- "helped an old man" (T001, 5★)
- "( you have to be old to get this)" (T002, 5★)
- "as old age advances" (T103, 5★)
- "So easy for the elderly people like myself to handle." (T137, 5★)
- "I am elderly, not too fit & am now a widower" (T177, 5★)
- "We are elderly and making the bed now is a breeze." (T253, 5★)
- "Now that I’m not a spring chicken" (T175, 5★)
- "perfect for the lazy persons, busy house wife or elderly people." (T105, 5★)
- "Purchased Zip on Bed Sheets for my elderly mother." (T283, 5★)
- "despite age and arthritis" (T249, 5★)

**Gesundheit und Mobilität (26 Bewertungen):** Arthritis (T064 Hände der Ehefrau, T074 Hände, T249, T286 Beine), Gelenke (T047), Rücken (T046 Rücken-OP, T078 "Back pains", T274, T284), Beine (T126 Bein-OPs, T134 "leg problems"), eingeschränkte Mobilität/Behinderung (T025, T079, T162, T269, T290), Herz (T043), Krebs/Chemotherapie (T070 "secondary breast cancer", T231 Schlaganfall + Lymphom), Diabetes/Angst (T079), diabetische Neuropathie (T212), Verletzungen (T072 Gefahr, T158 zwei gebrochene Zehen, T168 Autounfall), Erschöpfung (T095, T257), Maske in der Nacht (T102 "Have to wear a mask at night", Art der Maske n/a).

**Lebenssituation:**
- Witwer/allein: T029 ("after my wife passed away"), T177 und T236 (Witwer), T079 ("I live on my own"), T268 ("especially on your own"), T251 (Trauer nach zwei Todesfällen).
- Paare: zahlreich ("we", "my wife", "my husband"), u. a. T003, T054, T064, T108, T140, T166, T202, T232, T279.
- Kinder kaufen für Eltern / Käufer kaufen für Kinder: T171 ("Ordered for mother.. she can be fussy with what she buys.. I Trustpilot.. I read reviews"), T283 (ZipSheet für die ältere Mutter), T196, T200, T289 (für den Sohn), J008 (für die Kinder), T252 (für einen Freund), T133 (Geburtstagsgeschenk an sich selbst).
- Einsatzorte: Gästezimmer/Zweitbett (T027, T087, T094, T172, T175, T258, T290), Ferienhaus (T251), Campervan (T072), Dachzelt/„rooftop“ (J014), „busy household“ (T058, T123 ganzer Haushalt).
- Haustiere: Katzen (T067, T177).
- Kälteempfindliche bzw. Paare mit unterschiedlichem Wärmeempfinden: T289, T054, T166.

**Allergiker:** nur 1 Hinweis (T202, verstopfte Nase). **Wechseljahre:** 0 ausdrückliche Erwähnungen; Nachtschweiß/Schwitzen in 3 Bewertungen, alle von Männerkonten (T057 „Mr Gibbie“, T105 „Janos Madar“, T170 „Nicholas Roberts-Pendragon“). Angle B wird von Käufern als Sommerhitze/Winterkälte erlebt, nicht als Wechseljahresthema.

**Kaufverhalten:** In 28 Bewertungen werden 2 oder mehr Decken bzw. Sets genannt, 50 positive Bewertungen (18 %) erwähnen Wiederkauf, weitere Betten oder Gäste. 14 Bewertungen verweisen auf die Werbung bzw. Werbeversprechen (z. B. T052 "I saw the ad on Facebook", T098 "I only saw the advert on facebook", T175 "I was positively beaming when I saw the Pleene advertisement", T192 "claims by companies on FB").

**Bewertungsverhalten:** Die Bewerter sind erfahrene Trustpilot-Nutzer (Median 10 Bewertungen pro Konto) und schreiben kurz (Median 198 Zeichen).

### Anhang

#### A1 – Alle Trustpilot-Bewertungen mit 1–3 Sternen (8 von 8, wörtlich)

Vollständigkeit: Sternfilter `?stars=1&stars=2&stars=3` meldet totalCount 8; erfasst 8. Keine dieser Bewertungen hat eine öffentliche Antwort von Pleene, keine ist auf Judge.me importiert.

**T036 · 2026-08-01 · 3★ · Land GB · Bruce · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Great duvet, but watch out when you order"

> I want to say that I am very impressed with the Duvet. It's great and washes easily (I have a Superking, and it does wash in my 8Kg Ebac machine (which has quite a small drum). I wasn't impressed with the sales process, though. I made the purchase, and got another page asking me to confirm an order. I thought I was just confirming the purchase I'd made (probably wasn't concentrating) but it added a second Duvet, that I didn't want) to the order at a discount. I contacted the company immediately, and they said they would try to change the order. I now have two Duvets.

Link: https://uk.trustpilot.com/reviews/6a6e581c0214e9bd265addae

**T059 · 2026-08-09 · 1★ · Land GB · Ross Boyer · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Says it's a London based company...The…"

> Says it's a London based company...The address 128 City Road, London (EC1V 2NX) is a well-known mass-registration office used by thousands of UK corporate entities via virtual address providers like Companies Made Simple. 
> It doesn't state where the goods are shipped from and it offers two free pillow cases but no indication of this when you come to pay

Link: https://uk.trustpilot.com/reviews/6a7846e3448acc3c2b560c4e

**T094 · 2026-08-23 · 1★ · Land GB · Geoff Luxton · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Took 13 days instead of 6 day…"

> Took 13 days instead of 6 day advertised...Item is very creased I need it for spare bed before my relative arrived  IT arrived after he had gone

Link: https://uk.trustpilot.com/reviews/6a8a21a6241b281f61d5b406

**T115 · 2026-09-01 · 1★ · Land GB · Michael · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Is this real??"

> Ordered a month ago. No product. Customer support has taken 5 days to respond and then didn’t help just said out for delivery. Now going to my bank to get my money back as this seems to be a scam.

Link: https://uk.trustpilot.com/reviews/6a966b45bcb53b426f7ba3b3

**T119 · 2026-09-02 · 3★ · Land GB · Scotty McLeod · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "They say a free return - no"

> They say a free return - no they don’t I was told my miss-order would cost me too much to return to China so they offered me a percentage off another order which I accepted.
>
> The new order was slower than the first one despite me paying for enhanced delivery and was clearly ‘bubbled’ with lining coming out through a series of minute minute punctures in the surface but nothing meaningful it turned out.
>
> Light weight and good quality.

Link: https://uk.trustpilot.com/reviews/6a9802e358d9be5b6054125c

**T127 · 2026-09-04 · 2★ · Land GB · Mr Sideways · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "item took 3 weeks to arrive no reply to…"

> item took 3 weeks to arrive no reply to email. Its not warm too thin, waste of money

Link: https://uk.trustpilot.com/reviews/6a9a85be8c8f5ebd62ffbfb4

**T240 · 2026-09-29 · 1★ · Land GB · Customer Angela B · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Pleene! ~ NO STARS CON"

> I would give this company NO STARS if I could.  I placed my order and waited and waited.  I eventually wrote to them and they claimed my order was "damaged in transit"  (HOW CAN YOU DAMAGE BEDDING?)  They than claimed that Evri had the parcel in thier london hub days ago you Evri have no record of the tracking numbers given AVOID THIS COMPANY AT ALL COST!

Link: https://uk.trustpilot.com/reviews/6abb6824023069e7859dabe1

**T277 · 2026-10-05 · 1★ · Land GB · Nicola · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Regretably the duvet arrived unfinished…"

> Regretably the duvet arrived unfinished and very poor quality. I am now trying to be reimbursed, to which there seems to be reluctance. I have been offered a free one, but it would not be free as I have already paid for unusable goods.

Link: https://uk.trustpilot.com/reviews/6ac40d00f2726921042362f5

#### A2 – Judge.me 1–3 Sterne

Nur J121 (3★), wörtlich in 4.2; Text identisch mit Trustpilot T109 (dort 5★). Judge.me 1★ und 2★: 0.

#### A3 – Die 30 aussagekräftigsten 4–5-Sterne-Bewertungen (wörtlich)

Auswahl nach Informationsgehalt (konkrete Situation, Einwand, Vergleich, Lebenslage), nicht nach Länge allein; alle Trustpilot.

**T003 · 2026-08-01 · 5★ · Land GB · Brian Hutchings · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Duvets and pillowcases."

> The two duvets we bought were of good quality, likewise the pillowcases. The duvets were lightweight, which is ideal for this hot weather, and being able to put them in the washing machine in one piece without having to take covers off and put them back on is a life saver. My wife and I are in our 80's and need all the help we can get, so thank you so much for them.

Link: https://uk.trustpilot.com/reviews/6a6e1bbb66d4bb84f9c3618c

**T008 · 2026-08-01 · 4★ · Land GB · Mrs Val Harper · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I am delighted with my new duvet"

> I am delighted with my new duvet, all in one. It is a good fit on my king size bed. Although it was expensive, the hassle it saves in time and effort make it great. It is also reversible, so after a week, I can turn it over and have a new clean duvet. Why this has not been thought out before, I don't know. 
>
> Only bad thing I have to say is, how it was packed. It had been squashed with the pillowcases into a compressed package, thus the pillowcases are still very creased, and I feel loathe to iron them in case I spoil them. The duvet itself after a few shakes, has sorted itself out. This is why I have taken one star off.

Link: https://uk.trustpilot.com/reviews/6a6e1d9a1f863fd5dd3f0d20

**T025 · 2026-08-01 · 5★ · Land GB · JanetFoster · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I am absolutely delighted with my new bedding."

> I am absolutely delighted with my new bedding, and having limited mobility, it’s a real dream not having to change duvet covers any more.
> The duvet itself is really soft and comfortable, and beyond my expectations.
> I have now ordered the zip-on bottom sheets to make my new bed complete.
> Thank you Pleene.

Link: https://uk.trustpilot.com/reviews/6a6e317fa74bb554d5e4538f

**T029 · 2026-08-01 · 5★ · Land GB · John Cubbins · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I ordered these after my wife passed…"

> I ordered these after my wife passed away , I got two and they are really of good quality both in cold and hot weather and make it so easy for me to wash and change them, thank you

Link: https://uk.trustpilot.com/reviews/6a6e38a9947b905c2417b480

**T043 · 2026-08-02 · 5★ · Land GB · Mrs Jen Killeen · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Extremely pleased"

> I ordered two duvets as I was worried about getting it dry in the winter. When they came I was so pleased with them, they washed and dried so well. They are very comfortable to sleep in too. I am so pleased that I do not have to change the duvet cover now as I have a bad heart and it takes a lot out of me. Only thought I had is that they do not do patterened ones

Link: https://uk.trustpilot.com/reviews/6a6f18e22d7dc50cedbf7d9a

**T054 · 2026-08-06 · 5★ · Land GB · Mark Berry-Gough · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I was skeptical about this item"

> I was skeptical about this item. I like to be warm and cosy whereas my husband wants to be cool and unrestricted by quilts and additional quilt covers. The Pleene coverless duvet delivers for both of us! So comfortable!
> Washing and drying is a breeze, and making the bed is effortless.
> Constructive advice .....
> # my order took a long time to be delivered so please evaluate your logistical processes.
> # I subsequently ordered 2 more quilts because I liked the first one do much. I would have appreciated a loyalty discount for being a returning customer. 
> Thank you!!

Link: https://uk.trustpilot.com/reviews/6a7419fb00383eabcc95e111

**T066 · 2026-08-11 · 5★ · Land GB · Mrs conway · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I am in my late 70s and even though I…"

> I am in my late 70s and even though I have changed quilt covers all my life I am now finding it very difficult.i have a small double bed and I can’t always find bedding that fits. I liked the idea that I could get a long cover that would cover my feet perfectly. This cover does that and it is lovely to feel and snuggle up to.i picked the blue and it is a lovely shade. To make my bed in the morning is a joy. One shake and the bed is made and makes the room look tidy.

Link: https://uk.trustpilot.com/reviews/6a7b17a8107137c6fd39653e

**T070 · 2026-08-14 · 5★ · Land GB · Jeano · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Took longer than expected to arrive but…"

> Took longer than expected to arrive but definitely worth the wait. Makes my life so much easier especially as I’ve got secondary breast cancer and chemo makes me very fatigued so the fact there is no messing about getting my duvet in a cover is an absolute god send. Thank u

Link: https://uk.trustpilot.com/reviews/6a7f7c86d99cfa8b2485c42b

**T079 · 2026-08-18 · 5★ · Land GB · Alan Payton · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I live on my own and have struggled…"

> I live on my own and have struggled with changing quilt covers for at least 4 years providing me with anxiety and affecting my diabetes. Since ordering the quilts from Pleene I have found the anxiety is no more and the product is so very easy to use and there is no weight but adapts to my body temperature. I was able to choose between different colours and found the quality to be really high. I am so impressed with the product I have just ordered another two. I would highly recommend to others especially if you have disability issues

Link: https://uk.trustpilot.com/reviews/6a832f65e2073d574b7046de

**T103 · 2026-08-24 · 5★ · Land GB · Jenny · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "So far, so good"

> So far the bedding meets all my expectations, without the hassle of struggling with a cover.  Soft, comfortable, doesn't slip off the bed during the night.
> My biggest concern is, will the filling bunch up during washing?  I have not put that to the test yet.
> Provided it all stays exactly as new, this will be the best buy I have made for a long time, and has eliminated my ongoing worries as to how I shall cope with my bedding as old age advances.

Link: https://uk.trustpilot.com/reviews/6a8c631f5200149c2981f98f

**T107 · 2026-08-27 · 4★ · Land GB · Customer · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Recently bought a coverless duvet"

> Recently bought a coverless duvet. Took longer than I expected for it to arrive - despite the company being based in London, the product actually has to travel all the way from China. The product is very neat. Lovely colour and very comfortable to sleep with. As it is still summer, I cannot say how warm it will be for winter nights. It is claimed that the duvet will be like a 10 tog in winter. I will have to wait and see. I have yet to wash it but I did check it fits in the standard size washing machine - just makes it so I assume it will wash OK. I have the king size so anything smaller will definitely be fine.

Link: https://uk.trustpilot.com/reviews/6a9017c338f7b7597a50ac02

**T120 · 2026-09-02 · 5★ · Land FR · Mr Mayes · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I was a bit unsure at first however am…"

> I was a bit unsure at first however am very pleased with the product - It has certainly made life easier! With a duvet and cover I always ended up with too much duvet at the feet end and not enough at the head end!!

Link: https://uk.trustpilot.com/reviews/6a98069e5e9351e171ad6351

**T126 · 2026-09-04 · 5★ · Land GB · Rona Dixon · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I was pleasantly surprised to find how…"

> I was pleasantly surprised to find how good my Pleene product was. I bought a king size and although it is a tight fit in my washing machine it washed well and dried quickly. I especially like the ease with which I can now change bedding and the fact I no longer get twisted up in duvet covers. As it is lightweight it is so much easier to sleep as heavy duvets hampered my sleep as I turned over in bed. Having had operations on my legs Pleene has been gentler on me.I will buy more in the future.

Link: https://uk.trustpilot.com/reviews/6a9a7b8d667004a42061e0f2

**T133 · 2026-09-05 · 5★ · Land GB · Julie  Carter · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "My Birthday treat to myself"

> My Birthday treat to myself - the duvet arrived the day before my 84th!  I can honestly say that I have never had so many nights of uninterrupted sleep under my beautiful blue Pleene duvet.  It is like lying asleep in a floating  cloud.  I love it, and such a wonderful idea never again having to wrestle with taking off and putting on duvet covers.  Grateful thanks, so clever to have realised the need for less struggle and more simplicity.  Julie Carter

Link: https://uk.trustpilot.com/reviews/6a9c12c056635f7622aefd70

**T140 · 2026-09-06 · 5★ · Land GB · Sanderson · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "My wife always looked forward to…"

> My wife always looked forward to changing our duvet cover (not really!) . . . bought these. . . now i dont hear any more cursing and frustration venting!
>
> They look great, feel great and they are super comfortable to sleep under. But the best thing is changing the bed is now a breeze with the added bonus of being able to wash and dry the cover and duvet as one item in 2hrs (and no ironing!)
>
> In fact we have just ordered our 3rd set
>
> Highly recommend these to anyone who struggles changing and cleaning duvets

Link: https://uk.trustpilot.com/reviews/6a9d4944a66ca75b76852cbd

**T146 · 2026-09-07 · 5★ · Land GB · Cecilia Skudder · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Sceptical!"

> I did not believe the duvet would fit into the washing machine so as soon as it arrived I unpacked it and put it into that beast!  It fitted!   Not only does it look lovely it is comfortable and I wasn't hot!  I slept well!   I like a king size, but it is so generous I think a double would have been ok!   My next thought is will it dry in  a short time?  Will it be warm when the weather gets cold?  Watch this space.  Still a little sceptical, but so far just good!  For the future, please get some patterns in!

Link: https://uk.trustpilot.com/reviews/6a9ee7d177d786b1df266f3a

**T150 · 2026-09-07 · 5★ · Land GB · Michael Blanchard · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "My order came from China"

> My order came from China, took awhile but no problem. I've been using the duvet for a couple of weeks and I love it. The only thing I worried about were the claims it was warm for such a thin material. I needn't have worried it feels as good as my previous 11 tog duvet but very light on your body.. I haven't tried washing it yet, but I'm sure after the claims made, it will be easy. A great buy, I recommend it.

Link: https://uk.trustpilot.com/reviews/6a9ef6239fbd7d04b67022b0

**T170 · 2026-09-12 · 4★ · Land GB · Nicholas Roberts-Pendragon · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Overall they worked."

> Though they did not fully work in the way they described I.e. still felt hot sometimes and had to throw the Pleene EasyRest duvet off myself on some occasions. Overall it did stop my night sweats and waking up to wet sheets so they did work.

Link: https://uk.trustpilot.com/reviews/6aa56b8a3dea0aa742acca70

**T175 · 2026-09-12 · 5★ · Land GB · Sheffielder · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Being a person who likes camping"

> Being a person who likes camping, I’ve long thought how simple and easy a sleeping bag is and to be honest have used a sleeping bag more than once on a clean fitted sheet, whilst waiting for a duvet cover to dry and the duvet itself being returned from the cleaners.  Now that I’m not a spring chicken, the thought of arguing with a duvet has lost its attraction and I was positively beaming when I saw the Pleene advertisement.  I ordered and avidly followed my salvation as it made its way across the world until it finally landed at my back door.   It was very quickly unpacked and was on my bed within minutes, making me a very happy person.   The colour is lovely.  I chose the green.   The material is soft and comfortable and I’ve certainly been warm enough during the last few chilly nights.   My cover is due its first wash next week. 
>
> Today I’ve ordered an extra large single for the spare bed in my study.  Having friends to stay the night will now be quick and easy to prepare and quick and easy to wash afterwards.

Link: https://uk.trustpilot.com/reviews/6aa5968888999c43218ec8bd

**T177 · 2026-09-12 · 5★ · Land GB · MR D WALKER · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "A great addition to my home."

> The simplicity of making up the bed gave me my first big smile. I am elderly, not too fit & am now a widower, so making up the new bed system alone was a joy. Secondly, the product quality was excellent. I didn't really know what to expect. The colour I chose went very well with my existing bedroom colours, so another big plus. The weight of the quilt was great, neither too light nor too heavy. I experienced an excellent sleep & so did my wee black cat who seems to approve & sleeps on top of the quilt with me. I would really welcome winning another quilt, as it would have a good home in my spare bedroom.

Aktualisiert: 2026-09-13

Link: https://uk.trustpilot.com/reviews/6aa5bae9a3d9fef83c78e76f

**T192 · 2026-09-18 · 5★ · Land GB · Rowan I · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I was wrong"

> Where to start? I, like you, am somewhat suspicious of claims by companies on FB etc, but I thought at least I will have another quilt.  How wrong was I.  What a terrific purchase.  From the delivery of the airtight package to allowing the quilt to fluff out, my term, I was impressed with the process.  First night on I had a comfortable complete nights sleep.  I was suffering from broken nights previously.  As I said I was suspicious but since using it it feels so light, comfortable and never too hot or too cold.  So okay, I admit it, I was completely wrong, it is the best bedding quilt I have ever purchased and will not be buying any different ones.  Test to wash it but putting it all in the machine appeals to my inane lazy side!! Don’t take my word for it…well do!  You will not regret it!!!

Link: https://uk.trustpilot.com/reviews/6aacef17c5692f0093bb2b68

**T202 · 2026-09-21 · 5★ · Land GB · Tom56 · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Took rather a long time to arrive but…"

> Took rather a long time to arrive but once it did I was pleased with it.  Quality is good the size is good I got a super king for a king size bed as both of us are quilt hoggers .  The one thing that has intrigued me is having a quilt I can wash I no longer wake up with a bunged up nose.

Link: https://uk.trustpilot.com/reviews/6ab16d64c10b8a8ed93bc932

**T212 · 2026-09-23 · 5★ · Land GB · James Annette · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Product arrived before due date and the…"

> Product arrived before due date and the results have been excellent I generally don’t sleep more than 4/5 hours at a time but with my pleene I’m getting up to 7 hours ( I have diabetic neuropathy and had trouble sleeping previously) very happy

Link: https://uk.trustpilot.com/reviews/6ab3c39f8be5c6faf2bb27da

**T231 · 2026-09-28 · 5★ · Land AU · Gillian Stella Bufton · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I bought one and then decided on 2"

> I bought one and then decided on 2. 
> I’ve recently had a small stroke and now have lymphoma and I’m on chemotherapy. My strength and enery are low. 
> This is ideal as couldn’t change the dooner cover. 
> Company easy to deal with and description accurate. 
> Very happy with my purchases. Thank you 😊

Link: https://uk.trustpilot.com/reviews/6ab9f3be2240702f4199a530

**T236 · 2026-09-28 · 5★ · Land GB · Graham · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Solo Person"

> As a widower living on my own changing the king size  duvet cover on my own was struggle so the all in one duvet is ideal for somebody like me. 
> I have found it to be warm at night and stays on the bed with no problem

Link: https://uk.trustpilot.com/reviews/6aba79c5293e48cbfaca7c33

**T251 · 2026-10-01 · 5★ · Land GB · Consumer · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Saving my sanity."

> Finding this bedding has been the best thing at a time of great upset. In the last few years there has been the loss of two close family members, the most recent just months ago, and trying to cope with the trauma while maintaining a household, I find myself doing the absolute minimum. Having this bedding, I can give myself the haven needed to recharge at the end of the day. It has been so bad, I hadn’t even put the quilt cover on…just pulled it over me in the sheer exhaustion of grief. I feel, as the bedroom now looks like a bedroom, I can deal with other parts of the house I have neglected. I have also bought bedding for a holiday home, so my peace of mind continues. Thank you.

Link: https://uk.trustpilot.com/reviews/6abed148d8d603b12254dead

**T269 · 2026-10-04 · 5★ · Land GB · Mrs Maureen Lane · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Well I ordered the quilt with cover in…"

> Well I ordered the quilt with cover in a beautiful colour to match my bedroom walls… Lavender….. the quilt is absolutely gorgeous and covers our king size bed it keeps us nice and warm and cosy while being light on the body. I’m a 77 years old disabled woman who took a long time trying to make my mind up to order one as I didn’t think you could have a quilt all in one that you could put in a washing machine and dry it quickly then put it back on the bed……it’s a miracle. So pleased I ordered one.

Link: https://uk.trustpilot.com/reviews/6ac2c1f0d46672a75225f5a7

**T270 · 2026-10-05 · 5★ · Land GB · Richard Pettit · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Initially dubious."

> I liked the concept but I've been caught out before with internet orders, but decided to take the plunge and order two king-size duvets. Initially I thought I'd have to return as the size is so generous it will be a struggle to fit into my washing machine, (obviously not Pleene's fault).
> I'm glad I've kept them. Lovely feel to the material, so easy to handle and after the first wash no "bunching" or lumpiness to the filling (unlike my last quilt). Contacted their support department about a return before I decided to keep them and, surprising in this day and age, found Amelia quick to respond with here advice.

Link: https://uk.trustpilot.com/reviews/6ac34d32c00dcdb218027d37

**T273 · 2026-10-05 · 5★ · Land GB · Carol · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "I love my new duvet"

> I love my new duvet . Lightweight but warm. Crisp yet soft. Easy to wash and dry . It took a while to arrive but it was worth the wait and the communication around tracking was good. I chose the white one and it’s like a wispy cloud . After having goose down duvets I thought I’d be disappointed but it actually suits me well, as a person who struggles with the faff of changing bedding . Very glad I went for it. And the pillow cases were a nice surprise

Link: https://uk.trustpilot.com/reviews/6ac3a04da2c260a8323ed044

**T289 · 2026-10-07 · 5★ · Land GB · Mary Eleftheriou · Label: kein Label (Organic, not-verified) · Antwort Pleene: keine**

Titel: "Did it keep me warm?…"

> I am always cold and have the heaviest quilt i can find to keep me warm at night.
> So I was worried this would not keep me warm at its alot lighter than I usually use.
> It is amazing 100% does what it says. Warm all night no need for my heated blanket and in the morning bed made in seconds not minutes where i used to struggle to shake out a king size quilt with cover. 
> So good I am telling all my family and friends have ordered another 2 for  my son and will be replacing all the bedding in the house.
> Washing very easy washed and dried same day.

Link: https://uk.trustpilot.com/reviews/6ac5e8843957785385cc5250

