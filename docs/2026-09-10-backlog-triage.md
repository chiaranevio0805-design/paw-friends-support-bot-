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
