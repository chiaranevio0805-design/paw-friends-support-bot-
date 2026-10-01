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
