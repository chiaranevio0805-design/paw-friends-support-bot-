# Paw-Friends — Daily Support Report
**Window: 21 Sep 2026 08:13 UTC → 22 Sep 2026 08:13 UTC**
**Compiled from `docs/2026-09-21-backlog-triage.md` and `docs/2026-09-22-backlog-triage.md`.**

---

## 0. Two things to say before the numbers

**This report was not emailed, and no Gmail draft was created.** `create_draft`
and the label tools have been blocked on this account since **21 August**.
**Twenty-one attempts have been made; no twenty-second was made today.** The
report was written to the repository first, committed, and is posted in chat.
**Nothing was sent to `nevio.marasa@icloud.com`.** If the block is lifted, say so
and the draft will be created.

**No email has been sent to any customer.** Every item below is a draft in
`docs/entwuerfe-zum-kopieren.md` and nowhere else.

---

## 1. Counts by category

| Category | Count |
|---|---|
| Draft Ready | **0** |
| Bot/Needs Approval | **0** |
| **Bot/Escalated — Owner Attention** | **24** |
| No Action | **0** |

Twenty-three customer cases on 21 Sep from 08:13 onward, one on 22 Sep.
**Plus one finding with no customer contact and therefore no draft — see §3.**

### By theme

| Theme | Count | Orders |
|---|---|---|
| Durability / toy destroyed | 11 | #6384, #8406, #3387, #8002, #8003, #7898, #8295, #7578, #6311, #7813, #8142 |
| Advertising or guarantee disputed | 11 | #8406, #7048, #7541, #7815, #3387, #8003, #7898, #7168, #2852, #6311, #7813, #8142 |
| Money promised, not received | 2 | #6583, #6546 |
| Never delivered / replacement never sent | 2 | #2894, #3089 |
| Short shipment | 2 | #7989, #6656 |
| Return of unused goods requested | 1 | #6254 |
| Order cannot be matched to the sender | 1 | jscalera1@aol.com |

*(Cases appear in more than one row.)*

---

## 2. Refunds actually issued

**None. Zero. In the whole window.**

**No case met rule 4** (confirmed wrong item shipped). The two short-shipment
cases (#7989, #6656) are **missing goods, not a wrong variant**, and were
deliberately not treated as rule-4. `refundCreate` and `orderCancel` remain
blocked for the bot in any case.

---

## 3. 🔴 The finding that matters most

**#4812 — Carolyn Marmalejo.** On **21 Sep at 09:34 UTC** the shop account told
her, in writing:

> *"We can confirm that your **full refund for the unused toys has been
> processed** to your original payment method."*

**Shopify shows `totalRefundedSet` 0.00 USD and an empty `refunds` list.**
Order #4812, **$116.92 / £86.89**, placed 6 Aug. **Nothing was paid.**

**This is the seventh promise of money that was never executed:**

| Order | Amount | Promised | Status in Shopify |
|---|---|---|---|
| **#4812** Carolyn Marmalejo | **£86.89 / $116.92** | full refund, 21 Sep | **nothing booked** |
| **#6546** Vik Jehdian | **$41.55** | 50%, "processed" 9 Sep | **nothing booked** |
| **#6583** Ken Beville | **£30.54** | full refund 3 Sep, **repeated verbatim 21 Sep** | **nothing booked** |
| **#5148** Trudi Wright | open | 50%, "processed" twice | **nothing booked** |
| **#6259** Nick Tarrant | open | reported executed 19 Sep | **nothing booked**; Trading Standards, deadline expired |
| **#4998** | £19.95 | promised | **nothing booked** |
| **#7060** | open | 30% accepted | **nothing booked** |

**No draft was written to Carolyn Marmalejo.** She has not written to us, and
this desk does not send unsolicited mail to a customer — least of all mail
telling her that yesterday's promise is not backed by a booking. **That is the
owner's call.**

**Recommended next step, and it is the first one on this list:** either make the
bookings, or correct the promises to the customers who hold them. **Both can
only be done from the Shopify admin.**

---

## 4. All escalated items, with recommended next steps

### 4.1 Oldest unanswered cases — nobody has ever replied to these

| Order | Customer | Situation | Recommended next step |
|---|---|---|---|
| **#2894** | Jeff Hughes | arrived damaged 23 Jul, **replacement promised in writing 24 Jul, never despatched**, **eight follow-ups**, 46 days silent | Owner decision: send the replacement or refund **£19.95**. Draft ready; it states plainly that eight messages went unanswered. |
| **#3089** | Sue Steer | **never delivered** since 28 Jul, **four follow-ups, not one reply** | Owner decision: **£27.95**. Two discrepancies (she says three items, order records two; she names Evri, the order records another carrier) are **set side by side, not resolved**. |

### 4.2 Money promised and not paid

| Order | Customer | Recommended next step |
|---|---|---|
| **#6583** | Ken Beville | He received **the identical promise twice** (3 Sep and 21 Sep). **£30.54.** Book it or tell him the truth. |
| **#6546** | Vik Jehdian | 50% accepted twice, confirmed as "processed" 9 Sep. **$41.55.** Note: he writes from an address **not recorded on the order**, so the draft names no order number, amount or contents. |

### 4.3 Deadline running

| Order | Customer | Recommended next step |
|---|---|---|
| **#8295** | Ivan Griffen | **His deadline expires tomorrow, 23 Sep.** Fifth draft. He has corresponded since 6 Sep; yesterday's reply to him opened with **"Dear Customer"** after three weeks. |

### 4.4 The chew-damage template, and what it did on 21 Sep

**At least twenty-five sends went out on the morning of 21 Sep.** Four replies
came back within thirty minutes. Several were addressed **"Dear Customer"** to
people on their third and fifth contact.

| Order | Customer | What the template did | Recommended next step |
|---|---|---|---|
| **#7989** | Karen Reynolds | She reported a **short shipment**. She was sent a **chew-damage refusal**. Her reply: *"NO NO NO NO … Nothing is damaged... Read my email."* | Resolve the quantity: paid for 2, received 1. **Do not tell her she miscounted** — the draft does not. |
| **#6254** | David Hickman | The template invited returns of unused items. He answered: *"I … do have two in their packaging untouched. Can I please return these items?"* **There is no returns address.** | The refusal **created** a return case the shop cannot fulfil. Decide the refund or give a returns address. |
| **#6311** | Garth Callaghan (AU) | He asked for a **replacement** as advertised. He was sent a **money-back condition**. | Answer the question he asked. **AU rights passage quoted to him verbatim, not interpreted.** |
| **#8002** | Thomas Robinson | Received it **twice**, second time as "Dear Customer". Asked: *"Is this an automated response?"* | The draft answers **yes**. No third send. |
| **#7541** | Lois Hertz | *"Who wants to return an unopened product? You are conmen."* | She names the logical break precisely. Owner question whether the condition is defensible — **no legal assessment given.** |
| **#6384** | Simon Foord | Consumer Rights Act cited, **Klarna and Trading Standards** notified | No legal assessment, no third refusal, **no attempt to talk him out of either.** |
| **#8406** | Joyce Abdalla | *"30 day guarantee implies you stand behind your product."* | She is **also a swallowing report** from 18 Sep. **Not raised again unprompted**, and **nothing said about material safety.** |
| **#6804**, **#7815**, **#3387**, **#8003**, **#7898**, **#8142**, **#7578**, **#7813** | — | durability and advertising | All escalated; no promise, no refusal, no template in any draft. |

### 4.5 Short shipments — both unresolved

| Order | Customer | Recommended next step |
|---|---|---|
| **#7989** | Karen Reynolds | paid for 2, received 1; a variant was promised in writing 29 Aug and never actioned |
| **#6656** | Jesse Sida | paid for 4, received 2 — **the order records two, both despatched**. **Bank claim announced.** The two statements are set side by side; **the bundle display is named as a possible cause but not asserted.** Only the admin can see what he was charged for. |

### 4.6 Cannot be matched

| Sender | Recommended next step |
|---|---|
| **jscalera1@aol.com** (Joe Scalera) | **Third report.** The sending address is on no order. A customer of the **same name** exists under a **different address** — **this was not disclosed to him**, and no order data was released. **Only the owner can look behind the accounts.** |

---

## 5. 🟦 Where the advertising claim might actually be

**Forty independent customer statements** now rest on a guarantee or durability
claim. **Six possible sources are identified. Five of them can only be opened by
the owner:**

1. **Klaviyo marketing emails of 27 Aug** — evidenced, quoted back by a
   customer: *"30-day money-back guarantee — Zero risk on your side."*
   **No condition attached.**
2. **Two advertorial pages** (`angelina-notes-dog-toys`,
   `sophie-dog-toy-counter`) — the API returns an **empty `body`**; built in a
   page builder. **Not readable from here.**
3. **A customer PDF** named *"Plushies Dog Toys Email"* (#7898) — **not opened.**
4. **A product image** said to carry *"with a replacement guarantee"* (#7168) —
   **images are not readable from here.**
5. **Facebook** — named independently by **#2852** and **#6311**.
   **Instagram** — named by **#6311**. An **embedded banner image (542 × 144)**
   sits in #6311's own email. **Not opened.**
6. **The product name itself** — **#7813** quotes *"Designed for Furry Friends
   Who Destroy Everything"*. **This one needs no owner access: it is the article
   name in the shop, and it was confirmed to her as such.**

**Two customers now speak of a _replacement_ guarantee** (#7168, #6311) — a
different promise from the 30-day money-back guarantee, and **not conflated with
it in any draft.**

---

## 6. Two corrections to my own earlier statements

- **`fulfillments.updatedAt == createdAt` does not prove non-delivery.** #2852
  carries that signature **and the goods demonstrably arrived** — the customer
  used and discarded them. The four flagged shipments (#8080, #6002, #8221,
  #6546) remain **notable**, but "stalled" was a stronger claim than the data
  supports.
- **The draft file holds 308 drafts, not the "124" carried in earlier logs.**
  That figure was a running count that had stopped being checked against the
  file. Measured values apply from here.

---

## 7. What no draft in this window contains

No refund promised · no replacement promised · no refusal · no returns address
invented · no chew-damage template · no legal assessment in either direction ·
no claim that a customer was already told something · no reconstruction of an
advertisement · no assertion about what a photo, PDF or image contains · no
photo demanded · no currency conversion · no referral to a carrier · no attempt
to talk anyone out of a review, chargeback, Klarna claim or Trading Standards
report · no order data to an address not on the order · no escalation marker in
any customer-facing text.
