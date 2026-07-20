# Backlog triage — 2026-07-20

## Run 1 (hourly check-in, ~08:13 UTC)

One genuinely new/unresolved thread; the other two matches were the same
already-verified stale threads (no actual unread messages).

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: Refund – Order 1240" | Sharon Alberio (pinkpookie16) | #1240 | Repeat unresolved contact (this is her 6th message since 25 June) — a pre-existing reply (17 July, before this bot existed) already approved her return but **sent the literal placeholder text `[RETURN ADDRESS – PLEASE ADD]` instead of a real address**. She's now asked twice for the actual address | Drafted an honest apology that doesn't invent an address; says the correct one is being confirmed | `Bot/Escalated - Owner Attention` |

### Important: no real returns address exists anywhere in this system

This isn't just about Sharon. Every approved-return case in the queue so
far (Joanne Hopkins #2433, Do Robinson #1915, Niki Curtis #1218, Lucy
Haskins #2188, Karen Mournahan #2784, and now Sharon Alberio #1240) has
been told "return instructions/address coming shortly" — correctly, since
this bot has never had access to a real return address to give out. But
that means **none of these customers can actually complete their return
yet**, and at least one prior reply (Sharon's) already leaked an unfilled
template placeholder to a customer, which looks unprofessional and is a
symptom of the same underlying gap. The owner needs to either supply a
real returns address for the bot to use going forward, or confirm returns
should route through a different process entirely (e.g. no physical
return required, refund on photo evidence only).

## Run 2 (hourly check-in, ~14:15 UTC)

Non-customer notices only this run (2x Klaviyo account-security emails,
German language, MFA prompts) — filtered, no reply needed, not logged as
a substantive entry.

## Run 3 (hourly check-in, ~15:15 UTC)

Two new threads.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Re: Order #2817 confirmed" | Lorraine Reimann | #2817 | Rule 1 — both plush toys destroyed within 10 minutes, no refund requested, no defect claim, photos attached | Drafted friendly no-refund reply | `Bot/Draft Ready` |
| "Re: Important Update Regarding Your Order" | Lynda Corney (richfdx602) | #1485 | **Serious escalation trigger, multiple at once**: order dispatched 25 June, still not confirmed received (25+ days in transit); a prior reply's "we're a legitimate business" reassurance was rejected; customer now explicitly cites Trust Pilot reviews and threatens to contact her bank and report Paw Friends as fraudulent | Drafted an honest reply that does **not** repeat the "legitimate business" reassurance or make new promises; acknowledges her right to contact her bank; escalates directly | `Bot/Escalated - Owner Attention` |

### Note on Lynda Corney (#1485)

This is now the second customer (after daz.38 on 2026-07-18) to explicitly
invoke Trust Pilot while threatening a bank/chargeback dispute. Given the
pattern is recurring, worth checking whether there's a shared root cause
(e.g. a batch of orders from the same period/courier all running very
late) rather than treating each as an isolated case.

## Run 4 (hourly check-in, ~15:57 UTC)

One new thread.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Order #3017" | Bernadette Murphy | #3017 | Not one of the 6 explicit rules, but about as clean as a refund request gets: order placed 3 days ago and confirmed UNFULFILLED in Shopify — a straightforward pre-shipment cancellation | Drafted a confident reply agreeing to cancel and refund | `Bot/Needs Approval` (not rule-4, so still requires sign-off, but no complication of any kind) |
