# Paw Friends — Daily Support Report

**Window:** 16.09.2026 08:14 UTC → 17.09.2026 08:14 UTC
**Source:** `docs/2026-09-16-backlog-triage.md` (runs 09:20–22:20) and
`docs/2026-09-17-backlog-triage.md` (runs 00:20–07:20)
**Branch:** `claude/paw-friends-support-bot-fa27s0`

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **21** |
| `Bot/Needs Approval` | **8** |
| `Bot/Draft Ready` | **1** |
| **Total cases handled** | **30** |

Drafts written in the window: **28**, of which **8 are second, third or fourth
versions** replacing a draft that a template denial overtook before it could be
sent.

---

## 2. Refunds actually issued

**None. Zero refunds were issued.**

No confirmed rule-4 wrong-item case. `refundCreate` and `orderCancel` remain
blocked. **No email was sent to any customer.** **No write operation of any
kind was performed in Shopify** — not even the address correction on #8548,
where it would plainly have helped the customer.

---

## 3. Three customers are waiting for money nobody released

This is the most serious pattern of the window, and all three expectations were
created by **our own replies**, not by the customers.

| # | Customer | What happened | Next step |
|---|---|---|---|
| **#5148** | **Trudi Wright** | Told on **07.09.** and again on **16.09.** that a **50% refund "has been processed"**. Shopify shows `totalRefundedSet 0.00 £`, `refunds: []`, status `PAID`. *Not established that no money moved* — a payment through another route would not appear here. **Established: nothing is recorded, and the order reads as paid in full.** Also: on **25.08.** she was told "the relevant team" would send her the returns address. **That was 23 days ago.** | **Check the payment records. Then either execute the 13.98 £ or show her when it left.** A third assurance is not an option. |
| **#7547** | **Luke Prior** | Asked for a refund on **11.09., before delivery**, because the wait had become unacceptable. Answered on the 13th and the 15th — **both times about delivery only**. His refund question went past us **three times**. He now writes *"Waiting on a refund please."* | **Decide it.** It is a pre-delivery cancellation, **not** chew damage. 19,95 £. |
| **#7610** | **Vicky Blow** | Refund requested **13.09.**, answered on the 15th with a **policy statement, not a decision**. Third contact today. **She is the customer who has already published a Trustpilot review.** | **Decide it.** 19,95 £. Do **not** ask her to alter the review; nothing was made conditional on it. |

**In all three drafts I have told the customer plainly that nothing is
arranged** — so they stop waiting — **and in none of them have I issued a
refusal.**

---

## 4. Two errors provable from our own records

### 4.1 #7989 Karen Reynolds — a change we confirmed in writing was never made

| Date | Who | What |
|---|---|---|
| 28.08. | Reynolds | *"Can I please confirm my order is for **1x Hippo and 1x Frog**."* |
| **29.08.** | **Us** | *"I can confirm that your order request is for: **1 × Hippo, 1 × Frog**. We'll make sure your requested selection is noted for your order."* |
| **17.09.** | Reynolds | *"**I only got the Hippo, where is the frog as I payed for both.**"* |

**The order record still reads `quantity: 2, variantTitle: "hippo"`.** The
confirmed change was never carried out, and she had no way of knowing. She also
reports receiving **one** item where the record shows **two** despatched.

**Nothing was triggered from here** — no refund, no reshipment, no order edit.
What was in the box cannot be established from this connection; the photo was
not opened, and **she was not told she must have miscounted.** This is **not** a
confirmed rule-4 case, but it is **the first shop error provable from our own
sent mail**. She ships to **Australia**.

### 4.2 #5682 — the order confirmation renders a duplicate line

Brian Carr's confirmation lists five Plushies; the order holds four. The
email's own arithmetic settles it: the line prices sum to **$94.64** while the
stated subtotal is **$75.71**, which is exactly four toys. **The customer was
neither short-shipped nor overcharged — the email duplicates a line.** He was
not told, because he did not ask and suffered no loss. **Scope unknown**: sent
confirmations are not in this mailbox.

---

## 5. The advertising question is now three-sourced

**"Indestructible" appears on none of the nine product pages** — the whole
catalogue is checked — and **eighteen customers have now used the word.** Three
have named a source outside the product pages:

- **#7698 Amy Burnell** — Facebook reviews
- **#7312 Ricky Gaugano** — a **promotional video**, *"you will refund me when my dog destroys your toy"*
- **John Keefauver (#6205)** — *"my refund **as promised in your Facebook marketing**"*

**Two of the three describe a promised refund**, not merely durability. **None
of it is visible from this connection.** This remains the single most
answerable open question, and only you can answer it.

**Meanwhile, four failures occurred at exactly the feature the copy
advertises** — three at the rope (*"Rope-reinforced construction for extra
durability"*) and, new this window, **#7378 Gary Green at the seams**, on
Fluffys, whose page says *"Triple-stitched at every seam"* three times.

---

## 6. Escalated — Owner Attention (21)

**Deadlines:** **#7699 Lorraine Sale — today.** #7479 — **21.09.**, then
regulators. #7323 — **22.09.**, then ASA and Trading Standards. #1998 and #4975
— 22.09. **#6877 and Stephen Board expired on 15.09. with no visible reply.**

**#7479 Richard Bellamy — third contact, and the one you can half-answer
today.** His address question **is** answerable: the trading address is
published in your own Terms of Service. His actual question is not — he holds
an **unopened item in original packaging**, which is precisely the condition our
denials cite, and there is no returns route to give him.

**Unused goods, refund blocked only by the missing returns address (10):**
#7479, #7030, #7660, #7347, #5973, #6254, #6528, #7292, **#8372 Kerri Forbey**
(the whole order unused, reported on the day of delivery), **#7119 Susan
McGee** (one of two untouched).

**Disputed advertising (14):** #6384, #6806, #7072, #6804, #6205, #7378, #6233,
#8133, #7192, #7625, #7119, #5880, #7525, #7114.

**#7072 Jane Bromirski** put the sharpest objection of the window: *"Am I
supposed to leave it in the packaging and somehow determine that it is going to
get destroyed in 31 minutes?"* — **the third independent formulation** after
#7001 and #6528, from three countries. She also announced a payment dispute.

**#7525 Carol Garvey — fifth contact**, and a new observation nobody had made:
*"every response I have received has come directly from you… the company may
not be as large or established as it is presented to be."* **I neither
confirmed nor denied it and invented no story about the company.** She is also
the customer who confirmed from outside that the site has no returns
information — **she was told plainly that she had not missed anything.**

---

## 7. Needs Approval (8)

| # | Customer | What is needed |
|---|---|---|
| **⏰ #8548** | Enedino Calleros | **Wrong delivery address, order still `UNFULFILLED`.** Correctable **only until dispatch**. I do not edit orders — this needs you, in the admin. |
| **🔧 #8588** | Darren Law | **Checkout fault reported 20 minutes after ordering**: a free item added automatically without the amount coming off, so he removed it. **Not verifiable from here.** The first signal in this whole log from a *buying* rather than a disappointed customer — it costs revenue every time nobody reports it. |
| **#7950**, **#6233**, **#8377**, **#7215**, **#5682** | — | Chew damage, **none of them asked for anything.** Yes or no on a refund. |
| **#7160** | Kim Maguire | Invoked the guarantee, asked for the process. **She paid a voluntary tip** (separate line) — don't overlook it in any refund. |

## 8. Draft Ready (1)

**#8195 Georgia Caccavale** — status query, answerable in full from ship date,
carrier, tracking number and link.

---

## 9. Standing blockers

1. **No returns address. 36 days. Twenty questions about it in this window
   alone**, none answerable. Every affected draft warns the customer **not** to
   post anything.
2. **1,170 of 7,561 orders are `PARTIALLY_FULFILLED`.** Five surfaced here by
   accident — #7255, #6254, #6528, #8372, #5880 — and in each the outstanding
   line is the paid digital guide. **None of the five knew.**
3. **Thirteen currency mismatches** (GBP in Shopify, USD or AUD on the
   confirmation). Not bridged.
4. **`create_draft` is blocked** — 21 consecutive failures. **All drafts live in
   the repo, none in Gmail**, which is also why handled threads keep resurfacing
   unread.

---

## 10. One operational note

At 22:20 the local checkout had been rolled back to the 15.09. state, so the
push was rejected. **It was not forced.** Had it gone through it would have
deleted 4,595 lines — the entire day. The local copy was reset to `origin`,
nothing was missing there, and only that run's two additions were re-applied.
