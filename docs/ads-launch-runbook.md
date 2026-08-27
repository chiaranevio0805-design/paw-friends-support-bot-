# Ads-Launch-Runbook (Meta Ads Manager)

Vorlage für den wiederkehrenden Ablauf: **neue Adsets in einer laufenden
Kampagne anlegen, Creatives hochladen, Ads bauen** — alles pausiert, damit
nur noch scharf geschaltet werden muss.

Erhoben am 27.08.2026 aus dem Live-Konto. Die IDs unten sind der
Ausgangspunkt jedes Launches — nicht raten, hier nachschlagen.

## Konto und Kampagne

| Feld | Wert |
|---|---|
| Werbekonto | `2479996745858211` — „Uk 1" (Business: Ecommerce Marasa) |
| Währung | GBP |
| Standard-Kampagne | `120247283540670270` — „Plüschies 02.06.26" |
| Kampagnen-Ziel | `OUTCOME_SALES` |
| Budgetlogik | **ABO** — Budget liegt pro Adset, nicht auf der Kampagne |
| Facebook-Seite | `1147503868444857` — „Paw-Friends.Uk" |
| Pixel | `1311406010460496` |
| Ausschluss-Audience | `120250751148250270` — „Costumer die schon gekauft haben" |

Weitere laufende Kampagnen im selben Konto, falls ein Launch dorthin soll:

| Kampagne | ID | Budget |
|---|---|---|
| Bottel of Funnel 21.08.2026 | `120251876756240270` | ABO |
| Fluffys 11.08.26 USA – Kopie | `120251586285160270` | ABO |
| CBO USA – Kopie | `120251500531540270` | CBO £150/Tag |
| Fluffys 04.08.26 UK | `120251349861320270` | ABO |
| CBO USA | `120251097884290270` | CBO £75/Tag |

**Wichtig bei CBO-Kampagnen:** dort bekommen neue Adsets *kein* eigenes
Budget und *keine* eigene Gebotsstrategie — Meta lehnt das sonst mit
„Must Use Campaign Bid Strategy" ab.

## Standard-Adset (Vorlage)

Ausgelesen aus „Uk Sunny Ads 1 24.08.26 Long" (`120251949506070270`).
Jedes neue Adset wird so gebaut; abweichen nur, wo es ausdrücklich gesagt
wird.

- Optimierungsziel: `OFFSITE_CONVERSIONS` (Conversions)
- Abrechnung: `IMPRESSIONS`
- Gebotsstrategie: Highest Volume (`LOWEST_COST_WITHOUT_CAP`)
- Promoted Object: Pixel `1311406010460496`, Event `PURCHASE`
- Land: `GB` (bzw. `US` / `AU` je nach Adset), Location Types: home + recent
- Alter: 18–65, Geschlecht: alle
- Advantage+ Audience: **an** (`targeting_automation.advantage_audience = 1`)
- Ausgeschlossen: Custom Audience `120250751148250270`
- Platzierungen: automatisch — Facebook, Instagram, Threads;
  Mobile + Desktop
- Attribution: Standard (7 Tage Klick + 1 Tag View), nicht überschreiben
- Budget: pro Adset, wird beim Launch genannt (Bestand liegt zwischen
  £15 und £125/Tag)

Weil Advantage+ Audience an ist, sind Alter 18–65 nur ein Signal, keine
harte Grenze. Falls eine harte Altersgrenze gewünscht ist:
`targeting_automation.advantage_audience = 0` setzen.

## Standard-Ad (Vorlage)

Ausgelesen aus Creative `1411888704181543`:

- Format: Video (`object_type: VIDEO`)
- Seite: `1147503868444857`
- Call to Action: `ORDER_NOW`
- Headline (`title`) und Primary Text (`body`) kommen pro Launch neu
- Instagram läuft über das seitengebundene IG-Konto — im Konto ist kein
  separates IG-Konto für die API freigegeben, das ist normal und
  funktioniert

## Creatives: was geht und was nicht

Das ist der echte Engpass. Stand 27.08.2026 für Konto `2479996745858211`:

| Weg | Video | Bild |
|---|---|---|
| `picture` in `link_data` des Creative-Specs | ❌ | ✅ |
| `image_url` auf Creative-Ebene | ❌ | ❌ (still ignoriert) |
| Liegt schon in der Meta-Mediathek (per Hash/ID referenzieren) | ✅ | ✅ |
| `ads_creative_upload_media`, `upload_source: URL` | ❌ | ❌ |
| `ads_creative_upload_media`, `upload_source: LOCAL_FILE` | ❌ | ❌ |
| Google Drive / Dropbox / Canva-Freigabelink | ❌ | ❌ |

Beide Upload-Wege sind für dieses Konto zu: LOCAL_FILE ist deaktiviert
(„Local file upload is not available for ad account"), und der URL-Upload
ist noch nicht ausgerollt („This tool is new and is being gradually rolled
out"). Ein separates `ads_creative_upload_image` gibt es in diesem
MCP-Server nicht.

**`image_url` auf Creative-Ebene funktioniert NICHT.** Am 27.08. getestet:
das Feld wird ignoriert, der Aufruf meldet Erfolg und spiegelt die URL im
Response, aber Meta setzt ein beliebiges bereits vorhandenes Bild des
Kontos ein. Fünf Ads mit fünf verschiedenen URLs bekamen alle denselben
Hash. Die Empfehlung im Tool-Text ist an dieser Stelle falsch.

**Richtig ist `picture` innerhalb von `link_data`.** Am 27.08. verifiziert:
damit bekommt jede Ad ihren eigenen Bild-Hash, und die Maße stimmen mit der
Quelldatei überein. Meta holt das Bild selbst von der URL — ein separater
Upload ist nicht nötig.

**Pflichtprüfung nach jedem `ads_create_ad`:** den `image_hash` des
erzeugten Creatives über `ads_get_creatives` auslesen und gegen die anderen
Ads vergleichen. Gleicher Hash bei verschiedenen Bildern = das Bild ist
nicht angekommen. Ein Erfolg im Response beweist nichts.

**Für Videos** bleibt nur: einmal per Drag & Drop in die Meta-Mediathek
(Ads Manager → Mediathek) legen, danach über `ads_get_ad_videos` per Titel
finden und die Video-ID im Creative referenzieren.

Bilder, die per Chat geschickt werden, landen **nicht** auf der Platte und
sind damit nicht verwertbar. Wenn sie mit Higgsfield erzeugt wurden, lassen
sie sich über `show_generations` anhand des Prompt-Textes wiederfinden —
die `results.rawUrl` ist eine öffentliche CDN-URL und genau das, was
`image_url` braucht. Der Sandbox-Proxy blockiert diesen CDN-Host allerdings,
die Bilder lassen sich also nicht herunterladen und visuell prüfen; die
Zuordnung läuft über den Prompt-Text und gehört vor dem Scharfschalten in
der Ads-Vorschau gegengeprüft.

Ein automatischer Umweg über die Shopify-Files-API ist hier **nicht**
möglich: `mcp__Shopify__graphql_mutation` steht in `.claude/settings.json`
auf `deny`.

## Adsets in „Plüschies 02.06.26": nur von Hand

Diese Kampagne lässt sich per API nicht um Adsets erweitern. Sie ist ABO,
Meta verlangt also ein Adset-Budget (`Ad Set Budget is Missing`, subcode
1885649) — aber die Vorabprüfung von `ads_create_ad_set` weist jedes
`daily_budget` mit „Parent campaign uses Campaign Budget Optimization
(CBO)" zurück. Die Erkennung ist falsch: die Kampagne hat kein
Kampagnenbudget, nur eine Gebotsstrategie auf Kampagnenebene.

`source_adset_id` hilft nicht — das Budget wird nicht mitkopiert. Ein
Update-Tool für Adsets existiert in diesem MCP-Server nicht.

`adset_spec` inline in `ads_create_ad` hilft ebenfalls nicht und ist die
gefährlichste der Sackgassen: das Feld wird ignoriert, die Ad landet im
Adset aus `ad_set_id`, und der Aufruf meldet trotzdem Erfolg und spiegelt
`adset_spec` im Response zurück. Wer das nicht nachprüft, hält eine Ad im
falschen Adset für ein neues Adset. **Nach jedem `ads_create_ad` die
tatsächliche `adset_id` der Ad abfragen.**

Betroffen sind genau die Kampagnen mit Gebotsstrategie auf Kampagnenebene
**ohne** Kampagnenbudget. Stand 27.08.2026:

| Kampagne | Adset anlegen |
|---|---|
| Plüschies 02.06.26 | ❌ |
| Fluffys 11.08.26 USA – Kopie | ❌ |
| Bottel of Funnel 21.08.2026 | ✅ |
| Fluffys 04.08.26 Uk | ✅ |
| CBO USA / CBO USA – Kopie | echtes CBO, Adsets ohne Budget |

Zwei Wege: **Adset von Hand im Ads Manager anlegen** und die ID durchgeben,
danach die Ads per API hineinbauen. Oder in eine Kampagne launchen, die
nicht betroffen ist — dort läuft alles vollautomatisch.

Für neue Kampagnen gilt: Gebotsstrategie **nicht** auf Kampagnenebene
setzen, sondern auf Adset-Ebene. Dann bleibt die Kampagne dauerhaft
beschreibbar. `ads_create_campaign` ohne `campaign_bid_strategy` und ohne
Kampagnenbudget aufrufen — so ist
`120252017271800270` (Plüschies USA Image Ads) angelegt und funktioniert.

## Schreibsperre des Kontos

Zu viele Schreibversuche in kurzer Zeit lösen bei Meta eine
Sicherheitsprüfung aus (`error_code 31`, subcode `3858385`,
„Please authenticate your account"). Danach ist Anlegen und Ändern gesperrt,
bis der Inhaber sich im Ads Manager verifiziert; laufende Ads sind nicht
betroffen. Am 27.08. genau so passiert.

Deshalb: **erst eine einzelne Ad anlegen und verifizieren, dann den Rest** —
nie fünf Creates parallel abfeuern, und Fehlversuche nicht in Serie
wiederholen.

## Autopilot: wo die Creatives liegen müssen

Der einzige echte Engpass für unbeaufsichtigte Launches ist die Herkunft
der Bilder. Was funktioniert und was nicht:

| Quelle | Nutzbar | Warum |
|---|---|---|
| Higgsfield-Generierung | ✅ | über `show_generations` auffindbar, `results.rawUrl` ist eine öffentliche URL |
| Shopify → Inhalte → Dateien | ✅ **empfohlen** | liefert eine `cdn.shopify.com`-URL |
| Beliebige öffentliche Direkt-URL | ✅ | wird direkt als `link_data.picture` gesetzt |
| Bild in den Chat gelegt | ❌ | landet nicht auf der Platte, es gibt keine URL |
| Google Drive / Dropbox / Canva | ❌ | liefern eine Login- oder Zwischenseite |
| Knight Vision | ✅ | `list_images` liefert `image_url` |

Am 27.08. konkret aufgetreten: sechs per Chat geschickte Motive waren weder
in Higgsfield noch in Knight Vision noch in Shopify Files und damit
unbrauchbar. Für Autopilot gilt deshalb: **Creatives gehören in Shopify
Files, Higgsfield oder Knight Vision — nicht in den Chat.**

### Shopify Files ist der vorgesehene Ablageort

Am 27.08. verifiziert. Die Dateien lassen sich lesend über
`mcp__Shopify__graphql_query` auflisten, inklusive öffentlicher CDN-URL:

```graphql
query GetFiles($first: Int!) {
  files(first: $first, sortKey: CREATED_AT, reverse: true) {
    edges { node { id alt createdAt
      ... on MediaImage { image { url width height } } } }
  }
}
```

`image.url` ist genau das, was `link_data.picture` braucht. Der Inhaber legt
die Motive per Drag & Drop unter Inhalte → Dateien ab, sonst nichts — kein
Verschicken, keine Links.

**Benennung ist Pflicht**, sonst ist die Zuordnung Motiv ↔ Headline nicht
maschinell möglich (die Bilder selbst kann der Sandbox-Proxy nicht laden).
Schema: `plushies-<land oder all>-<nummer>-<headline-stichwort>.png`, und
das `alt`-Feld mit der gewünschten Headline füllen. Dann kommen Ad-Name und
Headline direkt aus der Datei.

Der Rest des Ablaufs ist dann unbeaufsichtigt fahrbar: eine Routine weckt
eine Sitzung nach Zeitplan, die Sitzung liest die neuesten Generierungen,
gruppiert sie zu Fünferpaketen, legt pro Paket ein Adset je Land an und
baut die Ads hinein — alles pausiert, das Scharfschalten bleibt beim
Inhaber.

## Mehrländer-Struktur

Ein Land = eine Kampagne, damit Budget und Reporting sauber getrennt
bleiben und die Adset-Nummerierung pro Land durchläuft.

| Land | Kampagne |
|---|---|
| USA | `120252017271800270` — Plüschies USA Image Ads |
| AU | `120252017644050270` — Plüschies AU Image Ads |
| UK | `120252017649260270` — Plüschies UK Image Ads |

Creatives werden von Meta kontenweit dedupliziert: dieselbe Bild-URL und
derselbe Text ergeben in allen drei Ländern dieselbe `creative_id`. Der
Hash-Check muss deshalb nur einmal pro Motiv laufen, nicht pro Land.

## Budget im Blick behalten

Der Vollausbau ist grösser, als er im Einzelschritt wirkt. Stand
27.08.2026: 8 Adsets je Land × 3 Länder × £20 = **£480 pro Tag**, wenn
alles gleichzeitig läuft. Vor dem Scharfschalten gegenrechnen und im
Zweifel gestaffelt aktivieren — erst zwei Blöcke je Land, den Rest
nachziehen.

## Ablauf eines Launches

1. **Sammeln:** Creatives (Mediathek-Namen oder Direkt-URLs), Primary Text,
   Headline, CTA, Ziel-URL, Land, Budget pro Adset, Anzahl Adsets.
2. **Vorlage prüfen:** aktuelle Einstellungen des Vorlage-Adsets frisch
   auslesen, nicht aus diesem Dokument abschreiben — Meta ändert Defaults.
3. **Adsets anlegen** unter der Kampagne, ein Adset pro Land/Winkel.
4. **Creatives hochladen** bzw. aus der Mediathek referenzieren.
5. **Ads anlegen**, ein Ad pro Creative, in jedes passende Adset.
6. **Gegenprüfen:** Delivery-Fehler abfragen, bevor irgendwas scharf geht.
7. **Übergeben:** Liste der angelegten Adset- und Ad-IDs mit Namen — das
   Scharfschalten macht ein Mensch im Ads Manager.

Adsets und Ads werden von der API **immer pausiert** angelegt. Das ist
Absicht und lässt sich nicht umgehen: nichts gibt Geld aus, bevor es
jemand angesehen hat.

## Startzeit nachträglich ändern: geht nur von Hand

Der MCP-Server kann nur **anlegen**. Es gibt kein Update-Tool für Adsets,
also lässt sich `start_time` nach dem Anlegen per API nicht mehr
verschieben. Am 27.08. angefragt und geprüft: kein `ads_update_ad_set`,
kein Edit-Pfad, auch nicht über einen Umweg.

Der Weg im Ads Manager (schnell, weil Sammelbearbeitung geht):

1. Ads-Manager-Reiter **Anzeigengruppen** öffnen, auf die Kampagne filtern.
2. Alle Adsets der Kampagne über die Kopf-Checkbox markieren.
3. **Bearbeiten** → im Seitenbereich unter *Zeitplan* das neue Startdatum
   und die Uhrzeit setzen → auf alle markierten anwenden → veröffentlichen.
4. Für jede der drei Länder-Kampagnen einmal.

Zwei Dinge, die dabei oft verwechselt werden:

- Eine Startzeit **in der Vergangenheit** blockiert nichts. Das Adset
  startet dann einfach, sobald es aktiviert wird. Eine knappe Uhrzeit ist
  also kein Grund zur Eile — verpasst man sie, läuft es sofort los.
- Die Startzeit allein schaltet nichts scharf. Alles wird PAUSED angelegt
  und bleibt PAUSED, bis ein Mensch aktiviert.

Konsequenz fürs nächste Mal: **Startzeit vor dem Anlegen festzurren.**
Neu anlegen wäre die einzige API-Alternative — und würde die alten 24
Adsets samt 117 Ads als Handarbeit zum Löschen hinterlassen, also deutlich
mehr Aufwand als die Sammelbearbeitung oben.

## Massen-Launch: Batch-Verfahren für mehrere Länder

Bewährt am 27.08.2026 (39 Motive, 24 Adsets, 117 Ads, drei Länder in einem
Durchlauf). Ohne dieses Verfahren wird der Ablauf oben bei mehr als einer
Handvoll Ads unübersichtlich.

Aufteilung: Motive durchnummerieren und in Blöcke zu 5 schneiden. Jeder
Block wird ein Adset **pro Land**. Bleibt am Ende ein Rest, bekommt der
letzte Block weniger Ads — kein Grund, ein Motiv doppelt zu nehmen.

Je Block der immer gleiche Vierschritt:

1. **3 Adsets anlegen** (USA / AU / UK), identische Einstellungen bis auf
   `geo_locations.countries`.
2. **5 USA-Ads anlegen** mit vollem `object_story_spec` und dem Bild in
   `link_data.picture`.
3. **`creative_id` je Ad auslesen** — `ads_get_ad_entities`, Level `ad`,
   gefiltert auf `adset.id`, Feld `creative`.
4. **Je 5 Klon-Ads für AU und UK** mit `creative": {"creative_id": "…"}`.

Warum Klonen statt neu Anlegen: Meta dedupliziert Creatives kontoweit. Ein
Klon über `creative_id` zeigt garantiert dasselbe Bild wie das Original —
zweimal dieselbe URL zu schicken kann dagegen zwei Creatives erzeugen.
Nebenbei spart es zwei Drittel der Schreibaufrufe, was die Schreibsperre
(siehe unten) seltener auslöst.

Schritt 2 und 3 sind sequenziell — der `creative_id` existiert erst nach
dem Anlegen. Schritt 1 des nächsten Blocks lässt sich mit Schritt 3 des
laufenden bündeln.

### Pflicht-Gegenprüfung am Ende

- `ads_get_ad_entities` auf Level `adset`, gefiltert auf die Kampagnen:
  Anzahl, Budget, Startzeit, Status stimmen?
- `ads_get_ad_entities` auf Level `ad`: sind es so viele Ads wie geplant?
- `ads_get_creatives` mit allen neuen `creative_ids` und Feld `image_hash`:
  **alle Hashes müssen verschieden sein.** Gleiche Hashes über mehrere
  Motive heißt, das Bild ist nicht angekommen und Meta hat einen
  Fallback gesetzt.
- `ads_get_errors` über alle Kampagnen-IDs.

Was auf diesem Weg **nicht** prüfbar ist: ob Bild und Headline visuell
zusammenpassen. Der Sandbox-Proxy blockiert die Bild-CDNs. Die Zuordnung
kommt aus den Prompt-Texten der Generierung — ein Mensch muss vor dem
Scharfschalten einmal durch die Ads-Manager-Vorschau scrollen.

## Namensschema

Bestand im Konto ist uneinheitlich („– Kopie 2", „dupliziert 25.07.26").
Für neue Launches:

```
Adset:  <Winkel> <Land> <TT.MM.JJ>      z.B. "Knete Ad UK 27.08.26"
Ad:     <Creative-Name> <Land> <TT.MM.JJ>
```

## Copy-Warnung vor jedem Launch

Der Bestandstext der Vorlage-Ad wirbt mit „Anti-tear construction" und
„built for dogs who destroy everything". Genau diese Haltbarkeits-Aussage
ist in `docs/2026-07-18-backlog-triage.md` und
`docs/2026-07-19-backlog-triage.md` als offenes Geschäftsrisiko vermerkt:
mehrere Kundinnen und Kunden begründen ihre Erstattungsforderung damit,
dass das Produkt als „indestructible" beworben wurde, eine Person beruft
sich auf den UK Consumer Rights Act 2015.

Vor dem Übernehmen von Bestandstext in neue Ads einmal prüfen, ob die
Haltbarkeits-Formulierung noch so laufen soll. Das ist eine Entscheidung
des Inhabers, keine Sache dieses Runbooks — aber ungeprüft weiterkopieren
skaliert das Risiko mit dem Budget.

## Offene Punkte

- **Ziel-URL** ist in diesem Dokument noch nicht hinterlegt — die Creative-
  API gibt sie nicht flach zurück. Beim ersten Launch einmal nennen, dann
  hier eintragen.
- Landet ein Launch in einer **CBO**-Kampagne, gilt die Budget-Warnung oben.
