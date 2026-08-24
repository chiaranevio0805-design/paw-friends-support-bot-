# Backlog-Triage 2026-08-21

Lauf verspätet ausgeführt: der Connector (Gmail/Shopify) war am 21.08. und
weite Teile des 22.08. nicht durchgehend erreichbar, und der Worker-Prozess
wurde wiederholt mitten im Lauf neu gestartet. Die Shopify-Daten unten sind
verifiziert (Stand 23.08. 06:17 UTC nachgeprüft); die Gmail-Entwürfe waren zum
Zeitpunkt dieses Eintrags **noch nicht angelegt** — siehe „Offen" am Ende.

## Neue Fälle

### #6870 — Mary Jacobs — Stornierung vor Versand

- **Absender:** todd.jacobsw@gmail.com (20.08., 21:51 UTC), Betreff „Order Cancel"
- **Bestellung läuft auf:** marypowerjacobs@gmail.com
- **Shopify:** #6870, angelegt 20.08. 21:15 UTC, **PAID / UNFULFILLED**,
  `totalPrice` **£45,95**, Versandziel El Dorado Hills, Kalifornien
- **Positionen:** Zahnbuddy (Blue Mop Plush Dog), Plushies fox, Plushies hippo
- **Klassifikation:** Regel 3 — vor Versand storniert. Voller Betrag zurück,
  ohne Diskussion.
- **Hinweis:** Der Kunde nennt „$62.64", Shopify führt £45,95. Nicht dieselbe
  Zahl — im Entwurf deshalb **kein Betrag**, nur „der volle gezahlte Betrag".
- **Kategorie:** `Bot/Needs Approval`
- **Owner-Aktion:** #6870 in Shopify **stornieren *und* erstatten**, in dieser
  Reihenfolge (siehe support-policy.md — eine reine Erstattung stoppt den
  Versand nicht).

### #6905 — Wendy Higgins — Stornierung vor Versand

- **Absender:** usfmom02@gmail.com (21.08., 02:50 UTC), Betreff „Cancel order",
  ohne Bestellnummer. Über die E-Mail-Adresse in Shopify zugeordnet: nur eine
  Bestellung vorhanden.
- **Shopify:** #6905, angelegt 21.08. 01:49 UTC, **PAID / UNFULFILLED**,
  `totalPrice` **£28,52**, Versandziel Port Richey, Florida
- **Positionen:** Plushies fox, Plushies frog
- **Klassifikation:** Regel 3 — vor Versand storniert.
- **Kategorie:** `Bot/Needs Approval`
- **Owner-Aktion:** #6905 stornieren *und* erstatten.

### #3310 — Timothy Carroll — Chargeback eingereicht

- **Absender:** tcarroll@cadvanced.com (20.08., 21:18 UTC), im Thread
  „Re: A shipment from order #3310 is on the way"
- **Wortlaut:** „Your ad stated that your toys couldn't be torn apart by a dog
  OR YOUR MONEY BACk. **I already disputed this charge with my cc company**"
- **Shopify:** #3310, 24.07., £35,64, PAID / PARTIALLY_FULFILLED, versandt
  29.07. (RD Express RD1025823949HM), Crossville, Tennessee
- **Eskalationsgrund:** Zwei Trigger gleichzeitig — Chargeback bereits
  eingereicht (Kreditkartenanbieter) und ausdrücklich bestrittene
  Werbeaussage. Zusätzlich vierter Kontakt im selben Fall.
- **Kategorie:** `Bot/Escalated - Owner Attention`
- **Kauschaden — fällt NICHT unter die Erstattungsregel.** Gehört nicht auf
  die Erstattungsliste. Was hier ansteht, ist eine Owner-Entscheidung zum
  Chargeback, keine Kulanzerstattung durch den Bot.

## Befund: zwei Vorlagen-Absagen sind bereits rausgegangen

Der Thread #3310 enthält zwei `SENT`-Nachrichten, die **nicht** aus einem
Bot-Lauf stammen:

- 19.08. 08:46 UTC — „Our returns policy states that damage…"
- 20.08. 20:27 UTC — „We're sorry that you're so disappointed…"

Beide sind Vorlagen-Absagen an einen Kunden, der zu diesem Zeitpunkt bereits
die Werbeaussage bestritten und mit dem Kreditkartenanbieter gedroht hatte.
Genau das schließt die Policy für Eskalationsfälle aus („honest non-committal
reply, **not a template denial**"). Der Chargeback kam 51 Minuten nach der
zweiten Absage.

## Offen (zum Zeitpunkt dieses Eintrags)

Die drei Entwürfe waren wegen der Connector-Ausfälle **noch nicht angelegt**.
Sie sind der nächste Schritt; bis dahin gilt für den Abend-Report:
**Volltext nicht im Log — vor dem Senden in Gmail-Entwürfen prüfen.**
