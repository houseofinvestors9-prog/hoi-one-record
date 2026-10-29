# One record for one family

**100xEngineers Cohort 7 — Final Capstone**
House of Investors, Hyderabad · October 2026

---

## The observation

In Hyderabad, one family looking for a home is worked by several channel partners,
several project teams and the builder at the same time. Each of them keeps its own list.

So the family answers the same five questions to four different people. Two partners
claim the same buyer and argue about who gets the commission. The builder who owns the
inventory has to ask someone for a spreadsheet to find out what happened this week.

The record of that family exists in everybody's sheet and nobody's system.

## The hypothesis

If a family is given one identity at first contact, and every later touch is written
against that identity, then duplicate work falls, attribution stops being an argument,
and the builder can see his own inventory without asking a person for a report.

Every touch means: the ad click, the WhatsApp reply, the call, the site visit, the
expression of interest, the cheque, the booking, and the re-enquiry eight months later.

## What would prove me wrong

If partners keep disputing attribution at the same rate after the single record exists,
and executives keep re-asking qualifying questions that are already on the record, then
the problem was never the data. It was behaviour, and no system fixes that.

## Where it stands today

Read 29 October 2026, from the live databases. Method in [docs/04-evidence.md](docs/04-evidence.md).

| | |
|---|---|
| Families with one permanent record | **9,100** |
| Of those, pulled out of spreadsheets | **6,415** (cutoff 6 Oct 2026) |
| New families recorded since that cutoff | **2,685 in 23 days**, about 117 a day |
| Contacts logged against those records | **30,000 to 40,000** |
| Partner firms registered on the partner desk | **234** |
| Duplicate claims caught automatically | **24** |
| Attribution disputes arbitrated | **3** |
| Site visits scheduled through the system | **420 to 500** |
| Bookings closed on the record | **74** |
| People using it every working day | **27**, across six roles |
| Projects live on it | **10** |

## The systems

Six of them, one spine. The spine is the family record.

| System | What it is | Link |
|---|---|---|
| hyderabad.properties | Public. Checks whether a project is legally safe, from government records | https://hyderabad.properties |
| HOI Lead Engine | Internal. The family record itself, plus routing, calling, visits, bookings | https://hoi-lead-flow.base44.app |
| Sri Aditya Lead Desk | Partner facing. 234 firms register buyers, attribution is arbitrated here | https://aditya-lead-desk.base44.app |
| HOI Partner Hub | Partner onboarding and project material | https://hoi-partner-hub.base44.app |
| Oxygen Forest Partner Desk | Same, for one project | https://oxygen-forest-partners.base44.app |
| Wealth Snapshot | The family sees what it owns and what to do next | https://wealth-blueprint-hoi.base44.app |

Architecture: [docs/02-architecture.md](docs/02-architecture.md)
Data model: [docs/03-data-model.md](docs/03-data-model.md)

## The four submissions

| Deliverable | Link |
|---|---|
| Live project | https://hyderabad.properties |
| Code | this repository, plus [hyderabad-properties](https://github.com/houseofinvestors9-prog/hyderabad-properties) |
| Demo video | see [demo/video-script.md](demo/video-script.md) |
| Case study | [CASE-STUDY.md](CASE-STUDY.md) |

## Honest state of things

Three numbers in the table above are counted exactly. Four are bounded by probe, because
the API pages at 500 and an exact count was not worth the calls. Which is which is
written down in [docs/04-evidence.md](docs/04-evidence.md).

The time saved per family is not yet measured. The method for measuring it, and the five
conversations that have to happen outside the company, are in
[docs/06-validation.md](docs/06-validation.md). That work is open, and it is named as open.
