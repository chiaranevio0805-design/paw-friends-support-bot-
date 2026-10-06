# Paw Friends — daily support report, Tuesday 6 October 2026

**Compiled 08:15 UTC from `docs/2026-10-05-backlog-triage.md` and
`docs/2026-10-06-backlog-triage.md`. No Gmail draft was created — see the end
of this report for why.**

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

**The zeros are not a quiet inbox. They are a loss of access.**

**Since 4 October 19:20 UTC the Gmail connection has pointed at the owner's
personal mailbox (`chiaranevio0805@gmail.com`) instead of
`support.pawfriends.uk@gmail.com`.** **Thirty-five consecutive runs have now
been logged without access** — all of 5 October (24 runs) and 00:20 to 07:20
on 6 October. **The support mailbox has been unattended for about 37 hours and
I cannot say what arrived in that time.**

While the connection is wrong I do not triage the personal mailbox, do not
open anything in it, and do not create Gmail drafts in it.

## 2. Nothing new to approve or escalate — but five cases are still waiting

**These came in on 4 October before access was lost. None of them has a
draft, because none could be written. They are now two days old.**

| Case | What is open | Recommended next step |
|---|---|---|
| **`richard@brownwolf.net`** | 30 → 50 → 60 → **70 %** offered, all declined; goods unopened; relies on "no-quibble"; asked for the business address | **Owner decision on a full refund.** Nothing from this desk can settle it. |
| **#7347 Jill Hibbs** | asking since **24 September** for return details; 4 October: *"I just want a full refund once I have returned it!"* | **A returns address, or a refund without return.** She cannot comply with a condition that has no address. |
| **`laceymick31@gmail.com`** | 30 September: *"you sent him a new toy free of charge, can you explain why you do that for one and not for me?"*; cites UK consumer law | **Owner must establish whether a free replacement was in fact given**, and to whom. First concrete sign of one. |
| **#7982 Rod O'Donnell** | received the intake template on 4 October; relies on "indestructible" and consumer law | **Owner decision**; the advertising finding applies. |
| **Nigel Bennett** | second contact, 4 October: stuffing out, *"Please advise."* | **A reply at all.** **He raised no safety concern and none is to be imputed to him.** |

**Also still open and unchanged from the 5 October evening report:** 362
current drafts in `docs/entwuerfe-zum-kopieren.md`, of which **83 are blocked**
by the advertising correction and **5** by send-stops; **13 confirmed
"processed" letters** with no payment traced, plus #6583 and #2894; **5 open
safety reports**; **4 proven duplicate letters**; **6 non-delivery cases**;
**3 unexecuted cancellations**.

## 3. Refunds issued

**None.** No case in the last 24 hours meets the refund rule, and no refund,
cancellation or order change was made in Shopify. Shopify has required
re-authentication since 1 October 17:20 UTC (sixth day); `refundCreate` and
`orderCancel` are blocked in any case. **`switch-shop` is deliberately not
called — it would revoke the existing token.**

## 4. What the owner needs first

1. **Put the Gmail connection back on `support.pawfriends.uk@gmail.com`** — and
   check whether the switch was intended. **If it was not, this is an access
   incident**; the 26 September passkey alert is still unchecked.
2. **Stop the parallel sending, or tell me who is doing it.** Four letters left
   the support mailbox without me on 4 October; the earliest evidence of
   outbound customer mail bypassing this mailbox is **2 July**, from the
   personal account.
3. **#8764 Craig Wren** — the deadline he set has been running since 2 October.
4. **Look at the three threads where the support address is a co-recipient**,
   in particular the card dispute with the bank in the address field.
5. Re-authenticate Shopify; decide 14 versus 30 days and whether "unused" is a
   condition; give a returns address or refund without return; pay or withdraw
   the 13 "processed" confirmations; answer the five safety reports; open the
   three advertising attachments.

---

## Why no Gmail draft was created

**The routine asks for a `create_draft` to `nevio.marasa@icloud.com`.** **I did
not create it, deliberately: the connection points at the owner's private
mailbox, so the draft would be written into a private account this task does
not cover.** **The report is delivered in chat instead, and the draft will be
created as soon as the connection is correct.**

**Still outstanding from before: the report prepared on 4 October
(`docs/2026-10-04-daily-report-en.md`) was never delivered. That was my
failure, not a tool failure. The file is in the repository.**
