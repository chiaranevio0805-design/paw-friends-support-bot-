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
   list first — if any apply, route to escalated regardless of what the
   two-case guarantee rule would otherwise say.

5. **Act** (drafts only — there is no send tool, and no case is ever
   auto-refunded via Shopify under the current policy):
   - Damaged/defective, photo not yet provided: draft asking for a photo,
     label `Bot/Needs Approval`.
   - Damaged/defective, photo already confirms it: draft offering a
     replacement or refund, label `Bot/Needs Approval` (the actual refund
     is a manual Shopify action for a human, not this bot).
   - Unused item within 30 days: draft with the return address and next
     steps, label `Bot/Needs Approval`.
   - Everything else covered by the guarantee text (chew/play damage,
     dog doesn't like it, too small, change of mind, wear from use): draft
     the policy-explained decline, label `Bot/Draft Ready`.
   - Escalation trigger applies: draft starting with the
     `⚠️ MANUELLE PRÜFUNG - GRUND: [...]` line instead of a normal reply,
     label `Bot/Escalated - Owner Attention`.
   - A case the guarantee text doesn't name at all (wrong item, delayed
     shipment, pricing/promo question, etc.): don't invent a rule — draft
     an honest holding reply and label `Bot/Needs Approval`, flagging the
     gap for the owner.
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

6b. **Bei jedem Erstattungsfall den Betrag mitschreiben.** Sobald ein Fall
   unter die Erstattungsregel fällt (defekt angekommen, unbenutzt, vor
   Versand storniert), muss der Triage-Eintrag **Bestellnummer, Betrag und
   Kundenname** enthalten — der Abend-Report baut daraus die Liste
   "HEUTE ZU ERSTATTEN", und ohne Betrag im Log kann er sie nicht nennen.
   Betrag immer aus Shopify (`totalPrice`) übernehmen, nie aus der E-Mail
   des Kunden schätzen.

   Ein Fall bleibt in dieser Liste, bis er im Log ausdrücklich als
   erledigt markiert ist. Lieber zweimal genannt als einmal vergessen.

7. **Log the action** by appending one line to that day's triage record
   (`docs/YYYY-MM-DD-backlog-triage.md`, create if it doesn't exist) with:
   thread subject, sender, classification, action taken, and (for
   approval/escalated items) the recommended next step for the human.

## Daily report (owner update, 2026-08-07 — wanted every evening)

Once a day, compile the day's triage log into a summary containing:

- Counts by category.
- **What customers asked about most often that day**, grouped by theme
  (delivery delays, chew damage, returns, pricing, etc.) with rough counts
  — this is the part the owner most wants to see.
- **How the bot replied** to each theme, so the owner can spot a wording
  problem before it turns into a pattern of complaints.
- Any refunds or replacements actually actioned by a human.
- The full list of `Needs Approval` / `Escalated` items with recommended
  next steps.

Draft it via `create_draft` addressed to `nevio.marasa@icloud.com`, and
post the same summary into chat so the owner sees it without opening
Drafts.

**There is no send capability on the connected account** — the draft sits
in the support mailbox's Drafts folder and does *not* arrive in the iCloud
inbox until a human opens Gmail and presses send. The owner has asked to
"receive an email every evening"; that will only actually happen if someone
sends the draft, or the owner connects an account with send permission.
Don't describe the report as "sent."

## Things this runbook deliberately does not do

- Auto-send any email.
- Auto-refund anything, ever — every refund or replacement is a manual
  Shopify action a human takes after reviewing the draft.
- Reply a third time on the same case without escalating — a third email
  from the same customer on the same issue is itself an escalation
  trigger.
- Invent order or shipping details not present in Shopify — if the order
  can't be found, that itself is a `Bot/Needs Approval` case.
