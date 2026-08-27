# Paw Friends Support Bot

Support-inbox triage for Paw Friends UK (`paw-friends.uk`). Reads incoming
customer emails, classifies them against the policy in
[`docs/support-policy.md`](docs/support-policy.md), and prepares the
appropriate action, following the operational steps in
[`docs/runbook.md`](docs/runbook.md).

## What this actually does, and what it doesn't

This was built inside a Claude Code environment against the Gmail and
Shopify connections available there. Two real limits shape the design —
read this before assuming it's a fully unattended system:

1. **No email-send capability.** The connected Gmail integration can create
   drafts but has no send tool. Every reply the bot writes lands in
   `support.pawfriends.uk@gmail.com`'s Drafts, labeled for triage — a human
   clicks send. This is true for *all* cases, including the "auto" tier
   below, not a limitation added for safety — it's just what the tool
   supports.
2. **No durable 5-minute cron.** The scheduler available for recurring
   automation has an hourly minimum interval, and nothing in this
   environment can run genuinely 24/7 unattended indefinitely. What's
   configured is an hourly check. If you need a real always-on, 5-minute,
   auto-sending pipeline, that requires different infrastructure (e.g.
   Shopify Flow, or a small server/cloud function using the Gmail API with
   send scope + a webhook or tight poll) — this repo's docs describe the
   logic that infrastructure would need to run, but nothing here executes
   it in the background 24/7 on its own.

**What *is* fully automatic:** Shopify refunds for the one clear-cut case
(wrong item delivered, rule 4) — refunds are a real, direct API mutation,
not a draft. See `docs/support-policy.md` for exactly which cases are
auto-refunded versus queued for approval, per the store owner's explicit
decision.

## Structure

- `docs/support-policy.md` — the classification rules, refund policy, tone
  and disclosure decisions. Source of truth for how "Lisa" replies.
- `docs/runbook.md` — the step-by-step procedure each check-in run follows.
- `docs/2026-07-18-backlog-triage.md` — record of the first backlog pass,
  including two items flagged for the owner rather than auto-handled.
- `docs/ads-launch-runbook.md` — Meta Ads Manager launch template: account,
  campaign and pixel IDs, the standard ad set/ad settings to clone, what
  the creative upload can and cannot accept, and the durability-claim
  warning that ties back to the business-risk flag below.

## Known business-risk flag (not a bot issue — flagging for the owner)

Multiple customers (Katy Markham #1329, Alan Crump #1135, and others)
describe the plushie toys as advertised "indestructible" on Facebook. That
alone could be dismissed as third-party ad copy the store doesn't fully
control. But as of 2026-07-19, **two more customers (Pat McCarty, Sarah
Goldring) independently say the durability claim came from "the
description"** — i.e. the Shopify product listing text itself, not an
external ad. That's a stronger signal: it points at the on-site copy, which
the owner directly controls, not just Facebook creative. The product's own
title is "Plushies – Designed for Furry Friends Who Destroy Everything,"
so there may be a live mismatch between that title and the body/description
copy on the same listing. One customer (Katy Markham) has also explicitly
invoked the UK Consumer Rights Act 2015 and referenced a pattern of similar
complaints on Trust Pilot. This is a marketing/legal question worth the
owner's direct attention, and now specifically worth checking the actual
live product description text — a support bot's refund policy can't paper
over a false-advertising claim, and no rule in the policy doc auto-resolves
it. See `docs/2026-07-18-backlog-triage.md` and
`docs/2026-07-19-backlog-triage.md` for the specific threads.
