# Backlog triage — 2026-08-14

## ⚠️ Zuerst: Sicherheitswarnung für das Support-Postfach

Um **07:20 UTC am 14.08.** sind zwei Google-Sicherheitswarnungen für
`support.pawfriends.uk@gmail.com` eingegangen, zwei Sekunden auseinander:

1. „Die E-Mail-Adresse zur Kontowiederherstellung wurde geändert"
2. „Die Telefonnummer zur Kontowiederherstellung wurde geändert"

Beide Wiederherstellungswege desselben Kontos wurden im selben Moment
geändert. Das ist genau das Muster einer Kontoübernahme: Wer beide
Wiederherstellungswege austauscht, sperrt den rechtmäßigen Inhaber aus.

**Kein Kundenvorgang — nicht beantworten.** Wenn der Owner diese Änderungen
nicht selbst vorgenommen hat, ist das der dringendste Punkt im ganzen Postfach,
vor jeder Erstattung:

- Passwort ändern
- Unter `myaccount.google.com/security` alle fremden Sitzungen abmelden
- Wiederherstellungs-E-Mail und -Telefonnummer zurücksetzen
- Prüfen, ob Weiterleitungen oder Filter eingerichtet wurden (typischer
  nächster Schritt nach einer Übernahme — eingehende Kundenmails werden
  unbemerkt umgeleitet)

Label: `Bot/No Action` (kein Kundenfall), aber im Report ganz oben.

## Neu im Posteingang seit dem 13.08.

Rund 30 neue Threads. Verteilung:

- **Werbeaussage bestritten** (Eskalation nach Policy): nikki.1988,
  breebear3593 #3480, michael@ravencanyon, stevencoombs1973 #4107,
  daniel1983nolan, nicola-cummings #3668, k.fox3090 #3990, g.simper #4241
  (zwei Mails), barra1985 #4118, marchedges #4368, adamsellens
- **Kauschaden ohne Werbebezug**: randykerr62 (zwei Mails), hallett4725,
  bevross99 #3708
- **Lieferstatus**: katrinarumgay, karnut74 #3892, bonsonpv #4686 (drei
  Mails), brian.litchfield74, ibstock #3318 (Evri schickt das Paket zurück)
- **Kontosicherheit**: die zwei Google-Warnungen oben

Diese Fälle sind in diesem Lauf **nicht** einzeln beantwortet worden. Der
Posteingang wächst mit rund 25–30 Mails pro Tag; die Ursache dafür ist in der
Datei vom 13.08. dokumentiert und liegt in der Werbung, nicht im Support.

## Nicht getan

- Keine Erstattung und kein Storno in Shopify ausgeführt — der Connector
  blockiert beides (`category: "financial"`).
- Keine Mail versendet.
- Keine Rücksendeadresse erfunden.

---

# Lauf 2 (spät abends, ~21:0x UTC)

26 weitere Threads seit dem Vormittagslauf. **Der Gmail-Connector ist während
dieses Laufs mehrfach ausgefallen** — Entwürfe konnten nicht angelegt werden.
Die Shopify-Prüfung lief durch, deshalb hier die Befunde, damit sie nicht
verloren gehen.

## ⏱ Zeitkritisch — heute Abend noch zu retten

**#6126 — Alex Marris — 29,95 £ — Storno vor Versand**

- Bestellt **14.08. 20:32 UTC**, Storno-Mail **20:38 UTC** — sechs Minuten später
- Shopify: `PAID`, `UNFULFILLED`, keine Fulfillments
- Artikel: Frosch + Affe, Versand nach Scunthorpe DN17 4LZ
- **Achtung, Adressabweichung:** Die Bestellung läuft auf `amarris@aol.com`,
  die Storno-Mail kam von `alexmarris82@gmail.com`. Vor der Erstattung kurz
  abgleichen.

→ **Stornieren + 29,95 £ voll erstatten, bevor die Fulfillment-Automatik
zugreift.** Genau in dieser Konstellation sind #4617, #3944, #4212 und #5474
schiefgegangen: Der Kunde storniert rechtzeitig, es passiert nichts, die
Bestellung geht am Folgetag raus. Storno **und** Erstattung, in dieser
Reihenfolge — Erstatten allein stoppt den Versand nicht.

Entwurf konnte wegen des Connector-Ausfalls nicht angelegt werden. Kein Text
aus dem Gedächtnis rekonstruiert.

## Wiederholte Kontakte (Eskalationstrigger, noch unbeantwortet)

| Kunde | Bestellung | Trigger |
|---|---|---|
| G. Zalarick | #3959 | **Zweite Mail**, ausdrücklich „not indestructible as advertised"; erste Mail vom 11.08. blieb liegen |
| Frankie Grant | — | **Zweite Mail**, bittet um „the courtesy of a reply"; erste Mail vom 10.08. blieb vier Tage liegen |
| Becky (bloomphoto) | — | Betreff „**Second inquiry**", beruft sich auf die Geldzurück-Garantie |
| Paul Russell | #4459 | Zitiert „as it says indestructible"; Adressfall vom 06.08. ist derselbe Kunde |

Alle vier gehören nach Policy in `Bot/Escalated - Owner Attention`. Sie sind
in diesem Lauf **nicht** beantwortet worden.

## Weitere neue Fälle (unbearbeitet)

- **Werbeaussage bestritten:** kirsty_waugh („robust toy with a 30 day money
  back guarantee"), e_harvey8, yog97, jessicastokes80, am.smitheram,
  lauracmcintyre #4461 („not fit for purpose")
- **Lieferstatus:** angel #4957 (zweite Anfrage), davbutterworth #4916
- **Sonstiges:** n.simpson727 fragt nach dem versprochenen Gratis-E-Book, das
  sie nie erhalten hat — eigener Fehlertyp, bisher nicht in der Policy erfasst

## Hinweis zum Ablauf

Der Posteingang wächst seit dem 12.08. um 25–30 Mails pro Tag. Bearbeitet
werden pro Lauf deutlich weniger. Die Ursache ist in der Datei vom 13.08.
dokumentiert und liegt in der Werbung, nicht im Support — solange die Anzeige
mit den Absolutaussagen läuft, ist der Rückstand nicht einholbar.
