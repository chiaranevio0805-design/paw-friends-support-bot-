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

Das ist der einzige echte Engpass. Der Upload akzeptiert:

| Weg | Video | Bild |
|---|---|---|
| Öffentliche Direkt-URL (Shopify-CDN, S3, eigener Server) | ✅ | ✅ |
| Liegt schon in der Meta-Mediathek des Kontos | ✅ | ✅ |
| Datei vom Rechner über Upload-Fenster | ❌ | ✅ (JPEG/PNG/GIF) |
| Google Drive / Dropbox / Canva-Freigabelink | ❌ | ❌ |

Drive- und Dropbox-Links liefern eine Login- bzw. Zwischenseite statt der
Datei — der Upload schlägt fehl, auch wenn der Link auf „jeder mit dem
Link" steht.

**Empfohlener Weg für Videos:** einmal per Drag & Drop in die Meta-Mediathek
(Ads Manager → Mediathek) legen und die Dateinamen durchgeben. Von dort
werden sie ohne Upload direkt in die Ads übernommen.

Ein automatischer Umweg über die Shopify-Files-API ist hier **nicht**
möglich: `mcp__Shopify__graphql_mutation` steht in `.claude/settings.json`
auf `deny`.

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
