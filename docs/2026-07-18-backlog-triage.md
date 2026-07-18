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

## Run 2 (hourly check-in, ~20:50 UTC)

Found a much larger backlog than the first pass — 21 unread threads. Two
were already labeled from Run 1 but resurfaced due to a query bug (see
runbook fix below). 13 were genuinely new. All actions are drafts only;
no refunds were issued.

| Thread | Sender | Order | Classification | Action | Label |
|---|---|---|---|---|---|
| "Chewed item" | Gary Sanderson | — | Not a refund request — proactive feedback on a stitching weakness, dog still enjoys the toy | Drafted warm thank-you, no refund needed (none requested), noted the product-design feedback (reinforce leg stitching) | `Bot/Draft Ready` |
| "Broken toys" | booboos.uk@gmail.com | — | Rule 1 — chewed, no defect claim, cites site's "long lasting" claim | Drafted friendly no-refund reply | `Bot/Draft Ready` |
| "FULL REFUND RETURN REQUEST" | Do Robinson | #1915 | Rule 5 — unused, original packaging, **first requested 10 July (20 days after the 16 June order, within window)**; two prior replies wrongly treated this as a shipping-delay question, not a return | Drafted corrected return-instructions reply, apologising for the misclassification | `Bot/Needs Approval` |
| "Order 1218" | Niki Curtis | #1218 | Rule 5 — "not fit for purpose," **first requested ~1 July (20 days after the 11 June order, within window)**; repeatedly misclassified as shipping delay across 4 weeks; order is now PARTIALLY_FULFILLED (unrelated to her complaint, not investigated further) | Drafted corrected return-instructions reply | `Bot/Escalated - Owner Attention` (repeat unresolved contact, 4+ weeks) |
| "Order 1135" | Alan Crump | #1135 | **New escalation trigger: broken promise.** A 50% refund was offered and accepted (2 July), a later reply then said no refunds on used items, the refund was never paid, and Alan quoted the contradiction back to us, threatening negative reviews and to flag Facebook ads | Drafted honest, non-templated acknowledgment; makes no new promises; **flagged directly below for the owner** | `Bot/Escalated - Owner Attention` |
| "Return of toys" | Darren Lockwood (daz.38) | — | Escalation trigger: **active credit-card chargeback already filed**, hostile/abusive language, Trust Pilot citation | Drafted brief, calm closing reply; no action requested of customer | `Bot/Escalated - Owner Attention` |
| "IMPORTANT MESSAGE" | vfiyinfunoluwa@gmail.com | — | Not a support case — asks "who owns this store?" with no context. Sender pattern and vague/urgent subject line look like a phishing or social-engineering probe | Drafted a minimal reply that reveals no owner/personal information; asked what it's regarding | `Bot/Escalated - Owner Attention` (security awareness, not a refund matter) |
| "#1173" | Darren Smith | #1173 | Resolved — misdelivery investigation from Run 1's predecessor thread; customer confirmed satisfaction ("that is great thank you") | No reply needed | `Bot/No Action` |
| "Dog toys" | Derek Thomson | — | Resolved — order arrived, customer happy, no complaint | No reply needed | `Bot/No Action` |
| "Missing parcel" | maureenbear27 | — | Resolved — "my parcel arrived yesterday" | No reply needed | `Bot/No Action` |
| "Order #1826" | Sue Richards | #1826 | Resolved — "it has now arrived" | No reply needed | `Bot/No Action` |
| "Order" | Paula Solieri | — | Informational — order arrived (after a prior lost-parcel report), toy destroyed by dog, but no refund requested | No reply needed | `Bot/No Action` |
| "Poor Quality order 1411" | pevreallm | #1411 | Resolved — "that's great, thank you very much" | No reply needed | `Bot/No Action` |
| "Re: Your Store Has Been Selected for Expert Assistance" | shopifyrevenuefix@gmail.com | — | Vendor spam solicitation, not a customer | No reply | `Bot/No Action` |
| Klaviyo renewal notice, 2x Google account-security notices | — | — | Not customer emails | No reply | `Bot/No Action` |

### Runbook bug fixed this run

The "find new mail" search query didn't quote multi-word labels
(`-label:Bot/Draft Ready` instead of `-label:"Bot/Draft Ready"`), so Gmail
tokenized it as an exclude on `Bot/Draft` plus an unrelated `Ready` search
term — already-labeled threads from Run 1 kept resurfacing as "new."
Fixed in `docs/runbook.md`.

## Three items that need the owner directly, this run

- **Alan Crump (#1135) — broken promise, top priority.** A 50% refund was
  explicitly offered and accepted in writing, then a later reply
  contradicted it and said no refund was possible, and the money was never
  paid. He's now quoting our own words back at us and threatening to flag
  every Facebook ad with a negative review. This needs the owner to either
  actually pay the 50% refund that was already promised, or personally
  explain why not — another bot-drafted reply would make this worse, so
  the draft only acknowledges the situation and does not repeat a promise
  or a denial.
- **Darren Lockwood / daz.38 (Return of toys) — active chargeback.** Has
  already disputed with his card provider. Worth pulling together order,
  tracking, and correspondence evidence for the chargeback response
  regardless of what happens with the email thread.
- **Do Robinson (#1915) and Niki Curtis (#1218) — process gap, not just
  these two.** Both had straightforward, clearly-within-window return
  requests that got auto-replied with an unrelated "your order is on its
  way from our international warehouse" shipping-delay template, for
  weeks, before either customer could get a human to notice they'd asked
  for a *return*, not a delivery update. That's a systemic issue with
  however replies were being triaged before this bot existed, not just
  bad luck twice — worth checking whether other closed/trashed threads
  have the same mismatch.
