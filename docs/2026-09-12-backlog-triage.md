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
