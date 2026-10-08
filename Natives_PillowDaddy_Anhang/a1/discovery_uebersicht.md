# PillowDaddy – Netzwerk-Übersicht: Domains, Märkte, Advertiser-Seiten (Lane `pd_discovery`)

Stand: 08.10.2026, ca. 11:20–11:55 UTC · Agent 1 · Belege/Suchprotokoll: `a1/discovery/log_searches.md` · Detailraster der neu gefundenen Seiten: `a1/grid_pd_discovery.md`

## Kurzfazit

- **Zwei neue Advertiser-Seiten gefunden**, beide Persona-Seiten:
  - **Sofía Hernandez** (brand 5852810, Meta-Page 985891847950208): spanischsprachige Persona für **US-Hispanics**, 58 Bild-Ads (12.06.–12.08.2026, heute 0 aktiv), Ziel: spanisches Advertorial auf der bekannten US-Funnel-Domain (`try.pillowdaddy-us.com/advert-1-neck-therapy-pillow-dizziness-es`). Zwei Konzepte liefen 57–61 Tage → Winner.
  - **Brielle Grace** (brand 12216278, Meta-Page 1357323017460512): englische Persona für **UK**, seit 06.10.2026 25 aktive PillowDaddy-Ads („PillowDaddy Cloudflare™“, „The Neck Therapy Pillow“) auf der **neuen Domain feelgoodtrends.com/neckpillow/** (Funnelish) mit Checkout im fremden Shopify-Store **zifarra.com** (GBP). Die Seite ist eine Mehrzweck-Persona eines UK-Media-Buyer-Netzes (84 weitere Ads für fremde Produkte).
- **Neue Märkte:** US-Hispanic (spanisch, seit Juni) und **UK (seit 06.10.2026, Testphase)**. Die Storefront-Shops selbst decken weiter nur DE/AT (+CH-Währung) und US (+en-GB-hreflang) ab.
- **Keine weiteren Länderdomains:** pillowdaddy.co.uk / -uk.com / .uk / .at / .ch / .fr / .nl / .it / .es / .pl / .be / .se / .dk / .ca / .com.au und alle getesteten try./shop.-Varianten existieren per DNS nicht (NXDOMAIN). pillowdaddy.com ist eine GoDaddy-Parkseite („for sale“). **pillowdaddy.eu** existiert und zeigt auf die Funnelish-IP (151.101.2.184), ist aber ohne Ads und ohne erreichbare Startseite (vermutlich reservierte Funnel-Domain).
- **Fehlzuordnung:** Im GetHooked-Shop 134422 (pillowdaddy-us.com) steht ein 6. Advertiser „Somaia“ (5349214) mit 1 Ad – die Ad landet auf www.somaia.es (spanische Fremdmarke „SomaiaSleep“, eigenes Nackenkissen, 532 aktive Ads auf somaia.es/somaiapt.store) → **kein Teil des PillowDaddy-Netzwerks**.

## 1. Domains und Märkte

| Domain | Status (DNS/HTTP, 08.10.) | Rolle | Markt / Sprache / Währung | Advertiser mit aktiven Ads auf Domain (get_domain_advertisers 11:24 UTC) | Belege |
|---|---|---|---|---|---|
| **pillowdaddy.de** (+ www → 301) | Shopify (23.227.38.65), 200 | Haupt-Shop/Startseite (Shopify-Store `the-leggie.myshopify.com`) | DE (x-default), Store-Land AT; EUR, CHF als Währung im Store | 0 (keine Ad zeigt direkt auf die Root-Domain) | hreflang de → pillowdaddy.de; Titel „PillowDaddy \| Ergonomische Kissen, die den Unterschied machen!“; Kontakt info@pillowdaddy.de |
| **shop.pillowdaddy.de** | CNAME domains.funnelish.com, Root 404 | Funnel-Domain DE (Advertorials, Listicles, Vergleichstests, PDPs) | DE/AT, deutsch, EUR | Gesund Leben Journal 74 · Claudia Reichardt 55 · Daniela Koch 25 · Karin Zimmermann 18 · Thomas Brandt 8 · PillowDaddy 7 = **187** | Traffic-Anteile Shop 134422: DE 72 %, AT 13 %, US 10 %, PH 6 % |
| **pillowdaddy-us.com** | Shopify, 200 (www → Shopify 409) | US-Storefront (gleicher Shopify-Store wie .de, Markets-Umschaltung) | US + **en-GB** (hreflang en-GB und en-US → pillowdaddy-us.com), USD | 0 | Shopify.country US, currency USD; support@pillowdaddy-us.com; GetHooked-Shop 134422 (207.522 Besuche/Monat Aug 2026, +138 %) |
| **try.pillowdaddy-us.com** | CNAME domains.funnelish.com, Root 404 | Funnel-Domain US (Advertorials, PDPs) – inkl. **spanisches Advertorial** `/advert-1-neck-therapy-pillow-dizziness-es` | US (englisch) + **US-Hispanic (spanisch)**, USD | The Daily Health 30 · Stephanie Robertson 16 · PillowDaddy 9 · Gary Kuhlman 6 · Rebecca Fitzgerald 5 = **66**; inaktiv zusätzlich **Sofía Hernandez (58 Ads, Jun–Aug)** | Shop-Publication 03.10.: 120 Ads, Advertiser DH 44, GK 28, PD 19, SR 16, RF 12, (Somaia 1 = Fehlzuordnung) |
| **feelgoodtrends.com/neckpillow/** (NEU) | Cloudflare; Pfad = Funnelish-Funnel, Root 404 | **UK-Funnel** (Advertorial `/adv-tinnitus/` + PDP `/products/neckpillow/`) | **UK, englisch, GBP** (1x £49.95 … 4x £149.95) | **Brielle Grace 25** (first_seen 06.10.2026) · Elara Vandenberg 1 (andere Offer `/oxivaflow/`, kein PD) | Footer „MT Ecommerce GmbH, Krenngasse 12, 8010 Graz, Austria, UID ATU82513102“; GTM über ss.pillowdaddy.de; Funnel-JSON-URL `shop.pillowdaddy.co.uk/neck-therapy-pillow-7-tinnitus` |
| **zifarra.com** (NEU, Checkout) | Shopify `kdudw1-00.myshopify.com`, GBP, Land GB | Warenkorb/Checkout des UK-Funnels (Produkt „PillowDaddy“, angelegt 30.09.2026) – Multi-Offer-Store mit ~60 fremden Produkten | UK | 12 Persona-Seiten (Dr. Alva Mirelle 18, Brielle Grace 14, Elara Noemi 10, Helena Rossi 10, Nature’s Secret Discoveries 9, Adrien Morel 9, Dylan Cooper 3, je 1: Dr. Elena Kovács, Amalia Serrano, Astrid Svea, Elias Virel, Theo Laurent) – **alle 80 indexierten zifarra-Ads bewerben andere Produkte** (incontinence1, hand-care, primalmarin, seraflow, lung-health, migraine-health, gut-health) | Cart-Links der PDP: zifarra.com/cart/59532449153349:1 usw. = Varianten 1x/2x/3x/4x „PillowDaddy“ |
| **pillowdaddy.eu** | DNS → 151.101.2.184 (Funnelish/Fastly), HTTPS-Root nicht erreichbar | vermutlich reservierte Funnel-Domain (EU) | – | 0; search_ads(query „pillowdaddy.eu“) 0 | nur DNS-Beleg |
| ss.pillowdaddy.de, t.pillowdaddy.de, t.pillowdaddy-us.com | Tracking-Subdomains | Server-Side-GTM (GTM-TP7ZC855), Tracking | – | – | in allen Funnel-/Shop-HTMLs referenziert; zusätzlich Taboola-Pixel (taboolaId 1996268) und wetracked.io-Pixel im Shop |
| pillowdaddy.com | GoDaddy-Parking → forsale.godaddy.com | **nicht PillowDaddy** (Domain zum Verkauf) | – | 0 | |
| pillowdaddy.co.uk, pillowdaddy-uk.com, pillowdaddy.uk, .at, .ch, .fr, .nl, .it, .es, .pl, .be, .se, .dk, .ca, .com.au, pillowdaddy-eu/-au/-ca/-fr/-nl/-it/-ch/-at/-de.com, pillowdaddy.shop/.store, mypillowdaddy.com, getpillowdaddy.com, trypillowdaddy.com, thepillowdaddy.com, pillowdaddyshop.com, try.pillowdaddy.de, shop.pillowdaddy-us.com, try./shop.pillowdaddy.co.uk, try./shop.pillowdaddy.com | **NXDOMAIN** (Cloudflare-DoH) bzw. nicht erreichbar | existieren nicht | – | get_domain_advertisers für .com/.co.uk/-uk.com/.at/.ch/.fr: je 0 | |

## 2. Alle Advertiser-Seiten (bekannt + neu)

Aktive Ads je Domain = `get_domain_advertisers` (08.10., 11:24 UTC). first_seen = Datum, an dem GetHooked die Seite erstmals auf der Domain sah (Achtung: 12.06.2026 ist bei vielen Seiten der Start des GetHooked-Domain-Rosters, nicht das Gründungsdatum). Gründungsdatum der Meta-Seiten ist über die verfügbaren Tools nicht abrufbar → stattdessen früheste bekannte Ad.

| Seite | brand_id | Meta-Page-ID | Typ | Markt / Domain | aktive Ads auf Domain | first_seen (Domain) | früheste bekannte Ad | Ads im Fenster (Lane) | Bemerkung |
|---|---|---|---|---|---|---|---|---|---|
| PillowDaddy | 157840 | 101822769415384 | **Marke** | DE/AT shop.pillowdaddy.de + US try.pillowdaddy-us.com | 7 (DE) + 9 (US) | 12.06.2026 (DE) / 19.09.2026 (US) | 11.05.2025 (45452602, a2-Beleg) | 207 (135 `pd_marke_bis_juli` + 72 `pd_marke_ab_aug`) | US-Ads der Marke erst ab Sept. 2026 |
| Gesund Leben Journal | 1872051 | 526059080581896 | **Fake-Magazin** | DE/AT shop.pillowdaddy.de | 74 | 12.06.2026 | 07.04.2025 | 483 (`persona_de_journal_brandt`) | größte Native-Seite (1.211 Ads seit 04/2025) |
| Claudia Reichardt | 1247984 | 903175946203822 | Persona-Person (Frau) | DE/AT shop.pillowdaddy.de | 55 | 04.07.2026 | 17.01.2026 (Rohdaten) | andere Lane | |
| Daniela Koch | 3930663 | 1012608671928965 | Persona-Person (Frau) | DE/AT shop.pillowdaddy.de | 25 | 12.06.2026 | 11.02.2026 (Rohdaten) | andere Lane | |
| Karin Zimmermann | 626049 | 550667068122477 | Persona-Person (Frau) | DE/AT shop.pillowdaddy.de | 18 | 21.08.2026 | 09.11.2025 (Rohdaten) | andere Lane | lt. a2-Notiz > 600 inaktive Ads |
| Thomas Brandt – Tipps für Rücken & Nacken | 21391046 | 591200527416229 | **Experte** (Chiropraktiker-Persona; „fiktive Person“ laut DE-Advertorial-Footer) | DE/AT shop.pillowdaddy.de | 8 | 29.09.2026 | 29.09.2026 | 10 (`persona_de_journal_brandt`) | gleiche Autor-Figur in DE-, US- und ES-Advertorials |
| The Daily Health | 3551625 | 874379962435015 | **Fake-Magazin** | US try.pillowdaddy-us.com | 30 | 12.06.2026 | 07.03.2026 (Rohdaten) | andere Lane | Shop-Publication: 44 Ads |
| Stephanie Robertson | 1904510 | 910977565432259 | Persona-Person (Frau) | US try.pillowdaddy-us.com | 16 | 03.07.2026 | 01.01.2026 (Rohdaten; Langläufer 82191398 01.01.–07.05.) | andere Lane | 502 inaktive Ads gesamt |
| Gary Kuhlman | 2777246 | 829794000226606 | Persona-Person (Mann) | US try.pillowdaddy-us.com | 6 | 13.09.2026 | 14.12.2025 (Rohdaten) | andere Lane | 355 inaktive Ads gesamt |
| Rebecca Fitzgerald | 2777235 | 955574097644624 | Persona-Person (Frau) | US try.pillowdaddy-us.com | 5 | 13.06.2026 | 18.02.2026 (Rohdaten) | andere Lane | 1.680 inaktive Ads gesamt |
| **Sofía Hernandez (NEU)** | **5852810** | **985891847950208** | Persona-Person (Frau, US-Hispanic); im Aug.-Test als „terapeuta vestibular“ (Expertin) inszeniert | US-Hispanic, try.pillowdaddy-us.com/advert-1-neck-therapy-pillow-dizziness-es | 0 (alle inaktiv) | – (nicht im aktiven Roster) | 12.06.2026 | **58** (diese Lane) | 2 Winner-Konzepte (57–61 T), 3 Verlierer-Konzepte (Aug.) |
| **Brielle Grace (NEU)** | **12216278** | **1357323017460512** | Persona-Person (Frau, UK) – **Mehrzweck-Persona eines fremden Netzes** | UK, feelgoodtrends.com/neckpillow (+ zifarra.com u. a. für Fremd-Offers) | **25** (feelgoodtrends) + 14 (zifarra, fremd) | 06.10.2026 (feelgoodtrends) / 01.10.2026 (zifarra) | 28.09.2026 (Fremd-Offer) / 06.10.2026 (PillowDaddy) | **25 PD** + 84 Nicht-PD (diese Lane) | Aufwärmphase mit 40 Engagement-Posts ohne Link |
| Somaia | 5349214 | 499004999960030 | Fremdmarke (ES/PT) | somaia.es, somaiapt.store | 0 auf PD-Domains | – | – | – | GetHooked-Fehlzuordnung im Shop 134422 (LP www.somaia.es) |
| Elara Vandenberg | 11855309 | 1323652134163031 | Persona des zifarra-Netzes | feelgoodtrends.com/oxivaflow | 0 PD (1 Fremd-Offer) | 01.10.2026 | – | – | teilt nur die Domain feelgoodtrends.com, kein PillowDaddy |

## 3. Wie das Netzwerk aufgebaut ist

```text
Betreiber: MT Ecommerce GmbH, Krenngasse 12, 8010 Graz (AT), UID ATU82513102, Mitglied WKÖ
│
├─ Shopify-Store "the-leggie.myshopify.com"  (ein Store, Shopify Markets)
│    ├─ pillowdaddy.de        → DE/AT (EUR; CHF hinterlegt)    hreflang de / x-default
│    └─ pillowdaddy-us.com    → US + en-GB (USD)               hreflang en-US, en-GB
│
├─ Funnel-Schicht (Funnelish): Advertorial → PDP mit Bundles → Shopify-Checkout
│    ├─ shop.pillowdaddy.de        (DE)   Autor "Thomas Brandt, Chiropraktiker" (fiktiv)
│    ├─ try.pillowdaddy-us.com     (US)   Autor "Thomas Brandt, Chiropractor"
│    │     └─ /advert-1-neck-therapy-pillow-dizziness-es  (US-Hispanic) "Thomas Brandt, Quiropráctico"
│    ├─ feelgoodtrends.com/neckpillow (UK, seit 10/2026) Autor "James Crawford, Chiropractor"
│    │     └─ Checkout: zifarra.com (fremder UK-Multi-Offer-Shopify-Store, Produkt "PillowDaddy", GBP)
│    └─ pillowdaddy.eu (nur DNS → Funnelish, ungenutzt)
│
├─ Tracking: ss.pillowdaddy.de (Server-Side-GTM GTM-TP7ZC855, auch im UK-Funnel), t.pillowdaddy.de,
│            t.pillowdaddy-us.com, Taboola-Pixel 1996268, wetracked.io
│
└─ Meta-Werbeseiten (Absender der Ads)
     ├─ Marke: PillowDaddy (DE + US)
     ├─ DE: Fake-Magazin "Gesund Leben Journal" · Experte "Thomas Brandt – Tipps für Rücken & Nacken"
     │      · Personas Claudia Reichardt, Daniela Koch, Karin Zimmermann
     ├─ US: Fake-Magazin "The Daily Health" · Personas Stephanie Robertson, Rebecca Fitzgerald, Gary Kuhlman
     ├─ US-Hispanic: Persona "Sofía Hernandez" (Jun–Aug 2026)            ← NEU
     └─ UK: Persona "Brielle Grace" (Mehrzweckseite eines UK-Media-Buyer-Netzes,
            schaltet parallel Inkontinenz-, Haut-, Lungen-, Magnesium-Offers in UK/ZA/DE/ES/BR/PT) ← NEU
```

Muster:
- **Pro Markt dieselbe Rollenverteilung:** 1 Markenseite (wenig Ads, Retargeting/Angebot), 1 Fake-Magazin (größtes Volumen, Patientenberichte/Tests), mehrere Ich-Personas (meist Frauen 45–60), 1 Experten-Figur (Chiropraktiker „Thomas Brandt“, in UK umbenannt in „James Crawford“). Alle verlinken auf Advertorials derselben Funnel-Domain.
- **Neue Märkte werden über Übersetzung + neue Persona erschlossen**, nicht über neue Shops: US-Hispanic läuft auf der US-Funnel-Domain mit übersetztem Advertorial; UK läuft über einen geklonten Funnel (Footer/Tracking von PillowDaddy) auf einer neutralen Domain mit fremdem Checkout – vermutlich Kooperation mit einem UK-Media-Buyer-Netz (Persona-Seiten mit vielen Offers, Checkout-Store zifarra.com mit ~60 Produkten). Ob PillowDaddy selbst oder ein Partner die UK-Ads bezahlt, ist nicht belegbar.
- **Zeitachse:** Marke seit 05/2025, Gesund Leben Journal seit 04/2025 (DE); US-Funnel ab ~12/2025 (Traffic pillowdaddy-us.com: Dez 2025 203 → Jan 2026 76.119 Besuche); US-Personas ab 12/2025–03/2026; Karin Zimmermann ab 11/2025; spanische Persona 06–08/2026; Thomas-Brandt-Seite seit 29.09.2026; **UK seit 06.10.2026**.
- **Kein PillowDaddy-Netz auf weiteren Ländern im Ad-Index:** GetHooked-Volltextsuchen (strict) „pillowdaddy-us.com“ und „pillowdaddy.de“ finden nur die 6 bzw. 6 bekannten Seiten (+ Sofía); „PillowDaddy“, „Nacken Therapiekissen“, „Therapiekissen“ nur bekannte Seiten; „Schlaftherapie Kissen“, „Almohada Terapéutica Cervical“, „PillowDaddy Cloudflare“, „pillowdaddy.eu“ 0 Treffer; „Neck Therapy Pillow“ 61 Marken, davon nur bekannte PD-Seiten aus dem Netzwerk, Rest Konkurrenz (Mellow, CradleSloth, Sleepsake, Monsori, Callixe …).

## 4. Durchgeführte Suchen (Kurzprotokoll, Details in `a1/discovery/log_searches.md`)

| Suche | Ergebnis |
|---|---|
| get_domain_advertisers: pillowdaddy.de, pillowdaddy-us.com, pillowdaddy.com, .co.uk, -uk.com, .at, .ch, .fr, pillowdaddy.eu | je 0 Advertiser |
| get_domain_advertisers: shop.pillowdaddy.de / try.pillowdaddy-us.com | 6 bzw. 5 bekannte Seiten (truncated=false) |
| get_domain_advertisers: feelgoodtrends.com / zifarra.com | Brielle Grace 25 + Elara Vandenberg 1 / 12 Personas (alle fremde Offers außer BG-Verknüpfung) |
| get_shop_advertisers(134422) / get_shop_landing_pages(134422) | 6 Advertiser (5 bekannt + Somaia = Fehlzuordnung); 7 LPs (6 try.pillowdaddy-us.com + 1 www.somaia.es) |
| list_shops(q="pillowdaddy") | nur Shop 134422 (pillowdaddy-us.com); kein separater Shop für pillowdaddy.de |
| get_shop_brand_group(134422) | nicht gruppiert |
| search_brands("pillowdaddy" / "pillow daddy") | nur brand 157840 |
| search_ads strict URL-Query "pillowdaddy-us.com" (1 Ad/Marke) | 6 Marken: PillowDaddy, Gary Kuhlman, The Daily Health, Stephanie Robertson, Rebecca Fitzgerald, **Sofía Hernandez (neu)** |
| search_ads strict "pillowdaddy.de" | 6 bekannte DE-Seiten |
| search_ads strict "PillowDaddy" / "Nacken Therapiekissen" / "Therapiekissen" | nur bekannte Seiten (+ Fremdmarken Wirbelfrei, Freivonschmerzen) |
| search_ads strict "Schlaftherapie Kissen", "Almohada Terapéutica Cervical", "PillowDaddy Cloudflare", "pillowdaddy.eu" | 0 |
| search_ads strict "Neck Therapy Pillow" | 61 Marken (Konkurrenz + bekannte PD-Seiten) |
| Meta Ad Library search_terms "pillowdaddy" (ALL) | u. a. **Brielle Grace** (→ GetHooked 12216278 verifiziert), Gesund Leben Journal, Claudia Reichardt, Daniela Koch, Karin Zimmermann; „Wellness blogs“ (106649068410877, FR, Kniekissen „Vous dormez sur le côté ? Le confort commence entre vos genoux.“) – in GetHooked nicht auffindbar, Bezug zu PillowDaddy **nicht verifiziert** (Meta-Suche ist unscharf) |
| search_ads landing_page_domain=sunvanna/espavesa/thandaro/medativa/zynvanna/zynvannahalsa + "pillow" | 0 (PillowDaddy nur über feelgoodtrends.com) |
| DNS (Cloudflare DoH) für 30 Domain-Varianten | siehe Tabelle 1 |
| WebSearch „PillowDaddy“ (DE/UK) | keine weiteren Shops/Domains; nur SEO-Review-Blogs („PillowDaddy Reviews: Can It Stop Snoring“ u. ä. auf fremden Domains) |

## 5. Lücken

- Gründungsdaten der Meta-Seiten nicht abrufbar (kein Tool liefert Page-Creation-Date); angegeben sind first_seen und früheste bekannte Ad (bei bekannten Seiten aus unvollständigen Rohdaten des Erstlaufs).
- Inaktive Seiten, die vor Juni 2026 endeten und keine gespeicherten Ads im Index haben, sind über GetHooked nicht auffindbar (inactive-Suche braucht brand_id); die Meta-Ad-Library-Suche wurde nur einmal (Keyword „pillowdaddy“, 50 Treffer) genutzt.
- UK-Ads von Brielle Grace sind 2–3 Tage alt → noch keine Aussage über Erfolg; Spend/Performance unbekannt.
- Rollenverteilung UK (PillowDaddy selbst vs. Partnernetz) nur indiziell belegt.
