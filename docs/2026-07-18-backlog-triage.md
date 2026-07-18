# Backlog triage — 2026-07-18

First run against the existing inbox backlog. 5 unread threads with real
customer content were found and processed. All actions below are **drafts
only** — nothing was sent, and no refunds were issued (none of today's
cases were confirmed rule-4 wrong-item cases).

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Indestructible toy" | Pat McCarty | #2679 | Rule 1 — dog destroyed toy, no defect claimed | Drafted friendly no-refund reply | `Bot/Draft Ready` |
| "Payment security question" | smithsofystorebuilder@gmail.com | — | Pre-sale question, not covered by the 6 rules | Drafted factual reply. **Sender address pattern looks like vendor/spam outreach, not a genuine customer — verify before sending.** | `Bot/Draft Ready` |
| "Important Update Regarding Your Order" | Alison Whybrow | #1208 | Rule 3, but escalation trigger: shipped 12 June (37 days ago), still not received, customer already given the same "please wait" reply 3 times | Drafted honest escalation reply offering reship-or-refund; **does not repeat the warehouse-delay excuse a 4th time**. Recommend: confirm with courier whether parcel is lost, then reship or refund per customer preference. | `Bot/Escalated - Owner Attention` |
| "RE: Order #1329" | Katy Markham | #1329 | Escalation trigger: cites Consumer Rights Act 2015, alleges pattern of unresolved Trust Pilot complaints, disputes "indestructible" advertising claim | Drafted honest holding reply that escalates to management without denying or promising a specific outcome. **Needs the owner personally — see README's business-risk flag.** | `Bot/Escalated - Owner Attention` |
| "REFUND REQUEST" | Joanne Hopkins | #2433 | Mixed: one item destroyed by dog in ~7 min (rule 1, no refund), one item unopened (rule 5, return-eligible — order is 23 days old, within 30-day window) | Drafted reply: no refund on destroyed item, refund recommended on the unopened one pending approval | `Bot/Needs Approval` |

## Two items that need the owner directly, not just approval-queue review

- **Alison Whybrow (#1208):** 5+ weeks since dispatch with no delivery and
  three prior "please wait" replies. This reads as a lost parcel. The
  draft reply commits to *a* resolution (reship or refund) but the owner
  needs to actually pick one and follow through — don't let this sit in
  Drafts.
- **Katy Markham (#1329):** Explicit Consumer Rights Act 2015 citation +
  claim of a Trust Pilot pattern of unresolved complaints about the same
  "indestructible" claim. This is a legal/marketing question (see README),
  not something the support policy can resolve on its own.
