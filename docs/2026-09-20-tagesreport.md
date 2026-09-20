# Paw-Friends — Daily Support Report
**Window: Sat 19 Sep 2026 08:13 UTC → Sun 20 Sep 2026 08:13 UTC**
**To: nevio.marasa@icloud.com**

> **Delivery note.** This report could not be placed in Gmail Drafts.
> `create_draft` has been blocked on this account since 21 August; twenty-one
> attempts have failed and no twenty-second was made. The report is committed to
> the repository and posted in chat instead. Nothing was sent to any customer.

---

## 1. Counts by category

**24 customer cases in the window, 24 drafts written, plus one fraud email.**

| Label | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **21** |
| `Bot/Needs Approval` | **2** — #8080 (stalled shipment), #8669 (cancellation) |
| `Bot/Draft Ready` | **0** |
| `Bot/No Action` | **1** — fourth pretexting email |

**Not a single case qualified as `Draft Ready`.** Every customer case in this
window either disputes an advertising claim, concerns an unused item with no
returns route, involves a refund that was promised and not paid, or needs a
decision only the owner can make.

## 2. Refunds actually issued

**None. Zero cases fell under rule 4 (confirmed wrong item).**
`refundCreate` and `orderCancel` remain blocked for the bot
(`{"blocked":true,"category":"financial"}`).

**Refunds that need executing are listed in section 4.**

## 3. What customers wrote about

| Theme | Cases |
|---|---|
| Durability / advertising claims | **17** |
| Unused items, no way to return them | **6** |
| Refunds stated as paid but not recorded | **2** |
| Shipping, tracking, cancellation | **4** |
| Regulators and payment disputes | **6** |

**Fifteen of the seventeen advertising complaints used or paraphrased the word
"indestructible".** Two quoted our own product pages verbatim
("built to last", "40,000 dogs can't beat it").

## 4. 🔴 Needs a decision from you — ranked

### Expiring today, Monday 21 September

**1. #6259 Nick Tarrant — Trading Standards, deadline today.**
On 19 Sep at 10:28 he was told *"your full refund has been processed to your
original payment method."* Shopify shows `PAID`, `totalRefundedSet` **0.00 GBP**,
`refunds` **[]**. A payment made outside Shopify cannot be checked from here.
→ **Verify in the payment provider today. If it is not booked, book it.**

**2. #7479 Richard Bellamy-Williams — deadline today, fifth contact, no reply
on 19 Sep.** He is the only acute case that got no answer at all yesterday. He
wants two things and both already exist: a way to return an **unopened** Fluffy
(the Fluffys page carries a 30-day guarantee with **no condition attached**),
and a postal address for service (published in the Terms of Service **and in
the footer of every marketing email**).
→ **Answer him today. A draft is ready.**

### Time-critical while nothing has shipped

**3. #8669 Chad Lovell — $38.19, cancelled eleven minutes after ordering.**
`UNFULFILLED`, no fulfillments, `cancelledAt: null`.
→ **Cancel and refund while the window is open.** The same window was missed on
18 Sep for #6870 and #6905.

### Refunds stated as done, not recorded

**4. #5148 Trudi Wright — Trading Standards.** 50% of £27.95 accepted on
6 Sep, stated as processed on **7, 16 and 18 September**; Shopify `refunds: []`.
She was also promised a return address on 25 Aug that does not exist.
**5. #6583** and **6. #4998** — refunds reported as done, not in Shopify,
amounts not quantified in the log.
→ **Check all three in the payment provider.**

### Accepted in writing, only execution outstanding

**7.** #4055 — £11.97 · **8.** #6936 — £8.39 · **9.** #6528 — £22.93 ·
**10.** #6159 — 30% of £30.56

## 5. 🟦 The finding that explains the rest

**The advertising claim was located on 19 September.** It is not on the product
pages. It is in the shop's own Klaviyo email of **27 August**, sent from
`paw-friends.uk@paw-friends.uk`, quoted back to us by customer #7555:

> *"Backed by our **30-day money-back guarantee. Still unbeaten.**"*
> *"If you've stopped buying toys because **nothing survives the week** … and
> **you're covered either way**."*
> *"30-day money-back guarantee — **Zero risk on your side. Nobody has needed it
> yet.**"*

**No condition is attached to the guarantee in that text.** The chew-damage
refusal template argues against our own, older wording. That template went out
**fourteen times to eleven customers in five days** and **not once did it close
a case**: it produced two consumer-law citations, one chargeback, one ACCC
referral, two Trading Standards referrals, and a correction of a fact the
template had invented.

**No legal assessment is offered here.** The finding is factual: the two texts
contradict each other, and the marketing text is the older one. **Only you can
check the ads and the storefront.**

## 6. Other things worth knowing

- **Third order with an unfulfilled e-book line:** #8372, #7555, #6592. On
  19 Sep, #7555 stated plainly that he never received it. **Check whether that
  line is ever delivered.**
- **Shipping delay is systemic:** twenty orders in this window's history sat
  **5 to 12 days** before dispatch. #7975 (12 days) is the longest, #6592
  (5 days) the shortest.
- **Two shipping statements our own records do not support:** #7771 was told on
  1 Sep the order had shipped (fulfillment created 3 Sep); #4604 was told the
  opposite in August.
- **Fourth pretexting email** (`shopifyanalyticscentre@gmail.com`, "store placed
  on probation", 24-hour deadline). Not answered, no data released, no link
  opened.
- **Still no published returns address.** Fourteen unused items are waiting on
  one, and every affected customer has been told plainly not to post anything
  back.

## 7. What the bot did not do

No refund was issued. No cancellation was executed. No email was sent. No
customer was promised or refused a refund. No legal position was taken. No
photograph or video attachment was opened. No returns address was invented. No
currency amounts were bridged. No customer was asked to withdraw a complaint,
a chargeback, a regulator referral or a public review.
