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

## Korrigierte Ads (v2) — diese gelten

Nach Aufhebung der Kontosperre am 27.08. mit `link_data.picture` statt
`image_url` neu angelegt. Alle fünf haben einen **eigenen** Bild-Hash,
alle 1024×1024 PNG — passend zu den Higgsfield-Quelldateien. Die falschen
Creatives waren 1280×1280 JPG, der Unterschied ist also auch an den
Maßen erkennbar. `ads_get_errors` über alle fünf: leer.

| Ad | ID | image_hash |
|---|---|---|
| Donkey – No Dog Has Beaten … v2 | `120252017449760270` | `cc0db34c…` |
| Fox – Destroy Everything … v2 | `120252017468300270` | `c78aac62…` |
| Monkey – Is Yours The First … v2 | `120252017472450270` | `569522d8…` |
| Elephant – Think Yours Is Different … v2 | `120252017479620270` | `dc1f38a5…` |
| Duck – 40000 Dogs Tried … v2 | `120252017481360270` | `f85ab990…` |

Das `v2` im Namen trennt sie von den fehlerhaften Ads darunter, die kein
Delete-Tool entfernen kann. Nach dem Löschen der alten kann der Suffix weg.

Visuell geprüft ist die Zuordnung Bild ↔ Headline weiterhin **nicht** —
der Sandbox-Proxy blockiert sowohl den Higgsfield-CDN als auch Metas
`fbcdn.net`. Der Abgleich läuft über Prompt-Text, Dateiname und Bildmaße.
Ein Blick in die Ads-Vorschau bleibt Pflicht.

## Australien und UK (27.08. nachgezogen)

Dieselben fünf Creatives, je eine eigene Kampagne, Struktur identisch zur
USA-Kampagne: ABO, keine Gebotsstrategie auf Kampagnenebene, £25/Tag,
Start 28.08. 04:00, Pixel-PURCHASE, Advantage+ Audience, Käufer
ausgeschlossen, automatische Platzierungen. Alles pausiert.

| Land | Kampagne | Adset |
|---|---|---|
| AU | `120252017644050270` | `120252017654900270` |
| UK | `120252017649260270` | `120252017657020270` |

Meta hat die Creatives dedupliziert: die AU- und UK-Ads verweisen auf
**exakt dieselben** creative_ids wie die verifizierten USA-v2-Ads
(`1096702496202409` Donkey, `1568938381392224` Fox, `1793156828384215`
Monkey, `1691925281896909` Elephant, `1593597578776794` Duck). Die Bilder
sind damit per Konstruktion korrekt — der Hash-Check von USA gilt mit.

## Set 2 (27.08., alle drei Länder)

Fünf weitere Motive, direkt aus der Higgsfield-Historie gezogen — kein
Zuschicken nötig. £20/Tag je Adset, sonst identisch zur Vorlage.

| Land | Adset |
|---|---|
| USA | `120252017762190270` — Image Ads USA Set 2 |
| AU | `120252017764850270` — Image Ads AU Set 2 |
| UK | `120252017765350270` — Image Ads UK Set 2 |

Fünf eigene Bild-Hashes, geprüft: `d7f3bcf1` Think Yours Is Different,
`ec32d3a9` He Wrecks Everything, `bdd092d4` No Dog Has Ever Beaten These,
`d4a5a2ec` For Dogs That Destroy Everything, `38fc9551` 40,000 Dogs Tried
Zero Won.

**Klon-Trick für weitere Länder:** die Creatives einmal in einem Land mit
`link_data.picture` anlegen, dann in den anderen Ländern nur noch
`{"creative_id":"..."}` übergeben. Spart den Text, das Bild und den
erneuten Hash-Check — Meta dedupliziert ohnehin.

## Vollausbau Set 3–6 (27.08., unbeaufsichtigt gebaut)

20 weitere Motive aus der Higgsfield-Historie, in Fünferpakete geteilt,
jedes Paket in allen drei Ländern. Damit stehen **18 Adsets und 90 Ads**.

| Set | USA | AU | UK |
|---|---|---|---|
| 3 | `120252017810660270` | `120252017811790270` | `120252017812490270` |
| 4 | `120252017816640270` | `120252017820790270` | `120252017823480270` |
| 5 | `120252017825470270` | `120252017826130270` | `120252017827270270` |
| 6 | `120252017828610270` | `120252017829160270` | `120252017829820270` |

Motive je Set — 3: Never Beaten, Unbeaten, See The Difference, Stop Buying
The Wrong Toys, Not All Dog Toys Are Equal. 4: Why Dogs Can't Beat Ours,
Undefeated, Built To Survive Him, Ours vs Ordinary Toys, Still Standing.
5: 40,000 Tried Zero Wins, 40,000 Dogs Have Tried, Think Your Dog Is
Different, Meet The Challengers, Every Dog Has Tried. 6: Same Week Very
Different Result, Stop Wasting Money, The Math Is Simple, Other Toys Don't
Stand A Chance, He Beats Every Toy Not This One.

Alles pausiert, `ads_get_errors` über alle drei Kampagnen: leer.

### Tagesbudget im Vollausbau

3 Adsets à £25 (Set 1) + 15 Adsets à £20 (Set 2–6) = **£375 pro Tag**,
sobald alles scharf geschaltet wird.

### Ungeprüft: die Bildinhalte

Die Motive wurden über Prompt-Text und Dateiname zugeordnet, **nicht
visuell** — der Proxy blockiert Higgsfield-CDN und fbcdn gleichermassen.
Bei KI-erzeugtem Text im Bild sind Schreibfehler nicht auszuschliessen.
Vor dem Scharfschalten gehört jedes Adset einmal durch die Ads-Vorschau.

## Wo die Chat-Bilder herkommen — ungeklärt

Sechs per Chat geschickte Motive sind in keiner erreichbaren Quelle:
Higgsfield (120 neueste Generierungen durchsucht), Higgsfield Marketing
Studio (leer), alle Higgsfield-Workspaces (nur einer), Knight Vision
(neueste 18.08.), Shopify Files (neueste 22.08.). Google Drive bietet über
MCP nur Schreib-Tools, kein Lesen.

Die Serie dazu existiert in Higgsfield („OURS ARE STILL STANDING", drei
Toys, schwarze Fußleiste), aber **alle acht Varianten dort haben
Studio-Hintergründe** — keine hat die Wohnzimmer-Szene mit den zerfetzten
Spielzeugen. Diese Motive stammen aus einem Werkzeug, auf das dieser
Zugang keinen Zugriff hat.

## ⚠️ Die ersten fünf Ads sind fehlerhaft — nicht scharf schalten

Alle fünf Creatives tragen denselben Bild-Hash
`5142c41441073142e2e341d5fe8dc647` — ein bereits vorhandenes Bild namens
„untitled_105" (1280×1280, angelegt 07.08.2026). Keines der fünf
übergebenen Motive ist angekommen.

Ursache: `image_url` auf **Creative-Ebene** wird ignoriert. Meta meldet
keinen Fehler, sondern setzt ersatzweise ein beliebiges vorhandenes Bild
des Kontos ein. Der Aufruf gibt Erfolg zurück und spiegelt die `image_url`
im Response — genau dieselbe Falle wie bei `adset_spec`.

Die Empfehlung im Tool-Text („If you have only an image URL, place it at
the creative top level, not inside link_data") führt also ins Leere.
Richtig ist vermutlich `link_data.picture`. **Ungetestet** — der Test
scheiterte an der Kontosperre unten.

**Regel daraus: nach jedem `ads_create_ad` den `image_hash` des erzeugten
Creatives auslesen und prüfen, dass er sich zwischen den Ads
unterscheidet.** Ein Erfolg im Response sagt nichts über das Bild aus.

## ⚠️ Konto für Schreibzugriffe gesperrt

Seit dem 27.08. lehnt Meta jedes Anlegen und Ändern ab:

> Please authenticate your account: We think someone may have tried to
> access your account without permission. (error_code 31, subcode 3858385)

Bestehende Ads laufen weiter. Die Sperre muss der Inhaber im Ads Manager
per Identitätsprüfung aufheben, bevor die Bilder korrigiert werden können.
Ausgelöst vermutlich durch die Menge an Schreibversuchen in kurzer Zeit —
also: bei künftigen Launches erst einen Testfall verifizieren, dann den
Rest, statt fünf Creates parallel abzufeuern.

## Aufräumliste (nur von Hand möglich, kein Delete-Tool)

- Die 5 Ads **ohne** `v2` im Namen — falsches Bild, ersetzt durch die v2-Ads
- Ad `120252017037980270` im Adset `120251949571290270`
  („Image Ad 4 Australien – Kopie 4") — Fehlversuch mit `adset_spec`

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

---

# Vollausbau 27.08.2026 — 24 Adsets, 117 Ads, 3 Länder

Ersetzt die oben beschriebenen Erst-Versuche. Alles PAUSED, Start
28.08.2026 04:00 Kontozeit, £20/Tag je Adset.

## Kampagnen

| Land | Kampagnen-ID | Name |
|---|---|---|
| USA | `120252017271800270` | Plüschies USA Image Ads 28.08.26 |
| Australien | `120252017644050270` | Plüschies AU Image Ads 28.08.26 |
| UK | `120252017649260270` | Plüschies UK Image Ads 28.08.26 |

Kein Kampagnenbudget, keine Bid-Strategy auf Kampagnenebene (ABO) — sonst
greift die CBO-Fehlerkennung des Create-Tools, siehe Runbook.

## Adsets (8 Batches × 3 Länder = 24)

| Batch | Motive | USA | AU | UK |
|---|---|---|---|---|
| B1 | 0–4 | `120252018113460270` | `120252018115520270` | `120252018117690270` |
| B2 | 5–9 | `120252018120510270` | `120252018122640270` | `120252018125010270` |
| B3 | 10–14 | `120252018287960270` | `120252018290100270` | `120252018290800270` |
| B4 | 15–19 | `120252018292500270` | `120252018297060270` | `120252018299440270` |
| B5 | 20–24 | `120252018379050270` | `120252018379860270` | `120252018380130270` |
| B6 | 25–29 | `120252018405140270` | `120252018406630270` | `120252018408050270` |
| B7 | 30–34 | `120252018430070270` | `120252018430780270` | `120252018431470270` |
| B8 | 35–38 | `120252018450150270` | `120252018451370270` | `120252018451870270` |

B1–B7 haben je 5 Ads pro Land, B8 nur 4 (39 Motive gehen nicht glatt durch
5 auf). Summe: 117 Ads.

Adset-Einstellungen identisch für alle 24:

```
optimization_goal  OFFSITE_CONVERSIONS
billing_event      IMPRESSIONS
bid_strategy       LOWEST_COST_WITHOUT_CAP (Highest Volume)
daily_budget       2000  (= £20,00)
destination_type   WEBSITE
start_time         2026-08-28T04:00:00+02:00
promoted_object    {"pixel_id":"1311406010460496","custom_event_type":"PURCHASE"}
targeting          Land (US | AU | GB), home+recent, 18–65,
                   Advantage+ Audience an,
                   Ausschluss 120250751148250270
attribution        7 Tage Klick + 1 Tag View (Default)
Platzierungen      automatisch
```

## Ads

Alle: Seite `1147503868444857` (Paw-Friends.Uk), CTA `ORDER_NOW`,
`conversion_domain` `paw-friends.uk`, Ziel-URL

`https://paw-friends.uk/products/cross-border-new-pet-plush-sound-cotton-rope-toy-fox-frog-pig-dog-interactive-tug-of-war-training-supplies`

Primary Text: der bestehende Plushies-Text („Bought this toy expecting my
dog to destroy it within hours ❌ …"), identisch in allen 117 Ads.

Bilder: 39 Higgsfield-Motive vom 26.08.2026 (Gruppen-/Varianten-Shots, die
Collagen mit Hundefotos am Rand sind bewusst nicht dabei). Basis-URL

`https://d8j0ntlcm91z4.cloudfront.net/user_3BvvIV0xKOjMxRy4PeLGy70LaFW/`

Vorgehen je Batch: 3 Adsets anlegen → 5 USA-Ads mit `link_data.picture`
→ `creative_id` je Ad auslesen → je 5 Klon-Ads für AU und UK mit
`{"creative_id":"…"}`. Meta dedupliziert Creatives kontoweit, ein Klon
zeigt garantiert dasselbe Bild.

## Verifikation 27.08.

- 24 Adsets, alle `PAUSED`, alle £20,00 GBP, alle Start
  `2026-08-28T03:00:00+0100` (= 04:00 MESZ) — geprüft per
  `ads_get_ad_entities`
- 117 Ads angelegt, Verteilung 15/15/15/15/15/15/15/12
- `ads_get_errors` über alle drei Kampagnen: leer
- `image_hash` aller 29 in B3–B8 neu angelegten Creatives ausgelesen:
  29 verschiedene Hashes, keiner davon der alte Fallback
  `5142c41441073142e2e341d5fe8dc647`. Die Bilder sind also drin.

Was **nicht** verifiziert werden konnte: ob Motiv und Headline visuell
zusammenpassen. Der Sandbox-Proxy blockiert den CDN-Host, die Bilder
lassen sich nicht herunterladen und ansehen. Die Zuordnung stammt aus den
Higgsfield-Prompt-Texten. Vor dem Scharfschalten einmal durch die Vorschau
scrollen.

## Muss von Hand gelöscht werden

Es gibt in diesem MCP-Server kein Delete- oder Update-Tool. Diese Reste
aus früheren Versuchen liegen pausiert im Konto und müssen im Ads Manager
weg:

1. Die drei Adsets „Image Ads USA / AU / UK Set 5" — das sind die
   Hundefoto-Collagen, die nicht gewollt sind.
2. Die 5 Ads in „Image Ads USA Set 1" **ohne** `v2` im Namen — die haben
   das falsche Bild (`5142c41441073142e2e341d5fe8dc647`).
3. Ad `120252017037980270` („Donkey - No Dog Has Beaten USA 28.08.26") im
   Adset `120251949571290270`.

## Budget beim Scharfschalten

24 Adsets × £20 = **£480/Tag**, wenn alles gleichzeitig läuft. Pro Land
£160/Tag. Wer kleiner starten will: erst B1–B2 je Land aktivieren
(£120/Tag) und den Rest nachziehen.
