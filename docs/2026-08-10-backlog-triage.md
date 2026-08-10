# Backlog triage — 2026-08-10

Erster Lauf nach drei Tagen Pause. 26 Threads im Posteingang. Viele der
Entwürfe vom 07.08. wurden am 09.08. abends gesendet — dadurch sind
zahlreiche Kundenantworten eingegangen.

## Der eigentliche Befund: die Werbeaussage

**15 von 20 Kundenanliegen in diesem Lauf drehen sich um dieselbe Sache.**
Nicht um Kauschäden an sich — sondern darum, dass die Spielzeuge als
unzerstörbar beworben wurden.

Ich habe den Produkttext im Shop geprüft. Er sagt **nicht** „indestructible".
Er ist sogar vorsichtig formuliert:

> „Rope-reinforced construction", „Reinforced double stitching to help
> prevent tearing", „Anti-tear design built for strong chewers",
> „built to last"

Kunden zitieren aber wörtlich Formulierungen, die dort **nicht stehen**:

- David Kiff (#3715): „our plushies are made for dogs that destroy
  everything. 40000 owners. Not one dog got through"
- idontplayfrisby: „40000 dogs aren't as amazing as my Ella!"
- Lindsey Lake (#3590): „Your advert says … products are indestructible"
- Lisa Good (#3689): „your whole website advertise indestructible toys"
- tongaym: will die Facebook-Anzeige suchen, um sie zu bewerten

Die Zahl „40.000" und das Wort „indestructible" stammen also aus einer
anderen Quelle als der Produktseite — mit hoher Wahrscheinlichkeit aus den
Meta-/Facebook-Anzeigen. Ein Abgleich über die Ad Library war mir mangels
Berechtigung nicht möglich (`ads_library_search` gab einen Permission-Fehler
zurück).

**Das ist der Hebel.** Solange diese Anzeige läuft, erzeugt sie weiter
Beschwerden, die im Support nicht lösbar sind — der Widerspruch entsteht
vor dem Kauf, nicht danach.

## Neu eskaliert

| Kunde | Order | Auslöser |
|---|---|---|
| Lindsey Lake | #3590 | **Trading Standards ausdrücklich angedroht** + bestrittene Werbeaussage, zweiter Kontakt |
| David Kiff | #3715 | Zitiert Werbeaussage wörtlich, nennt es „false advertising", zweiter Kontakt |
| idontplayfrisby (Ella) | — | Zitiert „40000 dogs", beruft sich auf die 30-Tage-Garantie |
| Lisa Good | #3689 | Bestreitet Werbung der gesamten Website, verweist auf Bewertungen, zweiter Kontakt |
| tongaym | — | Zweiter Kontakt, kündigt öffentliche Facebook-Bewertung an |
| Sandra Sant | #1476 | Fordert jetzt ausdrücklich volle Erstattung **£62,85**, nennt Kommunikation „disgusting" |
| Michael Green | #3486 | Ware nach langer Wartezeit angekommen und in 3 Std. zerstört |
| cmgrive | #3536 | Höflich, will keine Erstattung — kritisiert aber ausdrücklich den Produkttitel |

## Draft Ready

| Kunde | Order | Fall |
|---|---|---|
| Beverley Ross | #3708 | Kauschaden nach 5 Min., Erstkontakt |
| Ryan Smith | — | Kauschaden, nennt die Werbung als Kaufgrund |
| ed33351 | #3271 | Kauschaden nach 10 Min. |
| meatmaster618 | #3172 | Zwei Spielzeuge in 2 Std. |
| d_edmunds27 | #3351 | Zweiter Kontakt, resigniert |
| Sara Reeves | #4421 | Lieferfrage, versandt 5. Aug., Tracking mitgeteilt |

## Needs Approval

| Kunde | Order | Fall |
|---|---|---|
| Jak Richardson | #4978 | **£34,95, seit 7. Aug. bezahlt und UNVERSANDT.** Kein Tracking, weil nichts versandt wurde |
| Deborah Savage | #4756 | Bedankt sich für die zugesagte Erstattung **£51,27** — ist die ausgeführt? |
| Nicholas Kloepfer | #4604 | Wartet auf Tracking. **Adresse immer noch nicht geändert** |

## No Action

Nicholas Dibbs (#3637, Dank), Holly Priest (Humor, will keine Erstattung),
j0hnmav0n8 (Agentur-Werbung).

## Zweiter Befund: Versand-Rückstand

Bei der Suche nach Jak Richardsons Bestellung fiel auf, dass praktisch alle
Bestellungen vom 7.–9. August auf **UNFULFILLED** stehen — #5333, #5287,
#5234, #5202, #5182, #5082, #5011, #4978, #4946, #4882 und weitere. Von 60
Treffern in der Stichprobe war keine einzige versandt.

Das erklärt die Lieferanfragen und wird in den nächsten Tagen mehr davon
erzeugen. Getrennt vom Werbethema, aber ähnlich strukturell.

## Korrektur während des Laufs

Im ersten Entwurf an Jak Richardson stand, es gebe keine Bestellung unter
seiner Adresse. Das war ungeprüft und **falsch** — #4978 existiert. Der
Entwurf wurde korrigiert, bevor er in den Report ging. Auslöser war die
Log-Pflicht aus Runbook 6a: beim Aufschreiben des Volltexts fiel die
unbelegte Behauptung auf.
