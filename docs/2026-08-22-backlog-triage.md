# Backlog-Triage 2026-08-22

Nachgetragen. Der Connector war über weite Teile des 22.–24.08. instabil
(Gmail und Shopify fielen wiederholt mitten im Lauf aus, der Worker-Prozess
wurde mehrfach neu gestartet). Was hier steht, ist aus Gmail und Shopify
verifiziert, nicht rekonstruiert.

## Befund: das Postfach redet Stornierungen aus

Am 22.08. sind aus `support.pawfriends.uk@gmail.com` zwei Antworten
rausgegangen, die **nicht** aus einem Bot-Lauf stammen:

- **08:54 UTC an todd.jacobsw@gmail.com** (#6870): „Dear Todd, … Before we
  proceed with the cancellation, may we ask what is the reason you would like
  to cancel your order? If you decide to keep the order…"
- **09:01 UTC an usfmom02@gmail.com** (#6905): derselbe Text, „Dear Wendy…"

Die Policy ist an dieser Stelle eindeutig (support-policy.md, Regel 3):
*„cancel and refund the full amount, **no argument, no attempt to talk them
out of it**."* Beide Mails tun genau das Gegenteil — sie fragen nach einem
Grund und bieten ein Halten-Angebot an, bevor storniert wird.

Ergebnis bei Wendy Higgins, **10:56 UTC**:

> „I simply changed my mind and no longer want the order. Please go ahead and
> cancel it as I previously requested."

Das ist ihr zweiter Kontakt in derselben Sache — erzeugt allein durch die
Rückfrage. Todd Jacobs hat auf die Rückfrage bisher gar nicht geantwortet;
#6870 steht seit dem 20.08. unbearbeitet.

Beide Bestellungen waren zu diesem Zeitpunkt noch **UNFULFILLED**, also noch
stornierbar. Das Zeitfenster ist der eigentliche Punkt: die
Fulfilment-Automatik zieht die Aufträge weiter, und wenn sie erst raus sind,
ist es der Fall #4617 (erstattet *und* versandt, £51,27 weg) noch einmal.

## Fälle

| Fall | Kunde | Klassifikation | Kategorie |
|---|---|---|---|
| #6870 | Mary Jacobs (Anfrage über todd.jacobsw@gmail.com) | Regel 3, vor Versand storniert | `Bot/Needs Approval` |
| #6905 | Wendy Higgins (usfmom02@gmail.com) | Regel 3, vor Versand storniert, zweiter Kontakt | `Bot/Needs Approval` |
| #3310 | Timothy Carroll (tcarroll@cadvanced.com) | Chargeback + bestrittene Werbeaussage | `Bot/Escalated - Owner Attention` |

Shopify-Stand, nachgeprüft 23.08. 06:17 UTC:

- **#6870** — £45,95 — PAID / **UNFULFILLED** — angelegt 20.08. 21:15 UTC
- **#6905** — £28,52 — PAID / **UNFULFILLED** — angelegt 21.08. 01:49 UTC
- **#3310** — £35,64 — PAID / PARTIALLY_FULFILLED — versandt 29.07.

## Was der Owner tun muss

1. **#6870 stornieren und erstatten** — £45,95, volle Summe. Erst stornieren,
   dann erstatten.
2. **#6905 stornieren und erstatten** — £28,52, volle Summe. Ebenso.
3. **#3310** — Entscheidung zum Chargeback. Kein Bot-Thema: der Kunde hat den
   Streitfall bereits bei seinem Kreditkartenanbieter eröffnet, und aus dem
   Postfach sind ihm dazu schon zwei Vorlagen-Absagen geschickt worden.
   Kauschaden — **fällt nicht unter die Erstattungsregel** und gehört nicht
   auf die Erstattungsliste.
4. **Die Rückfrage-Vorlage bei Stornierungen abschalten.** Sie widerspricht
   Regel 3 direkt und hat in beiden Fällen des 22.08. nur Verzögerung und
   einen Zweitkontakt erzeugt.

## Entwürfe

Zum Zeitpunkt dieses Eintrags **noch nicht angelegt** — die Gmail-Tools waren
in jedem Lauf-Versuch abgebrochen, bevor `create_draft` durchging. Für den
Abend-Report gilt damit ausdrücklich: **Volltext nicht im Log — vor dem
Senden in Gmail-Entwürfen prüfen.** Kein Text wird hier rekonstruiert.
