# Backlog-Triage 2026-09-13

Stündliche Läufe gegen `support.pawfriends.uk@gmail.com` nach
`docs/runbook.md`. Erstattungen nur bei bestätigtem Regel-4-Fall (falscher
Artikel) — sonst Entwurf und Label. **`create_draft` bricht seit dem 21.08. bei
jedem Versuch ab** (zuletzt gestern, Versuch 21), deshalb stehen die
Entwurfstexte in `docs/entwuerfe-zum-kopieren.md` statt im Postfach.

## ⏰ Fristen, die heute laufen

- **#7190 Steve Solley** — seine eigene 48-Stunden-Frist endet **heute 19:32**.
  Die von ihm berechnete Lieferfrist ist am 12.09. abgelaufen. Entwurf liegt
  vor; die Erstattungsentscheidung ist Owner-Sache und **heute fällig**.
- **#7699 Lorraine Sale** — ihre selbstgesetzte Frist läuft am **17.09.** ab.
- **#7292 tracy hartley** — höchste Priorität aus dem gestrigen 22:20-Lauf: der
  veröffentlichte Garantietext ist auf der Live-Seite zu prüfen, und ihre
  Verschluckungsmeldung vom 10.09. ist weiterhin unbeantwortet.

---

## Lauf 02:20 UTC — 🚩 #7645 Betty Brown

**02:02**, Betreff „Toy", vollständiger Text:

> „Received toy **today**. **Ma dog took the ear off in 10 minutes.** This toy is
> **not for heavy chewers**. **False advertisement and comments from customers.**
> Very unhappy with your product."

**Shopify:** #7645, bestellt **24.08. 20:43**, **43,92 £**, `PAID` /
`FULFILLED`, Tags `Kaching Bundles`, `UpCart Rewards`, **drei Positionen**
(Zahnbuddy „Blue Mop Plush Dog", Plushie hippo, Plushie donkey), versandt
**04.09. 04:33** ab Kirchstr. 2, **D&S Express `JDW101400617914`**, Oakland,
Kalifornien. **Elf Tage** bis zum Versand.

### Drei Punkte

**1. Sie bestreitet nicht nur die Werbung, sondern auch die Bewertungen.**
„False advertisement **and comments from customers**" — sie hält beides für
unzutreffend. **Dritte Kundin, die die Bewertungen in Zweifel zieht**, nach
**#5973 Stephen Cooil** (09.09., „I can't believe these are genuine") und
**#4745 Steph Hanlon** (gestern, „your reviews speak for themselves").

Das steht neben dem Befund vom 11.09. zu **#6606**: der shopeigene
Bewertungspool des Hauptprodukts zeigt **78 Bewertungen, Durchschnitt 5,0,
keine einzige negative**, und zehn namentliche Haltbarkeits-Testimonials tragen
Zeitstempel **aus zehn Minuten** am 01.06.2026. **Der Bot hat keine externe
Bewertungsseite aufgerufen und behauptet über deren Inhalt nichts.**

**2. „This toy is not for heavy chewers."** Das ist die Gegenaussage zu
„**Anti-tear design built for strong chewers**" — einer Formulierung, die
gestern **wörtlich in der Shopify-Produktbeschreibung nachgewiesen** wurde.
Ihr Vorwurf trifft damit einen belegten Text, nicht eine Erinnerung.

**3. 🔎 Ein Zusteller, der bisher nicht vorkam:** **D&S Express**
(`JDW101400617914`). Bisher dokumentiert: Yanwen Special Line (+ Promotion,
+ US, + Registered Airmail), 4PX (Economic/Standard/US), JQ Express US, Yun
Express (+ US), WB US, RD Express, SunSu Packet. **D&S Express ist der zehnte
Zusteller.** Ob das relevant ist, ist offen — festgehalten wird nur, dass er
neu ist.

**Drittes Teil ungeklärt:** Sie schreibt „**toy**" im Singular, bestellt sind
**drei** Positionen. Ob die beiden übrigen unbenutzt sind, sagt sie nicht —
**wird gefragt, nicht angenommen.** Fünfter Fall dieser Art seit gestern nach
#7165, #6781, #7246 und #6936.

**Sie fordert nichts.** Kein Geld, kein Ersatz, keine Rücksendung. **Sechster
Fall ohne jede Forderung** seit gestern.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage gegen einen belegten
Produkttext, zusätzlich bestrittene Kundenbewertungen.

**Nicht auf der Erstattungsliste** — Kauschaden, keine Forderung. Ein etwaiger
Regel-2-Anteil für die beiden anderen Positionen **erst nach ihrer Antwort**,
dann im Admin zu bestimmen (Kaching-Bundle).

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#7645**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, keine
externe Bewertungsseite aufgerufen, keine Aussage über deren Inhalt, kein
Anteil geschätzt, kein Label gesetzt.

---

## Lauf 08:20 UTC — #8505 John Marsh: eine Adresskorrektur, elf Minuten nach der Bestellung

**07:23**, Betreff „Re: Order #8505 confirmed":

> „The **house number is missing** from the shipping address but is on the
> billing address. Shipping is to **6 Ermine Close, Ancaster, Grantham, Lincs,
> NG32 3RD**. Thanks for your help."

**Shopify:** #8505, bestellt **heute 07:12:42**, **19,95 £**, `PAID` /
**`UNFULFILLED`**, 1 × Plushie (fox).

**Die hinterlegte Lieferanschrift bestätigt ihn:**

```
address1: "Ermine Close, Ancaster, Grantham NG32 3RD, UK"
address2: "Ancaster"
city:     "Grantham"
zip:      "NG32 3RD"
```

**Es steht keine Hausnummer darin.** Seine Angabe — **6 Ermine Close** — ist die
fehlende Information.

### Warum das ein guter Fall ist, wenn er heute erledigt wird

- **Er hat elf Minuten nach der Bestellung geschrieben**, aus eigenem Antrieb,
  bevor irgendetwas schiefgehen konnte.
- **Die Bestellung ist `UNFULFILLED`.** Die Korrektur ist vor dem Versand
  möglich — und Septemberbestellungen gehen inzwischen in **ein bis drei Tagen**
  raus (#8359 ein Tag, #8344 zwei, #8343 drei). **Das Zeitfenster ist klein.**
- Wird die Adresse korrigiert, wird aus diesem Vorgang **nie eine Beschwerde**.

**Der Gegenfall steht im Log:** **#8081 Matthew Pierce** — dort ist eine
vollständige, korrekte Anschrift **vierzehn Tage lang** als unzureichend
behandelt worden, mit einer Nachforderung, die es bei APO-Adressen nicht gibt.
**Hier ist die Anschrift tatsächlich unvollständig, und der Kunde liefert die
Korrektur selbst.**

### Was der Bot nicht tut

**Die Adresse wird nicht geändert.** Nach `runbook.md` ist der einzige
zulässige schreibende Shopify-Vorgang die Erstattung bei einem bestätigten
Regel-4-Fall; alles andere ist Entwurf und Label. Eine Änderung an der
Bestellung eines Kunden fällt nicht darunter. **Die Korrektur gehört in den
Admin, durch den Owner — vor dem Versand.**

→ `Bot/Needs Approval`.
**Kein Eskalationstrigger:** keine Forderung, keine Werbeaussage, keine Frist,
keine Behörde, Erstkontakt, freundlicher Ton.
**Nicht auf der Erstattungsliste** — nichts zu erstatten.

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#8505**.

**Nicht getan:** keine Adressänderung in Shopify, keine Bestätigung, dass die
Adresse geändert wurde, kein Versanddatum, kein Zustelltermin, kein Label
gesetzt.

---

## Lauf 09:20 UTC — #7119 und #8009

### 🚩 #7119 Susan McGee — Chargeback angekündigt, weil die Sendungsnummer fehlt

**08:33**, Betreff „ORDER #7119":

> „I have **not received these items** & **I have not got a tracking number**.
> Please supply this **or I will have to have this payment reversed by the
> bank**."

**Shopify:** #7119, bestellt **22.08. 04:43**, **28,50 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (pig, fox), versandt
**02.09. 10:49** ab Kirchstr. 2, **Yanwen Registered Airmail `VR959018244YP`**,
Blackstone Heights, Tasmanien. **Elf Tage** bis zum Versand.

**Die Sendungsnummer existiert seit dem 02.09. — seit elf Tagen — und sie hat
sie nicht.**

**Das ist der sechste Fall dieser Art in drei Tagen:**

| Kunde | Nummer vorhanden seit | Ausgang |
|---|---|---|
| #7525 Carol Garvey | 03.09. | nicht genannt, sie bedankt sich trotzdem |
| #7547 Luke Prior | 03.09. | nicht genannt, will stornieren |
| **#7190 Steve Solley** | 02.09. | nicht genannt, **48-Stunden-Frist läuft heute ab** |
| #4726 Marilyn Penniall | 22.08. | nicht genannt, dritter Kontakt |
| #7627 Charlotte Matthews | 03.09. | nicht genannt, „won't purchase again" |
| **#7119 Susan McGee** | 02.09. | nicht genannt, **Chargeback angekündigt** |

**Dieser Fall ist der einfachste von allen sechs und der einzige, der sich mit
einer einzigen Zeile auflösen lässt:** sie verlangt ausdrücklich nur die
Nummer und knüpft die Rückbuchung daran, sie **nicht** zu bekommen.
`VR959018244YP` liegt vor.

**Derselbe Ablauf hat bei #7771 Barb Fitzgerald zu einer tatsächlichen
Chargeback-Frist geführt** — dort ist die Nummer bis heute nicht genannt worden.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** angekündigte Rückbuchung über die Bank.
**Nicht auf der Erstattungsliste** — kein Regelfall, Ware unterwegs.

---

### #8009 Yvonne Ware — der Termin ist vorbei

**09:16**, Betreff „#8009", vollständiger Text:

> „Can I please have my money back, as **the date I wanted the order has now
> been and gone**!"

**Shopify:** #8009, bestellt **28.08. 09:26**, **27,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (frog, Little Bear), versandt
**08.09. 07:32** ab Kirchstr. 2, Yanwen Special Line `UL493229620YP`, Hull,
England. **Elf Tage** bis zum Versand.

**Sie nennt keinen Termin und sagt nicht, ob sie ihn dem Shop mitgeteilt hat.**
**Das wird nicht angenommen und nicht rekonstruiert.** Aus den Daten geht
hervor: bestellt am 28.08., versandt am 08.09., bis heute nicht angekommen —
**sechzehn Tage nach der Bestellung**.

**Kein Regelfall.** Regel 3 deckt Stornierungen **vor** Versand; hier wurde am
08.09. versandt. Eine Erstattung wegen eines verpassten Anlasses ist
**Owner-Entscheidung**.

→ `Bot/Needs Approval`. Sagbar: Versanddatum, Zusteller, Nummer, Trackinglink,
und offen, dass elf Tage bis zum Versand vergingen. **Nicht sagbar:** ein
Zustelltermin, die 7–21-Tage-Formel, und **keine Rückfrage nach dem Anlass** —
sie muss ihren Grund nicht belegen.

**Nicht auf der Erstattungsliste** — kein Regelfall.

---

### Nebenbefund zur Versanddauer

**#8009 wurde am 28.08. bestellt und am 08.09. versandt — elf Tage.** Das
bestätigt die Einordnung vom 12.09.: die schnellen Versandzeiten (ein bis drei
Tage) betreffen **Septemberbestellungen**; Augustbestellungen liegen weiterhin
bei neun bis siebzehn Tagen, unabhängig davon, wann sie tatsächlich rausgingen.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#7119** und
**#8009**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, keine
Zustellprognose, keine 7–21-Tage-Formel, kein Verweis an den Zusteller, kein
Anlass erfragt oder unterstellt, kein Label gesetzt.

---

## Lauf 10:20 UTC — 🚩🚩 #2894 Jeff Hughes: eine Ersatzlieferung, zugesagt am 24. Juli

**09:28**, vollständiger Text:

> „Hi, **Can you arrange for this to be sorted out ASAP please.** Jeff"

**Shopify:** #2894, bestellt **11.07.2026 14:02**, **19,95 £**, `PAID` /
`FULFILLED`, 1 × Plushie (fox), versandt **14.07. 07:50** ab Kirchstr. 2,
**SunSu Packet `SYGB022179102`**, Northwich, England.
**In Shopify existiert nur diese eine Sendung. Eine Ersatzlieferung ist nie
angelegt worden.**

### Der Vorgang, aus den eigenen Logs

| Datum | Was im Log steht |
|---|---|
| **23.07.** | Ware **mit einem Riss angekommen**, Foto beigefügt. Log: „now genuinely defective on arrival". **Ersatz (elephant oder fox) wird bestätigt**, Rücksendung ausdrücklich nicht verlangt. `Bot/Needs Approval` |
| **24.07.** | **Ersatz zugesagt** — „I'll be back in touch shortly to confirm" |
| **29.07.** | Erste Nachfrage. Log: „no shipped update yet" |
| **31.07.** | Zweite Nachfrage |
| **05.08.** | Dritte Nachfrage. **Hochgestuft auf `Bot/Escalated - Owner Attention`**, Log: „replacement promised 24 July, **still not dispatched nearly two weeks later**" |
| 06.08. | Antwort aus dem Postfach |
| **13.08.** | „**If you were the customer, how long would you reasonably accept this scenario to go on?**" — im Postfach mit `Label_7` versehen |
| **27.08.** | „Ok, so where are we up to with this now? It's taking a while." |
| **13.09.** | „Can you arrange for this to be sorted out ASAP please." |

### Was das heisst

**Die Ersatzlieferung ist seit dem 24. Juli zugesagt. Heute sind das
einundfünfzig Tage.** In Shopify ist sie **nie angelegt worden**.

**Das ist die dritte offene Ersatzzusage** — und die mit Abstand älteste:

| Fall | zugesagt | offen seit |
|---|---|---|
| **#2894 Jeff Hughes** | **24.07.** | **51 Tage** |
| #4317 Charles Rivera | 19.08. | 25 Tage |
| Gary Sanderson | 19.08. | 25 Tage |

**Er hat mindestens sechsmal nachgefasst** — 29.07., 31.07., 05.08., 13.08.,
27.08., heute — **und ist in jeder einzelnen Mail höflich geblieben.** Seine
Frage vom 13.08. steht seit einem Monat unbeantwortet im Postfach:

> „If you were the customer, **how long would you reasonably accept this
> scenario to go on?**"

**Der Fall war am 05.08. bereits eskaliert** und trägt seit dem 13.08. das
Escalated-Label. Er ist seither nicht gelöst worden.

→ `Bot/Escalated - Owner Attention`, **hohe Priorität wegen der Dauer**.
**Eskalationsgrund:** seit 51 Tagen zugesagte, nie ausgeführte Ersatzlieferung;
mindestens sechster unbeantworteter Nachfassversuch; bereits am 05.08.
eskaliert und seither unverändert.

**✅ Auf der Erstattungsliste — und zwar als Regelfall.**
**#2894 — 19,95 £ — Jeff Hughes — defekt angekommen (Riss bei Ankunft, Foto vom
23.07.).** Das ist **Regel 1**. Der Anspruch besteht unabhängig davon, dass
stattdessen ein Ersatz zugesagt wurde; wird der Ersatz nicht geschickt, ist der
Kaufpreis zu erstatten. **Bisher stand dieser Fall nicht auf der Liste** — er
gehört dorthin.

---

### Ohne neue Nachricht wieder aufgetaucht

**Kimberley Shenton (`kim.shenton@me.com`)** — keine neue Kundenmail; die letzte
bleibt **20.08. 06:26** („I would appreciate a response and a resolve on this
matter asap please").

**Der Vorgang ist trotzdem offen und gehört benannt:** Sie hat am **15.08.** um
Rückgabe gebeten („due to the quality"), am **16.08.** begründet — „**It is not
as advertised or pictured**" — und am **20.08.** nachgefasst. Die Antwort vom
**21.08.** fragte nach der **Bestellnummer**, die zuvor schon einmal erfragt
worden war. **Seither ist nichts passiert.**

**In Shopify ist zu dieser Adresse keine Bestellung über die E-Mail-Suche
auffindbar.** Nach dem Befund vom 12.09. (googlemail/gmail) wäre die
**Namenssuche** der nächste Schritt — sie ist hier **möglich**, weil der Name
bekannt ist: **Shenton**. Das gehört im Admin geprüft, bevor sie ein drittes Mal
nach ihrer Bestellnummer gefragt wird.

→ Kein neuer Eintrag, kein neues Label. **Vermerkt, weil der Vorgang seit 24
Tagen stillsteht und die Rückfrage nach der Bestellnummer vermeidbar ist.**

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#2894**.

**Nicht getan:** keine Ersatzzusage wiederholt, keine Erstattung zugesagt, kein
Liefertermin, keine Bestellnummer für Kimberley Shenton geraten, kein Label
gesetzt.
