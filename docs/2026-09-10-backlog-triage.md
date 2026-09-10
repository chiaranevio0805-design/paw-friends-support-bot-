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

---

## Lauf 06:20 UTC — #7525 Carol Garvey: „The tracking information hasn't been updated either"

**06:07**, Betreff „Order 7525":

> „I had an email to say my order was **on its way on 3/9** and I **still
> haven't received it**. **The tracking information hasn't been updated
> either.** Please can you confirm when I will…"

**Shopify, geprüft 10.09. 06:2x UTC:**

- **#7525**, bestellt **24.08. 05:11 UTC**, **27,95 £**, `PAID` / `FULFILLED`
- 2 × Plushie (monkey, fox)
- Versandt **03.09. 07:37 UTC** — **zehn Tage** nach der Bestellung
- Yanwen Special Line Promotion, `UL478624631YP`
- Chelwood Gate RH17 7LS (UK)

### Der Punkt, der zählt

Sie hat die Sendungsnummer **bereits** — die Shopify-Versandbenachrichtigung vom
03.09. enthält sie. **Ihr Problem ist, dass sie nichts anzeigt.**

Damit ist sie der **vierte** Fall, in dem eine genannte Sendungsnummer beim
Zusteller keine Bewegung zeigt:

| Kunde | Bestellung | Zusteller | Befund |
|---|---|---|---|
| Robert Gagne | — | `WNBAA…YQ` | Zusteller: Nummer **ungültig** |
| Dorothy Rysh | #6872 | `WNBAA…YQ` | „**order not found**" |
| John Collins | #7053 | Yanwen US | „not showing any **information**" |
| **Carol Garvey** | **#7525** | **Yanwen** | „**hasn't been updated**" |

**Das ist ein anderes Problem als die fehlende Nummer.** Bei #7771, #6751,
#8295, #6199, #6872, #6044 und #6280 wurde die vorhandene Nummer nicht
weitergegeben. Hier ist sie weitergegeben worden und **nützt nichts**.

Für die Antwort heißt das: Die Nummer noch einmal zu nennen, wäre keine Hilfe.
Was ihr belegt gesagt werden kann, ist das **Versanddatum 03.09.**, der
**Zusteller** und die Tatsache, dass zwischen Bestellung und Versand **zehn
Tage** lagen — mehr steht in Shopify nicht. Ob die Sendung sich bewegt, ist von
hier aus **nicht feststellbar**, und das gehört ehrlich gesagt.

→ `Bot/Needs Approval` (nicht `Draft Ready`): Der Standardtext „your parcel is
currently progressing through the delivery network" wäre hier **nachweislich
unbelegt** — genau das bestreitet sie. Dieselbe Formel steckt in der
Liefer-Vorlage, die gestern an #7114, #7559 und am 01.09. an #7771 ging.

**Kein Zustelldatum, keine 7–21-Tage-Formel** (die Frist läuft bei ihr ohnehin
erst am 24.09. ab und beantwortet ihre Frage nicht), **keine Behauptung, die
Sendung sei in Bewegung.**

**Nicht auf der Erstattungsliste** — die Ware ist unterwegs, kein Regelfall.

**Nicht getan:** kein Entwurf, kein Label, keine Zustellprognose, nicht
behauptet, die Sendung bewege sich, kein Text rekonstruiert.

---

## Lauf 07:20 UTC — 🔧 #4035 Christina Williams: die Teilerstattungs-Chronologie war falsch

**Shopify, geprüft 10.09. 07:2x UTC:**

- **#4035**, bestellt **31.07. 16:21 UTC**, **27,95 £**, `PAID` / `FULFILLED`
- 2 × Plushie (donkey, hippo)
- Versandt **05.08. 04:32 UTC**, Yanwen, `UL393919026YP`

### Der vollständige Verlauf (`get_thread`, sieben Nachrichten)

| Datum | Wer | Inhalt |
|---|---|---|
| **19.08. 02:15** | Kundin | „I recently purchased 2 of your **'strong'** dog toys, my dogs **ripped them to bits in a day**. Can I have a refund please?" |
| **20.08. 20:33** | Postfach | Vorlagen-Absage („does not cover items that have been used or damaged by a…") |
| **21.08. 00:54** | Kundin | „**so what exactly does your 30 day money back guarantee cover?** for the toys that you claim are **super tough**? and **£15 each**? I would like a refund please. I have **pictures**…" |
| **22.08. 09:00** | Postfach | Antwort mit **20 % Teilerstattung** |
| **29.08. 14:43** | Kundin | „I would like a **full** refund please, **20 % is not enough**, the toys are rubbish, **a replacement will be the same**" |
| **31.08. 09:38** | Postfach | *„As a further goodwill gesture, we can **increase the offer to a 25 % partial refund** while you keep the toys."* |
| **10.09. 06:57** | Kundin | Foto beigefügt: „This was **within 24 hours of delivery**. **Why would I want a replacement or partial refund? I want my money back please**" |

### 🔧 Zwei Korrekturen an meinen eigenen Logs

**1. Die Teilerstattungs-Vorlage begann nicht am 26.08., sondern am 22.08.**

Im Log vom 08.09. (Lauf 23:20) steht die Chronologie mit **Sharon Lagos
(#5205, 26.08.)** als erstem Fall. Das ist falsch: **Christina Williams hat sie
am 22.08. bekommen** — vier Tage früher.

**2. Es gibt eine 25-%-Stufe, die in keinem meiner Logs stand.**

Am 31.08. wurde ihr **25 %** angeboten, ausdrücklich als Erhöhung des
vorherigen Angebots. Die bisher notierten Stufen waren 15 %, 20 % und 30 %.

**Die berichtigte Chronologie — neun Angebote, nicht sieben:**

| Datum | Kunde | Angebot | Anspruch nach Regel |
|---|---|---|---|
| **22.08.** | **Christina Williams (#4035)** | **20 %** | Kauschaden — kein Anspruch |
| 26.08. | Sharon Lagos (#5205) | 20 % | angenommen, **nie ausgezahlt** |
| 31.08. | Ken Beville (#6583) | 20 % | **voll (Regel 2)** — abgelehnt |
| **31.08.** | **Christina Williams (#4035)** | **25 %** | Kauschaden — abgelehnt |
| 01.09. | Ken Beville (#6583) | 30 % | **voll (Regel 2)** — abgelehnt |
| 03.09. | Trudi Trotter (#5148) | 30 % | **voll (Regel 2)** — abgelehnt |
| 05.09. | Viken Jehdian (#6546) | Teilbetrag | angenommen, **nie ausgezahlt** |
| 07.09. | Karen McCormick (#4606) | 15 % Rabatt | **voll (Regel 3)** |
| 07.09. | Sheila Keirnan (#1301) | 30 % | **voll (Regel 1 + 2)** |

**Neun Angebote in 16 Tagen, fünf davon gegen einen vollen Regelanspruch, zwei
angenommen und nie ausgezahlt, vier ausdrücklich abgelehnt.**

### 🔧 Dritte Korrektur: die Garantie-Frage ist älter als gedacht

Am **21.08.** fragte sie: „**what exactly does your 30 day money back guarantee
cover?**" Das ist **die früheste Fassung** dieser Frage — im Log vom 09.09.
hatte ich `bev212.bs` (06.09.) als ersten Fall notiert.

**Fünf Kunden, beginnend am 21.08.:** Christina Williams (21.08.),
`bev212.bs` (06.09.), Gary Lindsay #4273 (09.09., „the guarantee… is
**pointless**"), Deborah Gould #6286 (09.09.), Sofia Christopoulos #6760
(10.09.).

### Einordnung des heutigen Vorgangs

**Klassifikation: Kauschaden → keine Erstattung nach der Regel.** Ihr Anspruch
auf die vollen 27,95 £ ergibt sich aus den drei Regeln **nicht**.

**Aber:** Ihr sind zwei Teilbeträge angeboten worden (20 %, dann 25 %) — das ist
**kein** Bestandteil der Policy. Sie fragt jetzt zu Recht: „**Why would I want a
replacement or partial refund?**" Ein drittes Angebot würde denselben Weg
nehmen; das ist bei Ken Beville (#6583) nach zwei Angeboten dokumentiert.

Dazu: **Foto beigefügt**, Schaden **innerhalb von 24 Stunden nach Lieferung**,
**vierter Kontakt** seit dem 19.08.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** vierter Kontakt, bestrittene Werbeaussage
(„'strong'", „super tough"), zweimal abgelehntes Abwehrangebot, offene Frage zum
Geltungsbereich der Garantie seit dem 21.08. unbeantwortet.

**Nicht auf der Erstattungsliste** — Kauschaden. Ob ihr über die Regel hinaus
erstattet wird, ist eine **Owner-Entscheidung**; nach zwei eigenen Angeboten
steht die Sache aber anders da als bei einem Fall ohne Vorgeschichte.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, **kein drittes
Teilangebot**, kein Text rekonstruiert.

---

## Lauf 08:20 UTC — 🚩 #3770 Steph Bentley: eine Erstattung, die seit dem 03.09. zugesagt ist

### 🚩🚩 #3770 — der zweite Fall einer zugesagten und nicht gezahlten Erstattung binnen fünf Stunden

**Shopify, geprüft 10.09. 08:2x UTC:**

- **#3770**, bestellt **29.07. 11:23 UTC**, **19,95 £**
- **Status: `PAID` / `FULFILLED`** — **keine Erstattung im System**
- Versandt 30.07., Yanwen, `UL375777043YP`
- Bestell-Adresse `steph.bentley84@gmail.com`, sie schreibt von
  `steph.bentley84@googlemail.com`

**Der Verlauf, vollständig (`get_thread`, acht Nachrichten):**

| Datum | Wer | Inhalt |
|---|---|---|
| bis **11.08.** | Kundin | zwei Mails, unbeantwortet |
| **14.08. 10:26** | Kundin | Betreff: „**3rd CHASER NO RESPONSE**". „Please advise where I can return this awful small toy so I can obtain my **£20 refund** asap. **your reviews are false** as your communication is diabolical!" |
| **15.08. 16:09** | Postfach | *„Before we proceed, could you please let us know **the reason** you would like to return…"* — die **Rückfrage-Vorlage** |
| **15.08. 17:37** | Kundin | „**My reasoning is in the last 2 emails**… as per your returns policy I would like to return for a **full refund**, please advise **where to send** to" |
| **21.08. 10:51** | Kundin | „**Surprise surprise another week past and still no return details**" |
| **22.08. 09:15** | Postfach | „We have forwarded your return request to **the relevant team**" |
| **01.09. 20:35** | Kundin | „I have now waited **25 days** to return this item **within your return period**… I want my money back now" |
| **03.09. 09:57** | Postfach | *„**There is no need for you to return the item. We will**…"* — **Erstattung zugesagt** |
| **10.09. 07:53** | Kundin | „**Please advise when I will receive this refund**" |

### Was das bedeutet

**Das ist Regel 2 in Reinform** — unbenutzte Ware, Rückgabe innerhalb der Frist
verlangt (sie hat am 11.08. begonnen, elf Tage nach Lieferung). Nach der Policy:
volle Erstattung, „**no argument, no attempt to talk them out of it**".

Stattdessen:

1. **Die Rückfrage-Vorlage** („the reason you would like to return") — dieselbe,
   die am 22.08. an Todd Jacobs und Wendy Higgins ging und die die Policy für
   Rückgaben ausschließt. Sie hatte den Grund bereits zweimal genannt.
2. **Die Rücksendeadresse wurde nie genannt** — sie hat viermal danach gefragt.
   Es gibt keine (offener Blocker seit 13.08.).
3. **Am 03.09. wurde die Erstattung zugesagt** („no need for you to return the
   item"). **In Shopify steht die Bestellung sieben Tage später unverändert auf
   `PAID`.**

**Damit ist es der zweite Fall an einem Vormittag**, in dem eine schriftlich
zugesagte Erstattung nicht ausgeführt wurde — nach **#8253 Tim Kipling**
(zugesagt 06.09., heute Betrugsvorwurf). Insgesamt der **dritte** nach **#5841**
(Log 01.09.) und **#2228 Ann Price** (zugesagt 17.07., seit acht Wochen offen).

**Vier zugesagte, nicht ausgeführte Erstattungen** — #2228, #5841, #8253, #3770.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** fünfter Kontakt, offene Erstattungszusage
seit dem 03.09., Rückgabeverlangen seit dem 11.08. unerfüllt, Vorwurf gefälschter
Bewertungen („your reviews are false").

**⚠️ ERSTATTUNG: 19,95 £, Regel 2 — unbenutzt.** Sie ist bereits schriftlich
zugesagt. **Keine weitere Zusage senden, bevor die Zahlung ausgeführt ist** —
genau das ist bei #8253 der Auslöser für die Betrugsmeldung gewesen.

### #8081 Matthew Pierce — eine Militäranschrift, und das nächste Adressproblem

- **10.09. 07:14 aus dem Postfach:** „we noticed that **two different postcodes**
  have been provided… our system is **unable to recognise** the…"
- **10.09. 07:48 Kunde:** „Confirming my address: **Matthew Pierce, Box 5647
  PSC 3, APO AP 96266**"

**Shopify:** **#8081**, bestellt **29.08. 05:56 UTC**, **20,35 £**, `PAID` /
**`UNFULFILLED`** — seit **zwölf Tagen** nicht versandt.
Hinterlegt: `Box 5647 PSC 3`, **APO**, **Armed Forces Pacific**, `96266-0057`.

**Das ist eine US-Militärpostanschrift (APO/PSC)**, keine fehlerhafte Eingabe.
Die im System hinterlegte Adresse **stimmt bereits mit der überein**, die er
jetzt bestätigt hat — bis auf die vierstellige Postcode-Erweiterung `-0057`,
die vermutlich die „zwei verschiedenen Postleitzahlen" erklärt.

**Der Fall gehört zum PO-Box-Komplex** (#5817, #6209, #4606, `annafg72`): eine
Adressform, die das Versandsystem nicht verarbeitet, führt dazu, dass eine
bezahlte Bestellung liegen bleibt. Bei #4606 Karen McCormick hat genau das zu
zwei Stornierungen und einem Rabattangebot geführt; bei #6209 wurde am Ende doch
an die P.O. Box versandt.

**Offen und vom Bot nicht entscheidbar:** ob die Zusteller (4PX, Yanwen, WB US)
APO/FPO überhaupt beliefern. **Wenn nicht, ist das kein Adressproblem, sondern
ein Erstattungsfall** — und er wartet dann seit zwölf Tagen auf eine Sendung,
die nie rausgehen kann.

→ `Bot/Needs Approval`. **Nicht bestätigen, dass die Adresse jetzt passt** —
ungeprüft. **Keine Versandprognose.** Zuerst klären, ob APO zustellbar ist.

### Wieder aufgetaucht, unverändert

- **#4940 Rena Barnes** — keine neue Nachricht seit dem 06.09. Die
  Vorlagen-Absage vom 08.09. 07:58 ist weiterhin die einzige der fünf aus jenem
  Block **ohne** Rückläufer.
- **#7784 Cameron Dayton** — hat um 01:54 „my order number and proof of
  purchase" nachgereicht. Stand unverändert (Log 09.09. 23:20); die Frage, ob er
  „extra" für den Versand gezahlt hat, bleibt im Admin zu prüfen.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, keine
Erstattungszusage wiederholt, keine Rücksendeadresse erfunden, nicht bestätigt,
dass die APO-Adresse zustellbar ist.

---

## Lauf 09:20 UTC — 🚩 #2283 Tara Harte: die fünfte offene Erstattungszusage, seit dem 17.07.

### 🚩🚩 #2283 — acht Wochen, dritter belegter Kontakt, Thread trägt bereits `Label_7`

**Shopify, geprüft 10.09. 09:2x UTC:**

- **#2283**, bestellt **22.06. 07:55 UTC**, **19,95 £**
- **Status: `PAID` / `FULFILLED`** — **keine Erstattung im System**
- Versandt 25.06., SunSu Packet, `SYGB021701028`

**Verlauf, Betreff „Indestructible toy":**

- **17.07.** — im Thread zitiert: eine Antwort aus dem Postfach von diesem Datum
- **12.08. 10:24:** „This has been going on for **quite a while** now. Can I have
  an **update on my refund** please"
- **17.08. 14:45:** „Can someone please respond to my email below. This has been
  going on for **6 weeks** and is **simply not good enough**. **I would like my
  refund**"
- **10.09. 09:06:** „Hi Lisa, can you update me please — **I still haven't
  received my refund**"

**Der Thread trägt bereits `Label_7` (`Bot/Escalated - Owner Attention`)** — er
ist also erfasst und seit Wochen als Eskalation markiert. Passiert ist nichts.

### Das ist jetzt der fünfte Fall — und der zweite vom 17.07.

| Bestellung | Kunde | Zusage seit | Betrag | Stand |
|---|---|---|---|---|
| **#2228** | Ann Price | **17.07.** | 19,95 £ | `PAID`, nie gezahlt |
| **#2283** | **Tara Harte** | **17.07.** | **19,95 £** | `PAID`, nie gezahlt |
| — | #5841 | — | — | als „erledigt" gemeldet, nie gezahlt |
| **#8253** | Tim Kipling | 06.09. | 44,04 £ | heute Betrugsvorwurf |
| **#3770** | Steph Bentley | 03.09. | 19,95 £ | heute Nachfrage |

**Zwei Erstattungen wurden am selben Tag — dem 17.07. — zugesagt und sind beide
bis heute nicht ausgezahlt.** Das ist kein Einzelversäumnis mehr, sondern ein
Muster mit fünf Belegen, das inzwischen **56 Tage** zurückreicht.

Bei **Ann Price** ist die Folge dokumentiert: „**how many people have you conned
out of money with this statement!**" (30.08.). Bei **Tim Kipling** heute früh die
Meldung an BBB Fraud Department und Commerce Department. Tara Harte ist bislang
sachlich geblieben — nach acht Wochen und drei Nachfragen.

→ bleibt `Bot/Escalated - Owner Attention`.
**⚠️ ERSTATTUNG: 19,95 £.** Seit dem 17.07. zugesagt.
**Keine weitere Zusage senden.** Der Text für Ann Price in
`entwuerfe-zum-kopieren.md` („I'm not going to make you that promise a fourth
time from this desk") passt inhaltlich auch hier — **aber er ist für sie
geschrieben, nicht für Tara Harte, und darf nicht einfach umadressiert werden.**

### #7627 Charlotte Matthews — Lieferanfrage mit Erstattungsalternative

**08:18**, Betreff „Order no 7627":

> „I placed an order on **24th August** and have **still not received it**. Can
> you please let me know what's going on **or refund my money**?"

**Shopify:** **#7627**, bestellt **24.08. 19:23 UTC**, **27,95 £**, `PAID` /
`FULFILLED`, versandt **03.09. 07:41 UTC**, Yanwen, `UL478624234YP`,
Bury Saint Edmunds (UK).

**Zehn Tage** zwischen Bestellung und Versand, seither sieben.

Sie stellt die Erstattung als **Alternative** — „or refund my money" —, nicht als
Forderung. Der Fall fällt unter **keine** der drei Regeln (Ware unterwegs, Storno
nach Versand), also **keine Erstattungszusage**.

Sie ist die **vierte** Kundin aus dem Versandstapel vom **03.09.** (nach #7559
Rod Smith, #7741 Linda Phillips, #7525 Carol Garvey) — alle vier am selben Tag
versandt, alle vier melden sich jetzt.

→ `Bot/Draft Ready`. Versanddatum **03.09.**, Yanwen, `UL478624234YP` nennen und
die zehn Tage Liegezeit offen benennen. **Kein Zustelldatum, keine
7–21-Tage-Formel** — bei Carol Garvey (#7525) zeigt dieselbe Zusteller-Nummer
seit einer Woche nichts an; ob sich diese Sendung bewegt, ist von hier aus nicht
feststellbar.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, keine
Erstattungszusage, kein fremder Entwurfstext umadressiert, kein Text
rekonstruiert.

---

## Lauf 10:20 UTC — #7031 Neil Wilcock: die 21-Tage-Grenze ist heute erreicht

**Shopify, geprüft 10.09. 10:2x UTC:**

- **#7031**, bestellt **21.08. 18:26 UTC**, **19,95 £**, `PAID` / `FULFILLED`
- 1 × Plushie „monkey", Lydiate L31 2PA (UK)
- Versandt **02.09. 10:45 UTC** — **zwölf Tage** nach der Bestellung
- Yanwen, `UL476303254YP`

**Verlauf:**

- **29.08. 11:12:** „can I have an update as to where my item is… I thought I
  might have at least had an update by now"
- **31.08. 09:31 aus dem Postfach:** die Liefer-Vorlage, hier in einer
  **erweiterten Fassung**: „…Delivery usually takes **7–21 days**… Your parcel
  is progressing through the delivery network, although we're unfortunately
  **unable to provide an exact delivery date**… We're sorry that **the tracking
  information has not provided clearer updates**"
- **10.09. 09:27:**

> „I'm still waiting for my order and this is now **as of today 21 days** and
> still waiting. I **originally ordered hoping to receive from the UK** as I
> have stated, so **to be told I'm receiving from another country was a
> surprise**, but to be waiting **over 3 weeks** and still to be waiting isn't
> great and has **definitely put me off ordering in future**."

### Drei Punkte

**1. Die selbst genannte Frist ist heute abgelaufen.** Am 31.08. wurden ihm
„7–21 days" zugesagt. Er zählt ab Bestellung: **21.08. bis 10.09. = 20 Tage**,
er sagt 21. Rechnet man ab **Versand** (02.09.), sind es acht. Beide Rechnungen
sind vertretbar — **die Vorlage sagt nicht, ab wann gezählt wird.** Genau
deshalb ist sie hier zum Bumerang geworden: er hat sie ab Bestelldatum
verstanden, und danach ist die Zusage **heute gerissen**.

Das ist der **erste** Fall, in dem die 7–21-Tage-Formel nachweislich fällig
wird. Sie ist mindestens an **#7771, #6280, #7559, #7114, #7525** und ihn
gegangen. Bei den anderen läuft die Frist noch — **bei #7771 Barb Fitzgerald
(versandt 03.09.) am 24.09., bei #7525 Carol Garvey ebenso.**

**2. Zweiter Fall der bestrittenen Lieferzusage** nach **#7190 Steve Solley**
(gestern 12:27). Auch Neil Wilcock sagt, er habe **UK-Versand erwartet** — „as I
have stated", also hat er das schon vorher gesagt — und die Umstellung auf ein
anderes Land sei „a surprise" gewesen. Zwei Kunden in 21 Stunden, die dieselbe
Angabe beim Kauf bestreiten. Der Prüfauftrag aus dem 13:25-Eintrag von gestern
steht damit doppelt: **was stand am Bestelltag auf der Produkt- und
Checkout-Seite?**

**3. Die Antwort vom 31.08. war die ehrlichste Fassung der Vorlage**, die in
diesen Logs vorkommt: sie sagt ausdrücklich, dass **kein exaktes Zustelldatum**
genannt werden kann, und räumt ein, dass **die Sendungsverfolgung keine klaren
Informationen liefert**. Beides ist zutreffend und richtig formuliert.
**Trotzdem enthält sie weiterhin die 7–21-Tage-Angabe** — und genau die ist
jetzt der Streitpunkt. Die beiden ehrlichen Sätze nützen nichts, solange die
Frist danebensteht.

### Einordnung

**Kein Fall der drei Regeln** — Ware unterwegs, keine Erstattungsforderung. Er
verlangt nichts; er sagt, er werde nicht wieder bestellen.

→ `Bot/Needs Approval`.
Sagbar: Versanddatum **02.09.**, Yanwen, `UL476303254YP`, und offen, dass
**zwölf Tage** zwischen Zahlung und Versand lagen — das ist der eigentliche
Grund für seine Wartezeit und steht bisher in keiner Antwort an ihn.
**Nicht sagbar:** eine neue Frist, ein Zustelldatum, oder dass die Sendung sich
bewegt. **Und die 7–21-Tage-Formel darf hier nicht wiederholt werden** — sie ist
nach seiner Rechnung heute abgelaufen.

**Nicht auf der Erstattungsliste.** Ob nach 21 Tagen etwas erstattet wird, ist
eine **Owner-Entscheidung**; die Policy sieht dafür nichts vor.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, keine neue Frist
genannt, kein Text rekonstruiert.

---

## Lauf 11:20 UTC — 🚩 #6286 Deborah Gould: die ACCC, und der im Log vorhergesagte Verlauf

### Der Fall, der gestern namentlich prognostiziert wurde

Im Eintrag vom **09.09. 04:20** steht zu #6286 wörtlich:

> „→ `Bot/Needs Approval`. Absage **mit** dem Unterschied zwischen Frist und
> Geltungsbereich, ausdrücklich ohne die Behauptung, sie sei zu spät dran.
> **Keine Vorlagen-Absage** — nach dem gestrigen Befund (vier Eskalationen aus
> vier Vorlagen-Absagen) ist das hier der **teuerste mögliche Fehler**."

**Heute 10:26** ging die Vorlagen-Absage raus, adressiert an „**Dear
Customer**" — obwohl sie mit Namen unterschrieben hatte.

**Heute 10:39, dreizehn Minuten später:**

> „I find that **absolutely ridiculous**.
> I bought your product **only because of your 30 Day money back guarantee**.
> What you're saying is that the guarantee only covers the product **on arrival
> and not used** — **who would return them?!**
> **You need to remove your claims and the guarantee as this is false
> advertising!!!**
> **I will be contacting the ACCC** for what my rights are."

### Drei Befunde

**1. Die ACCC ist die fünfte Behörde.** Australian Competition and Consumer
Commission — sie schreibt aus **New South Wales**. Bisher: Trading Standards
(UK, dreimal), Better Business Bureau (zweimal), FTC, State Attorney General.
**Fünf verschiedene Stellen in fünf Tagen, auf drei Kontinenten.**

**2. Ihr Argument ist wortgleich mit dem von Gary Lindsay (#4273)** — und sie
kann es nicht von ihm haben:

| | Formulierung |
|---|---|
| Gary Lindsay, 09.09. 10:34 | „the guarantee — which is **pointless if a dog toy cannot be used by a dog** or the guarantee is invalidated" |
| **Deborah Gould, 10.09. 10:39** | „the guarantee only covers the product on arrival and not used — **who would return them?!**" |

Zwei Kunden auf zwei Kontinenten kommen unabhängig voneinander zu demselben
Schluss: **eine Haltbarkeitsgarantie, die nur für unbenutzte Ware gilt, ist in
sich widersprüchlich.** Das ist kein Missverständnis der Kunden mehr — es ist
ein Einwand gegen die Konstruktion.

**Sechs Kunden** haben diesen Punkt inzwischen erhoben: Christina Williams
(21.08.), `bev212.bs` (06.09.), Gary Lindsay (09.09.), Deborah Gould (09. und
10.09.), Sofia Christopoulos (10.09.), Keith Crane (10.09.).

**3. „Dear Customer".** Sie hat mit „Kind regards, **Deborah**" unterschrieben
und wurde als „Dear Customer" angeschrieben. In allen anderen Vorlagen-Antworten
dieser Woche stand der Vorname. Bei einer Kundin, die ohnehin den Eindruck hat,
nicht gehört zu werden, ist das kein Formfehler ohne Folgen.

### Einordnung

→ `Bot/Escalated - Owner Attention` (zuvor `Needs Approval`).
**Eskalationsgrund (nur fürs Log):** Verbraucherschutzbehörde eingeschaltet
(ACCC), ausdrücklicher Vorwurf der Falschwerbung, Forderung nach Entfernung der
Werbeaussage **und** der Garantie, Zweitkontakt nach Vorlagen-Absage.

**Keine zweite Absage.** Bei #4919, #6259 und #6213 hat genau die zu
Verbraucherrechtszitat, Trading Standards und „dumb" geführt.

**Kein Erstattungsfall nach der Regel** (Kauschaden). Sie steht **nicht** auf
der Erstattungsliste; 45,83 £ wären eine Owner-Entscheidung.

**Vordringlich:** Sie verlangt zweierlei — die Werbeaussage **und** die Garantie
zu ändern. Beides ist Owner-Sache und beides steht seit dem 21.08. offen.

### Wieder aufgetaucht, unverändert

- **#4812 Carolyn Marmalejo** (`Label_7`) — keine neue Nachricht seit dem
  22.08. Stand unverändert: „**I only opened one toy**… therefore I never opened
  the **other new toys**" — Regel 2, seit **19 Tagen** unbeantwortet. Der
  Ur-Fall der Verwechslung, die sich seither bei #6528, #5973, #7179 und #7292
  wiederholt hat.
- **#6751 Jonathan Pizzo** — keine neue Nachricht. Sendungsnummer
  `JCHSG0000004362556` liegt seit dem 02.09. bereit und ist ihm nie genannt
  worden; er hat zweimal danach gefragt, zuletzt am 01.09.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, keine zweite
Absage, kein Text rekonstruiert.

---

## Lauf 12:20 UTC — 🚩🚩 #4317 Charles Rivera: die Ersatzlieferung wurde zugesagt — und nie verschickt

**Das ist der Beleg, der in der offenen Ersatzgarantie-Frage bisher gefehlt hat.**

**Shopify, geprüft 10.09. 12:2x UTC:**

- **#4317**, bestellt **03.08. 01:48 UTC**, **28,51 £**, `PAID` / `FULFILLED`
- 2 × Plushie (hippo, elephant), versandt 05.08., Yun Express US,
  `YT2621700703209981`
- **Es existiert keine zweite Bestellung** unter dieser Adresse. **Kein
  Ersatzauftrag ist je angelegt worden.**

**Verlauf:**

| Datum | Wer | Inhalt |
|---|---|---|
| **18.08. 12:35** | Kunde | „We were excited to finally purchase a dog toy that was said to be **indestructible**… **Both toys did not last 3 days**. **I really don't want a refund.** I would…" |
| **19.08. 10:57** | **Postfach** | *„We can **arrange two replacement toys** for you. Before we proceed, please confirm…"* |
| **19.08. 13:22** | Kunde | „**Yes, please go ahead and send the 2 replacement toys.** Thank you for your help." |
| **20.08. 20:29** | Postfach | *„We've **forwarded your replacement request to our team** for processing. They will review the request and arrange the replacement accordingly."* |
| **10.09. 12:04** | Kunde | „**I have not received my replacement dog toys. Nor have I gotten an email that they were shipped.** Can you please give me an update…" |

### Warum das den Ersatzgarantie-Komplex entscheidet

Seit dem 14.08. steht in diesen Logs die Frage offen, ob es eine
**Ersatzgarantie** gibt. Vier Kunden berufen sich darauf, einer davon hat
deswegen **Trading Standards** eingeschaltet:

| Datum | Kunde | Quelle |
|---|---|---|
| 14.08. | Adam Sellens | Anzeige mitgeschickt, seit 25.08. ohne Antwort |
| 18.08. | Gary Sanderson | Anzeige |
| 05.09. | **Nick Tarrant (#6259)** | **Website** — 10.09. Trading Standards |
| 09.09. | Jeff Williams (#5851) | „your company stated" |

**`support-policy.md` kennt keine Ersatzgarantie.** Aber am **19.08.** hat das
Postfach einem Kunden eine Ersatzlieferung **ausdrücklich angeboten** — „we can
arrange two replacement toys for you" — und er hat sie **angenommen**.

Damit ist die Frage nicht mehr, ob die Werbung etwas verspricht, das die Policy
nicht kennt. **Der Support selbst hat es zugesagt.** Und **22 Tage später ist
nichts passiert**: kein Ersatzauftrag in Shopify, keine Versandmitteilung, keine
Rückmeldung.

**Charles Rivera ist außerdem der Kunde, der ausdrücklich schrieb: „I really
don't want a refund."** Er wollte nur funktionierende Spielzeuge. Er gehört
damit zu der Gruppe, die seit dem 09.09. sechsmal aufgetreten ist (#6044, #3344,
#7559, #7101, #7271, #6952) — und er ist der Einzige davon, dem **etwas zugesagt
wurde**.

### Die Liste der offenen Zusagen wächst auf sechs

| Vorgang | Kunde | Zugesagt am | Art | Stand |
|---|---|---|---|---|
| #2228 | Ann Price | 17.07. | Erstattung | nie gezahlt |
| #2283 | Tara Harte | 17.07. | Erstattung | nie gezahlt |
| **#4317** | **Charles Rivera** | **19.08.** | **Ersatzlieferung** | **nie verschickt** |
| — | #5841 | — | Erstattung | als erledigt gemeldet, nie gezahlt |
| #3770 | Steph Bentley | 03.09. | Erstattung | nie gezahlt |
| #8253 | Tim Kipling | 06.09. | Erstattung | nie gezahlt, heute Betrugsvorwurf |

**Sechs schriftliche Zusagen, keine einzige ausgeführt.** Die älteste ist
**56 Tage** alt.

### Einordnung

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** offene Ersatzzusage seit dem 19.08.,
Zweitkontakt nach 22 Tagen Funkstille, bestrittene Werbeaussage.

**Was zu entscheiden ist — und zwar für alle fünf Fälle gemeinsam:** Gibt es
eine Ersatzlieferung oder nicht? Bei Charles Rivera ist sie **zugesagt und
angenommen**; bei Nick Tarrant führt die unbeantwortete Frage danach bereits zu
einer Behörde. Der Support kann das nicht auflösen.

**Nicht auf der Erstattungsliste** — er will **kein** Geld, er will die Ware.
Eine Erstattung wäre nicht das, worum er gebeten hat.

**Nicht getan:** kein Entwurf, kein Label, keine Ersatzlieferung veranlasst
(nicht möglich), keine neue Zusage, kein Text rekonstruiert.

---

## Lauf 14:20 UTC — 🚩 #4745 Stephen Hanlon: Trustpilot wird zum Argument

### 🚩 #4745 — der erste Kunde, der sich auf die Bewertungsplattform beruft

**14:02**, Betreff „my order":

> „your toys are **shite**.. **one day** they lasted before the **stuffing was
> flying** like any other toy you claimed not to be like. **i should have read
> the trust pilot reviews that says it all.. everyone says they are shite!!**"

**Shopify, geprüft 10.09. 14:2x UTC:**

- **#4745**, bestellt **06.08. 13:07 UTC**, **54,95 £** — **der höchste
  Einzelbetrag der letzten Tage**
- `PAID` / `FULFILLED`, versandt **22.08. 01:30 UTC** — **sechzehn Tage** nach
  der Bestellung
- Yun Express, `YT2623400701612777`

**Was daran neu ist:** Er beruft sich nicht auf die Werbung, sondern auf
**Trustpilot** — und zwar als Beleg dafür, dass die Erfahrung kein Einzelfall
sei. Bisher liefen alle Verweise auf Bewertungen in die andere Richtung:

| Datum | Kunde | Bezug |
|---|---|---|
| 26.08. | David Andrews (#5316) | „can be seen from the **thousands of reviews online**" |
| 08.09. | Matt Pinnock (#6606) | **kündigt an**, eine Bewertung zu schreiben |
| 08.09. | Meredith Spicer (#6213) | **kündigt an**, eine Bewertung zu schreiben |
| **10.09.** | **Stephen Hanlon (#4745)** | **hat sie gelesen — nachträglich** |

Er sagt sinngemäß, die Bewertungen hätten ihn gewarnt, wenn er sie vorher
gelesen hätte. Das ist kein Eskalationsmittel, sondern eine **Feststellung über
die Außenwirkung** — und die deckt sich mit dem, was David Andrews am 26.08.
schrieb.

Dazu passt **Steph Bentley** (#3770, 14.08.): „**your reviews are false**" — sie
meinte damit die Bewertungen **auf der Website**. Zusammen ergibt das zwei
gegenläufige Aussagen über Bewertungen: die im Shop seien geschönt, die
außerhalb seien vernichtend. **Beides gehört an den Owner**, nicht in eine
Support-Antwort.

**Klassifikation: Kauschaden → keine Erstattung nach der Regel.** Er verlangt
auch keine — er beschwert sich, ohne eine Forderung zu stellen. Damit ist er der
**siebte** dieser Art seit dem 09.09.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** bestrittene Werbeaussage plus Verweis auf
öffentliche Bewertungen als Beleg — das ist der „public-review pattern
complaint" aus der Policy.
**Keine Vorlagen-Absage.** Sie würde ihm die Rückgabepolicy erklären, die er
nicht angesprochen hat.

**Nicht auf der Erstattungsliste** — Kauschaden, und keine Forderung.
**Nebenbefund:** 16 Tage bis zum Versand bei einem 54,95-£-Auftrag; das ist die
längste Liegezeit, die in diesen Logs bisher belegt ist.

### #7316 Brett Merriman — kurz und ohne Forderung

**13:51**, weitergeleitete Versandbestätigung, vollständiger Inhalt:

> „**This toy lasted 20 minutes... Junk**"

**Shopify:** **#7316**, bestellt **23.08. 03:19 UTC**, **20,34 £**, `PAID` /
`FULFILLED`, 1 × Plushie „frog", versandt **02.09. 10:59 UTC**, **WB US**,
`WNBAA0497794623YQ`, Mesa (US).

Kauschaden, keine Erstattungsforderung, keine Werbezitate. **Siebter Fall aus
dem Versandstapel vom 02.09.**, und mit ihm der **achte** Kunde seit dem 09.09.,
der sich beschwert, ohne Geld zu verlangen.

⚠️ Sendungsnummer erneut aus der Familie `WNBAA…YQ` — **fünfter Fall** (Robert
Gagne, #6872, #7741, #7001, jetzt #7316).

→ `Bot/Needs Approval`. Kurz, ohne Vorlage, ohne Rückgabepolicy — er hat nichts
gefordert. **Nicht auf der Erstattungsliste.**

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, keine
Vorlagen-Absage, kein Text rekonstruiert.

---

## Lauf 16:20 UTC — 🚩🚩🚩 #1301 Sheila Keirnan: UKICC, und drei Korrekturen

**15:35:**

> „I've **taken advice** on this matter of your company **refusing to refund me,
> my full purchase price of £32.95**. I've been **instructed to give you one
> last opportunity** to give me a full refund, before bringing this matter to
> the attention of the **International Consumer Centre (UKICC)**."

Ich habe den vollständigen Thread gelesen (sieben Nachrichten). Er korrigiert
drei Angaben aus meinen eigenen Logs.

### 🔧 Korrektur 1: Am 01.09. wurde ihr die Rückgabe **zugesagt**

Im Log vom 09.09. steht nur, sie habe „am 05.09. ausdrücklich nach der
Rücksendeanleitung gefragt". Tatsächlich hat sie danach gefragt, **weil sie ihr
angeboten worden war.** Aus dem Postfach, **01.09. 11:00**:

> „The **two unopened toys may be returned in their original condition for a
> refund**. Please let us know if you would like to proceed with returning those
> items, and **we'll provide the return instructions**."

Sie hat am 05.09. genau das getan — und **statt der Anleitung kam am 07.09. ein
30-%-Angebot**. Die Zusage wurde also nicht vergessen, sondern **zurückgenommen
und durch ein Teilangebot ersetzt**.

**Damit ist es die siebte schriftliche Zusage, die nicht eingehalten wurde:**
#2228, #2283, #4317, #5841, #3770, #8253 — und **#1301**.

### 🔧 Korrektur 2: Es gab am 09.09. ein **50-%-Angebot**

Das stand in keinem meiner Logs. Aus dem Postfach, **09.09. 11:18**:

> „While we're **unable to arrange a full refund and prepaid return** in this
> case, we would like to **increase our goodwill offer to a 50 % partial
> refund**… allowing you to keep all of the items without needing to return
> them."

**Die berichtigte Chronologie: zehn Angebote, und eine neue Höchststufe.**

| Datum | Kunde | Angebot |
|---|---|---|
| 22.08. | Christina Williams (#4035) | 20 % |
| 26.08. | Sharon Lagos (#5205) | 20 % |
| 31.08. | Ken Beville (#6583) | 20 % |
| 31.08. | Christina Williams (#4035) | 25 % |
| 01.09. | Ken Beville (#6583) | 30 % |
| 03.09. | Trudi Trotter (#5148) | 30 % |
| 05.09. | Viken Jehdian (#6546) | Teilbetrag |
| 07.09. | Karen McCormick (#4606) | 15 % |
| 07.09. | Sheila Keirnan (#1301) | 30 % |
| **09.09.** | **Sheila Keirnan (#1301)** | **50 %** |

**Bei ihr ist die Vorlage von 30 % auf 50 % geklettert, um eine Rückgabe
abzuwenden, die zuvor schriftlich zugesagt worden war.** Sie hat beides
abgelehnt.

### 🔧 Korrektur 3: Ihr Fall ist von Anfang an ein Sicherheitsfall — und wurde als Kauschaden behandelt

Ihre Erstmail vom **09.08.** ging an die **Privatadresse des Owners**
(`chiaranevio0805@gmail.com`) und wurde erst am 30.08. weitergeleitet — drei
Wochen Liegezeit. Inhalt: beim Spielen löste sich der Kopf des Hippos, **darin
steckte eine Nadel mit lila Spitze**.

Die Antwort vom 01.09. enthält den richtigen Satz — „**Please do not allow your
dogs to use the toys** while this matter is being reviewed" — **und im selben
Absatz die Kauschaden-Absage** für den Hippo: „our policy does not cover toys
that have been **used and damaged by chewing**".

**Eine Nadel im Spielzeug ist kein Kauschaden.** Das Produkt war bei Anlieferung
fehlerhaft; der Hund hat den Defekt nur freigelegt. Das ist **Regel 1**, nicht
die Kauschaden-Ausnahme.

### 🚩 Nebenbefund: zwei verschiedene Zahlen auf der Website

Am 05.09. schrieb sie:

> „…one of your **40,000 happy dog owners** that have purchased your product
> that you advertise on your website, **or is it 25,000**?"

Sie hat auf der Website **zwei unterschiedliche Kundenzahlen** gefunden. Das ist
der **fünfte shop-eigene Text**, an dem sich ein Kunde festmacht — nach „With
replacement guarantee" (#6259 → Trading Standards), der Lieferzusage (#7190,
#7031), dem Artikelnamen (#4851) und den fehlenden Quietscher-Angaben (#7292).
**Unbeantwortet geblieben.**

### Einordnung

→ bleibt `Bot/Escalated - Owner Attention`, **jetzt mit Frist**.
**Eskalationsgrund (nur fürs Log):** Verbraucherschutzstelle angekündigt
(UKICC), Rechtsberatung eingeholt, zurückgenommene schriftliche Zusage,
Sicherheitsbefund (Nadel im Produkt), fünfter Kontakt.

**Die UKICC ist die sechste Stelle** nach Trading Standards, BBB, FTC, State
Attorney General und ACCC — **innerhalb von sechs Tagen**.

**⚠️ ERSTATTUNG: 32,95 £, Regel 1 + Regel 2.** Der Hippo kam **defekt** an
(Fremdkörper), die zwei anderen sind **ungeöffnet**. Beide Regeln greifen; ein
Teilbetrag ist hier nicht vorgesehen und dreimal abgelehnt worden.

**Kein drittes Teilangebot.** Nach 30 % und 50 % wäre das der Punkt, an dem aus
einem Sicherheitsfall ein Verhandlungsfall wird — und genau das hat sie mit
„taken advice" beendet.

**Rücksendung weiterhin nicht organisierbar** — es gibt keine Rücksendeadresse
(offener Blocker seit 13.08.). Sie ist am 01.09. zugesagt worden und existiert
nicht. Das gehört ehrlich gesagt, statt es ein viertes Mal mit einem Prozentsatz
zu umgehen.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, **kein weiteres
Teilangebot**, keine Rücksendeadresse erfunden, kein Text rekonstruiert.

---

## Lauf 17:20 UTC — #7899 Anna Howie

**17:09**, Betreff „My order":

> „My order number is **#7899**. I have not received my order yet and **there is
> no update in my order**. I would like to know when to expect my order."

**Shopify, geprüft 10.09. 17:2x UTC:**

- **#7899**, bestellt **27.08. 07:34 UTC**, **27,95 £**, `PAID` / `FULFILLED`
- 2 × Plushie (elephant, donkey)
- Versandt **03.09. 07:52 UTC** — **sieben Tage** nach der Bestellung
- 4PX Economic Registered, `4PX3003125178279CN`
- Fochabers, Schottland IV32 7JG

Sachlich, ohne Vorwurf, ohne Erstattungsforderung. Sieben Tage bis zum Versand
ist die **kürzeste** Liegezeit unter den heutigen Lieferanfragen (gegenüber
zehn bei #7627, zwölf bei #7031 und #7001, sechzehn bei #4745).

**„There is no update in my order"** — sie hat die Sendungsnummer aus der
Versandbenachrichtigung und sieht keine Bewegung. Damit ist sie der **fünfte**
Fall dieser Art, nach Robert Gagne, #6872 Dorothy Rysh, #7053 John Collins und
**#7525 Carol Garvey** (heute 06:07, dieselbe Formulierung: „the tracking
information hasn't been updated").

**Sie ist außerdem die fünfte Kundin aus dem Versandstapel vom 03.09.** — nach
#7559 Rod Smith, #7741 Linda Phillips, #7525 Carol Garvey und #7627 Charlotte
Matthews. Von den beiden großen Versandtagen melden sich damit heute
**sieben Kunden aus dem 02.09.-Stapel und fünf aus dem 03.09.-Stapel**.

→ `Bot/Needs Approval` (nicht `Draft Ready`, aus demselben Grund wie bei #7525):
Der Vorlagensatz „your parcel is currently **progressing through the delivery
network**" wäre bei ihr **unbelegt** — genau das bestreitet sie.

**Sagbar:** Versanddatum **03.09.**, Zusteller 4PX, Nummer
`4PX3003125178279CN`, `https://t.17track.net/en#nums=4PX3003125178279CN`, und
dass zwischen Bestellung und Versand sieben Tage lagen.
**Nicht sagbar:** ein Zustelldatum, die 7–21-Tage-Formel (heute bei #7031
nachweislich fällig geworden), oder dass die Sendung sich bewegt.

**Nicht auf der Erstattungsliste** — Ware unterwegs, kein Regelfall, keine
Forderung gestellt.

**Nicht getan:** kein Entwurf, kein Label, keine Zustellprognose, nicht
behauptet, die Sendung bewege sich, kein Text rekonstruiert.
