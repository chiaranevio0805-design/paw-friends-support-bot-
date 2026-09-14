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

---

## Lauf 07:20 UTC — #5032, und ein Fehler in der eigenen Suche

### Zuerst die Korrektur

**Die Meldungen „nichts Neues" um 05:20 und um 06:20 waren falsch.**

Adam Murgatroyds Antwort ist am **14.09. um 04:31 UTC** eingegangen. Sie lag
damit **in beiden Suchfenstern** und ist in **beiden Läufen nicht
aufgetaucht**: `in:inbox newer_than:2h` lieferte um 05:20 nur #7673 und um
06:20 gar nichts. Erst die Suche über `newer_than:1d` in diesem Lauf hat sie
sichtbar gemacht — und dieselbe `newer_than:2h`-Suche, die sie um 06:20
verschwiegen hat, liefert sie jetzt um 07:20, **obwohl 04:31 dann längst mehr
als zwei Stunden zurückliegt**.

**Damit ist `newer_than:Nh` als Grundlage für den Stundenlauf unbrauchbar.**
Gmail dokumentiert für `newer_than` die Einheiten `d`, `m`, `y` — Stunden
nicht. Was zurückkommt, ist weder ein sauberes Zeitfenster noch
reproduzierbar. Der Fall hier hat **drei Stunden** gekostet, bei einer
Verbraucherrechts-Zuschrift.

**Änderung des Vorgehens ab sofort:** Der Stundenlauf sucht mit
`in:inbox newer_than:1d` und gleicht gegen das ab, was im Tagesprotokoll
bereits steht, statt sich auf ein Stundenfenster zu verlassen. Das ist
teurer und dafür vollständig.

**Abgleich für die letzten 24 Stunden nachgeholt:** Ausser #5032 gibt es
seit dem letzten protokollierten Lauf (13.09. 22:20) **keine weitere
übersehene Zuschrift** — #7673, #7030 und #4822 sind erfasst, alles Übrige
ist auf dem Stand vom 13.09. 21:56 oder älter.

### #5032 — Adam Murgatroyd (`acmurgatroyd1@gmail.com`), 14.09. 04:31 UTC

Antwort auf die Vorlagen-Absage vom 13.09. 20:12. **Zeitabstand: 8 Stunden
19 Minuten.**

- Bestellung **08.08.**, Versand **25.08.** — **17 Tage bis zum Versand**
- **42,90 £**, bezahlt, FULFILLED, Tags `Kaching Bundles`, `UpCart Rewards`
- Drei Positionen: Zahnbuddy (Blue Mop Plush Dog) sowie zwei Plushies,
  *frog* und *pig*
- Yanwen Special Line Promotion, `UL451107611YP`
- **Lieferadresse West Kilbride, Schottland — Vereinigtes Königreich**

**Die Einzelpreise summieren sich auf 54,85 £, bezahlt wurden 42,90 £**
(Kaching-Bundle). Nach der stehenden Regel wird **kein Anteil je Position
geschätzt**; was auf eine einzelne Position entfällt, ist im Shopify-Admin
zu bestimmen.

Wortlaut: *„Under the Consumer Rights Act 2015 in the UK, goods that are
supplied that arent fit for purpose or last a reasonable length of time are
entitled to a refund. These toys are described as \"designed for everything\"
and your 30 day money back guarantee is misleading, as them being unopened
and unused is simply a basic consumer right, not for consumers to test your
product and a statement of your confidence in the quality of them. These
toys lasting a whole 30 minutes before being ripped apart is not \"designed
for everything\"."*

Drei Punkte:

1. **Er ist im Vereinigten Königreich ansässig.** Bei #5829 und #6781 war das
   ebenfalls so. Der Bot nimmt **keine rechtliche Einordnung** vor — er hält
   nur fest, dass die Voraussetzung, unter der die Frage überhaupt gestellt
   wird, hier sachlich zutrifft und die Zuschrift deshalb nicht als
   Missverständnis abgetan werden kann.
2. **„designed for everything"** ist seine Kurzform für den Produkttitel
   **„Plushies – Designed for Furry Friends Who Destroy Everything"**. Der
   Titel steht in seiner Bestellung und in der Versandbenachrichtigung —
   **aus Shop-Daten belegt.**
3. **Sein Einwand gegen die Garantie ist der schärfste bisher formulierte:**
   dass eine Geld-zurück-Garantie, die nur für ungeöffnete und unbenutzte
   Ware gilt, kein Vertrauensbeweis sei, sondern nur das ohnehin bestehende
   Widerrufsrecht wiederhole. **Das ist die fünfte unabhängige Fassung
   desselben Konstruktionsvorwurfs** — nach #7101, #7316, #6891 und #7292.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** Berufung auf den Consumer Rights Act 2015; bestrittene
Werbeaussage; Wiederkontakt nach Vorlagen-Absage.
**Nicht auf der Erstattungsliste** — kein Regelfall nach der geltenden Regel,
und der Betrag je Position ist ohne Admin nicht bestimmbar.

### Stand der Vorlagen-Absagen

**Dreiundzwanzig Kauschaden-Absagen seit dem 11.09.** Mit #5032 sind
**alle** beantworteten eskaliert — die Quote ist unverändert
ausnahmslos. **Zwei ausdrückliche Berufungen auf den Consumer Rights Act
2015** (#5829, #5032), eine dritte mit derselben Formulierung ohne
Gesetzesnennung (#6781).

### Entwürfe

Volltext in `docs/entwuerfe-zum-kopieren.md`: **#5032 Adam Murgatroyd**.

**Nicht getan:** keine rechtliche Einordnung und keine Stellungnahme dazu, ob
der Consumer Rights Act hier greift; keine Erstattung zugesagt oder
abgelehnt; kein Anteil je Position geschätzt; keine Fundstelle für die
Garantiebedingung erfunden; keine Rücksendeadresse genannt; kein Label
gesetzt; **kein Entwurf in Gmail angelegt**.

---

## Lauf 08:20 UTC — #6936 nennt es Betrug, #7657 fragt nur nach dem Paket

Erster Lauf nach dem umgestellten Suchverfahren (`newer_than:1d` plus
Abgleich gegen das Tagesprotokoll). **Zwei neue Zuschriften, beide um
07:30–07:34.**

### 🚩 #6936 — Lisa Steggel (`lisac131@googlemail.com`), 14.09. 07:34 UTC

Antwort auf die Vorlagen-Absage vom 13.09. 20:10. **Abstand: 11 Stunden
24 Minuten.**

- Bestellung **21.08.**, Versand **02.09.** — **12 Tage bis zum Versand**
- **27,95 £**, bezahlt, FULFILLED, Tag `Kaching Bundles`
- Zwei Plushies: *monkey* und *donkey*
- Yanwen Special Line Promotion, `UL476302846YP`
- Lieferadresse Bristol, England — **Vereinigtes Königreich**
- **Im Shop steht sie als `LisaC131@gmail.com`**, geschrieben hat sie von
  `lisac131@googlemail.com` — das ist der Fall vom 12.09., an dem die
  exakte `email:`-Suche gescheitert war.

Wortlaut:

> „Oh dear that's not very good customer service is it. **You claim no dog
> has beaten it and that it is durable, what an out and out lie. False
> advertising.** Why would I spend £30 on something he destroyed in less than
> an hour! I should've gone to the pound shop and had the same results.
> **Disgraceful false advertising. Ripped off. Stop lying, to sell your poor
> quality products. I'll make sure nobody else falls for this.**"

Zwei Punkte:

1. **„You claim no dog has beaten it"** ist eine **neue** Formulierung. In der
   am 12.09. geprüften Produktbeschreibung steht sie **nicht** — weder
   wörtlich noch sinngemäss. Damit steht sie in derselben Reihe wie
   „indestructible" (#7030, #4822) und „the stuffing won't come out"
   (#4939): **Zusagen, die Kundinnen und Kunden zitieren und die im
   geprüften Beschreibungsfeld fehlen.** Woher sie stammen, ist von hier aus
   **nicht feststellbar**.
2. **„I'll make sure nobody else falls for this"** ist eine angekündigte
   öffentliche Verbreitung. Zusammen mit dem dreimal erhobenen Vorwurf der
   Lüge ist das der Eskalationsauslöser.

**Zum Betrag:** Sie schreibt von 30 £; bezahlt wurden **27,95 £**
(Kaching-Bundle, Einzelpreise 2 × 29,95 £). **Kein Anteil je Position
geschätzt.** Die Abweichung wird in der Antwort **nicht aufgegriffen** — sie
zu korrigieren wäre hier kleinlich und ginge am Anliegen vorbei.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** Vorwurf irreführender Werbung, angekündigte öffentliche
Verbreitung, Wiederkontakt nach Vorlagen-Absage.
**Nicht auf der Erstattungsliste** — kein Regelfall nach der geltenden Regel.

### #7657 — John Furlong (`johnfurlong.66@btinternet.com`), 14.09. 07:30 UTC

Betreff: „Re order Order #7657". Vollständiger Text: *„Can you please tell me
where my order is"*.

- Bestellung **24.08.**, Versand **03.09.** — **10 Tage bis zum Versand**
- **27,95 £**, bezahlt, FULFILLED, Tag `Kaching Bundles`
- Zwei Plushies: *fox* und *Duck*
- Yanwen Special Line Promotion, `UL478624336YP`
- Lieferadresse Sittingbourne, England

**Keine Forderung, keine Beschwerde, kein Eskalationsauslöser.** Er fragt nach
dem Verbleib seiner Bestellung, und **die Auskunft liegt vollständig vor**:
Versanddatum, Zusteller, Sendungsnummer, Trackinglink.

**Das ist der achte Fall, in dem eine zurückgehaltene Sendungsnummer die
ganze Anfrage ausmacht** — nach #7525, #7547, #7190, #4726, #7627, #7119 und
#6835. Einer davon hatte in eine Chargeback-Drohung geführt, die mit einer
Zeile zu erledigen gewesen wäre.

→ `Bot/Draft Ready`. **Keine Owner-Entscheidung nötig.** Sagbar sind
Versanddatum, Zusteller, Nummer und Link. **Nicht gesagt wird**, er möge sich
an den Zusteller wenden.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`: **#6936 (zweite Fassung)**,
**#7657**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, **die Formulierung „no dog has beaten it" weder bestätigt noch
bestritten**, keine rechtliche Einordnung, kein Anteil je Position geschätzt,
die Betragsabweichung nicht aufgegriffen, kein Verweis auf den Zusteller,
keine Rücksendeadresse, kein Label gesetzt, **kein Entwurf in Gmail angelegt**.

---

## Lauf 10:20 UTC — 🚩🚩 #1998: ein Rückruf, zugesagt am 17. Juli

### #1998 — Alexandra Bizzios-O'Connell (`alexbizoc@icloud.com`), 14.09. 09:25 UTC

Betreff: „Re: Recent order - second email sent".

- Bestellung **17.06.**, Versand **25.06.** — 8 Tage bis zum Versand
- **24,95 £**, bezahlt, FULFILLED
- Zwei Plushies: *pig* und *elephant*
- **CNE Express(ECO)**, `3A5V734103582` — **elfter Zusteller**, bisher nicht
  gesehen
- Lieferadresse Aldershot, England — Vereinigtes Königreich
- Im Shop steht sie als **Alexandra Bizzios-O'Connell**, identisch mit der
  Unterschrift — keine Namensunsicherheit

### Der Ablauf, vollständig aus dem Thread belegt

| Datum | Ereignis |
|---|---|
| **02.07.** | Erstkontakt. Ein Plushie „destroyed within a very short time frame", **Foto mit Zeitstempel** beigelegt. Bittet um volle Erstattung, *„have not met my needs or lived up to their description of being durable and hard wearing"*. |
| **06.07.** | Zweite Mail: *„I am contacting you again following no reply to my first email sent last week."* |
| **17.07.** | **Antwort des Shops.** Entschuldigung für die ausgebliebene Antwort — und: *„I have passed your refund request directly to our **Resolutions Team** who will be in contact with you shortly."* |
| **14.09.** | *„I am still waiting to be contacted by your resolutions team almost two months after the date of your last email. I have not been contacted and I have not yet received a refund."* |

**Erstkontakt vor 74 Tagen. Die Zusage eines Rückrufs liegt 59 Tage
zurück.**

### Was hier genau zugesagt wurde — und was nicht

**Zugesagt wurde ein Rückruf durch ein „Resolutions Team", nicht die
Erstattung.** Der Satz vom 17.07. lautet, die Erstattungsanfrage sei
weitergegeben worden und man werde sich melden. **Das ist keine
Erstattungszusage**, und der Fall wird deshalb **nicht** wie #2894 Jeff
Hughes als Regel-1-Fall auf die Erstattungsliste gesetzt.

**Zugesagt und nicht eingehalten wurde der Rückruf.** Das steht fest und ist
aus dem Thread belegt.

**Ob es ein „Resolutions Team" gibt, kann der Bot nicht feststellen** und
behauptet dazu nichts — weder dass es existiert noch dass es nicht existiert.
**Das ist eine Owner-Frage**, und sie ist nicht nebensächlich: der
Kundin wurde vor zwei Monaten eine Stelle genannt, von der sie seither
nichts gehört hat.

### Das Muster

**Zweiter Fall binnen zwei Tagen, in dem eine Zusage aus dem Juli nie
ausgeführt wurde** — nach **#2894 Jeff Hughes** (Ersatzlieferung zugesagt
**24.07.**, nie in Shopify angelegt, inzwischen **52 Tage**). Bei Jeff Hughes
war es ein Ersatz, hier ein Rückruf. **Beide Zusagen stammen aus demselben
Monat, beide sind unerledigt.**

→ `Bot/Escalated - Owner Attention`, **hohe Priorität wegen der Dauer**.
**Eskalationsgrund:** seit 59 Tagen nicht eingehaltene Rückrufzusage;
wiederholter unerledigter Kontakt seit 74 Tagen; bestrittene Werbeaussage
(*„durable and hard wearing"*).

**Nicht auf der Erstattungsliste** — aus dem oben genannten Grund. **Die
Entscheidung über die Erstattung selbst steht beim Owner und ist seit dem
02.07. offen.**

### Entwürfe

Volltext in `docs/entwuerfe-zum-kopieren.md`: **#1998**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, **nichts über die Existenz eines „Resolutions Team" behauptet**,
keine neue Frist genannt, das Foto nicht bewertet, keine rechtliche
Einordnung, keine Rücksendeadresse, kein Label gesetzt, **kein Entwurf in
Gmail angelegt**.

---

## Lauf 11:20 UTC — #7578 und #7663, fünfzehn Minuten auseinander

### #7578 — Luke Buttrey (`lukebuttrey@hotmail.co.uk`), 14.09. 10:56 UTC

Betreff: „Luke Buttrey". Vollständiger Text: *„Where's my order please ?"*

- Bestellung **24.08.**, Versand **03.09.** — **10 Tage bis zum Versand**
- **27,95 £**, bezahlt, FULFILLED
- **Zwei** Plushies der Variante *Elk*
- Yanwen Special Line Promotion, `UL478624163YP`
- Lieferadresse Bradford, England

**Ein Foto liegt bei** (`IMG_8173.jpeg`). Der Bot hat es **nicht geöffnet und
beurteilt es nicht**; vermerkt wird nur, dass etwas beigefügt war. Was es
zeigt, ist unbekannt — es kann ebenso gut ein Screenshot der Trackingseite
wie ein Bild der Ware sein. **Daraus wird nichts abgeleitet.**

**Keine Forderung, keine Beschwerde, kein Eskalationsauslöser.** Die Auskunft
liegt vollständig vor.

→ `Bot/Draft Ready`. **Keine Owner-Entscheidung nötig.**

**Das ist der neunte Fall, in dem eine zurückgehaltene Sendungsnummer die
ganze Anfrage ausmacht** — der zweite allein heute, nach #7657 um 07:30.
Beide Bestellungen wurden am **03.09. mit demselben Zusteller** versendet,
die Sendungsnummern liegen nur 173 auseinander (`UL478624163YP` und
`UL478624336YP`). **Zwei Kunden aus derselben Versandcharge fragen am selben
Vormittag dasselbe.**

### #7663 — Murray „Muzz" McLean (`muzz.mclean@gmail.com`), 14.09. 10:41 UTC

Betreff: „Plushies". Wortlaut: *„I received plushes but alas one afternoon and
they have been destroyed by my groodle. Refund please"*

- Bestellung **24.08.**, Versand **04.09.** — **11 Tage bis zum Versand**
- **44,23 £**, bezahlt, FULFILLED
- Drei Positionen: Zahnbuddy (Blue Mop Plush Dog), Plushie *monkey*,
  Plushie *elephant*
- 4PX Standard Registered, `4PX3003127441579CN`
- Lieferadresse **Mullaloo, Western Australia — Australien**

Im Shop steht er als **Murray McLean**, unterschrieben hat er mit **Muzz
McLean**. **Das ist keine Namensunsicherheit** wie bei #8359 — er hat selbst
unterschrieben, und die Anrede folgt seiner Unterschrift.

**Er nennt keinen Betrag.** Die Bestellung ist in **GBP** ausgewiesen, geliefert
wurde nach Australien. **Eine Umrechnung wird nicht vorgenommen und keine
Währungsdifferenz angesprochen** — es gibt hier nichts zu überbrücken, weil
er nichts beziffert hat.

**Einstufung:** Erstkontakt, kein Verbraucherrecht zitiert, keine Bewertung
angedroht, kein Sicherheitsproblem, kein ausdrücklicher Werbevorwurf.
**Formal kein Eskalationsauslöser** — dieselbe Lage wie bei #7673 Michelle
Barnes heute früh, und aus demselben Grund **keine Vorlagen-Absage**: das
Produkt heisst „Designed for Furry Friends Who Destroy Everything", und sein
Hund hat genau das getan.

→ `Bot/Needs Approval`. **Offen ist ein Ja oder Nein zur Erstattung.**
**Nicht auf der Erstattungsliste** — kein Regelfall nach der geltenden Regel.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`: **#7578**, **#7663**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, **das Foto von #7578 nicht geöffnet und nichts daraus abgeleitet**,
kein Verweis an den Zusteller, keine Währungsumrechnung, kein Zustelldatum
versprochen, keine Rücksendeadresse, keine rechtliche Einordnung, kein Label
gesetzt, **kein Entwurf in Gmail angelegt**.
