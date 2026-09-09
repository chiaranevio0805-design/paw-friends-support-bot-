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
