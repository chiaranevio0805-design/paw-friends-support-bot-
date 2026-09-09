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
