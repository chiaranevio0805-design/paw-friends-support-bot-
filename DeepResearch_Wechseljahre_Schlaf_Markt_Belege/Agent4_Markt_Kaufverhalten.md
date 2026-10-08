# Belege: Agent 4 – Marktzahlen und Kaufverhalten

*Teil der Abgabe [DeepResearch_Wechseljahre_Schlaf_Markt](../DeepResearch_Wechseljahre_Schlaf_Markt.md), Stand 8. Oktober 2026. Jede Aussage mit Einordnung, wörtlichem Zitat (Original), Link, Quellendatum, Einschränkung und Ergebnis des unabhängigen Wahrheits-Checks.*

Legende: ✅ BELEGT · ⚠️ EINGESCHRÄNKT (nur mit Einschränkung verwenden) · ❌ NICHT BELEGT / MYTHOS (nicht verwenden). Verworfene Einträge stehen nur im Hauptdokument, Anhang A.

## Track 4A: Marktgröße, Wachstum, Online-Anteil

*Prüf-Fazit: Der Track ist insgesamt verlässlich: Alle 43 Claims ließen sich an den angegebenen oder an besseren Primärquellen prüfen, keiner musste verworfen werden. Echte Zahlenfehler gab es nur im Detail (ONS-Rohwerte in 4A-28, ein Google-Trends-Monatswert, 17,6 % statt 18 % bei Dunelm 2022). Korrigiert werden mussten vor allem Interpretationen und Begründungen: die falsch benannte Methodikänderung bei den ONS-Ausgaben, die Zusammensetzung der ONS-Gruppe 'Household goods stores', 'jedes Jahr November-Peak', die Black-Friday-Zuordnung der Trends-Spitzenwoche, die Herleitung des Dunelm-Marktwachstums (eher ca. 2 % als knapp 3 %), die unbelegte Aussage 'der Großteil wird importiert' (HMRC: nur ca. £43 Mio. Bettdecken-Importe) und der IKEA-Preis (nur In-Store-Aktion). Für Ads direkt nutzbar sind fast nur die Händlerpreise als datierte Momentaufnahme und die amtlichen Online-Anteile. Marktgrößen und Wachstumsraten sind Näherungen mit großer Unsicherheit; eine belastbare Duvet-Marktgröße oder -CAGR gibt es öffentlich nicht.*

### 1 Marktgröße

#### 4A-01

✅ BELEGT · Angle: Markt

**UK-Haushalte gaben im Finanzjahr April 2024 bis März 2025 durchschnittlich £1,30 pro Woche für Schlafzimmertextilien einschließlich Bettdecken und Kissen aus, zusammen £38 Mio. pro Woche.**

> “Table A1 Detailed expenditure with full-method standard errors, UK, financial year ending 2025 … 5.2.1 | Bedroom textiles, including duvets and pillows | 1.30 | 38 | 380 | 15.6 [Spalten: Average weekly expenditure all households (£) | Total weekly expenditure (£ million) | Recording households in sample | Percentage standard error (full method)]”

- **Quelle:** [Office for National Statistics – Family Spending Workbook 1: Detailed expenditure and trends (FYE 2025 edition), Table A1](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Living Costs and Food Survey, 5.000 Haushalte UK, April 2024–März 2025; 380 Haushalte mit Ausgaben in dieser Kategorie; gewichtet auf 28,71 Mio. Haushalte (Tabelle A6)
- **Einordnung/Einschränkung:** Amtliche Statistik für das ganze UK mit dokumentierter Methodik. Einschränkungen: Der Standardfehler beträgt 15,6 %, das 95-%-Intervall reicht also grob von £0,90 bis £1,70 pro Woche. Die Kategorie heißt 'Bedroom textiles, including duvets and pillows' und wird nicht weiter aufgeschlüsselt; der Bezeichnung nach ist Bettwäsche (Bezüge, Laken) sehr wahrscheinlich enthalten. Ab FYE 2025 berechnet die ONS die Standardfehler mit einer neuen Methode. Nur als Marktrahmen nutzen, nicht in Ads.
- **Wahrheits-Check:** *korrigiert*. Datensatzseite per WebFetch (Release 11.06.2026, nächste Ausgabe offen) und Original-xlsx FYE 2025 per curl gelesen. Zeile 5.2.1 exakt bestätigt (1.30 | 38 | 380 | 15.6), ebenso 5.000 Haushalte und 28.710 Tsd. gewichtete Haushalte. Begründung präzisiert: Dass Bettwäsche enthalten ist, ist aus der Kategoriebezeichnung abgeleitet. Den nicht belegten Allgemeinsatz zur Tagebuch-Untererfassung habe ich entfernt und die neue Standardfehler-Methode laut 'Background notes' ergänzt.

#### 4A-02

⚠️ EINGESCHRÄNKT · Angle: Markt

**Hochgerechnet geben UK-Haushalte etwa £2,0 Mrd. pro Jahr für Schlafzimmertextilien inkl. Bettdecken und Kissen aus, vermutlich einschließlich Bettwäsche (eigene Rechnung £38 Mio. × 52 Wochen; Unsicherheitsbereich etwa £1,4–2,6 Mrd.).**

> “5.2.1 | Bedroom textiles, including duvets and pillows | 1.30 | 38 | 380 | 15.6”

- **Quelle:** [Office for National Statistics – Family Spending Workbook 1, Table A1 (FYE 2025)](https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends/fye2025/workbook1detailedexpenditureandtrends.xlsx)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** LCF, 5.000 Haushalte UK, FYE 2025
- **Einordnung/Einschränkung:** Die Jahreszahl ist eine eigene Hochrechnung, keine Angabe der ONS: £38 Mio. × 52 = £1,976 Mrd. Unsicherheit: ±1,96 × 15,6 % ≈ ±31 %, also etwa £1,37–2,58 Mrd. Bettwäsche ist der Kategoriebezeichnung nach vermutlich enthalten; ein reiner 'Duvet-Markt' lässt sich daraus nicht ablesen. Es handelt sich um Konsumentenausgaben, nicht um Händlerumsätze. Nur als Größenordnung nennen, nicht in Ads.
- **Wahrheits-Check:** *korrigiert*. xlsx selbst geöffnet, Rechnung nachvollzogen. Aussage leicht korrigiert: Dass Bettwäsche enthalten ist, ist aus der Bezeichnung abgeleitet und nicht ausgewiesen.

#### 4A-03

✅ BELEGT · Angle: Markt

**Für Haushaltstextilien insgesamt (inkl. Kissen, Handtücher, Vorhänge) gaben UK-Haushalte FYE 2025 durchschnittlich £2,40 pro Woche aus, zusammen £70 Mio. pro Woche (hochgerechnet etwa £3,6 Mrd. pro Jahr).**

> “5.2 | Household textiles | 2.40 | 70 | 970 | 10.7 … 5.2.2 | Other household textiles, including cushions, towels, curtains | 1.10 | 32 | 970 | 14.4”

- **Quelle:** [Office for National Statistics – Family Spending Workbook 1, Table A1 und A6 (FYE 2025)](https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends/fye2025/workbook1detailedexpenditureandtrends.xlsx)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** LCF, 5.000 Haushalte UK, April 2024–März 2025; Standardfehler 10,7 %
- **Einordnung/Einschränkung:** Die Wochenwerte sind amtlich und gelten für das ganze UK. Die Jahreszahl von etwa £3,6 Mrd. ist eine eigene Rechnung (£70 Mio. × 52). In Tabelle A6 ('Detailed household expenditure by gross income decile group') geben das neunte und das oberste Einkommensdezil je £4,50 pro Woche für Haushaltstextilien aus, fast doppelt so viel wie der Durchschnitt (£2,40).
- **Wahrheits-Check:** *bestätigt*. Tabelle A1 (Zeilen 5.2 und 5.2.2) und Tabelle A6 (Zeile 5.2: 1.90 | 1.20 | 1.40 | 3.00 | 1.70 | 2.00 | 2.00 | 2.20 | 4.50 | 4.50 | 2.40) aus der Original-xlsx bestätigt. Wortlaut um die zwei fehlenden Spalten von 5.2.2 ergänzt.

#### 4A-05

✅ BELEGT · Angle: Markt

**Dunelm beziffert seinen adressierbaren Markt auf etwa £24 Mrd. Gemeint ist laut GlobalData der kombinierte UK-Markt für Homewares und Möbel ohne Küchen- und Badmöbel (12 Monate bis Juni 2025, inkl. MwSt.).**

> “Total addressable market¹ £ 24 bn … ¹ Based on GlobalData UK combined homewares and furniture markets, excluding kitchen cabinetry and bathroom furniture, for the 12 months to June 2025, including VAT.”

- **Quelle:** [Dunelm Group plc – Annual Report 2025 (Investor-Seite)](https://corporate.dunelm.com/investors/results-reports-and-presentations/annual-report-2025/)
- **Datum der Quelle:** 2025 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Geschäftsbericht eines börsennotierten Unternehmens mit klarer Quellenangabe (GlobalData) und Abgrenzung. Einschränkungen: Der Markt ist sehr breit (alle Homewares plus Möbel), es ist keine Zahl für Bettwaren oder Bettdecken. Die Methodik von GlobalData ist nicht öffentlich, und auf der Seite steht kein genaues Veröffentlichungsdatum.
- **Wahrheits-Check:** *bestätigt*. Investor-Seite per WebFetch geprüft: '£ 24 bn' und Fußnote stehen dort wörtlich. Ein Veröffentlichungsdatum gibt die Seite nicht an.

#### 4A-06

✅ BELEGT · Angle: Markt

**Dunelm hält laut GlobalData 7,9 % am kombinierten UK-Markt für Homewares und Möbel (12 Monate bis Juni 2026, +0,1 Prozentpunkte zum Vorjahr).**

> “increasing market share by 10bps year-on-year to 7.9% … GlobalData UK combined homewares and furniture markets, excluding kitchen cabinetry and bathroom furniture, for the 12 months to June 2026. Market share for the 12 months to June 2025 was 7.8% (restated by GlobalData UK from 7.9%)”

- **Quelle:** [Dunelm Group plc – Preliminary Results for the 52 weeks ended 27 June 2026 (RNS)](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle Pflichtmitteilung (RNS) mit Marktdefinition in der Fußnote; den Vorjahreswert hat GlobalData von 7,9 % auf 7,8 % korrigiert. Einen Marktanteil nur für Homewares oder Bettwaren nennt die Mitteilung nicht. Aus £1.825,5 Mio. Umsatz / 7,9 % ergäbe sich rechnerisch ein Markt von etwa £23 Mrd. (eigene Rechnung; Abgrenzungen wie inkl./exkl. MwSt. können abweichen).
- **Wahrheits-Check:** *bestätigt*. RNS per WebFetch und curl gelesen; Satz und Fußnote wörtlich bestätigt. Fußnotentext in den Wortlaut aufgenommen.

#### 4A-10

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut IBISWorld liegt der Umsatz der UK-Branche 'Household Textile & Soft Furnishing Manufacturing' bei etwa £2,6 Mrd. und ist über die fünf Jahre bis 2025-26 nicht gewachsen.**

> “Over the five years through 2025-26, industry revenue has remained flat at £2.6 billion, with no growth and profit margins hitting an estimated 15.5% in 2025-26. However, industry revenue is projected to climb at a compound annual rate of 2.3% in the current year, indicating a slow recovery is underway.”

- **Quelle:** [IBISWorld – Household Textile & Soft Furnishing Manufacturing in the UK (Branchenseite)](https://www.ibisworld.com/united-kingdom/industry/household-textile-soft-furnishing-manufacturing/755/)
- **Datum der Quelle:** 2026-03-31 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Gemessen wird die Herstellung, nicht der Einzelhandel. Die Branche umfasst laut Seite 'Bedding, Canvas goods and Technical textiles'. Laut IBISWorld machen Importe einen hohen Anteil am Branchenumsatz aus. Die Methodik ist nicht öffentlich.
- **Wahrheits-Check:** *korrigiert*. Seite per curl gelesen; Wortlaut bestätigt und um den Folgesatz ergänzt. Datum korrigiert: Laut Seitenmetadaten datePublished 2026-03-31 ('March 2026').

#### 4A-11

✅ BELEGT · Angle: Markt

**UK-Hersteller verkauften 2025 gefüllte Bettwaren (laut ONS-Bezeichnung inkl. Quilts/Eiderdowns, Kissen, Sitzkissen, Polster) für zusammen etwa £361 Mio.: £318,2 Mio. mit anderer Füllung als Federn/Daunen und £43,3 Mio. mit Federn/Daunen.**

> “13922499 (CN 94049090), Articles of bedding filled other than with feathers or down, INCLUDING: quilts and eiderdowns, cushions, pouffes, pillows, EXCLUDING: mattresses, sleeping bags | Value £000's | … 2024: 307344 | 2025: 318166 // 13922493 (CN 94049010), Articles of bedding of feathers or down, INCLUDING: quilts and eiderdowns, cushions, pouffes, pillows … | Value £000's | … 2024: 36431 | 2025: 43329”

- **Quelle:** [Office for National Statistics – UK Manufacturers' Sales by Product Survey (ProdCom) 2025, Table 5 (prodcomfinal25.xlsx)](https://www.ons.gov.uk/businessindustryandtrade/manufacturingandproductionindustry/datasets/ukmanufacturerssalesbyproductprodcom)
- **Datum der Quelle:** 2026-07-24 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** ProdCom-Herstellerbefragung UK; laut Cover Sheet 'estimated totals … for 2025, revised estimates for 2024'
- **Einordnung/Einschränkung:** Amtliche Herstellerstatistik. Einschränkungen: Erfasst sind Umsätze inländischer Hersteller, keine Einzelhandelswerte und keine Importe. Kissen, Sitzkissen und Polster sind mit enthalten. 2025 ist eine vorläufige Schätzung. Zur Abgrenzung: Die ONS-Bezeichnung schließt Quilts und Eiderdowns ausdrücklich ein. Der mitgenannte CN-Code 94049090 schließt Bettdecken laut HMRC-Warenverzeichnis seit der Tarifrevision 2022 jedoch aus (Bettdecken: CN 9404 40), die Abgrenzung ist also nicht völlig eindeutig. Zum Vergleich 2024: £343,8 Mio. (eigene Summe), also etwa +5 %.
- **Wahrheits-Check:** *korrigiert*. prodcomfinal25.xlsx selbst heruntergeladen: Werte 2024/2025 und Cover Sheet bestätigt. Korrigiert: Die nicht belegte Aussage 'ein großer Teil der Bettdecken wird importiert' habe ich entfernt; die HMRC-Importe von Bettdecken lagen 2025 nur bei etwa £43 Mio. (siehe 4A-V05). Hinweis auf die CN-Abgrenzung ergänzt.

#### 4A-12

⚠️ EINGESCHRÄNKT · Angle: Markt

**Die National Bed Federation, der Verband der UK-Hersteller von Betten und ihrer Zulieferer, gibt an, dass ihre Mitglieder etwa 75 % des 'UK bedding'-Umsatzes stellen. Mit 'bedding' sind dort Betten und Matratzen gemeint, nicht Bettdecken.**

> “The National Bed Federation is the recognised trade association representing UK manufacturers of beds and their suppliers. Founded in 1912, its members today account for about 75% of the total UK bedding turnover.”

- **Quelle:** [National Bed Federation – Startseite/About; NBF Sales Tracker](https://www.bedfed.org.uk/)
- **Datum der Quelle:** unbekannt · **Typ:** Fachgesellschaft/Charity
- **Einordnung/Einschränkung:** Selbstangabe des Branchenverbands, ohne Datum und ohne Marktvolumen. Laut Sales-Tracker-Seite (https://www.bedfed.org.uk/market-intelligence/nbf-sales-tracker/) umfasst der Tracker 'mattresses, bed sets, bases, bedsteads, sofa beds, headboards etc.'; die Daten sind nur für Mitglieder zugänglich. Dieselbe Seite rechnet mit Mitgliedern, die '50% of UK manufacturing output by units and 70% by value' stellen. Das passt nicht zur 75-%-Angabe der Startseite. Folge: 'UK bedding market'-Zahlen meinen oft Betten und Matratzen. Bettdecken-Zahlen nie ohne Prüfung der Abgrenzung übernehmen.
- **Wahrheits-Check:** *korrigiert*. Startseite und Sales-Tracker-Seite per curl gelesen. Wortlaut bestätigt und um 'representing UK manufacturers of beds and their suppliers' ergänzt. Widersprüchliche Repräsentativitätsangabe (50 % nach Stückzahl, 70 % nach Wert) in der Begründung ergänzt.

#### 4A-13

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut einer GlobalData-Umfrage 2026 unter 2.000 national repräsentativ ausgewählten UK-Verbrauchern hat über die Hälfte in den letzten 12 Monaten Schlafzimmertextilien gekauft; am höchsten ist der Anteil bei 16- bis 24-Jährigen.**

> “The report focuses on overall bedroom textiles products and its five sub-categories: Pillows & duvets, Covers, Blankets, Sheets and Bedroom accessories. Consumer data is based on our 2026 UK bedroom textiles survey, using a panel of 2,000 nationally representative consumers. … Over half of UK consumers have purchased bedroom textiles products in the last 12 months, with the highest purchasing penetration among 16-24 year-olds.”

- **Quelle:** [GlobalData – United Kingdom (UK) Home: Bedroom Textiles – Market Trends, Analysis, Consumer Dynamics and Spending Habits (Report-Seite, Code GDRT260006CPUK-ST)](https://www.globaldata.com/store/report/uk-bedroom-textiles-market-analysis/)
- **Datum der Quelle:** 2026-07-30 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** n=2.000, national repräsentatives Panel, UK, 2026 (Feldzeit nicht genannt)
- **Einordnung/Einschränkung:** Seriöses Institut mit genannter Stichprobe, aber Paywall: Genauer Prozentwert und Feldzeit sind nicht öffentlich. 'Bedroom textiles' umfasst fünf Unterkategorien (Pillows & duvets, Covers, Blankets, Sheets, Bedroom accessories); der Wert gilt also nicht speziell für Bettdecken.
- **Wahrheits-Check:** *korrigiert*. Seite per curl gelesen; ?p=1907364 leitet auf die kanonische URL weiter, die ich eingesetzt habe. Wortlaut und 'Published: July 30, 2026' bestätigt, Report-Code und Unterkategorien ergänzt.

#### 4A-V03

⚠️ EINGESCHRÄNKT · Angle: Markt

**Am reinen UK-Homewares-Markt (ohne Möbel) hatte Dunelm laut GlobalData im Kalenderjahr 2023 einen Anteil von 11,3 % (2022: 10,8 %). In den geprüften Mitteilungen ab September 2024 weist Dunelm nur noch den Anteil am kombinierten Markt für Homewares und Möbel aus.**

> “Homewares market share 15 11.3% +60bps Furniture market share 15 2.1% +10bps Combined market share 15 7.6% +50bps … 15 GlobalData UK homewares and furniture markets, January 2023 to December 2023. Furniture excludes kitchen and bathroom furniture. // RNS 15.02.2023: In homewares, our market share increased by 160bps to 10.8%”

- **Quelle:** [Dunelm Group plc – Interim Results for the 26 weeks ended 30 December 2023 (RNS, FCA NSM); Interim Results for the 26 weeks ended 31 December 2022 (RNS, FCA NSM)](https://data.fca.org.uk/artefacts/NSM/RNS/5066499.html)
- **Datum der Quelle:** 2024-02-14 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärquelle mit GlobalData als Datenbasis, aber veraltet (Stand 2023). Ein aktueller reiner Homewares-Anteil ist öffentlich nicht verfügbar; die Prelims vom 11.09.2024 und 08.09.2026 sowie die Interims vom 10.02.2026 nennen nur den kombinierten Anteil. Zweite Fundstelle: https://data.fca.org.uk/artefacts/NSM/RNS/4674663.html (15.02.2023).
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. Beide RNS per curl gelesen. Schließt die Lücke zum reinen Homewares-Anteil von Dunelm, allerdings nur bis 2023; die in der Presse zitierten 11,5 % habe ich nicht gefunden.

#### 4A-V05

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut HMRC-Außenhandelsdaten importierte das UK 2025 Bettdecken, Steppdecken und Tagesdecken (CN 9404 40, alle Füllungen) im Wert von rund £43 Mio. (2024: rund £35 Mio.); knapp die Hälfte (£20,8 Mio.) kam aus China.**

> “CN 94044010 'Quilts, bedspreads, eiderdowns and duvets "comforters", filled with feathers or down': 2024 £6,8 Mio., 2025 £9,3 Mio.; CN 94044090 'Quilts, bedspreads, eiderdowns and duvets "comforters" (excl. filled with feathers or down)': 2024 £28,0 Mio., 2025 £34,1 Mio. [eigene Summe der Monatswerte, EU- und Nicht-EU-Importe, OTS]; größte Herkunftsländer 2025: China £20,75 Mio., Pakistan £4,84 Mio., Indien £3,92 Mio.”

- **Quelle:** [HM Revenue & Customs – uktradeinfo, Overseas Trade Statistics (OTS-API)](https://api.uktradeinfo.com/OTS)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Monatliche Importwerte 01/2024–12/2025, FlowType 1 (EU) und 3 (Nicht-EU)
- **Einordnung/Einschränkung:** Amtliche Handelsdaten, aber eigene Summierung über die API; einzelne Werte können unterdrückt sein (SuppressionIndex). Es sind Zollwerte, keine Einzelhandelspreise. Tagesdecken sind enthalten, Kissen nicht (CN 9404 90). Ein Vergleich mit den PRODCOM-Herstellerumsätzen (£361 Mio. inkl. Kissen und Polster, 4A-11) ist wegen der unterschiedlichen Abgrenzung nicht sauber möglich. Die frühere Aussage, der Großteil des Marktes werde importiert, lässt sich damit jedenfalls nicht stützen.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. OTS-API selbst abgefragt (Commodity- und Country-Endpunkte zur Code- und Länderprüfung); schließt die Lücke zu den HMRC-Importdaten. Hinweis: Seit der HS-Revision 2022 laufen Bettdecken unter 9404 40, nicht mehr unter 9404 90.

### 2 Wachstum

#### 4A-04

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut ONS stiegen die durchschnittlichen UK-Haushaltsausgaben für Schlafzimmertextilien inkl. Bettdecken und Kissen von £0,80 (FYE 2023) über £0,90 (FYE 2024) auf £1,30 pro Woche (FYE 2025).**

> “FYE 2023: 5.2.1 | Bedroom textiles, including duvets and pillows | 0.8 | 24 | 310 | 14.8; FYE 2024: … | 0.90 | 26 | 290 | 12.6; FYE 2025: … | 1.30 | 38 | 380 | 15.6”

- **Quelle:** [Office for National Statistics – Family Spending Workbook 1, Table A1 (Editionen FYE 2023, FYE 2024, FYE 2025)](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** LCF, 4.460 (FYE 2023), 4.210 (FYE 2024) bzw. 5.000 (FYE 2025) Haushalte UK; 290–380 Haushalte mit Ausgaben in dieser Kategorie
- **Einordnung/Einschränkung:** Die Werte stehen so in den drei offiziellen Editionen. Als Trend sind sie aber schwach: Standardfehler 12,6–15,6 %, nur 290–380 Haushalte mit Ausgaben in der Kategorie, laufende Preise (nicht inflationsbereinigt). Dazu kommen Methodikbrüche: Ab FYE 2024 wird mit Census-2021-Daten gewichtet, ab FYE 2025 gilt eine neue Methode für die Standardfehler. Die Editionen FYE 2023 und FYE 2024 wurden am 11.06.2026 korrigiert; das betraf die Standardfehler. Der Sprung auf £1,30 kann zum Teil Zufallsschwankung sein. Nicht als 'Markt wächst um 44 %' kommunizieren.
- **Wahrheits-Check:** *korrigiert*. Alle drei xlsx selbst geladen, Werte exakt bestätigt. Korrigiert: Die Begründung nannte eine Änderung der 'Äquivalenzskala'. Diese betrifft laut 'Background notes' nur die äquivalisierten Einkommenstabellen, nicht Tabelle A1. Relevant sind stattdessen die neue Standardfehler-Methode (FYE 2025), die Census-2021-Gewichtung (ab FYE 2024) und die Korrektur vom 11.06.2026 (Blatt 'Correction'). Stichprobengrößen ergänzt.

#### 4A-07

⚠️ EINGESCHRÄNKT · Angle: Markt

**GlobalData erwartet, dass der UK-Homewares-Markt von 2024 bis 2029 um durchschnittlich 2,2 % pro Jahr auf £16,0 Mrd. wächst.**

> “The homewares market is projected to grow at a compound annual growth rate (CAGR) of 2.2% between 2024 and 2029, reaching £16.0bn by the end of the period.”

- **Quelle:** [GlobalData – United Kingdom (UK) Homewares Market Analysis by Categories, Revenue, Consumer Trends, Key Players and Forecast to 2029 (Report-Seite, Code GDRT250000CSUK-ST)](https://www.globaldata.com/store/report/uk-homewares-retail-market-analysis/)
- **Datum der Quelle:** 2025-07-31 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Prognose eines etablierten Marktforschungsinstituts. Basiswert 2024, Methodik und Kategorieaufteilung liegen hinter der Paywall. Die Prognose gilt für Homewares insgesamt, nicht für Bettdecken; auf der öffentlichen Seite kommen Textilien nicht vor. Eine neuere Ausgabe mit Prognose bis 2030 habe ich nicht gefunden.
- **Wahrheits-Check:** *bestätigt*. Seite per WebFetch und curl geprüft: Wortlaut, 'Published: July 31, 2025' und Report-Code bestätigt.

#### 4A-09

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut GlobalData sollen die Absatzmengen im UK-Homewares-Markt ab 2026 wieder wachsen; Haupttreiber des Umsatzwachstums bleibt die Inflation.**

> “Volumes are forecast to begin growing from 2026 onwards, although inflation will continue to be the primary driver of sales growth.”

- **Quelle:** [GlobalData – UK Homewares Market … Forecast to 2029 (Report-Seite)](https://www.globaldata.com/store/report/uk-homewares-retail-market-analysis/)
- **Datum der Quelle:** 2025-07-31 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Qualitative Prognose ohne veröffentlichte Mengenzahlen. Wichtig für die Einordnung: Das nominale Wachstum von etwa 2 % ist überwiegend Preiswachstum, nicht Mengenwachstum.
- **Wahrheits-Check:** *korrigiert*. Wortlaut vervollständigt ('of sales growth') und kanonische URL eingesetzt.

#### 4A-35

✅ BELEGT · Angle: Markt

**Dunelm steigerte den Umsatz im Geschäftsjahr bis 27.06.2026 um 3,1 % auf £1.825 Mio. und wuchs nach eigener Aussage schneller als der kombinierte Markt für Homewares und Möbel.**

> “We delivered a solid performance in FY26, with total sales up 3.1% to £1,825m (FY25: £1,771m). … Overall, we continued to outperform the combined homewares and furniture market, increasing market share by 10bps year-on-year to 7.9%”

- **Quelle:** [Dunelm Group plc – Preliminary Results for the 52 weeks ended 27 June 2026 (RNS)](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle Zahl. Eine Marktwachstumsrate nennt die Mitteilung nicht. Rechnerisch (Umsatz / Marktanteil: £1.825,5 Mio./7,9 % vs. £1.771,0 Mio./7,8 %) ergibt sich ein Marktwachstum von etwa +1,8 %. Wegen der gerundeten Anteile liegt die Spanne grob bei 0,5–3 %. Das ist eine eigene Ableitung.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Zahlen im RNS bestätigt. Korrigiert: Die frühere Ableitung 'Gesamtmarkt knapp unter 3 % gewachsen' rechnet sich nicht; richtig sind etwa 1,8 % (Spanne 0,5–3 %).

#### 4A-36

⚠️ EINGESCHRÄNKT · Angle: Markt

**Der wöchentliche Durchschnittsumsatz der ONS-Warengruppe 'Household goods' in Großbritannien lag 2025 nominal etwa 3,1 % über 2024 (£1,52 Mrd. vs. £1,47 Mrd. pro Woche).**

> “MCIW … Household goods … Average Weekly Retail Sales in £thousands, Great Britain [Monatswerte 2024: 1.335.755–1.817.705; 2025: 1.400.390–1.922.554]”

- **Quelle:** [Office for National Statistics – Retail sales pounds data (poundsdata.xlsx, Tabelle MCIW)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/datasets/poundsdatatotalretailsales)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** 56 große Händler plus Hochrechnung, Großbritannien
- **Einordnung/Einschränkung:** Eigene Rechnung aus amtlichen Werten, gewichtet mit der Wochenzahl: 2025 hat im ONS-Kalender 53 Wochen (£80,44 Mrd.), 2024 hat 52 Wochen (£76,57 Mrd.). Das ergibt £1.517,8 Mio. vs. £1.472,5 Mio. pro Woche (+3,1 %). Nominal, nicht inflationsbereinigt; die Warengruppe ist breit. Nur als Rahmen für das Marktwachstum verwenden.
- **Wahrheits-Check:** *bestätigt*. poundsdata.xlsx selbst geladen; Rechnung inkl. 53 Wochen 2025 (Januar 2025 = 5-Wochen-Periode laut Note 2) exakt nachvollzogen. Spannen im Wortlaut präzisiert.

#### 4A-V04

✅ BELEGT · Angle: Markt

**Laut Dunelm kam das Wachstum im ersten Halbjahr GJ26 (bis 27.12.2025) vor allem aus Kernkategorien, darunter Heimtextilien wie Bettwaren und Kissen. Die Absatzmengen blieben etwa stabil, die durchschnittlichen Artikelwerte stiegen durch Kategorie- und Produktmix, nicht durch höhere Listenpreise.**

> “Volumes in the first half were broadly stable year-on-year whilst average item values increased, driven by category and product mix, rather than headline retail prices. Growth across the half was again driven by core categories, coming from our heritage ranges in soft textiles, including bedding and cushions, and also more recent areas of specialism such as lighting.”

- **Quelle:** [Dunelm Group plc – Interim Results for the 26 weeks ended 27 December 2025 (RNS, FCA National Storage Mechanism)](https://data.fca.org.uk/artefacts/NSM/RNS/46870cf2-4dbf-438c-a8a4-65d3316387a1.html)
- **Datum der Quelle:** 2026-02-10 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle qualitative Aussage ohne Kategorieumsätze. 'Bedding' umfasst bei Dunelm Bettwäsche und Bettdecken; ein Wert speziell für Bettdecken fehlt. Zeigt, dass Bettwaren beim Marktführer zu den Wachstumstreibern gehören.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Wortlaut im Interim-RNS per curl bestätigt.

### 3 Online-Anteil

#### 4A-08

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut GlobalData-Prognose wächst der Online-Kanal im UK-Homewares-Markt bis 2029 mit 3,2 % pro Jahr, der stationäre Kanal mit 1,7 %.**

> “The online channel will outpace offline growth in every year of the forecast period, growing at a CAGR of 3.2% versus 1.7%, with retailers that have strong online propositions like Amazon and Dunelm well-placed to maintain their forward momentum in the sector.”

- **Quelle:** [GlobalData – UK Homewares Market … Forecast to 2029 (Report-Seite, Code GDRT250000CSUK-ST)](https://www.globaldata.com/store/report/uk-homewares-retail-market-analysis/)
- **Datum der Quelle:** 2025-07-31 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Prognose eines seriösen Instituts, Details hinter der Paywall. Den aktuellen Online-Anteil im Homewares-Markt nennt die öffentliche Seite nicht. Gilt für alle Homewares, nicht speziell für Bettwaren.
- **Wahrheits-Check:** *korrigiert*. Die URL ?p=4332478 ist dieselbe Seite; ich habe die kanonische URL eingesetzt. Wortlaut auf den vollständigen Satz erweitert (inkl. Nennung von Amazon und Dunelm).

#### 4A-14

⚠️ EINGESCHRÄNKT · Angle: Markt

**In der GlobalData-Umfrage 2026 (n=2.000, UK) ist Amazon der meistgenutzte Händler für Schlafzimmertextilien, vor Dunelm und ASDA, und hat die höchste Conversion-Rate. Für die Mehrheit ist der Preis das wichtigste Kaufkriterium.**

> “Amazon is the most popular retailer for purchasing bedroom textiles products, followed by Dunelm and ASDA. … Amazon holds the highest conversion rate in the overall bedroom textiles market followed by Dunelm … A majority of respondents cited price as the driver of choice for their bedroom textiles purchases”

- **Quelle:** [GlobalData – UK Home: Bedroom Textiles – Market Trends, Analysis, Consumer Dynamics and Spending Habits (Report-Seite)](https://www.globaldata.com/store/report/uk-bedroom-textiles-market-analysis/)
- **Datum der Quelle:** 2026-07-30 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** n=2.000, national repräsentatives UK-Panel, 2026
- **Einordnung/Einschränkung:** Nur eine Rangfolge ohne veröffentlichte Prozentwerte (Paywall). Gemessen wird, wo Verbraucher kaufen, nicht der Umsatzanteil. Trotzdem der beste öffentliche Hinweis, dass Amazon im Bettwaren-Kanal eine zentrale Rolle spielt.
- **Wahrheits-Check:** *korrigiert*. Wortlaut bestätigt und um den Satz zur Conversion-Rate ergänzt; kanonische URL eingesetzt.

#### 4A-21

✅ BELEGT · Angle: Markt

**In Großbritannien wurden 2025 laut ONS 27,5 % aller Einzelhandelsumsätze online gemacht (2019: 19,2 %; Höchststand 2021: 30,7 %).**

> “'Title','Internet sales as a percentage of total retail sales (ratio) (%)' 'CDID','J4MC' … '2019','19.2' '2020','28.1' '2021','30.7' '2022','26.6' '2023','26.7' '2024','27.1' '2025','27.5'”

- **Quelle:** [Office for National Statistics – Time series J4MC: Internet sales as a percentage of total retail sales (ratio) (%), Dataset DRSI](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/j4mc/drsi)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry (Monthly Business Survey), Großbritannien
- **Einordnung/Einschränkung:** Amtliche Zeitreihe nach Umsatzwert. Einschränkungen: Sie gilt nur für Großbritannien (ohne Nordirland), nicht für das ganze UK. J4MC ist die nicht saisonbereinigte Reihe (Tabelle ISCPNSA3 der Internet-Referenztabellen).
- **Wahrheits-Check:** *korrigiert*. Offizielles CSV der Serie selbst geladen (Release 18-09-2026, nächster Termin 23.10.2026); alle Jahreswerte bestätigt. Dass J4MC nicht saisonbereinigt ist, habe ich über die Internet-Referenztabellen bestätigt. Entfernt: die Angabe zur Behandlung von Click & Collect, weil ich sie in den geprüften ONS-Dokumenten nicht gefunden habe.

#### 4A-22

✅ BELEGT · Angle: Markt

**Der saisonbereinigte Online-Anteil am Einzelhandel in Großbritannien stieg laut ONS von 28,4 % im Juli 2026 auf 28,8 % im August 2026.**

> “The total spend (the sum of in-store and online sales) rose by 1.3% over the month. As a result, the proportion of sales made online rose from 28.4% in July 2026 to 28.8% in August 2026.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: August 2026 (Statistical bulletin)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/august2026)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry, Großbritannien; Rücklaufquote August 2026: 56,7 % (92,3 % Umsatzabdeckung)
- **Einordnung/Einschränkung:** Neuester amtlicher Monatswert; der nächste Release folgt am 23.10.2026. Es ist der saisonbereinigte Wert (Serie MS6Y, Tabelle ISCPSA3: 28.4 / 28.8). Der nicht bereinigte Wert J4MC lag im August 2026 bei 27,3 %. Beide nicht verwechseln. Gilt nur für Großbritannien.
- **Wahrheits-Check:** *bestätigt*. Bulletin per curl gelesen: Satz, Release- und Folgedatum sowie Rücklaufquote bestätigt. MS6Y = 28,8 (Aug 2026) und 28,4 (Jul 2026) in der xlsx gegengeprüft.

#### 4A-24

⚠️ EINGESCHRÄNKT · Angle: Markt

**Bei den Geschäften der ONS-Gruppe 'Household goods stores' (Großbritannien) lag der saisonbereinigte Online-Anteil im August 2026 bei 28,8 % (August 2025: 25,4 %; Durchschnitt 2019 etwa 14,5 %).**

> “ISCPSA3 - INTERNET SALES INDEX: VALUE SEASONALLY ADJUSTED INTERNET SALES AS A PROPORTION OF ALL RETAILING … Household goods stores [Note 2] (MS77) … 2025 Aug 25.4 … 2026 Aug 28.8”

- **Quelle:** [Office for National Statistics – Retail Sales Index internet sales (internetreferencetables.xlsx); Retail Sales Index categories and their percentage weights (indexcatweights2025.xlsx, 27.03.2026)](https://www.ons.gov.uk/file?uri=/businessindustryandtrade/retailindustry/datasets/retailsalesindexinternetsales/current/internetreferencetables.xlsx)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry, Großbritannien
- **Einordnung/Einschränkung:** Amtliche Werte; den Mittelwert für 2019 habe ich aus den zwölf Monatswerten berechnet (14,53 %). Wichtige Einschränkung: Die ONS ordnet Umsätze nach Geschäftstyp zu, nicht nach Produkt. Laut Gewichtungstabelle 2025 umfasst 'Household goods stores' (6,91 % des Einzelhandels) Eisenwaren/Farben/Glas (47.52), Elektro-Haushaltsgeräte (47.54), Möbel/Leuchten/Haushaltsartikel (47.59) sowie Audio/Video. Reine Textilgeschäfte (47.51) gehören zur Bekleidungsgruppe. Versand- und Internethändler ('Mail order houses (including internet retailers)', 12,64 %) fallen unter 'Non-store retailing' (13,28 %). Den tatsächlichen Online-Anteil bei Bettwaren gibt diese Kennzahl daher nicht wieder; eine amtliche Zahl dazu gibt es nicht.
- **Wahrheits-Check:** *korrigiert*. Beide xlsx selbst geladen: MS77 25,4 (Aug 2025) und 28,8 (Aug 2026) sowie den 2019-Mittelwert bestätigt. Korrigiert: Die Begründung beschrieb die Gruppe als 'Möbel- und Heimtexgeschäfte'. Laut ONS-Gewichtungstabelle sind reine Textilgeschäfte aber nicht enthalten, dafür Eisenwaren und Elektro. Das nicht gefundene ONS-Zitat 'retailers that do not have a store presence' habe ich durch die Bezeichnung aus der Gewichtungstabelle ersetzt.

#### 4A-26

✅ BELEGT · Angle: Markt

**Dunelm, nach eigener Aussage der führende UK-Homewares-Händler, machte im Geschäftsjahr bis 27.06.2026 42 % seines Umsatzes digital (Vorjahr 40 %). Darin enthalten sind Heimlieferung, Click & Collect und Tablet-Käufe im Laden.**

> “Digital participation increased by a further 2ppts to 42%, leveraging the benefits of investment in digital capabilities over time. … Digital sales include home delivery, Click & Collect and tablet-based sales in store.”

- **Quelle:** [Dunelm Group plc – Preliminary Results for the 52 weeks ended 27 June 2026 (RNS)](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle Pflichtmitteilung. Einschränkung: Dunelm fasst 'digital' weiter als die ONS (Click & Collect und Tablet-Käufe im Laden zählen mit). Gilt für das gesamte Dunelm-Sortiment, nicht nur für Bettwaren. Im H1 GJ26 waren es laut Interim-RNS vom 10.02.2026 41 %, im Q4 GJ26 45 % (siehe 4A-V02). Laut RNS hat die App '740k downloads'.
- **Wahrheits-Check:** *korrigiert*. Wortlaut, Definition, die 41 % (H1) und '740k downloads' in beiden RNS bestätigt. Formulierung angepasst: Dunelm nennt sich 'the UK's leading homewares retailer'; 'der größte' war eine Zuspitzung.

#### 4A-27

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut ECDB-Modellschätzung lag der Online-Anteil im UK-Möbelmarkt 2025 bei 30–35 %.**

> “The UK Furniture E-Commerce Market reached an online share of 30-35% in 2025. This e-commerce market share measures what percentage of revenues are generated through online channels. The online share is expected to reach 30-35% in 2026.”

- **Quelle:** [ECDB (ecommerceDB) – eCommerce market United Kingdom: Furniture (Sample Data)](https://ecdb.com/resources/sample-data/market/gb/furniture)
- **Datum der Quelle:** unbekannt · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Modellschätzung eines kommerziellen Datenanbieters, nur als Spanne und ohne Datum veröffentlicht; gemeint ist der Möbelmarkt, nicht Bettwaren. Die Seite wirkt schablonenhaft: Dieselbe Spanne '30-35%' steht auch beim Label '2024', für die Prognose 2026 und sogar als 'e-commerce growth rate' 2025, bei einem E-Commerce-Umsatz von US$10.569 Mio. Die URL ecommercedb.com/markets/gb/bedding leitet auf dieselbe Möbelseite weiter. Nur als sehr grober Vergleichswert brauchbar, nicht in Ads.
- **Wahrheits-Check:** *korrigiert*. Seite per curl gelesen; Wortlaut bestätigt und um den Prognosesatz ergänzt. Begründung um die schablonenhaften, widersprüchlichen Seitenwerte und die Weiterleitung der Bedding-URL ergänzt.

#### 4A-V02

✅ BELEGT · Angle: Markt

**Dunelms Digitalanteil stieg im GJ26 von Quartal zu Quartal: Q1 40 %, Q2 42 %, Q3 43 %, Q4 (bis 27.06.2026) 45 %; im Gesamtjahr waren es 42 %.**

> “Quarterly analysis: 52 weeks to 27 June 2026 Q1 Q2 H1 Q3 Q4 H2 FY … Digital % total sales 2 40% 42% 41% 43% 45% 44% 42% … 52 weeks to 28 June 2025 … Digital % total sales 2 37% 40% 39% 41% 42% 42% 40%”

- **Quelle:** [Dunelm Group plc – Preliminary Results for the 52 weeks ended 27 June 2026 (RNS), Quarterly analysis](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle Zahlen nach Dunelms eigener Definition (inkl. Click & Collect und Tablet-Käufen im Laden). Gilt für das gesamte Sortiment.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. Damit ist der Q4-Digitalanteil von 45 %, der bisher nur aus Sekundärquellen bekannt war, an der Primärquelle bestätigt.

### 1 Marktgröße (Mythos-Check)

#### 4A-15

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Angabe, der UK-Bettwarenmarkt erreiche 2026 '£4,2–4,5 Mrd.' (45 % Matratzen, 30 % Bettwäsche, 25 % Bettdecken/Kissen), stammt aus einem KI-generierten Report ohne nachvollziehbare Quelle.**

> “Created by SourceReady AI agent · 2026-4-15 … The UK bedding market in 2026 is projected to reach £4.2 billion to £4.5 billion … based on current market intelligence and trade data through early 2026 … Mattresses 45% … Bed Linen 30% … Duvets & Pillows 25%”

- **Quelle:** [SourceReady – UK Bedding Market Report 2026](https://www.sourceready.com/report/detail/uk-bedding-market-report-2026)
- **Datum der Quelle:** 2026-04-15 · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Von einem 'AI agent' erstellt, ohne Methodik oder Primärquelle. Der Anbieter widerspricht sich selbst: Sein UK-Sleep-Products-Report nennt £480 Mio. für 'Pillows & Bedding' und £1,15 Mrd. für Matratzen (2025, siehe 4A-16). 25 % bzw. 45 % von £4,2–4,5 Mrd. wären dagegen etwa £1,05–1,1 Mrd. bzw. £1,9–2,0 Mrd. Die im selben Report genannte '3.2% CAGR in the home textiles sector' ist ebenfalls ohne Quelle. Nicht verwenden.
- **Wahrheits-Check:** *bestätigt*. Seite per curl gelesen; Wortlaut, KI-Kennzeichnung und Datum bestätigt. Unbelegtheit bestätigt.

#### 4A-16

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Angabe 'Pillows & Bedding' im UK = £480 Mio. (2025) bzw. £510 Mio. (2026) stammt aus einem KI-generierten Report und widerspricht anderen Zahlen desselben Anbieters.**

> “Created by SourceReady AI agent · 2026-4-15 … Mattresses £1.15 billion £1.21 billion +2.5% Pillows & Bedding £480 million £510 million +6.3% Sleep Tech & Apps £320 million £390 million +21.9% Total Core Market £1.95 billion £2.11 billion +8.2%”

- **Quelle:** [SourceReady – UK Sleep Products Market Report 2026](https://www.sourceready.com/report/detail/uk-sleep-products-market-report-2026)
- **Datum der Quelle:** 2026-04-15 · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** KI-generiert, ohne Methodik, und um mehr als den Faktor 2 im Widerspruch zu 4A-15. Der Wert liegt weit unter dem ONS-Näherungswert für Konsumausgaben (etwa £2 Mrd. für Schlafzimmertextilien, 4A-02) und nur leicht über den Ab-Werk-Umsätzen der UK-Hersteller (etwa £361 Mio., 4A-11). Nicht verwenden.
- **Wahrheits-Check:** *bestätigt*. Seite per curl gelesen, Tabellenwerte wörtlich bestätigt. Unbelegtheit bestätigt.

#### 4A-18

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Angabe, Dunelm habe 2026 '10–12 %' am gesamten UK-Homewares-Markt, steht ohne Quelle in einem KI-Report. Dunelm selbst nannte zuletzt 11,3 % am reinen Homewares-Markt für das Kalenderjahr 2023 (GlobalData). Seitdem weist das Unternehmen nur den Anteil am kombinierten Markt für Homewares und Möbel aus (7,9 %, 12 Monate bis Juni 2026).**

> “Dunelm maintains market dominance with an estimated 10-12% share of the total homewares market, leveraging its extensive physical store network and dual-tier 'Value' and 'Dorma' product ranges.”

- **Quelle:** [SourceReady – UK Bedding Market Report 2026](https://www.sourceready.com/report/detail/uk-bedding-market-report-2026)
- **Datum der Quelle:** 2026-04-15 · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** KI-Report ohne Herkunftsangabe; einen aktuellen reinen Homewares-Anteil für 2026 gibt es öffentlich nicht. Die Spanne ist nicht abwegig: In seinen RNS nannte Dunelm laut GlobalData 10,8 % für 2022 und 11,3 % für 2023 (siehe 4A-V03). Für 2026 ist sie aber nicht belegt.
- **Wahrheits-Check:** *korrigiert*. Wortlaut auf der Seite bestätigt. Aussage korrigiert: Die frühere Formulierung, nur 7,9 % seien belegt, war unvollständig. Ältere reine Homewares-Anteile (10,8 % / 11,3 %) habe ich in Dunelms Primärquellen gefunden (FCA NSM, RNS vom 15.02.2023 und 14.02.2024). Die Einordnung bleibt NICHT_BELEGT, weil SourceReady keine Quelle nennt und es keinen Wert für 2026 gibt.

#### 4A-19

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die per Pressemitteilung verbreitete Zahl, der UK-Markt für Luxus-Bettwaren betrage US$94,2 Mio. und erreiche bis 2031 US$132,9 Mio. (CAGR 4,4 %), ist methodisch nicht nachvollziehbar und in sich widersprüchlich.**

> “U.K. Luxury Bedding Market is estimated to value at US$ 94.2 Million in the year 2024 and is anticipated to reach US$ 132.9 Million by 2031, at a CAGR of 4.4% during forecast period 2024-2031. … With a market size of US$ 94.2 million in 2023 and a CAGR of 4.4% forecasted for the period of 2023 to 2030 …”

- **Quelle:** [Coherent Market Insights via PR Newswire – U.K. Luxury Bedding Market Size to Surpass Around US$ 132.9 Million 2031](https://www.prnewswire.co.uk/news-releases/uk-luxury-bedding-market-size-to-surpass-around-us-132-9-million-2031--recording-a-cagr-of-4-4--report-by-coherentmi-302114512.html)
- **Datum der Quelle:** 2024-04-11 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Typische Pressemitteilung zur Vermarktung eines Reports: keine Methodik, und die Mitteilung widerspricht sich selbst. US$94,2 Mio. stehen einmal für 2024, einmal für 2023; der Prognosezeitraum einmal als 2024–2031, einmal als 2023–2030. Eine spätere Ausgabe nennt US$98,5 Mio. für 2025. Angabe in US-Dollar und nur für das Luxussegment. Nicht verwenden.
- **Wahrheits-Check:** *bestätigt*. PR-Newswire-Seite per curl gelesen: Datum 11.04.2024 und beide widersprüchlichen Passagen bestätigt. Den Folgewert US$98,5 Mio. (2025) → US$135,0 Mio. (2032) habe ich nur im Suchergebnis-Auszug der CoherentMI-Seite gesehen. Unbelegtheit bestätigt.

#### 4A-20

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die im Netz kursierende Zahl, der 'UK Home Bedding Market' habe 2021 US$75,7 Mrd. betragen, ist offensichtlich unplausibel und nicht belegt.**

> “In 2021, the UK Home Bedding Market Size reached USD 75,684.9 Million.”

- **Quelle:** [wiuwi.com Blog – UK Home Bedding Market Top Manufactures Industry Size Growth Analysis](https://wiuwi.com/blogs/112871/UK-Home-Bedding-Market-Top-Manufactures-Industry-Size-Growth-Analysis)
- **Datum der Quelle:** unbekannt · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Die Seite liefert HTTP 404; den Wortlaut gibt es nur noch im Suchergebnis-Auszug. Laut Auszug enthält die Seite auch fremden Vorlagentext ('UK Men's Hair Color Market') und rechnet in sich nicht stimmig (5 % CAGR vs. rechnerisch etwa 4,4 %). Die Zahl entspräche etwa dem 30-Fachen der ONS-Konsumausgaben für alle Haushaltstextilien (etwa £3,6 Mrd./Jahr, 4A-03). Typischer Spam auf Report-Seiten.
- **Wahrheits-Check:** *bestätigt* (Seite vom Prüfer nicht direkt abrufbar). Selbst per curl abgerufen: HTTP 404 (LiteSpeed). Wortlaut nur über den Suchergebnis-Auszug nachvollziehbar, daher selbst_abgerufen=false. Unbelegtheit bestätigt.

### 3 Online-Anteil (Mythos-Check)

#### 4A-17

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Behauptung, reine Onlinehändler würden 2026 'über 35 %' des UK-Bettwarenmarkts erreichen, ist nicht belegt.**

> “The premiumization trend is particularly pronounced, with online-only retailers projected to capture over 35% of the total bedding market by 2026, driven by convenient delivery logistics and industry-standard 'sleep trial' programs.”

- **Quelle:** [SourceReady – UK Bedding Market Report 2026](https://www.sourceready.com/report/detail/uk-bedding-market-report-2026)
- **Datum der Quelle:** 2026-04-15 · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** KI-generiert und ohne Quelle. Einen amtlichen Online-Anteil speziell für Bettwaren gibt es nicht. Zum Vergleich: Die ONS-Gruppe 'Household goods stores' liegt bei 28,8 % (4A-24), der gesamte Einzelhandel ebenfalls bei 28,8 % (saisonbereinigt, August 2026). Für Bettwaren ist die Zahl nicht prüfbar.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Seite bestätigt und um den vollständigen Satz erweitert. Unbelegtheit bestätigt.

### 3 Online-Anteil / 4 Saisonalität

#### 4A-23

✅ BELEGT · Angle: Markt

**Der nicht saisonbereinigte Online-Anteil im britischen Einzelhandel erreicht in den meisten Jahren im November seinen Monatshöchststand (2015–2020, 2023–2025), zuletzt 32,4 % im November 2025 (Oktober 2025: 28,0 %, Dezember 2025: 29,5 %). In den Lockdown-Folgejahren 2021 und 2022 lag die Spitze im Januar.**

> “'2025 SEP','27.3' '2025 OCT','28.0' '2025 NOV','32.4' '2025 DEC','29.5' '2026 JAN','28.7' … '2021 JAN','37.8' … '2022 JAN','30.1' '2022 NOV','29.9'”

- **Quelle:** [Office for National Statistics – Time series J4MC (DRSI)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/j4mc/drsi)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry, Großbritannien
- **Einordnung/Einschränkung:** Amtliche Werte. November-Spitzen: 2023 31,3 %, 2024 30,3 %, 2025 32,4 %. Sie fallen mit Black Friday zusammen. Gilt für den gesamten Einzelhandel in Großbritannien, nicht speziell für Bettwaren.
- **Wahrheits-Check:** *korrigiert*. Aus dem offiziellen CSV alle Monatsmaxima 2015–2026 geprüft. Korrigiert: Die Aussage 'jedes Jahr im November' ist falsch, 2021 (Jan 37,8 %) und 2022 (Jan 30,1 % vs. Nov 29,9 %) lag die Spitze im Januar.

### 3 Online-Anteil / 2 Wachstum

#### 4A-25

✅ BELEGT · Angle: Markt

**Die Online-Ausgaben im britischen Einzelhandel lagen in den drei Monaten bis August 2026 laut ONS um 10,1 % über dem Vorjahreszeitraum.**

> “Online spending values rose by 10.1% on the three months to August 2025. Within the monthly series, online sales values rose by 2.5% over the month to August 2026, up from a fall of 4.2% in July, and were 8.9% higher compared with August 2025.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: August 2026](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/august2026)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry, Großbritannien
- **Einordnung/Einschränkung:** Amtlicher Wert, nominal (Wert, nicht Menge). Gilt für den gesamten Einzelhandel, nicht speziell für Bettwaren. Gegenüber August 2025 lag das Plus im Einzelmonat bei 8,9 %.
- **Wahrheits-Check:** *bestätigt*. Bulletin per curl gelesen; Wortlaut bestätigt und um den Folgesatz ergänzt.

### 4 Saisonalität

#### 4A-28

⚠️ EINGESCHRÄNKT · Angle: Markt

**Der Umsatz mit Haushaltswaren (ONS-Warengruppe 'Household goods') lag in Großbritannien im November 2025 pro Woche etwa 34 % über dem Durchschnitt von Januar bis September 2025 (Dezember +24 %, Oktober +12 %).**

> “MCIW: VALUE OF RETAIL SALES BY COMMODITY AT CURRENT PRICES, NON-SEASONALLY ADJUSTED - Average Weekly Retail Sales in £thousands, Great Britain … Estimates in this table have been produced by combining a breakdown of commodity sales from 56 large retailers with total sales from other retailers. … Household goods: 2025OCT 1611143; 2025NOV 1922554; 2025DEC 1780628 [Jan–Sep 2025: 1.400.390–1.501.200]”

- **Quelle:** [Office for National Statistics – Retail sales pounds data (poundsdata.xlsx, Tabelle MCIW)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/datasets/poundsdatatotalretailsales)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Warengruppen-Aufschlüsselung von 56 großen Händlern, hochgerechnet mit den Gesamtumsätzen der übrigen Händler; Großbritannien
- **Einordnung/Einschränkung:** Amtliche Daten, die Prozentwerte habe ich selbst berechnet: Mittel Jan–Sep 2025 = £1.436,8 Mio. pro Woche; November £1.922,6 Mio. (+33,8 %), Dezember +23,9 %, Oktober +12,1 %. 2024 sah es ähnlich aus (November +28,5 %, Dezember +30,8 %). Einschränkung: 'Household goods' ist eine breite Warengruppe, deren Zusammensetzung die Datei nicht aufschlüsselt; der November-Effekt kann von anderen Produkten (z. B. Elektro) getrieben sein. Die ONS-Monate sind 4- bzw. 5-Wochen-Perioden (Dezember 5 Wochen). Stützt ein starkes Q4, ist aber keine Bettdecken-Zahl.
- **Wahrheits-Check:** *korrigiert*. poundsdata.xlsx (Release 18.09.2026) selbst geladen und Rechnung nachvollzogen. Korrigiert: Die Rohwerte im Wortlaut waren leicht falsch (1611111 / 1922596 / 1780566 statt 1611143 / 1922554 / 1780628). Die Prozentwerte bleiben unverändert. Die nicht belegte Liste der Inhalte der Warengruppe habe ich entfernt.

#### 4A-29

⚠️ EINGESCHRÄNKT · Angle: Markt, B Wechseljahre

**Nach '10.5 tog duvet' wird in Großbritannien im September etwa 2,2-mal so oft gesucht wie im Juni (Google-Trends-Monatsmittel über 5 Jahre: 37,8 vs. 17,1); die Spitzenwochen liegen im September. Nach '13.5 tog duvet' wird im November gut 4-mal so oft gesucht wie im Juni, '4.5 tog duvet' hat seine Spitze im Mai/Juni.**

> “Google Trends, GB, 'today 5-y', wöchentlich, eigene Monatsmittel (Abruf 08.10.2026): 10.5 tog duvet – Jan 25.0, Feb 21.6, Mär 19.3, Apr 18.3, Mai 18.0, Jun 17.1, Jul 20.9, Aug 26.2, Sep 37.8, Okt 29.8, Nov 32.0, Dez 27.6; 13.5 tog duvet – Jun 11.8, Nov 48.0; 4.5 tog duvet – Mai 32.5, Nov 10.4; Top-Wochen 10.5 tog: 25.9.–1.10.2022 (57), 6.–12.9.2026 (57), 7.–13.9.2025 (51)”

- **Quelle:** [Google Trends – Suchinteresse 10.5/13.5/4.5 tog duvet, Großbritannien, 5 Jahre (Abruf 08.10.2026)](https://trends.google.com/trends/explore?date=today%205-y&geo=GB&q=10.5%20tog%20duvet,13.5%20tog%20duvet,4.5%20tog%20duvet)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Sonstiges
- **Stichprobe/Methodik:** Wöchentliche Indexwerte (0–100, relativ), GB, 03.10.2021–10.10.2026 (letzte, unvollständige Woche ausgeschlossen)
- **Einordnung/Einschränkung:** Gemessen wird nur das relative Suchinteresse, nicht der Absatz. Die drei Begriffe wurden gemeinsam abgefragt und sind daher untereinander vergleichbar. Google Trends arbeitet mit Stichproben, ein erneuter Abruf kann leicht abweichen. Nur als Hinweis auf saisonale Muster nutzen. Dass die September-Spitze bei 10.5 tog den Umstieg auf die Winterdecke zeigt, ist eine Interpretation.
- **Wahrheits-Check:** *korrigiert*. Selbst über den Trends-Datenendpunkt (curl) neu abgerufen und die Monatsmittel nachgerechnet; der erste Versuch scheiterte an HTTP 429. Juni, September, November sowie die Werte für 13.5 und 4.5 tog sind exakt reproduziert. Korrigiert: Oktober 29,8 statt 30,3 (anderes Zeitfenster), Zeitfenster und Spitzenwochen ergänzt; die Spitzen liegen im September, nicht 'September/Oktober'.

#### 4A-30

⚠️ EINGESCHRÄNKT · Angle: Markt

**Das Google-Suchinteresse für 'duvet' liegt in Großbritannien im November am höchsten (Monatsmittel 76 gegenüber 42,5 im Juni). Hohe Wochenwerte gab es in der zweiten Novemberhälfte 2025 (16.–22.11.: 88, Woche vor Black Friday; 23.–29.11.: 84) und zum Jahreswechsel (28.12.2025–03.01.2026: 87).**

> “Google Trends, GB, 'duvet', today 5-y, eigene Monatsmittel (Abruf 08.10.2026): Jan 61.1, Feb 54.2, Mär 47.4, Apr 44.0, Mai 44.5, Jun 42.5, Jul 47.7, Aug 58.3, Sep 69.6, Okt 68.0, Nov 76.0, Dez 66.6; Wochen: '16–22 Nov 2025' 88, '23–29 Nov 2025' 84, '28 Dec 2025–3 Jan 2026' 87, '15–21 Feb 2026' 100”

- **Quelle:** [Google Trends – Suchinteresse 'duvet', Großbritannien, 5 Jahre (Abruf 08.10.2026)](https://trends.google.com/trends/explore?date=today%205-y&geo=GB&q=duvet)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Sonstiges
- **Stichprobe/Methodik:** Wöchentliche Indexwerte, GB, 03.10.2021–10.10.2026
- **Einordnung/Einschränkung:** Nur ein Indiz, kein Absatz. Der Höchstwert 100 in der Woche 15.–21.02.2026 ist ein Ausreißer mit unbekannter Ursache und verzerrt die Skala. 'duvet' umfasst auch Suchen nach 'duvet cover'. Black Friday 2025 war am 28.11.2025, die Woche 16.–22.11. lag also davor.
- **Wahrheits-Check:** *korrigiert*. Selbst neu abgerufen und nachgerechnet; Monatsmittel und Wochenwerte reproduziert (Oktober 68,0 statt 68,2). Korrigiert: Die Woche 16.–22.11.2025 ist nicht die Black-Friday-Woche (Black Friday war am 28.11.); die tatsächliche Black-Friday-Woche 23.–29.11. (84) habe ich ergänzt.

#### 4A-31

⚠️ EINGESCHRÄNKT · Angle: Markt, B Wechseljahre

**GlobalData-Analystin Emily Salter vermutete im Januar 2024, dass ein wärmer als üblicher Dezember 2023 den Absatz dicker Bettdecken und Decken gedämpft hat. Mit dem Kälteeinbruch und den höheren Energiepreisen zum Jahresbeginn dürfte die Nachfrage im Januar stark gestiegen sein.**

> “Sales of warm, energy-saving items like thicker duvets and blankets will have been dampened by a warmer than average December, although demand will have risen sharply in January with the recent onset of cold weather combined with the increase in energy bills at the start of the year. Dunelm is well positioned to capitalise on this demand …”

- **Quelle:** [Insight DIY – GlobalData on Dunelm's recent trading update (Kommentar Emily Salter, Lead Retail Analyst, GlobalData)](https://www.insightdiy.co.uk/news/globaldata-on-dunelms-recent-trading-update/13257.htm)
- **Datum der Quelle:** 2024-01-22 · **Typ:** Presse
- **Einordnung/Einschränkung:** Einschätzung einer Analystin ('will have been') ohne Absatzzahlen, fast drei Jahre alt und in einer Phase hoher Energiekosten. Stützt nur qualitativ, dass der Absatz dicker Bettdecken wetterabhängig ist und sich in den Januar verschieben kann.
- **Wahrheits-Check:** *korrigiert*. Seite per curl gelesen; vollständiger Wortlaut inkl. Januar-Satz und Datum 22.01.2024 bestätigt. Aussage korrigiert: Es ist eine Vermutung der Analystin, keine Feststellung; 'ungewöhnlich mild' steht so nicht in der Quelle ('warmer than average').

#### 4A-32

⚠️ EINGESCHRÄNKT · Angle: Markt, B Wechseljahre

**Dunelm steigerte im Quartal bis 31.12.2022 (Q2 GJ23) den Umsatz um 17,6 % auf £478,3 Mio. Laut Dunelm kamen die 'Winter Warm'- und Weihnachtssortimente gut an, weil Kunden steigende Heizkosten abfedern wollten. Genannt werden Teppiche, Thermovorhänge und beheizte Wäscheständer, Bettdecken nicht.**

> “Customers responded well to our 'Winter Warm' and Christmas ranges. As people try to find ways to mitigate heating costs, lines such as rugs, thermal curtains and heated airers proved popular. … The YoY growth rate included a benefit of c.2ppts from the timing of our Winter Sale … Quarterly analysis … Q2 Total sales £478.3m … Total sales growth 17.6%”

- **Quelle:** [Dunelm Group plc – Interim Results for the 26 weeks ended 31 December 2022 (RNS, FCA National Storage Mechanism)](https://data.fca.org.uk/artefacts/NSM/RNS/4674663.html)
- **Datum der Quelle:** 2023-02-15 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärquelle, aber veraltet und ein Sonderfall (Energiekrise 2022). Der Termin des Winter Sale verzerrt den Vergleich: Wegen der 53. Woche im GJ22 fielen sechs Tage des Winter Sale in Q2; für H1 bezifferte Dunelm den Effekt auf etwa 2 Prozentpunkte. Für Q2 allein nennt das Q2-Trading-Update (PDF nicht mehr abrufbar) laut Suchergebnis etwa 4 Prozentpunkte. Bettdecken werden weder genannt noch beziffert. Gilt nur als qualitativer Beleg für ein starkes Q4-Geschäft mit Wärmeprodukten.
- **Wahrheits-Check:** *korrigiert*. Den Presseartikel (Retail Bulletin, 19.01.2023) per curl geprüft: '18% uplift', '£478 million' und das Winter-Warm-Zitat stehen dort. Durch die Primärquelle ersetzt (Interim-RNS 15.02.2023 im FCA NSM): genau 17,6 % und £478,3 Mio. Die 'c.4ppts' standen nicht im Presseartikel; die Primärquelle nennt c.2ppts für H1. Klargestellt, dass Bettdecken nicht genannt werden.

#### 4A-33

✅ BELEGT · Angle: Markt, D Geschenk

**Dunelm beschreibt die Black-Friday-Phase 2025 als 'extrem umkämpft', bei der Rabatttiefe wie bei den Ausgaben für Performance-Marketing. Den Dezember 2025 nennt Dunelm schwierig für Homewares, den Winter Sale gut.**

> “In the first half consumer confidence remained subdued, and market data pointed towards a particularly challenging December for both homewares and the UK retail sector more generally. We also saw an extremely competitive Black Friday period, both in terms of the depth of discounts and performance marketing spend. … We remained disciplined in our promotional approach, despite elevated competitive activity, particularly from around Black Friday and in the run up to Christmas. … we are seeing stronger sales growth in early Q3 following a good Winter Sale”

- **Quelle:** [Dunelm Group plc – Interim Results for the 26 weeks ended 27 December 2025 (RNS, FCA National Storage Mechanism)](https://data.fca.org.uk/artefacts/NSM/RNS/46870cf2-4dbf-438c-a8a4-65d3316387a1.html)
- **Datum der Quelle:** 2026-02-10 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle Mitteilung. Belegt qualitativ, dass Black Friday und der Winter Sale (ab Ende Dezember) die zentralen Rabattfenster im Homewares-Markt sind und dort stark mit Performance-Marketing konkurriert wird. Zahlen zum Umsatzanteil dieser Phasen nennt Dunelm nicht. Umsatz H1: £926,3 Mio. (+3,6 %), Q2 nur +1,6 %.
- **Wahrheits-Check:** *korrigiert*. RNS per curl gelesen. Den gekürzten Wortlaut auf die vollständigen Sätze erweitert (Rabatttiefe und Performance-Marketing, schwieriger Dezember). Q2-Wachstum ergänzt.

#### 4A-34

✅ BELEGT · Angle: Markt

**Dunelm meldete wegen einer längeren Phase ungewöhnlich heißen Wetters ein deutlich schwächeres Geschäft in den ersten sechs Wochen des Geschäftsjahrs 2027 (ab Ende Juni 2026); nach kühlerem Wetter lief es laut Unternehmen besser.**

> “As a result of the extended period of unusually hot weather, however, we saw significantly softer trading in first six weeks of FY27 · Strong online conversion and increasing store footfall give confidence in our current proposition, and we have seen better trading following cooler weather”

- **Quelle:** [Dunelm Group plc – Preliminary Results for the 52 weeks ended 27 June 2026 (RNS)](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle Aussage. Sie zeigt, wie wetterabhängig die Nachfrage nach Homewares ist, gilt aber für das ganze Sortiment, nicht speziell für Bettdecken. Dass kaltes Herbstwetter die Nachfrage nach Winterdecken stützt, ist eine Ableitung, keine Aussage von Dunelm. Das Q1-Trading-Update folgt am 15.10.2026.
- **Wahrheits-Check:** *korrigiert*. RNS per curl gelesen. Wortlaut korrigiert: Der bisher zitierte Satz 'Unseasonably hot weather towards the end of the year …' betrifft das Ende des GJ26. Die Aussage zum GJ27 steht im Outlook; den Satz zur besseren Entwicklung nach kühlerem Wetter habe ich ergänzt.

#### 4A-V01

✅ BELEGT · Angle: Markt, D Geschenk

**Bei Dunelm ist das zweite Geschäftsquartal (Oktober bis Ende Dezember) das umsatzstärkste. Im GJ26 entfielen £498,2 Mio. von £1.825,5 Mio. (27,3 %) auf Q2 (Q1 £428,1 Mio., Q3 £471,7 Mio., Q4 £427,5 Mio.); im GJ25 ebenso (Q2 £490,5 Mio. von £1.771,0 Mio.).**

> “Quarterly analysis: 52 weeks to 27 June 2026 Q1 Q2 H1 Q3 Q4 H2 FY Total sales £428.1m £498.2m £926.3m £471.7m £427.5m £899.2m £1,825.5m … 52 weeks to 28 June 2025 Q1 Q2 H1 Q3 Q4 H2 FY Total sales £403.2m £490.5m £893.7m £461.9m £415.4m £877.3m £1,771.0m”

- **Quelle:** [Dunelm Group plc – Preliminary Results for the 52 weeks ended 27 June 2026 (RNS), Quarterly analysis](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Offizielle Quartalszahlen; den Anteil von 27,3 % habe ich selbst berechnet. Q2 endet mit dem Halbjahr am 27.12.2025 und umfasst Black Friday und den Beginn des Winter Sale. Gilt für das gesamte Dunelm-Sortiment (inkl. Möbel und Weihnachtsartikel), nicht speziell für Bettdecken.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. Quartalstabelle im RNS per curl gelesen; schließt die Lücke zu Händlerdaten zur Saisonalität (Q4-Kalenderquartal).

#### 4A-V06

⚠️ EINGESCHRÄNKT · Angle: Markt

**IKEA UK bewarb am 08.10.2026 Bettdecken mit einer 'Cosy Season essentials'-Aktion (20 % Rabatt, nur im Laden, gültig vom 07.09. bis 01.11.2026).**

> “SÄFFEROT Duvet, 7.5 TOG, Double £ 20 Price £ 20 20% off Cosy Season essentials - in store only Offer valid from 07.09.26 until 01.11.26”

- **Quelle:** [IKEA UK – Duvets (Kategorie)](https://www.ikea.com/gb/en/cat/duvets-20529/)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026
- **Einordnung/Einschränkung:** Ein einzelner Händler und nur ein qualitatives Indiz: Er setzt im Herbst gezielte Aktionen auf Bettdecken. Stützt den September/Oktober als aktives Verkaufsfenster, belegt aber keine Absatzanteile.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Wortlaut per curl auf der Kategorieseite bestätigt.

### 5 Preisniveau

#### 4A-37

✅ BELEGT · Angle: Markt, D Geschenk

**Bei Dunelm kosteten reine 10.5-tog-Bettdecken (ohne Sets) in Double am 08.10.2026 zwischen £16 (So Soft) und £205 (Dorma Hungarian Goose Down). Synthetik-Modelle lagen meist bei £20–46.**

> “So Soft 10.5 Tog Double – now 16; Fogarty 10.5 Tog Combi DB – 20; Fogarty AA 10.5 DB – 24; Soft Cotton Duvet 10.5 Tog Double – 26; Snuggledown LuxHotel Duvet 10.5Tog Dbl – 30 (nicht vorrätig); Fogarty Superfull 10.5 Tog DB – 36; Fogarty Temperature Balance 10.5 Tog DB – 46; Fogarty WDFD 10.5 Tog DB – 65; Dorma Full Forever 10.5 Tog DB – 75; SDown Hungarian GD Duvet 10.5 Tog Dbl – 150; Dorma Luxurious GD duvet 10.5 Tog DB – 200; Dorma Hungarian WGD 10.5Tog DB – 205; Bed in a Bag Double – now 15.4, was 22”

- **Quelle:** [Dunelm – Kategorie Duvets und Produktseiten (z. B. So Soft 10.5 Tog Duvet, Dorma Hungarian Goose Down 10.5 Tog Duvet)](https://www.dunelm.com/category/home-and-furniture/bedding/duvets)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026; die Kategorie zeigte 182 Bettdecken, davon rund 40 Produkte mit '10.5' im Namen (inkl. Sets und Duo-Decken)
- **Einordnung/Einschränkung:** Die Preise habe ich am 08.10.2026 selbst aus den Produktdaten der Kategorieseite und der Produktseiten gelesen (Double-Variante je Produkt). Dorma Full Forever ist laut Produktseite synthetisch ('Fill: 100% Recycled Polyester'), keine Daune. Günstigstes Double-Angebot insgesamt ist das Set 'Bed in a Bag' (Bettdecke plus Kissen) für £15,40 im Abverkauf. Nur eine Momentaufnahme; Aktionen ändern die Preise häufig. Preisvergleiche in Ads ('günstiger als …') sind daraus nicht ableitbar und bräuchten eine gesonderte Prüfung nach CAP-Code.
- **Wahrheits-Check:** *korrigiert*. Alle genannten Double-Preise auf den Produktseiten per curl bestätigt. Korrigiert und präzisiert: 'reine Bettdecken ohne Sets'; das günstigere Set (£15,40), weitere Preispunkte (Daune £150–205) und die fehlende Verfügbarkeit von Snuggledown LuxHotel in Double ergänzt. Stichprobe neu beschrieben (die alte Angabe '22 Produkte' war nicht nachvollziehbar).

#### 4A-38

✅ BELEGT · Angle: C Bettbeziehen, Markt

**Dunelm verkauft bereits 'coverless' 10.5-tog-Bettdecken ohne separaten Bezug. In Double kostete Snuggledown Coverless (inkl. Kissenbezug) am 08.10.2026 £30, die Modelle Coverless Stripe und Coverless Gingham je £40 (beide in Double am Stichtag nicht vorrätig).**

> “Snuggledown Coverless 10.5 tog Duvet Dbl – now 30 (inStock: true); Coverless Stripe 10.5 Tog DB Natural – now 40 (inStock: false); Coverless Gingham 10.5 Tog DB Blue – now 40 (inStock: false)”

- **Quelle:** [Dunelm – Produktseiten Snuggledown 10.5 Tog Coverless Duvet & Pillowcase Set; Coverless Striped 10.5 Tog Duvet and Pillowcase Set; Coverless Gingham 10.5 Tog Duvet](https://www.dunelm.com/product/snuggledown-105-tog-coverless-winter-duvet-pillowcase-set-1000245452)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026
- **Einordnung/Einschränkung:** Selbst abgelesen; weitere Produkte: https://www.dunelm.com/product/coverless-striped-105-tog-duvet-1000295265 und https://www.dunelm.com/product/coverless-gingham-105-tog-duvet-1000295264. Relevant für Angle C: Große Händler adressieren das Problem 'Bezug aufziehen' bereits mit Coverless-Produkten. Ads sollten das eigene Produkt daher nicht als 'einzige Lösung' darstellen. Nur eine Momentaufnahme.
- **Wahrheits-Check:** *korrigiert*. Preise in den Produktdaten bestätigt. Ergänzt: Coverless Stripe Double war nicht vorrätig, das Listing heißt 'Coverless Striped 10.5 Tog Duvet and Pillowcase Set'; Coverless Gingham (£40) als weiteres Modell aufgenommen.

#### 4A-39

✅ BELEGT · Angle: Markt, D Geschenk

**Bei M&S kostete die 10.5-tog-Bettdecke 'Smart Wash & Dry' in Double am 08.10.2026 £35, die 'Down Rich' £100. Über alle Größen reichten die 10.5-tog-Bettdecken der M&S-Eigenmarke auf der Kategorieseite von £30 bis £130; die Fremdmarke Bedfolk ging bis £459.**

> “Smart Wash & Dry 10.5 Tog Duvet … 'primarySize':'Double (4 ft 6)' … 'currentPrice':35 // Down Rich 10.5 Tog Duvet … 'primarySize':'Double (4 ft 6)' … 'currentPrice':100 // Kategorieseite: 'Product name is Smart Wash & Dry 10.5 Tog Duvet, Product brand is M&S, Price is £30 - £40' … 'Down Rich 10.5 Tog Duvet, Product brand is M&S, Price is £90 - £130' … 'Duck Feather & Down 10.5 Tog Duvet, Product brand is Bedfolk, Price is £189 - £459'”

- **Quelle:** [Marks & Spencer – Kategorie Duvets und Produktseiten Smart Wash & Dry 10.5 Tog Duvet, Down Rich 10.5 Tog Duvet](https://www.marksandspencer.com/smart-wash-and-dry-10-5-tog-duvet/p/hbp60779727)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026
- **Einordnung/Einschränkung:** Die Produktseiten habe ich per curl gelesen, die Preise je Größe stammen aus den Produktdaten. Down Rich: https://www.marksandspencer.com/down-rich-10-5-tog-duvet/p/hbp60779534; Kategorie: https://www.marksandspencer.com/l/home-and-furniture/bedding/duvets. Smart Wash & Dry steht auf der Kategorieseite mit '£30 - £40', auf der Produktseite mit '£30 - £50' (Super King £50). Nur eine Momentaufnahme.
- **Wahrheits-Check:** *korrigiert*. Double-Preise £35 und £100 bestätigt. Korrigiert: Die Spanne '£30 bis £130' gilt nur für die M&S-Eigenmarke; auf derselben Kategorieseite steht Bedfolk Duck Feather & Down 10.5 Tog mit £189–459.

#### 4A-40

✅ BELEGT · Angle: C Bettbeziehen, Markt

**M&S bietet eine 10.5-tog-'Coverless'-Bettdecke der Fremdmarke Night Lark inkl. Kissenbezügen an, die mit leichterem Bettwechsel beworben wird; in Double kostete sie am 08.10.2026 £75.**

> “This soft duvet set from Night Lark has a coverless design to make changing the bedding a breeze. The 10.5 tog duvet has a textured seersucker design for a distinctive look and comes with two pil[lowcases] … 'primarySize':'Double (4 ft 6)' … 'currentPrice':75”

- **Quelle:** [Marks & Spencer – 10.5 Tog Coverless Duvet & Pillowcase (Night Lark)](https://www.marksandspencer.com/10-5-tog-coverless-duvet-and-pillowcase/p/hbp23082601)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026
- **Einordnung/Einschränkung:** Selbst abgerufen; Spanne über alle Größen £55–85, auf der Kategorieseite als 'Online Only' markiert. Weitere Night-Lark-Coverless-Sets bei M&S kosten £70–98. Für Angle C: Ein Wettbewerber wirbt bereits mit demselben Nutzen ('changing the bedding a breeze'). Nur eine Momentaufnahme.
- **Wahrheits-Check:** *bestätigt*. Beschreibungstext, Marke (Nightlark) und Größenpreise (Single 55, Double 75, King 85) per curl bestätigt.

#### 4A-41

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Die John-Lewis-Suche nach '10.5 tog duvet double' zeigte am 08.10.2026 61 Treffer, davon rund 37 Bettdecken bzw. Sets mit 10.5 tog. Die Preisspannen reichten von £30–50 (Eigenmarke Synthetic Soft Touch Washable) bis £279–719 (Bedfolk 100% Duck Down); Preise speziell für Double wurden nicht angezeigt.**

> “John Lewis Synthetic Soft Touch Washable Duvet, 10.5 Tog: £30.00 – £50.00 … Silentnight Luxury Hotel Collection Duvet, 10.5 tog: £32.00 – £55.00 … John Lewis Climate Control Duvet, 10.5 Tog: £50.00 – £70.00 … Bedfolk 100% Duck Down Duvet, 10.5 Tog: £279.00 – £719.00”

- **Quelle:** [John Lewis – Suchergebnisse '10.5 tog duvet double' und Produktseite John Lewis Synthetic Soft Touch Washable Duvet, 10.5 Tog](https://www.johnlewis.com/search?search-term=10.5%20tog%20duvet%20double)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026; 61 Suchtreffer inkl. anderer Tog-Werte
- **Einordnung/Einschränkung:** Per WebFetch abgerufen (curl wurde blockiert). Sichtbar sind nur Spannen über alle Größen (Single bis Super King); auch die Produktseite (https://www.johnlewis.com/john-lewis-synthetic-soft-touch-washable-duvet-10-5-tog/p443935) zeigt keinen Double-Preis. Die Trefferliste enthält auch andere Tog-Werte und Zubehör. Nur zur Orientierung.
- **Wahrheits-Check:** *korrigiert*. Suchseite und Produktseite per WebFetch geprüft, Preisspannen bestätigt. Korrigiert: Die Suche ergab 61 Treffer, davon nach meiner Zählung rund 37 mit 10.5 tog (vorher 'rund 39').

#### 4A-42

⚠️ EINGESCHRÄNKT · Angle: C Bettbeziehen, Markt

**John Lewis führt mehrere 10.5-tog-'Coverless'-Bettdecken der Marke Night Lark zu Preisen zwischen £50 und £105 je nach Größe und Design (Stand 08.10.2026).**

> “Night Lark Seersucker Coverless Duvet, 10.5 Tog, Olive Green: £55.00 – £85.00 … Night Lark Seersucker Coverless Duvet & Pillowcase Set, 10.5 Tog, Polar White: £50.00 – £80.00 … Eleanor Bowmer x Night Lark® Rainbow Coverless Duvet & Pillowcase Set, 10.5 Tog, Multi: £75.00 – £105.00 … The in-built cover is crafted with peachskin microfibre, feather-soft to the touch for maximum comfort”

- **Quelle:** [John Lewis – Suchergebnisse '10.5 tog duvet double'; Produktseite Night Lark Seersucker Coverless Duvet, 10.5 Tog, Olive Green](https://www.johnlewis.com/night-lark-seersucker-coverless-duvet-10-5-tog-olive-green/p115865353)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026
- **Einordnung/Einschränkung:** Per WebFetch abgerufen; nur Spannen über alle Größen, kein Double-Preis. Laut Produktseite maschinenwaschbar bei 40 °C; die Größe King braucht eine 10-kg-Maschine. Für Angle C: Coverless ist bei mehreren großen UK-Händlern (Dunelm, M&S, John Lewis) bereits etabliert.
- **Wahrheits-Check:** *bestätigt*. Produktseite und Suchseite per WebFetch geprüft; Preise und Zitat bestätigt. Der Hinweis zur 10-kg-Waschmaschine ist für Angle C relevant.

#### 4A-43

⚠️ EINGESCHRÄNKT · Angle: Markt

**IKEA UK führt in der Duvet-Kategorie keine 10.5-tog-Bettdecken, sondern u. a. 2.5-, 4-, 7.5- und 12-tog-Modelle. Die SÄFFEROT 7.5 tog Double kostete am 08.10.2026 £20, allerdings als In-Store-Aktionspreis (20 % Rabatt).**

> “18 items … SÄFFEROT Duvet, 7.5 TOG, Double £ 20 Price £ 20 20% off Cosy Season essentials - in store only Offer valid from 07.09.26 until 01.11.26 … Option: SÄFFEROT, Duvet, 12 TOG, Double … FJÄLLARNIKA Duvet, 7.5 TOG, Double £ 49”

- **Quelle:** [IKEA UK – Duvets (Kategorie)](https://www.ikea.com/gb/en/cat/duvets-20529/)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Stichprobe/Methodik:** Momentaufnahme 08.10.2026, 18 Produkte
- **Einordnung/Einschränkung:** Per WebFetch und curl abgerufen; '10.5' kommt auf der Seite nicht vor. Der £20-Preis gilt nur im Laden im Rahmen der Aktion. IKEA-Größen weichen von den britischen Standardmaßen ab; ein direkter Vergleich mit 10.5 tog ist daher nicht möglich. Wirkt als Preisanker im Einstiegssegment.
- **Wahrheits-Check:** *korrigiert*. Seite per curl vollständig gelesen. Korrigiert: Die £20 sind ein In-Store-Aktionspreis ('20% off … in store only', gültig 07.09.–01.11.2026); 12-tog-Varianten bestätigt. Die frühere Angabe 'Double = 200×200 cm' habe ich nicht geprüft und daher entfernt.

## Nachrecherche G6 (zu Track 4A)

*Auftrag: Markt – britischer Bettwaren-/Homewares-Markt mit öffentlich prüfbaren Zahlen: (a) Dunelm Geschäftsbericht/Ergebnis FY2026 (Geschäftsjahr bis Juni 2026, veröffentlicht ca. Sept. 2026) – Umsatz, Digital-Anteil, Marktanteil, Aussagen zum Homewares-Markt; (b) GlobalData UK Homewares/Home Textiles Pressemitteilungen 2025/2026 (Marktgröße, Prognose, Online-Anteil); (c) Mintel-Pressemitteilungen zu Bedding/Home Textiles/Beds UK; (d) ONS Family Spending (neueste Ausgabe) – wöchentliche Haushaltsausgaben für household textiles / bedding; (e) HMRC/uktradeinfo Importwerte für Bettdecken/Steppdecken (CN 9404 90); (f) ONS Internet sales als Anteil des Einzelhandels – neuester Monatswert 2026 und Wert für 'household goods stores'.*

*Prüf-Fazit: Der Track ist insgesamt sehr verlässlich: Alle 48 Claims wurden selbst an der Quelle nachvollzogen, Zahlen aus ONS-XLSX, HMRC-API, Zolltarif-API und Dunelm-RNS/PDF wurden exakt reproduziert, und es musste kein Claim verworfen werden. Die Korrekturen betreffen Details: einen nicht belegten Firmennamen (Home Focus), die Quartalsabgrenzung, eine falsche Byline, überzogene oder ungeprüfte Nebensätze in Begründungen (Mintel 2017, SourceReady, '£14–16 Mrd.'), eine zu starke Formulierung zur Intervall-Überschneidung und fehlende Datumsangaben bei den HMRC-Daten. Neu aufgenommen wurde der GlobalData-Heimtextilienmarkt (£6,07 Mrd. 2024, via Business Gateway, mit CAGR-Unstimmigkeit). Für Ads belastbar sind nur die amtlichen ONS- und HMRC-Werte sowie Dunelm-Primärzahlen, jeweils mit genauer Bezugsgröße (Homewares+Möbel, GB statt UK, Zollwert statt Umsatz, 'digital' statt 'online'). Eine prüfbare Marktgröße speziell für Bettdecken fehlt weiterhin.*

### (a) Dunelm FY2026 – Umsatz

#### G6-01

✅ BELEGT · Angle: Markt

**Der Dunelm-Konzern (UK und Irland) steigerte seinen Umsatz in den 52 Wochen bis 27. Juni 2026 um 3,1 % auf £1.825,5 Mio. (Vorjahr £1.771,0 Mio.).**

> “FY26 FY25 YoY Total sales £1,825.5m £1,771.0m +3.1% ... During the year we grew our sales by 3.1% to £1,825m, gained 10bps of market share to 7.9%”

- **Quelle:** [Dunelm Group plc – Preliminary Results for the 52 weeks ended 27 June 2026 (RNS, via Investegate)](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärquelle (Pflichtmitteilung an die Börse). Einschränkungen: Der Umsatz enthält Irland ('new space contributing c.100bps to sales growth, including the full-year impact of our Ireland acquisition'). Dunelm berichtet nur ein Segment ('retail of homewares in the UK and Ireland'). Umsätze nach Kategorie, etwa Bettwaren, werden nicht ausgewiesen.
- **Wahrheits-Check:** *korrigiert*. Tabellenzeile und Satz im RNS-Text per curl und WebFetch selbst gelesen, Datum 08.09.2026 bestätigt. Korrigiert: Der Name 'Home Focus' steht nicht in der Mitteilung, dort heißt es nur 'Ireland acquisition'. Begründung entsprechend angepasst.

### (a) Dunelm FY2026 – Digital-Anteil

#### G6-02

✅ BELEGT · Angle: Markt

**Digitale Verkäufe machten im Dunelm-Geschäftsjahr 2026 42 % des Umsatzes aus (Vorjahr 40 %), im vierten Quartal (13 Wochen bis 27. Juni 2026) 45 %. 'Digital' umfasst Lieferung nach Hause, Click & Collect und Tablet-Bestellungen im Laden.**

> “Together with home delivery, digital sales participation increased by 2ppts to 42%. [Fußnote 9:] Includes home delivery, Click & Collect and tablet-based sales in store”

- **Quelle:** [Dunelm Group plc – Preliminary Results FY26 (RNS, via Investegate)](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Laut Quartalstabelle der Primärquelle ('Digital % total sales'): Q1 40 %, Q2 42 %, Q3 43 %, Q4 45 %, Gesamtjahr 42 %. Vorjahr: 37/40/41/42 %, Gesamtjahr 40 %. 'Digital' heißt nicht 'online nach Hause bestellt', denn Click & Collect und Tablet-Käufe im Laden zählen mit. Deshalb nicht als 'Online-Anteil' bewerben.
- **Wahrheits-Check:** *korrigiert*. Wortlaut, Fußnote und Quartalswerte im RNS-Text gefunden. Korrigiert: Q4 ist nicht 'April–Juni', sondern die 13 Wochen bis 27.06.2026 (Q3 endete laut Retail Times am 28.03.2026).

### (a) Dunelm FY2026 – Marktanteil

#### G6-03

✅ BELEGT · Angle: Markt

**Dunelms Anteil am kombinierten britischen Homewares- und Möbelmarkt (GlobalData, ohne Küchen- und Badmöbel) lag in den 12 Monaten bis Juni 2026 bei 7,9 %. Das sind 10 Basispunkte mehr als der rückwirkend auf 7,8 % korrigierte Vorjahreswert.**

> “GlobalData UK combined homewares and furniture markets, excluding kitchen cabinetry and bathroom furniture, for the 12 months to June 2026. Market share for the 12 months to June 2025 was 7.8% (restated by GlobalData UK from 7.9%)”

- **Quelle:** [Dunelm Group plc – Preliminary Results FY26, Fußnoten 6/11](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Herkunft (GlobalData) und Marktabgrenzung stehen in der Fußnote. Einschränkung: Der Markt umfasst Homewares UND Möbel, es ist kein Anteil am reinen Homewares- oder Bettwarenmarkt. Auf der Dunelm-Seite zum Geschäftsbericht 2025 steht für FY25 noch 7,9 %, später auf 7,8 % korrigiert.
- **Wahrheits-Check:** *bestätigt*. Fußnote wörtlich im RNS-Text gefunden. Die frühere Angabe 7,9 % für FY25 auf corporate.dunelm.com/…/annual-report-2025/ selbst bestätigt.

### (a) Dunelm FY2026 – Marktgröße Homewares+Möbel

#### G6-04

✅ BELEGT · Angle: Markt

**Der kombinierte britische Homewares- und Möbelmarkt umfasste laut GlobalData (zitiert von Dunelm) in den 12 Monaten bis Juni 2026 rund £25 Mrd. inklusive Mehrwertsteuer. Für die 12 Monate bis Juni 2025 nannte Dunelm £24 Mrd.**

> “As the market leader in the UK's combined £25bn homewares and furniture market, we operate from a position of strength. [Fußnote 7:] GlobalData UK combined homewares and furniture markers, excluding kitchen cabinetry and bathroom furniture, for the 12 months to June 2026. Market size includes VAT”

- **Quelle:** [Dunelm Group plc – Winning Hearts & Homes: A self-funded growth plan (Strategy update)](https://corporate.dunelm.com/media/jq2b41c3/strategy-update-winning-hearts-homes.pdf)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Herkunft (GlobalData), Zeitraum, Abgrenzung und MwSt.-Basis sind angegeben, die Methodik von GlobalData ist nicht öffentlich. Vorjahreswert laut Dunelm-Seite zum Geschäftsbericht 2025: 'Total addressable market £24bn', 12 Monate bis Juni 2025, inkl. MwSt. Der Wert enthält Möbel. Eine Teilzahl für Bettwaren oder Bettdecken gibt es nicht.
- **Wahrheits-Check:** *bestätigt*. PDF per curl/pdftotext selbst gelesen, Satz und Fußnote 7 wörtlich gefunden ('markers' ist ein Tippfehler im Original). £24 bn auf der Seite zum Geschäftsbericht 2025 selbst bestätigt.

### (a) Dunelm FY2026 – Kundenreichweite

#### G6-05

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Dunelm-Managementschätzung kaufen rund 85 % der britischen Bevölkerung nicht regelmäßig bei Dunelm, und selbst die treuesten Kunden geben rund 80 % ihrer Ausgaben fürs Zuhause anderswo aus.**

> “Around 85% of the UK population does not yet shop with Dunelm frequently, while even our most loyal customers continue to direct approximately 80% of their spend on the home elsewhere.”

- **Quelle:** [Dunelm Group plc – Winning Hearts & Homes (Strategy update), Fußnoten 8/9](https://corporate.dunelm.com/media/jq2b41c3/strategy-update-winning-hearts-homes.pdf)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** Management estimates using Barclays UK data (85 %) bzw. Barclays and Kantar UK data (80 %); Methodik nicht offengelegt
- **Einordnung/Einschränkung:** Managementschätzung auf Basis von Zahlungs- und Paneldaten. Was 'frequently' bedeutet und wie gerechnet wurde, ist nicht offengelegt. Als Signal für einen fragmentierten Markt brauchbar, nicht als harte Statistik.
- **Wahrheits-Check:** *bestätigt*. Satz und Fußnoten 8/9 in der PDF (pdftotext) wörtlich gefunden.

### (a) Dunelm FY2026 – Verbraucherverhalten

#### G6-06

⚠️ EINGESCHRÄNKT · Angle: Markt

**Dunelm berichtet für das Geschäftsjahr 2026, dass britische Kunden selektiver einkaufen und vermehrt über Aktionen nach Preiswert suchen, besonders bei verzichtbaren Kategorien wie Homewares.**

> “Geopolitical uncertainty, elevated interest rates and inflation, and a changing UK political landscape continued to weigh on consumer confidence, with customers shopping more selectively and increasingly seeking value through promotions, particularly in discretionary categories such as homewares.”

- **Quelle:** [Dunelm Group plc – Preliminary Results FY26](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Qualitative Einschätzung des größten Homewares-Händlers, keine Messzahl. Im nächsten Satz der Quelle heißt es: 'Unseasonably hot weather towards the end of the year also affected customers' shopping patterns.' Die Aussage passt zu Mintel ('more competitive, especially on price') und GlobalData 2026 ('majority … cited price').
- **Wahrheits-Check:** *bestätigt*. Wortlaut im RNS-Text exakt gefunden.

### (a) Dunelm FY2026 – Kundenzahl

#### G6-07

⚠️ EINGESCHRÄNKT · Angle: Markt

**Die Zahl der Dunelm-Kunden blieb im Geschäftsjahr 2026 laut Unternehmen 'weitgehend stabil'. Mehr Kunden kauften über mehrere Kanäle (Managementschätzung auf Basis von Barclays-Daten).**

> “Though customer numbers remained broadly stable across the year, we saw more customers shopping multiple channels”

- **Quelle:** [Dunelm Group plc – Preliminary Results FY26](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** Fußnote 12: Management estimates using Barclays UK data
- **Einordnung/Einschränkung:** Keine absolute Kundenzahl, nur eine qualitative Angabe, der Multichannel-Teil ist eine Managementschätzung. Das Wachstum kam damit eher nicht aus neuen Kunden.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Fußnote 12 im RNS-Text gefunden.

### (a) Dunelm FY2026 – Bettwaren-Test

#### G6-08

⚠️ EINGESCHRÄNKT · Angle: Markt, C Bettbeziehen

**Dunelm testete in der umgebauten Filiale St Albans neue Präsentation und Kundenführung für unifarbene Bettwäsche (plain-dye bedding) und meldet dort ein zweistelliges Umsatzplus gegenüber dem Vorjahr.**

> “We have also tested merchandising and flow changes in plain-dye bedding, with year-on-year sales up double-digits in our St Albans refit.”

- **Quelle:** [Dunelm Group plc – Winning Hearts & Homes (Strategy update)](https://corporate.dunelm.com/media/jq2b41c3/strategy-update-winning-hearts-homes.pdf)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** Einzelfiliale (St Albans), keine genaue Prozentzahl
- **Einordnung/Einschränkung:** Der einzige Leistungshinweis zu Bettwaren in den FY26-Unterlagen. Er betrifft nur eine Filiale, nennt keine genaue Zahl und bezieht sich auf Bettwäsche, nicht auf Bettdecken. Nicht auf den Markt übertragbar.
- **Wahrheits-Check:** *bestätigt*. Satz in der PDF (pdftotext) wörtlich gefunden.

### (a) Dunelm FY2026 – Saisonalität/Ausblick

#### G6-09

✅ BELEGT · Angle: Markt

**Dunelm meldete wegen einer längeren Hitzeperiode 'deutlich schwächere' Umsätze in den ersten sechs Wochen des Geschäftsjahres 2027 (ab Ende Juni 2026). Nach kühlerem Wetter habe sich das Geschäft in den letzten Wochen verbessert.**

> “As a result of the extended period of unusually hot weather, however, we saw significantly softer trading in first six weeks of FY27 · Strong online conversion and increasing store footfall give confidence in our current proposition, and we have seen better trading following cooler weather”

- **Quelle:** [Dunelm Group plc – Preliminary Results FY26 (Outlook)](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Direkte Aussage der Primärquelle. Für keine Kategorie angegeben, ob also gerade Bettwaren betroffen waren, ist nicht belegt. Hinweis für die Planung: Das Wetter beeinflusst den Homewares-Absatz spürbar.
- **Wahrheits-Check:** *bestätigt*. Beide Sätze im Outlook-Abschnitt gefunden. Wortlaut um 'better trading following cooler weather' ergänzt, Aussage inhaltlich unverändert.

### (a) Dunelm FY2026 – App

#### G6-10

✅ BELEGT · Angle: Markt

**Die im Februar 2026 vollständig gestartete Dunelm-App hatte 740.000 Downloads. App-Kunden geben laut Dunelm pro Transaktion rund 40 % mehr aus, und die Conversion liegt um mehr als einen Prozentpunkt höher.**

> “The Dunelm App has attracted 740k downloads to date and is driving encouraging engagement. Since launching fully in February 2026, customers shopping through the App already spend c.40% more per transaction, with conversion more than one percentage point higher.”

- **Quelle:** [Dunelm Group plc – Preliminary Results FY26](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Unternehmenseigene Kennzahl aus der Primärquelle. Es ist eine Korrelation, keine Kausalität, denn App-Nutzer sind vermutlich ohnehin aktivere Kunden. Pulse2 (10. und 12.09.2026) gibt die Zahlen korrekt wieder. Ein Artikel ergänzt 'than other channels', das steht so nicht in der Primärquelle.
- **Wahrheits-Check:** *bestätigt*. Wortlaut im RNS-Text exakt gefunden. Beide Pulse2-Artikel per curl geprüft.

### (a) Dunelm FY2026 – Mythos App-Kennzahlen

#### G6-11

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die kursierende Angabe, die Dunelm-App habe die Conversion um 51 % und den durchschnittlichen Bestellwert um 42 % gesteigert, ist nicht belegt. Laut Primärquelle geben App-Kunden rund 40 % mehr pro Transaktion aus, und die Conversion liegt um gut einen Prozentpunkt höher.**

> “customers shopping through the App already spend c.40% more per transaction, with conversion more than one percentage point higher.”

- **Quelle:** [Gegenprüfung: Dunelm Preliminary Results FY26; Pulse2-Artikel vom 10.09. und 12.09.2026](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Presse
- **Einordnung/Einschränkung:** Weder die RNS noch die beiden Pulse2-Artikel enthalten '51 %'. Die 42 % sind dort der Digitalanteil am Umsatz. Woher die Zahl stammt, ist nicht nachvollziehbar, vermutlich eine Verwechslung. Nicht verwenden.
- **Wahrheits-Check:** *bestätigt*. RNS und beide Pulse2-Artikel per curl nach '51%' durchsucht, kein Treffer. Unbelegtheit bestätigt.

### (a) Dunelm FY2026 – Mythos Marktanteil

#### G6-12

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Kurzform 'Dunelm hat 7,9 % des britischen Homewares-Markts' ist so nicht belegt. Die 7,9 % beziehen sich auf den kombinierten Homewares- UND Möbelmarkt (rund £25 Mrd., GlobalData).**

> “Overall, we continued to outperform the combined homewares and furniture market, increasing market share by 10bps year-on-year to 7.9%”

- **Quelle:** [Dunelm Group plc – Preliminary Results FY26](https://www.investegate.co.uk/announcement/rns/dunelm-group--dnlm/preliminary-results-/9759867)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Die Bezugsgröße ist ausdrücklich der kombinierte Homewares- und Möbelmarkt. Der Anteil am engeren Homewares-Markt ist öffentlich nicht beziffert. Zur Größenordnung: GlobalData prognostiziert für reine Homewares £16,0 Mrd. im Jahr 2029. Ein Basiswert 2024 von etwa £14,3 Mrd. ergibt sich nur rechnerisch (eigene Rechnung, siehe G6-13), GlobalData nennt ihn nicht. Für FY25 wurden 7,9 % genannt, später auf 7,8 % korrigiert.
- **Wahrheits-Check:** *korrigiert*. Wortlaut im RNS-Text gefunden, Unbelegtheit der Kurzform bestätigt. Korrigiert: Die frühere Begründung 'GlobalData beziffert den reinen Homewares-Markt auf rund £14–16 Mrd.' war überzogen. £16,0 Mrd. ist eine Prognose für 2029, £14,3 Mrd. ist nur eine eigene Rückrechnung.

### (b) GlobalData – Homewares-Prognose 2024–2029

#### G6-13

⚠️ EINGESCHRÄNKT · Angle: Markt

**GlobalData prognostiziert für den britischen Homewares-Markt (ohne Möbel) ein durchschnittliches Wachstum von 2,2 % pro Jahr zwischen 2024 und 2029 auf £16,0 Mrd. im Jahr 2029.**

> “The homewares market is projected to grow at a compound annual growth rate (CAGR) of 2.2% between 2024 and 2029, reaching £16.0bn by the end of the period.”

- **Quelle:** [GlobalData – UK Sector Series: Homewares, 2024-2029 (Store-Seite 'United Kingdom (UK) Homewares Market Analysis by Categories, Revenue, Consumer Trends, Key Players and Forecast to 2029', Report Code GDRT250000CSUK-ST)](https://www.globaldata.com/store/report/uk-homewares-retail-market-analysis/)
- **Datum der Quelle:** 2025-07-31 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Öffentlich sichtbare Zahl einer kostenpflichtigen Studie (ab $3.500), Methodik und Abgrenzung sind nicht einsehbar. Es ist eine Prognose, kein Ist-Wert. Rechnerisch ergibt sich ein Basiswert 2024 von etwa £14,3–14,4 Mrd. (eigene Rechnung, von GlobalData nicht öffentlich genannt). Nicht mit dem £25-Mrd.-Markt inklusive Möbel (G6-04) verwechseln.
- **Wahrheits-Check:** *bestätigt*. Satz, Datum 'Published: July 31, 2025', Report Code und Preis auf der Store-Seite selbst gefunden. Die Seite nennt keine Werte für 2024 oder 2025.

### (b) GlobalData – Online-Wachstum Homewares

#### G6-14

⚠️ EINGESCHRÄNKT · Angle: Markt

**GlobalData erwartet, dass der Online-Kanal im britischen Homewares-Markt 2024–2029 mit 3,2 % pro Jahr schneller wächst als der stationäre Handel mit 1,7 % pro Jahr.**

> “The online channel will outpace offline growth in every year of the forecast period, growing at a CAGR of 3.2% versus 1.7%, with retailers that have strong online propositions like Amazon and Dunelm well-placed to maintain their forward momentum in the sector.”

- **Quelle:** [GlobalData – UK Sector Series: Homewares, 2024-2029](https://www.globaldata.com/store/report/uk-homewares-retail-market-analysis/)
- **Datum der Quelle:** 2025-07-31 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Prognose aus einer kostenpflichtigen Studie. Die Seite nennt nur Wachstumsraten, keinen Online-Anteil in Prozent. Methodik nicht einsehbar.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Store-Seite exakt gefunden.

### (b) GlobalData – Volumen ab 2026

#### G6-15

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut GlobalData (Prognose vom Juli 2025) sollen die Absatzmengen im britischen Homewares-Markt erst ab 2026 wieder wachsen. Wichtigster Treiber des Umsatzwachstums bleibt die Inflation.**

> “Volumes are forecast to begin growing from 2026 onwards, although inflation will continue to be the primary driver of sales growth.”

- **Quelle:** [GlobalData – UK Sector Series: Homewares, 2024-2029](https://www.globaldata.com/store/report/uk-homewares-retail-market-analysis/)
- **Datum der Quelle:** 2025-07-31 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Prognose ohne öffentliche Volumenzahlen. Ob die Mengen 2026 tatsächlich wachsen, ist öffentlich nicht bestätigt. Dunelm meldete für FY26 nur +0,8 % store-enabled LFL, das ist ein Wert- und kein Volumenmaß.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Store-Seite exakt gefunden.

### (b) GlobalData – Volumen 2025 / 'cosy' Textilien

#### G6-16

⚠️ EINGESCHRÄNKT · Angle: Markt

**GlobalData erwartete für 2025 einen leichten Volumenrückgang im britischen Homewares-Markt. Dunelm habe im Herbst 2025 besonders mit 'cosy' Heimtextilien und Teppichen gepunktet.**

> “The volume growth is especially impressive considering GlobalData forecasts a small decline in homewares volumes in 2025. While Dunelm saw growth across categories, it performed especially well in its existing specialism of 'cosy' items in home textiles and rugs as consumers prepared their homes for the autumn and winter”

- **Quelle:** [Retail Times – 'Dunelm outdoes itself as consumers seek cosy comfort for the winter, says GlobalData' (Kommentar Oliver Maddison, GlobalData)](https://retailtimes.co.uk/dunelm-outdoes-itself-as-consumers-seek-cosy-comfort-for-the-winter-says-globaldata/)
- **Datum der Quelle:** 2025-10-23 · **Typ:** Presse
- **Einordnung/Einschränkung:** Analystenkommentar von GlobalData im Wortlaut, veröffentlicht über Retail Times. Die Höhe des Rückgangs wird nicht beziffert. Die Aussage zu 'cosy' Textilien interpretiert Dunelms Q1-Ergebnis und ist keine Marktmessung. Bettdecken werden nicht genannt.
- **Wahrheits-Check:** *bestätigt*. Wortlaut per curl exakt gefunden. Datum 23.10.2025 bestätigt, Artikel-Byline Fiona Briggs, zitiert wird Oliver Maddison.

### (b) GlobalData – Verbraucherstimmung 2026

#### G6-17

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut GlobalDatas 'future consumer sentiment tracker' fiel die britische Verbraucherstimmung im März 2026 gegenüber dem Vormonat um 8,2 Punkte. GlobalData wertete das als Signal für schwierige Zeiten im britischen Home-Handel.**

> “Dunelm's Q3 performance was weaker than it originally anticipated, taking a hit as consumer sentiment fell by 8.2 points month-on-month in March (according to GlobalData's future consumer sentiment tracker) signalling tough times for the UK home retail sector.”

- **Quelle:** [Retail Times – 'Declines in consumer confidence knock Dunelm's progress, says GlobalData' (Oliver Maddison)](https://retailtimes.co.uk/declines-in-consumer-confidence-knock-dunelms-progress-says-globaldata/)
- **Datum der Quelle:** 2026-04-16 · **Typ:** Presse
- **Stichprobe/Methodik:** GlobalData-eigener Tracker; Stichprobe/Methodik nicht angegeben
- **Einordnung/Einschränkung:** Eigener Index von GlobalData ohne öffentliche Methodik. Brauchbar als Zeitkontext, nicht als amtliche Konsumklima-Zahl.
- **Wahrheits-Check:** *bestätigt*. Wortlaut per curl exakt gefunden, Datum 16.04.2026 bestätigt.

### (b) GlobalData – Laden vs. Online bei Dunelm

#### G6-18

⚠️ EINGESCHRÄNKT · Angle: Markt

**GlobalData schätzt, dass Dunelms Ladenumsatz im Geschäftsjahr 2025/26 im Jahresdurchschnitt zurückging und nur im ersten Quartal wuchs, während der Online-Umsatz durchgehend besser lief.**

> “GlobalData estimates that Dunelm's instore revenue declined in the full-year average, albeit most significantly in Q4. ... Dunelm's instore sales have persistently underperformed its online sales throughout its financial year, and only grew in its Q1, when overall growth exceeded 6%.”

- **Quelle:** [Retail Times – 'Dunelm's decent year end signals recovering consumer confidence, says GlobalData' (Oliver Maddison)](https://retailtimes.co.uk/dunelms-decent-year-end-signals-recovering-consumer-confidence-says-globaldata/)
- **Datum der Quelle:** 2026-07-16 · **Typ:** Presse
- **Einordnung/Einschränkung:** GlobalData-Schätzung, nicht von Dunelm ausgewiesen. Dunelm schreibt selbst 'while sales through store checkouts alone declined'. Die Richtung ist damit gestützt, eine Zahl fehlt.
- **Wahrheits-Check:** *bestätigt*. Wortlaut per curl gefunden, Datum 16.07.2026 bestätigt. Wortlaut um den GlobalData-Schätzsatz ergänzt.

### (b) GlobalData – Schlafzimmertextilien 2026: Kaufquote

#### G6-19

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut GlobalData-Umfrage 2026 (n=2.000, national repräsentativ) hat mehr als die Hälfte der britischen Verbraucher in den letzten 12 Monaten Schlafzimmertextilien gekauft. Am höchsten war die Kaufquote bei den 16- bis 24-Jährigen.**

> “Consumer data is based on our 2026 UK bedroom textiles survey, using a panel of 2,000 nationally representative consumers. Scope Over half of UK consumers have purchased bedroom textiles products in the last 12 months, with the highest purchasing penetration among 16-24 year-olds.”

- **Quelle:** [GlobalData – United Kingdom (UK) Home: Bedroom Textiles – Market Trends, Analysis, Consumer Dynamics and Spending Habits (Store-Seite, GDRT260006CPUK-ST)](https://www.globaldata.com/store/report/uk-bedroom-textiles-market-analysis/)
- **Datum der Quelle:** 2026-07-30 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** n=2.000, Panel 'nationally representative', UK, Erhebung 2026 (Feldzeit nicht angegeben)
- **Einordnung/Einschränkung:** Seriöser Anbieter mit Stichprobenangabe, aber ohne genaue Prozentzahl ('over half') und ohne Feldzeit. Die Kategorie umfasst Pillows & duvets, Covers, Blankets, Sheets und Bedroom accessories. Die Kaufquote für Bettdecken ist nicht öffentlich.
- **Wahrheits-Check:** *bestätigt*. Wortlaut per curl auf der Store-Seite gefunden, 'Published: July 30, 2026' bestätigt.

### (b) GlobalData – Schlafzimmertextilien 2026: Händler

#### G6-20

⚠️ EINGESCHRÄNKT · Angle: Markt

**In der GlobalData-Umfrage 2026 ist Amazon der meistgenutzte Händler für Schlafzimmertextilien in UK, vor Dunelm und ASDA. Amazon hat auch die höchste Conversion-Rate, gefolgt von Dunelm.**

> “Amazon is the most popular retailer for purchasing bedroom textiles products, followed by Dunelm and ASDA. Key Highlights Amazon holds the highest conversion rate in the overall bedroom textiles market followed by Dunelm”

- **Quelle:** [GlobalData – UK Home: Bedroom Textiles (Store-Seite)](https://www.globaldata.com/store/report/uk-bedroom-textiles-market-analysis/)
- **Datum der Quelle:** 2026-07-30 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** n=2.000, UK, 2026
- **Einordnung/Einschränkung:** Rangfolge aus einer Verbraucherbefragung, öffentlich ohne Prozentwerte. Ein reiner Onlinehändler führt bei Schlafzimmertextilien.
- **Wahrheits-Check:** *bestätigt*. Wortlaut per curl exakt gefunden.

### (b) GlobalData – Schlafzimmertextilien 2026: Kaufkriterien

#### G6-21

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut GlobalData-Umfrage 2026 nannte die Mehrheit der britischen Käufer von Schlafzimmertextilien den Preis als Hauptkriterium, und die meisten recherchierten vor dem Kauf.**

> “A majority of respondents cited price as the driver of choice for their bedroom textiles purchases Most bedroom textiles consumers undertook some research before buying”

- **Quelle:** [GlobalData – UK Home: Bedroom Textiles (Store-Seite)](https://www.globaldata.com/store/report/uk-bedroom-textiles-market-analysis/)
- **Datum der Quelle:** 2026-07-30 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** n=2.000, UK, 2026
- **Einordnung/Einschränkung:** Nur qualitative Aussagen ('majority', 'most') ohne Prozentwerte, die Detailtabellen liegen hinter der Paywall. Passt zu den Dunelm-Beobachtungen in G6-06.
- **Wahrheits-Check:** *bestätigt*. Wortlaut per curl exakt gefunden.

### (b) GlobalData – Schlafzimmertextilien 2017 (veraltet)

#### G6-22

⚠️ EINGESCHRÄNKT · Angle: Markt

**GlobalData prognostizierte 2017 ein Wachstum des britischen Marktes für Schlafzimmertextilien um insgesamt 12,5 % zwischen 2017 und 2022. Damals erfolgten knapp über 80 % der Käufe als Ersatz vorhandener Textilien.**

> “The UK bedroom textiles market is set to grow by 12.5% between 2017 and 2022, with just over 80% of purchases made to replace existing textiles and around 58% made to achieve a new look, according to GlobalData”

- **Quelle:** [GlobalData – Pressemitteilung 'Scandinavian lifestyle trends will help drive UK bedroom textiles market growth to 2022' (Byline Kristian Jackson; zitiert Retail Analyst Sarah Johns)](https://www.globaldata.com/media/retail/scandinavian-lifestyle-trends-will-help-drive-uk-bedroom-textiles-market-growth-to-2022/)
- **Datum der Quelle:** 2017-04-20 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Echte GlobalData-Pressemitteilung, aber neun Jahre alt und für einen abgelaufenen Prognosezeitraum. 12,5 % ist ein Gesamtwachstum, keine Jahresrate. Die Ersatzkauf-Quote taugt nur als historischer Hinweis.
- **Wahrheits-Check:** *korrigiert*. Wortlaut per curl gefunden, Datum 20 Apr 17 bestätigt. Korrigiert: Die Byline lautet Kristian Jackson, Sarah Johns ist nur die zitierte Analystin. Wortlaut vervollständigt.

### (b) GlobalData – Pillows & duvets 2024 (nicht prüfbar)

#### G6-23

❌ NICHT BELEGT / MYTHOS · Angle: Markt, B Wechseljahre

**Die Angabe, 'Pillows & duvets' hätten im Mai 2024 die höchste Kaufquote aller Schlafzimmertextilien gehabt, mit Frauen als wichtigster Käufergruppe, ist derzeit nicht prüfbar.**

> “Pillows & duvets had the highest penetration as of May 2024 with female buyers being the leading demography.”

- **Quelle:** [GlobalData Report-Store (frühere Ausgabe 'UK Bedroom Textiles', nur als Such-Snippet sichtbar)](https://www.globaldata.com/store/?p=1907364)
- **Datum der Quelle:** 2024 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** unbekannt (frühere GlobalData-Konsumentenumfrage)
- **Einordnung/Einschränkung:** Der Satz steht nur im Suchmaschinen-Index. Die URL leitet auf die Ausgabe 2026 weiter (curl: HTTP 502; WebFetch: Seite vom 30.07.2026 ohne diesen Satz). Ein Archivabruf war nicht möglich (429/Egress blockiert). Nicht in Ads verwenden.
- **Wahrheits-Check:** *bestätigt*. URL selbst per curl und WebFetch aufgerufen: Weiterleitung auf die Ausgabe 2026, der Satz fehlt. Unbelegtheit bestätigt. Die Faktaussage selbst gilt als nicht verwendbar.

### (c) Mintel – Homewares-Käuferquote 2026

#### G6-24

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Mintel haben 78 % der Erwachsenen in UK im vergangenen Jahr Homewares gekauft, gegenüber 86 % im Jahr 2023.**

> “78% of UK adults have bought homewares in the past year, a decline from 86% in 2023.”

- **Quelle:** [Mintel – UK Homewares Retailing Market Report 2026 (Store-Seite)](https://store.mintel.com/report/uk-homewares-retailing-market-report)
- **Datum der Quelle:** 2026-02-24 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Mintel-Verbraucherbefragung UK; n und Feldzeit auf der Seite nicht angegeben
- **Einordnung/Einschränkung:** Öffentlich sichtbare Mintel-Zahl, Methodik nicht öffentlich (nur als Kapitel 'Consumer research methodology' im Inhaltsverzeichnis). Analystenzitat (Sam Nguyen, Senior Retail Analyst): 'An improved housing market has provided a welcome boost for the homewares sector. However, the landscape has become more competitive, especially on price.'
- **Wahrheits-Check:** *bestätigt*. Wortlaut per curl exakt gefunden, datePublished 2026-02-24 im Seitenquelltext bestätigt.

### (c) Mintel – Kaufkanal Homewares

#### G6-25

⚠️ EINGESCHRÄNKT · Angle: Markt

**Mintel stellt für 2026 fest, dass physische Läden ihre Position als wichtigster Kaufkanal für Homewares in UK gestärkt haben. Die angenommene Online-Dominanz nach der Pandemie habe sich umgekehrt.**

> “Physical stores have strengthened their position as the main purchasing channel, reversing an assumed post-pandemic online dominance and highlighting an enduring appetite for in-person inspiration.”

- **Quelle:** [Mintel – UK Homewares Retailing Market Report 2026 (Store-Seite)](https://store.mintel.com/report/uk-homewares-retailing-market-report)
- **Datum der Quelle:** 2026-02-24 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Mintel-Verbraucherbefragung UK; n nicht angegeben
- **Einordnung/Einschränkung:** Qualitative Aussage ohne öffentliche Prozentwerte. Im Inhaltsverzeichnis steht außerdem 'Online engagement continues to dip, while in-store purchasing remains resilient'. Das widerspricht nicht dem schnelleren Online-Wachstum laut GlobalData und ONS.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Kapitelüberschrift per curl gefunden.

### (c) Mintel – Ausgabenprognose und Haushaltstextilien

#### G6-26

⚠️ EINGESCHRÄNKT · Angle: Markt

**Mintel prognostiziert, dass die britischen Ausgaben für Homewares zwischen 2025 und 2030 um 4,1 % wachsen. Haushaltstextilien bilden das größte Segment des Homewares-Markts.**

> “Spending on homewares is forecast to grow 4.1% between 2025 and 2030 Graph 2: market value forecast for homewares (including VAT), 2019-30 Household textiles make up the largest share Graph 3: homewares market segmentation, 2024-25”

- **Quelle:** [Mintel – UK Homewares Retailing Market Report 2026 (Inhaltsverzeichnis auf der Store-Seite)](https://store.mintel.com/report/uk-homewares-retailing-market-report)
- **Datum der Quelle:** 2026-02-24 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Beides sind nur Kapitelüberschriften, die Werte liegen hinter der Paywall. '4,1 % zwischen 2025 und 2030' ist mehrdeutig, vermutlich ein Gesamtwachstum über fünf Jahre. Nicht als 'jährlich' zitieren. Laut Grafiktitel inkl. MwSt., ob nominal oder real, ist nicht angegeben.
- **Wahrheits-Check:** *korrigiert*. Überschriften per curl gefunden. Korrigiert: Die frühere Angabe 'nominal' steht nicht auf der Seite und wurde gestrichen. Wortlaut um die Grafiktitel ergänzt.

### (c) Mintel – Schlafzimmermöbel/Betten 2024

#### G6-27

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Mintel-Bericht vom Oktober 2024 wird der britische Markt für Schlafzimmermöbel inklusive Betten und Matratzen (ohne Bettdecken) durch knappe Budgets und einen schwachen Immobilienmarkt gebremst.**

> “The bedroom furniture market continues to be impacted by stretched budgets and a subdued housing market, but the recovery of consumer finances and an uptick in housing transactions have provided the market with a much-needed boost.”

- **Quelle:** [Mintel – UK Bedroom Furniture Market Report 2024 (Store-Seite, Autorin Sam Nguyen)](https://store.mintel.com/report/uk-bedroom-furniture-market-report)
- **Datum der Quelle:** 2024-10-16 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Zwei Jahre alt. Laut Definition auf der Seite deckt der Bericht Divans, Bettgestelle, Matratzen und nicht gepolsterte Schlafzimmermöbel ab, Bettdecken nicht. Keine öffentlichen Marktwerte. Der Satz fährt fort: Erholung der Finanzen und mehr Immobilientransaktionen hätten dem Markt Auftrieb gegeben.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Segmentdefinition und datePublished 2024-10-16 per curl bestätigt. Wortlaut vervollständigt, um ihn nicht einseitig negativ zu kürzen.

### (c) Mintel – 'Half of Brits struggle to sleep' (veraltet)

#### G6-28

⚠️ EINGESCHRÄNKT · Angle: B Wechseljahre, Allgemein

**Laut Mintel-Bericht 'Sleep Aids UK 2017' gab damals die Hälfte (50 %) der Briten an, typischerweise schlecht zu schlafen. Im Schnitt schliefen sie 6 Stunden 51 Minuten.**

> “today half (50%) of all Brits say they typically struggle to sleep. Failing to hit the seven hour mark, the minimum sleep time recommended for adults, the average Brit says they sleep for just six hours and 51 minutes per day.”

- **Quelle:** [Mintel Press Centre – 'The wide awake club: Half of Brits struggle to sleep'](https://www.mintel.com/press-centre/the-wide-awake-club-half-of-brits-struggle-to-sleep/)
- **Datum der Quelle:** 2017-12-01 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Mintel Sleep Aids UK 2017; n, Feldzeit und Methodik in der Pressemitteilung nicht angegeben
- **Einordnung/Einschränkung:** Neun Jahre alt und ohne Stichprobenangabe. Als Störfaktoren nennt die Mitteilung Lärm (59 %), Licht (57 %), Technik vor dem Schlafen (34 %) und den Partner (29 %). Temperatur, Hitze oder Bettwaren werden nicht genannt. Für Ads höchstens mit Jahresangabe 2017.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Datum 01.12.2017 per curl bestätigt. Korrigiert: Die Mitteilung nennt nicht 'nur Lärm und Licht', sondern auch Technik (34 %) und Partner (29 %). Bestätigt: kein Bezug zu Temperatur oder Bettwaren.

### (d) ONS Family Spending – Schlafzimmertextilien

#### G6-29

✅ BELEGT · Angle: Markt

**UK-Haushalte gaben im Finanzjahr April 2024 bis März 2025 durchschnittlich £1,30 pro Woche für 'Schlafzimmertextilien einschließlich Bettdecken und Kissen' aus, zusammen £38 Mio. pro Woche.**

> “5.2.1 | Bedroom textiles, including duvets and pillows | 1.30 | 38 | 380 | 15.6 [Average weekly expenditure all households (£) | Total weekly expenditure (£ million) | Recording households in sample | Percentage standard error (full method)]”

- **Quelle:** [ONS – Family spending workbook 1: detailed expenditure and trends, Table A1 (UK, financial year ending 2025)](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Living Costs and Food Survey, 5.000 UK-Haushalte (gewichtet 28,71 Mio.), April 2024–März 2025; 380 Haushalte mit Ausgaben in dieser Kategorie
- **Einordnung/Einschränkung:** Amtliche Statistik für das gesamte UK. Relativer Standardfehler 15,6 %, das 95-%-Intervall reicht etwa von £0,90 bis £1,70 pro Woche. Die Kategorie enthält auch Kissen, ist also kein reiner Bettdecken-Wert.
- **Wahrheits-Check:** *bestätigt*. FYE-2025-XLSX selbst heruntergeladen und mit openpyxl gelesen: A1 Zeile 5.2.1 exakt wie angegeben, Release date 11 June 2026 auf der Dataset-Seite.

### (d) ONS Family Spending – Hochrechnung Jahreswert

#### G6-30

⚠️ EINGESCHRÄNKT · Angle: Markt

**Hochgerechnet ergeben die ONS-Werte für FYE 2025 Ausgaben der UK-Haushalte für Schlafzimmertextilien inklusive Bettdecken und Kissen von rund £2,0 Mrd. pro Jahr (£38 Mio. × 52 Wochen, eigene Rechnung).**

> “5.2.1 | Bedroom textiles, including duvets and pillows | 1.30 | 38 | 380 | 15.6”

- **Quelle:** [ONS – Family spending workbook 1, Table A1 (FYE 2025); eigene Hochrechnung](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Living Costs and Food Survey, 5.000 Haushalte, UK, FYE 2025
- **Einordnung/Einschränkung:** £38 Mio. × 52 = £1,976 Mrd. Mit ±1,96 × 15,6 % ergibt sich eine Spanne von etwa £1,4 bis £2,6 Mrd. Das ist eine eigene Rechnung, keine ONS-Angabe, und gilt nur für Privathaushalte. Die Kategorie enthält Kissen und weitere Textilien. Als Größenordnung brauchbar, nicht als 'Bettdecken-Markt'.
- **Wahrheits-Check:** *bestätigt*. Ausgangswert in der XLSX bestätigt, Rechnung nachvollzogen.

### (d) ONS Family Spending – Haushaltstextilien gesamt

#### G6-31

✅ BELEGT · Angle: Markt

**UK-Haushalte gaben im FYE 2025 im Schnitt £2,40 pro Woche für Haushaltstextilien aus (£70 Mio. pro Woche insgesamt). Davon entfielen £1,30 auf Schlafzimmertextilien und £1,10 auf andere Textilien wie Kissen, Handtücher und Vorhänge.**

> “5.2 | Household textiles | 2.40 | 70 | 970 | 10.7 / 5.2.2 | Other household textiles, including cushions, towels, curtains | 1.10 | 32 | 970 | 14.4”

- **Quelle:** [ONS – Family spending workbook 1, Table A1 (UK, FYE 2025)](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** LCF, 5.000 Haushalte, UK, FYE 2025; 970 Haushalte mit Ausgaben für Haushaltstextilien
- **Einordnung/Einschränkung:** Amtliche Tabelle, Standardfehler 10,7 %. Zum Vergleich FYE 2024: Haushaltstextilien £2,20 pro Woche (£61 Mio.; 740 Haushalte; SE 12,4 %).
- **Wahrheits-Check:** *bestätigt*. Beide Zeilen in A1 der FYE-2025-XLSX exakt bestätigt, Vergleichswert aus der FYE-2024-XLSX.

### (d) ONS Family Spending – Einkommensgruppen

#### G6-32

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Haushalte im neunten und zehnten Bruttoeinkommens-Dezil gaben im FYE 2025 durchschnittlich £4,50 pro Woche für Haushaltstextilien aus, Haushalte im untersten Dezil £1,90.**

> “5.2 | Household textiles | 1.90 | 1.20 | 1.40 | 3.00 | 1.70 | 2.00 | 2.00 | 2.20 | 4.50 | 4.50 | 2.40 [Dezile 1–10 | alle Haushalte]”

- **Quelle:** [ONS – Family spending workbook 1, Table A6 'Detailed household expenditure by gross income decile group' (UK, FYE 2025)](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/familyspendingworkbook1detailedexpenditureandtrends)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** LCF, 440–540 Haushalte je Dezil, UK, FYE 2025
- **Einordnung/Einschränkung:** Amtlich, aber mit kleinen Fallzahlen je Dezil und ohne Standardfehler in A6. Der unregelmäßige Verlauf (Dezil 2 £1,20, Dezil 4 £3,00) zeigt das Rauschen. Die Tendenz ist plausibel, die Einzelwerte sind unsicher. Im FYE 2024 sah die Verteilung anders aus (Dezil 10: £6,20, Dezil 1: £0,70).
- **Wahrheits-Check:** *bestätigt*. A6 Zeile 5.2 und die Fallzahlen je Dezil (520/540/510/510/500/500/500/470/500/440) in der XLSX bestätigt.

### (d) ONS Family Spending – Mythos Ausgabensprung

#### G6-33

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Aussage, die Ausgaben britischer Haushalte für Bettdecken und Schlafzimmertextilien seien binnen eines Jahres um rund 44 % gestiegen (von £0,90 auf £1,30 pro Woche), ist statistisch nicht belegt.**

> “While sample sizes increased in FYE 2025, they remain small, and users should be aware that estimates for lower-level expenditure categories in the underlying data are subject to greater uncertainty”

- **Quelle:** [ONS – Family spending in the UK: April 2024 to March 2025 (Bulletin) sowie Workbook 1, Table A1 FYE 2024 und FYE 2025](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/bulletins/familyspendingintheuk/april2024tomarch2025)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** LCF FYE 2024: 4.210 Haushalte (290 mit Ausgaben für Schlafzimmertextilien, SE 12,6 %); FYE 2025: 5.000 (380, SE 15,6 %)
- **Einordnung/Einschränkung:** Beide Einzelwerte sind amtlich (FYE 2024: '5.2.1 | Bedroom textiles, including duvets and pillows | 0.90 | 26 | 290 | 12.6'). Eigene Prüfung: Differenz £0,40, Standardfehler der Differenz etwa £0,23, also z ≈ 1,7 und nicht signifikant auf dem 5-%-Niveau. Zudem sind es Nominalwerte. ONS: 'no formal significance testing has been undertaken'. Kein Wachstumstrend ableitbar.
- **Wahrheits-Check:** *korrigiert*. Bulletin-Zitat und beide Tabellenwerte selbst bestätigt. Korrigiert: Die Intervalle (ca. £0,68–1,12 bzw. £0,90–1,70) überschneiden sich nur teilweise, nicht 'deutlich'. Die Begründung stützt sich jetzt auf einen expliziten Differenztest.

### (d) ONS Family Spending – Gesamtausgaben

#### G6-34

✅ BELEGT · Angle: Markt

**Die durchschnittlichen wöchentlichen Haushaltsausgaben in UK stiegen im FYE 2025 auf £676,60 (+9 % nominal, +5 % real). Davon entfielen £40,60 pro Woche auf Haushaltswaren und -dienstleistungen.**

> “Average weekly household expenditure increased to £676.60, a nominal increase of £53.30 (9%) from the previous year; after accounting for inflation there was a real-terms increase of £35.10 (5%).”

- **Quelle:** [ONS – Family spending in the UK: April 2024 to March 2025 (Bulletin); Workbook 1 Table A1 ('5 | Household goods & services | 40.60')](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/bulletins/familyspendingintheuk/april2024tomarch2025)
- **Datum der Quelle:** 2026-06-11 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Living Costs and Food Survey, 5.000 Haushalte, UK, April 2024–März 2025
- **Einordnung/Einschränkung:** Amtlicher Hauptwert für das gesamte UK. Die Daten reichen nur bis März 2025. Schlafzimmertextilien machen rund 0,2 % der Gesamtausgaben aus (eigene Rechnung).
- **Wahrheits-Check:** *bestätigt*. Bulletin-Satz per curl exakt gefunden, Release date 11 June 2026. A1-Zeile '5 | Household goods & services | 40.60' in der XLSX bestätigt.

### (e) HMRC/Zolltarif – richtige Warennummer

#### G6-35

✅ BELEGT · Angle: Markt

**Im britischen Zolltarif stehen Bettdecken unter 9404 40 ('Quilts, bedspreads, eiderdowns and duvets (comforters)'), aufgeteilt in 9404 40 10 (Federn/Daunen) und 9404 40 90 (andere). 9404 90 ist die Restposition 'Other', u. a. für Kissen und Polster.**

> “9404400000 Quilts, bedspreads, eiderdowns and duvets (comforters) | 9404401000 Filled with feathers or down | 9404409000 Other | 9404900000 Other | 9404901000 Filled with feathers or down | 9404909000 Other”

- **Quelle:** [UK Government – UK Integrated Online Tariff (Trade Tariff), Heading 9404 (API v2)](https://www.trade-tariff.service.gov.uk/api/v2/headings/9404)
- **Datum der Quelle:** Live-Tarif, abgerufen 2026-10-08 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Offizieller UK-Zolltarif. In den uktradeinfo-Daten gibt es Werte unter 9404 40 erst ab Januar 2022, davor nur unter 9404 90. Die Aufteilung kam mit der HS-Revision 2022.
- **Wahrheits-Check:** *korrigiert*. API am 08.10.2026 per curl selbst abgefragt (HTTP 200), Codes und Beschreibungen exakt bestätigt. Nur das Datumsfeld wurde von 'unbekannt' auf das Abrufdatum präzisiert.

### (e) HMRC – Mythos CN 9404 90

#### G6-36

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Annahme, britische Bettdecken-Importe ließen sich über CN 9404 90 messen, ist seit 2022 überholt. Seither stehen Bettdecken unter 9404 40, und 9404 90 erfasst vor allem Kissen, Polster und Sitzkissen.**

> “Cn8LongDescription 94049090: "Articles of bedding and similar furnishing, fitted with springs or stuffed or internally filled with any material or of cellular rubber or plastics (excl. filled with feather or down, mattress supports, mattresses, sleeping bags, pneumatic or water mattresses and blankets, quilts, bedspreads, eiderdowns and duvets "comforters")"”

- **Quelle:** [HMRC uktradeinfo – API, Commodity-Tabelle](https://api.uktradeinfo.com/Commodity?$filter=CommodityId eq 94044010 or CommodityId eq 94044090)
- **Datum der Quelle:** Live-Daten, abgerufen 2026-10-08 · **Typ:** Behörde/NHS/Statistikamt
- **Einordnung/Einschränkung:** Die HMRC-Beschreibung von 9404 90 90 schließt 'quilts, bedspreads, eiderdowns and duvets' ausdrücklich aus. Wer heute 9404 90 auswertet, misst überwiegend Kissen und Polster (2025 rund £349 Mio., siehe G6-41).
- **Wahrheits-Check:** *korrigiert*. Commodity-API selbst abgefragt. Unbelegtheit der Annahme bestätigt. Wortlaut durch den stärkeren Beleg ersetzt (ausdrücklicher Ausschluss in der 9404-90-Beschreibung), Datumsfeld präzisiert.

### (e) HMRC – Importwert Bettdecken 2025

#### G6-37

✅ BELEGT · Angle: Markt

**UK importierte 2025 Steppdecken, Tagesdecken und Bettdecken (Warennummer 9404 40, aus EU und Nicht-EU) im Zollwert von £43,3 Mio. bei 9.063 Tonnen, nach £34,7 Mio. im Jahr 2024 (+24,8 %).**

> “OTS, CommodityId 94044010+94044090, FlowTypeId 1 (EU Imports) + 3 (Non-EU Imports), Summe Value 2025: 43,331,063 (EU 9,276,349; Non-EU 34,054,714); NetMass 9,062,746; Summe Value 2024: 34,726,146; SuppressionIndex 0”

- **Quelle:** [HMRC uktradeinfo – Overseas Trade Statistics (OTS) API, eigene Aggregation](https://api.uktradeinfo.com/OTS?$apply=filter((CommodityId eq 94044010 or CommodityId eq 94044090) and (FlowTypeId eq 1 or FlowTypeId eq 3) and MonthId ge 202201)/groupby((MonthId,CommodityId,FlowTypeId),aggregate(Value with sum as V)))
- **Datum der Quelle:** 2026-09-11 (HMRC-OTS-Veröffentlichung für Juli 2026; API-Abruf 2026-10-08) · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Vollerhebung Zollanmeldungen; Daten bis Juli 2026
- **Einordnung/Einschränkung:** Amtliche HMRC-Handelsdaten ohne Unterdrückung. Einschränkungen: Es ist ein Zoll- bzw. Importwert, kein Ladenumsatz, und die Position enthält auch Tagesdecken und Quilts. Weitere Jahre: 2022 £34,2 Mio., 2023 £32,9 Mio. Keine Stückzahlen (SuppUnit 0). Exporte 2025: £2,7 Mio.
- **Wahrheits-Check:** *korrigiert*. Abfrage selbst ausgeführt, alle Werte exakt reproduziert (inkl. 2022/2023, Exporte £2.747.803, SuppressionIndex 0). Datumsfeld auf die GOV.UK-Veröffentlichung vom 11.09.2026 präzisiert.

### (e) HMRC – Daune vs. andere Füllung

#### G6-38

✅ BELEGT · Angle: Markt

**Von den britischen Bettdecken-Importen 2025 (9404 40) entfielen £9,3 Mio. auf Decken mit Feder- oder Daunenfüllung (9404 40 10) und £34,1 Mio. auf andere Füllungen wie Synthetik (9404 40 90).**

> “OTS Summe Value 2025: CommodityId 94044010 = 9,261,503; CommodityId 94044090 = 34,069,560 (FlowTypeId 1+3)”

- **Quelle:** [HMRC uktradeinfo – OTS API, eigene Aggregation](https://api.uktradeinfo.com/OTS?$apply=filter((CommodityId eq 94044010 or CommodityId eq 94044090) and (FlowTypeId eq 1 or FlowTypeId eq 3) and MonthId ge 202201)/groupby((MonthId,CommodityId,FlowTypeId),aggregate(Value with sum as V)))
- **Datum der Quelle:** 2026-09-11 (HMRC-OTS-Veröffentlichung für Juli 2026; API-Abruf 2026-10-08) · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Vollerhebung Zollanmeldungen 2025
- **Einordnung/Einschränkung:** Amtliche Daten. Etwa 79 % des Importwerts entfallen auf Ware ohne Daunen (eigene Rechnung). Über Tog-Werte und Endpreise sagt das nichts.
- **Wahrheits-Check:** *korrigiert*. Werte selbst exakt reproduziert, Datumsfeld präzisiert.

### (e) HMRC – Importe Januar–Juli 2026

#### G6-39

✅ BELEGT · Angle: Markt

**Von Januar bis Juli 2026 importierte UK Waren der Position 9404 40 (Bettdecken/Quilts) im Wert von £26,4 Mio., 4,5 % mehr als im Vorjahreszeitraum (£25,2 Mio.). Die Menge stieg um 10,4 % auf 5.528 Tonnen.**

> “OTS Summe Value MonthId 202601–202607 (94044010+94044090, FlowTypeId 1+3): 26,356,322; NetMass 5,528,127 / MonthId 202501–202507: 25,231,635; NetMass 5,008,923”

- **Quelle:** [HMRC uktradeinfo – OTS API, eigene Aggregation](https://api.uktradeinfo.com/OTS?$apply=filter((CommodityId eq 94044010 or CommodityId eq 94044090) and (FlowTypeId eq 1 or FlowTypeId eq 3) and MonthId ge 202201)/groupby((MonthId,CommodityId,FlowTypeId),aggregate(Value with sum as V)))
- **Datum der Quelle:** 2026-09-11 (HMRC-OTS-Veröffentlichung für Juli 2026; API-Abruf 2026-10-08) · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Vollerhebung, Januar–Juli 2026 vs. Januar–Juli 2025
- **Einordnung/Einschränkung:** Neueste Monatsdaten. Die Werte für 2026 sind vorläufig und können revidiert werden. Dass die Menge stärker wuchs als der Wert, deutet auf niedrigere Importpreise je kg hin (eigene Interpretation).
- **Wahrheits-Check:** *korrigiert*. Werte selbst exakt reproduziert (+4,46 % Wert, +10,37 % Menge), letzter Monat 202607. Datumsfeld präzisiert.

### (e) HMRC – Herkunftsländer

#### G6-40

✅ BELEGT · Angle: Markt

**China lieferte 2025 47,9 % des Werts der britischen Importe unter 9404 40 (£20,8 Mio.), vor Pakistan mit 11,2 % und Indien mit 9,1 %.**

> “OTS 2025, 94044010+94044090, FlowTypeId 1+3, groupby CountryId: 720 (China) 20,750,363; 662 (Pakistan) 4,837,402; 664 (India) 3,923,601; Gesamt 43,331,063”

- **Quelle:** [HMRC uktradeinfo – OTS API, Country-Tabelle, eigene Aggregation](https://api.uktradeinfo.com/OTS?$apply=filter((CommodityId eq 94044010 or CommodityId eq 94044090) and (FlowTypeId eq 1 or FlowTypeId eq 3) and MonthId ge 202501 and MonthId le 202512)/groupby((CountryId),aggregate(Value with sum as V)))
- **Datum der Quelle:** 2026-09-11 (HMRC-OTS-Veröffentlichung für Juli 2026; API-Abruf 2026-10-08) · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Vollerhebung 2025
- **Einordnung/Einschränkung:** Amtliche Daten, Anteile selbst berechnet. Herkunft heißt Ursprungs- bzw. Versandland laut Zollanmeldung, nicht Marke. Rund 21 % des Werts kamen aus der EU.
- **Wahrheits-Check:** *korrigiert*. Abfrage selbst ausgeführt, Länder-IDs über die Country-Tabelle geprüft (720 China, 662 Pakistan, 664 India). Datumsfeld präzisiert.

### (e) HMRC – Importe unter 9404 90 (keine Bettdecken)

#### G6-41

✅ BELEGT · Angle: Markt

**Unter der Restposition 9404 90 (u. a. Kissen und Polster, seit 2022 ohne Bettdecken) importierte UK 2025 Waren im Wert von rund £349 Mio. (£22,0 Mio. Feder/Daune, £327,4 Mio. andere).**

> “OTS Summe Value 2025 (FlowTypeId 1+3): CommodityId 94049010 = 21,956,404; CommodityId 94049090 = 327,373,351; 2021: 94049010 35,594,369; 94049090 338,289,366; 2022 gesamt 349,938,835”

- **Quelle:** [HMRC uktradeinfo – OTS API, eigene Aggregation](https://api.uktradeinfo.com/OTS?$apply=filter((CommodityId eq 94049010 or CommodityId eq 94049090) and (FlowTypeId eq 1 or FlowTypeId eq 3) and MonthId ge 202001)/groupby((MonthId,CommodityId,FlowTypeId),aggregate(Value with sum as V)))
- **Datum der Quelle:** 2026-09-11 (HMRC-OTS-Veröffentlichung für Juli 2026; API-Abruf 2026-10-08) · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Vollerhebung 2020–2026
- **Einordnung/Einschränkung:** Die Zahl selbst ist amtlich, aber KEIN Bettdecken-Wert. Auffällig: 9404 90 fiel nach der Ausgliederung von 9404 40 kaum (2021 £373,9 Mio., 2022 £349,9 Mio.). Daraus ist nicht entscheidbar, ob Bettdecken vorher nur einen kleinen Anteil hatten oder weiter teils unter 9404 90 angemeldet werden.
- **Wahrheits-Check:** *korrigiert*. Werte selbst reproduziert. URL von der generischen API-Adresse auf die konkrete Abfrage geändert, Wortlaut auf exakte Werte gesetzt, Datumsfeld präzisiert.

### (f) ONS – Online-Anteil Einzelhandel August 2026

#### G6-42

✅ BELEGT · Angle: Markt

**Der Online-Anteil am Einzelhandel in Großbritannien (ohne Nordirland, ohne Kraftstoff) stieg saisonbereinigt von 28,4 % im Juli 2026 auf 28,8 % im August 2026.**

> “The total spend (the sum of in-store and online sales) rose by 1.3% over the month. As a result, the proportion of sales made online rose from 28.4% in July 2026 to 28.8% in August 2026.”

- **Quelle:** [ONS – Retail sales, Great Britain: August 2026 (Statistical bulletin)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/august2026)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Monthly Business Survey, Retail Sales Inquiry, Großbritannien
- **Einordnung/Einschränkung:** Amtlich, neuester Monat (nächste Veröffentlichung am 23.10.2026). Gilt für Großbritannien, nicht das gesamte UK. Entspricht der Reihe MS6Y 'All retailing excluding automotive fuel' in der Internet-Tabelle. Laut Bulletin lagen die Online-Ausgaben 8,9 % über August 2025.
- **Wahrheits-Check:** *korrigiert*. Bulletin-Satz und Release-Daten per curl bestätigt, MS6Y = 28,8 (Juli 28,4) in der XLSX bestätigt. Korrigiert: 'gesamter Einzelhandel' präzisiert auf 'ohne Kraftstoff', wie es der Tabellenkopf ausweist.

### (f) ONS – Online-Anteil nicht saisonbereinigt

#### G6-43

✅ BELEGT · Angle: Markt

**In der nicht saisonbereinigten ONS-Reihe J4MC lag der Online-Anteil am Einzelhandel in Großbritannien im August 2026 bei 27,3 % (wöchentlich £2.563,7 Mio. online von £9.403,8 Mio. gesamt).**

> “INTERNET – Internet Retail Sales (non seasonally adjusted): 2026 Aug | 9403.8 | 2563.7 | 27.3 [Average weekly value for all retailing (£ million) | Average weekly value for Internet retail sales (£ million) | Internet sales as a percentage of total retail sales (%), J4MC]”

- **Quelle:** [ONS – Retail Sales Index internet sales (internetreferencetables.xlsx, August 2026)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/datasets/retailsalesindexinternetsales)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry, Großbritannien
- **Einordnung/Einschränkung:** Amtlich. Erklärt, warum Sekundärquellen unterschiedliche Werte nennen: Es gibt eine saisonbereinigte (MS6Y, 28,8 %) und eine nicht saisonbereinigte Reihe (J4MC, 27,3 %). In Ads immer die Reihe angeben.
- **Wahrheits-Check:** *bestätigt*. XLSX selbst geladen (Cover: 'published at 7.00am 18 September 2026'), Zeile 2026 Aug exakt bestätigt.

### (f) ONS – Online-Anteil 'Household goods stores'

#### G6-44

✅ BELEGT · Angle: Markt

**Bei Haushaltswarenhändlern mit Ladengeschäft ('Household goods stores') in Großbritannien lag der Online-Anteil im August 2026 bei 28,8 % saisonbereinigt bzw. 27,5 % nicht saisonbereinigt. Im August 2025 waren es 25,4 % bzw. 23,7 %.**

> “ISCPSA3 – Internet sales as a proportion of all retailing (seasonally adjusted), Household goods stores (MS77): 2026 Aug 28.8; 2025 Aug 25.4 / ISCPNSA3 (non-seasonally adjusted), Household goods stores (KQ7C): 2026 Aug 27.5; 2025 Aug 23.7”

- **Quelle:** [ONS – Retail Sales Index internet sales (internetreferencetables.xlsx, August 2026)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/datasets/retailsalesindexinternetsales)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry, Großbritannien
- **Einordnung/Einschränkung:** Amtlich. Gemessen wird der Online-Anteil am Umsatz von Händlern mit Laden (Eisenwaren, Elektrogeräte, Möbel/Leuchten/Haushaltsartikel), nicht der Online-Anteil aller Haushaltswaren-Käufe. Reine Onlinehändler zählen zu 'Non-store retailing'. Gilt für Großbritannien.
- **Wahrheits-Check:** *bestätigt*. Blätter ISCPSA3 und ISCPNSA3 der XLSX selbst gelesen, alle vier Werte exakt bestätigt.

### (f) ONS – Online-Wachstum Household goods stores

#### G6-45

✅ BELEGT · Angle: Markt

**Der nicht saisonbereinigte Online-Umsatz der Haushaltswarenhändler mit Laden in Großbritannien lag im August 2026 nominal 22,8 % über dem Vorjahresmonat. Saisonbereinigt erreichte er im Schnitt £213,6 Mio. pro Woche.**

> “ISCPNSA1 – Internet sales: value non-seasonally adjusted percentage change on same month a year earlier, Household goods stores (KP3V): 2026 Aug 22.8 / IntValSA – Value seasonally adjusted average weekly internet sales in pounds million, Household goods stores (MZY2): 2026 Aug 213.6”

- **Quelle:** [ONS – Retail Sales Index internet sales (internetreferencetables.xlsx, August 2026)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/datasets/retailsalesindexinternetsales)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** Retail Sales Inquiry, Großbritannien
- **Einordnung/Einschränkung:** Amtlich und nominal, also nicht preisbereinigt. Monatswerte schwanken (Juni 2026 +20,1 %, Juli +17,5 %; saisonbereinigt August +20,3 %, KP8J). Es geht um alle Haushaltswarenhändler mit Laden, nicht um Bettwaren.
- **Wahrheits-Check:** *bestätigt*. KP3V und MZY2 in der XLSX exakt bestätigt, zusätzlich der saisonbereinigte Wert KP8J 20,3.

### (f) ONS – Abgrenzung 'Household goods stores'

#### G6-46

✅ BELEGT · Angle: Markt

**Die ONS-Gruppe 'Household goods stores' (Agg 7) umfasst Eisenwaren/Farben/Glas, Elektro-Haushaltsgeräte sowie Möbel, Leuchten und sonstige Haushaltsartikel. Sie hat 2025 ein Gewicht von 6,91 % im Einzelhandelsindex. Textil-Fachgeschäfte (SIC 47.51) zählen dagegen zur Gruppe Textil, Bekleidung und Schuhe.**

> “Household goods stores | Agg7 | 6.91 / Hardware, paints and glass | 2.52 | 47.52 / Electrical household appliances | 1.3 | 47.54 / Furniture, lighting equipment and household articles not elsewhere classified | 2.89 | 47.59 / [Clothing(Agg5):] Textiles | 0.11 | 47.51”

- **Quelle:** [ONS – Retail Sales Index categories and their percentage weights (indexcatweights2025.xlsx)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/datasets/retailsalesindexcategoriesandtheirpercentageweights)
- **Datum der Quelle:** 2026-03-27 · **Typ:** Behörde/NHS/Statistikamt
- **Einordnung/Einschränkung:** Amtliche Definition, nötig, um G6-44 und G6-45 richtig zu lesen. Das Bulletin definiert: 'Non-store retailing refers to retailers that do not have a store presence. While the majority is made up of online retailers, it also includes other retailers, such as street stalls and markets.'
- **Wahrheits-Check:** *bestätigt*. XLSX selbst gelesen, alle Gewichte exakt bestätigt. Release date 27 March 2026 auf der Dataset-Seite. Die Non-store-Definition steht wörtlich im Bulletin vom August 2026.

### (f) Mythos – 'Homewares werden überwiegend online gekauft'

#### G6-47

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die Behauptung, die meisten Homewares würden in UK inzwischen online gekauft, ist nicht belegt. Bei Haushaltswarenhändlern mit Laden liegt der Online-Anteil bei 27,5 % (nicht saisonbereinigt) bzw. 28,8 % (saisonbereinigt; ONS, August 2026, Großbritannien), und Mintel nennt physische Läden als Hauptkaufkanal.**

> “Physical stores have strengthened their position as the main purchasing channel, reversing an assumed post-pandemic online dominance and highlighting an enduring appetite for in-person inspiration.”

- **Quelle:** [Mintel – UK Homewares Retailing Market Report 2026; ONS – Retail Sales Index internet sales (August 2026)](https://store.mintel.com/report/uk-homewares-retailing-market-report)
- **Datum der Quelle:** 2026-02-24 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Die ONS-Zahlen (G6-44) und Mintel widersprechen der Behauptung. Dunelms 42 % 'digital' enthalten Click & Collect und Tablet-Käufe im Laden (G6-02). Einschränkung: Reine Onlinehändler wie Amazon sind in der ONS-Gruppe nicht enthalten, und den Online-Anteil aller Homewares-Käufe misst keine öffentliche Quelle. Korrekt formulierbar: 'online wächst schneller' (GlobalData G6-14, ONS G6-45).
- **Wahrheits-Check:** *korrigiert*. Mintel-Satz und ONS-Werte selbst bestätigt. Korrigiert: 'rund 28–29 %' auf die exakten Werte 27,5 % bzw. 28,8 % präzisiert, Region ergänzt.

### Mythos – UK-Bettwarenmarkt £4,2–4,5 Mrd.

#### G6-48

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die online kursierende Zahl, der britische Bettwarenmarkt erreiche 2026 £4,2 bis 4,5 Mrd. und Bettdecken und Kissen hätten daran 25 % Anteil, ist nicht belegt.**

> “Created by SourceReady AI agent · 2026-4-15 ... The UK bedding market in 2026 is projected to reach £4.2 billion to £4.5 billion ... Mattresses 45% ... Bed Linen 30% ... Duvets & Pillows 25%”

- **Quelle:** [SourceReady – UK Bedding Market Report 2026: Trends, Forecasts & Analysis](https://www.sourceready.com/report/detail/uk-bedding-market-report-2026)
- **Datum der Quelle:** 2026-04-15 · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Die Seite ist laut eigener Angabe KI-generiert und nennt keine überprüfbare Quelle. Sie zählt Matratzen mit (45 %). Zum Vergleich: Die ONS-Haushaltsausgaben für Schlafzimmertextilien liegen bei rund £2,0 Mrd. pro Jahr (G6-30), die Bettdecken-Importe bei £43 Mio. Zollwert (G6-37). Nicht in Ads oder Pitches verwenden.
- **Wahrheits-Check:** *korrigiert*. Seite per curl selbst gelesen, Kennzeichnung 'Created by SourceReady AI agent · 2026-4-15' und Zahlen bestätigt. Korrigiert: Die Behauptungen über eine widersprüchliche 'Sleep Products'-Schwesterseite und über Mordor, MarkWide und ReportCubes wurden nicht selbst geprüft und daher aus der Begründung gestrichen.

### (b) GlobalData UK Home Textiles – Marktgröße und Prognose

#### G6-V01

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut GlobalData-Daten, die der schottische Gründungsservice Business Gateway in Lizenz wiedergibt, war der britische Heimtextilien-Markt 2024 £6.068 Mio. wert und soll bis 2029 auf £6.726 Mio. wachsen. Schlafzimmertextilien sind die größte Heimtextilien-Kategorie und sollen wertmäßig am stärksten wachsen.**

> “The UK home textiles market was worth £6,068 million in 2024 and is forecast to grow to £6,726 million in 2029, a CAGR of 2.4% over the five-year period. ... The largest home textiles category, bedroom textiles, will see the highest growth by value as consumers make quick refreshes to their homes and invest in quality fabrics, trading up where they can. (GlobalData Explorer, Home Textiles, June 2025, This content is reproduced under license from GlobalData PLC, Copyright 2026).”

- **Quelle:** [Business Gateway (Scotland) – Market Report 'Sewing' (aktualisiert Mai 2026), zitiert GlobalData Explorer, Home Textiles, June 2025](https://www.bgateway.com/media/4bchl2tr/market-report-sewing-may-2026.pdf)
- **Datum der Quelle:** 2026-05 (Business-Gateway-Pack); GlobalData-Daten Stand Juni 2025 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Lizenzierte Wiedergabe von GlobalData-Daten durch einen öffentlich finanzierten Beratungsdienst, keine GlobalData-Pressemitteilung. Methodik, Abgrenzung und MwSt.-Basis sind nicht angegeben. 2029 ist eine Prognose. Die genannte CAGR von 2,4 % passt nicht zu den Eckwerten, denn £6.068 Mio. → £6.726 Mio. über fünf Jahre ergibt etwa 2,1 % pro Jahr (eigene Rechnung). Für Bettdecken allein gibt es keine Zahl.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. PDF per curl/pdftotext selbst gelesen, Absatz wörtlich gefunden, 'updated by Business Gateway in May 2026' bestätigt (PDF erstellt 29.05.2026). CAGR-Unstimmigkeit selbst nachgerechnet.

## Track 4B: Geschenkverhalten UK

*Prüf-Fazit: Der Track ist überwiegend solide recherchiert: 49 der 51 Original-Claims ließen sich an der angegebenen Fundstelle nachvollziehen. Korrekturen betrafen vor allem Wortlaut, URLs, Datumsangaben und Bezugsgruppen. Verworfen wurde nur 4B-38 (Vatertag Ø £54), weil die verlinkte Quelle die Zahlen nicht enthält. Herabgestuft wurde 4B-01 (PwC £24,6 Mrd.), weil es eine Hochrechnung ist und die PwC-Primärseite gesperrt bleibt. Belastbar für Ads sind vor allem YouGov (Medianbudgets, Muttertag), Which?/Deltapoll, Deloitte, ONS (veraltet) sowie gemessene Kartendaten. Händler-PR-Umfragen (Finder, VoucherCodes, eBay) und alle £-Mrd.-Hochrechnungen nur mit Quelle und als Absicht oder Schätzung formulieren. Für Bettdecken als Geschenk gibt es keinen Beleg; Aussagen wie „beliebtes Geschenk“ sind daher nicht zulässig.*

### 1. Weihnachten – Budget

#### 4B-01

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut PwC-Prognose (Festive Predictions, Dez. 2025) sollten UK-Verbraucher zu Weihnachten 2025 £24,6 Mrd. für Geschenke und Feiern ausgeben (+3,5 % gegenüber £23,7 Mrd. 2024). Pro Erwachsenem wären das im Schnitt £461 (2024: £449).**

> “UK consumers are set to spend £24.6billion on presents and celebrations over the Christmas period this year ... Average spending per adult is forecast to rise from £449 to £461.”

- **Quelle:** [PwC UK: Festive spending forecast to reach £24.6bn this year (Pressemitteilung, wiedergegeben von Insight DIY; PwC-Primärseite 403)](https://www.insightdiy.co.uk/news/festive-spending-forecast-to-reach-246bn-this-year/15891.htm)
- **Datum der Quelle:** 2025-12-12 · **Typ:** Presse
- **Stichprobe/Methodik:** Laut Suchzusammenfassung n=2.000 UK-Erwachsene, national repräsentativ, 31.10.–4.11.2025 (nicht selbst verifiziert). Insight DIY: Umfrage drei Wochen vor dem Budget.
- **Einordnung/Einschränkung:** Hochrechnung aus einer Absichtsumfrage, die Methodik ist nicht einsehbar (pwc.co.uk 403). Der Wert umfasst Geschenke UND Feiern/Essen, nicht nur Geschenke. Bei 3,6 % Inflation (Okt. 2025) bleibt real etwa keine Steigerung (laut Retail Insight Network). Gleiche Zahlen bei Grocery Gazette und Retail Insight Network (beide 12.12.2025).
- **Wahrheits-Check:** *herabgestuft*. Grocery Gazette geöffnet: £24,6 Mrd./+3,5 %/£461/£449 bestätigt, aber ohne Angabe, was enthalten ist. Insight DIY (gibt die PwC-Mitteilung wieder) bestätigt 'presents and celebrations' und £461 pro Erwachsenem. Die PwC-Seite bleibt gesperrt (WebFetch und curl 403). Als Prognose/Hochrechnung ohne einsehbare Methodik von BELEGT auf EINGESCHRAENKT herabgestuft; URL auf die Fundstelle mit vollständigerem Wortlaut geändert.

#### 4B-02

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut Finder/Censuswide planten Briten für Weihnachten 2025 im Schnitt £514 pro Person nur für Geschenke. 94 % wollten Geschenke kaufen, hochgerechnet £26,7 Mrd. insgesamt.**

> “Brits are expected to spend an average of £514 each on Christmas gifts in 2025. ... 94% of Brits plan to buy Christmas gifts for their loved ones, which is an impressive 52 million people.”

- **Quelle:** [Finder UK: Christmas statistics: What's the average spend in the UK?](https://www.finder.com/uk/christmas-shopping-statistics)
- **Datum der Quelle:** 2025-11-18 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Censuswide im Auftrag von Finder, n=2.000 UK-Erwachsene 18+, 14.–17.11.2025, quotiert nach Geschlecht/Alter/Region, ±2,2 %
- **Einordnung/Einschränkung:** Die Methodik ist offengelegt, es ist aber eine PR-Umfrage einer Vergleichsseite. Es sind geplante, keine gemessenen Ausgaben. Die Seite verwechselt 2024 und 2025 (z. B. £514 im Fließtext als 2024-Wert, 52 Mio. in den Highlights als 2024). Der Mittelwert wird durch Vielausgeber nach oben gezogen.
- **Wahrheits-Check:** *bestätigt*. Seite (Updated Nov 18, 2025) geöffnet. £514, 94 %/52 Mio., £26,7 Mrd. und Methodik bestätigt; die Jahresinkonsistenzen auf der Seite ebenfalls bestätigt.

#### 4B-05

✅ BELEGT · Angle: D Geschenk, Markt

**In der YouGov Big Survey (Nov. 2025) lag der Median der geschätzten Gesamtausgaben für Weihnachtsgeschenke bei £300 pro Person, für Weihnachten insgesamt (inkl. Essen, Reisen, Ausgehen) bei £550.**

> “the median total estimate given is £300. ... the median total Christmas spend amounts to £550.”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas – the cost of Christmas](https://yougov.com/en-gb/articles/53595-the-yougov-big-survey-on-christmas-the-cost-of-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov Big Survey on Christmas, n=4.243 GB-Erwachsene 18+, 19.–24.11.2025 (Angaben aus dem Hauptartikel 53587)
- **Einordnung/Einschränkung:** Unabhängiges Institut, große Stichprobe; der Median ist robuster als der Mittelwert. Basis sind Befragte mit Schätzung. Nur GB, ohne Nordirland.
- **Wahrheits-Check:** *bestätigt*. Artikel (28.11.2025, Dylan Difford) geöffnet, beide Medianwerte gefunden. n und Feldzeit im Hauptartikel 53587 bestätigt.

### 1. Weihnachten – Budget nach Alter

#### 4B-03

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut Finder/Censuswide planten Babyboomer für Weihnachten 2025 im Schnitt £416 für Geschenke (£577 insgesamt), die über 80-Jährigen („Silent Generation“) £576 für Geschenke (£865 insgesamt).**

> “Baby Boomers will be the most thrifty this Christmas, spending £577 each on average, and £416 on gifts. ... the silent generation, who plan to spend £865 in total, including £576 on gifts.”

- **Quelle:** [Finder UK: Christmas statistics: What's the average spend in the UK?](https://www.finder.com/uk/christmas-shopping-statistics)
- **Datum der Quelle:** 2025-11-18 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Censuswide/Finder, n=2.000 UK-Erwachsene, 14.–17.11.2025; Teilgruppengrößen nicht angegeben
- **Einordnung/Einschränkung:** Die Teilgruppen sind klein, besonders die 80+ in einer Online-Stichprobe mit n=2.000; ihre Größe ist nicht angegeben. PR-Umfrage. Für Ads höchstens als grobe Orientierung nutzen.
- **Wahrheits-Check:** *bestätigt*. Beide Sätze und alle vier Beträge auf der Seite gefunden.

### 1. Weihnachten – Budget/Kategorien

#### 4B-04

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut dem 'Shopping for Christmas Report 2025' von VoucherCodes.co.uk sollten 2025 in UK £11,59 Mrd. für Geschenke ausgegeben werden (+2,1 %), im Schnitt £443 pro Haushalt. Spielzeug (£2,13 Mrd.) und Elektronik (£2,03 Mrd.) führen; Deko liegt mit £0,63 Mrd. am niedrigsten.**

> “£11.59bn set to be spent on presents alone (+2.1% YoY) ... an average of £443 per household and 50.5% of all Christmas sales ... toys are topping the list of most popular gifts (£2.13bn) followed closely by electronics (£2.03bn).”

- **Quelle:** [Retail Times: Christmas shoppers set to splurge £91bn as retail sales rise 3.2% this year (VoucherCodes.co.uk Shopping for Christmas Report 2025)](https://retailtimes.co.uk/christmas-shoppers-set-to-splurge-91bn-as-retail-sales-rise-3-2-this-year/)
- **Datum der Quelle:** 2025-10-21 · **Typ:** Presse
- **Stichprobe/Methodik:** Im Artikel weder Institut noch n genannt. Laut früherer Suchzusammenfassung GlobalData, n=2.000 (nicht verifiziert).
- **Einordnung/Einschränkung:** Prognose im Auftrag eines Gutscheinportals, ohne Methodik im Artikel. 'Pro Haushalt' ist ein Mittelwert. Ein Homewares-Wert wird nicht genannt. Nicht mit PwC (pro Erwachsenem, inkl. Feiern) oder Finder (pro Person) vergleichbar.
- **Wahrheits-Check:** *korrigiert*. Zahlen bestätigt. Korrektur: Der Artikel nennt GlobalData nicht, nur den VoucherCodes-Report; Aussage und Stichprobenfeld angepasst. Deko-Wert (£0,63 Mrd.) ergänzt; einen Homewares-Wert gibt es nicht.

### 1. Weihnachten – Ausgaben für Eltern

#### 4B-06

✅ BELEGT · Angle: D Geschenk

**Laut YouGov (Nov. 2025) geben Briten für ein Weihnachtsgeschenk an ein Elternteil typischerweise £31–50 aus (Median-Kategorie).**

> “When it comes to buying gifts for parents, the median spend is between £31-50.”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas – the cost of Christmas](https://yougov.com/en-gb/articles/53595-the-yougov-big-survey-on-christmas-the-cost-of-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=4.243 GB-Erwachsene, 19.–24.11.2025
- **Einordnung/Einschränkung:** Unabhängiges Institut, aktuelle Daten, Median-Kategorie pro Elternteil. Eigene Schlussfolgerung: Ein Produkt deutlich über £50 liegt über dem typischen Budget für ein Elterngeschenk.
- **Wahrheits-Check:** *bestätigt*. Median £31–50 für Eltern auf der Seite bestätigt.

### 1. Weihnachten – Ausgaben für Enkel

#### 4B-07

✅ BELEGT · Angle: D Geschenk

**Laut YouGov (Nov. 2025) gibt knapp die Hälfte der Großeltern (46 %) bis £50 pro Enkelkind aus. Jede/r Fünfte (20 %) gibt mehr als £100 aus, 7 % weniger als £20.**

> “nearly half (46%) are spending up to £50 per child while the same number are going above that level. ... One in five grandparents (20%) spend more than £100 per grandchild, while 7% spend less than £20.”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas – the cost of Christmas](https://yougov.com/en-gb/articles/53595-the-yougov-big-survey-on-christmas-the-cost-of-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=4.243 GB-Erwachsene, 19.–24.11.2025 (Teilgruppe Großeltern)
- **Einordnung/Einschränkung:** Seriöse Quelle. Gemessen wird, was Großeltern verschenken, nicht was sie bekommen. Zeigt Großeltern als aktive Geschenkkäufer.
- **Wahrheits-Check:** *bestätigt*. 46 %, 20 % und 7 % auf der Seite bestätigt.

### 1. Weihnachten – Ausgaben für Partner

#### 4B-08

✅ BELEGT · Angle: D Geschenk, B Wechseljahre

**Laut YouGov (Nov. 2025) geben 46 % derer, die dem Partner etwas schenken, typischerweise weniger als £100 aus, 16 % mehr als £200. Männer geben häufiger über £100 aus als Frauen (50 % vs. 39 %).**

> “around half of those who buy a partner a Christmas present (46%) say they'd typically spend less than £100 ... including one in six (16%) who say they'd spend more than £200.”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas – the cost of Christmas](https://yougov.com/en-gb/articles/53595-the-yougov-big-survey-on-christmas-the-cost-of-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=4.243 GB-Erwachsene, 19.–24.11.2025
- **Einordnung/Einschränkung:** Seriöse Quelle. Relevant, falls die Decke als Partnergeschenk beworben wird (z. B. Angle B).
- **Wahrheits-Check:** *bestätigt*. 46 %, 16 % und 50 % vs. 39 % auf der Seite bestätigt.

### 1. Weihnachten – Ausgaben für Eltern/Großeltern (alt)

#### 4B-09

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Eine First-Choice-Umfrage unter Eltern ergab 2017 geplante Weihnachtsgeschenk-Budgets von £69 und £40 für 'parents and grandparents'. Die Zuordnung (£69 Eltern, £40 Großeltern) ergibt sich nur aus der Reihenfolge.**

> “parents and grandparents come next in the gift giving pecking order at £69 and £40.”

- **Quelle:** [TUI/First Choice Pressemitteilung: First Choice reveals true cost of Christmas](https://www.tui.co.uk/press/first-choice-reveals-true-cost-christmas/)
- **Datum der Quelle:** 2017-12-05 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 'Parents polled in a new survey', n und Zeitraum nicht angegeben
- **Einordnung/Einschränkung:** Veraltet (2017), nur Eltern befragt, PR-Umfrage eines Reiseveranstalters ohne Methodik. Unklar, ob die eigenen Eltern oder die Großeltern der Kinder gemeint sind. Für Ads stattdessen YouGov 2025 (4B-06) verwenden.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Datum bestätigt. Die Aussage 'für die eigenen Eltern' war eine Interpretation und wurde abgeschwächt, weil die Seite die Zuordnung nicht ausdrücklich nennt.

### 1. Weihnachten – Stimmung/Stress

#### 4B-10

✅ BELEGT · Angle: D Geschenk, Allgemein

**Laut Deloitte (Dez. 2025) finden 33 % der UK-Verbraucher Weihnachtseinkäufe stressig. 30 % wollten mehr ausgeben als im Vorjahr, 18 % weniger.**

> “Around one in three consumers (30%) in the UK are planning to spend more this Christmas ... Overall, just one in five (18%) UK consumers plan to spend less this Christmas compared with last year. ... A third of UK consumers find Christmas shopping (33%) stressful.”

- **Quelle:** [Deloitte UK: A third of UK consumers plan to spend more this Christmas, but many blame higher prices](https://www.deloitte.com/uk/en/about/press-room/a-third-of-uk-consumers-plan-to-spend-more-this-christmas-but-many-blame-higher-prices.html)
- **Datum der Quelle:** 2025-12-15 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** Deloitte ConsumerSignals, n=1.000 Erwachsene 18+ pro Land (7 europäische Märkte inkl. UK), Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Seriöse Quelle mit klarer Stichprobe, aber ohne £-Betrag. Von denen, die mehr ausgeben, nennt ein Drittel höhere Preise als Grund. Laut Mitteilung würden weniger Verbraucher bei Gutscheinen, Gastgeben zu Hause sowie Home-Deko/Saisonartikeln sparen (ohne Zahlen). 'Stress' ist eine Einstellung, kein Kaufverhalten.
- **Wahrheits-Check:** *bestätigt*. Wortlaut für 30 %, 18 % und 33 % wörtlich bestätigt, Datum 15.12.2025 bestätigt. Aussage zu Gutscheinen/Home-Deko in der Begründung ergänzt.

### 1. Weihnachten – Finanzsorgen

#### 4B-11

✅ BELEGT · Angle: D Geschenk, Allgemein

**Laut YouGov (Nov. 2025) machen sich 33 % der Briten zumindest ziemliche Sorgen über die Auswirkungen von Weihnachten auf ihre Finanzen. Bei Haushaltseinkommen unter £30.000 sind es 42 %, gar keine Sorgen haben 21 %.**

> “A third of Britons (33%) say they are typically at least fairly worried about the impact of Christmas ... this rising to 42% among those in households with incomes of under £30,000.”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas – the cost of Christmas](https://yougov.com/en-gb/articles/53595-the-yougov-big-survey-on-christmas-the-cost-of-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=4.243 GB-Erwachsene, 19.–24.11.2025
- **Einordnung/Einschränkung:** Seriöse Quelle; gibt den Kontext für preissensible Geschenkkäufe.
- **Wahrheits-Check:** *bestätigt*. 33 %, 42 % und 21 % auf der Seite bestätigt.

### 1. Weihnachten – Budget nach Alter (65+)

#### 4B-12

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer VoucherCodes-Umfrage (März 2025) planen Briten für Weihnachten im Schnitt £371,44 ein; die über 65-Jährigen geben mit £428,64 am meisten aus.**

> “Christmas is set to see an average spend of £371.44, with those aged 65+ spending the most on average (£428.64).”

- **Quelle:** [Retail Times: Brits set to spend more on mum than dad this year – plus Mother's Day deals under £25 (VoucherCodes.co.uk-Umfrage)](https://retailtimes.co.uk/brits-set-to-spend-more-on-mum-than-dad-this-year-plus-mothers-day-deals-under-25/)
- **Datum der Quelle:** 2025-03-25 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 'a new survey by VoucherCodes.co.uk'; n, Institut und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Händler-PR ohne Angabe von Stichprobe oder Institut. Unklar, ob nur Geschenke gemeint sind. Widerspricht Finder (Boomer am sparsamsten); die Altersaussage ist daher nicht als Fakt verwendbar.
- **Wahrheits-Check:** *korrigiert*. Wortlaut bestätigt. Die URL ?p=146341 leitet auf den Artikel weiter und wurde durch die endgültige URL ersetzt.

### 1. Weihnachten – Ältere als Käufer

#### 4B-13

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**In einer KPMG/OnePoll-Umfrage (Sept. 2023) erwarteten 39 % der UK-Verbraucher wegen der Lebenshaltungskosten ein kleineres Geschenkbudget. Über 65-Jährige sagten am seltensten, dass sie ihr Geschenkbudget kürzen müssten.**

> “the cost of living meant that they would have a smaller budget to buy gifts this year ... People aged 65 and over were least likely to say that they had to reduce their gift buying budget.”

- **Quelle:** [KPMG UK: Research shows likely cost of living hit to Christmas spending](https://kpmg.com/uk/en/media/press-releases/2023/10/research-shows-likely-cost-of-living-hit-to-christmas-spending.html)
- **Datum der Quelle:** 2023-10-20 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** OnePoll für KPMG UK, n=2.625 (Geschenkfrage), 1.–12.09.2023, UK
- **Einordnung/Einschränkung:** Seriös, aber veraltet (2023). Keine KPMG-UK-Weihnachtsumfrage 2025 gefunden; die KPMG-Holiday-Studie 2025 betrifft die USA.
- **Wahrheits-Check:** *bestätigt*. 39 %, die Aussage zu den 65+, n=2.625, Feldzeit und Datum 20.10.2023 bestätigt.

### 1. Weihnachten – Geschenkwünsche/Kategorien

#### 4B-14

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**In einer Statista-Umfrage (28.10.–10.11.2025) würden sich je 39 % der UK-Onliner über Kleidung/Textilien/Schuhe bzw. Gutscheine freuen, je 38 % über Geld bzw. Kosmetik/Parfum/Pflege und 36 % über Essen/Getränke.**

> “39 percent of the respondents said that they would be happy to get clothing, textiles, shoes”

- **Quelle:** [Statista: Christmas gifts desired by UK consumers 2025](https://statista.com/statistics/1084794/christmas-gifts-desired-by-uk-consumers)
- **Datum der Quelle:** 2025-11-27 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Statista-Online-Umfrage, n=1.044, UK-Online-Bevölkerung 18–80 J., 28.10.–10.11.2025, Mehrfachnennung
- **Einordnung/Einschränkung:** Werte sichtbar, Methodik angegeben. Aber: nur Online-Bevölkerung bis 80 Jahre, Mehrfachantworten. 'Textiles' ist nicht aufgeschlüsselt, ob Bettwaren dazugehören, bleibt offen.
- **Wahrheits-Check:** *korrigiert*. Alle Kategorien und Prozentwerte sowie die Methodik bestätigt. Datum auf das Seitendatum 27.11.2025 präzisiert, Essen/Getränke 36 % ergänzt.

### 1. Weihnachten – praktische/kuschelige Geschenke

#### 4B-15

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut YouGov (Dez. 2022) würden sich 88 % der Briten, die Weihnachten feiern, über einen Pullover und 81 % über Hausschuhe freuen. Bei den über 65-Jährigen sind es für Hausschuhe 80 %.**

> “nearly nine in ten Britons who celebrate Christmas (88%) saying they'd be happy to receive one ... 81% would be happy with a pair”

- **Quelle:** [YouGov: Most Britons would be pleased to receive socks, underwear or deodorant this Christmas](https://yougov.com/en-gb/articles/44751-which-traditionally-dubious-christmas-gifts-would-)
- **Datum der Quelle:** 2022-12-14 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, Basis: Briten, die Weihnachten feiern; n und Feldzeit nicht auf der Seite angegeben
- **Einordnung/Einschränkung:** Seriöses Institut, aber von 2022 und ohne Stichprobenangabe. Decken und Bettwaren wurden nicht abgefragt; die Daten belegen also nicht die Bettdecke als Wunschgeschenk.
- **Wahrheits-Check:** *bestätigt*. 88 %, 81 % und 80 % der 65+ bestätigt. Keine Erwähnung von Decken oder Bettwaren auf der Seite.

### 1. Weihnachten – Wunsch nach praktischen Geschenken

#### 4B-16

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut YouGov (2018) halten 30 % der Männer, aber nur 16 % der Frauen ein praktisches Geschenk für die beste Art von Weihnachtsgeschenk.**

> “Men are twice as likely as women to prefer a practical gift (30% of men versus 16% of women)”

- **Quelle:** [YouGov: Stuck for gift ideas? Brits genuinely want socks](https://yougov.com/en-gb/articles/22202-stuck-gift-ideas-brits-genuinely-want-socks)
- **Datum der Quelle:** 2018-12-18 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n und Feldzeit nicht auf der Seite angegeben
- **Einordnung/Einschränkung:** Veraltet (2018). Auf der Seite gibt es keinen Gesamtwert und keine Werte für 55+/65+, nur für 18–24 (22 %). Die Aussage 'Ältere wollen praktische Geschenke' ist damit NICHT belegbar.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum bestätigt; kein Alterswert für Ältere vorhanden.

### 1. Weihnachten – Überraschung vs. Wunschliste

#### 4B-17

✅ BELEGT · Angle: D Geschenk

**Laut YouGov (Nov. 2025) bekommen 44 % der Briten ihre Geschenke lieber als Überraschung, 32 % sagen lieber, was sie wollen, und 15 % wollen gar keine Geschenke.**

> “More Britons prefer their presents to be a surprise (44%) than to dictate what they get (32%). ... One in seven (15%) don't want any presents”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas](https://yougov.com/en-gb/articles/53587-the-yougov-big-survey-on-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=4.243 GB-Erwachsene 18+, 19.–24.11.2025
- **Einordnung/Einschränkung:** Seriöse Quelle, aktuell, große Stichprobe. Keine Altersaufschlüsselung auf der Seite.
- **Wahrheits-Check:** *bestätigt*. Wortlaut wörtlich bestätigt, ebenso n und Feldzeit.

### 1. Weihnachten – Wer kauft die Geschenke

#### 4B-18

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut YouGov (Nov. 2025) sagen 46 % der Frauen, dass sie alle Weihnachtsgeschenke einkaufen, gegenüber 10 % der Männer. Die Bezugsgruppe ist auf der Seite nicht definiert.**

> “Women are notably more likely than men to be stressed by Christmas (30% vs 20%) and to also have to be doing all the work, e.g. 46% say they do all the gift shopping vs 10% of men”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas](https://yougov.com/en-gb/articles/53587-the-yougov-big-survey-on-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=4.243 GB-Erwachsene, 19.–24.11.2025
- **Einordnung/Einschränkung:** Seriöse Quelle, aber die Basis ist unklar (alle Befragten, Paare oder Haushalte?). Nur mit Vorbehalt nutzen. Für das Targeting relevant: Frauen kaufen die Geschenke ein.
- **Wahrheits-Check:** *bestätigt*. Satz vollständig gefunden; Wortlaut um den Satzanfang ergänzt, damit die Bezugsgruppe (Frauen) erkennbar ist.

### 1. Weihnachten – unerwünschte Geschenke

#### 4B-19

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut Finder/Censuswide (Nov. 2024) haben 58 % der Erwachsenen schon einmal mindestens ein Weihnachtsgeschenk bekommen, das ihnen nicht gefällt. Finder schätzt den Wert auf £41 pro Person bzw. £1,27 Mrd. insgesamt.**

> “3 in 5 UK adults (58%), approximately 31 million people, have been given at least one Christmas gift they don't like. ... The total estimated spend on these unwanted gifts works out at £1.27 billion. ... As of 2024, the average value of unwanted gifts received per person is £41.”

- **Quelle:** [Finder UK: Unwanted gifts statistics](https://www.finder.com/uk/unwanted-gifts)
- **Datum der Quelle:** 2026-04-28 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Censuswide im Auftrag von Finder, n=2.000 Erwachsene 18+, 'throughout Great Britain', 8.–11.11.2024, quotiert nach Geschlecht/Alter/Region
- **Einordnung/Einschränkung:** PR-Umfrage. Die Hochrechnung auf £1,27 Mrd. wird nicht erklärt (rechnerisch ca. 31 Mio. × £41). Die Stichprobe deckt GB ab, die Überschrift spricht von UK. 'Jemals bekommen' ist keine jährliche Quote. Die Seite wurde im April 2026 aktualisiert, die Daten stammen von Nov. 2024.
- **Wahrheits-Check:** *korrigiert*. Zahlen bestätigt. Wortlaut zu £1,27 Mrd. und £41 auf den tatsächlichen Seitentext korrigiert ('works out at', 'As of 2024'). Methodik und Datum (Updated Apr 28, 2026) bestätigt.

### 1. Weihnachten – MYTHOS „Brits waste £5bn on unwanted gifts“

#### 4B-20

❌ NICHT BELEGT / MYTHOS · Angle: D Geschenk

**Die oft zitierte Zahl, Briten verschwendeten £5 Mrd. für unerwünschte Weihnachtsgeschenke, stammt aus einer Finder-Pressemitteilung von Dezember 2017 ohne nachvollziehbare Hochrechnung. Spätere Finder-Werte (£1,27 Mrd.) haben sie überholt.**

> “Research by price comparison site, finder.com has found that £5 billion will be wasted on unwanted Christmas gifts ... According to a survey of 2,000 UK adults, people received on average three gifts they didn't like, amounting to £41.70 each.”

- **Quelle:** [Finder UK Press Release December 2017: Brits expected to waste £5 billion on unwanted gifts this Christmas](https://www.finder.com/uk/media/press-release-december-2017-brits-expected-to-waste-5-billion-on-unwanted-gifts-this-christmas)
- **Datum der Quelle:** 2017-12-31 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Mortar London für finder.com, n=2.000 UK-Erwachsene, Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Die Mitteilung nennt weder Bevölkerungsbasis noch Rechenweg. Unklar ist auch, ob die 'drei Geschenke' alle Befragten oder nur Betroffene meinen. Andere 'Mrd.'-Zahlen widersprechen sich und sind selbst unbelegt: £2,3 Mrd. (2007, nur über einen Blog mit Reuters-Bezug), ~£1 Mrd. (Blumberg-Seite, undatiert, nicht selbst geprüft), £1,27 Mrd. (Finder 2024). Nicht in Ads verwenden.
- **Wahrheits-Check:** *bestätigt*. Ursprung bestätigt (Finder, 31.12.2017, Mortar London, n=2.000). Wortlaut auf den genauen Text korrigiert. Ein Rechenweg ist nicht vorhanden; der Mythos bleibt unbelegt. Die Gumtree-Zahl (£2,4 Mrd.) konnte ich nicht finden und habe sie aus der Begründung entfernt.

### 1. Weihnachten – Weiterverschenken

#### 4B-21

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut YouGov (Dez. 2020) halten 57 % der Briten das Weiterverschenken eines Geschenks für akzeptabel, 40 % haben es selbst schon getan.**

> “Overall, 57% of Britons think that re-gifting a present to another person is acceptable ... Two in five (40%) Britons say they have used an unwanted present from one person as a present for another”

- **Quelle:** [YouGov: Most Britons would not be too upset if someone passed on one of their gifts to someone else](https://yougov.com/en-gb/articles/33440-it-acceptable-re-gift-presents)
- **Datum der Quelle:** 2020-12-15 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n und Feldzeit nicht auf der Seite angegeben
- **Einordnung/Einschränkung:** Seriöses Institut, aber veraltet (2020) und ohne Stichprobenangabe auf der Seite.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum bestätigt.

### 1. Weihnachten – Rückgaben

#### 4B-22

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer Opinium-Umfrage für die Post Office (Feb. 2023) wollte ein Drittel der UK-Verbraucher mindestens ein Weihnachtsgeschenk von 2022 zurückgeben oder abgeben. Zurückgegeben werden sollten Geschenke im Wert von £232 Mio.**

> “one third of UK consumers will be returning or giving up at least one of the gifts they received for Christmas 2022 ... Gifts worth £232 million will be returned across the UK,”

- **Quelle:** [Opinium: Third of consumers plan to return or give up Christmas gifts](https://www.opinium.com/third-of-consumers-plan-to-return-or-give-up-christmas-gifts/)
- **Datum der Quelle:** 2023-02-01 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** Opinium im Auftrag von Post Office Ltd; n und Feldzeit nicht auf der Seite angegeben
- **Einordnung/Einschränkung:** Seriöses Institut, aber Auftragsstudie, veraltet (Weihnachten 2022), ohne n. Am häufigsten zurückgegeben: Kleidung/Schuhe (21 %) und nicht-elektrische Beauty-Artikel (18 %).
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Auftraggeber, Kategorien und Datum bestätigt.

### 1. Weihnachten – unerwünschte Geschenke (Which? 2019)

#### 4B-23

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**In einer Which?-Umfrage (2019, n=2.071) hatte mehr als ein Viertel ein unerwünschtes Geschenk bekommen. 27 % spendeten es, 26 % verschenkten es weiter.**

> “Our survey, which questioned 2,071 people, found that more than a quarter received a present they didn't want.”

- **Quelle:** [Which?: What are you going to do with your unwanted gifts this Christmas?](https://www.which.co.uk/news/article/what-are-you-going-to-do-with-your-unwanted-gifts-this-christmas-aaoUZ1K6tfMF)
- **Datum der Quelle:** 2019-12-28 · **Typ:** Fachgesellschaft/Charity
- **Stichprobe/Methodik:** Which?, n=2.071, Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Verbraucherorganisation, aber veraltet (2019). Inzwischen gibt es eine neuere Which?-Umfrage (4B-V06: 21 %, Weihnachten 2024). Ohne Beleg gibt es laut Which? 'almost certainly' keine Erstattung.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, 27 %, 26 % und Datum bestätigt; auf die neuere Which?-Zahl (4B-V06) verwiesen.

### 1. Weihnachten – unerwünschte Geschenke (Herkunft „3 Geschenke“)

#### 4B-24

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer OnePoll-Umfrage für die Salvation Army (2014) erhalten Briten im Schnitt drei unerwünschte Geschenke. Bei 42 % landen sie meist unten im Schrank.**

> “on average, we each receive three presents we don't actually want. ... the majority (42 per cent) usually end up keeping them in the bottom of a cupboard”

- **Quelle:** [The Salvation Army: Brits set to waste money on millions of unwanted gifts this Christmas](https://salvationarmy.org.uk/news/brits-set-waste-money-millions-unwanted-gifts-christmas)
- **Datum der Quelle:** 2014-11-10 · **Typ:** Fachgesellschaft/Charity
- **Stichprobe/Methodik:** OnePoll im Auftrag der Salvation Army Trading Company Ltd, n=2.000 UK-Einwohner, Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Stark veraltet (2014), Auftragsstudie einer Charity mit eigener Kleidersammlung. Nicht für Ads verwenden.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Methodik und Datum bestätigt.

### 1. Weihnachten – unerwünschte Geschenke (YouGov 2018)

#### 4B-25

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer von UK Fundraising berichteten YouGov-Umfrage (veröffentlicht Nov. 2018) bekommen 57 % der Menschen in UK, die Weihnachten feiern, mindestens ein unerwünschtes Geschenk. Hochgerechnet könnten das 60 Mio. verschwendete Geschenke sein.**

> “60 million presents could be wasted in the UK this year ... Over half (57%) of people in the UK who celebrate Christmas”

- **Quelle:** [UK Fundraising: 60m Christmas presents could be wasted this year, survey shows](https://fundraising.co.uk/?p=251905)
- **Datum der Quelle:** 2018-11-30 · **Typ:** Presse
- **Stichprobe/Methodik:** YouGov, n=2.000, 'in October' (Jahr nicht ausdrücklich genannt); beworben von der Charity Send a Cow, Auftraggeber nicht genannt
- **Einordnung/Einschränkung:** Sekundärbericht, veraltet (2018), Auftraggeber unklar, Hochrechnung ohne Rechenweg. Die Größenordnung passt zu Finder 2024 (58 %).
- **Wahrheits-Check:** *korrigiert*. Zahlen und Datum bestätigt. Ergänzt: Send a Cow als Verbreiter; das Jahr der Feldzeit ist im Artikel nicht genannt.

### 2. Muttertag – Datum 2027

#### 4B-26

✅ BELEGT · Angle: D Geschenk

**Mothering Sunday fällt in UK 2027 auf Sonntag, den 7. März (2026: 15. März) und ist kein gesetzlicher Feiertag.**

> “2027 United Kingdom Sun, Mar 7 Not A Public Holiday”

- **Quelle:** [Office Holidays: Mothering Sunday in United Kingdom](https://www.officeholidays.com/holidays/united-kingdom/mothering-sunday)
- **Datum der Quelle:** unbekannt · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Selbst nachgerechnet: Ostersonntag 2027 = 28.03.2027, Mothering Sunday = vierter Fastensonntag = 21 Tage davor = 07.03.2027. Für 2026 ergibt sich der 15.03.2026. Die Grocery Gazette nannte für 2026 fälschlich den 21. März. Der US-Muttertag (9. Mai 2027) ist für UK irrelevant.
- **Wahrheits-Check:** *bestätigt*. Tabellenzeilen 2025 (30.3.), 2026 (15.3.) und 2027 (7.3.) gefunden. Per Python (dateutil.easter) nachgerechnet: korrekt.

### 2. Muttertag – Ausgaben gesamt 2025

#### 4B-27

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**GlobalData prognostizierte für den UK-Muttertag 2025 Ausgaben von £2,4 Mrd. (+5 %). 56,4 % der Verbraucher wollten mindestens einen Artikel kaufen (+2,9 Prozentpunkte).**

> “set to reach £2.4 billion, reflecting a 5% increase from the previous year. ... has risen to 56.4%, a 2.9ppt increase on 2024.”

- **Quelle:** [GlobalData: UK Mother's Day spending to reach £2.4 billion, as consumer participation rises](https://www.globaldata.com/media/retail/uk-mothers-day-spending-to-reach-2-4-billion-as-consumer-participation-rises-reveals-globaldata/)
- **Datum der Quelle:** 2025-03-17 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** GlobalData Mother's Day Intentions Report 2025; Methodik und n nicht öffentlich
- **Einordnung/Einschränkung:** Seriöses Marktforschungsinstitut, aber eine Prognose ohne offengelegte Methodik. Die Ø-Ausgabe von £125,30 ist nicht als 'pro Person' definiert und widerspricht GlobalData 2026 (~£50). Am meisten gefragt sind Kleidung, Schmuck/Uhren sowie Gesundheit & Beauty; Homewares werden nicht genannt.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, £125,30, Kategorien und Datum (17.03.2025) bestätigt.

### 2. Muttertag – Ausgaben 2026

#### 4B-28

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut GlobalData (März 2026) wollten die meisten Briten zum Muttertag 2026 so viel ausgeben wie im Vorjahr, rund £50. 57 % wollten mindestens einen Artikel kaufen.**

> “most intend to stick to what they spent last year – around £50. ... at least one item has edged up slightly to 57%”

- **Quelle:** [GlobalData: UK Mother's Day 2026 spend to rise as more consumers intend to shop despite flat budgets](https://www.globaldata.com/media/retail/uk-mothers-day-2026-spend-to-rise-as-more-consumers-intend-to-shop-despite-flat-budgets-says-globaldata/)
- **Datum der Quelle:** 2026-03-11 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** GlobalData Retail Occasions Series: UK Mother's Day Intentions 2026; n und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Kaufabsicht, keine tatsächlichen Ausgaben; Methodik nicht öffentlich. Keine Gesamtsumme in £. Homewares werden nur als Nischengeschenk mit früherem Kauf erwähnt.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum bestätigt; die Mitteilung enthält keine £-Mrd.-Zahl.

### 2. Muttertag – beliebte Geschenke

#### 4B-29

✅ BELEGT · Angle: D Geschenk

**Laut YouGov (März 2025) planen 34 % der Befragten Blumen als Muttertagsgeschenk, 22 % Schokolade/Süßes, 12 % Schmuck und nur 6 % Erlebnisse. 24 % derer, die den Muttertag feiern, planen kein Geschenk, bei den 55+ sind es 52 %.**

> “flowers continue to be the most popular option, chosen by 34% of respondents ... Chocolates and sweets follow at 22% ... while 12% opt for jewellery ... 24% of respondents who celebrate Mother's Day say they are not planning to give a gift ... a percentage that jumps to 52% among those aged 55 and over”

- **Quelle:** [YouGov: How the UK plans to celebrate Mother's Day in 2025](https://yougov.com/en-gb/articles/51868-how-the-uk-plans-to-celebrate-mothers-day-in-2025)
- **Datum der Quelle:** 2025-03-21 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=2.212 UK-Erwachsene 18+, national repräsentativ, gewichtet nach Alter/Geschlecht/Bildung/Region, online 17.–18.03.2025
- **Einordnung/Einschränkung:** Unabhängiges Institut, große Stichprobe, Methodik angegeben. Homeware wird nicht erwähnt. Die 52 % der 55+ dürften auch daran liegen, dass viele keine lebende Mutter mehr haben (eigene Vermutung, nicht in der Quelle).
- **Wahrheits-Check:** *bestätigt*. Alle Werte und Bezugsgruppen geprüft: 34 % bezieht sich auf alle Befragten, 24 %/52 % auf die Feiernden. Methodik und Datum bestätigt.

### 2. Muttertag – Budget pro Person

#### 4B-30

✅ BELEGT · Angle: D Geschenk

**Laut YouGov (März 2025) ist £21–50 das häufigste Muttertagsbudget (29 %). 25 % wollten unter £20 ausgeben, 15 % £51–100 und nur 6 % über £100.**

> “The most common budget range is £21-£50 (29%) ... A smaller portion (15%) plan to spend between £51-£100, while just 6% will exceed £100. ... 25% of respondents expect to spend under £20”

- **Quelle:** [YouGov: How the UK plans to celebrate Mother's Day in 2025](https://yougov.com/en-gb/articles/51868-how-the-uk-plans-to-celebrate-mothers-day-in-2025)
- **Datum der Quelle:** 2025-03-21 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=2.212 UK-Erwachsene, 17.–18.03.2025
- **Einordnung/Einschränkung:** Robuster als die Ø-Werte von GlobalData oder VoucherCodes. Zeigt: Ein Muttertagsgeschenk über £100 ist die Ausnahme (6 %).
- **Wahrheits-Check:** *bestätigt*. Alle vier Budgetwerte bestätigt.

### 2. Muttertag – Wünsche der Mütter

#### 4B-31

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**In einer YouGov-Umfrage unter 500 britischen Müttern (Feb. 2024) wünschten sich 43 % eine Karte, 39 % Blumen und 34 % ein Essen auswärts. Kleidung wünschten sich nur 7 %.**

> “The most popular gifts among mothers are greeting cards, with 43% of mums saying they'd like to receive one. ... This is followed by flowers (39%), being taken out for a meal (34%) ... Clothing, however, is the least popular gift with only 7% of respondents selecting this option.”

- **Quelle:** [YouGov: What do British mums want for Mother's Day?](https://yougov.com/en-gb/articles/48754-what-do-british-mums-want-for-mothers-day-2024)
- **Datum der Quelle:** 2024-02-27 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov Surveys: Self-serve, n=500 Mütter in UK, online 21.–22.02.2024, gewichtet
- **Einordnung/Einschränkung:** Seriöses Institut, aber kleine Stichprobe, Self-Serve-Tool, Daten von 2024. Home oder Bettwaren wurden nicht abgefragt.
- **Wahrheits-Check:** *bestätigt*. Werte, Methodik und Datum bestätigt.

### 2./3. Muttertag vs. Vatertag – Ø-Ausgaben

#### 4B-32

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer VoucherCodes-Umfrage (März 2025) planen Briten im Schnitt £80,94 für den Muttertag und £70,85 für den Vatertag ein.**

> “On average, the nation expects to spend £80.94 on Mother's Day, compared to £70.85 on Father's Day.”

- **Quelle:** [Retail Times: Brits set to spend more on mum than dad this year – plus Mother's Day deals under £25 (VoucherCodes.co.uk-Umfrage)](https://retailtimes.co.uk/brits-set-to-spend-more-on-mum-than-dad-this-year-plus-mothers-day-deals-under-25/)
- **Datum der Quelle:** 2025-03-25 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** VoucherCodes.co.uk; n, Institut und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Händler-PR ohne Methodik. Die Mittelwerte sind durch Ausreißer verzerrt: Im North West planten laut Artikel 3 % über £900. Andere Quellen sollen andere Verhältnisse zeigen (MyVoucherCodes, NerdWallet), das ist aber nicht selbst geprüft. Für Budgets stattdessen YouGov-Spannen verwenden (4B-30, 4B-V07).
- **Wahrheits-Check:** *korrigiert*. Wortlaut bestätigt; die £900-Angabe (North West, 3 %) gefunden. Nicht selbst geprüfte Vergleichszahlen (MyVoucherCodes £54,06/£44,80, NerdWallet £92/£90) als ungeprüft gekennzeichnet.

### 2. Muttertag – Savvy „£18bn“

#### 4B-33

❌ NICHT BELEGT / MYTHOS · Angle: D Geschenk, Markt

**Die von der Grocery Gazette berichtete Savvy-Prognose von £18 Mrd. Muttertagsausgaben 2026 (+15 %) hat keine definierte Abgrenzung und ist mit anderen Marktdaten unvereinbar (GlobalData: £2,4 Mrd. für 2025).**

> “spend expected to reach £18bn in 2026, which marks a 15 per cent increase year-on-year.”

- **Quelle:** [Grocery Gazette: UK shopping spend expected to hit £18bn for Mother's Day (Savvy)](https://www.grocerygazette.co.uk/2026/03/11/uk-shopping-spend-expected-to-hit-18bn-for-mothers-day/)
- **Datum der Quelle:** 2026-03-11 · **Typ:** Presse
- **Stichprobe/Methodik:** Savvy; auf der Seite weder n noch Methodik (laut früherer Suchzusammenfassung n=1.000, nicht verifiziert)
- **Einordnung/Einschränkung:** Der Artikel erklärt nicht, was die £18 Mrd. umfassen; der Wert ist das 7,5-Fache des GlobalData-Werts. Derselbe Artikel nennt ein falsches Datum ('Mother's Day (21 March)' statt 15.03.2026). Nicht in Ads verwenden. Belastbar ist daraus nur die Absicht: 65 % wollten feiern, in Haushalten mit Kindern 88 %.
- **Wahrheits-Check:** *bestätigt*. Unbelegtheit bestätigt: keine Definition, keine Methodik, falsches Datum '21 March'. 65 %/88 % gefunden.

### 2. Muttertag – MYTHOS „drittgrößtes Handelsereignis“

#### 4B-34

❌ NICHT BELEGT / MYTHOS · Angle: D Geschenk, Markt

**Die Behauptung, der Muttertag sei in UK das drittgrößte Handelsereignis, ist durch keine UK-Quelle belegt.**

> “it is the 3rd largest retail event of the year”

- **Quelle:** [Microsoft Advertising Blog (Australien): Making the most of Mother's Day (April 2015), nur laut Suchsnippet](https://about.ads.microsoft.com/en-au/blog/post/april-2015/making-the-most-of-mother-s-day)
- **Datum der Quelle:** 2015-04 · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Einzige Fundstelle ist ein australischer Werbe-Blog von 2015 ohne Quellenangabe und ohne UK-Bezug; die URL führt heute auf eine Blog-Übersicht. UK-Daten stützen kein Ranking: Mintel (2017) nennt den Muttertag nur das Frühjahrs-/Sommer-Event mit den meisten Käufern (vor Ostern, Valentinstag, Vatertag), ohne Umsatzranking. GlobalData sieht Ostern 2025 (£2,3 Mrd.) und Muttertag 2025 (£2,4 Mrd.) etwa gleichauf. Eine öffentliche UK-Rangliste aller Anlässe (inkl. Black Friday) existiert nicht. Die US-Formel stammt aus NRF-Daten und ist nicht übertragbar.
- **Wahrheits-Check:** *bestätigt* (Seite vom Prüfer nicht direkt abrufbar). URL (und alte bingads-URL per 301) geöffnet: Sie führt auf eine Blog-Übersicht, der Satz ist nicht auffindbar, daher selbst_abgerufen=false. Suche nach 'third biggest retail event UK' ergab keine UK-Quelle. Mintel 2017 und GlobalData Ostern 2025 selbst geöffnet (4B-V09, 4B-V10). Die frühere Begründung 'laut Mintel-Snippet 2015 war Ostern größer' war nicht überprüfbar und wurde ersetzt.

### 3. Geburtstag – Budget

#### 4B-35

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer VoucherCodes-Umfrage (März 2025) liegt das Ø-Budget für Geburtstage bei £245,48. Insgesamt planen Briten im Schnitt £2.007 pro Jahr für Feieranlässe ein. Ob nur Geschenke oder auch Feiern gemeint sind, ist nicht angegeben.**

> “Birthdays are to be celebrated in style with an average budgeted spend of £245.48. ... Overall, Brits intend to spend a whopping average of £2,007 annually on celebrations.”

- **Quelle:** [Retail Times: Brits set to spend more on mum than dad this year – plus Mother's Day deals under £25 (VoucherCodes.co.uk-Umfrage)](https://retailtimes.co.uk/brits-set-to-spend-more-on-mum-than-dad-this-year-plus-mothers-day-deals-under-25/)
- **Datum der Quelle:** 2025-03-25 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** VoucherCodes.co.uk; n, Institut und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Einzige gefundene UK-Geburtstagszahl. PR-Umfrage ohne Methodik, nicht nach Empfängern aufgeschlüsselt; unklar, ob Geschenke, Feiern oder der eigene Geburtstag gemeint sind. NerdWallet UK 2025 war nicht mehr abrufbar (HTTP 410).
- **Wahrheits-Check:** *korrigiert*. Wortlaut bestätigt. URL auf die endgültige Adresse geändert. Aussage präzisiert: '£245,48 pro Jahr für Geschenke' steht so nicht im Text.

### 3. Vatertag – Ausgaben 2025

#### 4B-36

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**GlobalData prognostizierte für den UK-Vatertag 2025 Ausgaben von £1,123 Mrd. (+1,8 %). 45 % der Verbraucher wollten mitmachen (−1,5 Prozentpunkte gegenüber 2024).**

> “Father's Day spending in the UK is set to rise by 1.8% in 2025 to reach a value of GBP1,123 million. ... 45% of UK consumers intend to participate in the occasion in 2025, a decrease of 1.5 ppts on 2024.”

- **Quelle:** [GlobalData: UK Father's Day spend to rise 1.8% in 2025, but retailers must act to unlock full potential](https://www.globaldata.com/media/retail/uk-fathers-day-spend-rise-1-8-2025-retailers-must-act-unlock-full-potential-says-globaldata/)
- **Datum der Quelle:** 2025-05-27 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** GlobalData UK Father's Day Intentions 2025; Methodik nicht öffentlich
- **Einordnung/Einschränkung:** Prognose ohne offengelegte Methodik und ohne Ø-Ausgabe pro Person. Karten und Geschenkpapier: nur 20 % Kaufabsicht (Vorjahr 23 %). Den Vorjahreswert '£695 Mio. 2024' konnte ich nicht selbst prüfen.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Datum bestätigt. Die nicht geprüfte Vorjahreszahl (£695 Mio., nur aus einer Suchzusammenfassung) als ungeprüft markiert; Karten/Geschenkpapier ergänzt.

### 3. Vatertag – 2026

#### 4B-37

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut GlobalData (Juni 2026) wollten 49,2 % der UK-Verbraucher den Vatertag am 21. Juni 2026 begehen, 4,1 Prozentpunkte mehr als 2025.**

> “49.2% of UK consumers intend to participate in the occasion on 21 June ... representing a 4.1 percentage-point increase on 2025”

- **Quelle:** [GlobalData: UK Father's Day spending set to rise in 2026, but cautious consumers keep budgets restrained](https://www.globaldata.com/media/retail/uk-fathers-day-spending-set-to-rise-in-2026-but-cautious-consumers-keep-budgets-restrained-says-globaldata/)
- **Datum der Quelle:** 2026-06-15 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** GlobalData UK Father's Day Intentions 2026; Methodik nicht öffentlich
- **Einordnung/Einschränkung:** Kaufabsicht, keine £-Werte, Methodik nicht offen. Den Zuwachs führt GlobalData auf jüngere Verbraucher zurück. Wichtigster Anlass ist laut Prognose Essen gehen.
- **Wahrheits-Check:** *bestätigt*. 49,2 %, +4,1 Prozentpunkte und Datum 15.06.2026 bestätigt; 21.06.2026 als dritter Junisonntag nachgerechnet.

### 3. Großelterntag UK – Datum

#### 4B-39

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Der Großelterntag wird in UK am ersten Sonntag im Oktober begangen, laut Wikipedia seit 2008 (2026: 4. Oktober, 2027: 3. Oktober). Eingeführt wurde er 1990 von Age Concern, laut Wikipedia ist er aber wenig verbreitet.**

> “The day was introduced to the UK in 1990 by the charity Age Concern ... but it has not been widely accepted by the British public. ... It has been celebrated on the first Sunday in October since 2008.”

- **Quelle:** [Wikipedia: Grandparents' Day (Abschnitt United Kingdom, zitiert Age Concern 2008); ergänzend Age UK Pressemitteilung 29.09.2017](https://en.wikipedia.org/wiki/Grandparents%27_Day)
- **Datum der Quelle:** unbekannt · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Historie und 'wenig verbreitet' stützen sich nur auf Wikipedia (Quelle: Age-Concern-Mitteilung von 2008, nicht abrufbar). Age UK bestätigt die Praxis: 2017 bewarb Age UK den 'national Grandparents' Day this Sunday (1st October)', also den ersten Oktobersonntag. Die Daten 2026/2027 habe ich selbst berechnet. Ausgabenzahlen gibt es nicht. Für Ads nur ein Nischen-Aufhänger; der Termin 2026 ist vorbei.
- **Wahrheits-Check:** *korrigiert*. Wikipedia-Abschnitt bestätigt (Ref.: Age Concern, 26.02.2008). Zusätzlich Age UK, 29.09.2017 geöffnet: 'national Grandparents' Day this Sunday (1st October)'. Daten per Python nachgerechnet (04.10.2026, 03.10.2027).

### 4. Home als Geschenk – Mintel

#### 4B-40

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Im UK-Weihnachtsbericht 2025 von Mintel trägt ein Unterkapitel die Überschrift, dass die gestiegene Nachfrage nach Home-Produkten auch auf Geschenke übergreifen werde. Zahlen sind nicht öffentlich.**

> “Uptick in home demand will extend to gifts”

- **Quelle:** [Mintel Store: UK Prospects for Christmas Market Report 2025 (Inhaltsverzeichnis)](https://store.mintel.com/report/uk-prospects-for-christmas-market-report)
- **Datum der Quelle:** 2025-11-07 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Mintel; Methodik und Zahlen hinter der Paywall
- **Einordnung/Einschränkung:** Nur eine Kapitelüberschrift ohne öffentliche Zahl. Ein qualitativer Hinweis, nicht als Fakt zitierfähig. Weiteres Unterkapitel: 'Demand for value will push shoppers to Black Friday'.
- **Wahrheits-Check:** *bestätigt*. Beide Unterüberschriften (Kapitel 4, Non-Food) gefunden; Metadatum 2025-11-07 bestätigt; keine öffentlichen Zahlen.

### 4. Home als Geschenk – Kartendaten

#### 4B-41

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut Barclays-Kartendaten stiegen die Umsätze von Möbelhäusern im Dezember 2024 um 1,7 %, das stärkste Plus seit März 2022. Barclays erklärt das u. a. mit Geschenken und Wohnungsverbesserungen vor Weihnachten. Die gesamten Kartenausgaben stagnierten (0,0 %).**

> “Furniture stores also saw an increase (1.7 per cent), the category's highest level of growth since March 2022”

- **Quelle:** [Barclays: Consumer card spending stalled in December, as joy-seekers prioritised entertainment and travel over essentials](https://home.barclays/news/press-releases/2025/01/consumer-card-spending-stalled-in-december--as-joy-seekers-prior)
- **Datum der Quelle:** 2025-01-07 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** Barclays-Kartendaten 16.11.–23.12.2024 vs. Vorjahr; Zusatzumfrage Opinium n=2.000, 13.–18.12.2024
- **Einordnung/Einschränkung:** Die Kartendaten sind belastbar, die Begründung 'as Brits shopped for gifts and home improvements ahead of Christmas' ist aber Barclays' Interpretation. Daten von 2024, Bettwaren nicht separat ausgewiesen.
- **Wahrheits-Check:** *bestätigt*. Wortlaut wörtlich bestätigt, ebenso Gesamtwert 0,0 %, Zeitraum und Datum.

### 4. Bettwaren als Geschenk – Belege?

#### 4B-42

❌ NICHT BELEGT / MYTHOS · Angle: D Geschenk

**Keine öffentlich einsehbare UK-Umfrage weist Bettdecken oder Bettwäsche als beliebtes Geschenk aus. In der Statista-Wunschliste 2025 gibt es dafür keine Kategorie, und Home-nahe Kategorien liegen niedrig (Haushaltsgeräte 14 %, Deko 10 %, Möbel 7 %).**

> “Household appliances 14% | Decoration articles 10% | Furniture 7% (Tabellenwerte zur Frage: 'What kind of Christmas gift would you personally be happy about?')”

- **Quelle:** [Statista: Christmas gifts desired by UK consumers 2025](https://statista.com/statistics/1084794/christmas-gifts-desired-by-uk-consumers)
- **Datum der Quelle:** 2025-11-27 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Statista-Online-Umfrage, n=1.044, UK 18–80 J., 28.10.–10.11.2025
- **Einordnung/Einschränkung:** Die Einordnung gilt der Behauptung 'Bettdecken sind ein beliebtes Geschenk'; dafür gibt es keine Quelle. YouGov 2022, YouGov Muttertag 2024/2025 und YouGov Vatertag 2024 erwähnen weder Bettwaren noch Homeware. Ob Bettwaren in 'clothing, textiles' (39 %) stecken, ist nicht belegbar. Warnsignal: 2017 waren laut Finder-PR 11,5 % der unerwünschten Geschenke 'household items' (4B-V08). Für Ads also nicht 'Lieblingsgeschenk der Briten' o. Ä. behaupten.
- **Wahrheits-Check:** *bestätigt*. Statista-Tabelle vollständig geprüft: keine Kategorie für Bettwaren oder Heimtextilien. Unbelegtheit in mehreren weiteren Quellen bestätigt.

### 4. Ältere Käufer online – ONS

#### 4B-43

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut ONS hatten Anfang 2020 65 % der über 65-Jährigen in Großbritannien in den letzten 12 Monaten online eingekauft (2008: 16 %). Bei allen Erwachsenen waren es 87 %.**

> “In January to February 2020, 87% of all adults shopped online within the last 12 months, up from 53% in 2008; those aged 65 years and over had the highest growth, rising from 16% to 65% over this period.”

- **Quelle:** [ONS: Internet access – households and individuals, Great Britain: 2020](https://www.ons.gov.uk/peoplepopulationandcommunity/householdcharacteristics/homeinternetandsocialmediausage/bulletins/internetaccesshouseholdsandindividuals/2020)
- **Datum der Quelle:** 2020-08-07 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** ONS Opinions and Lifestyle Survey, Jan.–Feb. 2020, Großbritannien
- **Einordnung/Einschränkung:** Amtliche Statistik, aber vor der Pandemie erhoben und nur GB. Die Serie ist seit 03.05.2023 eingestellt; die ONS verweist auf Ofcom. Ofcom 2025 war nicht abrufbar (403). Der heutige Wert dürfte höher liegen, das ist aber nicht belegt.
- **Wahrheits-Check:** *bestätigt*. Wortlaut wörtlich bestätigt; Release 07.08.2020; Hinweis auf Einstellung (03.05.2023) bestätigt.

### 4. Ältere Internetnutzer – ONS

#### 4B-44

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut ONS waren 2020 54 % der über 75-Jährigen in UK aktuelle Internetnutzer. 6,3 % aller Erwachsenen hatten das Internet noch nie genutzt.**

> “compared with 54% of adults aged 75 years and over. ... 6.3% of adults in the UK had never used the internet in 2020, down from 7.5% in 2019.”

- **Quelle:** [ONS: Internet users, UK: 2020](https://www.ons.gov.uk/businessindustryandtrade/itandinternetindustry/bulletins/internetusers/2020)
- **Datum der Quelle:** 2021-04-06 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** ONS Labour Force Survey, UK, Jan.–März 2020
- **Einordnung/Einschränkung:** Amtliche Statistik, aber Daten von 2020; Serie eingestellt. Eigene Schlussfolgerung für Angle D: Ein relevanter Teil der Hochbetagten kauft nicht selbst online, daher eher Kinder und Enkel als Käufer ansprechen.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Release 06.04.2021 und Datenbasis (LFS Jan.–März 2020) bestätigt.

### 5. Kaufzeitpunkt – PwC 2025

#### 4B-45

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**In der PwC-Umfrage (Anfang Nov. 2025) sagten 46 % der UK-Verbraucher, sie seien mit ihren Weihnachtseinkäufen vor Anfang Dezember fertig. 47 % wollten den Großteil Anfang bis Mitte Dezember erledigen, 8 % erst in der Woche vor Weihnachten.**

> “46% say they have finished their shopping before the beginning of December. ... The majority of consumers (47%) will still do their festive spending in early-to-mid December ... with 8% leaving it until the week before Christmas.”

- **Quelle:** [PwC UK: Festive spending forecast to reach £24.6bn this year (Pressemitteilung, wiedergegeben von Insight DIY; PwC-Primärseite 403)](https://www.insightdiy.co.uk/news/festive-spending-forecast-to-reach-246bn-this-year/15891.htm)
- **Datum der Quelle:** 2025-12-12 · **Typ:** Presse
- **Stichprobe/Methodik:** Laut Suchzusammenfassung n=2.000 UK-Erwachsene, 31.10.–4.11.2025 (nicht selbst verifiziert); laut Insight DIY drei Wochen vor dem Budget erhoben
- **Einordnung/Einschränkung:** Die Zahlen sind über eine wörtliche Wiedergabe der PwC-Mitteilung geprüft, die Primärseite bleibt gesperrt. Da Anfang November erhoben, handelt es sich um Absichten, nicht um tatsächlich abgeschlossene Einkäufe. Gründe für frühes Kaufen: Organisation (34 %), beste Preise (31 %), Budget verteilen (22 %). Frauen 4 % vs. Männer 12 % in der letzten Woche.
- **Wahrheits-Check:** *korrigiert*. PwC-Seite erneut 403 (WebFetch, curl), ebenso Retail Sector und Jewellery Focus. Insight DIY (gibt die PwC-Mitteilung wieder) geöffnet: 46 %/47 %/8 % und Gründe 34/31/22 % wörtlich gefunden. URL ersetzt, selbst_abgerufen jetzt true. Aussage präzisiert: Absicht zum Zeitpunkt der Befragung.

### 5. Kaufzeitpunkt – PwC 2024

#### 4B-46

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut PwC sagten 2024 48 % der UK-Verbraucher, sie hätten die meisten Weihnachtsgeschenke vor Anfang Dezember gekauft (2023: 43 %).**

> “48% saying they have already bought most of their presents before the beginning of December, compared to 43% last year.”

- **Quelle:** [CXM Today über PwC: UK Consumers Set to Spend £22.7bn on Festive Gifts](https://cxmtoday.com/news/uk-consumers-set-to-spend-22-7bn-on-festive-gifts/)
- **Datum der Quelle:** 2024-12-11 · **Typ:** Presse
- **Stichprobe/Methodik:** PwC-Umfrage 2024; n und Feldzeit im Artikel nicht genannt
- **Einordnung/Einschränkung:** Sekundärquelle, Vorjahresdaten. Nicht direkt mit 2025 vergleichbar (2024 'most of their presents', 2025 'finished their shopping'). Vermutlich ebenfalls Absichten aus einer Vorab-Umfrage.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Vergleichswert 43 % bestätigt; URL ?p=30901 durch die endgültige Adresse ersetzt.

### 5. Kaufzeitpunkt – GlobalData 2025

#### 4B-47

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut GlobalData (Jan. 2026) begann 2025 ein Fünftel der Käufer erst in den letzten Novemberwochen mit den Weihnachtseinkäufen. Der Anteil der Verbraucher mit Weihnachtsausgaben sank; ein Drittel fühlte sich finanziell schlechter gestellt.**

> “A fifth of shoppers delayed their Christmas shopping, starting only in the last few weeks of November. ... The proportion of consumers spending on Christmas declined in 2025.”

- **Quelle:** [GlobalData: United Kingdom (UK) Christmas – Analysing Buying Dynamics, Channel Usage, Spending and Retailer Selection (Report-Zusammenfassung)](https://www.globaldata.com/store/report/uk-christmas-retail-market-analysis/)
- **Datum der Quelle:** 2026-01-19 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** GlobalData-Verbraucherumfrage zu Weihnachten 2025; n und Feldzeit nicht öffentlich
- **Einordnung/Einschränkung:** Nur die öffentliche Zusammenfassung; Detailzahlen (z. B. 'Homewares penetration, total (2023-2025)') sind kostenpflichtig.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Drittel 'worse off' und Datum 19.01.2026 bestätigt; Homewares-Tabellen nur als Titel sichtbar.

### 5. Black Friday – Teilnahme

#### 4B-48

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut Finder/Censuswide (Okt. 2025) wollten 58 % der UK-Erwachsenen am Black-Friday-Wochenende 2025 einkaufen, mit im Schnitt geplanten £124 (hochgerechnet ca. £3,9 Mrd.).**

> “3 in 5 UK adults (58%) plan to spend during the Black Friday weekend ... The average person plans to spend £124 on Black Friday this year. ... The UK plans to spend an estimated £3.9 billion during the 2025 Black Friday sales weekend.”

- **Quelle:** [Finder UK: Black Friday statistics](https://www.finder.com/uk/black-friday-statistics)
- **Datum der Quelle:** 2025-10-17 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Censuswide im Auftrag von Finder, n=2.000 UK-Erwachsene, 1.–6.10.2025, ±2,19 %
- **Einordnung/Einschränkung:** PR-Umfrage einer Vergleichsseite zu Absichten. Sie unterscheidet nicht zwischen Weihnachtsgeschenken und Käufen für sich selbst. Black Friday 2026 ist am 27.11.2026 (selbst berechnet).
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Methodik und Datum bestätigt. Black Friday 2026 = 27.11.2026 per Python nachgerechnet.

### 5. Black Friday – Ältere

#### 4B-49

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut Finder/Censuswide wollten 2025 nur rund 3 von 10 Babyboomern (61–79) am Black Friday kaufen (Ø £50) und 22 % der über 80-Jährigen (Ø £39), gegenüber 81 % der Millennials (29–44).**

> “3 in 10 (31%) baby boomers, aged 61–79, are intending to buy something ... with a planned average spend of £50 ... Only a fifth (22%) of the silent generation, aged 80+ ... Millennials, aged 29-44, are even more likely to partake – with 81% planning to make a Black Friday purchase.”

- **Quelle:** [Finder UK: Black Friday statistics](https://www.finder.com/uk/black-friday-statistics)
- **Datum der Quelle:** 2025-10-17 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Censuswide/Finder, n=2.000, 1.–6.10.2025; Teilgruppen klein, besonders 80+
- **Einordnung/Einschränkung:** PR-Umfrage mit kleinen Teilgruppen. Die Seite ist inkonsistent: Fließtext 31 %, Tabelle 30 % für Boomer. Die Tendenz ist plausibel: Ältere nutzen Black Friday seltener. Eigene Schlussfolgerung für Angle D: Kinder und Enkel sind die bessere Zielgruppe.
- **Wahrheits-Check:** *korrigiert*. Werte bestätigt. Korrektur: Die Tabelle nennt 30 % statt 31 %; Aussage auf 'rund 3 von 10' geändert, Millennials-Wortlaut ergänzt.

### 5. Weihnachten 2025 – Ergebnis/Januar-Sales

#### 4B-50

✅ BELEGT · Angle: Markt, D Geschenk

**Die Barclays-Kartenausgaben fielen im Dezember 2025 (25.11.–24.12.) um 1,7 % zum Vorjahr. Laut BRC wurden weniger Weihnachtsgeschenke verkauft als erwartet, und viele Käufer warteten auf Boxing Day und Januar-Sales.**

> “overall consumer card spending fell by 1.7% in December from the same month in 2024 ... Non-food sales were almost flat with fewer Christmas gifts sold than expected, the BRC said. ... Many people were clearly holding out for discounts,”

- **Quelle:** [ESM Magazine/Reuters: UK Consumers Cut Spending In December By Most Since 2021, Barclays Says](https://www.esmmagazine.com/retail/uk-consumers-cut-spending-in-december-by-most-since-2021-barclays-says-303995)
- **Datum der Quelle:** 2026-01-15 · **Typ:** Presse
- **Stichprobe/Methodik:** Barclays-Kartendaten 25.11.–24.12.2025; BRC-KPMG Retail Sales Monitor, 5 Wochen bis 3.1.2026 (Gesamtumsatz +1,2 %)
- **Einordnung/Einschränkung:** Gemessene Transaktions- und Umsatzdaten, keine Absichtsumfrage, berichtet von Reuters. Die Primärmitteilungen von Barclays und BRC waren nicht direkt abrufbar.
- **Wahrheits-Check:** *bestätigt*. −1,7 %, das BRC-Zitat, das Dickinson-Zitat ('Many people were clearly holding out for discounts') und die Zeiträume bestätigt.

### 5. Kauf für sich selbst / Black-Friday-Effekt

#### 4B-51

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut Barclays (Dez. 2024) gaben 40 % der Befragten an, sich und ihren Liebsten im Dezember etwas zu gönnen. Nach Black Friday und Cyber Monday stiegen die Umsätze allgemeiner Einzelhändler durch Geschenkkäufe und Rabatte um 1,6 %.**

> “two in five (40 per cent) said they were treating themselves and their loved ones in December ... gift shopping and seasonal discounts spurred growth of 1.6 per cent at general retailers”

- **Quelle:** [Barclays: Consumer card spending stalled in December, as joy-seekers prioritised entertainment and travel over essentials](https://home.barclays/news/press-releases/2025/01/consumer-card-spending-stalled-in-december--as-joy-seekers-prior)
- **Datum der Quelle:** 2025-01-07 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** Opinium für Barclays, n=2.000, 13.–18.12.2024; Kartendaten 16.11.–23.12.2024
- **Einordnung/Einschränkung:** Die Frage vermischt 'sich selbst UND Liebste'; ein reiner Anteil für Käufe für sich selbst lässt sich nicht ableiten. Daten von 2024.
- **Wahrheits-Check:** *bestätigt*. Beide Passagen wörtlich bestätigt; Methodik und Datum bestätigt.

### 5. Kaufzeitpunkt – YouGov 2025

#### 4B-V01

✅ BELEGT · Angle: D Geschenk, Markt

**Laut YouGov Big Survey (19.–24.11.2025) sagten 24 % der Briten, sie hätten schon vor November mit ihren Weihnachtseinkäufen begonnen.**

> “24% of Britons say they have started their Christmas shopping before November”

- **Quelle:** [YouGov: The YouGov Big Survey on Christmas](https://yougov.com/en-gb/articles/53587-the-yougov-big-survey-on-christmas)
- **Datum der Quelle:** 2025-11-28 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=4.243 GB-Erwachsene 18+, 19.–24.11.2025
- **Einordnung/Einschränkung:** Unabhängiges Institut, große Stichprobe, rückblickende Angabe Ende November (keine bloße Absicht). Nur GB. Relevant für das Timing von Geschenk-Ads: Ein Viertel kauft schon im Oktober oder früher.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Satz wörtlich auf der Seite gefunden, Methodik bestätigt.

### 5. Black Friday – Geschenkkäufe (eBay Advertising)

#### 4B-V02

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**In einer Censuswide-Umfrage für eBay Advertising UK (Juli 2025) stimmten 49 % derjenigen, die Weihnachtsgeschenke kaufen wollten, (eher) zu, Geschenke am Black Friday zu kaufen. 29 % aller Erwachsenen erledigen den Großteil ihrer Weihnachtseinkäufe in den Sales, und 27 % wollten vor dem Black Friday fertig sein.**

> “49% of UK consumers that plan to buy Christmas gifts this year are likely to buy gifts on Black Friday, with 29% of all adults doing most of their Christmas shopping during the sales ... more than a quarter (27%) of shoppers say they'll finish their Christmas shopping before Black Friday even begins”

- **Quelle:** [ChannelX: How UK shoppers are approaching Black Friday 2025 (eBay Advertising UK); ergänzend Insight DIY, 12.11.2025](https://channelx.world/2025/11/how-uk-shoppers-are-approaching-black-friday-2025/)
- **Datum der Quelle:** 2025-11-11 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Censuswide für eBay Advertising, n=2.001 UK-Erwachsene, die Weihnachten feiern, 11.–15.07.2025; 49 % = 'strongly' + 'somewhat agree'
- **Einordnung/Einschränkung:** PR-Umfrage eines Marktplatzes. Es sind Zustimmungswerte (Absicht), erhoben im Juli, also lange vor der Saison. Der beste verfügbare UK-Wert zur Frage 'Weihnachtsgeschenke am Black Friday', aber nur mit Quellenangabe und als Absicht formulieren.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. ChannelX geöffnet (49 % und Methodik); Insight DIY geöffnet (29 %, 27 % und Fußnote zur Zustimmungsskala). Die eBay-Primärseite war nicht erreichbar.

### 5. Black Friday – Geschenkkäufe (Barclays)

#### 4B-V03

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut Barclays-Umfrage (Nov. 2025) wollten 45 % der Black-Friday-Teilnehmer dabei Weihnachtsgeschenke mit Rabatt kaufen. Black-Friday-Käufer planten im Schnitt £430 auszugeben. Babyboomer (60–78) stöbern laut Barclays am häufigsten online in den Sales (81 %).**

> “Of those participating in Black Friday, 45% plan to pick up Christmas gifts at a discount. ... Black Friday shoppers expect to spend an average of £430 each in upcoming sales ... Baby Boomers (aged 60-78) are the most likely generation to browse the sales online, at 81%.”

- **Quelle:** [Retail Times: Barclays – UK shoppers set to spend £10.2bn in the Black Friday sales](https://retailtimes.co.uk/barclays-uk-shoppers-set-to-spend-10-2bn-in-the-black-friday-sales/)
- **Datum der Quelle:** 2025-11-25 · **Typ:** Presse
- **Stichprobe/Methodik:** Barclays Consumer Spend research; Institut, n und Feldzeit im Artikel nicht genannt
- **Einordnung/Einschränkung:** Sekundärquelle ohne Methodik; Absichten. Bezugsgruppe für 45 % sind die Black-Friday-Teilnehmer, nicht alle Erwachsenen. Bei den 81 % der Boomer ist die Basis unklar (vermutlich Black-Friday-Käufer). Die Barclays-Primärmitteilung war nicht abrufbar.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; alle drei Sätze wörtlich auf der Seite gefunden.

### 5. Black Friday – Kauf für sich selbst (PwC)

#### 4B-V04

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut PwC (Black-Friday-Umfrage, Nov. 2025, über TechRound) wollten 68 % der Black-Friday-Käufer etwas für sich selbst kaufen, bei Männern 74 %. Das Interesse am Black Friday sank auf 46 % (Vorjahr 53 %); Teilnehmer planten im Schnitt £262.**

> “PwC UK found that 68% of shoppers will buy something for themselves. The figure is higher for men at 74%. ... interest in the event has fallen to 46%. Last year it reached 53%. ... shoppers who take part expect to spend £262 each.”

- **Quelle:** [TechRound über PwC UK: UK consumers set to spend £6.4bn this Black Friday (PwC-Primärseite 403)](https://techround.co.uk/news/%E2%81%A0black-friday-pwc-uk-consumers-spend/)
- **Datum der Quelle:** 2025-11-20 · **Typ:** Presse
- **Stichprobe/Methodik:** PwC-Umfrage; n und Feldzeit im Artikel nicht genannt
- **Einordnung/Einschränkung:** Sekundärquelle, die PwC-Primärseite ist gesperrt (403). Die Basis 'shoppers' meint vermutlich Black-Friday-Teilnehmer. 'Christmas stocking fillers and health and beauty items' liegen zusammen bei 28 %; einen reinen Anteil für Weihnachtsgeschenke gibt es nicht.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Sätze auf TechRound gefunden. PwC-Mitteilung und PwC-NI-Regionalmitteilung jeweils 403.

### 5. Kauf für sich selbst (eBay Advertising)

#### 4B-V05

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer eBay-Advertising-Umfrage (Sept. 2025) geben 29 % der Weihnachtskäufer zu Weihnachten eher mehr für sich selbst aus als für Freunde oder Familie, bei Millennials 50 %.**

> “almost 1 in 3 (29%) shoppers tend to spend more on themselves than friends or family at Christmas ... jumping to 50% of Millennials”

- **Quelle:** [Retail Times: One in two Millennials spend more on themselves than others at Christmas, finds eBay Advertising UK](https://retailtimes.co.uk/one-in-two-millennials-spend-more-on-themselves-than-others-at-christmas-finds-ebay-advertising-uk/)
- **Datum der Quelle:** 2025-09-12 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 'more than 2,000 Christmas shoppers'; Institut, Feldzeit und Gewichtung im Artikel nicht genannt
- **Einordnung/Einschränkung:** PR-Umfrage eines Marktplatzes mit unvollständiger Methodik. Keine Werte für Ältere. Laut Artikel steht Mode/Accessoires mit 31 % auf der Liste für Selbstgeschenke an Black Friday und Weihnachten oben.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Wortlaut und Datum auf der Seite bestätigt.

### 1. Weihnachten – unerwünschte Geschenke (Which? 2025)

#### 4B-V06

✅ BELEGT · Angle: D Geschenk

**Laut Which?/Deltapoll (Feldzeit Jan. 2025) hatte jede/r Fünfte (21 %) zu Weihnachten 2024 ein unerwünschtes oder unpassendes Geschenk bekommen. Davon behielten 33 % es und wollen es nutzen, 15 % behielten es ungenutzt, 34 % wurden es los.**

> “found that one in five (21%) had received an unwanted or unsuitable gift. ... three in 10 (33%) said they kept it and will use it ... one in six (15%) said they kept it but would not use it. ... a third (34%) admitted they had gotten rid of the gift”

- **Quelle:** [Which?: Marmite-scented deodorant, used pyjamas and rotten fruit – Which? reveals the UK's most disappointing Christmas presents](https://www.which.co.uk/policy-and-insight/article/marmite-scented-deodorant-used-pyjamas-and-rotten-fruit-which-reveals-the-uks-most-disappointing-christmas-presents-a2MYW4I4pDSJ)
- **Datum der Quelle:** 2025-12-29 · **Typ:** Fachgesellschaft/Charity
- **Stichprobe/Methodik:** Deltapoll für Which?, n=2.047 UK-Erwachsene 18+, online, 24.–27.01.2025, gewichtet auf die UK-Bevölkerung
- **Einordnung/Einschränkung:** Unabhängige Verbraucherorganisation, anerkanntes Institut, Methodik offengelegt, UK. Bezieht sich auf Weihnachten 2024 (Mitteilung vom Dez. 2025). Die aktuellste unabhängige Zahl, deutlich niedriger als Finders 'jemals'-Wert (58 %). Von denen, die es loswurden: 12 % an Freunde/Familie, 11 % Charity-Shop, 8 % online verkauft.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Wortlaut, Methodik (Notes to editors) und Seitendatum 29.12.2025 bestätigt.

### 3. Vatertag – Budget und Geschenke (YouGov 2024)

#### 4B-V07

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut YouGov (Mai 2024) planten 36 % der Befragten £21–40 für ein Vatertagsgeschenk, je rund 17 % über £100 bzw. höchstens £20. Alkohol ist mit 31 % ein Top-Geschenk.**

> “The classic option of a bottle of alcohol (whiskey, wine, etc.) remains a top contender (31%). ... More than a third (36%) of respondents plan to spend between £21 and £40. Around 17% intend to purchase more expensive gifts (£101+), while a notable 17% prefer budget-friendly options, planning to spend £20 or under.”

- **Quelle:** [YouGov: What are Britons gifting their dads this Father's Day?](https://yougov.com/en-gb/articles/49555-what-are-britons-gifting-their-dads-this-fathers-day)
- **Datum der Quelle:** 2024-05-30 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov, n=2.036 GB-Erwachsene 18+, national repräsentativ, online 20.–21.05.2024
- **Einordnung/Einschränkung:** Unabhängiges Institut mit offengelegter Methodik, aber Daten von 2024. Die Basis 'respondents' ist unklar (alle oder nur Schenkende). Ersetzt die verworfene Retail-Times-Zahl (4B-38). Homeware wird nicht erwähnt.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen (Primärquelle der in 4B-38 verlinkten YouGov-Angabe); Wortlaut, Methodik und Datum bestätigt.

### 1. Weihnachten – unerwünschte Geschenkkategorien

#### 4B-V08

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**In einer Finder-PR-Umfrage (Dez. 2017) waren Kleidung/Accessoires (25 %), Kosmetik/Düfte (18 %) und Haushaltsartikel (11 %) die am wenigsten geschätzten Geschenkarten. Rund 14 % der unerwünschten Geschenke kamen von den Eltern.**

> “Clothing and accessories were the least liked type of gift (25.03 percent), followed by cosmetics and fragrances (17.63 percent) and household items (11.49 percent). ... followed by parents (13.92 percent) and parents-in-law (11.31 percent).”

- **Quelle:** [Finder UK Press Release December 2017: Brits expected to waste £5 billion on unwanted gifts this Christmas](https://www.finder.com/uk/media/press-release-december-2017-brits-expected-to-waste-5-billion-on-unwanted-gifts-this-christmas)
- **Datum der Quelle:** 2017-12-31 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Mortar London für finder.com, n=2.000 UK-Erwachsene, Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Veraltete PR-Umfrage ohne vollständige Methodik. Nur als Warnsignal für Angle D nutzen: Haushaltsartikel gehören zu den häufiger unerwünschten Geschenken. Nicht in Ads verwenden.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Sätze wörtlich in der Pressemitteilung gefunden.

### 2. Muttertag – Stellenwert (Mintel 2017)

#### 4B-V09

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut Mintel (März 2017) war der Muttertag in UK das Frühjahrs-/Sommer-Event, für das die meisten Verbraucher Geld ausgeben, mehr als für Ostern, Valentinstag oder Vatertag. Ein Umsatzranking ist das nicht.**

> “it remains the most purchased for event in the Spring/Summer season ... a greater number of consumers spending money on Mother's Day than on the other events like Easter, Valentine's Day and Father's Day”

- **Quelle:** [Mintel: Mother's Day 2017](https://www.mintel.com/insights/retail/mothers-day-2017/)
- **Datum der Quelle:** 2017-03-24 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Mintel; Methodik und Zahlen auf der Seite nicht angegeben
- **Einordnung/Einschränkung:** Seriöses Institut, aber veraltet (2017). Bezieht sich auf die Zahl der Käufer, nicht auf den Umsatz, und nur auf Frühjahr/Sommer. Stützt NICHT die Behauptung 'drittgrößtes Handelsereignis' (4B-34).
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Wortlaut und Datum (24.03.2017, aktualisiert 10.01.2023) bestätigt.

### 2. Muttertag – Vergleich Ostern (GlobalData)

#### 4B-V10

⚠️ EINGESCHRÄNKT · Angle: Markt

**GlobalData prognostizierte für Ostern 2025 in UK Ausgaben von £2,3 Mrd., etwa gleichauf mit der GlobalData-Prognose für den Muttertag 2025 (£2,4 Mrd.).**

> “projected total expenditure of GBP2.3 billion”

- **Quelle:** [GlobalData: UK consumers to shell out GBP2.3 billion on Easter](https://www.globaldata.com/media/retail/uk-consumers-to-shell-out-gbp2-3-billion-on-easter-reveals-globaldata/)
- **Datum der Quelle:** 2025-04-07 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** GlobalData; Methodik nicht öffentlich
- **Einordnung/Einschränkung:** Prognose ohne offengelegte Methodik. Dient nur als Gegenbeleg zum Mythos 'drittgrößtes Handelsereignis' (4B-34).
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Wortlaut und Datum 07.04.2025 bestätigt.

### 4. Ältere online – Age UK 2025

#### 4B-V11

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut Age UK (Juli 2025) nutzen 2,4 Mio. (19 %) ältere Menschen in UK das Internet kaum (seltener als einmal im Monat) oder gar nicht. Die Altersgrenze ist in der Mitteilung nicht definiert.**

> “2.4 million (19%, nearly one in five) older people have limited use of the internet ... using it less than once a month or not at all”

- **Quelle:** [Age UK: Age UK warns 2.4 million digitally excluded older people are at risk of being left behind in an increasingly digital world](https://www.ageuk.org.uk/latest-press/articles/age-uk-warns-22.4-million-digitally-excluded-older-people-are-at-risk-of-being-left-behind-in-an-increasingly-digital-world/)
- **Datum der Quelle:** 2025-07-29 · **Typ:** Fachgesellschaft/Charity
- **Stichprobe/Methodik:** 'New analysis for Age UK'; Datenquelle, n und Altersband nicht angegeben
- **Einordnung/Einschränkung:** Aktuellste gefundene Zahl zur Internetnutzung Älterer, aber Methodik und Altersgrenze sind nicht offengelegt. Zur Online-Kaufquote der 65+ sagt sie nichts. Stützt die Schlussfolgerung, für Angle D eher die Kinder und Enkel als Käufer anzusprechen.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen; Wortlaut und Datum 29.07.2025 (aktualisiert 29.12.2025) bestätigt; keine Angaben zum Online-Einkauf.

## Track 4C: Q4-Kalender UK 2026 / Januar-Sales

*Prüf-Fazit: Der Track ist insgesamt verlässlich: Ich habe alle 61 Claims selbst an den Quellen geöffnet. Die meisten Zahlen, Daten und Wortlaute stimmten. Korrigiert habe ich unter anderem einen nicht auffindbaren Wortlaut (World Menopause Day; neue Sekundärquellen), ein unbelegtes 'erstmals' (Adobe Boxing Day), eine übertriebene Which?-Formulierung, den Messzeitraum der BRC-Preise und den Tracked-24-Widerspruch. Einen Claim habe ich verworfen: 'National Bed Month' ist nicht eingestellt, er fand laut NBF-Primärquelle im März 2026 statt. Royal Mail 2025 habe ich durch die Primärquelle hochgestuft und elf geprüfte Fakten ergänzt (Salesforce UK, ONS, NBF sowie die CMA-Fälle Emma Sleep, Simba und Wayfair). Schwach bleiben die Adobe- und Barclays-Zahlen (nur Sekundärquellen), alle Versandtermine 2026 (noch nicht veröffentlicht) und der World Menopause Day (IMS-Seite gesperrt). Wichtig für die Ads: Marktzahlen zu Black Friday 2025 widersprechen sich je nach Messmethode. Es gibt keine Bettwaren-spezifischen Zahlen. Die CMA verfolgt Countdown- und Rabattangaben gerade in der Bettwarenbranche aktiv.*

### 1 Black Friday / Cyber Weekend 2026

#### 4C-01

✅ BELEGT · Angle: Markt, D Geschenk

**Black Friday fällt 2026 auf Freitag, den 27. November 2026 (Freitag nach dem US-Thanksgiving am Donnerstag, 26.11.2026).**

> “Date Day after US Thanksgiving ... 2026 date November 27”

- **Quelle:** [Wikipedia – Black Friday (shopping), Infobox](https://en.wikipedia.org/wiki/Black_Friday_(shopping))
- **Datum der Quelle:** 2026-09-17 (zuletzt bearbeitet) · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Das Datum folgt aus dem Kalender (Freitag nach dem vierten Donnerstag im November); nachgerechnet: 26.11.2026 ist ein Donnerstag, 27.11.2026 ein Freitag. Die ONS bestätigt die Regel für 2025 ('Black Friday took place on 28 November 2025'). Wikipedia ist keine Primärquelle, das Datum ist aber eindeutig ableitbar.
- **Wahrheits-Check:** *bestätigt*. Seite abgerufen, Infobox '2026 date November 27' gefunden; Wochentage per Kalender geprüft; Datum der letzten Bearbeitung ergänzt.

#### 4C-02

✅ BELEGT · Angle: Markt, D Geschenk

**Cyber Monday ist 2026 am Montag, 30. November 2026; das Cyber Weekend umfasst damit Freitag, 27., bis Montag, 30.11.2026.**

> “2026 date November 30 ... Cyber Monday is a marketing term for the Monday after Thanksgiving in the United States, to encourage e-commerce and online shopping.”

- **Quelle:** [Wikipedia – Cyber Monday, Infobox und Einleitung](https://en.wikipedia.org/wiki/Cyber_Monday)
- **Datum der Quelle:** 2026-08-04 (zuletzt bearbeitet) · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Kalenderregel nachgerechnet (Montag nach Thanksgiving am 26.11.2026). Der 30.11.2026 ist laut gov.uk in Schottland zugleich Bankfeiertag (St Andrew's Day, im JSON bestätigt). Adobe misst das 'Cyber Weekend' über die vier Tage von Black Friday bis Cyber Monday, IMRG eine 8-Tage-Woche (Mo–Mo), Salesforce die Cyber Week vom 25.11. bis 01.12.
- **Wahrheits-Check:** *bestätigt*. Infobox und Einleitung wörtlich gefunden; 30.11.2026 = Montag geprüft; St Andrew's Day 2026-11-30 im gov.uk-JSON bestätigt.

### 1 Black Friday / Cyber Weekend – Umsatz 2025

#### 4C-03

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Adobe Analytics gaben britische Käufer 2025 an den vier Tagen von Black Friday bis Cyber Monday online 3,8 Mrd. £ aus, 4,6 % mehr als im Vorjahr.**

> “LONDON, Dec 2 (Reuters) - British shoppers spent 3.8 billion pounds ($5.0 billion) online across the four days of Black Friday to Cyber Monday, up 4.6% year-on-year, according to data from Adobe Analytics published on Tuesday.”

- **Quelle:** [Global Banking & Finance Review – Abdruck einer Reuters-Meldung (Adobe-Analytics-Daten)](https://www.globalbankingandfinance.com/holidayshopping-retail-black-friday-britain-nine/)
- **Datum der Quelle:** 2025-12-02 · **Typ:** Presse
- **Einordnung/Einschränkung:** Nur Online-Umsätze, nur das Adobe-Analytics-Panel. Die Adobe-Primärseite (business.adobe.com/uk/resources/holiday-shopping-report.html) war auch bei der Prüfung nicht abrufbar (503 bzw. HTTP/2-Abbruch). Die Zahl widerspricht dem IMRG-Index (−1,2 % in der 8-Tage-Woche), weil Messbasis und Zeitraum verschieden sind. Für Ads keine Aussage wie 'Rekord-Black-Friday' ableiten.
- **Wahrheits-Check:** *bestätigt*. Reuters-Text wörtlich auf der Seite gefunden (Posted on December 2, 2025); Adobe-Primärquelle erneut versucht (503).

#### 4C-04

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Adobe war Black Friday 2025 mit 1,16 Mrd. £ Online-Ausgaben der umsatzstärkste Online-Tag des Jahres in UK; November und Dezember 2025 zusammen brachten 26,9 Mrd. £ online (+4,1 %).**

> “The data shows UK consumers spent £26.9 billion online during November and December 2025. That figure rose 4.1% from the same period in 2024. ... Adobe said Black Friday was the biggest online shopping day of the year, with £1.16 billion spent. Cyber Weekend delivered £3.8 billion in online spend, it said.”

- **Quelle:** [CMOtech UK (TechDay) – Bericht über Adobe-Digital-Insights-Daten zur Saison 2025](https://cmotech.uk/story/mobile-ai-power-record-uk-online-christmas-sales)
- **Datum der Quelle:** 2026-01-20 · **Typ:** Presse
- **Einordnung/Einschränkung:** Sekundärquelle für Adobe-Daten, die Adobe-Seite war nicht abrufbar. Gilt nur online und nur für das Adobe-Händlerpanel. Laut demselben Artikel entfielen 61,5 % der Online-Ausgaben in November und Dezember auf Mobilgeräte, und Adobe nennt den Zeitraum 'the highest online spending Christmas period on record'. Die Methodik ist nicht einsehbar.
- **Wahrheits-Check:** *bestätigt*. Alle Zahlen (26,9 Mrd., 4,1 %, 1,16 Mrd., 3,8 Mrd., 61,5 %) wörtlich gefunden; Datum 20.01.2026 bestätigt.

#### 4C-05

✅ BELEGT · Angle: Markt

**Laut IMRG Online Retail Index sank der Online-Umsatz in UK in der 8-tägigen Black-Friday-Woche 2025 (24.11.–01.12.) um 1,2 % gegenüber dem Vorjahr; der Black Friday selbst lag bei +1,3 %.**

> “Across the 8-day Black Friday week (Mon 24th Nov-Mon 1st Dec), total market revenue was down -1.2% Year-on-Year (see the first green bar on the chart above) according to IMRG data. Black Friday itself was up +1.3% YoY, but the standout performer was Tuesday which was up +4.4% YoY.”

- **Quelle:** [IMRG – Black Friday 2025: the data and insights are in (Ellie-Rose Davies)](https://www.imrg.org/blog/black-friday-2025-the-data-and-insights-are-in/)
- **Datum der Quelle:** 2025-12-22 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Primärquelle des Branchenverbands, Umsatzdaten teilnehmender Online-Händler. Für dieses Index-Panel klar belegt, aber im Widerspruch zu Adobe (+4,6 %) und Salesforce (+3 %). Für Ads deshalb weder 'Black Friday wächst' noch 'schrumpft' als Gesamtmarktaussage verwenden.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und 'Published 22/12/25' auf der Seite bestätigt.

#### 4C-06

✅ BELEGT · Angle: Markt

**Laut IMRG lag der Online-Umsatz in UK am Cyber Monday 2025 um 3,2 % unter dem Vorjahr.**

> “Interestingly, Cyber Monday was down -3.2% YoY; last year Cyber Monday was flat and in 2023 it performed exceptionally well (+5.6% YoY).”

- **Quelle:** [IMRG – Black Friday 2025: the data and insights are in](https://www.imrg.org/blog/black-friday-2025-the-data-and-insights-are-in/)
- **Datum der Quelle:** 2025-12-22 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Primärquelle des IMRG-Index; gilt nur für das IMRG-Händlerpanel und nur online.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Seite gefunden.

#### 4C-07

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Barclays-Kartendaten war Black Friday (28.11.2025) der bis dahin transaktionsstärkste Einzelhandelstag 2025, mit 62,5 % mehr Transaktionen als an einem durchschnittlichen Tag 2025.**

> “Overall retail spending dipped -1.1 per cent in November, however retailers enjoyed their busiest day of the year so far on Black Friday (28th), with transaction volumes up 62.5 per cent in comparison to the average day in 2025.”

- **Quelle:** [InsightDIY – Wiedergabe des Barclays Consumer Spend Report November 2025](https://www.insightdiy.co.uk/news/barclays-card-spending-sees-greatest-fall-since-2021/15883.htm)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Presse
- **Einordnung/Einschränkung:** Gilt nur für Karten von Barclays-Kunden (Barclays sieht laut eigener Angabe knapp 40 % der UK-Kartentransaktionen). Gezählt wird die Zahl der Transaktionen, nicht der Wert, und verglichen wird mit einem Durchschnittstag, nicht mit Black Friday 2024. Eine Barclays-Primärseite für November 2025 war nicht auffindbar; mehrere URL-Varianten auf home.barclays ergaben 404.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum 09.12.2025 auf InsightDIY bestätigt; Primärquelle weiterhin nicht gefunden (404).

#### 4C-08

⚠️ EINGESCHRÄNKT · Angle: Markt

**Die Kartenausgaben von Barclays-Kunden in UK sanken im November 2025 um 1,1 % gegenüber dem Vorjahr, der stärkste Rückgang seit Februar 2021.**

> “Consumer card spending declined -1.1 per cent year-on-year in November – the greatest fall recorded since February 2021 (-9.5 per cent), and considerably lower than the latest CPIH inflation rate of 3.8 per cent.”

- **Quelle:** [InsightDIY – Wiedergabe des Barclays Consumer Spend Report November 2025](https://www.insightdiy.co.uk/news/barclays-card-spending-sees-greatest-fall-since-2021/15883.htm)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Presse
- **Einordnung/Einschränkung:** Gilt nur für Barclays-Debit- und Barclaycard-Kreditkarten, nominal, ohne Bargeld und andere Banken. Die Primärseite war nicht abrufbar (404). Zeigt, dass Black Friday 2025 in ein schwaches Konsumumfeld fiel.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Seite gefunden.

#### 4C-12

✅ BELEGT · Angle: Markt

**Laut BRC-KPMG Retail Sales Monitor stiegen die UK-Einzelhandelsumsätze im Black-Friday-Monat November 2025 (02.–29.11.) nur um 1,4 % gegenüber dem Vorjahr, das schwächste Wachstum seit sechs Monaten.**

> “UK Total retail sales increased by 1.4% year on year in November, against a decline of 3.3% in November 2024. ... Pre-Budget jitters among shoppers meant the month of Black Friday did not deliver as strongly as retailers had hoped or the economy needed. Sales growth was the weakest in six months, despite the elevated inflation.”

- **Quelle:** [British Retail Consortium – Pre-Budget jitters dampen Black Friday sales (BRC-KPMG Retail Sales Monitor)](https://brc.org.uk/news-and-events/news/corporate-affairs/2025/ungated/pre-budget-jitters-dampen-black-friday-sales/)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG Retail Sales Monitor, 4 Wochen 02.–29.11.2025, UK, Umsätze von BRC-Mitgliedern (nominal)
- **Einordnung/Einschränkung:** Primärquelle mit klarem Zeitraum. Non-Food lag nur bei +0,1 %. Nominale Werte, also nicht inflationsbereinigt. Der Vorjahresvergleich ist verzerrt: Laut Sekundärquelle (MarketNews, 03.12.2024; nicht primär geprüft) lag der BRC-Zeitraum November 2024 vom 27.10. bis 23.11.2024 und enthielt Black Friday nicht. Die ONS-Aussage zu ihrem eigenen Berichtszeitraum lässt sich nicht direkt auf den BRC übertragen.
- **Wahrheits-Check:** *korrigiert*. Zahl, Zeitraum und Datum bestätigt; Wortlaut um den Satz 'weakest in six months' ergänzt; Begründung zum Basiseffekt präzisiert (ONS-Zeitraum ≠ BRC-Zeitraum).

### 1 Black Friday / Cyber Weekend – Erwartungen 2025

#### 4C-09

⚠️ EINGESCHRÄNKT · Angle: Markt

**Vor Black Friday 2025 wollten laut Barclays-Umfrage 43 % der UK-Erwachsenen Deals suchen, mit durchschnittlich geplanten 430 £ pro Käufer und hochgerechnet über 10,2 Mrd. £ insgesamt.**

> “Barclays’ research indicates that Black Friday, which arrives on November 28th, will see those shopping spending an average of £430 each - £91 more than last year – amounting to a total of over £10.2 billion. Over two in five UK adults (43%) will be on the hunt for deals, up six percentage points up from 2024’s figure.”

- **Quelle:** [Barclays – Black Friday spending (Barclays Consumer Spend Report, Insights)](https://home.barclays/insights/2025/11/Black-Friday-Predicted-Spend/)
- **Datum der Quelle:** 2025-11 (laut URL; kein Datum auf der Seite) · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Barclays Consumer Spend Report; Institut, n und Feldzeit stehen nicht auf der Seite (Presseberichte nennen Opinium, >2.000 Befragte – nicht primär verifiziert)
- **Einordnung/Einschränkung:** Das sind Kaufabsichten aus einer von Barclays beauftragten Umfrage, keine tatsächlichen Ausgaben. Die 10,2 Mrd. £ sind eine Barclays-Hochrechnung. Die tatsächlichen Daten (4C-07, 4C-08) zeigen eine schwächere Entwicklung.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Seite gefunden; keine Methodik auf der Seite.

### 1 Glaubwürdigkeit Black-Friday-Rabatte

#### 4C-10

⚠️ EINGESCHRÄNKT · Angle: Markt, Allgemein

**68 % der von Barclays befragten UK-Erwachsenen sind skeptisch, ob Black-Friday- und Cyber-Monday-Deals wirklich etwas wert sind.**

> “Nearly seven in 10 (68%) are sceptical about the real value of Black Friday and Cyber Monday deals, and 65% believe such sales events encourage unnecessary spending.”

- **Quelle:** [Barclays – Black Friday spending (Barclays Consumer Spend Report, Insights)](https://home.barclays/insights/2025/11/Black-Friday-Predicted-Spend/)
- **Datum der Quelle:** 2025-11 (laut URL) · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Barclays Consumer Spend Report; Methodik auf der Seite nicht angegeben
- **Einordnung/Einschränkung:** Unternehmensumfrage ohne offengelegte Stichprobe. Die Richtung passt zu Which? (4C-20, 4C-21). Für Ads relevant: Rabattbotschaften brauchen echte, nachprüfbare Referenzpreise.
- **Wahrheits-Check:** *bestätigt*. Zahl 68 % zweimal auf der Seite gefunden; Wortlaut um den Fließtext-Satz ergänzt.

### 1 Trend zu längeren Aktionszeiträumen

#### 4C-11

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Barclays begannen 2025 60 % der Käufer schon im Oktober mit der Suche nach Black-Friday-Deals ('eher ein Marathon als ein Sprint').**

> “The sales event is now more of a marathon than a sprint, with 60 per cent of shoppers starting their search as early as October, presenting businesses with ample opportunity to engage savvy consumers on the hunt for deals.”

- **Quelle:** [Barclays – Black Friday spending (Zitat Harshna Cayley, Head of Payment Acceptance, Barclaycard Payments)](https://home.barclays/insights/2025/11/Black-Friday-Predicted-Spend/)
- **Datum der Quelle:** 2025-11 (laut URL) · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Barclays-Umfrage; Methodik auf der Seite nicht angegeben
- **Einordnung/Einschränkung:** Zitat eines Unternehmensvertreters mit einer Umfragezahl ohne offengelegte Methodik. Inhaltlich gestützt durch IMRG (4C-16), BRC (4C-17) und ONS (4C-15).
- **Wahrheits-Check:** *bestätigt*. Zitat und Sprecherin auf der Seite gefunden.

#### 4C-15

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut ONS fiel Black Friday 2025 (28.11.) in den November-Berichtszeitraum, und einige Händler führten höhere Kaufhausumsätze auf längere Black-Friday-Rabattphasen zurück.**

> “Department stores' sales volumes rose, which some retailers attributed to longer Black Friday discounting, while retailers of footwear and leather goods also did well.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: November 2025](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/november2025)
- **Datum der Quelle:** 2025-12-19 · **Typ:** Behörde/NHS/Statistikamt
- **Einordnung/Einschränkung:** Amtliche Quelle, die Begründung 'longer Black Friday discounting' stammt aber aus Händlerkommentaren, ist also qualitativ. Der Berichtszeitraum war der 02.–29.11.2025; 2024 fiel Black Friday laut ONS in den Dezember-Zeitraum. Nur Großbritannien.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum bestätigt.

#### 4C-16

✅ BELEGT · Angle: Markt

**Im IMRG-Panel von 278 Händlern hatten am ersten Werktag im November 2025 bereits 58 Händler eine Black-Friday-Kampagne live (2021: 12; 2023: 41); 60 % starteten früher als 2024, 50 % ließen ihre Kampagnen länger laufen.**

> “From our panel of 278 retailers, we have noted that each year more and more retailers have a live Black Friday campaign running on the 1st working day of November. From 12 retailers in 2021, to 41 in 2023, and 58 and 2025. 60% of retailers launched their campaign earlier this year compared to 2024, only 4% kept their campaign the same, and 36% went later. What is interesting is that while retailers started earlier, most also ran their campaigns for longer (50%).”

- **Quelle:** [IMRG – Black Friday 2025: the data and insights are in](https://www.imrg.org/blog/black-friday-2025-the-data-and-insights-are-in/)
- **Datum der Quelle:** 2025-12-22 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** IMRG-Händlerpanel, n=278 Online-Händler, UK, 2021–2025
- **Einordnung/Einschränkung:** Primärquelle mit genannter Panelgröße. Gilt für das IMRG-Panel, nicht für den Gesamtmarkt. Der Tippfehler '58 and 2025' steht so in der Quelle.
- **Wahrheits-Check:** *bestätigt*. Wortlaut vollständig auf der Seite gefunden; die 50 % für längere Laufzeit aus der Begründung in die Aussage übernommen.

#### 4C-17

✅ BELEGT · Angle: Markt

**Laut BRC begannen die Black-Friday-Deals 2025 früher als üblich, und die Non-Food-Ladenpreise in UK lagen in der Messwoche 01.–07.11.2025 um 0,6 % unter dem Vorjahr.**

> “Period Covered: 01 – 07 November 2025 ... Non-Food inflation decreased to -0.6% year on year in November, against a decline of -0.4% in October. ... Black Friday deals began earlier than normal as competition between retailers hit fever pitch.”

- **Quelle:** [British Retail Consortium – Black Friday comes early as competition heats up (BRC-NielsenIQ Shop Price Monitor; Zitat Helen Dickinson)](https://brc.org.uk/news-and-events/news/corporate-affairs/2025/ungated/black-friday-comes-early-as-competition-heats-up/)
- **Datum der Quelle:** 2025-12-02 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-NielsenIQ Shop Price Monitor, Messzeitraum 01.–07.11.2025
- **Einordnung/Einschränkung:** Primärquelle. Die Preisänderung ist ein Messwert, erhoben aber nur in der ersten Novemberwoche, nicht im ganzen Monat. 'Earlier than normal' ist eine qualitative Einschätzung der BRC-Chefin. Die gesamte Ladenpreisinflation lag bei 0,6 %.
- **Wahrheits-Check:** *korrigiert*. Messzeitraum (01.–07.11.2025) laut Seite ergänzt; 'im November 2025' war zu weit gefasst.

### 1 Online-Anteil

#### 4C-13

✅ BELEGT · Angle: Markt

**Im November 2025 wurden laut BRC 44 % der Non-Food-Käufe in UK online getätigt (November 2024: 43,8 %), der höchste Wert seit 2022.**

> “The online penetration rate (the proportion of Non-Food items bought online) increased to 44% in November from 43.8% in November 2024. This was above the 12-month average of 37.3%. ... Not unexpectedly, online dominated, with the proportion of non-food bought online reaching its highest level since 2022.”

- **Quelle:** [British Retail Consortium – Pre-Budget jitters dampen Black Friday sales](https://brc.org.uk/news-and-events/news/corporate-affairs/2025/ungated/pre-budget-jitters-dampen-black-friday-sales/)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG Retail Sales Monitor, 02.–29.11.2025, UK
- **Einordnung/Einschränkung:** Primärquelle; gilt nur für Non-Food und BRC-Mitglieder. Der Halbsatz 'höchster Wert seit 2022' steht wörtlich im Zitat von BRC-Chefin Helen Dickinson. Saisonal: Im Oktober 2025 lag die Quote bei 37,9 %, im Dezember 2025 bei 38,6 %, im Januar 2026 bei 37,2 %.
- **Wahrheits-Check:** *korrigiert*. Die Begründung behauptete, 'seit 2022' stehe nicht im BRC-Wortlaut. Das ist falsch, es steht dort; Wortlaut ergänzt. Saisonwerte auf den BRC-Seiten Okt/Dez/Jan geprüft.

#### 4C-14

✅ BELEGT · Angle: Markt

**Laut ONS wurden im Dezember 2025 28,3 % aller Einzelhandelsumsätze in Großbritannien online getätigt (November 2025 revidiert: 28,0 %).**

> “Total spend (the sum of in-store and online sales) rose by 0.8% over the month. As a result, the proportion of sales made online rose from 28.0% in November 2025 to 28.3% in December 2025.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: December 2025](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/december2025)
- **Datum der Quelle:** 2026-01-23 · **Typ:** Behörde/NHS/Statistikamt
- **Einordnung/Einschränkung:** Amtliche Statistik, aber nur Großbritannien (ohne Nordirland) und alle Einzelhandelsumsätze inklusive Lebensmittel und Kraftstoff. Der November-Wert wurde revidiert: Im November-Bulletin (19.12.2025) stand noch 28,6 %. Neuester Wert: 28,8 % im August 2026 (siehe 4C-V05).
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Release date 23.01.2026 bestätigt; 28,6 % im November-Bulletin bestätigt; Verweis auf neueren Wert ergänzt.

### 1 Black Friday – Vorlauf und Kategorien

#### 4C-18

✅ BELEGT · Angle: Markt, D Geschenk

**Im Oktober 2025 (05.10.–01.11.) stiegen die UK-Einzelhandelsumsätze laut BRC um 1,6 %; viele Käufer warteten auf Black Friday, während Möbel und Homeware besser liefen, weil Haushalte sich auf Familienbesuche zu den Feiertagen vorbereiteten.**

> “October was a subdued month, with the weakest growth since May. Many delayed spending, waiting for Black Friday deals and cooler temperatures before buying toys, electronics and clothing. Furniture and other homeware fared better as people began preparing their homes ahead of family festive gatherings.”

- **Quelle:** [British Retail Consortium – Consumers hold back for Black Friday deals](https://brc.org.uk/news-and-events/news/corporate-affairs/2025/ungated/consumers-hold-back-for-black-friday-deals/)
- **Datum der Quelle:** 2025-11-11 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG Retail Sales Monitor, 4 Wochen 05.10.–01.11.2025, UK
- **Einordnung/Einschränkung:** Primärquelle; die Kategorieaussage ist qualitativ, es gibt keine Zahl für Homeware. Relevant für Angle D: Die Vorbereitung auf Weihnachtsbesuch (Gästebett, Bettwaren) ist ein Kaufanlass im Oktober und November (siehe auch 4C-V02).
- **Wahrheits-Check:** *bestätigt*. 1,6 %, Zeitraum, Datum und Zitat bestätigt.

### 1 Footfall Black Friday 2025

#### 4C-19

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut MRI Software stieg die Besucherfrequenz in UK-Einkaufslagen am Black Friday 2025 um 11,7 % gegenüber der Vorwoche, lag aber 1,9 % unter Black Friday 2024.**

> “A relatively strong week revealed daily increases in visitor activity with double digit rises recorded in all UK retail destinations on Tuesday (+10.9%), Black Friday (+11.7%), and Saturday (+10.4%), week on week. ... Retail footfall on Black Friday also remained -1.9% lower compared to Black Friday last year with shopping centres (-3.6%), once again, leading the decline, followed by high streets (-2%) and retail parks (-0.1%).”

- **Quelle:** [InsightDIY – Bericht über MRI-Software-Footfall-Daten (Black Friday Week Delivered Solid Boost Across Retail Destinations)](https://www.insightdiy.co.uk/news/black-friday-week-delivered-solid-boost-across-retail-destinations/15850.htm)
- **Datum der Quelle:** 2025-12-01 · **Typ:** Presse
- **Einordnung/Einschränkung:** Nur über die Fachpresse belegt, die MRI-Originalmitteilung habe ich nicht gefunden. Der Artikel nennt zwei Wochenabgrenzungen: Für die ganze Black-Friday-Woche lag die Frequenz im Jahresvergleich bei −2,2 % (So–Sa) bzw. −2,5 % (Mo–So). Der Tageswert am Black Friday ist in beiden −1,9 %.
- **Wahrheits-Check:** *korrigiert*. Werte bestätigt; die in der Begründung genannte Retail-Times-Zahl (−1,3 % im November) habe ich nicht geprüft und deshalb entfernt; Wochenwerte ergänzt.

### 1 Which?-Analyse Black-Friday-Preise

#### 4C-20

⚠️ EINGESCHRÄNKT · Angle: Markt, Allgemein

**Which? fand für 175 Haushalts-, Technik- und Gesundheitsgeräte von 8 großen Händlern, dass 83 % außerhalb des vierwöchigen Black-Friday-Zeitraums 2024 (15.11.–12.12.2024) mindestens einmal gleich teuer oder günstiger waren.**

> “Which? compared prices on 175 home, tech, and health appliances from eight major retailers - Amazon, AO, Argos, Boots, Currys, John Lewis, Richer Sounds, and Very. Prices were tracked for a full year surrounding the 2024 Black Friday sale (May 2024 to May 2025). Overall, the study found that 83 per cent of products were cheaper or equal in price on at least one occasion outside of the four-week Black Friday sales period in Which?’s analysis.”

- **Quelle:** [Which? – Don't believe the hype: most Black Friday deals the same price or cheaper at other times of the year](https://www.which.co.uk/policy-and-insight/article/dont-believe-the-hype-most-black-friday-deals-the-same-price-or-cheaper-at-other-times-of-the-year-which-finds-a3TbD5x5KADs)
- **Datum der Quelle:** 2025-11-25 · **Typ:** Fachgesellschaft/Charity
- **Stichprobe/Methodik:** 175 Produkte (Haushalt/Technik/Gesundheit), 8 Händler, Preise Mai 2024–Mai 2025; Black-Friday-Zeitraum 15.11.–12.12.2024
- **Einordnung/Einschränkung:** Seriöse Verbraucherorganisation mit offengelegter Methodik. Das Ergebnis gilt aber für Elektro- und Haushaltsgeräte beim Sale 2024, nicht für Bettwaren. Eine Which?-Analyse des Sales 2025 habe ich auch bei erneuter Suche nicht gefunden.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Methodik und Datum 25.11.2025 auf der Seite bestätigt.

### 1 Mythos: Black Friday = günstigster Preis des Jahres

#### 4C-21

❌ NICHT BELEGT / MYTHOS · Angle: Markt, Allgemein

**Die verbreitete Annahme, am Black Friday gebe es den günstigsten Preis des Jahres, ist nicht belegt: Bei der Which?-Preisverfolgung (175 Geräte, 8 Händler, Sale 2024) war am Black-Friday-Tag selbst kein einziger Deal zu seinem Tiefstpreis des Untersuchungsjahres.**

> “On the day of Black Friday itself, Which? found there were no deals at all that were at their cheapest of the year surrounding the sale, suggesting that shoppers have plenty of time to bag a good deal this year. ... When Which? looked solely at Black Friday itself, it found none of the deals were at their cheapest only on that day.”

- **Quelle:** [Which? – Don't believe the hype: most Black Friday deals the same price or cheaper at other times of the year](https://www.which.co.uk/policy-and-insight/article/dont-believe-the-hype-most-black-friday-deals-the-same-price-or-cheaper-at-other-times-of-the-year-which-finds-a3TbD5x5KADs)
- **Datum der Quelle:** 2025-11-25 · **Typ:** Fachgesellschaft/Charity
- **Stichprobe/Methodik:** 175 Produkte, 8 Händler, Preisverlauf Mai 2024–Mai 2025
- **Einordnung/Einschränkung:** Mythos-Check: Die Behauptung 'Black Friday = bester Preis' widerspricht der Which?-Preisverfolgung. Die Aussage betrifft die am Black Friday angebotenen Deals, nicht zwingend alle 175 Produkte, und Geräte, nicht Bettwaren. Für eigene Ads folgt daraus: keine Aussage wie 'niedrigster Preis des Jahres', solange sie nicht für das eigene Produkt belegbar ist.
- **Wahrheits-Check:** *korrigiert*. Unbelegtheit bestätigt; Aussage von 'kein einziges der 175 Produkte' auf 'kein Deal am Black-Friday-Tag' korrigiert, weil die Quelle von 'deals' spricht; zweiten Quellsatz ergänzt.

### 1 Mythos: Black Friday 2025 war ein Rekordjahr

#### 4C-22

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Eine pauschale Aussage, Black Friday 2025 habe in UK Rekordumsätze gebracht, ist nicht belastbar: Gesamtmarktdaten zeigen Schwäche (BRC +1,4 % im November, schwächstes Wachstum seit sechs Monaten; IMRG −1,2 % in der Black-Friday-Woche; Barclays-Kartenausgaben −1,1 %). Nur Anbieterpanels für Online-Umsätze (Adobe +4,6 %, Salesforce +3 % bei −1 % Bestellungen) melden Wachstum bzw. einen 'Rekord'.**

> “Sales growth was the weakest in six months, despite the elevated inflation.”

- **Quelle:** [British Retail Consortium – Pre-Budget jitters dampen Black Friday sales](https://brc.org.uk/news-and-events/news/corporate-affairs/2025/ungated/pre-budget-jitters-dampen-black-friday-sales/)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Marktforschung
- **Einordnung/Einschränkung:** Mythos-Check: BRC, IMRG und Barclays zeigen ein schwaches Bild. Adobe (Online, +4,6 %) und Salesforce ('record-breaking week', über 6 Mrd. £, +3 %, Bestellungen in UK −1 %) melden Online-Wachstum aus eigenen Panels. Eine 'Rekord'-Aussage hängt also an der Messbasis und ist für den Gesamtmarkt nicht belegt. Ads sollten nicht mit Rekord- oder 'alle kaufen jetzt'-Aussagen arbeiten.
- **Wahrheits-Check:** *korrigiert*. Die Begründung 'nur Adobe meldet Wachstum' ist falsch, auch Salesforce meldet für UK einen 'record'. Aussage und Begründung präzisiert; Unbelegtheit als Gesamtmarktaussage bestätigt.

### 2 Feiertage Weihnachten 2026

#### 4C-23

✅ BELEGT · Angle: D Geschenk, Allgemein

**Weihnachten 2026 ist Freitag, 25.12.2026; weil Boxing Day auf einen Samstag fällt, ist Montag, 28.12.2026, in England/Wales, Schottland und Nordirland Ersatz-Bankfeiertag.**

> “Upcoming bank holidays in England and Wales 2026 | Date | Day of the week | Bank holiday | 25 December | Friday | Christmas Day | 28 December | Monday | Boxing Day (substitute day)”

- **Quelle:** [GOV.UK – UK bank holidays (Seite und bank-holidays.json)](https://www.gov.uk/bank-holidays)
- **Datum der Quelle:** 2025-08-11 (dateModified laut Seitenmetadaten) · **Typ:** Parlament/Regierung
- **Einordnung/Einschränkung:** Offizielle Regierungsseite. Im JSON steht für alle drei Landesteile 'Boxing Day', 2026-12-28, 'Substitute day'. Heiligabend (Do 24.12.2026) ist kein Bankfeiertag. Für die Versandplanung: Zwischen Fr 25.12. und Mo 28.12. liegt ein langes Wochenende.
- **Wahrheits-Check:** *bestätigt*. Tabellenzeile auf der Seite und JSON-Einträge für alle drei Landesteile bestätigt; Seitendatum ergänzt.

### 2 Feiertage Neujahr 2027

#### 4C-24

✅ BELEGT · Angle: Allgemein

**Neujahr ist Freitag, 01.01.2027 (UK-weit Bankfeiertag); in Schottland ist zusätzlich Montag, 04.01.2027, als Ersatztag für den 2. Januar frei.**

> “4 January | Monday | 2nd January (substitute day)”

- **Quelle:** [GOV.UK – UK bank holidays (Abschnitt Scotland) und bank-holidays.json](https://www.gov.uk/bank-holidays)
- **Datum der Quelle:** 2025-08-11 (dateModified laut Seitenmetadaten) · **Typ:** Parlament/Regierung
- **Einordnung/Einschränkung:** Offizielle Quelle. Im JSON: scotland '2nd January', 2027-01-04, 'Substitute day'; New Year’s Day 2027-01-01 in allen Landesteilen.
- **Wahrheits-Check:** *bestätigt*. Wortlaut an den Tabellentext der Seite angepasst; JSON bestätigt.

### 2 Letzte Versandtage Royal Mail (Referenz 2025)

#### 4C-25

✅ BELEGT · Angle: D Geschenk

**Für Weihnachten 2025 lagen die letzten empfohlenen Royal-Mail-Einlieferungstage (UK-Inland) bei Mi 17.12. (2nd Class), Sa 20.12. (1st Class) und Di 23.12.2025 (Special Delivery Guaranteed); die Termine für 2026 waren am 08.10.2026 nicht veröffentlicht.**

> “Royal Mail is also reminding people to send their cards by the last recommended posting dates to arrive in time for the big day - Wednesday 17 December for Second Class and Saturday 20 December for First Class. [Post Office, 2025:] Royal Mail’s Special Delivery Guaranteed: Tuesday 23rd December”

- **Quelle:** [Royal Mail / International Distribution Services – Royal Mail announces magical card prize draw and last posting dates for Christmas; ergänzend Post Office (Mynewsdesk) für Special Delivery](https://www.internationaldistributionservices.com/en/press-centre/press-releases/royal-mail/royal-mail-announces-magical-card-prize-draw-and-last-posting-dates-for-christmas/)
- **Datum der Quelle:** 2025-11-24 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärquelle von Royal Mail für 2nd und 1st Class, ausdrücklich nur als Referenz für 2025. Special Delivery Di 23.12.2025 laut Post Office. Achtung: Der Infokasten 'Full Last recommended posting dates' derselben Royal-Mail-Mitteilung nennt veraltete Termine von 2024 (Wednesday 18, Friday 20, Saturday 21, Monday 23 December); maßgeblich ist der Fließtext. Für 2026 gilt: Die Royal-Mail-Pressemitteilungsliste enthielt bis 07.10.2026 keine Termine, und royalmail.com blockiert den Abruf (403). Weihnachten 2026 fällt auf einen Freitag, nicht 1:1 übertragbar.
- **Wahrheits-Check:** *hochgestuft*. Royal-Mail-Primärquelle (24.11.2025) über die IDS-Pressemitteilungsliste gefunden; 2nd/1st Class dort bestätigt, Special Delivery über Post Office. Einordnung von EINGESCHRAENKT auf BELEGT (als Referenz 2025).

### 2 Letzte Versandtage Royal Mail Tracked (Referenz 2025)

#### 4C-26

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**2025 galten laut Post Office für Royal Mail Tracked 48 Fr 19.12. und für Tracked 24 So 21.12.2025 als letzte Einlieferungstage; eine abweichende Angabe 'Mo 22.12.' ließ sich nicht belegen.**

> “Last Royal Mail Tracked 48 date: Friday 19th December ... Last Royal Mail Tracked 24 date: Sunday 21st December”

- **Quelle:** [Post Office (Mynewsdesk) – Post Office Announces Last Posting Dates for Sending Christmas Presents](https://www.mynewsdesk.com/uk/post-office/pressreleases/post-office-announces-last-posting-dates-for-sending-christmas-presents-3420939)
- **Datum der Quelle:** 2025-12-10 (Datumszeile im Text; Mynewsdesk-Zeitstempel 19.12.2025) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Simply Business (10.11.2025) nennt ebenfalls Fr 19.12. für Tracked 48 und So 21.12. für Tracked 24. Die Royal-Mail-Primärmitteilung nennt für Tracked 48/24 nur veraltete Termine von 2024 im Infokasten. Den HuffPost-Artikel mit 'Mo 22.12.' habe ich nicht gefunden; Montag, 22.12., galt laut Post Office für Parcelforce express24. Nur als Referenz für 2025 verwenden.
- **Wahrheits-Check:** *korrigiert*. Widerspruch geprüft: zwei unabhängige Quellen nennen So 21.12.; die Angabe 'Mo 22.12.' war nicht auffindbar und ist aus der Aussage entfernt.

### 2 Letzte Versandtage Parcelforce, Evri, DPD (Referenz 2025)

#### 4C-27

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Für Weihnachten 2025 lagen die letzten Einlieferungstage über Post-Office-Filialen bei Parcelforce express48 am Fr 19.12. und express24 am Mo 22.12., bei Evri Standard am Fr 19.12. und Next Day am Mo 22.12., bei DPD 2Day am Sa 20.12., Next Day am Mo 22.12. und DPD Gold am Di 23.12.2025.**

> “Last Parcelforce express48 date: Friday 19th December ... Last Evri Standard date: Friday 19th December ... Last DPD 2Day date: Saturday 20th December ... Last Parcelforce express24 date: Monday 22nd December Last Evri Next Day date: Monday 22nd December Last DPD Next Day date: Monday 22nd December (some postcode exceptions) ... DPD Gold: Tuesday 23rd December”

- **Quelle:** [Post Office (Mynewsdesk) – Post Office Announces Last Posting Dates for Sending Christmas Presents](https://www.mynewsdesk.com/uk/post-office/pressreleases/post-office-announces-last-posting-dates-for-sending-christmas-presents-3420939)
- **Datum der Quelle:** 2025-12-10 (Datumszeile im Text; Mynewsdesk-Zeitstempel 19.12.2025) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Gilt für die Einlieferung über Post-Office-Filialen 2025. Die eigenen Seiten waren nicht prüfbar: parcelforce.com/christmas lieferte 403, die Evri-Weihnachtsseite ist leer ('can't find that page') und die DPD-URL ergab 404. Für Schottland, Inseln und Nordirland gelten oft frühere Termine. Die Termine für 2026 sind offen.
- **Wahrheits-Check:** *bestätigt*. Alle Termine in Liste und Tabelle der Mitteilung bestätigt; DPD 2Day in die Aussage aufgenommen; Datumsabweichung der Seite notiert; Carrier-Seiten selbst versucht.

### 2 Versandkapazität Q4 2026

#### 4C-28

✅ BELEGT · Angle: Markt, D Geschenk

**Royal Mail stellt für Black Friday, Cyber Monday und Weihnachten 2026 knapp 22.000 Saisonkräfte ein, die von Ende Oktober 2026 bis Anfang Januar 2027 arbeiten.**

> “The seasonal work covers Black Friday, Cyber Monday and Christmas ... Today, the business announced it is recruiting almost 22,000 temporary workers to help transport, sort and deliver the additional parcels and mail the company expects to process over the festive period. ... The seasonal roles will run from late October through to early January 2027.”

- **Quelle:** [International Distribution Services / Royal Mail – Royal Mail to hire 22,000 temporary workers to help deliver Christmas](https://www.internationaldistributionservices.com/en/press-centre/press-releases/royal-mail/royal-mail-to-hire-22-000-temporary-workers-to-help-deliver-christmas/)
- **Datum der Quelle:** 2026-09-24 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primäre Pressemitteilung des Royal-Mail-Mutterkonzerns. Sie nennt keine Last-Posting-Dates für 2026. Die neueste Royal-Mail-Mitteilung in der Liste (07.10.2026, 'Royal Mail Organisational Review') enthält ebenfalls keine.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum (24.09.2026) bestätigt; Pressemitteilungsliste bis 07.10.2026 geprüft.

### 2 Letzte Bestelltage Amazon UK

#### 4C-29

✅ BELEGT · Angle: D Geschenk

**Amazon UK nennt keine festen Weihnachts-Bestellfristen, sondern verweist darauf, dass das Lieferdatum an der Kasse maßgeblich ist und Cut-off-Termine nur Richtwerte sind.**

> “Always check the final delivery date at checkout, as delivery cut off dates are a guideline and can be impacted by external factors.”

- **Quelle:** [Amazon UK (About Amazon) – Amazon last date to order for Christmas delivery](https://aboutamazon.co.uk/news/retail/amazon-last-date-order-christmas-delivery)
- **Datum der Quelle:** 2025-12-05 (dateModified; erstmals veröffentlicht 2024-12-09) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Unternehmensquelle mit eindeutiger Aussage. Die Seite bezieht sich auf die Saison 2025 (Rückgabe bis 31.01.2026). Termine für 2026 sind nicht veröffentlicht.
- **Wahrheits-Check:** *bestätigt*. Wortlaut gefunden; Datum aus den Seitenmetadaten ergänzt (vorher 'unbekannt').

### 2 Letzte Bestelltage Händler (Referenz 2025)

#### 4C-30

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut MoneySavingExpert-Tabelle 2025 war die letzte Express-Bestellung bei Amazon für Lieferung bis Heiligabend am Di 23.12.2025 möglich (für Prime-Mitglieder kostenlos), bei John Lewis die Standardlieferung kleiner Artikel bis Fr 19.12.2025.**

> “Christmas last order dates for 2025 (so you get it by Christmas Eve) ... Amazon* TBC Last year it was 19 December for non-Prime members but it can vary by item. ... Tuesday 23 December Free for Prime members; usually £3.99-£5.99 for non-Prime members ... John Lewis* Friday 19 December for small items”

- **Quelle:** [MoneySavingExpert – Christmas last order dates 2025](https://www.moneysavingexpert.com/deals/deals-hunter/last-order-dates/)
- **Datum der Quelle:** 2025-12-18 · **Typ:** Presse
- **Einordnung/Einschränkung:** Redaktionelle Zusammenstellung, nur für 2025. Bei Amazon war die Standardlieferung 'TBC'. Weitere Werte 2025: Argos Standard Mo 22.12., M&S Standard Sa 20.12., Next 20 Uhr Mo 22.12. Dunelm ist nicht gelistet.
- **Wahrheits-Check:** *bestätigt*. Tabellenwerte für Amazon, John Lewis, Argos, M&S und Next bestätigt; dateModified 18.12.2025.

### 2 Verspätete Weihnachtspost (Umfrage)

#### 4C-31

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer Post-Office-Umfrage (n=2.000 UK-Erwachsene, Oktober 2025) haben 67 % der Briten schon Weihnachtskarten oder -geschenke erst nach dem 25. Dezember per Post erhalten, und 17 % haben schon einmal den letzten Einlieferungstag verpasst.**

> “New research reveals 67 per cent of Brits have received festive cards and presents in the post after Christmas Day. ... the 17 per cent of Brits who’ve previously left it too late and missed the final posting date.”

- **Quelle:** [Post Office (Mynewsdesk) – Post Office Announces Last Posting Dates for Sending Christmas Presents](https://www.mynewsdesk.com/uk/post-office/pressreleases/post-office-announces-last-posting-dates-for-sending-christmas-presents-3420939)
- **Datum der Quelle:** 2025-12-10 (Datumszeile im Text; Mynewsdesk-Zeitstempel 19.12.2025) · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Post Office 'Hot Topics', Oktober 2025, n=2.000 bevölkerungsrepräsentative UK-Erwachsene, Sample: Dynata
- **Einordnung/Einschränkung:** Die Methodik ist offengelegt, die Umfrage wurde aber vom Anbieter selbst in Auftrag gegeben (PR-Kontext). Als Begründung für 'rechtzeitig bestellen' in Geschenk-Ads (Angle D) nutzbar, wenn die Quelle genannt wird. 'Have received' heißt jemals, nicht pro Jahr.
- **Wahrheits-Check:** *bestätigt*. Zahlen und Methodikhinweis wörtlich bestätigt.

### 3 Boxing-Day-Sales

#### 4C-32

⚠️ EINGESCHRÄNKT · Angle: Markt

**Barclays erwartete für Boxing Day 2025 Ausgaben von 3,6 Mrd. £ in UK; nur 26 % der Befragten planten dafür Ausgaben (2024: 28 %), bei durchschnittlich 253 £ pro Käufer.**

> “New data from the Barclays Consumer Spend report reveals that UK consumers are expecting to spend £3.6 billion in the Boxing Day sales. The average shopper has increased their budget by £17 compared to 2024, yet fewer consumers will be taking part – 26 per cent plan to spend on Boxing Day this year, down from 28 per cent in 2024.”

- **Quelle:** [Barclays – UK shoppers set to spend £3.6 billion in the Boxing Day sales](https://home.barclays/news/press-releases/2025/12/uk-shoppers-set-to-spend-p3-6-billion-in-the-boxing-day-sales/)
- **Datum der Quelle:** 2025-12-26 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Opinium Research im Auftrag von Barclays, n=2.000 je Welle, 21.–25.11.2025, repräsentativ für UK nach Alter, Geschlecht, Region, Einkommen
- **Einordnung/Einschränkung:** Kaufabsichten und eine Hochrechnung (25,8 % Teilnahme × Durchschnittsbudget), keine gemessenen Umsätze. Die Prognose liegt deutlich unter der Prognose für 2024 (4,6 Mrd. £). Laut derselben Mitteilung bevorzugen 40 % online, und 97 % wollen zumindest einen Teil ihrer Schnäppchensuche im Laden machen.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Methodik und Datum bestätigt; '4,6 Mrd.' als Prognose 2024 präzisiert.

### 3 Boxing-Day-/Winter-Sales – Kategorien

#### 4C-33

⚠️ EINGESCHRÄNKT · Angle: Markt

**20 % der Sale-Käufer in der Barclays-Umfrage hatten Homeware auf ihrer Einkaufsliste für die Sales 2025, gleichauf mit Beauty und hinter Kleidung (37 %) sowie Essen und Trinken (27 %).**

> “Clothes, shoes and accessories are at the top of shoppers’ wish lists this year, chosen by 37 per cent, after the category saw subdued spending in 2025. Food and drink (27 per cent), beauty products (20 per cent), homeware (20 per cent) and discounted Christmas items (19 per cent) ranked next.”

- **Quelle:** [Barclays – UK shoppers set to spend £3.6 billion in the Boxing Day sales](https://home.barclays/news/press-releases/2025/12/uk-shoppers-set-to-spend-p3-6-billion-in-the-boxing-day-sales/)
- **Datum der Quelle:** 2025-12-26 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Opinium für Barclays, n=2.000, 21.–25.11.2025, UK
- **Einordnung/Einschränkung:** Umfrage unter Sale-Käufern, Kaufabsicht. Bettwaren sind nicht separat ausgewiesen; 'homeware' ist eine Sammelkategorie.
- **Wahrheits-Check:** *bestätigt*. Wortlaut um den ersten Satz ergänzt; Zahlen bestätigt.

### 3 Boxing Day online

#### 4C-34

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Adobe überstiegen die UK-Online-Ausgaben am Boxing Day 2025 500 Mio. £.**

> “Adobe also reported that Boxing Day passed £500 million.”

- **Quelle:** [CMOtech UK (TechDay) – Bericht über Adobe-Digital-Insights-Daten](https://cmotech.uk/story/mobile-ai-power-record-uk-online-christmas-sales)
- **Datum der Quelle:** 2026-01-20 · **Typ:** Presse
- **Einordnung/Einschränkung:** Sekundärquelle für Adobe, ohne genaue Zahl. Nur online, Adobe-Panel. 'Erstmals' steht nicht in der Quelle; die Adobe-Prognose mit 'for the first time' ist nicht prüfbar (Adobe-Seite 503).
- **Wahrheits-Check:** *korrigiert*. 'Erstmals' aus der Aussage entfernt, weil die abgerufene Quelle es nicht belegt; Wortlaut bestätigt.

### 3 Weihnachten / Boxing Day / Januar-Sales (BRC)

#### 4C-35

✅ BELEGT · Angle: Markt, D Geschenk

**Laut BRC stiegen die UK-Einzelhandelsumsätze im Dezember 2025 nur um 1,2 %, Geschenkartikel liefen schlechter als erwartet, und die letzte Dezemberwoche wuchs dank Boxing Day und Beginn der Januar-Sales deutlich.**

> “UK Total retail sales increased by 1.2% year on year in December, against a growth of 3.2% in December 2024. ... It was a drab Christmas for retailers, as sales growth slowed for the fourth consecutive month. While food sales rose on the back of ongoing food inflation, non-food sales fell flat in the run up to Christmas, with gifting items doing worse than expected. Many people were clearly holding out for discounts, with the last week showing significant growth off the back of Boxing Day and beginning of the January sales.”

- **Quelle:** [British Retail Consortium – Drab Christmas as consumers wait for sales](https://brc.org.uk/news-and-events/news/corporate-affairs/2026/ungated/drab-christmas-as-consumers-wait-for-sales/)
- **Datum der Quelle:** 2026-01-13 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG Retail Sales Monitor Dezember 2025, UK
- **Einordnung/Einschränkung:** Primärquelle. Non-Food −0,3 %, Online-Anteil bei Non-Food 38,6 %. 'Significant growth' in der letzten Woche ist nicht beziffert.
- **Wahrheits-Check:** *bestätigt*. Zahlen, Zitat und Datum bestätigt.

### 3 Januar-Sales (BRC)

#### 4C-36

✅ BELEGT · Angle: Markt

**Im Januar 2026 stiegen die UK-Einzelhandelsumsätze laut BRC-KPMG um 2,7 %; viele hatten auf die Januar-Sales gewartet, und Möbel gehörten zu den stärksten Kategorien.**

> “UK Total retail sales increased by 2.7% year on year in January ... Many shoppers had held off Christmas spending and waited for the January sales, with the start of the new year showing the strongest growth. ... January sales enticed consumers to spend, with personal electronics, furniture, and children’s clothes and toys, all among the best performing categories.”

- **Quelle:** [British Retail Consortium – January sales boost for shoppers and retailers](https://brc.org.uk/news-and-events/news/corporate-affairs/2026/ungated/january-sales-boost-for-shoppers-and-retailers/)
- **Datum der Quelle:** 2026-02-10 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG Retail Sales Monitor Januar 2026, UK
- **Einordnung/Einschränkung:** Primärquelle. Das erste Zitat stammt von Helen Dickinson (BRC), das zweite von Linda Ellett (KPMG). Non-Food +1,7 %, Online-Non-Food +1,3 %, Non-Food im Laden +2,0 %. Bettwaren sind nicht separat ausgewiesen.
- **Wahrheits-Check:** *bestätigt*. Zahlen und Zitate bestätigt; Sprecherzuordnung ergänzt.

### 3 Blue Monday 2027 – Datum und Herkunft

#### 4C-37

⚠️ EINGESCHRÄNKT · Angle: Allgemein

**'Blue Monday' wird meist auf den dritten Montag im Januar gelegt, 2027 also Montag, 18.01.2027; der Begriff stammt aus einer Pressemitteilung des Reiseanbieters Sky Travel von 2005.**

> “Blue Monday is a day in January (typically the third Monday of the month) which is said by UK travel agency Sky Travel to be the most depressing day of the year. ... The date is generally reported as falling on the third Monday in January, but also on the second or fourth Monday. The first such date declared was 24 January in 2005 as part of a Sky Travel press release.”

- **Quelle:** [Wikipedia – Blue Monday (date)](https://en.wikipedia.org/wiki/Blue_Monday_(date))
- **Datum der Quelle:** 2026-05-11 (zuletzt bearbeitet) · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Das Datum ist eine Konvention (manchmal auch zweiter oder vierter Montag); der dritte Montag 2027 ist der 18.01. (nachgerechnet). Die Samaritans legen ihren 'Brew Monday' ebenfalls auf 'the third Monday in January'. Wikipedia ist keine Primärquelle.
- **Wahrheits-Check:** *bestätigt*. Wortlaut gefunden; Montage im Januar 2027 (4., 11., 18., 25.) geprüft; Samaritans-Konvention ergänzt.

### 3 Mythos: Blue Monday ist wissenschaftlich der traurigste Tag

#### 4C-38

❌ NICHT BELEGT / MYTHOS · Angle: Allgemein, B Wechseljahre

**Dass der dritte Montag im Januar (2027: 18.01.) wissenschaftlich nachweisbar der deprimierendste Tag des Jahres sei, ist nicht belegt; die Samaritans sagen ausdrücklich, dass es keinen 'Blue Monday' gibt.**

> “At Samaritans we know there’s no such thing as ‘Blue Monday’ and that feeling low isn’t just something that happens on Mondays or a random day in January.”

- **Quelle:** [Samaritans – Brew Monday 2026](https://www.samaritans.org/support-us/campaign/brew-monday/)
- **Datum der Quelle:** unbekannt (Seite 'Brew Monday 2026') · **Typ:** Fachgesellschaft/Charity
- **Einordnung/Einschränkung:** Mythos-Check: Es handelt sich um eine PR-Erfindung (Sky Travel 2005, Cliff Arnall). Laut Wikipedia wurde die Pressemitteilung über die PR-Agentur Porter Novelli vorformuliert; 'Some have dismissed the idea as pseudoscience', und eine Stellungnahme im Guardian distanzierte die Leitung der Cardiff University davon. In Ads keine Wissenschaftsbehauptung damit verbinden.
- **Wahrheits-Check:** *bestätigt*. Samaritans-Wortlaut wörtlich gefunden; Wikipedia-Angaben zu Pseudoscience, Porter Novelli und Cardiff geprüft; Unbelegtheit bestätigt.

### 4 World Menopause Day

#### 4C-39

⚠️ EINGESCHRÄNKT · Angle: B Wechseljahre

**Der World Menopause Day ist jedes Jahr am 18. Oktober (2026: Sonntag) und wird laut Sekundärquelle seit 2009 von der International Menopause Society (IMS) organisiert; Springer Nature nennt Oktober zudem 'Menopause Awareness Month'.**

> “For Menopause Awareness Month (October), and World Menopause Day (18th October), we are highlighting selected Springer Nature article Collections ... [Police Federation West Midlands, 2025:] Tomorrow (Saturday 18 October) is World Menopause Day with this year’s theme being lifestyle medicine. The day has been organised each year since 2009 by the International Menopause Society (IMS)”

- **Quelle:** [Springer Nature Research Communities – Menopause Awareness Month 2026 (Sophie Gray); ergänzend Police Federation West Midlands – Guide published to mark World Menopause Day (2025)](https://communities.springernature.com/posts/menopause-awareness-month-2026)
- **Datum der Quelle:** 2026-10-05 · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Zwei voneinander unabhängige Sekundärquellen bestätigen das Datum 18.10. Springer Nature verlinkt auf die IMS-Seite 'World Menopause Day 2026'. Die IMS-Primärseiten (imsociety.org/education/world-menopause-day-2026/) liefern bei WebFetch und Download HTTP 403. Ein Thema 2026 ist nicht verifiziert. Zweite URL: https://polfed.org/westmids/news-and-events/2025/guide-published-to-mark-world-menopause-day/
- **Wahrheits-Check:** *korrigiert*. Der bisherige Wortlaut 'for World Menopause Day 2012' steht nicht auf der Wikipedia-IMS-Seite (Volltext und HTML ohne Treffer). Quelle durch Springer Nature (05.10.2026) und Police Federation ersetzt; das Datum 18.10. ist damit sekundär belegt.

### 4 Menopause Awareness Month (Oktober)

#### 4C-40

⚠️ EINGESCHRÄNKT · Angle: B Wechseljahre

**Laut Bed Advice UK (National Bed Federation) ist Oktober der 'World Menopause Awareness Month'; der Beitrag vom 01.10.2026 empfiehlt mit Tipps der Sleep Charity eine Schlafzimmertemperatur von etwa 16–18 °C, atmungsaktive Materialien und mehrere leichtere Schichten statt einer schweren Decke.**

> “October is World Menopause Awareness Month, and we’re sharing The Sleep Charity’s essential tips ... Keeping your bedroom cool (around 16-18°C) can make a big difference. ... Opt for breathable, moisture-wicking materials like bamboo or cotton for your bedding and nightwear. ... Layer Up Wisely – Instead of using a heavy duvet, try layering with lighter blankets.”

- **Quelle:** [Bed Advice UK (National Bed Federation) – Menopause and Sleep: How to Stay Cool and Comfortable at Night](https://bedadvice.co.uk/menopause-and-sleep-how-to-stay-cool-and-comfortable-at-night/)
- **Datum der Quelle:** 2026-10-01 (laut Seite 'First published in October 2025, republished in 2026') · **Typ:** Händler-/Hersteller-Ratgeber
- **Einordnung/Einschränkung:** Branchenverband der Bettenhersteller (Interessenvertretung) mit Tipps der Sleep Charity. Eine offizielle Ausrufung des Monats durch NHS, BMS oder IMS habe ich nicht gefunden; Springer Nature nennt den Monat ebenfalls (4C-39). Wichtig für Angle B: Die Quelle rät von einer schweren Decke ab und zu Schichten. Ein Tog-Wert wird nicht genannt. Eine 10,5-Tog-Decke darf daher nicht mit dieser Quelle als 'ideal bei Nachtschweiß' beworben werden.
- **Wahrheits-Check:** *bestätigt*. Alle Zitate wörtlich gefunden; datePublished 2026-10-01 und Hinweis 'republished' bestätigt; Schicht-Tipp in Aussage und Wortlaut aufgenommen.

### 4 Uhrumstellung 2026

#### 4C-41

✅ BELEGT · Angle: Allgemein

**In UK werden die Uhren am Sonntag, 25.10.2026, um 2 Uhr nachts eine Stunde zurückgestellt (nächste Umstellung vorwärts: 28.03.2027).**

> “Clocks go back | 2026 | 25 October | 2027 | 28 March ... In the UK the clocks go forward 1 hour at 1am on the last Sunday in March, and back 1 hour at 2am on the last Sunday in October.”

- **Quelle:** [GOV.UK – When do the clocks change?](https://www.gov.uk/when-do-the-clocks-change)
- **Datum der Quelle:** 2025-08-11 (dateModified laut Seitenmetadaten) · **Typ:** Parlament/Regierung
- **Einordnung/Einschränkung:** Offizielle Regierungsseite; Tabelle und Regel bestätigt.
- **Wahrheits-Check:** *bestätigt*. Tabelle 2026/2027 und Regeltext gefunden; Seitendatum ergänzt.

### 4 National Sleep-In Day

#### 4C-42

⚠️ EINGESCHRÄNKT · Angle: Allgemein

**Bed Advice UK (National Bed Federation) bewirbt den Tag der Zeitumstellung, Sonntag, 25.10.2026, als 'National Sleep-In Day' mit einer Stunde mehr Schlaf.**

> “As National Sleep-In Day approaches, the day the clocks go back, and we get an extra hour in bed on Sunday 25th October.”

- **Quelle:** [Bed Advice UK (National Bed Federation) – Sleep & the Clock Change in 2026](https://bedadvice.co.uk/sleep-the-clock-change-from-the-sleep-charity/)
- **Datum der Quelle:** 2026-10-08 · **Typ:** Händler-/Hersteller-Ratgeber
- **Einordnung/Einschränkung:** Aktionstag der Branche ohne offiziellen Status; das Datum selbst ist über gov.uk belegt (4C-41). Möglicher Content-Anlass ('eine Stunde mehr im Bett').
- **Wahrheits-Check:** *bestätigt*. Wortlaut und datePublished 2026-10-08 bestätigt.

### 4 Carers Rights Day 2026

#### 4C-43

✅ BELEGT · Angle: D Geschenk

**Der Carers Rights Day von Carers UK findet 2026 am Donnerstag, 19. November, statt; Carers UK spricht von 5,8 Millionen unbezahlt pflegenden Angehörigen in UK.**

> “This year Carers Rights Day is taking place on Thursday 19 November, and we're coming together to help people recognise sooner that they're a carer. ... Get involved in Carers Rights Day 2026”

- **Quelle:** [Carers UK – Carers Rights Day](https://www.carersuk.org/carers-rights-day/)
- **Datum der Quelle:** unbekannt (Seite bezieht sich ausdrücklich auf 2026) · **Typ:** Fachgesellschaft/Charity
- **Einordnung/Einschränkung:** Primärquelle des Veranstalters. Die Seite nennt ausdrücklich 'Carers Rights Day 2026', und der 19.11.2026 ist ein Donnerstag. Die 5,8 Mio. stehen auf derselben Seite ('the UK’s 5.8 million unpaid carers'); ihre Herkunft habe ich nicht geprüft.
- **Wahrheits-Check:** *korrigiert*. Die Begründung 'die Seite nennt kein Jahr' ist falsch, sie nennt 'Carers Rights Day 2026'; korrigiert und Wortlaut ergänzt.

### 4 Ofgem-Preisdeckel

#### 4C-44

✅ BELEGT · Angle: Allgemein

**Der Ofgem-Energiepreisdeckel für einen typischen Haushalt mit Strom und Gas (Lastschrift) liegt vom 01.10. bis 31.12.2026 bei 1.723 £ pro Jahr (+4 %); er wird alle drei Monate angepasst, die nächste Periode beginnt am 01.01.2027.**

> “Energy regulator Ofgem has today (Wednesday 26 August) announced a 4% increase of the energy price cap for the period covering 1 October to 31 December 2026. ... It is updated every three months to reflect changes in the underlying costs of supplying energy. ... from October, the price cap will rise by £60 per year (or £5 per month) to £1,723 for the average household using both electricity and gas if this level was sustained for a year.”

- **Quelle:** [Ofgem – Energy price cap will rise by 4% from October 2026](https://www.ofgem.gov.uk/press-release/energy-price-cap-will-rise-4-october-2026)
- **Datum der Quelle:** 2026-08-26 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle des Regulierers. Ofgem ist für Großbritannien zuständig; eine Regionsangabe steht nicht auf der Seite. Der Beginn der nächsten Periode am 01.01.2027 folgt aus dem Quartalsrhythmus ('We set the price cap level every 3 months'); Höhe und Bekanntgabetermin waren am 08.10.2026 nicht veröffentlicht. Laut Mitteilung entfällt die Mehrwertsteuer auf Haushaltsstrom, und die Gasrechnungen steigen um 8 %. Für 'Heizung runter, warme Decke'-Argumente gilt: keine Einsparbeträge pro Decke behaupten.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, 1.723 £, +4 %, Zeitraum, Gas +8 % und Quartalsrhythmus (auch auf der Ofgem-Erklärseite) bestätigt.

### 4 Mothering Sunday 2027

#### 4C-45

✅ BELEGT · Angle: D Geschenk

**Mothering Sunday (britischer Muttertag) fällt 2027 auf Sonntag, den 7. März 2027.**

> “Mothering Sunday always falls on the fourth Sunday in Lent (Laetare Sunday), 3 weeks before Easter Sunday. ... 7 March 2027”

- **Quelle:** [Wikipedia – Mothering Sunday](https://en.wikipedia.org/wiki/Mothering_Sunday)
- **Datum der Quelle:** 2026-09-06 (zuletzt bearbeitet) · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Mit amtlicher Quelle gegengeprüft: Laut gov.uk-JSON ist Karfreitag der 26.03.2027, Ostersonntag also der 28.03.2027; drei Wochen davor ist der 07.03.2027 (nachgerechnet, Sonntag). Wichtig für Angle D; die Versandfristen davor müssen eigens geplant werden.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Tabelle (7 March 2027) gefunden; Good Friday 2027-03-26 im gov.uk-JSON bestätigt.

### 4 World Sleep Day 2027

#### 4C-46

⚠️ EINGESCHRÄNKT · Angle: Allgemein, B Wechseljahre

**Der World Sleep Day findet am Freitag vor der März-Tagundnachtgleiche statt; 2027 wäre das voraussichtlich Freitag, der 19. März 2027 (offiziell noch nicht angekündigt).**

> “World Sleep Day is observed annually on the Friday before the March Equinox.”

- **Quelle:** [Wikipedia – World Sleep Day](https://en.wikipedia.org/wiki/World_Sleep_Day)
- **Datum der Quelle:** 2026-03-12 (zuletzt bearbeitet) · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Abgeleitet, nicht offiziell. Laut Wikipedia-Tabelle 'March equinox' ist die Tagundnachtgleiche 2027 am 20.03. um 20:25 UTC (Samstag), der Freitag davor also der 19.03.2027. 2021 lag die Tagundnachtgleiche ebenfalls auf einem Samstag (20.03.), und der World Sleep Day war am 19.03.2021. worldsleepday.org nennt bisher nur 2026 ('World Sleep Day 2026 took place on Friday, March 13, 2026').
- **Wahrheits-Check:** *bestätigt*. Regel, Tagundnachtgleiche 2027 und offizielle Seite geprüft; Analogie 2021 ergänzt.

### 4 Grandparents' Day UK

#### 4C-47

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Der Grandparents' Day wird in UK seit 2008 am ersten Sonntag im Oktober begangen (2026: 4.10., also schon vorbei; 2027: 3.10.), ist laut Quelle aber wenig verbreitet.**

> “The day was introduced to the UK in 1990 by the charity Age Concern but it has not been widely accepted by the British public. It has been celebrated on the first Sunday in October since 2008.”

- **Quelle:** [Wikipedia – Grandparents' Day (Abschnitt United Kingdom)](https://en.wikipedia.org/wiki/Grandparents%27_Day)
- **Datum der Quelle:** 2026-07-14 (zuletzt bearbeitet) · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Keine Primärquelle (Age UK nicht geprüft). Laut Quelle 'not widely accepted', als Anlass für Geschenk-Ads in UK also schwach. Weihnachten und Mothering Sunday sind die relevanteren Anlässe.
- **Wahrheits-Check:** *bestätigt*. Wortlaut gefunden; Wochentage 04.10.2026 und 03.10.2027 geprüft.

### 4 Singles' Day 11.11.

#### 4C-48

⚠️ EINGESCHRÄNKT · Angle: Markt

**Singles' Day (11.11., 2026 ein Mittwoch) ist ein inoffizieller chinesischer Aktionstag; eine nennenswerte Bedeutung für den UK-Handel ist damit nicht belegt.**

> “Singles' Day ... or Double 11 ... is an unofficial Chinese holiday for people who are not in a relationship. The date, 11 November (11/11), was chosen because the numeral 1 resembles a bare stick”

- **Quelle:** [Wikipedia – Singles' Day](https://en.wikipedia.org/wiki/Singles%27_Day)
- **Datum der Quelle:** 2026-09-18 (zuletzt bearbeitet) · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Ursprung und Datum sind belegt. UK-Umsatzzahlen zum Singles' Day habe ich nicht gefunden; die geprüften IMRG-, BRC- und ONS-Berichte erwähnen ihn nicht. Laut derselben Wikipedia-Seite gibt es in UK einen 'National Singles Day' am 11. März, der nichts mit dem Handelstag zu tun hat.
- **Wahrheits-Check:** *bestätigt*. Wortlaut gefunden; 11.11.2026 = Mittwoch geprüft.

### 5 DMCC Act – Bußgelder

#### 4C-50

✅ BELEGT · Angle: Allgemein

**Die CMA kann seit dem DMCC Act bei Verstößen gegen Verbraucherrecht Bußgelder von bis zu 10 % des weltweiten Umsatzes eines Unternehmens oder 300.000 £ verhängen, je nachdem, welcher Betrag höher ist.**

> “The penalty can be up to 10% of your business’ global turnover or £300,000 (whichever is greater).”

- **Quelle:** [CMA / GOV.UK – How the CMA uses its direct consumer enforcement powers](https://www.gov.uk/government/publications/how-the-cma-uses-its-direct-consumer-enforcement-powers/how-the-cma-uses-its-direct-consumer-enforcement-powers)
- **Datum der Quelle:** 2025-08-28 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle des Regulierers, gestützt auf DMCC Act s.182(6) und s.204 (4C-51).
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum 28.08.2025 bestätigt.

### 5 DMCC Act – Gesetzestext

#### 4C-51

✅ BELEGT · Angle: Allgemein

**Nach Section 182(6) DMCC Act 2024 darf ein CMA-Bußgeld in einer abschließenden Verletzungsmitteilung höchstens 300.000 £ oder, falls höher, 10 % des Umsatzes betragen; Section 204 zählt dazu ausdrücklich auch Umsatz außerhalb UK.**

> “(6) The amount of a monetary penalty imposed under subsection (4)(b) must be a fixed amount not exceeding £300,000 or, if higher, 10% of the total value of the turnover (if any) of the respondent.”

- **Quelle:** [legislation.gov.uk – Digital Markets, Competition and Consumers Act 2024, section 182 (Final infringement notice)](https://www.legislation.gov.uk/ukpga/2024/13/section/182)
- **Datum der Quelle:** 2024 · **Typ:** Parlament/Regierung
- **Einordnung/Einschränkung:** Gesetzestext. Section 204(1)(a): 'turnover both in and outside the United Kingdom' (https://www.legislation.gov.uk/ukpga/2024/13/section/204), daher 'weltweiter Umsatz'.
- **Wahrheits-Check:** *bestätigt*. s.182(6) und s.204(1)(a) wörtlich bestätigt; Kontext 'Final infringement notice' ergänzt.

### 5 DMCC Act – Inkrafttreten

#### 4C-52

✅ BELEGT · Angle: Allgemein

**Die CMA-Durchsetzungsregeln zum Verbraucherschutz nach dem DMCC Act (SI 2025/267) sind am 6. April 2025 in Kraft getreten.**

> “The statutory instrument (SI) 2025/267 approving the CMA Consumer Enforcement Rules came into force on 6 April 2025.”

- **Quelle:** [CMA / GOV.UK – Direct consumer enforcement guidance and rules (CMA200/CMA201)](https://www.gov.uk/government/publications/direct-consumer-enforcement-guidance-cma200)
- **Datum der Quelle:** 2025-03-14 (aktualisiert 2025-04-04) · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle. Die UCP-Leitlinie CMA207 wurde zuletzt am 18.11.2025 aktualisiert.
- **Wahrheits-Check:** *bestätigt*. Wortlaut sowie Veröffentlichungs- und Aktualisierungsdatum bestätigt; CMA207 'Updated 18 November 2025' bestätigt.

### 5 Verbotene Praktiken – Countdown / falsche Befristung

#### 4C-53

✅ BELEGT · Angle: Allgemein

**Es ist in UK in jedem Fall verboten (Banned practice 7), fälschlich zu behaupten, ein Produkt oder Preis gelte nur für begrenzte Zeit; ein Countdown, der nach Ablauf neu startet, ist das Beispiel der CMA.**

> “Banned practice 7 Falsely stating that a product will only be available for a limited time, or that it will only be available on particular terms for a limited time, in order to elicit an immediate decision and deprive consumers of sufficient opportunity or time to make an informed choice. Example A trader falsely tells a consumer that an offer will end when a countdown clock runs out ... When the time runs down, the offer does not in fact end, but continues and the countdown clock restarts.”

- **Quelle:** [CMA – Unfair commercial practices (CMA207), Kapitel 3 Banned practices](https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices)
- **Datum der Quelle:** 2025-11-18 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Offizielle CMA-Leitlinie; die 32 Praktiken in Schedule 20 sind 'in all circumstances considered unfair'. Laut CMA ist ein wahrer Countdown unproblematisch, solange nicht kurz danach ein im Wesentlichen gleiches Angebot erscheint ('unlikely to be problematic'). Für Black-Friday- und Weihnachts-Ads gilt: Enddaten nur nennen, wenn sie wirklich gelten.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und 'in all circumstances' bestätigt.

### 5 CMA-Durchsetzung – Homeware/Time-limited Sales

#### 4C-54

✅ BELEGT · Angle: Allgemein, Markt

**Die CMA eröffnete am 18.11.2025 ihre ersten 8 Verfahren mit den neuen Befugnissen, darunter gegen den Homeware-Händler Wayfair wegen zeitlich begrenzter Sales, nachdem sie über 400 Unternehmen in 19 Branchen geprüft hatte.**

> “Homeware retailers Wayfair, Appliances Direct, and Marks Electrical – are being investigated to determine whether their time-limited sales ended when they said they would, or whether customers are being automatically opted in to purchasing additional services. ... Cases are the first launched by the CMA using its new consumer protection powers”

- **Quelle:** [CMA / GOV.UK – CMA launches major consumer protection drive focused on online pricing practices](https://www.gov.uk/government/news/cma-launches-major-consumer-protection-drive-focused-on-online-pricing-practices)
- **Datum der Quelle:** 2025-11-18 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle. Die CMA hat damit noch keinen Verstoß festgestellt ('At this stage, the CMA has reached no conclusions'). Laut Mitteilung gibt es Compliance-Bedenken in 14 Branchen, 'including drip pricing and the use of misleading countdown timers', und Hinweisschreiben an 100 Unternehmen. Laut Fallseite läuft das Wayfair-Verfahren noch (4C-V10).
- **Wahrheits-Check:** *bestätigt*. Wortlaut, '400 businesses in 19 different sectors' und 'first' bestätigt.

### 5 CMA-Durchsetzung – Bilanz bis August 2026

#### 4C-55

✅ BELEGT · Angle: Allgemein

**Seit Inkrafttreten der neuen Befugnisse hat die CMA bis August 2026 Bußgelder von fast 6,2 Mio. £ verhängt und über 1,95 Mio. £ Erstattungen für Verbraucher erwirkt.**

> “Since its strengthened consumer powers came into force – which allow it to fine companies for breaches and secure refunds – the CMA has launched investigations across ticketing, gyms, homeware, online reviews and air travel, securing more than £1.95 million in refunds for UK consumers and levying fines close to £6.2 million.”

- **Quelle:** [CMA / GOV.UK – Trainline, Virgin Atlantic and RED Driving School investigated for drip pricing](https://www.gov.uk/government/news/trainline-virgin-atlantic-and-red-driving-school-investigated-for-drip-pricing)
- **Datum der Quelle:** 2026-08-19 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle. Bestraft wurden laut Mitteilung die Fahrschulen AA und BSM sowie StubHub UK wegen Drip Pricing; laut CMA-Mitteilung vom 28.05.2026 erhielt die AA 4,2 Mio. £ Bußgeld. Zum Ausgang des Wayfair-Verfahrens enthält die Seite nichts.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Datum 19.08.2026 bestätigt.

### 5 Referenzpreise ('was/now') – CTSI-Leitlinie

#### 4C-56

✅ BELEGT · Angle: Allgemein

**Laut CTSI-Leitlinie (Stand April 2026, an den DMCC Act angepasst) sollte ein 'War-Preis'-Vergleich höchstens so lange laufen wie zuvor der höhere Preis galt, und zum höheren Preis sollte nennenswert verkauft worden sein.**

> “The price comparison is made for a period that is the same or shorter than the period during which the higher price was offered ... The retailer can provide evidence to show significant sales at the higher price or that this was a realistic selling price for the product”

- **Quelle:** [Chartered Trading Standards Institute (Business Companion) – Guidance for Traders on Pricing Practices, Abschnitt 17 'Using reference prices'](https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices)
- **Datum der Quelle:** 2026-04 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Offizielle Best-Practice-Leitlinie ('reviewed and updated by CTSI in April 2026'; Seite 'Government-backed'). Sie ersetzt den Pricing Practices Guide der Regierung von 2010 und bezieht sich ausdrücklich auf den DMCC Act. Sie ist kein Gesetz, sondern eine Auslegungshilfe. Weitere Kriterien: Aktualität des Vergleichspreises, gleiche Verkaufsstellen, keine Vergleiche mit Preisen außerhalb der Saison. Nach dem Emma-Sleep-Urteil (4C-V09) ist die gerichtliche Auslegung von 'War/Jetzt'-Preisen in Bewegung.
- **Wahrheits-Check:** *bestätigt*. Kriterien und Stand April 2026 wörtlich bestätigt.

### 5 Mythos: feste 28-Tage-Regel für 'War-Preise'

#### 4C-57

❌ NICHT BELEGT / MYTHOS · Angle: Allgemein

**Eine feste gesetzliche '28-Tage-Regel' (War-Preis muss mindestens 28 Tage gegolten haben) ist in der aktuellen UK-Leitlinie nicht enthalten; maßgeblich sind Einzelfallkriterien wie Dauer, Aktualität und Absatz zum höheren Preis.**

> “Guidance for Traders on Pricing Practices was originally produced by the Chartered Trading Standards Institute (CTSI) in 2018 ... It replaced the Government's 2010 Pricing Practices Guide.”

- **Quelle:** [Chartered Trading Standards Institute (Business Companion) – Guidance for Traders on Pricing Practices, Einleitung](https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices)
- **Datum der Quelle:** 2026-04 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Mythos-Check: Die vollständige aktuelle CTSI-Leitlinie enthält keine 28-Tage-Frist (Volltextsuche nach '28' ohne passenden Treffer). Stattdessen gilt ein Kriterienkatalog (4C-56). Ob der alte Leitfaden von 2010 eine 28-Tage-Faustregel enthielt, habe ich nicht geprüft. Eine 28-Tage-Frist ist weder Pflicht noch 'sicherer Hafen'; ein über 28 Tage verlangter Preis kann trotzdem irreführend sein, wenn kaum zu ihm verkauft wurde (4C-58).
- **Wahrheits-Check:** *bestätigt*. Volltextsuche im heruntergeladenen Seitentext erneut durchgeführt; Unbelegtheit bestätigt.

### 5 Referenzpreise – CMA-Leitlinie

#### 4C-58

✅ BELEGT · Angle: Allgemein

**Laut CMA muss der höhere Vergleichspreis in einer Rabattaussage ein echter und realistischer Verkaufspreis sein, den das Unternehmen belegen kann; wer zum höheren Preis kaum verkauft hat (Beispiel: 5 Stück zu 150 £, 200 Stück zu 100 £), handelt wahrscheinlich irreführend.**

> “Trader A’s claims are likely to be misleading because the reference price is not a genuine and realistic selling price. The item did not sell in significant numbers at the higher price ... The higher price in a price reduction claim must be a genuine and realistic selling price – and a business should be able to demonstrate this.”

- **Quelle:** [CMA – Urgency and price reduction claims: compliance advice for online businesses (open letter), Beispiel 10 und Fußnote 8](https://assets.publishing.service.gov.uk/media/64232b153d885d000cdadd30/OCA_business_open_letter_FINAL.pdf)
- **Datum der Quelle:** 2023-03-29 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Offizielle CMA-Leitlinie, damals noch auf Basis der CPRs 2008. Sie ist auf gov.uk weiter veröffentlicht ('Using urgency and price reduction claims online', 29.03.2023), und die CTSI-Leitlinie verweist 2026 auf sie. Sie enthält auch Beispiele zu ständig wechselnden Preisen ('flip-flopping').
- **Wahrheits-Check:** *bestätigt*. PDF abgerufen; Beispiel 10 (150 £/5 Stück, 100 £/200 Stück) und Fußnote 8 wörtlich bestätigt; Datum 29.03.2023.

### 5 ASA/CAP-Regeln – Preisvergleiche/UVP

#### 4C-59

✅ BELEGT · Angle: Allgemein

**Nach CAP-Code-Regel 3.39 dürfen Preisvergleiche keinen falschen Preisvorteil vorspiegeln; Vergleiche mit einer UVP (RRP) sind wahrscheinlich irreführend, wenn diese deutlich vom üblichen Verkaufspreis abweicht.**

> “3.39 Price comparisons must not mislead by falsely claiming a price advantage. Comparisons with recommended retail prices (RRPs) are likely to mislead if the RRP differs significantly from the price at which the product or service is generally sold.”

- **Quelle:** [ASA/CAP – UK Code of Non-broadcast Advertising (CAP Code), Section 03 Misleading advertising](https://www.asa.org.uk/type/non_broadcast/code_section/03.html)
- **Datum der Quelle:** unbekannt · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Gilt direkt für Social-/Meta-Ads in UK. Der CAP Code verweist für Preisangaben auf die CTSI-Leitlinie ('Price statements in marketing communications should take into account the Chartered Trading Standards Institute’s Guidance for traders on pricing practices'). Regel 3.38: Die Vergleichsbasis muss klar sein.
- **Wahrheits-Check:** *bestätigt*. Regeln 3.38 und 3.39 sowie der CTSI-Verweis wörtlich bestätigt.

### 5 ASA/CAP-Regeln – falscher Zeitdruck

#### 4C-60

✅ BELEGT · Angle: Allgemein

**Nach CAP-Code-Regel 3.30 dürfen Werbeanzeigen in UK nicht fälschlich behaupten, ein Produkt oder Angebot sei nur für begrenzte Zeit verfügbar.**

> “3.30 Marketing communications must not falsely claim that the marketer is about to cease trading or move premises. They must not falsely state that a product, or the terms on which it is offered, will be available only for a limited time to deprive consumers of the time or opportunity to make an informed choice.”

- **Quelle:** [ASA/CAP – UK Code of Non-broadcast Advertising (CAP Code), Section 03](https://www.asa.org.uk/type/non_broadcast/code_section/03.html)
- **Datum der Quelle:** unbekannt · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Werbe-Selbstregulierung, inhaltlich deckungsgleich mit Banned practice 7 im DMCC Act (4C-53). Für Ads mit 'Nur bis Sonntag' oder 'Letzte Chance vor Weihnachten' gilt: Die Aussage muss tatsächlich zutreffen.
- **Wahrheits-Check:** *bestätigt*. Regel 3.30 wörtlich bestätigt.

### 5 Gesamtpreis inkl. Pflicht-Versandkosten (Drip Pricing)

#### 4C-61

✅ BELEGT · Angle: Allgemein

**Laut CTSI-Leitlinie müssen alle nicht optionalen Fracht-, Liefer- und Portokosten inklusive Steuern im beworbenen Gesamtpreis enthalten sein; die CMA geht seit 2025 gezielt gegen 'Drip Pricing' vor.**

> “DO include all non-optional / compulsory freight, delivery and postal charges (together with any taxes) in the total price of the product. If these cannot be calculated in advance, indicate how the charges will be calculated - for example, freight charges dependent on location.”

- **Quelle:** [Chartered Trading Standards Institute (Business Companion) – Guidance for Traders on Pricing Practices, Abschnitt 8 General requirements](https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices)
- **Datum der Quelle:** 2026-04 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Best-Practice-Leitlinie. Die CMA-Leitlinie CMA209 'Price transparency' (veröffentlicht 18.11.2025, aktualisiert 07.01.2026) behandelt 'drip pricing (when prices are added as consumers proceed with a transaction)'. Wer in Ads einen Preis nennt, muss Pflicht-Versandkosten einrechnen oder klar ausweisen; optionale Express-Lieferung fällt nicht darunter.
- **Wahrheits-Check:** *bestätigt*. CTSI-Wortlaut und CMA209-Daten (18.11.2025 / 07.01.2026) auf gov.uk bestätigt.

### 1 Black Friday / Cyber Week – Umsatz 2025 (Salesforce)

#### 4C-V01

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Salesforce Shopping Index lösten UK-Käufer in der Cyber Week 2025 (25.11.–01.12.2025) über 6 Mrd. £ Umsatz aus, 3 % mehr als im Vorjahr; die Zahl der Bestellungen sank in UK aber leicht um 1 %.**

> “It was another record-breaking week, with UK shoppers driving over £6 billion ($8.4 billion) in sales – a 3% increase from last year ... Cyber Week order volumes still grew by 2% globally compared with last year, albeit with a slight drop of 1% in the UK.”

- **Quelle:** [Salesforce UK Newsroom – Salesforce Data: AI And Agents Propel UK Cyber Week to Record Over £6B in Spend](https://www.salesforce.com/uk/news/press-releases/2025/12/11/cyber-week-ai-agents-sales-uk/)
- **Datum der Quelle:** 2025-12-11 · **Typ:** Unternehmensbericht
- **Stichprobe/Methodik:** Salesforce Shopping Index: aggregierte Daten aus Salesforce-Commerce-Produkten, über 1,5 Mrd. Käufer weltweit, 1,5 Bio. Seitenaufrufe; Zeitraum 25.11.–01.12.2025
- **Einordnung/Einschränkung:** Anbieterdaten aus der eigenen Kundenplattform, auf den Markt hochgerechnet; die genaue Methodik ist nicht offengelegt. 'Record-breaking' ist eine Selbstbeschreibung. Die Zahl steht im Widerspruch zu IMRG (−1,2 %) und schließt die von Track 4C gemeldete Salesforce-Lücke.
- **Wahrheits-Check:** *bestätigt*. Pressemitteilung selbst abgerufen; Zahlen, Zeitraum und Methodikhinweis wörtlich bestätigt.

### 1 Black Friday – Kategorien (Homeware, Angle D)

#### 4C-V02

✅ BELEGT · Angle: Markt, D Geschenk

**Laut BRC verkauften sich im Black-Friday-Monat November 2025 (02.–29.11.) Homeware und Polstermöbel gut, weil viele Kunden Aktionen nutzten und sich auf Gäste über die Feiertage vorbereiteten; Mode lief schwächer.**

> “Many consumers took advantage of promotions, with homeware and upholstery selling well ahead of festive hosting. Fashion lagged, especially with the mild first half of November dampening demand for winterwear.”

- **Quelle:** [British Retail Consortium – Pre-Budget jitters dampen Black Friday sales (Zitat Helen Dickinson)](https://brc.org.uk/news-and-events/news/corporate-affairs/2025/ungated/pre-budget-jitters-dampen-black-friday-sales/)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG Retail Sales Monitor, 02.–29.11.2025, UK
- **Einordnung/Einschränkung:** Primärquelle; die Kategorieaussage ist qualitativ und nicht beziffert. Sie stützt den Kaufanlass 'Gäste über Weihnachten' (Angle D) im Black-Friday-Zeitraum.
- **Wahrheits-Check:** *bestätigt*. Beim Prüfen von 4C-12 auf derselben Seite gefunden; wörtlich bestätigt.

### 1 Black-Friday-Effekt 2025 (ONS)

#### 4C-V03

✅ BELEGT · Angle: Markt

**Laut ONS stiegen die nicht saisonbereinigten Einzelhandelsmengen in Großbritannien im November 2025 (mit Black Friday) um 11,9 % gegenüber dem Vormonat; saisonbereinigt sanken sie um 0,1 %, was auf einen etwas schwächeren Black-Friday-Effekt als üblich hindeutet.**

> “However, looking at our non-seasonally adjusted data (which do not adjust for Black Friday) sales volumes rose by 11.9% over the month to November 2025, compared with a rise of 4.4% in October 2025. ... Seasonally adjusted volumes fell by just 0.1% over the month, suggesting the Black Friday effect was slightly weaker than usual.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: November 2025, Abschnitt 4 Black Friday](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/november2025)
- **Datum der Quelle:** 2025-12-19 · **Typ:** Behörde/NHS/Statistikamt
- **Einordnung/Einschränkung:** Amtliche Statistik, nur Großbritannien, Mengen (nicht Werte). Stützt, dass Black Friday 2025 kein außergewöhnlich starkes Jahr war (vgl. 4C-22).
- **Wahrheits-Check:** *bestätigt*. Beim Prüfen von 4C-15 auf derselben Seite gefunden; wörtlich bestätigt.

### 1 Black-Friday-Absichten 2025 (ONS-Umfrage)

#### 4C-V04

✅ BELEGT · Angle: Markt

**Laut ONS-Umfrage planten im November 2025 rund 31 % der Erwachsenen in Großbritannien, im Black-Friday-Sale einzukaufen; 19 % wollten weniger einkaufen als im Vorjahr, 10 % mehr.**

> “Our Public opinion and social trends, Great Britain: November 2025 release reported that around 3 in 10 adults (31%) planned to shop in the Black Friday sales; 19% reported that they intended to shop less than last year, while 10% intended to shop more.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: November 2025 (Verweis auf Public opinion and social trends, November 2025)](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/november2025)
- **Datum der Quelle:** 2025-12-19 · **Typ:** Behörde/NHS/Statistikamt
- **Einordnung/Einschränkung:** Amtliche Umfrage (Opinions and Lifestyle Survey), nur Großbritannien, Kaufabsicht. Unabhängige Gegenprobe zur Barclays-Zahl von 43 % (4C-09). Die Originalveröffentlichung 'Public opinion and social trends' habe ich nicht separat geöffnet.
- **Wahrheits-Check:** *bestätigt*. Im ONS-November-Bulletin wörtlich gefunden.

### 1 Online-Anteil (neuester Wert)

#### 4C-V05

✅ BELEGT · Angle: Markt

**Laut ONS lag der Online-Anteil an allen Einzelhandelsumsätzen in Großbritannien im August 2026 bei 28,8 % (Juli 2026: 28,4 %); die nächste Veröffentlichung ist für den 23.10.2026 angekündigt.**

> “The total spend (the sum of in-store and online sales) rose by 1.3% over the month. As a result, the proportion of sales made online rose from 28.4% in July 2026 to 28.8% in August 2026.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: August 2026](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/august2026)
- **Datum der Quelle:** 2026-09-18 · **Typ:** Behörde/NHS/Statistikamt
- **Einordnung/Einschränkung:** Amtliche Statistik, neuester verfügbarer Wert. Nur Großbritannien, alle Einzelhandelsumsätze inklusive Lebensmittel.
- **Wahrheits-Check:** *bestätigt*. Neuestes Bulletin abgerufen; Release date 18.09.2026 und Next release 23.10.2026 bestätigt.

### 2 Royal Mail – Veröffentlichungszeitpunkt der Versandtermine

#### 4C-V06

✅ BELEGT · Angle: D Geschenk

**Royal Mail veröffentlichte die Last-Posting-Dates für Weihnachten 2025 am 24.11.2025; bis zur Mitteilung vom 07.10.2026 enthält die Royal-Mail-Pressemitteilungsliste keine Termine für 2026.**

> “ROYAL MAIL ANNOUNCES MAGICAL CARD PRIZE DRAW AND LAST POSTING DATES FOR CHRISTMAS #Royal Mail 24 November 25”

- **Quelle:** [International Distribution Services – Press releases, Royal Mail (Liste)](https://www.internationaldistributionservices.com/en/press-centre/press-releases/royal-mail/)
- **Datum der Quelle:** 2026-10-07 (neuester Eintrag) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primäre Pressemitteilungsliste. Für die Planung: Die Termine für 2026 werden voraussichtlich erst im November erscheinen. Das ist nur aus dem Vorjahr abgeleitet und nicht zugesagt.
- **Wahrheits-Check:** *bestätigt*. Liste selbst abgerufen; Einträge 07.10.2026 bis 24.11.2025 durchgesehen.

### 4 National Bed Month (März)

#### 4C-V07

✅ BELEGT · Angle: Markt, Allgemein

**Der National Bed Month ist eine jährliche Verbraucherkampagne der National Bed Federation im März; 2026 fand er statt (Marketing-Toolkit vom 22.01.2026), eine Ankündigung für März 2027 gibt es noch nicht.**

> “As National Bed Month approaches in March, the National Bed Federation (NBF) is calling on bed retailers and manufacturers to support the annual awareness campaign by downloading its newly updated marketing toolkit. The consumer campaign promotes the health benefits of a new bed, particularly one made by an NBF-approved member, tips on bed buying and bed care, and sleep advice from official supporter, The Sleep Charity.”

- **Quelle:** [National Bed Federation – NBF Releases Marketing Toolkit Ahead of 2026 National Bed Month in March](https://www.bedfed.org.uk/nbf-releases-marketing-toolkit-ahead-of-2026-national-bed-month-in-march/)
- **Datum der Quelle:** 2026-01-22 · **Typ:** Händler-/Hersteller-Ratgeber
- **Einordnung/Einschränkung:** Primärquelle des Veranstalters (Branchenverband, Interessenvertretung). Der Monat ist ein Branchen-Aktionsmonat, kein offizieller Gedenktag. Laut NBF-Marketingleiter Simon Williams findet er 'during what is often a quieter trading period' statt. Dass er 2027 wieder stattfindet, ist wahrscheinlich ('annual'), aber noch nicht angekündigt.
- **Wahrheits-Check:** *bestätigt*. Beim Gegenprüfen von 4C-49 gefunden; NBF-Seite selbst abgerufen, datePublished 2026-01-22.

### 5 CMA-Durchsetzung – Bettwarenbranche (Emma Sleep, Countdown/Rabatte)

#### 4C-V08

✅ BELEGT · Angle: Allgemein, Markt

**Die Matratzenfirma Emma Sleep hat vor dem High Court (Anordnung vom 22.05.2026) eingeräumt, mit irreführenden Countdown-Timern, falschen 'High demand'-Hinweisen und Rabattangaben gegen Verbraucherrecht verstoßen zu haben, und sich verbindlich verpflichtet, diese Praktiken einzustellen.**

> “The Competition and Markets Authority (CMA) has secured a settlement with Emma Sleep after the company admitted it broke consumer law by using misleading countdown timers, and false ‘high demand’ messages and ‘discount’ claims. ... It also stops Emma Sleep using ‘limited time’ sales or discounts where substantially similar deals continue after the deadline passes.”

- **Quelle:** [CMA / GOV.UK – Court endorses CMA action as Emma Sleep agrees to change sales practices](https://www.gov.uk/government/news/court-endorses-cma-action-as-emma-sleep-agrees-to-change-sales-practices)
- **Datum der Quelle:** 2026-05-28 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle. Das Verfahren lief noch unter den alten Befugnissen (vor April 2025, daher über das Gericht). Sehr relevant für Bettwaren-Ads: 'Limited time'-Aktionen, die danach im Wesentlichen weiterlaufen, sowie Countdowns und 'High demand'-Hinweise sind ein konkretes Durchsetzungsziel der CMA in der Branche.
- **Wahrheits-Check:** *bestätigt*. Über die gov.uk-Suche gefunden und selbst abgerufen; Wortlaut und Datum bestätigt.

### 5 Referenzpreise – Emma-Sleep-Urteil zu 'War/Jetzt'-Preisen

#### 4C-V09

✅ BELEGT · Angle: Allgemein

**Im 'War/Jetzt'-Teil des CMA-Verfahrens gegen Emma Sleep stellte der High Court am 30.07.2026 neben den eingeräumten Verstößen keine weiteren Verstöße fest; die CMA hat ihre Leitlinie für den Online-Matratzenverkauf daraufhin vorläufig zurückgezogen.**

> “The High Court handed down its judgment on 30 July 2026. The High Court found that Emma Sleep had infringed the law in relation to a number of admitted breaches, but did not make further findings of infringement. The Court has invited the CMA and Emma Sleep to work together to agree the terms of a further order. While the CMA carefully considers the judgment and its next steps, it is temporarily withdrawing the online mattress sales guidance.”

- **Quelle:** [CMA / GOV.UK – Emma Group: consumer protection case (Fallseite)](https://www.gov.uk/cma-cases/emma-group-consumer-protection-case)
- **Datum der Quelle:** 2026-07-30 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle (Fallseite der CMA); das Urteil (PDF) habe ich nicht im Detail gelesen. Folge: Die Auslegung von 'War/Jetzt'-Preisen ist gerichtlich unsicherer geworden. Die branchenspezifischen CMA-Grundsätze ('Discount and reference pricing principles: selling mattresses online', 2024) sind vorläufig zurückgezogen. Die allgemeinen CTSI- und CMA-Kriterien (4C-56, 4C-58) bleiben die konservative Richtschnur.
- **Wahrheits-Check:** *bestätigt*. Fallseite selbst abgerufen (Update 30.07.2026); Wortlaut bestätigt.

### 5 CMA-Durchsetzung – Stand Wayfair

#### 4C-V10

✅ BELEGT · Angle: Allgemein

**Das CMA-Verfahren gegen Wayfair wegen zeitlich begrenzter Sales lief laut CMA-Fallseite noch: Die letzte Aktualisierung vom 18.06.2026 nennt 'Investigation ongoing. Next update: Summer 2026'; eine Feststellung gibt es nicht.**

> “18 June 2026 Investigation ongoing. Next update: Summer 2026 ... The CMA is investigating whether time-limited sales ended when they said they would.”

- **Quelle:** [CMA / GOV.UK – Wayfair: consumer protection enforcement case](https://www.gov.uk/cma-cases/wayfair-consumer-protection-enforcement-case)
- **Datum der Quelle:** 2026-06-18 · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle. Am 08.10.2026 war kein neueres Update veröffentlicht, obwohl eines für den Sommer angekündigt war. Gegen Wayfair ist kein Verstoß festgestellt; nicht als Beispiel für einen Rechtsbruch zitieren.
- **Wahrheits-Check:** *bestätigt*. Fallseite selbst abgerufen; 'Last updated 18 June 2026' bestätigt.

### 5 Referenzpreise – Zusagen Simba Sleep (Bettwarenbranche)

#### 4C-V11

✅ BELEGT · Angle: Allgemein

**Simba Sleep hat sich gegenüber der CMA verpflichtet, einen höheren 'War'-Preis nur zu verwenden, wenn er durch Verkäufe zum höheren Preis über ausreichend lange Zeit und in ausreichender Menge als echt belegt ist, und Countdowns nur so einzusetzen, dass sie keinen falschen Zeitdruck erzeugen.**

> “where Simba wishes to use a higher ‘was’ or comparison price, it must ensure that it establishes the higher price as a genuine price by achieving sales of the product at the higher price for a sufficient period of time and in sufficient volumes ... countdown clocks must not give consumers a false impression that they have to act quickly to avoid missing out on a deal”

- **Quelle:** [CMA / GOV.UK – Simba Sleep Limited: consumer protection case (Fallseite)](https://www.gov.uk/cma-cases/simba-sleep-limited-consumer-protection-case)
- **Datum der Quelle:** 2026-10-05 (Zusagen vom 25.07.2024; geänderte Zusagen am 22.09.2026 angenommen) · **Typ:** Regulierer/Regelwerk
- **Einordnung/Einschränkung:** Primärquelle. Die Zusagen gelten nur für Simba, zeigen aber den Maßstab der CMA für Rabattangaben in der Bettwarenbranche. Eine feste Mindestdauer oder Mindestmenge wird nicht genannt ('sufficient').
- **Wahrheits-Check:** *bestätigt*. Fallseite über die gov.uk-Suche gefunden und selbst abgerufen; Wortlaut und Daten bestätigt.

## Nachrecherche G5 (zu Track 4C)

*Auftrag: Angle D/Timing – aktuelle Daten für Q4 2026: (a) Royal Mail Last Posting Dates Christmas 2026 (royalmail.com, Royal Mail Group Pressemitteilung, Post Office) – falls veröffentlicht; sonst 2025er Termine mit Primärquelle; (b) Parcelforce, DPD, Evri, Yodel, Amazon UK Last-Order-Dates 2026 bzw. 2025; (c) Weihnachts-Ausgabenprognosen 2026 für UK (GlobalData, Deloitte, PwC, Barclays, VoucherCodes/Retail Research, BRC – veröffentlicht Sept./Okt. 2026); (d) Ergebnisse Black Friday/Cyber Weekend 2025 UK (Barclays, IMRG, BRC-KPMG, Adobe, MRI Software) und Prognosen 2026; (e) Ergebnisse Boxing Day/Januar-Sales 2026 (BRC, Barclays, MRI). Immer Primärquelle mit Datum.*

*Prüf-Fazit: Der Track ist überwiegend verlässlich: Alle 50 Claims wurden an der Quelle geprüft, keine Kernzahl war falsch, und kein Claim musste verworfen werden. Korrigiert wurden vor allem Präzisierungen und Nebenangaben: MRI-Wochen- statt Tageswert, BRC-Online-Anteil als höchster Stand seit 2022, Bezug der BRC-Aussage zu Frauen, gestrichene unbelegte Werte (Adobe +4,6 %, Barclays +83,7 %, Inflationsangaben) und nachgetragene Methodik (Post Office, VoucherCodes/GlobalData). Yodel 2025 ist jetzt per Webarchiv belegt (hochgestuft), PwC über eine abrufbare Wiedergabe; neu sind die CRA-Primärnorm und zwei weitere Kontext-Claims. Die zentrale Lücke bleibt: Am 08.10.2026 gibt es weder offizielle Versandschlusstermine noch unabhängige Weihnachts- oder Black-Friday-Prognosen für 2026, deshalb dürfen Ads keine konkreten 'Bestellen bis'-Daten oder Marktprognosen für 2026 nennen.*

### (a) Royal Mail Last Posting Dates – Status 2026

#### G5-01

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Stand 08.10.2026 zeigt die Post-Office-Übersicht der letzten empfohlenen Versandtermine noch die Termine für Weihnachten 2025. Offizielle 2026er Termine von Royal Mail oder Post Office waren nicht auffindbar.**

> “Last posting dates 2025 Get your cards, gifts and greetings there in time for Christmas. Check the latest recommended posting dates for all UK and international services. As always, our advice is to post early and avoid the rush.”

- **Quelle:** [Post Office – Christmas Last Posting Dates](https://www.postoffice.co.uk/last-posting-dates)
- **Datum der Quelle:** unbekannt (Seitenstand 08.10.2026; Footer 'Copyright 2026 Post Office') · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Belegt ist nur der Seitenstand am 08.10.2026. Ob Royal Mail auf royalmail.com schon 2026er Termine veröffentlicht hat, ließ sich nicht prüfen (403). Die Royal-Mail-Pressemitteilung vom 24.09.2026 nennt keine Termine, und die Websuche ergab keine offiziellen 2026er Termine. Momentaufnahme; vor Kampagnenstart erneut prüfen.
- **Wahrheits-Check:** *bestätigt*. PO-Seite am 08.10.2026 selbst per curl abgerufen (WebFetch: 403). Überschrift 'Last posting dates 2025' und Footer 'Copyright 2026' bestätigt. royalmail.com (zwei Pfade) lieferte 403, ein geratener 2026er PDF-Pfad auf royalmailtechnical.com 404. Pressemitteilung vom 24.09.2026 ohne Termine; Websuche ohne offizielle Termine 2026.

### (a) Royal Mail Last Posting Dates 2025 – 2nd Class

#### G5-02

✅ BELEGT · Angle: D Geschenk

**Für Weihnachten 2025 war der letzte empfohlene Einlieferungstag für Royal Mail 2nd Class (inkl. Signed For) im UK-Inland Mittwoch, der 17. Dezember 2025.**

> “Latest Posting Dates for Christmas 2025 … Royal Mail - UK Inland services* … Wednesday, 17 December | 2nd Class, 2nd Class Signed For … * Please note, latest posting dates are correct at the time of publishing and are subject to change.”

- **Quelle:** [Royal Mail – Latest posting dates for Christmas 2025 (business customers), PDF](https://www.royalmailtechnical.com/rmt_docs/Deferred_Operation/RM-and-PFW-LPDs-for-Christmas-2025-Business-v1.pdf)
- **Datum der Quelle:** 2025-10-06 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärdokument von Royal Mail ('Classified: RMG – Public'; PDF erstellt 26.09.2025, geändert 06.10.2025). Die Post-Office-Seite nennt dasselbe Datum. Gilt nur für 2025 und ist nicht auf 2026 übertragbar, weil sich die Wochentage verschieben (17.12.2026 ist ein Donnerstag).
- **Wahrheits-Check:** *bestätigt*. PDF selbst per curl geladen. Text und Fußnote 'subject to change' bestätigt; pdfinfo: CreationDate 26.09.2025, ModDate 06.10.2025. Die Post-Office-Seite nennt ebenfalls 'Wednesday 17 December'.

### (a) Royal Mail Last Posting Dates 2025 – 1st Class

#### G5-03

✅ BELEGT · Angle: D Geschenk

**Für Weihnachten 2025 war der letzte empfohlene Einlieferungstag für Royal Mail 1st Class (inkl. Signed For) im UK-Inland Samstag, der 20. Dezember 2025.**

> “Saturday, 20 December | 1st Class, 1st Class Signed For”

- **Quelle:** [Royal Mail – Latest posting dates for Christmas 2025 (business customers), PDF](https://www.royalmailtechnical.com/rmt_docs/Deferred_Operation/RM-and-PFW-LPDs-for-Christmas-2025-Business-v1.pdf)
- **Datum der Quelle:** 2025-10-06 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Royal-Mail-Primärdokument; die Post-Office-Seite bestätigt den Termin ('Royal Mail 1st Class and 1st Class Signed For … Saturday 20 December'). Gilt nur für 2025, mit Hinweis 'subject to change'.
- **Wahrheits-Check:** *bestätigt*. Im PDF und auf der Post-Office-Seite selbst gefunden.

### (a) Royal Mail Last Posting Dates 2025 – Tracked 48/24

#### G5-04

✅ BELEGT · Angle: D Geschenk

**Für Weihnachten 2025 galten als letzte empfohlene Einlieferungstage Freitag, 19. Dezember (Royal Mail Tracked 48), und Sonntag, 21. Dezember 2025 (Royal Mail Tracked 24).**

> “Royal Mail Tracked 24 Last recommended posting date Sunday 21 December Royal Mail Tracked 48 Last recommended posting date Friday 19 December”

- **Quelle:** [Post Office – Christmas Last Posting Dates (Stand: 2025er Termine)](https://www.postoffice.co.uk/last-posting-dates)
- **Datum der Quelle:** unbekannt (Seitenstand 08.10.2026) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Das Royal-Mail-Business-PDF bestätigt beide Termine (Friday, 19 December: Royal Mail Tracked 48; Sunday, 21 December: Royal Mail Tracked 24). Für den Versand einer Bettdecke sind Paketdienste mit Tracking relevanter als Briefpost. Gilt nur für 2025.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Post-Office-Seite und Daten im PDF selbst gefunden.

### (a) Royal Mail Last Posting Dates 2025 – Special Delivery

#### G5-05

✅ BELEGT · Angle: D Geschenk

**Für Weihnachten 2025 war Dienstag, der 23. Dezember 2025, der letzte empfohlene Einlieferungstag für Royal Mail Special Delivery Guaranteed.**

> “Tuesday, 23 December | Special Delivery Guaranteed®”

- **Quelle:** [Royal Mail – Latest posting dates for Christmas 2025 (business customers), PDF](https://www.royalmailtechnical.com/rmt_docs/Deferred_Operation/RM-and-PFW-LPDs-for-Christmas-2025-Business-v1.pdf)
- **Datum der Quelle:** 2025-10-06 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärdokument; die Post-Office-Seite nennt ebenfalls 'Tuesday 23 December'. Premium-Dienst, also kein Maßstab für Standardversand. Gilt nur für 2025.
- **Wahrheits-Check:** *bestätigt*. Im PDF und auf der Post-Office-Seite selbst bestätigt.

### (a) Royal Mail – Saisonplanung Weihnachten 2026

#### G5-06

✅ BELEGT · Angle: D Geschenk, Markt

**Royal Mail stellt für Weihnachten 2026 fast 22.000 befristete Kräfte ein. Die Saisonstellen laufen von Ende Oktober 2026 bis Anfang Januar 2027, schließen Black Friday und Cyber Monday ein und haben ihre Spitze im Dezember.**

> “The seasonal roles will run from late October through to early January 2027. The period for the additional temporary work includes Black Friday and Cyber Monday but will be at its peak in December.”

- **Quelle:** [International Distribution Services / Royal Mail – Pressemitteilung 'Royal Mail to hire 22,000 temporary workers to help deliver Christmas'](https://www.internationaldistributionservices.com/en/press-centre/press-releases/royal-mail/royal-mail-to-hire-22-000-temporary-workers-to-help-deliver-christmas/)
- **Datum der Quelle:** 2026-09-24 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Aktuelle Primärquelle von Royal Mail für 2026 (im Text 'almost 22,000'). Sie belegt den Planungszeitraum, nennt aber keine Last-Posting-Dates und keine Liefertermine.
- **Wahrheits-Check:** *korrigiert*. Die alte URL auf royalmailgroup.com leitet per 301 auf internationaldistributionservices.com weiter; URL ersetzt. Datum '24 September 26', 'almost 22,000' und Wortlaut selbst bestätigt; keine Last-Posting-Dates auf der Seite.

### (a) Royal Mail Last Posting Dates 2026 – Mythos-Check

#### G5-07

❌ NICHT BELEGT / MYTHOS · Angle: D Geschenk

**Die im Netz kursierenden 'Royal Mail Last Posting Dates 2026' (z. B. 'Tuesday 23 December' für Special Delivery) sind nicht belegt. Ihre Wochentage entsprechen dem Kalender 2025, nicht 2026; es sind erkennbar umetikettierte 2025er Termine, und der 2nd-Class-Termin weicht sogar vom offiziellen 2025er Termin ab.**

> “The last day to post for UK Christmas 2026 arrival is Tuesday 23 December for Special Delivery Guaranteed, Sunday 21 December for Royal Mail Tracked 24, Saturday 20 December for 1st Class, Friday 19 December for Royal Mail Tracked 48, and Thursday 18 December for 2nd Class.”

- **Quelle:** [postofficehours.co.uk – Royal Mail Christmas Posting Dates 2026 (Drittanbieter, nicht Royal Mail/Post Office)](https://postofficehours.co.uk/christmas-posting-dates)
- **Datum der Quelle:** 2026-09-30 ('Last reviewed') · **Typ:** Sonstiges
- **Einordnung/Einschränkung:** Wochentage selbst berechnet: Im Jahr 2026 ist der 23.12. ein Mittwoch, der 21.12. ein Montag, der 20.12. ein Sonntag, der 19.12. ein Samstag und der 18.12. ein Freitag. Alle genannten Wochentage passen zu 2025. Den 2nd-Class-Termin gab Royal Mail für 2025 mit Mi 17.12. an, die Seite nennt Do 18.12. Laut Disclaimer ist die Seite 'not affiliated with … Post Office Ltd or Royal Mail' und nennt keine Royal-Mail-Quelle. Nicht in Ads verwenden.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, 'Last reviewed: 30 September 2026' und Disclaimer selbst gefunden. Wochentage für 2025 und 2026 per Python berechnet. Die Unbelegtheit ist bestätigt; ergänzt habe ich die Abweichung beim 2nd-Class-Termin.

### (a) Royal Mail/Post Office – Geschenkversand über Post Office

#### G5-08

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer Post-Office-Umfrage (Okt. 2025, 2.000 UK-Erwachsene) verschickt ein Drittel (33 %) der Menschen Geschenke über die Post Office.**

> “With a third (33 per cent) of people sending gifts via the Post Office … Research was conducted by Post Office ‘Hot Topics’ in October 2025 with 2,000 nationally representative UK adults using a sample provided by Dynata.”

- **Quelle:** [Post Office (Mynewsdesk) – 'Post Office announces last posting dates for sending Christmas presents'](https://www.mynewsdesk.com/uk/post-office/pressreleases/post-office-announces-last-posting-dates-for-sending-christmas-presents-3420939)
- **Datum der Quelle:** 2025-12-19 (Seitenkopf; Fließtext datiert 'Wednesday 10th December') · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Post Office 'Hot Topics', Oktober 2025, 2.000 national repräsentative UK-Erwachsene, Stichprobe von Dynata
- **Einordnung/Einschränkung:** Eigene PR-Umfrage eines Postunternehmens in eigener Sache. Die Methodik ist knapp offengelegt (n, Zeitraum, Panelanbieter), aber Fragestellung und Gewichtung fehlen. Taugt als Kontext, nicht als Ad-Claim.
- **Wahrheits-Check:** *korrigiert*. Die Methodik steht am Ende der Mitteilung; 'nicht angegeben' war falsch. Stichprobe, Aussage und Wortlaut ergänzt. Zitat und Daten (19.12.2025 bzw. 10.12.) selbst bestätigt.

### (b) Parcelforce Last Posting Dates 2025

#### G5-09

✅ BELEGT · Angle: D Geschenk

**Für Weihnachten 2025 waren die letzten Einlieferungstage bei Parcelforce Worldwide im UK-Inland Freitag, 19. Dezember (express48), und Montag, 22. Dezember 2025 (express10, expressPM und express24).**

> “Parcelforce Worldwide - UK Inland services* Date Service Friday, 19 December express48 Monday, 22 December express10, expressPM and express 24”

- **Quelle:** [Royal Mail – Latest posting dates for Christmas 2025 (business customers), PDF](https://www.royalmailtechnical.com/rmt_docs/Deferred_Operation/RM-and-PFW-LPDs-for-Christmas-2025-Business-v1.pdf)
- **Datum der Quelle:** 2025-10-06 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärdokument der Royal Mail Group (Parcelforce ist Konzerntochter). Die Post-Office-Seite nennt dieselben Termine ('express24. expressAM and express10 … Monday 22 December'). Nur für 2025; 2026er Termine sind nicht veröffentlicht.
- **Wahrheits-Check:** *bestätigt*. Im PDF und auf der Post-Office-Seite selbst bestätigt.

### (b) DPD Last Posting Dates 2025 (über Post Office)

#### G5-10

✅ BELEGT · Angle: D Geschenk

**Bei Einlieferung über Post-Office-Filialen war 2025 der letzte empfohlene Termin für DPD Next Day Montag, 22. Dezember (Festland). Für entlegene schottische Postleitzahlen wie HS1–HS9 oder ZE1–ZE3 lag er schon auf Mittwoch, 17. Dezember. DPD Gold lief bis Dienstag, 23. Dezember 2025.**

> “DPD Next Day and Next Day by 12 Postcode Last recommended posting date All postcodes (excluding those below) Monday 22 December … HS1-HS9, KW15-KW17, PA34, PA41-PA48, PA80, ZE1-ZE3 Wednesday 17 December … DPD Gold Last recommended posting date Tuesday 23 December”

- **Quelle:** [Post Office – Christmas Last Posting Dates (Stand: 2025er Termine)](https://www.postoffice.co.uk/last-posting-dates)
- **Datum der Quelle:** unbekannt (Seitenstand 08.10.2026) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Gilt nur für den Versandkanal Post Office. Dazwischen gab es Stufen (z. B. AB36–AB38, IV1–IV62: Sa 20.12.; IV63, KA28: Fr 19.12.). Die eigene Seite von DPD wurde nicht geprüft. Für einen Online-Shop gelten die Termine des eigenen Carrier-Vertrags.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und Postleitzahl-Stufen auf der Post-Office-Seite (curl) selbst gefunden.

### (b) Evri Last Posting Dates 2025 (über Post Office)

#### G5-11

✅ BELEGT · Angle: D Geschenk

**Bei Einlieferung über Post-Office-Filialen war 2025 der letzte empfohlene Termin für Evri Standard Tracked Freitag, 19. Dezember, und für Evri Next Day Tracked Montag, 22. Dezember 2025.**

> “Evri Standard Tracked Last recommended posting date Friday 19 December Evri Next Day Tracked Last recommended posting date Monday 22 December”

- **Quelle:** [Post Office – Christmas Last Posting Dates (Stand: 2025er Termine)](https://www.postoffice.co.uk/last-posting-dates)
- **Datum der Quelle:** unbekannt (Seitenstand 08.10.2026) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Gilt nur für den Post-Office-Kanal; Evris eigene Weihnachtsseite wurde nicht gefunden. Nur 2025.
- **Wahrheits-Check:** *bestätigt*. Wortlaut auf der Post-Office-Seite selbst gefunden.

### (b) Yodel Last Posting Dates 2025

#### G5-12

✅ BELEGT · Angle: D Geschenk

**Yodel Direct, Yodels Versandservice für Privatkunden, nannte für Weihnachten 2025 Freitag, den 19. Dezember, als letzten Versandtag für Zustellung vor dem 1. Weihnachtstag. Bei Abholungen vom 20. bis 23. Dezember war die Zustellung vor Weihnachten nicht mehr sicher. Die Seite leitet heute auf InPost Direct um, ohne Weihnachtstermine.**

> “Key Shipping Dates - Christmas 2025 & New Year Friday 19th December Last day to send parcels to be delivered before Christmas Day Saturday 20th - Tuesday 23rd December Deliveries will be made into local stores and lockers however collections made during these days may not be delivered before Christmas Day.”

- **Quelle:** [Yodel Direct – Key Shipping Dates (Archivkopie der Wayback Machine vom 18.12.2025)](https://web.archive.org/web/20251218100416/https://www.yodeldirect.co.uk/services/key-shipping-dates)
- **Datum der Quelle:** 2025-12-18 (Archivstand) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Archivierte Originalseite des Unternehmens. Gilt nur für Yodel Direct 2025, nicht automatisch für Geschäftskundenverträge mit Yodel (ChannelX nennt servicebezogene Termine 18./19./20./22.12., nicht geprüft). Die Live-URL leitet am 08.10.2026 per 308 auf inpostdirect.co.uk um, dort ohne Weihnachtstermine. Für 2026 kein Termin.
- **Wahrheits-Check:** *hochgestuft*. Live-URL selbst geprüft: Weiterleitung auf InPost Direct, keine Termine. Wayback-Snapshot vom 18.12.2025 per curl geladen, Wortlaut dort gefunden. Einordnung von NICHT_BELEGT auf BELEGT (nur 2025, nur Yodel Direct); Aussage, Quelle und URL ersetzt.

### (b) Amazon UK Last-Order-Date

#### G5-13

✅ BELEGT · Angle: D Geschenk

**Amazon UK nennt kein festes letztes Bestelldatum für Lieferung vor Weihnachten. Maßgeblich ist laut Amazon das Lieferdatum je Artikel bzw. an der Kasse.**

> “It depends on the item. To ensure your order arrives in time for Christmas, check the delivery details on the product page … Always check the final delivery date at checkout, as delivery cut off dates are a guideline”

- **Quelle:** [About Amazon UK – 'What’s the last date to order from Amazon in the UK for Christmas?'](https://aboutamazon.co.uk/news/retail/amazon-last-date-order-christmas-delivery)
- **Datum der Quelle:** 2025-12-05 (dateModified; Erstveröffentlichung 2024-12-09) · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Primärquelle; auf der Seite ist kein Datum sichtbar, die Metadaten sind eindeutig. Wer 'bei Amazon gilt der 23.12.' sagt, vereinfacht. Für 2026 noch nicht aktualisiert.
- **Wahrheits-Check:** *bestätigt*. Wortlaut per WebFetch bestätigt. dateModified 2025-12-05 und datePublished 2024-12-09 per curl in den Metadaten gefunden.

### (b) Amazon UK – Weihnachtsretouren

#### G5-14

✅ BELEGT · Angle: D Geschenk

**Bei Amazon UK konnten die meisten zwischen dem 1. November und 31. Dezember 2025 gekauften Artikel bis zum 31. Januar 2026 zurückgegeben werden.**

> “Most items purchased between 1 November and 31 December can now be returned until 31 January 2026.”

- **Quelle:** [About Amazon UK – 'What’s the last date to order from Amazon in the UK for Christmas?'](https://aboutamazon.co.uk/news/retail/amazon-last-date-order-christmas-delivery)
- **Datum der Quelle:** 2025-12-05 · **Typ:** Unternehmensbericht
- **Einordnung/Einschränkung:** Gilt nur für die Saison 2025 und für 'most items'. Zeigt den Wettbewerbsstandard bei Geschenk-Retouren (Angle D). Eigene Rückgabebedingungen müssen ein entsprechendes Versprechen tatsächlich erfüllen.
- **Wahrheits-Check:** *bestätigt*. Satz wörtlich auf der Seite gefunden.

### (b) Amazon UK Last-Order-Dates 2025 (Sekundärquelle)

#### G5-15

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut MoneySavingExpert war der letzte Bestelltag für Amazon-Expressversand (für Prime kostenlos) 2025 Dienstag, der 23. Dezember. Der Standardtermin war 'TBC'; im Vorjahr lag er für Nicht-Prime-Kunden auf dem 19. Dezember.**

> “Amazon* TBC Last year it was 19 December for non-Prime members but it can vary by item. … Tuesday 23 December Free for Prime members; usually £3.99-£5.99 for non-Prime members”

- **Quelle:** [MoneySavingExpert – 'Christmas last order dates for 2025'](https://www.moneysavingexpert.com/deals/deals-hunter/last-order-dates/)
- **Datum der Quelle:** 2025-12-18 · **Typ:** Presse
- **Einordnung/Einschränkung:** Verbraucherportal, das Händlerangaben sammelt; keine Amazon-Primärquelle. Amazon selbst nennt kein festes Datum (siehe G5-13). Der Standardtermin blieb unbestätigt.
- **Wahrheits-Check:** *bestätigt*. Seite (Stand 18.12.2025, Tabelle 'for 2025') selbst abgerufen; Amazon-Zeilen bestätigt.

### (b) Last-Order-Dates großer UK-Händler 2025 (Benchmark)

#### G5-16

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**Laut MoneySavingExpert lagen die Standardversand-Schlusstermine großer UK-Händler 2025 meist zwischen 17. und 20. Dezember, z. B. Ikea Mittwoch 17.12., John Lewis Freitag 19.12. (kleine Artikel) bzw. Donnerstag 18.12. (große Artikel) und M&S Samstag 20.12.**

> “Ikea Wednesday 17 December … John Lewis* Friday 19 December for small items £4.50 or free for £70+ orders Thursday 18 December for large items £19.95 … M&S* Saturday 20 December £3.99 or free for £60+ orders”

- **Quelle:** [MoneySavingExpert – Christmas last order dates for 2025](https://www.moneysavingexpert.com/deals/deals-hunter/last-order-dates/)
- **Datum der Quelle:** 2025-12-18 · **Typ:** Presse
- **Einordnung/Einschränkung:** Sekundäre Zusammenstellung von Händlerangaben. Benchmark für die eigene Cut-off-Kommunikation 2026, kein Beleg für 2026.
- **Wahrheits-Check:** *bestätigt*. Zeilen für Ikea, John Lewis und M&S selbst bestätigt.

### (b) Lieferzusage 'bis Weihnachten' – Verbraucherrecht

#### G5-17

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut MoneySavingExpert muss gesetzlich nur 'within a reasonable time' (bis zu 30 Tage) geliefert werden, und eine Erstattung wegen verspäteter Weihnachtslieferung gibt es nur, wenn der Händler Lieferung bis 25. Dezember zugesagt hat. Das ist eine vereinfachte Darstellung; die Primärnorm steht in G5-V01.**

> “By law, delivery only needs to be “within a reasonable time”, which could be up to 30 days – no use for Christmas. For you to get a refund if an item doesn’t arrive in time, the retailer must have stated goods will arrive by 25 December.”

- **Quelle:** [MoneySavingExpert – Christmas last order dates (Abschnitt 'Late delivery rights')](https://www.moneysavingexpert.com/deals/deals-hunter/last-order-dates/)
- **Datum der Quelle:** 2025-12-18 · **Typ:** Presse
- **Einordnung/Einschränkung:** Verbraucherportal, keine Rechtsquelle. Laut Consumer Rights Act 2015, s. 28(6) kann der Verbraucher auch dann vom Vertrag zurücktreten, wenn er dem Händler vor Vertragsschluss gesagt hat, dass die rechtzeitige Lieferung wesentlich ist, oder wenn sie nach den Umständen wesentlich war. MSE vereinfacht also. Für Ads gilt: Eine Zusage 'arrives before Christmas' macht den Termin verbindlich und sollte nur mit gesicherten Carrier-Terminen gemacht werden.
- **Wahrheits-Check:** *korrigiert*. MSE-Sinngehalt bestätigt. Primärnorm CRA 2015 s. 28 auf legislation.gov.uk selbst geprüft (siehe G5-V01); Begründung um die Fälle in s. 28(6)(b)/(c) ergänzt.

### (b) Feiertage Weihnachten 2026 (Versandpause)

#### G5-18

✅ BELEGT · Angle: D Geschenk

**In ganz UK ist der 25. Dezember 2026 (Freitag) Feiertag, der Boxing Day wird als Ersatzfeiertag am Montag, 28. Dezember 2026 begangen.**

> “{"title":"Christmas Day","date":"2026-12-25","notes":"","bunting":true} {"title":"Boxing Day","date":"2026-12-28","notes":"Substitute day","bunting":true}”

- **Quelle:** [GOV.UK – UK bank holidays (JSON-Datensatz)](https://www.gov.uk/bank-holidays.json)
- **Datum der Quelle:** unbekannt (abgerufen 08.10.2026) · **Typ:** Parlament/Regierung
- **Einordnung/Einschränkung:** Amtliche Quelle. Die Einträge sind für England & Wales, Schottland und Nordirland identisch. In Schottland kommt der 2nd January als Ersatzfeiertag am 04.01.2027 hinzu. Den Wochentag (Freitag) habe ich berechnet.
- **Wahrheits-Check:** *bestätigt*. JSON selbst geladen und für alle drei Landesteile ausgewertet; Wochentag per Python berechnet.

### (c) Weihnachtsprognose 2026 – Epsilon Golden Quarter

#### G5-19

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut einer Epsilon-Umfrage 2026 wollen UK-Verbraucher im Zeitraum von Black Friday bis zu den Januar-Sales insgesamt £17,9 Mrd. ausgeben, im Schnitt £334 pro Person.**

> “New Epsilon research shows where that waste happens across the peak window, which runs from Black Friday through to the January sales … UK consumers expect to spend £334 each over the peak window, or £17.9bn in total”

- **Quelle:** [Epsilon EMEA – 'Black Friday 2026: how to avoid wasting marketing budget' (auf Basis des Reports 'Advertising Under Pressure')](https://www.epsilon.com/emea/insights/blog/black-friday-2026-how-to-avoid-wasting-marketing-budget)
- **Datum der Quelle:** 2026-09-09 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 2.000 UK-Erwachsene, national repräsentativ gewichtet, plus 200 UK-Marketing-Entscheider; 2026 von Epsilon beauftragt, Institut und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Umfrage eines Adtech- und Marketing-Dienstleisters zu Ausgabeabsichten, nicht zu tatsächlichen Ausgaben. Institut und Feldzeit nicht genannt. Nicht mit VoucherCodes oder PwC vergleichbar, da Zeitfenster und Definition abweichen.
- **Wahrheits-Check:** *korrigiert*. Datum, Zahlen, Definition des 'peak window' und Methodik selbst bestätigt. Gestrichen: den Verweis auf eine Report-Seite vom 10.08.2026, weil nicht selbst geprüft.

### (c) Weihnachtsprognose 2026 – Kaufzeitpunkte (Epsilon)

#### G5-20

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut Epsilon-Umfrage 2026 kaufen 50 % der Shopper am Black Friday, 37 % am Boxing Day und 34 % in den Januar-Sales; 63 % schieben größere Anschaffungen auf.**

> “Our research puts the share of shoppers converting on Black Friday at 50%, falling to 37% on Boxing Day and 34% in the January sales … 63% are deferring bigger purchases, and 39% say they are buying less often but choosing better when they do.”

- **Quelle:** [Epsilon EMEA – 'Black Friday 2026: how to avoid wasting marketing budget'](https://www.epsilon.com/emea/insights/blog/black-friday-2026-how-to-avoid-wasting-marketing-budget)
- **Datum der Quelle:** 2026-09-09 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 2.000 UK-Erwachsene, gewichtet; 2026
- **Einordnung/Einschränkung:** Selbstauskunft in einer Anbieter-Umfrage; was 'converting' heißt, ist nicht genau definiert. Für die Timing-Planung bei einer größeren Anschaffung wie einer Bettdecke ein Hinweis, kein harter Beleg.
- **Wahrheits-Check:** *bestätigt*. Beide Sätze wörtlich gefunden (WebFetch und curl).

### (c) Weihnachts-/Black-Friday-Prognose 2026 – Shopify

#### G5-21

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut Shopify-Umfrage (Okt. 2026) planen UK-Shopper für das Black-Friday-Wochenende 2026 im Schnitt £165 ein (2025: £181). 53 % sagen, die Wirtschaftslage habe ihre Einkaufspläne negativ beeinflusst.**

> “Consumers are entering the holiday season under significant economic pressure, with 53% of UK shoppers saying recent conditions have negatively affected their shopping plans. Planned Black Friday weekend spending across the UK is expected to drop to £165 on average from £181 in 2025.”

- **Quelle:** [Retail Technology Innovation Hub – 'Shopify research: AI savvy UK shoppers set to spend £165 this Christmas but will make brands earn it'](https://retailtechinnovationhub.com/home/2026/10/5/shopify-ai-savvy-uk-shoppers-set-to-spend-165-this-christmas-but-will-make-brands-earn-it)
- **Datum der Quelle:** 2026-10-06 (Byline; URL-Pfad 05.10.2026) · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 18.000 Verbraucher in 9 Ländern (AU, CA, FR, DE, IT, JP, ES, UK, US) und 7.500 Entscheider aus Firmen unter 1.000 Mitarbeitern; UK-Teilstichprobe und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Die Zahl stammt aus Shopifys Mitteilung, wiedergegeben von einem Fachmedium; eine Shopify-Originalseite wurde nicht gefunden. Der Titel spricht von 'this Christmas', die Zahl gilt aber für das Black-Friday-Wochenende. Planwert, kein Ergebnis.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Datum und Methodik selbst bestätigt. Websuche fand keine Shopify-Primärquelle.

### (c) Weihnachtsprognose 2026 – Wertverständnis und Preisbeobachtung (Shopify)

#### G5-22

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut Shopify-Umfrage 2026 lassen 28 % der UK-Shopper Produkte bewusst im Warenkorb, um auf Preissenkungen zu warten, und 54 % definieren guten Wert als höhere Qualität, als für den Preis erwartet.**

> “28% said they deliberately leave products in their cart to see if the price drops. … 54% define good value as receiving higher-than-expected quality for the price, while 38% say it means products having a longer lifespan than expected.”

- **Quelle:** [Retail Technology Innovation Hub – Shopify research (UK)](https://retailtechinnovationhub.com/home/2026/10/5/shopify-ai-savvy-uk-shoppers-set-to-spend-165-this-christmas-but-will-make-brands-earn-it)
- **Datum der Quelle:** 2026-10-06 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 18.000 Verbraucher in 9 Ländern; UK-n nicht angegeben
- **Einordnung/Einschränkung:** Anbieter-Umfrage ohne UK-Stichprobengröße. Hilft beim Messaging (Qualität und Langlebigkeit statt reinem Rabatt), ist aber keine Marktgröße.
- **Wahrheits-Check:** *bestätigt*. Zahlen wörtlich bestätigt.

### (c) Weihnachtsprognose 2026 – Salsify Holiday Pulse

#### G5-23

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Salsify-Umfrage (April 2026, 400 UK-Befragte) wollen 26 % der UK-Shopper in der Weihnachtssaison 2026 mehr ausgeben als im Vorjahr.**

> “In terms of global markets, 26% of U.K. shoppers say they’ll spend more this holiday season.”

- **Quelle:** [Salsify – 'Consumer Spending Trends: How Much Will Holiday Shoppers Spend in 2026?' (2026 Holiday Pulse Report)](https://www.salsify.com/blog/consumer-spending-trends-holiday-spending-predictions)
- **Datum der Quelle:** 2026-04-30 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 1.212 Befragte: 412 USA, 400 UK, 400 Kanada; Institut und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Kleine UK-Stichprobe (n=400) in einer Anbieter-Umfrage, früh im Jahr erhoben, also vor der Eintrübung im Herbst laut BRC-Opinium.
- **Wahrheits-Check:** *bestätigt*. Datum, Satz und Stichprobe selbst bestätigt.

### (c) Konsumstimmung Herbst 2026 – BRC-Opinium

#### G5-24

✅ BELEGT · Angle: Markt

**Im BRC-Opinium-Monitor fiel die Erwartung der UK-Verbraucher an ihre eigenen Einzelhandelsausgaben in den nächsten drei Monaten im September 2026 auf +5 (August: +8).**

> “Their personal spending on retail fell to +5 in September, down from +8 in August.”

- **Quelle:** [British Retail Consortium – 'Budget must bolster wavering consumer confidence' (BRC-Opinium Consumer Sentiment)](https://brc.org.uk/news-and-events/news/corporate-affairs/2026/ungated/budget-must-bolster-wavering-consumer-confidence/)
- **Datum der Quelle:** 2026-09-24 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** BRC-Opinium-Monitor; n und Feldzeit auf der Seite nicht angegeben
- **Einordnung/Einschränkung:** Aktuellster Stimmungsindikator vor Q4 2026; ein Netto-Saldo, kein Ausgabenbetrag. Die Erwartung an die Wirtschaft sank auf -34 (August -28), an die persönliche Finanzlage auf -15 (August -9). Der Satz 'This decline was much sharper among women' bezieht sich auf das Vertrauen in Wirtschaft und Finanzlage, nicht auf die Einzelhandelsausgaben. Stichprobe auf der Seite nicht genannt.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Datum bestätigt. In der Begründung präzisiert, worauf sich die Aussage zu Frauen bezieht (Zitat Helen Dickinson per curl geprüft); Wert für die Finanzlage ergänzt.

### (c) Einzelhandelsumsatz Spätsommer 2026 – BRC-KPMG

#### G5-25

✅ BELEGT · Angle: Markt

**Laut BRC-KPMG Retail Sales Monitor stiegen die UK-Einzelhandelsumsätze im August 2026 nur um 0,7 % ggü. Vorjahr. Große Anschaffungen wie Möbel und Haushaltsgeräte gingen zurück.**

> “UK Total retail sales increased by 0.7% year on year in August, against growth of 3.1% in August 2025. … This was particularly true for discretionary spending, as big-ticket purchases like furniture and household appliances declined”

- **Quelle:** [British Retail Consortium – 'Consumer demand cools as summer ends' (BRC-KPMG Retail Sales Monitor August 2026)](https://brc.org.uk/news-and-events/news/corporate-affairs/2026/ungated/consumer-demand-cools-as-summer-ends/)
- **Datum der Quelle:** 2026-09-08 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Zeitraum 2.–29. August 2026; Händlerpanel des BRC
- **Einordnung/Einschränkung:** Etablierter Branchenmonitor, nominale Werte (nicht inflationsbereinigt). Zeigt die gedämpfte Ausgangslage vor Q4 2026. Der September-Monitor ist am 08.10.2026 noch nicht erschienen.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Datum und Zeitraum bestätigt. September-Monitor: Pfad /2026/sep/ 404, und die BRC-Newsliste nennt als letzten Monitor den für August.

### (c) Konsumvertrauen 2026 – Deloitte Consumer Tracker

#### G5-26

✅ BELEGT · Angle: Markt

**Der Deloitte-Konsumvertrauensindex fiel im ersten Quartal 2026 von -11,1 % auf -14,1 %, den tiefsten Stand seit Q3 2023.**

> “The Deloitte Consumer Confidence Index dropped 3 percentage points from -11.1% in Q4 2025 to -14.1% in Q1”

- **Quelle:** [Deloitte UK – Consumer Tracker Q1 2026](https://www.deloitte.com/uk/en/Industries/consumer/research/consumer-tracker.html)
- **Datum der Quelle:** 2026-04-20 · **Typ:** Umfrage (Institut/unabhängig)
- **Stichprobe/Methodik:** YouGov im Auftrag von Deloitte; online, national repräsentativ, über 3.000 UK-Erwachsene 18+, 12.–17. März 2026
- **Einordnung/Einschränkung:** Transparente Methodik, aber Q1-Stand und keine Weihnachtsprognose. Q2- und Q3-Ausgabe 2026 wurden weder auf der Seite noch per Websuche gefunden.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Methodik selbst bestätigt. Die Seite nennt die Q1-2026-Ausgabe mit Veröffentlichung am 20.04.2026; Datum präzisiert.

### (c) Weihnachtsprognose – Basis 2025 (VoucherCodes)

#### G5-27

⚠️ EINGESCHRÄNKT · Angle: Markt

**Der VoucherCodes 'Shopping for Christmas Report 2025', erstellt von GlobalData, prognostizierte für die sechs Wochen von Mitte November bis Ende Dezember 2025 UK-Umsätze von £91,12 Mrd. (+3,2 %) bei einem Absatzrückgang von 0,3 %.**

> “Christmas spending is set to hit record highs of £91.12bn this year … forecasts a 3.2% rise in sales across the six week festive period (from mid-November to end of December) … sales volume is forecast to decrease by 0.3% for the first time since 2023”

- **Quelle:** [Retail Times – 'Christmas shoppers set to splurge £91bn as retail sales rise 3.2% this year' (VoucherCodes Shopping for Christmas Report 2025)](https://retailtimes.co.uk/christmas-shoppers-set-to-splurge-91bn-as-retail-sales-rise-3-2-this-year/)
- **Datum der Quelle:** 2025-10-21 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Laut TheIndustry.fashion (22.10.2025) von GlobalData im Auftrag von VoucherCodes erstellt, national repräsentative Stichprobe von 2.000 UK-Verbrauchern; Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Prognose eines Gutscheinportals aus dem Vorjahr, wiedergegeben in der Fachpresse. Breite Definition, die u. a. Lebensmittel und Reisen umfasst. Eine Ausgabe für 2026 war am 08.10.2026 nicht erschienen. Nur als Basiswert verwenden.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Datum bei Retail Times bestätigt. Methodik (GlobalData, n=2.000) selbst bei TheIndustry.fashion nachgelesen und ergänzt.

### (c) Weihnachtsprognose – Geschenkausgaben 2025 (VoucherCodes)

#### G5-28

⚠️ EINGESCHRÄNKT · Angle: D Geschenk, Markt

**VoucherCodes/GlobalData prognostizierten für Weihnachten 2025 Geschenkausgaben von £11,59 Mrd. (+2,1 %), im Schnitt £443 je Haushalt.**

> “with £11.59bn set to be spent on presents alone (+2.1% YoY) – that equates to an average of £443 per household and 50.5% of all Christmas sales.”

- **Quelle:** [Retail Times – VoucherCodes Shopping for Christmas Report 2025](https://retailtimes.co.uk/christmas-shoppers-set-to-splurge-91bn-as-retail-sales-rise-3-2-this-year/)
- **Datum der Quelle:** 2025-10-21 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** GlobalData für VoucherCodes, 2.000 UK-Verbraucher (laut TheIndustry.fashion)
- **Einordnung/Einschränkung:** Prognose, kein Ergebnis. Der Artikel widerspricht sich selbst: £11,59 Mrd. sind nur rund 12,7 % von £91,12 Mrd., nicht 50,5 %. Die Bezugsgröße ist unklar, deshalb nur vorsichtig verwenden. Kein Wert für Bettwaren.
- **Wahrheits-Check:** *korrigiert*. Wortlaut bestätigt, Rechnung 11,59/91,12 nachgerechnet und Stichprobe ergänzt.

### (c) Weihnachtsprognose – Basis 2025 (PwC)

#### G5-29

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut PwC Festive Predictions Survey 2025 wollten UK-Verbraucher £24,6 Mrd. für Geschenke und Feiern ausgeben, 3,5 % mehr als 2024 (£23,7 Mrd.). Pro Erwachsenem stieg der Wert von £449 auf £461.**

> “UK consumers are set to spend £24.6billion on presents and celebrations over the Christmas period this year, a 3.5% increase from the £23.7billion spent in 2024. … Average spending per adult is forecast to rise from £449 to £461.”

- **Quelle:** [InsightDIY – 'Festive spending forecast to reach £24.6bn this year' (Wiedergabe der PwC-UK-Pressemitteilung; Original: pwc.co.uk, 403)](https://www.insightdiy.co.uk/news/festive-spending-forecast-to-reach-246bn-this-year/15891.htm)
- **Datum der Quelle:** 2025-12-12 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** nicht angegeben; laut Artikel 'undertaken three weeks before the Budget'
- **Einordnung/Einschränkung:** Die PwC-Originalseite lieferte bei WebFetch und curl 403. Die Fachpresse gibt die Mitteilung wieder; Grocery Gazette (12.12.2025) bestätigt £24,6 Mrd. und 3,5 %. Stichprobe und Feldzeit nicht offengelegt. Eine PwC-Prognose für 2026 wurde nicht gefunden.
- **Wahrheits-Check:** *korrigiert*. URL auf eine abrufbare Wiedergabe umgestellt (InsightDIY, 12.12.2025), Wortlaut dort gefunden, Wert je Erwachsenem ergänzt. Gestrichen: die Reuters-Aussage zu realen Mengen, weil nicht selbst geprüft. PwC-Original weiterhin 403.

### (d) Black Friday 2025 – Barclays Transaktionen

#### G5-30

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut Barclays-Kartendaten lag die Zahl der Transaktionen am Black Friday (28.11.2025) 62 % (Barclays-Original: 62,5 %) über einem durchschnittlichen Tag 2025, der Höchstwert des Jahres bis dahin.**

> “Spending data from Barclays shows transactions on November 28 reached a 2025-high, up 62% on the average as shoppers showed their determination to make the most of deals.”

- **Quelle:** [Nation.Cymru (PA) – 'Black Friday busiest day of the year so far for retailers, figures show'](https://nation.cymru/news/black-friday-busiest-day-of-the-year-so-far-for-retailers-figures-show/)
- **Datum der Quelle:** 2025-12-01 · **Typ:** Presse
- **Stichprobe/Methodik:** Barclays-Debit- und Barclaycard-Kreditkartentransaktionen (Barclays sieht laut eigener Mitteilung vom 11.02.2026 'nearly 40 per cent' der UK-Kartentransaktionen)
- **Einordnung/Einschränkung:** Vergleich mit einem Durchschnittstag, nicht mit dem Vorjahr, und Transaktionsvolumen statt Umsatz. Der Barclays-Originalbericht wurde nach der Neuberechnung entfernt. Die Wiedergabe bei InsightDIY (09.12.2025) nennt 'transaction volumes up 62.5 per cent in comparison to the average day in 2025'.
- **Wahrheits-Check:** *korrigiert*. PA-Wortlaut und Datum bestätigt; der genaue Wert 62,5 % stammt aus der InsightDIY-Wiedergabe. Gestrichen, weil nicht belegt: der Vergleichswert '+83,7 % am Black Friday 2024' (in keiner geprüften Quelle). Die 'knapp 40 %' auf Barclays' Formulierung 'nearly 40 per cent' (11.02.2026) korrigiert.

### (d) Black Friday 2025 – Barclays Vorab-Prognose

#### G5-31

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Barclays prognostizierte vor Black Friday 2025, dass UK-Shopper, die mitmachen, im Schnitt £430 ausgeben (zusammen über £10,2 Mrd.) und 43 % der Erwachsenen auf Schnäppchenjagd gehen.**

> “Barclays’ research indicates that Black Friday, which arrives on November 28th, will see those shopping spending an average of £430 each - £91 more than last year – amounting to a total of over £10.2 billion. Over two in five UK adults (43%) will be on the hunt for deals”

- **Quelle:** [Barclays – 'Retail set for Black Friday boost, with shoppers' average spend up by over £90'](https://home.barclays/insights/2025/11/Black-Friday-Predicted-Spend/)
- **Datum der Quelle:** 2025-11 (kein Datum auf der Seite, aus der URL abgeleitet) · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Barclays Consumer Spend research; n, Institut und Feldzeit auf der Seite nicht angegeben
- **Einordnung/Einschränkung:** Ausgabeabsicht vor dem Event, kein Ergebnis. Die gemessenen Ergebnisse (IMRG online -1,2 %, MRI-Frequenz -1,9 %, BRC November +1,4 %) passen nicht zu einem Budgetplus von £91 pro Kopf. Auf derselben Seite: 68 % zweifeln am echten Wert der Black-Friday- und Cyber-Monday-Deals.
- **Wahrheits-Check:** *bestätigt*. Zahlen, 43 % und 68 % auf der Seite bestätigt; Methodik dort nicht angegeben.

### (d) Black Friday – Start der Kaufsuche

#### G5-32

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**Laut Barclaycard Payments beginnen 60 % der Shopper ihre Suche nach Black-Friday-Angeboten bereits im Oktober.**

> “The sales event is now more of a marathon than a sprint, with 60 per cent of shoppers starting their search as early as October”

- **Quelle:** [Barclays – 'Retail set for Black Friday boost …' (Zitat Harshna Cayley, Barclaycard Payments)](https://home.barclays/insights/2025/11/Black-Friday-Predicted-Spend/)
- **Datum der Quelle:** 2025-11 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** nicht angegeben
- **Einordnung/Einschränkung:** Aussage aus einem Managerzitat ohne Methodik. Stützt den Start der Ads ab Oktober und passt zu IMRG (G5-34: Kampagnen starten früher).
- **Wahrheits-Check:** *bestätigt*. Zitat auf der Seite gefunden.

### (d) Black Friday/Cyber Weekend 2025 – IMRG Online-Umsatz

#### G5-33

✅ BELEGT · Angle: Markt

**Laut IMRG Online Retail Index sank der UK-Online-Umsatz in der 8-tägigen Black-Friday-Woche (24.11.–01.12.2025) um 1,2 % ggü. Vorjahr. Black Friday lag bei +1,3 %, Cyber Monday bei -3,2 %.**

> “Across the 8-day Black Friday week (Mon 24th Nov-Mon 1st Dec), total market revenue was down -1.2% Year-on-Year … Black Friday itself was up +1.3% YoY, but the standout performer was Tuesday which was up +4.4% YoY. Interestingly, Cyber Monday was down -3.2% YoY”

- **Quelle:** [IMRG – 'Black Friday 2025: The data and insights are in!'](https://www.imrg.org/blog/black-friday-2025-the-data-and-insights-are-in/)
- **Datum der Quelle:** 2025-12-22 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** IMRG Online Retail Index / Black Friday Tracker, Händlerpanel (laut IMRG 278 Händler)
- **Einordnung/Einschränkung:** Etablierter UK-Online-Index, aber nur Panelhändler und nominal. Adobe meldet für den Cyber Weekend £3,8 Mrd. online (G5-35); Messbasis und Zeitfenster unterscheiden sich, also die Werte nicht mischen. Bekleidung -7,3 %, Health & Beauty +8,9 %.
- **Wahrheits-Check:** *korrigiert*. Wortlaut, Datum (22/12/25) und Kategoriezahlen bestätigt. Gestrichen: Adobes angebliche '+4,6 %' für den Cyber Weekend, weil nicht selbst geprüft.

### (d) Black Friday 2025 – Kampagnenstart der Händler (IMRG)

#### G5-34

✅ BELEGT · Angle: Markt, D Geschenk

**Im IMRG-Panel starteten 60 % der Händler ihre Black-Friday-Kampagne 2025 früher als 2024. 58 Händler hatten schon am ersten Werktag im November eine Kampagne live (2021: 12).**

> “From our panel of 278 retailers, we have noted that each year more and more retailers have a live Black Friday campaign running on the 1st working day of November. From 12 retailers in 2021, to 41 in 2023, and 58 and 2025. 60% of retailers launched their campaign earlier this year compared to 2024”

- **Quelle:** [IMRG – 'Black Friday 2025: The data and insights are in!'](https://www.imrg.org/blog/black-friday-2025-the-data-and-insights-are-in/)
- **Datum der Quelle:** 2025-12-22 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Panel von 278 Händlern (IMRG Black Friday Tracker)
- **Einordnung/Einschränkung:** Gilt nur für das IMRG-Panel. Der Tippfehler 'and 2025' steht so im Original. Laut der Agentur Genie Goals im selben Beitrag brachten Rabatte Ende Oktober '30% lower CPCs'; das ist eine Einzelquelle und nicht verallgemeinerbar.
- **Wahrheits-Check:** *bestätigt*. Wortlaut und CPC-Aussage selbst gefunden.

### (d) Black Friday/Cyber Weekend 2025 – Adobe (Online)

#### G5-35

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Adobe-Daten war Black Friday 2025 mit £1,16 Mrd. der umsatzstärkste UK-Online-Tag des Jahres. Der Cyber Weekend brachte £3,8 Mrd. online, der Boxing Day mehr als £500 Mio.**

> “Adobe said Black Friday was the biggest online shopping day of the year, with £1.16 billion spent. Cyber Weekend delivered £3.8 billion in online spend, it said. Adobe also reported that Boxing Day passed £500 million.”

- **Quelle:** [IT Brief UK – 'Mobile & AI power record UK online Christmas sales' (Adobe Digital Insights)](https://itbrief.co.uk/story/mobile-ai-power-record-uk-online-christmas-sales)
- **Datum der Quelle:** 2026-01-20 · **Typ:** Presse
- **Stichprobe/Methodik:** Adobe Digital Insights; Methodik im Artikel nicht beschrieben
- **Einordnung/Einschränkung:** Die Adobe-Originalseite (business.adobe.com/uk/blog/uk-online-retail-spending-hits-record-high) lieferte 503 bzw. brach ab, daher nur über die Fachpresse belegt. Adobe misst nur Online-Umsatz auf Händlerseiten, die Adobe nutzen. Wachstumsrate für den Cyber Weekend nicht angegeben.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Datum bei IT Brief bestätigt; Adobe-Original nicht abrufbar (WebFetch 503, curl ohne Antwort). Gestrichen: Vorab-Prognose '£1,19 Mrd.', weil nicht selbst geprüft.

### (d) Online-Weihnachtssaison 2025 gesamt – Adobe

#### G5-36

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Adobe gaben UK-Verbraucher im November und Dezember 2025 online £26,9 Mrd. aus, 4,1 % mehr als im Vorjahreszeitraum; 61,5 % davon entfielen auf Mobilgeräte.**

> “The data shows UK consumers spent £26.9 billion online during November and December 2025. That figure rose 4.1% from the same period in 2024. … Adobe said mobile made up 61.5% of total online spend during the period.”

- **Quelle:** [IT Brief UK – 'Mobile & AI power record UK online Christmas sales' (Adobe Digital Insights)](https://itbrief.co.uk/story/mobile-ai-power-record-uk-online-christmas-sales)
- **Datum der Quelle:** 2026-01-20 · **Typ:** Presse
- **Stichprobe/Methodik:** Adobe Digital Insights
- **Einordnung/Einschränkung:** Sekundärquelle. Der Ergebniswert ist identisch mit Adobes Vorab-Prognose (Blogtitel laut Suchtreffer: 'UK shoppers expected to splash record £26.9 billion online during 2025 holiday season'), deshalb am Adobe-Original prüfen, das nicht abrufbar war. Nominale Werte. Der Mobilanteil spricht für Mobile-first-Creatives.
- **Wahrheits-Check:** *korrigiert*. Wortlaut einschließlich Mobilanteil bestätigt. Gestrichen: die nicht geprüfte Inflationsangabe '~3,5 %'.

### (d) Black Friday 2025 – BRC-KPMG November

#### G5-37

✅ BELEGT · Angle: Markt, D Geschenk

**Laut BRC-KPMG stiegen die UK-Einzelhandelsumsätze im November 2025, dem Black-Friday-Monat, nur um 1,4 %, das schwächste Wachstum seit sechs Monaten. Homeware und Polstermöbel verkauften sich vor den Festtagen gut, und der Online-Anteil bei Non-Food erreichte mit 44 % den höchsten Stand seit 2022.**

> “Pre-Budget jitters among shoppers meant the month of Black Friday did not deliver as strongly as retailers had hoped or the economy needed. Sales growth was the weakest in six months … Many consumers took advantage of promotions, with homeware and upholstery selling well ahead of festive hosting. … In November, total sales increased by 1.4% YoY … Non-Food online penetration hitting a high of 44%.”

- **Quelle:** [British Retail Consortium – Retail Sales Monitor November: 'Pre-Budget jitters dampen Black Friday sales'](https://brc.org.uk/market-intelligence/publications/monitors/retail-sales-monitor/2025/nov/)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG-Händlerpanel, November 2025
- **Einordnung/Einschränkung:** Etablierter Branchenmonitor; die Zusammenfassung ist öffentlich. 'Homeware' ist kein Bettwaren-Wert, nur ein Indiz für die Kategorie. Laut Text war der Online-Anteil 'its highest level since 2022', also kein Allzeithoch. Non-Food insgesamt +0,1 %, stationär -0,3 %, online +0,5 %.
- **Wahrheits-Check:** *korrigiert*. Per curl abgerufen (WebFetch 403; Inhalt trotz Status 403 geliefert). Datum 09.12.2025 und Wortlaut bestätigt. '44 %' als 'höchster Stand seit 2022' präzisiert, Non-Food-Werte ergänzt.

### (d) Black Friday 2025 – Passantenfrequenz (MRI Software)

#### G5-38

✅ BELEGT · Angle: Markt

**Laut MRI Software lag die Passantenfrequenz in UK-Einkaufslagen am Black Friday 2025 1,9 % unter dem Vorjahr, in der Black-Friday-Woche 2,2 % (Variante Mo–So: 2,5 %). Gegenüber der Vorwoche stieg die Frequenz am Black Friday um 11,7 % und in der ganzen Woche um 6,7 %.**

> “Retail footfall on Black Friday also remained -1.9% lower compared to Black Friday last year with shopping centres (-3.6%), once again, leading the decline, followed by high streets (-2%) and retail parks (-0.1%).”

- **Quelle:** [InsightDIY – 'Black Friday Week Delivered Solid Boost Across Retail Destinations' (MRI Software)](https://www.insightdiy.co.uk/news/black-friday-week-delivered-solid-boost-across-retail-destinations/15850.htm)
- **Datum der Quelle:** 2025-12-01 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** MRI-Software-Frequenzzählung in UK-Einkaufslagen
- **Einordnung/Einschränkung:** Misst Besucher, nicht Umsatz, und nur den stationären Handel. Ein Fachmedium gibt die MRI-Mitteilung wieder. Der Artikel enthält zwei Wochenabgrenzungen (So–Sa und Mo–So) mit fehlerhaften Datumsangaben.
- **Wahrheits-Check:** *korrigiert*. Korrigiert: Die +6,7 % sind der Wochenanstieg ggü. der Vorwoche (So–Sa), nicht der Black-Friday-Wert. Der Tag selbst lag bei +11,7 % ggü. Vorwoche. -1,9 % ggü. Vorjahr bestätigt.

### (d) Black Friday 2025 – amtliche Einzelhandelsstatistik (ONS)

#### G5-39

✅ BELEGT · Angle: Markt

**Laut ONS stiegen die nicht saisonbereinigten Einzelhandelsmengen in Großbritannien im November 2025 um 11,9 % ggü. Vormonat. Saisonbereinigt fielen sie um 0,1 %; der Black-Friday-Effekt war also etwas schwächer als üblich.**

> “sales volumes rose by 11.9% over the month to November 2025 … Seasonally adjusted volumes fell by just 0.1% over the month, suggesting the Black Friday effect was slightly weaker than usual.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: November 2025](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/november2025)
- **Datum der Quelle:** 2025-12-19 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** ONS Monthly Business Survey; Berichtszeitraum 2.–29. November 2025
- **Einordnung/Einschränkung:** Amtliche Statistik, gilt nur für Großbritannien (ohne Nordirland). Non-Food-Geschäfte +1,0 % ggü. Vormonat.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Datum, Zeitraum und Geografie bestätigt.

### (d) Black Friday 2025 – Teilnahmeabsicht (ONS-Umfrage)

#### G5-40

✅ BELEGT · Angle: Markt

**Laut ONS-Bevölkerungsumfrage planten rund 31 % der Erwachsenen in Großbritannien, bei den Black-Friday-Sales 2025 einzukaufen. 19 % wollten weniger einkaufen als im Vorjahr, 10 % mehr.**

> “around 3 in 10 adults (31%) planned to shop in the Black Friday sales; 19% reported that they intended to shop less than last year, while 10% intended to shop more.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: November 2025](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/november2025)
- **Datum der Quelle:** 2025-12-19 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** ONS Opinions and Lifestyle Survey, Erwachsene in Großbritannien; n hier nicht angegeben
- **Einordnung/Einschränkung:** Amtliche, unabhängige Umfrage; misst Absicht, nicht Verhalten. Deutlich niedriger als Anbieter-Umfragen (Barclays 43 %). Für realistische Erwartungen vorzuziehen.
- **Wahrheits-Check:** *bestätigt*. Wortlaut im Bulletin gefunden.

### (d) Black Friday 2026 – Cyber-Monday-Absicht (Salsify)

#### G5-41

⚠️ EINGESCHRÄNKT · Angle: Markt

**Laut Salsify-Umfrage (April 2026) planen 50 % der UK-Befragten, am Cyber Monday 2026 einzukaufen (USA 75 %, Kanada 58 %).**

> “Enthusiasm for Cyber Monday is highest in the U.S. (75%), followed by Canada (58%) and the U.K. (50%).”

- **Quelle:** [Salsify – 'Consumer Spending Trends: How Much Will Holiday Shoppers Spend in 2026?'](https://www.salsify.com/blog/consumer-spending-trends-holiday-spending-predictions)
- **Datum der Quelle:** 2026-04-30 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** 400 UK-Befragte (insgesamt 1.212 in USA, UK und Kanada); Institut und Feldzeit nicht angegeben
- **Einordnung/Einschränkung:** Kleine Anbieter-Stichprobe, früh im Jahr erhoben. Wirkt hoch im Vergleich zur ONS-Absicht für Black Friday 2025 (31 %). 'Enthusiasm' ist nicht klar als Kaufabsicht definiert.
- **Wahrheits-Check:** *bestätigt*. Satz wörtlich bestätigt.

### (d) Barclays-Kartendaten Nov./Dez. 2025 – neu berechnete Werte

#### G5-42

✅ BELEGT · Angle: Markt

**Nach Barclays' Neuberechnung stiegen die UK-Kartenausgaben ggü. Vorjahr im November 2025 um 0,6 % (Einzelhandel +0,8 %) und im Dezember 2025 um 0,3 % (Einzelhandel +0,2 %).**

> “We have updated our Consumer Spend data set and as such have restated our June-December 2025 figures, and removed the historical reports. … Overall 0.6% [Nov] 0.3% [Dec] … Retail 0.8% [Nov] 0.2% [Dec]”

- **Quelle:** [Barclays – 'Barclays Consumer Spend Data – June-December 2025'](https://home.barclays/news/press-releases/20260/02/barclays-consumer-spend-data---june-december-2025/)
- **Datum der Quelle:** 2026-02 (kein Datum auf der Seite, aus der URL abgeleitet) · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Barclays-Debit- und Barclaycard-Kreditkartentransaktionen
- **Einordnung/Einschränkung:** Aktueller Stand des Herausgebers; die Monatsangaben in eckigen Klammern sind aus der Tabelle ergänzt. Die Januar-Mitteilung vom 11.02.2026 nennt für Dezember im Einzelhandel ebenfalls 0,2 %. Ersetzt die ursprünglich berichteten -1,1 % (Nov.) und -1,7 % (Dez.). Kategorien wie Möbel enthält die neue Tabelle nicht.
- **Wahrheits-Check:** *bestätigt*. Hinweis zur Neuberechnung und Tabellenwerte bestätigt (Online: Nov. 2,3 %, Dez. 1,0 %). Dezemberwert im Einzelhandel in der Mitteilung vom 11.02.2026 gegengeprüft.

### (e) Dezember 2025 – überholte Barclays-Zahl (Mythos-Check)

#### G5-43

❌ NICHT BELEGT / MYTHOS · Angle: Markt

**Die viel zitierte Aussage, die UK-Kartenausgaben seien laut Barclays im Dezember 2025 um 1,7 % gefallen (stärkster Rückgang seit Februar 2021), ist durch Barclays' Neuberechnung (+0,3 %) überholt.**

> “Barclays said overall consumer card spending fell by 1.7% in December from the same month in 2024, the biggest such drop since the 12 months to February 2021, during the COVID pandemic.”

- **Quelle:** [ESM Magazine (Reuters) – 'UK Consumers Cut Spending In December By Most Since 2021, Barclays Says'](https://www.esmmagazine.com/retail/uk-consumers-cut-spending-in-december-by-most-since-2021-barclays-says-303995)
- **Datum der Quelle:** 2026-01-15 · **Typ:** Presse
- **Stichprobe/Methodik:** Barclays-Kartentransaktionen
- **Einordnung/Einschränkung:** Die Zahl wurde damals so berichtet. Barclays hat die Werte für Juni–Dezember 2025 neu berechnet und die alten Berichte entfernt (G5-42: Dezember +0,3 %). Dasselbe gilt für die ursprüngliche November-Angabe: 'Consumer card spending declined -1.1 per cent year-on-year in November', laut InsightDIY vom 09.12.2025, inzwischen +0,6 %. Nicht mehr verwenden.
- **Wahrheits-Check:** *bestätigt*. Reuters-Wortlaut (15.01.2026) und alte November-Zahl (InsightDIY) selbst gefunden. Neuberechnung auf der Barclays-Seite bestätigt; die Aussage ist überholt.

### (e) Weihnachten/Boxing Day 2025 – BRC-KPMG Dezember

#### G5-44

✅ BELEGT · Angle: Markt, D Geschenk

**Laut BRC-KPMG stiegen die UK-Einzelhandelsumsätze im Dezember 2025 nur um 1,2 % (Non-Food -0,3 %). Erst die letzte Woche mit Boxing Day und Beginn der Januar-Sales brachte deutliches Wachstum.**

> “UK Total retail sales increased by 1.2% year on year in December, against a growth of 3.2% in December 2024. … Many people were clearly holding out for discounts, with the last week showing significant growth off the back of Boxing Day and beginning of the January sales.”

- **Quelle:** [British Retail Consortium – 'Drab Christmas as consumers wait for sales' (BRC-KPMG Retail Sales Monitor December 2025)](https://brc.org.uk/news-and-events/news/corporate-affairs/2026/ungated/drab-christmas-as-consumers-wait-for-sales/)
- **Datum der Quelle:** 2026-01-13 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG-Händlerpanel, Dezember 2025
- **Einordnung/Einschränkung:** Etablierter Monitor, nominale Werte. Geschenkartikel liefen laut BRC 'worse than expected'. Online-Non-Food -0,1 %, Online-Anteil 38,6 %.
- **Wahrheits-Check:** *bestätigt*. Alle Werte und Zitate auf der Seite bestätigt.

### (e) Boxing Day 2025 – Passantenfrequenz (MRI Software)

#### G5-45

✅ BELEGT · Angle: Markt

**Laut MRI Software lag die Passantenfrequenz in UK-Einkaufslagen am Boxing Day 2025 4,4 % über dem Vorjahr, das stärkste Plus seit über zehn Jahren; Retail Parks lagen bei +8,8 %.**

> “Despite a slow start for high streets and shopping centres, Boxing Day proved to be a bumper day for all UK retail destinations with footfall up 4.4% year on year across the board; the strongest increase seen in over 10 years.”

- **Quelle:** [InsightDIY – 'MRI Software: Strong Boxing Day Footfall Performance' (Zitat Jenni Matthews, MRI Software)](https://www.insightdiy.co.uk/news/mri-software-strong-boxing-day-footfall-performance/15935.htm)
- **Datum der Quelle:** 2025-12-26 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** MRI-Software-Frequenzzählung in UK-Einkaufslagen
- **Einordnung/Einschränkung:** Misst Besucher, nicht Umsatz. Der Zuwachs lag vor allem zwischen 17 und 23 Uhr (+9,6 %); laut MRI dürften Freizeit und Gastronomie profitiert haben. Für Online-Ads nur Kontext.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, +8,8 % und +9,6 % bestätigt.

### (e) Boxing Day 2025 – Barclays-Prognose (kein Ergebnis)

#### G5-46

⚠️ EINGESCHRÄNKT · Angle: Markt

**Barclays rechnete per Umfrage hoch, dass UK-Shopper bei den Boxing-Day-Sales 2025 £3,6 Mrd. ausgeben (im Schnitt £253, Teilnahme 26 % nach 28 % im Jahr 2024). Das ist eine Prognose, kein gemessenes Ergebnis; für 2024 waren £4,6 Mrd. prognostiziert worden.**

> “New data from the Barclays Consumer Spend report reveals that UK consumers are expecting to spend £3.6 billion in the Boxing Day sales. The average shopper has increased their budget by £17 compared to 2024, yet fewer consumers will be taking part – 26 per cent plan to spend on Boxing Day this year, down from 28 per cent in 2024.”

- **Quelle:** [Barclays – Pressemitteilung 'UK shoppers set to spend £3.6 billion in the Boxing Day sales'](https://home.barclays/news/press-releases/2025/12/uk-shoppers-set-to-spend-p3-6-billion-in-the-boxing-day-sales/)
- **Datum der Quelle:** 2025-12-26 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Opinium im Auftrag von Barclays, 2.000 Befragte je Welle, repräsentativ für UK, 21.–25. November 2025
- **Einordnung/Einschränkung:** Hochrechnung laut Fußnote: 25,8 % Teilnahme × £252,80 × 55.022.253 Erwachsene ≈ £3,59 Mrd. Medienberichte über '£3,6 Mrd. ausgegeben' verwechseln Absicht und Ergebnis. Ein gemessener Boxing-Day-Umsatz von Barclays wurde nicht gefunden. 69 % erwarten Einschränkungen wegen Kostendrucks (2024: 47 %).
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Datum, Methodik und Rechenweg per curl bestätigt; Vorjahresprognose (£4,6 Mrd.) als Kontext ergänzt.

### (e) Januar-Sales – Kaufabsichten und Kategorien (Barclays)

#### G5-47

⚠️ EINGESCHRÄNKT · Angle: Markt, B Wechseljahre, C Bettbeziehen

**Laut Barclays-Umfrage (Nov. 2025) planten 44 % der UK-Verbraucher, in den Winter-Sales einzukaufen; davon wollten 89 % in den Januar-Sales kaufen. Homeware stand bei 20 % auf der Einkaufsliste; am häufigsten genannt wurden Kleidung, Schuhe und Accessoires (37 %).**

> “Nearly half (44 per cent) say they plan to shop at some point during the Christmas sales period, and for this group, the January sales are the most popular time to shop, chosen by 89 per cent. … Food and drink (27 per cent), beauty products (20 per cent), homeware (20 per cent) and discounted Christmas items (19 per cent) ranked next.”

- **Quelle:** [Barclays – Pressemitteilung 'UK shoppers set to spend £3.6 billion in the Boxing Day sales'](https://home.barclays/news/press-releases/2025/12/uk-shoppers-set-to-spend-p3-6-billion-in-the-boxing-day-sales/)
- **Datum der Quelle:** 2025-12-26 · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Opinium im Auftrag von Barclays, 2.000 Befragte je Welle, UK-repräsentativ, 21.–25. November 2025
- **Einordnung/Einschränkung:** PR-Umfrage mit offengelegtem Institut, n und Zeitraum. Homeware ist breiter als Bettwaren. Stützt eine Eigenkauf-Phase im Januar (B/C), weniger Angle D.
- **Wahrheits-Check:** *bestätigt*. Wortlaut bestätigt; die Spitzenkategorie Kleidung (37 %) habe ich zur Einordnung ergänzt.

### (e) Januar-Sales 2026 – BRC-KPMG Januar

#### G5-48

✅ BELEGT · Angle: Markt, B Wechseljahre, C Bettbeziehen

**Laut BRC-KPMG stiegen die UK-Einzelhandelsumsätze im Januar 2026 um 2,7 %, getragen von einer starken ersten Januarwoche; Möbel gehörten zu den gut laufenden Kategorien.**

> “January sales bounced back from a subdued November and December. Total sales were up 2.7%, with a strong week one which gradually declined a little each week through the month. … Toys, Computing, Furniture and Health & Beauty all performed well, whilst Footwear continued to struggle.”

- **Quelle:** [British Retail Consortium – Retail Sales Monitor January: 'January sales boost for shoppers and retailers'](https://brc.org.uk/market-intelligence/publications/monitors/retail-sales-monitor/2026/jan/)
- **Datum der Quelle:** 2026-02-10 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** BRC-KPMG-Händlerpanel, Januar 2026
- **Einordnung/Einschränkung:** Öffentliche Zusammenfassung des Monitors. Non-Food +1,7 %, stationärer Non-Food-Handel +2,0 % (stärkstes Wachstum seit über sechs Monaten), Online-Non-Food +1,3 %. Nominal. 'Furniture' ist nur ein Proxy für Bettwaren.
- **Wahrheits-Check:** *bestätigt*. Per curl abgerufen (WebFetch 403); Datum 10.02.2026 und Wortlaut bestätigt.

### (e) Januar-Sales 2026 – Barclays-Kartendaten

#### G5-49

✅ BELEGT · Angle: Markt, B Wechseljahre, C Bettbeziehen

**Laut Barclays stiegen die UK-Kartenausgaben im Januar 2026 nur um 0,8 %. Der Online-Einzelhandel (ohne Lebensmittel) legte um 5,7 % zu, sein Anteil lag mit 59,2 % so hoch wie zuletzt im Januar 2022.**

> “Consumer card spending increased 0.8 per cent in January – considerably less than the latest CPIH inflation rate of 3.6 per cent. … Online retail spend growth (excluding groceries) reached 5.7 per cent, with online’s share of retail spending (excluding groceries) at 59.2 per cent – its highest level since January 2022”

- **Quelle:** [Barclays – Pressemitteilung 'Online retail growth reaches 5.7 per cent in January, while cinemas and streaming services soar'](https://home.barclays/news/press-releases/20260/02/online-retail-growth-reaches-5-7-per-cent-in-january--while-cine/)
- **Datum der Quelle:** 2026-02-11 · **Typ:** Marktforschung
- **Stichprobe/Methodik:** Barclays-Debit- und Barclaycard-Kreditkartentransaktionen ('nearly 40 per cent of the nation's credit and debit card transactions')
- **Einordnung/Einschränkung:** Primärquelle mit transparenter Datenbasis; nominal und unter der Inflation. Laut Tabelle Möbelgeschäfte -0,1 %, 'Household' -1,4 %. Laut Barclays hielten sich Käufer offenbar für die Januar-Sales zurück.
- **Wahrheits-Check:** *bestätigt*. Wortlaut, Datum und Tabellenwerte bestätigt.

### (e) Januar-Sales 2026 – amtliche Einzelhandelsstatistik (ONS)

#### G5-50

✅ BELEGT · Angle: Markt

**Laut ONS stiegen die Einzelhandelsmengen in Großbritannien im Januar 2026 um 1,8 % ggü. Vormonat, der größte Monatsanstieg seit Mai 2024, nach +0,4 % im Dezember 2025.**

> “Sales volumes rose by 1.8% over the month during January 2026, which was the largest monthly rise since May 2024. This followed a rise of 0.4% in December 2025.”

- **Quelle:** [Office for National Statistics – Retail sales, Great Britain: January 2026](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/january2026)
- **Datum der Quelle:** 2026-02-20 · **Typ:** Behörde/NHS/Statistikamt
- **Stichprobe/Methodik:** ONS Monthly Business Survey; Großbritannien
- **Einordnung/Einschränkung:** Amtlich, nur Großbritannien. Laut ONS kam das Wachstum teils von Kunst- und Antiquitätenverkäufen sowie Online-Juwelieren, ist also kein reiner Sales-Effekt.
- **Wahrheits-Check:** *korrigiert*. Wortlaut und Datum bestätigt. Gestrichen: den Verweis auf 'Q4 2025 -0,3 % ggü. Q3', weil im Dezember-Bulletin nicht selbst geprüft.

### (b) Lieferzusage 'bis Weihnachten' – Primärnorm Consumer Rights Act 2015

#### G5-V01

✅ BELEGT · Angle: D Geschenk

**Nach dem Consumer Rights Act 2015 (s. 28) muss ein Händler ohne vereinbarten Liefertermin 'without undue delay' und spätestens 30 Tage nach Vertragsschluss liefern. Wird ein vereinbarter Termin verfehlt, kann der Verbraucher den Vertrag beenden, wenn die rechtzeitige Lieferung nach den Umständen bei Vertragsschluss wesentlich war oder er dem Händler vorher gesagt hat, dass sie wesentlich ist.**

> “(3) Unless there is an agreed time or period, the contract is to be treated as including a term that the trader must deliver the goods— (a) without undue delay, and (b) in any event, not more than 30 days after the day on which the contract is entered into. … (6) If the circumstances are that— (a) the trader has refused to deliver the goods, (b) delivery of the goods at the agreed time or within the agreed period is essential taking into account all the relevant circumstances at the time the contract was entered into, or (c) the consumer told the trader before the contract was entered into that delivery … was essential, then the consumer may treat the contract as at an end.”

- **Quelle:** [legislation.gov.uk – Consumer Rights Act 2015, section 28 (Delivery of goods)](https://www.legislation.gov.uk/ukpga/2015/15/section/28)
- **Datum der Quelle:** 2015 (Gesetz; Fassung abgerufen am 08.10.2026) · **Typ:** Parlament/Regierung
- **Einordnung/Einschränkung:** Amtlicher Gesetzestext. Präzisiert die vereinfachte MSE-Darstellung (G5-17). Für Ads heißt das: Ein zugesagter Liefertermin vor Weihnachten kann als 'agreed time' gelten, und bei Verfehlung drohen Rücktritt und Erstattung. Keine Rechtsberatung; der räumliche Geltungsbereich wird auf der Seite nicht angezeigt.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. Seite per WebFetch und curl selbst abgerufen; Wortlaut von s. 28(3) und (6) geprüft.

### (d) Barclays-Originalbericht November 2025 (vor Neuberechnung)

#### G5-V02

⚠️ EINGESCHRÄNKT · Angle: Markt, D Geschenk

**In seinem ursprünglichen November-2025-Bericht (wiedergegeben am 09.12.2025, inzwischen zurückgezogen) meldete Barclays Kartenausgaben von -1,1 % ggü. Vorjahr, am Black Friday 62,5 % mehr Transaktionen als an einem durchschnittlichen Tag 2025 und für Möbelgeschäfte +6,8 % Ausgaben ggü. Vorjahr.**

> “Consumer card spending declined -1.1 per cent year-on-year in November – the greatest fall recorded since February 2021 (-9.5 per cent) … retailers enjoyed their busiest day of the year so far on Black Friday (28th), with transaction volumes up 62.5 per cent in comparison to the average day in 2025. … Furniture Stores 6.8% 1.2%”

- **Quelle:** [InsightDIY – 'Barclays: Card Spending Sees Greatest Fall Since 2021' (Wiedergabe des Barclays Consumer Spend Report November 2025)](https://www.insightdiy.co.uk/news/barclays-card-spending-sees-greatest-fall-since-2021/15883.htm)
- **Datum der Quelle:** 2025-12-09 · **Typ:** Presse
- **Stichprobe/Methodik:** Barclays-Debit- und Barclaycard-Kreditkartentransaktionen
- **Einordnung/Einschränkung:** Belegt ist, dass Barclays diese Werte veröffentlicht hat. Barclays hat die Daten für Juni–Dezember 2025 aber neu berechnet und die Originalberichte entfernt (G5-42: November jetzt +0,6 %). Die Möbelzahl (+6,8 %) steht in der neuen Tabelle nicht. Überholter Datenstand, nicht für Ads verwenden.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen, um die Lücke 'Barclays-Möbelzahl nicht belegt' zu klären. Artikel per WebFetch und curl abgerufen, Tabellenzeile 'Furniture Stores 6.8% 1.2%' gefunden.

### (a) Verpasste Versandtermine – Post-Office-Umfrage

#### G5-V03

⚠️ EINGESCHRÄNKT · Angle: D Geschenk

**Laut einer Post-Office-Umfrage (Okt. 2025, 2.000 UK-Erwachsene) haben 17 % der Briten schon einmal den letzten Versandtermin vor Weihnachten verpasst.**

> “Postmasters are urging the public to send early to avoid being part of the 17 per cent of Brits who’ve previously left it too late and missed the final posting date.”

- **Quelle:** [Post Office (Mynewsdesk) – 'Post Office announces last posting dates for sending Christmas presents'](https://www.mynewsdesk.com/uk/post-office/pressreleases/post-office-announces-last-posting-dates-for-sending-christmas-presents-3420939)
- **Datum der Quelle:** 2025-12-19 (Seitenkopf; Fließtext 'Wednesday 10th December') · **Typ:** Umfrage (Händler/Marke/PR)
- **Stichprobe/Methodik:** Post Office 'Hot Topics', Oktober 2025, 2.000 national repräsentative UK-Erwachsene, Stichprobe von Dynata
- **Einordnung/Einschränkung:** PR-Umfrage eines Postunternehmens mit knapper Methodik. Passt als Kontext für Angle D (früh bestellen), sollte aber nicht als harte Ad-Zahl dienen.
- **Wahrheits-Check:** *bestätigt*. Neu aufgenommen. Satz und Methodik per curl auf der Mynewsdesk-Seite gefunden.

