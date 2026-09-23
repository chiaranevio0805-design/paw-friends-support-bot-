# Paw-Friends — Daily Support Report
**Window: 22 Sep 2026 08:14 UTC → 23 Sep 2026 08:14 UTC**
**Compiled from `docs/2026-09-22-backlog-triage.md` and `docs/2026-09-23-backlog-triage.md`.**

---

## 0. Two things before the numbers

**No Gmail draft was created and nothing was emailed to
`nevio.marasa@icloud.com`.** `create_draft` and the label tools have been
blocked on this account since **21 August**. **Twenty-one attempts have been
made; no twenty-second was made today.** The report was written to the
repository, committed, and posted in chat instead.

**No email has been sent to any customer.** Every item below is a draft in
`docs/entwuerfe-zum-kopieren.md` and nowhere else.

---

## 1. Counts by category

| Category | Count |
|---|---|
| Draft Ready | **0** |
| Bot/Needs Approval | **0** |
| **Bot/Escalated — Owner Attention** | **26** |
| No Action | **0** |

Twenty-three customer cases on 22 Sep from 08:14 onward, three on 23 Sep.
**Plus two findings from the sent folder with no customer contact and therefore
no draft.**

### By theme

| Theme | Count |
|---|---|
| Durability / toy destroyed | 14 |
| Advertising or guarantee disputed | 15 |
| Return of unused goods requested | 4 |
| Never arrived / shipment not updating | 3 |
| Money promised, not paid | 2 |
| Short shipment / missing free item | 1 |
| Cancellation | 1 |
| Not yet despatched | 1 |
| Sender cannot be matched to an order | 2 |

*(Cases appear in more than one row.)*

---

## 2. Refunds actually issued

**None. No cancellation carried out either.**

**No case met rule 4** (confirmed wrong item shipped). `refundCreate` and
`orderCancel` remain blocked for the bot.

---

## 3. 🔴 Three things that need the owner today, in order

### 3.1 ⏰ #8669 Chad Lovell — a cancellation refused on a false basis, window still open

On **22 Sep at 11:16** the shop account told him: *"order #8669 **has already
been shipped**, so we're unable to cancel it."*

Shopify, re-checked at 13:20 the same day:

| Field | Value |
|---|---|
| `displayFulfillmentStatus` | **UNFULFILLED** |
| `fulfillments` | **empty** |
| `fulfillmentOrders` | **OPEN / requestStatus UNSUBMITTED** |
| `cancelledAt` | **null** |
| `updatedAt` | **19 Sep 17:17:43** — six seconds after the order was placed |

**The despatch was never even requested. Nothing supports the statement he was
given.** He cancelled **eleven minutes** after ordering. **$38.19.**

**Next step: cancel and refund, or correct the statement to him. Only the admin
can do either, and the window closes the moment someone picks the parcel.**

### 3.2 🔴 Nine promises of money, none of them executed

| Order | Amount | What was said | Shopify |
|---|---|---|---|
| **#4812** Carolyn Marmalejo | **£86.89 / $116.92** | *"full refund … has been processed"* (21 Sep) | **nothing booked** |
| **#7884** Logan Bishop | **$8.30** | *"30% partial refund has been processed"* (22 Sep) | **nothing booked** |
| **#7179** Keith Crane | **$24.32** | 50% offered *"we will arrange it for you"*, **accepted 22 Sep** | **nothing booked** |
| **#6546** Vik Jehdian | **$41.55** | *"processed"* (9 Sep) | **nothing booked** |
| **#6583** Ken Beville | **£30.54** | promised 3 Sep, **repeated verbatim 21 Sep** | **nothing booked** |
| **#5148** Trudi Wright | open | *"processed"* twice | **nothing booked** |
| **#6259** Nick Tarrant | open | reported executed 19 Sep | **nothing booked**; Trading Standards, deadline expired |
| **#4998** | £19.95 | promised | **nothing booked** |
| **#7060** | open | 30% accepted | **nothing booked** |

**#7884 is the worst of them: he had explicitly said to keep his money.** The
message begins *"Thank you for confirming"* — **there is no confirmation from
him** — and **ten and twenty-three seconds later** two further, contradictory
messages went to the same address.

**No draft was written to #4812 or #7884.** Neither has written to us, and this
desk sends no unsolicited mail. **What goes to them depends on which way the
owner decides.**

### 3.3 ⛔ Five customers hold unused goods they cannot return

**#6254 · #8312 · #7347 · #8372 · #7479.** **In every one of them the
chew-damage template either created the request or refused it again.**

- **#8372 Kerri Forbey received the template twice for a product she never
  unwrapped** — the second time on 22 Sep, **three days after she had corrected
  us in writing.**
- **#7347 Jill Hibbs has asked three times** to return an undamaged Fluffy.
  **The Fluffys page carries the 30-day guarantee with no condition attached,
  and her item meets the condition she was quoted.**
- **#7479 Richard Bellamy-Williams** was offered **30% on an item the reply
  itself calls unopened and unused**, a day after his deadline expired, under
  **"Dear Customer"**. He declined on 22 Sep at 22:44: *"Thank you, but I'd
  rather have the refund."*

**There is no returns address. Every draft says so and tells the customer not
to post anything.**

---

## 4. The rest of the escalated items, with next steps

| Order | Customer | Situation | Next step |
|---|---|---|---|
| **#8295** | Ivan Griffen | **⏰ his deadline expires today** | Decide before it passes |
| **#5036** | Lynette Lumley | never arrived; refund asked **9 Sep**; **three follow-ups unanswered**; an investigation promised 10 Sep and never delivered; **Ombudsman announced** | **£27.95** |
| **#8605** | Gurvinder Ghattaura | **not despatched since 17 Sep**; **cancellation window still open** — he was told so | Despatch or cancel |
| **#8080** | Ryan Beam | tracking errors, **no update in 14 days**, **23 days elapsed against the 7–21 he was quoted** | Trace or refund |
| **#8483** | Linda Richardson | **no update in 8 days** | Trace |
| **#7608** | Patricia Arenella | *"buy one get one free, which I never received"*; the order records **one** item | Check the checkout |
| **#7989 · #6656** | Reynolds · Sida | short shipments, both unresolved; **#6656 announced a bank claim** | Check quantities |
| **#8337** | Cheryl Tagg | **has taken legal advice**; wrote 19 Sep *"please do not ignore this email"* and was ignored for three days | Owner decision |
| **#4792** | (order in another name) | **two refusals, 17 days**, now announcing a public post with photos | Owner decision; **the two refusals are not being upheld** |
| **#7472** | Francisco Almazan | **his size complaint from 18 Sep is still unanswered** — the template never touched it | Answer the actual complaint |
| **#7771** | Barb Fitzgerald | **sixth contact**, "Dear Customer"; she was told on 1 Sep the order had shipped — **the despatch is dated 3 Sep** | Owner decision |
| **#7041 · #7828 · #7457 · #5310 · #8407 · #8002** | — | all asked **how to get a refund** and were sent a policy refusal instead | Answer the question asked |
| **#8457 · #8466 · #7084 · #8126** | — | **asked for nothing**; offered, not assumed | Owner decision if they reply |
| **jscalera1 · executiveenamel06 · Maria Carter** | — | **three senders whose address is on no order** | **Only the admin can look behind the accounts** |

---

## 5. 🟦 Where the advertising claim might be

**Fifty independent customer statements** now rest on a guarantee or durability
claim — ten of them in this window alone.

**Six sources, five of which only the owner can open:** the evidenced Klaviyo
emails of 27 Aug (**guarantee stated with no condition**) · two advertorial
pages the API returns empty · a customer PDF (#7898) · a product image said to
carry *"with a replacement guarantee"* (#7168) · **Facebook** (#2852, #6311)
and **Instagram** (#6311), with an embedded banner sitting in #6311's own mail.

**The sixth needs no access at all: the article name.** #7813 and Maria Carter
both quote *"…for dogs that destroy toys"*, which is what the product is called
in the shop.

**Three customers now describe a _replacement_ guarantee** — #7179 (13 Sep, the
earliest), #7168, #6311. **That is a different promise from the money-back one
and is not conflated with it in any draft.**

**Five customers have now named the same logical break** — a guarantee that
only covers an unopened item cannot say anything about how long it lasts:
#7541, #6254, #6311, #8407, #7771.

---

## 6. One correction to my own figures

**The £14.98 carried for #7479 was an estimate and has been withdrawn.** The
order is a two-for-one: **£29.95 was paid for both Fluffys**, and the share for
the single unopened one **cannot be derived from a Kaching bundle price**. The
same applies to #7347 and #8312, both now shown as unquantified. **The
quantified refund total is £466.47, not £481.45.**

---

## 7. What no draft in this window contains

No refund promised · no replacement promised · no refusal · no returns address
invented · **no chew-damage template** · no legal assessment in either
direction · no attempt to talk anyone out of legal advice, an Ombudsman, a bank
claim, Klarna, Trading Standards or a public post · no statement about product
size or comparison with product images · nothing about material safety · no
earlier safety report re-raised unprompted · no claim about what an
advertisement said · no assertion that a quoted phrase does not exist · no
photo, PDF or attachment opened, and the customer is told so · no customer's
report reinterpreted as a refund request · no pressure toward a refund on
someone who declined one · no product change promised · no order data to an
address that is not on the order · no third party's order described · no
guessing of a customer's first name · no currency conversion · no line-item
share estimated from a bundle price · no referral to a carrier · no escalation
marker in any customer-facing text.
