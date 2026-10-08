# Anhang D – UK-Wettbewerb und Betreiber-Analyse (vollständige Einzelberichte)


# D1 Betreiber & Länder (Magic Splashy, Duune, Klone)

## Magic Splashy: Operator- und Länder-Analyse (Stand 08.10.2026)

**Datenbasis:** GetHooked MCP (Shop 12609 / Brand 88310 Magic Splashy, Shop 113780 / Brand 8066940 Duune), Live-Abrufe der Shop-Seiten per curl (Produkt-JSON, Impressum/Mentions légales, Shopify-Metadaten).
**Linkformat:** Bei jeder Anzeige stehen die GetHooked-ID, der GetHooked-Share-Link und der Meta-Ad-Library-Link (`https://www.facebook.com/ads/library/?id=<external_id>`).

---

### TL;DR

1. **Länder:** Magic Splashy schaltet **nur in Deutschland und Österreich**. 168 Anzeigen haben DE/AT-Geo-Daten, 16 haben gar keine Geo-Daten und 0 Anzeigen laufen in CH, GB, IE, NL, BE, FR, IT, ES, PL oder LU. Die Besucher kommen zu 95,9 % aus DE, zu 1,9 % aus AT und zu 1,7 % aus CH. `magicsplashy.ch` leitet auf `magicsplashy.de` weiter (eigener Shopify-Datensatz 12547, aber 0 Anzeigen und 0 Traffic). Die Karte „Targeted Countries“ von GetHooked ist leer: Die Reichweite ließ sich nicht zuordnen, 158 Anzeigen sind „unranked“.
2. **Duune (FR) ist wahrscheinlich derselbe Operator oder ein direkter Ableger. Die Evidenz ist mittel bis stark, aber nicht bewiesen.**
   - Hartes Indiz: Die Duune-Anzeige **136611698** (FR, gestartet am 09.06.2026, also am ersten Duune-Tag) trägt die Wortmarke **„MagicSplashy.“** im Creative. GetHooked ordnet die Duune-Page deshalb dem Shop magicsplashy.de als zweite verlinkte Page zu.
   - Die Anzeigentexte und PDP-Claims sind **1:1-Übersetzungen** von Magic Splashy (Body-Copy, „17.000“, SoftCloud® 49,99 €, 40 Nächte, ThermoBalance®).
   - Dagegen spricht: Der Rechtsträger ist ein anderer („Duune LLC“ mit Gmail-Adresse statt M&B Brands GmbH). Duune läuft auf einer eigenen Shopify-Instanz (`8va5jk-pw` statt `invictusgadgets`) mit einem anderen Theme (Horizon statt Dawn/SJ Adlox), mit anderen Farbnamen, Größen und Preisen (79,90–129,90 € statt 124,99–169,99 €).
   - Wichtig: SoftCloud, ThermoBalance, 40 Nächte und 49,99 € verwenden **auch die Copycats** Lunex (FR/BE), Cozily (UK) und Kallyon (UK). Diese Namen beweisen also nichts.
3. **Duune ist klein:** 118 aktive Anzeigen (87 Image, 31 Video), alle auf einer PDP. Die EU-Reichweite liegt insgesamt bei etwa 0,81 Mio., 68 % davon stammen aus 5 Anzeigen von Juni/Juli. Die aktiven Anzeigen sinken (Aug 269 → Sep 210 → Okt 118). Der Traffic liegt bei etwa 1,4 Tsd./Monat, bei Magic Splashy sind es 307,7 Tsd. Duune ist ein FR-Testmarkt, der nicht skaliert.
4. **Weitere Länder-Stores desselben Operators:** keine gefunden. Die Domains `.at/.com/.co.uk/.uk/.nl/.it/.es/.pl/.fr/.be` lösen nicht auf und haben 0 Advertiser. Es gibt keine weiteren Brands mit dem Namen „MagicSplashy“. Für „ThermoBalance“ gibt es 0 Treffer in Anzeigentexten.
5. **UK:** **Weder Magic Splashy noch Duune sind im UK präsent** (keine Anzeigen, keine Domain, keine Page). ABER: Die EasySleep-Idee ist im UK bereits von **drei Klonen** besetzt.
   - **Cozily** (552 aktive Anzeigen, Rechtsträger aus Guangzhou)
   - **Pleene** (137, inzwischen „EasyRest“)
   - neu: **Kallyon** (kallyon.com, GBP/GB, 52 aktive Anzeigen seit 09.08.2026). Kallyons PDP ist eine **wörtliche englische Übersetzung der Magic-Splashy-PDP**: „Coastal Blue“ = Küstenblau, „Fireside Red“ = Kaminrot, „Sunset Glow“ = Abendsonne, „Moonstone Grey“ = Mondstein Grau, dazu „No sweating, no freezing“, „Over 17,000 happy sleepers“, „worth £49.99“ und „40-night trial“.

   Die MS-Copy ist im UK also schon teilweise im Umlauf, allerdings mit schwacher Performance (Performance-Scores 16–58).

---

### 1) In welchen Ländern ist Magic Splashy aktiv?

| Quelle | Ergebnis |
|---|---|
| `get_shop_targeted_countries(12609, window=180)` | `targeted_countries: []`, `reach_coverage: unavailable`, 158 Anzeigen „unranked“, 1 ungültige Zeile. Daraus lässt sich nichts ablesen. |
| Geo-Filter auf Brand 88310 | **DE/AT: 168 Anzeigen** (Index inkl. gespeicherter Anzeigen), 16 ohne Geo-Daten. **0 Treffer** für CH, GB, IE, NL, BE, FR, IT, ES, PL und LU |
| Stichprobe der Top-21-Anzeigen (nach Impressions) | Alle mit `countries: ["AT","DE"]` oder leer, Sprache durchgehend `de` |
| Besucherländer (Shop 12609) | DE 95,92 %, AT 1,86 %, CH 1,67 %, ES 0,55 % |
| Domains | `magicsplashy.de` (Hauptshop, Shopify-Handle `invictusgadgets.myshopify.com`, Theme „Copy of SJ Adlox“/Dawn 12). `magicsplashy.ch` leitet auf .de um (GetHooked-Shop 12547: gleiches Logo, gleiche 5 Produkte, 0 Anzeigen „verified_empty“, 0 Traffic). |
| Rechtsträger | Impressum: „Handelsname: Magic Splashy … M&B Brands GmbH, Rathausstraße 2, 59555 Lippstadt … USt-IdNr.: DE360442448“ |
| Größe | 146 aktive Anzeigen (Brand-Zähler), 158 aktive Anzeigen in der Shop-Publikation (157 MagicSplashy-Page + 1 Duune-Page). Formate (Inzidenzen): Image 90, Video 50, DCO 37. Traffic 307.734 Besuche/Monat (Aug). Aktive Anzeigen pro Monat: Jun 220, Jul 277, **Aug 530**, Sep 358, Okt 146. |
| Landingpages (158 Anzeigen) | `/products/easysleep-ganzjahresdecke` 85, `/products/easysleep-decke` 50, `/products/magicsleep` 9, `/pages/frauen-magazin` 6 (Advertorial), `/pages/schlafen-im-sommer` 3, `/pages/gut-schlafen` 2, `/pages/umfrage` 1, `/pages/gesund-schlafen` 1, **duune.co-PDP 1** (die Duune-Page-Anzeige) |

**Ergebnis:** Magic Splashy ist ein **reiner DACH-Player mit Fokus DE und AT**. Die Schweiz wird über die Umleitung von .ch auf .de mitbedient, dort laufen aber keine eigenen Anzeigen. Die Schweiz liegt außerhalb der EU, deshalb sind CH-Anzeigen in GetHooked ohnehin schwer sichtbar.

Referenz-Anzeigen von Magic Splashy (zum Vergleich mit Duune):
- **129130363**, Video, Reichweite 1.610.672, seit 28.07., Titel „Nie wieder Bettwäsche wechseln 🛏️“. [GetHooked](https://app.gethookd.ai/share/ad/129130363?signature=2280883cdc1b06d68811f8455bca14dbebe3878407f4246090cb2afb6c5c467c), [Meta](https://www.facebook.com/ads/library/?id=1534211127599850)
- **126012757**, Video, Reichweite 1.315.088, Overlay „DAS WARS MIT BETTWÄSCHE WECHSELN!“ und „Ich hab die EasySleep Decke bestellt“. [GetHooked](https://app.gethookd.ai/share/ad/126012757?signature=4aa5cf75157a813c3daede61927240a452d4bf09046a0feee9ae288bd457658f), [Meta](https://www.facebook.com/ads/library/?id=1572451867734657)
- **125662052**, Video, Reichweite 1.343.347, Overlay „Nie wieder Bettbeziehen ❌“. [GetHooked](https://app.gethookd.ai/share/ad/125662052?signature=afca98f12b6dd400226ecbd2adcf32983adb04f2c06b179d502bd583a5f9a763), [Meta](https://www.facebook.com/ads/library/?id=2025964218008688)
- **112079858**, Image, Reichweite 1.101.845, **seit 21.03.2026**, „Nie wieder Bettwäsche wechseln. Decke + Bezug in EINEM.“ [GetHooked](https://app.gethookd.ai/share/ad/112079858?signature=d437bb1ca539176a632abb07f1c15432d04d11076276d79c6ca87de68d650db6), [Meta](https://www.facebook.com/ads/library/?id=1254640556806331)
- **112080336**, Image, seit 21.03.2026, „Nur noch 115 Stück unserer Variante Moon Stone verfügbar“. [GetHooked](https://app.gethookd.ai/share/ad/112080336?signature=8fad5c898a6a1514587b8c34f0cfb4e076a5c68a62d07ada19fb0a815bfb5f0e), [Meta](https://www.facebook.com/ads/library/?id=1264128265103506)
- **112081097**, Image, seit 18.06.2026, „+ GRATIS SOFTCLOUD KISSENBEZÜGE 😴“. [GetHooked](https://app.gethookd.ai/share/ad/112081097?signature=7afad60873a9d80dd51a5ce53ba5079e610a41023c079d462642d837f1b5630c), [Meta](https://www.facebook.com/ads/library/?id=1320942376832595)
- **181378999**, Image, seit 21.09.2026, „NUR HEUTE MIT GRATIS SOFTCLOUD KISSENBEZÜGE“. [GetHooked](https://app.gethookd.ai/share/ad/181378999?signature=755bac2d31d3bce402c0f3b1af6e816ca20077f3b7f42ba442f270cb80df9fcf), [Meta](https://www.facebook.com/ads/library/?id=1970650280282633)
- **200300928**, Video, seit 06.10.2026, Untertitel „Thermobalance-Klimafasern geschlafen hast,“. [GetHooked](https://app.gethookd.ai/share/ad/200300928?signature=a076a8051dcf61f06c68769dd07fa3bb8df5a95477881c1c99fe6e44e9a68334), [Meta](https://www.facebook.com/ads/library/?id=2574004779737289)

Standard-Body von Magic Splashy (wörtlich, z. B. 125662052): „Decke + Bezug in einem 🌙 / Die EasySleep Bettdecke macht Bettmachen endlich einfach. Waschen, trocknen und wieder aufs Bett legen. / ✓ Nie wieder Ärger mit Überzügen ✓ Angenehm kühl im Sommer, wohlig warm im Winter ✓ Hypoallergen und antibakteriell / Heute 2 SoftCloud Kissenbezüge gratis (49,99€ Wert) sichern. / 40 Tage risikofrei probeschlafen. / Genieße endlich ein Bett, das immer frisch ist.“

---

### 2) Duune (duune.co, FR): derselbe Operator?

#### 2a) Evidenz-Matrix

| # | Indiz | Richtung | Stärke |
|---|---|---|---|
| 1 | **Duune-Anzeige 136611698 (FR, Start 09.06.2026) zeigt die Wortmarke „MagicSplashy.“** unter „UNIQUEMENT AUJOURD'HUI : 2 TAIES D'OREILLER OFFERTES.“ Eine deutsche Vorlage mit genau diesem Layout ist im indexierten MS-Bestand vor diesem Datum nicht zu finden (die MS-Versionen „NUR HEUTE …“ starten erst am 18.06. bzw. 21.09.). [GetHooked](https://app.gethookd.ai/share/ad/136611698?signature=aa88737f74687274d51a3816d70c6d439ce3e0b7ae3afd35db50df0ad231279d), [Meta](https://www.facebook.com/ads/library/?id=2143387197057841) | gleicher Operator | **stark** (einziger „harter“ Beleg; ein Copycat könnte das Asset aber gestohlen haben) |
| 2 | GetHooked `get_shop_linked_pages(12609)` listet **2 Pages**: MagicSplashy (157 Anzeigen) und **Duune (1 Anzeige)**. `get_shop_advertisers` bestätigt das. Die Landingpage-Liste von magicsplashy.de enthält die duune.co-PDP mit 1 Anzeige. | gleicher Operator | mittel (abgeleitet aus Indiz 1, also nicht unabhängig) |
| 3 | Der Duune-Body ist eine **wörtliche FR-Übersetzung** des MS-Bodys: „🌙 Couette + housse en un seul produit / La couette EasySleep simplifie enfin votre quotidien. Lavez-la, laissez-la sécher, puis remettez-la directement sur votre lit. / ✓ Fini les contraintes des housses de couette ✓ Agréablement fraîche en été, confortablement chaude en hiver ✓ Hypoallergénique et antibactérienne / Recevez aujourd'hui 2 taies d'oreiller SoftCloud offertes (valeur de 49,99 €). / Essayez-la pendant 40 nuits sans risque. / Profitez enfin d'un lit toujours propre, frais et prêt à vous accueillir.“ | neutral bis Pro | schwach (Kallyon im UK macht dasselbe auf Englisch) |
| 4 | PDP-Claims: „17 000 clients dorment déjà plus sereinement avec EasySleep“ (MS: „17.000 Kunden schlafen bereits entspannter mit EasySleep“), SoftCloud® 51×76 cm, ThermoBalance®, „40 nuits d'essai“, 49,99 €. | neutral | schwach (Lunex FR, Cozily UK und Kallyon UK nutzen dieselben Bausteine) |
| 5 | Creative-Konzepte als Übersetzung: „NE CHANGEZ PLUS JAMAIS VOTRE LINGE DE LIT. Couette + housse en un seul produit.“ entspricht MS „Nie wieder Bettwäsche wechseln. Decke + Bezug in EINEM.“ (MS seit 21.03.). „J'ai commandé“-UGC entspricht MS „Ich hab die EasySleep Decke bestellt“. Die Duune-Videos zeigen **andere Darsteller**, sind also lokal neu produziert und keine Re-Uploads. | leicht Pro | schwach bis mittel (Eigenproduktion = Investment; Copycats nutzen aber auch Stock- oder AI-UGC) |
| 6 | Rechtsträger: „Le site duune.co est édité par : **Duune LLC** – Email : duune.contact@gmail.com“, MS dagegen: „M&B Brands GmbH, Lippstadt, DE360442448“. Keine Cross-Links oder Textreste der jeweils anderen Marke auf Policies und PDP. | contra | mittel (US-LLC plus Gmail ist im FR-Dropshipping Standard, z. B. Lunex „VALLEY LLC“, Kallyon „Garzette LLC“) |
| 7 | Technik: Duune nutzt `8va5jk-pw.myshopify.com`, Theme „Couette_20/08_HomeV2“ (Horizon 3.4.0), keine Pixel erkannt. MS nutzt `invictusgadgets.myshopify.com`, „Copy of SJ Adlox“ (Dawn 12). Gemeinsame Apps: Klaviyo, Loox, Shop Pay, Kaching Bundles (Standard-Stack). | contra | schwach bis mittel |
| 8 | Sortiment und Preise: Duune hat 8 generische Farben (Bleu, Beige, Gris, Noir, Orange, Vert, Rouge, Lavande), 3 Größen (135×200 / 200×200 / 230×230) und **79,90–129,90 €**. MS hat 8 Fantasienamen (Küstenblau, Kaminrot, Fliedertraum, Abendsonne, Sanftes Mintgrün, Creme Beige, Mitternacht Schwarz, Mondstein Grau), 5 Größen und **124,99–169,99 €**. Die Farbpalette ist identisch, die Benennung nicht. | leicht contra | schwach |
| 9 | Timing: Die Duune-PDP wurde am 09.06.2026 um 01:05 angelegt, die erste Duune-Anzeige startete am 08.06. Das war direkt nachdem MS im Mai/Juni hochskalierte (Traffic Mai 75 Tsd. → Jun 267 Tsd.). | neutral | – |

**Urteil:** **Wahrscheinlich derselbe Operator oder ein eng verbundener FR-Ableger (Evidenz mittel bis stark, nicht bewiesen).** Ein MagicSplashy-gebrandetes, aber französischsprachiges Creative vom ersten Tag gibt es weder bei Lunex noch bei Cozily, Pleene oder Kallyon. Es deutet auf Zugriff auf interne MS-Templates hin (Operator, gemeinsame Agentur oder Freelancer). Formal laufen beide Shops unter verschiedenen Rechtsträgern und auf getrennten Shopify-Instanzen. Für die UK-Strategie ist das zweitrangig: **Duune zeigt, wie MS einen Markt lokalisiert** (1:1-Copy-Übersetzung, neue lokale UGC, niedrigerer Einstiegspreis, Saison- und Popkultur-Statics).

#### 2b) Größe von Duune

- **Aktive Anzeigen:** 118 (Brand-Zähler und Domain-Roster). Die Shop-Publikation zählt 122 (inkl. 6 Anzeigen auf `/products/masseur-3-en-1`, also ein zweites Produkt im Test).
- **Formate:** Image 87, Video 31. Keine DCO, keine Carousels.
- **Landingpage:** Fast alles geht auf `duune.co/products/easysleep®-la-couette-2-en-1-a-sechage-rapide-qui-remplace-vos-draps` (116 von 122). Es gibt keine Advertorial-, Quiz- oder Listicle-Seiten, im Gegensatz zu MS mit `/pages/frauen-magazin` und `/pages/umfrage`.
- **Länder:** FR. Ab dem Batch vom 28.08. kommt zusätzlich **LU** dazu (FR+LU). Kein BE, kein CH. Die Besucher kommen zu 100 % aus FR.
- **Traffic:** 1.366 Besuche/Monat (Aug). Vorher wurde kein Traffic gemessen.
- **Gesamte EU-Reichweite:** ca. 809.600 (116 Anzeigen mit Daten). Die Top 5 bringen 552.800 (68 %), alle gestartet im Juni/Juli. Die Spend-Buckets der Top-Anzeigen liegen bei 501–2.000 $, der Rest bei 0–500 $.
- **Launch-Kadenz (Startmonat der heute aktiven Anzeigen):** Jun 28, Jul 21, **Aug 43**, Sep 10 (alle 25.–27.09.), Okt 16 (1.–7.10., davon 14 am 06.10.). Es wird in Batches gelauncht: 21.06. (11 Anzeigen), 09.08. (7), 16.–18.08. (14), 28.08. (8), 25.09. (8), 06.10. (14).
- **Trend:** Die aktiven Anzeigen pro Monat fallen (Aug 269 → Sep 210 → Okt 118). Die Reichweite neuer Anzeigen ab September ist klein: die meisten < 2.000, Ausnahme 184152257 mit 42.260. **Kein Scale-Signal.**

#### 2c) Top-Anzeigen von Duune (nach Impressions-Rang bzw. EU-Reichweite)

Der Body ist bei allen Anzeigen identisch (siehe oben). Der Hook steckt im Creative-Overlay bzw. im Video-Untertitel.

| # | ID / Links | Format, Start, Reichweite | Hook (FR, wörtlich) | Deutsch |
|---|---|---|---|---|
| 1 | **136609610**, [GetHooked](https://app.gethookd.ai/share/ad/136609610?signature=d635168d75432b505a9b7a150bde6a8127a98ce75702f23d07bb01150b146314), [Meta](https://www.facebook.com/ads/library/?id=908488145612872) | Video, 24.06., **171.182**, Spend 501–2.000 $ | „Dites adieu aux housses de couette.“ / Untertitel „J'ai commandé“ | „Sagen Sie Bettbezügen Lebewohl.“ / „Ich habe bestellt“ |
| 2 | **136610436**, [GetHooked](https://app.gethookd.ai/share/ad/136610436?signature=e6a768bccbb71f69aa1438ebf90f1e0ebd5cb1076df4513b25d11b77ad5523a2), [Meta](https://www.facebook.com/ads/library/?id=1785545752871966) | Image, 10.06., **130.762** | „Ne plus jamais remettre de housse de couette. Couette + taie d'oreiller EN UN SEUL PRODUIT !“ · „SOLDES“ · „Disponible en 7 couleurs différentes.“ | „Nie wieder einen Bettbezug aufziehen. Decke + Kissenbezug in EINEM Produkt!“ · „SALE“ · „In 7 verschiedenen Farben erhältlich.“ |
| 3 | **136609812**, [GetHooked](https://app.gethookd.ai/share/ad/136609812?signature=1f386f633609adf84ef3fa0876c4b5bc9752f896a716fb1c59ba284c3f2bcebb), [Meta](https://www.facebook.com/ads/library/?id=1562546001980406) | Image, 15.06., **107.520** | „NE CHANGEZ PLUS JAMAIS VOTRE LINGE DE LIT. Couette + housse en un seul produit.“ | „Wechseln Sie nie wieder Ihre Bettwäsche. Decke + Bezug in einem Produkt.“ (entspricht 1:1 MS 112079858) |
| 4 | **136610134**, [GetHooked](https://app.gethookd.ai/share/ad/136610134?signature=28e9fcc45658a7bacd550d02b37132dd9bfa6db441f86e5c2520457cade4e7b9), [Meta](https://www.facebook.com/ads/library/?id=1963735474341380) | Video, 11.07., **89.827** | „Dite adieu aux housse de couette“ (sic) / „J'ai commandé“ | „Sag den Bettbezügen Lebewohl“ / „Ich habe bestellt“ (gleiche Creatorin wie #1, Re-Cut) |
| 5 | **136609885**, [GetHooked](https://app.gethookd.ai/share/ad/136609885?signature=985e9e926ab3888b636908abd45a0a81ae7dd959bc381183d78c3f0b61f38407), [Meta](https://www.facebook.com/ads/library/?id=1305074924671188) | Video, 09.06., **53.500**, CTA „See details“ | „NE CHANGEZ PLUS VOS DRAPS.“ / „J'ai commandé“ | „Wechseln Sie Ihre Laken nicht mehr.“ / „Ich habe bestellt“ (älterer Mann im Karo-Pyjama) |
| 6 | **184152257**, [GetHooked](https://app.gethookd.ai/share/ad/184152257?signature=b3ef182fcebce95416ce919e3509d1f49084fb057057fc6aa166334fade6b3d0), [Meta](https://www.facebook.com/ads/library/?id=1073870208960910) | Image, 25.09., **42.260**, Score 78 | „Offre d'automne : 2 taies d'oreiller OFFERTES pour chaque couette“ · „40 nuits d'essai“ · „Acheter maintenant“ | „Herbstangebot: 2 Kissenbezüge GRATIS zu jeder Decke“ · „40 Nächte Probeschlafen“ (Pendant zu MS „Herbst Aktion“, 196669844) |
| 7 | **136610302**, [GetHooked](https://app.gethookd.ai/share/ad/136610302?signature=69dacd3324d8b266f093f4f4efdc4455e8df114b52f3a1ec2844f37a41fb6ab1), [Meta](https://www.facebook.com/ads/library/?id=1731163297900871) | Image, 08.07., **23.721** | „Tout le confort, zéro corvée.“ · „Housse de couette complète“ · „Lavable en machine“ · „Ne transpirez plus la nuit“ · „Plus de 17 000 clients satisfaits“ | „Voller Komfort, null Aufwand.“ · „Kompletter Bettbezug“ · „Maschinenwaschbar“ · „Nie mehr nachts schwitzen“ · „Über 17.000 zufriedene Kunden“ |
| 8 | **167736920**, [GetHooked](https://app.gethookd.ai/share/ad/167736920?signature=b53198ae5643a48acdff5e7de6575e11e9d09e74ae73f172e5fcb657f1beecb5), [Meta](https://www.facebook.com/ads/library/?id=4203024486655104) | Image, 28.08., **23.229**, FR+LU | „9 COLORIS POUR TOUS LES STYLES“ · „2 TAIES OFFERTES Pour toute couverture Duune“ · „DÉCOUVRIR LA COLLECTION“ | „9 Farben für jeden Stil“ · „2 Kissenbezüge gratis zu jeder Duune-Decke“ · „Kollektion entdecken“ |
| 9 | **136610513**, [GetHooked](https://app.gethookd.ai/share/ad/136610513?signature=8e314dc008e99125c42e4cc9fcdd214c28c4653cf178447503329d174ef6e0e7), [Meta](https://www.facebook.com/ads/library/?id=1377143850924025) | Video 41 s, 21.06., **16.475**, Score 100 | „Ne changez plus jamais vos draps !“ / „Je l'ai commandée“ | „Wechseln Sie nie wieder Ihre Laken!“ / „Ich habe sie bestellt“ |
| 10 | **136611698** (MagicSplashy-Logo), [GetHooked](https://app.gethookd.ai/share/ad/136611698?signature=aa88737f74687274d51a3816d70c6d439ce3e0b7ae3afd35db50df0ad231279d), [Meta](https://www.facebook.com/ads/library/?id=2143387197057841) | Image, 09.06., 1.711, Score 86 | „UNIQUEMENT AUJOURD'HUI : 2 TAIES D'OREILLER OFFERTES.“ · „Dans la limite des stocks disponibles.“ · „BONUS 2 taies d'oreiller en cadeau pour vous.“ · **„MagicSplashy.“** | „NUR HEUTE: 2 Kissenbezüge gratis.“ · „Solange der Vorrat reicht.“ · „BONUS: 2 Kissenbezüge als Geschenk für Sie.“ |

Weitere Duune-Hooks und Testwinkel (geringe Reichweite, aber aufschlussreich für das Playbook):
- **136611845** (erste Duune-Anzeige, 08.06., Video): „NE TRANSPIREZ PLUS JAMAIS LA NUIT“ / „Je ne sais“, auf Deutsch „Nie wieder nachts schwitzen“. [GetHooked](https://app.gethookd.ai/share/ad/136611845?signature=c6f003c8f63371b7577a83e9c3acaaebd4424d085755ec114fe9e95e1c16a903), [Meta](https://www.facebook.com/ads/library/?id=2160416554752751)
- **136610965** (Video): „Fini de combattre sa housse de couette“ / „Le pire“, auf Deutsch „Schluss mit dem Kampf gegen den Bettbezug“. [GetHooked](https://app.gethookd.ai/share/ad/136610965?signature=b5989600ec231c6ebe6bbe83fea0e75f6b3d5308b5f234cbd40c4b966e4768d1), [Meta](https://www.facebook.com/ads/library/?id=1991310054845545)
- **148509022** (Advertorial-Look): „DERNIÈRE MINUTE – LA COUETTE QUI CHANGE TOUT – DITES ADIEU AUX HOUSSES – Par l'équipe DUUNE“, auf Deutsch „Eilmeldung: Die Decke, die alles verändert“. [GetHooked](https://app.gethookd.ai/share/ad/148509022?signature=91022957cf4593392bf9e7d48b15b2dc775a0693c6719a308658a131b82cc4f5), [Meta](https://www.facebook.com/ads/library/?id=1031666143040041)
- **148509033**: „«Plus que jusqu'à vendredi !» 2 taies d'oreiller OFFERTES avec chaque couette. ~~49,99 €~~ · 3 pièces – 2 offertes GRATUITES“, auf Deutsch „Nur noch bis Freitag! 2 Kissenbezüge gratis …“ (Testimonial-Optik, Mann ca. 55+). [GetHooked](https://app.gethookd.ai/share/ad/148509033?signature=63ddcc1ee7dd16c35bf0a310908099e35444b308be9bea6f23b6bad4ad4f57f3), [Meta](https://www.facebook.com/ads/library/?id=834742079627885)
- **148509037**: „DITES ADIEU AUX HOUSSES DE COUETTE – JUSQU'À -30% sur toute la collection EasySleep – Une couette. Plus jamais de housse.“ (Rabatt-Test). [GetHooked](https://app.gethookd.ai/share/ad/148509037?signature=d127545a38abd5b6c9f13042d9eac6b2d4364f024d6131c195e898a1ed7f1606), [Meta](https://www.facebook.com/ads/library/?id=1065738126430655)
- **168261225**: „Plus jamais de galère de lit : housse et couette en un seul produit“ (Timeline 08h00 → 10h00 → 12h00 → 17h00, Waschmaschine und Trockenständer) · „40 jours d'essai“. [GetHooked](https://app.gethookd.ai/share/ad/168261225?signature=a0ed1422b732d0eb4204a2192e3c8fa6c72ca4842007935cb5212ed5a25dbe8c), [Meta](https://www.facebook.com/ads/library/?id=27879814665043392)
- **184152267**: „Les indispensables de l'automne : Marathon Harry Potter / Une couette encore plus cosy“ (Popkultur-Saison-Static), auf Deutsch „Herbst-Essentials: Harry-Potter-Marathon / eine noch kuscheligere Decke“. [GetHooked](https://app.gethookd.ai/share/ad/184152267?signature=7d207887d8ceb5e140aed301d44a78f9112d0289ed28a84021bec438ed27ac96), [Meta](https://www.facebook.com/ads/library/?id=1802508364409915)

---

### 3) Weitere Stores, Pages und Domains: wer ist es, und ist es derselbe Operator?

**Suchen:**
- search_ads ohne Geo-Filter mit „EasySleep“ (hybrid und strict), „EasySleep duvet“ (en), „SoftCloud“ (strict), „ThermoBalance“ (strict, **0 Treffer**), „MagicSplashy“ und „Magic Splashy“
- list_shops q = „magicsplashy“, „easysleep“, „duune“
- search_brands „magicsplashy“, „magic splashy“, „duune“
- get_domain_advertisers und curl für alle genannten Domains

#### 3a) Domain-Check

| Domain | HTTP | GetHooked-Advertiser | Bewertung |
|---|---|---|---|
| magicsplashy.de | 200 | MagicSplashy (88310), 146 aktive Anzeigen, seit 21.03.2026 | Hauptshop |
| magicsplashy.ch | 200 → Umleitung auf magicsplashy.de | 0 | **gleicher Operator** (sicher), kein eigener Markt |
| magicsplashy.at / .com / .co.uk / .uk / .nl / .it / .es / .pl / .fr / .be | lösen nicht auf (000) | 0 | nicht registriert bzw. nicht aktiv |
| duune.co | 200 | Duune (8066940), 118 | siehe Abschnitt 2 |
| duune.com | 200, „Duune – Construct“ | 0 | fremde Firma |
| duune.fr | 402, Shopify „Boutique indisponible“ | 0 | gesperrter oder inaktiver Shopify-Shop, Zuordnung unklar |
| duune.co.uk / duune.de | lösen nicht auf | 0 | – |

#### 3b) Alle gefundenen EasySleep- und SoftCloud-Marken

| Marke / Page (Brand-ID) | Domain | Land / Sprache | Aktive Anzeigen | Beispiel-Anzeige | Gleicher Operator? |
|---|---|---|---|---|---|
| **MagicSplashy** (88310) | magicsplashy.de (+ .ch-Umleitung) | DE/AT, de | 146 | siehe oben | Referenz (M&B Brands GmbH) |
| **Duune** (8066940) | duune.co | FR (+LU), fr | 118 | 136611698 (MS-Logo) | **wahrscheinlich, mittel bis stark** |
| **Lunex / Lunex Maison / Lunex boutique** (5349101 / 7516553 / 7516554) | lunex-officiel.com | FR + BE, fr | 317 / 1.241 / 276 (Brand-Zähler, alle Produkte) | **179873667** „Et si faire son lit prenait 10 secondes ?“, Reichweite **2.127.007**, Spend 10–20 Tsd. $. [GetHooked](https://app.gethookd.ai/share/ad/179873667?signature=2412bf3dcbfeca732143be7797ab7052cd34564486a314cb74fbc1d480a81ae0), [Meta](https://www.facebook.com/ads/library/?id=4631939297034144). Außerdem **132324726** „Le lit refait avant que le café soit prêt ☕“, Reichweite 433.904. [GetHooked](https://app.gethookd.ai/share/ad/132324726?signature=e16312869aa0aa713b154edb1bf9bb342db495cc5f4f4cc4aa1aa66a09d8b6f0), [Meta](https://www.facebook.com/ads/library/?id=1340419974746867) | **nein bzw. Copycat** (VALLEY LLC, Wyoming, Gmail; Theme Shopfinity; Handle a16654-7a; nutzt aber SoftCloud®, ThermoBalance® und 49,99 €). In FR deutlich größer als Duune. |
| **Kallyon** (11879647) | kallyon.com | **UK (GBP, Shopify.country GB)**, en | 52 (EasySleep + Titan-Pfanne) | siehe Abschnitt 4 | **eher nein, Copycat** (Garzette LLC, New Mexico; Gemischtwarenladen; Dawn 15.4.1; Handle ca08wk-kh). PDP ist aber eine wörtliche Übersetzung der MS-PDP. |
| **Cozily Store** (11837492) | cozily-shop.com | UK/EN | 552 | **190139665** „WHY BUY TWO... WHEN ONE DOES BOTH?“ · „+2 SOFT CLOUD PILLOWCASES FREE“ · „Satisfied or refunded within 40 days“. [GetHooked](https://app.gethookd.ai/share/ad/190139665?signature=0bd803ee90db3b968bf7a4334f5c2d11293b7a1488fc9f40ba20f066904e9c4e), [Meta](https://www.facebook.com/ads/library/?id=3204030089984436) | **nein, Copycat** (Guangzhou Lingcai Technology Co., Ltd.; Shrine PRO) |
| **Pleene** (7553008) | pleene.uk / pleene.com | UK, auch US-Geo | 137 | **186893867** „A Duvet That Works For You“ · „MY BED. MY WAY. Just wash, dry and put it back on.“. [GetHooked](https://app.gethookd.ai/share/ad/186893867?signature=427fec70c06030c12582ea7afc5367a9381e9977011adcea03ef8367788f4ba2), [Meta](https://www.facebook.com/ads/library/?id=1744189879967996) | **nein, Copycat** (Produkt heißt jetzt „EasyRest“) |
| Nesolia (15577863) | nesolia.com (`/products/nesolia-edredon-easysleep`) | ES, es | 28 | **196979777**. [GetHooked](https://app.gethookd.ai/share/ad/196979777?signature=47c4fd959fda0c0b28c9701b8a30c49a8ea819460293d86d2c4996823200b5d1), [Meta](https://www.facebook.com/ads/library/?id=28466507183042777) | unbekannt bzw. eher Copycat (nicht tief geprüft) |
| Maison NOVA (13340427) | maisonnova-contact.com | FR, fr | 15 | **199786188**. [GetHooked](https://app.gethookd.ai/share/ad/199786188?signature=b6e649abc706a43356f9ac6d6ed51c6f4826316b754429a02cf9e13eac8ff769), [Meta](https://www.facebook.com/ads/library/?id=1675251527355555) | eher Copycat (nicht tief geprüft) |
| DearMe (19303789) | dearme.fr | FR, fr | 15 | **194389310**. [GetHooked](https://app.gethookd.ai/share/ad/194389310?signature=57c3d5ad074b265579f348ce3add66669961b534fdb5c9643900553839423229), [Meta](https://www.facebook.com/ads/library/?id=1122911620200611) | eher Copycat (nicht tief geprüft) |
| Hooma (24359577) | hooma.store | FR, fr | 3 | **199650606**. [GetHooked](https://app.gethookd.ai/share/ad/199650606?signature=80116bd7ed14595e568993589096de77fd15a91fd1e85fcd29ca6a029d288e44), [Meta](https://www.facebook.com/ads/library/?id=1095049330160225) | eher Copycat (nicht tief geprüft) |
| SoftClouds.de (15576191) | soft-clouds.de (`/products/soft-cloud-2-in-1-decke`) | **DE**, de | 8 | **190904927**. [GetHooked](https://app.gethookd.ai/share/ad/190904927?signature=10f335453f7033c7f4afad004ab849aedb3333c2c8a98cd1e6f8b58986b7818e), [Meta](https://www.facebook.com/ads/library/?id=1648455450205005) | eher Copycat im MS-Heimatmarkt (nicht tief geprüft) |
| Lumeo South Africa (11472265) | lumeo.co.za/pages/easysleep | ZA, en | 332 (Brand gesamt) | **185133554**. [GetHooked](https://app.gethookd.ai/share/ad/185133554?signature=81b1917586d376f5ba20f49db9a3c0594bfb5a7b5f518a2d171e4de0e612c2ed), [Meta](https://www.facebook.com/ads/library/?id=1839377963697854) | nein (der Name „EasySleep“ steht dort auch für andere Produkte) |

**Wichtig für die Bewertung:** „EasySleep®“, „SoftCloud®“, „ThermoBalance®“, „40 Nächte“, „49,99“ und „17.000“ sind inzwischen **Gemeingut der Klon-Szene** (FR, UK, ES, DE). Nur das MagicSplashy-Logo in der Duune-Anzeige ist ein Operator-spezifischer Beleg. **Weitere Länder-Stores desselben Operators wurden nicht gefunden.**

---

### 4) Gibt es Magic Splashy oder EasySleep bereits im UK?

**Magic Splashy oder Duune selbst: NEIN.**
- 0 Anzeigen von Brand 88310 oder 8066940 mit GB-Geo. Alle MS-Anzeigen sind DE/AT, alle Duune-Anzeigen FR/LU.
- `magicsplashy.co.uk`, `.uk`, `.com`, `duune.co.uk` und `duune.com` (fremde Firma) haben keine Advertiser. Es gibt keine weitere Page namens „MagicSplashy“ oder „Duune“.
- Einschränkung: GB liegt außerhalb der EU-Transparenzdaten. Anzeigen nur für GB haben daher oft leere `countries`. Wir haben stattdessen nach Domains, Pages und Sprache (en) gesucht und auch dort keinen Treffer für MS oder Duune gefunden.

**Die EasySleep-Idee selbst: JA, im UK schon dreifach besetzt.**
1. **Cozily** (cozily-shop.com, 552 aktive Anzeigen, seit 10.07.2026 auf der Domain): EasySleep-PDP mit SoftCloud®-Kissenbezügen bzw. Spannbetttuch, 40 Nächten und Advertorial `/pages/advertorial`. Rechtsträger aus China. Beispiele:
   - 190139665 (siehe oben)
   - **190139652** „SO LIGHT... IT ALMOST SEEMS TO FLOAT“ · „+ 2 FREE 2 Soft Cloud pillowcases“. [GetHooked](https://app.gethookd.ai/share/ad/190139652?signature=e9d30007aab76c0ca215961341478f08d681c0c6c1c6b6dc6e601309b276bd0b), [Meta](https://www.facebook.com/ads/library/?id=2275200653318705)
2. **Pleene** (pleene.uk, 137): nutzt jetzt den eigenen Produktnamen „EasyRest“.
   - **193234278** „NEW: Lavender Mist“. [GetHooked](https://app.gethookd.ai/share/ad/193234278?signature=2acfe25ae18b9ee3fd409e989a071bce595dea12e1dca232a03824238d38b557), [Meta](https://www.facebook.com/ads/library/?id=1103531258742413)
3. **Kallyon** (kallyon.com, GBP, 52 aktive Anzeigen, erste Anzeige am 09.08.2026), **neu und bisher nicht auf dem Radar**:
   - Die PDP „EasySleep – The quick-drying 2-in-1 duvet that makes duvet covers unnecessary“ (angelegt am 02.08.2026) ist eine **wörtliche Übersetzung der MS-DE-PDP**. Farben: „Coastal Blue, Fireside Red, Sunset Glow, Soft Mint Green, Cream Beige, Midnight Black, Moonstone Grey“. Außerdem: „No sweating, no freezing“, „in 2 hours“, „ThermoBalance® climate fiber“, „SoftCloud® pillowcases … (£49.99)“, „17,000 other people“, „40-night sleep trial“. Preise £59.99–109.99.
   - Der Anzeigen-Body ist eine wörtliche Übersetzung des MS-Bodys: „Duvet and cover in one 🌙 / The Kallyon duvet finally makes making the bed easy. Just wash it, dry it and put it back on the bed. / ✓ No more hassle with duvet covers ✓ Pleasantly cool in summer, cosy and warm in winter ✓ Hypoallergenic and antibacterial / Get 2 SoftCloud pillowcases for free today (worth £49.99). / 40-night trial / Finally enjoy a bed that's always fresh.“
   - Beispiele:
     - **190939341** WhatsApp-Gruppenchat „Girls, I have to show you this 😍 I ordered this duvet from Kallyon. It's a duvet and bedding in one, never change it again“. [GetHooked](https://app.gethookd.ai/share/ad/190939341?signature=7cc392b1d63932dac9b924164d547f0528a714adf3c4c8d3757cd9dcaed6708e), [Meta](https://www.facebook.com/ads/library/?id=1599941168415216)
     - **190939220** „NO MORE CHANGING THE BEDDING · DUVET + DUVET COVER IN ONE · Cool in summer, warm in winter“. [GetHooked](https://app.gethookd.ai/share/ad/190939220?signature=6c713bbf4202d5fcdcb926f871c200f76f04d09306c524f242cae88ead5fe947), [Meta](https://www.facebook.com/ads/library/?id=2202986907149822)
     - **198183616** „Our customers describe it in 3 words: Lightweight · Comfortable · Cosy – Over 17,000 happy sleepers“. [GetHooked](https://app.gethookd.ai/share/ad/198183616?signature=f279af6651703ed77ed62bfa4161f6e9280432d183f1ab1401b6736e46d9a69c), [Meta](https://www.facebook.com/ads/library/?id=2246294822828264)
     - **191405287** „… (worth £59.99) … 30-night trial“. Kallyon testet hier Varianten von Bonus-Wert und Testdauer. [GetHooked](https://app.gethookd.ai/share/ad/191405287?signature=41fa6d68792b2412a2d8937530aa8d75faa3594964de47447fce7b8504922bab), [Meta](https://www.facebook.com/ads/library/?id=1605779731075530)
   - Die Performance ist schwach: Scores 16–58, keine Anzeige mit „Winning“-Score. Kallyon wirbt parallel für eine Titan-Pfanne, **199355573** „Five types of pans I would never buy at Tesco“. [GetHooked](https://app.gethookd.ai/share/ad/199355573?signature=3a1ae052ff541ad755fad221beea64d972a2282fd708fb9ec8424140affd872a), [Meta](https://www.facebook.com/ads/library/?id=1081448574646197). Das spricht für einen **generalistischen Dropshipper, nicht für Magic Splashy selbst**.

**Was das für das „First Mover“-Ziel des Kunden bedeutet:**
- **Echter Vorsprung ist noch möglich:** Der Operator hinter Magic Splashy ist nicht im UK. Die UK-Klone haben die MS-*Texte* übernommen, aber nicht die stärksten MS-*Formate*: hochskalierte deutsche UGC-Videos (1,3–1,6 Mio. EU-Reichweite pro Anzeige), Advertorial `/pages/frauen-magazin`, Quiz bzw. `/pages/umfrage`, Saison-Pages wie `/pages/schlafen-im-sommer`, DCO-Tests. Auch die Duune-Lokalisierungsmuster fehlen dort weitgehend (lokale „J'ai commandé“-UGC, Popkultur- und Saison-Statics).
- **Nicht „first“ sind wir bei:** den Namen EasySleep, SoftCloud und ThermoBalance, „17,000 happy sleepers“, „40-night trial“ und „2 free pillowcases worth £49.99“. Das läuft im UK schon bei Kallyon und teilweise bei Cozily. Diese Bausteine sollten im UK eigenständig benannt werden, damit wir uns nicht wie ein weiterer Klon lesen. Zusätzlich sollten wir sie durch eigenen Social Proof aus dem UK ersetzen.

---

### Methodik und Grenzen

- Die Länderdaten von GetHooked basieren auf EU-Transparenzdaten. **CH und GB sind strukturell unterbelichtet.** Deshalb wurden zusätzlich Domains, Pages, Sprache und Shop-Währung geprüft.
- Die Zahl „aktive Anzeigen“ ist ein Brand-Zähler zum letzten Brand-Spy. Die Shop-Publikation zählt bei abweichendem Stichtag 158 (MS) bzw. 122 (Duune).
- Die Reichweitensummen für Duune sind aus den einzelnen `eu_total_reach`-Werten aufaddiert (116 Anzeigen mit Daten).
- Rechtsträger, Shopify-Handles, Themes, Varianten und Preise stammen aus Live-Abrufen vom 08.10.2026: `/policies/legal-notice`, `Shopify.shop` / `Shopify.theme` und `/products/<handle>.js`.
- Nesolia, Maison NOVA, DearMe, Hooma und SoftClouds.de wurden nur über Anzeigen identifiziert. Ihre Rechtsträger wurden nicht geprüft.



# D2 Pleene (UK)

## Pleene (UK) – Wettbewerbs-Teardown

*Stand: 08.10.2026 · Quelle: GetHooked (Brand-ID 7553008, Shops 47758 `pleene.com` und 47737 `pleene.uk`), Meta Ad Library, Live-Abruf der Landingpages per curl*
*Linkformat je Ad: **[GH]** = GetHooked-Share-Link · **[Meta]** = Meta Ad Library. Englische Hooks, Headlines und Texte sind wörtlich zitiert.*

---

### 0. Das Wichtigste in Kürze

1. **Pleene ist ein direkter UK-Klon von Magic Splashy und fährt sehr hohes Volumen.** Seit dem ersten Ad am 01.06.2026 hat Pleene **692 Ads** gestartet. **137 davon sind aktiv**, 555 inaktiv. Von Juli auf August gab es einen Sprung von 48 auf 269 Launches, im September waren es 298, in der ersten Oktoberwoche schon 49.
2. **Der Haupt-Primärtext ist eine 1:1-Übersetzung des Magic-Splashy-Texts.** MS: „Decke + Bezug in einem 🌙 … Heute 2 SoftCloud Kissenbezüge gratis (49,99€ Wert) … 40 Tage risikofrei probeschlafen“. Pleene: „Duvet + Cover in One 🌙 … Get 2 free Pleene™ Pillow Cases today (worth £39.99). 90 nights to try it risk-free.“ Struktur, Emojis, Bullets und der Schlusssatz sind identisch.
3. **Auch mehrere MS-Video-Skripte sind wortgleich übersetzt.** Zwei Beispiele: „Bettbeziehen ist einer der sinnlosesten Zeitfresser im Haushalt“ (MS-Winner mit 10–20 k$ Spend) wurde zu „Changing your bed is one of the most pointless time-wasters in the house“. „Du duschst jeden Abend … Schweiß. Milben.“ wurde zu „You shower every night … Sweat. Dust mites.“
4. **Eigene UK-Lokalisierung kommt seit Mitte September dazu.**
   - **10.5 TOG** und Winter-Einwände: „Warm Enough For A British Winter“, „No way that keeps you warm in a Scottish winter“.
   - „No Launderette Needed“, „normal 7kg machine“.
   - Britischer UGC-Ton: „I bloody hate changing the bed“.
   - Senioren-Angle: „at my age“, „I'm 83“, „Bedding Made for Independence“, Enkel-Besuch.
5. **Das Angebot ist großzügiger als bei MS.**
   - **90 Nächte** Trial statt 40 Tage.
   - **2 Gratis-Kissenbezüge (Wert £39.99)**.
   - Seit 16.09. zusätzlich **„30% off“**. Auf der PDP: £74.99 statt £114.99 („SAVE 34%“), Double £89.99, King £119.99, Super King £129.99.
   - Gratis-Versand erst ab £100.
6. **Funnel:** Fast alles geht direkt auf die PDP `pleene.com/products/easyrest` (70 von 120 Ads in der Domain-Publikation). Daneben gibt es eine Winter-PDP `easyrest-duvet` (10 Ads) und seit 01.10. ein **Advertorial `pages/tb-6`** (8 Ads): „"Never change your bed linen on a Sunday again"“. Es gibt **keinen Quiz-Funnel und kein Listicle**.
7. **Diese Lücken lässt Pleene offen:** Wechseljahre und Nachtschweiß (0 Treffer), Geschenk und Weihnachten (0), Allergie als Lead-Angle (nur als Bullet), Öko. MS fährt den Wechseljahre-Angle in DE bereits („5 Gründe, warum deine Decke in den Wechseljahren ein Upgrade braucht“).
8. **Schwachstellen von Pleene:**
   - Betreiber sitzt in Hongkong (One Way Ecom Ltd.).
   - Die Reviews klagen wiederholt über lange Lieferzeiten.
   - Den Rückversand zahlt der Kunde.
   - Die Kundenzahlen widersprechen sich: PDP und Ads sagen „Over 10,000“, das Advertorial „7,000+“, Trustpilot zeigt 4.7 bei nur 250 Reviews.

---

### 1. Identität und Setup

| Feld | Wert |
|---|---|
| Brand (GetHooked) | Pleene, Brand-ID **7553008**, FB-Page-ID 998396186687205 |
| Shops | **47758 `pleene.com`**: 120 Live-Ads in der Domain-Publikation (Stand 05.10.), ca. 29.4 k Besuche/Monat (Aug), 100 % GB-Traffic. **47737 `pleene.uk`**: 1 Ad, leitet auf pleene.com |
| Advertiser auf der Domain | `get_domain_advertisers(pleene.com)`: nur **1 Account** (Pleene, 137 aktive Ads, erstmals gesehen am 11.06.2026). `pleene.uk` hat 0 Advertiser |
| Start | Erste Ads am 01./02.06.2026, Shop laut GetHooked ca. Juni 2026 |
| Betreiber (Impressum) | **One Way Ecom Limited**, World Trust Tower, Hongkong. Werbung „managed … by **21Commerce Limited**“, gleiche Adresse. Tel. +1 (205) 360-5811 (US-Nummer) |
| Tech | Shopify; Triple-Whale-Pixel; A/B-Test-Script im Quelltext; Template `easyrest-duvet-winter26` |
| Märkte | Shop in GBP, AUD, CAD und USD. Ads laufen in **UK** sowie seit 23.09. in den **USA**, dort als „EasyRest™ Comforter“ (`/products/easyrest-comforter`). Keine EU-Reach-Daten, weil UK nicht unter DSA-Transparenz fällt |
| Produkt | „Pleene EasyRest™ Duvet“: 2-in-1-Decke mit eingenähtem Bezug, 10.5 TOG, Mikrofaser, 3.12 kg (King), 10 Farben, 6 Größen in cm. Nebenprodukte: CosyRest™ Sherpa Throw, EasyRest™ Pillow, Kissenbezüge, FluffBalls™; Zipsheet (US-Test „Never lift your mattress again.“) |

---

### 2. Was Pleene jetzt fährt (aktiv, Stand 07./08.10.2026)

**Aktive Ads: 137** (Brand-Counter am 07.10.; Suchindex: 145 inklusive 8 zurückgehaltener Ads)

#### 2.1 Formate (137 aktive Ads, eigene Zählung)
| Format | Anzahl | Anteil |
|---|---|---|
| Image (Static) | 73 | 53 % |
| Video | 63 | 46 % |
| DCO/Carousel | 1 | 1 % |

`aggregate_ads` über 145 Ads im Index zählt Image 78, Video 65, DCO 2. CTA: SHOP_NOW 124, ORDER_NOW 15, SEE_DETAILS 6.

#### 2.2 Landingpages (Domain-Publikation, 120 Ads)
| Landingpage | Ads | Typ |
|---|---|---|
| `pleene.com/products/easyrest` | 70 | **PDP** (UK-Haupt-PDP, Template „winter26“) |
| `pleene.com/products/easyrest-comforter` | 32 | **PDP USA** („Comforter“, Zoll-Größen) |
| `pleene.com/products/easyrest-duvet` | 10 | **PDP** (Winter-Variante, gleiche Inhalte) |
| `pleene.com/pages/tb-6` | 8 | **Advertorial**: ausdrücklich als „Advertisement“ gekennzeichnet, Vergleichstabelle, Trustpilot-Social-Proof, FAQ (seit 01.10.) |

- **LP-Typen:** PDP etwa 93 %, Advertorial etwa 7 %. Kein Listicle, kein Quiz, keine VSL. `aggregate page_type`: product_page 83.
- **Historisch (inaktiv) zusätzlich:**
  - `/products/easyrest-pdp`: Juli-Test einer alternativen PDP.
  - `/products/pleene-easyrest-duvet-2in1`.
  - `/products/easyrest-everyday-duvet`: DPA/DCO.
  - `/products/zipsheet-us`.
  - US-URLs mit `?trybe=`-Parameter.

#### 2.3 Märkte innerhalb der aktiven Ads
- Etwa **35–40 aktive Ads sind US-Comforter-Ads**: Länder-Tag US oder LP `easyrest-comforter`, Copy mit „comforter“.
- Etwa **95–100 aktive Ads zielen auf UK**: GB-Tag, £-Preise, TOG und UK-Vokabular wie „launderette“, „British winter“.
- Eine Gruppe von etwa 11 Ads vom 06.10. hat US-Copy, verlinkt aber die UK-PDP, und trägt keinen Länder-Tag. Beispiele: „Bedding Made for Independence“, „Your Bed. Your Way.“ Das sieht nach einem Test der Senioren- bzw. Independence-Copy in UK aus.

---

### 3. Launch-Kadenz (letzte ca. 4 Monate)

| Startmonat | gestartet gesamt | davon heute noch aktiv | Überlebensrate |
|---|---|---|---|
| Juni 2026 | 28 | 5 | 18 % |
| Juli 2026 | 48 | 0 | 0 % |
| August 2026 | 269 | 12 | 4 % |
| September 2026 | 298 | 73 | 24 % |
| 1.–7. Oktober 2026 | 49 (+ mind. 47 noch aktiv) | 47 | – |
| **Summe** | **692** | **137** | |

- **Batch-Launches an einzelnen Tagen:**
  - 06.10.: 27 heute aktive Ads, ein UK+US-Test-Batch.
  - 05.10.: 13 GB-Videos (Hund, Gästebett, „When did you last wash“, „Too thin“).
  - 29.09.: 14 US-Statics.
  - 24.09.: etwa 15, überwiegend US.
  - 01.10.: 9.
  - 27.09.: 8.
- **Muster:** Pro Konzept starten sie 3–13 Varianten mit identischer Copy und unterschiedlichen Creatives (collapse `variant_count` bis 20). Die meisten Varianten sterben nach 2–9 Tagen. Gewinner laufen weiter: die Juni-Statics seit 116–120 Tagen, die August-Videos seit 56–67 Tagen.
- **Rhythmus:** etwa 9–10 neue Ads pro Tag (Aug–Sep). Wöchentlich kommen neue Konzepte dazu: Farb-Knappheit Anfang August, „Everyone said it“ Mitte August, Winter/TOG Mitte September, Senioren/Independence Ende September und Oktober.

---

### 4. Die 15 stärksten Ads (Performance-Score, Laufzeit, Varianten)

*EU-Reach ist für alle Pleene-Ads leer (UK-only, keine DSA-Daten). Das Ranking stützt sich deshalb auf performance_score (0–100), days_active und Skalierung über Varianten.*

| # | Ad-ID | Format | Start / Laufzeit | PS | Headline (wörtlich) | Hook / Kern-Copy (wörtlich) | Avatar | Angle | Offer | Links |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 136388964 | Static | 11.06. / 120 T | 100 | „No More Fighting With Duvet Covers“ | Bild: „3 things to STOP doing when you make the bed“ – „Wrestling the duvet into its cover“ / „Lifting the heavy mattress to tuck sheets“ / „Shaking out dusty bedding“ → „✅ Do this instead“ | keiner (Icon-Grafik) | Kein Bezug mehr / Mühe | 2 free Pillow Cases (£39.99), 90 nights | [GH](https://app.gethookd.ai/share/ad/136388964?signature=d0ff0d2a2536e91cfc3dacb7f3b055bf680241a71e3d485ea8d2c98436047966) · [Meta](https://www.facebook.com/ads/library/?id=884267707299487) |
| 2 | 136388847 | Static | 11.06. / 120 T | 100 | „No More Fighting With Duvet Covers“ | Bild: „Just want to sleep… but you've still got to change the bed?“ – „End up too hot and uncomfortable to drift off.“ | Frau ca. 30–40, verschwitzt, nachts im Bett | Bettbeziehen-Frust + Hitze | wie oben | [GH](https://app.gethookd.ai/share/ad/136388847?signature=422777a4ae4663b915702dc330ccb3f999733ab57559e373f53beb6af24567f7) · [Meta](https://www.facebook.com/ads/library/?id=1583232786477915) |
| 3 | 133366534 | Video | 03.08. / 67 T | 100 | „No More Fighting With Duvet Covers“ | Spoken: „Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it. When did you last actually wash it?“ | Mann ca. 35–45, weißes T-Shirt (UGC); Creative mehrfach recycelt (193234279, 193234275) | Hygiene | wie oben | [GH](https://app.gethookd.ai/share/ad/133366534?signature=ec7e21facd4f53244e7aacaf8002b409a7803a538b1d302bb66be766c52ef924) · [Meta](https://www.facebook.com/ads/library/?id=1372761711494763) |
| 4 | 139561428 | Video | 07.08. / 63 T | 100 | „Hearth Red. Nearly gone.“ | Overlay: „Only 17 left in Hearth Red“ · Copy: „Hearth Red is nearly sold out — and unlike most 'selling fast' claims, this one's just true.“ | kein Mensch, AI-Interieur | Farbe / Knappheit | – | [GH](https://app.gethookd.ai/share/ad/139561428?signature=1eb14bdf7f1f4b278f8b5996d37204958181d02f07e10262e225457c7f9a49fd) · [Meta](https://www.facebook.com/ads/library/?id=1034362836068724) |
| 5 | 139561410 | Video | 07.08. / 63 T | 100 | „Mint Green is almost gone.“ | „This week only: 2 free Pleene™ Pillow Cases with every duvet. And if you've been eyeing Mint Green — it's almost gone.“ | kein Mensch | Knappheit + Gratis-Bezüge | 2 free Pillow Cases „This week only“ | [GH](https://app.gethookd.ai/share/ad/139561410?signature=8993cc76f99c424613789bd7c6c9a9248d166b223587f503929e5077c7a435b2) · [Meta](https://www.facebook.com/ads/library/?id=1355121136744622) |
| 6 | 145443331 | Video | 14.08. / 56 T | 100 | „Everyone said it. They were right.“ | Spoken/Overlay: „I haven't changed my bed linen in three months and it's never felt fresher.“ · Copy: „I only ordered it because everyone said you never have to change the bed linen again. Annoyingly, they were right.“ | Mann ca. 35, britischer UGC-Creator, liegt im Bett (grünes Schlafzimmer) | Social Proof / kein Bezug | – | [GH](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) · [Meta](https://www.facebook.com/ads/library/?id=1440933327878495) |
| 7 | 163921089 | Video | 27.08. / 43 T | 100 | „Everyone said it. They were right.“ | wie #6 (Re-Launch) | wie #6 | wie #6 | – | [GH](https://app.gethookd.ai/share/ad/163921089?signature=18918dab03620f19a44f0f4ae4aabab8d5f163dfaa3984dcc8e6e691c7301c1d) · [Meta](https://www.facebook.com/ads/library/?id=1609110380938946) |
| 8 | 168246678 | Video | 29.08. / 41 T | 100 | „Check This Before You Buy“ | Overlay: „Before you buy a coverless duvet check 3 things“ · Copy: „✓ Does the WHOLE thing fit a normal washing machine? ✓ Is it dry in 2 hours without a tumble dryer? ✓ Can you test it at home for 90 nights? The Pleene EasyRest™: yes, yes and yes.“ | kein Mensch, Top-down-Bett mint | Kaufberatung / Einwände | 90 nights | [GH](https://app.gethookd.ai/share/ad/168246678?signature=0780e25635ebab07a104b29b13efc556f8d9616332f12537858f9d96c5a5cd59) · [Meta](https://www.facebook.com/ads/library/?id=1607904514111212) |
| 9 | 171191667 | Static | 03.09. / 36 T | 100 | „No More Fighting With Duvet Covers“ | Text-Meme: „“But you'd need a huge washing machine for that” 😂 That's what I thought too. The truth: 👉 The duvet is made extra light 👉 fits in any normal household machine 👉 dries in 2 hours even without a dryer … No cover. No stress.“ → „Duvet + cover in one“ | kein Mensch (Text + Produkt) | Waschmaschinen-Einwand + Quick-Dry | 2 free Pillow Cases, 90 nights | [GH](https://app.gethookd.ai/share/ad/171191667?signature=b03cc4b1b86af6280d5edfa0028fe241e19fd20d3b3592e580dd3f576a92669d) · [Meta](https://www.facebook.com/ads/library/?id=1583757549405276) |
| 10 | 172403389 | Static | 05.09. / 34 T | 100 | „Properly Warm, Never Heavy“ | Bild: „~~A light duvet can't keep you warm in winter.~~ Climate-regulating fibres keep you properly warm. Without the heavy feeling.“ · Copy: „… the whole duvet still goes in your washing machine, dry in 2 hours.“ | kein Mensch, Stapel aus 3 Farben | Winterwärme / Myth-Busting | „2 Free Pillow Cases · 90-Night Trial“ | [GH](https://app.gethookd.ai/share/ad/172403389?signature=fc57a29e066c788034eca64a557143f0c3e0b71232ea5868d51df06e7536000f) · [Meta](https://www.facebook.com/ads/library/?id=1725326416267519) |
| 11 | 172760571 | Static | 06.09. / 33 T | 100 | „Properly Warm, Never Heavy“ | Bild: „“It's what I've been looking for all this time!” — Customer, UK“ ✓ + 2 free pillow cases ✓ 90-night sleep trial | kein Mensch (Testimonial-Quote) | Testimonial | 2 free Pillow Cases, 90 nights | [GH](https://app.gethookd.ai/share/ad/172760571?signature=82cd0a698c2d4720c44c69a474abfa9e4e1f24189f59d7dd6d1f216aaf8e25b8) · [Meta](https://www.facebook.com/ads/library/?id=1415553300514250) |
| 12 | 136389861 | Video | 11.06. / 120 T | 61 | „No More Fighting With Duvet Covers“ | Spoken: „If your shoulders ache, don't do this. And if your back is sore, definitely don't do this. As we get older, making the bed shouldn't be this hard.“ | **AI-„Heiler“**: ostasiatischer Mann 70+ mit Rauschebart, Apothekenregal, **Union-Jack-Flagge** | Schmerz / Ältere / Experte | „two free Plein pillowcases worth £39.99“, „90-night trial“ | [GH](https://app.gethookd.ai/share/ad/136389861?signature=52dff4dac27abf45e6f9b062724b0d38f817b3ddcd8939d92684a863d31faaf8) · [Meta](https://www.facebook.com/ads/library/?id=1642037860240117) |
| 13 | 151025063 | Video | 22.08. / 48 T | 86 | „No More Fighting With Duvet Covers“ | Spoken: „I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“ | Frau ca. 50 (UGC, weißes T-Shirt, Karo-Pyjama), vermutlich dieselbe Creatorin wie 169082943 | Schmerz / Mühe | 2 free Pillow Cases, 90 nights | [GH](https://app.gethookd.ai/share/ad/151025063?signature=6a64477f3dd49f4b0e862e714a6a052a0839cfe3382654d8e4902e827f95d481) · [Meta](https://www.facebook.com/ads/library/?id=1369166828764339) |
| 14 | 178749251 | Video | 16.09. / 23 T | 81 | „Warm Enough For A British Winter“ | Spoken: „Looks lovely, but you'll freeze under that in winter. You won't freeze under this. The Plein EasyRest is made for cold nights“ · Copy: „❄️ "You'll freeze under that in winter." Here's the honest answer: the Pleene EasyRest™ is rated 10.5 tog, a proper autumn and winter weight…“ | n/a (Video nicht gesichtet); Geschwister-Ads: „No way that keeps you warm in a Scottish winter.“ (178749254), „Is it actually warm enough for winter?“ (178749247) | Winter / Wärme-Einwand | 90-night trial | [GH](https://app.gethookd.ai/share/ad/178749251?signature=f7a95b97af4df738359f0bc0b4a21bbd6f5508efef5391e097423762a823afc1) · [Meta](https://www.facebook.com/ads/library/?id=1792003651846452) |
| 15 | 178749258 | Static | 16.09. / 23 T | 81 | „No Launderette Needed. Ever.“ | „❄️ Your winter duvet shouldn't need a launderette. … ✓ Cover sewn in, nothing to strip off ✓ Fits a normal washing machine 🧺 ✓ Filling quilted in place, no cold spots ✓ Dry again in about 2 hours 🎁 Right now: 30% off + 2 FREE matching pillow cases.“ | kein Mensch | Waschsalon / Winter | **30% off + 2 FREE pillow cases** | [GH](https://app.gethookd.ai/share/ad/178749258?signature=26142585e8a79bd682cbb72cd7ae73d46e39dc00bb8ff65b79f19d32e5e4e2cb) · [Meta](https://www.facebook.com/ads/library/?id=1750276626195989) |

**Weitere aktive Long-Runner und Winner:**
- 136390001 (Static, 120 T): Bild „Change the bed in the summer heat / End up hot and sweaty / Now you need another shower → ✅ Or… switch to the easy way.“ [GH](https://app.gethookd.ai/share/ad/136390001?signature=1765b0a55cd4792881cb510eac2152901fc1b2187c69ce5fdd22929e5f2e6553) · [Meta](https://www.facebook.com/ads/library/?id=2687410064986677)
- 133366116 (Static, 116 T): Bild „You wash the cover… but never the duvet inside. Years of sweat, dead skin & dust mites — every night. … A fresher, healthier way to sleep.“ [GH](https://app.gethookd.ai/share/ad/133366116?signature=a2afe366ec4a13b6ab93d2e4edce9c7275c8292acd57172af7d5455a8b4dc87d) · [Meta](https://www.facebook.com/ads/library/?id=1687513282572901)
- 139561491 (Video, 63 T, PS 86): „Everyone's buying the blue one.“ Overlay „Everyone's buying it in Coastal Blue · Only 19 left“. [GH](https://app.gethookd.ai/share/ad/139561491?signature=5cbb3a8ead3ed2e5b41ef6ef544d7498f90d8427b339e0ba7304f344c120fb43) · [Meta](https://www.facebook.com/ads/library/?id=1526037445508180)
- 179476350 (Static, PS 81): „Warm Enough For A British Winter“. [GH](https://app.gethookd.ai/share/ad/179476350?signature=929eaf7be4e50da7829743ff0e7ad0be30111ad47d7408608f8bb7fc89e7de17) · [Meta](https://www.facebook.com/ads/library/?id=935523852471023)

**Inaktive Long-Runner (Juni bis Ende August/September, 85–97 Tage):**
- 133364681 (Static, 97 T): „This week only: 2 FREE Pillow Cases with every DUVET“, „FREE this week only“, £39.99 durchgestrichen. [GH](https://app.gethookd.ai/share/ad/133364681?signature=1f697d19a3e48473cc48ee7242eb827b0144b438577de47455947de87e8ab6aa) · [Meta](https://www.facebook.com/ads/library/?id=1332402255676454)
- 136389548 (Video, 89 T): Overlay „Why do all men in the United Kingdom love this duvet?“, Mann ca. 30 kniet auf Bett. [GH](https://app.gethookd.ai/share/ad/136389548?signature=04225e5f98e694f2d087aa884a689ec9ce7fa7995bfdc206597109cd1b3a02da) · [Meta](https://www.facebook.com/ads/library/?id=2264705503936499)
- 136389371 (Video, 89 T): „I don't know how the duvet does it,“ glatzköpfiger Mann ca. 45. [GH](https://app.gethookd.ai/share/ad/136389371?signature=a95032fa92b4fbf0d5f4b9744b87351beafdad9634c50e8b0ae18de242b06cd6) · [Meta](https://www.facebook.com/ads/library/?id=1666885827896282)
- 136388705 (Video, 89 T): „I ordered the Pleene EasyRest™ Duvet“, grauhaariger Mann ca. 50 im Karo-Pyjama. [GH](https://app.gethookd.ai/share/ad/136388705?signature=59cb41d55414e96286187aee0b49252cfc352ad2e8b678704364f32e28cbf745) · [Meta](https://www.facebook.com/ads/library/?id=2167721337409320)
- 136389753 (Static, 88 T): Wärmebild „Cool Duvet, Not a Sweat Duvet! The original Pleene EasyRest™ Duvet … The difference is measurable. Normal Duvet vs Pleene EasyRest™ … 10,000+ happy customers“. [GH](https://app.gethookd.ai/share/ad/136389753?signature=c11710ed0494a2be2e0de04459119cb94adb1abe7eb43daeb71696d9f786eaca) · [Meta](https://www.facebook.com/ads/library/?id=1496288965315983)
- 136389942 (Video, 42 T, 20 Varianten): „No more bed changing ❌ / Changing your bed is one of the most pointless time-wasters in the house“. [GH](https://app.gethookd.ai/share/ad/136389942?signature=5b0ab8b6147634fe5ba59e7d5acd104c90c5e8bdab91aa519a0d58a56b44bc1f) · [Meta](https://www.facebook.com/ads/library/?id=2123958901533050)

---

### 5. Alle Angles (aktiv und letzte ca. 3 Monate)

| Angle | Gewicht | Belege (wörtlich, Ad-ID) |
|---|---|---|
| **Kein Bezug mehr / Bettbeziehen-Frust** | ★★★★★ Kern | „No More Fighting With Duvet Covers“ (Standard-Headline auf ca. 20+ aktiven Ads); „🐙 Every wash day, my duvet cover turns into an angry octopus. Eight corners, none of them where they should be.“ (184134597, [GH](https://app.gethookd.ai/share/ad/184134597?signature=2b680d992f53e9489bd001330a9e608908df3f009b371ab2cf0e14275970f411) · [Meta](https://www.facebook.com/ads/library/?id=4249373995353335)); „I bloody hate changing the bed, not the sheets, that bit, the bit where the cover fights back.“ (184134597); „Changing your bed is one of the most pointless time-wasters in the house“ (136389942) |
| **Ganze Decke waschbar / normale Maschine / kein Waschsalon** | ★★★★★ | „No Launderette Needed. Ever.“ (178749258); „Still carrying your duvet to the launderette? … Normal 7kg machine at home. Whole duvet in.“ (184134603, [GH](https://app.gethookd.ai/share/ad/184134603?signature=04b974bad08fcb96f3f92cbac23fbe1adcf3ad40c7f37386edc5739c4519b6a2) · [Meta](https://www.facebook.com/ads/library/?id=1597178745488191)); „Yes, It Fits Your Machine“; Kommentar-Reply „janetfl.59: How do you wash it when you can't take the cover off?😅“ (169082936, [GH](https://app.gethookd.ai/share/ad/169082936?signature=3fc943823fe63b987d5bbedae0519a360c2b37140ce39fb729bcd9e379af0519) · [Meta](https://www.facebook.com/ads/library/?id=1403346028405151)) |
| **Quick-Dry „dry in 2 hours“** | ★★★★★ (in fast jeder Copy) | „wash it whole, dry in 2 hours, throw it back on“ (163921089); „dries in 2 hours even without a dryer“ (171191667) |
| **Winterwärme / „zu dünn?“-Einwand (10.5 TOG)** | ★★★★ seit 05.09., wachsend | „Warm Enough For A British Winter“; „No way that keeps you warm in a Scottish winter.“; „❄️ Too thin for winter? Look closer. ✓ Quilted in place, no cold spots“ (200037058, [GH](https://app.gethookd.ai/share/ad/200037058?signature=8b9260efa8d3e451a50636127320d32fc1789291c109321c5b496c3192bfb0e4) · [Meta](https://www.facebook.com/ads/library/?id=2388197505255466)); „This survives a British winter. And your washing machine.“ (178749244, [GH](https://app.gethookd.ai/share/ad/178749244?signature=e82eedb3d5627dfcb853ac65f9f4001d15d3830da366355715ee051dfd039d1d) · [Meta](https://www.facebook.com/ads/library/?id=1554811692528015)) |
| **Hygiene (Schweiß, Hautschuppen, Milben, „when did you last wash it?“)** | ★★★★ | „Sorry, but your duvet is probably the dirtiest thing in your bedroom“ (133366534, 193234224); „Be honest. When did you last wash it?“ (185228767, [GH](https://app.gethookd.ai/share/ad/185228767?signature=d4a01baf409b9ddc41f60bfabb36d11b1b0037cf0db9af90a7ff2251278f24be) · [Meta](https://www.facebook.com/ads/library/?id=947904747867427)); „🛏️ If a guest asked you when you last washed your duvet, not the cover, the duvet, what would you say?“ (200037062, [GH](https://app.gethookd.ai/share/ad/200037062?signature=cda1bc0bd9028c69d9fba9351c6e6030713ed82bd1d77fc8a1574dafccc5ec75) · [Meta](https://www.facebook.com/ads/library/?id=1426769122930670)); „“The cover keeps the duvet clean.” Really? Look inside.“ (184134596, [GH](https://app.gethookd.ai/share/ad/184134596?signature=a4195f16ec3a5a353e03ee2a4c3f1b6bce8ce4c15e281538b19b5e45849f727b) · [Meta](https://www.facebook.com/ads/library/?id=1844350933397173)) |
| **Ältere / Mobilität / Schmerz / Selbstständigkeit** | ★★★★ seit Ende Sep. stark ausgebaut | „I'm not going to lie, at my age, changing the bed had become a real struggle. All that bending and reaching…“ (200490716, AI-Seniorin ca. 65–70, [GH](https://app.gethookd.ai/share/ad/200490716?signature=f9af223b680c0ee04bd5687c44ba0fd8ca69eace21b5373ed6b6f893022689ff) · [Meta](https://www.facebook.com/ads/library/?id=2233952628001235)); „Bedding Made for Independence – Why wait for someone else to help with your bedding?“ (200490718, [GH](https://app.gethookd.ai/share/ad/200490718?signature=38b5623f18087b0df4c2c1716eb5005dc8644f32545bafb73badcec66bf77774) · [Meta](https://www.facebook.com/ads/library/?id=969394622234742)); „You can still take care of your own bed.“ (189550269, [GH](https://app.gethookd.ai/share/ad/189550269?signature=f3ebac77a9aabd296cb1e960812c63aa60881f30e0da69bded7fc73cec4371e1) · [Meta](https://www.facebook.com/ads/library/?id=2239984750193672)); „Change Your Bed Without The Pain After“ (184134601, [GH](https://app.gethookd.ai/share/ad/184134601?signature=f324617c96ac3410786e53ebffab6b89603f171280b705764cbded88f0d71dad) · [Meta](https://www.facebook.com/ads/library/?id=1094904756318997)); „A Winter Duvet You Can Actually Lift“ mit Overlay „I'm 83“ (184134602, [GH](https://app.gethookd.ai/share/ad/184134602?signature=d2740a7f2a1172b621d9dfe802a913d4a649abb13541a1a7a0b6034cfa223dfc) · [Meta](https://www.facebook.com/ads/library/?id=1153825353859983)); „My back just can't take this anymore.“ (200490722, [GH](https://app.gethookd.ai/share/ad/200490722?signature=dd70cdeb1b3f44685b65dd999b089fa20ba19c1b6db90d019468210a9539d0a1) · [Meta](https://www.facebook.com/ads/library/?id=1103563399362311)); Senior-Static „No Cover. No Corners. No Fuss.“ (190288324, Mann ca. 75, [GH](https://app.gethookd.ai/share/ad/190288324?signature=48aa562c5319cf72520957009999b67df783221b6bb58928f7e9f3e92219e0b3) · [Meta](https://www.facebook.com/ads/library/?id=1124276960537017)) |
| **Enkel / Gäste** | ★★ | „🛏️ The grandchildren are coming to stay this weekend, and the spare bed is already done: whole duvet washed this morning, not just the cover.“ (200037059, [GH](https://app.gethookd.ai/share/ad/200037059?signature=59009cf51aaea1c606c359bf3dde2a7411fd0a4e972af70643b9fad86da60902) · [Meta](https://www.facebook.com/ads/library/?id=1762566964862159)) |
| **Haustiere** | ★★ (neu 05.10.) | „🐾 Bella sleeps on our bed every night. And nobody worries about it, because the WHOLE duvet goes in the wash, not just the cover.“ (200037063, [GH](https://app.gethookd.ai/share/ad/200037063?signature=59e1350bb940afa8ce2ef4db6bc9f0dc9c3d58b5363f4541de87c32b08c94beb) · [Meta](https://www.facebook.com/ads/library/?id=1667265245004008)) |
| **Heiß/kalt, Ganzjahr, Temperatur** | ★★★ (im Sommer Lead, jetzt Bullet) | „✓ Pleasantly cool in summer, cosily warm in winter“ (Standard-Copy); Wärmebild „Cool Duvet, Not a Sweat Duvet!“ (136389753); „Heatwave Sale - ends today!“ (136390020, Juli, [GH](https://app.gethookd.ai/share/ad/136390020?signature=43bb77aaa3c476ecf22789be539884c3fee2eddcb6c104f3548e5ea8d2d92c24) · [Meta](https://www.facebook.com/ads/library/?id=2077394283142508)); „David, 58: My wife runs cold and I run hot.“ (PDP) |
| **Farbe / Knappheit / Neuheit** | ★★★★ | „Hearth Red. Nearly gone.“, „Mint Green is almost gone.“, „Everyone's buying the blue one.“, „NEW: Lavender Mist. Our newest colour, as a limited edition.“ (185228766, [GH](https://app.gethookd.ai/share/ad/185228766?signature=f4be2b097e5b58bb0f5013dc8e461a8cea74051b0e8dfd5a28059f540eaf99fb) · [Meta](https://www.facebook.com/ads/library/?id=1401480008764681)); „Pick a colour. Watch what happens. In the video: 8 duvets, 1 empty bed…“ (200490708, [GH](https://app.gethookd.ai/share/ad/200490708?signature=c478fee5f2f2b1906248ac292415fd4e4fb6b49899a564cd74f30be3cf28ac09) · [Meta](https://www.facebook.com/ads/library/?id=1410624373895542)) |
| **Engagement-Bait** | ★★ | „One colour has to go before winter. Which one? 👇“ (Grid 1–9, „Which Colour? Comment 1-9“, 178749246, 21 T, [GH](https://app.gethookd.ai/share/ad/178749246?signature=b56865ebc78f16250b8cbd28c54179f6839f72542e1c273bd2c8af04495a5e78) · [Meta](https://www.facebook.com/ads/library/?id=1940045106690283)) |
| **Social Proof / Testimonial** | ★★★ | „Everyone said it. They were right.“; „“Got 3, love them.” — Customer, back for the third time.“ (193234278, [GH](https://app.gethookd.ai/share/ad/193234278?signature=2acfe25ae18b9ee3fd409e989a071bce595dea12e1dca232a03824238d38b557) · [Meta](https://www.facebook.com/ads/library/?id=1103531258742413)); „Moira M. Warm duvets are always a nightmare to wash.“ (Kommentar-Overlay, 178749264, [GH](https://app.gethookd.ai/share/ad/178749264?signature=d8e08fd7024ff622ab3eacbab2d56418953b6cce8719c355c54bb885d2941843) · [Meta](https://www.facebook.com/ads/library/?id=832047280000629)); Link-Description „⭐️⭐️⭐️⭐️⭐️ – Over 10,000 Happy Customers“ |
| **Kaufberatung / Myth vs Truth / Größe** | ★★★ | „Check This Before You Buy“; „Myth: Changing the bed has to be a struggle. 🛏️ Truth: With the Pleene EasyRest™ there's nothing to change.“ (173929415, [GH](https://app.gethookd.ai/share/ad/173929415?signature=f0e1ccce27a60346510cf79fea8c03c205a409770a77094a35c9f7a4e9a2b927) · [Meta](https://www.facebook.com/ads/library/?id=1080653068157794)); „What bed have you got? … Single bed (3ft) → Single. Double bed (4ft6) → Double. King bed (5ft) → King.“ (182988091, [GH](https://app.gethookd.ai/share/ad/182988091?signature=d38f60d9788af1b85ef236ca2bc85df5cb3de0c4ac38b8240791e6ace576727a) · [Meta](https://www.facebook.com/ads/library/?id=1562707309236010)); „Now In Super King“ (185228765, [GH](https://app.gethookd.ai/share/ad/185228765?signature=fdc1176605c0f19ad51f2626b448a5fdfb307d0143360d07311941417feb5d0b) · [Meta](https://www.facebook.com/ads/library/?id=1107581421667412)) |
| **Paare** | ★ | „Still fighting over the duvet at 3am? You don't need to win. You need a bigger duvet.“ (145443340, 37 T, [GH](https://app.gethookd.ai/share/ad/145443340?signature=16e5742c4db77b5e7bba52412bce46bd9e1b48b5cf894d96de978e05ba364722) · [Meta](https://www.facebook.com/ads/library/?id=937322868660942)) |
| **Allergien / sensible Haut** | ★ (nur Bullet) | „✓ Hypoallergenic and kind to sensitive skin“ (Standard-Copy); PDP-FAQ „Is it suitable for allergy sufferers?“. Kein eigenes Allergie-Creative gefunden |
| **Schlafqualität** | ★ | nur am Rand (PDP-Review „Since buying and using I sleep better…“) |
| **Wechseljahre / Nachtschweiß** | – | **0 Treffer** (Suche „menopause“, „sweat“) |
| **Geschenk / Weihnachten** | – | keine Creatives gefunden |
| **Öko / Nachhaltigkeit** | – | keine Creatives gefunden |

---

### 6. Hook-Bibliothek (wörtlich)

**Spoken und Overlay (Video):**
- „Sorry, but your duvet is probably the dirtiest thing in your bedroom. Think about it. When did you last actually wash it?“ (133366534, 193234279, 193234275)
- „I haven't changed my bed linen in three months and it's never felt fresher.“ (163921089, 145443331, 193234221)
- „I bloody hate changing the bed“ / „…not the sheets, that bit, the bit where the cover fights back.“ (184134597, 145443318)
- „If your shoulders ache, don't do this. And if your back is sore, definitely don't do this.“ (136389861)
- „I only ordered it because changing the bed linen every time gave me pain in my shoulders and back.“ (151025063)
- „I'm not going to lie, at my age, changing the bed had become a real struggle.“ (200490716)
- „My back just can't take this anymore.“ (200490722)
- „I don't have a duvet cover anymore and honestly it was the best decision I ever made.“ (200490721, [GH](https://app.gethookd.ai/share/ad/200490721?signature=8697f9fa84603c6c5fe39198bba6510a3c6efe060e8c12de0cac95d04e13450e) · [Meta](https://www.facebook.com/ads/library/?id=2373725086706676))
- „Looks lovely, but you'll freeze under that in winter.“ / „No way that keeps you warm in a Scottish winter.“ / „Is it actually warm enough for winter?“ (178749251, 178749254, 178749247)
- „Before you buy a coverless duvet check 3 things“ (168246678)
- „Only 17 left in Hearth Red“ / „Everyone's buying it in Coastal Blue · Only 19 left“ (139561428, 139561491)
- „It took me four duvets to find one“ (178749241, [GH](https://app.gethookd.ai/share/ad/178749241?signature=6aeed07ee78eed5e22d99bb8187bd9d3d5d945249cf272ee3c10935ee517f838) · [Meta](https://www.facebook.com/ads/library/?id=986052237841995))
- „I haven't washed my bed linen in 6 months“ (169082944, Frau ca. 50, [GH](https://app.gethookd.ai/share/ad/169082944?signature=ccd7617745b1f844aa56ce5e2dd9e9fa2679a8a215c40a8d23d579a61d411b87) · [Meta](https://www.facebook.com/ads/library/?id=1063281430012872))
- „Why do all men in the United Kingdom love this duvet?“ (136389548)
- „After years of arguing with duvet covers,“ (184134601)
- „No more bed changing ❌ / Changing your bed is one of the most pointless time-wasters in the house“ (136389942)

**Static und Primärtext:**
- „3 things to STOP doing when you make the bed“ (136388964)
- „Just want to sleep… but you've still got to change the bed?“ (136388847)
- „“But you'd need a huge washing machine for that” 😂“ (171191667)
- „A light duvet can't keep you warm in winter." We hear it every autumn, and it's wrong.“ (172403389)
- „You wash the cover… but never the duvet inside.“ (133366116)
- „Change the bed in the summer heat / End up hot and sweaty / Now you need another shower“ (136390001)
- „❄️ Your winter duvet shouldn't need a launderette.“ (178749258)
- „You shower every night — then sleep under a duvet that's never been washed. Not because you're lazy: normal duvets don't fit normal machines. Ours does.“ (193234224, [GH](https://app.gethookd.ai/share/ad/193234224?signature=e67f0112dff4be83367fd2663a38a3c667a76a33044371dae7cb5e0307b1035b) · [Meta](https://www.facebook.com/ads/library/?id=1614086653522933))
- „Still carrying your duvet to the launderette?“ (184134603)
- „No Stuffing. No Shaking. Just One Duvet.“ (190288325, Frau ca. 50, [GH](https://app.gethookd.ai/share/ad/190288325?signature=5fb631c87cf69dc85e89d8b703b981cd94e212c894b87ecb72970ca5523d2b38) · [Meta](https://www.facebook.com/ads/library/?id=1348489960694867))
- „Only Until Friday! Never Change Bedding Again With the 2-in-1 Duvet“ (193234273, [GH](https://app.gethookd.ai/share/ad/193234273?signature=0ba2f670cf75a2cea80f69a0f1d518096f384fc05de8fe37422c55254a2856d1) · [Meta](https://www.facebook.com/ads/library/?id=2100922640555492))
- US: „Your Comforter Shouldn't Need A Field Trip.“ (182988040, [GH](https://app.gethookd.ai/share/ad/182988040?signature=70c523c1f926d7fd461c615515849a5b4da5e7a7cd0b682c0335da480ffd657a) · [Meta](https://www.facebook.com/ads/library/?id=2515261675637941)) · „Still Wrestling With Comforter Covers?“ (183445651, [GH](https://app.gethookd.ai/share/ad/183445651?signature=3af2be1a313fcc4887a0cd71ed59cf6121bb5f75f33757760103514ce37b379e) · [Meta](https://www.facebook.com/ads/library/?id=1640984024127964)) · „A fresh bed shouldn't mean waiting for a helping hand.“ (186893878, [GH](https://app.gethookd.ai/share/ad/186893878?signature=f232a426903d049b7b06b46c06d250fb7eea59242595dbbbfb87042d99c66827) · [Meta](https://www.facebook.com/ads/library/?id=28612939431667546))

**Avatar-Mix der Creatives:**
- Britische UGC-Männer ca. 30–40 (grünes Schlafzimmer, „bloody“).
- Frauen ca. 45–55 (UGC, Pyjama).
- **Senioren 65–83**, teils sichtbar **AI-generiert**: die Seniorin mit Brille (200490716 und das Heatwave-Video 136390020), der „TCM-Heiler“ mit Union Jack (136389861).
- Produkt- und Interieur-Videos ohne Menschen (Farb-Knappheit).
- **Auffällig:** Kein Avatar „Frau 48–63 in den Wechseljahren“. Das ist genau die MS-Kernzielgruppe mit 48–63-jährigen Testimonials.

---

### 7. Offers und Preise

| Element | Pleene UK | Magic Splashy DE (zum Vergleich) |
|---|---|---|
| Hauptangebot | **2 free Pleene™ Pillow Cases (worth £39.99)**: „This week only“, „Only Until Friday!“, „Autumn offer … while stocks last“ | 2 SoftCloud-Kissenbezüge gratis (49,99 €) |
| Rabatt | seit 16.09. in Ads **„30% off + 2 FREE matching pillow cases“**; PDP „SAVE 34%“ | Herbst-Aktion |
| Preis (PDP, GBP) | Narrow 90×200 **£74.99** (statt £114.99) · Single 140×200 £79.99 · Single XL 160×210 £84.99 · **Double 200×200 £89.99** (statt £139.99) · King 230×230 £119.99 · Super King 260×220 £129.99 | – |
| Trial / Garantie | **90-Night Home Trial**, „Money Back Guarantee“; Kleingedrucktes: Rückversand zahlt der Kunde, Decke muss „clean and resaleable“ zurückkommen | 40 Tage Probeschlafen |
| Versand | Gratis ab £100 (der Narrow-Single-Kauf liegt darunter) | – |
| Upsells im Warenkorb | Pillow-Cases £19.99, EasyRest™ Pillow £39.99, FluffBalls™ £14.99, Package Protection £2.99; „The Cosy Bundle“ Duvet + CosyRest™ Sherpa Throw £134.98 | – |
| Social Proof | Ads/PDP: „Over 10,000 Happy Customers“; PDP: „172 reviews“ (142× 5★, 29× 4★, gruppiert); Advertorial: „7,000+ customers“, „Excellent 4.7/5 on Trustpilot · 250 reviews“ | „17.000+ begeisterte Schläfer“ |
| Produktclaims | „10.5 TOG — proper winter warmth“, „Warm without overheating“, „Never change bedding again“, „Fits in every washing machine“, „Air dries in 2 hours“, „climate fibres“, King-Size wiegt 3.12 kg | ThermoBalance® Klimafasern, „in 2 Stunden an der Luft trocken“ |
| Sale-Events (Historie) | „Heatwave Sale - ends today!“ (Juli), „This week only“, Farb-Knappheit „Only 17 left“ | „nur bis Freitag“, „Herbst Aktion“, „nur noch 115 Stück“ |

---

### 8. Landingpages im Detail

**A) PDP `pleene.com/products/easyrest`** (abgerufen am 08.10., Template `easyrest-duvet-winter26`)
- **Hero:**
  - Banner „Cosy Season Is Here — Sleep Warm All Winter“ und „90 Nights Risk-Free — Try It In Your Own Bed“.
  - „172 reviews“, Preis £74.99 statt £114.99 mit „SAVE 34%“.
  - Bullets: „✔️ 10.5 TOG — proper winter warmth / ✔️ Warm without overheating / ✔️ Never change bedding again / ✔️ Fits in every washing machine / 🎁 Free with every duvet today 2 Pleene™ Pillow Cases (Value: £39.99)“.
  - „Ready to Ship – Limited Stock“. Zahlarten: Klarna, PayPal, Apple Pay.
- **Einwand-Akkordeons:**
  - „What is the TOG rating?“
  - „Does the Pleene™ duvet fit in my washing machine?“ mit der Antwort „A feather-filled king duvet weighs 4–6 kg … Ours weighs 3.12 kg“.
  - „It looks thin — is it really warm enough?“
- **Video-Testimonials:** „Peter / Brian / Dave ✓ Verified buyer“.
- **Testimonials mit Alter:**
  - „Margaret, 67 – At my age, wrestling a duvet into its cover was such a struggle. This is an absolute godsend — I can make my bed on my own again.“
  - „James, 55“, „Sarah, 41“, „Robert, 50“, „David, 58“.
  - Damit kopiert Pleene das MS-Muster mit Testimonials von 48–63-Jährigen und verschiebt es leicht älter.
- **Reviews:** Mehrere Reviews nennen **lange Lieferzeiten**, z. B. „Only problem it took a long time for the order to arrive.“ Einige sprechen Behinderung oder Unfallverletzungen an, z. B. „Having a disability there is less effort making my bed“.
- **Footer:** One Way Ecom Ltd. (Hongkong), Werbung über 21Commerce Ltd.

**B) Advertorial `pleene.com/pages/tb-6`** (seit 01.10. in 8 Ads)
- Kopf: „Advertisement“, dann „"Never change your bed linen on a Sunday again"“ und „How 7,000+ people said goodbye to putting duvet covers on – with a machine-washable 2-in-1 duvet“.
- Trust- und Vorteilsleiste: „Excellent 4.7/5 on Trustpilot · 7,000+ customers“, „No more putting covers on / Not too warm, not too cold / Fits any washing machine / Dry in about 2 hours“.
- Vergleichstabelle „EasyRest vs. classic bed linen“.
- Angebot: „Autumn offer – 2 matching pillowcases free … Worth £39.99 – while stocks last.“
- FAQ, 90-Nächte-Box, Disclaimer („Some images on this page were created or edited with the help of AI“).
- Die Struktur sieht aus wie ein übersetztes deutsches Advertorial: deutsche Satzstellung, „at 40°“, „Air-dries in 2–3 hours“.

---

### 9. Was direkt von Magic Splashy kopiert ist

| # | Pleene (UK) | Magic Splashy (DE) | Bewertung |
|---|---|---|---|
| 1 | **Primärtext** (Standard auf ca. 20+ aktiven und hunderten inaktiven Ads): „Duvet + Cover in One 🌙 The Pleene EasyRest™ makes changing the bed finally simple. Wash it, dry it, and lay it back on — that's it. ✓ No more wrestling with a separate duvet cover ✓ Pleasantly cool in summer, cosily warm in winter ✓ Hypoallergenic and kind to sensitive skin Get 2 free Pleene™ Pillow Cases today (worth £39.99). 90 nights to try it risk-free. Enjoy a bed that always feels fresh.“, z. B. 136388964 | „Decke + Bezug in einem 🌙 Die EasySleep Bettdecke macht Bettmachen endlich einfach. Waschen, trocknen und wieder aufs Bett legen. ✓ Nie wieder Ärger mit Überzügen ✓ Angenehm kühl im Sommer, wohlig warm im Winter ✓ Hypoallergen und antibakteriell Heute 2 SoftCloud Kissenbezüge gratis (49,99€ Wert) sichern. 40 Tage risikofrei probeschlafen. Genieße endlich ein Bett, das immer frisch ist.“, MS 177828057 [GH](https://app.gethookd.ai/share/ad/177828057?signature=3b67965984efc2f5e64fcfc8e9e4e27fe49bf473d88b8e760978d4664fbf1b08) · [Meta](https://www.facebook.com/ads/library/?id=936438562360509) | **1:1 übersetzt** (nur SoftCloud wird zu „Pleene™ Pillow Cases“, 40 Tage zu 90 Nächten, € zu £) |
| 2 | Headline „No More Fighting With Duvet Covers“ | „Nie wieder Bettwäsche wechseln 🛏️“ | sinngemäß übernommen |
| 3 | Video-Overlay „No more bed changing ❌ / Changing your bed is one of the most pointless time-wasters in the house“ (136389942, 20 Varianten, 42 T); gleicher Overlay-Stil „No more bed changing ❌“ auch auf 193234279 | MS-Winner „Nie wieder Bettbeziehen ❌“ mit Spoken-Hook „Bettbeziehen ist einer der sinnlosesten Zeitfresser im Haushalt. Und trotzdem machst du es jede Woche, bis jetzt.“ (MS 129130363, Spend $10–20 k, [GH](https://app.gethookd.ai/share/ad/129130363?signature=2280883cdc1b06d68811f8455bca14dbebe3878407f4246090cb2afb6c5c467c) · [Meta](https://www.facebook.com/ads/library/?id=1534211127599850)) | **Skript und Overlay 1:1**, neues Footage |
| 4 | Video 193234224: „Sorry, but your duvet is probably the dirtiest thing in your bedroom 🤢 / Your duvet doesn't fit in the washing machine / So it stays unwashed. Sweat. Dust mites. 🤢 / Only the cover gets changed. The same ritual every week:“ und Copy „You shower every night — then sleep under a duvet that's never been washed.“ | MS 139052723: „Du duschst jeden Abend. Und legst dich danach unter eine Decke, die du noch nie richtig gewaschen hast 🤮 / Deine Bettdecke passt nicht in die Waschmaschine. / Also bleibt sie ungewaschen. Schweiß. Milben. 🤢 / Nur der Bezug wird gewechselt. Jede Woche dasselbe Ritual: / Bezug ab. Ecken suchen.“ ([GH](https://app.gethookd.ai/share/ad/139052723?signature=896c7500a00ec5ed474ea18d14e007ff27a9cea881361be3ad541baf859aa9ed) · [Meta](https://www.facebook.com/ads/library/?id=2182272402331336)) | **1:1 übersetzt**, auch Emojis und Zeilenumbrüche; ähnliches Setup mit glatzköpfigem älterem Mann |
| 5 | „I ordered the Pleene EasyRest™ Duvet“ (136388705), „I only ordered it because …“ (151025063, 163921089, 169082943) | „Ich hab die EasySleep Decke bestellt, weil ich einfach keinen Bock mehr hatte, jede Woche mit der Bettwäsche zu kämpfen.“ (MS 126012757, $10–20 k, [GH](https://app.gethookd.ai/share/ad/126012757?signature=4aa5cf75157a813c3daede61927240a452d4bf09046a0feee9ae288bd457658f) · [Meta](https://www.facebook.com/ads/library/?id=1572451867734657)) | Hook-Template übernommen, Begründung lokalisiert (Schmerz bzw. „everyone said“) |
| 6 | „Only Until Friday!“ + „+ 2 FREE Pillow Cases“ (193234273) | „nur bis Freitag: Kissenbezüge GRATIS“ (MS 196671940, [GH](https://app.gethookd.ai/share/ad/196671940?signature=10e6c6facf34e98d7925e46eefb275bd3d896bdd1ef29852fb206cf1b52784f7) · [Meta](https://www.facebook.com/ads/library/?id=1732107347870709)) | Offer-Mechanik 1:1 |
| 7 | Farb-Knappheit: „Only 17 left in Hearth Red“, „Mint Green is almost gone.“, „NEW: Lavender Mist … limited edition“ | „Achtung: Fliedertraum ist bald vergriffen — nur noch 115 Stück auf Lager.“ (MS 196670846, [GH](https://app.gethookd.ai/share/ad/196670846?signature=b5b9b284d73a12e15630ec2c558b9dbfe8aca6bc097ccb8c627b5a352ed912ab) · [Meta](https://www.facebook.com/ads/library/?id=1110255681373443)) | gleiche Mechanik; Pleene fährt Farb-Knappheit seit 07.08., das gefundene MS-Beispiel ist vom 02.10. Wer das Format zuerst hatte, ist offen |
| 8 | „The grandchildren are coming to stay this weekend, and the spare bed is already done“ (200037059) | „„Die perfekte Decke fürs Oma-Wochenende““ (MS 144478362, [GH](https://app.gethookd.ai/share/ad/144478362?signature=f01b296a5e9835e1914523318bf370bfb0cd2b61fc8b07e8a749f31c04309c80) · [Meta](https://www.facebook.com/ads/library/?id=1783791422616725)) | Angle übernommen |
| 9 | Wärmebild „Cool Duvet, Not a Sweat Duvet! The original Pleene EasyRest™ Duvet“ (136389753) | „EISDECKE STATT SCHWITZDECKE!“ (MS 112079984, [GH](https://app.gethookd.ai/share/ad/112079984?signature=b1039ced43faa632883446506b949c75ff5b2bf5aab7d2e90f032f6002ba9bdc) · [Meta](https://www.facebook.com/ads/library/?id=971243182189865)) und Link-Description „Das Original- MagicSplashy“ | Headline-Formel und „Original“-Claim übernommen |
| 10 | Quote-Statics „“It's what I've been looking for all this time!” — Customer, UK“, „“Got 3, love them.”“ | „“Ich hab Bettwäsche gestrichen.” Decke + Bezug in EINEM.“ (MS 148248622, [GH](https://app.gethookd.ai/share/ad/148248622?signature=84d901c24974a36d3944f48f20a4e49c67491a96f0afc5eac2f108a8698f93ac) · [Meta](https://www.facebook.com/ads/library/?id=1772920517246961)) und „Unsere Kunden in 3 Worten“ (MS 179252420, [GH](https://app.gethookd.ai/share/ad/179252420?signature=b705ffb54efd1b5a03448c8012cc9821cb489e17ae0193cf7888c47b270547f2) · [Meta](https://www.facebook.com/ads/library/?id=1820936862425780)) | Format ähnlich |
| 11 | **Claims:** „dry in 2 hours“ / „Air dries in 2 hours“ · „climate-regulating fibres“ / „EasyRest climate fibres“ · „Not too warm, not too cold“ · „Fits in every washing machine“ · „Over 10,000 Happy Customers“ | „in 2 Stunden an der Luft trocken“ / „in 2h trocken - auch im Winter“ · „ThermoBalance® Klimafasern“ · „Kein Schwitzen. Kein Frieren.“ / „kein schwitzen, kein frieren“ · „passt komplett in die Waschmaschine“ · „17.000+ begeisterte Schläfer“ | Claims übersetzt; **die Markennamen „SoftCloud“ und „ThermoBalance“ sowie die Zahl „17,000“ übernimmt Pleene nicht** (0 Treffer) |
| 12 | Verdacht, ohne MS-Treffer in der Suche: Text-Meme „“But you'd need a huge washing machine for that” 😂 That's what I thought too. The truth: …“ (171191667) und „Why do all men in the United Kingdom love this duvet?“ (136389548) | typische DE-DTC-Templates („Das dachte ich auch. Die Wahrheit:“, „Warum lieben alle Männer in Deutschland…“) | wahrscheinlich aus DE übersetzt, Quelle nicht verifiziert |
| 13 | Größen in cm, darunter für UK untypische Größen „90 × 200 cm (Narrow)“ und „160 × 210 cm (Single XL)“ | EU-Katalog | Sortiment wirkt aus EU übernommen |

**Fazit Kopien:** Pleene hat das MS-Grundgerüst vollständig übernommen: Primärtext, Gratis-Kissenbezüge, Hygiene-Skript, „Zeitfresser“-Skript, „Ich hab bestellt“-Hook, Knappheit, Oma/Enkel und „Original“-Claim. Seit September lokalisiert Pleene stark (TOG, Waschsalon, britischer Slang, Senioren-Independence). **MS-Angles, die Pleene noch nicht übernommen hat:** Wechseljahre („5 Gründe, warum deine Decke in den Wechseljahren ein Upgrade braucht“, MS 196672418, [GH](https://app.gethookd.ai/share/ad/196672418?signature=2b67f5aeb5f32132de99b2807b254c0eb9516022333d03d75b13ab66c8ad5d12) · [Meta](https://www.facebook.com/ads/library/?id=4683073511929128)), „Herbst Aktion … eine Decke fürs ganze Jahr“ (MS 196672379, [GH](https://app.gethookd.ai/share/ad/196672379?signature=28de600475fe69fdf3bc9e39456dc0b85fde1cecf081ffed9e0141b9ea07b385) · [Meta](https://www.facebook.com/ads/library/?id=1817806592873693)), „Unsere Kunden in 3 Worten“.

---

### 10. Chancen für unseren Kunden (UK „first mover“ gegen Pleene)

1. **Wechseljahre und Nachtschweiß** für Frauen 48–63 besetzen. Das ist der MS-Kern-Avatar, und Pleene hat dort 0 Ads. Mögliche Hook-Richtung: „Kein Schwitzen. Kein Frieren.“ übertragen auf Hitzewallungen nachts.
2. **Allergie und Hausstaubmilben als Lead-Angle**, nicht nur als Bullet. Pleene erwähnt Milben nur im Hygiene-Kontext.
3. **Geschenk-Angle** für Weihnachten und Muttertag, etwa als Geschenk für die Eltern oder Großeltern („Independence“ für Senioren). Pleene hat dazu nichts.
4. **Vertrauen gegen Pleenes Schwächen ausspielen:** UK-Lager und Lieferzeit (Pleene-Reviews klagen über Wartezeit, Betreiber in Hongkong), kostenloser Rückversand (bei Pleene zahlt der Kunde), konsistente echte Kundenzahl.
5. **Offer-Benchmark:** Mindestens 90 Nächte und Gratis-Kissenbezüge sind in UK schon Standard. Pleene liegt bei £74.99 bis £129.99 mit „30% off“; Double kostet £89.99.
6. **Advertorial und Listicle früh aufbauen.** Pleene testet erst seit 01.10. ein Advertorial (tb-6) und hat noch kein Quiz und kein Listicle.

---

### 11. Methodik und Einschränkungen

- **Daten:** GetHooked `search_ads` (brand_id 7553008, status active mit 137 Zeilen bzw. inactive mit 555), `aggregate_ads`, `get_shop_landing_pages`, `get_domain_advertisers`, `get_ad` (Transkript 136389861) sowie das Feld `hook` für Spoken Hooks. Magic Splashy wurde zum Abgleich über brand_id 88310 durchsucht.
- **Performance:** EU-Reach und Spend sind für Pleene nicht verfügbar (UK ist nicht DSA-pflichtig). Das Ranking basiert auf GetHookd-performance_score, Laufzeit und Varianten-Skalierung.
- **Klassifizierung:** Die Taxonomie-Felder (cls_angle u. a.) sind für Pleene kaum befüllt (1 Ad). Angles und Avatare sind deshalb manuell aus Copy, Hooks und Thumbnails abgeleitet. „AI-generiert“ ist eine visuelle Einschätzung.
- **Transkripte:** Das Spoken-Hook-Transkript von 145443318 wurde als Walisisch erkannt („Oh, rydw i wedi gwneud…“). Das ist vermutlich eine Fehl-Erkennung des britischen Akzents.
- **Copy-Abgleich:** Der MS-Abgleich per Volltext erfasst nur Primärtexte und Spoken Hooks, keine Bild-Overlays. Die Kopien bei Statics (#10, #12) sind deshalb teils visuell bzw. als Verdacht eingestuft.



# D3 Cozily (UK)

## Cozily (UK) – Wettbewerbsanalyse: Meta-Ads & Funnel

Stand: 08.10.2026 · Quelle: GetHooked (MCP) und eigener curl der Landingpages · Analyst-Notiz für das Projekt „Magic Splashy als Erste nach UK bringen“

Linkformat je Ad: **GH** = GetHooked-Share-Link · **Meta** = Meta Ad Library (`https://www.facebook.com/ads/library/?id=<external_id>`)

---

### 0. TL;DR – das Wichtigste in 10 Punkten

1. **Cozily ist ein 1:1-Klon von Magic Splashy für UK und seit Ende September auch für die USA.** Produktname **EasySleep®**, Gratis-Beigabe **SoftCloud®-Kissenbezüge (Wert £49,99)**, **„ThermoBalance® fibres“**, **„No sweating, no freezing“** (= „Kein Schwitzen. Kein Frieren.“), **40-Nächte-Probeschlafen**, **„17,000+“**, Testimonials mit Altersangabe. Der **Primärtext aller 537 UK-Ads ist eine wörtliche Übersetzung** des MS-Haupttexts „Decke + Bezug in einem 🌙 …“.
2. **Betreiber laut Impressum: Guangzhou Lingcai Technology Co., Ltd. (China)**, Kontakt über eine Gmail-Adresse. Laut Shipping-Policy beträgt die Lieferzeit **6–9 Werktage**. Die Refund-Policy schließt **benutzte Ware aus Hygienegründen von der Rückgabe aus**, was dem beworbenen 40-Nächte-Probeschlafen widerspricht. Das ist der größte Angriffspunkt für unseren Kunden: UK-Lager, schnelle Lieferung und ein echtes Probeschlafen.
3. **552 aktive Ads** auf genau **einer FB-Page („Cozily Store“, ID 1164186490110671)** und genau **einer Domain (cozily-shop.com)**. Die Domain ist seit dem **10.07.2026** im Einsatz, die ganze Historie ist also rund 3 Monate alt.
4. **Formate: 348 Statics (63 %) und 204 Videos (37 %).** Es gibt keine Carousels und keine DCO. Jede Static-Idee läuft in mehreren Seitenverhältnissen (9:16, 4:5, 1:1) als eigene Ad.
5. **Landingpages: 87 % ein langes Advertorial** (`/pages/advertorial`, 467 Ads), **13 % die Produktseite** (70 Ads). Dazu kommen **15 US-Ads** auf `/pages/advertorial-easysleep-usa` (Wort „comforter“ statt „duvet“, $).
6. **Launch-Kadenz: aggressiv.** Im Schnitt kommen **~50 neue Ads pro Woche** dazu, in Batches von 15–41 Ads an einzelnen Tagen. Die Spitze war **KW 40 mit 84 Ads** (allein 41 am 30.09.).
7. **Die stärksten Ads (Performance-Score 64 = Maximum im Account) haben drei Muster.** Erstens **KI-generierte UGC-Talking-Heads mit Männern und Frauen 55–70** („I need to publicly apologize…“, „I'm 63 and…“). Zweitens **wiederverwendetes deutsches MS-UGC-Footage** mit englischen Captions („I ordered the EasySleep duvet“). Drittens **Overstock-/Lagerverkauf-Statics** („We've made too many. Help us clear them.“).
8. **Seit Mitte August ist das Angebot auf „40 % off + 2 free pillowcases“ umgestellt.** Davor lief „UP TO -36%“ bzw. „SAVE 35%“. Erzählt wird es als **Lagerräumung, Überproduktion oder Entschuldigung**. Auf der Seite stehen tatsächlich nur **29–36 %** (Single £69,99 statt £109,99).
9. **Zielgruppe ist klar 50+.** Darauf zahlen ein: „Perfect for those aged 55+“, „Ideal for carers“, ein Witwer in den Achtzigern als Testimonial, „Mum – no more fighting with the cover“, „Light enough to carry one-handed“ und „Karen, 52“.
10. **Lücken, die Cozily noch nicht besetzt, MS aber in DE gerade testet:** Wechseljahre und nächtliches Schwitzen bei Frauen (MS 196670813), Gelenke/Arthrose (MS 196670581), „5 Gründe“-Listicle-Video (MS 196671368) und den Einwand „Ist sie warm genug im Winter?“ (MS 196670101). Diese Ideen sollte unser Kunde in UK **vor Cozily** launchen.

---

### 1. Identifikation: Brand, Pages, Domains, Betreiber

| Feld | Wert |
|---|---|
| GetHooked-Brand | **Cozily Store**, brand_id **11837492** (`search_brands "cozily"` liefert genau 1 Treffer) |
| Facebook-Page-ID | **1164186490110671** · Ad Library: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=GB&view_all_page_id=1164186490110671 |
| Domain | **cozily-shop.com**. Laut `get_domain_advertisers` ist das der einzige Advertiser, mit 552 aktiven Ads, first_seen **10.07.2026** |
| Weitere Pages/Domains | Keine gefunden. `list_shops q="cozily"` liefert nur Curly-Hair-Shops, cozily-shop.com ist nicht im GetHooked-Shop-Katalog. |
| Shop-System | Shopify, Theme „Shrine“. Produkt angelegt am **13.06.2026**. Märkte: UK (GBP) und USA (USD) |
| Impressum (`/policies/legal-notice`) | **Guangzhou Lingcai Technology Co., Ltd.**, Room 506, No. 805 Xicha Road, Baiyun District, Guangzhou, China. Registrierungsnr. 91440111MAEUD1DM6F. E-Mail: contact.elina99@gmail.com. Das Template zitiert das italienische Decreto 70/2003, ist also ein kopiertes Rechtstext-Template. |
| Länder laut GetHooked | `countries` ist leer, weil UK/US keine EU-Transparenzdaten liefern. UK ergibt sich aus £-Copy, britischer Wortwahl („launderette“, „airing cupboard“, „tog“) und GBP. **15 Ads zielen auf die USA** ($, „comforter“, CTA LEARN_MORE). |
| CTA | UK: **SHOP_NOW** · US: **LEARN_MORE** |

---

### 2. Aktive Ads & Formate

- **Aktive Ads: 552** (Brand-Counter und `aggregate_ads`). Alle 552 sind über `search_ads` einzeln enumeriert.
  - **537 UK-Ads**, alle mit **identischem Primärtext** (414 Zeichen, siehe unten)
  - **15 US-Ads** (Start 27./28.09.2026) mit US-Variante des Texts
- **Format-Split** (`aggregate_ads group_by=display_formats`): **Image 348 / Video 204**. Es gibt keine Carousel-, DCO- oder DPA-Ads.
- GetHooked hat die Creatives dieses Accounts noch nicht klassifiziert (`cls_angle`, `cls_video_format` usw. sind leer). Die folgende Kategorisierung habe ich **manuell** aus ca. 120 gesichteten Creatives (Bilder und Hook-Frames) und 11 Video-Transkripten abgeleitet.
- Inaktive bzw. gestoppte Ads sind in GetHooked nicht indexiert, weil die Brand nicht gespied ist. **Wir sehen also nur die überlebenden Ads, nicht die Verlierer.**

**Primärtext UK** (alle 537 Ads, wörtlich):
> Duvet + Cover in One 🌙
>
> The EasySleep duvet makes making your bed effortless. Simply wash it, dry it, and place it straight back on your bed.
>
> ✓ No more struggling with duvet covers
> ✓ Comfortably cool in summer, cosy and warm in winter
> ✓ Hypoallergenic and antibacterial
>
> Get 2 SoftCloud pillowcases FREE today (worth £49.99).
>
> Enjoy a 40-night risk-free trial.
>
> Finally experience a bed that always feels fresh. ✨

**Primärtext US** (15 Ads, z. B. 190558622):
> Comforter + Cover in One 🌙 … The EasySleep® comforter makes making your bed effortless. Simply wash it, dry it, and put it straight back on your bed. ✓ No more struggling with comforter covers ✓ Comfortably cool in summer, cozy and warm in winter ✓ Hypoallergenic and antibacterial … Get 2 SoftCloud pillowcases FREE today (worth $49.99). Enjoy a 40-night risk-free trial. …

**Creative-Typen (manuell):**

| Typ | Beschreibung | Beispiele |
|---|---|---|
| KI-UGC-Talking-Head (Video) | Generierte „Testimonial“-Avatare, überwiegend **Männer und Frauen 55–70**, Selfie-Perspektive, Schlafzimmer-Setting, Untertitel | 188679985, 188681961, 188368675, 187361100, 190558325, 189724348, 189399825 |
| Wiederverwendetes MS-/DE-UGC (Video) | Echte Creator (deutsch wirkend), die englische Captions und ein englisches Voiceover bekommen haben | 189724357, 189724449, 190139667, 189399853, 189724373, 189724320, 190147133 |
| Produkt-Demo / B-Roll (Video) | Decke wird aufs Bett geworfen oder glattgestrichen, Text-Overlay, Hook-Caption „i ordered the EasySleep duvet“ | 190139671, 189399939, 189726663, 190147104 |
| KI-Szenen (Video) | z. B. Laden-Szene, streitendes Paar | 189722200, 189396916 |
| Text-on-Product (Static) | Headline + Produkt, oft mit Checkliste und Badge („+2 free SoftCloud pillowcases“, „40-night money-back guarantee“) | 189724500, 189399860, 190139665, 190558332 |
| Us-vs-Them / Vergleich (Static) | „A normal duvet vs this one“, „Two duvets. One obvious winner.“, „Why buy three…“ | 189397059, 189397035, 190558332 |
| Lagerverkauf / Overstock (Static) | Warehouse, Paletten, Pappschild, „-40%“-Tags | 189397232, 189723854, 189399854, 190558231, 190175678, 190558901 |
| Testimonial-Karte (Static) | Frau 50+ mit Zitat und Altersangabe | 189734435, 189726176, 190147077 |
| Minimal-Premium-Serif (Static) | Text-only oder ruhiges Interieur | 189398761, 190146305, 190558960 |
| Mockups | Bushaltestellen-Plakat, Whiteboard-Skizze, Grußkarte auf dem Bett | 189734456, 190175692, 190140600 |

---

### 3. Landingpages & LP-Typen

| LP | Typ | # aktive Ads | Anteil |
|---|---|---|---|
| `https://www.cozily-shop.com/pages/advertorial` | **Advertorial** (Long-Form, Story + Listicle + Timeline + FAQ) | **467** | 84,6 % (87 % der UK-Ads) |
| `https://cozily-shop.com/products/covering-easysleep®-the-2-in-1-quick-dry-duvet-that-eliminates-the-need-for-bed-sheets-…` (mit und ohne `?fbclid=fbclid`) | **Produktseite (PDP)** | **70** | 12,7 % |
| `https://cozily-shop.com/pages/advertorial-easysleep-usa` | **Advertorial (US-Version)** | **15** | 2,7 % |

**Muster im Zeitverlauf:**
- Juli (Start): starker PDP-Anteil. Am 20./21.07. gingen 18 von 40 Ads auf die PDP.
- August bis Mitte September: fast ausschließlich Advertorial.
- Ende September und Anfang Oktober: PDP kommt wieder stärker dazu. Am 30.09. und 01.–04.10. gingen 21 von 55 Ads auf die PDP, vor allem Sale-Statics mit `?fbclid=fbclid`.

**Advertorial: Aufbau** (curl am 08.10.2026, wörtliche Auszüge):
- Headline: **„I changed my bedding every week for 15 years. Then I finally realised the problem wasn't the sheets, it was the duvet.“** (Übersetzung des MS-Video-Hooks „Über 15 Jahre lang jede Woche das Bett frisch beziehen…“)
- Sub: „The EasySleep® 2-in-1 Duvet — duvet and cover in one. No stuffing. No wrestling. Just wash it — and it's back on the bed in 2 hours.“
- Social Proof: **„WE'VE ALREADY HELPED 17,000+ PEOPLE NEVER CHANGE THEIR BEDDING AGAIN…“**. 4 Testimonials, darunter „William H.: I'm a widower in my eighties. Making the bed on my own was always a struggle…“
- Problem-Agitation: **„When did you last actually wash your duvet? Not the cover. The duvet itself.“** (= MS-Hook „Wann hast du deine Bettdecke zuletzt wirklich gewaschen? Nicht den Bezug, die Decke selbst.“)
- „The 5 reasons why no one ever wants to go back“, dann eine Timeline „Night One … After 100 Nights“
- Zielgruppen-Block: **„Perfect for those aged 55+“**, **„Ideal for carers“**
- Preisbox: **„★★★★★ 4.9/5 | Based on 7,980+ Reviews · EasySleep Duvet £69.99 INSTEAD OF £109.99 with FREE pillowcases worth £49.99“** · CTA „TRY THE EasySleep® NOW / ✅ 40-night risk-free trial“
- Garantie: „40-night 100% money-back guarantee … no questions, no forms“ plus der Zusatz „We wash every returned duvet and donate it to care homes and charities“
- Autoritäten: „Jessica Smith – Founder“ und **„Tobie Fallschmidt, MA – Tobias comes from Germany … Textile Technology“** (deutscher Experte als Glaubwürdigkeits-Anker)

---

### 4. Launch-Kadenz (Startdatum der aktuell aktiven Ads)

| Monat | neue (noch aktive) Ads |
|---|---|
| Juli 2026 (ab 10.07., Großteil ab 20.07.) | 95 |
| August 2026 | 223 |
| September 2026 | 220 |
| Oktober 2026 (01.–04.) | 14 |

| KW | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| neue Ads | 70 | 36 | 58 | 52 | 74 | 2 | 47 | 60 | 29 | 39 | **84** |

**Batch-Tage:** 20.07. (25), 24.07. (19), 07.08. (24), 15.08. (25), 31.08. (25), 08.09. (26), 11.09. (22), 21.09. (24, alle Advertorial mit Score 1, also frischer Test), 29.09. (25), **30.09. (41)**.

**Interpretation:**
- Cozily launcht **alle 2–4 Tage einen Batch mit 10–40 Ads** und lässt fast alles laufen. Fast alle Ads seit 20.07. sind noch aktiv, was auf viele kleine Ad-Sets bzw. ABO-Testing hindeutet.
- Die älteste aktive Ad ist **186737375** (10.07., PDP-Video): https://app.gethookd.ai/share/ad/186737375?signature=2e48a90e900459dc4df559be8b396a117d1143d18cacdc3470d74779baf4d8c0 · https://www.facebook.com/ads/library/?id=1341400987542510
- **Ende September wird es saisonal:** „AUTUMN'S HERE. One duvet from now until spring.“, US-Start und eine Welle neuer Sale-/Lagerverkauf-Creatives.

---

### 5. Die 15 stärksten Ads

Stärke bemisst sich am GetHooked-Performance-Score. Das Maximum im Account liegt bei **64**. Zusätzlich zählen Laufzeit, Duplizierung (`used_count` 2) und die Zahl der Format-Varianten derselben Idee. Der Primärtext ist bei allen UK-Ads identisch (siehe oben). Unten stehen deshalb Hook, Headline und On-Screen-Text.

#### #1 – „I need to publicly apologize“ (Overproduction/Entschuldigung, Video)
- **188679985** · Video 45 s · Start 11.09. · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/188679985?signature=cf14743cbc7ef6f2888a2fe433b32611ade5596c697818e0bec33e3e8210a5a4 · Meta: https://www.facebook.com/ads/library/?id=1052591764343206
- On-Screen: **„🚨 TRIPLE DEAL ENDS TONIGHT!“** / „I NEED TO PUBLICLY APOLOGIZE“
- Gesprochen (Transkript, wörtlich): *„I need to publicly apologize to everyone who's already bought an easy sleep duvet, because I lied. I told you that was the best price you'd ever get, and then we overproduced. We made way too many easy sleep duvets. Yes, we seriously overproduced. So this is your chance to get the biggest offer we've ever had on our website. Up to 40% off. … Right now, you can get up to 40% off, plus two free soft cloud pillowcases with every easy sleep. Because once this extra stock is gone, it's gone. We won't be running an offer like this again for a very long time.“*
- Avatar: KI-generierter Mann ca. 70, graue Haare, Brille, kariertes Hemd, Selfie im Schlafzimmer
- Angle: Overstock + Entschuldigung + Deadline · Offer: up to 40 % off + 2 free SoftCloud pillowcases
- Varianten mit anderen Avataren (15.09., Score 56): **188681961** (Mann ca. 60, rote Bettwäsche, „Triple Discount End tonight 🚨“) GH https://app.gethookd.ai/share/ad/188681961?signature=6dd720c32e58e2f02e927911171ecedffb0cd7119d01f250bc2529ee80064191 · Meta https://www.facebook.com/ads/library/?id=29332012089722123. Außerdem **188368675** (Mann ca. 50, Brille, Schnurrbart) GH https://app.gethookd.ai/share/ad/188368675?signature=479f9699de5a5c97b4733c19ff172911bebd8272f09e1474c1e4e896c13a9c1d · Meta https://www.facebook.com/ads/library/?id=4056702414623797

#### #2 – „Hotel room every single day“ (Video)
- **190147104** · Video · Start 11.09. · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/190147104?signature=20e1b0d1b34ee69181d9523613390f27374b2750020f4f202b0dd573ee10c61e · Meta: https://www.facebook.com/ads/library/?id=1069474352335265
- On-Screen: **„WANT TO KNOW HOW I MAKE MY BED LOOK LIKE A HOTEL ROOM EVERY SINGLE DAY?“**
- Gesprochen: *„Everyone keeps asking me how I make my bed look like a hotel room. It's one thing. Having a…“*
- Avatar: keine Person im Bild, rote Decke im warmen Schlafzimmer (Produkt-B-Roll)
- Angle: Aspiration / Hotelbett · Offer: Standard (2 free pillowcases, 40 nights)
- **MS-Vorlage:** MS 112081187 „Jeden Tag ein Bett wie im Hotel…“

#### #3 – „I ordered the EasySleep duvet“ (Video, MS-Template)
- **190139671** · Video · Start 11.09. · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/190139671?signature=e5bdd8730429c31da6a2adfc60c8853ca0632306364540017b29dab4a128998e · Meta: https://www.facebook.com/ads/library/?id=1450070080298435
- On-Screen: **„Finally, an end to the bedsheet struggle.“** + Untertitel „i ordered the EasySleep duvet“
- Gesprochen: *„I ordered the Easy Sleep Duvet because I simply couldn't be bothered with struggling with…“*
- Avatar: kein Gesicht, Decke wird aufs Bett geschwungen (Demo)
- **Wörtliche Übersetzung von MS 126012757** („Ich habe die Easy-Sleep-Decke bestellt, weil ich einfach keinen Bock mehr hatte, jede Woche mit der Bettwäsche zu kämpfen…“, Overlay „DAS WARS MIT BETTWÄSCHE WECHSELN!“). Das ist eine der stärksten MS-Ads: Score 100, 83 Tage, Spend-Range $10–20k.
- Geschwister: **189399939** „Say goodbye to changing bedsheets the hard way.“ (11.09.) GH https://app.gethookd.ai/share/ad/189399939?signature=629de4cb5a0c6a66555208fed79be10ffee0214e04e29bfe5cf4fa58435c4489 · Meta https://www.facebook.com/ads/library/?id=1765352407944812

#### #4 – „If your duvet doesn't fit in your washing machine“ (Video, UK-lokalisiert)
- **189722200** · Video · Start 11.09. · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/189722200?signature=8416051deb9205f283139be0db4cf57c915186d9bee2ee513a0834dbf010321f · Meta: https://www.facebook.com/ads/library/?id=1400617288673382
- On-Screen: **„IF YOUR DUVET DOESN'T FIT IN YOUR WASHING MACHINE YOU NEED TO SEE THIS“**
- Gesprochen: *„Do you pay for dry cleaning or drag your duvet to the Laundrette every time it needs washing?“*
- Avatar: KI-Szene, Mann bezahlt im Bettwarenladen eine eingepackte Decke
- Angle: Waschmaschine/Waschsalon-Schmerz (typisch britisch) · eigene Cozily-Idee
- Passend dazu der Static **189405420** „No launderette. No service wash. Your machine at home does it.“ / „Fits an ordinary 6 to 7 kg drum. 40 degrees. Done.“ GH https://app.gethookd.ai/share/ad/189405420?signature=f1b32f94ac7571165e2173c77c98c3caba8a7394dd9230abdc5e57ad9223b245 · Meta https://www.facebook.com/ads/library/?id=1405624548345997

#### #5 – „Why are people ditching their old duvets?“ (Video)
- **189724348** · Video · Start 11.09. · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/189724348?signature=38cdb79583fb4765da2f8730c014721017ec63b97606dc1f4c4be5c494b1b6cc · Meta: https://www.facebook.com/ads/library/?id=2029805047661962
- On-Screen: **„WHY ARE PEOPLE DITCHING THEIR OLD DUVETS?“** · Gesprochen: *„Why are so many people replacing their old duvet with this one?“*
- Avatar: Mann ca. 40–45, Bart, Talking Head (KI-Look) · Angle: Neugier / Trend

#### #6 – „I'm 63 … independence“ (Senior-Testimonial, Video)
- **187361100** · Video · Start 28.07. (**73 Tage**) · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/187361100?signature=615b4d414152597bcfeb03ddc2d0d16b4b769786f1b34a49cf93b05207a0ff05 · Meta: https://www.facebook.com/ads/library/?id=1892926045003393
- Gesprochen: *„I'm 63 and I never expected to say a duvet handed me back a bit of my independence, but here we are.“*
- Avatar: weißhaariger Mann ca. 65, Navy-Pullover, britisches Wohnzimmer, hält eine gefaltete mintgrüne Decke (KI-Look)
- Angle: Senioren / Selbstständigkeit · nah an MS (MS-Testimonials 48–63 Jahre; MS 196670581 Gelenke)

#### #7 – „NEVER CHANGE THE BEDDING AGAIN“ (Video, MS-Creator-Footage)
- **189724357** · Video Split-Screen · Start 20.07. (**81 Tage**) · Score **64** · used_count 2 · LP **PDP**
- GH: https://app.gethookd.ai/share/ad/189724357?signature=c3675cb4a7e40e014bb46e65657023acdcc481a1f2fa99e46c86d61892fbe043 · Meta: https://www.facebook.com/ads/library/?id=1924056578550887
- On-Screen: **„NEVER CHANGE THE BEDDING AGAIN“** + „I ordered the EasySleep Duvet“
- Avatar: Mann ca. 30, Brille, schwarzes T-Shirt, petrolfarbenes Kopfteil. Das ist **derselbe Creator und dasselbe Set wie in MS 125662052 und MS 129130363** („Nie wieder Bettbeziehen ❌“, beide MS Score 100, Spend $10–20k). **Cozily nutzt hier offensichtlich das Original-Footage von Magic Splashy.**

#### #8 – „LAST WASHED 6 WEEKS AGO“ (Hygiene, Video)
- **189724373** · Video · Start 20.07. (**81 Tage**) · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/189724373?signature=b59b48ca5f0333f13c8ec5643a2c62ca552af0382c1e9bd6a38d5fa043ea66a7 · Meta: https://www.facebook.com/ads/library/?id=1058919523184656
- On-Screen: **„LAST WASHED 6 WEEKS AGO“** · Gesprochen: *„Every time I changed my bedding, I thought, never again.“*
- Avatar: junger Mann im Bett unter grauer Decke, kratzt sich (echtes UGC, wirkt deutsch) · Angle: Ekel/Hygiene (vgl. MS 139052723 „Du duschst jeden Abend. Und legst dich danach unter eine Decke, die du noch nie richtig gewaschen hast 🤮“)

#### #9 – „Never sweat at night again“ (Temperatur, Video)
- **189399853** · Video · Start 20.07. (**81 Tage**) · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/189399853?signature=1531cc34363d80bd82edd0bd94ff5d53657ea497797e2097eab40e17446bd457 · Meta: https://www.facebook.com/ads/library/?id=1644912116606250
- On-Screen: **„❌Never sweat at night again“** · Gesprochen: *„Do you sweat at night and never really wake up feeling refreshed?“*
- Avatar: Glatzkopf ca. 45, Green-Screen vor einem schweißnassen Gesicht (echtes UGC) · Angle: Nachtschweiß (= MS „Kein Schwitzen. Kein Frieren.“ bzw. „NIE MEHR SCHWITZEN NACHTS“)

#### #10 – „IMPORTANT, NOW IN SUMMER: IF YOU SWEAT AT NIGHT“ (Video)
- **189724449** · Video · Start 22.07. (**79 Tage**) · Score **64** · used_count 2 · LP **PDP**
- GH: https://app.gethookd.ai/share/ad/189724449?signature=2a4f774c381e487e6083c03b86bbab49632f230cfe13beb59543528088698f45 · Meta: https://www.facebook.com/ads/library/?id=1684247762799791
- On-Screen: **„IMPORTANT, NOW IN SUMMER: IF YOU SWEAT AT NIGHT“** + „Wait What?“ · Avatar: Frau ca. 35, Brille, schüttelt eine weiße Decke (echtes UGC, deutsche Wohnung). Die Formulierung ist eine typisch deutsche Satzstellung („WICHTIG, JETZT IM SOMMER: …“).
- Variante mit Rabatt-Badge **„SAVE 35%“**: **190139667** (24.07.) GH https://app.gethookd.ai/share/ad/190139667?signature=f224419b9cb2e09f5ce88f1993277702a61bdeb89843a0b7c440086391e333af · Meta https://www.facebook.com/ads/library/?id=27866642696292765

#### #11 – „Karen, 52“ (Testimonial-Static)
- **189734435** (9:16, Start 24.08.) und **189726176** (1:1, Start 04.08., 66 Tage) · beide Score **64** · used_count 2 · LP Advertorial
- GH 189734435: https://app.gethookd.ai/share/ad/189734435?signature=9cdec0bd0787b60f5648ebd44c6e58bb47fb43e8545712c539263f9ecce5288a · Meta: https://www.facebook.com/ads/library/?id=4381606525423205
- GH 189726176: https://app.gethookd.ai/share/ad/189726176?signature=61af38e4e8b6ca0701760a70feba82ed938af385d8a95529f6505f74ae33a5e5 · Meta: https://www.facebook.com/ads/library/?id=948236428292035
- Text: **„Karen, 52: “I used to wake up drenched every summer. Since I got this duvet that has completely stopped. I do not know how it works, but I simply stay dry at night.”“** + „17,000+ people now sleep with EasySleep“
- Avatar: Frau ca. 50, lange graue Haare, hält eine rote Decke hoch · Angle: Nachtschweiß + Social Proof (Frauen 50+, implizit Wechseljahre)
- **MS-Vorlage:** MS 139047107 „Ich weiß nicht, wie die Decke das macht, aber egal, ob heiße Sommernacht…“

#### #12 – „Never pull again.“ (Minimal-Produkt-Static, viele Varianten)
- **189395739** (4:5, 07.08., 63 Tage) und **189395750** (9:16, 11.08.) · beide Score **64** · used_count 2 · LP Advertorial. Weitere Farbvarianten: 190139594 (schwarz), 189724503 (salbei, PDP)
- GH 189395739: https://app.gethookd.ai/share/ad/189395739?signature=ab939d60f494f2046dbb7223f9f6d0c23b77f782343b0b5539136843f1b15215 · Meta: https://www.facebook.com/ads/library/?id=3179008848951738
- GH 189395750: https://app.gethookd.ai/share/ad/189395750?signature=6572083cda5121d7af5f4bf38e17997ffacb9fa19ab3583382a964a7bb8b1669 · Meta: https://www.facebook.com/ads/library/?id=2052858648663946
- Text: **„Never pull again.“ / „SALE - Duvet + cover IN ONE. 7 colours.“**
- Angle: Convenience / kein Bezug mehr · nah an MS 180516162 „Nie wieder Bettwäsche wechseln. Decke + Bezug in EINEM“

#### #13 – „Mum – no more fighting with the cover. Love, Claire x“ (Geschenk an die Eltern)
- **190140600** (9:16, 14.08.) und **189399821** (4:5, 11.08.) · beide Score **64** · used_count 2 · LP Advertorial
- GH 190140600: https://app.gethookd.ai/share/ad/190140600?signature=64270d925567b56d59313c88826f4dacef6ce5e15361ff005288d544e81e2083 · Meta: https://www.facebook.com/ads/library/?id=884638551108416
- GH 189399821: https://app.gethookd.ai/share/ad/189399821?signature=6d26f291d07d33c577d46965a209fa721c117868d45a1e70c8f69e815d20684e · Meta: https://www.facebook.com/ads/library/?id=1480725987314826
- Text: Grußkarte auf dem Bett *„Mum – no more fighting with the cover. Love, Claire x“* + Headline **„The whole thing washes. It dries in two hours.“** / „One less thing for her to manage.“
- Angle: erwachsene Kinder kaufen für Mutter oder Vater (Gifting, Fürsorge). **Bei MS nicht gesehen, also eine eigene und sehr gute Cozily-Idee, die Weihnachten 2026 tragen dürfte.**

#### #14 – Lagerverkauf-Familie: „We've made too many. Help us clear them.“
- **189397232** · Static 1:1 · Start 11.09. · Score **64** · used_count 2 · LP Advertorial
- GH: https://app.gethookd.ai/share/ad/189397232?signature=026f05568e07740a113b98caf9b7bbb5446bca779083bff3f28e85a986ca4bb6 · Meta: https://www.facebook.com/ads/library/?id=1087915160456366
- Text: Pappschild im Lager **„We've made too many. Help us clear them.“** + „40% off + 2 free pillowcases while stocks last“
- Weitere Ads der Familie mit Score 64 (31.08.):
  - **189723854** „Warehouse Sale...now live!“ / „40% off + 2 free pillowcases. Duvet and cover in one.“ GH https://app.gethookd.ai/share/ad/189723854?signature=8c28c2669ecef65eb42ca814587c2a416385b2208f3619c68f70bf4d14c5d3c4 · Meta https://www.facebook.com/ads/library/?id=1805727490841445
  - **189399854** „Stock is moving“ / „Warehouse sale: 40% off + 2 free pillowcases with every duvet“ / „40 nights to try. Full refund, no form to fill in.“ GH https://app.gethookd.ai/share/ad/189399854?signature=1761d7f5a9f5b86f9ee00a63db5a20d1bc6e7169ce2059cf817ec08656ced7c1 · Meta https://www.facebook.com/ads/library/?id=1389938529959731
- Angle: Overstock/Clearance (die Begründung für den Rabatt) · Offer: 40 % off + 2 gratis Kissenbezüge

#### #15 – „I didn't believe it. Until the first night.“ (Skeptiker wird überzeugt, Static)
- **190147077** · Static 1:1 Split · Start 21.07. (**80 Tage**) · Score **64** · used_count 2 · LP **PDP**
- GH: https://app.gethookd.ai/share/ad/190147077?signature=82ee0dd43e98c7b2be7f9663adc0825e40f668d49043cafbedc57e06330826b1 · Meta: https://www.facebook.com/ads/library/?id=1065508685810366
- Text: **„I didn't believe it. Until the first night.“** ✓ 40 night sleep trial – money back ✓ Keeps its promise ✓ Duvet + cover in one ✓ Fully washable ✓ Dries in just 2 hours
- Avatar: Frau ca. 55, links skeptisch mit COZILY-Verpackung, rechts glücklich schlafend · Angle: Skepsis bis Überzeugung + Risk-Reversal

**Weitere Score-64-Dauerläufer (Juli), kurz:**
- **190141560** „Looks new. Every time. Designed for regular washing — without losing quality.“ / „Day 1 · After 20 washes · After 50 washes“ (PDP, 21.07.) GH https://app.gethookd.ai/share/ad/190141560?signature=77ff00298a85bbf96fe7e89ea7d634791c3b1c3b59ea871427388577f54dd538 · Meta https://www.facebook.com/ads/library/?id=1536007064328602
- **190147148** „ONLY UNTIL SUNDAY 2 PILLOWCASES FREE. + 40 nights' trial sleep — risk free.“ (PDP, 29.07.) GH https://app.gethookd.ai/share/ad/190147148?signature=7806b691422f8422ed1334a350717d62f11b10551461334cef6dce63798deae1 · Meta https://www.facebook.com/ads/library/?id=1015761917903729
- **189724407** „ONLY UNTIL FRIDAY 2 Pillowcases FREE with every Duvet.“ / „Secure Your Free Bundle“ (29.07.) GH https://app.gethookd.ai/share/ad/189724407?signature=4703f92dbc6a42dd839e870163c027d4794aea157e206ff9b1a38edb003598ef · Meta https://www.facebook.com/ads/library/?id=1013995984575612
- **190558896** „“Does it dry quickly?” “Wash it today. Sleep with it tonight.”“ (Wäscheleine im britischen Garten, 28.07.) GH https://app.gethookd.ai/share/ad/190558896?signature=11129729be30a8407d6faf7079bbea11c3402cbee5aba427a7b533b0c994ff57 · Meta https://www.facebook.com/ads/library/?id=2485927431817164
- **189405325** „Never an empty corner.“ (frustrierte Frau ca. 45, 21.07.) GH https://app.gethookd.ai/share/ad/189405325?signature=6a1139a8e10080ea27d1c543aea918457e91e547489170668e0edad231193a48 · Meta https://www.facebook.com/ads/library/?id=1633360048160981
- **189398858** „Our duvet makes every other one feel...meh.“ (20.07.) GH https://app.gethookd.ai/share/ad/189398858?signature=b3c559bb80235007d5d5572da69079f6feaf4204fb052e0e0e35b87510efe7ac · Meta https://www.facebook.com/ads/library/?id=1774720443972921
- **189726248** „Everything you actually wanting to know:“ (sic) mit Checkliste und „Now 40% off. Duvet and cover in one.“ (31.08.) GH https://app.gethookd.ai/share/ad/189726248?signature=5c221f45268ce72f2e1ed0156a7ca317d21b82f71201db97155b7be63fa47768 · Meta https://www.facebook.com/ads/library/?id=1045449038368791

**Watchlist: neu und gerade im Test (Ende Sep./Okt.)**
- **190558325** „I'm returning my EasySleep duvet“. Gesprochen: *„I'm returning my Easy Sleep duvet, not because it's bad,“*. Frau ca. 60, hält einen EasySleep-Karton (30.09.). GH https://app.gethookd.ai/share/ad/190558325?signature=5042a326719c3520ecc9f427f27c0bfc7558751a427fd98f3b4d04d1e5e4ca86 · Meta https://www.facebook.com/ads/library/?id=1890720305246859
- **197407814** „AUTUMN'S HERE. One duvet from now until spring.“ / „10.5 TOG“ / „GET 40% OFF NOW + FREE DELIVERY + 2 free SoftCloud pillowcases + 40-night trial“ (04.10., PDP). GH https://app.gethookd.ai/share/ad/197407814?signature=f3179577688a90a983abb621da90266c1856326faa6e8c02921ac048c47cdeff · Meta https://www.facebook.com/ads/library/?id=1417419460578927
- **197405824** „★★★★★ LIGHT ENOUGH TO CARRY ONE-HANDED. So it's easy to wash and put back yourself.“ Ältere Frau auf der Treppe (03.10., PDP). GH https://app.gethookd.ai/share/ad/197405824?signature=cd840433d54139aba98afbd638849ab0cf41e61b00e4eb218b6a3ecad24a107c · Meta https://www.facebook.com/ads/library/?id=1065319596294234
- **190558968** „We're not angry. We're just 40% off now.“ / Zettel „The intern did this.“ / „40% off + 2 free pillowcases, until the mountain is gone.“ (20.09., Score 51). GH https://app.gethookd.ai/share/ad/190558968?signature=619206b61aa646107b43df619c767db62963122576575723335585bffba44238 · Meta https://www.facebook.com/ads/library/?id=1764646547943960
- **189397062** „Don't buy the EasySleep duvet. Not if you enjoy wrestling a cover every week.“ / „40% off + 2 free pillowcases, if you insist.“ (08.09.). GH https://app.gethookd.ai/share/ad/189397062?signature=2dfc366568a831fe0bf80a388ce2bb9a5227c967b8f24763a506fceb93f76cdd · Meta https://www.facebook.com/ads/library/?id=1057306373578220
- **190175692** Whiteboard **„HOT COLD – HE'S TOO HOT. SHE'S TOO COLD. → one duvet for both of you“** (29.09., PDP). GH https://app.gethookd.ai/share/ad/190175692?signature=cf444ad4404cba1bb6ea9cbb09efd3e816e3e4f31819816e6fc8e0b326c4fed5 · Meta https://www.facebook.com/ads/library/?id=1552551079871891

---

### 6. Vollständige Liste: Angles, Hooks, Offers

#### 6.1 Angles (nach Häufigkeit und Gewicht)

| # | Angle | Beispiel-Hooks (wörtlich) | Beispiel-IDs |
|---|---|---|---|
| 1 | **Nie wieder Bezug wechseln / Convenience** | „NEVER CHANGE THE BEDDING AGAIN“ · „Never pull again.“ · „YOUR BED IS MADE IN TEN SECONDS. No cover. No stuffing. No struggle.“ · „The old way: a wrestling match. The new way: ten seconds.“ · „No zip. No cover to thread. No spare for summer. One duvet, made in ten seconds.“ | 189724357, 189395739, 189724500, 189726720, 189398761 |
| 2 | **Hygiene / komplett waschbar / Milben** | „LAST WASHED 6 WEEKS AGO“ · „The cover you wash. The duvet you never do.“ · „What about dust mites? Wash the whole duvet at 40 degrees. Not just the cover.“ | 189724373, 190140724, 190141487 |
| 3 | **Schnelltrocknend (2 Std.)** | „“Does it dry quickly?” “Wash it today. Sleep with it tonight.”“ · „Seven colours. Not one duvet cover. … Dry in about two hours.“ | 190558896, 189399931 |
| 4 | **Passt in die Waschmaschine / kein Waschsalon (UK)** | „IF YOUR DUVET DOESN'T FIT IN YOUR WASHING MACHINE YOU NEED TO SEE THIS“ · „No launderette. No service wash. Your machine at home does it.“ · „That's why you don't need a huge washing machine 😅“ | 189722200, 189405420, 190558980 |
| 5 | **Temperatur / Nachtschweiß / Ganzjahr (10.5 tog)** | „❌Never sweat at night again“ · „IMPORTANT, NOW IN SUMMER: IF YOU SWEAT AT NIGHT“ · „EasySleep 40% OFF Summer or winter, the same duvet 10.5 TOG, ALL YEAR“ · „WHY BUY THREE... WHEN ONE DOES IT ALL? A summer duvet, a winter duvet and a cover, in one.“ | 189399853, 189724449, 190559121, 190558332 |
| 6 | **Paare** | „WE FINALLY STOPPED FIGHTING OVER THE DUVET“ · „HOT COLD – HE'S TOO HOT. SHE'S TOO COLD.“ | 189396916, 190175692 |
| 7 | **Senioren / Selbstständigkeit / 55+** | „I'm 63 and I never expected to say a duvet handed me back a bit of my independence“ · „LIGHT ENOUGH TO CARRY ONE-HANDED.“ · „She's worth every penny.“ (Frau ca. 60 im Blazer) | 187361100, 197405824, 190171503 |
| 8 | **Geschenk für die Eltern** | „Mum – no more fighting with the cover. Love, Claire x“ | 190140600, 189399821 |
| 9 | **Overstock / Lagerräumung / Entschuldigung** | „I need to publicly apologize“ · „We've made too many. Help us clear them.“ · „THE SHELVES ARE FULL. THEY HAVE TO GO. EVERY COLOUR MUST GO“ · „EVERY THING MUST GO“ · „Warehouse Sale every colour must go!“ · „We're not angry. We're just 40% off now.“ | 188679985, 189397232, 190558231, 190175678, 190558901, 190558968 |
| 10 | **Verknappung / Deadline** | „🚨 TRIPLE DEAL ENDS TONIGHT!“ · „Only until Friday!“ · „ONLY UNTIL SUNDAY“ · „This week only:“ · „LAST CALL“ · „last stock remaining“ · „“You don't get the 2 pillowcases for ever free.” Offer ends soon - take part while you still can.“ | 188679985, 189399830, 190147148, 190139624, 190175667, 189399940, 190140645 |
| 11 | **Social Proof (17.000)** | „17,000 homes sleep like this 4.9 out of 5 from verified reviews“ · „17,000 people have stopped buying duvet covers.“ · „Karen, 52: …“ | 190139642, 189722225, 189734435 |
| 12 | **Vergleich / Us vs Them** | „A normal duvet vs this one“ · „Two duvets. One obvious winner.“ · „STOP BUYING DUVET COVERS This one already has one built in“ · „WHY BUY TWO... WHEN ONE DOES BOTH?“ | 189397059, 189397035, 189399860, 190139665 |
| 13 | **Reverse Psychology** | „Don't buy the EasySleep duvet.“ · „I'm returning my EasySleep duvet“ | 189397062, 190558325 |
| 14 | **Skeptiker → Überzeugt** | „I didn't believe it. Until the first night.“ | 190147077 |
| 15 | **Haltbarkeit (Einwand)** | „Lost quality after washing? No. Looks like new — even after 50 washes.“ · „Looks new. Every time.“ | 190140606, 190141560 |
| 16 | **Farben / Einrichtung** | „PICK YOUR COLOUR. SKIP THE COVER.“ · „7 COLOURS. AN EASY CHOICE.“ · „Cannot decide? Start here.“ · „7 COLOURS ONE LESS THING TO WORRY ABOUT“ | 197404388, 190175694, 189405448, 197407503 |
| 17 | **Haustiere** | „With the dog on the bed. And still clean.“ | 190140714 |
| 18 | **Familie / Mehrfachkauf** | „Three beds in the house. Three duvets. 2 free pillowcases with every one.“ / „FAMILY BUNDLE - most popular“ | 189399929 |
| 19 | **Saison** | „AUTUMN'S HERE. One duvet from now until spring.“ · „IMPORTANT, NOW IN SUMMER…“ | 197407814, 189724449 |
| 20 | **Allergie (nur US-Test)** | „DIAGNOSED. NOW WASHABLE.“ · „WASH IT FOR YOUR ALLERGIES. NOT AGAINST YOUR WILL.“ · „YOUR DUVET MIGHT BE PART OF THE PROBLEM.“ · „WASH IT AT BREAKFAST. SLEEP UNDER IT TONIGHT.“ | 189733489, 189400477, 190146383, 189396915 |
| 21 | **Aspiration / Premium / Hotelbett** | „WANT TO KNOW HOW I MAKE MY BED LOOK LIKE A HOTEL ROOM EVERY SINGLE DAY?“ · „Effortless. Bed made in ten seconds.“ · „Once you have this one the others are pointless“ · „Never make the bed again.“ (Bushaltestellen-Mockup) | 190147104, 190146305, 190558960, 189734456 |
| 22 | **Neugier / Trend** | „WHY ARE PEOPLE DITCHING THEIR OLD DUVETS?“ · „Why I threw out all my duvets last month ?“ (gesprochen: „Three months ago, I threw out every single duvet cover I owned.“) | 189724348, 189398802 |
| 23 | **Leere Ecken / Füllung verrutscht** | „Never an empty corner.“ | 189405325 |

#### 6.2 Gesprochene Video-Hooks (Transkripte, wörtlich)
- 188679985: „I need to publicly apologize to everyone who's already bought an easy sleep duvet, because I lied.“
- 190147104: „Everyone keeps asking me how I make my bed look like a hotel room. It's one thing.“
- 190139671: „I ordered the Easy Sleep Duvet because I simply couldn't be bothered with struggling with…“
- 189722200: „Do you pay for dry cleaning or drag your duvet to the Laundrette every time it needs washing?“
- 189724348: „Why are so many people replacing their old duvet with this one?“
- 187361100: „I'm 63 and I never expected to say a duvet handed me back a bit of my independence, but here we are.“
- 189724373: „Every time I changed my bedding, I thought, never again.“
- 189399853: „Do you sweat at night and never really wake up feeling refreshed?“
- 190558325: „I'm returning my Easy Sleep duvet, not because it's bad,“
- 189398802: „Three months ago, I threw out every single duvet cover I owned.“
- 189722117: „Never change your bedding again. Now in Cream Beige and Chimney Red.“ GH https://app.gethookd.ai/share/ad/189722117?signature=5788423882ab14964f85e9dc25748da20646b78599ed12c4c1355696b8f53dab · Meta https://www.facebook.com/ads/library/?id=1591763752291220

#### 6.3 Offers
- **2 gratis SoftCloud-Kissenbezüge („worth £49.99“)** in jeder Ad, im Primärtext und meist auch im Creative
- **40-Nächte-Probeschlafen** in vielen Formulierungen: „40-night risk-free trial“, „40-night money-back guarantee“, „40 nights to try, full refund“, „Full refund. No form to fill in.“, „Satisfied or refunded within 40 days“, „Send it back if it is not the one.“
- **Rabatt:** im Juli/August „UP TO -36%“ (190141494) bzw. „SAVE 35%“ (190139667), seit ca. 31.08. **„40% off“ / „Up to 40% off“**. Auf der Seite stehen tatsächlich 29–36 %.
- **Free delivery** („+ FREE DELIVERY“, „Fast & Free Delivery“)
- **Deadlines:** „Only until Friday“, „Only until Sunday“, „This week only“, „Ends tonight“, „Triple Deal“, „while stocks last“, „Last call“
- **Family Bundle** („Three beds in the house. Three duvets.“)
- Upsells auf der Seite: SoftCloud® Pillow £29.99 (statt £49.99), SoftCloud® Fitted Sheet £19.99 (statt £39.99), „Spend £X more to get FREE shipping!“ im Cart
- **US:** „$129.99 INSTEAD OF $189.99“, Kissenbezüge „worth $49.99“

#### 6.4 Avatare / Wer ist im Ad
- **KI-Avatare 50–70 Jahre** (Männer dominieren bei den Videos, Frauen bei den Statics): Entschuldigungs-Männer, 63-jähriger Mann, Frau ca. 60 „returning“, Karen 52, Blazer-Frau, Treppen-Seniorin
- **Junge deutsche UGC-Creator** (MS-Footage): Mann mit Brille, Frau mit Brille, Glatzkopf, junger Mann im Bett
- **Paare** (KI), **keine Person** (Produkt-B-Roll und Statics), **Hund** (Beagle)

---

### 7. Was ist von Magic Splashy kopiert?

**Sicher kopiert:**

| Cozily | Magic Splashy (DE) | Art der Kopie |
|---|---|---|
| **Primärtext aller 537 UK-Ads** („Duvet + Cover in One 🌙 … Get 2 SoftCloud pillowcases FREE today (worth £49.99). Enjoy a 40-night risk-free trial. Finally experience a bed that always feels fresh.“) | MS **179252420** „Decke + Bezug in einem 🌙 … Heute 2 SoftCloud Kissenbezüge gratis (49,99€ Wert) sichern. 40 Tage risikofrei probeschlafen. Genieße endlich ein Bett, das immer frisch ist.“ (MS Score 100, ≥24 MS-Ads mit identischem Text) GH https://app.gethookd.ai/share/ad/179252420?signature=b705ffb54efd1b5a03448c8012cc9821cb489e17ae0193cf7888c47b270547f2 · Meta https://www.facebook.com/ads/library/?id=1820936862425780 | **Wörtliche Übersetzung** inkl. Emoji, Bullet-Reihenfolge und Preis 49,99 |
| Produkt- und Markennamen **EasySleep®**, **SoftCloud®**, **ThermoBalance® fibres**, „No sweating, no freezing“, Testimonials mit Alter („Jack - 62 years“, „Mike S. - 49 years“) | MS: EasySleep®, SoftCloud, „ThermoBalance® Klimafasern“, „Kein Schwitzen. Kein Frieren.“, Testimonials 48–63 J. | 1:1 übernommen, auch die Marken-Namen |
| **„17,000+“** (Advertorial, 190139642, 189722225, 189734435) | MS „17.000+ begeisterte Schläfer“ / „Über 17.000 zufriedene Schläfer“ | Zahl übernommen |
| **189724357** „NEVER CHANGE THE BEDDING AGAIN“ + „I ordered the EasySleep Duvet“ | MS **125662052** und **129130363** „Nie wieder Bettbeziehen ❌“ (gleicher Creator: Brille, schwarzes Shirt, petrolfarbenes Kopfteil). GH https://app.gethookd.ai/share/ad/125662052?signature=afca98f12b6dd400226ecbd2adcf32983adb04f2c06b179d502bd583a5f9a763 · Meta https://www.facebook.com/ads/library/?id=2025964218008688 · GH https://app.gethookd.ai/share/ad/129130363?signature=2280883cdc1b06d68811f8455bca14dbebe3878407f4246090cb2afb6c5c467c · Meta https://www.facebook.com/ads/library/?id=1534211127599850 | **Original-Footage** von MS mit englischen Captions |
| **190139671** „Finally, an end to the bedsheet struggle.“ / gesprochen „I ordered the Easy Sleep Duvet because I simply couldn't be bothered with struggling with…“ (dazu 189399939) | MS **126012757** „DAS WARS MIT BETTWÄSCHE WECHSELN!“ / „Ich habe die Easy-Sleep-Decke bestellt, weil ich einfach keinen Bock mehr hatte, jede Woche mit der Bettwäsche zu kämpfen.“ GH https://app.gethookd.ai/share/ad/126012757?signature=4aa5cf75157a813c3daede61927240a452d4bf09046a0feee9ae288bd457658f · Meta https://www.facebook.com/ads/library/?id=1572451867734657 | Script wörtlich übersetzt, gleiche Caption-Mechanik |
| Advertorial-Headline „I changed my bedding every week for 15 years…“ | MS **125661932** „Über 15 Jahre lang jede Woche das Bett frisch beziehen und trotzdem nie unter einer wirklich sauberen Decke schlafen.“ GH https://app.gethookd.ai/share/ad/125661932?signature=f787c134bed007bb6fe093c76e9db563304ede048b85626f76c9233c2b75debc · Meta https://www.facebook.com/ads/library/?id=1020681347385838 | Übersetzt |
| Advertorial „When did you last actually wash your duvet? Not the cover. The duvet itself.“ und Static 190141487 „What about dust mites? Wash the whole duvet at 40 degrees. Not just the cover.“ | MS **125661961** „Wann hast du deine Bettdecke zuletzt wirklich gewaschen? Nicht den Bezug, die Decke selbst.“ GH https://app.gethookd.ai/share/ad/125661961?signature=f4a9caceb7b9325cd7d704dc1eb89a90ca016b89a27e80abcc1b39e06ea27ae1 · Meta https://www.facebook.com/ads/library/?id=1344626053916338 | Übersetzt |
| **190147104** „…HOTEL ROOM EVERY SINGLE DAY?“ | MS **112081187** „Jeden Tag ein Bett wie im Hotel. Bezug plus Decke in einem. Vollwaschbar. In zwei Stunden trocken.“ GH https://app.gethookd.ai/share/ad/112081187?signature=4d6fcb92a41ecb364511c91898d5e1786c8b7adbdcfee34236b3f597291283d4 · Meta https://www.facebook.com/ads/library/?id=1769271164436256 | Angle übernommen |
| **189734435 / 189726176** „Karen, 52: … I do not know how it works, but I simply stay dry at night.“ | MS **139047107** „Ich weiß nicht, wie die Decke das macht, aber egal, ob heiße Sommernacht oder plötzlicher Wetterumschwung. Ich schlafe einfach…“ GH https://app.gethookd.ai/share/ad/139047107?signature=d92f3d774a51e16a6300c97ac99e88544f9fc74fb903be25e3686750f39f55f4 · Meta https://www.facebook.com/ads/library/?id=1847570229555369 | Testimonial übersetzt und als Static umgesetzt |
| „Never pull again. SALE - Duvet + cover IN ONE.“ | MS **180516162** „Nie wieder Bettwäsche wechseln. Decke + Bezug in EINEM“ GH https://app.gethookd.ai/share/ad/180516162?signature=74ea38819fd1c027c59bb810da449ee3690b6aee9183cc8f6336fcf44176124a · Meta https://www.facebook.com/ads/library/?id=1807384454013964 | Layout und Claim adaptiert |

**Sehr wahrscheinlich kopiert** (deutsches UGC-Footage oder deutsche Satzstellung, MS-Original nicht 1:1 gefunden):
- **189724449 / 190139667** „IMPORTANT, NOW IN SUMMER: IF YOU SWEAT AT NIGHT“ („WICHTIG, JETZT IM SOMMER: …“), echte Creatorin in deutscher Wohnung
- **189399853** „❌Never sweat at night again“ (vgl. MS MagicSleep 112080045 „NIE MEHR SCHWITZEN NACHTS – EISDECKE STATT SCHWITZDECKE“) GH https://app.gethookd.ai/share/ad/112080045?signature=a7c0bf67cdebd70c7faafeaad222244ccee96cb66ef9abf6a3da7490c6b22e21 · Meta https://www.facebook.com/ads/library/?id=2894910527516688
- **190147133** „Never sweat at night again ❌“ + „i don't know“ (= „Ich weiß nicht, wie die Decke das macht…“) GH https://app.gethookd.ai/share/ad/190147133?signature=68eaaf14ddff09298fa63ffe23c93925724b66c10687edc65a3477b72de95b89 · Meta https://www.facebook.com/ads/library/?id=2106878340223993
- **189724373** „LAST WASHED 6 WEEKS AGO“ (Hygiene, vgl. MS 139052723 „Du duschst jeden Abend. Und legst dich danach unter eine Decke, die du noch nie richtig gewaschen hast 🤮“) GH https://app.gethookd.ai/share/ad/139052723?signature=896c7500a00ec5ed474ea18d14e007ff27a9cea881361be3ad541baf859aa9ed · Meta https://www.facebook.com/ads/library/?id=2182272402331336
- **189724320** „THE STRUGGLE BEFORE CHANGING MY DUVET COVER!“ / „i used to hate laundry day“ GH https://app.gethookd.ai/share/ad/189724320?signature=6e87db6556d964f011f65d9edbb574766403591bb24897fedbd5f27c0446c799 · Meta https://www.facebook.com/ads/library/?id=1020850547634740
- Übersetzte Statics mit deutscher Grammatik: **190558980** „That's why you don't need a huge washing machine 😅 … Dries quickly even without a tumble dryer in just 2 hours … Simply throw it in. Done. No cover. No stress.“ (GH https://app.gethookd.ai/share/ad/190558980?signature=aaccdabd9f34483b4895acda64d4a56f4fcc171e3fb58cfd0367542d93c3a43e · Meta https://www.facebook.com/ads/library/?id=1018609411152617) und **190140645** „“You don't get the 2 pillowcases for ever free.” Offer ends soon - take part while you still can.“ (GH https://app.gethookd.ai/share/ad/190140645?signature=8c84c2aed52ac46b4f26b228798bc6483d9688c471b947464d70f50e3d480112 · Meta https://www.facebook.com/ads/library/?id=1031363033022296)

**Eigene Cozily-Ideen** (nicht bei MS gesehen; Kandidaten, die unser Kunde zurück nach DE spiegeln oder in UK schneller und besser machen kann):
- Overstock/Entschuldigung (188679985), Lagerverkauf-Statics (189397232 usw.)
- Geschenk an die Mutter (190140600)
- Waschsalon/„launderette“ (189722200, 189405420)
- Reverse Psychology „Don't buy“ und „I'm returning“ (189397062, 190558325)
- Family Bundle (189399929)
- Hund (190140714, Cozily am 07.08.; MS testet den Hund erst seit 02.10., 196670755)

---

### 8. Landingpage-Schnellcheck (curl, 08.10.2026)

| Punkt | Befund |
|---|---|
| Hauptprodukt | „EasySleep® Duvet – The 2-in-1 quick-dry duvet that eliminates the need for bed sheets.“ |
| **Preise (UK)** | Single 140×200 **£69.99** (statt £109.99) · Double 200×200 **£79.99** (statt £119.99/124.99) · King 230×230 **£84.99** (statt £124.99) · Super King 260×230 **£99.99** (statt £139.99). Badge „SAVE 36%“. |
| Preis US | $129.99 statt $189.99 (Advertorial-USA) |
| Farben | 7: Coastal Blue, Cream Beige, Chimney Red, Midnight Black, Moonstone Grey, Soft Mint Green, Sunset Orange |
| Gratis-Beigabe | 2 SoftCloud-Kissenbezüge „worth £49.99“ |
| Garantie (Marketing) | „40-night 100% money-back guarantee“, „no questions, no forms“, zurückgeschickte Decken gehen „to care homes and charities“ |
| **Garantie (Policy)** | Refund-Policy: 90 Tage, **„For hygiene reasons, we cannot accept returns of products that have already been used.“** Das widerspricht dem 40-Nächte-Probeschlafen. |
| **Lieferung** | „Orders are typically shipped within 12 hours … delivery generally takes between **6 to 9 business days**“ (Versand aus China) |
| **Review-Zahlen** | Advertorial: „4.9/5 \| Based on **7,980+** Reviews“ · PDP: „(**2788** Reviews)“ · Ads/Advertorial: „17,000+“ Kunden. Die Zahlen sind untereinander inkonsistent. |
| Technische Claims | „10.5 tog equivalent“, „ThermoBalance® fibres“, „OEKO-TEX certified“, „Dry in 2 hours“, „Fits a 6–7 kg drum“, Wäsche 40 °C (FAQ widerspricht sich: 40 °C vs. 50 °C) |
| Startseite | „Say goodbye to changing bed sheets forever.“ · „97% say their bed feels fresher“ · „87% reported sleeping better“ · „93% less bacteria“ |
| Sonstiges | Header im Oktober noch „SUMMER SALE ☀️“. Typo im Title-Tag „Advertorial EasySeep“. Gründerin „Jessica Smith“ und „Tobie Fallschmidt, MA“ aus Deutschland, beide vermutlich fiktiv. |

---

### 9. Was unser Kunde daraus machen sollte (UK first)

1. **Glaubwürdigkeit als Waffe.** Cozily ist ein China-Dropshipper mit 6–9 Werktagen Lieferzeit, Gmail-Kontakt und einer Rückgabe-Policy, die benutzte Ware ausschließt. Unser Kunde sollte **UK-Lager, Lieferung in 1–3 Tagen, ein echtes 40-Nächte-Probeschlafen mit kostenloser Rücksendung, UK-Kontakt und Trustpilot** in Creatives und LP sichtbar machen („Ships from the UK in 48h“, „Genuine 40-night trial – even if you've slept in it“).
2. **Originalmarke vor Kopie.** MS hat die Marken und das Original-Footage. Für UK eignen sich „The original EasySleep® – now in the UK“ und Creator-Content mit britischen Gesichtern, statt das deutsche Footage nur zu untertiteln, wie Cozily es tut.
3. **Bewährte Winner-Hooks zuerst und besser lokalisiert**, inhaltlich schon von Cozily validiert:
   - „I ordered the EasySleep duvet because…“ als echter britischer Creator
   - „When did you last actually wash your duvet? Not the cover.“
   - Waschsalon: „No launderette. No service wash.“
   - Hotelbett
   - Nachtschweiß-Testimonial einer Frau 50+
   - 63-Jährige(r): „gave me back my independence“
4. **Lücken besetzen, bevor Cozily sie kopiert:** Wechseljahre/Hitzewallungen (MS 196670813) GH https://app.gethookd.ai/share/ad/196670813?signature=18c04d33e4f05286ddb4bfdab9774e13d7241a51984b8736c07555d2620be093 · Meta https://www.facebook.com/ads/library/?id=1116906250849832. Gelenke/Arthrose (MS 196670581) GH https://app.gethookd.ai/share/ad/196670581?signature=e5a96a5e315b625f975238b8a61f8c6c33672b8b2180347f4772d5f22026f3f8 · Meta https://www.facebook.com/ads/library/?id=977761177919841. Winter-Wärme-Einwand (MS 196670101) GH https://app.gethookd.ai/share/ad/196670101?signature=3e5ff3a805e995959a3864b0fb19b9378cb4dfabfb2398618edf9f4b993c4f99 · Meta https://www.facebook.com/ads/library/?id=1412673014325623. „5 Gründe“-Listicle-Video (MS 196671368) GH https://app.gethookd.ai/share/ad/196671368?signature=a576b0c77fb5d304c2c69df7b5ae4b96ab08aaf5767f822655204d897252f638 · Meta https://www.facebook.com/ads/library/?id=1914664149698874.
5. **Weihnachten/Gifting:** Cozilys „Mum – … Love, Claire x“ ist ein Score-64-Winner. Unser Kunde sollte für Q4 eine eigene Gifting-Linie aufsetzen („The gift that makes Mum's week easier“), mit Geschenkverpackung und Lieferung vor Weihnachten aus UK. Hier kann Cozily mit 6–9 Tagen Lieferzeit nicht mithalten.
6. **Angebot nicht unterbieten, sondern strukturieren.** Cozily kommuniziert „40 % off“ und liefert real 29–36 %. Besser ist ein klares, ehrliches Angebot: Preis-Anker plus 2 Kissenbezüge plus UK Express. Dazu ein **Bundle/AOV** wie das „Family Bundle“ (189399929) und das Spannbettlaken-Upsell.
7. **Volumen einplanen.** Cozily launcht etwa 50 Ads pro Woche (Statics in 3 Formaten, KI-UGC-Avatare). Um in UK die Auktion zu gewinnen, braucht unser Kunde eine ähnliche Testing-Kadenz: mindestens 20–30 neue Creatives pro Woche, 60 % Static und 40 % Video, Advertorial als Haupt-LP.

---

### Anhang: Methodik & Datenhinweise
- Brand über `search_brands "cozily"` gefunden. `list_shops q="cozily"` ergab keinen Treffer für cozily-shop.com. `get_domain_advertisers cozily-shop.com` zeigt nur einen Advertiser.
- Alle 552 aktiven Ads sind über `search_ads` (brand_id 11837492, 19 Seiten à 30, sortiert nach Startdatum) **vollständig enumeriert**. Daraus stammen Formate, LPs und Kadenz. Die Sichtung der Creatives erfolgte über die mitgelieferten Previews (ca. 76) und `get_ad_media` für 12 Top-Statics. Die gesprochenen Hooks stammen aus `get_ad_hooks` und `get_ad`.
- **Startdaten:** Einige Ads mit älterer GetHooked-ID tragen ein späteres Startdatum (z. B. 30.09.). Das deutet auf Re-Launches bzw. Duplikate hin. Die Kadenz zeigt also „aktiv geschaltet ab“.
- **Performance-Score** ist GetHooked-intern (Impressions-Rang innerhalb der Brand, gedeckelt nach Laufzeit). Das Account-Maximum ist 64, die Score-64-Ads sind die relativ stärksten. Spend-Ranges und EU-Reach gibt es für UK/US nicht.
- Inaktive bzw. gestoppte Cozily-Ads sind nicht indexiert. Verlierer-Creatives lassen sich deshalb nicht auswerten.

---

### Anhang: Linkverzeichnis aller zitierten Cozily-Ads

| Ad-ID | Format | Hook/Headline (Kurz) | GetHooked | Meta Ad Library |
|---|---|---|---|---|
| 188679985 | Video | TRIPLE DEAL ENDS TONIGHT / I need to publicly apologize | [GH](https://app.gethookd.ai/share/ad/188679985?signature=cf14743cbc7ef6f2888a2fe433b32611ade5596c697818e0bec33e3e8210a5a4) | [Meta](https://www.facebook.com/ads/library/?id=1052591764343206) |
| 188681961 | Video | Triple Discount End tonight / apologize (Mann ~60) | [GH](https://app.gethookd.ai/share/ad/188681961?signature=6dd720c32e58e2f02e927911171ecedffb0cd7119d01f250bc2529ee80064191) | [Meta](https://www.facebook.com/ads/library/?id=29332012089722123) |
| 188368675 | Video | Triple Discount End tonight / apologize (Mann ~50) | [GH](https://app.gethookd.ai/share/ad/188368675?signature=479f9699de5a5c97b4733c19ff172911bebd8272f09e1474c1e4e896c13a9c1d) | [Meta](https://www.facebook.com/ads/library/?id=4056702414623797) |
| 190147104 | Video | HOTEL ROOM EVERY SINGLE DAY | [GH](https://app.gethookd.ai/share/ad/190147104?signature=20e1b0d1b34ee69181d9523613390f27374b2750020f4f202b0dd573ee10c61e) | [Meta](https://www.facebook.com/ads/library/?id=1069474352335265) |
| 190139671 | Video | Finally, an end to the bedsheet struggle | [GH](https://app.gethookd.ai/share/ad/190139671?signature=e5bdd8730429c31da6a2adfc60c8853ca0632306364540017b29dab4a128998e) | [Meta](https://www.facebook.com/ads/library/?id=1450070080298435) |
| 189399939 | Video | Say goodbye to changing bedsheets the hard way | [GH](https://app.gethookd.ai/share/ad/189399939?signature=629de4cb5a0c6a66555208fed79be10ffee0214e04e29bfe5cf4fa58435c4489) | [Meta](https://www.facebook.com/ads/library/?id=1765352407944812) |
| 189722200 | Video | IF YOUR DUVET DOESN'T FIT IN YOUR WASHING MACHINE | [GH](https://app.gethookd.ai/share/ad/189722200?signature=8416051deb9205f283139be0db4cf57c915186d9bee2ee513a0834dbf010321f) | [Meta](https://www.facebook.com/ads/library/?id=1400617288673382) |
| 189724348 | Video | WHY ARE PEOPLE DITCHING THEIR OLD DUVETS? | [GH](https://app.gethookd.ai/share/ad/189724348?signature=38cdb79583fb4765da2f8730c014721017ec63b97606dc1f4c4be5c494b1b6cc) | [Meta](https://www.facebook.com/ads/library/?id=2029805047661962) |
| 187361100 | Video | I'm 63 ... independence | [GH](https://app.gethookd.ai/share/ad/187361100?signature=615b4d414152597bcfeb03ddc2d0d16b4b769786f1b34a49cf93b05207a0ff05) | [Meta](https://www.facebook.com/ads/library/?id=1892926045003393) |
| 189724357 | Video | NEVER CHANGE THE BEDDING AGAIN (MS-Footage) | [GH](https://app.gethookd.ai/share/ad/189724357?signature=c3675cb4a7e40e014bb46e65657023acdcc481a1f2fa99e46c86d61892fbe043) | [Meta](https://www.facebook.com/ads/library/?id=1924056578550887) |
| 189724373 | Video | LAST WASHED 6 WEEKS AGO | [GH](https://app.gethookd.ai/share/ad/189724373?signature=b59b48ca5f0333f13c8ec5643a2c62ca552af0382c1e9bd6a38d5fa043ea66a7) | [Meta](https://www.facebook.com/ads/library/?id=1058919523184656) |
| 189399853 | Video | Never sweat at night again | [GH](https://app.gethookd.ai/share/ad/189399853?signature=1531cc34363d80bd82edd0bd94ff5d53657ea497797e2097eab40e17446bd457) | [Meta](https://www.facebook.com/ads/library/?id=1644912116606250) |
| 189724449 | Video | IMPORTANT, NOW IN SUMMER: IF YOU SWEAT AT NIGHT | [GH](https://app.gethookd.ai/share/ad/189724449?signature=2a4f774c381e487e6083c03b86bbab49632f230cfe13beb59543528088698f45) | [Meta](https://www.facebook.com/ads/library/?id=1684247762799791) |
| 190139667 | Video | IMPORTANT, NOW IN SUMMER + SAVE 35% | [GH](https://app.gethookd.ai/share/ad/190139667?signature=f224419b9cb2e09f5ce88f1993277702a61bdeb89843a0b7c440086391e333af) | [Meta](https://www.facebook.com/ads/library/?id=27866642696292765) |
| 190147133 | Video | Never sweat at night again / i don't know | [GH](https://app.gethookd.ai/share/ad/190147133?signature=68eaaf14ddff09298fa63ffe23c93925724b66c10687edc65a3477b72de95b89) | [Meta](https://www.facebook.com/ads/library/?id=2106878340223993) |
| 189724320 | Video | THE STRUGGLE BEFORE CHANGING MY DUVET COVER! | [GH](https://app.gethookd.ai/share/ad/189724320?signature=6e87db6556d964f011f65d9edbb574766403591bb24897fedbd5f27c0446c799) | [Meta](https://www.facebook.com/ads/library/?id=1020850547634740) |
| 189726663 | Video | One duvet. Zero hassle | [GH](https://app.gethookd.ai/share/ad/189726663?signature=35f614cb82c7c90f7d83d5de73db2076adca75914f5584e872dd7e304db95eff) | [Meta](https://www.facebook.com/ads/library/?id=867548059675967) |
| 189405389 | Video | Your bed just got an upgrade | [GH](https://app.gethookd.ai/share/ad/189405389?signature=746efb417781f53ca80981d04acb947c3fc28e61cef3cc295451c201c3200a11) | [Meta](https://www.facebook.com/ads/library/?id=1394493049453035) |
| 189396916 | Video | WE FINALLY STOPPED FIGHTING OVER THE DUVET | [GH](https://app.gethookd.ai/share/ad/189396916?signature=7c0c39e58d9486b242c8290a68d90c98076c56c93ee668c04a3f6abe38573f93) | [Meta](https://www.facebook.com/ads/library/?id=986346607835361) |
| 189398802 | Video | Why I threw out all my duvets last month ? | [GH](https://app.gethookd.ai/share/ad/189398802?signature=95ab5cb56844e8cfb52ae8b77eff816201d1d0d9aa98de6542567ea973a8eccc) | [Meta](https://www.facebook.com/ads/library/?id=2067520523864513) |
| 189399825 | Video | i was fed up (Mann ~55) | [GH](https://app.gethookd.ai/share/ad/189399825?signature=a67730194765919c49f66c1ece521a9c91137e5a576f9ccef2d3f8c60381e873) | [Meta](https://www.facebook.com/ads/library/?id=1590557842589558) |
| 190558325 | Video | I'm returning my EasySleep duvet | [GH](https://app.gethookd.ai/share/ad/190558325?signature=5042a326719c3520ecc9f427f27c0bfc7558751a427fd98f3b4d04d1e5e4ca86) | [Meta](https://www.facebook.com/ads/library/?id=1890720305246859) |
| 189722117 | Video | Never change your bedding again. Now in Cream Beige and Chimney Red. | [GH](https://app.gethookd.ai/share/ad/189722117?signature=5788423882ab14964f85e9dc25748da20646b78599ed12c4c1355696b8f53dab) | [Meta](https://www.facebook.com/ads/library/?id=1591763752291220) |
| 190139634 | Video | Wait (Waschmaschinen-Kampf) | [GH](https://app.gethookd.ai/share/ad/190139634?signature=f780dfcdd9d45d1d6a004d4c3538aa6b38fc9fdbac39a616cdf446a601b2b96f) | [Meta](https://www.facebook.com/ads/library/?id=1369744598648941) |
| 189396839 | Video | That's for changing the bed sheets | [GH](https://app.gethookd.ai/share/ad/189396839?signature=510c542433f496179a3488946e1d36a4752ca6ea070d19ead63e3a069fd19d21) | [Meta](https://www.facebook.com/ads/library/?id=1647420610328151) |
| 186737375 | Video | älteste aktive Ad (10.07.) | [GH](https://app.gethookd.ai/share/ad/186737375?signature=2e48a90e900459dc4df559be8b396a117d1143d18cacdc3470d74779baf4d8c0) | [Meta](https://www.facebook.com/ads/library/?id=1341400987542510) |
| 189734435 | Image | Karen, 52 (9:16) | [GH](https://app.gethookd.ai/share/ad/189734435?signature=9cdec0bd0787b60f5648ebd44c6e58bb47fb43e8545712c539263f9ecce5288a) | [Meta](https://www.facebook.com/ads/library/?id=4381606525423205) |
| 189726176 | Image | Karen, 52 (1:1) | [GH](https://app.gethookd.ai/share/ad/189726176?signature=61af38e4e8b6ca0701760a70feba82ed938af385d8a95529f6505f74ae33a5e5) | [Meta](https://www.facebook.com/ads/library/?id=948236428292035) |
| 189395739 | Image | Never pull again. (4:5) | [GH](https://app.gethookd.ai/share/ad/189395739?signature=ab939d60f494f2046dbb7223f9f6d0c23b77f782343b0b5539136843f1b15215) | [Meta](https://www.facebook.com/ads/library/?id=3179008848951738) |
| 189395750 | Image | Never pull again. (9:16) | [GH](https://app.gethookd.ai/share/ad/189395750?signature=6572083cda5121d7af5f4bf38e17997ffacb9fa19ab3583382a964a7bb8b1669) | [Meta](https://www.facebook.com/ads/library/?id=2052858648663946) |
| 190139594 | Image | Never pull again. (schwarz) | [GH](https://app.gethookd.ai/share/ad/190139594?signature=7e4ce19194a15845d3653f4f3f2e158394cd5dd002cd0fb049b48fbb277affc6) | [Meta](https://www.facebook.com/ads/library/?id=4502651596683019) |
| 189724503 | Image | Never pull again. (salbei, PDP) | [GH](https://app.gethookd.ai/share/ad/189724503?signature=861978691a95e25513f2f085baddd14fb39ec4fcbd18da0efe4ba55deb85c8ed) | [Meta](https://www.facebook.com/ads/library/?id=2088040342104588) |
| 190140600 | Image | Mum - no more fighting with the cover (9:16) | [GH](https://app.gethookd.ai/share/ad/190140600?signature=64270d925567b56d59313c88826f4dacef6ce5e15361ff005288d544e81e2083) | [Meta](https://www.facebook.com/ads/library/?id=884638551108416) |
| 189399821 | Image | Mum - no more fighting with the cover (4:5) | [GH](https://app.gethookd.ai/share/ad/189399821?signature=6d26f291d07d33c577d46965a209fa721c117868d45a1e70c8f69e815d20684e) | [Meta](https://www.facebook.com/ads/library/?id=1480725987314826) |
| 189397232 | Image | We've made too many. Help us clear them. | [GH](https://app.gethookd.ai/share/ad/189397232?signature=026f05568e07740a113b98caf9b7bbb5446bca779083bff3f28e85a986ca4bb6) | [Meta](https://www.facebook.com/ads/library/?id=1087915160456366) |
| 189723854 | Image | Warehouse Sale...now live! | [GH](https://app.gethookd.ai/share/ad/189723854?signature=8c28c2669ecef65eb42ca814587c2a416385b2208f3619c68f70bf4d14c5d3c4) | [Meta](https://www.facebook.com/ads/library/?id=1805727490841445) |
| 189399854 | Image | Stock is moving | [GH](https://app.gethookd.ai/share/ad/189399854?signature=1761d7f5a9f5b86f9ee00a63db5a20d1bc6e7169ce2059cf817ec08656ced7c1) | [Meta](https://www.facebook.com/ads/library/?id=1389938529959731) |
| 190147077 | Image | I didn't believe it. Until the first night. | [GH](https://app.gethookd.ai/share/ad/190147077?signature=82ee0dd43e98c7b2be7f9663adc0825e40f668d49043cafbedc57e06330826b1) | [Meta](https://www.facebook.com/ads/library/?id=1065508685810366) |
| 190141560 | Image | Looks new. Every time. | [GH](https://app.gethookd.ai/share/ad/190141560?signature=77ff00298a85bbf96fe7e89ea7d634791c3b1c3b59ea871427388577f54dd538) | [Meta](https://www.facebook.com/ads/library/?id=1536007064328602) |
| 190147148 | Image | ONLY UNTIL SUNDAY 2 PILLOWCASES FREE. | [GH](https://app.gethookd.ai/share/ad/190147148?signature=7806b691422f8422ed1334a350717d62f11b10551461334cef6dce63798deae1) | [Meta](https://www.facebook.com/ads/library/?id=1015761917903729) |
| 189724407 | Image | ONLY UNTIL FRIDAY 2 Pillowcases FREE | [GH](https://app.gethookd.ai/share/ad/189724407?signature=4703f92dbc6a42dd839e870163c027d4794aea157e206ff9b1a38edb003598ef) | [Meta](https://www.facebook.com/ads/library/?id=1013995984575612) |
| 190558896 | Image | Does it dry quickly? | [GH](https://app.gethookd.ai/share/ad/190558896?signature=11129729be30a8407d6faf7079bbea11c3402cbee5aba427a7b533b0c994ff57) | [Meta](https://www.facebook.com/ads/library/?id=2485927431817164) |
| 189405325 | Image | Never an empty corner. | [GH](https://app.gethookd.ai/share/ad/189405325?signature=6a1139a8e10080ea27d1c543aea918457e91e547489170668e0edad231193a48) | [Meta](https://www.facebook.com/ads/library/?id=1633360048160981) |
| 189398858 | Image | Our duvet makes every other one feel...meh. | [GH](https://app.gethookd.ai/share/ad/189398858?signature=b3c559bb80235007d5d5572da69079f6feaf4204fb052e0e0e35b87510efe7ac) | [Meta](https://www.facebook.com/ads/library/?id=1774720443972921) |
| 189726248 | Image | Everything you actually wanting to know | [GH](https://app.gethookd.ai/share/ad/189726248?signature=5c221f45268ce72f2e1ed0156a7ca317d21b82f71201db97155b7be63fa47768) | [Meta](https://www.facebook.com/ads/library/?id=1045449038368791) |
| 197407814 | Image | AUTUMN'S HERE. | [GH](https://app.gethookd.ai/share/ad/197407814?signature=f3179577688a90a983abb621da90266c1856326faa6e8c02921ac048c47cdeff) | [Meta](https://www.facebook.com/ads/library/?id=1417419460578927) |
| 197407503 | Image | 7 COLOURS ONE LESS THING TO WORRY ABOUT | [GH](https://app.gethookd.ai/share/ad/197407503?signature=7e99ffd19ded55960b6c33bbf26e92f6e2a4b81d707a8e0295a1f443e0fcda03) | [Meta](https://www.facebook.com/ads/library/?id=1408081458134690) |
| 197405824 | Image | LIGHT ENOUGH TO CARRY ONE-HANDED. | [GH](https://app.gethookd.ai/share/ad/197405824?signature=cd840433d54139aba98afbd638849ab0cf41e61b00e4eb218b6a3ecad24a107c) | [Meta](https://www.facebook.com/ads/library/?id=1065319596294234) |
| 197404388 | Image | PICK YOUR COLOUR. SKIP THE COVER. | [GH](https://app.gethookd.ai/share/ad/197404388?signature=02c926095aa9053ce88156f9a9d35c3b11893f7c37b36ab1d1285c58ce7e22a9) | [Meta](https://www.facebook.com/ads/library/?id=1114304077765899) |
| 190559121 | Image | 40% OFF Summer or winter, the same duvet | [GH](https://app.gethookd.ai/share/ad/190559121?signature=a9edf41e0a19f3aa679768c9cad2c4ba40c774a4c3ca38456a73c347186b32d5) | [Meta](https://www.facebook.com/ads/library/?id=2360215491385469) |
| 190558332 | Image | WHY BUY THREE... WHEN ONE DOES IT ALL? | [GH](https://app.gethookd.ai/share/ad/190558332?signature=7e0c8645448ed5e24b2a9edeef08c23f440c6f6443ea87f424bcc1faa0841a0f) | [Meta](https://www.facebook.com/ads/library/?id=1940656736894628) |
| 190175667 | Image | LAST CALL | [GH](https://app.gethookd.ai/share/ad/190175667?signature=8632a0a4a0567f8898f8ea669817048c936be55417dda11ad2b834637a426410) | [Meta](https://www.facebook.com/ads/library/?id=1492297926036017) |
| 190558231 | Image | THE SHELVES ARE FULL. | [GH](https://app.gethookd.ai/share/ad/190558231?signature=cba8f25ef2a0fea665fc65cb9334f31cfc17ba8064c52e2c0bed4fcec5f997ba) | [Meta](https://www.facebook.com/ads/library/?id=1752198692733367) |
| 190175694 | Image | 7 COLOURS. AN EASY CHOICE. | [GH](https://app.gethookd.ai/share/ad/190175694?signature=0a81ead345de74ae0c6a64d380a560b001d2b1e55f9ae89374779a14f2f980b3) | [Meta](https://www.facebook.com/ads/library/?id=1555585366320331) |
| 190175692 | Image | HOT COLD whiteboard | [GH](https://app.gethookd.ai/share/ad/190175692?signature=cf444ad4404cba1bb6ea9cbb09efd3e816e3e4f31819816e6fc8e0b326c4fed5) | [Meta](https://www.facebook.com/ads/library/?id=1552551079871891) |
| 190175678 | Image | EVERY THING MUST GO | [GH](https://app.gethookd.ai/share/ad/190175678?signature=bb3c05f24e91f279a8bc63fb76b673428299e947503bafaad4178a951ab11b50) | [Meta](https://www.facebook.com/ads/library/?id=1524006639746372) |
| 190558968 | Image | We're not angry. We're just 40% off now. | [GH](https://app.gethookd.ai/share/ad/190558968?signature=619206b61aa646107b43df619c767db62963122576575723335585bffba44238) | [Meta](https://www.facebook.com/ads/library/?id=1764646547943960) |
| 189397059 | Image | A normal duvet vs this one | [GH](https://app.gethookd.ai/share/ad/189397059?signature=f3c462de14c362d78df90712b5f86e301b5169ae764a6bcdd84fddff927354b7) | [Meta](https://www.facebook.com/ads/library/?id=29030442186592172) |
| 189397035 | Image | Two duvets. One obvious winner. | [GH](https://app.gethookd.ai/share/ad/189397035?signature=f6e7e218e825a484d4b86298194f9ca1b089ade29531217cff647569afd7113d) | [Meta](https://www.facebook.com/ads/library/?id=4652130688356155) |
| 190146305 | Image | Effortless. | [GH](https://app.gethookd.ai/share/ad/190146305?signature=c6dfe0c32fb7d1da8a60a6df8dd783e89d7be44600bae41323b2ffe1b98145c8) | [Meta](https://www.facebook.com/ads/library/?id=1095426712916209) |
| 190140724 | Image | The cover you wash. The duvet you never do. | [GH](https://app.gethookd.ai/share/ad/190140724?signature=f4ffbf89e6b89be759125598597cb22dff283f590efbd3adea771470c389f4f8) | [Meta](https://www.facebook.com/ads/library/?id=4584502161781457) |
| 189398761 | Image | No zip. No cover to thread. | [GH](https://app.gethookd.ai/share/ad/189398761?signature=37ecd794a44dd2e649af591b86e38414543a3afa684e424992c82f9bebd6bfe4) | [Meta](https://www.facebook.com/ads/library/?id=2372090983196715) |
| 189397062 | Image | Don't buy the EasySleep duvet. | [GH](https://app.gethookd.ai/share/ad/189397062?signature=2dfc366568a831fe0bf80a388ce2bb9a5227c967b8f24763a506fceb93f76cdd) | [Meta](https://www.facebook.com/ads/library/?id=1057306373578220) |
| 189399830 | Image | Only until Friday! 2 FREE pillowcases (PDP) | [GH](https://app.gethookd.ai/share/ad/189399830?signature=73473a2f015ebad40a3dd7e79957f15743814090824e6c34e56a6c28ac2589e8) | [Meta](https://www.facebook.com/ads/library/?id=1001718869591503) |
| 190558901 | Image | Warehouse Sale every colour must go! | [GH](https://app.gethookd.ai/share/ad/190558901?signature=67c2572267b8279b2a2558500ba9e6c883afe9944dc7a61c97499ac1a7eebabb) | [Meta](https://www.facebook.com/ads/library/?id=1827633148611912) |
| 190139642 | Image | 17,000 homes sleep like this | [GH](https://app.gethookd.ai/share/ad/190139642?signature=e28fb4a85c24fb7c6e027044d9629f457395167a65711e4919c3448f90df46c1) | [Meta](https://www.facebook.com/ads/library/?id=28726301933620635) |
| 190139624 | Image | This week only: 40% OFF + 2 FREE PILLOWCASES | [GH](https://app.gethookd.ai/share/ad/190139624?signature=ecf17459ec088928e01c75d4c79f07195516b7808f4eec04d1146ea5b2718495) | [Meta](https://www.facebook.com/ads/library/?id=4151980968287080) |
| 189734456 | Image | Never make the bed again. (Bushaltestelle) | [GH](https://app.gethookd.ai/share/ad/189734456?signature=b93c5efd72bfc061b73565ab76d7d9df77d781a37ab46a3eabb09cca35b7155d) | [Meta](https://www.facebook.com/ads/library/?id=28145391761787871) |
| 189726720 | Image | The old way: a wrestling match. | [GH](https://app.gethookd.ai/share/ad/189726720?signature=1f4205c32c8750a5261906c0099a8f60ab0cfc2d2d7f8742d02cff6462c3441d) | [Meta](https://www.facebook.com/ads/library/?id=1590760992700508) |
| 189405420 | Image | No launderette. No service wash. | [GH](https://app.gethookd.ai/share/ad/189405420?signature=f1b32f94ac7571165e2173c77c98c3caba8a7394dd9230abdc5e57ad9223b245) | [Meta](https://www.facebook.com/ads/library/?id=1405624548345997) |
| 189405448 | Image | Cannot decide? Start here. | [GH](https://app.gethookd.ai/share/ad/189405448?signature=9cff5d43ad1e5f57a4f127d93bb65741ca4048208076ea1d45da8d785f257b28) | [Meta](https://www.facebook.com/ads/library/?id=1721406789080140) |
| 189399940 | Image | last stock remaining / Only until Friday | [GH](https://app.gethookd.ai/share/ad/189399940?signature=def0dbc9a375ea714c6d96f904eaedeef04798a33a9270103eac36360748b4eb) | [Meta](https://www.facebook.com/ads/library/?id=1756902378652478) |
| 189399931 | Image | Seven colours. Not one duvet cover. | [GH](https://app.gethookd.ai/share/ad/189399931?signature=bc33910e934e65e76bda73ddf2e0311ffc501109c5336b1a50d091f754bbc0ba) | [Meta](https://www.facebook.com/ads/library/?id=1974425536553281) |
| 189399860 | Image | STOP BUYING DUVET COVERS | [GH](https://app.gethookd.ai/share/ad/189399860?signature=20f968661e839d6215f0e5fe32fa6d9855befb01ca967211f3431ed4ce4dce19) | [Meta](https://www.facebook.com/ads/library/?id=1506437151288152) |
| 190141494 | Image | A FRESH START - BIG SAVINGS! UP TO -36% | [GH](https://app.gethookd.ai/share/ad/190141494?signature=1512d1a442a393af576da5b12b91ddff64568f58b0db86a07b4990d8357a6f1c) | [Meta](https://www.facebook.com/ads/library/?id=1426870062592801) |
| 190558960 | Image | Once you have this one the others are pointless | [GH](https://app.gethookd.ai/share/ad/190558960?signature=df996470f4dc6fd68d9d3272793e0a51f5939c5e6cf67a190daa9cac46360ba4) | [Meta](https://www.facebook.com/ads/library/?id=1822932675783492) |
| 190140714 | Image | With the dog on the bed. And still clean. | [GH](https://app.gethookd.ai/share/ad/190140714?signature=af594a5eb5877afa073062d1a4b8b008c973515627543c95699462354ac022e2) | [Meta](https://www.facebook.com/ads/library/?id=1760082745119124) |
| 190140645 | Image | You don't get the 2 pillowcases for ever free. | [GH](https://app.gethookd.ai/share/ad/190140645?signature=8c84c2aed52ac46b4f26b228798bc6483d9688c471b947464d70f50e3d480112) | [Meta](https://www.facebook.com/ads/library/?id=1031363033022296) |
| 190141487 | Image | What about dust mites? | [GH](https://app.gethookd.ai/share/ad/190141487?signature=03fbc187d7809c11fb056e4e46e89390ee9f67c6144932f05777dffa2ad818a7) | [Meta](https://www.facebook.com/ads/library/?id=2027961381172257) |
| 190139665 | Image | WHY BUY TWO... WHEN ONE DOES BOTH? | [GH](https://app.gethookd.ai/share/ad/190139665?signature=0bd803ee90db3b968bf7a4334f5c2d11293b7a1488fc9f40ba20f066904e9c4e) | [Meta](https://www.facebook.com/ads/library/?id=3204030089984436) |
| 189724500 | Image | YOUR BED IS MADE IN TEN SECONDS. | [GH](https://app.gethookd.ai/share/ad/189724500?signature=ead85911ee301f6a63914d29988582ece097d9db33c0bb82fbc9ff2f1be72888) | [Meta](https://www.facebook.com/ads/library/?id=1640105387681826) |
| 189722225 | Image | 17,000 people have stopped buying duvet covers. | [GH](https://app.gethookd.ai/share/ad/189722225?signature=29fd368ca68453003a9ec487e9243568285bf70d7fbb854e662d2fbadcc182c1) | [Meta](https://www.facebook.com/ads/library/?id=1537687374250751) |
| 189399929 | Image | Three beds in the house. Three duvets. (Family Bundle) | [GH](https://app.gethookd.ai/share/ad/189399929?signature=f7c91a824b32cd657dec329f712cc089334a45308dc022338f240a34e5220241) | [Meta](https://www.facebook.com/ads/library/?id=1042169218538481) |
| 190558980 | Image | That's why you don't need a huge washing machine | [GH](https://app.gethookd.ai/share/ad/190558980?signature=aaccdabd9f34483b4895acda64d4a56f4fcc171e3fb58cfd0367542d93c3a43e) | [Meta](https://www.facebook.com/ads/library/?id=1018609411152617) |
| 190140606 | Image | Lost quality after washing? | [GH](https://app.gethookd.ai/share/ad/190140606?signature=7919d9111cd49ca569deab1a29fe27c91b56b93ad7c83b80142fe15127bb8439) | [Meta](https://www.facebook.com/ads/library/?id=964548543310305) |
| 190171503 | Image | She's worth every penny. | [GH](https://app.gethookd.ai/share/ad/190171503?signature=988aba25a994bcf174dd16528976506e3a6487cdec6b7652ef0f44ae6e6a4910) | [Meta](https://www.facebook.com/ads/library/?id=2266956880786667) |
| 190558622 | Image (US) | WASH IT MORE THAN ONCE A MONTH. GUARANTEED. | [GH](https://app.gethookd.ai/share/ad/190558622?signature=2e210f2998a897546f4b15bf8130919d9a0d22395b3c736f4dfab6ca73c41ce4) | [Meta](https://www.facebook.com/ads/library/?id=847810781722982) |
| 190146383 | Image (US) | YOUR DUVET MIGHT BE PART OF THE PROBLEM. | [GH](https://app.gethookd.ai/share/ad/190146383?signature=c5d36933283b9fbac17406cb5966bb01a68de4fee415d05e03d269a612520f50) | [Meta](https://www.facebook.com/ads/library/?id=1106790145139441) |
| 189733489 | Image (US) | DIAGNOSED. NOW WASHABLE. | [GH](https://app.gethookd.ai/share/ad/189733489?signature=7319e6fbb389baad5ceab2c6040f7484b8dd3d2c8fd138e69a947de9fdf429f1) | [Meta](https://www.facebook.com/ads/library/?id=973304582487664) |
| 189400477 | Image (US) | WASH IT FOR YOUR ALLERGIES. NOT AGAINST YOUR WILL. | [GH](https://app.gethookd.ai/share/ad/189400477?signature=c83211c2a3854d2d65f5d7d3c05de8d99a18a98ca7571cbcb44243c16d749435) | [Meta](https://www.facebook.com/ads/library/?id=4344461482533722) |
| 189396915 | Image (US) | WASH IT AT BREAKFAST. SLEEP UNDER IT TONIGHT. | [GH](https://app.gethookd.ai/share/ad/189396915?signature=35462e72cb17423144446868c85c6d4d935be8fdffb5af95805d1124f9481530) | [Meta](https://www.facebook.com/ads/library/?id=4071958376442603) |

### Anhang: Linkverzeichnis der zitierten Magic-Splashy-Vergleichs-Ads (brand_id 88310)

| Ad-ID | Format | Hook/Headline (Kurz) | GetHooked | Meta Ad Library |
|---|---|---|---|---|
| 179252420 | Image | Primärtext 'Decke + Bezug in einem' / 'Unsere Kunden in 3 Worten' | [GH](https://app.gethookd.ai/share/ad/179252420?signature=b705ffb54efd1b5a03448c8012cc9821cb489e17ae0193cf7888c47b270547f2) | [Meta](https://www.facebook.com/ads/library/?id=1820936862425780) |
| 180516162 | DCO | Nie wieder Bettwäsche wechseln. Decke + Bezug in EINEM | [GH](https://app.gethookd.ai/share/ad/180516162?signature=74ea38819fd1c027c59bb810da449ee3690b6aee9183cc8f6336fcf44176124a) | [Meta](https://www.facebook.com/ads/library/?id=1807384454013964) |
| 112080045 | Image | NIE MEHR SCHWITZEN NACHTS (MagicSleep) | [GH](https://app.gethookd.ai/share/ad/112080045?signature=a7c0bf67cdebd70c7faafeaad222244ccee96cb66ef9abf6a3da7490c6b22e21) | [Meta](https://www.facebook.com/ads/library/?id=2894910527516688) |
| 126012757 | Video | DAS WARS MIT BETTWÄSCHE WECHSELN! / Ich habe die Easy-Sleep-Decke bestellt | [GH](https://app.gethookd.ai/share/ad/126012757?signature=4aa5cf75157a813c3daede61927240a452d4bf09046a0feee9ae288bd457658f) | [Meta](https://www.facebook.com/ads/library/?id=1572451867734657) |
| 125662052 | Video | Nie wieder Bettbeziehen (Creator mit Brille) | [GH](https://app.gethookd.ai/share/ad/125662052?signature=afca98f12b6dd400226ecbd2adcf32983adb04f2c06b179d502bd583a5f9a763) | [Meta](https://www.facebook.com/ads/library/?id=2025964218008688) |
| 129130363 | Video | Nie wieder Bettbeziehen (Creator mit Brille) | [GH](https://app.gethookd.ai/share/ad/129130363?signature=2280883cdc1b06d68811f8455bca14dbebe3878407f4246090cb2afb6c5c467c) | [Meta](https://www.facebook.com/ads/library/?id=1534211127599850) |
| 125661932 | Video | Über 15 Jahre lang jede Woche das Bett frisch beziehen | [GH](https://app.gethookd.ai/share/ad/125661932?signature=f787c134bed007bb6fe093c76e9db563304ede048b85626f76c9233c2b75debc) | [Meta](https://www.facebook.com/ads/library/?id=1020681347385838) |
| 125661961 | Video | Wann hast du deine Bettdecke zuletzt wirklich gewaschen? | [GH](https://app.gethookd.ai/share/ad/125661961?signature=f4a9caceb7b9325cd7d704dc1eb89a90ca016b89a27e80abcc1b39e06ea27ae1) | [Meta](https://www.facebook.com/ads/library/?id=1344626053916338) |
| 112081187 | Video | Jeden Tag ein Bett wie im Hotel | [GH](https://app.gethookd.ai/share/ad/112081187?signature=4d6fcb92a41ecb364511c91898d5e1786c8b7adbdcfee34236b3f597291283d4) | [Meta](https://www.facebook.com/ads/library/?id=1769271164436256) |
| 139047107 | Video | Ich weiß nicht, wie die Decke das macht | [GH](https://app.gethookd.ai/share/ad/139047107?signature=d92f3d774a51e16a6300c97ac99e88544f9fc74fb903be25e3686750f39f55f4) | [Meta](https://www.facebook.com/ads/library/?id=1847570229555369) |
| 139052723 | Video | Du duschst jeden Abend ... (inaktiv seit 19.09.) | [GH](https://app.gethookd.ai/share/ad/139052723?signature=896c7500a00ec5ed474ea18d14e007ff27a9cea881361be3ad541baf859aa9ed) | [Meta](https://www.facebook.com/ads/library/?id=2182272402331336) |
| 196670813 | Video | Guter Schlaf in den Wechseljahren | [GH](https://app.gethookd.ai/share/ad/196670813?signature=18c04d33e4f05286ddb4bfdab9774e13d7241a51984b8736c07555d2620be093) | [Meta](https://www.facebook.com/ads/library/?id=1116906250849832) |
| 196670581 | Video | ...weil ich mit meinen Gelenken keine Kraft hatte | [GH](https://app.gethookd.ai/share/ad/196670581?signature=e5a96a5e315b625f975238b8a61f8c6c33672b8b2180347f4772d5f22026f3f8) | [Meta](https://www.facebook.com/ads/library/?id=977761177919841) |
| 196670101 | Video | Nur 44% der Easy-Sleep-Kunden ... Herbst- und Winternächte | [GH](https://app.gethookd.ai/share/ad/196670101?signature=3e5ff3a805e995959a3864b0fb19b9378cb4dfabfb2398618edf9f4b993c4f99) | [Meta](https://www.facebook.com/ads/library/?id=1412673014325623) |
| 196670755 | Video | Dieser Hund könnte erklären ... | [GH](https://app.gethookd.ai/share/ad/196670755?signature=5b342ba6dc43b0bc37f0a924e0f79d75fd204eef4c31f9e75379adecbc676706) | [Meta](https://www.facebook.com/ads/library/?id=1447587467313561) |
| 196671368 | Video | Fünf Gründe, warum deine Bettdecke ein Update braucht | [GH](https://app.gethookd.ai/share/ad/196671368?signature=a576b0c77fb5d304c2c69df7b5ae4b96ab08aaf5767f822655204d897252f638) | [Meta](https://www.facebook.com/ads/library/?id=1914664149698874) |



# D4 UK-Marktscan & Sättigungskarten

## UK-Marktscan: Coverless- / 2-in-1-Bettdecken (Meta Ads)

**Stand:** 08.10.2026 · **Quelle:** GetHooked Ad Library (search_ads, aggregate_ads, get_domain_advertisers) und Landingpages, mit curl abgerufen · **Auftrag:** UK-Sweep ohne Pleene und Cozily (beide werden von Kollegen abgedeckt, hier nur gelistet) · **Referenz:** Magic Splashy „EasySleep®“ (magicsplashy.de)

Linkformat pro Ad: `GetHooked-ID` → [GH] = GetHooked-Share-Link, [Meta] = Meta Ad Library.

---

### 1. Kernaussagen (TL;DR)

1. **Der Magic-Splashy-Funnel ist in UK schon 1:1 angekommen, und zwar bei Kallyon, nicht nur bei Pleene/Cozily.** kallyon.com (GBP, erste Ad am 09.08.2026, 52 aktive Ads) verkauft „EasySleep – The quick-drying 2-in-1 duvet that makes duvet covers unnecessary“ mit „ThermoBalance® climate fiber“, „2 SoftCloud® pillowcases (value: £49.99)“, „40-night sleep trial“, „Dries in approx. 2 hours“, „No sweating, no freezing“ und „17,000 other people are already sleeping better“. Auf der Landingpage steht sogar noch der deutsche Social-Proof-Name „Anna-Maria Zimmermann“. USPs, Offer und Preisanker stammen also schon von MS.
2. **Die Clone-Welle beschleunigt sich.** Nach Pleene (seit 11.06.) und Cozily (seit 10.07.) kamen Kallyon (09.08.), Ryva (16.09.), Moonora (28.09.) und Nuvex (29.09., vor allem IT/ES). Fast alle Clones nutzen dasselbe Copy-Gerüst, wörtlich von Pleene übernommen: „Duvet + Cover in One 🌙 … ✓ No more wrestling … ✓ cool in summer, cosy/warm in winter ✓ Hypoallergenic and antibacterial … 2 pillowcases FREE (£49.99 value) … X nights to try it risk-free.“
3. **Gesättigt sind in UK:** der Convenience-Angle (kein Bezug mehr), Quick-Dry und All-Season als **Bullet-Punkte**, Gratis-Kissenbezüge plus Probenächte als Offer, Rabatt-Anker (−40 bis −50 %), UGC-Video („I haven't changed my bed linen in three months“) und Produkt- bzw. Feature-Icon-Statics.
4. **Leer (Whitespace) sind in UK:** Menopause/Hitzewallungen (in den USA massiv genutzt, im UK-Duvet-Segment gar nicht), Senioren bzw. Arthritis/„Bettenmachen ab 60“ (kein einziger Advertiser), Geschenk für Eltern/Mum zu Weihnachten (kein Duvet-Advertiser), Hausstaubmilben/Hygiene als **Haupt-Hook** (nur als Bullet; in UK laufen aber Milben-Advertorials für Geräte seit 245–436 Tagen), Experte/Arzt, Advertorial- und Listicle-Landingpages, Quiz, Vergleichstabelle als Ad, Before/After-Static sowie Testimonials **mit Altersangabe** (MS-Signatur 48–63 J.).
5. **Tog fehlt bei allen Clones.** Die etablierten UK-Anbieter (Silentnight, Night Lark, OHS, Hygge Sheets, Duvet Hog) kommunizieren alle in Tog (2.5 / 4.5 / 7.5 / 10.5 / 13.5). Kein Clone nennt einen Tog-Wert, alle sagen nur „cool in summer, warm in winter“. Wer zuerst eine glaubwürdige Tog-Übersetzung des All-Season-Versprechens bringt, schließt eine echte Lücke.
6. **Preisband UK (Clones):** £59.99–£109.99 pro Decke (Kallyon), £64.99 (Ryva), £69.99 bzw. 2 Stück für £109.99 / 3 für £149.99 (Moonora), jeweils mit durchgestrichenem Preis von £99.99–£159.99. Etablierte Marken: Night Lark £70/£90/£100 (10.5 Tog), Kinder-Coverless von Hygge £24.99.

---

### 2. Methodik und Datenlage (wichtig für die Interpretation)

- Alle 12 Pflicht-Queries liefen zuerst mit `geo="GB"` und `language="en"`. **Ergebnis: Der GB-Filter ist für diese Kategorie kaum brauchbar.** (a) Die semantische Suche fiel bei GB-Filtern fast immer per Timeout auf reine Keyword-Suche zurück. (b) Viele UK-Ads haben in GetHooked **keine Länderdaten**: Eine Query meldete `excluded_no_geo = 23`, und Moonora, Kallyon, Ryva und Night Lark haben überwiegend `countries: []`. Beispiel: „all season duvet“ mit geo=GB brachte nur 2 irrelevante Musik-Ads, „duvet without cover“ und „2 in 1 duvet“ mit geo=GB nur fachfremde Advertorials.
- **Deshalb** liefen die Queries zusätzlich ohne geo (nur `language=en`). Ob ein Advertiser UK-relevant ist, habe ich anhand von Domain, GBP-Währung auf der Landingpage, UK-Größen und £-Preisen in der Copy eingeordnet.
- Die Creative-Taxonomie (`cls_angle` usw.) ist für die neuen Clone-Brands noch **nicht analysiert** (aggregate_ads lieferte leere Gruppen). Angles und Formate sind daher manuell aus Copy und Thumbnails codiert.
- Laufzeiten: Bei fast allen Clones ist `days_active` noch kurz (3–48 Tage). Der `performance_score` ist bei jungen Ads gedeckelt (optimized/winning brauchen ≥ 7 bzw. ≥ 14 Tage). Der einzige echte Langläufer-Winner im Segment ist Pleenes UGC-Video (`145443331` ([GH](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) · [Meta](https://www.facebook.com/ads/library/?id=1440933327878495)), Score 100, seit 14.08.).

---

### 3. Wettbewerber-Landkarte UK

#### 3a. Direkte Wettbewerber (Coverless / 2-in-1, UK-Shop)

| Advertiser (GetHooked brand_id) | Domain / Markt | Aktive Ads | Start im Segment | Positionierung | Offer |
|---|---|---|---|---|---|
| **Pleene** (7553008), *Kollegen* | pleene.com / pleene.uk, GBP, startet jetzt auch in den USA | 145 auf pleene.com | 11.06.2026 | „EasyRest“, Duvet + Cover in One | 2 Kissenbezüge gratis (£39.99), 90-night trial |
| **Cozily Store** (11837492), *Kollegen* | cozily-shop.com | 552 | 10.07.2026 | „covering-easysleep®-the-2-in-1-quick-dry-duvet-that-eliminates-the-need-for-bed-sheets“ (LP-Slug) | – (nicht geprüft) |
| **Kallyon** (11879647) | kallyon.com, GBP + ES/EUR | 52 | 09.08.2026 | **MS-1:1-Clone** („EasySleep“, ThermoBalance, SoftCloud) | 2 SoftCloud-Bezüge (£49.99), 30/40/100 Nächte (getestet), ab £59.99 |
| **Moonora** (13962083) | trymoonora.com, GBP, „Free UK delivery“ | 20 (19 Video, 1 Static) | 28.09.2026 | „The All-in-One Duvet“, 60 °C waschbar | £69.99 (statt £139.99), Bundles 2/3 Stück, 2 Bezüge (£49.99), 40 Nächte |
| **Ryva** (11837653) | shop-ryva.com, GBP | 4 | 16.09.2026 | „the 2-in-1 duvet that makes the duvet cover obsolete. For good.“ | £64.99 (statt £99.99), 2 Bezüge (£49.99), 100 Nächte, „Up to 40% off“ |
| **Nuvex** (15578000) | try-nuvex.com, Standard USD, mit GBP/AUD/CAD | 31 (überwiegend IT/ES-Copy) | 29.09.2026 | „CloudWrap® 2-in-1 Duvet“, „ClimaFlow®“ | bis −40 %, 2 Bezüge, 40 Nächte |
| **Night Lark / Fine Bedding Co.** (7106888) | finebedding.co.uk | 56 | Kampagnen-Refresh 30.08.–20.09.2026 | etablierte UK-Marke (vorher „Night Owl“), Kinder + Eco, Chester-Zoo-Kooperation | 10 % auf die erste Bestellung, 15 % auf Decke + Kissen |
| **Hygge Sheets** (252391) | hygge-sheets.com | 208 (gesamt) | 17.06.2026 | Kinder-Coverless, Bettnässen-Angle | £24.99, Gratisversand ab £30 |
| **Online Home Shop (OHS)** (212923) | onlinehomeshop.com | 568 (gesamt) | DPA seit 25.09.2026 | Retail-Range Coverless 4.5/7.5/10.5/13.5 Tog | Katalog/DPA |
| **Julian Charles Home** (7587928) | juliancharles.co.uk | 33 | 05.09.2026 | Händler für die Silentnight „Summer Breeze reversible coverless duvet“ 2.5 Tog | Code EXTRA15, „UP TO 70% OFF“ |

#### 3b. Angrenzende Wettbewerber und Referenzen (UK-Kontext)

- **Holsper** (282151, holsper.co.uk): „Easy Change“-Bettwäsche mit Reißverschluss an drei Seiten. Löst dasselbe Problem (Bezug), aber mit Bezug. Testimonial-Static „"Zip along three sides? Genius."“, `168691365` ([GH](https://app.gethookd.ai/share/ad/168691365?signature=38699f0616e36193f709a68cd05e365fef2e9fa8010b93624e5e8f23af049ba2) · [Meta](https://www.facebook.com/ads/library/?id=2597199830742409)) (Score 86), `162395799` ([GH](https://app.gethookd.ai/share/ad/162395799?signature=8418424988ebe3aee6c1a0bcb7dd9c98d12afa112681b580e8a39ec2ee6ae1bf) · [Meta](https://www.facebook.com/ads/library/?id=27868536366146250)), `165192427` ([GH](https://app.gethookd.ai/share/ad/165192427?signature=14e06e2af04275f743757ca51ce5efe546c3aa9ca8f32da18c6baa3f0250fc4e) · [Meta](https://www.facebook.com/ads/library/?id=1718961119184858)).
- **Silentnight via freemans** (163400): DPA „Silentnight All Seasons 3 in 1 Duvet“, `127943305` ([GH](https://app.gethookd.ai/share/ad/127943305?signature=5e8171b0b0d96b71687692d4de213e110b75f5d7b25c3f10477763f1d9270ea8) · [Meta](https://www.facebook.com/ads/library/?id=1013401628101649)) (GB, Juli–Aug. 2026). Das ist der klassische UK-All-Season-Ansatz: zwei Decken mit 4.5 + 9 Tog kombinierbar.
- **DUVET HOG** (14099886, duvethog.co.uk): normale, tierfreie Decke (Bezug empfohlen), Tog 4.5 / 10.5 / 13.5, £94–£139, „60 Nights to Know“. `189521382` ([GH](https://app.gethookd.ai/share/ad/189521382?signature=962ddc4f2482bad9cf5450a779def34dea42a977320344d117e0f822f3f7f50e) · [Meta](https://www.facebook.com/ads/library/?id=1655238635683167)) „Clean. Dry. Undisturbed.“ (130 Tage aktiv), `189521703` ([GH](https://app.gethookd.ai/share/ad/189521703?signature=4b09c25ba1644e27b2aa0d4b52258f83ed7f868ba19a2a3f4377054c4da4513a) · [Meta](https://www.facebook.com/ads/library/?id=1382693590575589)) „Summer Warm Duvet“.
- **NakedLab** (7620929, nakedlab.com, Brand aus Hongkong mit £-Shop): Bambus-Decke, nur Trockenreinigung. Angles: Milben, Nachtschweiß, Temperatur. `182677849` ([GH](https://app.gethookd.ai/share/ad/182677849?signature=5e2d211cfbe47638eeb08b183455d6cbc778caf65b391debdc293d52c1ac4078) · [Meta](https://www.facebook.com/ads/library/?id=1772141880577256)) „No More Night Sweats: 100% Bamboo Duvet“, `182677828` ([GH](https://app.gethookd.ai/share/ad/182677828?signature=c33309d2c9048e79b25014c38a21177a7a7bc2874a3d4a3f3013b06bd18fe7c4) · [Meta](https://www.facebook.com/ads/library/?id=1465123235428986)), `182677837` ([GH](https://app.gethookd.ai/share/ad/182677837?signature=0e65fbfd9d19e83c19cd037427826b9439962b0ac1b89fc7c6ca77b6a0e3e179) · [Meta](https://www.facebook.com/ads/library/?id=1745012746729996)).
- **Absolute Home Textiles** (551427): DPA „4.5 Tog Single Easy Care Duvet - Single Piece“, `121073563` ([GH](https://app.gethookd.ai/share/ad/121073563?signature=f822b8bd93a46382dccc04ac9f144e2cc5f56fd4e725c7798ddb3cdbcfdbe36f) · [Meta](https://www.facebook.com/ads/library/?id=1262930294712215)) (GB, 728 Tage Laufzeit).
- **The Lad Collective** (87245, UK-Marke): „All Seasons Magnetic Duvet“ mit Magnet-Ecken gegen Verrutschen im Bezug, **nur USA**: `200735947` ([GH](https://app.gethookd.ai/share/ad/200735947?signature=caab0bc2b1f910e137f0570a9aeb71cab8e8e9a746e2e27137403d81d8e49212) · [Meta](https://www.facebook.com/ads/library/?id=1761963314857623)).
- **Kabode** (199645, kabode.co.uk): Kinderbettwäsche „Breathable Bedding Parents Trust“, `122173844` ([GH](https://app.gethookd.ai/share/ad/122173844?signature=0991c8f189c93cc18ce9c0eb9932dbe6444e14815e582c7a43557775cab55ca3) · [Meta](https://www.facebook.com/ads/library/?id=2722844258072293)) (GB, 296 Tage, Score 100).
- **ZLEEPY** (241783): Bettwäsche-Hygienespray, GB: „Say Goodbye to Night Sweat Odour“ `122483614` ([GH](https://app.gethookd.ai/share/ad/122483614?signature=1e9dcf1ccd0cc8abdb6e3f9576158b1a1bbf8ec102078d0d2c4227a6182acd1b) · [Meta](https://www.facebook.com/ads/library/?id=974913134938324)), „Your sheets are dirtier than you think 🦠“ `122483597` ([GH](https://app.gethookd.ai/share/ad/122483597?signature=90a1e09315850e62688c398ef358626962bb4f330de0793d7c5b8044bac31934) · [Meta](https://www.facebook.com/ads/library/?id=971163668899126)).
- **DetoxSpa UK / Families vs. Dust Mites** (getuvlizer.co.uk): Milben-Advertorials für einen UV-Sauger, siehe Abschnitt 9.
- **Nicht-UK, aber zur Einordnung:** Brooklinen (US) „No Duvet Cover Required“ `81348902` ([GH](https://app.gethookd.ai/share/ad/81348902?signature=4e33785b84ff0efe4cc2f34d2bea37478b4e3d20d9e7c0ec96b026e16e425f29) · [Meta](https://www.facebook.com/ads/library/?id=25172670035741653)), Doze Bedding (US) „This Is Not Your Normal Duvet“ `132509351` ([GH](https://app.gethookd.ai/share/ad/132509351?signature=cac98d3f1a8e078f4064d5b1fb2cd23c95fa1295fee3d79ed2122bd3c079b104) · [Meta](https://www.facebook.com/ads/library/?id=1541445117681549)) (Score 100, 168 Tage), Sleep Club (AU) „Never change your bedding again 🛏️“ `186823970` ([GH](https://app.gethookd.ai/share/ad/186823970?signature=155009e86eedbf32ba7462cce981904290fbafd35f1f2ef56f8d1a045ea4fd53) · [Meta](https://www.facebook.com/ads/library/?id=1833359314499238)), Folkness (SE/NL) „Make your bed with Folkness in 15 seconds 👆“ `133205922` ([GH](https://app.gethookd.ai/share/ad/133205922?signature=61169968f9e91d26c12a6ddd97037853cd9fb22bf347778c4cf1f4c8f212d2a6) · [Meta](https://www.facebook.com/ads/library/?id=1793027032372033)) (Score 100, 106 Tage).

---

### 4. Query-für-Query-Protokoll

> „GB“ = Lauf mit geo=GB, „EN“ = Lauf mit language=en ohne geo. Aufgeführt sind nur UK-relevante Treffer; fachfremde Treffer werden als Rauschen markiert.

**Q1 „no duvet cover“ (GB, 22 Treffer, 10 davon unscharf/fachfremd)**
- Hygge Sheets: DPA „Coverless Duvets for Little Kids!“ `113915599` ([GH](https://app.gethookd.ai/share/ad/113915599?signature=b60744d7340d2f5bff38d07fbd4830614f1810770d0c67098414f4ddc2fc028e) · [Meta](https://www.facebook.com/ads/library/?id=1836974440611547)) (seit 17.06., 114 Tage, Score 86, Collection-Page). Hook: „When your child has a nighttime accident, changing bedding is the last thing you want to do.“ Bullets: „✔ Built-in cover — no duvet covers needed ✔ Machine washable and super quick to dry ✔ Lightweight, breathable 4.5 tog comfort ✔ Reversible design with matching pillowcase included“. Dazu UGC-Video „Coverless Duvets made for little ones 🩷“ `133953992` ([GH](https://app.gethookd.ai/share/ad/133953992?signature=ddd88ceeb1444a518b91779f93312a73ec2a71be4d4acfef1f6f16d69acc793f) · [Meta](https://www.facebook.com/ads/library/?id=1750897266250923)) (seit 05.08., Score 86).
- Pleene *(Kollegen)*: „No More Fighting With Duvet Covers“ (Static `193234215` ([GH](https://app.gethookd.ai/share/ad/193234215?signature=92968440b95005fe0fc1bf85409c9b3366e3ae8f6dbf240ce5448a242e85affb) · [Meta](https://www.facebook.com/ads/library/?id=1068343922634373)), Video `182988111` ([GH](https://app.gethookd.ai/share/ad/182988111?signature=3946cc0bedfae59cd046d6e8d5c8ada264c91345b8d4ccb1192ee02716cb1b00) · [Meta](https://www.facebook.com/ads/library/?id=1084737137379454))), „NEW: Lavender Mist“ `185228766` ([GH](https://app.gethookd.ai/share/ad/185228766?signature=f4be2b097e5b58bb0f5013dc8e461a8cea74051b0e8dfd5a28059f540eaf99fb) · [Meta](https://www.facebook.com/ads/library/?id=1401480008764681)) („dry in 2 hours“, 2 Bezüge, 90 Nächte).
- Night Lark: DPA „Night Lark® Soft Weave Coverless Duvet Set“ `184689041` ([GH](https://app.gethookd.ai/share/ad/184689041?signature=80a6da9acc51637f0c1992facc98358aff074f33f931545f52c9cf98a9ac3e99) · [Meta](https://www.facebook.com/ads/library/?id=1400512635551340)), „No cover. No Stress.“
- Holsper (angrenzend): „"Zip along three sides? Genius."“
- Rauschen: Hunde-Advertorial, Inkontinenz-Boxer, Schnarch-, Nervenschmerz- und Milben-Advertorials (getuvlizer `50009487` ([GH](https://app.gethookd.ai/share/ad/50009487?signature=c0884841e37a3c8d03f79c5b68c3b01f8bb2629853b72727e747cc8a6e62a378) · [Meta](https://www.facebook.com/ads/library/?id=829678626205721))).

**Q2 „duvet without cover“ (GB strikt und unscharf)**: keine relevanten Treffer (nur Hunde- und Nervenschmerz-Advertorials). In UK-Ads ist der Begriff ungebräuchlich; dort heißt es „coverless“ oder „duvet + cover in one“.

**Q3 „2 in 1 duvet“ (GB)**: keine relevanten Treffer. Ohne geo kommen über verwandte Queries Kallyon, Ryva, Nuvex und Cozily, die „2-in-1“ in Produktnamen bzw. LP-Slug nutzen.

**Q4 „coverless duvet“ (EN)**, die ergiebigste Query:
- Julian Charles / Silentnight: Video `172408841` ([GH](https://app.gethookd.ai/share/ad/172408841?signature=75f931a947dd7f66157e4090736b5d8704b8a8e22bca23a0c7749d05b5de3eb1) · [Meta](https://www.facebook.com/ads/library/?id=1078705575141820)) (Score 73) und Static `176904327` ([GH](https://app.gethookd.ai/share/ad/176904327?signature=6f767e326ec8754c2baa97e66f28045b2afa3debb2220cfc891e2a7b862dba1c) · [Meta](https://www.facebook.com/ads/library/?id=1052307607436353)). Auf der Verpackung steht „wash and dry within 90 minutes“, „5 year guarantee“, 40°, im Creative „CODE: EXTRA15 – EXTRA 15% OFF – ORDERS OVER £75“. Landingpage: PDP Single.
- Night Lark: „Shop Coverless Duvets“ / „Cosy by nature.“ / „BEDDING MADE EASY“ `184689162` ([GH](https://app.gethookd.ai/share/ad/184689162?signature=fba89c0271d00e90fa9ce79af82e338fe31e4862dbcbcdef5b499c5773773f5b) · [Meta](https://www.facebook.com/ads/library/?id=1303921581716801)); DPA-Canvas `184690331` ([GH](https://app.gethookd.ai/share/ad/184690331?signature=eb2553b7817270551e855502bbe4c6bf4da4f88a5b2d2ca6a7c796e4da5d2142) · [Meta](https://www.facebook.com/ads/library/?id=1389941746602169)) (Score 70).
- OHS: DPA „OHS Coverless Sherpa Fleece Reversible 10.5 Tog Duvet Set, Red/Navy - King“ `191549081` ([GH](https://app.gethookd.ai/share/ad/191549081?signature=bafac6993b715057fc219f74c9d5b68256360e94ca14f70b7ddda261b8bd5e84) · [Meta](https://www.facebook.com/ads/library/?id=1086761910770876)).
- Hygge Sheets: `193750511` ([GH](https://app.gethookd.ai/share/ad/193750511?signature=fdbd6aa6d317f357a6cc5e9393eaec06044587f73134151de1697f93e6e3f765) · [Meta](https://www.facebook.com/ads/library/?id=943157378406951)) (Relaunch des UGC-Videos am 02.10.).
- Pleene *(Kollegen)*: UGC „Check This Before You Buy“ `168246686` ([GH](https://app.gethookd.ai/share/ad/168246686?signature=a360c60671d85ebeec646d4238239e0ec57ba2d7b037d0bb4c8888b606378db0) · [Meta](https://www.facebook.com/ads/library/?id=2035183934551496)) (Score 86), `200490712` ([GH](https://app.gethookd.ai/share/ad/200490712?signature=5ca96434dc1391452bf61216cdc94bffb3d3b8ab283563c1354672fbd689d547) · [Meta](https://www.facebook.com/ads/library/?id=1570785790996577)).
- NakedLab, Nuvex, Duvet Hog; außerdem US-Anbieter (Brooklinen, Doze, Bedsure).

**Q5 „never change a duvet cover again“ (EN)**
- Pleene *(Kollegen)*: **UGC-Winner** „Everyone said it. They were right.“ `145443331` ([GH](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) · [Meta](https://www.facebook.com/ads/library/?id=1440933327878495)) (Score 100, 56 Tage). On-Screen-Texte: „I only ordered it because everyone said“, „I haven't changed my bed linen in three months“. Neu gestartet am 01.10. als `193234219` ([GH](https://app.gethookd.ai/share/ad/193234219?signature=0cb8964e6ba84cfd7298793d4bb26527250a2d845375dcbc5de0b9fc4c82562e) · [Meta](https://www.facebook.com/ads/library/?id=4170969413201905)).
- **Moonora**: Native-News-Static `189407350` ([GH](https://app.gethookd.ai/share/ad/189407350?signature=b7867253093bd22254c759d45384d6ff5fa70f1dbf06cf0558b60684cbe3d82b) · [Meta](https://www.facebook.com/ads/library/?id=1096009869545467)): „LATEST NEWS – A duvet brand has finally got rid of the duvet cover – “Honestly, what took them so long?” – In a rare move, the company has simplified the one job nobody ever enjoyed.“ Gezeigt wird eine Frau um die 60 mit Moonora-Rolle „DOUBLE“ im Lager. Dazu Videos `200081270` ([GH](https://app.gethookd.ai/share/ad/200081270?signature=64a539565aa701296fdacafa0554343800e5c0e563b03c2b4eeab3731eeb7bc6) · [Meta](https://www.facebook.com/ads/library/?id=3647292718772144)).
- **Kallyon**: Statics `190938412` ([GH](https://app.gethookd.ai/share/ad/190938412?signature=cf7d614578fc712fc48a3ba5e4d8bd63d668c9adb7099a15dd7180e3fba7a2bf) · [Meta](https://www.facebook.com/ads/library/?id=1750718696126137)) usw. (siehe Deep Dive).
- Night Lark: „Autumn/Winter Range“ `184690352` ([GH](https://app.gethookd.ai/share/ad/184690352?signature=fb87869787479a74a14c8cad03caefd7c4448ada81b2595ba3b776cdfb290bd2) · [Meta](https://www.facebook.com/ads/library/?id=1565281941486079)) („Hibernate in style.“).
- Sleep Club (AU): „Never change your bedding again 🛏️“, nicht UK.

**Q6 „quick dry duvet“ (EN)**
- Pleene *(Kollegen)*: „The Duvet You Can Actually Wash“ `193234224` ([GH](https://app.gethookd.ai/share/ad/193234224?signature=e67f0112dff4be83367fd2663a38a3c667a76a33044371dae7cb5e0307b1035b) · [Meta](https://www.facebook.com/ads/library/?id=1614086653522933)). In den USA neu „Ditch The Duvet Cover“ `200036996` ([GH](https://app.gethookd.ai/share/ad/200036996?signature=945bd160e24141ec27cd570f40308c72484012330c424f8889416548c509a965) · [Meta](https://www.facebook.com/ads/library/?id=38866239393024310)), in UK `200490719` ([GH](https://app.gethookd.ai/share/ad/200490719?signature=02b20c37beecbaad1d44b7e74cd81762006aa203ca85a92692a4fce5b3aa9e84) · [Meta](https://www.facebook.com/ads/library/?id=1099152986192830)).
- **Ryva**: `199399084` ([GH](https://app.gethookd.ai/share/ad/199399084?signature=5514cad4a4c3d93f48b848e524ab3042c9f9a61d96205bc67a20f738958a8deb) · [Meta](https://www.facebook.com/ads/library/?id=1771842654090109)) (Feature-Icon-Static „Air dries in around 2 hours“), UGC `193166959` ([GH](https://app.gethookd.ai/share/ad/193166959?signature=394b60762c06320cce565d652ef4630f42334cb11393151c9f53500ed3b326e9) · [Meta](https://www.facebook.com/ads/library/?id=941277938529032)).
- Kallyon `192912448` ([GH](https://app.gethookd.ai/share/ad/192912448?signature=9b8bb9b9d2aeaf31ccde30e763a6b5b8b14eeca0dc73d859b79ab3671ad3fd6d) · [Meta](https://www.facebook.com/ads/library/?id=1069345045471610)), `191407065` ([GH](https://app.gethookd.ai/share/ad/191407065?signature=3c5c5a14724851cdef8324e7923be6a697f0c54261a9001873033f0da8001e0f) · [Meta](https://www.facebook.com/ads/library/?id=1395147599214736)); Nuvex EN `198399654` ([GH](https://app.gethookd.ai/share/ad/198399654?signature=98064383d582764a8f725675448445aeaceb89c99c50a49f04c2d018dfd29b2d) · [Meta](https://www.facebook.com/ads/library/?id=3622794544545616)); Duvet Hog `189521382` ([GH](https://app.gethookd.ai/share/ad/189521382?signature=962ddc4f2482bad9cf5450a779def34dea42a977320344d117e0f822f3f7f50e) · [Meta](https://www.facebook.com/ads/library/?id=1655238635683167)).
- Absolute Home Textiles DPA „4.5 Tog Single Easy Care Duvet“ `121073563` ([GH](https://app.gethookd.ai/share/ad/121073563?signature=f822b8bd93a46382dccc04ac9f144e2cc5f56fd4e725c7798ddb3cdbcfdbe36f) · [Meta](https://www.facebook.com/ads/library/?id=1262930294712215)).
- Quick-Dry wird überall als **Bullet** genutzt, nirgends als Haupt-Hook.

**Q7 „all season duvet“ (GB: nur 2 irrelevante Musik-Ads; EN: vor allem Nicht-UK)**
- UK: freemans „Silentnight All Seasons 3 in 1 Duvet“ `127943305` ([GH](https://app.gethookd.ai/share/ad/127943305?signature=5e8171b0b0d96b71687692d4de213e110b75f5d7b25c3f10477763f1d9270ea8) · [Meta](https://www.facebook.com/ads/library/?id=1013401628101649)); Night Lark „Autumn/Winter Range“ `184690359` ([GH](https://app.gethookd.ai/share/ad/184690359?signature=ae4798368df240ce530a67afef8de8415632ad2cea7f939ef7de3fea72129f52) · [Meta](https://www.facebook.com/ads/library/?id=2060061884649016)); Duvet Hog.
- Nicht-UK: Lad Collective (USA), Bed Shop (Saudi-Arabien), Penguin (Ägypten), Eiderdown (NZ), Hush (CA), Lincove (USA).
- All-Season ist bei den Clones Standard-Bullet, als eigener Hook im UK-Coverless-Segment kommt es nicht vor.

**Q8 „menopause duvet“ (EN)**: **kein einziger UK-Duvet-Advertiser.** Im US-Markt ist der Angle stark besetzt: Dosaze „Menopause Has You Sleeping Hot? Try This.“ `201289923` ([GH](https://app.gethookd.ai/share/ad/201289923?signature=1496989efd19b81803386efd0720537e4e4bfaec52c2be779c4cb62be7fbfd2a) · [Meta](https://www.facebook.com/ads/library/?id=1108420401735235)) und „Temperature-Regulating Comfort for Menopause Nights“ `182307468` ([GH](https://app.gethookd.ai/share/ad/182307468?signature=9efa44afc2b3d8f332a481aa1865c3fa70a6b305e37f8f4f2f83e65424e5343b) · [Meta](https://www.facebook.com/ads/library/?id=1401386261483864)) (Dosaze hat auch uk.dosaze.com, die Ads laufen aber nur in den USA), Ice Blankets „Made For Menopause Nights“ `133796076` ([GH](https://app.gethookd.ai/share/ad/133796076?signature=ef625b6e15306caef9ffe4b1425b2cb6be8c7b4b55fad299400a9339aa5d92e5) · [Meta](https://www.facebook.com/ads/library/?id=1045657454625410)), Rest „94% Sleep Better With This "Cooling Comforter"“ `30297004` ([GH](https://app.gethookd.ai/share/ad/30297004?signature=9c76a6aae73a1520cfb85e881230dfdc0c0927e2bcdf2b22f13fdbccfd335bc1) · [Meta](https://www.facebook.com/ads/library/?id=2205074159937571)) (278 Tage) und Video `175766490` ([GH](https://app.gethookd.ai/share/ad/175766490?signature=53c2958ed27005a27439cfd8fcce153ed15d3c046df4e52dc85cc82432724af0) · [Meta](https://www.facebook.com/ads/library/?id=1780925026277621)) (Score 100), Bohobed „Give Your Menopause Nights a Break“ `196787605` ([GH](https://app.gethookd.ai/share/ad/196787605?signature=42fcf03cb635e863968fa22b7426198ef07749c50341f3c525ddb816cabe4f90) · [Meta](https://www.facebook.com/ads/library/?id=1545391287603526)), Linens & Hutch „Menopause Made Sleep Hard. We Can Help.“ `108758404` ([GH](https://app.gethookd.ai/share/ad/108758404?signature=b65b1d0eb1b4929ac6325bdebd613dbfd013e2187e135b32600ab4aa6a405b2e) · [Meta](https://www.facebook.com/ads/library/?id=853873067341138)). In UK nutzt nur ein Supplement-Advertorial den Angle: alaxi.co.uk „Why you keep waking up at 3am and what I did about it.“ `193046065` ([GH](https://app.gethookd.ai/share/ad/193046065?signature=a92c93134fd59cce149d1e4df899d8ecc365b75e8f1af43a714652d9e0033a9f) · [Meta](https://www.facebook.com/ads/library/?id=28677960895204821)).

**Q9 „night sweats duvet“ (Keyword-Fallback, 0 relevante Treffer) bzw. „night sweats bedding“ (EN)**
- UK: ZLEEPY `122483614` ([GH](https://app.gethookd.ai/share/ad/122483614?signature=1e9dcf1ccd0cc8abdb6e3f9576158b1a1bbf8ec102078d0d2c4227a6182acd1b) · [Meta](https://www.facebook.com/ads/library/?id=974913134938324)) / `122483597` ([GH](https://app.gethookd.ai/share/ad/122483597?signature=90a1e09315850e62688c398ef358626962bb4f330de0793d7c5b8044bac31934) · [Meta](https://www.facebook.com/ads/library/?id=971163668899126)); Kabode `122173844` ([GH](https://app.gethookd.ai/share/ad/122173844?signature=0991c8f189c93cc18ce9c0eb9932dbe6444e14815e582c7a43557775cab55ca3) · [Meta](https://www.facebook.com/ads/library/?id=2722844258072293)); Dore & Rose „❄️ Stay Cool All Night Long ❄️“ `130609130` ([GH](https://app.gethookd.ai/share/ad/130609130?signature=c267b243caee05de9d4c6670ac0715e258f3159b2e6ab9079046e24113141e6d) · [Meta](https://www.facebook.com/ads/library/?id=2634834240252021)) (GB/EU/US); Cosy House Collection, UGC mit Wärmebildkamera „DO YOU FEEL LIKE …“, Offer „50% OFF - Today Only!“ `200668070` ([GH](https://app.gethookd.ai/share/ad/200668070?signature=235626e3206a697b6c6b0c47db311e6b448c9c1af3f8534d13b80ca9eec3bb6e) · [Meta](https://www.facebook.com/ads/library/?id=1585882359958317)); Benji Sleep „Say Goodbye to Night Sweats!“ `131232015` ([GH](https://app.gethookd.ai/share/ad/131232015?signature=a95a97b842a03574bc711a296a4b426f20f85830f4df2af5bb6bee8ca7b58294) · [Meta](https://www.facebook.com/ads/library/?id=1690839722178749)) (Markt unklar).
- Im Coverless-Segment: nur Kallyon mit „No more night sweats“ im Feature-Static `195931651` ([GH](https://app.gethookd.ai/share/ad/195931651?signature=776c7b4deb8c1a11d49bd283c47f4c886e070822609ecda2bfc3e74c43283d2e) · [Meta](https://www.facebook.com/ads/library/?id=1871081214267591)); angrenzend NakedLab `182677849` ([GH](https://app.gethookd.ai/share/ad/182677849?signature=5e2d211cfbe47638eeb08b183455d6cbc778caf65b391debdc293d52c1ac4078) · [Meta](https://www.facebook.com/ads/library/?id=1772141880577256)).

**Q10 „dust mites duvet“ (EN)**: In UK besetzen **Geräte-Advertorials** das Milben-Thema, keine Decken: DetoxSpa UK „Eliminates Dust Mites In Your Home? (MUST READ)“, Static `77322638` ([GH](https://app.gethookd.ai/share/ad/77322638?signature=981cfbbe671dc3e1e372c758a78592c79a42aaee29293648e667de56fa530de7) · [Meta](https://www.facebook.com/ads/library/?id=848060581527812)) (245 Tage aktiv) und Video `80270006` ([GH](https://app.gethookd.ai/share/ad/80270006?signature=20213f2ee6b41377ee81640500cf7374b279c71704ec04b071a25a801fe48783) · [Meta](https://www.facebook.com/ads/library/?id=635387565726640)) (**436 Tage aktiv**), Families vs. Dust Mites „Read if you wake up congested in the morning 👆“ `46871558` ([GH](https://app.gethookd.ai/share/ad/46871558?signature=beca7fa48fe59c2ed0cd9b96afc2fcc7d6fe44fe4ab625b521d036151cddfe64) · [Meta](https://www.facebook.com/ads/library/?id=1167687025222234)) (211 Tage), „Read if you wake up coughing in the middle of the night 👆“ `50009487` ([GH](https://app.gethookd.ai/share/ad/50009487?signature=c0884841e37a3c8d03f79c5b68c3b01f8bb2629853b72727e747cc8a6e62a378) · [Meta](https://www.facebook.com/ads/library/?id=829678626205721)) (199 Tage). Landingpage: Advertorial (/pages/adv-dust-mites). **Kein UK-Coverless-Anbieter macht Milben zum Haupt-Hook**; Kallyon führt „anti-dust mite“ nur als Bullet (`193167969` ([GH](https://app.gethookd.ai/share/ad/193167969?signature=9fa2fd2f1c8b57d2d6a65a1d1ddeb841628ae03bc94ec732bf16a1198a957548) · [Meta](https://www.facebook.com/ads/library/?id=1824161848945314))).

**Q11 „duvet for seniors“ (Keyword-Fallback; Variante „duvet for elderly parents easy bed making“ lief in einen Timeout)**: **0 relevante Treffer.** Nur Brease (Gewichtsdecke, EU ohne GB) „Recommended by leading psychologists 🇩🇰“ `82508363` ([GH](https://app.gethookd.ai/share/ad/82508363?signature=4d1f81f4779dba8c4cc6be485f7510deac9ba0bd199c0fc65a9ec0fc7c0bb96d) · [Meta](https://www.facebook.com/ads/library/?id=1255282836544074)).

**Q12 „gift duvet“ (EN)**: **kein Coverless-Duvet mit Geschenk-Angle.** UK-Referenzen aus Nachbarkategorien:
- **Evely Rose** (Persona-Page „Alison Prescott“): Advertorial-Brief „Twelve Christmases. Eleven Presents Still In The Cupboard. And One She Actually Uses.“, `193148723` ([GH](https://app.gethookd.ai/share/ad/193148723?signature=4c9fa04e4327093fc4467466e6c8bdd3d25aed8e89cfc8db7f3c0a07f016b6e2) · [Meta](https://www.facebook.com/ads/library/?id=1397604122587046)) und `198162782` ([GH](https://app.gethookd.ai/share/ad/198162782?signature=e6c31fd6cdd812d0c7eafc462f94d98dc18b420465b7a41f164d62bce29642db) · [Meta](https://www.facebook.com/ads/library/?id=1123844373641873)) („Was £70. Now £34.95.“). Auf der LP: „My mother has been telling me not to buy her anything since 2014.“ / „she is seventy-seven“ / „What she needed wasn't another nice thing to put away. It was a better version of something she already used every single day.“ Produkt ist ein Wäschekorb. **Lässt sich direkt auf eine Coverless-Decke übertragen.**
- Happy Home Shop: Review-Static „Grandson loves it“ `197599038` ([GH](https://app.gethookd.ai/share/ad/197599038?signature=2844f5fd0368f0b6728ba7a7e1ff9d6b214a416d6ac0b308eb4be86c68d219c5) · [Meta](https://www.facebook.com/ads/library/?id=1108067788750197)); Rise & Fall „Free Extra Pillowcase Set worth £35“ `78044394` ([GH](https://app.gethookd.ai/share/ad/78044394?signature=366b56daa540615f53076e26023b20a35fd216da5894b6effca8837f0682bd85) · [Meta](https://www.facebook.com/ads/library/?id=1215520823522469)) (UK-Bettwäsche-Norm: Gratis-Kissenbezüge).

**Zusatz-Queries**
- „duvet and cover in one“ (EN): Kallyon „Our customers describe it in 3 words: Lightweight / Comfortable / Cosy – ★★★★★ Over 17,000 happy sleepers“ `198183616` ([GH](https://app.gethookd.ai/share/ad/198183616?signature=f279af6651703ed77ed62bfa4161f6e9280432d183f1ab1401b6736e46d9a69c) · [Meta](https://www.facebook.com/ads/library/?id=2246294822828264)), Moonora `200081846` ([GH](https://app.gethookd.ai/share/ad/200081846?signature=8411fb96a93b49aee91e8ae47ec8c3338f51a3315feaacebf2f621fc1784c61f) · [Meta](https://www.facebook.com/ads/library/?id=1626403019035121)), Pleene `200490719` ([GH](https://app.gethookd.ai/share/ad/200490719?signature=02b20c37beecbaad1d44b7e74cd81762006aa203ca85a92692a4fce5b3aa9e84) · [Meta](https://www.facebook.com/ads/library/?id=1099152986192830)), Cozily `197407814` ([GH](https://app.gethookd.ai/share/ad/197407814?signature=f3179577688a90a983abb621da90266c1856326faa6e8c02921ac048c47cdeff) · [Meta](https://www.facebook.com/ads/library/?id=1417419460578927)), Snuvie `186737710` ([GH](https://app.gethookd.ai/share/ad/186737710?signature=43adc124bba270fb6770ee18c01528ebc0ce6525f234b282b29a9c4e0b96c1df) · [Meta](https://www.facebook.com/ads/library/?id=2035987180395067)) (GBP-Shop, unklar).
- „Silentnight coverless duvet“ (strikt): nur Julian Charles; Silentnight selbst schaltet keine Coverless-Ads.
- „hate changing duvet cover“: Keyword-Fallback, nichts Neues.

---

### 5. Deep Dives zu den neuen UK-Clones

#### Kallyon: der direkte Magic-Splashy-Klon (52 Ads: 40 Image, 12 Video)
Landingpage (GBP): „EasySleep – The quick-drying 2-in-1 duvet that makes duvet covers unnecessary“, „Rated 4.8 by 1500+ Customers!“, „Cool in summer, warm in winter / Never change bed linens again / Hygienic & allergy-friendly / Fits in any washing machine“, „Never Make the Bed Again – No more bedding. No more fiddling. No more hassle.“, „ThermoBalance® fibers automatically adapt to your body.“, „No sweating, no freezing“, „Air-dries in 2 hours“, „Try the EasySleep for 40 nights“. Die Testimonials (James M., Richard S., „Martthew. P“, Emily M.) haben **keine Altersangaben**. Kallyon ist ein Dropship-Generalist und schaltet parallel eine Pfannen-Ad „Five types of pans I would never buy at Tesco“ `199355573` ([GH](https://app.gethookd.ai/share/ad/199355573?signature=3a1ae052ff541ad755fad221beea64d972a2282fd708fb9ec8424140affd872a) · [Meta](https://www.facebook.com/ads/library/?id=1081448574646197)).

Ads (Copy wörtlich):
- Review-Summary-Static „Our customers describe it in 3 words“ `198183616` ([GH](https://app.gethookd.ai/share/ad/198183616?signature=f279af6651703ed77ed62bfa4161f6e9280432d183f1ab1401b6736e46d9a69c) · [Meta](https://www.facebook.com/ads/library/?id=2246294822828264)) (11 Varianten, 03.10.)
- **Breaking-News-Static** „BREAKING NEWS – THE MOST IN-DEMAND DUVET HAS JUST LAUNCHED — FROM £79!“ plus Lager-Knappheits-Copy über 2.973 Zeichen („Orders keep coming into our warehouse, and our team are packing parcels one after another.“, „A limited number of EasySleep duvets have been set aside for orders placed directly through our website.“) `196136368` ([GH](https://app.gethookd.ai/share/ad/196136368?signature=bbe4e08b1bb6ac9f1979d44cdc708d250c998eab9efc73cbd24e07adb9760759) · [Meta](https://www.facebook.com/ads/library/?id=1081174088031833)) (01.10.)
- **Feature-Icon-Static** „All the comfort, none of the hassle.“ mit „Complete duvet set“ / „Machine washable“ / „No more night sweats – Breathable fabric that wicks away moisture for a cool, dry sleep.“ / „Over 17,000 happy customers“ `195931651` ([GH](https://app.gethookd.ai/share/ad/195931651?signature=776c7b4deb8c1a11d49bd283c47f4c886e070822609ecda2bfc3e74c43283d2e) · [Meta](https://www.facebook.com/ads/library/?id=1871081214267591)) (Copy mit 100-night trial)
- **Story-Native als Static** (4.060 Zeichen): „I was waiting to pay for my petrol, staring at nothing in particular the way you do in a queue, when I noticed a piece of paper taped to the pillar beside the till.“, dann „ZERO STARS … DO NOT RECOMMEND … THE DUVET COVER.“ `193810435` ([GH](https://app.gethookd.ai/share/ad/193810435?signature=c7ccc1c6a4f13f1b529113d015f90b12386fff0a769970074d4765b1a263ac7e) · [Meta](https://www.facebook.com/ads/library/?id=28817926904470633)) (28.09.)
- Videos „Duvet and cover in one 🌙“ (30-night trial) `195931636` ([GH](https://app.gethookd.ai/share/ad/195931636?signature=fc6298e518002bece9d47c9d99aeab8d84efe453bf2c42b059a19f1628f00ea7) · [Meta](https://www.facebook.com/ads/library/?id=1647967833565656)) (44 Tage, 7 Varianten), „No more stuffing, pulling and turning bed linen 🌙“ `193379622` ([GH](https://app.gethookd.ai/share/ad/193379622?signature=e8471bbcb8332f71cfecf1515a0df0e2ea04b219861f91aea241de6aa0ad612e) · [Meta](https://www.facebook.com/ads/library/?id=1046845118142921)) (48 Tage), „2-in-1 Duvet 🌙 Kallyon® makes your bed fresh in 5 minutes.“ mit „✓ Hypoallergenic and dust mite-resistant“ `193167969` ([GH](https://app.gethookd.ai/share/ad/193167969?signature=9fa2fd2f1c8b57d2d6a65a1d1ddeb841628ae03bc94ec732bf16a1198a957548) · [Meta](https://www.facebook.com/ads/library/?id=1824161848945314))
- Kallyon **testet die Trial-Länge** (30 / 40 / 100 Nächte) und nennt in der Static-Headline den Preis („from £79“).

Preise (Sale / durchgestrichen): Single 140×200 £59.99 / £109.99 · Single XL 160×230 £69.99 / £119.99 · Double 200×200 £79.99 / £129.99 · King 230×230 £89.99 / £139.99 · King Large 220×240 £99.99 / £149.99 · Super King 260×230 £109.99 / £159.99. Gratisversand ab £50. Größen in DE-cm-Logik mit UK-Labels, z. B. „Single 140×200“; Standard in UK ist 135×200.

#### Moonora (20 Ads, alle seit 28.09.)
- Native-News-Static `189407350` ([GH](https://app.gethookd.ai/share/ad/189407350?signature=b7867253093bd22254c759d45384d6ff5fa70f1dbf06cf0558b60684cbe3d82b) · [Meta](https://www.facebook.com/ads/library/?id=1096009869545467)), Copy: „After decades of corners that never line up and duvet covers that turn themselves inside out, one company has done something nobody really saw coming. It fixed the problem.“ und „It's not a revolution. It just finally makes sense.“
- **Founder-Voice-Copy auf einem Animationsvideo** (Claymation/AI-Stil, Mum mit Wäsche und Kindern, 16 Varianten) `200081846` ([GH](https://app.gethookd.ai/share/ad/200081846?signature=8411fb96a93b49aee91e8ae47ec8c3338f51a3315feaacebf2f621fc1784c61f) · [Meta](https://www.facebook.com/ads/library/?id=1626403019035121)): „Everyone makes their bed. Hardly anyone enjoys it.“, „I stopped wrestling with duvet covers the week our first Moonora sample turned up.“, „No more poppers that won't line up.“, „No more twenty minutes on a Sunday night hunting for the fourth corner.“, „My guess? You won't want to.“
- UGC im Wohnwagen/Wohnmobil `195378766` ([GH](https://app.gethookd.ai/share/ad/195378766?signature=849f2f567a8074d0e5b553a82d0dafff49d1d50a1f6c1610b712d8226f6c36ec) · [Meta](https://www.facebook.com/ads/library/?id=1542836134204862)) mit der Pleene-Copy („Duvet + Cover in One 🌙 … Get 2 Moonora pillowcases FREE today (£49.99 value). 40 nights to try it risk-free.“)
- Landingpage: „Your bed is made in 3 seconds“, ganze Decke bei 60 °C waschbar, „Hypoallergenic, antibacterial fabric“, **Vergleichstabelle „Moonora vs duvet + cover“**, „No tumble dryer needed“, 1.692 Reviews, £69.99 (statt £139.99), „Couple Bundle“ £109.99, „Family Bundle“ £149.99 (MOST POPULAR), Gratisversand in UK, 40 Nächte. Größen: Single 135×200, Double 200×200, King 230×230, Super King 264×229. Hinweis: Single bis King passen in eine Standardmaschine mit 7–8 kg, Super King braucht eine größere Trommel.

#### Ryva (4 Ads, seit 16.09.)
- Feature-Icon-Static „THE DUVET + COVER IN ONE – No cover to wrestle – Wash the whole duvet – Air dries in around 2 hours“ `199399084` ([GH](https://app.gethookd.ai/share/ad/199399084?signature=5514cad4a4c3d93f48b848e524ab3042c9f9a61d96205bc67a20f738958a8deb) · [Meta](https://www.facebook.com/ads/library/?id=1771842654090109)); UGC (Mann mit Decke, „It's basically a duvet“) `193166959` ([GH](https://app.gethookd.ai/share/ad/193166959?signature=394b60762c06320cce565d652ef4630f42334cb11393151c9f53500ed3b326e9) · [Meta](https://www.facebook.com/ads/library/?id=941277938529032)) (Score 44).
- Landingpage: £64.99 (statt £99.99), „Try it risk-free for 100 nights“, „Get Ready for Colder Nights - Up to 40% off, while October stock lasts“, „The duvet 20,000+ customers have chosen“, Before/After-Sektion („Before: Wrestling with the cover, flipping it inside out, chasing corners.“), 2 Bezüge (worth £49.99).

#### Nuvex (31 Ads, seit 29.09.): EU-Clone mit UK-Option
Überwiegend italienische und spanische Copy. Die englische Variante läuft mit einem AI-Lagerhallen-Video „END OF SEASON SALE !! / END-OF-SEASON CLEARANCE. LAST CHANCE AT THIS PRICE.“ `198399654` ([GH](https://app.gethookd.ai/share/ad/198399654?signature=98064383d582764a8f725675448445aeaceb89c99c50a49f04c2d018dfd29b2d) · [Meta](https://www.facebook.com/ads/library/?id=3622794544545616)). Interessante IT-Hooks zur Übersetzung: „Scusa, ma il tuo piumino è probabilmente la cosa più sporca della tua camera. 😬“ `198499376` ([GH](https://app.gethookd.ai/share/ad/198499376?signature=cabd3e9e90a0ddbefb93c722a3f6167e5b8395a0013b6726115f6dac24956a1e) · [Meta](https://www.facebook.com/ads/library/?id=1964300187570798)), „Abbiamo prodotto troppi piumini. 😭“ `196541774` ([GH](https://app.gethookd.ai/share/ad/196541774?signature=135d44bb0329e284348c097ef395886165eca4573d1d1660c0352e646d387f7a) · [Meta](https://www.facebook.com/ads/library/?id=1041924198838710)), Sprecher-Video „Il piumino di cui tutti parlano in questo periodo.“ `198020988` ([GH](https://app.gethookd.ai/share/ad/198020988?signature=4a74d6aeb2762f3a274b3cd0bb7cdcca81f751b80101025adc1a7fa0a320628a) · [Meta](https://www.facebook.com/ads/library/?id=3007739436285189)). Shop: Standard USD mit US-Größen (Twin/Full/Queen), $89.99 (statt $139.99), „4.8/5 from over 3,780 customers“.

#### Night Lark (Fine Bedding Co., 56 Ads): der etablierte UK-Player
Marken-Statics und leichtes Video, Fokus auf Kinder, Eco und Chester Zoo („10% of every purchase supports Chester Zoo's conservation work“ `184690366` ([GH](https://app.gethookd.ai/share/ad/184690366?signature=65f5158a939c32c48c61dbf6b322285484e71dc135f9b24edc49d0ef5fc6fb7f) · [Meta](https://www.facebook.com/ads/library/?id=1430462362550811))), „Sleeping under the stars. Made easy.“ `184690378` ([GH](https://app.gethookd.ai/share/ad/184690378?signature=810256594e268a250fda2c2d91e4e9ed14b1f1fc6075ca46065b36b990acc9a7) · [Meta](https://www.facebook.com/ads/library/?id=1107888698436252)), „Save 10% on your first order – Fuss-free Coverless Duvets that are easily washable and quick drying“ `184690349` ([GH](https://app.gethookd.ai/share/ad/184690349?signature=58e47f6f9e43eb0f8a607c1a926b5f552212b8d66e623e631b4008e798c92680) · [Meta](https://www.facebook.com/ads/library/?id=2104788427099426)) (Score 74), „Back in Stock!“ `184690339` ([GH](https://app.gethookd.ai/share/ad/184690339?signature=5f0787daf6b1c384f9325f8a495569574f19d0802fada7d0bfb3fe233206fcf8) · [Meta](https://www.facebook.com/ads/library/?id=4616690428602177)), „Supersoft, eco-friendly & coverless.“ `184690347` ([GH](https://app.gethookd.ai/share/ad/184690347?signature=e87567eee3ae02e250a9ea94e7b316144317f59edf3761c26d74dd56b9f3aff4) · [Meta](https://www.facebook.com/ads/library/?id=2501689300314654)), „Sleep soundly. Support wildlife. – Create calm with zero duvet faff.“ `184689223` ([GH](https://app.gethookd.ai/share/ad/184689223?signature=6b934e7bae5091b6add71957ade4eeaad0a3a0a2ff96f2800b5abd6136d42f64) · [Meta](https://www.facebook.com/ads/library/?id=2608844486219318)), „Extra layer. Extra cosy.“ `184690326` ([GH](https://app.gethookd.ai/share/ad/184690326?signature=2a07de4bac6d4c0776e67e9b61af1ffe61f50e19e3d9eceda07f124f0bfdcaec) · [Meta](https://www.facebook.com/ads/library/?id=1504854861376898)). Preise: Single £70 / Double £90 / King £100 (10.5 Tog). Single mit 1 Kissenbezug, sonst 2; King braucht eine 10-kg-Maschine; Gratisversand ab £85.

#### Hygge Sheets (Kinder)
„Coverless Duvets for Little Kids!“ `113915599` ([GH](https://app.gethookd.ai/share/ad/113915599?signature=b60744d7340d2f5bff38d07fbd4830614f1810770d0c67098414f4ddc2fc028e) · [Meta](https://www.facebook.com/ads/library/?id=1836974440611547)) und UGC `133953992` ([GH](https://app.gethookd.ai/share/ad/133953992?signature=ddd88ceeb1444a518b91779f93312a73ec2a71be4d4acfef1f6f16d69acc793f) · [Meta](https://www.facebook.com/ads/library/?id=1750897266250923)) (beide Score 86), „One less worry for busy parents 🌙💤“ `143411729` ([GH](https://app.gethookd.ai/share/ad/143411729?signature=16afed8d550969a2fc9102ae999b161bec4b73f9aeef2601fbe86ceb7cb7df79) · [Meta](https://www.facebook.com/ads/library/?id=2141230886820481)). Bewusst **nicht** wasserdicht („we found they were often heavy, hot and uncomfortable“), 4.5 Tog, nur Single, £24.99.

---

### 6. Angle-Sättigungskarte UK (Coverless / 2-in-1)

Gezählt sind direkte UK-Wettbewerber einschließlich Pleene/Cozily (max. 10). „Bullet“ heißt: Der Angle steht nur in der Feature-Liste. „Hook“ heißt: Er trägt Headline oder Eröffnung.

| Angle | # UK-Advertiser | Beispiele | Status |
|---|---|---|---|
| **Convenience / kein Bezug** („No more wrestling“) | 10 (Pleene, Cozily, Kallyon, Moonora, Ryva, Nuvex-EN, Night Lark, Hygge, OHS, Silentnight/Julian Charles) | `145443331` ([GH](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) · [Meta](https://www.facebook.com/ads/library/?id=1440933327878495)), `189407350` ([GH](https://app.gethookd.ai/share/ad/189407350?signature=b7867253093bd22254c759d45384d6ff5fa70f1dbf06cf0558b60684cbe3d82b) · [Meta](https://www.facebook.com/ads/library/?id=1096009869545467)), `199399084` ([GH](https://app.gethookd.ai/share/ad/199399084?signature=5514cad4a4c3d93f48b848e524ab3042c9f9a61d96205bc67a20f738958a8deb) · [Meta](https://www.facebook.com/ads/library/?id=1771842654090109)), `184689041` ([GH](https://app.gethookd.ai/share/ad/184689041?signature=80a6da9acc51637f0c1992facc98358aff074f33f931545f52c9cf98a9ac3e99) · [Meta](https://www.facebook.com/ads/library/?id=1400512635551340)) | **gesättigt** |
| **Quick Dry** („dry in 2 hours“) | 8 als Bullet (Pleene, Kallyon, Ryva, Nuvex, Night Lark, Hygge, Silentnight „90 minutes“, Moonora LP); 0 als Haupt-Hook | `199399084` ([GH](https://app.gethookd.ai/share/ad/199399084?signature=5514cad4a4c3d93f48b848e524ab3042c9f9a61d96205bc67a20f738958a8deb) · [Meta](https://www.facebook.com/ads/library/?id=1771842654090109)), `185228766` ([GH](https://app.gethookd.ai/share/ad/185228766?signature=f4be2b097e5b58bb0f5013dc8e461a8cea74051b0e8dfd5a28059f540eaf99fb) · [Meta](https://www.facebook.com/ads/library/?id=1401480008764681)), `176904327` ([GH](https://app.gethookd.ai/share/ad/176904327?signature=6f767e326ec8754c2baa97e66f28045b2afa3debb2220cfc891e2a7b862dba1c) · [Meta](https://www.facebook.com/ads/library/?id=1052307607436353)) | **gesättigt als Bullet**, als Hook frei |
| **All-Season-Temperatur** („cool in summer, warm in winter“) | 5 Clones als Bullet (Pleene, Kallyon, Moonora, Ryva, Nuvex) + Silentnight 3-in-1 (freemans); Markenfaser nur Kallyon (ThermoBalance) und Nuvex (ClimaFlow); **kein Clone nennt Tog** | `195931636` ([GH](https://app.gethookd.ai/share/ad/195931636?signature=fc6298e518002bece9d47c9d99aeab8d84efe453bf2c42b059a19f1628f00ea7) · [Meta](https://www.facebook.com/ads/library/?id=1647967833565656)), `127943305` ([GH](https://app.gethookd.ai/share/ad/127943305?signature=5e8171b0b0d96b71687692d4de213e110b75f5d7b25c3f10477763f1d9270ea8) · [Meta](https://www.facebook.com/ads/library/?id=1013401628101649)) | **gesättigt als Bullet**; Tog-Klarheit fehlt |
| **Nachtschweiß** | 1 im Segment (Kallyon-Static) + 2 angrenzend (NakedLab, ZLEEPY) | `195931651` ([GH](https://app.gethookd.ai/share/ad/195931651?signature=776c7b4deb8c1a11d49bd283c47f4c886e070822609ecda2bfc3e74c43283d2e) · [Meta](https://www.facebook.com/ads/library/?id=1871081214267591)), `182677849` ([GH](https://app.gethookd.ai/share/ad/182677849?signature=5e2d211cfbe47638eeb08b183455d6cbc778caf65b391debdc293d52c1ac4078) · [Meta](https://www.facebook.com/ads/library/?id=1772141880577256)), `122483614` ([GH](https://app.gethookd.ai/share/ad/122483614?signature=1e9dcf1ccd0cc8abdb6e3f9576158b1a1bbf8ec102078d0d2c4227a6182acd1b) · [Meta](https://www.facebook.com/ads/library/?id=974913134938324)) | **vorhanden, schwach** |
| **Menopause / Hitzewallungen** | **0** in UK (USA: ≥ 6 Advertiser) | US-Belege `182307468` ([GH](https://app.gethookd.ai/share/ad/182307468?signature=9efa44afc2b3d8f332a481aa1865c3fa70a6b305e37f8f4f2f83e65424e5343b) · [Meta](https://www.facebook.com/ads/library/?id=1401386261483864)), `133796076` ([GH](https://app.gethookd.ai/share/ad/133796076?signature=ef625b6e15306caef9ffe4b1425b2cb6be8c7b4b55fad299400a9339aa5d92e5) · [Meta](https://www.facebook.com/ads/library/?id=1045657454625410)), `30297004` ([GH](https://app.gethookd.ai/share/ad/30297004?signature=9c76a6aae73a1520cfb85e881230dfdc0c0927e2bcdf2b22f13fdbccfd335bc1) · [Meta](https://www.facebook.com/ads/library/?id=2205074159937571)) | **fehlt (Whitespace)** |
| **Hygiene / Milben / Allergie** | 4 als Bullet („Hypoallergenic and antibacterial“: Pleene, Kallyon, Moonora, Ryva; Kallyon zusätzlich „anti-dust mite“); 0 als Hook bei Decken. Geräte-Advertorials in UK als Hook seit über 1 Jahr | `193167969` ([GH](https://app.gethookd.ai/share/ad/193167969?signature=9fa2fd2f1c8b57d2d6a65a1d1ddeb841628ae03bc94ec732bf16a1198a957548) · [Meta](https://www.facebook.com/ads/library/?id=1824161848945314)), `80270006` ([GH](https://app.gethookd.ai/share/ad/80270006?signature=20213f2ee6b41377ee81640500cf7374b279c71704ec04b071a25a801fe48783) · [Meta](https://www.facebook.com/ads/library/?id=635387565726640)), `77322638` ([GH](https://app.gethookd.ai/share/ad/77322638?signature=981cfbbe671dc3e1e372c758a78592c79a42aaee29293648e667de56fa530de7) · [Meta](https://www.facebook.com/ads/library/?id=848060581527812)) | **Bullet gesättigt, Hook frei** (Nachfrage belegt) |
| **Senioren / Arthritis / leichtes Bettenmachen** | **0** (nur indirekt: Moonora-Static mit Frau um die 60) | `189407350` ([GH](https://app.gethookd.ai/share/ad/189407350?signature=b7867253093bd22254c759d45384d6ff5fa70f1dbf06cf0558b60684cbe3d82b) · [Meta](https://www.facebook.com/ads/library/?id=1096009869545467)) | **fehlt (Whitespace)** |
| **Geschenk** (Mum / Eltern / Weihnachten) | **0** im Segment; UK-Advertorial-Vorlage aus Nachbarkategorie | `193148723` ([GH](https://app.gethookd.ai/share/ad/193148723?signature=4c9fa04e4327093fc4467466e6c8bdd3d25aed8e89cfc8db7f3c0a07f016b6e2) · [Meta](https://www.facebook.com/ads/library/?id=1397604122587046)), `198162782` ([GH](https://app.gethookd.ai/share/ad/198162782?signature=e6c31fd6cdd812d0c7eafc462f94d98dc18b420465b7a41f164d62bce29642db) · [Meta](https://www.facebook.com/ads/library/?id=1123844373641873)) | **fehlt (Whitespace, Q4-Timing)** |
| **Schlafqualität** | 1–2 schwach (Kallyon-Testimonial „sweating much less“; Pleene „a bed that always feels fresh“) | `193234215` ([GH](https://app.gethookd.ai/share/ad/193234215?signature=92968440b95005fe0fc1bf85409c9b3366e3ae8f6dbf240ce5448a242e85affb) · [Meta](https://www.facebook.com/ads/library/?id=1068343922634373)) | **vorhanden, schwach** |
| **Eco** | 1 (Night Lark: „eco-friendly“, Chester Zoo) | `184690347` ([GH](https://app.gethookd.ai/share/ad/184690347?signature=e87567eee3ae02e250a9ea94e7b316144317f59edf3761c26d74dd56b9f3aff4) · [Meta](https://www.facebook.com/ads/library/?id=2501689300314654)) | **vorhanden, nischig** |
| **Preis / Rabatt / Knappheit** | 7 (Kallyon „from £79“ + Lagerknappheit, Ryva „Up to 40% off“, Nuvex „Clearance“, Moonora −50 % + Bundles, Julian Charles EXTRA15/70 %, Night Lark 10 %, Pleene Gratis-Bezüge) | `196136368` ([GH](https://app.gethookd.ai/share/ad/196136368?signature=bbe4e08b1bb6ac9f1979d44cdc708d250c998eab9efc73cbd24e07adb9760759) · [Meta](https://www.facebook.com/ads/library/?id=1081174088031833)), `198399654` ([GH](https://app.gethookd.ai/share/ad/198399654?signature=98064383d582764a8f725675448445aeaceb89c99c50a49f04c2d018dfd29b2d) · [Meta](https://www.facebook.com/ads/library/?id=3622794544545616)), `176904327` ([GH](https://app.gethookd.ai/share/ad/176904327?signature=6f767e326ec8754c2baa97e66f28045b2afa3debb2220cfc891e2a7b862dba1c) · [Meta](https://www.facebook.com/ads/library/?id=1052307607436353)) | **gesättigt** |
| *Extra: Kinder / Bettnässen* | 2 (Hygge, Night Lark Junior) | `113915599` ([GH](https://app.gethookd.ai/share/ad/113915599?signature=b60744d7340d2f5bff38d07fbd4830614f1810770d0c67098414f4ddc2fc028e) · [Meta](https://www.facebook.com/ads/library/?id=1836974440611547)), `184690378` ([GH](https://app.gethookd.ai/share/ad/184690378?signature=810256594e268a250fda2c2d91e4e9ed14b1f1fc6075ca46065b36b990acc9a7) · [Meta](https://www.facebook.com/ads/library/?id=1107888698436252)) | vorhanden (Nische) |
| *Extra: Social-Proof-Zahl* („17,000+“) | Kallyon (17.000 = MS-Zahl), Ryva (20.000+), Moonora (1.692 Reviews), Nuvex (3.780) | `198183616` ([GH](https://app.gethookd.ai/share/ad/198183616?signature=f279af6651703ed77ed62bfa4161f6e9280432d183f1ab1401b6736e46d9a69c) · [Meta](https://www.facebook.com/ads/library/?id=2246294822828264)) | gesättigt |

---

### 7. Format-Sättigungskarte UK

| Format | # UK-Advertiser (Segment) | Beispiele | Status |
|---|---|---|---|
| **UGC-Video** (Selfie/Talking Head, „I haven't changed my bed linen…“) | 5 (Pleene, Moonora, Ryva, Hygge, Kallyon-Videos) | `145443331` ([GH](https://app.gethookd.ai/share/ad/145443331?signature=0677e4ee983bd45fefa46f28b2a864fbfe4ab7b9403ae3289a1c98a1dd575660) · [Meta](https://www.facebook.com/ads/library/?id=1440933327878495)) (Score 100), `195378766` ([GH](https://app.gethookd.ai/share/ad/195378766?signature=849f2f567a8074d0e5b553a82d0dafff49d1d50a1f6c1610b712d8226f6c36ec) · [Meta](https://www.facebook.com/ads/library/?id=1542836134204862)), `193166959` ([GH](https://app.gethookd.ai/share/ad/193166959?signature=394b60762c06320cce565d652ef4630f42334cb11393151c9f53500ed3b326e9) · [Meta](https://www.facebook.com/ads/library/?id=941277938529032)), `133953992` ([GH](https://app.gethookd.ai/share/ad/133953992?signature=ddd88ceeb1444a518b91779f93312a73ec2a71be4d4acfef1f6f16d69acc793f) · [Meta](https://www.facebook.com/ads/library/?id=1750897266250923)) | **gesättigt** |
| **Founder** (on camera) | 0 in UK. Moonora nur als Founder-Copy auf Animation, Nuvex-Sprecher nur in IT | `200081846` ([GH](https://app.gethookd.ai/share/ad/200081846?signature=8411fb96a93b49aee91e8ae47ec8c3338f51a3315feaacebf2f621fc1784c61f) · [Meta](https://www.facebook.com/ads/library/?id=1626403019035121)), `198020988` ([GH](https://app.gethookd.ai/share/ad/198020988?signature=4a74d6aeb2762f3a274b3cd0bb7cdcca81f751b80101025adc1a7fa0a320628a) · [Meta](https://www.facebook.com/ads/library/?id=3007739436285189)) | **fehlt** |
| **Experte / Arzt** (Dermatologe, Allergologe, Schlafmediziner) | 0 | – | **fehlt** |
| **Advertorial / Native** | 2 als **Native-Static auf PDP** (Moonora „LATEST NEWS“, Kallyon „BREAKING NEWS“ + Petrol-Station-Story). **0 Advertorial-Landingpages** im Segment (UK-Nachbarkategorien: getuvlizer, Evely Rose) | `189407350` ([GH](https://app.gethookd.ai/share/ad/189407350?signature=b7867253093bd22254c759d45384d6ff5fa70f1dbf06cf0558b60684cbe3d82b) · [Meta](https://www.facebook.com/ads/library/?id=1096009869545467)), `196136368` ([GH](https://app.gethookd.ai/share/ad/196136368?signature=bbe4e08b1bb6ac9f1979d44cdc708d250c998eab9efc73cbd24e07adb9760759) · [Meta](https://www.facebook.com/ads/library/?id=1081174088031833)), `193810435` ([GH](https://app.gethookd.ai/share/ad/193810435?signature=c7ccc1c6a4f13f1b529113d015f90b12386fff0a769970074d4765b1a263ac7e) · [Meta](https://www.facebook.com/ads/library/?id=28817926904470633)) | **vorhanden** (Ad-Ebene), **LP-Ebene fehlt** |
| **Listicle** (Ad oder LP) | 0 | – | **fehlt** |
| **Quiz** | 0 | – | **fehlt** |
| **Static Before/After** | 0 in Ads (nur LP-Sektion bei Ryva) | – | **fehlt** |
| **Vergleichstabelle** (Us vs. Them) | 0 in Ads (nur Moonora-LP „Moonora vs duvet + cover“) | – | **fehlt** |
| **Testimonial-Static** | 1 im Segment (Kallyon „describe it in 3 words“); angrenzend Holsper, Happy Home Shop | `198183616` ([GH](https://app.gethookd.ai/share/ad/198183616?signature=f279af6651703ed77ed62bfa4161f6e9280432d183f1ab1401b6736e46d9a69c) · [Meta](https://www.facebook.com/ads/library/?id=2246294822828264)), `168691365` ([GH](https://app.gethookd.ai/share/ad/168691365?signature=38699f0616e36193f709a68cd05e365fef2e9fa8010b93624e5e8f23af049ba2) · [Meta](https://www.facebook.com/ads/library/?id=2597199830742409)), `197599038` ([GH](https://app.gethookd.ai/share/ad/197599038?signature=2844f5fd0368f0b6728ba7a7e1ff9d6b214a416d6ac0b308eb4be86c68d219c5) · [Meta](https://www.facebook.com/ads/library/?id=1108067788750197)) | **vorhanden, gering**; Testimonials **mit Alter**: 0 |
| *Extra: Feature-Icon-Static* | 3 (Kallyon, Ryva, Pleene-Statics) | `195931651` ([GH](https://app.gethookd.ai/share/ad/195931651?signature=776c7b4deb8c1a11d49bd283c47f4c886e070822609ecda2bfc3e74c43283d2e) · [Meta](https://www.facebook.com/ads/library/?id=1871081214267591)), `199399084` ([GH](https://app.gethookd.ai/share/ad/199399084?signature=5514cad4a4c3d93f48b848e524ab3042c9f9a61d96205bc67a20f738958a8deb) · [Meta](https://www.facebook.com/ads/library/?id=1771842654090109)) | gesättigt |
| *Extra: Produkt-/Lifestyle-Static, DPA* | 5 (Night Lark, OHS, Hygge, Julian Charles, Absolute) | `184689162` ([GH](https://app.gethookd.ai/share/ad/184689162?signature=fba89c0271d00e90fa9ce79af82e338fe31e4862dbcbcdef5b499c5773773f5b) · [Meta](https://www.facebook.com/ads/library/?id=1303921581716801)), `191549081` ([GH](https://app.gethookd.ai/share/ad/191549081?signature=bafac6993b715057fc219f74c9d5b68256360e94ca14f70b7ddda261b8bd5e84) · [Meta](https://www.facebook.com/ads/library/?id=1086761910770876)) | gesättigt |
| *Extra: AI-/Animationsvideo* | 2 (Moonora Claymation, Nuvex Lagerhalle) | `200081846` ([GH](https://app.gethookd.ai/share/ad/200081846?signature=8411fb96a93b49aee91e8ae47ec8c3338f51a3315feaacebf2f621fc1784c61f) · [Meta](https://www.facebook.com/ads/library/?id=1626403019035121)), `198399654` ([GH](https://app.gethookd.ai/share/ad/198399654?signature=98064383d582764a8f725675448445aeaceb89c99c50a49f04c2d018dfd29b2d) · [Meta](https://www.facebook.com/ads/library/?id=3622794544545616)) | neu im Kommen |

**Landingpage-Typen im Segment:** fast nur PDP (Kallyon, Moonora, Ryva, Nuvex, Pleene-PDP), Collection-Pages (Night Lark, Hygge, OHS, Holsper), eine Pleene-Custom-LP (pleene.com/pages/tb-6) und ein Facebook-Canvas (Night Lark DPA). **Advertorial-, Listicle- und Quiz-LPs: 0.**

---

### 8. UK-Größen, Tog, Preise und Offers

**Größenbezeichnungen:** Single / Double / King / Super King, teilweise mit „Long Single“ (Duvet Hog 135×220), „Single XL“ / „King Large“ (Kallyon, nicht UK-typisch). UK-Standardmaße: Single 135×200, Double 200×200, King 225×220 (Duvet Hog „Designed to fit standard U.K. duvet covers“) bzw. 230×220, Super King 260×220. Die Clones weichen ab (Kallyon Single 140×200 nach DE-Logik, Moonora King 230×230 und Super King 264×229). **Empfehlung:** echte UK-Maße und Labels übernehmen und nicht 1:1 die DE-Größen.

**Tog-Ratings:** etablierte Anbieter Silentnight 2.5 (Summer Breeze), Hygge 4.5, Absolute 4.5, OHS 4.5 / 7.5 / 10.5 / 13.5, Night Lark 10.5, Duvet Hog 4.5 / 10.5 / 13.5, freemans/Silentnight „All Seasons 3 in 1“. **Clones: kein Tog-Wert** (Pleene, Kallyon, Moonora, Ryva, Nuvex).

**Waschmaschinen-Hinweis** (UK-spezifisch): Moonora „Single, Double and King fit a standard 7 to 8 kg washing machine. The Super King needs a larger drum.“, Night Lark „The king-size duvet requires a 10kg washing machine.“

**Preispunkte:**
| Anbieter | Preis | Durchgestrichen / Offer |
|---|---|---|
| Kallyon | £59.99 (S) – £79.99 (D) – £109.99 (SK) | £109.99–£159.99; „from £79“ |
| Moonora | £69.99; 2 Stück £109.99; 3 Stück £149.99 | £139.99 / £219.99 / £299.99 |
| Ryva | £64.99 | £99.99; „Up to 40% off“ |
| Nuvex | $89.99; Duo $149.98; Family $209.97 | $139.99 |
| Night Lark | £70 (S) / £90 (D) / £100 (K) | 10 % Erstkauf, 15 % mit Kissen |
| Hygge Sheets (Kinder) | £24.99 | – |
| Duvet Hog (klassisch) | £94–£139 | – |

**Offer-Bausteine im Markt:** Gratis-Kissenbezüge (Wert £49.99 bei Kallyon/Moonora/Ryva, identisch mit MS 49,99 €; Pleene £39.99; Rise & Fall £35), Probezeit 30 / 40 / 60 / 90 / 100 Nächte, Gratisversand (Schwellen £30 / £40 / £50 / £85), Bundles 2er/3er, „Back in Stock“, „End-of-season clearance“, Lagerknappheit.

---

### 9. Was Magic Splashy in UK zuerst bringen kann

**A. Dort differenzieren, wo die Clones gleich klingen**
1. **Testimonials mit Alter (48–63 J.)** als Static und Video: Im UK-Segment nutzt das niemand (Kallyon zeigt nur Vornamen), bei MS ist es die Signatur. Vorschlag: „Margaret, 61, Leeds: “I stopped dreading Sunday bed-changing.”“
2. **Tog-Übersetzung des ThermoBalance-Versprechens.** Alle Clones sagen „cool in summer, warm in winter“, der UK-Kunde denkt aber in Tog. Eine ehrliche Angabe (z. B. „all-season, comparable to a ~7.5 tog“, vorher mit dem Produkt validieren) plus ein Explainer-Static „Why you don't need two duvets any more“ fehlt im Markt. Das ist zugleich ein Gegenentwurf zur Silentnight-3-in-1-Logik (`127943305` ([GH](https://app.gethookd.ai/share/ad/127943305?signature=5e8171b0b0d96b71687692d4de213e110b75f5d7b25c3f10477763f1d9270ea8) · [Meta](https://www.facebook.com/ads/library/?id=1013401628101649))).
3. **Echte UK-Größen** (135×200 Single, 225×220 King, 260×220 Super King) und einen 7–8-kg-Maschinen-Fit-Claim als Static-Bullet.

**B. Angles, die in UK frei sind (Whitespace)**
1. **Menopause / Hitzewallungen:** In den USA validiert (Dosaze, Ice Blankets, Rest Score 100, Bohobed, Linens & Hutch), im UK-Duvet-Segment nicht vorhanden. MS-Copy „Kein Schwitzen. Kein Frieren.“ übersetzen, etwa als „No more 3am kick-off-the-duvet-then-freeze“. Kallyons „No more night sweats“ (`195931651` ([GH](https://app.gethookd.ai/share/ad/195931651?signature=776c7b4deb8c1a11d49bd283c47f4c886e070822609ecda2bfc3e74c43283d2e) · [Meta](https://www.facebook.com/ads/library/?id=1871081214267591))) ist nur ein Icon-Bullet.
2. **Senioren, Arthritis und „Bettenmachen ohne Kampf“:** null Advertiser. Hook-Ideen: „At 68, the duvet cover was the one job I'd started asking my son to do.“ Moonoras Native-Static mit älterer Frau (`189407350` ([GH](https://app.gethookd.ai/share/ad/189407350?signature=b7867253093bd22254c759d45384d6ff5fa70f1dbf06cf0558b60684cbe3d82b) · [Meta](https://www.facebook.com/ads/library/?id=1096009869545467))) zeigt, dass die Zielgruppe angesprochen werden kann, ohne dass jemand den Angle ausspielt.
3. **Gift for Mum/Parents (Q4, Weihnachten):** null Coverless-Advertiser. Die UK-Vorlage ist der Evely-Rose-Brief („Twelve Christmases. Eleven Presents Still In The Cupboard…“ `193148723` ([GH](https://app.gethookd.ai/share/ad/193148723?signature=4c9fa04e4327093fc4467466e6c8bdd3d25aed8e89cfc8db7f3c0a07f016b6e2) · [Meta](https://www.facebook.com/ads/library/?id=1397604122587046))). Übertragen: „The present my 74-year-old mum actually uses every night.“
4. **Hygiene/Milben als Haupt-Hook mit Advertorial:** Dass UK-Kunden auf Milben-Angst reagieren, zeigen die Geräte-Advertorials (436 bzw. 245 Tage aktiv, `80270006` ([GH](https://app.gethookd.ai/share/ad/80270006?signature=20213f2ee6b41377ee81640500cf7374b279c71704ec04b071a25a801fe48783) · [Meta](https://www.facebook.com/ads/library/?id=635387565726640)), `77322638` ([GH](https://app.gethookd.ai/share/ad/77322638?signature=981cfbbe671dc3e1e372c758a78592c79a42aaee29293648e667de56fa530de7) · [Meta](https://www.facebook.com/ads/library/?id=848060581527812))). Bei Decken steht das Thema nur im Bullet. Hook-Vorlage aus Nuvex-IT zum Übersetzen: „Sorry, but your duvet is probably the dirtiest thing in your bedroom.“ (`198499376` ([GH](https://app.gethookd.ai/share/ad/198499376?signature=cabd3e9e90a0ddbefb93c722a3f6167e5b8395a0013b6726115f6dac24956a1e) · [Meta](https://www.facebook.com/ads/library/?id=1964300187570798))), dazu MS-Argument „Bei normalen Decken wäscht man nur den Bezug“ (steht schon auf Kallyon/Moonora-LPs, aber nicht in Ads).

**C. Formate, die in UK frei sind**
- **Advertorial-LP / „Letter from a reader“** (Gift- oder Menopause-Story) statt direkt auf die PDP, nach dem Muster von Evely Rose und getuvlizer.
- **Listicle** („5 reasons women over 50 are ditching the duvet cover“) und **Quiz** („Which tog do you actually need?“): beides 0 im Segment.
- **Experte** (Allergologe/Dermatologe zu Milben, Schlafmediziner zu Temperatur): 0 im Segment.
- **Vergleichstabelle als Ad** (EasySleep vs. Duvet + Cover vs. 3-in-1-System) und **Before/After-Static** (Sonntagabend-Kampf vs. „3 Sekunden“): auf LPs vorhanden, in Ads nicht.
- **Founder on camera**: Bisher gibt es nur Founder-Copy (Moonora). Mit echtem Gesicht wäre MS hier vorn.

**D. Was man vermeiden sollte (gesättigt bzw. nicht differenzierend)**
- Den Pleene-Copy-Block „Duvet + Cover in One 🌙 … ✓ … ✓ … ✓ … 2 pillowcases FREE … X nights“ nutzen inzwischen mindestens fünf Brands fast wortgleich (Pleene, Kallyon, Moonora, Ryva, Nuvex-EN).
- „17,000+ happy sleepers“ setzt Kallyon schon in UK ein. MS sollte eine eigene, belegbare UK-Zahl nutzen oder auf Reviews mit Alter ausweichen.
- Reiner Rabatt-Wettlauf (−40/−50 %, „Clearance“), weil sich Kallyon, Ryva, Nuvex und Moonora schon gegenseitig unterbieten.

---

### 10. Anhang: Format-Referenzen aus Nachbarkategorien (UK)

- Insider-Native-Hook (UK-Flair): „I've worked for a wealthy family in the Cotswolds for five years. The only luxury of theirs I actually copied costs less than a dinner out.“ (RevealCare) `197609362` ([GH](https://app.gethookd.ai/share/ad/197609362?signature=6de15a121b9e5548bcd485b196543acf2c8c1f77d2329a954d440c5e358e5e36) · [Meta](https://www.facebook.com/ads/library/?id=4599964530248388))
- Berufs-Insider-Hook (US, Matratzenauflage): „I made up thirty cabins a day on cruise ships for nineteen years and every time I came home I couldn't sleep in my own bed“ (Aging Well Daily) `201090796` ([GH](https://app.gethookd.ai/share/ad/201090796?signature=eb8a75ab90218bbc86d91377a82d714ea8786e175aaf4b7dabb829bf48b9905e) · [Meta](https://www.facebook.com/ads/library/?id=3054988194704450))
- Milben-Advertorial-Hooks (UK): „Read if you wake up congested in the morning 👆“ `46871558` ([GH](https://app.gethookd.ai/share/ad/46871558?signature=beca7fa48fe59c2ed0cd9b96afc2fcc7d6fe44fe4ab625b521d036151cddfe64) · [Meta](https://www.facebook.com/ads/library/?id=1167687025222234)), „Eliminates Dust Mites In Your Home? (MUST READ)“ `77322638` ([GH](https://app.gethookd.ai/share/ad/77322638?signature=981cfbbe671dc3e1e372c758a78592c79a42aaee29293648e667de56fa530de7) · [Meta](https://www.facebook.com/ads/library/?id=848060581527812))
- Hygiene-Hook (UK): „Your sheets are dirtier than you think 🦠“ (ZLEEPY) `122483597` ([GH](https://app.gethookd.ai/share/ad/122483597?signature=90a1e09315850e62688c398ef358626962bb4f330de0793d7c5b8044bac31934) · [Meta](https://www.facebook.com/ads/library/?id=971163668899126))
- Geschenk-Advertorial (UK): Evely Rose `193148723` ([GH](https://app.gethookd.ai/share/ad/193148723?signature=4c9fa04e4327093fc4467466e6c8bdd3d25aed8e89cfc8db7f3c0a07f016b6e2) · [Meta](https://www.facebook.com/ads/library/?id=1397604122587046)) / `198162782` ([GH](https://app.gethookd.ai/share/ad/198162782?signature=e6c31fd6cdd812d0c7eafc462f94d98dc18b420465b7a41f164d62bce29642db) · [Meta](https://www.facebook.com/ads/library/?id=1123844373641873))
- Zum Vergleich der Magnet-Duvet-Ansatz (USA): The Lad Collective `200735947` ([GH](https://app.gethookd.ai/share/ad/200735947?signature=caab0bc2b1f910e137f0570a9aeb71cab8e8e9a746e2e27137403d81d8e49212) · [Meta](https://www.facebook.com/ads/library/?id=1761963314857623))

