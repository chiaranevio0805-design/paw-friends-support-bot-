# Backlog triage — 2026-08-02

## Run 1 (hourly check-in, ~04:5x UTC)

One new thread — a broken promise on an already-confirmed cancellation.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Cancel order" (new thread) | Katharine Swann (swanny1412@gmail.com) | #3944 | Escalation trigger — customer quotes back a previous reply that promised the order hadn't shipped and would be cancelled/refunded (2026-07-31), but Shopify now shows the order was actually dispatched (2026-08-02, tracking UL383805642YP) — a broken promise, not a routine query | Drafted an honest reply acknowledging the mix-up directly, doesn't repeat the earlier promise or guess at an outcome, passes it to the owner as a priority | `Bot/Escalated - Owner Attention` |

### Note on Katharine Swann (#3944)

The 2026-07-31 cancellation confirmation reply told her the order hadn't shipped and would be cancelled/refunded, but Shopify's fulfillment record shows it was dispatched on 2026-08-02 anyway — the promised cancellation apparently wasn't actioned before dispatch. This is the exact failure mode called out in the support policy (a promised outcome not honoured, then contradicted by what actually happened) — worth checking whether other pending cancellation/address-correction requests from recent runs were actually actioned in Shopify.

## Run 2 (hourly check-in, ~05:5x UTC)

One new thread, clean pre-shipment cancellation.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Order 4212. Cancel" | Mandy Baker (mandyfindlater81@gmail.com) | #4212 | Cancellation request ("changed my mind") — order placed minutes earlier, still UNFULFILLED, so a clean pre-shipment cancel/refund | Drafted honest reply confirming the order hasn't shipped and can be cancelled/refunded in full | `Bot/Needs Approval` (cancellation/refund is a manual Shopify action, not something the bot can execute) |

## Run 3 (hourly check-in, ~09:2x/09:5x UTC)

Two new threads.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Order 2997" | Laura Vincent-Evans (lauraelizabethvincent@gmail.com) | #2997 | Repeat unresolved contact — dispatched 22 July, now well over a week overdue; she says she was already told it would be "escalated" and delivered yesterday, but it still hasn't arrived. Broken promise on delivery timing, apparently lost parcel | Drafted an honest reply that doesn't repeat the unfulfilled promise, flags it to the owner for an actual replacement/refund decision | `Bot/Escalated - Owner Attention` |
| "Your storefront" | emails.nexthos@gmail.com | — | Not a support case — vague "did you take a look at your storefront lately?" opener, same shape as prior marketing/agency solicitation probes | No reply | `Bot/No Action` |

## Run 4 (hourly check-in, ~13:1x UTC)

One new thread, routine follow-up on an existing return case.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: Order #3162 confirmed" | Jo Perry (jo_chris@live.co.uk) | #3162 | Rule 5 continuation — confirmed unused/original packaging (2026-07-31), now asking for return details to send items back for a full refund | Drafted a short reply confirming the return details/prepaid label will be sent along with the refund | `Bot/Needs Approval` (unchanged) |

## Run 5 (hourly check-in, ~18:2x UTC)

One item, no new action needed.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re order july 18 th" | Christine Macdonald (chrisandmac@sky.com) | #3050 | Repeat send, no new content — same "indestructible"/Sale of Goods Act/refund + return-label request already escalated on 2026-08-01 Run 3, sent from a new Gmail thread (different subject) that didn't inherit the existing Escalated label | No new draft needed; existing escalation and drafted reply from Run 3 still stand | `Bot/Escalated - Owner Attention` (relabeled — new thread wasn't carrying the label) |

## Run 6 (hourly check-in, ~20:2x UTC)

One new thread — an address correction combined with a security-sensitive payment request.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "ORDER #4284" | craigdebbie12@gmail.com (order under Debra Woods) | #4284 | Address-correction request (order still UNFULFILLED, time to fix) combined with the customer pasting a full card number in plaintext and asking us to charge it instead — a security-sensitive request the bot has no authority or safe channel to act on | Drafted a reply confirming the address fix is being actioned, firmly declining to process the card number sent by email (without repeating the digits back), and advising against sending card details by email going forward | `Bot/Escalated - Owner Attention` (payment/security judgment call, not a routine address correction) |

### Note on order #4284 (Debra Woods / craigdebbie12@gmail.com)

The customer emailed a full 16-digit card number in plaintext asking us to charge it instead of the original payment method. This isn't something the bot should ever act on or repeat back — flagging to the owner as a security/PCI concern as well as a routine address correction. Worth considering whether the reply should also mention deleting/not storing that email, though that's a call for the owner given it touches account security practices.
