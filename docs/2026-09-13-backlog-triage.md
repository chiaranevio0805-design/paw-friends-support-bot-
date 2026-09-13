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
