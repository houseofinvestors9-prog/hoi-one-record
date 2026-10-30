# One record for one family

**100xEngineers Cohort 7, Final Capstone**
Nikhil Reddy, CMO, House of Investors. Hyderabad, 30 October 2026.

Read as a page: **https://claude.ai/artifact/1tgQ61k4rGfeX2tPQt5ZZb**

---

## The short version

| | |
|---|---|
| **The problem** | Six people work the same family and each keeps a separate list. So the family answers the same questions four times, two firms fight over whose buyer it was, and the builder who paid for the ads has to ask somebody for a spreadsheet. |
| **What we did** | Gave the family one permanent ID at first contact. Everything after that, from the ad they clicked to the cheque they wrote, gets written against that one ID. |
| **Where it stands** | 9,100 families on one record, 6,415 of them spreadsheet rows until 6 October. Four of six surfaces live, 27 people on it daily, 198 firms registered. |
| **Still open** | Two of the six surfaces are named and not built. And the minutes saved per family is not measured. That is one afternoon of work. |

## What House of Investors is

A real estate wealth house in Hyderabad, working two lines. **Seller mandates**, where a
builder hands us a project to sell. And a **land co investment** product, where buyers put
money into a parcel together.

Both lines sell to the same families. A family that buys a flat through one line is often
the right buyer for a land deal a year and a half later. If nobody wrote down what
happened the first time, you start from nothing. That is the whole reason this exists.

## Two loops, one record

| Loop | Surface | Status | Size today |
|---|---|---|---|
| Family | hyderabad.properties, the public project check | **Live** | 4 government sources |
| Family | Wealth Snapshot, what the family owns | **Live** | 125 families |
| Family | Ratio, the family's full portfolio | Not built | zero |
| Builder | Lead Desk, where our people work | **Live** | 9,100 families |
| Builder | Partner Desk, outside firms | **Live** | 198 firms |
| Builder | Control Room, the builder's own screen | Not built | zero |

Underneath all six: the **Lead Engine**, 49 tables, and the counter that issues the family
ID. Both loops write to it.

**One record for one family. So nobody asks the same question twice.**

## The observation, with no product in it

A family decides to buy a flat. Over the next four months two or three partner firms will
work them, a sales executive at every project they enquire about, a site executive who
shows them the flat, and eventually somebody from the builder's office.

Every one of them keeps a list of their own. Usually a spreadsheet, often just WhatsApp.

So by the third call the family has stopped answering properly. Two firms find out they
registered the same number, and the commission fight gets settled by whoever shouts
louder. The builder is paying for the ads and owns the flats, but to find out how the week
went he has to ask someone for a sheet, which comes two days later and is already wrong.

**What would prove this wrong:** if firms keep disputing attribution at the same rate now
that the record exists, and executives keep re-asking questions already sitting on it,
then the problem was behaviour and not data. No system fixes that.

## The numbers

Read from the production databases on 29 October 2026.
Method, and which figures are exact, in [docs/04-evidence.md](docs/04-evidence.md).

| | |
|---|---|
| Families with one permanent record | **9,100** |
| pulled out of spreadsheets on 6 Oct | 6,415 |
| added since, over 23 days | 2,685 |
| Contacts logged against those records | 30,000 to 40,000 |
| Partner firms registered | **234** |
| duplicate claims caught | 24 |
| disputes settled with a written decision | 3 |
| Site visits scheduled | 420 to 500 |
| Booking records logged | 74 |
| Of those, verified | 43 |
| Ad spend tracked | ₹9,90,840 |
| Cost per lead, Aug to Oct | ₹454 to ₹236 |
| People using it every working day | 27 |
| Projects live on it | 10 |

## The systems

Six surfaces write to the same record. Only the first needs no login.

| System | Who uses it | Link |
|---|---|---|
| hyderabad.properties | Anyone. Checks whether a project is safe, from government records | https://hyderabad.properties |
| Lead Engine | Our team. The record itself, 49 tables, 135 fields on a family | https://hoi-lead-flow.base44.app |
| Lead Desk | 234 partner firms. Registration and attribution | https://aditya-lead-desk.base44.app |
| Partner Hub | Firms joining. Onboarding and project material | https://hoi-partner-hub.base44.app |
| Oxygen Forest Desk | One project's firms | https://oxygen-forest-partners.base44.app |
| Wealth Snapshot | The family. What it owns and what to do next | https://wealth-blueprint-hoi.base44.app |

## The documents

| | |
|---|---|
| [CASE-STUDY.md](CASE-STUDY.md) | The full case study, in the capstone pitch structure |
| [docs/01-observation.md](docs/01-observation.md) | Observation, hypothesis, falsifier, the sixty second version |
| [docs/02-architecture.md](docs/02-architecture.md) | The two loops and the six surfaces |
| [docs/03-data-model.md](docs/03-data-model.md) | The spine, the 135 fields, the attribution rule, row level security |
| [docs/04-evidence.md](docs/04-evidence.md) | Every number and how it was measured |
| [docs/05-null-test.md](docs/05-null-test.md) | What we chose not to build, and why |
| [docs/06-validation.md](docs/06-validation.md) | The five conversations, who and what to ask |
| [demo/video-script.md](demo/video-script.md) | Shot by shot script for the demo video |
| [demo/edit-sheet.md](demo/edit-sheet.md) | Timecodes for the cut and what is still to be recorded |
| [schema/](schema/) | 49 entity definitions exported from production. Field names only, no records |

## The four submissions

| Deliverable | Link |
|---|---|
| Live project | https://hyderabad.properties |
| Code | this repository, plus [hyderabad-properties](https://github.com/houseofinvestors9-prog/hyderabad-properties) |
| Case study | https://claude.ai/artifact/1tgQ61k4rGfeX2tPQt5ZZb |
| Demo video | [demo/one-record-demo.mp4](demo/one-record-demo.mp4), 2:57. Three shots are holding slates until the screen captures are recorded |

## What this does not claim

Three things, named rather than buried.

**Minutes saved per family.** No before figure was recorded. Until it is measured, the
benefit is not a number.

**Dispute rate before the system.** The 24 duplicates and 3 arbitrations are what the
system caught. What firms argued about earlier was never counted, because nobody was
counting.

**Revenue the system produced.** 43 verified bookings sit on the record. How many would have
closed anyway is unknown.
