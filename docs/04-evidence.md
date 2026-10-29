# Evidence

Everything below was read from the live production databases on **29 October 2026**.
Nothing here is an estimate unless it says so.

## How each number was read

Two apps were queried through the Base44 MCP interface, as the authenticated owner,
read only. Two methods were used.

**Exact count.** The query returns fewer records than the page limit of 500, so the
returned count is the true total.

**Bounded by probe.** For entities larger than 500 rows, the API pages at 500 and offers
no count endpoint. Instead the query was repeated with `limit: 1` and an increasing
`skip`. An empty result means the total is below that offset. Three or four probes
bracket the real number. These are reported as ranges, not as single figures, because a
range is what was actually established.

---

## HOI Lead Engine
`hoi-lead-flow.base44.app` · app id `6a8558145fe1f9a3e43b5482` · 49 entities

| Fact | Value | Method | Source |
|---|---|---|---|
| Client IDs issued | 9,100 | exact | `ClientCounter.value` where `key = "lead"` |
| Legacy records backfilled | 6,415 | exact | `ClientCounter.backfill_end` |
| Backfill cutoff | 2026-10-06T13:27:20Z | exact | `ClientCounter.backfill_cutoff` |
| New families since cutoff | 2,685 over 23 days | derived | 9,100 − 6,415 |
| Contacts logged | 30,000 to 40,000 | probe | `Activity`, empty at skip 40000, non-empty at 30000 |
| Legacy sheet rows reconciled | 3,500 to 4,000 | probe | `LeadHistory` |
| Ownership transfers | 1,000 to 1,500 | probe | `LeadTransfer` |
| Site visits scheduled | 420 to 500 | probe | `Visit` |
| Bookings | 74 | exact | `Booking` |
| Team members | 27 | exact | `TeamMember` |
| Projects | 10 | exact | `Project` |
| Fields on the family record | 135 | exact | `Lead` entity schema |

Team roles present: founder, admin, project_head, bdr, site_executive, marketing.

Projects: Terrace 35, Oxygen Forest, Aranya Chevella, SRIAS, Kollur, Prestige Clairemont
(active); DSR CIEL, Elite, UAE Expo (soft launch); hyderabad.properties (carried as a
lead source, code `HP`).

That last row matters. The public safety checker is wired into the same engine as a
source, which is the point of the loop.

## Sri Aditya Lead Desk
`aditya-lead-desk.base44.app` · app id `6a2a7979a089504da797f9b6` · 11 entities

| Fact | Value | Method | Source |
|---|---|---|---|
| Leads registered by partners | more than 2,000 | probe | `Lead`, non-empty at skip 2000 |
| Partner registrations | 234 | exact | `Partner` |
| Duplicates caught | 24 | exact | `Lead` where `attribution_status = "duplicate"` |
| Disputes arbitrated | 3 | exact | `Lead` where `contested = true` |
| Expressions of interest | 31 | exact | `EOIRecord` |

Of the 234 partner registrations, most are approved firms. A handful sit pending and two
are suspended. The company's own public figure is 195 partners, which is the count of
distinct approved firms after duplicates in company naming are merged.

## hyderabad.properties
Next.js, Postgres, Anthropic SDK. 23 commits, repository already exists.

Sources ingested: TG-RERA project registry and orders, TS-bPASS and HMDA and GHMC
permits, HYDRAA and irrigation full tank level polygons, IGR guideline values.

Change is detected by content hash. New PDFs are read by Claude. Nothing reaches the
public site until a person presses approve on the review desk.

---

## What is not measured yet

Say this plainly rather than dress it up.

1. **Minutes saved per family.** No before figure was recorded. The method to get one is
   in [06-validation.md](06-validation.md) and takes about a day.
2. **Dispute rate before the system.** 24 duplicates and 3 disputes are what the system
   caught. What partners were arguing about before it existed was never counted, because
   nobody was counting.
3. **Revenue attributable to the system.** 74 bookings are on the record. How many of
   those would have closed anyway is not known and should not be claimed.

The honest claim is the one the data supports: 9,100 families that used to live in
spreadsheets now have one record each, 234 partner firms work against that record, and
the arbitration that used to be an argument on WhatsApp is now a decision with a log.
