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
| `image_url` direkt im Creative-Spec der Ad | ❌ | ✅ |
| Liegt schon in der Meta-Mediathek (per Hash/ID referenzieren) | ✅ | ✅ |
| `ads_creative_upload_media`, `upload_source: URL` | ❌ | ❌ |
| `ads_creative_upload_media`, `upload_source: LOCAL_FILE` | ❌ | ❌ |
| Google Drive / Dropbox / Canva-Freigabelink | ❌ | ❌ |

Beide Upload-Wege sind für dieses Konto zu: LOCAL_FILE ist deaktiviert
(„Local file upload is not available for ad account"), und der URL-Upload
ist noch nicht ausgerollt („This tool is new and is being gradually rolled
out"). Ein separates `ads_creative_upload_image` gibt es in diesem
MCP-Server nicht.

**Was trotzdem funktioniert:** `image_url` direkt im Creative-Spec von
`ads_create_ad` mitgeben — Meta holt das Bild selbst und legt den Hash an.
Der Upload-Schritt entfällt damit komplett. Gilt nur für Bilder.

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

Ablauf deshalb: **Adset von Hand im Ads Manager anlegen** (oder ein
bestehendes duplizieren und Land, Budget, Name anpassen), Adset-ID
durchgeben, danach die Ads per API hineinbauen. Vor jedem Launch einmal neu
testen, ob die Vorabprüfung inzwischen korrigiert wurde.

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
