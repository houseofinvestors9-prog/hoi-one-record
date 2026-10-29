# Architecture

## The two loops

```
        THE FAMILY LOOP                                 THE BUILDER LOOP

  hyderabad.properties                                      Builders
  "is this project safe?"                           they give us homes to sell
          |                                                     |
          v                                                     v
    Wealth Snapshot          ---- ready buyer ---->      Lead Desk and Partners
  "what do I own, what next"                        <--- homes to sell ----
          ^                                        our team and 234 partner firms
          |                                         find the right home
        Ratio                                                   |
  family tracks every                                           v
  property with us                                       Control Room
          ^                                        builder sees every booking live
          |                                                     |
          +------------- buyer joins -------------------------- +
                                                      good results bring
                                                      the next project
```

Underneath both loops sits one table. A family gets a client id the first time it
touches any surface. Everything after that is written against that id.

## The six systems

### 1. hyderabad.properties — the public trust layer
Next.js App Router, Postgres with Drizzle, Anthropic SDK, deployed public.

Reads government records nobody reads: TG-RERA registrations and orders, TS-bPASS and
HMDA permits, HYDRAA lake boundaries, IGR guideline values. Detects change by hashing
page text, so a portal redesign does not break it. Claude reads newly linked PDFs and
extracts fields with a confidence label. Nothing publishes until a person approves it on
the review desk.

This is the only surface a stranger can use without logging in. It is also a lead source
into the engine, carried as project code `HP`.

### 2. HOI Lead Engine — the record itself
Base44. 49 entities. The `Lead` table has 135 fields and is the family record.

What it holds beyond contact details: the ad campaign, adset and creative the family came
from; every call, its outcome and who made it; site visit scheduling and who confirmed;
budget as stated and budget as revealed; a fit score across eight dimensions; booking
state, cheques and cancellation; re-enquiry dates; WhatsApp opt out; and the chain of
every executive who has ever owned the record.

Around it: a routing rota that assigns by project and weight, a scorecard that computes
daily call and meeting points, targets per person per month, attendance with geofencing
and hardware-backed punch keys, and an intelligence run that produces content drafts from
the week's market signals.

### 3. Sri Aditya Lead Desk — the partner surface
Base44. 11 entities. Where 234 partner firms register the buyers they bring.

The hard part is not the form. It is attribution. A partner registers a buyer and owns
that buyer for a set window, recorded as `attribution_until`. If a second partner
registers the same phone number, the record is marked `duplicate` and the earlier one
holds. If both have a genuine claim, it becomes `contested`, and an admin arbitrates with
the decision written to an audit log rather than settled in a WhatsApp argument.

Row level security is real here, not decorative. A partner reads only their own leads.
The buyer's name on a unit is readable by admin and sales and the builder, and by nobody
else.

It also carries the pricing engine: floor rise per floor, east facing premium, corner
premium, duplex rates, three car parking tiers, clubhouse, corpus, maintenance, GST. The
quote a partner gives is the quote the builder set, because it is computed from one place.

### 4, 5. Partner Hub and Oxygen Forest Partner Desk
Onboarding, RERA capture, approval state and project material for partner firms.

### 6. Wealth Snapshot
The family facing view. What it owns, what it is worth, what to do next.

## Why this is a workflow and not an agent

The nightly and per-event work is a fixed pipeline with known inputs and outputs. It does
not need open ended exploration. Claude is called at the stages where judgement is
actually required: reading a government PDF, scoring a lead's fit, drafting content from
signals. Everywhere else the system is deterministic, inspectable and replayable.

The one place a human is always in the loop is publication. No verdict about a builder's
project reaches the public site without a named person approving it, because the cost of
being wrong in public about somebody's project is a defamation suit, not a bad metric.
