# Backlog triage — 2026-07-19

## Run 1 (hourly check-in, ~10:18 UTC)

One genuinely new thread; the other two matches were the same
already-verified stale threads from 2026-07-18 (no actual unread
messages, just Gmail's thread-level `is:unread` matching quirk — see
previous day's log).

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "No delivery" | Sandra Sant | #1476 | Rule 3, escalation trigger — order 36 days old, **partially fulfilled** (some items never shipped), the shipped portion has been in transit 24 days with no delivery, customer has already bought replacement toys and mentions contacting Klarna (payment-dispute risk). Wants it treated as a return/refund | Drafted honest reply acknowledging the delay, explains the order is mixed/partially fulfilled so the exact refund needs checking, no promise of a specific amount | `Bot/Escalated - Owner Attention` |

### Note on Sandra Sant (#1476)

Not a simple "wrong item" or single-item return — it's a 6-line-item order
(£62.85) that Shopify shows as PARTIALLY_FULFILLED, with only one
fulfillment record dispatched 25 June. Owner needs to check exactly what
did and didn't ship before deciding what to refund/cancel; the draft
deliberately doesn't commit to a specific outcome. Mention of contacting
Klarna is worth treating with the same urgency as the daz.38 chargeback
case — a payment-provider dispute may already be in motion.

## Run 2 (hourly check-in, ~13:59 UTC)

Two new threads, neither a real support case.

| Thread | Sender | Classification | Action | Label |
|---|---|---|---|---|
| "👋" | fagzycreative020@gmail.com | Vague opener ("is this Pawfriends's store?"), no actual question. Same shape as prior openers that turned into scam pitches (smithsofystorebuilder) — cautious but not yet clearly malicious | Drafted a short, generic confirmation reply with no owner/personal info | `Bot/Draft Ready` |
| "An honest offer to help" | mailer.shopifysurelinkhub@gmail.com | Cold marketing/SEO-audit solicitation ("send me your store URL for a complimentary audit") — same template shape as the shopifyrevenuefix spam from 2026-07-18 Run 2 | No reply | `Bot/No Action` |

## Run 3 (hourly check-in, ~17:12 UTC)

Two new threads.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "#2730" | Jason Collins | #2730 | Not explicitly covered by the 6 rules — courier (Evri) claims proof-of-delivery, but the customer doesn't recognise the door/person in the photo and it wasn't left with a neighbour. Reads as a misdelivered/lost parcel, same shape as darrenmarshallsmith09's #1173 case from 2026-07-18 | Drafted honest reply committing to raise it with the courier; doesn't promise resend vs. refund until the investigation is done | `Bot/Escalated - Owner Attention` |
| "Re: Important Update Regarding Your Order" | Karen Mournahan | — | Rule 1 — order finally arrived after a delay, dog tore the ear off immediately, no refund requested, no defect claim | Drafted friendly no-refund reply | `Bot/Draft Ready` |

## Run 4 (hourly check-in, ~17:51 UTC)

fagzycreative020@gmail.com (the "👋" thread) confirmed as marketing spam,
not a genuine customer — follow-up pitched "6000+ highly interested
shoppers... without paying anything upfront," a growth-marketing
solicitation. Reclassified from `Bot/Draft Ready` to `Bot/No Action`; no
reply drafted. Same vague-opener-then-pitch shape as smithsofystorebuilder
and mailer.shopifysurelinkhub — worth remembering "hey, is this X's
store?" with no real question is a mild spam signal on its own.

## Run 5 (hourly check-in, ~19:04 UTC)

Two new messages.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: 👋" | fagzycreative020@gmail.com | — | Follow-up nudge on the already-confirmed marketing spam thread | No reply | `Bot/No Action` (unchanged) |
| "Re: Important Update Regarding Your Order" | Karen Mournahan | #2784 (6 July, within window) | Pushed back on the Rule 1 no-refund explanation, citing the product's own "destroy everything" naming, but clarified she has a **second, unopened toy** she wants to return — that's a clean Rule 5 case | Drafted reply: holds the line on Rule 1 for the destroyed toy (product naming isn't a durability guarantee), agrees to process the return on the unopened one pending approval | `Bot/Needs Approval` |
