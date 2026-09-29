# Paw Friends — Daily Support Report

**Period covered:** 28 Sep 2026, 08:14 UTC → 29 Sep 2026, 08:14 UTC
**Sources:** `docs/2026-09-28-backlog-triage.md` (runs 08:20 → 22:20) and
`docs/2026-09-29-backlog-triage.md` (runs 00:20 → 07:20)
**Compiled:** 29 Sep 2026, 08:15 UTC

---

## ⚠️ Two deviations to state up front

1. **No Gmail draft could be created for this report.** `create_draft` has
   been refused on this account since 21.08. Today's attempt is recorded in
   the appendix.
2. **No customer reply has been sent by this bot, and none can be.** Every
   reply exists only as text in `docs/entwuerfe-zum-kopieren.md` — **397
   drafts, none of them in Gmail.** **Four are marked superseded** (#8577,
   #7898 of 21.09, #8568 of 27.09, #7831 of 23.09) **and must not be sent
   alongside their replacements.**

---

## 0. The three things that outrank everything else in this report

### 🟥 A. All three open cancellation windows were closed by despatch, not by an answer

Checked this morning, the first time the order records have been reachable
since yesterday:

| Order | Cancellation history | Despatched (`fulfillments.createdAt`) |
|---|---|---|
| **#8781** Glenn Yarbrough · $37.69 | **asked three times — 24.09 15:42, 24.09 20:29, 25.09 22:41 — never answered** | **28.09 04:37:47** |
| **#8605** · £27.95 | open, unanswered | **28.09 04:31:16** |
| **#8669** Chad Lovell · $38.19 | refused 22.09 | **28.09 04:32:52** |

All three went out **within six minutes of each other**, about two hours
before the Shopify connection switched away — which is why this was not
visible until today.

**Two consequences I am recording, not interpreting:**

- **#8781 shipped despite three unanswered cancellation requests.** Every
  report from 26.09 onwards said the window was demonstrably still open.
  **It is now closed.** `cancelledAt` is still `null`; nothing was cancelled.
- **#8669 was told on 22.09 that the order "has already been shipped." The
  despatch record is dated 28.09 — six days later.** **The statement was not
  true when it was made.** What follows from that is your decision.

All three: `totalRefundedSet` **0.00**, `refunds` **empty**.

**No message was written to any of the three.** They have not written, and I
am not telling anyone unprompted that their cancellation went nowhere. That
is your call.

### 🟩 B. The Shopify connection is back on Paw-Friends.uk

`shop { name myshopifyDomain }` now returns **"Paw-Friends.uk",
`fiqb08-8n.myshopify.com`**, and order queries return full records again.
**I cannot determine from here exactly when it was restored**, and
`switch-shop` was never called.

**Every draft written between 28.09 06:20 and 29.09 06:20 deliberately
contains no order-record data** — #7626, `hud@hildebrandt.com.au`, #7373,
#7479, #6254, #7168, #8142, #7831, `betsey.barton@`, #8456, Barbara Johnson,
#8372. **I have not back-filled them.** They are honest as they stand; adding
figures retrospectively to a text that says the record could not be checked
would make it dishonest.

### 🟨 C. Still unresolved: the passkey alert of 26.09, 10:23 UTC

A new passkey was added to `support.pawfriends.uk@gmail.com`. **Unverifiable
from here. Nothing clicked, nothing changed.** It is the account all customer
traffic runs through, and it has now been open for three days.

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **10** |
| `Bot/Needs Approval` | **1** |
| `Bot/Draft Ready` | 0 |
| `Bot/No Action` | 0 |
| **Total customer cases** | **11** |

**Eleven new drafts** (386 → 397). Two cases (#8142, #7831) wrote three times
each within the window and count as one case each; their existing drafts were
amended rather than duplicated.

**Plus one non-customer item** — see section 4.

---

## 2. Refunds actually issued

**None. £0.00 / $0.00 / A$0.00.** No case met rule 4 (confirmed wrong item).
No cancellations executed, no address changes executed. `refundCreate` and
`orderCancel` remain blocked.

---

## 3. 🟥 The pattern that produced most of this window's traffic

**The chew-damage template was sent to people whose goods were sealed and
unopened. Four are now documented:**

| Customer | Times they said the goods were unused | What they got |
|---|---|---|
| **#8372 Kerri** | **four times** — 17.09, 19.09, 22.09, 24.09 (the last in capitals) | **three chew-damage refusals, then the batch template** |
| **#8142 Wendy Price** | **three times** — 24.09, 28.09 13:07, 28.09 13:17 | **two chew-damage refusals; the sealed item never mentioned** |
| **#7479 Richard Bellamy** | asked 16.09, **never answered** | **a third percentage offer instead of an answer** |
| **#8456 Cath Livesey** | 23.09 ×2 — **she never mentioned chewing at all** | **the template in BOTH her threads** |

**#8456 is the clearest single piece of evidence:** she replied *"I have not
said that the toys have been chewed."* The template reached both of her
threads, in which only quality and returns had been discussed.

**And the batch sends are now quantified exactly.** My earlier claim that the
true number was "not determinable from here" was **wrong** — `in:sent` returns
the Sent folder completely:

- **24.09: 37 messages, 12:18:01 – 12:39:49.**
- **28.09: 32 messages, 11:08:21 – 11:26:59.**

**Of the 32 recipients on 28.09, only six replied.** What the other
twenty-six received is unverified by any reply. **These were not sent from
this session — this account has no send capability. I record what is in Sent
and make no claim about who sent it.**

---

## 4. All 11 customer items, with recommended next steps

### `Bot/Escalated - Owner Attention` (10)

**🟥 #7324 — Kelly** (`kellydstudio@gmail.com`) · **AUD 106.66** ·
**Australia** · first contact · **29.09 06:08**
*"Within 4 min this happened. These are not as advertised. They are in fact
very weak and unsafe. Please refund."* One photo attached.
**Next step:** **this is the first explicit safety report a customer has
worded that way in these logs, and it should be on your desk today.** The
draft **makes no statement about product safety in either direction** — it
passes the report on, marked as a safety report and kept separate from the
refund question. It makes no guarantee determination and quotes no deadline.
**No chew-damage template**: she never said the goods were used, and it is not
imputed to her. Record: ordered 23.08, **despatched 02.09 — ten days**,
nothing refunded, **the e-book line is still unfulfilled** (told to her
unprompted). Total paid stated; **explicitly not broken down per item** —
the line prices sum to **353.00 AUD** against **106.66** actually paid.
Tracking number not used as delivery proof. Photo not opened. Warned not to
post anything, since no returns address exists. **Fifth Australian case**;
the AU section is named, not interpreted.

**🔴 #8372 — Kerri** (`wollenzienk@hotmail.com`) · **$96.89** · **ACCEPTED the
39 % offer, 29.09 01:11**
*"Yes, let's go ahead with the 39% partial refund. My order was for $96.89."*
**Next step:** **pay it or retract it. This is the twelfth open money
promise.** Her stated figure matches the record exactly; `totalRefundedSet`
**0.00**, `refunds` **empty**. **The amount to pay is the one in the offer
sent 28.09 11:25:34** — I deliberately did not restate or recalculate it, so
that no error enters an agreement she has already accepted. The draft records
her acceptance, **refuses to say it has been processed and gives no date**,
and states openly that she was sent chew-damage paragraphs four times about
goods she had said four times were untouched.

**⛔ Barbara Johnson** (`jurienink@gmail.com`) · second contact · **first
message unanswered for five days**
*"I purchased 2 plushies and sent you an email. Can you please get back to
me."* Her 23.09 first contact: *"I bought because you stated on website that
it would last but it did not."*
**Next step:** **seventy-third independent customer statement about the
advertising.** The draft names the five days as our failure, not a backlog.
**She bought two and gave one to her dog — whether the second is unopened is
asked, not assumed**, so she is not counted among the customers holding
unreturnable goods. Eleven attachments not opened and expressly declined.
Nothing inferred from her dog's breed or size.

**⛔🟥 #8456 — Cath Livesey** (`cath.lives@icloud.com`) · two threads ·
**first contact unanswered for five days**
*"I have not said that the toys have been chewed — they are in their original
packaging, unopened. Please advise where I can return them."*
**Next step:** see section 3; she is the clearest evidence that the template
goes out without the case being read. **One draft for both threads, to be sent
once.** Her phone number is not used or mentioned; her "( 3 )" was not
reconciled against the record.

**⛔🟥 #7831 — Mary Hollerich** (`mhollerich89@gmail.com`) · US · **three
contacts on 28.09** · first contact unanswered five days
*"This is the most bazar response I have ever heard… You said it would hold
up. I'll post this all over face book"*, then *"I am reporting you to the
BB."*
**Next step:** owner decision. **Nothing is tied to the Facebook post or the
BBB report** — no request for delay, no request to withdraw either, and the
draft says *"You do not owe us silence in exchange for an answer."* **No legal
or procedural assessment of the BBB report in either direction.** She threw
the items away the same evening; **that is not held against her and nothing
depends on it.** Her 23.09 draft is marked superseded.

**⛔🟥 #8142 — Wendy Price** (`wendyprice579@gmail.com`) · **three contacts on
28.09**
*"As explained I still have one sealed in its packaging — where do I send it
for my refund?"*, repeated ten minutes later.
**Next step:** see section 3. The draft answers the question she actually
asked — **there is no returns address** — and names the three times she was
answered about the chewed toy instead. **No third chew-damage template, and
she is told none is coming.** Nothing tied to her announced chargeback or
review.

**⛔ #7479 — Richard Bellamy** · received a **third percentage offer** in the
28.09 batch, after two refusals and after asking on 16.09 about his unopened
item — which has still never been answered.
**Next step:** answer the question he asked on 16.09. **No third offer is made
from here.** No legal assessment of the points he raised. **On his question
about an address, the draft points to the trading address published in our own
Terms of Service** — that is already public and checkable — and **confirms and
denies nothing about the details he says he obtained from German registers**,
beyond what is already published.

**⛔ #6254 — David Hickman** (`davehickman71@gmail.com`) · **counter-offer**
*"I would be satisfied with a 40% refund on the total order. Alternatively, I
am happy to return the items."*
**Next step:** his number goes to you verbatim. **No counter-figure was
introduced and no attempt was made to move him off his.** Two of his four
items are unopened; he is not told what to do with them. **He is told openly
that the return half of his proposal cannot be carried out — there is no
returns address — and that he had asked about that on 16.09.**

**⛔ #7168 — Phil & Sarah Hockley** (`philnsarahhockley@gmail.com`)
*"I still want this matter to be escalated… totally unacceptable to mislead
customers. Especially false advertising your product."*
**Next step:** he asked for escalation and this is it. **The draft does not
say the advertising was misleading, and does not say it was not** — expressly
named as not decidable from here. **No guessed first name**: the address names
two people and the message is unsigned.

**⛔ #7373 — Dom Frisina** (`isdom00@gmail.com`) · first contact
*"Your item lasted not even a day or to and was stated that was not
breakable."*
**Next step:** **seventy-second advertising statement.** **His "Like to ask"
names no demand — it is not interpreted**; the draft offers and asks what he
wants. **The draft does not claim the statement he quotes does not exist** —
it says only what is and is not in the twelve product descriptions, and does
not reconstruct the advertisement. Two photos not opened.

### `Bot/Needs Approval` (1)

**`betsey.barton@yahoo.com`** · first contact · **address change**
*"Is it too late to change the delivery address?"* — a new address in Mesa,
Arizona.
**Next step:** **you have to do this in the admin; I did not and will not
change an order.** She gives no order number, and the record was not checkable
at the time. **The draft neither says it is too late nor says it is still
possible** — it says plainly that the status cannot be checked from here and
asks for the number. **The new address goes to you verbatim and is not
repeated back to her.** No name guessed; no date promised. She is also offered
the chance to say if the parcel has already gone to the old address.

---

## 5. 🟨 One non-customer item

**`emmydigital4200@gmail.com`, 28.09 13:16 UTC** — unsolicited affiliate
proposal in German, 2 % commission, **asking for a WhatsApp number.**
**Not answered. No number given and none will be.** Nothing clicked, no data
released. **Third unsolicited business approach in this mailbox**, after
`shopifystoreregulatory.center@gmail.com` (06.09) and `permitshopify@gmail.com`
(26.09). Whether to engage is your call.

---

## 6. Standing items

### 🔴 Twelve promises of money, none executed — **£466.97 in quantified GBP, plus #8372**
#4812 · #4919 · #7884 · #7179 · #6546 · #6583 · **#5148 (£13.98, "processed"
four times)** · #6259 · #4998 · #7060 · **#5973 (£14.98)** · **#4055
(£11.97)** — and now **#8372 ($96.89 order, 39 % accepted).**

Re-checked this morning: **#4055, #5148 and #5973 all show
`totalRefundedSet` 0.00 and `refunds` empty.** No movement.

### 🟦 Two template defects still unchecked
- **The returns address that never existed** went to at least **two**
  customers in identical wording — **#5148 (25.08) and #4055 (23.08)**.
- **The 60/50 contradiction** has two documented occurrences — **#4940's six
  letters** and **#4055's offer of 17.09 10:37:14**, corrected eleven seconds
  later.

### ⛔ Customers holding goods they cannot return
**#7048 has now had no reply for six days** about the parcel she announced she
would post to a "UK department" that does not exist.

### ⚠️ Structural
- **Seventy-four independent customer statements about the advertising**
  (71 → 74 in this window: #7373, Barbara Johnson, #7324). Customers already
  counted were deliberately not counted again.
- **Five Australian cases** — #6893, #8228, #8431, `hud@hildebrandt.com.au`,
  **#7324**. The shop's own "Australia – Consumer Guarantees" section is named
  or quoted in all five drafts and **interpreted in none.**
- **Twelve orders carry an undelivered e-book line** — #7324 is the twelfth.
- **Three customers announced public or external steps in this window** —
  #7831 (Facebook and BBB), #8142 (review and chargeback), #7479 (a series of
  authorities). **Nothing was tied to any of them.**
- **Second-inbox blind spot** unchanged: `paw-friends.uk@paw-friends.uk`
  receives customer mail this mailbox never sees.
- **Five customers' first contacts went unanswered for days** — #7831 (five),
  #8456 (five), Barbara Johnson (five), #8142, #8372.

---

## 7. Recommended priority today

1. **#7324 — the safety report.** A customer has told us in writing that the
   product is unsafe. It should not wait behind anything else on this list.
2. **The passkey alert.** Three days old. Confirm it was you; if not, secure
   the account.
3. **#8781 and #8669.** Three unanswered cancellation requests shipped anyway,
   and a refusal on 22.09 that the despatch record contradicts.
4. **#8372.** She accepted in writing. Pay the amount in the 28.09 offer, or
   tell her plainly it will not be paid.
5. **#4055, #5148, #5973** — money confirmed in writing, `refunds` still
   empty. **And check who else received the 23.08/25.08 returns-address
   sentence.**
6. **Stop the chew-damage template** until the case is read first. Four people
   with sealed goods received it.
7. **`betsey.barton@`** — the address change needs doing in the admin, or she
   needs telling it is too late.
8. **#7048** — six days; stop the parcel.
9. **Unblock sending**, or these 397 drafts stay text in a repository.

---

## Appendix — create_draft attempt

Attempt **#27** was made while compiling this report. As with #22 to #26,
**no Gmail draft of this report exists**; it is delivered in chat and in this
repository instead.
