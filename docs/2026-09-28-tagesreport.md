# Paw Friends — Daily Support Report

**Period covered:** 27 Sep 2026, 08:14 UTC → 28 Sep 2026, 08:14 UTC
**Sources:** `docs/2026-09-27-backlog-triage.md` (runs 08:20 → 23:20) and
`docs/2026-09-28-backlog-triage.md` (runs 00:20 → 07:20)
**Compiled:** 28 Sep 2026, 08:15 UTC

---

## ⚠️ Two deviations to state up front

1. **No Gmail draft could be created for this report.** `create_draft` has
   been refused on this account since 21.08. Attempts **#22 (24.09) and #23
   (25.09) were cut off before they ran** — neither a success nor a refusal.
2. **No customer reply has been sent by this bot, and none can be.** Every
   reply exists only as text in `docs/entwuerfe-zum-kopieren.md` — **386
   drafts, none of them in Gmail.** **Three are marked superseded** (#8577,
   #7898 of 21.09, #8568 of 27.09 03:20) **and must not be sent alongside
   their replacements.**

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **4** |
| `Bot/Needs Approval` | **1** |
| `Bot/Draft Ready` | 0 |
| `Bot/No Action` | 0 |
| **Total customer cases** | **5** |

**Five new drafts** (381 → 386). One of them replaces an earlier draft rather
than adding a new case: **#8568 was re-classified from `Needs Approval` to
`Escalated` inside this window**, because he wrote a second time and had had
no reply to either message.

---

## 2. Refunds actually issued

**None. £0.00 / $0.00 / A$0.00.** No case met rule 4. No cancellations
executed — `orderCancel` and `refundCreate` remain blocked.

---

## 3. 🟥 The finding that outranks the customer cases

### Two orders in one morning could not be retrieved from Shopify

**#7626 is the serious one.** The customer replied to a **genuine Shopify
shipping confirmation** (`store+105151824221@t.shopifyemail.com`, 03.09),
which quotes the order number, both line items and the 4PX tracking number in
full. **Five different queries all returned nothing:**

| Query | Result |
|---|---|
| `orders(query:"name:7626")` | empty |
| `orders(query:"name:#7626")` | empty |
| `orders(query:"7626")` | empty |
| `orders(query:"4PX3003124889701CN")` | empty |
| `orders(query:"email:tonisfurryfriends@yahoo.com")` | empty |

**The same query form has worked reliably today and on every previous day**
(#8574, #7559, #8431, #4055, #7898 and others). **I am not interpreting why
#7626 cannot be retrieved — I am only recording it.** **It needs checking in
the admin.**

**The second case** is `hud@hildebrandt.com.au`, who has no order number to
give; there nothing was found either, but the missing number is a sufficient
explanation on its own.

**Consequence I applied:** the draft for **#7626 deliberately contains no
order-record data at all** — no amounts, no dates, and **not even the usual
line "nothing refunded to date."** **I do not state what I could not verify.**
And she is **not** told her order cannot be found: she produced her own
shipping confirmation, and the problem is on our side.

---

## 4. All 5 customer items, with recommended next steps

### `Bot/Escalated - Owner Attention` (4)

**🔴 #4055 — Kimberley Shenton** (`kim.shenton@me.com`) · **£19.95** ·
**£11.97 owed**
*"I've still received no refund."* 60 % accepted 17.09, confirmed
*"processed to your original payment method"* on **19.09**;
`totalRefundedSet` **0.00 £**, `refunds` **empty**. **Eight days.**
**Next step:** pay it or say plainly it will not be paid. **The draft makes no
second promise and does not claim the money is with her bank.** Her thread
produced **three findings that go beyond her case — see section 5.**

**⛔ #7898 — Tammy Brentlinger** (`pitbulladvocate@live.com`) · **$42.61** ·
second contact
*"I only bought them because of the 30 day guarantee… You won't be getting a
good review from me."* She received the chew-damage refusal on **24.09** as
part of the batch send.
**Next step:** owner decision. The draft tells her the checkable truth — **the
condition the refusal relied on ("returned unused and in their original
condition") appears in none of the twelve product descriptions and nowhere in
our own marketing**, where the guarantee appears unconditioned. **It does not
claim the guarantee covers chew damage, and does not claim it does not.** **It
does not pretend the 24.09 refusal was withdrawn or "not a decision" — it was
sent.** **Nothing is tied to her review.** Her 21.09 draft is marked
superseded.

**⛔ #8568 — Allen Irvin** (`allenirvin@aol.com`) · **$38.41** · second
contact, second thread
*"How do I get a refund. This is the second one that took 5 minutes."*
**Eighteen and a half hours after his first message, with no reply to
either.**
**Next step:** ⚠️ **He answered the question my earlier draft had asked** —
the second toy is **not** unopened; it went the same way. **Not assuming that
was right, and it is now established rather than guessed.** **Re-classified to
Escalated** on repeat-contact-without-reply. The merged draft says openly that
he wrote twice and heard nothing, does not claim he was ever answered, and
does not ask him to write a third time. **Nothing inferred from his dog's
breed or weight — and the draft tells him so.**

**⛔ `hud@hildebrandt.com.au`** · **Australia** · first contact · **no order
found**
*"I've given my Dog 3 out of 4 products within a couple days… you can work out
where we progress from here."*
**Next step:** **he names no order number and Shopify finds nothing under his
address or name.** **The draft does not suggest he did not order** — it says
openly what was searched, names the second-inbox blind spot
(`paw-friends.uk@paw-friends.uk`) and a possible different order address, and
asks for the number. **You can find him in the admin; I cannot from here.**
He makes **no request**, so the draft offers rather than assumes. **Fourth
Australian case** — our own *"Australia — Consumer Guarantees"* section is
**mentioned so he can read it himself, with no interpretation and no promise
derived from it.** **The fourth, ungiven toy is noted without telling him what
to do with it.**

### `Bot/Needs Approval` (1)

**#7626 — `tonisfurryfriends@yahoo.com`** · first contact · **order not
retrievable**
*"Your product is crap. My dogs ate them in 15 minutes."*
**Next step:** **she makes no request at all**, so the draft offers rather
than assumes. **No chew-damage template, and no statement about quality in
either direction — not even an agreeing one.** She does not mention the
advertising, so **nothing is asserted about it and she is not counted as an
advertising statement.** **No order data in the draft** (see section 3). No
escalation trigger met.

---

## 5. 🟦 Three findings from the #4055 thread that go beyond her case

**A. The returns address that never existed was promised to at least two
customers.** **#5148 on 25.08** and **#4055 on 23.08** received the identical
sentence:

> *"…they will provide you with the return address and further instructions…"*

**Yesterday this was "other recipients may have had the same." It is now
established: at least two, documented.** **This is a template defect and
should be checked in the admin.**

**B. The 60/50 contradiction is not confined to #4940.** The offer sent to
**#4055 on 17.09 at 10:37:14** headed with **60 %** and closed with *"the 50%
partial refund"* — **the same construction as in Rena Barnes's six letters.**
Here it was caught: **eleven seconds later** the corrected version went out.
**That makes it a template defect rather than a one-off.**

**C. #4055 was told her order could not be located — after three offers had
been made against it.** On **15.09**: *"we're currently unable to locate an
order under the details provided."* She said so herself: *"I'm struggling to
understand how it's been located before… and now it can't be located again."*
**Shopify finds #4055 immediately.** **The draft corrects this unprompted.**

---

## 6. Standing items that did not move

### 🟨 Still the most urgent item overall
**The Google security alert of 26.09, 10:23 UTC** — a new passkey added to
`support.pawfriends.uk@gmail.com`. **Unverifiable from here and still
unresolved.** It is the account all customer traffic runs through.

### ⏰ Still time-critical
- **#8781 — $37.69.** Three cancellation requests, never answered, record
  unchanged since **fourteen seconds after the order.**
- **#8669 — $38.19.** The 22.09 refusal (*"already been shipped"*) has no
  basis in the record.
- **#8605 — £27.95.**

### 🔴 Eleven promises of money, none executed — **£466.97 in quantified GBP**
#4812 · #4919 · #7884 · #7179 · #6546 · #6583 · **#5148 (£13.98, confirmed
four times)** · #6259 · #4998 · #7060 · **#5973 (£14.98)** — plus **#4055
(£11.97), newly quantified.**

### ⛔ Thirteen customers holding goods they cannot return
**#7048 has now had no reply for five days** about the parcel she announced
she would send to a "UK department" that does not exist.

### ⚠️ Structural
- **Seventy-one independent customer statements about the advertising** —
  **unchanged**; #7626, #8568 and `hud@…` do not mention it and are
  deliberately not counted, and #4055 and #7898 were counted earlier.
- **Four Australian cases now** — #6893, #8228, #8431, `hud@…`. The AU section
  is quoted or named in all four drafts and **interpreted in none.**
- **The batch send of 24.09 is still producing consequences** — #7898 is the
  latest.
- **Second-inbox blind spot** unchanged.

---

## 7. Recommended priority today

1. **The passkey alert.** Confirm it was you; if not, secure the account.
2. **#7626 in the admin** — an order documented by our own shipping
   confirmation that five queries cannot retrieve.
3. **#8781** — three requests, record untouched, window still open.
4. **#4055 and #5148** — money confirmed in writing, `refunds` empty.
   **And check who else received the 23.08/25.08 returns-address sentence.**
5. **Check the offer template** — the 60/50 defect now has two documented
   occurrences.
6. **#8669 and #8605.**
7. **#7048** — five days; stop the parcel.
8. **Unblock sending**, or these 386 drafts stay text in a repository.

---

## Appendix — create_draft attempt

Attempt **#26** was made while compiling this report. As with #22 to #25,
**no Gmail draft of this report exists**; it is delivered in chat and in this
repository instead.
