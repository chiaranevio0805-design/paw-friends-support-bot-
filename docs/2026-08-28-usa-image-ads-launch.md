# Launch-Spec: Image Ads USA 28.08.26

Angelegt am 27.08.2026, alles pausiert.

## Ergebnis

| Objekt | ID |
|---|---|
| Kampagne | `120252017271800270` — Plüschies USA Image Ads 28.08.26 |
| Adset | `120252017277300270` — Image Ads USA 28.08.26 |
| Ad 1 Donkey | `120252017285630270` |
| Ad 2 Fox | `120252017288220270` |
| Ad 3 Monkey | `120252017289710270` |
| Ad 4 Elephant | `120252017291570270` |
| Ad 5 Duck | `120252017294530270` |

`ads_get_errors` auf Kampagne und Adset: keine Zustellfehler.

**Nicht in Plüschies 02.06.26 gelandet.** Die Kampagne bleibt für das Tool
gesperrt (siehe Blocker unten), und der Auftrag lautete, ohne Handgriffe
des Inhabers fertigzuwerden. Deshalb eine eigene Kampagne — bewusst **ohne**
Gebotsstrategie auf Kampagnenebene, damit künftige Adsets dort ohne diesen
Fehler angelegt werden können.

## Adset — Soll-Werte (so umgesetzt)

| Feld | Wert |
|---|---|
| Kampagne | `120252017271800270` — Plüschies USA Image Ads 28.08.26 |
| Name | Image Ads USA 28.08.26 |
| Land | US (home + recent) |
| Tagesbudget | £25,00 (`daily_budget: 2500`) |
| Start | 28.08.2026, 04:00 (Kontozeit) |
| Ziel | OFFSITE_CONVERSIONS, Abrechnung IMPRESSIONS |
| Gebot | Highest Volume |
| Ziel-Event | Pixel `1311406010460496`, PURCHASE |
| Alter | 18–65, Advantage+ Audience an |
| Ausschluss | `120250751148250270` (Costumer die schon gekauft haben) |
| Platzierungen | automatisch |

## Die 5 Ads

Alle: Seite `1147503868444857` (Paw-Friends.Uk), CTA `ORDER_NOW`,
Primary Text = bestehender Plushies-Text aus Creative `1411888704181543`,
Ziel-URL = Produktseite (siehe „Offen").

| # | Ad-Name | Headline | Creative-URL |
|---|---|---|---|
| 1 | Donkey – No Dog Has Beaten USA 28.08.26 | No Dog Has Beaten Our Plushies Yet | `.../hf_20260826_153831_07b86826-f667-48da-bd7e-696cace203a9.png` |
| 2 | Fox – Destroy Everything USA 28.08.26 | For Dogs Who Destroy Everything | `.../hf_20260826_153832_2ddbaba0-6766-4a6f-8bb3-47b516af5578.png` |
| 3 | Monkey – Is Yours The First USA 28.08.26 | Is Yours The First? | `.../hf_20260826_155748_45febb4e-2fce-4eee-ac30-22b3e95d44d8.png` |
| 4 | Elephant – Think Yours Is Different USA 28.08.26 | Think Yours Is Different? Try It | `.../hf_20260826_155748_ad6b575d-aad9-446a-b0ac-b4bb778ceabd.png` |
| 5 | Duck – 40,000 Dogs Tried USA 28.08.26 | 40,000 Dogs Tried. Not One Has Won. | `.../hf_20260826_155749_bf4b8675-e305-42c5-9fce-a4ac228a3963.png` |

Basis-URL aller fünf:
`https://d8j0ntlcm91z4.cloudfront.net/user_3BvvIV0xKOjMxRy4PeLGy70LaFW/`

Die Bilder stammen aus dem Higgsfield-Konto (Generationen vom 26.08.2026,
15:38 und 15:57). Zuordnung erfolgte über die Prompt-Texte, nicht visuell —
der Sandbox-Proxy blockiert den CDN-Host, die Bilder konnten nicht
heruntergeladen und angesehen werden. Vor dem Scharfschalten also einmal
in der Vorschau gegenprüfen, dass Motiv und Headline zusammenpassen.

## Blocker: Adset lässt sich per API nicht anlegen

Die Kampagne ist ABO — Meta lehnt ein Adset ohne eigenes Budget mit
`Ad Set Budget is Missing` (subcode 1885649) ab. Gleichzeitig lehnt die
Vorabprüfung von `ads_create_ad_set` jedes `daily_budget` mit
„Parent campaign uses Campaign Budget Optimization (CBO)" ab. Beides
zusammen macht das Anlegen unmöglich.

Die CBO-Erkennung ist falsch: die Kampagne hat weder `daily_budget` noch
`lifetime_budget`, nur eine Gebotsstrategie auf Kampagnenebene
(„Highest volume") — die dürfte die Fehlklassifizierung auslösen. Ihre
bestehenden Adsets haben eigene Budgets zwischen £15 und £125.

Geprüft und ebenfalls erfolglos:

- `daily_budget` weglassen → Meta: Budget fehlt
- `source_adset_id` auf ein bestehendes £25-Adset → Budget wird nicht
  mitkopiert, gleicher Fehler
- Ein Update-Tool für Adsets gibt es in diesem MCP-Server nicht

Ebenfalls getestet und gescheitert: `adset_spec` inline in
`ads_create_ad`. Das Feld wird **stillschweigend ignoriert** — die Ad wird
angelegt, aber in dem Adset, das in `ad_set_id` steht, und kein neues Adset
entsteht. Der Aufruf meldet trotzdem Erfolg und gibt `adset_spec` im
Response-Spec zurück, was den Eindruck erweckt, es sei berücksichtigt
worden. Nicht darauf hereinfallen: nach jedem Anlegen die tatsächliche
`adset_id` der Ad gegenprüfen.

Dabei ist am 27.08. eine ungewollte Ad entstanden:
`120252017037980270` („Donkey - No Dog Has Beaten USA 28.08.26") im Adset
`120251949571290270` („Image Ad 4 Australien – Kopie 4"). Pausiert, kein
Spend — muss von Hand gelöscht werden, ein Delete-Tool gibt es hier nicht.

**Workaround:** das Adset einmal von Hand im Ads Manager anlegen (oder ein
bestehendes duplizieren und Land/Budget/Namen anpassen), dann die Adset-ID
durchgeben. Die 5 Ads lassen sich anschließend per API hineinbauen.

## Blocker: Bild-Upload

- `LOCAL_FILE`-Upload ist für Konto `2479996745858211` deaktiviert
- `ads_creative_upload_media` mit URL ist für dieses Konto noch nicht
  ausgerollt („gradually being rolled out")
- Ein separates `ads_creative_upload_image` existiert in diesem
  MCP-Server nicht

**Workaround:** beim Anlegen der Ad `image_url` direkt im Creative-Spec
mitgeben — Meta holt das Bild dann selbst und legt den Hash an. Deshalb
stehen oben URLs statt Image-Hashes.

Am 27.08. verifiziert: die Higgsfield-CDN-URL wurde von Meta beim Anlegen
der Ad akzeptiert. Der Bild-Weg funktioniert also, nur das Adset fehlt.

## Offen

- **Ziel-URL** noch nicht bestätigt. Kandidat aus dem Shop:
  `https://paw-friends.uk/products/cross-border-new-pet-plush-sound-cotton-rope-toy-fox-frog-pig-dog-interactive-tug-of-war-training-supplies`
  (Plushies, £29.95, aktiv). Falls eine eigene Landingpage läuft, die
  stattdessen verwenden.
- **Startzeit** „4 Uhr" wurde als 04:00 gelesen, nicht 16:00.
- **Haltbarkeits-Aussagen:** alle fünf Motive führen sie im Bild selbst
  („No dog has beaten", „40,000 dogs tried, not one has won"). Siehe die
  Copy-Warnung in `ads-launch-runbook.md` — die Aussage ist in den
  Triage-Docs als Erstattungs- und Consumer-Rights-Act-Risiko vermerkt.
  „40,000 Dogs Tried" ist zusätzlich eine konkrete Zahlenbehauptung.
