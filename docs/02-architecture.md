# Architecture

## The two loops

```
        THE FAMILY LOOP                                 THE BUILDER LOOP

  hyderabad.properties                                      Builders
  is this project safe?                             they give us flats to sell
          |                                                     |
          v                                                     v
    Wealth Snapshot          ---- ready buyer ---->        Lead Desk
  what do I own, what next                          <--- flats to sell ----
          ^                                        our team and 234 firms
          |                                         find the right flat
        Ratio                                                   |
  family tracks every                                           v
  property with us                                       Control Room
          ^                                        builder sees every booking live
          |                                                     |
          +------------- buyer joins -------------------------- +
                                                      good results bring
                                                      the next project
```

Underneath both loops sits one table. A family gets an ID the first time it touches any
surface. Everything after that is written against that ID.

## The six surfaces

### hyderabad.properties, the public one
Next.js App Router, Postgres with Drizzle, Anthropic SDK. Open to anyone.

It reads the records nobody reads: RERA registrations and orders, TS-bPASS and HMDA
permits, HYDRAA lake boundaries, IGR guideline values. Change is detected by hashing page
text rather than by CSS selectors, so a portal redesign does not break the collector.
Claude reads newly linked PDFs and pulls fields out with a confidence label. Nothing
publishes until a named person approves it.

This is also a lead source into the engine, carried as project code `HP`.

### Lead Engine, the record itself
Base44. 49 tables. The `Lead` table has 135 fields and is the family record.

Beyond contact details it holds: the ad campaign, adset and creative they came from; every
call, its outcome and who made it; site visit scheduling and who confirmed it; budget as
stated and budget as revealed; a fit score across eight dimensions; booking state, cheques
and cancellation; re-enquiry dates; WhatsApp opt out; and the chain of every executive who
has ever owned the record.

Around it sits a routing rota that assigns by project and weight, a scorecard that computes
daily call and meeting points, monthly targets per person, attendance with geofencing and
hardware-backed punch keys, and an intelligence run that turns the week's market signals
into content drafts.

### Lead Desk, where the firms work
Base44. 11 tables. 234 partner firms register the buyers they bring.

The hard part is not the form, it is the commission claim. A firm registers a buyer and
owns them for a set window, stored as `attribution_until`. A second firm registering the
same number is marked `duplicate` and the earlier claim holds. Where both firms have a real
claim it becomes `contested`, and an admin decides, with the decision written to an audit
log instead of settled in a WhatsApp argument.

Row level security is doing real work here. A firm reads only its own rows. The buyer's
name on a flat is readable by admin, sales and the builder, and by nobody else, so a
competing firm can see that a flat is taken but not who took it.

It also carries the pricing engine: floor rise per floor, east facing premium, corner
premium, duplex rates, three car parking tiers, clubhouse, corpus, maintenance, GST. The
quote a firm gives is the quote the builder set, because it is computed from one place.

### Partner Hub and Oxygen Forest Desk
Onboarding, RERA capture, approval state and project material for firms.

### Wealth Snapshot
The family facing view. What they own, what it is worth, what to do next.

## Why this is a fixed pipeline and not an autonomous loop

The nightly and per-event work has known inputs and known outputs. It does not need
open-ended exploration. Claude gets called at the three places where judgement is actually
required: reading a government PDF, scoring a lead's fit, drafting content from signals.
Everywhere else the system is deterministic, inspectable and replayable.

One place always has a human in it. No verdict about a builder's project reaches the public
site without a named person approving it. Being wrong in public about somebody's project
carries legal exposure, so a person signs it.
