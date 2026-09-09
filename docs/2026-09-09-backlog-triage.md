# Backlog-Triage 2026-09-09

Läufe 00:17, 01:17 und 02:17 UTC. Die ersten beiden waren leer. Der Gmail-
Schreibpfad bricht weiterhin ab (seit 21.08.) — keine Entwürfe, keine Labels,
kein Text rekonstruiert.

---

## Lauf 02:20 UTC — #6528 Tommy Johnson: ein sauberer Regel-2-Fall

**09.09. 01:43**, Betreff „**Order #6528 Return Request**", CC an
`kth3john@hotmail.com`, zwei Fotos beigefügt:

> „I recently purchased some plushies for my dog because I saw that they were
> **marketed for big-time chewers**. I was hoping she wouldn't be able to tear
> them up, but we've just given her the first plushie, and she's already
> destroyed it.
>
> I do not think these are a good fit for her.
>
> **Could we please return the other two that we have not given to her yet for a
> refund?**"

**Shopify, geprüft 09.09. 02:2x UTC:**

- **#6528**, bestellt **17.08. 16:50 UTC**, **45,86 £**, `PAID` /
  **`PARTIALLY_FULFILLED`**
- Positionen: **4 × Plushie** (frog, fox, Duck, donkey) **+ 1 × E-Book**
- Versandt **22.08. 02:01 UTC**, 4PX Economic Registered,
  `4PX3003088587125CN`, Monroe, Louisiana 71201
- Bestell-E-Mail: `thepelicanstyle@gmail.com` (er schreibt von
  `thomashjohnson23@gmail.com`)

### Klassifikation: Regel 2 — unbenutzt

Er verlangt **ausdrücklich keine** Erstattung für das zerstörte Exemplar. Er
fragt nur nach den **zwei ungeöffneten**. Das ist genau der Fall, für den
Regel 2 da ist: unbenutzte Ware, volle Erstattung des darauf entfallenden
Betrags.

**Der Fall ist deshalb heikel, weil er zwei bekannten Fehlern direkt im Weg
liegt:**

1. **Carolyn Marmalejo (#4812, 20.08.):** Sie fragte nach ihren **unbenutzten**
   Spielzeugen und bekam die Kauschaden-Absage („products that have been used
   and damaged by a pet are not eligible"). Die Absage bezog sich auf das
   zerstörte Exemplar, ihre Frage nicht. Seit dem 22.08. unbeantwortet.
2. **Ken Beville (#6583, 29.08.–01.09.):** verlangte zweimal ausdrücklich die
   Rückgabe und bekam zweimal einen Teilbetrag angeboten (20 %, dann 30 %).

Tommy Johnsons Mail enthält **beide Auslöser gleichzeitig**: sie erwähnt ein
zerstörtes Spielzeug (Kauschaden) **und** verlangt die Rückgabe unbenutzter
Ware (Regel 2). Eine Vorlagen-Absage auf das erste Stichwort würde das zweite
übergehen — genau wie bei Carolyn Marmalejo.

→ `Bot/Needs Approval`. **Keine Kauschaden-Absage. Kein Teilerstattungs-
angebot.**

### 🚩 Nebenbefund: eine vierte Position ist nie versandt worden

Er spricht von **drei** Plushies (eines zerstört, zwei ungeöffnet). Shopify
führt **vier** Plushies plus E-Book, und die Bestellung steht auf
**`PARTIALLY_FULFILLED`** — es gibt nur **eine** Sendung vom 22.08.

Das passt zusammen: **ein Plüschtier ist nie rausgegangen**, und er weiß nichts
davon. Das gehört ihm gesagt, auch wenn er nicht danach gefragt hat.

Damit ist es die **vierte Teilsendung** in zwei Tagen, über die der Kunde nicht
informiert wurde — nach #6116 Sharron Hodges (82,81 £), #6872 Dorothy Rysh
(50,43 £) und #1301 Sheila Keirnan (32,95 £). Bei #4606 Karen McCormick und
#4812 Carolyn Marmalejo steht derselbe Status. **Sechs Fälle.**

### Betrag

**Nicht bezifferbar aus dem Log.** Die Bestellung hat **45,86 £** gekostet; die
Einzelpreise der Positionen (4 × 30,97 £ + 36,13 £ = 160,01 £) sind
Listenpreise vor dem Bundle-Rabatt (`Kaching Bundles`) und ergeben in der Summe
**nicht** den gezahlten Betrag. Der auf zwei von vier Plüschtieren entfallende
Anteil lässt sich daraus **nicht ableiten**.

→ Der Betrag muss im Shopify-Admin **auf Positionsebene** ermittelt werden.
Nach Runbook 6b wird nicht geschätzt. Dasselbe Problem besteht bei
**#4812 Carolyn Marmalejo (86,89 £)**.

### Was ihm gesagt werden kann

Belegt: die Bestellung steht auf `PARTIALLY_FULFILLED`, eine Position ist nie
versandt worden; die vorhandene Sendung ging am 22.08. mit 4PX raus.

**Nicht sagbar:** eine Rücksendeadresse — es gibt keine (offener Blocker seit
13.08.). Das ist bei einem Kunden, der von sich aus zurücksenden will, der
entscheidende Punkt und gehört ehrlich benannt, statt ihn hinzuhalten oder ihm
stattdessen einen Rabatt anzubieten.

---

## Nicht getan

- Keine Entwürfe, keine Labels — Schreibpfad defekt seit 21.08.
- Keine Erstattung, kein Storno in Shopify ausgeführt.
- Keine Rücksendeadresse erfunden.
- **Kein Betrag geschätzt** — der erstattungsfähige Anteil von #6528 steht nicht
  fest.
- Kein Entwurfstext rekonstruiert.

---

## Lauf 03:20 UTC — 🚩 Mail gibt sich als Shopify-Regulierungsstelle aus

**08.09. 21:58 UTC**, Absender **`shopifystoreregulatory.center@gmail.com`**,
**keine Betreffzeile**, Inhalt vollständig:

> „I'd like to hear your thoughts on something."

### Warum das kein Support-Fall, sondern ein Sicherheitsbefund ist

- Der Absendername gibt eine **Regulierungs-/Aufsichtsstelle für Shopify-Shops**
  vor. Eine solche Stelle würde nicht von einer **gmail.com-Adresse** schreiben.
  Shopify kontaktiert Händler über `@shopify.com`, nicht über Freemail.
- **Kein Betreff, kein Anliegen, kein Bezug** — ein Einzeiler, dessen einziger
  Zweck es ist, eine Antwort zu erzeugen. Das ist das Standardmuster von
  Pretexting: erst Vertrauen über die vorgetäuschte Rolle aufbauen, der Inhalt
  kommt in der zweiten Mail.
- **Der Zeitpunkt passt zur Lage.** Im Postfach liegen aktuell eine
  Trading-Standards-Ankündigung (Jason Branch, Valerie #4829), eine Meldung ans
  **Better Business Bureau** (#6213, gestern 13:59), mehrere Chargebacks
  (#3310, #5111, #5316, #6173) und eine Sammelklage-Androhung. Eine Mail, die
  sich als Aufsichtsstelle ausgibt, trifft genau die Sorge, die ein Betreiber
  in dieser Lage hat — und erhöht die Chance, dass jemand antwortet.

### Einordnung im Kontext

Das ist der **vierte Sicherheitsbefund** in diesem Postfach:

| Datum | Befund |
|---|---|
| 14.08. | Google-Sicherheitswarnung: Wiederherstellungs-E-Mail **und** -Telefonnummer im selben Moment geändert |
| — | Vollständige Kreditkartennummer im Klartext im Thread #4284 |
| 06.09. | Phishing-Mail „Todd Jacobs Shared a Document with You", BCC-Massenversand, angeblicher OneDrive-Link |
| **08.09.** | **Mail als „Shopify Store Regulatory Center" von einer Gmail-Adresse** |

→ **`Bot/No Action`. Nicht antworten, nicht nachfragen, keine Informationen zum
Shop, zu Bestellungen oder zu laufenden Beschwerden herausgeben.** Auch keine
höfliche Rückfrage — jede Antwort bestätigt, dass die Adresse gelesen wird, und
liefert den Anknüpfungspunkt für die zweite Mail.

Der Owner sollte den Absender kennen, bevor er selbst ins Postfach sieht: eine
Mail, die sich als Aufsicht ausgibt, wirkt gerade jetzt plausibel.

**Nicht getan:** nicht geantwortet, nichts angeklickt, keine Shop-Daten
herausgegeben.

---

## Lauf 04:20 UTC — #6286 Deborah Gould und eine Akquise-Mail

### #6286 — Deborah Gould (debgould57@me.com), 04:16

Betreff „**Order #6286 Destroyed toys**", ein Foto beigefügt:

> „I had great hope that these toys would **live up to your claims**.
> Unfortunately my dog has chewed into the toys, **removed the squeaker and
> stuffing** all within a day or two.
> **I feel that this falls under your 30 Day Guarantee as I purchased them on
> 16/8/2026.**
> Photo attached of the destroyed toys."

**Shopify, geprüft 09.09. 04:2x UTC:**

- **#6286**, bestellt **15.08. 22:53 UTC**, **45,83 £**, `PAID` /
  **`PARTIALLY_FULFILLED`**
- 4 × Plushie (Little Bear, monkey, donkey, fox) + 1 × E-Book
- Versandt **20.08. 02:17 UTC**, 4PX Standard Registered,
  `4PX3003082535733CN`
- **Dee Why, New South Wales 2099 — Australien**

**Klassifikation: Kauschaden → keine Erstattung nach der Regel.** Der Hund hat
die Spielzeuge benutzt und dabei zerstört.

**Aber der Fall ist nicht der Standardfall, und die Vorlagen-Absage passt
nicht.** Sie streitet nicht über Werbung, sondern über die **Reichweite der
30-Tage-Garantie** — und der Teil ihres Arguments, der die **Frist** betrifft,
**stimmt**:

- Bestellt **15./16.08.**, sie schreibt am **09.09.** — das sind **24 Tage**,
  also **innerhalb** der 30 Tage.
- Falsch ist nur ihre Annahme, die Garantie decke **jeden Grund**. Sie deckt
  unbenutzte Ware und Ware, die defekt ankommt — nicht Kauschaden.

Eine Antwort, die ihr pauschal „die 30 Tage greifen hier nicht" schreibt, wäre
**sachlich irreführend**: die Frist greift, der Sachverhalt fällt nur nicht
darunter. Genau diesen Unterschied hat am 06.09. schon `bev212.bs@googlemail.com`
angegriffen: *„surely the 30 day money back **should state that**, as that again
is **very misleading**."* Zwei Kundinnen an derselben Stelle innerhalb von drei
Tagen — das ist ein Formulierungsproblem der Garantie, kein Einzelfall.

→ `Bot/Needs Approval`. Absage **mit** dem Unterschied zwischen Frist und
Geltungsbereich, ausdrücklich ohne die Behauptung, sie sei zu spät dran.
**Keine Vorlagen-Absage** — nach dem gestrigen Befund (vier Eskalationen aus
vier Vorlagen-Absagen) ist das hier der teuerste mögliche Fehler.

**Nebenbefund 1 — siebte Teilsendung.** `PARTIALLY_FULFILLED`, nur eine Sendung
vom 20.08. Sie spricht von „the toys" im Plural, weiß aber nichts davon, dass
eine Position nie rausgegangen ist. Nach #6116, #6872, #1301, #4606, #4812,
#6528 ist das der **siebte** Fall in zwei Tagen.

**Nebenbefund 2 — der Quietscher.** „Removed the **squeaker**" heißt: ein
kleines Hartteil ist aus dem Spielzeug herausgelöst worden. Sie meldet **kein**
Verschlucken, und das gehört ihr auch nicht unterstellt. Der Befund gehört
trotzdem in die Reihe #6283, Andy Sire, Kevin Saggers (#3197), #6741 und die
Nadel im Hippo (#1301) — **inzwischen sechs Meldungen über lose Kleinteile.**

### `stephanixtech10@gmail.com` — Akquise

> „We came across your brand and were impressed by your products. We see strong
> potential for a **short animated video**… We'd like to create an initial…"

Werbeagentur-Akquise, kein Support-Fall. → `Bot/No Action`, keine Antwort.

Fünfte Mail dieser Art nach `haminexpert01@` (01.09.), `yomtech006@` (06.09.),
`kejiconsult@` (08.09.) und `abolajiyus21@` (08.09.).

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Text
rekonstruiert, keine Rücksendeadresse erfunden, kein Verschlucken unterstellt.

---

## Lauf 06:20 UTC — `haiweimaoyi0814@gmail.com`, Akquise (Zweitkontakt)

**05:18**, Betreff „A few product ideas for Paw-Friends":

> „I just wanted to **follow up on my previous message**. I came across
> Paw-Friends and really liked your focus on durable, high-quality products for
> dogs…"

Lieferanten- bzw. Agenturakquise, kein Support-Fall. → `Bot/No Action`, keine
Antwort.

**Sechste Mail dieser Art** seit dem 01.09.: `haminexpert01@` (01.09.),
`yomtech006@` (06.09.), `kejiconsult@` (08.09.), `abolajiyus21@` (08.09.),
`stephanixtech10@` (09.09.), jetzt diese. Fünf davon in den letzten drei Tagen.

**Nebenbefund:** Sie schreibt „follow up on my **previous** message" — eine
erste Mail dieser Adresse ist im Postfach nicht auffindbar. Entweder ist sie im
Spam gelandet, oder der Satz ist Teil der Vorlage. Kein Handlungsbedarf, aber
es passt zum Muster der übrigen fünf, die alle dieselbe Form haben.

Nicht geantwortet, nichts angeklickt.

---

## Lauf 07:20 UTC — 🚩🚩 #6259 Nick Tarrant: Trading Standards, weil eine Frage zweimal nicht beantwortet wurde

Das ist der schwerste Vorgang seit gestern früh — und er korrigiert zugleich
den Befund von gestern.

**Shopify, geprüft 09.09. 07:2x UTC:**

- **#6259**, bestellt **15.08. 18:37 UTC**, **29,95 £**, `PAID` / `FULFILLED`
- 2 × Plushie (pig, monkey) — „BUY 1 AND GET 1 FREE"
- Versandt **22.08. 01:59 UTC**, Yanwen, `UL442893702YP`, Lichfield WS13 6US
- Kunde: **DR NICHOLAS TARRANT**

### Der Verlauf

- **03.09. 06:22** — Foto beigefügt: „In 5 mins, my female greyhound had torn
  off an ear and exposed the stuffing. I'd like to request a refund as these
  are **meant to be extra strong**."
- **04.09. 13:17 aus dem Postfach** — **erste** Vorlagen-Absage (Kauschaden).
- **05.09. 14:48 Nick**, eine einzige, präzise Frage:

  > „Your website mentions '**With replacement guarantee**'. **I'm keen to hear
  > what this means?**"

- **08.09. 08:23 aus dem Postfach** — **zweite** Vorlagen-Absage. Sie beginnt
  mit „**As explained**…", wiederholt die 30-Tage-Regel und schreibt:

  > „We appreciate your concerns regarding the product's durability **and the
  > wording used in our advertising**… Unfortunately, we're unable to provide a
  > refund, **replacement**, or exchange…"

  **Seine Frage nach der Ersatzgarantie wird mit keinem Wort beantwortet.** Die
  Antwort räumt sogar ein, dass es um die Werbeformulierung geht — und geht
  dann nicht darauf ein.

- **09.09. 06:54 Nick:**

  > „I'm not sure I really got an answer about my question about the replacement
  > guarantee? **I will be asking Trading Standards for their view as I think
  > this is deeply misleading.**"

### 🔧 Korrektur am Log vom 08.09.

Im gestrigen Eintrag „Bilanz des Tages" steht, es seien **vier** Antworten aus
dem Postfach gegangen (07:57, 07:58, 07:58, 08:25). **Das war unvollständig.**
Um **08:23** ging eine fünfte an Nick Tarrant — zwei Minuten vor der an Matt
Pinnock. Ich habe sie im 09:17-Lauf nicht erfasst, weil der Thread damals nicht
in der Trefferliste stand.

**Richtig ist:** Am 08.09. sind zwischen 07:57 und 08:25 **fünf**
Vorlagen-Antworten rausgegangen. **Vier davon haben inzwischen eskaliert:**

| Zeit | Kunde | Reaktion | Abstand |
|---|---|---|---|
| 07:57 | Vicky Blow (#7610) | Erstattungsforderung bekräftigt | 57 Min. |
| 07:58 | Rena Barnes (#4940) | bisher keine | — |
| 07:58 | Meredith Spicer (#6213) | Bewertung + **Better Business Bureau** | 6 Std. |
| **08:23** | **Nick Tarrant (#6259)** | **Trading Standards** | **22 Std.** |
| 08:25 | Matt Pinnock (#6606) | Bewertungsankündigung | 9 Min. |

### Warum dieser Fall anders liegt als die übrigen

Bei #6213, #6606, #4829 und #4792 ging es um **Werbeaussagen in Anzeigen**.
Nick Tarrant zitiert etwas, das **auf der Website selbst** steht: „With
replacement guarantee". Er hat nicht argumentiert und nicht gedroht — er hat
**eine sachliche Frage gestellt**, was diese Zusage bedeutet. Diese Frage ist
zweimal unbeantwortet geblieben. Erst danach hat er Trading Standards genannt.

Nach `support-policy.md` ist eine Ersatzgarantie **nicht Teil des Regelwerks**.
Damit steht die Website-Zusage gegen die Policy, und niemand im Support kann
sie beantworten, ohne dass der Owner entscheidet, was gilt.

**Er ist der dritte Kunde, der auf diese Antwort wartet:**

| Datum | Kunde | Beleg |
|---|---|---|
| 14.08. | **Adam Sellens** | hat die Anzeige mitgeschickt; am 15.08. „an unser Team weitergegeben"; seit 25.08. nichts |
| 18.08. | **Gary Sanderson** | dieselbe Ersatzzusage aus der Anzeige |
| 05.09. | **Nick Tarrant (#6259)** | **Zusage steht auf der Website**, zweimal nicht beantwortet, jetzt Trading Standards |

**Dritte Trading-Standards-Nennung** nach Jason Branch und Valerie (#4829).

### Einordnung

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** Behörde eingeschaltet, bestrittene
Werbeaussage, **zwei** Vorlagen-Absagen auf einen Eskalationsfall, eine direkte
Frage zweimal unbeantwortet.

**Keine dritte Absage.** Was er verlangt, ist keine Erstattung, sondern eine
**Auskunft**: was die auf der Website beworbene Ersatzgarantie bedeutet. Solange
der Owner das nicht entschieden hat, ist die einzige ehrliche Antwort, dass die
Frage an den Inhaber gegangen ist — **ohne** die Regel ein drittes Mal zu
zitieren und **ohne** eine Ersatzlieferung zuzusagen, die es im Regelwerk nicht
gibt.

**Kein Erstattungsfall nach der Regel** (Kauschaden). Er steht deshalb **nicht**
auf der Erstattungsliste — die 29,95 £ wären eine Owner-Entscheidung, keine
Regelfolge.

**Vordringlich:** Die Website-Formulierung „With replacement guarantee" gehört
geprüft, bevor der nächste Kunde danach fragt. Sie ist der Auslöser dieses
Falls, und es ist der erste, in dem eine Zusage **aus dem eigenen Shop** — nicht
aus einer Anzeige — bestritten wird.

---

## Lauf 10:20 UTC — #6044 Gregory Williams: der Kunde, der kein Geld will

**Der wichtigste Satz im Postfach seit Tagen — von einem Kunden, der nichts für
sich verlangt.**

**Shopify, geprüft 09.09. 10:2x UTC:**

- **#6044**, bestellt **14.08. 08:56 UTC**, **45,84 £**, `PAID` / `FULFILLED`
- 4 × Plushie (Duck, pig, monkey, hippo)
- Versandt **20.08. 02:14 UTC**, Yanwen Registered Airmail, `VR951952875YP`
- **Dalyellup, Western Australia 6230 — Australien**

### Der Verlauf

- **31.08. 08:59** — „Where is my order? I haven't received any updates"
- **01.09. 12:02 aus dem Postfach** — „shipped and is currently on…"
- **02.09. 02:52 Greg**, direkt gefragt: „May I ask? **When did you guys send my
  items?**"
- **03.09. 10:49 aus dem Postfach** — „your order has shipped and is currently
  on its way. Our **UK warehouse** is currently sold out, so your order was
  shipped from our…" — **das Versanddatum wird wieder nicht genannt.** Es steht
  seit dem 20.08. im System.
- **07.09. 15:19** — „My dog has almost destroyed 1 of the toys already"
- **07.09. 15:31** — „My dog (aka **destructor**) has already ripped a hole in
  the toy I only gave him **30 minutes** ago"
- **09.09. 09:51 aus dem Postfach** — Vorlagen-Absage (Kauschaden)
- **09.09. 10:03 Greg**, zwölf Minuten später:

> „**I'm not expecting my money back, it'll be good if you guys changed your
> ad**"

### Warum dieser Satz zählt

Seit dem 13.08. sind **rund 65 Fälle** mit bestrittener Werbeaussage
aufgelaufen. Fast alle enden in einer Erstattungsforderung, einer Bewertung
oder einer Behörde. **Greg verlangt ausdrücklich kein Geld.** Er nennt als
einzigen Wunsch, dass die Anzeige geändert wird.

Damit sagt ein Kunde von sich aus genau das, was in diesen Logs seit Wochen als
Ursache steht: **das Problem ist nicht die Rückgaberegel, sondern die Werbung.**
Er ist der einzige, dem man nicht entgegenhalten kann, er wolle nur sein Geld
zurück.

**Zugleich ist er der sechste Empfänger einer Vorlagen-Absage in 26 Stunden** —
und der einzige, dessen Antwort **keine** Eskalation ist. Nach #6259 (Trading
Standards heute früh), #6213 (Better Business Bureau), #6606 (Bewertung) und
#7610 (Erstattungsforderung) ist das der Kontrast, der den Punkt macht: Es ist
nicht die Absage allein, die eskalieren lässt — es ist die Absage auf eine
Werbeaussage, die der Kunde für unzutreffend hält, **wenn niemand darauf
eingeht**. Greg geht es nicht ums Geld, also eskaliert er nicht; sein Anliegen
bleibt trotzdem unbeantwortet.

### Einordnung

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** bestrittene Werbeaussage, ausdrücklich an
den Betreiber gerichtete Forderung nach einer Änderung der Anzeige. Das ist
nichts, was der Support entscheiden kann.

**Kein Erstattungsfall** (Kauschaden, und er verlangt keine Erstattung). Er
steht **nicht** auf der Erstattungsliste.

**Was ihm geantwortet werden kann:** dass sein Hinweis an den Inhaber
weitergegeben wurde — und zwar ehrlich, nicht als „wir nehmen Ihr Feedback zur
Kenntnis". Die Vorlage vom 09:51 enthält bereits den Satz „we will take it into
consideration as we review our products"; genau diese Formel hat Nick Tarrant
heute früh mit „I'm not sure I really got an answer" beantwortet.

**Nebenbefund:** Er hat am 02.09. **direkt nach dem Versanddatum gefragt** und
es nicht bekommen, obwohl es seit dem 20.08. in Shopify steht. Damit reiht er
sich in #6751, #8295, #6199 und #6872 ein — fünfter Fall, in dem eine
vorhandene Versandinformation den Kunden nicht erreicht.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Text
rekonstruiert.

---

## Lauf 11:20 UTC — zwei weitere Vorlagen-Absagen, zwei sofortige Rückläufer

Zwischen **09:51 und 11:04** sind heute Vormittag **drei** Vorlagen-Absagen
rausgegangen (Greg #6044, Gary #4273, John Beirne #3344). **Alle drei haben
innerhalb von 7 bis 39 Minuten geantwortet.**

### 🚩 #4273 Gary Lindsay — Werbetext wörtlich zitiert, Chargeback angekündigt

**Shopify, geprüft 09.09. 11:2x UTC:**

- **#4273**, bestellt **02.08. 19:24 UTC**, **27,95 £**, `PAID` / `FULFILLED`
- 2 × Plushie (monkey, hippo), versandt **05.08.**, Yanwen `UL393919732YP`
- Aberdeen AB10 7NW, Zahlung Karte endend **0991**

**07.09. 18:21** — mit **drei zeitgestempelten Fotos**:

> „I received the plushies on 14th August. The first picture below is when they
> were **opened at 17:41**. The 2nd picture is from **18:20, less than 40
> minutes later**. The 3rd is from 18th August, 4 days later. These did not last
> any longer than other toys we have bought. Please advise how to receive a
> refund."

**09.09. 09:55** — Vorlagen-Absage.

**09.09. 10:34**, 39 Minuten später:

> „**Is this a joke?** The advert focuses on the durability of the plushies —
> „**Extremely Durable & Long-Lasting**". And it makes a big point of the
> guarantee — **which is pointless if a dog toy cannot be used by a dog or the
> guarantee is invalidated. This is false advertising.**
> Please respond with how you aim to resolve this or **I will have no option but
> to contact my credit card company**."

**Sein Argument ist neu und trifft den wunden Punkt genauer als alle bisherigen:**
Nicht nur die Werbeaussage sei falsch, sondern die **Garantie selbst sei
gegenstandslos** — sie gelte nur für unbenutzte Ware, also nie für den Fall, für
den das Produkt beworben wird. Das ist dieselbe Beobachtung, die
`bev212.bs@googlemail.com` (06.09.) und **#6286 Deborah Gould** (heute 04:16)
gemacht haben, nur schärfer formuliert. **Drei Kunden in vier Tagen** an
derselben Stelle.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** wörtlich zitierte Werbeaussage,
ausdrücklicher Vorwurf „false advertising", **angekündigter Chargeback**,
Fotobeweis mit Zeitstempeln.
**Keine zweite Absage.** Fünfte Chargeback-Androhung nach #3310, #5111, #5316
und #6173.

### #3344 John Beirne — der zweite „ändert eure Werbung"-Fall an einem Tag

**09.09. 11:04** — Vorlagen-Absage. **11:11**, sieben Minuten später:

> „In light of this might I suggest that your **marketing doesn't make claims to
> be in some way ideal for animals that have chewed through other toys**. The
> reality is that your product is **no different to others at half the price**."

**Er verlangt keine Erstattung.** Wie Greg (#6044) heute früh bittet er darum,
die Werbung zu ändern.

**Das war der Fall, für den im Log vom 08.09. ausdrücklich stand**, er sei „der
einzige Fall dieser Woche, bei dem die Vorlagenantwort **richtig** wäre —
**vorausgesetzt, sie erklärt statt nur abzulehnen**". Die Vorlage hat abgelehnt,
ohne zu erklären, und die Bedingung damit nicht erfüllt. Er hat sachlich
reagiert, aber der Vorbehalt aus dem Log ist eingetreten.

→ `Bot/Escalated - Owner Attention` (Forderung nach Änderung der Werbung —
nichts, was der Support entscheiden kann). **Kein Erstattungsfall.**

### Der Befund

**Zwei von drei Kunden, die heute Vormittag eine Absage bekamen, wollen kein
Geld — sie wollen, dass die Anzeige geändert wird.** Greg um 10:03, John Beirne
um 11:11. Der dritte, Gary Lindsay, kündigt einen Chargeback an und nennt es
„false advertising".

Damit sind es seit gestern früh **acht** Vorlagen-Absagen, von denen **sieben**
umgehend zurückgekommen sind:

| Kunde | Absage | Reaktion | Abstand |
|---|---|---|---|
| Vicky Blow (#7610) | 08.09. 07:57 | Erstattungsforderung | 57 Min. |
| Rena Barnes (#4940) | 08.09. 07:58 | — | offen |
| Meredith Spicer (#6213) | 08.09. 07:58 | Bewertung + **BBB** | 6 Std. |
| Nick Tarrant (#6259) | 08.09. 08:23 | **Trading Standards** | 22 Std. |
| Matt Pinnock (#6606) | 08.09. 08:25 | Bewertungsankündigung | 9 Min. |
| **Greg Williams (#6044)** | **09.09. 09:51** | **„changed your ad"** | **12 Min.** |
| **Gary Lindsay (#4273)** | **09.09. 09:55** | **Chargeback + „false advertising"** | **39 Min.** |
| **John Beirne (#3344)** | **09.09. 11:04** | **„marketing doesn't make claims…"** | **7 Min.** |

### Wieder aufgetaucht, unverändert

**#5036 Lynette Lumley** — keine neue Nachricht. Stand unverändert: Stornowunsch
vom 07.09., 27,95 £, Ware seit dem 22.08. unterwegs, kein Regelfall.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Text
rekonstruiert.

---

## Lauf 12:20 UTC — sechs Vorgänge, darunter eine zweite Absage an einen Eskalationsfall

Am Vormittag sind zwischen 09:51 und 11:19 **fünf** Vorlagen-Antworten
rausgegangen. Die Bilanz mittags:

### 🚩🚩 #6213 Meredith Spicer — die zweite Absage nach der BBB-Meldung

Der Fall stand seit gestern im Log als `Bot/Escalated - Owner Attention` mit dem
ausdrücklichen Vermerk „**Keine zweite Absage.**"

- **08.09. 13:59** Kundin: Bewertung + **Better Business Bureau** wegen „false
  advertising"
- **09.09. 11:19 aus dem Postfach:** **dieselbe Vorlagen-Absage noch einmal** —
  Wort für Wort der Text vom 08.09. 07:58
- **09.09. 12:01** Kundin, ein Wort:

> „**dumb**"

Das ist genau der Ablauf, den `support-policy.md` für Eskalationen ausschließt,
und er ist an einem Fall passiert, der bereits als Eskalation erfasst war. Bei
#4919 Em Gregg (04.09.) und #6259 Nick Tarrant (08.09.) hat dieselbe zweite
Absage zu Verbraucherrechtszitat bzw. Trading Standards geführt.

**46,08 £**, `#6213`. → bleibt `Bot/Escalated`. **Dritte Absage ausgeschlossen.**

### 🚩 #5973 Stephen Cooil — Medienandrohung, und eine unbenutzte Ware wurde mit abgelehnt

**Shopify:** **#5973**, bestellt 13.08., **29,95 £**, `PAID` / `FULFILLED`,
**2 × Plushie (donkey, elephant)**, versandt 22.08., Yanwen `UL442891065YP`.

- **08.09. 09:54** (Zweitkontakt): „I wish to **return both items** for a full
  refund per the advertised 30 day guarantee."
- **09.09. 11:10 aus dem Postfach:** Vorlagen-Absage.
- **09.09. 12:15** Kunde:

> „Your advert makes great claims… with **testimonials** from people who say
> favourable things. **I can't believe these are genuine**… The Elephant is the
> toy destroyed in the video. **We do still have a Donkey, untouched.**
> …this seems like a **scam** and if I don't get satisfaction from you **I will
> be in touch with the media to expose your company**."

**Zwei neue Befunde:**

1. **Der Donkey ist unbenutzt.** Er hat um die Rückgabe **beider** Teile
   gebeten; die Absage hat beide abgelehnt. Der unbenutzte Donkey fällt unter
   **Regel 2**. Das ist der **dritte** Fall dieser Verwechslung nach Carolyn
   Marmalejo (#4812, 21.08.) und der Konstellation bei #6528 Tommy Johnson.
2. **Er bestreitet die Echtheit der Testimonials** und droht mit der **Presse** —
   eine Eskalationsstufe, die es bisher nicht gab (bisher: Bewertungen,
   Trading Standards, BBB, Chargebacks, Sammelklage).

→ `Bot/Escalated - Owner Attention`. **Erstattungsanspruch für den unbenutzten
Donkey** — Anteil von 29,95 £, im Admin auf Positionsebene zu bestimmen.

### 🚩 #6741 Zacharey McLaughlin — zweimal um Rückgabe gebeten, seit 07.09. unbeantwortet

**Shopify:** **#6741**, bestellt 19.08., **61,30 £**, `PAID` /
**`PARTIALLY_FULFILLED`**, 5 × Plushie + Zahnbuddy + E-Book, eine Sendung
25.08., Yanwen US `UL451109674YP`.

- **02.09.:** „I would like to **return** order #6741 for a **full refund**. I
  am very dissatisfied with the quality and **size**."
- **04.09. aus dem Postfach:** Rückfrage nach Details.
- **04.09. Kunde:** „The size of the product is too small for a larger dog. **My
  dog could swallow these.** The quality is that of a walmart $10 toy… Please
  proceed with the refund."
- **06.09. aus dem Postfach:** Teilabsage („While our 30-day money-back
  guarantee applies to items returned…").
- **07.09. 21:59 Kunde, zum dritten Mal:** „**I would like to return the
  products for a full refund please**" — seither **unbeantwortet**.

**Das ist ein Regel-2-Fall.** Er meldet keinen Kauschaden; er will die Ware
zurückgeben, weil Größe und Qualität nicht stimmen. Nichts deutet darauf hin,
dass die Spielzeuge benutzt wurden — im Gegenteil: er hält sie für zu klein, um
sie dem Hund zu geben.

Dazu ein **Sicherheitshinweis**: „my dog could swallow these" ist die
**siebte** Meldung über verschluckbare Teile bzw. Größenrisiko (#6283, Andy
Sire, Kevin Saggers #3197, #6741, die Nadel in #1301, der Quietscher in #6286).

→ `Bot/Escalated - Owner Attention` (dritter unbeantworteter Kontakt,
Sicherheitshinweis). **Erstattung: 61,30 £, Regel 2.** Rücksendung weiterhin
nicht organisierbar — es gibt keine Rücksendeadresse.

### #6004 Tina Mccallion — das fehlende BOGO-Teil

**Shopify:** **#6004**, bestellt 13.08., **29,95 £**, `PAID` / `FULFILLED` —
**nur eine Position: 1 × Plushie „hippo"**, versandt 22.08., 4PX
`4PX3003136921543CN`.

- **29.08.:** „when I bought this it was **buy 1 get 1 free which I never got**
  and my wee dog had it half an hour and it ripped already"
- **31.08. aus dem Postfach:** Antwort, die den Kauschaden bedauert
- **31.08. Kundin, zweimal:** „you state that your toys are **tough and durable
  for all dogs even small dogs** — that's the reason I bought it" + Foto
- **03.09.:** „**Well am I get my order fulfilled**" — seither unbeantwortet

**Der Kern ist nicht der Kauschaden, sondern die fehlende Ware.** Sie sagt, sie
habe „buy 1 get 1 free" gekauft; in Shopify steht **eine** Position. Ob das
Angebot bei ihrer Bestellung angewandt wurde, lässt sich aus der Bestellung
nicht ableiten — das muss im Admin geprüft werden.

→ `Bot/Needs Approval`. **Zuerst klären, ob ihr ein zweites Exemplar zusteht.**
Solange das offen ist, ist jede Antwort zum Kauschaden am Thema vorbei — sie
fragt seit sechs Tagen nach der Ware, nicht nach Geld.

### #5095 Chris Bradley — Routineanfrage

**Shopify:** **#5095**, bestellt **08.08. 13:32 UTC**, **19,95 £**, `PAID` /
`FULFILLED`, 1 × Plushie „donkey", versandt **22.08. 01:43 UTC**, Yanwen
`UL442892208YP`.

**12:16:** „Can you tell me where this order is please, seems a long time in
coming"

Er hat recht: **14 Tage** zwischen Bestellung und Versand, seither 18 weitere.
→ `Bot/Draft Ready`. Versanddatum und Nummer nennen, die Wartezeit offen
benennen. **Kein Zustelldatum.**

### ✅ #7114 Geoffrey Russell — erledigt, und zwar durch eine richtige Antwort

- **09.09. 11:18 aus dem Postfach:** Antwort mit Versandinformation
- **09.09. 11:56 Kunde:** „**Thank you for the update.**"

**Der einzige der fünf Vormittagsantworten, der positiv zurückkam** — und der
einzige, der keine Vorlagen-Absage war, sondern eine Auskunft. Das ist der
Gegenbeleg zu allen anderen Fällen dieses Tages: wenn die Information kommt, ist
der Fall erledigt.

---

## Zwischenstand 09.09. mittags

Seit gestern früh sind **zehn** Vorlagen-Absagen rausgegangen. **Acht** sind
verschärft zurückgekommen, **eine** ist noch offen (Rena Barnes), **eine**
Auskunft (#7114) hat den Fall gelöst.

Neu hinzugekommene Eskalationsstufen an einem einzigen Tag:
**Trading Standards** (#6259), **Chargeback** (#4273, der fünfte),
**Presse** (#5973), **„dumb"** nach der zweiten Absage (#6213) — und zweimal
die Bitte, **die Werbung zu ändern**, ohne Geld zu verlangen (#6044, #3344).

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Storno, kein
Text rekonstruiert, keine Rücksendeadresse erfunden, kein Betrag geschätzt.

---

## Lauf 13:25 UTC — 🚩 #7190 Steve Solley: nicht die Werbung, sondern die Lieferzusage

Ein neuer Fallschnitt. Zum ersten Mal bestreitet ein Kunde nicht die
**Produkt**aussage, sondern die **Liefer**zusage beim Kauf.

**Shopify, geprüft 09.09. 13:2x UTC:**

- **#7190**, bestellt **22.08. 14:52 UTC**, **27,95 £**, `PAID` / `FULFILLED`
- 2 × Plushie (pig, Duck), Sittingbourne ME10 4QT
- Versandt **02.09. 10:53 UTC**, Yanwen, `UL476311114YP` — **elf Tage** nach
  der Bestellung

**09.09. 12:27, Betreff „7190":**

> „I ordered these several weeks ago as I have had little update re delivery
> other than **it's now coming from another country**. I would like to request a
> full refund with immediate effect. **The original order was UK based and
> delivery was 4-5 working days, then I am emailed telling me that was not the
> case** and delivery would take longer. I still have not received the order so
> am requesting **as not the original agreement** a full refund.
> You can issue the refund directly into the account from where it came and will
> **expect this done by close of business today**."

### Warum das ein eigener Fall ist

Alle bisherigen ~68 Streitfälle drehen sich um die **Haltbarkeit**. Dieser
dreht sich um die **Lieferbedingungen zum Zeitpunkt des Kaufs**: er sagt, es
sei „UK based" mit „4-5 working days" verkauft worden, und die Änderung sei ihm
erst **nachträglich per Mail** mitgeteilt worden.

Diese Mail gibt es tatsächlich, und sie geht regelmäßig raus. Wortlaut aus dem
Postfach (u. a. an #5036 Lynette Lumley am 18.08., #7771 Barb Fitzgerald am
01.09., #6116 Sharron Hodges am 31.08., #6044 Greg Williams am 03.09.):

> „Our **UK warehouse is currently sold out**, so your order was shipped from
> our **international warehouse**."

**Er ist der erste, der daraus einen Anspruch ableitet**, statt nur nachzufragen.
Sein Punkt ist nachvollziehbar: elf Tage bis zum Versand, danach internationaler
Transport — das ist etwas anderes als 4–5 Werktage aus einem UK-Lager.

### Einordnung

**Kein Fall der drei Regeln.** Nicht defekt angekommen (Regel 1), nicht
unbenutzt zurückgegeben (Regel 2), und die Stornierung kommt **nach** dem
Versand (Regel 3). Der Bot darf ihm die Erstattung **nicht** zusagen.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** bestrittene Zusage aus dem Kaufvorgang
(Lieferzeit und Lieferland), Fristsetzung („close of business today"). Das
berührt die Angaben im Shop selbst, nicht die Rückgabepolicy — das kann der
Support nicht entscheiden.

**Was sagbar ist:** Versanddatum **02.09.**, Yanwen, `UL476311114YP`, und
offen, dass zwischen Zahlung und Versand elf Tage lagen. **Kein Zustelldatum,
keine Erstattungszusage, und keine Bestätigung seiner Frist.**

**Was zu prüfen ist:** Welche Lieferzeit und welches Versandland standen bei
seiner Bestellung am 22.08. auf der Produkt-/Checkout-Seite? Das entscheidet
seinen Fall — und den aller anderen, die dieselbe „UK warehouse sold out"-Mail
bekommen haben. **Das ist der zweite Website-Text nach „With replacement
guarantee" (#6259, heute früh), an dem sich ein Kunde festmacht.**

**Nicht in der Erstattungsliste** — er fällt unter keine Regel; 27,95 £ wären
eine Owner-Entscheidung.

### Kein Support-Fall

**`marketing-responses@klaviyo.com`** (13:14) — Newsletter des
E-Mail-Marketing-Anbieters („Your latest benchmarks are in"). → `Bot/No Action`.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, keine Fristzusage,
kein Text rekonstruiert.

---

## Lauf 14:25 UTC — 🚩🚩🚩 #5316 David Andrews: elf Vorlagen-Absagen, drei davon **nach** dem Chargeback

Der schwerwiegendste Einzelbefund dieser Logs. Ich habe den vollständigen Thread
gelesen (24 Nachrichten) — bisher war nur der Anfang erfasst.

**Shopify, geprüft 09.09. 14:2x UTC:**

- **#5316**, bestellt **09.08. 16:37 UTC**, **27,95 £**
- **Shopify-Status: `PAID` / `FULFILLED`** — versandt 13.08., Yanwen
  `UL418695131YP`, Kidderminster DY10 2UR

### 🔧 Korrektur an meinen eigenen Logs

Im Log vom **06.09.** steht: „#5316 … **Seit dem 26.08. unbeantwortet.**" Im
englischen Tagesreport von heute früh steht dasselbe: „*unanswered since
26.08.*"

**Beides ist falsch.** Die Angabe stammte aus `search_threads`, das nur die
**fünf ältesten** Nachrichten eines Threads anzeigt. `get_thread` zeigt das
Gegenteil: der Thread ist **nicht unbeantwortet** — er ist **elfmal** beantwortet
worden, jedes Mal mit derselben Vorlage.

### Der tatsächliche Verlauf

| Nr. | Absage aus dem Postfach | Antwort des Kunden |
|---|---|---|
| 1 | 25.08. 10:08 | 25.08. 11:31 — „You marketed this as an **indestructible** dog toy. Refund the full amount now." |
| 2 | 26.08. 18:03 | 26.08. 18:07 — „…which is a lie, what is worse is that **you know it is**" |
| 3 | 28.08. 11:35 | 28.08. 11:37 — „No I require a full refund **NOW**" |
| 4 | 30.08. 12:23 | 30.08. 15:34 — „You are **scammers**… **My bank will pursue you**" |
| 5 | 01.09. 11:53 | 01.09. 11:54 — „No - you will be refunding 100 %" |
| 6 | 02.09. 14:29 | 02.09. 14:40 — „You have **misrepresented the goods** and used **misleading advertising statements** to generate sales that would otherwise not have happened" |
| 7 | 04.09. 09:23 | 04.09. 10:11 — „You will need to refund 100 %" |
| 8 | 05.09. 08:27 | 05.09. 08:33 — „**You are disgusting scammers**" |
| 9 | 06.09. 16:59 | **06.09. 17:02 — „Sorry, 100 %. The bank have refunded me"** |
| 10 | **08.09. 07:59** | 08.09. 08:01 — „Arrange a full refund **today**" |
| 11 | **09.09. 11:05** | **09.09. 13:49 — „this is unacceptable… I require a full refund"** |

### Die drei Punkte, die zählen

**1. Der Chargeback ist bereits durch.** Am **06.09. 17:02** hat er mitgeteilt:
**„The bank have refunded me."** In Shopify steht die Bestellung trotzdem
weiterhin auf **`PAID`** — der Rückbuchung ist im System nichts zugeordnet.
Entweder ist sie noch nicht durchgereicht, oder sie ist übersehen worden. **Das
gehört heute im Zahlungsanbieter geprüft**, denn ein bereits erstatteter Betrag
kann sonst versehentlich ein zweites Mal ausgezahlt werden.

**2. Nach dieser Mitteilung sind noch zwei weitere Absagen rausgegangen** —
08.09. 07:59 und 09.09. 11:05. Beide erklären ihm die Rückgabepolicy für einen
Betrag, den seine Bank ihm bereits zurückgebucht hat. Das ist nicht nur
wirkungslos, es hält einen abgeschlossenen Vorgang künstlich offen.

**3. Elf identische Absagen an einen Fall mit drei Eskalationstriggern.** Er
hat die Werbeaussage bestritten (25.08.), „misrepresented the goods" und
„misleading advertising" ausdrücklich benannt (02.09.) und den Chargeback
angekündigt (30.08.). Nach `support-policy.md` hätte der Fall spätestens am
25.08. an den Owner gehen müssen. Stattdessen ist die Vorlage **elfmal**
verschickt worden — die letzte heute Vormittag, im selben Block wie die
Absagen an #6044, #4273, #3344, #6213 und #5973.

### Einordnung

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund (nur fürs Log):** vollzogener Chargeback, bestrittene
Werbeaussage, ausdrücklicher Vorwurf der Falschdarstellung, **elf**
Vorlagen-Absagen, davon **drei nach** der Mitteilung über die Rückbuchung.

**Keine zwölfte Absage.** Es gibt hier nichts mehr zu verweigern — das Geld ist
nach seiner Angabe bereits zurück. Die einzige sinnvolle Handlung ist, den
Zahlungsstatus zu prüfen und den Thread zu schließen.

**Nicht in der Erstattungsliste** — Kauschaden, und die Rückbuchung ist nach
seiner Angabe bereits erfolgt. **27,95 £ auf keinen Fall ein zweites Mal
auszahlen, bevor der Zahlungsanbieter geprüft ist.**

### Was daraus für die anderen Fälle folgt

`search_threads` zeigt nur die fünf ältesten Nachrichten. Überall dort, wo in
diesen Logs „seit dem … unbeantwortet" steht und der Befund **nicht** durch
`get_thread` bestätigt wurde, kann dasselbe passiert sein. **Zu prüfen sind
insbesondere:** #4919 Em Gregg, #4829 Valerie, #4792 countrygal2473,
Carolyn Marmalejo (#4812), Ann Price (#2228), Adam Sellens, #3310 Tim Carroll.

**Nicht getan:** kein Entwurf, kein Label, keine Erstattung, kein Text
rekonstruiert. **Insbesondere keine zweite Erstattung für #5316 veranlasst.**
