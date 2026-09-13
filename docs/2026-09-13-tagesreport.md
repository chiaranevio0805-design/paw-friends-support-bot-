# Paw Friends — Tagesreport
**Zeitraum: 12.09.2026 08:14 UTC – 13.09.2026 08:14 UTC**
**Für: nevio.marasa@icloud.com**

## Zahlen

| Kategorie | Anzahl |
|---|---|
| `Bot/Escalated - Owner Attention` | **16** |
| `Bot/Needs Approval` | **7** |
| `Bot/Draft Ready` | **2** |
| **Gesamt** | **25** |

**Tatsächlich ausgeführte Erstattungen: keine.** Kein bestätigter Regel-4-Fall;
`refundCreate` und `orderCancel` sind im Shopify-Zugang gesperrt.
**Gesendete Mails: keine.** Es gibt keine Sendefunktion.

## 🔴 Zum Gmail-Entwurf — Abweichung von der Routine

Der Auftrag verlangt einen Gmail-Entwurf an `nevio.marasa@icloud.com`.
**Dieses Mal wurde `create_draft` bewusst nicht aufgerufen.**

Grund: 21 Versuche seit dem 21.08., jeder mit demselben Ablauf — Schema lädt,
Worker-Prozess startet neu. **Gestern hat der Versuch den Chat-Report gekostet**;
er kam erst eine Stunde später beim nächsten Trigger an. Der Entwurfskanal hat
noch nie funktioniert, der Versuch zerstört aber zuverlässig den Kanal, der
funktioniert.

**Der Report liegt vollständig hier und ist gepusht.** Soll weiter täglich
versucht werden, genügt ein Wort — dann wird der Versuch wieder aufgenommen.

---

## Der Befund des Tages

**Zum ersten Mal wurde ein Werbevorwurf an den eigenen Shopify-Stammdaten
geprüft** — ausgelöst von **#7292 tracy hartley** (22:15).

**Wörtlich in der Produktbeschreibung nachgewiesen:**
- „**Anti-tear design built for strong chewers**"
- „**The result: A toy that lasts longer and stands up to everyday adventures.**"
- „**Reinforced double stitching to help prevent tearing**" (das Zitat aus #5829 und #6877)
- „Rope-reinforced construction for extra durability", „Shape-retaining structure for long-lasting play", „Built tough for tugging, carrying, chewing, and cuddling"

**Zwei Befunde aus derselben Abfrage:**

1. **Das Wort „indestructible" steht nicht in der Produktbeschreibung.** Kein
   einziges Mal — obwohl Dutzende Kunden es zitieren. **Herkunft offen** (Anzeige,
   anderer Seitenbereich, frühere Fassung). **Owner-Prüfung.**
2. **Der Garantietext steht nicht im Beschreibungsfeld.** Damit ist die
   Kernaussage von #7292 **weder bestätigt noch bestreitbar**:

   > „If you're not completely satisfied **for any reason**, simply contact us
   > within 30 days… **I cannot find any statement on the product page saying
   > that the 30-day guarantee applies only if the toy is unused and
   > undamaged.**"

   **Auf der Live-Seite zu verifizieren.** Trifft es zu, behauptet die
   Standardvorlage eine Bedingung, die die veröffentlichte Garantie nicht
   enthält.

Sie zitiert ausserdem den eigenen Sicherheitshinweis („Remove the toy
immediately at the first signs of damage") — **sie hat ihn befolgt und wird
deshalb abgelehnt.**

## Die Vorlagen-Bilanz

**Am 12.09. gingen drei Kauschaden-Absagen raus — alle drei eskaliert**
(#6286 nach 1 Std 41, #7316 nach 1 Std 33, **#4745 nach 4 Minuten 26** — der
schnellste Wert im Projekt).

**Korrektur, dritte Fassung:** Am 11.09. waren es **sieben** Absagen, nicht
sechs — die an #7292 um 10:05:57 fehlte. **Alle sieben eskaliert.**
**Gesamt: zehn von zehn.** Ursache der Untererfassung ist strukturell: die Läufe
lesen `in:inbox`; ausgehende Mails werden erst sichtbar, wenn ein Kunde
antwortet. **Alle Zählungen ausgehender Vorlagen sind Mindestzahlen.**

**Ausserdem im Umlauf:**
- Ein **30-%-Teilerstattungsangebot** an #7506 (mindestens das 13. seit 22.08.) —
  zwei Tage nachdem die Chronologie im Log stand.
- Eine **zweite Standardvorlage**, die in keinem Log stand: „**no plush toy can
  be guaranteed to be completely indestructible**" (#4726, 04.09.). Sie
  widerspricht dem Produktnamen und den heute belegten Haltbarkeitszusagen.
- Die **7–21-Tage-Formel** an #7627 und #7699 — bei #7627 **ohne** die seit dem
  03.09. vorhandene Sendungsnummer **und ohne ein Wort zu ihrer
  Erstattungsbitte vom 10.09.**

## Was sich verschoben hat

**Fünf Kunden verlangen die Änderung der Werbung statt Geld** — #6280, #6286,
#6891, plus zwei am 10.09.
**Sechs Kunden forderten überhaupt nichts** — #4939, #6936, #6891, #6280,
#5032, #7645.
**Vier unabhängige Formulierungen des Regel-2-Konstruktionsfehlers** — #7101,
#7316, #6891 („**not being able to return something that is not what is promised
is not a return policy**"), #7292.
**Drei Kunden bezweifeln die Bewertungen** — #5973, #4745, #7645.
**Fünf Kunden fragten, wie eine Rücksendung geht** — #6781, #7246, #6528,
#5973, #5186. **Alle unbeantwortbar: es gibt keine Rücksendeadresse, offen seit
dem 13.08. — 31 Tage.**

---

## `Bot/Escalated - Owner Attention` (16)

| # | Kunde | Betrag | Sachverhalt | Nächster Schritt |
|---|---|---|---|---|
| **#7292** | tracy hartley | 28,50 £ | Hält die Vorlage gegen den veröffentlichten Garantietext. Hat den eigenen Sicherheitshinweis befolgt. **Verschluckungsmeldung vom 10.09. („the tag that my dog swallowed") weiterhin unbeantwortet.** Bietet Rückgabe des **ungeöffneten Duck** an. | **Garantietext auf der Live-Seite prüfen.** Tiergesundheitsteil beantworten. Regel-2-Anteil für den Duck im Admin. |
| **#6528** | Tommy Johnson | Anteil offen | **Fünfter Kontakt.** Bitte vom 11.09., eine Rücksendung für **drei ungeöffnete** Teile einzurichten, seit 37 Std unbeantwortet. Durchgehend höflich. | Unstrittiger Regel-2-Fall. **Rücksendeadresse ist der Blocker.** |
| **#2283** | Tara Harte | **19,95 £** | Erstattung am **17.07. zugesagt**, seit **57 Tagen** nicht gezahlt. Vorgang läuft seit 22.06. | Auszahlen oder ihr sagen, warum nicht. |
| **#4726** | Marilyn Penniall | 34,95 £ | Dritter Kontakt, beruft sich auf die Geld-zurück-Garantie, „**not as described, promised or advertised**". Bestellung seit 06.08. `PARTIALLY_FULFILLED`. Sendungsnummer seit 22.08. nicht genannt. | Lieferumfang im Admin klären; Erstattungsentscheidung. |
| **#6891** | Michael Palermo | 43,92 £ | Verlangt **kein Geld**, sondern Änderung von Werbung **und** Rückgabepolicy. Schärfste Fassung des Regel-2-Problems. | Beide Texte entscheiden. |
| **#6286** | Deborah Gould | — | **Vierte Kontaktaufnahme**, zweite identische Absage **nach** ihrer ACCC-Meldung. „You must see now that it is **false advertising**." | Garantiebedingungen klären. |
| **#6280** | Jasin Vandenbroeke | 30,56 £ | Erstattungsforderung **fallengelassen**, verlangt nur noch Änderung der Werbung. | Werbetext entscheiden. |
| **#7316** | Brett Merriman | 20,34 £ | „Why would I return it before it got used?" | Rückgabebedingung entscheiden. |
| **#4745** | Steph Hanlon | 54,95 £ | Eskalation nach **4 Min 26**. Verweist auf externe Bewertungen. Verlangt nichts. | Kein Regelfall; Bewertungsfrage. |
| **#7165** | Andrea Dentel | 28,50 £ | „**too dangerous for my dog**" — Sicherheitsmeldung. Zweites Teil ungeklärt. | Rückfrage abwarten, dann Regel 2 prüfen. |
| **#6781** | Carlie Terry | 29,95 £ | „durable and long lasting" bestritten, zwei Fotos in acht Minuten. Fragt nach dem Rückgabeverfahren. | Rücksendeadresse. |
| **#7246** | Barbara Crouch | 28,50 £ | Zehn Minuten, Foto, „How do i get refunded?" | Rücksendeadresse. |
| **#6936** | Lisa Steggel | 27,95 £ | Unter einer Stunde, Quietscher liegt frei, beruft sich auf die Werbung, verlangt nichts. | Zweites Teil klären. |
| **#6882** | Chris Cobb | 30,66 £ | 15 Minuten, „**Please explain**". Währungsdifferenz 58,56 AUD / 30,66 £. | Erklärung, nicht Policy. |
| **#7645** | Betty Brown | 43,92 £ | Zehn Minuten. Bestreitet Werbung **und** Bewertungen. Neuer Zusteller D&S Express. | Bewertungsfrage; zwei weitere Positionen klären. |
| **becca23047@aol.com** | — | **unbekannt** | „Destroyed in 5 minutes", Erstattung des ganzen Auftrags verlangt. **Keine Bestellung zu dieser Adresse auffindbar**, Daten nur als Screenshot. | **Anhänge öffnen, Bestellung identifizieren.** |

## `Bot/Needs Approval` (7)

| # | Kunde | Betrag | Sachverhalt | Nächster Schritt |
|---|---|---|---|---|
| **#5407** | Nicolette Kirkwood | 27,95 £ | Versandt **13.08.**, **nie angekommen — 30 Tage**. Versand war schnell (3 Tage); die Verzögerung liegt vollständig im Transport. | Ersatz oder Erstattung — ein Sachstand ist keine Antwort mehr. |
| **#6420** | Keith Grice | 30,54 £ | **Als zugestellt gescannt** (25.08., Paketkasten), nie erhalten, keine Benachrichtigung, Trackingseite öffnet nicht. | Ersatz oder Erstattung. **Nicht an den Zusteller verweisen.** |
| **#7627** | Charlotte Matthews | 27,95 £ | Erstattungsbitte vom 10.09. **in der Antwort übergangen**. „I will know not to purchase again." | Ja/Nein zur Erstattung. Sendungsnummer nennen. |
| **#7506** | Adam Dowell | 28,51 £ | 30 % angeboten, **50 % gegengefordert**, nimmt sonst 30. Fragt nach grösseren Varianten. Hatte am 10.09. eine Rücksendung wegen der Grösse verlangt. | Prozentsatz entscheiden; Sortimentsfrage beantworten. |
| **#7874** | Patricia Butler | 28,50 £ | „money back **or** sent my order". Ware unterwegs. | Ja/Nein. |
| **#7699** | Lorraine Sale | 27,95 £ | Eigene Frist **17.09.** | Vor dem 17.09. entscheiden. |
| **#4939** | Sara Thompson | 34,95 £ | Geschenk, 20 Minuten, keine Forderung. Bestellung seit **07.08. `PARTIALLY_FULFILLED`** — 36 Tage. | Lieferumfang klären. |

## `Bot/Draft Ready` (2)

**#8359** (44,06 £, Lieferanfrage; Bestellung auf Norma Vickroy, Mail von
gary.lisacooper@ — Anrede vor dem Senden klären) · **#5032** Adam Murgatroyd
(42,90 £, alle drei Teile in einer Stunde, keine Forderung, „won't order again")

---

## ⏰ Heute fällig

- **#7190 Steve Solley** — seine 48-Stunden-Frist endet **heute 19:32**.
  Die von ihm berechnete Lieferfrist ist am 12.09. abgelaufen. **Kein Regelfall
  — die Entscheidung ist Owner-Sache und läuft heute ab.**

## Die drei Dinge mit der grössten Wirkung

1. **Die Kauschaden-Vorlage abschalten** — zehn von zehn Eskalationen.
2. **Eine Rücksendeadresse festlegen** — blockiert seit 31 Tagen fünf offene
   Regel-2-Ansprüche.
3. **Den Garantietext und das Wort „indestructible" auf der Live-Seite und im
   Werbekonto prüfen.** Beides ist heute konkret geworden und beides ist die
   Grundlage fast aller offenen Fälle.
