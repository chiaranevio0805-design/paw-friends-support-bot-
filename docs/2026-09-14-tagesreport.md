# Paw Friends — Daily Support Report

**Window:** 13.09.2026 08:14 UTC → 14.09.2026 08:14 UTC
**Source:** `docs/2026-09-13-backlog-triage.md` (runs 08:20–22:20) and
`docs/2026-09-14-backlog-triage.md` (runs 01:20, 04:20, 07:20)
**Branch:** `claude/paw-friends-support-bot-fa27s0`

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **24** |
| `Bot/Needs Approval` | **8** |
| `Bot/Draft Ready` | **1** |
| No action (noted only, no new label) | **1** |
| **Total cases handled** | **34** |

Drafts written in the window: **28** full reply texts, of which **11 are
second or third versions** replacing a draft that a template denial
overtook before it could be sent.

---

## 2. Refunds actually issued

**None. Zero refunds were issued in this window.**

No rule-4 wrong-item case arose. The `refundCreate` and `orderCancel`
mutations remain blocked for this connection in any event
(`{"blocked":true,"category":"financial"}`), so every refund on the list
below requires the owner to act in the Shopify admin.

**No email was sent to any customer by the bot.** There is no send
capability on this account; everything below exists as draft text in
`docs/entwuerfe-zum-kopieren.md` only.

---

## 3. Escalated — Owner Attention (24)

### Time-critical

| # | Customer | Issue | Next step |
|---|---|---|---|
| **#6877** | Alexander Meza | FTC complaint, Meta report and chargeback announced with a **48-hour deadline expiring 15.09. 12:38 UTC**. "Reinforced double stitching" confirmed as published; PARTIALLY_FULFILLED corroborates his missing free gift. | **Answer before the deadline.** Decide on refund and on the missing gift. This is the single most urgent item on the list. |
| **#5829** | David Coles / Tasmin Hunt | Formal Consumer Rights Act 2015 notice of 11.09. was answered on 13.09. with the chew-damage template. He has moved from *threatening* chargeback and Citizens Advice to *executing* both. Both phrases he quotes are verified in the shop data. | **Owner reply today.** Second draft version ready. Decide refund before the bank does. |
| **#7292** | tracy hartley | Has now asked **twice** where the guarantee's "unused" condition is published, and was answered twice with the template asserting it. **No citation exists that the bot can find.** | **Answer her actual question.** Third draft version ready. Either produce the source or say plainly that it is not published. |
| **#2894** | Jeff Hughes | Replacement promised **24.07.**, never created in Shopify, **51 days**, at least six polite chase-ups. | **On the refund list, £19.95, rule 1.** Issue it or ship the replacement. |

### Consumer-law citations

| # | Customer | Issue | Next step |
|---|---|---|---|
| **#5032** | Adam Murgatroyd | Cites the **Consumer Rights Act 2015** (Scotland, UK). Argues the 30-day guarantee is misleading because an unused/unopened condition merely restates an existing right. Sharpest form of the objection so far. | Owner decision. Kaching bundle — the per-item share must come from the admin (£54.85 of line prices against £42.90 paid). |
| **#6781** | Carlie Terry | "Not fit for purpose" — CRA language without naming the Act. Her returns-process question from 12.09. is still unanswered. | Answer the returns question and decide the refund. |

### Announced public action

| # | Customer | Issue | Next step |
|---|---|---|---|
| **#7610** | Vicky Blow | **Has actually posted a Trustpilot review** and announced more. First confirmed published review. | Owner reply. Do **not** ask her to remove or amend it, and do not make anything conditional on it. |
| **#6755** | Matt Murphy | After the denial: *"I will be posting negative reviews that will cost more in lost business than my $30."* | Owner decision on the $30. |
| **#7179** | — | Announced public dissemination; accuses the shop of lying. | Owner reply. |
| **becca23047@aol.com** | — | Announced an "honest review" about the guarantee not being honoured. **Order still not findable** (order data supplied only as a screenshot). | Identify the order from the screenshot, then decide. |
| **#7119** | — | Bank chargeback announced. | Decide before the bank does. |

### Disputed advertising claims

| # | Customer | Issue | Next step |
|---|---|---|---|
| **#7030** | Jordan Hauler | Quotes **"indestructible"** and "heavy chewers", sourcing it to *"the reviews and things you post"*. Two toys; he has put the **second one away unused**. | **Owner verification needed: where does "indestructible" appear?** It is not in the product description. |
| **#4822** | Melody Clement | *"they are not indestructible"*, refund requested, photo offered. | Same verification; then decide. |
| **#7608** | — | Safety and material claim. | High priority. No statement on material safety has been made in either direction. |
| **#6833** | Karen Wendland | Disputed claim against the verified product name. | Owner reply. |
| **#6835** | Terry Allen | Disputed claim with **two photo attachments**. | Owner reply. |
| **#4939** | Sara Thompson | Quotes **three promises at once**; two verified in the shop data ("double stitching", "a toy that lasts"), one unverified (money back). Her *"the stuffing won't come out"* is **not** in the checked description — origin unknown. Order **PARTIALLY_FULFILLED since 07.08. (37 days)**. | Owner reply plus: complete or cancel the outstanding fulfilment. |
| **#5436** | — | Guarantee understood as covering destruction. | Owner reply. |
| **#7034** | — | Guarantee understood as covering destruction. | Owner reply. |
| **#6882** | Chris Cobb | Had asked for an explanation; received the template instead. Escalated **4 min 51 s** after it. | Second draft ready. |
| **#7316** | Brett Merriman | **Third** denial. Escalated **3 min 17 s** after it — the fastest of the whole period. | Second draft ready. |
| **#7223** | — | High priority. | Owner reply. |
| **#7547** | Luke Prior | *"I was not given the choice to cancel"* — refund demand passed over twice. Upgraded from Needs Approval. | Owner decision. |
| **gacobalsam@aol.com** | — | Disputed claim; **order not findable**. Third `@aol.com` address in three days with no findable order. | See the pattern note in §6. |

---

## 4. Needs Approval (8)

| # | Customer | What is needed |
|---|---|---|
| **#7673** | Michelle Barnes | Refund request, **photo attached**, toy destroyed in five minutes. Formally a plain chew-damage case with no escalation trigger — but the product is sold under the name *"Designed for Furry Friends Who Destroy Everything"*. **Yes or no on the refund.** |
| **#8517** | — | Customer offered credit-card details by email. The draft declines them. **Nothing card-related may be requested, received or forwarded by email.** |
| **#8505** | John Marsh | Address correction eleven minutes after ordering. **The bot does not edit orders** — the correction has to be made in the admin. |
| **#8009** | Yvonne Ware | Promised date has passed. Sayable: ship date, carrier, number, tracking link. |
| **#7401** | Mick Lacey | Subject line as the whole message. |
| **#6420** | Keith Grice | Scanned as delivered 25.08., never received. Yesterday's stock delivery answer told him what he had already reported himself. **Replacement or refund is an owner decision.** |
| **#7610** | Vicky Blow | *(Also listed above — upgraded to Escalated during the day.)* Refund yes/no has been open since 11.09. |
| **#8321** | Darren Calver | *(Draft Ready — see below.)* |

---

## 5. Draft Ready (1)

**#8321 Darren Calver** — "any updates on my dogs toys pls?" Ship date,
carrier, tracking number and link are all sayable. No owner decision needed.

---

## 6. Findings the owner should see

1. **Twenty-three chew-damage template denials since 11.09. Every single one
   that was answered escalated. No exceptions.** Fastest turnaround from
   denial to escalation: **3 min 17 s**. The template is not resolving cases;
   it is generating them.
2. **"Indestructible" is not in the product description** — verified 12.09.
   Two customers used the word verbatim within fourteen minutes on 14.09. and
   one sourced it to "the reviews and things you post". **Where it is
   published is an open owner verification**; the ad texts have never been
   readable from here.
3. **The guarantee text is still not verifiable.** It is not in
   `descriptionHtml`. Ten customers in five days describe it as covering
   destruction. One has now asked twice for the citation. **No citation has
   been invented.**
4. **The product name works against the denial.** *"Plushies – Designed for
   Furry Friends Who Destroy Everything"* is in the order records and the
   Shopify shipping emails — evidenced, not alleged.
5. **Three `@aol.com` addresses in three days with no findable order**
   (dinod28, becca23047, gacobalsam). **No conclusion is drawn** — it may be
   a different address on the order. Worth checking whether it is an address
   mapping issue in the shop.
6. **No returns address exists.** Open 31 days; six customers have asked how
   to return.
7. **Still blocked:** `create_draft` (21 consecutive failures, each
   restarting the worker) and the Gmail labelling tools. This is why handled
   threads keep resurfacing as unread, and why every draft lives in the repo
   rather than in Gmail.
8. **Search method corrected today.** The hourly check was using
   `newer_than:2h`, which is not reproducible — Gmail documents `newer_than`
   for days, months and years only. It hid #5032 for three hours across two
   runs that reported "nothing new". The hourly run now uses `newer_than:1d`
   and diffs against the day's log. The last 24 hours have been reconciled;
   #5032 was the only case missed.

---

## 7. Open deadlines

- **#6877 Alexander Meza — 15.09. 12:38 UTC** (48 hours, FTC/Meta/chargeback)
- **#7699 Lorraine Sale — 17.09.** (her own date)
