# Backlog triage — 2026-07-28

## Run 1 (hourly check-in, ~01:2x UTC)

One new thread, not a support case.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Hi, I'm interested in buying today. Are you available?" | tech.joshgrowmmerceedge@gmail.com | — | Not a support case — vague solicitation with no order/product reference, sender pattern reads as a marketing/agency probe similar to prior spam (Fiverr, wholesale, bulk-order solicitations) | No reply | `Bot/No Action` |

## Run 2 (hourly check-in, ~08:0x UTC)

One new thread, routine.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "ORDER 3643" | Philip Draper | #3643 | Rule 3-adjacent — pre-shipment address confirmation request, order placed same morning, still UNFULFILLED. Address on file already matched what he asked for | Drafted a reply confirming the address matches and that tracking will follow once dispatched | `Bot/Draft Ready` |

## Run 3 (hourly check-in, ~10:1x/10:2x UTC)

Two new threads.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: Order #2964 confirmed" | Nicholas Killick | #2964 | Rule 3, with a correction — his second follow-up after a 24 July reply incorrectly said the order hadn't shipped yet due to stock; Shopify tracking actually shows it was dispatched 22 July (2 days *before* that reply), 6 days in transit now, within normal window | Drafted an honest reply correcting the earlier inaccurate info, with the real tracking link | `Bot/Draft Ready` |
| "Re: Order #3656 confirmed" | Kelly Hawkins | #3656 | Not covered by the six numbered rules — billing/pricing dispute, not a wrong-item or return case. She says checkout displayed the Zahnbuddy as a free gift but it was charged £14.95; screenshot attached. Order also carries an "UpCart Rewards" tag suggesting a gift-with-purchase promo may be involved | Drafted an honest reply that doesn't confirm or deny a refund itself, flags the promo/pricing question to the owner to check | `Bot/Needs Approval` |

### Note on Nicholas Killick (#2964)

The 24 July reply on this thread stated the order hadn't shipped due to UK stock issues, but Shopify's fulfillment record shows it was actually dispatched two days *before* that reply was drafted. Worth double-checking fulfillment status directly rather than relying on assumptions when a delay has already been mentioned once — this is the second instance this month of a shipping-status reply not matching the actual Shopify record (see also Helen Passfield's own tracking-lookup confusion, 2026-07-27).

## Run 4 (hourly check-in, ~11:3x UTC)

One new thread, routine (angry tone).

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: Important Update Regarding Your Order" | Brian Hall | #3426 | Rule 3 — first contact, terse and angry ("This is ridiculous") reply to a bulk shipping-delay notice; order still UNFULFILLED (2 days old), not yet an escalation trigger (no advertising dispute, no consumer-law citation, no repeat contact) | Drafted an honest, extra-friendly reply per Rule 6 tone modifier, explaining the international-fulfilment delay honestly and offering reship/refund if it doesn't move soon | `Bot/Draft Ready` |

## Run 5 (hourly check-in, ~12:3x UTC)

One new thread — continuation of a long-running, already-escalated case, from a new Gmail thread (different subject wording, so not caught by the label-exclusion search under its existing Escalated label).

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Order 13th June." | Lynda Corney (richfdx602) | #1485 | Continuation of the ongoing #1485 saga (first raised 19 June, escalated 2026-07-03 and 2026-07-20 for a Trust Pilot citation and legitimacy dispute). Order shows dispatched 25 June — over a month ago — still apparently undelivered. Terse, angry message ("Is this some kind of joke?") with a screenshot attached | Drafted an honest reply acknowledging the six-week failure directly, not disputing her right to escalate further, and flags to the owner that this needs an actual resend/refund decision now | `Bot/Escalated - Owner Attention` (relabeled — new thread wasn't previously labeled) |

## Run 6 (hourly check-in, ~14:5x UTC)

Two new threads.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Poor quality" | Peter Hensman | #2965 | Disputed advertising claim — toy destroyed within 30 minutes, explicitly quotes the "anti destructive structure" claim as the reason for purchase, requests a refund | Drafted an honest reply that doesn't apply the standard Rule-1 chew-damage denial, passes the advertising dispute and refund request to the owner | `Bot/Escalated - Owner Attention` |
| "Just ordered my address is 22 gwalia terrace Sa44dw" | pheaher@icloud.com | — (no order found under this email) | Not classifiable yet — no order number given, message body otherwise empty, and the sender's email doesn't match any Shopify order | Drafted a reply asking for the order number or the name it was placed under | `Bot/Draft Ready` |

### Note on Peter Hensman (#2965)

Twelfth customer overall to dispute the "indestructible"/"anti destructive structure" advertising claim — this pattern continues to recur multiple times per week.
