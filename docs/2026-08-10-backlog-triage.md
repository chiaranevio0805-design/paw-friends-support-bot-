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

## Run 2 (~09:2x UTC)

Zwei neue Threads — und ein Fehler auf unserer Seite, der beim Lesen von
Lynn Franks' Thread aufgefallen ist.

### Der Fehler: interner Vermerk ging an eine Kundin

Der Entwurf an Lynn Franks (#1952) wurde am 09.08. um 21:22 gesendet — **mit
der internen Markierung als erster Zeile**:

> ⚠️ MANUELLE PRÜFUNG - GRUND: Werbeaussage bestritten + dritte
> Kontaktaufnahme, seit 28.07. keine Antwort erhalten
>
> Hi Lynn, …

Eine britische Kundin, die bereits zweimal ohne Antwort geblieben war und
Trading Standards angedroht hatte, bekam damit einen deutschen internen
Vermerk zu sehen, der sie als Vorgang klassifiziert.

**Ursache ist mein Format, nicht der Versand.** Ich hatte die Markierung in
den Entwurfstext gesetzt; der Owner sendet Entwürfe unverändert. Bei
Nicholas Kloepfer wurde die Zeile vor dem Senden entfernt, bei Lynn nicht —
darauf darf sich das System nicht verlassen.

**Behoben:** `support-policy.md` und `runbook.md` sind geändert. Der
Eskalationsgrund steht ab sofort **ausschließlich im Log und im
Abend-Report**, nie im Entwurf. Entwürfe sind so zu schreiben, dass sie
unverändert versendbar sind.

**Zu prüfen:** Ob weitere Entwürfe mit der Markierung rausgingen. Eine
Gmail-Suche über `in:sent` nach dem Text lieferte keine Treffer (Gmail
indexiert die Zeichenfolge offenbar nicht zuverlässig), daher konnte ich es
nicht abschließend klären. Betroffen sein könnten die Eskalationsentwürfe
vom 07.08.: Stephanie Bentley (#3770) und Tor Vatne (#4617).

### Neue Vorgänge

| Kunde | Order | Klassifikation | Label |
|---|---|---|---|
| Lynn Franks | #1952 | **Eskalation** — vierter Kontakt. Fordert Erstattung **£17,95**, droht Trading Standards an. Ihre Beschwerde ist ausdrücklich „not as described / nicht wie abgebildet", nicht nur Kauschaden — das ist rechtlich ein anderer Fall | `Bot/Escalated - Owner Attention` |
| Nikki | — | Kauschaden nach 5 Min. nach langer Lieferzeit, Erstkontakt, verweist auf die Erwartung aus der Werbung | `Bot/Draft Ready` |

**Eskalationsgrund Lynn Franks:** Trading Standards angedroht, vierter
Kontakt, zwei gebrochene Rückmeldezusagen, bestrittene Produktbeschreibung.

### Entwürfe im Volltext

**Entwurf an Lynn Franks (casalyn262@hotmail.co.uk) — Betreff: Re: Order 1952**
> Hi Lynn,
>
> Two things, and I'll be straight with you on both.
>
> First — my last email to you had a line of internal text at the top, in German, that was never meant to leave our system. That was our mistake, not something you did, and I'm sorry it landed in your inbox. Please ignore it.
>
> Second, and more importantly: you're right that you've been told twice now that you'd hear back, and twice you haven't. I'm not going to make that promise a third time and leave it hanging.
>
> Your complaint isn't only that your dog destroyed the toy. You're saying the item didn't match the pictures and wasn't as described, and that it wasn't fit for purpose. That's a different argument from ordinary chew damage, and it's one I'm not in a position to dismiss.
>
> I've put your refund request in front of the owner as a decision that needs making, with your order details and the amount, £17.95. You've also mentioned Trading Standards, which is entirely your right and something I've flagged rather than glossed over.
>
> I'm sorry it has taken this many emails.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Keine Erstattung zugesagt — aber zugesagt, dass eine Entscheidung getroffen wird. Entschuldigung für den internen Vermerk. £17,95 falls erstattet.

**Entwurf an Nikki (nikki.1988@yahoo.com) — Betreff: Re: Destroyed**
> Hi Nikki,
>
> Sorry — a long wait followed by five minutes of use is a rotten combination, and I understand the disappointment.
>
> Our 30-day money-back guarantee covers items that arrive faulty and items returned unused within 30 days. Damage from chewing isn't something it covers, so I can't promise a refund on that basis.
>
> What I won't do is pretend the expectation you had came from nowhere. If the way these are advertised set you up for something different, that's a fair point and one I've passed on rather than argued with here.
>
> If anything looked wrong with the toy before your daughter's dog got hold of it, send me a photo and I'll take another look.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Keine Erstattung. Fotoprüfung angeboten, Werbepunkt weitergegeben.

### Zur Werbefrage, zweiter Beleg

Lynn Franks schreibt, der Artikel habe „nothing like the pictures" ausgesehen.
Das ist inhaltlich etwas anderes als die „40.000 Hunde"-Zitate der übrigen
Kunden — hier geht es um die Produktabbildung, nicht um die Haltbarkeits-
aussage. Beide Stränge zeigen aber auf dieselbe Stelle: das Werbematerial
außerhalb der Produktseite.
