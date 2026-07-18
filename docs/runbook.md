# Runbook — support inbox check-in

This is the procedure each scheduled check-in follows (see "Scheduling" in
the main README for how often it actually runs, and why not every 5
minutes). It's written to be run by Claude with the Gmail and Shopify MCP
tools connected, against the `support.pawfriends.uk@gmail.com` inbox and
the Paw-Friends.uk Shopify store.

## Each run

1. **Find new mail.**
   `search_threads` with `in:inbox is:unread -label:"Bot/Draft Ready"
   -label:"Bot/Needs Approval" -label:"Bot/Auto-Resolved"
   -label:"Bot/Escalated - Owner Attention" -label:"Bot/No Action"` —
   **quote every multi-word label.** An unquoted `-label:Bot/Draft Ready`
   gets tokenized by Gmail as `-label:Bot/Draft` plus a stray `Ready` search
   term, which does *not* exclude already-labeled threads — this bug let
   already-triaged threads resurface as "new" on the second run
   (2026-07-18). Even with the query fixed, treat it as a filter, not a
   guarantee: cross-check each result's `labelIds` before treating it as
   new, since Gmail's matching is thread-level and can still surface an
   already-labeled thread that got a new message.

2. **Read each thread in full**, including prior messages in the thread
   (don't classify off the snippet alone — context from earlier replies
   matters, e.g. "have we already apologized for this delay twice?").
   `search_threads` truncates a thread's message list (seen: 5 of 7
   messages shown, 2026-07-18 run 4) — don't trust it as complete, even
   for a thread you've already touched before. Use `get_thread` with
   `METADATA_ONLY` (cheap, untruncated) to check for messages beyond what
   a prior run already saw before assuming there's nothing new.

3. **Look up the order** in Shopify (`get-order` by order number if the
   customer gave one, otherwise `list-orders` by customer email) before
   deciding rule 3, 4, or 5 cases — never guess shipping/fulfillment status
   from the email alone.

4. **Classify against `support-policy.md`.** Check the escalation triggers
   list first — if any apply, route to escalated regardless of which
   numbered rule would otherwise apply.

5. **Act:**
   - Rule 4 (confirmed wrong item): issue the refund via
     `graphql_mutation` (Shopify Admin API `refundCreate` — look up exact
     fields with `graphql_schema` first since input shape can change),
     draft a confirmation reply, label `Bot/Auto-Resolved`.
   - Everything else: draft the reply only (never send — there's no send
     tool), label `Bot/Draft Ready` or `Bot/Needs Approval` per the policy
     doc, or `Bot/Escalated - Owner Attention` if a trigger applies.
   - Not a support case at all (spam/vendor solicitation, account-security
     notices, or a thread that's already resolved/closed with nothing left
     to do): label `Bot/No Action` so it stops resurfacing, and don't draft
     a reply.

6. **Mark the message read** (`unlabel_message` with
   `labelIds: ["UNREAD"]`) once you've acted on it. A Bot label alone does
   not stop an already-handled message from resurfacing in the next run's
   `is:unread` search — Gmail evaluates unread status per message, and a
   thread-level label doesn't retroactively cover it. Discovered
   2026-07-18 run 3: six threads already drafted in earlier runs
   reappeared as "new" purely because their messages were still unread.
   Removing `UNREAD` after drafting is what actually stops the repeat
   processing; the label is for humans triaging the inbox, not for the
   bot's own dedupe.

7. **Log the action** by appending one line to that day's triage record
   (`docs/YYYY-MM-DD-backlog-triage.md`, create if it doesn't exist) with:
   thread subject, sender, classification, action taken, and (for
   approval/escalated items) the recommended next step for the human.

## Daily report

Once a day, compile the day's triage log into a summary: counts by
category, any refunds actually issued, and the full list of
`Needs Approval` / `Escalated` items with recommended actions. Since
there's no Gmail send capability, this can't be emailed automatically —
draft it via `create_draft` addressed to `nevio.marasa@icloud.com` (it
will sit in the connected Gmail account's Drafts, not arrive in the
icloud inbox, until someone sends it) or paste it directly into chat/a
repo file for the owner to read, whichever the owner prefers.

## Things this runbook deliberately does not do

- Auto-send any email.
- Auto-refund anything except a confirmed rule-4 wrong-item case.
- Repeat an identical "please wait" holding reply to the same customer a
  third time — that's an escalation trigger, not a rule-3 case.
- Invent order or shipping details not present in Shopify — if the order
  can't be found, that itself is a `Bot/Needs Approval` case.
