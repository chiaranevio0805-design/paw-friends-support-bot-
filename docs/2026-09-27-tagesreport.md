# Paw Friends — Daily Support Report

**Period covered:** 26 Sep 2026, 08:14 UTC → 27 Sep 2026, 08:14 UTC
**Sources:** `docs/2026-09-26-backlog-triage.md` (runs 08:20 → 23:20) and
`docs/2026-09-27-backlog-triage.md` (runs 00:20 → 07:20)
**Compiled:** 27 Sep 2026, 08:15 UTC

---

## ⚠️ Two deviations to state up front

1. **No Gmail draft could be created for this report.** `create_draft` has
   been refused on this account since 21.08. Attempts **#22 (24.09) and #23
   (25.09) were both cut off before they ran** — neither a success nor a
   refusal. Today's attempt is recorded in the appendix.
2. **No customer reply has been sent by this bot, and none can be.** There is
   no send capability on the connected account. Every reply below exists only
   as text in `docs/entwuerfe-zum-kopieren.md` — **381 drafts, none of them in
   Gmail.**

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **3** |
| `Bot/Needs Approval` | **1** |
| `Bot/Draft Ready` | 0 |
| `Bot/No Action` | 0 |
| **Total customer cases** | **4** |

**Four new drafts were written in this period** (377 → 381).

**Plus two items that are not customer cases** and are covered in section 3.

**The quietest 24 hours since 23.09.** Between 12:20 and 23:20 UTC on 26.09
there were **nine consecutive empty check-ins**; the only traffic came in two
short bursts.

---

## 2. Refunds actually issued

**None. £0.00 / $0.00 / A$0.00.** No case met rule 4 (confirmed wrong item).
No cancellations executed — `orderCancel` and `refundCreate` remain blocked on
this account.

---

## 3. 🟨 Two non-customer items the owner should see

### A. Google security alert on the support account — 26.09, 10:23 UTC

Sender `no-reply@accounts.google.com`, subject *"Sicherheitswarnung"*:

> *"Neuer Passkey wurde Ihrem Konto hinzugefügt — support.pawfriends.uk@gmail.com"*

**I cannot determine from here whether the owner did this.** **Nothing was
clicked, nothing confirmed, nothing changed, and no link in the mail was
opened.** **If the owner did not create that passkey, this needs checking
immediately** — it is the account all customer traffic runs through. **This is
the single most urgent item in today's report, ahead of the customer cases.**

### B. Unsolicited sales approach — 26.09, 20:44 UTC

`permitshopify@gmail.com`, signed *"CJ Dropshipping"*, subject *"Pawfriends Uk
Feedback?"*, offering a free store audit.

The address looks official because of `permitshopify@`, but it is a Gmail
address; **Shopify does not write from Gmail addresses.** **Second message of
this kind in this mailbox**, after `shopifystoreregulatory.center@gmail.com`
on 06.09, which asked for shop and order data under a regulatory pretext.

**Not answered, nothing clicked, no data released.** **I do not assert that it
is fraudulent** — it is unsolicited advertising, and whether to engage is the
owner's call.

---

## 4. All 4 customer items, with recommended next steps

### `Bot/Escalated - Owner Attention` (3)

**#8431 — Sarah Williams** (`slw72@tpg.com.au`) · **A$53.53** · **Australia** ·
first contact
*"Could you please advise how I can proceed with a refund under your 30-Day
Guarantee?"* Ordered 09.09, despatched 14.09, **received 26.09 by her
account**. The donkey was destroyed in about ten minutes; **the elephant is
unopened** because she is now reluctant to give it to the dog.
**Next step:** owner decision on the guarantee claim. **The draft does not say
whether the guarantee covers this, in either direction, and it does not quote
or calculate any deadline** — neither 30 days from purchase nor from receipt.
**Third Australian case** after #6893 and #8228; our own published *"Australia
— Consumer Guarantees"* section is quoted verbatim **with no interpretation.**
She quoted the product title *"Plushies – Designed for Furry Friends Who
Destroy Everything"* **accurately — that is confirmed to her as our own
wording**, without any inference about durability or about her claim. Photos,
proof of purchase and "any other information" were **expressly declined** so
nothing becomes a condition. Her phone number is not used or mentioned; her
"$50+" is not reconciled against the record; her delivery date is recorded
rather than contradicted.

**#7559 — Rod Smith** (`smithrdrck@aol.com`) · **£19.95** · fourth contact
*"We REALLY love Donkey… HOWEVER he is not indestructible… I am happy to
accept a replacement rather than a refund… I DO NOT want to leave any kind of
negative review but for £20 I did believe your assurances."* Ordered 24.08,
despatched 03.09 — ten days.
**Next step:** he asks for a **replacement**, not money. ⚠️ **The draft does
not promise one**, and says so plainly — **#2894 has been waiting two months
for a replacement promised in writing on 24.07 that never shipped**, and a
second such promise is not made from here. **No refund is pushed on him**; he
said which he wanted. **Nothing is tied to his remark about not leaving a
review**, in either direction. His phone number and his "£20" are left alone.

**#8574 — John Husk** (`husky0877@googlemail.com`) · **£19.95** · first contact
*"One evening and our miniature Dachshund has destroyed the rope and ripped
the label off… Not as described, thought it was supposed to be tough!!"*
Ordered 16.09, despatched 17.09 — one day, no delay.
**Next step:** ⚠️ **address mismatch.** He writes from `…@googlemail.com`; the
order record carries `…@gmail.com`. The name matches exactly. **I did not
decide they are the same address, and no order details were released to the
address that does not match** — the draft explains why openly **without
implying he is not the customer**. **He makes no specific request**, so the
draft offers rather than assumes. Nothing inferred from his dog's breed or
size.

### `Bot/Needs Approval` (1)

**#8568 — Allen Irvin** (`allenirvin@aol.com`) · **$38.41** · US · first
contact
**The entire message is in the subject line**; the body reads only "Sent from
my Galaxy":
> *"How do I get my money back. My 42 lb pit bull terrier destroyed it in 2
> minutes."*
Ordered 16.09, despatched 17.09 — one day, no delay.
**Next step:** he asks a direct question and the draft answers it directly —
**there is no returns process and no returns address**, with a warning not to
post anything from Florida. ⚠️ **Nothing is inferred from his dog's breed or
weight, and the draft tells him so**: *"You mentioned them; I am not going to
use them."* ⚠️ **He writes "it" — singular — but the order has two toys. The
draft does not assume the second is unused; it asks.** He is therefore **not**
counted among the customers holding unreturnable goods. He does not mention
the advertising, so **nothing is asserted about it and he is not counted as an
advertising statement.** No escalation trigger is met.

---

## 5. Standing items that did not move

### ⏰ Still time-critical
- **#8781 Glenn Yarbrough — $37.69.** **Asked to cancel three times** (24.09
  15:42 and 20:29, 25.09 22:41), **never answered.** Record unchanged since
  **fourteen seconds after the order**: `UNFULFILLED`, `PAID`, `fulfillments`
  empty, `fulfillmentOrders: OPEN / UNSUBMITTED`, `cancelledAt: null`.
  **The window is demonstrably still open.**
- **#8669 Chad Lovell — $38.19.** Refused 22.09 because the order *"has
  already been shipped."* **The record does not support that.**
- **#8605 — £27.95.** Cancellation window likewise still open.

### 🔴 Eleven promises of money, none executed
#4812 (£86.89 / $116.92) · #4919 (£11.18) · #7884 ($8.30) · #7179 ($24.32) ·
#6546 ($41.55) · #6583 (£30.54) · **#5148 (£13.98, "processed" FOUR times —
07./16./18./22.09., `refunds` empty)** · #6259 (Trading Standards, deadline
expired) · #4998 · #7060 · **#5973 (£14.98, "processed" 17.09, `refunds`
empty).**

### 🟦 #5148 — the returns address promised on 25.08 that never existed
> *"…they will provide you with the return address and further instructions…
> Please do not send the items back until you receive the official return
> details."*

**It never came. She kept both toys unopened for a month.** **This should be
checked in the admin — other recipients may have had the same sentence.**

### ⛔ Thirteen customers holding goods they cannot return
#6254, #8312, #7347, #8372, #7479, #7048, #8456, #8484, #8577, #5973, #7034,
#5148, **#8431**. **#7048 announced on 23.09 that she is posting a parcel to a
"UK department" that does not exist and has had no reply in four days.**

### ⚠️ Structural
- **Seventy-one independent customer statements about the advertising**
  (68 → 71 in this period). **#8568 is deliberately not counted** — he did not
  mention it.
- **Eleven orders carry an undelivered e-book line.**
- **Five shipments show no tracking update since despatch:** #8080, #8079,
  #8483, #8432, #8476.
- **Second-inbox blind spot:** `paw-friends.uk@paw-friends.uk` receives
  customer mail this mailbox never sees; **#7401 is the sixth customer
  affected.**
- **Three Australian cases now** — #6893, #8228, **#8431**. The shop's own
  AU section is quoted verbatim in all three drafts and **interpreted in
  none.**
- **#2894 — two months since a written replacement promise**, no replacement,
  no refund, no reply. **#3089 unchanged.**

---

## 6. Recommended priority today

1. **The passkey alert.** Confirm you added it. If not, secure the account
   before anything else on this list.
2. **#8781** — three requests, record untouched, window still open.
3. **#5148** — four written confirmations of a refund that does not exist.
   **And check who else got the 25.08 returns-address promise.**
4. **#8669 and #8605** — same cancellation situation, older.
5. **#8431** — decide the guarantee claim; the unopened elephant is a
   separate question from the destroyed donkey.
6. **#7559** — he asked for a replacement and would accept one. **Do not
   promise one unless it will actually ship** (see #2894).
7. **#7048** — stop the parcel. Four days unanswered.
8. **Unblock sending**, or these 381 drafts stay text in a repository.

---

## Appendix — create_draft attempt

Attempt **#25** was made while compiling this report. As with #22, #23 and
#24, **no Gmail draft of this report exists**; the report is delivered in chat
and in this repository instead.
