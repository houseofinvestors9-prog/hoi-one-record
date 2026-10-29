# Data model

The full machine readable schema for the engine is in
[`schema/hoi-lead-engine.entities.json`](../schema/hoi-lead-engine.entities.json),
49 entities, exported from production on 29 October 2026. No records, schema only.

## The spine

```
ClientCounter ── issues ──> client_id  (HOI-009100)
                                │
                                ▼
                              Lead  (135 fields)
                                │
        ┌───────────────┬───────┼────────┬──────────────┬─────────────┐
        ▼               ▼       ▼        ▼              ▼             ▼
    Activity      LeadBudget  Visit   Booking      LeadTransfer   LeadHistory
  every contact    stated vs  site    cheques,     who owned it   the spreadsheet
   and outcome     revealed   visit   units, state   and when      row it came from
```

`client_id` is the thing that makes this work. It is issued once, by a counter, and never
reused. 6,415 of them were assigned during the backfill on 6 October 2026, which is how
legacy spreadsheet rows became records with an identity. `LeadHistory` keeps the original
sheet row, tab and file it came from, so a claim can always be traced back to the paper
it arrived on.

## What the family record carries

Grouped, because 135 fields listed flat is not readable.

| Group | Examples |
|---|---|
| Identity | `client_id`, `phone`, `alt_phone`, `name`, `is_nri`, `country_code` |
| Where they came from | `source`, `ad_campaign_name`, `adset_name`, `ad_name`, `ad_platform`, `is_organic`, `source_form` |
| What they want | `req_budget_min/max`, `req_size_min/max`, `req_bhk`, `req_purpose`, `req_timeline`, `locality_preference` |
| Who owns them | `owner_member_id`, `assigned_to_id`, `handlers`, `escalation_chain`, `transfer_count` |
| What happened | `first_call_date`, `call_attempts`, `site_visit_date`, `last_note`, `last_activity_date` |
| How good a fit | eight `score_*` fields plus `score_total`, `score_category`, `heat_manual` |
| Money | `booking_state`, `booking_date`, `booking_units`, `booking_via_cp`, `booking_cp_firm` |
| Coming back | `first_enquiry_date`, `reenquiry_date`, `project_history` |
| Consent | `wa_opt_out`, `wa_opt_out_at`, `ai_do_not_call` |

The consent group is small and it is load bearing. A record that follows a family for
years has to carry the family's right to be left alone.

## Attribution, which is the hard part

On the partner desk, `Lead` carries five fields that settle money:

| Field | Meaning |
|---|---|
| `attribution_status` | `owner`, `duplicate`, `contested`, `lost`, `lapsed` |
| `attribution_until` | the date the claim expires, set from the project's window |
| `contested` | two firms have a genuine claim |
| `contest_winner_lead_id` | which claim won |
| `contest_resolved` | an admin has decided |

The rule is simple and written down in advance, which is the only reason it holds:
first registration owns the buyer for the project's attribution window, default 90 days.
A later registration of the same number is marked `duplicate` automatically. Where both
firms have a real claim the record is marked `contested` and an admin decides, with the
decision written to `AuditLog`.

24 duplicates have been caught this way. 3 went to arbitration.

Before this existed the same disputes happened. They were settled on WhatsApp, by
whoever argued hardest, and nobody wrote down the outcome.

## Row level security

Not decorative. Declared per entity and enforced by the platform.

- A partner reads only rows where `owner_id` is their own user id.
- `Unit.linked_lead_name` is readable by admin, sales and builder roles, and by nobody
  else. A competing partner can see that a unit is taken. They cannot see who took it.
- `AuditLog` is create and read only. No role can update or delete it, including admin.

That last one is the difference between a log and a story.

## Sri Aditya Lead Desk, 11 entities

`Company`, `Partner`, `Lead`, `LeadActivity`, `Project`, `Unit`, `EOIRecord`, `Cheque`,
`AuditLog`, `AppSetting`, `User`.

`Project` carries the pricing engine: base rate, launch rate, floor rise per floor,
east facing premium, corner premium, duplex rate, three car parking tiers, clubhouse,
membership, water meter, bank and legal charges, maintenance per sft, corpus per sft,
GST. Retired fields are kept and labelled as retired with the date, rather than deleted,
so an old quote can still be reproduced.

`Unit` moves through `Available`, `EOI`, `Cheque Received`, `Confirmed`, `Blocked`, and
carries `condition` of `Standard`, `Mortgaged` or `Duplex`. The `Mortgaged` condition
exists because units pledged to a bank are not freely sellable, and a partner quoting one
as available is a problem that has to be caught in the inventory, not in a conversation.
