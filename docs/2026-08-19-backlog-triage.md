# Backlog triage — 2026-08-19

Suchlauf und Shopify-Abfrage sind durchgegangen, der Connector ist danach
erneut abgebrochen. **Keine Entwürfe angelegt, keine Labels gesetzt, kein Text
rekonstruiert.**

---

## ⏱ Zeitkritisch — Adresse vor Versand korrigieren

**#6095 — Cristina LaMont — 46,26 £ — noch UNFULFILLED**

- Bestellt 14.08. 16:25, Adressmeldung 18.08. 22:37
- Shopify zeigt: `150 Glacier Dr, Apt 238, Mineral, Washington 98355`
- Kundin nennt als richtig: `1215 195th St, Long Beach, WA 98631`
- Das sind **zwei völlig verschiedene Orte**, nicht nur eine Hausnummer — geht
  das Paket an die hinterlegte Adresse, ist es weg.
- Status `PAID`, keine Fulfillments. Änderung ist noch möglich.

*Adressabweichung beachten:* Die Bestellung läuft auf `cristina.lamont@gmail.com`,
die Mail kam von `cristinalamont@gmail.com` — **ohne Punkt**. Vor der Änderung
kurz abgleichen. (Bei Gmail sind beide Schreibweisen dasselbe Postfach, aber
Shopify behandelt sie als verschiedene Kunden.)

→ **Adresse ändern, bevor die Fulfillment-Automatik zugreift.** Gleiche
Konstellation wie #5896 und #4926, die beide noch offen sind.

## Zwei Kunden warten seit über einer Woche auf eine Antwort

| Kunde | Bestellung | Erstkontakt | Jetzt |
|---|---|---|---|
| Lisa McManus | #4125 | 11.08. | 19.08.: „I haven't received any response from you. I would like a refund please." |
| Rick Macunovich | — | 10.08. | 19.08.: „I sent an email on 8/10/26 [...] Please respond!" |

Beides sind inhaltlich Kauschäden, also nach Regel **keine** Erstattung. Aber
beide sind jetzt Eskalationen — nicht wegen des Falls, sondern wegen der
Funkstille. Für McManus lag seit dem 13.08. ein fertiger Entwurf im Postfach
(`Bot/Draft Ready`), der nie abgesendet wurde. Genau dieses Muster hat schon
Sharon Alberio, Dave Reid und Paul Steadman erzeugt.

→ **Ein unversendeter Entwurf ist keine Antwort.** Solange Entwürfe liegen
bleiben, produziert der Bot Eskalationen statt sie zu verhindern.

## Ellen Rosey (#4071) meldet sich erneut

Am 13.08. bereits eskaliert (zitierte „no dog has ever destroyed your furry
animals"). Jetzt neue Bestellung/neuer Schaden am Frosch, mit Angebot, Fotos zu
schicken: „Would you like photos of your indestructible toy?" **Dritter
Kontakt**, der Entwurf vom 13.08. ist nie rausgegangen.

## Weitere neue Fälle (unbearbeitet)

- **Werbeaussage bestritten:** tazistic #4444 („You advised these at
  indestructible for tough chewers", Foto beiliegend), tridds („your 'strong'
  dog toys"), grandpappyty („Less than 30 seconds")
- **Lieferstatus:** skinzie471 #3568 (**seit 27.07.**, „this was to be mail in
  3 to 5 days"), cstyle2008 #4740, boblister65 #5513 (Tracking hängt auf
  „Waiting for details")

`#3568` ist der älteste offene Lieferfall im Postfach — über drei Wochen.

---

## Nicht getan

- Keine Entwürfe, keine Labels — Connector-Ausfall.
- Keine Erstattung, kein Storno, keine Adressänderung in Shopify ausgeführt.
- Keine Rücksendeadresse erfunden.

## Unverändert offen

Erstattungsliste 310,96 £, die Sicherheitswarnung vom 14.08., die
Kreditkartennummer im Thread #4284 und der Trading-Standards-Fall Jason Branch.
Siehe die Logs vom 13., 14. und 18.08.
