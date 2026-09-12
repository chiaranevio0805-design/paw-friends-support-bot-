# Backlog-Triage 2026-09-12

Stündliche Läufe gegen `support.pawfriends.uk@gmail.com` nach
`docs/runbook.md`. Erstattungen nur bei bestätigtem Regel-4-Fall (falscher
Artikel) — sonst Entwurf und Label. **`create_draft` bricht seit dem 21.08. bei
jedem Versuch ab**, deshalb stehen die Entwurfstexte in
`docs/entwuerfe-zum-kopieren.md` statt im Postfach.

## ⏰ Fristen, die heute laufen

- **#7190 Steve Solley** — die von ihm berechnete Lieferfrist (7–21 Tage ab
  Bestellung 22.08.) läuft **heute, 12.09.** ab. Seine eigene 48-Stunden-Frist
  endet **13.09. 19:32**. Entwurf liegt vor, Erstattung ist Owner-Entscheidung.
- **#5829 Tasmin Hunt / David Coles** — die 30-Tage-Frist ab Bestellung
  (12.08.) ist gestern abgelaufen. Die Rüge nach Consumer Rights Act 2015 ist
  davon unabhängig.

---

## Lauf 00:20 UTC — zwei Erstattungsforderungen aus der Nacht

**Neu im Postfach:** zwei Mails, 23:24 und 23:59 (beide 11.09.).

---

### 🚩 #7383 JoAnn Jinks — „sold as indestructible"

**23:59**, Betreff „Return":

> „order # 7383 **indestructible donkey**. I ordered this toy, **it was sold as
> indestructible**, my dog **in 5 minutes** had the arms off and an ear. I would
> like a refund as the toy is **not what I payed for**."

**Shopify:** #7383, bestellt **23.08. 12:36**, **20,34 £**, `PAID` /
`FULFILLED`, 1 × Plushie (donkey), versandt **03.09. 07:31** ab Kirchstr. 2,
**WB US `WNBAA0498036412YQ`**, Toms River, New Jersey. **Elf Tage** bis zum
Versand.

**Neunter Kunde aus dem Versandstapel vom 03.09.** — nach #7568, #7525, #7547,
#7899 und den übrigen.

**Sie bestreitet die Werbeaussage ausdrücklich** („sold as indestructible") und
begründet die Forderung damit, nicht mit Kulanz: „not what I payed for".

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage als Anspruchsgrundlage.

**Nicht auf der Erstattungsliste** — Kauschaden, kein Regelfall.

**Nebenbefund:** `WNBAA…YQ` (WB US) — die Ware ist angekommen. Nach #7060
Felecia Pierce (gestern) der **siebte** Datenpunkt zu dieser Nummernfamilie und
der zweite positive; fünf Meldungen „invalid" / „order not found" stehen
weiterhin dagegen.

---

### #6755 Matt Murphy — Erstattungsforderung ohne Werbevorwurf

**23:24**, Betreff „Refund request", mit weitergeleiteter Versandbestätigung:

> „Please process our refund. We are not satisfied. **After waiting months**, the
> toys finally arrived and **did not last three minutes** with our dog. I'd like
> a full refund."

**Shopify:** #6755, bestellt **19.08. 23:07**, **30,54 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (monkey, donkey), versandt
**02.09. 10:30** ab Kirchstr. 2, **JQ Express US `JCHSG0000004362705`**,
Cleves, Ohio.

**Zur Angabe „months":** vom Bestelldatum 19.08. bis zur Ankunft sind es rund
**drei Wochen**, nicht Monate — davon **vierzehn Tage bis zum Versand**. Die
Wahrnehmung ist übertrieben, die Ursache nicht: der grössere Teil der Wartezeit
lag vor der Übergabe an den Zusteller. **Das gehört in der Antwort benannt,
nicht richtiggestellt.**

**Kein Eskalationstrigger.** Er zitiert keine Werbeaussage, droht nichts an,
nennt keine Behörde, schreibt zum ersten Mal. Es ist eine schlichte
Erstattungsforderung nach Kauschaden.

→ `Bot/Needs Approval`. Eine Erstattung ausserhalb der drei Regeln ist
**Owner-Entscheidung**; der Bot sagt sie nicht zu. **Keine Vorlagen-Absage** —
nach dem gestrigen Befund (fünf von fünf eskaliert) ist sie bei einer
ausdrücklichen Forderung das schlechteste verfügbare Instrument.

**Nicht auf der Erstattungsliste** — Kauschaden, kein Regelfall.

---

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#7383** und
**#6755**. Kein Gmail-Entwurf angelegt.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, keine
Rücksendeadresse, keine Zustellprognose, keine 7–21-Tage-Formel (gestern bei
#7190 nachweislich gerissen), kein Label gesetzt.

---

## Lauf 03:20 UTC — 🚩 #8081 Matthew Pierce: eine Bestellung, die an einer erfundenen Anforderung hängt

**Neu im Postfach:** eine Mail, **02:44**, von `vad_shooter@yahoo.com`.
**Sie enthält keinen eigenen Text** — nur den zitierten Verlauf. Entweder eine
versehentlich leere Antwort oder eine wortlose Rückgabe der letzten Nachricht.
**Der Bot deutet das nicht.**

**Shopify:** #8081, bestellt **29.08. 05:56**, **20,35 £**, `PAID` /
**`UNFULFILLED`**, 1 × Plushie (Duck). Lieferanschrift, so wie sie in Shopify
steht:

```
Box 5647 PSC 3
APO
Armed Forces Pacific
96266-0057
United States
```

**Seit vierzehn Tagen bezahlt und nicht versandt.**

### Der Ablauf

| Zeit | Vorgang |
|---|---|
| 10.09. 07:14 | Shop: „we noticed that **two different postcodes** have been provided… our system is **unable to recognise the APO address format**… please confirm your complete and accurate delivery address, **including the correct postcode and full street address**" |
| 10.09. 07:48 | Kunde antwortet vollständig: „Matthew Pierce, Box 5647 PSC 3, APO AP 96266, United States" |
| **11.09. 09:57:44** | Shop: „Thank you for providing the updated address. **We have received the details and will update your order accordingly.**" |
| **11.09. 10:01:11** | Shop, **drei Minuten und 27 Sekunden später**: „could you please provide **the physical street address and house/building number** associated with your APO address?" |
| 12.09. 02:44 | Kunde antwortet — **ohne eigenen Text** |

### Drei Feststellungen

1. **Die beiden Antworten vom 11.09. widersprechen sich.** Die erste sagt, alles
   liege vor. Die zweite, keine vier Minuten später, verlangt etwas Weiteres.
   Aus Kundensicht ist das nicht auflösbar.

2. **Eine APO-Anschrift hat keine Strassenadresse.** `PSC 3, Box 5647, APO AP
   96266` ist eine vollständige Anschrift der US-Militärpost; ein Haus oder eine
   Strasse gehört dort nicht dazu — das ist keine Lücke, sondern die Bauart
   dieser Anschriften. **Es wird etwas verlangt, das es nicht gibt.**
   Strukturell derselbe Fall wie „a P.O. Box cannot be processed" — eine
   Aussage, die inzwischen **dreimal** widerlegt ist (#5817, #6209, #7101).

3. **„Two different postcodes" trifft nicht zu.** Shopify führt
   **96266-0057**, der Kunde nennt **96266**. Das ist dieselbe ZIP einmal mit
   und einmal ohne die vierstellige Zusatzangabe, nicht zwei Postleitzahlen.

**Die Anschrift steht in Shopify korrekt und vollständig.** Die Bestellung hängt
seit vierzehn Tagen an einer Rückfrage, die die eigenen Stammdaten bereits
beantworten.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bezahlte Bestellung seit 14 Tagen unversandt; zwei
einander widersprechende Antworten binnen vier Minuten; Nachforderung einer
Angabe, die es bei dieser Anschriftenart nicht gibt; unzutreffende Begründung
(„zwei Postleitzahlen").

### Erstattungslage

**Kein Regelfall — noch nicht.** Er hat nicht storniert. **Wenn er es tut, ist
es ein glatter Regel-3-Fall:** die Bestellung ist `UNFULFILLED`, die Stornierung
käme vor Versand, und nach der Policy gilt dann „no argument, no attempt to talk
them out of it". **Das ist im Voraus festgehalten, damit bei einer Stornierung
nicht wieder eine Rückfrage rausgeht** — genau das ist bei #6870 Todd Jacobs am
20.08. passiert und hat dreizehn Tage gekostet, bis die Ware trotz Storno
rausging.

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#8081**.
Kein Gmail-Entwurf angelegt — `create_draft` bricht seit dem 21.08. ab.

**Nicht getan:** keine Strassenadresse nachgefordert, kein Versanddatum
zugesagt, keine Erstattung zugesagt, die leere Antwort nicht gedeutet, kein
Label gesetzt.

---

## Läufe 08:20 und 09:20 UTC — drei neue Fälle, und der Tagesreport

### 🔴 `create_draft` erneut gescheitert — Versuch Nr. 21

Der Tagesreport-Auftrag verlangt ausdrücklich einen Gmail-Entwurf an
`nevio.marasa@icloud.com`. Es wurde **ein** Versuch unternommen: das Schema lud,
danach wurde der Worker-Prozess neu gestartet — dasselbe Muster wie an jedem Tag
seit dem **21.08.** Der Entwurf existiert **nicht**.

**Der Tagesreport liegt stattdessen vollständig in
`docs/2026-09-12-tagesreport.md`** und ist gepusht. Er wurde **vor** dem
Entwurfsversuch geschrieben und committet, genau deshalb ist er nicht
verlorengegangen.

---

### 🚩 #6882 Chris Cobb — „15 mins and my Jack Russell gutted the first one"

**Zwei Mails, 08:56 und 09:00.**

**08:56**, Betreff „WTF":

> „Received this arv. **15 mins** and my Jack Russell **gutted** the first one.
> Lucky I didn't give it to the Staffys. I have bought **shit from discount
> stores that last longer**. **Please explain**."

**09:00:** ein Foto (`Image.jpeg`) plus die weitergeleitete
Bestellbestätigung. **Kein weiterer eigener Text.**

**Shopify:** #6882, bestellt **20.08. 22:10**, **30,66 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (monkey, elephant), versandt
**02.09. 10:37** ab Kirchstr. 2, Yanwen Special Line `UL476302497YP`, Tewantin,
Queensland. **Dreizehn Tage** bis zum Versand.

**Währungsdifferenz:** Die Bestellbestätigung weist **58,56 AUD** aus, Shopify
führt **30,66 £**. Wie bei #7179 (48 USD / 35,64 £) wird das **nicht
überbrückt** — der Betrag gehört dem Owner vorgelegt.

**Was er verlangt, ist keine Erstattung, sondern eine Erklärung.** „Please
explain" ist die ganze Forderung. Er bestreitet damit die Grundannahme des
Produkts, unter dessen Namen er es gekauft hat.

**„Gutted"** heisst, die Füllung liegt offen. Er schreibt **nicht**, dass der
Hund etwas gefressen hat — **das wird hier nicht hineingelesen.** Die Frage
gehört aber in die Antwort, so wie bei #7179.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Produktzusage mit Fotobeleg und ausdrücklicher
Erklärungsforderung.
**Nicht auf der Erstattungsliste** — Kauschaden, kein Regelfall, keine
Erstattungsforderung.

---

### 🚩 #5407 Nicolette Kirkwood — dreissig Tage unterwegs

**08:57:**

> „I ordered these 2 toys **in good faith** on the 13th of August and they have
> **never arrived**. Please can you look into this and provide an update."

**Shopify:** #5407, bestellt **10.08. 08:11**, **27,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Paw-Friends™-Fluffys (frog, giraffe),
versandt **13.08. 10:44** ab Kirchstr. 2, Yanwen Special Line `UL418684575YP`,
Prestwick, Schottland.

**Das ist der längste Nichtzustellungsfall im Projekt.**

- Versandt am **13.08.** — heute sind das **dreissig Tage**.
- **Und der Versand war schnell:** drei Tage nach der Bestellung. Die gesamte
  Verzögerung liegt **im Transport**, nicht im Lager.
- Ihre Datumsangabe „13th of August" bezieht sich auf die
  **Versandbenachrichtigung**, nicht auf die Bestellung (10.08.). Kein
  Widerspruch.

**Die 7–21-Tage-Formel ist hier um neun Tage überschritten** — in jeder
Lesart, ab Bestellung wie ab Versand. **Sie darf ihr auf keinen Fall geschickt
werden.**

→ `Bot/Needs Approval`. Sie verlangt einen Sachstand, keine Erstattung. Nach
dreissig Tagen ist ein Sachstand aber keine ehrliche Antwort mehr: die Sendung
ist mit hoher Wahrscheinlichkeit nicht mehr unterwegs. **Ob Ersatz oder
Erstattung angeboten wird, ist Owner-Entscheidung** — kein Regelfall, der Bot
sagt nichts zu.

---

### #7699 Lorraine Sale — eigene Frist, 17.09.

**08:13:**

> „Can you please advise **where the items I ordered from yourselves are**! I
> feel this is quite an **excessive time** now to be waiting. **If they are not
> here by 17th September I want a full refund.**"

**Shopify:** #7699, bestellt **25.08. 07:13**, **27,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (frog, Duck), versandt
**03.09. 07:44** ab Kirchstr. 2, Yanwen Special Line `UL478625416YP`, Leicester,
England. **Neun Tage** bis zum Versand.

**Zehnter Kunde aus dem Versandstapel vom 03.09.** — nach #7568, #7525, #7547,
#7383, #7899 und den übrigen.

**Sie setzt selbst eine Frist: 17.09.** Das ist die zweite selbstgesetzte Frist
binnen zwei Tagen (nach #7190 Steve Solley, 48 Stunden ab gestern 19:32).

→ `Bot/Needs Approval`. Sagbar: Versanddatum, Zusteller, Nummer, Trackinglink,
und offen, dass neun Tage bis zum Versand vergingen. **Die Erstattungszusage für
den 17.09. ist Owner-Entscheidung** — kein Regelfall, die Ware ist versandt.
**Nicht sagbar:** ein Zustelltermin, und **nicht** die 7–21-Tage-Formel.

---

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#6882**, **#5407**
und **#7699**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, keine Frist
akzeptiert, keine 7–21-Tage-Formel, keine Zustellprognose, keine
Währungsdifferenz überbrückt, kein Verschlucken hineingelesen, kein Label
gesetzt.

---

## Lauf 10:20 UTC — 🚩 #4726 Marilyn Penniall, und eine zweite Vorlage, die bisher in keinem Log steht

**Neu seit 09:20:** eine Mail, **09:46**, mit Foto (`1000013047.jpg`):

> „Thank you for the response however **I am not happy with the reply** & **you
> offer a money back guarantee**. I would like to have a **full refund** as they
> are **absolutely not as described, promised or advertised**."

**Shopify:** #4726, bestellt **06.08. 11:01**, **34,95 £**, `PAID` /
**`PARTIALLY_FULFILLED`**, Tag `Kaching Bundles`, vier Positionen (3 × Plushie —
monkey, fox, elephant — plus E-Book). **Eine einzige Sendung am 22.08.
10:30**, Yanwen Special Line `UL442894597YP`, Northampton, England.
**Sechzehn Tage** bis zum Versand.

### 🔎 Eine zweite Vorlage — und sie widerspricht der eigenen Werbung

Am **04.09. 09:26** bekam sie **nicht** die Kauschaden-Absage, sondern einen
anderen Text. Der Kern, wörtlich:

> „While our toys are **designed with durability in mind**, **no plush toy can
> be guaranteed to be completely indestructible**, particularly for dogs who are
> strong or persistent chewers."

**Das ist der Shop selbst, schriftlich, gegenüber einer Kundin.** Es ist damit
eine shopseitige Aussage, die genau das einräumt, was seit dem 13.08. rund
siebzig Kunden bestreiten — und sie steht im Widerspruch zu dem Produktnamen,
unter dem verkauft wird, und zu der gestern zweimal zitierten Anzeigenzusage
(#7060 „or you get a refund", #5851 „replace it free").

**Diese Vorlage steht in keinem bisherigen Log.** Bis heute war nur die
Kauschaden-Absage bekannt. **Es sind also mindestens zwei verschiedene
Standardtexte im Umlauf, die sich gegenseitig untergraben:** der eine lehnt mit
Verweis auf die Garantiebedingungen ab, der andere räumt ein, dass die
beworbene Eigenschaft nicht zugesichert werden kann.

→ **Owner-Prüfung: welche Standardtexte existieren und wer sie verschickt.**
Der Bot hat den Postausgang **nicht** systematisch durchsucht — dieselbe Lücke,
die gestern den Vorfall bei #6116 zwei Tage lang verdeckt hat.

### Der Verlauf

| Datum | Vorgang |
|---|---|
| 06.08. | Bestellung, 34,95 £ |
| **22.08.** | eine Sendung raus — **16 Tage** später |
| 25.08. 08:34 | „Please advise on when I will receive my order" |
| 26.08. 17:50 | „has been shipped… progressing through the delivery network" — **ohne Sendungsnummer** |
| 02.09. 14:51 | „I purchased this on the understanding **from your advert** that it was a tuff toy… feel **ripped off & scammed**" |
| **04.09. 09:26** | die zweite Vorlage (s. o.) |
| **12.09. 09:46** | **dritter Kontakt**, Foto, ausdrückliche Berufung auf die Geld-zurück-Garantie |

**Auch hier wurde eine vorhandene Sendungsnummer nicht genannt** —
`UL442894597YP` lag seit dem 22.08. vor. **Vierter solcher Fall** in zwei Tagen
(nach #7525, #7547, #7190).

### Offene Frage zum Lieferumfang

Die Bestellung ist bis heute **`PARTIALLY_FULFILLED`**: vier Positionen, eine
Sendung. Sie schrieb am 02.09. „Thank you for delivering my order", hat also
etwas erhalten. **Welche Positionen versandt wurden und welche nicht, ist aus
den vorliegenden Daten nicht ableitbar** — das ist im Admin zu prüfen, bevor ihr
geantwortet wird. Der Bot behauptet dazu nichts.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage („not as described, promised or
advertised"), ausdrückliche Berufung auf die Geld-zurück-Garantie, dritter
Kontakt ohne Lösung, Betrugsvorwurf („ripped off & scammed"), dazu eine
unvollständig ausgelieferte Bestellung.

**Nicht auf der Erstattungsliste.** Kauschaden ist kein Regelfall, und für
Regel 2 wären die Teile unbenutzt — das sind sie nicht. **Die Frage, ob die
Ware „as described" war, ist Owner- und ggf. Rechtssache**, ebenso die nicht
ausgelieferten Positionen. Der Bot sagt nichts zu und lehnt nichts ab.

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#4726**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, keine Aussage zum Lieferumfang, keine Zustellprognose, keine
7–21-Tage-Formel, kein Label gesetzt.

---

## Lauf 11:20 UTC — 🚩 #4745 Steph Hanlon: vier Minuten 26 Sekunden

**Neu seit 10:20:** eine Kundenantwort, **10:36:18**. Sie ist die Reaktion auf
eine Vorlagen-Absage, die heute um **10:31:52** rausging.

**Abstand: 4 Minuten 26 Sekunden.** Das ist die **schnellste Eskalation im
Projekt** — bisheriger Wert: 28 Minuten (#7101 Cameron Herpich, gestern).

**Shopify:** #4745, bestellt **06.08. 13:07**, **54,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, fünf Positionen (4 × Plushie — hippo,
elephant, Duck, frog — plus Fur Wonder Brush), versandt **22.08. 01:30** ab
Kirchstr. 2, Yun Express `YT2623400701612777`, Coatbridge, Schottland.
**Sechzehn Tage** bis zum Versand.

**Der Fall ist bereits erfasst** — Log vom 10.09., 14:20: „#4745 Stephen
Hanlon: Trustpilot wird zum Argument". Seine Mail vom 10.09. 14:02:

> „your toys are shite.. **one day they lasted** before the stuffing was flying
> like any other toy **you claimed not be like**. I should have read the **trust
> pilot reviews** that says it all.. **everyone says they are shite!!**"

**Was daraufhin passiert ist:** Am **12.09. 10:31:52** — zwei Tage später — ging
die **Kauschaden-Vorlage** an ihn raus. Seine Antwort, 10:36:

> „the product didnt meet my expectations because **the company is full of shite
> making ridiculous claims** that your toys are better than everyone elses and
> **will out last any dog** blah blah bullshit.. your toys are pish and **your
> reviews speak for themselves**."

### Die Zählung

**Sechs von sechs.** Fünf Absagen gestern (#5973, #5851, #7179, #7101, #7271),
eine heute (#4745) — **alle sechs eskaliert, keine Ausnahme.** Über drei Tage
gerechnet: **17 von 17.**

**Die heutige Absage ging raus, nachdem der Befund drei Tage lang im Log
steht** und gestern im Tagesreport an erster Stelle stand.

### Was er zusätzlich sagt

**„Your reviews speak for themselves"** — er meint die **externen** Bewertungen,
auf die er schon am 10.09. verwiesen hat. Das steht neben dem Befund von gestern
zu **#6606**: der **shopeigene** Bewertungspool des Hauptprodukts zeigt **78
Bewertungen, Durchschnitt 5,0, keine einzige negative**.

**Beides gleichzeitig kann der Owner prüfen, der Bot nicht** — er hat die
Trustpilot-Seite **nicht** aufgerufen und behauptet über deren Inhalt nichts.
Festgestellt ist nur: **zwei Kunden** (#4745 am 10.09. und heute) berufen sich
auf externe Bewertungen als Gegenbeleg, und **ein Kunde** (#6606 Matt Pinnock)
fragt seit vier Tagen vergeblich, wie er auf der Shop-Seite eine abgeben kann.

**Er zitiert ausserdem eine weitere Werbeaussage:** „your toys are **better than
everyone elses** and **will out last any dog**". Ob dieser Wortlaut so geschaltet
wurde, ist **ungeprüft** — wie bei #7060 und #5851. Der Bot liest keine
Anzeigentexte.

→ `Bot/Escalated - Owner Attention` (bleibt).
**Eskalationsgrund:** dritter Kontakt, bestrittene Werbeaussage, Verweis auf
externe Bewertungen als Beleg für ein Muster, Betrugsvorwurf gegen das
Unternehmen.

**Nicht auf der Erstattungsliste** — Kauschaden, kein Regelfall, und er verlangt
keine Erstattung. **Er verlangt überhaupt nichts.** Wie #7101 und #7271
gestern: eine Beschwerde ohne Forderung, beantwortet mit der Ablehnung einer
nicht gestellten Forderung.

### Ohne neue Nachricht wieder aufgetaucht

**#6751 Jonathan Pizzo** — keine neue Kundenmail. Letzte Nachricht weiterhin
**01.09. 22:01**, in der er höflich nachfragt, ob die am **28.08.** zugesagte
Sendungsnummer inzwischen vorliegt („We are currently checking with our courier
team"). **Seit elf Tagen unbeantwortet.** Vollständig erfasst im Log vom 08.09.,
22:20. Kein neuer Eintrag nötig — **aber die Zusage vom 28.08. steht weiterhin
offen.**

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#4745**.

**Nicht getan:** keine Vorlagen-Absage wiederholt, keine Erstattung zugesagt,
keine Trustpilot-Seite aufgerufen, kein Anzeigentext behauptet, kein Label
gesetzt.

---

## Lauf 12:20 UTC — drei weitere Eskalationen, und eine Korrektur der Zählung

### 🔧 Korrektur: es waren acht Antworten am 11.09., nicht sieben

Im Eintrag vom 20:20 gestern steht, es seien **sieben** Antworten zwischen 09:47
und 10:09 rausgegangen. Es waren **acht**. Fehlte: **10:02:41 an
`jasinv13@gmail.com` (#6280)** — die **sechste** Kauschaden-Absage.

**Ursache, und sie ist strukturell:** Die Läufe durchsuchen `in:inbox`. Eine
gesendete Antwort wird erst sichtbar, wenn der Kunde darauf antwortet. Jede
Zählung ausgehender Mails ist deshalb **zum Zeitpunkt des Laufs zwangsläufig
eine Untergrenze**. Dasselbe Loch hat gestern den Vorfall bei #6116 zwei Tage
lang verdeckt. **Alle Angaben zu ausgehenden Vorlagen in diesen Logs sind als
Mindestzahlen zu lesen.**

### Der Stand nach heute

| Tag | Kauschaden-Absagen | eskaliert |
|---|---|---|
| 11.09. | #5973, #5851, #7179, #7101, #7271, **#6280** | **6 von 6** |
| 12.09. | #4745, #7316, #6286 | **3 von 3** |

**Neun von neun.** Die drei heutigen gingen raus, **nachdem** der Befund drei
Tage im Log stand und gestern im Tagesreport an erster Stelle stand.

---

### 🚩 #6280 Jasin Vandenbroeke — verlangt jetzt nur noch die Änderung der Werbung

**Shopify:** #6280, bestellt **15.08. 22:02**, **30,56 £**, `PAID` /
`FULFILLED`, 2 × Plushie (Little Bear, hippo), versandt **20.08. 02:16** ab
Kirchstr. 2, **4PX Economic Registered `4PX3003082535801CN`**, Dudley, North
Carolina.

| Datum | Vorgang |
|---|---|
| 29.08. | „This is taking too long… going on 11 or so days" |
| 31.08. | Lieferauskunft: „**At around 11 days**, your order is still within the usual delivery timeframe" |
| 10.09. | „**less than 20 minutes** to tear them open and get the **squeaker** out… I would like to request a full refund" |
| **11.09. 10:02:41** | **Kauschaden-Absage** |
| **12.09. 11:21** | die Mail unten, mit Foto |

> „I am writing to **formally request that Paw-Friends reconsider its
> advertising language** regarding product durability. Marketing your toys as
> **'indestructible'** sets an explicit expectation… When a product advertised
> in this manner **fails within 20 minutes**, it **fails to meet the basic
> standards established by your own promotional claims**. I strongly encourage
> your team to **revise these product descriptions** to ensure accurate
> marketing and to **avoid misleading future customers**."

**Er hat die Erstattungsforderung fallengelassen.** Am 10.09. hat er eine
verlangt; heute verlangt er **nur noch, dass die Werbung geändert wird**. Das
ist der **dritte** Kunde, der das ausdrücklich fordert, nach den beiden Fällen
vom 10.09.

**Nebenbefund zur 7–21-Tage-Formel:** Ihm wurde sie am 31.08. **mit Startpunkt**
geschickt („at around 11 days" — also ab Bestellung). Bei **#7190 Steve Solley**
ging sie am 11.09. **ohne** Startpunkt raus, und genau daran ist sie gerissen.
**Die Formel wird also uneinheitlich verschickt** — das ist präziser als die
bisherige Formulierung im Log und gehört so festgehalten.

→ `Bot/Escalated - Owner Attention`. **Nicht auf der Erstattungsliste** —
Kauschaden, und er fordert keine Erstattung mehr.

---

### 🚩 #7316 Brett Merriman — „Why would I return it before it got used?"

**Shopify:** #7316, bestellt **23.08. 03:19**, **20,34 £**, `PAID` /
`FULFILLED`, versandt **02.09. 10:59** ab Kirchstr. 2, **WB US
`WNBAA0497794623YQ`**, Mesa, Arizona.

Erste Mail **10.09. 13:51**: „This toy lasted **20 minutes**… Junk".
Absage **12.09. 10:31:38**. Antwort **12:04:22** — **1 Std 33 Min**:

> „Ya so your toys suck and so does your company. **Why the fuck would I return
> it before it got used?** Clowns"

**Das ist zum zweiten Mal derselbe strukturelle Einwand** wie bei **#7101
Cameron Herpich** gestern: die Bedingung „unbenutzt zurück" ist bei einem
Kauspielzeug nicht erfüllbar, ohne auf die Prüfung zu verzichten. Zwei Kunden,
zwei Kontinente, dieselbe Beobachtung, beide unabhängig voneinander.

→ `Bot/Escalated - Owner Attention`. **Nicht auf der Erstattungsliste** —
Kauschaden.

---

### 🚩 #6286 Deborah Gould — vierter Kontakt, „false advertising"

Absage **10.09. 10:26**, Antwort **10.09. 10:39** („I bought your product **only
because of your 30 Day money back guarantee**"), **zweite Absage 12.09.
09:54:57**, Antwort **11:36:12** — **1 Std 41 Min**:

> „**I will be watching to see if you change your 30 day guarantee** and that
> you **outline what constitutes your money back guarantee**. **You must see now
> that it is false advertising.** Not happy!"

**Sie ist die Kundin, die am 10.09. die ACCC eingeschaltet hat.** Sie bekommt
danach dieselbe Absage ein zweites Mal — und formuliert jetzt exakt dieselbe
Forderung wie #6280 heute und wie die beiden Fälle vom 10.09.: **die Werbung
und die Garantiebedingungen sollen geändert werden.**

→ `Bot/Escalated - Owner Attention` (bleibt). **Nicht auf der Erstattungsliste**
— Kauschaden.

---

### Das Muster, das sich über alle drei legt

**Vier Kunden verlangen inzwischen ausdrücklich nicht Geld, sondern eine
Änderung der Werbung** (#6280 heute, #6286 heute, plus zwei am 10.09.).
Dazu kommen **zwei**, die den Konstruktionsfehler der Regel 2 benennen (#7101,
#7316), und **drei**, denen eine Erstattung abgelehnt wurde, die sie nie
verlangt hatten (#7101, #7271, #4745).

**Das ist keine Erstattungsfrage mehr.** Es ist eine Frage an den Text auf der
Seite und an die Garantiebedingung.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#6280**, **#7316**
und **#6286**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, keine Zusage zur Änderung von Werbung oder Garantie — **das ist
Owner-Sache und wird im Text ausdrücklich so benannt**, kein Anzeigentext
gelesen, kein Label gesetzt.

---

## Lauf 13:20 UTC — 🚩 #7165 Andrea Dentel: „too dangerous for my dog"

**Neu seit 12:20:** eine Mail, **12:22**, Betreff „Return Request - order 7165",
mit Foto (`image0.jpeg`):

> „my dog destroyed the toy **within 20 minutes** of receiving it. Picture
> attached. **These types of toys are too dangerous for my dog.** I'm requesting
> to **return the items** and receive a **full refund** of my order."

**Shopify:** #7165, bestellt **22.08. 12:37**, **28,50 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, **2 × Plushie** (frog, pig), versandt
**02.09. 10:51** ab Kirchstr. 2, **JQ Express US `JCHSG0000004363079`**,
Gurnee, Illinois. **Elf Tage** bis zum Versand.

### Zwei Dinge, die diesen Fall von den übrigen unterscheiden

**1. Sie nennt es eine Gefahr, nicht einen Mangel.** „**Too dangerous for my
dog**" ist kein Qualitätsurteil, sondern eine Sicherheitsaussage. Das ist die
**neunte** Meldung, die auf verschluckbares oder gefährliches Material zielt —
nach #6283, Andy Sire, Kevin Saggers #3197, #6741, der Nadel in #1301, dem
Quietscher in #6286, #7179 („eating the cotton") und #5186 („he tries to eat
them").

**Nach `support-policy.md` ist eine Sicherheitsmeldung ein eigener
Eskalationstrigger** — unabhängig davon, ob ein Erstattungsanspruch besteht.

**2. Sie schreibt „the toy" im Singular und „the items" im Plural.** Bestellt
sind **zwei** Plüschtiere. Ob das zweite unbenutzt ist, sagt sie **nicht** —
**das ist zu fragen, nicht anzunehmen.** Wenn ja, ist es ein **Regel-2-Fall**
und damit ein voller Anspruch auf den entsprechenden Anteil, und die
Kauschaden-Absage wäre hier zum **achten** Mal der falsche Text.

Der Anteil ist bei einer Kaching-Bundle-Bestellung **im Admin zu bestimmen** —
die Listenpreise (2 × 30,78 £) ergeben nicht den gezahlten Betrag von 28,50 £.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** Sicherheitsmeldung („too dangerous"), dazu ein möglicher
Regel-2-Anspruch auf das zweite Teil, der vor jeder Antwort zu klären ist.

**Noch nicht auf der Erstattungsliste** — erst nach der Rückfrage zum zweiten
Teil. **Das zerstörte Teil ist und bleibt Kauschaden und kommt nicht darauf.**

### Ohne neue Nachricht wieder aufgetaucht

**#5186 John Abbott** — keine neue Kundenmail; die letzte bleibt **10.09.
19:54** („Would like a full refund. Sorry, this went to Spam and just seeing
this"). Vollständig erfasst im Log vom 10.09. Kein neuer Eintrag.

**Der Vorgang bleibt aber offen und gehört zum heutigen Muster:** Er hat am
26.08. gefragt „How do I return these?", bekam am 28.08. die
**Rückfrage-Vorlage** („could you please let us know the reason"), antwortete am
30.08. mit einer **Sicherheitsangabe** („way too small for my dog. **He tries to
eat them**") — und bekam darauf am 01.09. **ein Teilerstattungsangebot statt
einer Rücknahme**. Am 10.09. verlangt er die volle Erstattung. **Seither
unbeantwortet.**

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#7165**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, kein Anteil
geschätzt, keine Rücksendeadresse genannt (es gibt keine), nicht angenommen,
dass das zweite Teil unbenutzt ist, kein Label gesetzt.

---

## Lauf 14:20 UTC — 🚩 #6781 Carlie Terry: „Not what you say in your adverts!"

**Neu seit 13:20:** zwei Mails derselben Kundin, **13:21** und **13:29**, beide
mit Foto.

**Betreff: „Not what you say in your adverts!"** — der Werbevorwurf steht in der
Betreffzeile.

**13:21** (`1000111046.jpg`):

> „I have just received my order and my dog **has not had it 20 minutes** and
> has already started to destroy it, it certainly **isn't as durable and long
> lasting as you state**! Please see picture attached after 20 mins of having
> his new toy! **Total waste of money.** Please advise on your **refund
> process** please."

**13:29**, acht Minuten später, zweites Foto:

> „And a few minutes later......**this!** Clearly not durable and long lasting!!"

**Shopify:** #6781, bestellt **20.08. 05:24**, **29,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, **2 × Plushie** (pig, Duck), versandt
**02.09. 10:31** ab Kirchstr. 2, Yanwen Special Line `UL476290860YP`,
Gillingham, England. **Dreizehn Tage** bis zum Versand.

### Drei Punkte

**1. Eine weitere Wortlaut-Variante.** Sie zitiert „**durable and long
lasting**" als das, was „you state". Das ist eine Formulierung, die in keinem
bisherigen Fall vorkam. Die Liste der bestrittenen shopseitigen Wortlaute steht
damit bei:

| Wortlaut | zuerst zitiert von |
|---|---|
| „indestructible" | zahlreich, seit 13.08. |
| „Designed for Furry Friends Who Destroy Everything" (Artikelname) | #5829, #8343 |
| „reinforced rope structure, double stitching, anti-tear design" | #5829, #6877 |
| „indestructible **or you get a refund**" | #7060 (11.09.) |
| „**replace it free**" | #5851 (11.09.) |
| „better than everyone elses", „will out last any dog" | #4745 (heute) |
| „**durable and long lasting**" | **#6781 (heute)** |

**Keiner dieser Wortlaute ist vom Bot geprüft worden.** Er liest keine
Anzeigentexte und keine Produktseite. Festgehalten ist nur, **was Kunden
zitieren** — und dass es inzwischen sieben verschiedene Formulierungen sind.

**2. Sie fragt nach dem Verfahren, nicht nach einer Zusage.** „Please advise on
your refund process" — das ist dieselbe Frage wie bei **#5973 Stephen Cooil**
(„How do I go about this?") und **#5186 John Abbott** („How do I return
these?"). **Alle drei sind unbeantwortbar, solange es keine Rücksendeadresse
gibt** — offener Blocker seit dem 13.08., heute **dreissig Tage**.

**3. Zweites Teil ungeklärt.** Bestellt sind **zwei** Plüschtiere, sie schreibt
von „**his new toy**" im Singular. Ob das zweite unbenutzt ist, sagt sie nicht —
**wird gefragt, nicht angenommen.** Derselbe offene Punkt wie bei **#7165 Andrea
Dentel** vor einer Stunde.

### Beide Fälle von heute Mittag gehören zusammen

**#7165 Andrea Dentel (12:22)** und **#6781 Carlie Terry (13:21)**: beide
Bestellungen aus dem Versandstapel vom **02.09.**, beide diese Woche zugestellt,
beide melden **zwanzig Minuten**, beide bestellten **zwei** Teile und schreiben
über **eines**. Sie wissen nichts voneinander.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage, ausdrücklich im Betreff und im
Text mit Wortlaut; zwei Fotobelege binnen acht Minuten.

**Nicht auf der Erstattungsliste** — das zerstörte Teil ist Kauschaden. **Der
Anteil für ein etwaiges unbenutztes zweites Teil erst nach ihrer Antwort**, und
dann im Admin zu bestimmen (Kaching-Bundle: 2 × 29,95 £ Listenpreis gegen
29,95 £ gezahlt).

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#6781**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, kein
Rücksendeverfahren beschrieben (es gibt keins), keine Rücksendeadresse erfunden,
kein Anteil geschätzt, kein Anzeigentext geprüft oder behauptet, kein Label
gesetzt.

---

## Lauf 15:20 UTC — #7246 und #8359

### 🚩 #7246 Barbara Crouch — „How do i get refunded?"

**14:41**, mit Foto:

> „Very disappointed in **the claim that my dog wont destroy these plushies**.
> This was **10 minutes** of play time. **How do i get refunded?**"

**Shopify:** #7246, bestellt **22.08. 20:52**, **28,50 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, **2 × Plushie** (hippo, elephant), versandt
**02.09. 10:56** ab Kirchstr. 2, **4px US `4PX3003122373561CN`**, Clarksville,
Tennessee. **Elf Tage** bis zum Versand.

**Sie ist die vierte Kundin an diesem Tag, die nach dem Verfahren fragt** — nach
**#5973** („How do I go about this?"), **#5186** („How do I return these?") und
**#6781** („Please advise on your refund process"). **Alle vier Fragen sind
unbeantwortbar**, weil es keine Rücksendeadresse gibt. Der Blocker ist heute
**dreissig Tage** alt.

**Achter bestrittener Wortlaut:** „the claim that my dog **wont destroy** these
plushies". Ungeprüft wie die übrigen sieben.

**Zehn Minuten** ist die zweitkürzeste gemeldete Nutzungsdauer — kürzer war nur
**#7383 JoAnn Jinks** mit fünf Minuten (heute Nacht).

**Sie schreibt „these plushies" im Plural** — anders als #7165 und #6781 deutet
das darauf hin, dass **beide** Teile benutzt wurden. **Sicher ist es nicht**, und
es wird nicht angenommen; die Rückfrage steht im Entwurf.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage mit Fotobeleg.
**Nicht auf der Erstattungsliste** — Kauschaden.

---

### #8359 — Lieferanfrage, und der Gegenbeleg zum Versandproblem

**14:56**, vollständiger Text: „**Have not received my order**"

**Shopify:** #8359, bestellt **07.09. 04:35**, **44,06 £**, `PAID` /
`FULFILLED`, Tags `Kaching Bundles`, `UpCart Rewards`, drei Positionen
(1 × Zahnbuddy „Blue Mop Plush Dog", **2 × Plushie donkey**), versandt
**08.09. 07:50** ab Kirchstr. 2, **RD Express `RD1026898162HM`**, Morning Sun,
Iowa.

**⚠️ Namensabweichung:** Die Bestellung läuft auf **Norma Vickroy**, geschrieben
hat `gary.lisacooper@gmail.com`. **Der Bot rät keinen Vornamen** und redet die
Person im Entwurf nicht mit einem Namen an, den er nicht belegen kann. Vor dem
Senden im Admin klären, wer Ansprechpartner ist.

**Der Befund zur Versanddauer:** **ein Tag** zwischen Bestellung und Versand.
Zusammen mit **#8344** (zwei Tage, 10.09.) und **#8343** (drei Tage, gestern) ist
das der dritte Beleg: **die Versandverzögerung ist für Septemberbestellungen
weg.** Zum Vergleich dieselbe Woche: #6781 dreizehn Tage, #7246 elf Tage, #4726
sechzehn Tage — alles Augustbestellungen.

**Ihre Erwartung ist damit aber nicht erfüllt:** die Ware ist seit vier Tagen
unterwegs. Ein Zustelltermin wird **nicht** genannt, und die 7–21-Tage-Formel
**nicht** verwendet.

→ `Bot/Draft Ready`. Kein Eskalationstrigger: Erstkontakt, keine Forderung,
keine Werbeaussage, keine Frist.
**Nicht auf der Erstattungsliste** — Ware unterwegs, keine Forderung.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#7246** und
**#8359**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, kein
Rücksendeverfahren beschrieben, keine Adresse erfunden, kein Vorname geraten,
keine Zustellprognose, keine 7–21-Tage-Formel, kein Label gesetzt.

---

## Lauf 16:20 UTC — drei Fälle, einer davon ohne feststellbare Bestellnummer

### 🚩 becca23047@aol.com — „Destroyed in 5 minutes", Bestellung nicht auffindbar

**15:20**, Betreff „Destroyed in 5 minutes", **drei Anhänge**
(`image0.png`, `image1.png`, `image2.jpeg`):

> „These toys are **no where near indestructible**, my dog destroyed it in **five
> minutes**. **Please refund my whole order** to the credit card I used. **See
> attached photos for ordering information** and a photo of the toy."

**🔎 Die Bestellung ist nicht feststellbar.**

- In Shopify liegt **keine Bestellung** zu `becca23047@aol.com` — weder über die
  Bestell- noch über die Kundensuche.
- Die Bestelldaten stehen **in den Screenshots**. **Der Bot kann Bildinhalte
  nicht lesen** und rät keine Bestellnummer.

**Das ist der zweite Fall dieser Art binnen 24 Stunden** — nach
**dinod28@aol.com** gestern, wo ebenfalls keine Bestellung zur Adresse
auffindbar war. Beide sind `@aol.com`. Ob das zusammenhängt, ist **offen**; der
Bot stellt nur fest, dass es zweimal vorkam.

**→ Owner: die Anhänge öffnen und die Bestellung identifizieren.** Ohne Nummer
ist weder der Betrag noch der Umfang belegbar, und eine Erstattung „des ganzen
Auftrags" ist nicht bezifferbar.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage („no where near indestructible"),
Erstattungsforderung über den gesamten Auftrag, Bestellung nicht zuordenbar.
**Nicht auf der Erstattungsliste** — Kauschaden, und ohne Bestellnummer
ohnehin nicht bezifferbar.

**Fünf Minuten** ist damit zum zweiten Mal heute die kürzeste gemeldete
Nutzungsdauer — nach **#7383 JoAnn Jinks** heute Nacht.

---

### 🚩 #7627 Charlotte Matthews — die Erstattungsbitte wurde übergangen

**Shopify:** #7627, bestellt **24.08. 19:23**, **27,95 £**, `PAID` /
`FULFILLED`, versandt **03.09. 07:41** ab Kirchstr. 2, Yanwen Special Line
`UL478624234YP`, Bury Saint Edmunds, England. **Zehn Tage** bis zum Versand.
**Elfter Kunde aus dem Versandstapel vom 03.09.**

| Zeit | Vorgang |
|---|---|
| 10.09. 08:18 | „I placed an order on 24th August and have still not received it. Can u please let me know what's going on **or refund my money**?" |
| **12.09. 09:50** | Lieferauskunft mit **7–21-Tage-Formel**, **ohne Sendungsnummer** — **und ohne ein Wort zur Erstattungsbitte** |
| **12.09. 16:15** | ihre Antwort |

> „Ok. **Your website doesn't specify that orders will take that long.** When I
> placed my order **that time frame was not communicated**. I will know **not to
> purchase again** in future."

**Drei Befunde, alle heute schon dagewesen:**

1. **Ihre Erstattungsbitte vom 10.09. ist in der Antwort nicht vorgekommen.**
   Dasselbe wie bei #7179 (drei Punkte, einer beantwortet) und #5973 (dreimal
   dieselbe Frage, zweimal am Thema vorbei).
2. **Die Sendungsnummer lag seit dem 03.09. vor und wurde nicht genannt.**
   **Fünfter Fall** in zwei Tagen — nach #7525, #7547, #7190, #4726.
3. **Sie bestreitet die Lieferzusage**, wie Carol Garvey gestern („There was no
   note to say shipping would take so long") und Steve Solley („not the original
   agreement"). **Dritte Kundin** mit demselben Punkt in zwei Tagen.

Sie eskaliert nicht. Sie hört auf zu kaufen.

→ `Bot/Needs Approval`. **Offen ist ein Ja oder Nein zur Erstattung** — die
Bitte steht seit dem 10.09. unbeantwortet im Raum. Kein Regelfall (versandt
03.09.), also Owner-Entscheidung. Sendungsnummer in jedem Fall nennen.
**Nicht auf der Erstattungsliste.**

---

### #4939 Sara Thompson — Geschenk, zwanzig Minuten, und eine Bestellung von Anfang August

**15:47**, mit Foto, vollständiger Text:

> „I just gave **my mom her new teddy** purchased from you. **Here is the outcome
> 20 mins later...**"

**Keine Forderung. Kein Vorwurf. Kein Zitat.** Wie #7101 Cameron Herpich und
#7271 Rosalind Welch — beide bekamen darauf eine Absage und beide sind
eskaliert.

**Shopify:** #4939, bestellt **07.08. 15:04**, **34,95 £**, `PAID` /
**`PARTIALLY_FULFILLED`**, Tag `Kaching Bundles`, **vier Positionen**
(3 × Paw-Friends™-Fluffys — Duck, giraffe, frog — plus E-Book). **Eine einzige
Sendung am 24.08. 02:20**, Yun Express `YT2623600701636706`, Tipton, England.
**Siebzehn Tage** bis zum Versand.

**🚩 Die Bestellung ist seit dem 07.08. — sechsunddreissig Tagen — nicht
vollständig ausgeliefert.** Wie bei **#6116 Sharron Hodges** (82,81 £, neun
Positionen, eine Sendung) und **#4726 Marilyn Penniall** (vier Positionen, eine
Sendung). **Welche Positionen versandt wurden, ist aus den vorliegenden Daten
nicht ableitbar** — im Admin zu prüfen. Der Bot behauptet dazu nichts.

**Das ist der dritte `PARTIALLY_FULFILLED`-Fall in zwei Tagen.**

→ `Bot/Needs Approval`. Die Antwort selbst verspricht nichts, **aber die
unausgelieferten Positionen sind eine Owner-Entscheidung**, und sie soll keine
Zusage bekommen, bevor klar ist, was sie überhaupt erhalten hat.
**Nicht auf der Erstattungsliste** — der zerstörte Teddy ist Kauschaden; die
fehlenden Positionen sind kein Regelfall, sondern eine Lieferfrage.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **becca23047**,
**#7627** und **#4939**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, **keine Bestellnummer geraten**, keine Bildinhalte gedeutet, keine
Aussage zum Lieferumfang, keine Zustellprognose, keine 7–21-Tage-Formel, kein
Label gesetzt.

---

## Lauf 17:20 UTC — #6936, und warum drei Bestellungen heute „nicht auffindbar" waren

### 🔎 Der Suchfehler, nicht die Bestellung

Die Mail von **16:52** kam von `lisac131@**googlemail**.com`. Die Suche
`email:lisac131@googlemail.com` in Shopify liefert **nichts**.

Die Kundensuche nach dem **Nachnamen** liefert sofort **#6936 Miss L Steggel** —
hinterlegt ist dort `LisaC131@**gmail**.com`.

**Es ist dieselbe Mailbox.** `googlemail.com` und `gmail.com` sind bei Google
Aliasse; Kunden in Grossbritannien und Deutschland schreiben oft aus der
Googlemail-Variante. **Die Shopify-Suche `email:` vergleicht die Zeichenkette
exakt und findet solche Fälle nicht.**

**Das ist ein Befund über die eigene Suchmethode, nicht über die Kunden** — und
er ist heute dreimal aufgetreten:

| Adresse | Stand |
|---|---|
| `lisac131@googlemail.com` | **aufgelöst** über die Namenssuche → #6936 |
| `dinod28@aol.com` (11.09.) | **weiterhin offen** — kein Name bekannt, Namenssuche nicht möglich |
| `becca23047@aol.com` (heute 15:20) | **weiterhin offen** — Bestelldaten liegen nur als Bild vor |

**Empfehlung:** Bei „keine Bestellung gefunden" künftig **zusätzlich über den
Nachnamen** suchen, bevor der Fall als nicht zuordenbar geführt wird. Für die
beiden `@aol.com`-Fälle hilft das nicht, weil dort kein Name im Text steht —
**diese beiden bleiben Owner-Sache.**

**Frühere Aussagen im Log werden dadurch nicht falsch**, aber sie waren
unvollständig: bei `dinod28@aol.com` steht im Eintrag vom 11.09., die Suche sei
„weder über die Bestell- noch über die Kundensuche" erfolgreich gewesen — die
Kundensuche lief dort über die **Adresse**, nicht über einen Namen, weil keiner
bekannt war. Das bleibt so.

---

### 🚩 #6936 Lisa Steggel — „after reading your advert"

**Shopify:** #6936, bestellt **21.08. 08:03**, **27,95 £**, `PAID` /
`FULFILLED`, **2 × Plushie** (monkey, donkey), versandt **02.09. 10:40** ab
Kirchstr. 2, Yanwen Special Line `UL476302846YP`. **Zwölf Tage** bis zum
Versand.

**16:52**, zwei Fotos plus ein Google-Drive-Link:

> „Received my parcel **today** and **Mr Donkey has not even lasted an hour**
> with Bert. **The squeak is out now** and Mr Donkey is dead. I was hoping it
> would survive a little longer **after reading your advert**."

**Drei Punkte:**

1. **Sie verlangt nichts.** Kein Geld, kein Ersatz, keine Rücksendung. Sie
   berichtet — freundlich, mit Humor („Mr Donkey is dead"). **Das ist der dritte
   solche Fall an diesem Tag** nach **#4939 Sara Thompson** und, gestern,
   **#7101** und **#7271** — bei den letzten beiden hat die Vorlagen-Absage
   genau daraus eine Eskalation gemacht.
2. **„after reading your advert"** — Werbebezug, ohne Wortlaut. Sie zitiert
   nichts, sie beruft sich nur darauf. Ein achter Wortlaut kommt damit **nicht**
   dazu; der Bot trägt keine Formulierung ein, die nicht dasteht.
3. **„The squeak is out now."** Der Quietscher liegt frei. Sie schreibt
   **nicht**, dass der Hund ihn verschluckt hat — **das wird nicht
   hineingelesen.** Der Punkt gehört aber in die Antwort: beim Quietscher ist
   das schon bei **#6286** und **#6280** aufgetreten.

**Zweites Teil ungeklärt:** Bestellt sind **zwei** Plüschtiere, zerstört ist der
Esel. Ob der Affe unbenutzt ist, sagt sie nicht — **wird gefragt, nicht
angenommen.** Vierter Fall dieser Art heute nach #7165, #6781, #7246.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** ausdrücklicher Bezug auf die Werbung als Kaufgrundlage,
mit Fotobeleg.

**Nicht auf der Erstattungsliste** — Kauschaden, und sie fordert nichts. Ein
etwaiger Regel-2-Anteil für den Affen **erst nach ihrer Antwort**, dann im Admin
zu bestimmen.

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#6936**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, kein
Verschlucken hineingelesen, keine Werbeformulierung erfunden, kein Anteil
geschätzt, kein Label gesetzt.

---

## Lauf 18:20 UTC — drei Fälle: #6891, #7506, #6528

### 🚩 #6891 Michael Palermo — die schärfste Formulierung des Regel-2-Problems bisher

**17:29**, Betreff: **„Your toys are not what you advertise - ORDER 6891"**

> „We finally received the **'indestructible'** plush chew toys and our Aussie
> **destroyed 2-3 in the span of 5 minutes** or so.
>
> **Please change your advertising** to reflect that they are for heavy chewers
> as that is not the case at all. Also, **your return policy could reflect a
> year so as long as you do not test the product with your pet. Not being able
> to return something that is not what is promised is not a return policy.**
>
> I am very disappointed **in myself** for believing the claims made on the
> website as it is **no where near the truth** of what we received."

**Shopify:** #6891, bestellt **20.08. 23:10**, **43,92 £**, `PAID` /
`FULFILLED`, Tags `Kaching Bundles`, `UpCart Rewards`, drei Positionen
(Plushie monkey, Plushie pig, Zahnbuddy „Blue Mop Plush Dog"), versandt
**02.09. 10:37** ab Kirchstr. 2, **JQ Express US `JCHSG0000004362459`**,
Fairport, New York. **Dreizehn Tage** bis zum Versand.

**Zwei Dinge, und beide sind keine Erstattungsforderung:**

1. **„Please change your advertising."** **Fünfter Kunde**, der das ausdrücklich
   verlangt — nach #6280 und #6286 heute und zwei Fällen am 10.09.
2. **Der Satz zur Rückgabepolicy ist die präziseste Fassung des Problems, die
   bisher im Postfach stand:** *„Not being able to return something that is not
   what is promised is not a return policy."* Das ist die **dritte unabhängige
   Formulierung** des Regel-2-Konstruktionsfehlers — nach **#7101 Cameron
   Herpich** (gestern) und **#7316 Brett Merriman** (heute Mittag). Drei Kunden,
   drei Länder, dieselbe Beobachtung.

**Er verlangt kein Geld.** Vierter Fall an diesem Tag ohne jede Forderung —
nach #4939 Sara Thompson, #6936 Lisa Steggel und, gestern, #7101 und #7271.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage im Betreff und im Text,
ausdrückliche Forderung nach Änderung von Werbung **und** Rückgabepolicy.
**Nicht auf der Erstattungsliste** — Kauschaden, keine Forderung.

---

### #7506 Adam Dowell — die Teilerstattungs-Vorlage ist wieder im Umlauf

| Zeit | Vorgang |
|---|---|
| **10.09. 18:19** | „**i would like to return these**, they are **extremely smaller** than i thought when i purchased for the price" |
| **12.09. 10:38** | **30-%-Teilerstattungsangebot**: „**Rather than going through the return process**, we'd like to offer you a **30% partial refund** … allowing you to keep the items **without needing to return them**" |
| **12.09. 17:32** | „Can we do **50%**, feel slighted with **size** and **'indestructible'** cause he had them **destroyed in literally 5 minutes**. If you cant do 50% **ill take the 30%** and **do you have bigger ones??**" |

**Shopify:** #7506, bestellt **24.08. 01:58**, **28,51 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (donkey, Elk), versandt
**03.09. 07:36** ab Kirchstr. 2, **4px US `4PX3003124889497CN`**, Macomb,
Michigan. **Zehn Tage** bis zum Versand. **Zwölfter Kunde aus dem
Versandstapel vom 03.09.**

**Drei Befunde:**

1. **Ein neues Teilerstattungsangebot ist heute rausgegangen.** Nach der
   Chronologie im Log vom 10.09. (zwölf Angebote seit dem 22.08.) ist das
   **mindestens das dreizehnte**. Es ging raus, **nachdem** die Chronologie
   zwei Tage im Log stand.
2. **Er hatte am 10.09. um eine Rücksendung gebeten** — wegen der **Grösse**,
   nicht wegen eines Kauschadens. Zu diesem Zeitpunkt war die Ware
   höchstwahrscheinlich unbenutzt und damit ein **Regel-2-Fall mit vollem
   Anspruch**. Statt der Rücknahme kam zwei Tage später ein Prozentangebot.
   **In der Zwischenzeit hat der Hund die Teile zerstört** — der Regel-2-Weg ist
   damit zu. **Derselbe Ablauf wie bei dinod28 und #5186.**
3. **Er will weiterhin kaufen.** „do you have bigger ones??" — die Frage steht
   unbeantwortet im Raum und ist die einzige im ganzen heutigen Postfach, die
   nach einem weiteren Kauf klingt.

→ `Bot/Needs Approval`. **Bewusst nicht `Escalated`:** Er nennt zwar
„indestructible" und fühlt sich „slighted", droht aber nichts an, zitiert keine
Behörde und will verhandeln. Der offene Punkt ist eine **kaufmännische
Entscheidung** — 30 % oder 50 % — und die gehört dem Owner, nicht einer
Eskalationsschleife.

**Nicht auf der Erstattungsliste** — kein Regelfall mehr, seit die Ware benutzt
ist. **Der Prozentsatz ist Owner-Entscheidung; der Bot schlägt keinen vor.**

---

### 🚩 #6528 Tommy Johnson — fünfter Kontakt, 37 Stunden

**17:23**, vollständiger Text:

> „Hi Lisa, **Just wanted to check in on this again.** Thank you, Tommy"

Er bezieht sich auf seine Mail vom **11.09. 03:54**:

> „I understand that the destroyed stuff cannot be returned, but I ordered
> multiple in this order. **Could you please set up a return for the other 3
> stuffies** that I have not opened?"

**Seither unbeantwortet — 37 Stunden 29 Minuten.**

**Das ist der fünfte Kontakt in diesem Vorgang.** Der Fall steht seit dem
**09.09.** im Log, dort namentlich mit der Vorhersage, dass eine
Kauschaden-Absage hier falsch wäre; sie ging am 10.09. trotzdem raus. Am 11.09.
wurde er als **vierte Wiederholung derselben Verwechslung** erfasst.

**Sein Anliegen ist unstrittig:** drei von vier Plüschtieren **ungeöffnet**,
Rücksendung verlangt, **Regel 2**, voller Anspruch auf den entsprechenden
Anteil. **Blockiert durch die fehlende Rücksendeadresse** — heute **dreissig
Tage** offen.

**Er ist höflich geblieben. Über fünf Kontakte und zwei Wochen.**

→ `Bot/Escalated - Owner Attention` (bleibt).
**Auf der Erstattungsliste:** Anteil für **drei von vier ungeöffneten**
Plüschtieren, Regel 2 — Betrag im Admin zu bestimmen.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#6891**, **#7506**
und **#6528**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, **kein
Prozentsatz vorgeschlagen**, keine Rücksendeadresse erfunden, keine Aussage zu
grösseren Varianten (nicht geprüft), kein Anteil geschätzt, kein Label gesetzt.

---

## Lauf 19:20 UTC — #6420 und #5032

### 🚩 #6420 Keith Grice — als zugestellt gescannt, nie erhalten

**19:16**:

> „I am requiring about order number #6420. I went on the site to find out if
> there was an update on the package. **I didn't know there was a third party
> delivery service.** When I clicked on the tracking, it states it was
> **delivered on August 25th in a locker**. **I received no information that I
> had a package and I have not received the item.** I tried to go to the third
> party site but **it is not opening up for me**. I was hoping you can help me."

**Shopify:** #6420, bestellt **16.08. 21:24**, **30,54 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (donkey, monkey), versandt
**18.08. 07:45** ab Kirchstr. 2, **JQ Express US `JCHSG0000004217579`**,
Orlando, Florida.

**Das ist eine Fallart, die im Log bisher nicht vorkam.** Keine Verzögerung,
kein Kauschaden: die Ware ist **als zugestellt gescannt** — am **25.08. in
einen Paketkasten** — und der Kunde hat sie nie bekommen und nie eine
Benachrichtigung erhalten. **Achtundzwanzig Tage** liegen zwischen dem
Zustellscan und seiner Mail.

**Drei Dinge, die er sagt und die stimmen:**

1. Er wusste nichts von einem Drittzusteller. In der Bestellbestätigung steht
   „Standard"; der Zusteller taucht erst in der Versandmail auf.
2. Die Trackingseite öffnet bei ihm nicht.
3. Eine Zustellbenachrichtigung hat er nicht erhalten.

**Nach `support-policy.md` darf er nicht an den Zusteller verwiesen werden.**
Das ist hier besonders wichtig: er hat es bereits selbst versucht und kommt
nicht durch.

**Nebenbefund zur Versanddauer:** **zwei Tage** von der Bestellung bis zum
Versand — bei einer Bestellung vom **16.08.** Die Verzögerung im August war
also **nicht durchgängig**: #4726 sechzehn Tage, #4745 sechzehn Tage, #5032
siebzehn Tage, aber #6420 zwei Tage. **Die bisherige Formulierung „die
Verzögerung betraf die Augustbestellungen" ist zu grob** — sie traf einen Teil
von ihnen.

→ `Bot/Needs Approval`. **Kein Regelfall** — nicht defekt, nicht unbenutzt
zurückgegeben, nicht vor Versand storniert. **Ob Ersatz oder Erstattung, ist
Owner-Entscheidung.** Was der Bot tun kann: die Nummer und den Trackinglink
nennen, den Sachverhalt festhalten und **nicht** an JQ Express verweisen.

**Nicht auf der Erstattungsliste** — kein Regelfall.

---

### #5032 Adam Murgatroyd — alle drei, eine Stunde, keine Forderung

**18:38**, mit Fotos:

> „**All of these toys** have been destroyed **within 1 hour** of giving them to
> our dog. **He loves them** but they simply **aren't suitable for him**. Really
> disappointed with them and **won't order again**."

**Shopify:** #5032, bestellt **08.08. 06:24**, **42,90 £**, `PAID` /
`FULFILLED`, Tags `Kaching Bundles`, `UpCart Rewards`, drei Positionen
(Zahnbuddy „Blue Mop Plush Dog", Plushie frog, Plushie pig), versandt
**25.08. 01:41** ab Kirchstr. 2, Yanwen Special Line `UL451107611YP`, West
Kilbride, Schottland. **Siebzehn Tage** bis zum Versand.

**Er verlangt nichts.** Kein Geld, kein Ersatz, keine Rücksendung, kein Zitat
aus der Werbung. **Fünfter Fall an diesem Tag ohne jede Forderung** — nach
#4939, #6936, #6891 und #6280.

**Alle drei Teile sind zerstört** — es gibt **keinen Regel-2-Rest**.

**„He loves them but they simply aren't suitable for him"** ist der freundlichste
Satz im heutigen Postfach. **„Won't order again"** ist die Folge. Wie bei
#7627 Charlotte Matthews heute Nachmittag: keine Eskalation, sondern ein
Kunde, der aufhört.

→ `Bot/Draft Ready`. Kein Eskalationstrigger: keine Forderung, kein
Werbezitat, keine Drohung, keine Behörde, Erstkontakt.
**Nicht auf der Erstattungsliste** — Kauschaden, keine Forderung.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#6420** und
**#5032**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, **kein
Verweis an den Zusteller**, keine Zustellprognose, keine Aussage darüber, wo
das Paket ist, kein Label gesetzt.
