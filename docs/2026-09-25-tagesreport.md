# Paw Friends — Daily Support Report

**Period covered:** 24 Sep 2026, 08:14 UTC → 25 Sep 2026, 08:14 UTC
**Sources:** `docs/2026-09-24-backlog-triage.md` (runs 11:20 → 23:20) and
`docs/2026-09-25-backlog-triage.md` (run 02:20)
**Compiled:** 25 Sep 2026, 08:15 UTC

---

## ⚠️ Two deviations to state up front

1. **No Gmail draft could be created for this report.** `create_draft` has been
   refused on this account since 21.08. The result of today's attempt is
   recorded at the end of this file.
2. **No customer reply has been sent by this bot, and none can be.** There is no
   send capability on the connected account. Every reply below exists only as
   text in `docs/entwuerfe-zum-kopieren.md` — **362 drafts, none of them in
   Gmail.**

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **12** |
| `Bot/Needs Approval` | **2** |
| `Bot/Draft Ready` | 0 |
| `Bot/No Action` | **1** |
| **Total customer cases** | **15** |

**Busiest 24 hours recorded so far.** By contrast, the period 23.09 20:20 →
24.09 10:20 produced **fourteen consecutive empty check-ins** — the volume
arrived in a single afternoon and evening.

---

## 2. Refunds actually issued

**None. £0.00 / $0.00 / A$0.00.** No case met rule 4. No cancellations executed
(`orderCancel` is blocked on this account).

---

## 3. 🟥 The two findings that matter most

### A. A batch of at least fifteen template replies went out from the shop account

Between **12:25 and 12:40 UTC on 24.09**, the Sent folder shows **at least
fifteen messages** to customers whose cases are logged here as escalated.
**That did not come from this session — this account cannot send.** I record
only what is in Sent and do not assert who sent them. Fifteen is a **floor**,
not a total: the message to #5310 only surfaced later, because thread previews
do not show every message.

What it produced within hours:

- **#8372 Kerri Forbey** received the chew-damage template a **third** time, for
  goods she has said three times she never unwrapped. She replied: *"I DID NOT
  USE the product. It is NOT DAMAGED."*
- **#7347 Jill Hibbs** was offered 30 % **again** after declining it on 22.09.
  She replied: *"No thank you. I would like to RETURN the toy."*
- **#8142 Wendy Price** — after four contacts and five days of silence, the
  template was the **first reply she has ever received.**
- **#8295 Ivan Griffen** — his deadline expired 23.09; the template arrived
  24.09. He now announces a Facebook post: *"a scam advert."*
- **#8080** was told again in writing that the order shipped from the
  international warehouse.

**⚠️ Consequence for the drafts:** several existing drafts tell a customer that
"the message of 22 September was not a decision." **Those are overtaken by the
24.09 send and must be checked before use.**

### B. Six offer letters name a percentage at the top and "the 30% refund" at the bottom

**#4940 Rena Barnes** caught it and said so: *"you are not clever thinking we
won't see the 30% further down the letters."*

Verified in the thread. Six offers were sent — **09.09, 11.09, 13.09, 15.09,
17.09, 19.09** — headline figures **30 % → 35 % → 40 % → 50 % → 60 % → 70 %**.
**Every one of them closes with the identical line:**

> *"Please let us know if you would like to accept **the 30% refund**, and we'll
> be happy to arrange it."*

**The draft confirms this openly and deliberately does not guess which of the
two figures was meant.** No seventh percentage offer was made.

**This is a defect in the template text itself and may affect other
recipients — it should be checked in the admin.**

### C. Also established: the template's guarantee condition is not in our own material

The #5310 thread preserves the **full text of both templates**. Both assert that
the 30-day guarantee *"applies to items returned unused and in their original
condition."* **That condition appears in none of the twelve product
descriptions and nowhere in our own marketing wording**, where the guarantee
appears **without any condition.** This is now documented, not inferred.

---

## 4. All 15 items, with recommended next steps

### `Bot/Escalated - Owner Attention` (12)

**⏰ #8781 — Glenn Yarbrough** (`glennyarbrough@gmail.com`) · **$37.69** ·
**most time-critical item in this report**
Ordered 24.09 at 15:20:59 UTC, asked to cancel at **15:42:15 — 21 minutes
later**, *"I made the order in error."* No reply went back, so he wrote again at
**20:29**, forwarding his own order confirmation. Shopify, re-checked at 21:20:
`UNFULFILLED`, `PAID`, `fulfillments` empty, `fulfillmentOrders: OPEN /
UNSUBMITTED`, `cancelledAt: null`, `updatedAt` unchanged since 15:21:13.
**Next step:** the window is still open and nothing has moved. Cancel and refund,
or tell him it will not happen. The draft deliberately does **not** claim the
order is cancelled, and does **not** repeat the #8669 error of claiming it
shipped.

**#4940 — Rena Barnes** (`renabarnes@hotmail.com`) · **£27.95** · eighth contact
The six contradictory offer letters (see 3B). Also: Trading Standards announced
11.09; *"I have screen prints of your advert"*; *"the law states that if the
advert was false advertising then 100% refund is due."* Ordered 07.08,
despatched **22.08 — fifteen days**. `refunds` is an empty list.
**Next step:** owner decision on the 100 % demand. Her legal argument goes over
unedited and without any assessment from support. **No offer was ever accepted,
so this is not an outstanding money promise.**

**#8142 — Wendy Price** · **£27.95** · fourth contact
*"What an absolutely ridiculous reply. It is not fit for purpose… Are we supposed
to look at the toy and not let the dog play with it?"*
**Next step:** the draft states plainly that she is right and answers her actual
question — there is no returns address. Bank claim and review are her decision
and nothing is conditional on them. Owner decision on the refund.

**#7347 — Jill Hibbs** · **£29.95** · declined the percentage twice
**Next step:** no third percentage offer. Her request — return and full refund
for the unused toy — goes over in her own words. **No figure is quoted for the
single unused item**: £29.95 is a two-for-one price and halving it would be a
guess.

**#8372 — Kerri Forbey** · **$96.89** · third wrong reply
**Next step:** the draft names the triple failure as ours, treats the goods as
unused, and warns her not to post an international parcel to an address that
does not exist. Also carries an undelivered e-book line.

**#8295 — Ivan Griffen** · **£27.95** · Facebook post announced
**Next step:** the expired deadline is acknowledged as our failure and the 24.09
template is stated not to have been a decision. No attempt to talk him out of
posting, no request to take anything down.

**#5310 — Heather Taylor** · **$38.47** · third contact
Quotes a specific claim: *"Your advertising says no dog has ever destroyed the
toy. That's false."* **Second customer in two days to quote that same
sentence** — after **#7440** on 23.09.
**Next step:** the draft separates what is checkable from what is not, and
explicitly does **not** claim the sentence does not exist — only that it was not
found where support can look.

**#2852 — John Conrad** · **$47.76**
*"The dog toys certainly did not last as describe they would."* Undelivered
e-book line flagged unprompted.

**#8079 — Nick Wright** · **£19.95** · first contact
*"I still haven't received my order… confirm when its coming or give me a
refund."* Despatched 08.09, **no tracking update in sixteen days.**
**Next step:** both halves of his question go over unchanged. No delivery date
quoted, no referral to the carrier.

**#8484 — Sue Quick** · **£19.95** · first contact
Asks one question: how to return. **Next step:** there is no returns address —
that is the first line of the draft, with a warning not to post anything. Eighth
customer in this position.

**#6893 — Eloise Newbrook** · **A$39.00** · **Australia**
Ordered 21.08 (local), despatched 02.09 — thirteen days — arrived 23.09:
**thirty-four days door to door.** Invokes the 30-day guarantee.
**Next step:** our **own published refund policy** has a section headed
*"Australia — Consumer Guarantees"* stating those rights are *"not limited by the
requirement that an item be unused or in its original packaging."* The draft
quotes it verbatim and **draws no conclusion from it** — that is the owner's
call. Nothing is asserted about whether the 30 days were met.

**#7208 — Nikki Shefferd** · **£27.95** · first contact, two threads merged
Invokes the 30-day guarantee and asks how to claim.
**Next step:** the draft neither claims the guarantee covers chew damage nor
claims it does not. Owner decision.

### `Bot/Needs Approval` (2)

**#8270 — Paul Thomas** (`paulthomas2407@gmail.com`) · **£19.95**
Complains about delivery time and quality but **makes no request at all**.
Ordered 30.08, despatched 08.09 — nine days, acknowledged openly as ours.
**Next step:** the draft offers rather than assumes — it does not convert his
report into a refund request. A goodwill decision is yours.

**Payment enquiry — `hephzibahogunbiyi96@gmail.com`** · no order
Message in full: subject *"Aw are u doing"*, body *"Aw do I pay pls"*.
**Deliberately not interpreted.** Shopify has **no order and no customer record**
for this address.
**Next step:** the draft asks which of three things she means, says openly that
nothing was found under her address without implying she did not order, and
warns her unprompted never to send card or bank details by email. **No payment
details were requested and no payment link was sent.**

### `Bot/No Action` (1)

**#7813 — Tasha Payne** — replied only *"Thank you for your response."* No
question, no request. Nothing unsolicited was written to her.
**⚠️ To check:** Shopify maps **#7813 to `tpayne743@gmail.com` / Tasha Payne**,
while the 18.09 log attributes #7813 to Maria Carter. **I am not deciding which
is right — the earlier entry may be my own error.**

---

## 5. Standing items that did not move

### ⏰ Still time-critical
- **#8669 Chad Lovell — $38.19.** Told 22.09 the order *"has already been
  shipped."* Shopify says otherwise: `UNFULFILLED`, `fulfillments` empty,
  `fulfillmentOrders: OPEN / UNSUBMITTED`, `cancelledAt: null`. **The refusal
  has no basis in the record.**
- **#8605 — £27.95.** Cancellation window likewise still open.
- **#8781** — see above.

### 🔴 Ten promises of money, none executed
#4812 (£86.89 / $116.92) · **#4919 (£11.18, confirmed "processed" twice —
08.09 and word-for-word again 17.09, `refunds` empty)** · #7884 ($8.30) ·
#7179 ($24.32) · #6546 ($41.55) · #6583 (£30.54, promise sent twice) · #5148 ·
#6259 (Trading Standards, deadline expired) · #4998 · #7060.

### ⛔ Eight customers holding goods they cannot return
#6254, #8312, #7347, #8372, #7479, #7048, #8456, **#8484**. **#7048 has
announced she is posting a parcel to a "UK department" that does not exist.**

### ⚠️ Structural
- **Sixty independent customer statements about the advertising.**
- **Nine orders carry an undelivered e-book line.**
- **Five shipments show no tracking update since despatch:** #8080 and #8079
  (16 days each), #8483, #8432, #8476 (10 days each).
- **Five customers in three days forwarded their own mail or wrote again because
  nothing came back:** #7041, #8142, #3387, #7608, #8781.
- **#2894 — two months since a written replacement promise**, no replacement, no
  refund, no reply. **#3089 unchanged.**

---

## 6. Recommended priority today

1. **#8781** — 21-minute cancellation, asked twice, record untouched. Act before
   anything ships.
2. **#8669 and #8605** — same situation, older, and #8669's refusal was
   ungrounded.
3. **#4919** — issue the £11.18 or say plainly it will not be issued. Two
   written "processed" confirmations, seventeen days.
4. **Check the offer template** — six letters contradict themselves; other
   recipients may have had the same.
5. **#7048** — stop the parcel before she posts it.
6. **#2894** — send or refund.
7. **Unblock sending**, or these 362 drafts stay text in a repository.

---

## Appendix — create_draft attempt

Attempt #23 was prepared while compiling this report but **did not complete** —
the call was cut off before it ran, exactly as on 24.09. **It is neither a
success nor a refusal, and no Gmail draft of this report exists.** The report is
delivered in chat and in this repository instead.
