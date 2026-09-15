# Paw Friends — Daily Support Report

**Window:** 14.09.2026 08:14 UTC → 15.09.2026 08:14 UTC
**Source:** `docs/2026-09-14-backlog-triage.md` (runs 08:20–23:20) and
`docs/2026-09-15-backlog-triage.md` (runs 02:20, 03:20, 07:20)
**Branch:** `claude/paw-friends-support-bot-fa27s0`

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **19** |
| `Bot/Needs Approval` | **12** |
| `Bot/Draft Ready` | **4** |
| **Total cases handled** | **35** |

**Not one template denial was sent in this window.** Every chew-damage case
went to you as a draft that neither grants nor refuses.

---

## 2. Refunds actually issued

**None. Zero refunds were issued.**

No rule-4 wrong-item case arose. `refundCreate` and `orderCancel` remain
blocked on this connection, and no email was sent to any customer — there is
no send capability. Every draft below exists only in
`docs/entwuerfe-zum-kopieren.md`.

---

## 3. Two deadlines expire TODAY

| Expires | Case | What was announced |
|---|---|---|
| **12:38 UTC** | **#6877 Alexander Meza** | FTC complaint, Meta report, chargeback |
| **~19:30 UTC** | **Stephen Board** (probably #8004) | Payment withdrawal, report to Facebook |

Then **#7699 Lorraine Sale — 17.09.** and **#7479 Richard Bellamy-Williams —
21.09.**, after which he says he goes to the regulators.

---

## 4. Escalated — Owner Attention (19)

### Legal and regulatory

| # | Customer | Issue | Next step |
|---|---|---|---|
| **#7479** | Richard Bellamy-Williams | Cites **Consumer Rights Act 2015** *and* **Electronic Commerce Regulations 2002**. Has kept **copies of the advertising, a scrape of the website and the domain registration data**. Demands the physical business address *"should it be required for subsequent service"*. Deadline **21.09.**, then regulators. **His claim is for the second item, unopened, in its original packaging** — the first case where the template's own stated condition is met. | **Answer the address request yourself.** I gave him nothing: Shopify's "Kirchstr. 2" is a fulfilment field, not a verified trading address, and handing it over for service of process is not mine to do. |
| **Stephen Board** | — | 16 days, no delivery, no reply to an earlier mail. **24-hour notice** then chargeback and Facebook. | **His address matches no order.** A name search finds #8004 under a *different* email. I released **no** order data. Verify identity, then answer today. |

### Delivery disputed against the tracking record

| # | Customer | Issue | Next step |
|---|---|---|---|
| **#8009** | Yvonne Ware | Told this morning the parcel was "delivered on 14 September"; replied **2 min 6 s later**: *"No I haven't not received my order."* Her refund request from **13.09. is still unanswered**, and the condition attached to it is now met. | **Check the proof of delivery.** Second case after #6420. If the scan doesn't hold, it becomes a rule case. |
| **#7525** | Carol Garvey | Fourth contact. **Searched the site for the returns route and found none** — the first customer to confirm the blocker from outside. | Answer the return question. It cannot be answered while nothing is published. |

### Advertising claims — with two named sources

| # | Customer | Issue |
|---|---|---|
| **#7698** | Amy Burnell | *"under the advertisement of being indestructible"*; **names Facebook reviews as her source**; reports a **choking hazard**. |
| **#7312** | Ricky Gaugano | *"In your **promotional video**, you will refund me when my dog destroys your toy."* Order **PARTIALLY_FULFILLED for 22 days**. |
| **#7323** | David Buckley | Bought it *"specifically because it was advertised as being designed for dogs that destroy toys"*; **"unsafe for continued use"**, three photos. |
| **#6477** | Bev McManus | **Fluffys**, £29.95, asks for exactly that back. **The only case where nothing needs determining** — single item, UK, no bundle, no currency gap. Also expected buy-one-get-one. |
| **#6869** | Martin Sellwood | *"2 of these fluffy toys **that you claim cannot be beaten**"* — matches the Fluffys copy. Asks how to return. |
| **#7647** | Jack Carter | *"sold as 'indestructible'"*; says we are in breach of a **"customer promise"** — a term not in either description. |
| **#6936** | Lisa Steggel | *"out and out lie. False advertising […] I'll make sure nobody else falls for this."* |
| **#7754**, **#6806** | Margaret Timmings, Jay Heap | **Both name the rope** — nine minutes apart, two countries. The description says *"Rope-reinforced construction for extra durability."* |
| **#7031**, **#7072**, **#7303**, **#7937**, **#7246**, **#1998** | — | Disputed claims, photo and video evidence; #1998 is a **callback promised 17.07. and never made — 59 days**. |

---

## 5. Needs Approval (12)

| # | Customer | What is needed |
|---|---|---|
| **#7060** | Felecia Pierce | **She accepted the 30% offer** — *"Yes, I accept."* This is no longer a decision, it is an **execution**. Pay it in the admin. **No figure quoted to her**: 30% of £20.35 or of $27.76 is unresolved. |
| **#7865** | Talia McClenahan | *"the seam was already split"* — possibly **defective on arrival**, which would be a rule case. Her answer decides it; the draft asks without leading her. |
| **#7660** | Rebecca Seaton | Ordered Fluffys instead of Plushies; **second one still wrapped**; wants an **exchange**, not a refund. Exchange is your action. |
| **#7587** | Susan Hines | Wanted to cancel; already shipped 11 days ago and never given tracking. Cancellation told to her plainly as impossible. |
| **#7298** | Brian Becker | Quoted **#7295 — someone else's order**. His is #7298. Nothing about #7295 was disclosed. Asks about returns. |
| **#7663, #7368, #7231, #7581, #6223, #7001, #7114** | — | Chew damage, no escalation trigger. **Yes or no on a refund.** #6223 volunteered card digits — **not repeated, not forwarded**. |

---

## 6. Draft Ready (4) — no decision needed

**#7657 John Furlong**, **#7578 Luke Buttrey**, **#8321 Darren Calver**,
**#8359**. All four are answered in full by ship date, carrier, tracking
number and link.

**#8321 asked twice.** His first enquiry was drafted on 13.09. and never went
out, because `create_draft` is blocked. **That second contact is our gap, not
his.**

---

## 7. What the owner should see

1. **The guarantee text has been found.** The **Fluffys** description carries
   *"✓ 30-day money-back guarantee"* **with no condition attached** — no
   "unused", no "original condition". The template asserts a condition the
   shop page does not state. **This bears on all 24 prior denials.**
2. **"Indestructible" appears in neither description** — both now checked —
   yet **eight customers used the word in 27 hours**. Two sources are now
   named: **Facebook** and **a promotional video**. Neither is visible from
   here. **This is the single most answerable open question.**
3. **Two customers independently reported failure at the rope**, the exact
   feature the description names as reinforcement.
4. **The currency mismatch is systematic**, not a typo: #7368 and #7581 both
   show **$27.76** on the confirmation against **£20.34** in Shopify. Which
   sum was actually charged is not determinable from here **and it blocks the
   #7060 payout.**
5. **No returns address, 33 days.** Nine customers have now asked; one
   searched the site and confirmed it isn't there.
6. **A correction I made yesterday:** I had recorded that "no dog has beaten
   it" appeared nowhere. I had only checked the Plushies page. It is in the
   Fluffys copy, verbatim: *"40,000 dogs have tried. Not one has beaten them
   yet."* I now check more than one product before calling a phrase absent.
7. **Still blocked:** `create_draft` (21 consecutive failures, each restarting
   the worker) and the Gmail label tools.
