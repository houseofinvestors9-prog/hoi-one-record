# One record for one family

**Case study · 100xEngineers Cohort 7 Final Capstone**
House of Investors · Hyderabad · 29 October 2026

---

## 1. Problem

A family buying a home in Hyderabad is worked by several channel partners, several
project teams and the builder at the same time, and every one of them keeps a separate
list, so the family is asked the same questions four times, two partners claim the same
buyer and argue about the commission, and the builder cannot see how his own project sold
this week without asking a person for a spreadsheet.

## 2. Solution

One permanent identity for the family, issued at first contact, that every partner firm,
every executive and the builder writes against, with attribution arbitrated by rule
instead of by argument.

## 3. Product demo

Public, no login: **https://hyderabad.properties**
Reads TG-RERA, TS-bPASS, HYDRAA lake boundaries and IGR guideline values, and tells a
buyer whether a project is safe before they fall in love with it. Every verdict carries
its sources and its date, and no verdict publishes until a person approves it.

Behind the login, five more surfaces, listed in the README with their URLs. The demo
walks the same family through all of them: ad click, partner registration, duplicate
caught, call, site visit, EOI, cheque, booking, and the builder watching it happen.

Shot by shot script: [demo/video-script.md](demo/video-script.md)

## 4. Traction

Read from production on 29 October 2026. Method, and which figures are exact versus
bounded, in [docs/04-evidence.md](docs/04-evidence.md).

| | |
|---|---|
| Families with one permanent record | 9,100 |
| Lifted out of spreadsheets into that record | 6,415 |
| Added since, in 23 days | 2,685, about 117 a day |
| Contacts logged against those records | 30,000 to 40,000 |
| Partner firms registered | 234 |
| Duplicate claims caught automatically | 24 |
| Disputes arbitrated with a written decision | 3 |
| Site visits scheduled | 420 to 500 |
| Bookings closed on the record | 74 |
| People using it every working day | 27 |
| Projects live | 10 |

Not claimed, because it is not measured: minutes saved per family, dispute rate before
the system existed, and revenue attributable to the system. The method for getting the
first of those is written down in [docs/06-validation.md](docs/06-validation.md) and takes
an afternoon. It is the main thing still open.

## 5. Build journey

Dates derived from record creation timestamps in the production databases.

| When | What happened |
|---|---|
| 11 Jun 2026 | Sri Aditya Lead Desk goes up. Partner registration and attribution first |
| 12 Jun 2026 | First expression of interest recorded. One day after the app existed |
| 25 Jun 2026 | First outside partner firm registers |
| 28 Jul 2026 | Wealth Snapshot. The family facing view |
| 19 Aug 2026 | HOI Lead Engine. The record itself, and Terrace 35 moves onto it |
| 21 Sep 2026 | First bookings recorded on the engine rather than in a sheet |
| 28 Sep 2026 | Oxygen Forest partner desk |
| 30 Sep 2026 | Partner hub |
| 1 Oct 2026 | hyderabad.properties, first commit |
| 2 Oct 2026 | hyderabad.properties wired into the engine as a lead source |
| 6 Oct 2026 | 6,415 legacy spreadsheet rows backfilled and given client ids |
| 29 Oct 2026 | 9,100 families on one record |

The order is the lesson. Attribution was built first, before the CRM, because attribution
is what partners actually care about and nothing else gets adopted until that is settled.
The pretty family facing view came third. The public trust layer came last, five months
in, once there was an engine for it to feed.

What was learned the hard way, in order:

**Partners do not adopt software. They adopt a fair rule.** The first version let anyone
register anyone. It was useless until `attribution_until` and the duplicate check existed,
because without them registering a buyer was not worth the typing.

**The backfill is the product.** A clean new system next to 6,415 rows of history is not
one record, it is a seventh list. The 6 October backfill, which reconciled the old sheets
into `LeadHistory` and issued client ids against them, is the day the thing actually
started working.

**A log nobody can edit is worth more than a log everyone trusts.** `AuditLog` is create
and read only, including for admins. That constraint is why an arbitration decision can
be shown to the losing partner.

**Some of this should not have been built.** The weekly ad reviews and the market signal
scans run as scheduled prompts with a connector, not as applications, because that is all
they needed. See [docs/05-null-test.md](docs/05-null-test.md).

## 6. Team

Nikhil Reddy, founder. Built and operates the systems. 27 people use them daily across
six roles: founder, admin, project head, business development, site executive, marketing.
234 partner firms work against them from outside the company.

---

## The self check

The eight questions from the Custom Capstone office hour, answered.

**1. Observation with no product in it.** Section 1 above, and
[docs/01-observation.md](docs/01-observation.md). No tool, platform or stack is named.

**2. Is it mine.** Yes. I run the advisory that sits between the partners, the builders
and the families, and I have been on all three sides of this.

**3. Does it compress to sixty seconds.** Yes.
[docs/01-observation.md](docs/01-observation.md), last section.

**4. The falsifier.** If disputes continue at the same rate and executives keep re-asking
questions already on the record, the problem was behaviour, not data. Both are measurable
now.

**5. Baseline and target.** Partly. The system side is counted: 6,415 records that had no
identity now have one, 24 duplicates caught, 3 disputes decided with a log. The human side
is not counted yet, and the measurement is scheduled rather than claimed. This is the
weakest answer of the eight and it is not hidden.

**6. The null test.** Passed on the spine, failed deliberately on the edges, which were
then not built as applications. [docs/05-null-test.md](docs/05-null-test.md).

**7. Five people outside friends and family, one controlling a budget.** 234 partner
firms and the builders already use it, which is stronger than five interviews. But the
five conversations the review actually asks for, including with a builder who does not
work with us, are planned and not yet done.
[docs/06-validation.md](docs/06-validation.md).

**8. Run it by hand this week, ship v1 in four to five weeks.** It was run by hand for
years. That is where the rules came from. v1 shipped in June, five months ago, and has
been in daily production use since.
