# One record for one family

**House of Investors, Hyderabad. Capstone for 100xEngineers Cohort 7.**
30 October 2026. Read as a page: **https://claude.ai/artifact/1tgQ61k4rGfeX2tPQt5ZZb**

---

## Read this bit if you read nothing else

A family buying a flat in Hyderabad gets worked by about six different people. Each one
keeps a list of their own. So the family answers the same questions four times, two firms
end up fighting over whose buyer it was, and the builder who paid for the ads has to ask
somebody for a spreadsheet to find out how his own project sold this week.

We gave the family one permanent ID instead. Everything that happens after that, from the
ad they clicked to the cheque they wrote, gets written against that one ID.

**9,100 families have one today.** 6,415 of them were rows in a spreadsheet until the
sixth of October.

Around that record sit six surfaces. Four are live and carrying real work right now. Two
are named and not built. One of the live ones is public and needs no login at all.

---

## What House of Investors actually is

A real estate wealth house in Hyderabad. Two lines of business:

| Line | What it means |
|---|---|
| **Seller mandates** | A builder hands us their project to sell. We are the desk on it. |
| **Land co investment** | Buyers put money into a land parcel together. |

Both lines sell to the same families. That is the entire reason this project exists. A
family that buys a flat through one line is often the right buyer for a land deal a year
and a half later. If nobody wrote down what happened the first time, you start again from
nothing, and you ask them everything all over again.

---

## The problem, told properly

Picture a family in Jubilee Hills who decide they want a bigger flat.

Over the next four months they will talk to two or three partner firms, a sales executive
at every project they enquire about, a site executive who actually shows them the flat,
and somebody from the builder's office. That is six people, minimum.

Every one of those six keeps their own list. A notebook, a WhatsApp thread, a spreadsheet,
sometimes a proper CRM. The lists never meet.

So three things go wrong, every single time.

**The family gets tired.** By the third call they have explained their budget, their
timeline and their school requirement to four different people. They stop answering
properly. Not because they are not interested. Because answering is now work.

**Two firms fight.** Both registered the same phone number. Both say they introduced the
buyer. The booking happens, the commission is real money, and the argument plays out on
WhatsApp with no record of who said what first. Whoever argues hardest wins.

**The builder is blind.** He is paying for the ads. He owns the flats. And to find out how
his own project sold this week he has to message somebody and wait for a sheet.

Here is the part that took me a while to accept: **none of this is a software problem.**
Most of these people already have a CRM and most of them use it properly. The lists are
fine. There is just nothing underneath for any of the work to add up against.

---

## So we gave the family one record, and built two loops around it

```
        THE FAMILY LOOP                           THE BUILDER LOOP

  hyderabad.properties                                 Builders
  buyer checks if a project is safe          they hand us a project to sell
            │                                              │
            ▼                                              ▼
     Wealth Snapshot          ready buyer   Lead Desk     homes to sell
  family sees what it owns   ───────────▶   and Partners  ◀──────────
            │                              our team plus              │
            ▼                              198 firms                  ▼
         Ratio                                   │               Control Room
  family tracks every                            ▼            builder sees every
  property with us                         live bookings       booking as it lands
            ▲                                    │                    │
            └──────── buyer joins ◀──────────────┘                    │
                                                                      ▼
        they tell friends and buy again              good results bring the next project
```

Both loops write to the same record. That is the only clever idea in the whole thing.

**One record for one family. So nobody asks the same question twice.**

---

## The six surfaces, and where each one honestly stands

| # | Surface | Who uses it | Status | Size today |
|---|---|---|---|---|
| 1 | **hyderabad.properties** | Any buyer, no login | **Live** | 4 government sources |
| 2 | **Wealth Snapshot** | Families we already serve | **Live** | 125 families |
| 3 | **Lead Desk** | Our 27 people | **Live** | 9,100 families |
| 4 | **Partner Desk** | Outside firms | **Live** | 198 firms registered |
| 5 | **Ratio** | Families, portfolio view | Named, not built | zero |
| 6 | **Control Room** | Builders | Named, not built | zero |

Underneath all six sits the **Lead Engine**: 49 entities, and the counter that issues the
family ID.

Two of the six do not exist. I am not going to dress that up. They are on the slide
because that is the shape of the thing, and they are marked NEXT on the slide for the same
reason they are marked honestly here.

### 1. hyderabad.properties

Public, free, no login, live now. It reads the records nobody reads: RERA filings and
orders, building permits, lake boundaries, government guideline values. Then it tells a
buyer whether a project is safe before they commit money.

Claude reads each new document. A person approves every verdict before it publishes,
because a wrong verdict in public about somebody's project carries legal exposure, so a
human signs it.

Change detection is by content hash, not by CSS selector. Government portals get redesigned
without warning and selector-based scrapers die quietly. Hashes do not.

And a buyer who checks a project here becomes a family record in the same engine. That is
what closes the family loop.

### 2. Wealth Snapshot

125 families have one. It shows a family what it currently owns through us and what the
sensible next move looks like. One entity, `WealthProfile`, and it is deliberately small.

### 3. The Lead Desk

Where our 27 people work, every working day, across six roles: founder, admin, project
head, business development, site executive, marketing.

### 4. The Partner Desk

198 firms are registered. They see live inventory, hold a unit while they close, and pull
call scripts and project material without phoning us for it.

On the mandate project, Sri Aditya's Terrace 35, the desk carries **234 partner records**
of its own. Those two numbers count different things and both are real: 198 firms in the
house registry, 234 partner records on that one project's desk.

### 5 and 6. Ratio and Control Room

Ratio is the family tracking every property it holds with us. Control Room is the builder
watching bookings land live instead of asking for a sheet.

Both are specified. Neither is built. Control Room is the one that matters more, because
"the builder is blind" is a third of the problem I just described and right now the record
fixes it only for us, not for him.

---

## The part that decides money

234 partner firms register buyers on the mandate desk. They compete with each other and
they do not trust each other. So the attribution rule is written down in advance, which is
the only reason it holds.

| Rule | |
|---|---|
| First registration owns the buyer | 90 days by default, set per project |
| Second firm, same number | marked `duplicate` automatically |
| Both have a real claim | marked `contested`, an admin decides |
| The decision | written to `AuditLog` |

**24 duplicates caught. 3 disputes decided.**

`AuditLog` is create and read only. No role can edit it or delete from it, mine included.
That constraint is the reason an arbitration decision can be shown to the firm that lost
it. Before this existed the same fights happened on WhatsApp and nobody wrote down the
outcome.

---

## Every number, and how it was counted

| Number | What it is | How I got it |
|---|---|---|
| 9,100 | family IDs issued | `ClientCounter.value`, exact |
| 6,415 | backfilled from spreadsheets | `ClientCounter.backfill_end`, exact |
| 2,685 | new in 23 days | 9,100 minus 6,415, about 117 a day |
| 30,000 to 40,000 | activities logged | offset probe, so a range not a point |
| 27 | people using it daily | attendance punches, last 23 days |
| 74 | bookings closed | `Booking` records with a cheque |
| 234 | partner records, mandate desk | `Partner` count, exact |
| 198 | firms in the house registry | `PartnerRegistry` count, exact |
| 125 | families with a Wealth Snapshot | `WealthProfile` count, exact |
| 49 | entities in the Lead Engine | schema export |
| 24 and 3 | duplicates caught, disputes decided | `attribution_status`, `contest_resolved` |

Where I could not count exactly I said range, not a confident number. The 30,000 to 40,000
is the only one like that, and it is a range because the table is past the 500 row page
limit and there is no count endpoint.

---

## What this does not claim

**Minutes saved per family. Not measured.** No before figure was ever recorded. The old
spreadsheet rows are still in `LeadHistory`, so the measurement is one afternoon: time five
executives finding a returning buyer's history on the system, then time them finding it in
the old sheets. Until that is done, the honest claim is that the work now adds up, not that
it is faster.

**Two of six surfaces do not exist.** Ratio and Control Room are specified and empty.

**Five outside validations, not done.** 234 firms and several builders use this daily,
which is usage, not validation. The five formal conversations, including one with a builder
who does not work with us, are planned and have not happened.

---

## The self-check

The eight questions from the Custom Capstone office hour.

| Question | Verdict | Why |
|---|---|---|
| Observation with no product in it | Clear | Six people, six lists, nothing underneath |
| Is it mine | Clear | I run the house sitting between the firms, the builders and the families |
| Compresses to sixty seconds | Clear | The first section |
| States its falsifier | Clear | If disputes continue at the same rate and families keep being re-asked, I am wrong |
| Baseline and target number | **Open** | System side counted. Minutes saved not. Weakest of the eight |
| Survives the null test | Clear | An LLM with a connector cannot issue an identity, hold it for years, or arbitrate money |
| Five confirmations from outside | **Open** | Daily usage is not the same as five Mom Test conversations |
| Run by hand, ship in five weeks | Clear | It ran by hand for years. That is where the rules came from |

Both open items close with the same afternoon of work.

---

## Team

Nikhil Reddy, founder. Built and runs all of it.

27 people use it every working day. 198 firms are registered on the partner desk and 234
partner records sit on the mandate desk. None of them work for me, which is the interesting
part: they adopted a rule, not a piece of software.
