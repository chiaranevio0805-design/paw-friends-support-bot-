# Paw-Friends — Daily Support Report
**Saturday 19 September 2026, 08:13 UTC**
**Window: 18 Sep 08:13 → 19 Sep 08:13 UTC**
Source: `docs/2026-09-18-backlog-triage.md` (runs 08:20–21:20) and
`docs/2026-09-19-backlog-triage.md` (runs 00:20–06:20).

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **20** |
| `Bot/Draft Ready` | **4** |
| `Bot/Needs Approval` | **3** |
| `Bot/No Action` | **2** (Klaviyo mailing, CJ-Dropshipping pretext) |
| **Total entries** | **29** (27 customer cases + 2 system mails) |

## 2. Refunds actually issued

**None. Zero refunds were issued in this window, and none since this bot began.**

No case met rule 4 (confirmed wrong-item delivery). Two came close and neither
qualifies: **#7989** is a short shipment plus an unimplemented variant
confirmation, and **#4604** is a misdelivery caused by us — neither is a wrong
item.

## 3. `Bot/Needs Approval` — money already agreed, only execution missing

| # | Customer | Amount | Status |
|---|---|---|---|
| **#6528** | Tommy Johnson | **£22.93** (50%) | accepted in writing 19 Sep |
| **#4055** | Kimberley Shenton | **£11.97** (60%) | accepted 17 Sep *(carried over)* |
| **#6936** | Lisa Steggel | **£8.39** (30%) | accepted 18 Sep |
| **#6159** | Mary Linan | **30% of £30.56** | accepted 19 Sep |

**Next step for all four: release the money. No new decision is required — the
shop made each offer and each customer accepted it in writing.**

## 4. Deadlines — Monday 21 September

| # | Customer | What happens |
|---|---|---|
| **#7479** | Richard Bellamy | 4th contact, **has announced he will serve process**. Holds an **unopened** item, notified in time, and has asked *how* to return it — there is no returns address to give him. |
| **#6259** | Nick Tarrant | Trading Standards engaged. Offers ran 30→50→60%; he wants 100%. |

**Also open:** #7323 (22 Sep), #1998 and #4975 (22 Sep), #8295 (23 Sep, set by
the customer himself and since overtaken by his refund demand).

## 5. Time-critical and still repairable

**#8081 Matthew Pierce** — ordered 29 Aug, **still `UNFULFILLED`, not
cancelled, nothing refunded, 21 days**. His APO military address has no street
number; on 11 Sep he was told the address was updated and then, four hours
later, asked for a street number that does not exist. **On 12 Sep he offered to
accept a refund. Seven days of silence since.**
**Next step: ship it or cancel and refund. Both are one action.**

## 6. The advertising question — now on seven independent customer statements

| Claim | Customers |
|---|---|
| The ad promises a **refund or replacement if the toy rips** | #7255 (US), #6311 (AU), #6205 (US), #3405 (US) |
| A **guarantee text with no "unused" condition** | #4998 (GB), #7778 (US) |
| The phrases **"Anti-Destruction Structure"** and **"extremely durable & long lasting"** | #4998 (GB), **#8189 (US)** |

**The last row is the strongest finding.** Two customers, two countries,
sixteen days apart, quoted **the same two phrases verbatim**. **Neither appears
in any of the twelve product descriptions** — I read all of them.

**A single quotation can be a misreading. Two independent, word-identical ones
are not.** This text exists somewhere on the storefront that this desk cannot
see. **No draft confirms or denies any of it. Only you can check the
Facebook/Instagram advertising and the storefront pages outside the product
descriptions.**

## 7. Returns — the structural blocker

**There is still no published returns address.** In this window alone:

- **#4812 Carolyn Marmalejo** asked **five times** since 20 Aug — 29 days,
  four percentage offers instead of an address.
- **#6528 Tommy Johnson** asked **five times** — same pattern.
- **#6159 Mary Linan** asked on 29 Aug and was told on 31 Aug, in writing,
  *"the second toy is unused, it would normally be eligible for return"* — then
  offered a percentage instead of the return.
- **#6384, #7168, #8312, #8189** all asked how to return or offered to send
  items back this window.

**Eleven unused items are now waiting on an address that does not exist.**
Every draft warns the customer explicitly **not** to post anything.

## 8. Refunds stated as done but never paid

| # | What was said | Actually refunded |
|---|---|---|
| **#4998** | *"the 20% partial refund **has now been processed**"* (7 Sep) | **£0.00** |
| **#6583** | *"they will arrange a **full refund**"* (3 Sep) | **£0.00** |
| **#5148** | 50% described as *"processed"* **twice** | **£0.00** |

**No draft in this window tells any customer that a refund has been processed.**

## 9. Safety reports — five in two days

**#8406** (a piece swallowed), **#8189** (stuffing swallowed), **#8312** (fear
of swallowing loose parts), **#8407** and **#6936** (squeaker chewed out).

**No draft makes any statement about material, toxicity or safety in either
direction**, and none gives veterinary advice. Where a customer raised concern,
they were pointed to their vet with no assessment from us.

## 10. Other findings in this window

- **#4604 Nicholas Kloepfer** — the clearest documented shop error: wrong
  address reported 5 Aug, correction promised twice, **never applied**, and the
  9 Aug statement *"hasn't been dispatched"* was **already untrue** (it shipped
  8 Aug). 44 days, nothing received, nothing refunded.
- **#8002 Thomas Robinson** — quoted two sentences of the Plushies page; **both
  verified verbatim, emojis included.**
- **Six customers chased us because nothing came back** — #8295, #7555, #7041,
  #7989, #6205, #7275. **Three opened a new thread to do it**, which makes them
  look like new customers in a threaded view.
- **Ten orders sat eight to twelve days before dispatch.** One (#8407) shipped
  next day, so the delay is intermittent, not uniform.
- **A third pretexting attempt** arrived (`storeclean.panel@gmail.com`, posing
  as CJ Dropshipping). Not answered, nothing released, no link opened.

## 11. Note on delivery of this report

**No Gmail draft was created.** `create_draft` has failed on every attempt
since 21 August (21 consecutive failures, each restarting the worker). No 22nd
attempt was made. This report is committed to the repository and posted in
chat instead. **All 72 reply drafts likewise exist only in
`docs/entwuerfe-zum-kopieren.md` — none are in your Gmail Drafts folder.**
