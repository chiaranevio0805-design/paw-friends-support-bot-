# Paw Friends — Daily Support Report

**Period covered:** 25 Sep 2026, 08:14 UTC → 26 Sep 2026, 08:14 UTC
**Sources:** `docs/2026-09-25-backlog-triage.md` (runs 08:20 → 23:20) and
`docs/2026-09-26-backlog-triage.md` (runs 00:20 → 07:20)
**Compiled:** 26 Sep 2026, 08:15 UTC

---

## ⚠️ Two deviations to state up front

1. **No Gmail draft could be created for this report.** `create_draft` has been
   refused on this account since 21.08. Attempts **#22 (24.09) and #23 (25.09)
   were both cut off before they ran** — neither a success nor a refusal.
   Today's attempt is recorded in the appendix.
2. **No customer reply has been sent by this bot, and none can be.** There is
   no send capability on the connected account. Every reply below exists only
   as text in `docs/entwuerfe-zum-kopieren.md` — **377 drafts, none of them in
   Gmail.** One of them (the first #8577 draft) is superseded and must not be
   sent in addition to its replacement.

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **12** |
| `Bot/Needs Approval` | **2** |
| `Bot/Draft Ready` | 0 |
| `Bot/No Action` | 0 |
| **Total customer cases** | **14** |

**Fifteen new drafts were written in this period** (362 → 377); #8577 accounts
for two of them because she opened a second thread, and the earlier one is
marked replaced.

**A note on the window:** **#8228** wrote at **08:07 UTC on 25.09 — seven
minutes before the last report's cut-off** — but was triaged in the 08:20 run,
after that report was compiled. He is therefore listed here rather than lost
between the two.

---

## 2. Refunds actually issued

**None. £0.00 / $0.00 / A$0.00.** No case met rule 4 (confirmed wrong item).
No cancellations executed — `orderCancel` and `refundCreate` remain blocked on
this account.

---

## 3. 🟥 The three findings that matter most

### A. #5148 — the 50 % was confirmed as "processed" **four** times, not twice

**This corrects my own earlier log entry.** The full thread recovered at 07:20
today shows the 50 % partial refund confirmed in writing on **7 September, 16
September, 18 September and 22 September**. Shopify: `totalRefundedSet`
**0.00 £**, `refunds` an **empty list**. Her message this morning:

> *"It has been 3 weeks now and still no payment. I am resigned to the fact
> that no payment is ever going to be made."*

**The draft does not make a fifth promise.** It states plainly that the refund
does not exist in the record.

### B. #5148 was promised a returns address in writing on 25 August — there is none

> *"…they will provide you with the return address and further instructions…
> **Please do not send the items back until you receive the official return
> details.**"*

**It never came. She kept both toys unopened for a month waiting for it.**
**This should be checked in the admin — other recipients may have had the same
sentence.**

### C. #5036 — a delivery claim that our own record does not support

She was told on 08.09 that the parcel was *"delivered to a safe place on 1
September at 12:54."* She checked the property and the neighbours and replied
*"Rest assured we do not have the items."* **Our own Shopify record shows no
update at all since despatch on 22.08** (`updatedAt == createdAt`). Three
emails since 15.09 went unanswered; **she has already left a review.**

**The draft adopts neither statement.** Both are set side by side and go to the
owner as they stand.

---

## 4. All 14 items, with recommended next steps

### `Bot/Escalated - Owner Attention` (12)

**⏰⏰ #8781 — Glenn Yarbrough** (`glennyarbrough@gmail.com`) · **$37.69** ·
**still the single most urgent item**
Third contact, 25.09 22:41: *"Were you all able to cancel this order?"* He
asked at 15:42 (**21 minutes after ordering**), again at 20:29, and now a third
time — **thirty-one hours, no reply to any of them.** Shopify, checked a third
time: `UNFULFILLED`, `PAID`, `fulfillments` empty, `fulfillmentOrders: OPEN /
UNSUBMITTED`, `cancelledAt: null`, `updatedAt` still **2026-09-24T15:21:13Z —
fourteen seconds after the order.**
**Next step:** nothing has shipped and nothing has been done. Cancel and refund,
or tell him it will not happen. The draft answers his question with a plain
**no** and does not claim the order is cancelled, in progress, or shipped.

**🔴🔴 #5148 — Trudi Wright** (`truditrotter67@icloud.com`) · **£27.95**
Four written "processed" confirmations, `refunds` empty, and a returns address
promised on 25.08 that does not exist (see 3A and 3B).
**Next step:** issue the 50 % or say plainly it will not be issued. **Do not
send a fifth confirmation.** Check whether the 25.08 returns-address wording
went to anyone else.

**🔴 #5973 — Stephen Cooil** (`stevecooil@me.com`) · **£29.95** · eleventh
unexecuted promise
50 % confirmed "processed" on 17.09; `totalRefundedSet` 0.00 £, `refunds`
empty. *"I've not seen any sign of my refund yet."* His question of **11.09** —
how to return the one **unused** toy — has been open for fourteen days.
**Next step:** execute or retract. The draft names no percentage figure, only
the order total and the fact that 0.00 £ is refunded. His statements about item
size and about the testimonials are passed on **without any assertion either
way.** He has mentioned going to the media; no attempt was made to talk him out
of it.

**⛔🔴 #5036 — Lynette Lumley** (`lynette_lumley@hotmail.com`) · **£27.95** ·
sixth contact, review already left
*"I hope others look at the reviews, including the one i have left, and you
never get another sale. Enjoy my £30."*
**Next step:** owner decision. See 3C. **She was not asked to change or remove
the review, and nothing is conditional on it.** Her figure of "£30" was **not
corrected** against the order record — both go to you side by side.

**⛔ #7048 — Josephine Carr** (`jocarr247@yahoo.com`) · **£27.95** · fifth
contact
*"PLEASE LET ME KNOW ASAP WHEN YOU WILL BE REFUNDING ME AS I DONT WISH TO KEEP
THE PRODUCTS."* Her message of 23.09 — announcing she would post the goods to a
"UK department" — **is still unanswered after three days, so the warning has
still not reached her.**
**Next step:** the warning is the first line of the draft. **Stop the parcel.**
No third percentage offer (30 % and 40 % already declined), and no date quoted,
because none can be.

**⛔ #8312 — Paul Beaver** (`mrpbeaver@gmail.com`) · **£27.95** · third request
to return
*"As I have already stated, I want to return the item for a full refund…
Please confirm the process."* He received the 30 % template on 24.09 as part of
the batch send.
**Next step:** the draft confirms honestly that there is no process and no
returns address. No further percentage offer, **no share of the bundle price
estimated.**

**⛔ #8577 — Shirley McCutcheon** (`shirls_mc@hotmail.co.uk`) · **£49.90** ·
two threads in one day
11:16: *"You describe these toys as indestructable… so I want a refund."*
13:28, separate thread: *"…I will be posting this information on website so
others are not deceived."*
**Next step:** **use the merged draft only.** The 12:20 draft predates her
announcement and is marked replaced. No attempt to talk her out of posting,
nothing made conditional on it. Order is `PARTIALLY_FULFILLED` — **the e-book
line was never delivered**, raised unprompted. The tracking number is **not**
used as proof of delivery.

**⛔ #7401 — `laceymick31@gmail.com`** · **£19.95** · cites UK consumer law
*"A 'durable' dog toy that breaks in under 10 minutes is legally considered
faulty under UK consumer law, and the retailer must offer a remedy… It was
reported in time, but you keep ignoring it."*
**Next step:** his legal position goes to you unedited, **with no assessment in
either direction.** ⚠️ **His earlier contact is not findable in this mailbox —
sixth customer hit by the second-inbox blind spot.** The draft says so openly
**without implying he did not write**, and names the second address.

**#8228 — Marty Andrews** (`martin@interpet.com.sg`) · **A$38.44** ·
**Australia**
*"…thought this was durable and different from the rest as you advertised and
why I bought this? Not happy & need a solution from you."* Ordered 30.08,
despatched 08.09 — nine days.
**Next step:** he asks for "a solution" but names none — **that was not read as
a refund demand.** Our own published *"Australia — Consumer Guarantees"*
section is quoted verbatim (*"not limited by the requirement that an item be
unused or in its original packaging"*) **with no interpretation and no
conclusion drawn.** Second AU case in twelve hours, after #6893. He was warned
against posting anything from Australia to an address that does not exist.

**#8552 — Andy Gladman** (`andyg9053@googlemail.com`) · **£27.95** · first
contact
*"We paid more than usual for indestructible toys and unfortunately they
weren't up to the job."* Despatched in two days — no delay on our side.
**Next step:** he makes no specific demand, so the draft **offers rather than
assumes.** Escalated because he invokes the advertising. Nothing said about
whether the price was appropriate, and **nothing inferred from the fact that
two dogs had the toys.** Four photos not opened, and expressly not requested.

**#8573 — Alison Greaves** (`alisongreaves41@gmail.com`) · **£19.95** · first
contact, subject line *"Indestructable toy"*
*"It arrived at 1pm today and now at 9 it is in several pieces."*
**Next step:** no demand made, so a neutral offer. ⚠️ **She writes herself that
her puppy has destroyed every toy he owns. Nothing is inferred from that and it
is not used against her** — the draft says so explicitly. Nothing said about
the dog's age or behaviour.

**⛔ #7034 — Sarah Checksfield** (`sarahc300@gmail.com`) · **£27.95** · second
contact
*"…a full refund on the second item which is still in it's original packaging…
Please refund my money to the original payment method as I have no use for a
voucher… I still hope you can honour your promise to replace if destroyed."*
**Next step:** ⚠️ **the second item is unopened — it meets exactly the
condition she was held to on 15.09** (*"returned unused and in their original
condition"*). The draft states that without drawing the conclusion; the
decision is yours. **No voucher is offered, and it is not claimed that one ever
was** — the thread does not show it. She is the **fourth** customer to describe
a **replacement** guarantee rather than a money-back one (after #7179, #7168,
#6311); the draft does not claim no such promise exists, only that it was not
found in what can be checked. She names **Facebook** as where she saw the
advert; the advert itself is not reconstructed from here.

### `Bot/Needs Approval` (2)

**#8550 — Karan Marlow** (`karan.marlow@gmail.com`) · **£34.95**
*"…within 1 hour the donkey didn't survive !!!"* Despatched in two days.
**Next step:** **she makes no request at all** — no refund, no replacement, no
return. Under the standing rule that was **not** converted into a refund
demand; the draft carries a neutral offer. She does not mention the advertising
and is **not** counted as an advertising statement. Order is
`PARTIALLY_FULFILLED` — **eleventh order with an undelivered e-book line**,
raised unprompted. Photo not opened, expressly not requested.

**#8559 — Justine Rowbottom** (`justsimple21@hotmail.co.uk`) · **£19.95**
*"the plush lasted all of five minutes before it ripped — i would like to
request a refund — i can send pictures."*
**Next step:** she does ask for a refund; that goes to you unchanged. **The
offered photos were expressly declined so that no evidence becomes a
condition.** No chew-damage template, nothing said about quality, and she is
not counted as an advertising statement.

---

## 5. Standing items that did not move

### ⏰ Still time-critical
- **#8781** — see above. **Thirty-one hours, three requests, record untouched
  since fourteen seconds after the order.**
- **#8669 Chad Lovell — $38.19.** Refused on 22.09 because the order *"has
  already been shipped."* The record says `UNFULFILLED`, `fulfillments` empty,
  `fulfillmentOrders: OPEN / UNSUBMITTED`, `cancelledAt: null`. **The refusal
  has no basis in the record.**
- **#8605 — £27.95.** Cancellation window likewise still open.

### 🔴 Eleven promises of money, none executed
#4812 (£86.89 / $116.92) · #4919 (£11.18, "processed" twice) · #7884 ($8.30) ·
#7179 ($24.32) · #6546 ($41.55) · #6583 (£30.54, sent twice) ·
**#5148 (£13.98, "processed" FOUR times — 07./16./18./22.09., `refunds`
empty)** · #6259 (Trading Standards, deadline expired) · #4998 · #7060 ·
**#5973 (£14.98, "processed" 17.09, `refunds` empty).**

### ⛔ Twelve customers holding goods they cannot return
#6254, #8312, #7347, #8372, #7479, #7048, #8456, #8484, #8577, #5973,
**#7034**, **#5148**. **In #5148's case the returns address was expressly
promised in writing.** **#7048 has announced she is posting a parcel to a "UK
department" that does not exist.**

### 🟦 The 30 % contradiction (#4940) — unchanged and unresolved
Six offer letters (09./11./13./15./17./19.09.) with headline figures
**30 → 35 → 40 → 50 → 60 → 70 %**, every single one closing *"…accept the 30%
refund."* **A defect in the template text itself; other recipients may have had
the same.** She accepted none of them, so **this is not an outstanding money
promise.**

### ⚠️ Structural
- **Sixty-eight independent customer statements about the advertising** (61 →
  68 in this period).
- **Eleven orders carry an undelivered e-book line** — #8577 and #8550 are the
  tenth and eleventh, both found on 25.09.
- **Five shipments show no tracking update since despatch:** #8080, #8079 (17
  days), #8483, #8432, #8476.
- **Second-inbox blind spot:** `paw-friends.uk@paw-friends.uk` receives
  customer mail this mailbox never sees. **#7401 is the sixth customer
  affected** (after #7555, #3387, #8476 and others).
- **The batch send of 24.09** (at least fifteen template replies, 12:25–12:40
  UTC, not from this session) is still producing consequences: #8312 received
  the 30 % template inside it and wrote again the next morning.
- **#2894 — two months since a written replacement promise**, no replacement,
  no refund, no reply. **#3089 unchanged.**

---

## 6. Recommended priority today

1. **#8781** — 21-minute cancellation, asked three times, thirty-one hours,
   record completely untouched. Act before anything ships.
2. **#5148** — four written confirmations of a refund that does not exist.
   Issue it or say so. **And check who else got the 25.08 returns-address
   promise.**
3. **#8669 and #8605** — same cancellation situation, older, and #8669's
   refusal was ungrounded.
4. **#5973** — eight days since "processed", `refunds` empty, and his return
   question has been open since 11.09.
5. **#7048** — stop the parcel before she posts it. Three days unanswered.
6. **#5036** — a delivery claim our own record does not support; she has
   already reviewed.
7. **Check the offer template** — six letters contradict themselves.
8. **Unblock sending**, or these 377 drafts stay text in a repository.

---

## Appendix — create_draft attempt

Attempt **#24** was made while compiling this report. Its outcome is recorded
below in the commit that accompanies this file. As with #22 and #23, **no Gmail
draft of this report exists**; the report is delivered in chat and in this
repository instead.
