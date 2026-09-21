# Paw-Friends — Daily Support Report
**Window: Sun 20 Sep 2026 08:13 UTC → Mon 21 Sep 2026 08:13 UTC**
**To: nevio.marasa@icloud.com**

> **Delivery note.** This report could not be placed in Gmail Drafts.
> `create_draft` has been blocked on this account since 21 August; twenty-one
> attempts have failed and no twenty-second was made. The report is committed to
> the repository and posted in chat instead. **Nothing was sent to any
> customer.**

---

## 1. Counts by category

**13 customer cases in the window, 13 drafts written, plus three system emails.**

| Label | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **10** |
| `Bot/Needs Approval` | **2** — #8221 (stalled shipment), #5086 (replacement) |
| `Bot/Draft Ready` | **0** |
| `Bot/No Action` | **3** — Stripe receipt, Klaviyo invoice, Klaviyo notice |

## 2. Refunds actually issued

**None. Zero cases fell under rule 4 (confirmed wrong item).**
**No cancellation was executed either.** `refundCreate` and `orderCancel` remain
blocked for the bot.

## 3. What customers wrote about

| Theme | Cases |
|---|---|
| Durability / advertising claims | **10** |
| Customers who asked for nothing at all | **3** (#8171, #7884, and one AU report) |
| Refund expected but never agreed | **2** (#7041, #5310) |
| Shipping / stalled delivery | **1** (#8221) |
| Replacement rather than refund | **2** (#5086, #6592 carried over) |
| Safety concern about the filling | **1** (#7749) |
| Size complaint | **1** (#7884) |

## 4. 🔴 Needs a decision from you — ranked

### Both deadlines expired yesterday without action

**1. #6259 Nick Tarrant — Trading Standards. Deadline was 21 September.**
Told on 19 Sep at 10:28 that the refund was "processed"; Shopify shows `PAID`,
`totalRefundedSet` **0.00 GBP**, `refunds` **[]**.
→ **Check the payment provider today. If it is not booked, book it.**

**2. #7479 Richard Bellamy-Williams — deadline was 21 September, sixth contact.**
He has had **nothing from us since 15 September**. He has now found the trading
address, the sole-trader registration and the tax reference himself, and has
announced a referral to the **European Consumer Centre Germany**. His actual
question — how to return an **unopened** Fluffy — remains the easiest one in the
inbox: the Fluffys page carries a 30-day guarantee with **no condition
attached**, and the only obstacle is that no returns address exists.
→ **Answer him today. A sixth draft is ready.**

### Time-critical, window still open

**3. #8669 Chad Lovell — $38.19, cancelled eleven minutes after ordering.**
Still `UNFULFILLED`, no fulfillments, `cancelledAt: null`.
→ **Cancel and refund before anything ships.**

### Refunds stated as done, not recorded

**4. #5148 Trudi Wright** (Trading Standards; stated three times) ·
**5. #6583** · **6. #4998**
→ **Check all three in the payment provider.**

### Accepted in writing, only execution outstanding

**7.** #4055 — £11.97 · **8.** #6936 — £8.39 · **9.** #6528 — £22.93 ·
**10.** #6159 — £9.17

### New this window

**11. #7041 Tim Fitton — three messages since 16 September, not one reply.**
He writes that he is "still awaiting a full refund". **No such agreement is
findable.** He was told so plainly rather than left waiting.
**12. #8221 Beau Ricketts — shipment with no tracking update in twelve days.**
Third such case after #8080 and #6002.
**13. #7884 Logan Bishop — states he paid about $47; the order records $27.66.**
Not bridged, not explained away. **Only checkable in the payment records.**

## 5. ⚠️ A correction about my own figures

**The chew-damage refusal template has now gone out at least seventeen times to
at least thirteen customers since 15 September.** I have had to revise that
number upwards **four times**, most recently this morning.

**The reason is structural:** a sent refusal only becomes visible to me when the
customer later replies and the thread shows an unread message. **Threads where
the customer gave up stay invisible.**

**So "seventeen" is a floor, not a total.** Establishing the real number needs
the sent folder searched **by text pattern**, which I cannot do from here.
**Every count in these reports should be read as "at least".**

**What is not in doubt:** of the sends that are visible, **not one closed a
case.** They produced two consumer-law citations, one chargeback, one ACCC
referral, two Trading Standards referrals, one announced European Consumer
Centre referral, at least one 1-star public review, and one refusal that
invented a fact about the customer's own case.

## 6. 🟦 The advertising finding, unchanged

The guarantee wording customers quote is **not on the product pages**. It is in
the shop's own Klaviyo email of **27 August**: *"30-day money-back guarantee —
**Zero risk on your side**"*, *"**you're covered either way**"*, *"**Nobody has
needed it yet**"* — **with no condition attached.** The Klaviyo invoice of
20 September confirms **the subscription is paid for the coming month**, so that
text keeps going out until it is changed. **Thirty independent customer
statements now rest on it.**

## 7. What the bot did not do

No refund issued. No cancellation executed. No email sent. No customer promised
or refused a refund or a replacement. No legal position taken. No statement made
about material safety in either direction. No photograph, video or receipt
opened. No returns address invented. No currency amounts bridged. No product
size assessed and no product image compared. No customer asked to withdraw a
complaint, a chargeback, a regulator referral or a public review.
