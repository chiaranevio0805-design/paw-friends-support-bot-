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
