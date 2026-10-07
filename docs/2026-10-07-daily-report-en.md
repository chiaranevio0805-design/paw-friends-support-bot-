# Paw Friends — daily support report, Wednesday 7 October 2026

**Compiled 08:14 UTC from `docs/2026-10-06-backlog-triage.md` and
`docs/2026-10-07-backlog-triage.md`. No Gmail draft was created — reason at
the end.**

---

## 1. Counts for the last 24 hours

| Category | Count |
|---|---|
| Draft Ready | **0** |
| Bot/Needs Approval | **0** new |
| Bot/Escalated — Owner Attention | **0** new |
| No Action | **0** |
| Customer messages read | **0** |
| Drafts written | **0** |
| **Refunds actually issued (rule 4, wrong item)** | **0** |
| Emails sent by me (all time) | **0** |

**Third calendar day with every category at zero, and the reason has not
changed: since 4 October 19:20 UTC the Gmail connection points at the owner's
personal mailbox (`chiaranevio0805@gmail.com`) instead of
`support.pawfriends.uk@gmail.com`.**

| | |
|---|---|
| 5 October | 24 runs, **0** with access |
| 6 October | 20 runs, **0** with access |
| 7 October to 07:20 | 8 runs, **0** with access |
| **Consecutive runs without access** | **59** |
| **Support mailbox unattended** | **about 60 hours** |

**I cannot say what has arrived in those 60 hours.** While the connection is
wrong I do not triage the personal mailbox, do not open anything in it, and
do not create Gmail drafts in it.

**This report will keep saying the same thing until the connection is put
back. That is not a technical nuisance — it is three days of customer mail
nobody has looked at.**

## 2. Nothing new to approve or escalate — the same five cases are waiting

**They arrived on 4 October before access was lost. None has a draft, because
none could be written. Today is their third day.**

| Case | What is open | Recommended next step |
|---|---|---|
| **`richard@brownwolf.net`** | 30 → 50 → 60 → **70 %** offered, all declined; goods unopened; relies on "no-quibble"; asked for the business address | **Owner decision on a full refund** |
| **#7347 Jill Hibbs** | asking since **24 September** for return details; 4 Oct: *"I just want a full refund once I have returned it!"* | **A returns address, or a refund without return** |
| **`laceymick31@gmail.com`** | 30 Sept: *"you sent him a new toy free of charge, can you explain why you do that for one and not for me?"*; cites UK consumer law | **Establish whether a free replacement was in fact given, and to whom** |
| **#7982 Rod O'Donnell** | got the intake template on 4 Oct; relies on "indestructible" and consumer law | **Owner decision**; the advertising finding applies |
| **Nigel Bennett** | second contact, 4 Oct: stuffing out, *"Please advise."* | **A reply at all.** He raised no safety concern and none is to be imputed to him |

**Also open, unchanged:** **nine drafts whose full wording is in
`docs/2026-10-05-abendreport.md`** (#6384 — blocked by the advertising
correction —, #8712, #7292, #5310, #5829, #7440, #4071, #4919, Tamara
Heathcote); **362 current drafts** in total, of which **83 blocked** by the
advertising correction and **5** by send-stops; **13 confirmed "processed"
letters** with no payment traced, plus #6583 and #2894; **5 open safety
reports**; **4 proven duplicate letters**; **6 non-delivery cases**; **3
unexecuted cancellations**.

**🟥 #8764 Craig Wren: the deadline he set himself has now been running since
2 October — five days.**

## 3. Refunds issued

**None.** No case meets the refund rule; no refund, cancellation or order
change was made in Shopify. Shopify has required re-authentication since
1 October 17:20 UTC (seventh day); `refundCreate` and `orderCancel` are
blocked in any case, and `switch-shop` is deliberately not called because it
would revoke the existing token.

## 4. What the owner needs first

1. **Put the Gmail connection back on `support.pawfriends.uk@gmail.com`** — and
   check whether the switch was intended. **If it was not, this is an access
   incident**; the 26 September passkey alert is still unchecked.
2. **#8764 Craig Wren — his deadline has run five days.**
3. **Stop the parallel sending, or tell me who is doing it.** Four letters left
   the support mailbox without me on 4 October; the earliest evidence of
   outbound customer mail bypassing this mailbox is **2 July**.
4. **Look at the three threads where the support address is a co-recipient**,
   in particular the card dispute with the bank in the address field.
5. Re-authenticate Shopify; decide 14 versus 30 days and whether "unused" is a
   condition; give a returns address or refund without return; pay or withdraw
   the 13 "processed" confirmations; answer the five safety reports; open the
   three advertising attachments; have the "twelve product texts" sentence
   struck from the 83 blocked drafts.

---

## Why no Gmail draft was created

**The routine asks for a `create_draft` to `nevio.marasa@icloud.com`.** **I did
not create it, for the third day and for the same reason: the connection
points at the owner's private mailbox, so the draft would be written into a
private account this task does not cover.** **The report is delivered in chat
instead, and the draft will be created as soon as the connection is correct.**
