# Backlog triage — 2026-08-07

First day running the revised policy (two-case guarantee, no automatic
refunds), plus the owner's 2026-08-07 shipping/discount-code update.

## Run 1 (check-in, ~12:0x UTC)

Nine items. Note that several drafts made earlier today were denied and
redrafted against the updated policy.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "a thought about, Paw Friends" | samsonjaymes07@gmail.com | — | Not a support case — agency solicitation, no order reference | No reply | `Bot/No Action` |
| "Traffic retention insights" | dynovaconsult@gmail.com | — | Not a support case — agency solicitation ("why your traffic isn't converting") | No reply | `Bot/No Action` |
| "Re: Return order" | Fred Braun (fredbraun1966@gmail.com) | #3114 | Chew damage — toys destroyed within a day of arrival; outside the guarantee | Drafted the guarantee explanation, offered a photo review if anything looked wrong on arrival | `Bot/Draft Ready` |
| "Re: A shipment from order #3790 is on the way" | David Yendle (davidyendle14@gmail.com) | #3790 | Delivery question — dispatched 2 Aug, ~5 days | Tracking given, UK-warehouse/international-fulfilment explanation + 10–14 working day window, `Paw-Friends10` offered | `Bot/Draft Ready` |
| "Order eta 3590" | Lindsey Lake (lindseylake73@gmail.com) | #3590 | Delivery question — dispatched 29 July, ~9 days, tracking not yet scanning | Tracking given, same shipping explanation, `Paw-Friends10` offered | `Bot/Draft Ready` |
| "Cancel Order #4617" | Tor Vatne (vikingflooringlv@gmail.com) | #4617 | Pre-dispatch cancellation — order still UNFULFILLED, placed 5 Aug | Drafted confirmation that it can be stopped; needs the manual Shopify cancel/refund | `Bot/Needs Approval` |
| "Checkout price incorrect" | Claire Roberts (clairejroberts@btinternet.com) | — (pre-purchase) | Zahnbuddy billed at £14.95 despite being shown as a free gift — screenshot supplied. Same defect reported by Ian Beswick (#4543) and others | Drafted honest acknowledgement, advised not to complete the order until fixed, passed to owner | `Bot/Needs Approval` |
| "Fwd: Order #3770 confirmed" | Stephanie Bentley (steph.bentley84@googlemail.com) | #3770 | **Escalation** — cancellation request was never answered, and she is now threatening to report the store as a scam. Order already dispatched 30 July | `⚠️ MANUELLE PRÜFUNG` draft, acknowledges the unanswered cancellation, promises nothing | `Bot/Escalated - Owner Attention` |
| "Re: Order 1952" | Linda (casalyn262@hotmail.co.uk) | #1952 | **Escalation** — disputes how the toy was advertised, and this is her third contact with no reply since 28 July | `⚠️ MANUELLE PRÜFUNG` draft, no repeat policy explanation, handed to owner | `Bot/Escalated - Owner Attention` |

## Run 2 (check-in, ~12:1x UTC)

One new thread.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: #3714" | Sue Tudor (susie_tudor@hotmail.co.uk) | #3714 | Delivery question, second contact — our 31 July reply said it hadn't shipped; it then went out 1 Aug, so there was a genuine new update to give rather than a repeat holding line | Tracking given, shipping explanation, `Paw-Friends10` offered | `Bot/Draft Ready` |

## Run 3 (check-in, ~12:2x UTC)

One new thread — and it caught a real error on our side.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: Hello" | Nicholas Kloepfer (nicholaskloepfer@icloud.com) | #4604 | **Escalation** — third contact on the same case, and the address change he asked for on 5 Aug was never actually applied. Shopify still shows the original Orlando address; order is UNFULFILLED. He believes it was corrected because our reply quoted his new address back to him | `⚠️ MANUELLE PRÜFUNG` draft correcting his assumption honestly, confirming no tracking yet because it hasn't shipped, and flagging the change as urgent | `Bot/Escalated - Owner Attention` |

### Note on #4604 — needs action before this ships

The address correction has been requested three times and applied zero
times. The order is still unfulfilled, so it is fixable right now, but if
it dispatches to the Orlando address first this becomes a lost-parcel
claim on a US delivery. Worth doing today.

A quoted-back address in a reply is not a change. This is the second time
this week a customer has read a confirmation of *what they asked for* as
confirmation it was *done* (see Debra Woods #4284, 2026-08-04).

## Refund rule clarified + auto-refund attempted (2026-08-07)

The owner clarified the refund line: chew/play damage stays a firm no, but
unused items and pre-dispatch cancellations get the **full amount back**,
and asked the bot to execute those directly in Shopify.

**Attempted and blocked.** `orderCancel` (with refund) on #4617 was refused
by the Shopify connector's safety policy:

> `{"blocked": true, "matched": "orderCancel", "category": "financial",
> "reason": "Order cancellation and capture are blocked — they can move
> funds and trigger irreversible order-state changes."}`

`refundCreate` is blocked the same way. This is enforced by the connector
before the request reaches Shopify, so no policy wording or permission
change on our side unblocks it — it needs doing in Shopify admin.

Practical consequence: "refund — yes" cases are drafted and labelled
`Bot/Needs Approval` with the order number and exact amount stated, so the
owner can action them in a few seconds. **Pending right now: #4617, cancel
+ refund £51.27 in full.**

### Recurring defect worth fixing at source

The Zahnbuddy "free gift, then charged" checkout bug has now been reported
by at least five separate customers (Ian Beswick #4543, Kelly Hawkins,
Robert Brookfield, Priscilla, Brooke Layzell, now Claire Roberts). It is
generating support volume every few days and is a pricing-accuracy problem,
not a support one — fixing the checkout would remove the whole category.

## Offene Entwürfe im Volltext (Stand 2026-08-07 13:2x UTC)

Ab sofort wird jeder Entwurf beim Anlegen hier im Volltext protokolliert
(siehe Runbook 6a). Die folgenden lagen schon vorher im Entwurfsordner —
für die mit Volltext unten ist die Fassung verbürgt, die übrigen lassen
sich über den Gmail-Connector nicht mehr auslesen (`list_drafts` liefert
`plaintextBody` nur für den zuletzt erstellten Entwurf) und müssen vor dem
Senden in Gmail gelesen werden.

### Mit verbürgtem Volltext

**Entwurf an Tor Vatne (vikingflooringlv@gmail.com) — Betreff: Re: Cancel Order #4617**
> Hi Tor,
>
> Thanks for letting us know quickly — that made this easy.
>
> Order #4617 hasn't been dispatched, so it can be stopped. It's being cancelled and refunded in full — the whole £51.27 back to the card you paid with. You don't need to do anything.
>
> Refunds usually take a few working days to show on your statement depending on your bank. You'll get a confirmation from Shopify once it's gone through.
>
> Sorry the order went in by mistake, and thanks for catching it early.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Volle Erstattung £51,27. Muss in Shopify ausgeführt werden, bevor bzw. direkt nachdem diese Mail rausgeht.

**Entwurf an Nicholas Kloepfer (nicholaskloepfer@icloud.com) — Betreff: Re: Hello**
> ⚠️ MANUELLE PRÜFUNG - GRUND: Adressänderung #4604 wurde NICHT im System vorgenommen — Bestellung steht weiterhin auf der alten Adresse (13722 Lagoon Isle Way, Orlando) und ist unversandt. Kunde glaubt, sie sei korrigiert. Dritter Kontakt. Muss vor Versand geändert werden.
>
> Hi Nicholas,
>
> Thanks for checking — and I'm glad you did, because I need to correct something rather than let you assume it's sorted.
>
> When I quoted your address back to you, that was me confirming what you'd sent me, not confirming it had been changed on the order. I've just looked, and the order still has the original address on it. I'm sorry — that's on us, not you.
>
> Two things:
>
> There's no tracking yet, because #4604 hasn't been dispatched. So nothing has gone to the wrong address, and there's still time to fix it.
>
> I've flagged the address change as urgent so it's applied before the order ships. Once it does ship you'll get the tracking automatically, and I'll double-check it went out to the right place.
>
> Sorry for the back and forth on this one.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Adresse wird vor Versand geändert. Die ⚠️-Zeile vor dem Senden entfernen — sie ist nur für den Owner.

**Entwurf an Sue Steer (suesteer@hotmail.com) — Betreff: Re: Order #3089**
> Hi Sue,
>
> I'm really sorry to hear this — and thank you for the detail, that's genuinely helpful. A delivery photo showing your parcel somewhere that isn't even your property, combined with what you're hearing from others locally about EVRI, does suggest this one's gone astray rather than actually reached you.
>
> I've flagged this to the team with a view to getting a replacement sent out, since it doesn't look like this was your parcel going missing through any fault of yours. I can't confirm the exact next step myself, but wanted you to know this is being looked at properly rather than just pointed back to the courier.
>
> Thanks also for the feedback on EVRI — that's worth us knowing about.
>
> Sorry again for the hassle, Sue, and I'll be in touch as soon as I have an update.
>
> Best wishes,
> Lisa
> Paw Friends Customer Care
>
> **Zusage darin:** Ersatzlieferung wird geprüft, Rückmeldung zugesagt. Wenn kein Ersatz geschickt wird, muss sie trotzdem eine Antwort bekommen.

**Entwurf an Sandra Sant (sasant73@gmail.com) — Betreff: Re: Order**
> Hi Sandra,
>
> I'm really sorry — over six weeks since dispatch with no delivery, and multiple emails from you that never got a reply, is well below what you should expect from us. I don't want to just point you to tracking again without acknowledging that.
>
> For reference, order #1476 was dispatched on 25 June (tracking WNBAA0474015057YQ, https://t.17track.net/en#nums=WNBAA0474015057YQ), but I understand that doesn't help much at this point given how long it's been and that you've already had to buy replacements yourself.
>
> I'm flagging this directly to the owner as a priority so your refund request gets a proper answer rather than another wait. I can't approve it myself, but I want you to know this has been raised urgently.
>
> Thank you for your patience, Sandra, and I'm sorry this has taken so long to reach someone.
>
> Best wishes,
> Lisa
> Paw Friends Customer Care
>
> **Zusage darin:** Antwort auf ihren Erstattungswunsch zugesagt — keine Erstattung versprochen, aber eine Entscheidung. Betrag falls erstattet: £62,85.

**Entwurf an Ann Welsh (priceann100@gmail.com) — Betreff: Re: Dog toy fox**
> Hi Ann,
>
> I'm really sorry — nearly a month with no follow-up after being told the Resolutions Team would be in touch is not okay, and I don't want to just repeat that same promise again without anything to back it up.
>
> I'm flagging this directly to the owner now so it actually gets sorted rather than leaving you waiting any longer. I can't confirm the refund myself, but I want you to know this has been escalated properly this time.
>
> Thanks for your patience, Ann, and sorry again for how long this has dragged on.
>
> Best wishes,
> Lisa
> Paw Friends Customer Care
>
> **Zusage darin:** Entscheidung zum bereits zugesagten Refund. Achtung: ihr wurde am 17. Juli eine Erstattung zugesagt — Kauschaden, fällt eigentlich nicht unter die Regel. Owner muss entscheiden, ob die alte Zusage gehalten wird.

**Entwurf an Hector Cruz (hlcandassociates@gmail.com) — Betreff: Re: My Dog destroyed the Toy**
> Hi Hector,
>
> Thanks for coming back to me, and I understand you're not happy with how this has landed — that's a fair thing to feel.
>
> I don't want to just repeat the policy line again, so I'm passing this on to the team along with your message so they're aware of your feedback on how we describe durability and the review you're planning to leave. I can't promise a different outcome on the refund from where things stand, but I wanted to be upfront that this isn't being ignored.
>
> Thanks for your patience, Hector.
>
> Best wishes,
> Lisa
> Paw Friends Customer Care
>
> **Zusage darin:** Keine. Feedback wird weitergegeben, ausdrücklich kein anderes Ergebnis versprochen.

**Entwurf an Irene Hatter (irenehatter@hotmail.com) — Betreff: Re: Delivered 3 hours ago !!!**
> Hi Irene,
>
> Sorry to hear that — three hours is no time at all, and I completely understand why that feels wrong given how we describe these.
>
> Chew damage from normal play isn't something we're able to refund under our policy, since it's not a fault with the toy itself, so my hands are a little tied on that front. But I don't want to just wave off the point you're raising about the "indestructible" description — I'm passing that on to the team directly so it gets a proper look rather than a quick policy answer from me.
>
> Sorry again for the frustration, Irene, and thanks for flagging it.
>
> Best wishes,
> Lisa
> Paw Friends Customer Care
>
> **Zusage darin:** Keine Erstattung. Werbeaussage wird intern geprüft.

**Entwurf an Michael Green (groca69@googlemail.com) — Betreff: Re: Awaiting order**
> Hi Michael,
>
> Good question, and I want to be straight with you rather than leave it vague: your order is coming from our international fulfilment partner rather than a UK warehouse, which is why the tracking behaves a bit differently to a standard UK parcel. That's the reason it's taking longer than you'd expect for something ordered from a UK-based store.
>
> On standards — the toys go through the same safety testing regardless of which warehouse they ship from, so that side of things isn't affected by the shipping route.
>
> Thanks for bearing with us, Michael — hope it lands soon and is worth the wait.
>
> Best wishes,
> Lisa
> Paw Friends Customer Care
>
> **Zusage darin:** Keine. Enthält aber eine Aussage zur Sicherheitsprüfung — nur senden, wenn das stimmt.

### Volltext nicht mehr auslesbar — vor dem Senden in Gmail lesen

Diese Entwürfe wurden in früheren Läufen heute angelegt; der Connector gibt
ihren Text nicht mehr heraus:

- Susie Tudor (susie_tudor@hotmail.co.uk) — "Re: #3714"
- Casalyn (casalyn262@hotmail.co.uk) — "Re: Order 1952"
- Steph Bentley (steph.bentley84@googlemail.com) — "Re: Order #3770 confirmed"
- Claire Roberts (clairejroberts@btinternet.com) — "Re: Checkout price incorrect"
- Lindsey Lake (lindseylake73@gmail.com) — "Re: Order eta 3590"
- David Yendle (davidyendle14@gmail.com) — "Re: A shipment from order #3790 is on the way"
- Fred Braun (fredbraun1966@gmail.com) — "Re: Return order"

Ab dem nächsten Lauf tritt dieses Loch nicht mehr auf.

## Run 4 (check-in, ~14:2x UTC)

Drei neue Threads.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Fwd: Order #4617 confirmed" | Tor Vatne (vikingflooringlv@gmail.com) | #4617 | **Eskalation** — zweite Stornierungsanfrage. Die erste von heute Vormittag wurde nie beantwortet (Entwurf liegt unversendet), die Stornierung nie ausgeführt. Bestellung weiterhin UNFULFILLED, £51,27 | `⚠️ MANUELLE PRÜFUNG`-Entwurf, entschuldigt das Schweigen, bestätigt volle Erstattung | `Bot/Escalated - Owner Attention` |
| "(kein Betreff)" | Samantha Sheppard (s.j.sheppard@icloud.com) | #3657 | Sendung seit ~6 Tagen beim Zusteller ohne Bewegung. Evri hat sie an uns zurückverwiesen — sie darf auf keinen Fall wieder zum Zusteller geschickt werden (Policy: „Den Kunden nicht an den Versanddienstleister verweisen") | Entwurf mit Tracking, Zusage dass **wir** beim Carrier nachfassen | `Bot/Needs Approval` |
| "Re: Order #4926 confirmed" | Amy Jo Stevenson (ajstevenson@frontier.com) | #4926 | Adressänderung, Bestellung heute 14:05 aufgegeben, UNFULFILLED. Die angegebene Adresse ist unvollständig (nur Straße, keine Stadt/ZIP) | Entwurf fragt die vollständige Adresse ab, stellt ausdrücklich klar dass noch nichts geändert wurde | `Bot/Needs Approval` |

### Entwürfe im Volltext

**Entwurf an Tor Vatne (vikingflooringlv@gmail.com) — Betreff: Re: Order #4617 confirmed**
> ⚠️ MANUELLE PRÜFUNG - GRUND: Zweite Stornierungsanfrage von Tor. Die erste vom 07.08. wurde nie beantwortet, die Stornierung nie ausgeführt. #4617 ist weiterhin UNFULFILLED, £51,27 bezahlt. Muss heute in Shopify storniert + voll erstattet werden.
>
> Hi Tor,
>
> You're right to chase — you asked us to cancel this earlier today and hadn't heard back. Sorry about that.
>
> Order #4617 hasn't been dispatched, so it can still be stopped. It's being cancelled and refunded in full — the whole £51.27 back to the card you paid with. You don't need to do anything else.
>
> Refunds usually take a few working days to appear on your statement depending on your bank, and you'll get a confirmation from Shopify once it goes through.
>
> Sorry again for the silence on the first email.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Volle Erstattung £51,27. Zweite Zusage in Folge — die erste wurde nicht eingelöst. Muss heute ausgeführt werden. ⚠️-Zeile vor dem Senden entfernen.

**Entwurf an Samantha Sheppard (s.j.sheppard@icloud.com) — Betreff: Re: Order #3657**
> Hi Samantha,
>
> Thanks for letting us know, and for going to the trouble of speaking to Evri first — you shouldn't have had to do that.
>
> I won't send you back to them. Your order #3657 went out on 1 August under tracking UL381230954YP (https://t.17track.net/en#nums=UL381230954YP), and if it's been sitting with the courier for a week without moving, that needs chasing from our end rather than yours.
>
> I've passed it on so we can take it up with the carrier directly. I'll come back to you with what they say, or with a replacement if the parcel can't be located — I'd rather tell you that once we actually know, than guess now.
>
> Sorry for the wait, Samantha.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Wir fassen beim Carrier nach UND melden uns zurück. Ersatzlieferung als Möglichkeit genannt, nicht zugesagt. Wenn niemand beim Carrier nachfragt, ist das eine gebrochene Zusage — Betrag falls Ersatz/Erstattung: £27,95.

**Entwurf an Amy Jo Stevenson (ajstevenson@frontier.com) — Betreff: Re: Order #4926 confirmed**
> Hi Amy Jo,
>
> Thanks for catching this quickly — your order #4926 hasn't been dispatched yet, so there's time to change the address.
>
> Before I pass it on, could you send me the full address including town and ZIP? I have "N2660 Hayton Road" from your message, and I don't want to guess the rest and send it somewhere wrong. Your order currently has:
>
> 2235 Wisconsin Avenue
> New Holstein, Wisconsin 53061
>
> Once you confirm the complete new address, I'll get it changed before the order ships.
>
> To be clear, it isn't changed yet — I'll confirm once it actually has been.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Adressänderung vor Versand, sobald sie die vollständige Adresse schickt. Ausdrücklich klargestellt, dass noch nichts geändert ist (Lehre aus #4604).

### Muster, das sich wiederholt

Tor ist der zweite Fall diese Woche, bei dem ein Kunde nachhakt, **weil unser
Entwurf nie rausging**. Nicholas Kloepfer (#4604) war der erste. Beide Fälle
wären mit einem Klick erledigt gewesen.

Solange Entwürfe im Ordner liegen bleiben, erzeugt der Bot Arbeit statt sie
zu sparen — der Kunde schreibt erneut, und der Fall wird schlimmer statt
kleiner.

**Adressänderungen dieser Woche, keine davon ausgeführt:** #4604 Kloepfer
(3× angefragt), #4459 Russell (zu spät, bereits versandt), #4284 Woods,
jetzt #4926 Stevenson. Das ist ein eigener Rückstand.
