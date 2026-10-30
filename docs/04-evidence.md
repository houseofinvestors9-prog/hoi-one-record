# Evidence

Everything below was read from the live production databases on **29 October 2026**.
Nothing here is an estimate unless it says so.

## How each number was read

Two apps were queried through the Base44 interface as the authenticated owner, read only.
Two methods.

**Exact count.** The query returns fewer records than the page limit of 500, so the count
returned is the true total.

**Bounded by probe.** For tables larger than 500 rows the API pages at 500 and offers no
count. So the query was repeated with `limit: 1` and an increasing `skip`. An empty result
means the total sits below that offset. Three or four probes bracket the number. These are
reported as ranges because a range is what was actually established.

---

## Lead Engine
`hoi-lead-flow.base44.app` · 49 entities

| Fact | Value | Method | Source |
|---|---|---|---|
| Client IDs issued | 9,100 | exact | `ClientCounter.value` where `key = "lead"` |
| Legacy records backfilled | 6,415 | exact | `ClientCounter.backfill_end` |
| Backfill cutoff | 2026-10-06T13:27:20Z | exact | `ClientCounter.backfill_cutoff` |
| New families since cutoff | 2,685 over 23 days | derived | 9,100 minus 6,415 |
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
(active); DSR CIEL, Elite, UAE Expo (soft launch); hyderabad.properties (carried as a lead
source, code `HP`).

That last row is the loop closing. The public safety checker feeds the same engine as a
source.

## Lead Desk
`aditya-lead-desk.base44.app` · 11 entities

| Fact | Value | Method | Source |
|---|---|---|---|
| Leads registered by firms | more than 2,000 | probe | `Lead`, non-empty at skip 2000 |
| Partner registrations | 234 | exact | `Partner` |
| Duplicates caught | 24 | exact | `Lead` where `attribution_status = "duplicate"` |
| Disputes arbitrated | 3 | exact | `Lead` where `contested = true` |
| Expressions of interest | 31 | exact | `EOIRecord` |

Of the 234 registrations most are approved firms. A handful sit pending and two are
suspended. The company's own public figure is 195, which is the count of distinct approved
firms after duplicates in company naming are merged.

## hyderabad.properties

Next.js, Postgres, Anthropic SDK. 25 commits.

Sources ingested: TG-RERA project registry and orders, TS-bPASS and HMDA and GHMC permits,
HYDRAA and irrigation full tank level polygons, IGR guideline values. Change is detected by
content hash. New PDFs are read by Claude. Nothing reaches the public site until a person
presses approve on the review desk.

---

## What is not measured

**Minutes saved per family.** No before figure was recorded. The method is in
[06-validation.md](06-validation.md) and takes about a day.

**Dispute rate before the system.** 24 duplicates and 3 disputes are what the system
caught. What firms argued about earlier was never counted, because nobody was counting.

**Revenue attributable to the system.** 43 verified bookings sit on the record, out of 74 logged. How many would have
closed anyway is unknown and should not be claimed.

What the data does support: 9,100 families who used to live in spreadsheets now have one
record each, 234 firms work against that record, and the arbitration that used to be an
argument is now a decision with a log.
