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
