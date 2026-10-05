# Paw Friends — Backlog-Triage, Montag 5. Oktober 2026

**Vorgängertag:** `docs/2026-10-04-backlog-triage.md`.
**Der Befund, der alles überlagert:** `docs/produktseiten-live-befund.md`.

---

## 🟥 Dieser Tag beginnt ohne Zugang zum Support-Postfach

**Seit dem 04.10. 19:20 UTC hängt die Gmail-Verbindung am privaten Postfach des
Owners (`chiaranevio0805@gmail.com`), nicht an
`support.pawfriends.uk@gmail.com`.** **Die Gegenprobe ist seit fünf Läufen
leer.**

**Solange das so ist, gilt:**

- **Es wird nichts gelesen, nichts bearbeitet, nichts eskaliert, nichts
  gesendet.**
- **Das private Postfach wird NICHT triagiert** — der Auftrag lautet auf das
  Support-Postfach, und ein anderes ist davon nicht gedeckt, auch wenn es
  demselben Menschen gehört.
- **Pro Lauf wird hier eine Zeile geführt**, damit später niemand annimmt, das
  Postfach sei in diesen Stunden betreut worden.

### Stundenprotokoll

| Lauf (UTC) | Gegenprobe `to:support.pawfriends.uk@gmail.com` | Ergebnis |
|---|---|---|
| **00:20** | `newer_than:5d` | **leer** — sechster Lauf ohne Zugang |
| **01:20** | `newer_than:5d` | **leer** — siebter Lauf ohne Zugang |
| **02:20** | `newer_than:6d` | **🟨 NICHT leer, aber auch kein Zugang** — ein Thread, siehe unten |
| **03:20** | `in:inbox is:unread newer_than:6h` | **nur privates Postfach** — neunter Lauf ohne Zugang |
| **04:20** | `in:inbox is:unread newer_than:7h` | **nur privates Postfach, unverändert** — zehnter Lauf ohne Zugang |
| **05:20** | `in:inbox is:unread newer_than:8h` | **nur privates Postfach, unverändert** — elfter Lauf ohne Zugang |
| **06:20** | `in:inbox is:unread newer_than:9h` | **nur privates Postfach, unverändert** — zwölfter Lauf ohne Zugang |

---

## Was offen in diesen Tag hineinreicht

### 🟥 Fünf Fälle vom 04.10. früh, alle ohne Entwurf

**Sie wurden um 10:17 UTC über die alte Verbindung erfasst und sind
dokumentiert; ohne Postfachzugang können sie nicht weiterbearbeitet werden.**

| Fall | Stand |
|---|---|
| **`richard@brownwolf.net`** | 30 → 50 → 60 → **70 %** angeboten, **alle abgelehnt**; **Ware ungeöffnet**; beruft sich auf „no-quibble"; **hat nach der Geschäftsadresse gefragt**. 15 Nachrichten. |
| **#7347 Jill Hibbs** | bittet seit **24.09.** um die Rücksendedetails, bekam 50 %, dann **60 %**; 04.10.: *„I just want a full refund once I have returned it!"* |
| **`laceymick31@gmail.com`** | **🟥 *„you sent him a new toy free of charge"*** (30.09.) — erster konkreter Hinweis auf einen geleisteten Gratis-Ersatz; zitiert UK-Verbraucherrecht |
| **#7982 `mrodonnell66@gmail.com`** | stand schon im Übertrag vom 29.09.; hat am 04.10. die **Eingangsvorlage** bekommen; beruft sich auf „indestructible" und Verbraucherrecht |
| **Nigel Bennett** | zweiter Kontakt, 04.10. 08:54: Füllung heraus, *„Please advise."* **Keine Sicherheitsmeldung erhoben — es wird ihm keine unterstellt.** |

### 🟥 Vier Briefe gingen am 04.10. zwischen 07:55 und 08:03 aus dem Postfach

**Zwei Prozentangebote (70 % und 60 %) und zwei Kauschaden-Vorlagen.**
**Dieses Postfach sendet also — nur nicht durch mich.** **Solange parallel
gesendet wird, sind meine Entwürfe nicht die Antwort des Hauses, sondern eine
zweite Stimme daneben.**

### Die Zahlen, Stand 04.10. 23:20

| | |
|---|---|
| **Entwürfe in `entwuerfe-zum-kopieren.md`** | **483** · ersetzt **121** · **geltend 362** |
| davon ⛔ Werbebefund-Sperre | **83** |
| davon sonstige Sendesperre | **5** (#6936, #7179, #6528, zwei #7316) |
| **Bestätigte „processed"-Briefe** | **13** · ungeprüfte Kandidaten **30** |
| **Offene Sicherheitsmeldungen** | **5** |
| **Belegte Doppelbriefe** | **4** |
| **Offene Nichtlieferungsfälle** | **6** |
| **Von mir gesendete E-Mails, gesamt** | **0** |

### Was der Owner zuerst braucht

1. **Die Gmail-Verbindung zurück auf `support.pawfriends.uk@gmail.com`** — und
   prüfen, ob der Wechsel beabsichtigt war. **Wenn nicht, ist das ein
   Zugriffsvorfall**; die Passkey-Warnung vom 26.09. ist weiter ungeprüft.
2. **Das parallele Senden stoppen oder mir sagen, wer es macht.**
3. **#8764 Craig Wren — die von ihm gesetzte Frist läuft seit 02.10.**
4. **Shopify neu anmelden** — fünfter Tag. **Nicht `switch-shop` aufrufen.**
5. **Entscheiden: 14 oder 30 Tage, und ob „unbenutzt" eine Bedingung ist.**
6. **Rücksendeadresse nennen oder ohne Rücksendung erstatten.**
7. **Die 13 „processed"-Zusagen plus #6583 und #2894 zahlen oder zurücknehmen.**
8. **Die fünf Sicherheitsmeldungen beantworten.**

---

## Lauf 02:20 UTC — die Gegenprobe ist diesmal nicht leer, und das ist ein Befund für sich

**Achter Lauf ohne Zugang zum Support-Postfach — aber die Abfrage
`to:support.pawfriends.uk@gmail.com newer_than:6d` hat erstmals EINEN Treffer.**
**Ich stelle genau fest, warum, damit das nicht als „Zugang wiederhergestellt"
missverstanden wird:**

- **Der Thread liegt im privaten Postfach** (`chiaranevio0805@gmail.com` als
  Empfänger) — **er ist nur deshalb gefunden worden, weil das Support-Postfach
  bei einer der beiden Nachrichten als MIT-Empfänger eingetragen ist.**
- **Die Verbindung hängt also unverändert am privaten Postfach.** **Der
  Zugang zum Support-Postfach ist nicht wiederhergestellt.**
- **Ich habe den Thread NICHT geöffnet.** Die Abfrage lief mit
  `THREAD_VIEW_METADATA_ONLY` — **kein Betreff, kein Textauszug, kein
  Inhalt.**

### 🟥 Was die Metadaten allein schon zeigen, und es gehört dem Owner

**Absenderin: `trafford.pam@gmail.com`. Zwei Nachrichten, 09.09. und 29.09.**
**Bei der ersten vom 09.09. ist als zweiter Empfänger
`carddisputes@co-operativebank.co.uk` eingetragen.**

**Das ist eine Kartenreklamation bei ihrer Bank, und das Support-Postfach ist
bei der zweiten Nachricht mitadressiert.** **Pam Trafford ist nicht neu: sie
stand am 01.10. schon einmal in einer ausgehenden Nachricht dieses Postfachs.**

**Mehr sage ich dazu nicht, weil ich den Inhalt nicht gelesen habe und auch
nicht lesen werde, solange die Verbindung am privaten Postfach hängt.**
**Der Owner sollte diesen Thread selbst ansehen** — eine Kartenreklamation mit
der Bank im Adressfeld ist die Art Vorgang, die keine Woche warten darf.

**Nichts gelesen, nichts bearbeitet, nichts gesendet, kein Entwurf, keine
Erstattung. Das private Postfach wurde nicht triagiert.**
