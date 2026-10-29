# One record for one family

**Case study. 100xEngineers Cohort 7, Final Capstone.**
House of Investors, Hyderabad. 29 October 2026.

Read as a page: **https://claude.ai/artifact/1tgQ61k4rGfeX2tPQt5ZZb**

House of Investors is a real estate wealth house in Hyderabad. It works two lines: seller
mandates on builder launches, and a land co investment product for HNI and NRI buyers.
Both lines sell to the same families, which is why 9,100 of them had to be given one
identity before anything else could be counted.

---

## 1. Problem

Every firm working a family keeps its own list, so the family gets asked the same
questions four times and two firms end up fighting over who owns the buyer.

## 2. Solution

One permanent ID for the family, issued at first contact, that every firm and every
executive writes against, with the commission claim settled by rule instead of by
argument.

## 3. Product demo

**https://hyderabad.properties** is public and needs no login. It reads RERA filings,
building permits, lake boundaries and government guideline values, and tells a buyer
whether a project is safe before they commit. Every verdict carries its source and its
date, and a person approves it before it publishes.

The other five surfaces are behind a login and are listed in
[docs/02-architecture.md](docs/02-architecture.md). The demo walks one family through all
of them: ad click, registration by a partner firm, duplicate caught, call, site visit,
expression of interest, cheque, booking, and the builder watching it happen.

Script: [demo/video-script.md](demo/video-script.md)

## 4. Traction

Read from the production databases on 29 October 2026. Method in
[docs/04-evidence.md](docs/04-evidence.md).

| | |
|---|---|
| Families with one permanent record | 9,100 |
| pulled out of spreadsheets on 6 Oct | 6,415 |
| added since, over 23 days | 2,685 |
| Contacts logged against those records | 30,000 to 40,000 |
| Partner firms registered | 234 |
| duplicate claims caught | 24 |
| disputes settled with a written decision | 3 |
| Site visits scheduled | 420 to 500 |
| Bookings closed on the record | 74 |
| People using it every working day | 27 |
| Projects live on it | 10 |

Three things are not claimed, because they are not measured: minutes saved per family,
the dispute rate before the system existed, and revenue the system produced. The method
for the first is in [docs/06-validation.md](docs/06-validation.md) and takes an afternoon.

## 5. Build journey

Dates taken from record creation timestamps in the production databases.

| When | What happened |
|---|---|
| 11 Jun 2026 | Lead Desk goes live. Partner registration and attribution, nothing else |
| 12 Jun 2026 | First expression of interest recorded, one day after the app existed |
| 25 Jun 2026 | First outside firm registers |
| 28 Jul 2026 | Wealth Snapshot, the family facing view |
| 19 Aug 2026 | Lead Engine. The record itself, with Terrace 35 the first project on it |
| 21 Sep 2026 | Bookings start being recorded on the engine instead of in a sheet |
| 28 Sep 2026 | Oxygen Forest partner desk |
| 30 Sep 2026 | Partner hub |
| 1 Oct 2026 | hyderabad.properties, first commit |
| 2 Oct 2026 | hyderabad.properties starts feeding the engine as a lead source |
| **6 Oct 2026** | **6,415 old spreadsheet rows reconciled and given IDs** |
| **29 Oct 2026** | **9,100 families on one record** |

Three things came out of that order.

**Attribution was built before the CRM, and that is why firms used it.** The first
version let anyone register anyone. Nobody typed into it. It became worth the typing only
once the 90 day window and the duplicate check existed, because that is what protects a
firm's commission.

**The backfill on 6 October is when it started working.** A clean new system standing next
to 6,415 rows of old sheets is just a seventh list. Reconciling those rows into
`LeadHistory` and issuing IDs against them is what made it one record.

**The audit log is create and read only, including for admins.** That constraint is the
reason an arbitration decision can be shown to the firm that lost it.

## 6. Team

Nikhil Reddy, founder. Built and runs the systems. 27 people use them every working day
across six roles: founder, admin, project head, business development, site executive,
marketing. 234 partner firms work against them from outside the company.

The house runs two lines against the same record. Seller mandates on builder launches,
where HOI is the desk on the project. And a land co investment product, where buyers put
money into a parcel together. A family that arrives through one line is often sold the
other eighteen months later, which is why the record has to survive the transaction
instead of closing with it.

---

## The self-check

The eight questions from the Custom Capstone office hour.

| Question | Verdict | Why |
|---|---|---|
| Observation with no product in it | Clear | No tool or platform appears in the opening statement |
| Is it mine | Clear | I run the advisory sitting between the firms, the builders and the families |
| Compresses to sixty seconds | Clear | The short version at the top of the README |
| States its falsifier | Clear | If disputes continue at the same rate and questions keep getting re-asked, the observation is wrong |
| Baseline and target number | **Open** | The system side is counted. Minutes saved per family is not. Weakest of the eight |
| Survives the null test | Clear | Clear on the record itself, deliberately failed at the edges, which were then not built |
| Five confirmations from outside | **Open** | 234 firms and several builders use it daily. The five formal conversations are planned and not done |
| Run by hand, ship in five weeks | Clear | It ran by hand for years, which is where the rules came from. Version one shipped in June |

Both open items close with the same exercise. Time five executives finding a returning
buyer's history on the system, then time them finding it in the old sheets, which are
still in the database.
