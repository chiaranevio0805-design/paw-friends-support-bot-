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
