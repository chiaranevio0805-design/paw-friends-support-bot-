# Backlog-Triage 2026-09-10

Der Gmail-Schreibpfad bricht weiterhin ab (seit 21.08.) — keine Entwürfe, keine
Labels, kein Text rekonstruiert.

---

## Lauf 00:20 UTC — fünf Fälle in 45 Minuten

Zwischen **23:29 und 00:14** sind fünf Kundenmails eingegangen. Alle fünf
Bestellungen wurden **am selben Tag versandt: 02.09.** — der Tag, an dem ein
großer Versandstapel rausging (siehe #7274, #7053, #6999, #7114, #7190, #6751).
Sie kommen jetzt alle gleichzeitig an.

### 🚩 #7179 Keith Crane — Füllwatte gefressen, und zwei ungeöffnete Teile

**23:29**, Betreff „**Junk**":

> „I received my order today with the 3 toys for my dog. **48 dollars** for
> these things is a joke… my dog destroyed this in less than 30 minutes and is
> **now eating the cotton!** **I only opened the donkey.** **I would like to
> return these** and I expect a full refund. These were supposed to be
> **indestructible**. What a joke."

**Shopify, geprüft 10.09. 00:2x UTC:**

- **#7179**, bestellt **22.08. 13:37 UTC**, **35,64 £**, `PAID` /
  **`PARTIALLY_FULFILLED`**
- 3 × Plushie (frog, donkey, monkey) + 1 × E-Book
- Versandt **02.09. 10:52 UTC** — elf Tage nach der Bestellung
- Yanwen Special Line US, `UL476310958YP`

**Drei Sachverhalte in einer Mail — und die Vorlage trifft nur den ersten:**

1. **Kauschaden am donkey** → keine Erstattung nach der Regel.
2. **🚩 Sicherheitsvorfall: „is now eating the cotton"** — der Hund frisst die
   Füllung, **jetzt gerade**. Das ist die **achte** Meldung über verschluckbares
   Material (#6283, Andy Sire, Kevin Saggers #3197, #6741, die Nadel in #1301,
   der Quietscher in #6286, jetzt #7179). Es ist die erste, die einen laufenden
   Vorgang beschreibt.
3. **Regel 2: „I only opened the donkey"** — **zwei von drei Plüschtieren sind
   ungeöffnet.** Er verlangt ausdrücklich „I would like to **return these**".
   Dafür besteht ein **voller Erstattungsanspruch** auf den entsprechenden
   Anteil.

**Das ist exakt die Konstellation, die heute schon dreimal falsch behandelt
wurde:** Carolyn Marmalejo (#4812, 21.08.), Tommy Johnson (#6528, heute 01:43)
und Stephen Cooil (#5973, heute 11:10 abgelehnt). Eine Kauschaden-Absage würde
den ungeöffneten Teil erneut übergehen.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** laufender Sicherheitsvorfall (Hund frisst
Füllmaterial), bestrittene Werbeaussage, Rückgabeverlangen für unbenutzte Ware.
**Erstattungsanspruch für die zwei ungeöffneten Plüschtiere** — Anteil von
35,64 £, im Admin auf Positionsebene zu bestimmen, **nicht schätzen**.

**Betragsdifferenz:** Er nennt **48 $**, Shopify führt **35,64 £**. Vor jeder
Zusage klären — dasselbe Problem wie bei #4975 Darlene Futrel gestern Abend.

**Nebenbefund:** `PARTIALLY_FULFILLED` — er spricht von drei Spielzeugen und hat
drei erhalten; offen ist damit das **E-Book**. Achte Teilsendung.

### #6760 Sofia Christopoulos — Australien, 14 Minuten

**00:01**, Betreff „Order 6760":

> „We received delivery today. **Within 14 minutes** the toy had already been
> destroyed. **Unfortunately not indestructible as per your ad.** Kindly arrange
> a refund **as part of your 30 day refund**. Happy to…"

**Shopify:** **#6760**, bestellt **20.08. 00:22 UTC**, **30,54 £**, `PAID` /
`FULFILLED`, versandt **02.09. 10:30 UTC**, 4PX Standard Registered,
`4PX3003122360714CN`, Bentleigh East, **Australien**.
Bestell-Adresse: `soph_tots@hotmail.com` — sie schreibt von
`schristopoulos@openwayfood.com.au`.

Kauschaden → keine Erstattung. **Aber sie beruft sich auf die 30-Tage-Regel**,
wie **#6286 Deborah Gould** gestern 04:16 und `bev212.bs` am 06.09. — **vierter
Fall** dieses Missverständnisses. Und der Fristteil stimmt auch bei ihr:
bestellt 20.08., heute 10.09., **21 Tage** — **innerhalb** der 30.

→ `Bot/Needs Approval`. Die Antwort muss **Frist und Geltungsbereich trennen**;
ihr zu schreiben, die 30 Tage griffen nicht, wäre unzutreffend.

### #7101 Cameron Herpich — Australien, freundlich

**23:36**, mit Foto:

> „These arrived this morning in the Post Office. Unfortunately they are **not
> indestructible**. Please see photo and **the current champion**. We will
> **keep trying** to get a product that he cannot chew…"

**Shopify:** **#7101**, bestellt **22.08. 01:03 UTC**, **28,32 £**, `PAID` /
`FULFILLED`, versandt **02.09. 10:48 UTC**, Yanwen Special Line
`UL476307375YP`, North Lakes, **Australien**.

**Er verlangt keine Erstattung.** Er meldet den Befund, schickt ein Foto und
sagt, er werde es weiter versuchen. Nach Greg Williams (#6044) und John Beirne
(#3344) gestern ist er der **dritte** Kunde in zwei Tagen, der die Werbeaussage
bestreitet, **ohne Geld zu fordern**.

→ `Bot/Draft Ready`. Freundlich antworten, den Ton aufnehmen, **keine
Vorlagen-Absage** — es gibt hier nichts abzulehnen, weil nichts gefordert wird.
Eine Absage auf eine Mail ohne Forderung wäre der vermeidbarste Fehler im
ganzen Postfach.

### #7271 Rosalind Welch — Geschenk

**00:01**, Betreff „Order":

> „Sent this toy as a **gift**. The dog pull off ears in **less than 1 hour**.
> **Your claim was not true.** Very disappointed."

**Shopify:** **#7271**, bestellt **22.08. 22:50 UTC**, **20,34 £**, `PAID` /
`FULFILLED`.

Kauschaden, bestrittene Werbeaussage, keine ausdrückliche Erstattungsforderung.
Besonderheit: **sie ist nicht die Halterin** — das Spielzeug war ein Geschenk.
→ `Bot/Needs Approval`, erklärende Antwort statt Vorlage.

### #7001 Keith Furman — Lieferanfrage

**00:14:** „**Where is my order!**"

**Shopify:** **#7001**, bestellt **21.08. 15:16 UTC**, **20,35 £**, `PAID` /
`FULFILLED`, versandt **02.09. 10:43 UTC**, **WB US**,
`WNBAA0497780784YQ`, Seaford (US).

Zwölf Tage bis zum Versand, seither acht Tage.
→ `Bot/Draft Ready`. Versanddatum und Nummer nennen, die zwölf Tage offen
benennen. **Kein Zustelldatum.**
⚠️ Die Nummer gehört zur Familie `WNBAA…YQ` — bei Robert Gagne vom Zusteller
für **ungültig** erklärt, bei #6872 „order not found", gestern auch bei #7741
und #7784. **Vierter Fall.** Nummer nennen, aber **nicht zusagen**, dass die
Verfolgung funktioniert.

---

## Befund dieses Laufs

**Der Versandstapel vom 02.09. kommt jetzt an.** Alle fünf Bestellungen wurden
an diesem Tag verschickt, nach elf bis dreizehn Tagen Liegezeit. Vier der fünf
Kunden melden innerhalb von Minuten bis Stunden nach Erhalt einen Schaden.

**Zwei der fünf verlangen kein Geld** (#7101 Cameron Herpich, #7271 Rosalind
Welch). Damit sind es seit gestern **fünf** Kunden, die die Werbeaussage
bestreiten, ohne eine Erstattung zu fordern — #6044, #3344, #7101, #7271 und
teilweise #6259.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Betrag
geschätzt, keine Betragsdifferenz überbrückt, kein Text rekonstruiert, keine
Rücksendeadresse erfunden.

---

## Lauf 02:20 UTC — #6280 Jasin Vandenbroeke: aus einem Lieferfall wird ein Kauschaden

**Shopify, geprüft 10.09. 02:2x UTC:**

- **#6280**, bestellt **15.08. 22:02 UTC**, **30,56 £**, `PAID` / `FULFILLED`
- 2 × Plushie (Little Bear, hippo)
- Versandt **20.08. 02:16 UTC** — fünf Tage, ungewöhnlich schnell für diesen
  Zeitraum
- 4PX Economic Registered, `4PX3003082535801CN`, Dudley (US)

**Verlauf:**

- **29.08. 14:51**, Betreff „**I want a refund**": „This is taking too long for
  the items to get to me. It's going on **11 or so days**."
- **31.08. 09:39 aus dem Postfach:** die Liefer-Vorlage — „has been shipped and
  is currently on the way… **UK warehouse is currently sold out**… Delivery
  usually takes **7–21 days**… **At around 11 days, your order is still within
  the usual delivery timeframe** and should arrive as soon as possible."
  **Keine Sendungsnummer**, obwohl sie seit dem 20.08. vorlag.
- **10.09. 02:16**, mit Foto:

> „The dog toys **did not last** — it took my dog **less than 20 minutes** to
> tear them open and **get the squeaker out**. Given the poor quality and
> durability issues, I [would] like to request a **full refund**."

### Zwei Beobachtungen

**1. Der Fall hat die Kategorie gewechselt.** Er hat als Lieferbeschwerde
begonnen und ist nach der Zustellung ein Kauschadensfall geworden. Der
Betreff „I want a refund" steht seit dem 29.08. im Thread — jetzt aber aus
einem völlig anderen Grund. Wer nur den Betreff liest, beantwortet den
falschen Fall.

**2. „get the squeaker out" — neunte Meldung über lose Kleinteile**, nach
#6283, Andy Sire, Kevin Saggers (#3197), #6741, der Nadel in #1301, dem
Quietscher in #6286, der Füllwatte in #7179 (vor zwei Stunden) und dem
Größenrisiko bei #4975. Er meldet **kein** Verschlucken, und das gehört ihm
nicht unterstellt.

**Klassifikation: Kauschaden → keine Erstattung nach der Regel.**

→ `Bot/Needs Approval`. **Keine Vorlagen-Absage** — bei sechs von sechs am
09.09. hat sie eskaliert. Die Antwort muss außerdem berücksichtigen, dass ihm
am 31.08. bereits eine Antwort geschickt wurde, die **die Sendungsnummer
wegließ**, obwohl sie seit elf Tagen im System lag. Das ist der **siebte**
Fall dieser Art (#7771, #6751, #8295, #6199, #6872, #6044, jetzt #6280).

**Nicht auf der Erstattungsliste** — Kauschaden fällt unter keine der drei
Regeln.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Verschlucken
unterstellt, kein Text rekonstruiert.

---

## Lauf 03:20 UTC — 🚩🚩🚩 zwei schwere Fälle

### 🚩🚩🚩 #8253 Tim Kipling — Storno bestätigt, Erstattung bestätigt, Ware trotzdem versandt, Geld nie zurück

**Der gravierendste Vorgang in diesen Logs.** Drei schriftliche Zusagen, keine
davon eingehalten.

**Shopify, geprüft 10.09. 03:2x UTC:**

- **#8253**, bestellt **30.08. 13:18 UTC**, **44,04 £**
- **Status: `PAID` / `FULFILLED`** — **keine Erstattung im System**
- **Versandt 08.09. 07:45 UTC**, 4px US, `4PX3003140315567CN`
- 1 × Zahnbuddy + 2 × Plushie (monkey, Duck), Chula Vista, Kalifornien

**Der Verlauf, vollständig:**

| Zeit | Ereignis |
|---|---|
| **30.08. 13:18** | Bestellung |
| **30.08. 14:31** | **Storno nach 73 Minuten:** „Please cancel my order and **do not ship the product**… I have notified my bank to stop payment." |
| **01.09. 11:49** | Aus dem Postfach: *„We can confirm that your order **has been cancelled as requested**. **The product will not be shipped**."* |
| **01.09. 19:35** | Kunde: „Per your email you stated that this order was canceled and I would not be charged. **You have since charged me**, have not canceled order — as per the email I received stating it was being shipped…" |
| **03.09. 09:54** | Aus dem Postfach: Entschuldigung für „the confusion" |
| **04.09. 23:46** | Kunde: „**When will I see my refund**… It appears that you are making **no effort** to refund my funds." |
| **06.09. 09:53** | Aus dem Postfach: *„I can confirm that your **refund has now been processed** to your original payment method."* |
| **08.09. 07:45** | **Shopify: Sendung angelegt und verschickt** — **zwei Tage nach der Erstattungsbestätigung**, zehn Tage nach dem Storno |
| **10.09. 02:23** | Kunde: „**This is my last request before I turn this over as a fraudulent transaction to the Fraud Department of the Better Business Bureau and Commerce Department.**" |

### Was hier belegt ist

1. **Das Storno kam 73 Minuten nach der Bestellung** — es gab kein
   Zeitfenster-Problem. **Regel 3** greift eindeutig.
2. **Die Stornierung wurde schriftlich bestätigt** („will not be shipped") und
   **nicht ausgeführt**.
3. **Die Erstattung wurde schriftlich bestätigt** („has now been processed") und
   **ist in Shopify nicht vorhanden** — der Status steht unverändert auf `PAID`.
   Das ist der **zweite** Fall dieser Art nach **#5841** (Log 01.09.).
4. **Die Ware ist zwei Tage nach der Erstattungsbestätigung rausgegangen.**

**Siebter Fall des Musters** „storniert verlangt, nicht storniert, Ware raus":
#4617, #3944, #4212, #5474, #6173, #6870, **jetzt #8253** — und der einzige, bei
dem zusätzlich eine Erstattung fälschlich als erledigt gemeldet wurde.

→ `Bot/Escalated - Owner Attention`, **höchste Priorität, noch vor #4975**.
**Eskalationsgrund (nur fürs Log):** Betrugsvorwurf mit angekündigter Meldung an
**BBB Fraud Department** und **Commerce Department**, zwei nicht eingehaltene
schriftliche Zusagen, laufende Bankmeldung, fünfter Kontakt.

**⚠️ ERSTATTUNG: 44,04 £, Regel 3 — vor Versand storniert.** Sie ist ihm am
06.09. schriftlich bestätigt worden. Bis sie tatsächlich ausgeführt ist, steht
eine schriftliche Zusage unerfüllt im Raum — das ist der Kern seines
Betrugsvorwurfs. **Keine weitere Zusage senden, bevor die Zahlung im
Zahlungsanbieter sichtbar ist.**

**Nicht senden:** irgendeine Bestätigung, dass die Erstattung „bearbeitet wird".
Genau dieser Satz steht seit dem 06.09. im Thread und ist der Grund für seine
letzte Mail.

### 🚩 #7292 Tracy Hartley — ein Etikett wurde verschluckt

**03:10**, weitergeleitete Bestellbestätigung:

> „My order took **18 days to arrive** and less than 20 minutes for my dog to
> destroy the Pig. I looked at the sales page and **don't find any mention of
> the fact that they have squeakers, which encourage aggression**. I would NEVER
> buy a squeaker toy for any dog…
> What is the **return procedure**? I will gladly return **the unopened duck**
> and the pig that's missing an ear… and **the tag that my dog swallowed**
> before I knew the toy was clearly NOT indestructible!
> I've been so looking forward to these indestructible toys. **I feel so stupid
> now.**"

**Shopify:** **#7292**, bestellt **22.08. 23:53 UTC**, **28,50 £** (Kundin nennt
**$38,90**), `PAID` / `FULFILLED`, 2 × Plushie (Duck, pig), versandt **02.09.
10:58 UTC**, 4px US `4PX3003122374414CN`, Alhambra, Kalifornien.

**Drei Punkte:**

1. **🚩 „the tag that my dog swallowed" — ein tatsächlich verschlucktes Teil.**
   Nicht „möglicherweise", nicht „könnte": sie berichtet es als geschehen. Das
   ist die **zehnte** Meldung dieser Art und nach #6283 und Andy Sire der
   **dritte bestätigte Verschluckungsvorgang**. Sicherheitsbefund.
2. **Regel 2: „the unopened duck"** — ein Teil ist ungeöffnet, sie will es
   zurückgeben und fragt ausdrücklich nach dem **Rückgabeverfahren**. **Es gibt
   keine Rücksendeadresse** (offener Blocker seit 13.08.). Das gehört ihr
   ehrlich gesagt.
3. **Produktinformation:** Sie wirft vor, die **Quietscher** seien auf der
   Verkaufsseite nicht erwähnt. Das ist **der vierte shop-eigene Text** in zwei
   Tagen, an dem sich ein Kunde festmacht — nach „With replacement guarantee"
   (#6259), der Lieferzusage (#7190) und dem Artikelnamen (#4851). Diesmal geht
   es nicht um eine falsche Angabe, sondern um eine **fehlende**.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** bestätigter Verschluckungsvorfall,
bestrittene Werbeaussage, Vorwurf fehlender Produktinformation,
Rückgabeverlangen für unbenutzte Ware.

**Erstattungsanspruch für den ungeöffneten Duck** — Anteil von 28,50 £, im Admin
auf Positionsebene zu bestimmen. **Betragsdifferenz** (28,50 £ vs. $38,90) vor
jeder Zusage klären — dritter Fall nach #4975 und #7179.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, keine
Rücksendeadresse erfunden, kein Betrag geschätzt, keine Zusage zu #8253
wiederholt.

---

## Lauf 04:20 UTC — #6952 Daniel Piekarski: „Not asking for a refund"

**04:05**, Betreff „Order #6952", ein Foto beigefügt:

> „Was really excited to get these **Plushies – Designed for Furry Friends Who
> Destroy Everything**.
> Unfortunately, the fox **didn't even last 10 minutes** before it started
> coming apart.
> **Not asking for a refund, just providing feedback** that there's **no way any
> of the stuff that 'makes these different' is accurate**."

**Shopify, geprüft 10.09. 04:2x UTC:**

- **#6952**, bestellt **21.08. 11:00 UTC**, **28,50 £**, `PAID` / `FULFILLED`
- 2 × Plushie (Elk, fox)
- Versandt **02.09. 10:40 UTC** — zwölf Tage nach der Bestellung
- 4PX Standard Registered, `4PX3003122368741CN`, Belgrave, Victoria,
  **Australien**

**Wieder aus dem Versandstapel vom 02.09.** — der sechste Fall daraus in vier
Stunden (#7179, #6760, #7101, #7271, #7001, jetzt #6952).

### Einordnung

Er sagt **zweimal ausdrücklich**, dass er kein Geld will: „Not asking for a
refund, just providing feedback." Was er stattdessen sagt, ist eine
Produktaussage: **„there's no way any of the stuff that ‚makes these different'
is accurate"** — er bezieht sich damit nicht auf ein einzelnes Wort, sondern auf
den **gesamten Differenzierungsanspruch** des Produkts.

**Das ist der sechste Kunde in zwei Tagen, der die Werbeaussage bestreitet, ohne
eine Erstattung zu fordern:**

| Datum | Kunde | Was er stattdessen will |
|---|---|---|
| 09.09. 10:03 | Greg Williams (#6044) | „it'll be good if you guys **changed your ad**" |
| 09.09. 11:11 | John Beirne (#3344) | „your **marketing** doesn't make claims…" |
| 09.09. 18:18 | Rod Smith (#7559) | nichts — abgeschlossen |
| 10.09. 23:36* | Cameron Herpich (#7101) | „We will **keep trying**" |
| 10.09. 00:01 | Rosalind Welch (#7271) | nichts — „Very disappointed" |
| **10.09. 04:05** | **Daniel Piekarski (#6952)** | **„just providing feedback"** |

*(#7101 am 09.09. 23:36 eingegangen)*

**Sechs von sechs** dieser Kunden nennen die Werbung als Kern. **Keiner** von
ihnen verlangt Geld. Das ist inzwischen kein Nebenbefund mehr, sondern die
zweitgrößte Gruppe im Postfach — und die einzige, bei der die Kauschaden-Absage
**nichts** zu verweigern hätte, weil nichts gefordert wird.

→ `Bot/Draft Ready`. Freundlich, kurz, **den Hinweis annehmen statt ihn
abzuwehren**. Keine Erwähnung der Rückgabepolicy — er hat nicht danach gefragt.
**Eine Vorlagen-Absage auf diese Mail wäre der vermeidbarste Fehler im ganzen
Postfach**, und es wäre der zweite Anlauf dazu: bei John Beirne (#3344) ist
gestern genau das passiert, sieben Minuten vor seiner Antwort.

**Nicht auf der Erstattungsliste** — Kauschaden, und er verlangt ausdrücklich
keine Erstattung.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Text
rekonstruiert.
