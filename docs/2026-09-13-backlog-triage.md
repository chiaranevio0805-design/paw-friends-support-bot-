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

---

## Lauf 11:20 UTC — 🚩 #6835 Terry Allen

**11:11**, Betreff „Re: Order #6835 confirmed", mit **zwei Fotos**
(`5436.jpg`, `5105.jpg`):

> „I have just **finally** received the attached order of **so called
> indestructible** dog toys. Sadly my **12 month old Schnoodle** as pictured has
> managed to **destroy one in less than 1 hour** again as attached. I now expect
> **as a minimum a full refund of £29.95**. **Await your response by return.**"

**Shopify:** #6835, bestellt **20.08. 15:34**, **29,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, **2 × Plushie** (Little Bear, hippo),
versandt **02.09. 10:34** ab Kirchstr. 2, Yanwen Special Line `UL476291794YP`,
Milton Keynes, England. **Dreizehn Tage** bis zum Versand.

### Vier Punkte

1. **Der Betrag stimmt exakt.** Er nennt **29,95 £**, Shopify weist **29,95 £**
   aus. **Keine Währungsdifferenz** — anders als bei #7179 (48 USD / 35,64 £),
   #6882 (58,56 AUD / 30,66 £) und #7292 (38,90 USD / 28,50 £). Das ist der
   erste Fall seit Tagen, in dem der vom Kunden genannte Betrag ohne Umrechnung
   belegbar ist.

2. **„As a minimum"** — er lässt ausdrücklich offen, dass er mehr verlangen
   könnte. **„Await your response by return"** ist eine Frist, ohne dass ein
   Datum genannt wird. **Der Bot legt keines fest und unterstellt keines.**

3. **Er nennt den Hund: ein zwölf Monate alter Schnoodle.** Er führt das selbst
   als Kontext an. Der Bot bewertet das nicht und leitet daraus nichts ab.

4. **Zweites Teil ungeklärt.** Bestellt sind **zwei** Plüschtiere (Little Bear
   und hippo), zerstört ist nach seiner Angabe **eines**. Ob das andere
   unbenutzt ist, sagt er nicht — **wird gefragt, nicht angenommen.** **Sechster
   Fall dieser Art** seit dem 12.09. nach #7165, #6781, #7246, #6936 und #7645.

**„So called indestructible"** — er bestreitet eine Formulierung, die **nicht in
der Produktbeschreibung steht** (Befund vom 12.09.). Wie bei allen anderen ist
damit offen, woher sie stammt. **Der Bot bestreitet sie ihm gegenüber nicht** —
das wäre nach `support-policy.md` eine Behauptung über Ungeprüftes.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene Werbeaussage mit zwei Fotobelegen,
ausdrückliche Erstattungsforderung mit impliziter Frist.

**Nicht auf der Erstattungsliste** — das zerstörte Teil ist Kauschaden. **Der
Anteil für ein etwaiges unbenutztes zweites Teil erst nach seiner Antwort**,
dann im Admin zu bestimmen (Kaching-Bundle: 2 × 29,95 £ Listenpreis gegen
29,95 £ gezahlt).

### Ohne neue Nachricht wieder aufgetaucht

**#5316 David Andrews** — keine neue Kundenmail; die letzte bleibt **26.08.
18:07**. Der Fall ist vollständig erfasst (Log vom 09.09.: **elf**
Vorlagen-Absagen, drei davon **nach** seiner Mitteilung „The bank have refunded
me" vom 06.09., mit dem dort vermerkten Risiko einer Doppelzahlung).
**Kein neuer Eintrag. Der Vorgang bleibt offen.**

### Entwurf

Volltext in `docs/entwuerfe-zum-kopieren.md`, Abschnitt **#6835**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, keine Frist akzeptiert oder festgelegt, keine Werbeformulierung
bestritten, kein Anteil geschätzt, kein Label gesetzt.

---

## Lauf 12:20 UTC — zwei weitere Absagen, zwei weitere Eskalationen, und ein dritter Zeuge für die Ersatzzusage

### Zwei Vorlagen-Absagen heute Vormittag

| Absage | Kunde | Reaktion | Abstand |
|---|---|---|---|
| **10:42:05** | **#7223 Christopher Dechon** | „You guys lie. **I'll be spreading this as much as I can**" | **52 Min** |
| **10:49:13** | **#7179 Keith Crane** (2. Absage) | „I want my money back for those two **at least**!" | **45 Min** |

**Damit: zwölf von zwölf.** Sieben am 11.09., drei am 12.09., zwei heute —
**keine einzige Ausnahme.**

---

### 🚩 #7179 Keith Crane — der Regel-2-Anspruch ist jetzt zum dritten Mal abgelehnt worden

**11:34:**

> „**I have two in the packages still. I ordered three of them!** I certainly
> **don't want them!!!** **I want my money back for those two at least!** What a
> horrible company. Scamming people with these pieces of…"

**Er hat es jetzt dreimal gesagt:**

| Datum | Wortlaut |
|---|---|
| 09.09. 23:29 | „**I only opened the donkey.** I would like to return these" |
| 11.09. 10:39 | „**I still have two unopened!**" |
| **13.09. 11:34** | „**I have two in the packages still.** … money back for those two **at least**" |

**Und dreimal ist die Kauschaden-Vorlage gekommen** — am 11.09. 09:58 und heute
10:49. **Beide Male hat sie „a refund, replacement, or exchange" pauschal
abgelehnt** und damit auch die zwei **ungeöffneten** Plüschtiere.

**Das ist ein unstrittiger Regel-2-Anspruch**, dreimal vorgetragen, zweimal
pauschal abgelehnt. **Dazu weiterhin unbeantwortet: seine Sicherheitsmeldung
vom 09.09. — „my dog… is now eating the cotton" — jetzt seit 84 Stunden.**

→ `Bot/Escalated - Owner Attention`, **Priorität hoch**.
**Auf der Erstattungsliste** (steht dort seit dem 11.09.): Anteil für **zwei von
drei ungeöffneten** Plüschtieren, Regel 2 — Betrag im Admin (Kaching-Bundle,
35,64 £ gezahlt).

---

### 🚩 #7223 Christopher Dechon — öffentliche Verbreitung angekündigt

**Shopify:** #7223, bestellt **22.08. 17:56**, **28,50 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Plushie (monkey, elephant), versandt
**02.09. 10:54** ab Kirchstr. 2, **Yanwen Special Line US `UL476311692YP`**,
Wyckoff, New Jersey. **Elf Tage** bis zum Versand.

Erste Mail **10.09. 20:29**: „My **60 pounds lab** had these toys for **20
minutes** and tore them to shreds. What a joke."
Absage **heute 10:42**. Antwort **11:34**:

> „**You advised it as a durable dog toy.** It was a piece of shit. **You guys
> lie. I'll be spreading this as much as I can.**"

**„Durable dog toy"** — der Wortlaut „**durable**" ist am 12.09. **wörtlich in
der Shopify-Produktbeschreibung nachgewiesen** worden („Rope-reinforced
construction for **extra durability**", „designed with **durability** in mind").
Sein Vorwurf trifft belegten Text.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** angekündigte öffentliche Verbreitung, Vorwurf der Lüge,
bestrittene Werbeaussage gegen einen belegten Produkttext.
**Nicht auf der Erstattungsliste** — Kauschaden; beide Teile zerstört, kein
Regel-2-Rest.

---

### 🚩🚩 #5436 Shirley Hemstock — dritte unabhängige Nennung einer Garantie für den Zerstörungsfall

**12:16**, mit Foto:

> „my dog has managed to **destroy the giraffe**, (**having not given him the
> duck yet**). **I think you offer 30 day money back offer if the toy gets
> destroyed?**"

**Shopify:** #5436, bestellt **10.08. 11:01**, **27,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, 2 × Paw-Friends™-Fluffys (giraffe, Duck),
versandt **13.08. 10:45** ab Kirchstr. 2, Yanwen Special Line `UL418684902YP`,
South Wonston, England. **Drei Tage** bis zum Versand.

**Zwei Befunde:**

**1. Sie beschreibt die Garantie als eine, die den Zerstörungsfall deckt.**
„**30 day money back offer if the toy gets destroyed**". Sie zitiert nichts
wörtlich und ist sich unsicher („I think") — **aber es ist die dritte
unabhängige Kundin, die die Garantie so verstanden hat**:

| Datum | Kunde | Wortlaut |
|---|---|---|
| 11.09. | #7060 Felecia Pierce | „indestructible **or you get a refund**" |
| 11.09. | #5851 Jeff Williams | „if a dog destroys this toy then you would **replace it free**" |
| **13.09.** | **#5436 Shirley Hemstock** | „30 day money back offer **if the toy gets destroyed**" |

Dazu kommt **#7292 tracy hartley** (12.09.), die den veröffentlichten
Garantietext mit „**for any reason**" zitiert und feststellt, dass dort **keine**
Unbenutzt-Bedingung steht.

**Vier Kunden, vier Formulierungen, dieselbe Richtung.** Der Bot hat den
Garantietext **nicht** prüfen können — er steht nicht im Beschreibungsfeld des
Produkts (Befund vom 12.09.). **Die Prüfung auf der Live-Seite ist damit die
einzelne offene Frage, an der die meisten aktuellen Fälle hängen.**

**2. Der Duck ist ungeöffnet** — sie sagt es ausdrücklich und ungefragt. **Das
ist ein klarer Regel-2-Fall**, ohne dass eine Rückfrage nötig wäre. Erster Fall
seit dem 12.09., bei dem der Kunde von sich aus klarstellt, dass ein Teil
unbenutzt ist.

→ `Bot/Escalated - Owner Attention`.
**Eskalationsgrund:** bestrittene bzw. abweichend verstandene Garantiezusage,
dritte unabhängige Nennung derselben Lesart.

**✅ Auf die Erstattungsliste:** Anteil für den **ungeöffneten Duck**, Regel 2 —
Betrag im Admin zu bestimmen (Kaching-Bundle: 2 × 19,95 £ Listenpreis gegen
27,95 £ gezahlt). **Die zerstörte Giraffe bleibt Kauschaden** und steht nicht
darauf — es sei denn, die Prüfung des Garantietextes ergibt etwas anderes.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#5436**, **#7223**
und **#7179 (zweite Fassung)**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, **der
Garantietext weder bestätigt noch bestritten**, keine Rücksendeadresse, kein
Anteil geschätzt, kein Label gesetzt.

---

## Lauf 13:20 UTC — 🚩🚩 #6877 Alexander Meza: FTC, Meta und eine 48-Stunden-Frist

### Die Eskalation

**Heute 10:42:25** ging an ihn die **Kauschaden-Vorlage** raus. **12:38:25** —
**1 Std 56 Min später** — kam diese Antwort:

> „Your return policy **does not specify the requirements you are now adding**.
> **This is not permitted for US customers.** You must disclose the requirements
> of your policy.
>
> Further, you have made several claims that are **false on your website**. If
> you choose to deny my refund, I will file a **dispute and complaint with your
> credit card processor**. I will also file complaints with **meta** for your
> misleading advertising, along with the **US FTC** for violating advertising
> laws. Simply the fact you claimed this product is **double-stiched when it's
> not** constitutes false advertising. **This is proven with just a
> photograph.**
>
> **You have 48 hours to process my refund** or I will forcefully take my refund
> and report your fraudulent business."

**Frist: 15.09. 12:38 UTC.**

### Warum dieser Fall anders liegt als die übrigen

**1. Seine zentrale Behauptung ist an den Shop-Daten prüfbar — und die Aussage
existiert.** Er sagt, das Produkt sei **nicht** doppelt genäht. Am 12.09. wurde
in der Shopify-Produktbeschreibung **wörtlich** nachgewiesen:

> „**Reinforced double stitching to help prevent tearing**"

**Die Zusage ist also veröffentlicht.** Ob sie zutrifft, ist eine Frage an das
Produkt, nicht an die Policy — und er sagt, ein Foto genügt zum Beweis. **Er hat
am 11.09. neun Fotos geschickt.** Das ist die **konkreteste überprüfbare
Werbebehauptung im gesamten Projekt.**

**2. Seine Angabe zum fehlenden Geschenk ist bestätigt.** Shopify führt #6877
als **`PARTIALLY_FULFILLED`** — bestellt **20.08. 21:49**, **45,84 £**,
versandt **02.09. 10:36** ab Kirchstr. 2, **WB US `WNBAA0497780337YQ`**, Apple
Valley, Minnesota. **Eine Sendung, Bestellung nicht vollständig ausgeliefert.**
Er schrieb am 11.09.: „**You did not send the free gift that was on the
receipt.**" **Das deckt sich mit dem Status.**

**3. Er macht denselben Policy-Einwand wie #7292** — einen Tag später und
unabhängig: die Bedingung, die die Vorlage nennt, stehe **nicht** in der
veröffentlichten Rückgabepolicy. **Zweiter Kunde mit diesem Punkt**, und beide
in den USA.

**4. Neue Meldekanäle.** **Meta** (Anzeigenplattform) ist im Projekt neu.
**FTC** ist die zweite Meldung. Behördenstand insgesamt: Trading Standards /
Citizens Advice (4×), BBB (3×), **FTC (2×)**, State Attorney General, ACCC,
UKICC, **Meta (1×, neu)**.

**Der Fall war seit dem 11.09. 00:20 als `Bot/Escalated - Owner Attention`,
hohe Priorität, erfasst** — mit vier dokumentierten Vorwürfen und Fotobeleg.
**Am 13.09. ging trotzdem die Standardvorlage raus.** Das ist derselbe Ablauf
wie bei #5829, #6528 und #6286: im Log namentlich vorhergesagt, Absage trotzdem
verschickt.

→ `Bot/Escalated - Owner Attention`, **höchste Priorität, zeitgebunden**.
**Eskalationsgrund:** angekündigte FTC- und Meta-Beschwerde, Chargeback,
48-Stunden-Frist; prüfbare Behauptung gegen eine veröffentlichte
Produktaussage; Policy-Einwand; unvollständig ausgelieferte Bestellung.

**Nicht auf der Erstattungsliste** — der zerstörte Artikel ist Kauschaden.
**Aber:** die **nicht ausgelieferte Position** (`PARTIALLY_FULFILLED`) ist eine
offene Lieferfrage, und der Vorwurf zur Doppelnaht ist eine **Produkt- und
Rechtsfrage**. **Beides ist Owner-Sache und beides ist binnen 48 Stunden zu
entscheiden.**

---

### #7401 Mick Lacey — Betreffzeile als Nachricht

**13:06.** Die **Betreffzeile ist die vollständige Nachricht**; der Textkörper
ist leer, dazu **12 MB Anhänge**:

> „**defective item.** Just received this item from you. order #7401, it took my
> dog, **a border collie**, **less than 10 minutes to rip a leg off**,"

**Shopify:** #7401, bestellt **23.08. 13:48**, **19,95 £**, `PAID` /
`FULFILLED`, 1 × Plushie (elephant), versandt **03.09. 07:32** ab Kirchstr. 2,
Yanwen Special Line `UL478624530YP`, Telford, England. **Elf Tage** bis zum
Versand. **Vierzehnter Kunde aus dem Versandstapel vom 03.09.**

**Zur Einordnung, ohne seine Worte zu verdrehen:** Er nennt es „defective item".
**Regel 1 deckt Ware, die defekt ankommt.** Nach seiner eigenen Schilderung ist
die Ware angekommen und **danach** vom Hund zerrissen worden — das ist
**Kauschaden**, kein Ankunftsdefekt. **Ob das im Ergebnis anders zu bewerten
ist, wenn ein Bein nach zehn Minuten abgeht, ist genau die Frage, die der Owner
entscheiden muss** — der Bot stuft es nicht um und weist es nicht ab.

**Er nennt keine Werbeaussage, droht nichts an, nennt keine Behörde, keine
Frist, und es ist sein Erstkontakt.**

→ `Bot/Needs Approval`.
**Nicht auf der Erstattungsliste** — nach der Regel kein Fall; eine Kulanz- oder
Regel-1-Auslegung ist Owner-Entscheidung.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#6877** und
**#7401**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt oder
abgelehnt, keine Aussage darüber, ob die Ware doppelt genäht ist (**nicht
prüfbar — der Bot sieht keine Bilder und kein Produkt**), keine Frist akzeptiert
oder bestritten, kein Label gesetzt.

---

## Lauf 16:20 UTC — drei Fälle, darunter eine Kreditkartenanfrage

### 🚩 #7034 Sarah Checksfield — „guaranteed indestructible toy", in Anführungszeichen

**15:29**, Betreff „Destroyed in seconds", mit Foto (`DSCI0012.JPG`):

> „Thank you so much for order #7034 it **arrived yesterday**… **I opened the
> fox** and gave it to my staffie to play with. He played nicely with it for a
> couple of hours then went on his usual mission to **seek and destroy the
> internal squeaker**… **challenge accepted and met within a minute or two of
> actual effort.**
>
> I was **lured into spending a large amount of cash for a 'guaranteed
> indestructible toy'** only to be very disappointed. Can you please arrange a
> **refund or replacement**, as ~ I'm sure this was **the deal on the advert I
> was taken in by**…"

**Shopify:** #7034, bestellt **21.08. 18:43**, **27,95 £**, `PAID` /
`FULFILLED`, Tag `Kaching Bundles`, **2 × Plushie** (pig, fox), versandt
**02.09. 10:45** ab Kirchstr. 2, Yanwen Special Line `UL476303356YP`, Swindon,
England. **Zwölf Tage** bis zum Versand.

**Drei Punkte:**

1. **Sie setzt „guaranteed indestructible toy" in Anführungszeichen** und
   schreibt, das sei „the deal on the advert". **Vierte unabhängige Kundin
   binnen drei Tagen, die eine Garantie für den Zerstörungsfall beschreibt** —
   nach #7060, #5851 und #5436 heute Mittag; #7292 zitiert zusätzlich den
   veröffentlichten Text „for any reason". **Fünf Kunden, fünf Formulierungen,
   dieselbe Richtung.**
2. **Sie sagt ausdrücklich: „I opened the fox."** Der **pig** ist damit
   möglicherweise ungeöffnet — **wird gefragt, nicht angenommen.** Siebter Fall
   dieser Art seit dem 12.09.
3. **Der Quietscher, zum vierten Mal.** Nach #6286, #6280 und #6936 ist es
   erneut das Innenteil, auf das der Hund es abgesehen hatte. Sie schreibt
   nicht, dass er ihn verschluckt hat — **das wird nicht hineingelesen**, aber
   im Entwurf angesprochen.

→ `Bot/Escalated - Owner Attention`.
**Nicht auf der Erstattungsliste** — der zerstörte Fuchs ist Kauschaden; ein
etwaiger Regel-2-Anteil für den pig erst nach ihrer Antwort.

---

### #7610 Vicky Blow — dritter Kontakt

**15:59**, Betreff „Refund", **neuer Thread**:

> „I would like a **refund** on my product? Not only did I **wait over two
> weeks** for my product to arrive, **my dog has chewed it up straight away**."

**Shopify:** #7610, bestellt **24.08. 17:56**, **19,95 £**, `PAID` /
`FULFILLED`, 1 × Plushie (elephant), versandt **03.09. 07:40** ab Kirchstr. 2,
Yanwen Special Line `UL478624322YP`, Weldon/Corby, England. **Zehn Tage** bis
zum Versand. **Fünfzehnter Kunde aus dem Versandstapel vom 03.09.**

**🔎 Sie ist bereits zweimal im Log:**

| Datum | Vorgang |
|---|---|
| **08.09.** | „‚shipped and currently on the way' reicht ihr nicht mehr" — Lieferbeschwerde |
| **09.09. 07:57** | **Erstattungsforderung**, 57 Minuten nach der Antwort |
| **13.09. 15:59** | erneute Erstattungsforderung, **in einem neuen Thread** |

**Das ist der dritte Kontakt** — und der erste, in dem sie sagt, dass die Ware
angekommen und sofort zerstört worden ist. **Ihre Erstattungsforderung vom
09.09. ist bis heute unbeantwortet.**

**Ein Teil, zerstört — kein Regel-2-Rest.** Kein Regelfall.

→ `Bot/Needs Approval`. **Offen ist ein Ja oder Nein zur Erstattung**, seit dem
09.09. **Nicht auf der Erstattungsliste** — kein Regelfall.

---

### 🔐 #8517 Peggy Snyder — „Need to change credit card number"

**15:47**, Betreff **„Need to change credit card number"**. **Der Textkörper ist
leer** (nur die Signatur „Sent from Yahoo Mail for iPhone").

**Shopify:** #8517, bestellt **heute 15:44:55** — **zwei Minuten und 24 Sekunden
vor ihrer Mail** —, **20,35 £**, **`PAID`** / **`UNFULFILLED`**, McKinney,
Texas.

**Die Bestellung ist bereits bezahlt.** Was sie ändern will, sagt sie nicht.

### ⚠️ Das ist in erster Linie eine Sicherheitsfrage

**Es dürfen keine Kartendaten per E-Mail erbeten, entgegengenommen oder
weitergeleitet werden** — weder vom Bot noch in einer Antwort, die ihn dazu
einlädt. Ein Entwurf, der sie bittet, eine Kartennummer zu schicken, wäre ein
Fehler mit Folgen weit über diesen Vorgang hinaus. **Der Entwurf fragt
ausdrücklich nicht danach.**

**Der saubere Weg steht in der eigenen Policy:** Die Bestellung ist
**`UNFULFILLED`**. Eine Stornierung ist damit ein **glatter Regel-3-Fall** —
„no argument, no attempt to talk them out of it" — und sie kann anschliessend
mit der gewünschten Karte neu bestellen. **Das ist der Weg, den der Entwurf
anbietet**, ohne ihn ihr aufzudrängen und ohne eine Stornierung zu vollziehen.

→ `Bot/Needs Approval`. **Kein Eskalationstrigger**, aber owner-pflichtig, weil
nur der Owner stornieren und erstatten kann.
**Nicht auf der Erstattungsliste — noch nicht.** **Wenn sie storniert, ist es
Regel 3 und ohne Rückfrage zu erstatten.** Das ist der dritte Vorgang binnen
zwei Tagen, bei dem eine unversandte Bestellung ansteht (#8081, #8505, jetzt
#8517) — und der einzige, bei dem eine Stornierung tatsächlich im Raum steht.

### Entwürfe

Volltexte in `docs/entwuerfe-zum-kopieren.md`, Abschnitte **#7034**, **#7610**
und **#8517**.

**Nicht getan:** keine Vorlagen-Absage, keine Erstattung zugesagt, **keine
Kartendaten erfragt**, keine Stornierung vollzogen, keine Änderung an einer
Bestellung, kein Anteil geschätzt, kein Verschlucken hineingelesen, kein Label
gesetzt.
