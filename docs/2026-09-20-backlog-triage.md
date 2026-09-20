# Paw-Friends Support — Triage-Protokoll Sonntag, 20.09.2026

**Fristen, die morgen (Montag, 21.09.) ablaufen:**

1. **#7479 Richard Bellamy-Williams — 21.09.** Fünfter Kontakt am 19.09., und
   **als einziger akuter Fall am 19.09. ohne jede Antwort geblieben.** Er hat
   sieben Beschwerde- und Meldewege aufgeführt und verlangt seit fünf Tagen
   zweierlei: eine Rücksendemöglichkeit für einen **ungeöffneten** Fluffy und
   eine Anschrift für Zustellungen. **Beide Antworten existieren** — die
   Fluffys-Seite führt die Garantie ohne Bedingung, und eine vollständige
   Postanschrift steht in den Terms of Service **und in jeder Werbemail.**
2. **#6259 Nick Tarrant — 21.09.** Trading Standards. Ihm wurde am **19.09.
   10:28** geschrieben, die volle Erstattung sei **„processed"**. Shopify:
   `PAID`, `totalRefundedSet` **0,00 £**, `refunds` **`[]`**.

**🔴 Ebenfalls offen, ohne Frist, aber gleicher Schwere:**

- **#5148 Trudi Wright** — Trading Standards seit 19.09. 50 % **dreimal** als
  ausgeführt gemeldet (07.09., 16.09., 18.09.), Shopify `refunds: []`. Ihr wurde
  am **25.08. eine Rücksendeadresse zugesagt**, die es nicht gibt.
- **#6583** und **#4998** — Erstattungen als erledigt mitgeteilt, in Shopify
  nicht vorhanden, Beträge im Log nicht beziffert.

**⏰ Zeitkritisch, solange nichts rausgeht:**

- **#8669 Chad Lovell — 38,19 $.** Storno **elf Minuten** nach der Bestellung
  vom 19.09., `UNFULFILLED`, keine Fulfillments. Am 18.09. wurde dasselbe
  Fenster bei #6870 und #6905 verpasst.

**💷 Schriftlich angenommen, nur noch auszuführen:**
#4055 — 11,97 £ · #6936 — 8,39 £ · #6528 — 22,93 £ · #6159 — 30 % von 30,56 £

**🟦 Stand der Werbefrage:** Seit dem 19.09. ist der Ursprung belegt. Die
Klaviyo-Mail vom **27.08.** aus `paw-friends.uk@paw-friends.uk` führt:
*„30-day money-back guarantee — **Zero risk on your side**"*, *„**you're covered
either way**"*, *„**Nobody has needed it yet**"*, *„**Still unbeaten**"* —
**ohne jede Bedingung.** Die Kauschaden-Absage schreibt gegen diesen Text an;
sie ging in fünf Tagen **vierzehnmal an elf Kunden** und hat **kein einziges Mal
einen Fall beendet.**

---

## Lauf 00:20 UTC

**Drei neue Nachrichten von zwei Absendern.**

### #7440 — Aaron Kell (`aaron.kell30@gmail.com`), 19.09. 23:40 UTC — Erstkontakt

> *„I just received my Elk and Fox toys for my Jack Russell and **within a few
> days** the fox has a hole in its forehead above the eyes and the elks antlers
> are chewed off. Such a joke of a product that is **advertised that no dog has
> ever destroyed one**."*

**Vorab-Suche nach älteren Threads desselben Absenders:** ein einziger Thread.

**⚠️ Zwanzigste unabhängige Kundenaussage zur Werbung.** Seine Formulierung
*„no dog has ever destroyed one"* liegt inhaltlich neben zwei belegten Texten:
der Fluffys-Seite (*„40,000 dogs have tried. **Not one has beaten them yet.**"*,
*„Still undefeated."*) und der Klaviyo-Mail vom 27.08. (*„**Nobody has needed it
yet**"*, *„**Still unbeaten**"*). **Seine Bestellung ist aber ein Plushies** —
dieselbe Konstellation wie bei #7401. **Welche Anzeige ihm gezeigt wurde, ist
von hier nicht feststellbar, und der Entwurf sagt genau das.** Ihm wird
bestätigt, dass eine Aussage dieser Art in unserem Material vorkommt — **ohne
Zuordnung zu einer bestimmten Seite.**

**Shopify (#7440):** bestellt **23.08.**, Versand angelegt **03.09.** (**elf
Tage**), zwei Plushies, **£28,50 / $38,90** (presentment USD, **nichts
umgerechnet**), **0,00 £ erstattet**, Newport, **Pennsylvania (US)**.
**Achtzehnte Bestellung mit auffälliger Versandverzögerung.**

**Er hat nichts verlangt.** Seine Meldung wird **nicht als Erstattungsforderung
ausgelegt**; im Entwurf steht das ausdrücklich, verbunden mit dem Angebot, sie
auf ein Wort hin so weiterzugeben. **Keine Erstattung zugesagt, keine Absage,
keine Vorlagen-Antwort.**

**Label:** `Bot/Escalated - Owner Attention`.

---

### ⛔ `jscalera1@aol.com`, 19.09. 23:40 und 20.09. 00:16 UTC — zwei Meldungen, **Bestellung nicht zuzuordnen**

> *„The monkey **didn't last three hours**. Unbelievable."* (23:40)
> *„**Lasted 5 minutes.** Only 6 month old puppy doing this"* (00:16)

**Zwei getrennte Threads, 36 Minuten auseinander, derselbe Absender.** In einer
Thread-Ansicht sehen sie aus wie zwei Kunden. Beide tragen Bildanhänge —
**nicht geöffnet.**

**Zuordnung ungesichert:**

- `orders(query:"email:jscalera1@aol.com")` → **null Treffer.**
- `customers(query:"scalera")` → **ein** Datensatz: **Joseph Scalera,
  Harrisburg, Pennsylvania — aber unter `jscalera3214@gmail.com`**, einer
  **anderen** Adresse, mit einer Bestellung.

**Namensähnlichkeit ist keine Zuordnung.** Nach der stehenden Regel werden
**keine Bestelldaten an eine Adresse herausgegeben, die nicht an der Bestellung
hinterlegt ist** — und es wird **keine Bestellung auf einen ähnlichen Namen hin
zugeschrieben.** **Der Entwurf enthält deshalb keine Bestellnummer, keinen
Betrag und keine Anschrift**, und **das wird ihm offen gesagt**, verbunden mit
der Bitte um die Bestellnummer im Klartext.

**Für den Owner:** Der Datensatz *Joseph Scalera / `jscalera3214@gmail.com` /
Harrisburg PA* existiert. **Ob er mit dem Absender identisch ist, kann nur im
Admin geprüft werden — hier wird es nicht behauptet.**

**Er hat nichts verlangt.** Auch seine Meldungen werden nicht ausgelegt.
**Keine Anrede mit geratenem Vornamen** — er hat nicht unterschrieben.

**Label:** `Bot/Escalated - Owner Attention` (ungesicherte Zuordnung +
Haltbarkeitsbeschwerde).

---

### Stand nach diesem Lauf

- **Zwei Kundenvorgänge am 20.09.** (drei Nachrichten von zwei Absendern).
- **Dreiundneunzig Entwürfe**, **keiner in Gmail** — `create_draft` seit 21.08.
  blockiert (21 Versuche, kein 22.).
- **Keine Erstattung ausgeführt.** Kein Fall fiel unter Regel 4.
- **⚠️ Zwanzig unabhängige Kundenaussagen zur Werbung.**
- **⏱️ Achtzehnte Bestellung mit auffälliger Versandverzögerung.**
- Die Fristen und offenen Punkte aus dem Kopf dieser Datei bleiben unverändert
  bestehen.

---

## Lauf 03:20 UTC

**Ein neuer Kundenvorgang. Keine Sendungen aus dem Shop-Konto seit 19.09. 10:57.**

### #8053 — Angie Zgonina (`azgonina@icloud.com`), 20.09. 02:47 UTC — Erstkontakt

> *„Your plushies and fluffies lasted about 10 minutes! **What a scam!!!**"*

**Vorab-Suche nach älteren Threads desselben Absenders:** ein einziger Thread.

**Shopify (#8053):** bestellt **28.08.**, Versand angelegt **08.09.** (**elf
Tage**), **vier Positionen** — zwei Plushies **und zwei Paw-Friends™-Fluffys —**,
**£59,05 / $79,93** (presentment USD, **nichts umgerechnet**), **0,00 £
erstattet**, Richview, **Illinois (US)**. **Neunzehnte Bestellung mit
auffälliger Versandverzögerung.**

**Der höchste Einzelbetrag unter den Haltbarkeitsbeschwerden dieses und des
Vortages.**

**Besonderheit gegenüber den bisherigen Fällen:** Sie hat **beide Produktlinien**
gekauft. **Die Fluffys-Beschreibung führt „✓ 30-day money-back guarantee" ohne
jede Bedingung** (Vollabgleich aller zwölf Produkttexte am 18.09.). **Das wird
ihr im Entwurf wahrheitsgemäß genannt** — zusammen mit dem **ausdrücklichen
Hinweis, dass damit nichts entschieden ist** und die Entscheidung beim Owner
liegt. **Es wird weder behauptet, die Garantie decke ihren Fall, noch wird eine
„unbenutzt"-Bedingung erfunden, die dort nicht steht.** Das ist der schmale Grat
zwischen Verschweigen und Zusagen, und er wird hier bewusst so gezogen.

**Sie hat nichts verlangt.** *„What a scam"* ist eine Bewertung, keine
Forderung. **Ihre Meldung wird nicht als Erstattungsforderung ausgelegt**;
stattdessen das Angebot, sie auf ein Wort hin so weiterzugeben. **Auf das Wort
„scam" wird nicht reagiert** — weder zustimmend noch widersprechend.

**Keine Erstattung ausgeführt, keine zugesagt, keine Absage, keine
Vorlagen-Antwort.**

**Label:** `Bot/Escalated - Owner Attention` (Haltbarkeitsbeschwerde über beide
Produktlinien + Entscheidung außerhalb der Regel + eigener Versandverzug).

---

### Stand nach diesem Lauf

- **Drei Kundenvorgänge am 20.09.**
- **Vierundneunzig Entwürfe**, **keiner in Gmail.**
- **Keine Erstattung ausgeführt.** Kein Fall fiel unter Regel 4.
- **⏱️ Neunzehnte Bestellung mit auffälliger Versandverzögerung.**
- Die Fristen und offenen Punkte im Kopf dieser Datei bleiben unverändert:
  **#7479 und #6259 laufen heute ab.**
