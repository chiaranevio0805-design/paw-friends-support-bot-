# Paw Friends — Backlog-Triage, Donnerstag 1. Oktober 2026

**Übertrag aus dem 30.09.** (Tagesabschluss im Protokoll vom Vortag):
elf Kundenfälle, **425 Entwürfe in `docs/entwuerfe-zum-kopieren.md` und keiner
davon in Gmail**, **fünfzehn offene Geldzusagen** (drei ausdrücklich
angenommen, eine — **#5973** — zweimal schriftlich als ausgeführt bestätigt,
obwohl der Datensatz **£0,00** zeigt), **zehn Menschen mit ungeöffneter Ware
ohne Rückgabeweg**, **mindestens fünf Sicherheitsmeldungen**, und die
**Passkey-Warnung vom 26.09.**, heute **fünf Tage alt**.

**Weiterhin gesperrt:** `create_draft` und sämtliche Label-Werkzeuge
(seit 21.08.), `refundCreate` und `orderCancel`. **Dieses Postfach hat keine
Sendefunktion.**

---

## Lauf 00:20 UTC — ein Fall

### 🟥 #7831 — Mary Hollerich (`mhollerich89@gmail.com`), US — **Bot/Escalated – Owner Attention**

**Eingegangen 30.09. 23:36:21 UTC**, sechzehn Minuten nach dem Tagesabschluss
vom 30.09. **In einem neuen Thread** (`Defective dog toys`), nicht im alten.

**Eskalationsgrund:** bestrittene Werbeaussage **und** angekündigter
öffentlicher Beitrag **und** angekündigte Meldung an eine Stelle **und**
wiederholter unbeantworteter Kontakt — **der vierte.**

**🟥 Die Pflichtsuche nach älteren Threads derselben Absenderin hat den Fall
erst sichtbar gemacht.** Ohne sie wäre dies als Erstkontakt eingestuft worden.
Der Verlauf:

| Datum | Was passiert ist |
|---|---|
| **23.09. 09:53** | Erstkontakt (Thread `Items`): *„Your toys destroyed with 5 min of giving them to my dog… You should refund my money for all of it."* |
| **28.09. 11:10** | **Fünf Tage später:** Kauschaden-Vorlage, angeredet mit **„Dear Customer"**, obwohl sie unterschrieben hatte |
| **28.09. 14:20** | *„This is the most bazar response I have ever heard… I'll post this all over face book so others can see."* — **nie beantwortet** |
| **28.09. 17:10** | *„I am reporting you to the BB."* — **nie beantwortet** |
| **30.09. 23:36** | **Neuer Thread**, dieselbe Forderung: *„They did not hold up like your advertisement stated. I would like a full refund."* |

**Shopify-Befund, heute geprüft:** `#7831` — bestellt **26.08.**, versandt
**03.09.** (**acht Tage**), Gesamtbetrag **US$48,58**,
`totalRefundedSet` = **$0.00**, `refunds` leer, `cancelledAt: null`.

**🟦 Drei Plushies-Positionen — und eine vierte Position, die nie geliefert
wurde:** das E-Book *„Why Your Dog Destroys Every Toy (And How to Finally Stop
It)"* steht mit **`unfulfilledQuantity: 1`**. **Sie hat dafür bezahlt und es
nicht bekommen.** Das ist unabhängig vom Streit über die Haltbarkeit und steht
im Entwurf als eigener Punkt.

**Entwurf geschrieben.** **Die beiden früheren #7831-Entwürfe (23.09. und
28.09.) sind als ersetzt markiert.**

**🟥 Eine Korrektur am Entwurf vom 28.09., die hier festgehalten gehört:**
jener Entwurf machte aus ihrem *„the BB"* ein ausgeschriebenes **„Better
Business Bureau"**. **Das war eine Deutung ihrer Worte und keine Information,
die im Thread steht.** Der neue Entwurf benennt die Meldung nur so, wie sie
sie genannt hat. Gesendet wurde der alte Entwurf nie.

**Im neuen Entwurf ausdrücklich NICHT:** keine zweite Kauschaden-Vorlage (und
gesagt, dass keine kommt); keine Erstattung zugesagt, kein Termin, keine
Absage; keine Garantieentscheidung in irgendeine Richtung; nicht behauptet,
die von ihr erinnerte Werbeaussage existiere nicht; keine Rekonstruktion der
Anzeige; **nichts an ihren angekündigten Beitrag oder ihre Meldung geknüpft**
und nicht um Aufschub gebeten; **ihr nicht vorgehalten, die Artikel
weggeworfen zu haben**; kein Nachweis verlangt; **der Betrag in USD genannt,
nicht in GBP umgerechnet und nicht aufgeteilt**; nichts aus ihrem Welpen
gefolgert.

**Keine Erstattung ausgelöst** — `refundCreate` gesperrt, und #7831 ist kein
Regel-4-Fall. **Nichts versendet.**

### Stand nach diesem Lauf

- **Kundenfälle am 01.10.: einer.**
- **Entwürfe in der Datei: 426.** **Weiterhin die Zahl der geschriebenen
  Texte, nicht der versendbaren Antworten.**
- **🟦 Die E-Book-Position auf #7831 ist eine weitere unter den bereits
  dokumentierten Bestellungen mit nicht ausgelieferten E-Book-Zeilen.**

---

## Lauf 01:20 UTC — nichts Neues im Posteingang · #8295 abgearbeitet

**Posteingang geprüft: keine neue Nachricht seit 23:36 UTC.** Die #7831 aus
dem 00:20-Lauf bleibt die jüngste.

**Stattdessen den seit dem 30.09. offenen Posten erledigt: den
zusammengeführten Entwurf für #8295.**

### 🟥 #8295 — Ivan Griffen (`griffenivan@gmail.com`), GB — **Bot/Escalated – Owner Attention**

**Er hat in FÜNF getrennten Threads geschrieben**, alle zur selben Bestellung,
und wurde in jedem behandelt, als wäre er jemand anderes. **In der
Entwurfsdatei standen sechs Fassungen.** **Alle sechs sind jetzt als ersetzt
markiert; es gibt genau einen geltenden Entwurf.**

**Vollständiger Verlauf, aus allen fünf Threads zusammengesetzt:**

| Datum | Was passiert ist |
|---|---|
| 31.08. 01:24 | Bestellung #8295 |
| 05.09. | *„When is my order going to arrive and when will I get a tracking number."* |
| **06.09. 17:04** | **Antwort: „your order has been shipped and is currently on its way"** |
| 06.09. 17:45 | *„Havel you got a tracking number"* |
| 07.09. | Zweimal *„Can I have a tracking number please"* — in **zwei weiteren Threads** |
| **08.09. 07:47** | **Tatsächlicher Versand laut `fulfillments.createdAt`** |
| 08.09. 08:20 / 08:24 | Zwei Antworten, „shipment details have been received" |
| 09.09. | Trackingnummer gegeben |
| 17.09. | **Vierter Thread:** *„Thought I would pre warn you that it looks like Evri may have lost my package"* |
| 18.09. | **Fünfter Thread:** *„Still haven't got my order"* |
| **18.09. 14:30** | *„I have sent you a few emails with out receiving a response **I need you to refund my money**"* |
| 21.09. 09:40 | **Drei Tage später:** ein Tracking-Absatz an **„Dear Customer"** — **die Erstattungsforderung wird nicht erwähnt** |
| 21.09. 10:54 | *„It took 8 minutes for my dog to destroy the toy"* — das Paket war also angekommen |
| 24.09. 12:25 | Kauschaden-Vorlage, angeredet **„Dear IVan"** |
| 24.09. 12:29 | *„Absolutely crap marketing a **scam advert** to get people's to buy !! will be showing the state of the toy after 8 minutes on facebook"* |
| 28.09. 11:22 | **Zweite Kauschaden-Vorlage**, wieder **„Dear Customer"** |
| seither | **nichts mehr von uns, nichts mehr von ihm** |

**🟥 Zwei Befunde, die bisher nirgends standen:**

1. **Am 06.09. wurde ihm geschrieben, die Bestellung „has been shipped and is
   currently on its way". `fulfillments.createdAt` ist der 08.09. 07:47.**
   **Als ihm gesagt wurde, es sei versandt, war es nicht versandt** — zwei
   Tage zu früh.
2. **Seine Erstattungsforderung vom 18.09. wurde nie als Erstattungsforderung
   beantwortet.** Sie steht wörtlich im Thread, und die Antwort vom 21.09.
   ging auf alles andere ein. **Heute sind das dreizehn Tage.**

**Shopify-Befund:** `#8295` — bestellt **31.08.**, versandt **08.09.**
(**acht Tage**), **£27,95**, zwei Plushies zum Bündelpreis,
`totalRefundedSet` = **£0.00**, `refunds` leer, `cancelledAt: null`.

**Im Entwurf ausdrücklich NICHT:** **der Zusteller wird nicht erwähnt und er
wird nicht an ihn verwiesen**, obwohl er ihn selbst mehrfach genannt hat — die
Verzögerung wird allein unserem Versanddatum zugeschrieben; **die
Trackingnummer wird nicht als Zustellnachweis benutzt** (dass das Paket ankam,
steht fest, weil er es selbst geschrieben hat); **nicht gesagt, seine
Bewertung nach acht Minuten sei verfrüht**; keine dritte Kauschaden-Vorlage;
keine Erstattung zugesagt, kein Termin, keine Absage; keine
Garantieentscheidung; **nicht behauptet, die Werbung sei kein „scam advert" —
und auch nicht, dass sie einer sei**; keine Rekonstruktion der Anzeige;
nichts an seinen angekündigten Beitrag geknüpft; vor dem Porto gewarnt;
nichts aus seinem Hund gefolgert.

**Keine Erstattung ausgelöst, nichts versendet.**

### Stand nach diesem Lauf

- **Entwürfe in der Datei: 427.**
- **Offene Posten aus der Entwurfsdatei-Prüfung: #8295 ist erledigt.**
  **Offen bleiben: #7608** (zwei Threads — unklar, ob der neueste den
  Gratis-Artikel und die Füllung aus dem ersten Thread abdeckt) **und 87
  weitere Kunden**, die nur die neutrale Warnzeile tragen, sowie **der
  vollständige Durchgang auf veraltete Zeitangaben.**

---

## Lauf 02:20 UTC — nichts Neues im Posteingang · #7608 abgearbeitet

**Posteingang geprüft: leer seit 23:36 UTC.**

**Stattdessen den zweiten seit dem 30.09. offenen Posten erledigt: die
Entscheidung zu #7608.** Die Frage war, ob der Entwurf vom 29.09. den ersten
Thread mit abdeckt. **Antwort: nein — und zwar in einem Punkt, der schwerer
wiegt als gedacht.**

### 🟥 #7608 — Patricia Arenella (`patty.arenella@gmail.com`), US — **Bot/Escalated – Owner Attention**

**Zwei Threads, beide zur selben Bestellung. In der Datei standen fünf
Fassungen. Alle fünf sind jetzt als ersetzt markiert; es gibt genau einen
geltenden Entwurf.**

| Datum | Was passiert ist |
|---|---|
| 24.08. | Bestellung #7608 |
| 03.09. | Versand (**zehn Tage**) |
| **13.09. 20:06** | Erstkontakt: *„My dog destroyed the toy in 3 minutes… I would like a full refund I can send a photo also **the toxic stuffing was very dangerous for my dog to swallow**"* |
| 15.09. | **Vorlage 1**, „Dear Patricia" |
| 19.09. | *„Your advertisement stated that the toys are indestructible…"* |
| 22.09. 11:10 | **Vorlage 2**, „Dear Patricia" |
| **22.09. 14:12** | *„In addition it was **buying one get one free, which I never received** kindly refund me or…"* |
| 24.09. | **Vorlage 3**, „Dear Customer" |
| 23.09. | **Zweiter Thread** eröffnet: `Damaged toy order 7608. Please refund` |
| 28.09. | **Vorlage 4**, „Dear Customer" |
| 29.09. 17:33 | *„This is a **con job**… Also the advertisement stated that there was a gift…"* |

**🟥 Zwei Fehler in der bisherigen Bearbeitung, beide hier korrigiert:**

1. **Ihre Sicherheitsmeldung vom 13.09. — die Füllung, die ihr Hund
   verschlucken könnte — ist in allen vier Vorlagenbriefen UND im Entwurf vom
   29.09. überhaupt nicht vorgekommen.** **Heute sind das achtzehn Tage.**
   Sie gehört zu den mindestens fünf dokumentierten Sicherheitsmeldungen; der
   neue Entwurf gibt sie **getrennt vom Erstattungsthema** als
   Sicherheitsmeldung weiter, **ohne jede Aussage zur Sicherheit oder
   Giftigkeit in irgendeine Richtung.**
2. **Die Überschrift des Entwurfs vom 29.09. lautete „nennt erstmals ein
   beworbenes Geschenk". Das stimmt nicht.** Sie hat den fehlenden
   Gratisartikel **bereits am 22.09.** genannt. Der neue Entwurf sagt ihr
   ausdrücklich, dass sie es zweimal geschrieben hat und beide Male keine
   Antwort bekam.

**Dritte, kleinere Korrektur:** der Entwurf vom 29.09. nannte den Artikel
„the monkey plush toy". **Der Datensatz gibt das nicht her** — die Position
heißt schlicht „Plushies – Designed for Furry Friends Who Destroy
Everything". Der neue Entwurf sagt nur „one item".

**Shopify-Befund:** `#7608` — bestellt **24.08. 17:44**, versandt
**03.09. 07:40** (**zehn Tage**), **US$27,75**, **genau eine Position**,
`totalRefundedSet` = **$0.00**, `refunds` leer, `cancelledAt: null`.
**Kein Gratisartikel und keine zweite Position auf der Bestellung.**

**Keine Erstattung ausgelöst, nichts versendet.**

### Stand nach diesem Lauf

- **Entwürfe in der Datei: 428.**
- **Beide am 30.09. offen gelassenen Posten sind erledigt: #8295 und #7608.**
- **Offen bleiben: 87 Kunden mit reiner Warnzeile** (mehrere Fassungen, nicht
  geprüft, welche gilt) **und der vollständige Durchgang auf veraltete
  Zeitangaben.**
- **🟥 Für den Owner neu auf der Liste:** **#7608 ist die zweite
  Sicherheitsmeldung, die wochenlang unter Kauschaden-Vorlagen verschwunden
  ist** — die andere ist #7749. **Beide sind weiterhin unbeantwortet.**

---

## Lauf 03:20 UTC — nichts Neues im Posteingang · dritter offener Posten begonnen

**Posteingang geprüft: leer.**

**Den dritten seit dem 30.09. offenen Posten angefasst: den Durchgang auf
veraltete Zeitangaben in der Entwurfsdatei.**

### 🟥 133 geltende Entwürfe enthalten relative Zeitangaben

**Gesucht wurde nach** `yesterday`, `last night`, `this morning`,
`this afternoon`, `this evening`, `tonight`, `tomorrow`, Wochentagen
(`on Thursday`, `last Friday` …), `this week`, `last week`, `next week`,
`a few days ago`, `the other day`. **Bereits als ersetzt markierte Fassungen
wurden ausgenommen** — gezählt sind nur Entwürfe, die nach heutigem Stand
gelten würden.

**Befund: 133.**

**Warum das zählt:** jeder dieser Texte wurde an dem Tag geschrieben, an dem
die Angabe stimmte, und **keiner ist je versendet worden.** Wird einer davon
heute abgeschickt, **enthält er eine falsche Aussage über den Vorgang der
Kundin oder des Kunden** — und zwar gegenüber genau den Menschen, denen schon
mehrfach etwas Unzutreffendes geschrieben wurde.

**Die vollständige Liste steht in `docs/entwuerfe-mit-relativen-datumsangaben.md`**,
mit der jeweils gefundenen Formulierung pro Entwurf.

**Bewusst NICHT getan: die 133 Entwürfe automatisch umgeschrieben.** Ein
Skript, das `this morning` durch ein Datum ersetzt, müsste raten, welcher Tag
gemeint war — und bei mehreren Nachrichten am selben Tag rät es falsch.
**Die Liste ist eine Prüfliste zum Abarbeiten, keine Reparatur.** In der
Datei steht ausdrücklich: **lieber den Satz streichen als ein Datum einsetzen,
das vielleicht nicht stimmt.**

### Stand nach diesem Lauf

- **Entwürfe in der Datei: 428** (unverändert — in diesem Lauf wurde kein
  Entwurf geschrieben und keiner geändert).
- **Offen aus der Entwurfsdatei-Prüfung:** **87 Kunden mit reiner Warnzeile**
  und **die Abarbeitung der 133 Datumsangaben.**
- **Keine Erstattung ausgelöst, nichts versendet.**

---

## Lauf 04:20 UTC — nichts Neues im Posteingang · Mehrfachfassungen inventarisiert

**Posteingang geprüft.** `newer_than:2h` lieferte drei Threads, deren jüngste
Nachrichten aber alle vom **29.09.** sind — **das ist die bekannte Eigenart,
dass `newer_than:` THREADS trifft und nicht Nachrichten.** Alle drei sind
bearbeitet: `mrpbeaver@gmail.com` (#8312, Entwurf vom 29.09. abends),
`yvettemears@yahoo.co.uk` (#8307) und `mrodonnell66@gmail.com` (#7982, beide
im Abendreport vom 29.09.). **Nichts ist neuer als die #7831 von
30.09. 23:36.**

### Inventar der ungeklärten Mehrfachfassungen

**Gezählt: 98 Kundinnen und Kunden haben mehrere Entwürfe in der Datei.**
**Bei 84 davon ist mehr als eine Fassung NICHT als ersetzt markiert — zusammen
203 Fassungen.**

**Die vollständige Liste steht jetzt in
`docs/entwuerfe-mehrfachfassungen.md`**, sortiert nach Anzahl der ungeklärten
Fassungen, mit allen Überschriften je Kunde und einer Anleitung, wie ein Fall
abzuarbeiten ist.

**🟥 Warum das nicht automatisch geht, steht dort ausdrücklich drin:** **die
jüngste Fassung ist nicht automatisch die vollständigste.** Bei **#7608**
deckte genau die jüngste Fassung die Sicherheitsmeldung aus dem ersten Thread
nicht ab. Wer dort blind die neueste genommen hätte, hätte eine seit achtzehn
Tagen unbeantwortete Sicherheitsmeldung ein weiteres Mal übergangen.
**Deshalb wird hier nichts pauschal markiert.**

**Bisher abgearbeitet (11):** #7479, #7048, #7347, #8142, #8372, #7547, #6254,
#5973, #7831, #8295, #7608.

### Stand nach diesem Lauf

- **Entwürfe in der Datei: 428** (unverändert).
- **Offen:** **84 Kunden mit ungeklärten Mehrfachfassungen** und **133
  Entwürfe mit relativen Zeitangaben** — beide jetzt als eigene Prüflisten im
  Repository, nicht mehr nur als Satz im Protokoll.
- **Keine Erstattung ausgelöst, nichts versendet.**

---

## Lauf 05:20 UTC — nichts Neues im Posteingang · #7041 abgearbeitet

**Posteingang geprüft.** Dieselben drei Threads wie um 04:20, alle mit
jüngster Nachricht vom **29.09.** und alle bearbeitet. **Nichts ist neuer als
#7831 von 30.09. 23:36.**

**Aus der Prüfliste `docs/entwuerfe-mehrfachfassungen.md` den nächsten Fall
abgearbeitet.**

### 🟥 #7041 — Tim Fitton (`fitton@fitton.karoo.co.uk`), GB — **Bot/Escalated – Owner Attention**

**Drei Threads, zwei Absenderadressen, vier Entwurfsfassungen. Alle vier sind
jetzt als ersetzt markiert; es gibt genau einen geltenden Entwurf.**

| Datum | Was passiert ist |
|---|---|
| 21.08. 19:30 | Bestellung #7041 |
| **02.09. 10:45** | Versand — **zwölf Tage** |
| 15.09. | Nach seiner Angabe erhalten |
| 16.09. 19:39 | Erstkontakt von `fitton@fitton.karoo.co.uk` |
| 17.09. 21:15 | Nachfass, gleiche Adresse |
| **21.09. 05:49** | Von `fittontim@gmail.com`: *„I am still awaiting **a full refund** on this as both items were of poor quality and **not as described**"* |
| 21.09. 09:24 | **Vorlage 1**, „Dear Tim" |
| 22.09. 10:20 | *„That is really disappointing they are of such poor quality and a complete waste of money!"* |
| 24.09. 12:18 | **Vorlage 2**, „Dear Customer" |
| 24.09. 12:30 | **Vorlage 3**, „Dear Customer" |
| seither | nichts |

**🟦 Der entscheidende Befund:** **die Artikel auf #7041 sind
`Paw-Friends™-Fluffys`.** **Der eigene Fluffys-Produkttext trägt die Zeile
„30-day money-back guarantee" — ohne jede Bedingung.** Alle drei
Absagebriefe stützten sich auf eine Bedingung („returned unused"), **die in
keinem der zwölf Produkttexte steht.** Das ist dasselbe Muster wie bei #7479
und #7347.

**Zweiter Befund:** **seine ausdrückliche Erstattungsforderung vom 21.09.
wurde nie als solche beantwortet** — drei Vorlagen zum Kauschaden, kein Wort
zur Forderung. **Heute sind das zehn Tage.**

**Shopify-Befund:** `#7041` — bestellt **21.08.**, versandt **02.09.**
(**zwölf Tage**), **£29,95**, zwei Fluffys zum Bündelpreis,
`totalRefundedSet` = **£0.00**, `refunds` leer, `cancelledAt: null`.
**E-Mail auf der Bestellung: `fitton@fitton.karoo.co.uk`.**

**🟥 Adressregel angewandt:** er schreibt auch von `fittontim@gmail.com`.
**Der Entwurf geht an die Adresse auf der Bestellung**, und der Grund wird ihm
offen genannt — **ohne seine Identität in Zweifel zu ziehen.** Es werden
keine Bestelldaten an die Zweitadresse gegeben.

**Weiter im Entwurf ausdrücklich NICHT:** keine vierte Kauschaden-Vorlage;
keine Erstattung zugesagt, kein Termin, keine Absage; **nicht entschieden, ob
die bedingungslose Fluffys-Garantie auf seinen Fall anwendbar ist**; nicht
behauptet, die von ihm erinnerte Beschreibung existiere nicht; **nicht
unterstellt, der zweite Artikel sei benutzt — und auch nicht, er sei
ungeöffnet**; vor dem Porto gewarnt; nichts aus seinem Hund gefolgert.

**Keine Erstattung ausgelöst, nichts versendet.**

### Stand nach diesem Lauf

- **Entwürfe in der Datei: 429.**
- **Mehrfachfassungen abgearbeitet: 12** (neu: #7041). **Offen: 83.**
- **Entwürfe mit relativen Zeitangaben: weiterhin 133 offen.**

---

## Lauf 06:20 UTC — nichts Neues im Posteingang · #7989 abgearbeitet

**Posteingang geprüft: nichts neuer als #7831 von 30.09. 23:36.**

**Nächster Fall aus `docs/entwuerfe-mehrfachfassungen.md`.**

### 🟥 #7989 — Karen Reynolds (`House54@outlook.com.au`), AU — **Bot/Escalated – Owner Attention**

**Zwei Threads, vier Entwurfsfassungen. Alle vier sind jetzt als ersetzt
markiert; es gibt genau einen geltenden Entwurf.**

| Datum | Was passiert ist |
|---|---|
| 28.08. 00:43 | Bestellung #7989 |
| 28.08. 00:47 | *„Can I please confirm my order is for 1x Hippo and 1x Frog."* |
| **29.08. 18:04** | **Schriftliche Bestätigung: *„I can confirm that your order request is for: 1 × Hippo, 1 × Frog. We'll make sure your requested selection is noted for your order."*** |
| **08.09. 07:31** | Versand — **elf Tage** |
| 17.09. | *„Half my order just arrived. I only got the Hippo where is the frog as I payed for both."* |
| 18.09. | **Zweiter Thread** `Missing Item.`: dieselbe Meldung |
| 19.09. | Antwort: man bedaure, der Frosch fehle, man kümmere sich |
| **21.09. 09:28** | **Kauschaden-Vorlage** auf eine Fehlmengenmeldung: *„sorry to hear that the toy was damaged after your dog used it"* |
| 21.09. 10:47 | *„NO NO NO NO I only got half my order… **Nothing is damaged**… Read my email."* |
| 23.09. | *„Can we please sort out this situation."* |
| **24.09. 12:24** | **Zusage: *„they will arrange to send the missing Frog toy to you."*** |
| seither | **nichts** |

**🟥 Der Shopify-Befund stellt den ganzen Vorgang auf den Kopf:**

`#7989` hat **genau eine Position: Menge 2, `variantTitle: "hippo"`.**
**Es steht überhaupt kein Frosch auf der Bestellung.**

**Das heißt:**

1. **Die schriftliche Bestätigung vom 29.08. wurde nie auf die Bestellung
   übernommen.** Ihr wurde zugesagt, ihre Auswahl werde vermerkt. Sie wurde
   es nicht.
2. **Die Zusage vom 24.09., den fehlenden Frosch zu schicken, ist vom
   Datensatz nicht gedeckt** — es gibt keine Froschposition zum Nachsenden
   und nichts Offenes (`unfulfilledQuantity: 0`, `fulfillmentOrders.status:
   CLOSED`). **Der Entwurf wiederholt diese Zusage deshalb NICHT.** Eine
   zweite Zusage derselben Art wäre eine zweite ungedeckte Zusage.
3. **Sie sagt, ein Artikel kam an. Der Datensatz sagt, Menge 2 wurde am
   08.09. in einer Sendung versandt.** **Ihr wird NICHT gesagt, sie habe sich
   verzählt.** Beide Angaben stehen im Entwurf nebeneinander und gehen so an
   den Owner.

**Weitere Daten:** bestellt **28.08.**, versandt **08.09.** (elf Tage),
**A$53,87**, `totalRefundedSet` = **$0.00**, `refunds` leer,
`cancelledAt: null`.

**Im Entwurf ausdrücklich NICHT:** keine Wiederholung der Frosch-Zusage;
keine Erstattung, kein Ersatz, keine Nachsendung zugesagt; kein Termin; keine
Absage; **keine Aussage zur Größe der Verpackung und kein Vergleich mit
Produktbildern**, obwohl sie das angesprochen hat; Fotos nicht geöffnet;
Betrag in AUD, nicht umgerechnet; der AU-Policy-Abschnitt nur benannt, nicht
ausgelegt.

**Anmerkung zur Quellenlage:** der Thread `Re: Order #7989 confirmed` meldet
`messageCount: 6`, ausgeliefert wurden **fünf** Nachrichten. **Die sechste
konnte ich nicht einsehen.** Der Entwurf stützt sich nur auf das, was
tatsächlich gelesen wurde.

**Keine Erstattung ausgelöst, nichts versendet.**

### Stand nach diesem Lauf

- **Entwürfe in der Datei: 430.**
- **Mehrfachfassungen abgearbeitet: 13.** **Offen: 82.**
- **🔴 Für die Owner-Liste:** **#7989 ist eine weitere Zusage, die der
  Datensatz nicht deckt** — neben #5973 (zweimal „processed", £0,00
  erstattet). **Das sind jetzt zwei Fälle, in denen schriftlich etwas
  bestätigt wurde, das nie geschehen ist.**
