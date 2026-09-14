# Backlog-Triage 14.09.2026

Laufende Fristen, die an diesem Tag sichtbar bleiben müssen:

- **#6877 Alexander Meza** — selbst gesetzte 48-Stunden-Frist (FTC, Meta,
  Chargeback) läuft **15.09. 12:38 UTC** ab.
- **#7699 Lorraine Sale** — selbst gesetztes Datum **17.09.**

---

## Lauf 01:20 UTC — zwei Neukontakte, beide mit dem Wort „indestructible"

Seit dem letzten Eintrag (13.09. 22:20) sind zwei neue Erstkontakte
eingegangen. **Beide sind Kauschaden, beide berufen sich wörtlich auf
„indestructible".** Das ist genau das Wort, das am 12.09. gegen die
Produktbeschreibung geprüft wurde und **dort kein einziges Mal vorkommt**.

### #7030 — Jordan Hauler (`jhauler0317@gmail.com`), 14.09. 00:42 UTC

Betreff: „My order". Keine Bestellnummer in der Mail; über die
E-Mail-Suche in Shopify eindeutig zugeordnet.

- Bestellung **21.08.**, Versand **02.09.** — **12 Tage bis zum Versand**
- **28,51 £**, bezahlt, FULFILLED
- **Zwei** Plushies: Variante *donkey* und Variante *monkey*
- Yanwen Special Line US (Including taxes), `UL476304250YP`

Wortlaut: *„I saw all the reviews and things you post about your items being
indestructible and yet within an hour of my dogs having your items they tore 1
of them completely apart. I took away the other one i bought so they wouldn't
rip that apart as well but what can you do for me as you claim they are for
heavy chewers yet they didn't stand a chance?"*

Drei Punkte, die hier festzuhalten sind:

1. **Er nennt als Quelle „the reviews and things you post"** — also nicht die
   Produktseite, sondern Bewertungen und Veröffentlichtes. Die
   Produktbeschreibung wurde am 12.09. geprüft; **„indestructible" steht dort
   nicht.** Wo er es gelesen hat, **kann der Bot nicht feststellen** — die
   Anzeigentexte waren nie einsehbar (Meta-Ads-Prüfung am 11.09. abgebrochen,
   nur die Existenz des Werbekontos „Uk 1" belegt). **Das ist eine
   Owner-Prüfung.**
2. **„you claim they are for heavy chewers"** — in der geprüften Beschreibung
   steht *„Anti-tear design built for **strong** chewers"*. **Sinngemäss
   deckungsgleich, im Wortlaut nicht.**
3. Er hat **das zweite Spielzeug weggenommen und nicht benutzt.** Das ist
   sachlich festzuhalten, weil die Vorlage sich auf „unbenutzt" stützt —
   **eine Zusage wird daraus hier ausdrücklich nicht abgeleitet**, weil der
   Bot die Fundstelle für diese Bedingung bis heute nicht belegen kann.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage („indestructible", „heavy
chewers"), Berufung auf veröffentlichte Bewertungen.
**Nicht auf der Erstattungsliste** — kein Regelfall. Er stellt ausserdem keine
bezifferte Forderung, sondern fragt offen *„what can you do for me"*.

### #4822 — Melody Clement (`jclement959@yahoo.com`), 14.09. 00:28 UTC

Antwort auf die Shopify-Versandbenachrichtigung.

- Bestellung **06.08.**, Versand **22.08.** — **16 Tage bis zum Versand**,
  passt in das August-Muster (#4726/#4745/#5032: 16–17 Tage)
- **20,35 £**, bezahlt, FULFILLED
- Ein Plushie, Variante *donkey*
- Yun Express US (selected postal codes), `YT2623400701617537`
- Lieferadresse Pasadena, Texas

Wortlaut: *„I gave my dog his toy a week ago and it is now torn up, missing a
leg and ear, they are not indestructible. I believe I should get a refund
please. I can send a picture if needed."*

Sie beschwert sich **nicht** über die Versanddauer — die 16 Tage werden hier
nur der Vollständigkeit halber vermerkt und **in der Antwort nicht von sich
aus angesprochen**.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage („indestructible"), ausdrückliche
Erstattungsforderung.
**Nicht auf der Erstattungsliste** — kein Regelfall (Kauschaden).

### Was das für die Zählung bedeutet

**Mit #7030 und #4822 sind es jetzt zehn Kundinnen und Kunden binnen fünf
Tagen, die die Haltbarkeitswerbung ausdrücklich angreifen** — nach #7060,
#5851, #7292, #5436, #7034, #7608, becca23047, #4939.

**Neu ist die Wortwahl:** #7030 und #4822 benutzen beide **wörtlich
„indestructible"**. Bisher hatten Kundinnen und Kunden die Garantie
sinngemäss wiedergegeben; hier steht zweimal dasselbe Wort, das **in der
Produktbeschreibung nachweislich fehlt**. Zwei unabhängige Personen in
vierzehn Minuten mit demselben Wort — **der Bot zieht daraus keinen Schluss
über die Quelle**, hält aber fest, dass es eine geben muss, die nicht die
geprüfte Produktbeschreibung ist.

**Kein Vorlagenversand.** Beide Fälle erfüllen einen Eskalationsauslöser;
nach der Anweisung ist darauf **ehrlich und unverbindlich** zu antworten,
nicht mit einer Vorlagen-Absage. Die zweiundzwanzig Kauschaden-Absagen seit
dem 11.09. haben **ausnahmslos** zu einer Eskalation geführt — das ist der
Grund, diese beiden nicht in dieselbe Schiene zu geben.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`: **#7030 Jordan Hauler**,
**#4822 Melody Clement**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, das Wort
„indestructible" **in keinem der beiden Entwürfe verwendet**, keine Fundstelle
für die Garantiebedingung erfunden, keine Rücksendeadresse genannt, keine
rechtliche Einordnung vorgenommen, kein Label gesetzt (Label-Werkzeug weiter
blockiert), **kein Entwurf in Gmail angelegt** — `create_draft` bleibt nach 21
Fehlschlägen ausgesetzt.

---

## Lauf 04:20 UTC — #7673, und die Frage, die sich nicht mehr umgehen lässt

### #7673 — Michelle Barnes (`jjmbarnes15@gmail.com`), 14.09. 03:58 UTC

Betreff: „Refund Request - Order #7673". Bestellnummer selbst genannt, in
Shopify bestätigt.

- Bestellung **25.08.**, Versand **03.09.** — **9 Tage bis zum Versand**
- **20,35 £**, bezahlt, FULFILLED
- Ein Plushie, Variante **Duck**
- WB US (Selected postal codes), `WNBAA0498036347YQ`
- Lieferadresse Durham, North Carolina

Wortlaut: *„I received the below order and it was destroyed by my daughter's
dog within five minutes. I would like to request a full refund. Please see
attached picture of the destroyed duck."*

**Ein Foto liegt bei** (`DC3DFB3C-…jpeg`). Der Bot hat den Bildinhalt **nicht
geöffnet und beurteilt ihn nicht** — festgehalten wird nur, dass ein Beleg
mitgeschickt wurde.

### Einstufung — und warum sie diesmal begründet wird

Sie zitiert **kein** Verbraucherrecht, droht **keine** Bewertung an, ist
**Erstkontakt**, nennt **kein** Sicherheitsproblem und greift die Werbung
**nicht ausdrücklich** an. **Nach der Liste der Eskalationsauslöser ist das
keiner.** Formal ist es der Regelfall Kauschaden.

Trotzdem geht der Fall **nicht** mit der Vorlagen-Absage hinaus, und der Grund
gehört ins Protokoll:

**Das Produkt, das sie gekauft hat, heisst im Shop wörtlich „Plushies –
Designed for Furry Friends Who Destroy Everything".** Dieser Titel steht in
der Bestellung, in der Versandbenachrichtigung und in ihrer eigenen Mail —
er ist **aus Shop-Daten belegt**, nicht behauptet. Einer Kundin, deren Hund
das Spielzeug in fünf Minuten zerstört hat, mit „Kauschaden ist nicht gedeckt"
zu antworten, heisst, ihr den Namen des Produkts entgegenzuhalten, den der
Shop selbst vergeben hat.

**Zweiundzwanzig Vorlagen-Absagen seit dem 11.09., und jede beantwortete hat
eskaliert.** Der Bot leitet daraus keine Regeländerung ab — die Regel ist
Sache des Owners. Er legt den Fall aber als **`Bot/Needs Approval`** vor
statt ihn selbst abzuschliessen, weil eine Absage hier eine Entscheidung
wäre, die er nicht zu treffen hat.

→ `Bot/Needs Approval`.
**Nicht auf der Erstattungsliste** — kein Regelfall. **Die Erstattung wird im
Entwurf weder zugesagt noch abgelehnt.**

### Entwürfe

Volltext in `docs/entwuerfe-zum-kopieren.md`: **#7673 Michelle Barnes**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, nicht
behauptet, die Garantie decke oder decke nicht — sondern offengelegt, dass
die Bedingung nicht belegbar ist; das Foto nicht bewertet; keine
Rücksendeadresse genannt; keine rechtliche Einordnung; kein Label gesetzt;
**kein Entwurf in Gmail angelegt**.
