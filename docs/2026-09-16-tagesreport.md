# Paw Friends — Daily Support Report

**Window:** 15.09.2026 08:14 UTC → 16.09.2026 08:14 UTC
**Source:** `docs/2026-09-15-backlog-triage.md` (runs 08:20–23:20) and
`docs/2026-09-16-backlog-triage.md` (runs 01:20–04:20)
**Branch:** `claude/paw-friends-support-bot-fa27s0`

---

## 1. Counts by category

| Category | Count |
|---|---|
| `Bot/Escalated - Owner Attention` | **32** |
| `Bot/Needs Approval` | **5** |
| `Bot/Draft Ready` | **2** |
| No action (recorded only — pretexting mail, service pitch) | **2** |
| **Total cases handled** | **41** |

Drafts written in the window: **34**, of which **9 are second, third or fourth
versions** replacing a draft that a template denial overtook before it could be
sent.

---

## 2. Refunds actually issued

**None. Zero refunds were issued.**

No confirmed rule-4 wrong-item case arose. `refundCreate` and `orderCancel`
remain blocked on this connection. **No email was sent to any customer** —
there is no send capability. **No write operation of any kind was performed in
Shopify.**

**One case now points toward rule 4 and was deliberately not acted on:**
**#7164 Barry Dunster** says what arrived *"is not plush"* — a wrong-item
claim, not chew damage. It is **unconfirmed**: the photo was not opened, the
product images were not compared, and nothing was said about the material. It
went to you as a verification request, not as an executed refund.

---

## 3. The three findings that matter most

### 3.1 The condition the template relies on is not published anywhere

Prompted by **tracy hartley's fourth request for a citation**, the shop's
published policies were queried for the first time. Result:

- The **Return/Refund Policy consists entirely of an Australia section.** No
  general part, no UK part, no US part, no procedure, no returns address. It
  refers to *"the conditions stated above"* — **nothing stands above it.**
- The words *"unused"* and *"original packaging"* appear **once** in the entire
  published body, and only to say that Australian consumer guarantees **are not
  limited by them.** The condition itself is **never stated as a rule** — not
  on the Plushies page (which carries no guarantee text at all), not in the
  policy, not in the terms.

**Roughly 36 denials since 11.09. rest on a condition the shop does not
publish.** This answers #7292, #5032, #7001 and #7479 at once.

**#7663 Murray McLean is the sharpest instance:** he ships to Western
Australia, he was denied on exactly that requirement on 15.09., and the only
section the published policy contains is the one that says Australian rights
are *not* limited by it. **Worth checking how many of the ~36 denials went to
Australian addresses.** Known so far: #7323, #7885, #7663.

### 3.2 1,170 orders have a paid line item that was never delivered

```
PARTIALLY_FULFILLED:  1,170 orders   (EXACT)
Total orders:         7,561          (EXACT)
```

**Every sixth order.** In a sample of the 50 oldest (all 6–13 June), the
outstanding line is the **digital guide "Why Your Dog Destroys Every Toy"** in
**49 of 50**. *Not extrapolated to all 1,170 — the sample is the oldest page of
the list, not a random draw.*

Three of these surfaced independently through customers writing about something
else entirely: **#7255, #6254, #6528**. **None of them knew.** Not one of the
1,170 has ever been reported through the support inbox.

**Next step:** check whether the guide was ever delivered automatically at all.
If a digital-delivery app is missing or was never configured, that explains
every case at once.

### 3.3 The business address is published — #7479 can be answered

The shop's own Terms of Service state, twice:

> **Chiara Marasa, trading as Paw-Friends.uk**, Kirchstrasse 2, 56753 Mertloch,
> Germany · +49 175 2437033

**#7479 Richard Bellamy-Williams** demanded the trading address *"should it be
required for subsequent service"* and was given nothing, because until
yesterday "Kirchstr. 2" was only a fulfilment field. **It is now confirmed as
the shop's own published trading address.** Nobody has been given it from here
— but you can now point him at a public page instead of staying silent.

**Two things in the live published terms worth your attention:**
1. An unfinished editorial note is visible to customers: *"No commercial
   register number or VAT identification number is stated because none has been
   provided. If you have either number, it must be added where legally
   required."*
2. Governing law is Germany while the shop trades as `.uk`. **No legal
   assessment is offered here** — it is recorded, not evaluated.

---

## 4. Escalated — Owner Attention (32)

### Deadlines

| Expires | Case | Announced |
|---|---|---|
| **EXPIRED 15.09. 12:38** | **#6877 Alexander Meza** | FTC, Meta, chargeback — **passed with no visible reply** |
| **EXPIRED 15.09. ~19:30** | **Stephen Board** | Payment withdrawal, report to Facebook — **passed with no visible reply** |
| **17.09.** | #7699 Lorraine Sale | her own deadline |
| **21.09.** | #7479 Richard Bellamy-Williams | then regulators |
| **22.09.** | **#7323 David Buckley** | ASA + Citizens Advice / Trading Standards |
| **22.09.** | #1998, #4975 | — |

### Two live negotiations the shop itself opened

| # | Customer | State | Next step |
|---|---|---|---|
| **#5973** | Stephen Cooil | 30% (13.09.) → **40% (15.09.)** → he asks **50%**. **The gap is £2.99.** He has an **unopened Donkey**; his return question of 11.09. is still unanswered. Media announcement standing. | **Close it.** Three days of haggling over three pounds. |
| **#6528** | Tommy Johnson | **Asked four times** (9th, 10th, 12th, 14th) how to return **three unopened toys in original packaging**, citing your own policy. He **accepts** the denial for the used one. Offered 30% instead of an answer; now prefers **returning them**, or 75%. | **His 75% equals three of four toys.** Decide: return route, or the figure. |

### Consumer-law citations

**#7663 McLean** (AU, see 3.1) · **#1998 Bizzios-O'Connell** (formal CRA 2015
rebuke; callback promised 17.07., never made) · **#7479 Bellamy-Williams**
(CRA 2015 + E-Commerce Regs; kept advertising copies, site scrape, domain
records) · **#7292 hartley** (four requests for the citation)

### Public review / authority announced

**#7323 Buckley** — cites the public Trustpilot profile (his figures: 1.2/5,
99% one-star; **not verified from here**) and recognises the pattern from
outside. **#7988 Cooke**, **#7832 Shakeshaft** — both found the reviews after
buying; #7832 quotes **"anti-tear"** and **"double stitching"**, and **both are
verbatim in the Plushies description — the first customer quote that matches
the shop word for word.** **#7610 Blow**, **#7001 Furman** (will repeat his
complaint under any social ad).

### Disputed advertising claims

**#7147 Walley**, **#7347 Hibbs**, **#7114 Russell** (third contact in 26h,
third separate thread), **#6835 Allen**, **#7937 Allaton**, **#4975 Futrel**
(fourth attempt), **#6936 Steggel**, **#7401 Lacey**, **#7754 Timmings**,
**#7568 Preston**, **#7712 Cocks**, **#7627 Matthews**, **#6254 Hickman**,
**#7255 Crum**, **#7587 Hines**, **#7885 McNess**.

**#7001 Keith Furman** deserves reading in his own words — the sharpest
objection anyone has made: *"There could never be a return because you need to
open the packaging to see if the dog will destroy the toy."* The draft neither
refutes nor concedes it; it says plainly there is no good answer from here.

### Safety reports (3)

**#7323** (stuffing being pulled out, "unsafe for continued use"),
**#1084 Foley** (swallowed piece, **unanswered 78 days**, and the 15.09.
template denial does not mention it), **#7164 Dunster**. **Nothing has been
said about product safety in either direction, and no photo or video was
opened.**

### Data protection held (3)

**Jim Wigo** — sender address on no order; a name match exists in the shop and
**was neither confirmed nor hinted at**. **#7298**, **#8359** — same line.
Also: **Wigo's earlier request is nowhere in this mailbox** (`in:anywhere`
searched). **There is an inbound channel this bot cannot see.**

### Not a customer

**`wixassesmentteam@gmail.com`** — poses as "Wix Technical Support" although
the shop runs on Shopify, names no URL or trademark, and only wants a call with
a "lead developer". **Second pretexting attempt after 06.09. Not answered,
nothing released, no link opened.** `bradleybosun1@gmail.com` — service pitch.

---

## 5. Needs Approval (5)

| # | Customer | What is needed |
|---|---|---|
| **#6804** | Jill Brown | Toy destroyed in 3 minutes; asks how to get a refund. **Whether the second toy is unopened is not stated** — the draft asks rather than assumes. |
| **#6599** | Annette Townsend | Reports only, **asks for nothing**. One of two toys damaged. Yes/no on a refund. |
| **#7048** | Josephine Carr | Goods unused by her own account, size complaint. **£27.95.** |
| **#7865** | Talia McClenahan | Seam possibly split on arrival → would be a rule case. Her answer decides it. |
| **#8517** | — | Card details offered by email. The draft declines them. |

## 6. Draft Ready (2)

**#8267 Sharon Brinson** and **#8321 Darren Calver** — both answerable in full
from ship date, carrier, tracking number and link. No decision needed.

---

## 7. Standing blockers

1. **No returns address. 35 days. Ten customers have now asked** — #7525,
   #6869, #7298, #7660, #5973, #7048, #7255, #6254, #6528, #6804. **Not one
   could be answered.** Every affected draft warns the customer **not** to post
   anything, so nobody pays postage for a parcel with nowhere to arrive.
2. **"Indestructible" is in none of the nine product descriptions** — the whole
   catalogue is now checked — while **twelve customers quote it.** Sources they
   name: **Facebook** and a **promotional video**, neither visible from here.
3. **Five currency mismatches** (#7368, #7581, #4975, #7001, #6804): GBP in
   Shopify, USD on the confirmation. **Not bridged.** It still blocks the
   #7060 payout.
4. **`create_draft` is blocked** — 21 consecutive failures, each restarting the
   worker. **All 34 drafts live in the repo, none in Gmail.** The Gmail label
   tools are blocked too, which is why handled threads keep resurfacing unread.

---

## 8. One correction

**#5973 arrived at 16:35 and was missed by two consecutive runs.**
`search_threads` shows only the five *oldest* messages per thread and marks no
truncation; that thread now has nine. The pitfall has been documented in this
log since 13.09. and I walked into it anyway. **Delay: about three hours.**
Procedure changed: any thread showing five or more messages in the preview is
now opened with `get_thread` before being marked as already seen.
