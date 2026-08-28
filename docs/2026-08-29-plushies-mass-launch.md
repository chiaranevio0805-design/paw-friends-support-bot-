# Launch 29.08.2026 02:30 — 150 Higgsfield-Motive × 3 Länder

Erstellt am 28.08.2026 aus allen Higgsfield-Generierungen ab **18:13 UTC**
(= 20:13 Uhr Ortszeit, die vom Kunden gesetzte Grenze "erst ab 8:13 p.m.").
Die älteren Motive mit grünem Hintergrund von 02:40 Uhr sind bewusst **nicht** enthalten.

## Eckdaten

| | |
|---|---|
| Motive | 150, sortiert nach Higgsfield-`createdAt` (Erstellungsreihenfolge) |
| Aufteilung | 5 Motive je Adset → 30 Adsets pro Land |
| Länder | USA, Australien, UK → **90 Adsets, 450 Ads** |
| Tagesbudget | £20 pro Adset (ABO) = £1.800/Tag bei Vollaktivierung |
| Start | 2026-08-29T02:30:00+02:00 |
| Status bei Anlage | alle PAUSED (API legt zwingend pausiert an) |
| Optimierung | OFFSITE_CONVERSIONS / IMPRESSIONS / LOWEST_COST_WITHOUT_CAP |
| Pixel | 1311406010460496, Event PURCHASE |
| Page | 1147503868444857 |
| Targeting | Land + home/recent, 18–65, Advantage+ Audience an |
| Ausschluss | Custom Audience 120250751148250270 (Käufer) |
| Attribution | 7 Tage Klick + 1 Tag View |
| CTA | ORDER_NOW → Produktseite cross-border-new-pet-plush-… |

## Kampagnen (dieselben wie am 27./28.08.)

| Land | Kampagne | ID |
|---|---|---|
| USA | Plüschies USA Image Ads | `120252017271800270` |
| AU  | Plüschies AU Image Ads  | `120252017644050270` |
| UK  | Plüschies UK Image Ads  | `120252017649260270` |

## Adset-IDs

Motiv-Nummern beziehen sich auf die Erstellungsreihenfolge in Higgsfield.

| Adset | Motive | USA | AU | UK |
|---|---|---|---|---|
| S01 | 001–005 | `120252068427460270` | `120252068680220270` | `120252068710810270` |
| S02 | 006–010 | `120252068428300270` | `120252068680680270` | `120252068711390270` |
| S03 | 011–015 | `120252068429250270` | `120252068681550270` | `120252068711980270` |
| S04 | 016–020 | `120252068430050270` | `120252068682310270` | `120252068712410270` |
| S05 | 021–025 | `120252068430860270` | `120252068683510270` | `120252068713010270` |
| S06 | 026–030 | `120252068431620270` | `120252068684410270` | `120252068714560270` |
| S07 | 031–035 | `120252068435520270` | `120252068684950270` | `120252068715340270` |
| S08 | 036–040 | `120252068436370270` | `120252068686550270` | `120252068716770270` |
| S09 | 041–045 | `120252068437450270` | `120252068687600270` | `120252068717260270` |
| S10 | 046–050 | `120252068438640270` | `120252068688240270` | `120252068717660270` |
| S11 | 051–055 | `120252068439470270` | `120252068689190270` | `120252068718950270` |
| S12 | 056–060 | `120252068440640270` | `120252068689620270` | `120252068719720270` |
| S13 | 061–065 | `120252068444430270` | `120252068690210270` | `120252068720530270` |
| S14 | 066–070 | `120252068445500270` | `120252068690960270` | `120252068721410270` |
| S15 | 071–075 | `120252068446300270` | `120252068691900270` | `120252068722100270` |
| S16 | 076–080 | `120252068446890270` | `120252068692510270` | `120252068722460270` |
| S17 | 081–085 | `120252068448240270` | `120252068693680270` | `120252068722960270` |
| S18 | 086–090 | `120252068448910270` | `120252068694490270` | `120252068727650270` |
| S19 | 091–095 | `120252068454280270` | `120252068695190270` | `120252068728450270` |
| S20 | 096–100 | `120252068454940270` | `120252068695870270` | `120252068729330270` |
| S21 | 101–105 | `120252068456610270` | `120252068699010270` | `120252068731130270` |
| S22 | 106–110 | `120252068457120270` | `120252068700290270` | `120252068731510270` |
| S23 | 111–115 | `120252068457750270` | `120252068701490270` | `120252068732040270` |
| S24 | 116–120 | `120252068458400270` | `120252068702860270` | `120252068732810270` |
| S25 | 121–125 | `120252068459830270` | `120252068703270270` | `120252068733730270` |
| S26 | 126–130 | `120252068460510270` | `120252068703660270` | `120252068734900270` |
| S27 | 131–135 | `120252068461070270` | `120252068704540270` | `120252068735720270` |
| S28 | 136–140 | `120252068461580270` | `120252068705100270` | `120252068737380270` |
| S29 | 141–145 | `120252068462050270` | `120252068705810270` | `120252068738090270` |
| S30 | 146–150 | `120252068462550270` | `120252068708040270` | `120252068738610270` |
## Aufbau-Verfahren

1. 30 USA-Adsets anlegen.
2. 150 USA-Ads mit `link_data.picture` (Higgsfield-CloudFront-URL) — das ist der
   einzige Weg, der zuverlässig das richtige Bild zieht; `image_url` auf
   Creative-Ebene wird still ignoriert.
3. 30 AU- und 30 UK-Adsets anlegen.
4. Die 150 USA-`creative_id`s per `ads_get_ad_entities` (level=ad, campaign-Filter)
   auslesen und als `{"creative_id":"…"}` nach AU und UK klonen. Meta dedupliziert
   Creatives kontenweit, deshalb ist Klonen sauberer als erneutes Hochladen.

## Verifikation

- 450/450 `ads_create_ad`-Aufrufe erfolgreich, alle mit Status PAUSED.
- 150 `creative_id`s eindeutig, keine Duplikate, keine Lücken (001–150).
- `ads_get_errors` über alle drei Kampagnen: leer.
- Stichprobe Adset S01 USA: 5 verschiedene `image_hash`, keiner davon der
  bekannte Fallback-Hash `5142c41441073142e2e341d5fe8dc647`.
- Alle 90 Adsets: £20/Tag, Start 2026-08-29T01:30+0100 (= 02:30 MESZ), PAUSED.

## Offen — muss von Hand erledigt werden

**Aktivieren.** Die Meta-Ads-Tools in dieser Session können nur anlegen und lesen;
es gibt kein Tool für Statuswechsel. Jedes Adset und jede Ad wird zwingend PAUSED
angelegt. Zum Scharfschalten pro Kampagne alles markieren und den Toggle umlegen:

- USA: https://www.facebook.com/adsmanager/manage/adsets?act=2479996745858211&selected_campaign_ids=120252017271800270
- AU:  https://www.facebook.com/adsmanager/manage/adsets?act=2479996745858211&selected_campaign_ids=120252017644050270
- UK:  https://www.facebook.com/adsmanager/manage/adsets?act=2479996745858211&selected_campaign_ids=120252017649260270

Wichtig: Adset **und** Ad müssen auf ON stehen, sonst liefert nichts aus.

**Bildkontrolle.** Ob Bild und Headline inhaltlich zusammenpassen, konnte nicht
geprüft werden — der Sandbox-Proxy blockiert das CloudFront-CDN. Die Zuordnung
beruht auf dem Higgsfield-Prompt-Text, nicht auf dem gerenderten Bild.

**Budget.** 90 Adsets × £20 = £1.800/Tag. Dazu die 24 Adsets vom 27./28.08. mit
£480/Tag, von denen ein Teil bereits ACTIVE ist. Bei Vollaktivierung also bis zu
£2.280/Tag.
