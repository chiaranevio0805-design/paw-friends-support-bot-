# Pleene – Vollanalyse (Stand 2026-10-08)

## Methodik-Notiz

- **Quellen:** GetHooked (brand_id 7553008; Shops 47758 pleene.com und 47737 pleene.uk) für Ads, Scores, Transkripte und Medien; Live-Abrufe der Landingpages auf pleene.com und pleene.uk (curl, Playwright/Chromium, Shopify-Produkt-JSON, Warenkorb bis vor den Checkout); Trustpilot (`uk.trustpilot.com/review/pleene.com`, pleene.uk führt auf dieselbe Business Unit); die Bewertungs-App Judge.me (Widget der Produktseite).
- **Keine Reichweite, kein Spend:** GetHooked liefert für GB weder Reichweite noch Spend (überall n/a). Ersatzsignale sind days_active, performance_score (nur aktive Ads; bei inaktiven null) und used_count. Ranking = days_active × max(used_count, 1) × max(performance_score, 1). Ein hoher Score bedeutet nicht zwingend hohen Umsatz (nicht verifiziert).
- **Datenstand:** Inventar-Abruf am 08.10.2026 ca. 10:30 UTC: 137 aktive und 555 inaktive Ads = 692 Ads. Die 137 aktiven Ads sind alle einzeln analysiert: 63 Videos (Anhang A2) und 74 Statics, davon 73 Bilder und 1 DCO (Anhang A3).
- **Datenabweichungen:**
  - Erwartet waren 45 aktive Video-Ads; GetHooked lieferte am 08.10. **63** aktive Video-Ads. Analysiert sind alle 63.
  - `search_ads` (aktiv) meldete meta.total=145, geliefert wurden 137 Zeilen; 8 Ads hielt GetHooked zurück, sie sind nicht identifizierbar (Teil 1, Regeln & Datenbasis).
  - Live meldete `search_ads` am 08.10. bereits 153 aktive Ads; rund 19 der neuesten Ads (Start 07.10.) sind nicht analysiert (Teil 2, 2.10).
  - Teil 1 zählt Angles nach Text (Headline + Primärtext, z. B. C 60 aktiv, Winner C 7). Teil 2, Executive Summary und Angriffsfläche zählen nach Inhalt (z. B. C 47, Winner C 5); 36 von 137 Ads weichen ab.
  - Neue Tests: Teil 1 zählt aktive Ads mit Start ab 24.09. (94), Teil 2 und die Executive Summary die letzten 14 Tage ab 25.09. (79 aktive); die Differenz sind die 15 aktiven Ads mit Start am 24.09.
  - Live-Werte aus `get_ad` weichen teils vom Inventar ab (z. B. 145443318: Score 61 statt 74; einige Ads seit 07.10. inaktiv). Ausgewiesen ist der Inventarwert, Live-Abweichungen stehen jeweils dabei.
  - GetHooked-Transkripte sind teils fehlerhaft (Platzhalter „the next, video!!“ bei reinen Musik-Videos, Sprache fälschlich als Walisisch erkannt); diese Fälle sind in A2 per Audio-Check, Whisper bzw. Untertiteln geprüft und markiert.
- **Zitate und Links:** Text aus Ads, Seiten und Bewertungen steht wörtlich im englischen Original, die Analyse auf Deutsch. Die englischen Hook-Vorschläge in der Angriffsfläche sind eigene Vorschläge, keine Pleene-Zitate. Verlinkt sind nur die GetHooked-share_url und die Meta-Ad-Library (`https://www.facebook.com/ads/library/?id=<external_id>`); signierte Media-URLs (laufen nach 24 h ab) sind nicht enthalten.
- **Kennzeichnung:** Fehlende Werte = „n/a“, Unsicheres = „nicht verifiziert“.

## Inhaltsverzeichnis

- [Methodik-Notiz](#methodik-notiz)
- [Executive Summary](#executive-summary)
- [Teil 1 – Ads-Inventar](#teil-1--ads-inventar)
  - [Zusammenfassung](#zusammenfassung)
  - [Regeln & Datenbasis](#regeln--datenbasis)
  - [Gruppierungen](#gruppierungen)
  - [Zeitachse](#zeitachse)
  - [Top 20 nach Ranking](#top-20-nach-ranking)
  - [Neue Tests (aktiv, Start ≥ 2026-09-24)](#neue-tests-aktiv-start--2026-09-24)
  - [Verlierer / Aufgegeben](#verlierer--aufgegeben)
- [Teil 2 – Creative-Muster und Gewinner-System](#teil-2--creative-muster-und-gewinner-system)
  - [2.0 Kurzfazit](#20-kurzfazit)
  - [2.1 Gewinner-System](#21-gewinner-system)
  - [2.2 Die 5 Hook-Muster der Winner](#22-die-5-hook-muster-der-winner)
  - [2.3 Angles A–F](#23-angles-af)
  - [2.4 Neue Tests der letzten 14 Tage (25.09.–08.10.)](#24-neue-tests-der-letzten-14-tage-25090810)
  - [2.5 Aufgegebenes: Verlierer, inaktive Familien und Lehren](#25-aufgegebenes-verlierer-inaktive-familien-und-lehren)
  - [2.6 Avatare, die Pleene nicht anspricht (Abgleich mit dem Käuferprofil aus s4)](#26-avatare-die-pleene-nicht-anspricht-abgleich-mit-dem-käuferprofil-aus-s4)
  - [2.7 Formate, die Pleene nicht nutzt](#27-formate-die-pleene-nicht-nutzt)
  - [2.8 Hygiene-Spezialfrage](#28-hygiene-spezialfrage)
  - [2.9 Kongruenz Ad → Seite und Funnel-Muster (aus s3, ergänzt um s2)](#29-kongruenz-ad--seite-und-funnel-muster-aus-s3-ergänzt-um-s2)
  - [2.10 Wichtige Datenlücken und Unsicherheiten](#210-wichtige-datenlücken-und-unsicherheiten)
  - [Anhang zu Teil 2: Links zu zentralen Nicht-Winner-Ads](#anhang-zu-teil-2-links-zu-zentralen-nicht-winner-ads)
- [Teil 3 – Funnel und Landingpages](#teil-3--funnel-und-landingpages)
  - [3.0 Zusammenfassung](#30-zusammenfassung)
  - [3.1 Vergleichstabelle der Landingpages](#31-vergleichstabelle-der-landingpages)
  - [3.2 Preiswelten GBP und USD](#32-preiswelten-gbp-und-usd)
  - [3.3 Seite 1: `pleene.com/products/easyrest` (83 Ads, GB) — Produktseite](#33-seite-1-pleenecomproductseasyrest-83-ads-gb--produktseite)
  - [3.4 Seite 2: `pleene.com/products/easyrest-comforter` (40 Ads, US) — Produktseite (US-PDP)](#34-seite-2-pleenecomproductseasyrest-comforter-40-ads-us--produktseite-us-pdp)
  - [3.5 Seite 3: `pleene.com/pages/tb-6` (8 Ads, GB) — Advertorial (Pre-Lander)](#35-seite-3-pleenecompagestb-6-8-ads-gb--advertorial-pre-lander)
  - [3.6 Seite 4: `pleene.com/products/easyrest-duvet` (6 Ads, GB) — Produktseite (Klon)](#36-seite-4-pleenecomproductseasyrest-duvet-6-ads-gb--produktseite-klon)
  - [3.7 Garantie, Probeschlafen, Rückgabe und Versand (für alle Seiten)](#37-garantie-probeschlafen-rückgabe-und-versand-für-alle-seiten)
  - [3.8 Bewertungs-Apps und -Zahlen](#38-bewertungs-apps-und--zahlen)
  - [3.9 Warenkorb, Upsells und Cross-Sells (bis vor den Checkout)](#39-warenkorb-upsells-und-cross-sells-bis-vor-den-checkout)
  - [3.10 Kongruenz: Ad und Landingpage](#310-kongruenz-ad-und-landingpage)
  - [3.11 Technik](#311-technik)
  - [3.12 Home-Page und weitere Funnel-Elemente](#312-home-page-und-weitere-funnel-elemente)
  - [3.13 Offene Punkte (n/a bzw. nicht verifiziert)](#313-offene-punkte-na-bzw-nicht-verifiziert)
  - [3.14 Dateien](#314-dateien)
- [Teil 4 – Bewertungen und Einwände](#teil-4--bewertungen-und-einwände)
  - [4.1 Zusammenfassung](#41-zusammenfassung)
  - [4.2 Zahlen](#42-zahlen)
  - [4.3 Kategorien: Probleme und Einwände](#43-kategorien-probleme-und-einwände)
  - [4.4 Lob-Lücken: Was Käufer loben und die Ads nicht nutzen](#44-lob-lücken-was-käufer-loben-und-die-ads-nicht-nutzen)
  - [4.5 Voice of Customer: das alte Problem in Käuferworten](#45-voice-of-customer-das-alte-problem-in-käuferworten)
  - [4.6 Tempo](#46-tempo)
  - [4.7 Käuferprofil](#47-käuferprofil)
- [Für Chrome / Ad-Library-Check](#für-chrome--ad-library-check)
- [Für Nevio zum Ansehen](#für-nevio-zum-ansehen)
  - [1. 145443331 – „Everyone said it. They were right.“ (Video 47 s, 56 Tage, Score 100, used_count 2)](#1-145443331--everyone-said-it-they-were-right-video-47-s-56-tage-score-100-used_count-2)
  - [2. 136389861 – „No More Fighting With Duvet Covers“ (Video 38 s, 120 Tage, Score 61)](#2-136389861--no-more-fighting-with-duvet-covers-video-38-s-120-tage-score-61)
  - [3. 133366534 – „No More Fighting With Duvet Covers“ (Video 93 s, 67 Tage, Score 100)](#3-133366534--no-more-fighting-with-duvet-covers-video-93-s-67-tage-score-100)
  - [4. 139561410 – „Mint Green is almost gone.“ (Video 16 s, 63 Tage, Score 100)](#4-139561410--mint-green-is-almost-gone-video-16-s-63-tage-score-100)
  - [5. 168246678 – „Check This Before You Buy“ (Video 27 s, 41 Tage, Score 100)](#5-168246678--check-this-before-you-buy-video-27-s-41-tage-score-100)
- [Angriffsfläche – 10 Punkte](#angriffsfläche--10-punkte)
  - [1. Angle E konkret statt „Schulter/Rücken“: Arthritis, Erschöpfung, Herz](#1-angle-e-konkret-statt-schulterrücken-arthritis-erschöpfung-herz)
  - [2. Angle B als Paar-Konflikt („er schwitzt, sie friert“) statt nur „warm genug im Winter“](#2-angle-b-als-paar-konflikt-er-schwitzt-sie-friert-statt-nur-warm-genug-im-winter)
  - [3. Avatar: der ältere Mann bzw. Witwer als Ich-Erzähler](#3-avatar-der-ältere-mann-bzw-witwer-als-ich-erzähler)
  - [4. Avatar: erwachsene Kinder, die vor Weihnachten für Mum und Dad kaufen](#4-avatar-erwachsene-kinder-die-vor-weihnachten-für-mum-und-dad-kaufen)
  - [5. Format: Beweis-Video – Zeitraffer vom Waschen bis Trocknen mit Uhr, daneben eine normale Decke](#5-format-beweis-video--zeitraffer-vom-waschen-bis-trocknen-mit-uhr-daneben-eine-normale-decke)
  - [6. Format: Konter-Checkliste auf Basis von Pleenes eigenem Winner-Format](#6-format-konter-checkliste-auf-basis-von-pleenes-eigenem-winner-format)
  - [7. Angebot: Rückgabe, die wirklich kostenlos ist, und Beigaben, die im Warenkorb stehen](#7-angebot-rückgabe-die-wirklich-kostenlos-ist-und-beigaben-die-im-warenkorb-stehen)
  - [8. Behauptung: prüfbare Zahlen statt „any machine“ und „2 hours“](#8-behauptung-prüfbare-zahlen-statt-any-machine-und-2-hours)
  - [9. Behauptung: Hygiene nur mit Beleg und nur als Nebenargument](#9-behauptung-hygiene-nur-mit-beleg-und-nur-als-nebenargument)
  - [10. Seite: Vertrauensblock above the fold mit echten Bewertungen, Antworten und Herkunft](#10-seite-vertrauensblock-above-the-fold-mit-echten-bewertungen-antworten-und-herkunft)
- **[Anhang](#anhang)**
  - [A1 – Vollinventar und Primärtexte](#a1--vollinventar-und-primärtexte)
    - [Vollinventar aktiv (137 Ads)](#vollinventar-aktiv-137-ads)
    - [Vollinventar inaktiv (555 Ads, Start ab 2026-04-08)](#vollinventar-inaktiv-555-ads-start-ab-2026-04-08)
    - [Primärtext-Anhang](#primärtext-anhang)
  - [A2 – Video-Ads im Detail](#a2--video-ads-im-detail)
    - [A2.1 – Video-Batch 1 (7 Videos)](#a21--video-batch-1-7-videos)
    - [A2.2 – Video-Batch 2 (7 Videos)](#a22--video-batch-2-7-videos)
    - [A2.3 – Video-Batch 3 (7 Videos)](#a23--video-batch-3-7-videos)
    - [A2.4 – Video-Batch 4 (7 Videos)](#a24--video-batch-4-7-videos)
    - [A2.5 – Video-Batch 5 (7 Videos)](#a25--video-batch-5-7-videos)
    - [A2.6 – Video-Batch 6 (7 Videos)](#a26--video-batch-6-7-videos)
    - [A2.7 – Video-Batch 7 (7 Videos)](#a27--video-batch-7-7-videos)
    - [A2.8 – Video-Batch 8 (7 Videos)](#a28--video-batch-8-7-videos)
    - [A2.9 – Video-Batch 9 (7 Videos)](#a29--video-batch-9-7-videos)
  - [A3 – Static-Ads im Detail](#a3--static-ads-im-detail)
    - [A3.1 – Static-Batch 1 (15 Ads)](#a31--static-batch-1-15-ads)
    - [A3.2 – Static-Batch 2 (15 Ads)](#a32--static-batch-2-15-ads)
    - [A3.3 – Static-Batch 3 (15 Ads)](#a33--static-batch-3-15-ads)
    - [A3.4 – Static-Batch 4 (15 Ads)](#a34--static-batch-4-15-ads)
    - [A3.5 – Static-Batch 5 (14 Ads)](#a35--static-batch-5-14-ads)
  - [A4 – Bewertungen wörtlich](#a4--bewertungen-wörtlich)
    - [A4.1 – Alle Trustpilot-Bewertungen mit 1–3 Sternen (8 von 8, wörtlich)](#a41--alle-trustpilot-bewertungen-mit-13-sternen-8-von-8-wörtlich)
    - [A4.2 – Judge.me 1–3 Sterne](#a42--judgeme-13-sterne)
    - [A4.3 – Die 30 aussagekräftigsten 4–5-Sterne-Bewertungen (wörtlich)](#a43--die-30-aussagekräftigsten-45-sterne-bewertungen-wörtlich)

---

## Executive Summary

1. **Datenbasis:** 692 Ads (137 aktiv, 555 inaktiv (Abfragefenster Start ab 08.04.; frühester gefundener Start 01.06.)); alle 137 aktiven Ads sind inhaltlich analysiert (63 Videos, 73 Bilder, 1 DCO). Reichweite und Spend sind für GB n/a. Am 08.10. meldete `search_ads` bereits 153 aktive Ads, rund 19 Ads vom 07.10. sind deshalb nicht analysiert.
2. **Gewinner-System:** 20 Winner (aktiv, mindestens 30 Tage, Score ≥ 61), Zielland 13 laut GetHooked GB, 7 ohne Länderangabe (151025063, 171191667, 172760571, 151025052, 169082912, 173307160, 174599778); GB für diese 7 nicht verifiziert (Indiz: GB-PDP `/products/easyrest`; „£39.99“ in Text oder Bild bei 4 der 7, „Customer, UK“ bei 1, bei 151025052 und 169082912 nur die PDP); alle auf `/products/easyrest`, gestartet 11.06.–09.09. (11 Videos, 9 Bilder). Sie stammen aus fünf Video-Familien (Creator-Bekenntnis 145443331, Schmerz-Hook 136389861/151025063, 93-s-Hygiene-Kompilation 133366534, 16-s-KI-Template mit Farbknappheit 139561428/410/491, Checkliste 168246678/686) und den Bildfamilien T01 „No More Fighting With Duvet Covers“ (136388964/847, je 120 Tage) und T15 „Properly Warm, Never Heavy“.
3. **Rezept:** Kein Hook nennt das Produkt; die Hooks sind Ich-Bekenntnis, Knappheit/Farbe, Einwand bzw. Checkliste, Schmerz-Verbot oder Ekel. Der Body folgt immer „duvet and cover in one“ → Waschmaschine und Trockner → warm/kühl → „I swear to you, my bed always feels fresh.“, am Ende fast immer „2 free Pleene™ Pillow Cases (worth £39.99)“ plus „90-night trial“.
4. **Angles:** (nach Inhalts-Angle, Teil 2.3) F-Knappheit/Farbe ist am effizientesten (5 Winner aus 14 aktiven Ads, Ø Score 49,3), C (Beziehen) trägt das Volumen (47 aktiv, 5 Winner), B (Temperatur) hat unter den Kern-Angles den höchsten Ø Score (37,8, nur GB 43,5) und E (Beschwerden) die längste Laufzeit (Ø 35,4 Tage). Wechseljahre kommen in 0 Ads und 0 Bewertungen vor.
5. **Aktuelle Tests:** 37–91 Launches pro Woche, 119 in den letzten 14 Tagen (heute 79 aktiv), meist 3 Hooks auf einem Body. Neu sind Hygiene als Persona-Geschichte (2000370xx), „Selbstständigkeit im Alter“ (11 aktiv, alle Score 1), das Advertorial `/pages/tb-6`, der US-Markt (40 aktive Ads auf der Comforter-Seite), eine KI-Seniorin als Sprecherin (200490716) und „30% off“.
6. **Testergebnis:** Von 34 wirklich neuen Creatives erreichen nur 4 Score ≥ 41, alle Bilder (185228766, 193234214, 193234215, 184134598); kein neues Video, keine US-Ad und kein Selbstständigkeits-Creative liegt laut Inventar über Score 12, die Persona-Videos laut Live-Abfrage bei höchstens 44. Einschätzung: Pleene hat den Herbst-Winner noch nicht gefunden und lädt Sommer-Winner 1:1 neu hoch, die Kopien tragen meist nicht (Score 1, teils nach 2 Tagen wieder aus).
7. **Aufgegeben:** ZipSheet komplett (76 Ads), die Listicle-Seite `duvet-10r` (19 von 19 Verlierer), Headlines, die nur das Produkt beschreiben, reine Rabatt-Headlines und das Kommentar-Quiz. Die Hygiene-Welle vom 25.09. endete nach höchstens 12 Tagen, die neuen E-Ads nach 6–7 Tagen, die Winter-Familie 178749xxx ist seit 07.10. trotz Score 70–81 inaktiv; im September liefen 62 % der beendeten Ads weniger als 7 Tage.
8. **Funnel:** 4 Landingpages, alle auf pleene.com, keine auf pleene.uk. Die GB-Produktseite führt mit B („10.5 TOG — proper winter warmth“), die meisten GB-Ads mit C, A oder Knappheit; Preise £74.99–£129.99 mit Streichpreis („SAVE 23–35 %“), Kaching-„Couple-Bundle“ (−10 %) vorausgewählt, Gratisversand ab £100, im Warenkorb ein „180-Day Return Policy – Upgrade“ für £2.99 und nach etwa 4 s ein Gewinnspiel-Pop-up ohne auffindbare Teilnahmebedingungen.
9. **Kongruenzbrüche:** Knappheit („Only 17 left in Hearth Red“) ohne Lagerhinweis auf der Seite; Gratis-Kissenbezüge nicht im Warenkorb (Kaching `freeGifts: []`); „30% off“ gegen „SAVE 23–35 %“ und „Value £49.99“ (200490716) gegen „worth £39.99“; „CoolRest™“ im Winner 174599778; „Fits in every washing machine“ gegen die Trommelgröße 6–8 kg der eigenen Tabelle; drei Fassungen von „dry in 2 hours“; „10.5 TOG“ gegen „mid-weight, all-season“; „Over 10,000“ gegen „7,000+“.
10. **Reviews:** Trustpilot 291 Bewertungen (Ø 4,8, 86 % 5★), alle seit 01.08.2026. Judge.me besteht zu 154 von 172 aus Trustpilot-Importen, übernommen wurden 0 von 6 negativen und 0 von 7 mit China-Erwähnung; Pleene antwortet auf 0 von 291, und die „✓ Verified“-Testimonials der Produktseite (Margaret 67, James 55 usw.) finden sich in keiner Bewertung.
11. **Einwände der Käufer:** Lieferzeit 51 Bewertungen (17,5 %, im September 26 %), Versand aus China bzw. unklare Herkunft 11, teure Rücksendung trotz „Money back, no questions asked“ (T055, T119), Winter noch ungetestet 14, Betrugsangst beim Facebook-Kauf schon vor dem Kauf 8 (z. B. T098). Verklumpen und negativer Geruch kommen nicht vor.
12. **Käufer:** 91,8 % GB, durchweg ältere Menschen, nach Vornamen 56 % Männerkonten (Schätzung), viele mit Arthritis, Rücken-, Herz- oder Chemo-Belastung und eingeschränkter Mobilität, dazu Witwer, Paare und Mehrfachkäufer (28 Bewertungen). Ihr Vokabular ist „fight“, „wrestle“, „struggle“, „faff“; Hygiene nennen nur 8 von 283 positiven Bewertungen, „mites“, „bacteria“ und „allergy“ keine.
13. **Größte Lücken bei Pleene:** Kein älterer Mann tritt als alleiniger Ich-Erzähler bzw. Witwer auf. Ein älterer Mann spricht nur im Paar-UGC 200490722/200490658 (Start 06.10., Score 1) und als sehr wahrscheinlich KI-generierter Presenter im Hook von 136389861; den Witwer „George, 82“ gibt es nur in der dritten Person (Off-VO und Review-Karte in 133366534). Keine Ad nennt eine konkrete Krankheit wie Arthritis, Herz oder Krebs/Chemo (einzige genannte Erkrankung: Allergie in 133366534 „Especially because of her allergies.“ und 193234224 „Ruth S. now washes hers every week — because of her allergies“). In GB gibt es vor Weihnachten keine Geschenk-Ad, keinen Paar-Temperatur-Hook und keine Trust-Ad. Es fehlt jedes Beweis-Format (Zeitraffer, Vergleichstest, Experte), und die Hygiene-Claims haben weder Beleg noch Resonanz bei den Käufern.
14. **Unser Hebel:** Pleene gewinnt mit Bequemlichkeit, Farbknappheit und Gratis-Kissenbezügen, ist aber offen bei Vertrauen, Lieferung, Rückgabe, belegbaren Angaben und den echten Käufer-Avataren. Dort setzen die 10 Punkte unten an.

---

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
- Angle „F-Selbstständigkeit im Alter“ erscheint erst ab 2026-09-29 (18 Ads; aktiv 14, inaktiv 4; inkl. Nebencode; als Haupt-Code 15, davon 11 aktiv); D (Geschenk/„their routine“) erstmals 2026-10-07.
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

**Zielland der Top 20 (GetHooked-Feld `countries`, `a3data/countries.json`, Dateistand 08.10. 10:44 UTC):** 13 laut GetHooked GB, 7 ohne Länderangabe (151025063, 171191667, 172760571, 151025052, 169082912, 173307160, 174599778); GB für diese 7 nicht verifiziert (Indiz: GB-PDP `/products/easyrest`, auf die 52 der 63 GB-markierten und keine der 37 US-markierten aktiven Ads verlinken; GBP-Copy „worth £39.99“ im Anzeigentext von 151025063, 171191667 und 174599778, „~~£39.99~~“ im Bild von 173307160, „— Customer, UK“ im Bild von 172760571; bei 151025052 und 169082912 weder £ noch UK-Bezug, Indiz nur die PDP). Keiner der 20 ist laut GetHooked US. Live-Abruf `get_ad` am 08.10. abends: `countries` ist bei allen 7 weiterhin `[]`.

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

> Vollinventar (137 aktive und 555 inaktive Ads) und Primärtext-Anhang: siehe [A1 – Vollinventar und Primärtexte](#a1--vollinventar-und-primärtexte).

---

## Teil 2 – Creative-Muster und Gewinner-System

Marke: Pleene (UK), Produkt EasyRest (Decke und Bezug in einem). GetHooked brand_id 7553008, Shops 47758 und 47737. Analysestand: 08.10.2026.

**Datenbasis und Methode**

- **Inventar:** 692 Ads aus `wf/inventory.json` (Stand ca. 10:30 UTC am 08.10.), davon 137 aktiv und 555 inaktiv.
- **Inhaltsanalyse:** alle 137 aktiven Ads aus `wf/s2_video_batch1–9.md` (63 Videos, 1 DCO) und `wf/s2_static_batch1–5.md` (73 Bilder). Dazu kommen der Funnel aus `wf/s3_funnel.md` und die Bewertungen aus `wf/s4_reviews.md`.
- **Leistungssignale:** Reichweite und Spend gibt es für GB nicht (n/a). Als Ersatz dienen days_active, performance_score (bei inaktiven Ads null) und used_count. Ein hoher Score bedeutet nicht zwingend hohen Umsatz (nicht verifiziert).
- **Block-Regeln (aus s1):**
  - Winner: aktiv, mindestens 30 Tage, Score ≥ 61.
  - Starker Kandidat: 15–29 Tage mit Score ≥ 61, oder mindestens 30 Tage mit Score 41–60.
  - Neuer Test: Start ab 24.09.
  - Verlierer: inaktiv nach weniger als 7 Tagen.
- **Angle-Codes:** A Hygiene, B Wechseljahre/Temperatur, C Beziehen, D Geschenk, E körperliche Beschwerden, F weitere (Knappheit/Farbe, Angebot, Social Proof, Einwand/Kaufhilfe, Neuheit/Größe, Selbstständigkeit im Alter, Upgrade/Luxus).
- **Zwei Angle-Sichten:**
  - Text-Angle: aus Headline und Primärtext (s1).
  - Inhalts-Angle: was Bild bzw. Video tatsächlich zeigt und sagt (s2, für alle 137 aktiven Ads manuell zugeordnet; Skript `wf/s5_scripts/angles.py`, Ergebnis `wf/s5_scripts/content_angle.json`). Bei 36 von 137 aktiven Ads weichen beide ab, am häufigsten Text C gegenüber Inhalt A (8×) und Text C gegenüber Inhalt E (5×).
- **Abweichende Live-Werte:** Die Live-Abfragen in s2 (get_ad) weichen teils vom Inventar ab. Einige Ads sind inzwischen inaktiv (end_date 07.10.), einige Scores sind gestiegen (z. B. 22 auf 32 bzw. 44). Ausgewiesen wird jeweils der Inventarwert; Live-Abweichungen stehen dabei.
- **Links:** Ad-Library-Links folgen dem Schema `https://www.facebook.com/ads/library/?id=<external_id>`. GetHooked-Links sind die share_url.

---

### 2.0 Kurzfazit

1. **Das Gewinner-System ist schmal und stammt aus dem Sommer.** Es gibt 20 Winner, alle laufen auf `/products/easyrest` und alle starteten zwischen dem 11.06. und dem 09.09. Zielland: 13 laut GetHooked GB, 7 ohne Länderangabe (151025063, 171191667, 172760571, 151025052, 169082912, 173307160, 174599778); GB für diese 7 nicht verifiziert (Indiz: GB-PDP `/products/easyrest`; „£39.99“ in Text oder Bild bei 4 der 7, „Customer, UK“ bei 1, bei 151025052 und 169082912 nur die PDP). Von den 337 Ads, die in KW33–37 (10.08.–13.09.) starteten, sind heute nur 14 aktiv (4 %).
2. **Die typische Winner-Ad** ist ein Video mit 16–50 Sekunden (Median 29 s) oder ein einfaches Bild. Der Hook ist ein Ich-Satz, ein Knappheits-Text oder ein Einwand. Gesprochen wird entweder echter Creator-O-Ton, eine Off-Stimme über Kompilation oder gar nichts (nur Musik über einer KI-Szene). Alle außer 151025052 nennen das Angebot „2 free Pillow Cases (worth £39.99)“ und „90-night trial“.
3. **Knappheit/Farbe ist der effizienteste Angle:** 5 von 14 aktiven Ads sind Winner, der Ø Score liegt bei 49,3. Beziehen (C) hat das größte Volumen (47 aktive Ads), aber nur 5 Winner und einen Ø Score von 19,8.
4. **Hygiene (A) wird massiv getestet, gewinnt aber selten.** Von 28 aktiven A-Ads sind 2 Winner (133366534, 171191667) und 23 neue Tests (Start ≥ 24.09.; 19 davon ab 25.09.). Kein inaktiver Hygiene-Text hielt länger als 27 Tage. Die Headline „Be honest. When did you last wash it?“ lief in 51 Ads, 45 davon sind inaktiv, keine lief länger als 24 Tage.
5. **Teststrategie:** 37–91 Launches pro Woche, gebündelt an wenigen Tagen. Pro Body werden meist 3 Hooks getestet, Verlierer schnell abgeschaltet (September: 62 % der inaktiven Ads liefen unter 7 Tagen). Ein Teil der neuen Ads sind 1:1-Re-Uploads alter Winner. Dabei erben die Kopien den Score nicht.
6. **Neu seit 25.09. (119 Launches, davon 79 aktiv):**
   - Hygiene als Persona-Geschichte (Großeltern, Hund, Gästebett; 2000370xx)
   - „Selbstständigkeit im Alter“ (15 Ads)
   - Advertorial-Pre-Lander `tb-6`
   - US-Markt mit Comforter-Seite
   - GB/US-Zwillings-Launches
   - KI-Figuren (200490716)
   - „30% off“ im Skript
7. **Nicht besetzte Avatare:** Laut Reviews kaufen vor allem ältere Briten, mehrheitlich Männerkonten, mit Krankheiten, Witwer, Paare und Geschenkkäufer. Die Senioren-Personas der Ads sind Frauen bzw. „Großmütter“ (2000370xx „I'm 66“/„I'm 71“, 200490716), männliche Ich-Erzähler sind nur Creator ca. 30–40 (145443331/318, 193234221/219). Ältere Männer kommen nur am Rand vor: Sprechend nur im Paar-UGC 200490722/200490658 (Mann ca. 60–70 mit O-Ton; Start 06.10., Score 1) und als sehr wahrscheinlich KI-generierter Presenter (ca. 70+) im Hook von 136389861, sonst stumm im Bild (u. a. 200490718/200490660, 177443533/185228773/200490708, 193234224, 178749251). Es fehlen der ältere Mann als alleiniger Ich-Erzähler bzw. Witwer, konkrete Krankheiten (Arthritis, Chemo), Paare mit unterschiedlichem Wärmeempfinden, Weihnachtsgeschenke und das Vertrauensthema.
8. **Nicht genutzte Formate:**
   - Experten
   - Founder
   - Podcast
   - Street-Interview
   - echter Vergleichstest
   - Zeitraffer-Waschdemo (das Versprechen „2 hours“ wird nie gezeigt)
   - Unboxing
   - Quiz
   - Geschenk-/Tochter-Ads (nur 1 US-Ad)

   Die Mikroskop-Visualisierung kommt nur in einem Video vor.
9. **Hygiene-Belege sind dünn und widersprüchlich.**
   - „dust mites“ steht in 5 Ads, „bacteria“ in keiner Ad, nur auf der US-Seite („No chance for dust mites & bacteria“).
   - „2 hours“ erscheint mit Trockner, ohne Trockner und an der Luft; die eigene Seite sagt „2–3 hours“.
   - „7kg“ steht gegen „any washing machine“, „Hypoallergenic“ ist ohne Beleg.
   - In den positiven Bewertungen kommt Hygiene in 8 von 283 vor, „mites/bacteria/allergy“ in keiner einzigen.
10. **Kongruenz-Brüche:**
    - Knappheits-Ads ohne Lagerhinweis auf der Seite
    - Farbtext „Hearth Red“ auf schwarzen bzw. blauen Decken
    - wechselnde Restbestände für Mint Green (12, 26, 79)
    - „Value £49.99“ statt £39.99
    - „30% off“ gegen „SAVE 23–35 %“
    - fremder Produktname „CoolRest™“ in Winner 174599778
    - US-Wortwahl „comforter“ auf GB-Ads

---

### 2.1 Gewinner-System

#### 2.1.1 Die 20 Winner (aktiv, mindestens 30 Tage, Score ≥ 61)

| # | ID | Format, Länge | Start | Tage | Score | Inhalts-Angle (Text-Angle) | Hook (wörtlich) | Sprecher und Machart | Links |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 136389861 | Video 38 s | 11.06. | 120 | 61 | E (C) | „If your shoulders ache, don't do this.“ | KI-Presenter („Heiler/Lehrer“, sehr wahrscheinlich KI) im Hook, danach männliches Off-VO über UGC- und KI-B-Roll | [AL](https://www.facebook.com/ads/library/?id=1642037860240117) · [GH](https://app.gethookd.ai/share/ad/136389861?signature=52dff4dac27abf45e6f9b062724b0d38f817b3ddcd8939d92684a863d31faaf8) |
| 2 | 136388964 | Bild | 11.06. | 120 | 100 | C (C) | „3 things to STOP doing when you make the bed“ | Piktogramm-Listicle, keine Person | [AL](https://www.facebook.com/ads/library/?id=884267707299487) · [GH](https://app.gethookd.ai/share/ad/136388964?signature=d0ff0d2a2536e91cfc3dacb7f3b055bf680241a71e3d485ea8d2c98436047966) |
| 3 | 136388847 | Bild | 11.06. | 120 | 100 | C (C) | „Just want to sleep... but you've still got to change the bed?“ | Problem-Lösung-Split, verschwitzte Frau (KI-Look) | [AL](https://www.facebook.com/ads/library/?id=1583232786477915) · [GH](https://app.gethookd.ai/share/ad/136388847?signature=422777a4ae4663b915702dc330ccb3f999733ab57559e373f53beb6af24567f7) |
| 4 | 133366534 | Video 93 s | 03.08. | 67 | 100 | A (C) | „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ | Off-VO männlich (nicht verifiziert) über echte UGC- bzw. Lizenzclips, Badges, Review-Karten | [AL](https://www.facebook.com/ads/library/?id=1372761711494763) · [GH](https://app.gethookd.ai/share/ad/133366534?signature=ec7e21facd4f53244e7aacaf8002b409a7803a538b1d302bb66be766c52ef924) |
| 5 | 139561428 | Video 16 s | 07.08. | 63 | 100 | F-Knappheit/Farbe | „Only 17 left in Hearth Red“ | KI-Template (Hand, Türrahmen), nur Musik, Texteinblendungen | [AL](https://www.facebook.com/ads/library/?id=1034362836068724) · [GH](https://app.gethookd.ai/share/ad/139561428?signature=1eb14bdf7f1f4b278f8b5996d37204958181d02f07e10262e225457c7f9a49fd) |
| 6 | 139561410 | Video 16 s | 07.08. | 63 | 100 | F-Knappheit/Farbe + Angebot | „This week only: 2 FREE Pillow Cases with every DUVET“ / „Only 26 left in Mint Green“ | wie #5 | [AL](https://www.facebook.com/ads/library/?id=1355121136744622) · [GH](https://app.gethookd.ai/share/ad/139561410?signature=8993cc76f99c424613789bd7c6c9a9248d166b223587f503929e5077c7a435b2) |
| 7 | 139561491 | Video 16 s | 07.08. | 63 | 86 | F-Knappheit/Farbe | „Everyone's buying it in Coastal Blue“ / „Only 19 left“ | wie #5 | [AL](https://www.facebook.com/ads/library/?id=1526037445508180) · [GH](https://app.gethookd.ai/share/ad/139561491?signature=5cbb3a8ead3ed2e5b41ef6ef544d7498f90d8427b339e0ba7304f344c120fb43) |
| 8 | 145443331 | Video 47 s | 14.08. | 56 | 100 (used 2) | C (F-Social-Proof) | „I haven't changed my bed linen in three months and it's never felt fresher.“ | echter UGC-Creator (Mann ca. 30–40), O-Ton | [AL](https://www.facebook.com/ads/library/?id=1440933327878495) · [GH](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) |
| 9 | 145443318 | Video 50 s | 14.08. | 56 | 74 | C (F-Social-Proof) | „I bloody hate changing the bed“ | wie #8 (Hook-Swap) | [AL](https://www.facebook.com/ads/library/?id=1474663121347221) · [GH](https://app.gethookd.ai/share/ad/145443318?signature=be73a154548ac1fdbbec6cdf47867c12c72f8b288e40c2faaa6b1db18c69b49b) |
| 10 | 151025052 | Bild | 20.08. | 50 | 61 | F-Knappheit/Farbe | „Everyone's buying it in Coastal Blue – Only 19 left“ | KI-Schlafzimmer, keine Person, **ohne Angebot** | [AL](https://www.facebook.com/ads/library/?id=1363184622691769) · [GH](https://app.gethookd.ai/share/ad/151025052?signature=fa0ac684d0e23c918a286f4c72318a4110a6ecece18af70548ebdfc97ba1bc3e) |
| 11 | 151025063 | Video 29 s | 22.08. | 48 | 86 | E (C) | „I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“ | Off-VO weiblich (f0 ca. 193 Hz), Mix aus echtem, Stock-3D- und KI-Material | [AL](https://www.facebook.com/ads/library/?id=1369166828764339) · [GH](https://app.gethookd.ai/share/ad/151025063?signature=6a64477f3dd49f4b0e862e714a6a052a0839cfe3382654d8e4902e827f95d481) |
| 12 | 163921089 | Video 47 s | 27.08. | 43 | 100 | C (F-Social-Proof) | wie #8 (gleiche Datei) | Re-Upload von #8 | [AL](https://www.facebook.com/ads/library/?id=1609110380938946) · [GH](https://app.gethookd.ai/share/ad/163921089?signature=18918dab03620f19a44f0f4ae4aabab8d5f163dfaa3984dcc8e6e691c7301c1d) |
| 13 | 168246686 | Video 27 s | 29.08. | 41 | 86 | F-Einwand/Kaufhilfe | „Seen coverless duvets all over your feed?“ → „Check these 3 things before you buy.“ | KI-Hand, nur Musik | [AL](https://www.facebook.com/ads/library/?id=2035183934551496) · [GH](https://app.gethookd.ai/share/ad/168246686?signature=a360c60671d85ebeec646d4238239e0ec57ba2d7b037d0bb4c8888b606378db0) |
| 14 | 168246678 | Video 27 s | 29.08. | 41 | 100 | F-Einwand/Kaufhilfe | „Before you buy a coverless duvet check 3 things“ | wie #13 | [AL](https://www.facebook.com/ads/library/?id=1607904514111212) · [GH](https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59) |
| 15 | 169082912 | Bild | 31.08. | 39 | 74 | F-Knappheit/Farbe + Angebot | „This week only: 2 FREE Pillow Cases with every DUVET – Only 26 left in Mint Green“ | KI-Szene, keine Person | [AL](https://www.facebook.com/ads/library/?id=2192690231462965) · [GH](https://app.gethookd.ai/share/ad/169082912?signature=4ab996ca26c1daf73d6ef9a482fc283fbce80f5ccef0bc6ead1abbcdb159c5e0) |
| 16 | 171191667 | Bild | 03.09. | 36 | 100 | A (C) | „“But you'd need a huge washing machine for that” [Emoji: Lachen]“ | Text-Post plus Produktfoto, keine Person | [AL](https://www.facebook.com/ads/library/?id=1583757549405276) · [GH](https://app.gethookd.ai/share/ad/171191667?signature=b03cc4b1b86af6280d5edfa0028fe241e19fd20d3b3592e580dd3f576a92669d) |
| 17 | 172403389 | Bild | 05.09. | 34 | 100 | B (B) | durchgestrichen: „A light duvet can't keep you warm in winter.“ | Myth-Busting plus Farbstapel | [AL](https://www.facebook.com/ads/library/?id=1725326416267519) · [GH](https://app.gethookd.ai/share/ad/172403389?signature=fc57a29e066c788034eca64a557143f0c3e0b71232ea5868d51df06e7536000f) |
| 18 | 172760571 | Bild | 06.09. | 33 | 100 | F-Social-Proof (B) | „“It's what I've been looking for all this time!” — Customer, UK“ | Testimonial plus Farbstapel | [AL](https://www.facebook.com/ads/library/?id=1415553300514250) · [GH](https://app.gethookd.ai/share/ad/172760571?signature=82cd0a698c2d4720c44c69a474abfa9e4e1f24189f59d7dd6d1f216aaf8e25b8) |
| 19 | 173307160 | Bild | 07.09. | 32 | 81 | F-Angebot + Knappheit (B) | „2 FREE Pillow Cases … Only 79 left in Mint Green – FREE this week only“ | KI-Schlafzimmer (C2PA: KI) | [AL](https://www.facebook.com/ads/library/?id=1770207397626174) · [GH](https://app.gethookd.ai/share/ad/173307160?signature=20a01e20e8d0bc5720968b8ee00d824e45a8e18af15aa506b60fd22b7789241f) |
| 20 | 174599778 | Bild | 09.09. | 30 | 74 | B (C) | „CoolRest™ Cooling Duvet – ON/OFF: Cools all night long … Sweat-free nights“ | ON/OFF-Infografik; trägt den Namen eines **anderen** Pleene-Produkts (CoolRest) | [AL](https://www.facebook.com/ads/library/?id=2301727147248244) · [GH](https://app.gethookd.ai/share/ad/174599778?signature=0f3b267681520755857f3c8967162b7f9b49eb9f935ce9ac83a4c94572252bc1) |

**Verteilung:**

- **Format:** 11 Videos und 9 Bilder.
- **Videolängen:** 16, 16, 16, 27, 27, 29, 38, 47, 47, 50 und 93 s (Median 29 s).
- **Inhalts-Angle:** C 5, F-Knappheit/Farbe 5, A 2, B 2, E 2, F-Einwand 2, F-Social-Proof 1, F-Angebot 1.
- **Text-Angle laut s1:** C 7, F-Knappheit 5, B 3, F-Social-Proof 3, F-Einwand 2.
- **Landingpage:** alle 20 auf `/products/easyrest`.
- **Zielland:** 13 laut GetHooked GB, 7 ohne Länderangabe (151025063, 171191667, 172760571, 151025052, 169082912, 173307160, 174599778); GB für diese 7 nicht verifiziert (Indiz: GB-PDP `/products/easyrest`, auf die 52 der 63 GB-markierten und keine der 37 US-markierten aktiven Ads verlinken; GBP-Copy „worth £39.99“ im Anzeigentext von 151025063, 171191667 und 174599778, „~~£39.99~~“ im Bild von 173307160, „— Customer, UK“ im Bild von 172760571; bei 151025052 und 169082912 weder £ noch UK-Bezug, Indiz nur die PDP). Live-Abruf `get_ad` am 08.10. abends: `countries` ist bei allen 7 weiterhin `[]`.
- **CTA:** überwiegend SHOP_NOW. ORDER_NOW nutzen die Textfamilien T04 und T25 (145443331, 145443318, 163921089, 168246678/686), SEE_DETAILS nutzt 136389861.

**Starke Kandidaten (7, alle aus dem September):**

| ID | Format | Start | Tage | Score | LP | Kern |
|---|---|---|---|---|---|---|
| 178749258 | Bild | 16.09. | 23 | 81 | easyrest-duvet | „No Launderette Needed. Ever.“, erstes „30% off“ |
| 178749251, 178749254, 178749247 | Video 34–35 s | 16.09. | 23 | 81 / 70 / 70 | easyrest-duvet | Winter-Kommentar-Hooks |
| 179476350 | Bild | 16.09. | 22 | 81 | easyrest-duvet | „Warm Enough For A British Winter“ |
| 180153186 | Bild | 20.09. | 21 | 66 | easyrest | Vorher/Nachher |
| 182988073 | Video 25 s | 21.09. | 18 | 72 | easyrest | Farb-Reveal |

Laut Live-Abfrage in s2 sind 178749xxx und 179476350 seit 07.10. inaktiv.

#### 2.1.2 Steckbrief der typischen Winner-Ad

| Merkmal | Ausprägung | Belege |
|---|---|---|
| Format | Video 9:16 mit 16–50 s; daneben ein einfaches Bild mit maximal 2 Textzeilen | 11 Videos, 9 Bilder |
| Länge | zwei Cluster: **16 s** (KI-Template, nur Text) und **27–50 s** (Sprecher). Die einzige Langform ist 133366534 (93 s) | 139561428/410/491 (16 s); 168246678/686 (27 s); 151025063 (29 s); 145443331/163921089 (47 s); 145443318 (50 s) |
| Hook-Typ | Ich-Satz (Bekenntnis bzw. Testimonial), Knappheit/Farbe, Einwand bzw. Prüfliste, Schmerz bzw. Warnung, Ekel | Abschnitt 2.2 |
| Sprecher | entweder **echter Creator mit O-Ton** (3), **Off-Stimme über Kompilation** (3) oder **kein Sprecher, KI-Bild und Musik** (5). Dass eine Person im Hook in die Kamera spricht, ist selten (nur 145443331/163921089, 145443318 und der KI-Presenter in 136389861) | Tabelle 2.1.1 |
| Aufbau Sprecher-Video | Hook → „duvet and cover in one“ → Waschmaschine/Trockner → Temperatur (warm im Winter, kühl im Sommer) → „I swear to you, my bed always feels fresh“ → Kissenbezüge „super soft“ → Farben → Angebot → „test it yourself“ | 136389861, 145443331, 145443318, 151025063, 163921089 |
| Aufbau Template-Video | Text-Hook (Knappheit/Angebot) 0–3 s → „The duvet with no cover / Wash the whole thing“ 3–7 s → „Dry in 2 hours / Back on the bed“ 7–10,8 s → Angebotskarte bis 16 s | 139561428, 139561410, 139561491 |
| Angebot | „2 free Pleene™ Pillow Cases (worth £39.99)“ plus „90-night trial“, oft „This week only“. In keiner Winner-Ad steht „30% off“; das taucht erst ab 16.09. auf (178749258). 151025052 nennt kein Angebot | alle außer 151025052 |
| Beweis | meist nur ein Ich-Testimonial („I swear to you…“). Zahlen („Over 10,000 sleepers“, „96%“) und Review-Karten nur in 133366534 | 133366534 |
| LP | `/products/easyrest` (GB-PDP mit Kaching-Bundles, Gratis-Kissenbezüge im ATF) | alle 20 |
| Primärtext | wenige Textfamilien: **T01** „Duvet + Cover in One … ✓ Hypoallergenic and kind to sensitive skin / Get 2 free Pleene™ Pillow Cases today (worth £39.99). / 90 nights to try it risk-free.“, T04, T08, T15, T19, T25, T26 | s1-Anhang |

#### 2.1.3 Skript-Templates

**Generation 1 (Juni bis August; 136389861, 151025063, 145443331, 163921089, 145443318, ab 01.10. als Kopie in 193234221 und 193234219):**

| Schritt | Wortlaut (Beispiel) | Beleg |
|---|---|---|
| 1 Hook | Ich-Satz oder Warnung (siehe 2.2) | – |
| 2 Produkt | „duvet and cover in one … no more separate bed linen“ | 136389861, 145443331 |
| 3 Waschen | „Just put it in the washing machine and then in the tumble dryer.“ | 145443331 12,56–15,12 s; 145443318 14,96–17,82 s; 151025063 8,32–11,44 s |
| 4 Temperatur | „the breathable fibres adapt to your body. Nice and warm in the winter, comfortable and cool in the summer.“ | 145443318 21,76–27,5 s; 151025063 11,44–17,76 s |
| 5 Frische | „I swear to you, my bed always feels fresh.“ | 136389861 24–26 s; 145443331 25,2–27,8 s; 145443318 28–30 s |
| 6 Zusatznutzen | „the Pleene™ Pillow Cases really feel super soft“ | 145443318 30,62–36,10 s |
| 7 Farben | „And the Pleene EasyRest™ comes in loads of limited colours and all different sizes.“ | 145443331 31,04–35,44 s |
| 8 Angebot | „two free … Pillow Cases worth £39.99 and a 90-night trial sleep guarantee“ | 136389861, 151025063 |
| 9 Abschluss | „you can simply test it yourself“ | Gen-1-Videos |

**Generation 2 (ab 25.09.; 184134597/616/607, 200037044/061/062, 200037052/047/059, 200037049/045/063):**

| Schritt | Wortlaut (Beispiel) | Beleg |
|---|---|---|
| 1 Hook plus Persona | Humor-Frust („Every wash day, my duvet cover turns into a demented octopus.“) oder Hygiene-Frage („Quick question, when you change your bed, what actually gets washed?“) oder Persona („This is Bella.“, „I'm 71“) | 184134616 0–4,28 s; 200037044 0–2,8 s; 200037049 |
| 2 Problem | „The duvet underneath never got washed because it didn't fit in the machine“ | 200037045 13,2–21,04 s |
| 3 Waschen und Trocknen | „The double goes straight into my normal 7kg washing machine, then the tumble dryer, and it's dry in two hours.“ | 200037047 34,52–40,48 s; 184134597 17,6–25,92 s |
| 4 Wärme | „It's 10.5 tog, so it's every bit as warm as a winter duvet, just without the weight,“ | 184134597 25,92–31,12 s; 200037044 30,2–34,2 s |
| 5 Atmung | „and the breathable fibres mean it never feels stuffy on you.“ | 184134597 31,12–34,6 s |
| 6 Frische | „I swear to you, my bed always feels fresh.“ (Satz aus Gen 1 übernommen) | 184134597 34,6–37,96 s; 200037052 58,4–60,96 s |
| 7 Angebot | „30% off, plus two free … pillowcases“ | Gen-2-Videos |
| 8 CTA | „Tap the link below and have a look.“ | Gen-2-Videos |

**Was sich zwischen den Generationen ändert:**

- Gen 2 ersetzt das vage Temperaturversprechen durch eine **Zahl** („10.5 tog“).
- Gen 2 präzisiert die Waschmaschine auf „7kg“.
- Gen 2 stellt **Hygiene als Problem** an den Anfang. Gen 1 nutzt Hygiene nur als Nebennutzen („feels fresh“).
- Ob Gen 2 besser performt, ist nicht belegt. Kein Gen-2-Video hat bisher einen Score über 44 (184134597: 41; 2000370xx laut Live-Abfrage maximal 44).

#### 2.1.4 Varianten-Stammbaum (Familien mit IDs, Start, Laufzeit)

| Familie | Mutter-Ad (Start, Tage, Score) | Ableger (Start, Score, Status) | Art | Befund |
|---|---|---|---|---|
| V1 Creator „Everyone said it. They were right.“ (Datei a22e6497) | 145443331 (14.08., 56 T., 100, used 2) | 163921089 (27.08., 43 T., 100, Re-Upload); 193234221 (01.10., tb-6, 52; live seit 07.10. inaktiv); Hook-Swaps 145443318 (14.08., 56 T., 74) und 193234219 (01.10., tb-6, 1) | Re-Upload und Hook-Swap | Der Re-Upload vom August wurde Winner, die Oktober-Kopien auf tb-6 nicht. Dazu kommen 15 inaktive Ads mit T04-Text (Inhalt nicht verifiziert); eine lief 31 Tage bis 13.09. |
| V2 Hygiene-Kompilation (Datei 9877275e, 93 s) | 133366534 (03.08., 67 T., 100) | 193234275 (01.10., easyrest, 52, Octopus-Primärtext); 193234279 (01.10., tb-6, 44, live 41); Text-Schnittfassung 193234224 (01.10., tb-6, 1, live seit 07.10. inaktiv) | Re-Upload und Neuschnitt | Einzige Ekel-Ad unter den Winnern. Die Kopien bleiben deutlich unter dem Original. |
| V3 Schmerz-Skript | 136389861 (11.06., 120 T., 61) | 151025063 (22.08., 48 T., 86, neuer Hook „… pain in my shoulders and back“); 200490716 (06.10., 12, eigenes Skript mit KI-Seniorin „at my age“) | Hook-Swap, dann Neuproduktion | E funktioniert als Langläufer. Neue E-Ads vom 25.09. starben in höchstens 7 Tagen (siehe 2.5). |
| V4 KI-Türrahmen-Template (16 s) | 139561428 Hearth Red, 139561410 Mint, 139561491 Blue (alle 07.08., 63 T., 100/100/86) | Re-Uploads 185228755 (27.09., 60) und 200490701 (06.10., 12) von 139561410; Neuschnitt mit Tog-Hook 185228767 (27.09., 60), davon 193234216 (02.10., tb-6, 1); Statics im selben Look: 151025052 (20.08., 50 T., 61), 169082912 (31.08., 39 T., 74), 173307160 (07.09., 32 T., 81), 184134598 (25.09., 41, mit 30% off) | Farb- und Hook-Varianten | Robusteste Familie mit 3 Video- und 3 Bild-Winnern. Die Farbe wird als Variable getauscht. |
| V5 Checkliste „check 3 things“ | 168246678 (29.08., 41 T., 100) | Hook-Variante 168246686 (29.08., 86); 168246672 inaktiv; Re-Uploads 185228764 (27.09., 1) und 200490712 (06.10., 12, live nach 2 Tagen inaktiv) | Hook-Variante, Re-Upload | Das Text-A/B lief mit gleicher Laufzeit: der „check 3 things“-Hook kam auf Score 100, der „Seen coverless duvets…“-Hook auf 86. Die Re-Uploads scheitern. |
| V6 Farb-Reveal | 182988073 (21.09., 18 T., 72, Live 61) „Best thing I got for years.“ | 182988111 „Your bed is boring.“ (1); 182988108 „7 colours. Your choice.“ (1) | 3 Text-Hooks auf einem Video | Nur der Social-Proof-Hook trägt. |
| V7 „Pick a colour. Watch.“ | 2 Ads mit 53–55 Tagen, am 28. bzw. 30.09. beendet | 177443533 (15.09., 1); 185228773 (27.09., 1); 200490708 (06.10., 12) | Re-Uploads | Die Langläufer wurden durch Kopien ersetzt, die bisher nicht tragen. |
| V8 Cue-Cards „Be honest. When did you last wash it?“ | 177443532 (15.09., 24 T., 1) | 185228772 (27.09., 1); 193234218 (01.10., tb-6, 1) | Re-Uploads | Hygiene-Scham ohne Sprecher. Alle aktiven Fassungen haben Score 1. |
| V9 Winter-Kommentar-Hook | 178749251 / 178749254 / 178749247 (16.09., 23 T., 81/70/70) | Statics 178749258 (81), 179476350 (81), 180646058 (41) | 3 Hooks, ein Body | B mit Einwand-Kommentar („Looks lovely, but you'll freeze under that in winter.“). Live seit 07.10. inaktiv, trotz hoher Scores. |
| V10 Winter-Shorts (KI, 16 s) | – | 200037058 / 053 / 051 (05.10., 22; live 32/32/44) | 3 Overlay-Hooks | Neuer B-Test |
| V11 Persona-Familien | – | „When did you last wash“: 200037044 (live 44), 200037061, 200037062. Spare Bed: 200037052, 200037047 (live 44), 200037059. Bella: 200037049, 200037045 (live 44), 200037063 (alle 05.10.) | je 3 Hooks auf einem Body | Hygiene als Geschichte. Je Familie hat eine Variante früh Score 44. |
| V12 UGC-Zwillinge GB/US | – | 200490722/658 („My back just can't take this anymore.“), 721/655 (Waschdemo), 718/660 („I used to need help with this.“), 714/657 („I got rid of my duvet cover…“), 719/996 („This is your sign to rethink your duvet.“); nur US: 656, 654 (alle 06.10.) | identische Datei auf GB- und US-Seite | Markttest mit identischem Creative |
| V13 Octopus-Hooktest | – | 184134597 (25.09., 41) „I bloody hate changing the bed, not the sheets, that bit…“; 184134616 (1) „… demented octopus“; 184134607 (1) „Changing a duvet cover is the work of the devil.“ | 3 Hooks, ein Body (Gen 2) | Nur der Hook aus der Winner-Familie V1 („I bloody hate…“) erreicht Score 41. |
| S1 T01-Bildtest (Juni) | 136388964, 136388847 (11.06., 120 T., 100) | 136390001 (1), 133366116 (116 T., 1), 171191667 (100), 174599778 (74), 180153186 (66), davon 182988115 (41); 182988114 (41); 193234214/215 (52); Kopie 200490706 (06.10., live nach 2 Tagen inaktiv) | Bild-Varianten auf gleichem Text T01 | 58 T01-Ads auf easyrest liefen 30–97 Tage und wurden Ende August bzw. September abgeschaltet. |
| S2 T15 „Properly Warm, Never Heavy“ | 172403389 (05.09., 34 T., 100) | 172760571 (100), 173307160 (81), 178011633 (Relaunch von 172403394), Klon 185228774 (27.09., 1), 193234278 (Lavender-Copy, 40) | Bild-Varianten | 3 Winner aus einer Textfamilie |
| S3 Super-King-Bild | 157492463 (inaktiv) | 182988119 (60), 180646058 (41), 185228765 (1) | Re-Upload | – |
| S4 „What bed have you got?“ | 145443340 und 145443335 (je 37 T., inaktiv) | 182988112 (1), 182988109 (1), 182988091 (41) | Re-Upload | – |
| S5 US-Serien | 182988xxx (23./24.09.), 1868938xx (29.09.) | GB-Spiegelungen 200490723–726, 709, 720, 725 (06.10.) | Markt-Spiegelung | „comforter“-Wortlaut landet auf der GB-PDP |

---

### 2.2 Die 5 Hook-Muster der Winner

| # | Muster | Wirkmechanismus | Beispiele aus Winnern (wörtlich, mit ID) | Zweitbelege außerhalb der Winner |
|---|---|---|---|---|
| 1 | **Ich-Bekenntnis bzw. Testimonial-Satz** (UGC, erste Person) | Provokante oder gestandene Ich-Aussage, die erst im Body aufgelöst wird; wirkt wie eine echte Empfehlung | „I haven't changed my bed linen in three months and it's never felt fresher.“ (145443331, 163921089; 0–3,76 s) · „I bloody hate changing the bed“ (145443318) · „I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“ (151025063) | 184134597 „I bloody hate changing the bed, not the sheets, that bit…“ (41); 200490716 „I'm not going to lie, at my age, changing the bed had become a real…“ |
| 2 | **Knappheit/Farbe als Text-Hook** (ohne Sprecher) | Farbe und Restmenge, oft kombiniert mit Gratis-Angebot und Frist | „Only 17 left in Hearth Red“ (139561428) · „This week only: 2 FREE Pillow Cases with every DUVET“ / „Only 26 left in Mint Green“ (139561410, 169082912) · „Everyone's buying it in Coastal Blue“ / „Only 19 left“ (139561491, 151025052) | 173307160 „Only 79 left in Mint Green“; 184134598 „Mint Green: only 12 left.“ |
| 3 | **Einwand bzw. Prüfliste** (Kaufhilfe, Myth-Busting, zitierter Zweifel) | Nimmt den Hauptzweifel vorweg (Waschmaschine, Wärme, „Trend“) und beantwortet ihn | „Before you buy a coverless duvet check 3 things“ (168246678) · „Seen coverless duvets all over your feed?“ (168246686) · „“But you'd need a huge washing machine for that” [Emoji: Lachen]“ (171191667) · durchgestrichen „A light duvet can't keep you warm in winter.“ (172403389) | 178749251 „Looks lovely, but you'll freeze under that in winter.“ (81) |
| 4 | **Schmerz bzw. Warnung** („don't do this“, „STOP doing“, Problemfrage) | Körperlicher bzw. Alltags-Schmerz plus Verbot; spricht ältere und belastete Käufer an | „If your shoulders ache, don't do this.“ (136389861) · „3 things to STOP doing when you make the bed“ (136388964) · „Just want to sleep... but you've still got to change the bed?“ (136388847) | 200490722 „My back just can't take this anymore.“ |
| 5 | **Ekel bzw. Schock** (Hygiene-Provokation) | Direkter Angriff auf das eigene Bett, danach Mechanismus und Beweis | „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ (133366534, 0–4 s, mit Badge „No more bed changing [Emoji: Kreuz]“) | Nur 1 Winner. Kopien 193234275 (52) und 193234279 (44); Persona-Varianten 200037061 „How old is the duvet you slept under last night? Mine was 12 years old …“ und 200037045 „If your dog sleeps on your bed, when did you last wash the duvet?“ (beide 05.10.) |

**Was die Hooks verbindet:**

- **Kein Hook nennt das Produkt.** Alle Hooks setzen beim Problem oder beim Zweifel an.
- **Kaum Fragen-Hooks:** nur 136388847 und 168246686. Die Fragen-Hooks vom September/Oktober („Be honest. When did you last wash it?“, „Quick question…“) sind bisher kein Winner.
- **Text-Hooks dominieren:** Alle 11 Video-Winner zeigen den Hook als Einblendung. 5 davon haben keinen Sprecher (139561428/410/491, 168246678/686), die übrigen 6 blenden das Gesprochene als Untertitel ein.

---

### 2.3 Angles A–F

**Alle 137 aktiven Ads nach Inhalts-Angle** (Quelle `wf/s5_scripts/angles.py`; Ø Tage und Ø Score beziehen sich auf die aktiven Ads des Angles):

| Angle | aktiv | Winner | Starke Kand. | Neue Tests | Ø Tage | Ø Score | Score ≥ 41 | Video / Bild | davon US-LP |
|---|---|---|---|---|---|---|---|---|---|
| A Hygiene | 28 | 2 | 1 | 23 | 15,9 | 23,6 | 8 | 16 / 12 | 5 |
| B Temperatur (Wechseljahre: 0) | 15 | 2 | 3 | 9 | 15,9 | 37,8 | 7 | 8 / 7 | 2 |
| C Beziehen | 47 | 5 | 2 | 34 | 20,6 | 19,8 | 12 | 18 / 28 (+1 DCO) | 22 |
| D Geschenk | 1 | 0 | 0 | 1 | 2,0 | 1 | 0 | 0 / 1 | 1 |
| E körperliche Beschwerden | 5 | 2 | 0 | 3 | 35,4 | 32,2 | 2 | 5 / 0 | 1 |
| F-Knappheit/Farbe | 14 | 5 | 1 | 6 | 28,4 | 49,3 | 9 | 9 / 5 | 0 |
| F-Selbstständigkeit im Alter | 11 | 0 | 0 | 11 | 7,4 | 1,0 | 0 | 2 / 9 | 7 |
| F-Einwand/Kaufhilfe | 7 | 2 | 0 | 2 | 20,7 | 34,6 | 3 | 4 / 3 | 0 |
| F-Social-Proof | 3 | 1 | 0 | 2 | 17,0 | 47,0 | 1 | 0 / 3 | 1 |
| F-Neuheit/Größe | 3 | 0 | 0 | 1 | 16,3 | 34,0 | 2 | 0 / 3 | 0 |
| F-Angebot | 2 | 1 | 0 | 1 | 17,5 | 47,0 | 1 | 0 / 2 | 0 |
| F-Upgrade/Luxus | 1 | 0 | 0 | 1 | 3,0 | 12 | 0 | 1 / 0 | 1 |
| **Summe** | **137** | **20** | **7** | **94** | | | **45** | **63 / 73 (+1)** | **40** |

**Nur GB (ohne die 40 US-Ads auf `/products/easyrest-comforter`):**

| Angle | aktiv | Winner | Ø Tage | Ø Score | Video / Bild |
|---|---|---|---|---|---|
| C | 25 | 5 | 28,7 | 31,8 | 13 / 12 |
| A | 23 | 2 | 16,3 | 26,2 | 16 / 7 |
| B | 13 | 2 | 16,5 | 43,5 | 8 / 5 |
| F-Knappheit/Farbe | 14 | 5 | 28,4 | 49,3 | 9 / 5 |
| F-Einwand/Kaufhilfe | 7 | 2 | 20,7 | 34,6 | 4 / 3 |
| E | 4 | 2 | 43,5 | 40,0 | 4 / 0 |
| F-Selbstständigkeit im Alter | 4 | 0 | 4,5 | 1,0 | 1 / 3 |
| F-Neuheit/Größe | 3 | 0 | 16,3 | 34,0 | 0 / 3 |
| F-Social-Proof | 2 | 1 | 20,5 | 70,0 | 0 / 2 |
| F-Angebot | 2 | 1 | 17,5 | 47,0 | 0 / 2 |

**Deutung:**

- **F-Knappheit/Farbe** hat die höchste Winner-Quote (5 von 14) und den höchsten Ø Score (49,3). Der Angle läuft fast nur in GB und fast nur über das KI-Template V4. Er ist ein Verstärker (Dringlichkeit), kein eigenständiges Nutzenversprechen. Allerdings scheiterten auch reine Knappheits-Familien: „Only 26 Left In Hearth Red“ (3 von 3 Verlierer) und „Ready for the colder nights“ (4 von 4 Verlierer).
- **C (Beziehen)** ist das Rückgrat nach Volumen. In GB ist C solide (Ø 31,8). Der Gesamtwert wird durch 22 neue US-Ads mit Score 1 gedrückt.
- **A (Hygiene)** ist der Angle mit dem größten Testaufwand der letzten 14 Tage (34 der 119 Launches nach Text-Angle, 19 der 79 aktiven nach Inhalt), bringt aber nur 2 Winner. Beide verbinden Hygiene mit einem anderen Mechanismus:
  - 133366534: Ekel, dann Lösung, dann Beweise.
  - 171191667: Einwand Waschmaschine.
- **B (Temperatur)** hat unter den Kern-Angles den höchsten Ø Score (37,8, GB 43,5) und 3 Starke Kandidaten (Winter-VO V9). B wird bei Pleene ausschließlich als **Winterwärme bzw. Nicht-Schwitzen** gespielt. **Wechseljahre kommen in 0 Ads vor** (und in 0 Bewertungen, s4).
- **E (Beschwerden)** hat die längste Laufzeit (Ø 35,4 Tage), getragen von den alten Winnern 136389861 und 151025063. Die neuen E-Ads vom 25.09. hielten höchstens 7 Tage (siehe 2.5). Ab 06.10. kommt E als Paar-UGC und KI-Seniorin wieder.
- **F-Selbstständigkeit im Alter** ist ein neuer, US-getriebener Angle (11 aktiv, alle Score 1, Ø 7 Tage). Er wurde ab 30.09. bzw. 06.10. auf GB übertragen (189550275, 200490709, 200490718, 200490720).
- **D (Geschenk)** existiert nur als 200490661 (US, 07.10.). s4 zählte noch 0 Geschenk-Ads, weil die Ad danach startete.

**Text-Angle gegenüber Inhalts-Angle:**

- Viele Bilder tragen den Beziehen-Text T01 („No More Fighting With Duvet Covers“), zeigen aber Hygiene (133366116, 171191667, 193234214/215) oder Temperatur (174599778).
- Die Video-Winner 136389861 und 151025063 haben ebenfalls T01-Text, sind inhaltlich aber Schmerz-Ads (E).
- **Folge:** Eine Auswertung nur nach Primärtext unterschätzt A und E und überschätzt C.

---

### 2.4 Neue Tests der letzten 14 Tage (25.09.–08.10.)

#### 2.4.1 Testvolumen pro Woche (alle 692 Ads nach Startdatum, ISO-KW)

| KW | Zeitraum | Launches | heute aktiv | Verlierer (< 7 T.) | Video / Bild / sonst | Landingpages | Top-Text-Angles |
|---|---|---|---|---|---|---|---|
| KW23–30 | 01.06.–26.07. | 59 | 5 | n/a | n/a | n/a | n/a |
| KW31 | 27.07.–02.08. | 27 | 0 | n/a | n/a | n/a | n/a |
| KW32 | 03.–09.08. | 65 | 4 | n/a | n/a | n/a | n/a |
| KW33 | 10.–16.08. | 55 | 2 | 6 | 31 / 23 / 1 | easyrest 22, zipsheet-us 33 | C 28, F-Knappheit 8 |
| KW34 | 17.–23.08. | 37 | 2 | 9 | 26 / 11 / 0 | easyrest 23, zipsheet-us 8, everyday-duvet 6 | C 24, F-Knappheit 5 |
| KW35 | 24.–30.08. | 91 | 3 | 37 | 68 / 21 / 2 | easyrest 70, **duvet-10r 19** | C 41, F-SP 19, F-Angebot 10 |
| KW36 | 31.08.–06.09. | 73 | 4 | 31 | 56 / 15 / 2 | easyrest 71 | C 26, F-Knappheit 20, A 16 |
| KW37 | 07.–13.09. | 81 | 3 | 54 | 60 / 19 / 2 | easyrest 78 | **A 35**, C 14, F-SP 13 |
| KW38 | 14.–20.09. | 46 | 10 | 30 | 22 / 24 / 0 | easyrest 27, **easyrest-duvet 19** | A 25, B 6 |
| KW39 | 21.–27.09. | 76 | 37 | 21 | 32 / 43 / 1 | easyrest 57, **easyrest-comforter 17** | C 28, A 22 |
| KW40 | 28.09.–04.10. | 45 | 30 | 10 | 10 / 32 / 3 | easyrest 20, comforter 16, **tb-6 8** | C 16, **F-Selbstständigkeit 11**, A 9 |
| KW41 | 05.–07.10. (3 Tage) | 37 | 37 | 0 | 28 / 9 / 0 | easyrest 29, comforter 8 | C 15, A 10 |

- **Rhythmus:** Seit August starten 37–91 Ads pro Woche (Ø KW32–40: 63). Die letzten 14 Tage brachten 119 Launches, davon heute 79 aktiv und 40 inaktiv. In den 14 Tagen davor (11.–24.09.) waren es 126 Launches, davon nur noch 35 aktiv.
- **Überlebensquote:** Von den 337 Ads aus KW33–37 sind heute 14 aktiv (4,2 %). Der Verlierer-Anteil an den inaktiven Ads stieg von 23 % (August) auf 62 % (September).

#### 2.4.2 Launch-Tage (letzte 14 Tage)

| Datum | Wochentag | Launches | davon aktiv | Inhalt |
|---|---|---|---|---|
| 25.09. | Fr | 25 | 4 | Octopus-Hooks (184134597/616/607), Mint-30%-Static 184134598. 21 Ads (E- und A-Familien) inzwischen inaktiv |
| 27.09. | So | 12 | 8 | Re-Uploads alter Winner (185228755, 764, 772, 773, 774, 765), Lavender 185228766, Tog-Neuschnitt 185228767 |
| 28.09. | Mo | 4 | 1 | US-Diashow 185395501 |
| 29.09. | Di | 17 | 14 | US-Static-Serie 1868938xx („Selbstständigkeit im Alter“, Wortspiele „Retire…“) |
| 30.09. | Mi | 12 | 5 | GB-Übertragung 189550267/269/275, 190288311/319 |
| 01.10. | Do | 11 | 9 | Advertorial-Test tb-6 (193234214/215/218/219/221/224/279) und 193234275, 193234278 |
| 02.10. | Fr | 1 | 1 | 193234216 (tb-6) |
| 05.10. | Mo | 12 | 12 | Persona-Familien und Winter-Shorts 2000370xx |
| 06.10. | Di | 24 | 24 | UGC-Zwillinge GB/US, GB-Spiegelungen der US-Statics, Re-Uploads (200490701/706/708/712), KI-Seniorin 200490716, Lavender-Angebot 200490698 |
| 07.10. | Mi | 1 | 1 | Geschenk-Ad 200490661 (US) |

#### 2.4.3 Profil der 79 aktiven neuen Tests

- **Inhalts-Angle:** C 25, A 19, F-Selbstständigkeit 11, B 7, F-Knappheit/Farbe 6, E 3, F-Einwand 2, F-Social-Proof 2, F-Neuheit 1, F-Angebot 1, F-Upgrade/Luxus 1, D 1. Nur GB (55): A 18, C 14, B 6, F-Knappheit/Farbe 6, F-Selbstständigkeit 4, Rest 7.
- **Text-Angle aller 119 Launches:** C 34, A 34, F-Selbstständigkeit 15, F-Knappheit/Farbe 12, E 8, B 4, F-Angebot 3, F-Social-Proof 3, F-Neuheit 2, F-Einwand 2, D 1, n/a 1.
- **Format:** 44 Videos, 34 Bilder, 1 DCO. In GB 36 Videos und 19 Bilder. Video-Längen von 9 bis 93 s, Median 30 s, mit drei Clustern: 15–16 s (Template, Shorts), 23–30 s (UGC ohne Ton) und 44–51 s bzw. 73–93 s (Sprecher, Persona).
- **Landingpages (alle 119):** easyrest 85, easyrest-comforter 24, tb-6 8, easyrest-duvet 2.
- **Avatare bzw. Personas (neu):**
  - Großeltern 66–71 mit Gästebett, Enkeln und Hund: 200037052/047/059 („I'm 71“), 200037049/045/063 („I'm 66“).
  - Senioren mit Unabhängigkeitswunsch: 1868938xx, 189550275, 200490709/718/720/660; Beispiele „I CAN STILL DO THIS.“ (186893869), „STILL DOING IT MYSELF.“ (186893875/200490720), „I used to need help with this.“ (200490718).
  - Paar 55+ mit Rückenproblemen (200490722/658).
  - Seniorin „at my age“ mit Tochter als Käuferin (200490716: „Then my daughter got me the Plein Easy Rest Duvet“).
  - Gastgeber 35–60 (200037062).
  - US-Frau 30–50 mit Deko-Interesse (200490656/654).
  - Kinder, die für die Eltern kaufen (200490661, US).
- **Neue Hook-Formen:**
  - Fragen: „Quick question, when you change your bed, what actually gets washed?“ (200037044), „How old is the duvet you slept under last night?“ (200037061), „If a guest asked you when you last washed your duvet, not the cover, the duvet, what would you say?“ (200037062).
  - Persona-Intros: „This is Bella. She sleeps on our bed every night…“ (200037049), „Wet November walk, two muddy paws, straight onto the bed.“ (200037063).
  - Humor-Frust: „… demented octopus“ (184134616), „Changing a duvet cover is the work of the devil.“ (184134607).
  - Pattern-Interrupt: „Don't scroll. Pick your colour first.“ (185228773/200490708), „This is your sign to rethink your duvet.“ (200490719/200036996).
  - Winter-Einwand als Overlay: „TOO THIN FOR WINTER? LOOK CLOSER.“ (200037051).
- **Sprecher:**
  - Off-VO ältere Frau mit POV-Händen (Persona-Familien).
  - Off-VO, vermutlich weiblich (Octopus).
  - Echter UGC-O-Ton (200490655/721 Frau 50–60; 200490722/658 Paar; 193234221/219 Mann).
  - KI-Figur vor der Kamera (200490716).
  - Kein Sprecher, nur Musik (Template, Cue-Cards, Shorts, UGC-Paare 714/657, 718/660, 719/996).
- **KI-Anteil (Einschätzung aus s2, nicht verifiziert):** Bei 23 der 44 aktiven neuen Videos ist das Bild überwiegend KI-generiert. Dazu gehören 184134597/616/607, 185228755/764/767/772/773, 193234216/218, 200037058/053/051, die 6 Persona-Videos 2000370xx (POV-Bilder „wahrscheinlich KI“), 200490701/708/712 und 200490716 (KI-Seniorin). Echte Aufnahmen zeigen 21 Videos (193234219/221/224/275/279, 200037044/061/062, die 12 UGC-Videos vom 06.10. – 200490654/655/656/657/658/660/714/718/719/721/722 und 200036996 – sowie 185395501 mit Standbildern). Bei den Statics tragen 193234214/215 und 182988114 C2PA-Signaturen von Google bzw. OpenAI; mehrere 1868938xx-Motive haben „KI-Anmutung“.

**Klassifikation der 79 aktiven neuen Tests:**

| Art | IDs | Anzahl |
|---|---|---|
| 1:1-Re-Upload bestehender Medien | 185228755 (= 139561410), 185228764 (= 168246678), 185228765 (Super-King-Bild), 185228772 (= 177443532), 185228773 (= 177443533), 185228774 (= 172403389), 190288311 (= 182988027), 193234218 (= 177443532), 193234221 (= 145443331), 193234275 und 193234279 (= 133366534), 200490701 (= 139561410), 200490706 (= 136388847), 200490708 (= 177443533), 200490712 (= 168246678), 200490709 (= 186893837), 200490720 (= 186893875), 200490723 (= 182988041), 200490724 (= 186893814), 200490725 (= 182988043), 200490726 (= 182988035) | 21 |
| GB/US-Zwilling (gleiche Datei am selben Tag) | 200490658, 200490655, 200490660, 200490657, 200036996 (US-Seite der GB-Ads 722, 721, 718, 714, 719) | 5 |
| Hook-Variante bzw. Neuschnitt eines bekannten Bodys | 184134597/616/607, 185228767, 193234216, 193234219, 193234224, 200037044/061/062, 200037052/047/059, 200037049/045/063, 200037058/053/051 | 19 |
| Neu (erstmals gesehenes Creative bzw. Motiv) | 184134598, 185228766, 185395501, 1868938xx (14 inkl. DCO 186893864), 189550267, 189550269, 189550275, 190288319, 193234214, 193234215, 193234278, 200490654, 200490656, 200490661, 200490698, 200490714, 200490716, 200490718, 200490719, 200490721, 200490722 | 34 |

Die Abgrenzung ist teils unscharf. 189550269 nutzt das Foto aus 182988024, 190288319 das aus 186893878, 193234278 übernimmt das T15-Template, und die Persona-Familien zählen erst ab dem zweiten Hook als Varianten. Die Zuordnung „Re-Upload“ stützt sich auf Datei- bzw. md5-Gleichheit laut s2.

**Frühe Signale (Score ≥ 41 bei den 79):**

- Score 60: 185228755, 185228766, 185228767
- Score 52: 193234275, 193234221, 193234214, 193234215
- Score 44: 193234279
- Score 41: 184134597, 184134598
- Live-Abfrage s2: 200037044, 200037045, 200037047 und 200037051 je 44

Die meisten stammen aus den Familien V1, V2 und V4 oder aus den Persona-Familien. **Von den 34 neuen Creatives erreichen bisher nur 4 Score ≥ 41:** 185228766 (Lavender-Static, 60; die Headline „NEW: Lavender Mist“ lief schon ab 05.09. in 3 Ads mit je 32 Tagen, ob dort dasselbe Motiv, ist nicht verifiziert), 193234214/215 (KI-Statics, 52, tb-6) und 184134598 (Mint-Static mit 30 %, 41). Alle 4 sind Statics. Kein neues Video, keine US-Ad und kein Selbstständigkeits-Creative liegt bisher über Score 12.

#### 2.4.4 Deutung der Teststrategie

1. **Hohes Volumen, schnelles Abschalten.**
   - Rund 60 Launches pro Woche, gebündelt an 1–3 Tagen.
   - Die Welle vom 25.09. (25 Ads) war nach höchstens 12 Tagen bis auf 4 Ads abgeschaltet.
   - 202 Verlierer insgesamt; im September endeten 62 % der inaktiven Ads nach weniger als 7 Tagen.
2. **Struktur: 3 Hooks auf einem Body.**
   - V9 (178749251/254/247), V13 (184134597/616/607), V10 (200037058/053/051) und die drei Persona-Familien V11.
   - Dazu Text-Hook-Tests auf gleichem Video (V5 168246678/686, V6 182988073/111/108).
3. **Winner-Recycling.**
   - Alte Winner werden 1:1 neu hochgeladen (vermutlich in neue Kampagnen bzw. Ad Sets, nicht verifiziert): 185228755, 185228764, 200490701, 200490712, 193234221, 193234275/279.
   - Die Kopien starten bei Score 1 bzw. bleiben unter dem Original. 200490712 und 200490706 waren nach 2 Tagen wieder aus.
4. **Angle-Rotation mit der Saison.**
   - Sommer: C und F-Knappheit.
   - Ab KW37: Hygiene (A 35 von 81).
   - Ab KW38: Winter/Tog (B, eigene LP easyrest-duvet) und 30 % Rabatt.
   - Ab KW40: Selbstständigkeit im Alter.
   - Ab KW41: Hygiene als Persona-Geschichte.
5. **Funnel-Tests parallel.**
   - duvet-10r (Listicle-LP, KW35, 19 von 19 Verlierer)
   - easyrest-duvet (Winter-Klon, 6 aktiv)
   - tb-6 (Advertorial, 8 Ads ab 01.10.)
6. **Markterweiterung USA.**
   - 40 aktive Ads auf der Comforter-PDP seit 23.09.
   - Zwillings-Launches am 06.10.
   - Rückspiegelung der US-Statics mit „comforter“-Wortlaut auf die GB-PDP.
7. **KI als Produktionsmittel.** Rund die Hälfte der neuen Videos ist KI-basiert. Neu ist die KI-Person als Sprecherin (200490716). Zuvor diente KI nur als Kulisse bzw. Hand.
8. **Einordnung (Einschätzung):** Pleene sucht den nächsten Winner nach dem Sommer-Set, hat ihn aber noch nicht gefunden. Die besten neuen Signale sind wieder Kopien oder Ableger der Sommer-Winner. Die neuen Angles (Selbstständigkeit, US-Statics) zeigen bisher durchgehend Score 1.

---

### 2.5 Aufgegebenes: Verlierer, inaktive Familien und Lehren

**Verlierer gesamt:** 202 von 555 inaktiven Ads liefen weniger als 7 Tage.

| Dimension | Verlierer / inaktiv | Quote |
|---|---|---|
| Video | 141 / 347 | 41 % |
| Bild | 56 / 192 | 29 % |
| DPA (Katalog) | 5 / 8 | 62 % |
| Start August | 60 / 257 | 23 % |
| Start September | 140 / 225 | 62 % |
| EasyRest | 184 / 479 | 38 % |
| ZipSheet | 18 / 76 | 24 % |

**Familien ohne aktive Ad (mindestens 3 Ads, Auswahl nach Größe; Quelle `wf/s5_scripts/losers.py`):**

| Start | Familie (Headline) | Ads | davon Verlierer | max. Tage | Ende | Angle | Lehre |
|---|---|---|---|---|---|---|---|
| 03.08. | „Never Lift Your Mattress Again“ (ZipSheet) | 66 | 14 | 34 | 07.09. | C | **Zweites Produkt komplett eingestellt.** Dazu „Made for hands that hurt“ (6) und „Not your normal fitted sheet“ (4 von 4 Verlierer) |
| 07.08. | „Best decision I ever made“ | 12 | 7 | 18 | 12.09. | F-Social-Proof | Generischer Testimonial-Titel ohne Spannung trägt nicht |
| 14.08. | „Duvet & Cover In One“ | 11 | 6 | 31 | 28.09. | C | Produktbeschreibung als Hook ist zu schwach |
| 20.08. | „The Cover Is Sewn In“ | 12 | 6 | 12 | 12.09. | C | dto. |
| 25.08. | „A Duvet With No Cover?“ | 15 | 7 | 16 | 17.09. | F-Social-Proof | dto. |
| 25.08. | „End Of Season Sale“ | 12 | 7 | 17 | 23.09. | F-Angebot | Sale-Headline beendet. Der Rabatt wandert als „30% off“ in den Body (ab 16.09.) |
| 25.08. | „I've Quit Bed Linen“ | 4 | 4 | 5 | 29.08. | C | – |
| 29.08. | „2 Free Pillow Cases [Emoji: Geschenk]“ | 12 | 6 | 17 | 01.10. | F-Angebot | Angebot als Headline trägt nicht; als Abschluss ist es Standard |
| 29.08. | „The Duvet That Goes In The Wash“ | 12 | 6 | 9 | 12.09. | A | Waschbarkeit als Headline scheitert |
| 05.09. | „Done fighting with bed linen“ | 6 | 6 | 6 | 10.09. | C | – |
| 05.09. | „Only 26 Left In Hearth Red“ | 3 | 3 | 5 | 09.09. | F-Knappheit | Knappheit als Headline ohne Template-Video scheitert |
| 05.09. | „Ready for the colder nights“ | 4 | 4 | 6 | 10.09. | F-Knappheit/B | Winter zu früh bzw. zu vage |
| 16.09. | „"You'll Never Wash That." Watch Us“ | 3 | 3 | 4 | 19.09. | A | Hygiene-Challenge als Bild scheitert |
| 16.09. | „Which colour? Comment 1-9“ | 5 | 0 | 21 | 06.10. | F-Farbe | Kommentar-Quiz aufgegeben (wie „Which colour survives?“ 3 Ads, 9 Tage; „Which one is our bestseller?“ 3 Ads, 15 Tage). „Who wins in your house?“ lief bis 54 Tage |
| 25.09. | „A Winter Duvet You Can Actually Lift“ | 3 | 3 | 6 | 30.09. | E | Neue E-Ansätze fallen durch |
| 25.09. | „Change Your Bed Without The Pain After“ | 4 | 1 | 7 | 01.10. | E | dto. |
| 25.09. | „When did you last wash the duvet?“ / „Winter-ready in one wash“ / „Yes, it fits your machine“ / „You never actually wash your duvet“ | 5 / 3 / 5 / 4 | 4 / 2 / 1 / 0 | 10 / 7 / 10 / 12 | 01.–06.10. | A | Ganze Hygiene-Welle in höchstens 12 Tagen beendet |

**Weitere aufgegebene Linien:**

- **Listicle-LP `/pages/duvet-10r`:** 19 Ads in KW35, alle Verlierer (Headlines u. a. „No More Fighting With Duvet Covers“ 5, „Everyone said it“ 3, „End Of Season Sale“ 3). Der Pre-Lander-Gedanke kehrt mit tb-6 als Advertorial zurück.
- **T02-Headline „Be honest. When did you last wash it?“:** 51 Ads (45 Videos), 45 inaktiv (27 Verlierer), maximal 24 Tage, Starts 05.–15.09. gehäuft. Der Inhalt der inaktiven Ads ist nicht verifiziert; die Headline sitzt auch auf Nicht-Hygiene-Videos wie 185228767.
- **„The Duvet You Can Actually Wash“:** 20 Ads, 19 inaktiv, maximal 27 Tage.
- **95 Langläufer (mindestens 30 Tage) inzwischen beendet:**
  - 58 T01-Ads auf easyrest (30–97 Tage), 11 auf easyrest-pdp, 5 auf pleene-easyrest-duvet-2in1.
  - Abschaltwellen: 28./29.08. (viele mit 88–89 Tagen), 05.–08.09., 13./14.09.
  - Längste: 133364681 (Bild, 02.06.–06.09., 97 Tage).
  - Von der Juni-Kohorte laufen nur 136389861, 136388964, 136388847, 136390001 und 133366116 weiter.
- **Seit 07.10. inaktiv (Live-Abfrage s2):** 178749xxx (Winter-VO trotz Score 70–81), 179476350, 180646058, 193234221/215/224, 200490706/712, 190288319, 189550267.

**Lehren für die eigene Planung:**

1. **Headlines, die nur das Produkt beschreiben, scheitern** („Duvet & Cover In One“, „The Cover Is Sewn In“, „The Duvet That Goes In The Wash“). Winner-Headlines tragen eine Behauptung, einen Konflikt oder eine Knappheit.
2. **Hygiene allein trägt nicht.** Alle Hygiene-Familien ohne Ekel-Story und Beweisführung endeten nach 4–27 Tagen. Nur die 93-s-Kompilation 133366534 (Ekel, Mechanismus, Zahlen, Testimonials, Future Pacing) wurde Winner.
3. **Ein neues Schmerz-Creative ist schwer.** Die alten E-Winner laufen 48 bzw. 120 Tage, neue E-Ads vom 25.09. hielten nur 6–7 Tage. Die E-Botschaft wirkt offenbar nur mit glaubwürdiger Person (Einschätzung).
4. **Re-Uploads garantieren keinen Erfolg.** Die Kopien der Winner (185228764, 200490712, 200490706, 193234218) liegen bei Score 1 oder waren schnell aus.
5. **Kommentar-Quiz und reine Rabatt-Headlines wurden aufgegeben.** Das Angebot bleibt nur als Schluss-Element.
6. **Pre-Lander-Listicle (duvet-10r) gescheitert.** Für tb-6 liegt noch kein Ergebnis vor (2 von 8 Ads laut Live-Abfrage bereits inaktiv: 193234215, 193234224; 193234221 ebenfalls).

---

### 2.6 Avatare, die Pleene nicht anspricht (Abgleich mit dem Käuferprofil aus s4)

**Käuferprofil laut Bewertungen (s4):**

- **Herkunft:** 91,8 % GB (267 von 291 Trustpilot-Bewertungen).
- **Geschlecht der Konten:** 56 % männlich, 31 % weiblich, 13 % unklar. Geschätzt nach Vornamen, nicht verifiziert; Kontoinhaber und Nutzer sind nicht immer dieselbe Person.
- **Alter:** 16 Bewertungen nennen ein Alter oder einen Seniorenhinweis, alle Senioren: T003 (80er), T133 (84), T066 (späte 70er), T269 (77), T284 (72), T274 (66). Keine einzige Bewertung deutet auf jüngere Käufer hin.
- **Kaufmotiv:** vor allem Erleichterung beim Beziehen trotz körperlicher Einschränkung. Das Vokabular ist „fight“, „wrestle“, „struggle“, „battle“, „faff“, „nightmare“.

| Käufer-Segment (Reviews) | Belege in s4 | Wie Ads es heute bedienen | Lücke bzw. Chance |
|---|---|---|---|
| **Ältere Männer, Witwer, Alleinlebende** | 56 % Männerkonten; Witwer bzw. Alleinlebende T029, T177, T236, T079, T251 | Männliche Ich-Erzähler sind nur Creator ca. 30–40 (145443331/318, 193234221/219), dazu kommen männliche Off-Stimmen. **Ein älterer Mann spricht nur zweimal:** (1) im Paar-UGC 200490722 und seinem US-Zwilling 200490658 (Mann ca. 60–70, echter O-Ton mit Ansteckmikro und passendem f0-Wechsel, z. B. „And I haven't been too hot or too cold once.“; Start 06.10., Score 1); (2) als Hook-Presenter im Winner 136389861 (männlich, ca. 70+, lippensynchron, sehr wahrscheinlich KI, „If your shoulders ache, don't do this.“). **Stumm im Bild** ist ein älterer Mann in der Selbstständigkeits-Serie „Bedding Made for Independence“ 200490718/200490660 (ca. 65–75 im Bademantel, Einblendung „I used to need help with this.“), in der Farb-Serie 177443533/185228773/200490708 (ca. 55–65, Demonstrator), in 193234224 (ca. 65–75, Bademantel) und 178749251 (ca. 60+; beide laut Live-Abfrage seit 07.10. inaktiv), außerdem in 200490719/200036996 (ca. 55–65), als schlafendes Motiv in 186893864/862 (US) und als Paar ca. 65–75 in der US-Geschenk-Ad 200490661. Den Witwer gibt es nur in der dritten Person: Off-VO „George is over 80. A widower. Making the bed alone was always a struggle. Now it's easy.“ mit Review-Karte „George, 82“ in 133366534 (der gezeigte Mann wird auf ca. 45–55 geschätzt); „Peter R.“ ist in 193234224 nur ein eingeblendeter Name. Die übrigen Ads der Selbstständigkeits-Serie (1868938xx, 189550275, 200490709/720) zeigen nur Frauen. | **Kein älterer Mann als alleiniger Ich-Erzähler bzw. Witwer.** Er spricht nur im Paar (Hook ist der Rücken der Frau, Test mit Score 1) oder als KI-Autoritätsfigur, sonst ist er stummes B-Roll. Das ist der größte Widerspruch zwischen Käuferbasis und Creative. |
| **Hochbetagte 75+** | T003, T133, T066, T269 | Personas sind 66 und 71 Jahre alt (2000370xx, „I'm 66“, „I'm 71“). Die US-Statics zeigen Frauen ca. 60–75. | Die Altersgruppe 80+ fehlt. |
| **Konkrete Krankheiten** | Arthritis T064, T074, T249, T286; Rücken T046, T078, T274, T284; Herz T043; Chemo T070, T231; Diabetes T079; Mobilität T025, T290 | Nur allgemein: „If your shoulders ache…“ (136389861), „pain in my shoulders and back“ (151025063), „My back just can't take this anymore.“ (200490722/658), „at my age“ (200490716). Hände bzw. Arthritis gab es nur in der eingestellten ZipSheet-Familie „Made for hands that hurt“. | Keine Ad nennt Arthritis, Herz, Chemo oder Erschöpfung. E ist in den Ads ein Schulter- und Rückenproblem; Käufer erleben es als Krankheits- bzw. Kraftproblem. |
| **Paare mit unterschiedlichem Wärmeempfinden** | T054, T166, T289 | Nur indirekt: Louise-Zitat „I feel it is light, but I don't feel cold at night.“ (182988027, 190288311; die Original-Bewertung T166 nennt Ehemann und Ehefrau). Das Paar in 200490722/658 dreht sich um Rückenschmerzen. | Ein Hook wie „er schwitzt, sie friert“ fehlt, obwohl B der Angle mit dem höchsten Ø Score ist. |
| **Kinder kaufen für Eltern, Geschenke** | T171 (Mutter), T283 (Mutter), T196 (Sohn, Weihnachten), T200, T289, T252, T133 (Geburtstag) | 200490661 (US, 07.10.) „One Less Chore For Mum & Dad.“; 200490716 „Then my daughter got me the Plein Easy Rest Duvet“ | **In GB keine Geschenk-Ad, obwohl Weihnachten bevorsteht.** |
| **Zweitbett-Haushalte** (Gästezimmer, Camper, Ferienhaus) | Camper T072; Ferienhaus T251; Gäste T027 („so no guilt for us or short stay visitors!!“) | Gästezimmer seit 05.10. (200037052/047/059, „The spare room is the coldest room in the house“); US 200490654 | Camper und Ferienhaus fehlen. |
| **Mehrfachkäufer** | 28 Bewertungen mit Mehrfachkauf | 193234278 „“Got 3, love them.” — Customer, back for the third time.“; 193234224 („Peter R. ordered himself a second…“) | Kein Bundle-Narrativ „eine für jedes Bett“, obwohl Kaching „Couple-Bundle“ vorauswählt. |
| **Skeptiker und Vertrauen** | E2 Vertrauen bzw. Scam-Angst 11 Bewertungen; 8 mit Angst vor Facebook-Käufen, z. B. T098: „i only saw the advert on facebook and wasn't sure if this would be a scam“ | Einwand-Ads behandeln Produktzweifel (168246678, 171191667), aber nie das Vertrauen in den Händler. Trustpilot erscheint im Creative nur als veraltetes Badge (182988038) und auf tb-6. | Keine Trust-Ad (UK-Kundenstimmen, Rückgabe, Lieferzeit). |
| **Nachtschweiß** | nur Männerkonten: T057, T105, T170 | Schweiß-Claims gibt es (182988114, 178749251, 185228767), aber ohne Persona | Kein Männer-Nachtschweiß-Avatar. **Wechseljahre: 0 Ads und 0 Bewertungen.** Dafür gibt es keine Evidenz als Käufersegment, das wäre ein unbelegter Test. |
| **Haustierhalter** | Katzen T067, T177 | Hund „Bella“ (200037049/045/063, seit 05.10.) | Katzen fehlen; Haustier ist ansonsten frisch besetzt. |
| **Allergiker** (umgekehrte Lücke) | nur T202 („having a quilt I can wash I no longer wake up with a bunged up nose“) | „Hypoallergenic“ in Primärtext T01 (viele Ads); Sarah bzw. Ruth S. mit Allergie (133366534, 193234224) | Die Ads bedienen ein Segment, das unter den Käufern kaum vorkommt. |
| **Jüngere Pragmatiker 25–45** (umgekehrte Lücke) | 0 Belege | Der Winner-Creator 145443331 und die Octopus-Ads zielen laut s2 auf 25–45 bzw. 35–65 | Der Winner wirkt womöglich bei Älteren, obwohl der Creator jung ist (nicht verifiziert). |

---

### 2.7 Formate, die Pleene nicht nutzt

| Format | Nutzung | Belege (IDs) | Bewertung |
|---|---|---|---|
| Native Ad bzw. Advertorial | **nur als Landingpage** | `/pages/tb-6` (8 Ads ab 01.10.; Kennzeichnung „Advertisement“). Ein Ad-Creative im Zeitungs- bzw. Artikel-Look wurde nicht gefunden. | Das Advertorial wird getestet, das Native-Creative nicht. |
| Storytelling | **teilweise, neu** | Persona-Familien 2000370xx (Bella, Spare Bed, „Mine was 12 years old“) seit 05.10.; Future Pacing in 133366534 (75,5–84,7 s „Your first night … After the first week … After a month“) | Echte Geschichte mit Wendepunkt nur in den Persona-Ads, die alle wahrscheinlich KI-Bilder nutzen. |
| Mikroskop- bzw. Milben-Visualisierung | **minimal** | Nur 133366534 = 193234275/279: Kreis-Einschub mit Mikroskopbild bei 5,4–7,3 s und 14,1–16,0 s (längliche Organismen; dass es Milben sind, ist nicht verifiziert). Staubpartikel in 200037059 (ca. 2–3 s). | Kein Makro- oder Laborbild, keine UV- oder Tupfer-Demo, keine Zahl. |
| Experten (Allergologe, Dermatologe, Schlafforscher) | **nein** | Einzige Autoritätsfigur: KI-Presenter „Heiler/Lehrer“ im Hook von 136389861 (sehr wahrscheinlich KI) | Keine echte Fachperson, kein Zertifikat, keine Studie. |
| Vorher-Nachher | **ja, als Grafik** | 180153186, 182988115 (Betten), 182988032 (gleiche Person vorher und nachher, US), 182988039, 182988042 (US), 193234214/215 („washed: never“ gegenüber „every single week“; „days... if ever“ gegenüber „2 hours“) | Kein echtes Kunden-Vorher-Nachher, kein Video-Split |
| Tochter/Mutter bzw. Geschenk für die Eltern | **fast nein** | 200490661 (US, 07.10.) „One Less Chore For Mum & Dad.“; 200490716 „Then my daughter got me…“ | Großes Potenzial vor Weihnachten (siehe 2.6) |
| Founder-Ad | **nein** | – | Nicht vorhanden. Der Betreiber ist laut Impressum One Way Ecom Limited (Hongkong). |
| Podcast bzw. Yapper (langes Reden in die Kamera) | **nein** | Am nächsten kommen Talking-Head-UGC 200490655/721 (51 s, Frau 50–60, O-Ton) und 145443331 (47 s) | Kein Podcast-Setting, kein Interview |
| Street-Interview | **nein** | – | – |
| Vergleichstest gegen Konkurrenz oder klassische Decke | **nein** | Nur Grafik-Vergleiche (182988039 „REMOVE ↓ WASH ↓ … ↓ BED“ gegenüber „WASH ↓ DRY ↓ BED“, tb-6-Vergleichstabelle). Demo 200490655/721 „But watch this.“ (Decke in den Frontlader, 22,7–29,7 s) ohne Gegenprodukt. | Kein Test „normale Decke gegen EasyRest in der Maschine“ |
| Wasch-Demo im Zeitraffer | **nein** | Gezeigt wird nur das Einlegen (185228772 22,07–24,07 s; 200490655 22,7–29,7 s; 133366534) oder die Wäscheleine (200490719, 200036996) | **Das Kernversprechen „dry in 2 hours“ wird nie mit Uhr bzw. Zeitraffer bewiesen.** |
| UGC-Unboxing | **nein** | In keiner Ad Verpackung oder Lieferung | – |
| Listicle | **ja** | 136388964 (Winner, „3 things to STOP doing…“), 136390001 (PAS-Listicle, Score 1), Checkliste 168246678 („check 3 things“, Winner); LP duvet-10r (19 Verlierer) | Als Static und Checkliste erfolgreich, als Pre-Lander gescheitert |
| Quiz | **nein** | Nur Kommentar-Aufrufe: „Which colour is going on YOUR bed? Comment 1-7 – selling out fast“ (179476350), „Which colour? Comment 1-9“ (inaktiv), „Don't scroll. Pick your colour first.“ (177443533/185228773/200490708). Kein Bedarfs- oder Größen-Quiz. | – |

---

### 2.8 Hygiene-Spezialfrage

#### 2.8.1 Überblick

- **Häufigkeit in den Ads:** Hygiene, Allergie oder Frische stecken in 59 von 137 aktiven Ads (s4). Als Inhalts-Haupt-Angle sind es 28 aktive Ads (A).
- **Häufigkeit in den Bewertungen:** Bei den Käufern erscheint Hygiene nur in 8 von 283 positiven Bewertungen (3 %). Die Wörter „hygiene“, „mites“, „bacteria“, „germs“, „dust“, „allergy“ und „sensitive skin“ kommen in 0 von 291 Trustpilot- und 0 von 172 Judge.me-Texten vor (s4).
- **Fünf Bausteine, in dieser Reihenfolge der Häufigkeit:**
  1. Ganze Decke waschbar („Wash the whole thing“)
  2. Trocknen in 2 Stunden
  3. Frische („my bed always feels fresh“)
  4. „Nie gewaschen“-Scham („Duvet: 0“)
  5. Ekel durch Milben, Schweiß, Hautpartikel und Schmutz
- **Waschtemperaturen und Bakterien** stehen ausschließlich auf den Landingpages.

#### 2.8.2 Alle Hygiene-Zitate aus Ads, nach Kategorie (wörtlich, mit ID und Sekunde)

Quellen: Abschnitte „Hygiene-Zitate“ in `wf/s2_video_batch1–9.md` und `wf/s2_static_batch1–5.md`. Gleichlautende Stellen in mehreren Ads sind zusammengefasst. VO = gesprochen, UT = Untertitel, E = Einblendung, P = Primärtext, H = Headline, B = Bildtext.

**a) Milben, Bakterien, Hautpartikel**

| Zitat | Ad-ID und Sekunde |
|---|---|
| „Sweat, dust mites, skin particles. It all builds up,“ | 133366534, 193234275, 193234279: VO und UT 13,4–16,0 s |
| Mikroskop-Kreis mit länglichen Organismen und Pfeil auf die Decke (Bild) | 133366534, 193234275, 193234279: ca. 5,4–7,3 s und 14,1–16,0 s |
| „So it stays unwashed. Sweat. Dust mites. [Emoji: Übelkeit]“ | 193234224: E ca. 0–15 s |
| „You wash the cover... but never the duvet inside.“ / „Years of sweat, dead skin & dust mites — every night.“ / „A fresher, healthier way to sleep.“ | 133366116: B (Bild, 116 Tage aktiv, Score 1) |
| „bacteria“ | **in keiner Ad**. Nur auf der US-LP: „No chance for dust mites & bacteria“ |

**b) Schmutz, Ekel, „nie gewaschen“**

| Zitat | Ad-ID und Sekunde |
|---|---|
| „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ | 133366534, 193234275, 193234279: VO und UT 0–4 s; 193234224: E ca. 0–10 s (mit [Emoji: Übelkeit]) |
| „When did you last actually wash it? Not the cover. The duvet itself.“ | 193234275/279 (= 133366534): VO 4,0–8,4 s |
| „Most people never do, because it doesn't fit in a normal washing machine.“ / „And even if it does, drying takes forever.“ | 193234275/279: VO 8,4–10,8 s und 10,8–13,4 s; dazu rotes X über der Waschmaschine |
| „while you tell yourself that swapping the cover is enough“ | 133366534, 193234275/279: VO 16,0–18,6 s |
| „Covers washed this year: 52“ → „Duvet: 0“ → „Not the cover, the duvet itself“ → „Exactly, never“ → „It never fits the machine.“ → „This one does.“ | 177443532 (ca. 0,5–15,3 s), 185228772 (0,5–15,4 s), 193234218 (ca. 1–12 s); H „Be honest. When did you last wash it?“ |
| „Quick question, when you change your bed, what actually gets washed?“ / „The sheets? Yes. The cover? Yes. The duvet? Never.“ | 200037044: VO 0–2,8 s und 2,8–5,6 s |
| „Mine hadn't been washed in years, and I'd never even thought about it.“ | 200037044 (10,9–13,6 s), 200037062 (9,84–12,58 s), 200037061 (10,4–13,2 s) |
| „How old is the duvet you slept under last night?“ / „Mine was 12 years old, and in 12 years it had never once been washed.“ plus Bild: Frau riecht an der Decke (2,04–3,96 s) | 200037061: VO 0–2,0 s und 2,0–5,1 s |
| „If a guest asked you when you last washed your duvet, not the cover, the duvet, what would you say?“ | 200037062: VO 0–4,54 s |
| „For years, the spare duvet lived in the cupboard between visits and never once got washed.“ plus Bild: Staubpartikel über der alten Decke (ca. 2–3 s) | 200037059: VO 0–4,4 s |
| „I'd wash the cover and hope for the best. Not anymore.“ | 200037059: VO 5,2–9,04 s |
| „If your dog sleeps on your bed, when did you last wash the duvet?“ / „Not the cover, the duvet.“ | 200037045: VO 0–4,4 s und 4,4–7,2 s |
| „and with a dog on the bed every night that started to bother me.“ | 200037045 (21,04–24,08 s), 200037049 (22,32–24,1 s), 200037063 (22,56–25,68 s) |
| „Dog hair, muddy paw prints, biscuit crumbs from the grandchildren, the whole lot just goes in the wash…“ plus Pfotenabdrücke im Bild | 200037045 (43,12–50,84 s; Bild ca. 42,4–46,1 s), 200037049 (ca. 43–50,8 s; Bild 42,8–46,5 s), 200037063 (44,72–52,4 s; Bild 44,27–47,93 s) |
| „Wet November walk, two muddy paws, straight onto the bed.“ | 200037063: VO 0–4,08 s; Bild Pfotenabdrücke 4,13–8,73 s |
| „Be honest — how old is the duvet you're sleeping under?“ / „washed: never“ / „washed: every single week“ | 193234214: B |
| „You shower every night — then sleep under a duvet that's never been washed. Not because you're lazy: normal duvets don't fit normal machines. Ours does.“ | 193234224: P |
| „Susan, 62: „Was skeptical about the hygiene at first, but here everything gets clean in one wash. Climbing into a fresh clean duvet straight from the shower — absolutely amazing[Emoji]““ | 185395501 (US): E 6,0–9,0 s |
| „Shaking out dusty bedding“ (als Don't) | 136388964: B |

**c) Schweiß**

| Zitat | Ad-ID und Sekunde |
|---|---|
| „No more sweating in summer. No more freezing in winter.“ | 133366534, 193234275/279: VO und UT 54,9–57,6 s |
| „So you're warm all night, and you don't wake up sweating at 3 AM with the heating on.“ | 178749251 (13,68–17,12 s), 178749254 (13,76–17,36 s), 178749247 (13,08–16,74 s) |
| „10.5 TOG · warm, never sweaty“ | 185228767 und 193234216: E 0–3,0 s |
| „✓ No sweating. No freezing.“ | 185395501 (US): E 3,0–6,0 s |
| „No sweating in summer [Emoji] No freezing in winter [Emoji]“ | 193234224: E ca. 19–38 s |
| „NEVER SWEAT AT NIGHT AGAIN“ / „ICE DUVET, NOT A SWEAT DUVET“ | 182988114: B |
| „Change the bed in the summer heat“ / „End up hot and sweaty“ / „Now you need another shower“ | 136390001: B |
| „End up too hot and uncomfortable to drift off.“ (dazu Frau mit Schweißtropfen) | 136388847 (Winner), 200490706: B |
| „CoolRest™ Cooling Duvet“ … „Sweat-free nights“ / „Traps heat and moisture“ | 174599778 (Winner): B |
| „and the breathable fibres mean it never feels stuffy on you.“ (schweißnah) | 184134597 (31,12–34,6 s), 184134616 (32,24–35,72 s), 184134607 (31,12–34,72 s), 200037044 (34,2–36,6 s), 200037052 (52,4–55,92 s), 200037047 (53,68–56,76 s), 200037049 (50,8–62,8 s), 200037045 (50,84–59,72 s), 200037063 (56,4–61,2 s), 200037061 (33,8–36,2 s), 200037059 (52,32–56,4 s) |

**d) Allergie**

| Zitat | Ad-ID und Sekunde |
|---|---|
| „One duvet, all year round. Hypoallergenic.“ | 133366534, 193234275/279: VO und UT 57,6–59,8 s |
| „And Sarah. Washing her whole duvet has become a weekly routine. Especially because of her allergies.“ plus Review-Karte „I'm allergic to dust and pollen, so being able to wash the entire duvet, not just the cover, is exactly what I needed. Sarah — Verified buyer“ | 133366534, 193234275/279: VO 70,8–75,5 s; Karte 72,1–75,7 s |
| „Ruth S. now washes hers every week — because of her allergies“ | 193234224: E ca. 28–47 s (dieselbe Geschichte mit **anderem Namen** als „Sarah“) |
| „✓ Hypoallergenic and kind to sensitive skin“ | P (T01-Familie), in genau 20 aktiven Ads: 136388964, 136388847, 136389861, 133366534, 151025063, 171191667, 174599778, 180153186, 182988073/108/111/114/115, 193234214/215/279, 136390001, 133366116, 200490706, 200490716 |

**e) Waschen und Maschinengröße**

| Zitat | Ad-ID und Sekunde |
|---|---|
| „Just put it in the washing machine and then in the tumble dryer.“ | 136389861 (16–19 s), 145443331 (12,56–15,12 s), 145443318 (14,96–17,82 s), 151025063 (8,32–11,44 s), 163921089, 193234221 (12,56–15,12 s), 193234219 (12,24–14,8 s) |
| „It fits in any normal household washing machine.“ plus Badge „[Emoji: Häkchen] Fits any washing machine“ | 133366534, 193234275/279: VO 39,8–42,1 s; Badge 40–42 s |
| „The entire duvet. Everything gets washed out.“ | 133366534, 193234275/279: VO 42,1–44,8 s |
| „When it needs washing, the whole thing goes into your normal 7kg washing machine, then“ | 184134597 (17,6–22,48 s), 184134616 (18,72–23,6 s), 184134607 (17,56–25,84 s) |
| „The double goes straight into my normal 7kg washing machine,“ | 200037044 (21,9–24,6 s), 200037052 (34,32–37,52 s), 200037047 (34,52–40,48 s), 200037049 (ca. 32–43 s), 200037045 (33,56–43,12 s), 200037063 (37,68–41,76 s), 200037062 (20,9–25,74 s), 200037061 (21,5–24,2 s), 200037059 (28,88–37,52 s) |
| „STILL FITS A NORMAL WASHING MACHINE.“ | 200037058 (7,5–9,77 s), 200037053 (7,13–9,53 s), 200037051 (7,63–10,03 s) |
| „Fits in any washing machine.“ | 177443533, 185228773, 200490708: E 4,97–7,63 s |
| „Washes whole, fits any Washing machine, dry in 2 hours“ | 185228767, 193234216: E 6,4–10,2 s |
| „1. Does the WHOLE thing fit a normal washing machine?“ → „Ours does.“ | 168246678, 168246686, 185228764, 200490712: E 3,7–9,87 s |
| „The duvet with no cover / Wash the whole thing“ | 139561428/410/491, 185228755, 200490701: E 3,0–7,0 s |
| „Now I know exactly what you're thinking, that thing is never going to fit in a normal washing machine.“ → „But watch this.“ (Demo im Frontlader) | 200490655 und 200490721: VO 14,72–20,34 s und 20,74–22,74 s; Bild bis 29,7 s |
| „And it's not a heavy duvet, it still fits easily into a normal washing machine.“ | 178749251 (23,54–27,8 s), 178749254, 178749247 |
| „“But you'd need a huge washing machine for that” [Emoji: Lachen]“ / „The duvet is made extra light“ / „fits in any normal household machine“ / „Toss it in. Done.“ | 171191667 (Winner): B |
| „WASH THE WHOLE THING. RIGHT AT HOME.“ / „Fits Standard Home Washers“ | 182988043 (US), 200490725: B |
| „Your Comforter Shouldn't Need A Field Trip.“ / „Fully Machine Washable“ | 182988040 (US): B |
| „No Launderette Needed. Ever.“ / „Washed by lunchtime.“ | 178749258: H und B |

**f) Trocknen (drei unvereinbare Fassungen)**

| Fassung | Zitat | Ad-ID und Sekunde |
|---|---|---|
| **mit** Trockner | „the tumble dryer, and it's dry in two hours.“ | 184134597 (22,48–25,92 s), 184134616 (23,6–27,04 s), 184134607 (21,32–25,84 s), 200037044 (24,6–26,8 s), 200037052 (37,52–40,24 s), 200037047, 200037049, 200037045, 200037063 (41,76–44,72 s), 200037062, 200037061 (24,2–26,3 s), 200037059 (37,52–42,48 s) |
| **mit** Trockner, ohne Zeit | „goes straight in the machine and then the tumble dryer. That's it.“ | 200490716: VO 19,6–24,64 s |
| **ohne** Trockner | „And it's dry in two hours. Even without a dryer.“ plus Badge „[Emoji: Häkchen] Quick-drying“ | 133366534, 193234275/279: VO 44,8–47,2 s |
| **ohne** Trockner | „2. Is it dry in 2 hours without a tumble dryer?“ → „2 hours. No dryer.“ | 168246678, 168246686, 185228764, 200490712: E 9,87–16,1 s |
| **ohne** Trockner | „dries in 2 hours even without a dryer“ | 171191667: B |
| **ohne** Trockner | „✓ Dry in 2 hours, no tumble dryer“ | 173929415: P |
| **Luft** | „and then I just air dry it for 2 hours“ | 200490718 und 200490660: E 11,44–14,0 s |
| **Luft** (Bild) | „Two hours later, it's dry“ plus Wäscheleine | 200490719 (9,58–13,58 s), 200036996 (9,78–13,0 s) |
| **Luft** | „Air Dries in 2 Hours“ / „AIR DRIES IN 2 HOURS“ / „✓ Rapid 2-Hour Air Dry“ | 182988040, 182988024, 186893859 (US), 189550269 (GB): B |
| offen | „Dry in 2 hours / Back on the bed“ | 139561428/410/491, 185228755, 200490701: E 7,0–10,8 s |
| offen | „Dry again in two hours.“ | 178749251 (27,8–29,08 s), 178749254 (27,92–29,4 s) |
| offen, mit Einschränkung | „WASHES WHOLE. DRY AGAIN IN ABOUT 2 HOURS.“ | 200037058 (9,77–12,0 s), 200037053 (9,53–11,77 s), 200037051 (10,03–12,27 s) |
| offen | „And no, it doesn't take ages to dry, just two hours and then you can put it back onto your bed.“ | 200490655 und 200490721: VO 30,74–37,14 s |
| offen | „Dry in 2 hours“ | 177443532, 185228772 (24,07–25,4 s), 193234218 |
| offen | „Dries in 2 hours.“ | 177443533, 185228773, 200490708: E 7,63–ca. 11,5 s |
| Routine | „In the machine in the morning. Fresh on the bed by evening.“ / „After the first week, wash day done in two hours.“ | 133366534, 193234275/279: VO 47,2–49,9 s und 79,9–84,7 s |
| Routine | „So the morning after guests leave, the whole duvet is washed, dried, and back on the bed before lunch.“ | 200037052 (40,24–45,36 s), 200037047 (40,48–45,6 s), 200037059 (42,48–47,28 s) |

**g) Wasch-Temperatur:** In **keiner Ad** wird eine Wasch-Temperatur (°C oder °F) genannt.

**h) Körpertemperatur (Hygiene-nah):**

- „It's 10.5 tog, so it's every bit as warm as a winter duvet, just without the weight,“: 184134597 (25,92–31,12 s) und alle Gen-2-Videos.
- „the breathable fibres adapt to your body/temperature. Nice and warm in winter, … cool in summer“: alle Gen-1-Videos.
- „Climate-regulating fibres balance your temperature automatically“: 193234224, E ca. 15,5–35 s.

**i) Frische:**

- „I swear to you, my bed always feels fresh.“: 136389861 (24–26 s), 145443331 (25,2–27,8 s), 145443318 (28–30 s), 151025063 (14,64–17,76 s), 184134597 (34,6–37,96 s), 200037044 (36,6–38,6 s), 200037052 (58,4–60,96 s) und weitere Gen-2-Videos.
- „I haven't changed my bed linen in three months and it's never felt fresher.“: 145443331, 163921089, 193234221, jeweils 0–3,76 s.
- „Your first night. You feel lighter, fresher, different.“: 133366534, 75,5–79,9 s.

#### 2.8.3 Hygiene auf den Landingpages (aus s3)

| Seite | Zitat (wörtlich) |
|---|---|
| `/products/easyrest` (GB) Section 7 | „**Washable like bed linen**“ / „The Pleene EasyRest™ fits in any normal washing machine.“ / „Winter bedding usually goes months without a proper wash, because the duvet itself never goes in. Only the cover does.“ / „With Pleene EasyRest™, everything goes in. One wash. All clean.“ / „Air dries in 2 hours — or even faster in the dryer.“ |
| `/products/easyrest` FAQ | „We recommend washing it at 40°C on a spin cycle of around 800 rpm. / Pleene™ is designed to absorb far less sweat and dirt than traditional bedding, so 40°C is perfectly sufficient for everyday washing … / If you ever want a deeper clean, you can occasionally wash it at 60°C. … Air-dried, it is usually completely dry in about 2 hours.“ |
| `/products/easyrest` FAQ 5 | „Why is the Pleene EasyRest™ more hygienic than a normal duvet?“ — „… usually only the cover is washed while the duvet itself is rarely cleaned, so over time sweat, dust and allergens can build up. With Pleene EasyRest™, your bed stays regularly fresh and hygienically clean.“ |
| `/products/easyrest` FAQ 7 | „Is it suitable for allergy sufferers?“ — „Yes. Because you can wash the whole duvet regularly and it contains no feathers or down, it is well suited to allergy sufferers. Regular washing helps keep dust and allergens to a minimum.“ |
| `/products/easyrest` Galerie-Testimonial | „Susan, 62: „I'm always the cold one in our house, but under some duvets I'd still wake up boiling at 3am. With this one, neither happens. Not cold, not sweating.““ |
| `/products/easyrest` Produkt-JSON (nicht angezeigt) | „Breathable and temperature regulating, so no sweating even in summer“, „Care: machine washable, quick-drying“ |
| `/products/easyrest-comforter` (US) Galerie | „Comforter + cover in one. Completely washable.“ mit „Air dries in about 2 hours“, „**No chance for dust mites & bacteria**“, „Fits any washing machine“; „No sweating. No freezing.“ |
| `/products/easyrest-comforter` Testimonials | „Robert, 61: „… I don't sweat at night anymore. In summer I wake up dry — that used to be unthinkable.““; „James, 55: „… I sweat a lot less at night now, too.““ |
| `/products/easyrest-comforter` FAQ | „washing it on a warm cycle (around 105°F)“ … „occasionally wash it on a hot cycle (around 140°F)“ … „Air-dried, it's usually completely dry in about 2 hours.“ |
| `/pages/tb-6` | Checks „Whole duvet machine-washable at 40°“, „Air-dries in 2–3 hours“; ATF „Dry in about 2 hours“; Tabelle „Drying time \| 2–3 hours \| Often overnight“, „Hygiene \| Whole duvet washable \| Duvet rarely washed“; FAQ „Around 2 hours in the air, faster in a tumble dryer.“, „With ordinary bedding only the cover gets washed. With the EasyRest the whole duvet goes in the wash every time, so you can clean it as often as normal bed linen.“, „… wick moisture away … without feeling clammy.“ |
| `/pages/tb-6` Disclaimer | „Drying times depend on room temperature, airflow and spin speed.“ / „Health: The EasyRest™ is a bedding product, not a medical device. Statements about allergies and sleep are general information and do not replace medical advice.“ |
| Home-Page | „NO DUVET COVER · WASHES AT 40°C · TUMBLE-DRYER SAFE“; „40°C, normal cycle / Wash the duvet on its own with a mild detergent. …“, „Tumble-dry on low, ideally with dryer balls to keep the fill even.“ |

#### 2.8.4 Bewertung: Zahlen, Bilder, Behauptungen

| Behauptung | Wo | Beleg | Stärke als Werbeargument | Belegt? |
|---|---|---|---|---|
| „dirtiest thing in your bedroom“ | 133366534, 193234275/279, 193234224 | keiner; durch „probably“ abgeschwächt | **hoch** (einziger Ekel-Winner, Score 100) | nein, rhetorisch |
| „Sweat, dust mites, skin particles. It all builds up“ / „Years of sweat, dead skin & dust mites — every night.“ | 133366534, 193234275/279, 133366116, 193234224 | keine Zahl, keine Quelle; Mikroskopbild unklarer Herkunft | mittel. Das Bild bleibt vage; die Static 133366116 läuft 116 Tage mit Score 1 | nein |
| „No chance for dust mites & bacteria“ | nur US-LP | keiner | absolut formuliert | **nein**. Für einen objektiven Claim fehlt jeder Beleg; regulatorisch riskant (Einschätzung) |
| „Hypoallergenic and kind to sensitive skin“ / „Hypoallergenic.“ | Primärtext T01 (viele Ads), 133366534 VO 57,6–59,8 s | kein Zertifikat, keine Prüfung genannt; tb-6-Disclaimer relativiert („not a medical device“) | gering. Keine Bewertung bestätigt es | nein |
| Allergie-Testimonial „Sarah“ bzw. „Ruth S.“ | 133366534/193234275/279 bzw. 193234224 | Review-Karte „Verified buyer“; s3 findet die Testimonials der Seiten in keiner Bewertung; gleiche Geschichte mit zwei Namen | mittel | **nicht verifiziert**, widersprüchlich |
| „Covers washed this year: 52“ / „Duvet: 0“ | 177443532, 185228772, 193234218 | fiktive Rechnung | mittel (Scham-Mechanik); alle Fassungen Score 1 | nicht nötig (rhetorisch) |
| „Mine was 12 years old … never once been washed“ | 200037061 | Persona-Aussage | hoch als Hook; noch kein Ergebnis | Persona, nicht verifiziert |
| „dry in 2 hours“ | fast alle Ads | Reviews: T140 „in 2hrs“, J011 „dry in about 2 hours“; dagegen T019 „about 4hours“, T262 „within 1 day“. tb-6: „2–3 hours“ plus Disclaimer | **sehr hoch** (Standardbaustein jeder Winner-Familie) | **teilweise**. Drei unvereinbare Fassungen (mit Trockner, ohne Trockner, an der Luft); die eigene Seite schränkt ein |
| „fits any normal washing machine“ | 133366534, 177443533, 185228767, 171191667 u. a. | Größentabelle der eigenen PDP: „Fits a drum from 6–8 kg“; Gen 2 sagt „7kg“; Review Rona Dixon im Original: „although it is a tight fit in my washing machine“ (auf tb-6 herausgekürzt) | hoch | **eingeschränkt**. „any“ ist durch die eigene Tabelle widerlegt |
| „10.5 tog, every bit as warm as a winter duvet“ | Gen 2, 184134598, 185228767 | PDP „10.5 TOG — proper winter warmth“; Home-Page „mid-weight, all-season“; 14 Käufer schreiben, den Winter noch nicht getestet zu haben (s4) | hoch (Zahl, konkret) | Tog-Wert nicht unabhängig verifiziert; Home-Page widerspricht |
| „absorb far less sweat and dirt than traditional bedding“ | LP-FAQ GB und US | keiner | gering (nur FAQ) | nein |
| 40 °C bzw. 60 °C (US 105 °F bzw. 140 °F) | nur LP | Pflegehinweis | gering. Bei Milben-Argumentation wäre 60 °C das stärkste Argument, wird aber in keiner Ad genutzt | Herstellerangabe |
| „Over 10,000 sleepers“ / „96% never want to go back after their 90 night trial“ | 133366534, 193234275/279, 193234224 | tb-6 nennt „7,000+“; Trustpilot 291 Bewertungen | mittel | **widersprüchlich**, nicht verifiziert |

**Gesamturteil:**

1. **Die Hygiene-Argumentation ist emotional stark, sachlich schwach.** Es gibt keine einzige Messzahl (Milbenzahl, Keimreduktion, Laborbefund), keinen Experten, kein Zertifikat und keine Vorher-Nachher-Probe.
2. **Die stärksten Bilder sind Scham-Situationen:** Gast fragt, Hund im Bett, 12 Jahre alte Decke, „Duvet: 0“. Das einzige Ekel-Bild ist der vage Mikroskop-Kreis.
3. **Die belastbarste Zahl ist „2 hours“.** Gerade sie ist intern widersprüchlich und wird nie bewiesen.
4. **Hygiene ist bei Pleene ein Werbe-Thema, kein Käufer-Thema.** Käufer erleben das Produkt als Bequemlichkeits- bzw. Kraftlösung (s4).
5. **Ansatzpunkte für einen Wettbewerber (Einschätzung):**
   - belegte Hygiene-Claims (60 °C waschbar mit Nachweis, Prüfsiegel, Allergologe)
   - eine echte Zeitraffer-Waschdemo mit Uhr
   - eine konsistente Trocknungsangabe

#### 2.8.5 Performance von Hygiene-Ads

- **Winner mit A-Inhalt: 2.** 133366534 (Ekel-Kompilation, 67 Tage, Score 100) und 171191667 (Waschmaschinen-Einwand, 36 Tage, Score 100).
- **Inaktive A-Textfamilien:** maximal 27 Tage. Bis heute aufgegeben: 45 Ads mit „Be honest. When did you last wash it?“, 19 mit „The Duvet You Can Actually Wash“, 12 mit „The Duvet That Goes In The Wash“ und die gesamte A-Welle vom 25.09.
- **Aktive A-Ads mit Score ≥ 41:** 8 von 28. Darunter die Kopien 193234275 (52), 193234279 (44) und die KI-Statics 193234214/215 (52). Die neue Persona-Welle liegt laut Live-Abfrage bei 22–44.

---

### 2.9 Kongruenz Ad → Seite und Funnel-Muster (aus s3, ergänzt um s2)

**Funnel-Muster:**

| Weg | Ads (aktiv) | Muster |
|---|---|---|
| Ad → GB-PDP `/products/easyrest` | 83 (alle 20 Winner) | Direktverkauf. Die PDP führt mit B („10.5 TOG — proper winter warmth“), Gratis-Kissenbezüge „(Value: £39.99)“ im ATF, Kaching-Bundles (2 Stück −10 % vorausgewählt) |
| Ad → Winter-Klon `/products/easyrest-duvet` | 6 | B auf B: Tog-Ads auf eine Tog-Seite (versteckter Produktklon, Vorlage „winter26“) |
| Ad → Advertorial `/pages/tb-6` → PDP | 8 (ab 01.10.) | Pre-Lander für C und Social Proof („How 7,000+ people said goodbye to putting duvet covers on“). Alle CTAs führen auf `/products/easyrest` |
| Ad → US-PDP `/products/easyrest-comforter` | 40 (US) | eigener US-Funnel mit USD-Preisen und „comforter“-Wortlaut |
| Warenkorb | – | Gratisversand ab £100; Upsells Pillow-Cases £19.99, Pillow £39.99, FluffBalls £14.99, Package Protection £2.99; auf /cart „180-Day Return Policy – Upgrade“ für £2.99 |

**Brüche zwischen Ad und Seite (mit IDs):**

1. **Angle-Bruch:** Die PDP führt mit B (Tog), die meisten GB-Ads mit C, A oder Knappheit. Nur die Tog-Ads (178749xxx, 2000370xx-Shorts) passen zum Seiteneinstieg.
2. **Knappheit ohne Entsprechung:**
   - „Only 17 left in Hearth Red“ (139561428), „Only 26 left in Mint Green“ (139561410, 169082912, 185228755, 200490701), „Only 19 left“ (139561491, 151025052).
   - Die Seite zeigt nur den statischen Text „Ready to Ship – Limited Stock“ für jede Farbe und Größe und hat keinen Countdown. Hearth Red ist normal wählbar.
   - Die Restmenge für Mint Green ist in den Ads selbst widersprüchlich: 26 (139561410), 79 (173307160), 12 (184134598).
3. **Farbtext passt nicht zum Bild:** Die Hearth-Red-Copy läuft auf schwarzen bzw. blauen Decken (177443532, 185228772, 193234218, 193234216, 185228767). Die Lavender-Copy läuft ohne Lavender im Bild (193234278, 200490698).
4. **Angebotsbrüche:**
   - „30% off“ (ab 178749258, Gen-2-Skripte) gegen „SAVE 23–35 %“ je nach Größe auf der PDP.
   - „This week only“ gegen „Autumn offer … while stocks last“ auf tb-6.
   - „Value £49.99“ auf der Endkarte von 200490716 gegen „worth £39.99“ überall sonst.
   - Gratis-Kissenbezüge: Die Kaching-Konfiguration hat `freeGifts: []`, im Warenkorb erscheint keine Position. Ob sie geliefert werden, ist nicht verifiziert.
5. **Garantie:** „90 nights to try it risk-free“ bzw. „90-Night Free Trial. Money back, no questions asked.“ gegen die Policy: Rücksendekosten trägt der Kunde, Versand wird nicht erstattet. In den Reviews klagen T055 und T119 über teure Rücksendung nach China.
6. **Produktname:** Winner 174599778 zeigt „CoolRest™ Cooling Duvet“, ein anderes Pleene-Produkt, und verlinkt auf die EasyRest-PDP.
7. **Hygiene-Hooks auf tb-6:** 193234218 („Be honest. When did you last wash it?“) und 193234224 laufen auf tb-6. Dort kommt Hygiene nur in Tabelle und FAQ vor. s3 bewertet das als **schwach**.
8. **US-Wortlaut auf der GB-PDP:** 200490723–726, 709, 720 und 725 tragen „comforter“-Copy aus der US-Serie, verlinken aber auf `/products/easyrest` (GB).
9. **Testimonials:**
   - Louise ★5 „Verified“ (182988027, 190288311) gegen die Original-Bewertung T166 mit 4★, nicht verifiziert.
   - „Margaret, 67“ (PDP, auch 186893873) ist in keiner Bewertung auffindbar.
   - 182988038 zeigt ein veraltetes Trustpilot-Badge (4.7/193).
   - Rona Dixons Bewertung ist auf tb-6 um den Nachteil „tight fit“ gekürzt.
10. **Kundenzahlen:** „Over 10,000“ (Ads, PDP) gegen „7,000+“ (tb-6).

**Gut kongruent (laut s3):**

- Tog-Ads auf easyrest-duvet (178749251, 179476350: „sehr stark kongruent“).
- Testimonial-Ads auf tb-6 (193234221: „stark kongruent“).
- Checkliste auf PDP (168246678: kongruent in allen drei Punkten).
- Wasch-Ads auf der US-Seite (182988043: „stark kongruent“).

---

### 2.10 Wichtige Datenlücken und Unsicherheiten

1. **Keine Spend-, Reichweiten- oder Conversion-Daten für GB.** „Winner“ beruht auf Laufzeit und GetHooked-Score. Ein Score von 100 kann auch bei kleinem Budget entstehen (nicht verifiziert). Score-Werte inaktiver Ads fehlen (null), Verlierer lassen sich nur über die Laufzeit erkennen.
2. **Inventar-Stand gegenüber Live:**
   - s3 meldet laut `search_ads` am 08.10. bereits 153 aktive Ads, darunter 20 neue vom 07.10. (13 GB, 7 US). Im Inventar steht nur eine Ad vom 07.10. **Rund 19 der neuesten Ads sind hier nicht analysiert.**
   - Die Live-Abfragen in s2 zeigen weitere Abschaltungen am 07.10. und geänderte Scores.
3. **Inhalt der inaktiven Ads:** Die 555 inaktiven Ads wurden nicht angesehen. Familien- und Angle-Aussagen zu ihnen stützen sich auf Headline und Primärtext. Beispiel: Die Headline T02 sitzt auch auf Nicht-Hygiene-Videos.
4. **KI-Einstufung:** Die KI-Anteile beruhen auf Sichtprüfung und teils C2PA- bzw. Metadaten (hf-job-id, Google, OpenAI). Ohne Metadaten ist die Einstufung eine Einschätzung.
5. **Sprecher-Geschlecht und -Alter:** geschätzt über Tonhöhe (f0) und Bild, nicht verifiziert.
6. **Echtheit von Testimonials und Kommentaren:** Die eingeblendeten Kommentare (Janet Whitfield, Moira McAllister, Susan Hargreaves in 178749xxx), die Review-Karten (George, Sarah, Ruth S., Peter R.) und die Seiten-Testimonials sind nicht verifiziert; mehrere sind in keiner Bewertung auffindbar.
7. **Angle-Zuordnung:** Der Inhalts-Angle ist eine manuelle Einordnung der Hauptbotschaft. Viele Ads verbinden 3–5 Angles. Bei Batch 2 und 9 der Videos wurde der Angle aus dem Fließtext übernommen, weil die Kurz-Tabelle maschinell nicht lesbar war.
8. **Re-Upload-Erkennung:** Datei- bzw. md5-Gleichheit ist nur für die in s2 angesehenen aktiven Ads geprüft. Beziehungen zu inaktiven Ads (z. B. Lavender ab 05.09.) sind nicht verifiziert.
9. **US-Anteil:** 40 aktive Ads gehören zum US-Funnel. In die Winner-Analyse geht keine ein: Keiner der 20 Winner ist laut GetHooked US und keiner verlinkt auf `/products/easyrest-comforter`. Von den 20 Winnern sind 13 laut GetHooked GB, 7 ohne Länderangabe (151025063, 171191667, 172760571, 151025052, 169082912, 173307160, 174599778); GB für diese 7 nicht verifiziert (Indiz: GB-PDP `/products/easyrest`; „£39.99“ in Text oder Bild bei 4 der 7, „Customer, UK“ bei 1, bei 151025052 und 169082912 nur die PDP). Die Angle-Durchschnitte sind deshalb zusätzlich für GB ausgewiesen.
10. **Reviews:** Geschlecht über Vornamen geschätzt; Judge.me zu 154 von 172 Kopien von Trustpilot. Der Anhang A1–A3 mit wörtlichen Reviews in s4 wurde für diesen Teil nicht erneut gelesen. Die Review-Zitate stammen aus dem Hauptteil von s4.
11. **Trocknungszeiten, Tog-Wert und Maschinengröße** sind Herstellerangaben. Eine unabhängige Messung liegt nicht vor.

---

### Anhang zu Teil 2: Links zu zentralen Nicht-Winner-Ads

| ID | Rolle | Ad Library | GetHooked |
|---|---|---|---|
| 178749258 | erste Ad mit „30% off“, Starker Kandidat | [AL](https://www.facebook.com/ads/library/?id=1750276626195989) | [GH](https://app.gethookd.ai/share/ad/178749258?signature=26142585e8a79bd682cbb72cd7ae73d46e39dc00bb8ff65b79f19d32e5e4e2cb) |
| 178749251 | Winter-Kommentar-Hook (V9) | [AL](https://www.facebook.com/ads/library/?id=1792003651846452) | [GH](https://app.gethookd.ai/share/ad/178749251?signature=f7a95b97af4df738359f0bc0b4a21bbd6f5508efef5391e097423762a823afc1) |
| 182988073 | Farb-Reveal (V6), Starker Kandidat | [AL](https://www.facebook.com/ads/library/?id=1307634398016532) | [GH](https://app.gethookd.ai/share/ad/182988073?signature=18244261546a933ac17b6d832e4abb5f9491a76500ae006902ed5c113947df05) |
| 184134597 | Gen-2-Skript, Octopus-Test (V13) | [AL](https://www.facebook.com/ads/library/?id=4249373995353335) | [GH](https://app.gethookd.ai/share/ad/184134597?signature=2b680d992f53e9489bd001330a9e608908df3f009b371ab2cf0e14275970f411) |
| 185228767 | Tog-Neuschnitt des KI-Templates | [AL](https://www.facebook.com/ads/library/?id=947904747867427) | [GH](https://app.gethookd.ai/share/ad/185228767?signature=d4a01baf409b9ddc41f60bfabb36d11b1b0037cf0db9af90a7ff2251278f24be) |
| 177443532 | Cue-Cards „Duvet: 0“ (V8) | [AL](https://www.facebook.com/ads/library/?id=2894384197604810) | [GH](https://app.gethookd.ai/share/ad/177443532?signature=0e0c69630ceb34cd905e1db339879cccd638942624cbd67020f4cfb3c8937ccb) |
| 193234275 | Kopie der Hygiene-Kompilation (easyrest) | [AL](https://www.facebook.com/ads/library/?id=931889339640196) | [GH](https://app.gethookd.ai/share/ad/193234275?signature=ffce5170bcd8108ccef8ec8fa356ebe88ee4788757813cf94c27b340e5ff2e63) |
| 193234279 | Kopie der Hygiene-Kompilation (tb-6) | [AL](https://www.facebook.com/ads/library/?id=28476177958733795) | [GH](https://app.gethookd.ai/share/ad/193234279?signature=13f6122c0c5d22eb8c8b6141c88c013e8051538391bd99bbd1f57e3f4702f207) |
| 193234224 | Text-Schnitt mit „Dust mites“ (tb-6) | [AL](https://www.facebook.com/ads/library/?id=1614086653522933) | [GH](https://app.gethookd.ai/share/ad/193234224?signature=e67f0112dff4be83367fd2663a38a3c667a76a33044371dae7cb5e0307b1035b) |
| 193234221 | Creator-Winner-Kopie auf tb-6 | [AL](https://www.facebook.com/ads/library/?id=2325762131511604) | [GH](https://app.gethookd.ai/share/ad/193234221?signature=34d449a91191d816e5a91f7d690e2d93f52044d2af092704c3b3dece336abb59) |
| 193234214 | KI-Static „washed: never“ (tb-6) | [AL](https://www.facebook.com/ads/library/?id=2366124124211597) | [GH](https://app.gethookd.ai/share/ad/193234214?signature=4c554cee5f2b53ee0a1c202d4fe10ee2f6cfb8b5f6e3a6b4936aab8a10f4eec3) |
| 133366116 | Static „sweat, dead skin & dust mites“ (116 T., Score 1) | [AL](https://www.facebook.com/ads/library/?id=1687513282572901) | [GH](https://app.gethookd.ai/share/ad/133366116?signature=a2afe366ec4a13b6ab93d2e4edce9c7275c8292acd57172af7d5455a8b4dc87d) |
| 182988114 | „ICE DUVET, NOT A SWEAT DUVET“ | [AL](https://www.facebook.com/ads/library/?id=1426446732803436) | [GH](https://app.gethookd.ai/share/ad/182988114?signature=45373dfa7ccdf466516a711b6593e9207307858450c4d58f1857ebd0d9c95216) |
| 200037044 | Persona-Hygiene „Quick question…“ (V11) | [AL](https://www.facebook.com/ads/library/?id=2217517888813082) | [GH](https://app.gethookd.ai/share/ad/200037044?signature=a19c242b496cbc5e92ce74a3a3303e782e4f5f6f23b854194823c49f93fb0260) |
| 200037045 | Persona Hund „If your dog sleeps on your bed…“ | [AL](https://www.facebook.com/ads/library/?id=1251620417158236) | [GH](https://app.gethookd.ai/share/ad/200037045?signature=9dbc6af8a2932afed3e5a991ab6f9ad12e1fef2910914283018eeff2b95baea8) |
| 200037052 | Persona Gästebett „I'm 71“ | [AL](https://www.facebook.com/ads/library/?id=961172106430872) | [GH](https://app.gethookd.ai/share/ad/200037052?signature=ab0ea3d22bfd746992e616204067846b3fc4ad0b9794701144978049c326996a) |
| 200490716 | KI-Seniorin „at my age“, „Value £49.99“ | [AL](https://www.facebook.com/ads/library/?id=2233952628001235) | [GH](https://app.gethookd.ai/share/ad/200490716?signature=f9af223b680c0ee04bd5687c44ba0fd8ca69eace21b5373ed6b6f893022689ff) |
| 200490655 | UGC-Waschdemo „But watch this.“ (US) | [AL](https://www.facebook.com/ads/library/?id=4392590044384955) | [GH](https://app.gethookd.ai/share/ad/200490655?signature=7d24527061b5c2c8f21d9243b2a93c078b438788a757590a49fc3e5bc7294145) |
| 200490718 | Selbstständigkeit „I used to need help with this.“ (GB) | [AL](https://www.facebook.com/ads/library/?id=969394622234742) | [GH](https://app.gethookd.ai/share/ad/200490718?signature=38b5623f18087b0df4c2c1716eb5005dc8644f32545bafb73badcec66bf77774) |
| 200490661 | einzige Geschenk-Ad „One Less Chore For Mum & Dad.“ (US) | [AL](https://www.facebook.com/ads/library/?id=2272066053740371) | [GH](https://app.gethookd.ai/share/ad/200490661?signature=114722e2aec9d0a68a974913b4cf9f5a2ba74b9f5bf1d0b762ad013438a493dc) |
| 185395501 | US-Diashow mit Hygiene-Testimonial „Susan, 62“ | [AL](https://www.facebook.com/ads/library/?id=4386478151596961) | [GH](https://app.gethookd.ai/share/ad/185395501?signature=015f1978dac5f9d276bb167b0564e2fe687605d8c9ad005f1b15479977650936) |
| 182988043 | US-Wasch-Static „Wash The Whole Comforter“ | [AL](https://www.facebook.com/ads/library/?id=29208178135432493) | [GH](https://app.gethookd.ai/share/ad/182988043?signature=474ac523034272536a305779503c22ea294092cc8bd3cc7b069288c8fe337071) |

Eigene Skripte zu diesem Teil: `wf/s5_scripts/` (parse_kurz.py, weekly.py, inact14.py, angles.py, losers.py; Ergebnisse kurz.json und content_angle.json).

---

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

---

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

> Die Bewertungen wörtlich (alle 1–3★ von Trustpilot, Judge.me 1–3★, die 30 aussagekräftigsten 4–5★): siehe [A4 – Bewertungen wörtlich](#a4--bewertungen-wörtlich).

---

## Für Chrome / Ad-Library-Check

**Ranking:** days_active × max(used_count, 1) × max(performance_score, 1) über alle 692 Ads. Werte aus dem Inventar vom 08.10. (ca. 10:30 UTC). Die TOP 20 sind identisch mit den 20 Winnern. Inaktive Ads haben bei GetHooked keinen Score und landen deshalb nicht in der Liste. Laut GetHooked laufen alle 20 auf facebook, instagram, audience_network, messenger und threads, Landingpage `pleene.com/products/easyrest`. Zielland: 13 laut GetHooked GB, 7 ohne Länderangabe (151025063, 171191667, 172760571, 151025052, 169082912, 173307160, 174599778); GB für diese 7 nicht verifiziert (Indiz: GB-PDP `/products/easyrest`, auf die 52 der 63 GB-markierten und keine der 37 US-markierten aktiven Ads verlinken; GBP-Copy „worth £39.99“ im Anzeigentext von 151025063, 171191667 und 174599778, „~~£39.99~~“ im Bild von 173307160, „— Customer, UK“ im Bild von 172760571; bei 151025052 und 169082912 weder £ noch UK-Bezug, Indiz nur die PDP). Live-Abruf `get_ad` am 08.10. abends: `countries` ist bei allen 7 weiterhin `[]`.

| Rang | GetHooked-ID | Meta-Ad-ID | Format | Start | Tage | Score | used_count | Ranking-Wert | Headline | Ad Library | share_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 136388964 | 884267707299487 | Bild | 2026-06-11 | 120 | 100 | 1 | 12000 | No More Fighting With Duvet Covers | [Ad Library](https://www.facebook.com/ads/library/?id=884267707299487) | [GetHooked](https://app.gethookd.ai/share/ad/136388964?signature=d0ff0d2a2536e91cfc3dacb7f3b055bf680241a71e3d485ea8d2c98436047966) |
| 2 | 136388847 | 1583232786477915 | Bild | 2026-06-11 | 120 | 100 | 1 | 12000 | No More Fighting With Duvet Covers | [Ad Library](https://www.facebook.com/ads/library/?id=1583232786477915) | [GetHooked](https://app.gethookd.ai/share/ad/136388847?signature=422777a4ae4663b915702dc330ccb3f999733ab57559e373f53beb6af24567f7) |
| 3 | 145443331 | 1440933327878495 | Video 47 s | 2026-08-14 | 56 | 100 | 2 | 11200 | Everyone said it. They were right. | [Ad Library](https://www.facebook.com/ads/library/?id=1440933327878495) | [GetHooked](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) |
| 4 | 136389861 | 1642037860240117 | Video 38 s | 2026-06-11 | 120 | 61 | 1 | 7320 | No More Fighting With Duvet Covers | [Ad Library](https://www.facebook.com/ads/library/?id=1642037860240117) | [GetHooked](https://app.gethookd.ai/share/ad/136389861?signature=52dff4dac27abf45e6f9b062724b0d38f817b3ddcd8939d92684a863d31faaf8) |
| 5 | 133366534 | 1372761711494763 | Video 93 s | 2026-08-03 | 67 | 100 | 1 | 6700 | No More Fighting With Duvet Covers | [Ad Library](https://www.facebook.com/ads/library/?id=1372761711494763) | [GetHooked](https://app.gethookd.ai/share/ad/133366534?signature=ec7e21facd4f53244e7aacaf8002b409a7803a538b1d302bb66be766c52ef924) |
| 6 | 139561428 | 1034362836068724 | Video 16 s | 2026-08-07 | 63 | 100 | 1 | 6300 | Hearth Red. Nearly gone. | [Ad Library](https://www.facebook.com/ads/library/?id=1034362836068724) | [GetHooked](https://app.gethookd.ai/share/ad/139561428?signature=1eb14bdf7f1f4b278f8b5996d37204958181d02f07e10262e225457c7f9a49fd) |
| 7 | 139561410 | 1355121136744622 | Video 16 s | 2026-08-07 | 63 | 100 | 1 | 6300 | Mint Green is almost gone. | [Ad Library](https://www.facebook.com/ads/library/?id=1355121136744622) | [GetHooked](https://app.gethookd.ai/share/ad/139561410?signature=8993cc76f99c424613789bd7c6c9a9248d166b223587f503929e5077c7a435b2) |
| 8 | 139561491 | 1526037445508180 | Video 16 s | 2026-08-07 | 63 | 86 | 1 | 5418 | Everyone's buying the blue one. | [Ad Library](https://www.facebook.com/ads/library/?id=1526037445508180) | [GetHooked](https://app.gethookd.ai/share/ad/139561491?signature=5cbb3a8ead3ed2e5b41ef6ef544d7498f90d8427b339e0ba7304f344c120fb43) |
| 9 | 163921089 | 1609110380938946 | Video 47 s | 2026-08-27 | 43 | 100 | 1 | 4300 | Everyone said it. They were right. | [Ad Library](https://www.facebook.com/ads/library/?id=1609110380938946) | [GetHooked](https://app.gethookd.ai/share/ad/163921089?signature=18918dab03620f19a44f0f4ae4aabab8d5f163dfaa3984dcc8e6e691c7301c1d) |
| 10 | 145443318 | 1474663121347221 | Video 50 s | 2026-08-14 | 56 | 74 | 1 | 4144 | Everyone said it. They were right. | [Ad Library](https://www.facebook.com/ads/library/?id=1474663121347221) | [GetHooked](https://app.gethookd.ai/share/ad/145443318?signature=be73a154548ac1fdbbec6cdf47867c12c72f8b288e40c2faaa6b1db18c69b49b) |
| 11 | 151025063 | 1369166828764339 | Video 29 s | 2026-08-22 | 48 | 86 | 1 | 4128 | No More Fighting With Duvet Covers | [Ad Library](https://www.facebook.com/ads/library/?id=1369166828764339) | [GetHooked](https://app.gethookd.ai/share/ad/151025063?signature=6a64477f3dd49f4b0e862e714a6a052a0839cfe3382654d8e4902e827f95d481) |
| 12 | 168246678 | 1607904514111212 | Video 27 s | 2026-08-29 | 41 | 100 | 1 | 4100 | Check This Before You Buy | [Ad Library](https://www.facebook.com/ads/library/?id=1607904514111212) | [GetHooked](https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59) |
| 13 | 171191667 | 1583757549405276 | Bild | 2026-09-03 | 36 | 100 | 1 | 3600 | No More Fighting With Duvet Covers | [Ad Library](https://www.facebook.com/ads/library/?id=1583757549405276) | [GetHooked](https://app.gethookd.ai/share/ad/171191667?signature=b03cc4b1b86af6280d5edfa0028fe241e19fd20d3b3592e580dd3f576a92669d) |
| 14 | 168246686 | 2035183934551496 | Video 27 s | 2026-08-29 | 41 | 86 | 1 | 3526 | Check This Before You Buy | [Ad Library](https://www.facebook.com/ads/library/?id=2035183934551496) | [GetHooked](https://app.gethookd.ai/share/ad/168246686?signature=a360c60671d85ebeec646d4238239e0ec57ba2d7b037d0bb4c8888b606378db0) |
| 15 | 172403389 | 1725326416267519 | Bild | 2026-09-05 | 34 | 100 | 1 | 3400 | Properly Warm, Never Heavy | [Ad Library](https://www.facebook.com/ads/library/?id=1725326416267519) | [GetHooked](https://app.gethookd.ai/share/ad/172403389?signature=fc57a29e066c788034eca64a557143f0c3e0b71232ea5868d51df06e7536000f) |
| 16 | 172760571 | 1415553300514250 | Bild | 2026-09-06 | 33 | 100 | 1 | 3300 | Properly Warm, Never Heavy | [Ad Library](https://www.facebook.com/ads/library/?id=1415553300514250) | [GetHooked](https://app.gethookd.ai/share/ad/172760571?signature=82cd0a698c2d4720c44c69a474abfa9e4e1f24189f59d7dd6d1f216aaf8e25b8) |
| 17 | 151025052 | 1363184622691769 | Bild | 2026-08-20 | 50 | 61 | 1 | 3050 | Everyone's buying the blue one. | [Ad Library](https://www.facebook.com/ads/library/?id=1363184622691769) | [GetHooked](https://app.gethookd.ai/share/ad/151025052?signature=fa0ac684d0e23c918a286f4c72318a4110a6ecece18af70548ebdfc97ba1bc3e) |
| 18 | 169082912 | 2192690231462965 | Bild | 2026-08-31 | 39 | 74 | 1 | 2886 | Mint Green is almost gone. | [Ad Library](https://www.facebook.com/ads/library/?id=2192690231462965) | [GetHooked](https://app.gethookd.ai/share/ad/169082912?signature=4ab996ca26c1daf73d6ef9a482fc283fbce80f5ccef0bc6ead1abbcdb159c5e0) |
| 19 | 173307160 | 1770207397626174 | Bild | 2026-09-07 | 32 | 81 | 1 | 2592 | Properly Warm, Never Heavy | [Ad Library](https://www.facebook.com/ads/library/?id=1770207397626174) | [GetHooked](https://app.gethookd.ai/share/ad/173307160?signature=20a01e20e8d0bc5720968b8ee00d824e45a8e18af15aa506b60fd22b7789241f) |
| 20 | 174599778 | 2301727147248244 | Bild | 2026-09-09 | 30 | 74 | 1 | 2220 | No More Fighting With Duvet Covers | [Ad Library](https://www.facebook.com/ads/library/?id=2301727147248244) | [GetHooked](https://app.gethookd.ai/share/ad/174599778?signature=0f3b267681520755857f3c8967162b7f9b49eb9f935ce9ac83a4c94572252bc1) |

**Hinweise zur Tabelle:**

- **Dubletten:**
  - 163921089 ist byte-identisch mit 145443331.
  - 145443318 ist ein Hook-Swap derselben Creator-Aufnahme.
  - 139561428, 139561410 und 139561491 sind dasselbe KI-Template mit getauschter Farbe.
  - 168246678 und 168246686 sind ein Text-A/B auf demselben Video.
- **Live-Abweichungen zum Inventar (s2, 08.10.):**
  - 145443318: Score jetzt 61 statt 74.
  - Share-JSON vom Abend: 171191667 90, 151025052 86, 169082912 80, 173307160 100.
  - Keine der 20 Ads steht in der s2-Liste der seit 07.10. beendeten Ads.
- **Fremder Produktname:** 174599778 zeigt im Bild „CoolRest™ Cooling Duvet“ (ein anderes Pleene-Produkt), verlinkt aber auf die EasyRest-Seite.

**Anleitung: was in der Ad Library pro Ad geprüft werden soll**

Jede Ad über den Ad-Library-Link öffnen, die Detailansicht der Anzeige aufrufen und Folgendes festhalten (Screenshot je Ad):

1. **Status und Startdatum:**
   - Notieren: „Active“ oder „Inactive“ und das angezeigte Startdatum.
   - Mit der Spalte „Start“ vergleichen. Wenn die Ad inzwischen beendet ist, das Enddatum notieren.
2. **UK-Reichweite:**
   - Prüfen, ob für die Ad irgendeine Reichweite, Impression-Spanne oder Altersverteilung für das Vereinigte Königreich angezeigt wird. Den genauen Wortlaut übernehmen.
   - Erwartung (nicht verifiziert): Bei Ads, die nur in GB laufen, zeigt Meta keine Reichweite. Dann „n/a (Ad Library zeigt keine UK-Reichweite)“ eintragen und nichts schätzen.
   - Bei den 7 Ads ohne GetHooked-Länderangabe (151025063, 171191667, 172760571, 151025052, 169082912, 173307160, 174599778) zusätzlich in der Ad-Library-Suche den Länderfilter „United Kingdom“ setzen und notieren, ob die Ad dort erscheint. Ob das Erscheinen eine Ausspielung in GB belegt, ist nicht verifiziert; das Ergebnis wörtlich in die Spalte „Notiz“ übernehmen.
3. **EU-Transparenz:**
   - Prüfen, ob ein Abschnitt zur EU-Transparenz existiert.
   - Falls ja, festhalten: Reichweite in der EU, Länderaufteilung (z. B. Irland), Alter/Geschlecht sowie Begünstigter und Zahler.
   - Beim Zahler besonders auf „One Way Ecom Limited“ (Betreiber laut Impressum) und „21Commerce Limited“ (laut Footer für die Werbung zuständig) achten.
   - Gibt es keinen solchen Abschnitt, lief die Ad sehr wahrscheinlich nicht in der EU (nicht verifiziert). Dann „kein EU-Abschnitt“ notieren.
4. **Ausspielungsorte:**
   - Die angezeigten Plattform-Symbole notieren und mit GetHooked vergleichen (facebook, instagram, audience_network, messenger, threads).
   - Abweichungen vermerken, z. B. wenn Threads oder Audience Network fehlen.
5. **Varianten:**
   - Prüfen, ob die Ad „multiple versions“ hat. Die Anzahl der Versionen notieren und bei jeder Version festhalten, was sich ändert (Headline, Primärtext, Bild/Video, Format 9:16 oder 1:1, CTA).
   - Falls angezeigt wird, wie viele Ads dieses Creative und diesen Text nutzen: Zahl notieren und mit used_count vergleichen (nur 145443331 hat used_count 2).
   - Bei 139561428/410/491 und 168246678/686 prüfen, ob die Varianten als eigene Ads oder als Versionen derselben Ad erscheinen.
6. **Ziel-URL:** Auf den CTA-Button gehen und notieren, ob er wirklich auf `pleene.com/products/easyrest` führt und welche URL-Parameter angehängt sind.
7. **Seitenebene (einmal pro Marke):**
   - Seitenname und Gesamtzahl der aktiven Ads der Seite notieren. Vergleichswerte: 137 im Inventar, 153 laut `search_ads` am 08.10.
   - Prüfen, ob die Seite US-Ads mit „comforter“ zeigt (40 aktive laut Inventar).
   - In der Seitentransparenz, falls angezeigt, Erstellungsdatum und frühere Seitennamen notieren.

Erfassungsbogen (eine Zeile pro Ad):

| Meta-Ad-ID | Status/Start lt. Library | UK-Reichweite | EU-Transparenz (Reichweite, Länder, Zahler) | Plattformen | Versionen (Anzahl, was variiert) | Ads mit gleichem Creative | Ziel-URL | Notiz |
|---|---|---|---|---|---|---|---|---|
| (z. B. 884267707299487) | | | | | | | | |

---

## Für Nevio zum Ansehen

**Auswahlmethode:** Kandidaten sind alle aktiven Video-Ads, sortiert nach Laufzeit × Score (× used_count). Pro Skript-Familie kommt höchstens eine Ad in die Auswahl. Deshalb fallen weg:

- 163921089 und 145443318 (gleiche Familie wie 145443331)
- 151025063 (Hook-Swap von 136389861)
- 139561428 und 139561491 (gleiches Template wie 139561410)
- 168246686 (Text-A/B von 168246678)

Die fünf besten Familien sind zugleich die fünf lehrreichsten, weil jede einen anderen Mechanismus zeigt: echter Creator, Schmerz mit Autorität, Ekel-Langform, sprecherloses Knappheits-Template und Kaufkriterien-Checkliste.

### 1. 145443331 – „Everyone said it. They were right.“ (Video 47 s, 56 Tage, Score 100, used_count 2)

- GetHooked: https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660
- Ad Library: https://www.facebook.com/ads/library/?id=1440933327878495

Signal: Mit Score 100, used_count 2 und einem byte-identischen Re-Upload (163921089, ebenfalls Score 100) ist das das stärkste Skalierungssignal im ganzen Account. Lernen: Ein echter Mann (ca. 30–40) mit O-Ton, ein kontraintuitiver Ich-Hook („I haven't changed my bed linen in three months and it's never felt fresher.“) und nur 1,5 Schnitte pro 10 s schlagen jede Hochglanz-Produktion; achte auf die Reihenfolge Hook → Waschmaschine/Trockner → warm/kühl → „I swear to you, my bed always feels fresh.“ → Angebot.

### 2. 136389861 – „No More Fighting With Duvet Covers“ (Video 38 s, 120 Tage, Score 61)

- GetHooked: https://app.gethookd.ai/share/ad/136389861?signature=52dff4dac27abf45e6f9b062724b0d38f817b3ddcd8939d92684a863d31faaf8
- Ad Library: https://www.facebook.com/ads/library/?id=1642037860240117

Signal: Mit 120 Tagen ist das die am längsten laufende Video-Ad aller 692 Ads (das nächstlängste Video lief 89 Tage), und der Hook-Swap 151025063 („I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“) holt mit fast gleichem Body Score 86. Lernen: Angle E („As we get older, making the bed shouldn't be this hard.“) ist bei der älteren Käuferschaft ein Dauerläufer, und der Verbots-Hook „If your shoulders ache, don't do this.“ mit einer sehr wahrscheinlich KI-generierten Lehrerfigur zeigt, wie billig sich ein Pattern-Interrupt mit Autorität bauen lässt.

### 3. 133366534 – „No More Fighting With Duvet Covers“ (Video 93 s, 67 Tage, Score 100)

- GetHooked: https://app.gethookd.ai/share/ad/133366534?signature=ec7e21facd4f53244e7aacaf8002b409a7803a538b1d302bb66be766c52ef924
- Ad Library: https://www.facebook.com/ads/library/?id=1372761711494763

Signal: Das ist die einzige Ekel- bzw. Hygiene-Ad unter den 20 Winnern, und ihre Kopien vom 01.10. (193234275 Score 52, 193234279 Score 44) erreichen das Original nicht. Lernen: Hygiene funktioniert bei Pleene nur als komplette 93-s-Beweiskette (Ekel-Hook „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ → Reframe „The problem isn't your bed linen. The problem is your duvet.“ → Mechanismus → „Over 10,000 sleepers“ und „96%“ → Review-Karten → Future Pacing), nicht als Einzeiler; zugleich sind genau diese Zahlen und Karten nicht verifiziert.

### 4. 139561410 – „Mint Green is almost gone.“ (Video 16 s, 63 Tage, Score 100)

- GetHooked: https://app.gethookd.ai/share/ad/139561410?signature=8993cc76f99c424613789bd7c6c9a9248d166b223587f503929e5077c7a435b2
- Ad Library: https://www.facebook.com/ads/library/?id=1355121136744622

Signal: Das 16-s-KI-Template ohne Sprecher läuft in drei Farben (139561428 Hearth Red Score 100, 139561491 Coastal Blue Score 86), wurde zweimal neu hochgeladen (185228755, 200490701) und als Bild kopiert (169082912, 173307160), ist also Pleenes robusteste Familie. Lernen: Farbe als austauschbare Variable plus Angebot und Restmenge direkt im Hook („This week only: 2 FREE Pillow Cases with every DUVET / Only 26 left in Mint Green“) bringen mit minimalem Produktionsaufwand Winner, wobei die Knappheit auf der Seite durch nichts belegt ist (dort steht nur „Ready to Ship – Limited Stock“).

### 5. 168246678 – „Check This Before You Buy“ (Video 27 s, 41 Tage, Score 100)

- GetHooked: https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59
- Ad Library: https://www.facebook.com/ads/library/?id=1607904514111212

Signal: Im direkten Text-A/B bei gleicher Laufzeit gewinnt dieser Hook (Score 100) gegen „Seen coverless duvets all over your feed?“ (168246686, Score 86); die Re-Uploads (185228764 Score 1, 200490712 nach 2 Tagen aus) tragen dagegen nicht. Lernen: Pleene definiert selbst die Kaufkriterien („1. Does the WHOLE thing fit a normal washing machine?“ / „2. Is it dry in 2 hours without a tumble dryer?“ / „3. Can you test it at home for 90 nights?“ → „yes, yes and yes.“), und genau dieses Format können wir mit Kriterien kontern, bei denen Pleene schwach ist (siehe Angriffsfläche, Punkt 6).

---

## Angriffsfläche – 10 Punkte

**Vorbemerkung:** Daten zu unserem eigenen Produkt liegen in dieser Analyse nicht vor (n/a). Jeder Angriff setzt voraus, dass wir die jeweilige Eigenschaft wirklich haben und belegen können. Testimonial-Hooks dürfen nur mit echten eigenen Kunden umgesetzt werden. Pleene wird in keiner Ad namentlich genannt; ob eine vergleichende Werbung zulässig ist, müsste vorher geprüft werden (Einschätzung, nicht verifiziert).

Verteilung: Angle 2, Avatar 2, Format 2, Angebot 1, Behauptung 2, Seite 1.

### 1. Angle E konkret statt „Schulter/Rücken“: Arthritis, Erschöpfung, Herz

- **Beobachtung bei Pleene:**
  - Angle E kommt in den Ads nur allgemein vor: „If your shoulders ache, don't do this.“ (136389861), „pain in my shoulders and back“ (151025063), „My back just can't take this anymore.“ (200490722) und „at my age“ (200490716, Score 12).
  - Neue E-Ads vom 25.09. starben nach höchstens 6–7 Tagen („A Winter Duvet You Can Actually Lift“, 3 von 3 Verlierer; „Change Your Bed Without The Pain After“). Die einzige Hand- bzw. Arthritis-Linie („Made for hands that hurt“) gehörte zum eingestellten ZipSheet.
  - Die Käufer nennen dagegen konkrete Erkrankungen: „The wifes hands are quite bad with Athritis“ (T064), „esp if you have arthritus in hands“ (T074), „chemo makes me very fatigued so the fact there is no messing about getting my duvet in a cover is an absolute god send“ (T070), „I have a bad heart and it takes a lot out of me“ (T043). Insgesamt gibt es 26 Bewertungen zu Gesundheit und Mobilität.
- **Unser Angriff:**
  - Hook: „If arthritis has got into your hands, the duvet cover is the hardest job in the house.“
  - Format: 30–40-s-Video mit Großaufnahme echter, älterer Hände. Zuerst Druckknöpfe und Bezugsecken (alt), dann wird die Decke in einem Zug aufs Bett gelegt (neu). Dazu O-Ton einer echten Kundin oder eines echten Kunden mit Arthritis.
  - Zweite Variante für Erschöpfung (Chemo, Herz) mit dem Hook „When you've only got so much energy in a day, don't spend it on a duvet cover.“
- **Erwarteter Vorteil:**
  - Wir treffen die Sprache und Lebenslage der tatsächlichen Käufer.
  - E hat bei Pleene die längste Ø Laufzeit (35,4 Tage), wenn es glaubwürdig ist. Mit einer echten Person schlagen wir Pleenes KI-Seniorin (200490716) bei der Glaubwürdigkeit (Einschätzung).

### 2. Angle B als Paar-Konflikt („er schwitzt, sie friert“) statt nur „warm genug im Winter“

- **Beobachtung bei Pleene:**
  - B hat unter den Kern-Angles den höchsten Ø Score (37,8, nur GB 43,5). Pleene spielt B aber ausschließlich als Winterwärme bzw. Nicht-Schwitzen („Looks lovely, but you'll freeze under that in winter.“, 178749251). Diese Familie ist seit 07.10. inaktiv.
  - Das Paar-Motiv steht nur auf der eigenen Produktseite, als nicht auffindbares Testimonial: „David, 58: My wife runs cold and I run hot. First winter duvet we've agreed on in years.“
  - Käufer: „I like to be warm and cosy whereas my husband wants to be cool and unrestricted by quilts and additional quilt covers.“ (T054); Nachtschweiß nennen nur Männerkonten (T057, T105, T170).
  - Wechseljahre: 0 Ads und 0 Bewertungen. Ein Wechseljahre-Angle wäre deshalb ein unbelegter Test und kein Angriff.
- **Unser Angriff:**
  - Hook: „She's freezing at 3am. He's kicked the duvet off. Same bed, every single night.“
  - Format: Split-Screen eines echten Paares 55–70 im eigenen Schlafzimmer; die Auflösung zeigt zwei Decken, eine pro Person, beide ganz waschbar.
  - Angebot: Zweier-Set als Standard.
  - Voraussetzung: Unsere Temperatur-Claims sind belegt.
- **Erwarteter Vorteil:**
  - Wir besetzen den Angle mit dem höchsten Ø Score und einer Situation, die Pleene in keiner Ad zeigt.
  - Das Paar-Narrativ erklärt organisch, warum man zwei Stück kauft. Pleene muss das Couple-Bundle dagegen per Vorauswahl erzwingen.

### 3. Avatar: der ältere Mann bzw. Witwer als Ich-Erzähler

- **Beobachtung bei Pleene:**
  - Nach Vornamen sind 56 % der Trustpilot-Konten männlich (Schätzung, nicht verifiziert), und die Käufer sind durchweg Senioren.
  - Witwer schreiben: „As a widower living on my own changing the king size duvet cover on my own was struggle“ (T236), „I ordered these after my wife passed away“ (T029), „Absolute magic just helped an old man to enjoy his duvet without the continuous fight.“ (T001).
  - Kein älterer Mann tritt als alleiniger Ich-Erzähler bzw. Witwer auf. Ein älterer Mann spricht nur im Paar-UGC 200490722/200490658 (Start 06.10., Score 1) und als sehr wahrscheinlich KI-generierter Presenter im Hook von 136389861.
  - Sonst erscheinen ältere Männer nur stumm im Bild (u. a. 200490718/200490660 „Bedding Made for Independence“, 177443533/185228773/200490708, 193234224, 178749251) oder als Review-Karte „George, 82“ in 133366534 (Off-VO in der dritten Person: „George is over 80. A widower.“), zu der ein Mann gezeigt wird, der auf ca. 45–55 geschätzt wird. Männliche Ich-Erzähler sind nur Creator ca. 30–40 (145443331).
  - Pleenes neue Senioren-Personas sind Frauen und laufen größtenteils mit KI-Bildern (200037052 „I'm 71“, 200037049 „I'm 66“, 200490716).
- **Unser Angriff:**
  - Hook (nur mit einem echten Kunden): „I'm 79, I live on my own now, and the duvet cover was the one job I couldn't do.“
  - Format: Talking Head mit O-Ton im eigenen Schlafzimmer, ohne KI-Bilder, 40–50 s, ruhiger Schnitt wie bei Pleenes Creator-Winner (1,5 Schnitte pro 10 s). Dazu eine Bild-Ad mit Porträt und Zitat.
- **Erwarteter Vorteil:**
  - Wir sprechen das größte Käufersegment direkt an, das Pleene nie als Ich-Erzähler zeigt.
  - Echte Senioren wirken glaubwürdiger als Pleenes KI-Personas. Die Persona-Videos liegen laut Live-Abfrage bei höchstens 44, 200490716 liegt bei 12 (Einschätzung zur Glaubwürdigkeit).

### 4. Avatar: erwachsene Kinder, die vor Weihnachten für Mum und Dad kaufen

- **Beobachtung bei Pleene:**
  - In GB gibt es **keine** Geschenk-Ad. Die einzige ist US-only und erst seit 07.10. live: „One Less Chore For Mum & Dad.“ (200490661). In 200490716 klingt das Motiv nur an: „Then my daughter got me the Plein Easy Rest Duvet“.
  - Käufer kaufen bereits für andere: T171 („Ordered for mother“), T196 (Sohn, Weihnachten), T289 und T200 (für den Sohn), T133 (Geschenk an sich selbst zum 84. Geburtstag). „She wants to remain independent“ (T283).
  - Pleenes Lieferung ist der häufigste Kritikpunkt (51 Bewertungen, z. B. „Took over 3 weeks to be delivered“, T143).
- **Unser Angriff:**
  - Hook: „Mum will never ask for help with the duvet cover. So give her one that doesn't need one.“
  - Format: Bild plus 20-s-Video aus Sicht der Tochter bzw. des Sohnes 35–55: Paket kommt an, die Mutter legt die Decke allein aufs Bett.
  - Angebot: Geschenkverpackung oder Geschenkkarte und eine feste Liefergarantie vor Weihnachten mit konkretem Stichtag. Nur anbieten, wenn wir sie logistisch halten können.
  - Start: jetzt (Oktober), damit das Lernbudget vor der Hochsaison liegt.
- **Erwarteter Vorteil:**
  - Wir erreichen einen zweiten, jüngeren und online-affinen Käufer, den Pleene in GB nicht anspricht.
  - Die Liefergarantie trifft genau Pleenes Schwachstelle in der umsatzstärksten Saison.

### 5. Format: Beweis-Video – Zeitraffer vom Waschen bis Trocknen mit Uhr, daneben eine normale Decke

- **Beobachtung bei Pleene:**
  - „dry in 2 hours“ steht in fast jeder Ad, wird aber **nie gezeigt**. Gezeigt wird nur das Einlegen (200490655/721 „But watch this.“) oder eine Wäscheleine (200490719).
  - Es gibt drei unvereinbare Fassungen: mit Trockner („the tumble dryer, and it's dry in two hours.“, 184134597), ohne Trockner („2 hours. No dryer.“, 168246678) und an der Luft („and then I just air dry it for 2 hours“, 200490718).
  - Die eigene Seite tb-6 sagt „Air-dries in 2–3 hours“ und schränkt ein: „Drying times depend on room temperature, airflow and spin speed.“
  - Käufer: „Drying takes about 4hours but all good.“ (T019), „dried inside within 1 day“ (T262). Vor dem Kauf hatten 4 Käufer Zweifel an der Waschmaschine und 2 am Trocknen im Winter.
  - Es gibt keinen Vergleichstest gegen eine normale Decke.
- **Unser Angriff:**
  - Hook: „9:02am. King-size duvet, standard 7kg machine. Keep your eye on the clock.“
  - Format: ein durchgehender Take als Zeitraffer, Uhr im Bild, Trommelgröße auf dem Typenschild lesbar, Raumtemperatur eingeblendet. Daneben eine normale Daunen- bzw. Faserdecke im selben Ablauf. Am Ende der echte Messwert, auch wenn er über 2 Stunden liegt.
  - Drei Schnittfassungen: 15 s, 30 s und 60 s.
- **Erwarteter Vorteil:**
  - Wir zeigen einen Beweis, wo Pleene nur behauptet, und beantworten die beiden wichtigsten Produkt-Einwände.
  - Pleene kann dieses Format nicht kopieren, ohne seine eigenen widersprüchlichen Angaben offenzulegen (Einschätzung).

### 6. Format: Konter-Checkliste auf Basis von Pleenes eigenem Winner-Format

- **Beobachtung bei Pleene:**
  - Die Checkliste 168246678 ist ein Winner (41 Tage, Score 100). Sie fragt aber nur, was Pleene mit „yes“ beantworten kann (Waschmaschine, 2 Stunden, 90 Nächte).
  - Die Schwachstellen fragt sie nicht ab:
    - Lieferzeit: 51 Bewertungen, z. B. „Took 13 days instead of 6 day advertised“ (T094).
    - Herkunft: „despite the company being based in London, the product actually has to travel all the way from China“ (T107).
    - Rücksendung: „They say a free return - no they don't“ (T119).
    - Waschmaschine: Die eigene Größentabelle verlangt „Fits a drum from“ 6–8 kg.
  - Pleenes Re-Uploads dieser Checkliste tragen nicht (185228764 Score 1, 200490712 nach 2 Tagen aus).
- **Unser Angriff:**
  - Hook: „Before you buy a coverless duvet off a Facebook ad, ask these 3 questions.“
  - Einblendungen: „1. Where does it ship from, and how many days?“ / „2. Who pays the postage if you send it back?“ / „3. Which drum size does YOUR size need?“, jeweils mit unserer konkreten Antwort.
  - Format: Text-Template 25–30 s ohne Sprecher (wie das Original) und als Bild.
  - Pleene nicht nennen.
- **Erwarteter Vorteil:**
  - Wir nutzen ein bei Pleene erprobtes Siegerformat und verschieben die Kaufkriterien auf Lieferung, Rückgabe und Maße, also dorthin, wo Pleene laut Bewertungen schwach ist.
  - Wer beide Ads sieht, prüft Pleene anschließend mit unseren Kriterien (Einschätzung).

### 7. Angebot: Rückgabe, die wirklich kostenlos ist, und Beigaben, die im Warenkorb stehen

- **Beobachtung bei Pleene:**
  - Pleene wirbt mit „90-Night Free Trial. Money back, no questions asked.“ Die eigene Policy sagt dagegen: „Return shipping Paid by the customer, unless the return is due to an error on our side“, „Original shipping fees are non-refundable“, und vor der Rücksendung soll man erst den Support kontaktieren.
  - Im Warenkorb wird zusätzlich ein „180-Day Return Policy – Upgrade“ für £2.99 verkauft.
  - Käufer: „it would be really expensive to return the item as the company was based in China“ (T055), „They say a free return - no they don't“ (T119).
  - Die beworbenen Gratis-Kissenbezüge „(Value: £39.99)“ stehen nicht im Warenkorb (Kaching `freeGifts: []`). Dasselbe Produkt kostet im Drawer £19.99; ob das ein Paar oder ein einzelner Bezug ist, ist nicht verifiziert. Ein Käufer schreibt: „it offers two free pillow cases but no indication of this when you come to pay“ (T059, 1★).
- **Unser Angriff:**
  - Hook bzw. Endkarte: „Not for you? We send the return label. You don't pay a penny.“
  - Im Ad und above the fold: „Free UK returns – prepaid label, UK return address“.
  - Jede Gratisbeigabe erscheint im Warenkorb als eigene Position mit £0.00, und der genannte Wert entspricht unserem eigenen Einzelpreis.
  - Voraussetzung: Wir haben ein UK-Retourenlager bzw. eine UK-Retourenadresse (n/a, zu prüfen).
- **Erwarteter Vorteil:**
  - Wir nehmen dem Facebook-skeptischen Senior das Risiko ab (8 Bewertungen nennen Betrugsangst schon vor dem Kauf, z. B. „i only saw the advert on facebook and wasn't sure if this would be a scam“, T098).
  - Pleene kann das bei Rücksendungen nach China nicht ohne Weiteres nachziehen (Einschätzung, nicht verifiziert).

### 8. Behauptung: prüfbare Zahlen statt „any machine“ und „2 hours“

- **Beobachtung bei Pleene:**
  - Waschmaschine: „Fits in every washing machine“ steht im ATF der Produktseite, „It fits in any normal household washing machine.“ in 133366534. Die eigene Größentabelle sagt dagegen: Narrow und Single ab 6 kg, Single XL und Double ab 7 kg, King und Super King ab 8 kg. Käuferin Rona Dixon schreibt „although it is a tight fit in my washing machine“; dieser Satz ist auf tb-6 herausgekürzt.
  - Wärme: „10.5 TOG — proper winter warmth“ auf der Produktseite gegen „It's a mid-weight, all-season duvet“ auf der Home-Page.
  - Kundenzahl: „Over 10,000 customers“ gegen „7,000+“ auf tb-6. „96% never want to go back“ in 133366534 ist nicht verifiziert.
- **Unser Angriff:**
  - Jede Ad trägt genau eine nachprüfbare Zahl mit Bedingung.
  - Hook für ein Bild: „Check the sticker on your washing machine door. 7kg? Your Double fits. 8kg? Go King.“ (Kilowerte durch die Angaben unserer eigenen Größentabelle ersetzen.)
  - Trocknen nur mit Bedingung, z. B. „Dry in [eigener Messwert] on a line at 20°C, faster in the dryer.“
  - Kundenzahlen nur, wenn wir sie belegen können, und überall dieselbe Zahl.
- **Erwarteter Vorteil:**
  - Glaubwürdigkeit gegenüber skeptischen Käufern („I, like you, am somewhat suspicious of claims by companies on FB etc“, T192) und weniger Retouren wegen zu kleiner Maschine.
  - Geringeres Beschwerderisiko bei Werbeaufsicht bzw. ASA als mit absoluten „any“-Claims (Einschätzung, nicht verifiziert).

### 9. Behauptung: Hygiene nur mit Beleg und nur als Nebenargument

- **Beobachtung bei Pleene:**
  - In Hygiene steckt Pleene den größten Testaufwand: 34 von 119 Launches in 14 Tagen nach Text-Angle, 28 aktive A-Ads. Daraus kommen nur 2 Winner. Die Headline „Be honest. When did you last wash it?“ lief in 51 Ads, keine länger als 24 Tage.
  - Belegt wird nichts:
    - „bacteria“ steht in keiner Ad. Nur die US-Seite behauptet „No chance for dust mites & bacteria“.
    - Die Milben zeigt nur ein vager Mikroskop-Kreis (133366534).
    - „Hypoallergenic and kind to sensitive skin“ steht ohne Zertifikat da.
    - 60 °C kommt nur in der FAQ vor („you can occasionally wash it at 60°C“), in keiner Ad.
  - Die Käufer interessiert das kaum: Hygiene nennen 8 von 283 positiven Bewertungen, „mites“, „bacteria“ und „allergy“ keine einzige.
- **Unser Angriff:**
  - Hygiene wird nicht unser Lead-Angle; Pleene soll dort weiter Budget verbrennen.
  - Als Nebenargument eine einzige harte Zahl, z. B. eine Endkarte „Whole duvet washable at 60°C.“ mit Pflegeetikett im Bild.
  - Milben-, Allergie- oder Bakterien-Claims nur mit Prüfbericht, der in der Ad als Beleg genannt wird.
  - Hook-Beispiel als Nebenargument in einem C-Video: „Your cover gets washed every week. The duvet inside it never has. Ours goes in whole, at 60°C.“
- **Erwarteter Vorteil:**
  - Eine konkrete Zahl schlägt Pleenes vage Ekel-Bilder.
  - Wir sparen Testbudget auf einem Angle, der laut Bewertungen nicht der Kaufgrund ist, und vermeiden unbelegte Gesundheitsclaims (Einschätzung).

### 10. Seite: Vertrauensblock above the fold mit echten Bewertungen, Antworten und Herkunft

- **Beobachtung bei Pleene:**
  - Bewertungen:
    - Das Judge.me-Widget zeigt 172 Bewertungen, davon 154 Trustpilot-Importe. Übernommen wurden 0 von 6 negativen und 0 von 7, die China erwähnen.
    - Die einzigen Foto-Bewertungen (J004–J011) entstanden in 3 Minuten 23 Sekunden.
    - Pleene antwortet auf 0 von 291 Trustpilot-Bewertungen.
    - tb-6 nennt „Excellent 4.7/5 · 250 reviews“, erfasst waren am 08.10. 291.
  - Testimonials:
    - Die „✓ Verified“-Karten (Margaret 67, James 55, Sarah 41, Robert 50, David 58) finden sich in keiner Bewertung.
    - „Robert, 61“ sagt auf der UK- und der US-Seite völlig verschiedene Dinge.
  - Firmenangaben:
    - „AS FEATURED IN“ zeigt Logos ohne Artikel; die Dateien heißen `Design_ohne_Titel.png`.
    - Impressum: One Way Ecom Limited, Hongkong, Telefon „+1 (205) 360-5811“.
  - Pop-up: Das Gewinnspiel „Win a free Duvet“ erscheint nach etwa 4 s und hat keine auffindbaren Teilnahmebedingungen.
- **Unser Angriff:**
  - Unter Preis und CTA ein fester Block mit drei Elementen:
    1. Live-Trustpilot-Widget mit allen Sternen inklusive 1★ und sichtbaren öffentlichen Antworten von uns.
    2. „Ships from [UK-Ort] · tracked · [echter Median] days“ mit UK-Rücksendeadresse.
    3. Ein Gründer- bzw. Team-Foto mit Namen und UK-Telefonnummer.
  - Kein Pop-up in den ersten 30 s. Testimonials nur mit Namen und Link zur Originalbewertung.
  - Voraussetzung: Diese Fakten treffen auf uns zu (n/a, zu prüfen).
- **Erwarteter Vorteil:**
  - Die Seite beantwortet genau die Fragen, die Pleenes Käufer laut Bewertungen vor dem Kauf haben: „Too often you are taken in by amazing ads you see online.“ (T076), „pleene has a low security rating“ (T020).
  - Wer zwischen beiden Shops vergleicht, findet bei uns prüfbare Belege und bei Pleene nicht auffindbare Testimonials (Einschätzung).

---


---
*Kurzfassung ohne Anhang. Vollinventar, alle 63 Videos und 74 Statics im Detail sowie die Bewertungen wörtlich stehen in Pleene_Analyse.md.*
