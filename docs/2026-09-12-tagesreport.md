# Paw Friends — Tagesreport
**Zeitraum: 11.09.2026 08:14 UTC – 12.09.2026 08:14 UTC**
**Für: nevio.marasa@icloud.com**

## Zahlen

| Kategorie | Anzahl |
|---|---|
| `Bot/Escalated - Owner Attention` | **14** |
| `Bot/Draft Ready` | **5** |
| `Bot/Needs Approval` | **2** |
| `Bot/No Action` | **3** |
| **Gesamt** | **24** |

**Tatsächlich ausgeführte Erstattungen: keine.**
Es gab keinen bestätigten Regel-4-Fall (falscher Artikel) — nur dafür darf der
Bot selbst erstatten. Unabhängig davon sind `refundCreate` und `orderCancel` im
Shopify-Zugang **gesperrt** (`{"blocked":true,"category":"financial"}`).

**Gesendete Mails: keine.** Es gibt keine Sendefunktion, und `create_draft`
bricht seit dem 21.08. bei jedem Versuch ab. Alle 16 Entwurfstexte des Zeitraums
stehen im Klartext in `docs/entwuerfe-zum-kopieren.md`.

---

## Der wichtigste Befund des Tages

**Zwischen 09:47 und 10:09 gingen sieben Antworten aus dem Postfach. Fünf davon
waren die Kauschaden-Vorlage. Alle fünf sind eskaliert.**

| Absage | Kunde | Reaktion | Abstand |
|---|---|---|---|
| 09:47 | #5973 Stephen Cooil | dritte Nachfrage zum ungeöffneten Teil | 3 Std 56 |
| 09:50 | #5851 Jeff Williams | Chargeback + BBB | 5 Std 18 |
| 09:58 | #7179 Keith Crane | Chargeback | **41 Min** |
| 09:59 | #7101 Cameron Herpich | PayPal + öffentliche Bewertung | **28 Min** |
| 10:01 | #7271 Rosalind Welch | „deceptive" + öffentliche Bewertung | 3 Std 16 |

Die beiden übrigen Antworten waren Lieferauskünfte mit der **7–21-Tage-Formel**.
Eine (#7525) wurde mit einem Dank beantwortet. Die andere (#7190) ist neun
Stunden später als Frist gegen den Shop verwendet worden.

Nach dem 29.08. (sechs von sechs) und dem 09.09. (sechs von sechs) ist das die
**dritte Serie ohne Ausnahme**.

---

## Drei Sachverhalte, die heute neu sind

### 1. Eine Werbezusage, die eine Erstattung verspricht — zweimal unabhängig zitiert

| Zeit | Kunde | Zitat |
|---|---|---|
| 14:01 | **#7060 Felecia Pierce** (San Diego) | „advertised as indestructible **or you get a refund**" |
| 15:08 | **#5851 Jeff Williams** (Cedar Park) | „if a dog destroys this toy then you would **replace it free** — **that is the only reason I ordered**" |

Beide berufen sich auf eine **Anzeige**, nicht auf die Produktseite. Anders als
die bisherigen rund 70 Werbevorwürfe betrifft das keine Haltbarkeitsaussage,
sondern eine **zugesagte Rechtsfolge**. Wenn dieser Text geschaltet wurde, lehnt
die Standardvorlage etwas ab, das der Shop selbst zugesagt hat.

**Ungeprüft.** Der Bot hat festgestellt, dass ein GBP-Werbekonto **„Uk 1"
(`2479996745858211`)** existiert, hat aber **keine Anzeigentexte gelesen**.
→ **Prüfung im Werbekonto und auf der Live-Seite: Owner.**

### 2. Falsch adressierte Antwort mit Kundendaten eines Dritten

Am **09.09. 12:36:59** ging aus `support.pawfriends.uk@gmail.com` an
**`sharronhodges@gmail.com`** (#6116, Kalifornien) eine deutschsprachige Mail
raus, adressiert „Guten Tag **Elisabeth**", über eine Zahlung von **CHF 9.–** und
einen **LUNA Coastal Sandal, Schwarz, Grösse 40**, gezeichnet **„Lisa, Valcor
Zurich"**. 45 Sekunden später ging die eigentlich gemeinte Antwort raus.

Damit sind Name, Kaufbetrag, Artikel, Grösse und Bearbeitungsstand einer Kundin
an eine unbeteiligte Kundin gegangen. Zugleich der erste Beleg dafür, dass aus
demselben Postfach ein zweiter Shop bedient wird.

→ **Owner, sofort.** Benachrichtigung von Sharron Hodges und von Elisabeth sowie
eine mögliche Meldepflicht sind **Rechtsfragen**, keine Support-Entscheidungen.
Der Bot kann die Mail nicht zurückholen und kennt Elisabeths Adresse nicht.

**Ableitung:** Die Läufe prüfen nur `in:inbox`. Dieser Vorfall lag zwei Tage
unbemerkt. **Empfehlung: einmalige Durchsicht von `in:sent` seit dem 13.08.** —
nicht durchgeführt, weil nicht Teil des Auftrags.

### 3. Der Bewertungspool des Hauptprodukts

Abgefragt bei #6606: **78 Bewertungen, Durchschnitt 5,0, keine einzige
negative** — bei rund 70 Haltbarkeitsbeschwerden im Postfach im selben Zeitraum.
**Zehn Einträge mit vollständigen Namen und Haltbarkeits-Testimonials tragen
Zeitstempel vom 01.06.2026 zwischen 18:41:05 und 18:50:57** — aus zehn Minuten.
Die übrigen haben maskierte Namen und generische Texte.

**Der Bot stellt keine Absicht und keine Unechtheit fest**, nur die Zeitstempel.
Damit ist der Vorwurf von #5973 Stephen Cooil vom 09.09. („I can't believe these
are genuine") an den Shop-Daten überprüfbar. Er hat darauf zweimal die
Haltbarkeits-Vorlage bekommen.

---

## `Bot/Escalated - Owner Attention` (14) — mit empfohlenem nächsten Schritt

**Zeitkritisch zuerst.**

| # | Kunde | Betrag | Sachverhalt | Empfohlener nächster Schritt |
|---|---|---|---|---|
| **#7190** | Steve Solley | 27,95 £ | Formelle Stornierung mit **48-Std-Frist (endet 13.09. 19:32)**. Die vom Shop genannte 7–21-Tage-Frist läuft nach seiner Zählung **heute** ab. Verlangt Sendungsnummer **und** Begründung bei Verweigerung. Bestreitet „UK, 4–5 Werktage" als Vertragsbruch. | **Heute** entscheiden. Sendungsnummer `UL476311114YP` (seit 02.09. vorhanden) sofort nennen — sie ist ihm zweimal vorenthalten worden. Erstattungsentscheidung ist Owner-Sache; kein Regelfall. |
| **#7179** | Keith Crane | 35,64 £ | **Sicherheitsmeldung seit 09.09. unbeantwortet**: „my dog is now eating the cotton". Dazu zwei ungeöffnete Plüschtiere (Regel 2), pauschal mit abgelehnt. Chargeback angekündigt. | Tiergesundheitsteil **zuerst** beantworten. Regel-2-Anteil im Admin bestimmen (Kaching-Bundle). |
| **#8081** | Matthew Pierce | 20,35 £ | Seit **29.08. bezahlt und unversandt** (14 Tage). Blockiert durch die Nachforderung einer **Strassenadresse zu einer APO-Anschrift** — die es nicht gibt. Zwei sich widersprechende Antworten binnen 3½ Minuten. Begründung „zwei Postleitzahlen" trifft nicht zu. | Bestellung **freigeben**. Falls er storniert: glatter **Regel-3-Fall**, ohne Rückfrage erstatten. |
| **#5829** | Tasmin Hunt / David Coles | 19,95 £ | Förmliche Rüge nach **Consumer Rights Act 2015**, short-term right to reject. Citizens Advice und Chargeback angekündigt. Zitiert den **Shopify-Produkttitel**. Auslöser war die Vorlagen-Absage vom 10.09., die im Log vom 08.09. ausdrücklich abgeraten war. | Rechtliche Bewertung. **Keine weitere Vorlagen-Absage.** |
| **#6116** | Sharron Hodges | 82,81 £ | Datenschutzvorfall (s. o.). Zusätzlich: neun Positionen bestellt, **bis heute `PARTIALLY_FULFILLED`**, eine einzige Sendung am 25.08. Ihr wurde am 31.08. „your order has been shipped" geschrieben. Dritter Kontakt. | Zwei getrennte Entscheidungen: Datenschutz (Recht) und Nachlieferung/Erstattung der offenen Positionen. **Bewusst kein Entwurf geschrieben**, bis Ersteres entschieden ist. |
| **#5973** | Stephen Cooil | 29,95 £ | **Zweite Absage am 11.09. 09:47**, wieder ohne ein Wort zum ungeöffneten Esel. Fragt zum **dritten Mal**: „How do I go about this?" Medienkontakt am 09.09. angekündigt. | Der Esel ist ein **unstrittiger Regel-2-Fall**. Die Frage ist nur wegen der **fehlenden Rücksendeadresse** (offener Blocker seit 13.08., 30 Tage) nicht beantwortbar. **Diese Adresse ist die Wurzel mehrerer Fälle.** |
| **#6606** | Matt Pinnock | 29,95 £ | Hat die Absage **angenommen** und fragt seit drei Tagen nur noch, **wie man eine Bewertung abgibt**. Zweimal keine Antwort. Verlangt nichts. | Ihm den Weg zur Bewertung **nennen**. Eine dritte Nicht-Antwort ist nach `support-policy.md` unzulässig („scripted concealment"). |
| **#7101** | Cameron Herpich | 28,32 £ | Vier **Screenshots der eigenen Shop-Seite** gesichert, PayPal und öffentliche Bewertung angekündigt. Benennt den Konstruktionsfehler von Regel 2: ein Kauspielzeug ist nicht prüfbar, ohne es zu benutzen. **Lieferung an P.O. Box zugestellt** — dritter Beleg gegen „a P.O. Box cannot be processed". | Der Policy-Einwand gehört entschieden, nicht beantwortet. **#4606 Karen McCormick (71,60 £) ist auf der widerlegten PO-Box-Aussage blockiert.** |
| **#7060** | Felecia Pierce | 20,35 £ | Zitiert „or you get a refund". **Kein Kauschadensfall** — beanstandet das Produkt am Tag der Zustellung. Kaufbeleg beigefügt. | Werbetext prüfen. **Rückfrage im Entwurf:** ob die Ware unbenutzt ist. Wenn ja: Regel 2. |
| **#5851** | Jeff Williams | 44,03 £ | Zitiert die Ersatz-Zusage, **dritte BBB-Meldung** seit 05.09., Chargeback. Erstmail vom 09.09. blieb zwei Tage unbeantwortet. | Werbetext prüfen. Chargeback-Antwort vorbereiten. |
| **dinod28@** | (Name unbekannt) | **unbekannt** | Lehnt das **20-%-Teilerstattungsangebot vom 03.09.** ab: „why have a 30 day money back guarantee if you don't take the toy back?" Hat am 31.08. bestätigt: zweites Spielzeug **unbenutzt, Originalverpackung**. | **Bestellung im Admin suchen** — über `dinod28@aol.com` ist in Shopify weder Bestellung noch Kunde auffindbar. Ohne Nummer ist weder Betrag noch Anteil belegbar. Regel-2-Anspruch besteht. |
| **#7271** | Rosalind Welch | 20,34 £ | **Hat nie eine Erstattung verlangt** — nur die Werbeaussage bestritten. Bekam eine Absage auf eine nicht gestellte Forderung, kündigt jetzt eine öffentliche Bewertung an. | Kein Regelfall. Antwort ohne Wiederholung der Garantiebedingungen. |
| **#8343** | Christopher Hikade | 35,63 £ | Zugestellt 11.09., dem Hund um 12:00 gegeben, um 13:00 alle drei zerstört. Foto, minutengenau. Zitiert den **Artikelnamen** als Versprechen. | Kein Regelfall. **Keine Vorlagen-Absage.** |
| **#7383** | JoAnn Jinks | 20,34 £ | „sold as indestructible", nach 5 Minuten Arme und Ohr ab. Stützt die Forderung auf „not what I payed for". | Kein Regelfall. **Keine Vorlagen-Absage.** |

## `Bot/Needs Approval` (2)

| # | Kunde | Betrag | Sachverhalt | Empfohlener nächster Schritt |
|---|---|---|---|---|
| **#7547** | Luke Prior | 19,95 £ | Ware nicht angekommen, will stornieren. **Kein Regelfall** — versandt 03.09., Storno acht Tage danach. Sendungsnummer lag seit 03.09. vor und wurde ihm nicht genannt. | Ja/Nein zur Erstattung. Sendungsnummer `UL478624693YP` in jedem Fall nennen. |
| **#6755** | Matt Murphy | 30,54 £ | Kauschaden, direkte Erstattungsforderung, **kein Werbezitat, keine Drohung, Erstkontakt**. 14 Tage lagen zwischen Bestellung und Versand. | Ja/Nein zur Erstattung. Kein Eskalationstrigger — aber die Vorlagen-Absage ist nach dem heutigen Befund das schlechteste Instrument. |

## `Bot/Draft Ready` (5)

#7568 Pete Preston · #7525 Carol Garvey · #7853 Matthew Bent · #6799 Adam Garner
· #7248 Dianna Battistella — alles Lieferanfragen. Entwürfe liegen bereit
(ausser #7568: **Volltext nicht im Log**).

**Gemeinsamer Befund:** Bei **drei** Kunden (#7525, #7547, #7190) war eine
Sendungsnummer seit Tagen vorhanden und ist ihnen in der Antwort **nicht genannt
worden**. Bei #6799 hat der Kunde die Nummer und fragt trotzdem, ob versandt
wurde — die Verfolgung zeigt ihm nichts.

## `Bot/No Action` (3)

Kaltakquise `zainababdulsalam697@` · zwei Klaviyo-Dienstmitteilungen.
**Hinweis:** Die Klaviyo-Mitteilung zum Data Processing Agreement gehört
angesichts des Vorfalls bei #6116 vor dem Löschen gesehen.

---

## Die drei Dinge, die heute am meisten bewirken würden

1. **Die Kauschaden-Vorlage abschalten.** Fünf von fünf Eskalationen an einem
   Vormittag; siebzehn von siebzehn über drei Tage.
2. **Eine Rücksendeadresse festlegen.** Sie blockiert seit dem 13.08. jeden
   Regel-2-Fall — aktuell #5973, #7179, #6528, dinod28, #4812.
3. **Die 7–21-Tage-Formel abschalten oder mit Startpunkt versehen.** Sie ist
   gestern bei #7190 als Frist gegen den Shop verwendet worden, neun Stunden
   nachdem sie rausging.
