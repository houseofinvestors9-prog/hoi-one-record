# The null test

> Before you commit, build the cheapest version of your idea with the tools you already
> have: a skill, an MCP connector, a scheduled trigger. If that version is good enough to
> provide the desired output, pick a different problem.

Run honestly against each piece.

## Where a scheduled prompt was enough, and we used one

These were built as skills and scheduled triggers, and they stayed that way because that
is all they needed.

**The weekly Terrace 35 advertising review.** Pulls Meta spend and compares it against
lead quality in the sheet. A connector plus a prompt on a schedule. No app was built.

**The weekly market signal scan.** Web search across four lanes, appended to a status
file. Same shape.

Naming these matters. When the answer to the null test is that a skill already does it,
the right move is to use the skill and not build. We did that, more than once.

## Where it was not enough

**One identity across 234 firms that do not trust each other.**
A prompt cannot hold a 90 day claim, decide which of two registrations on the same number
owns it, stop a firm from reading another firm's rows, and leave a log that stands up in
front of the firm that lost. That needs multi-tenant state, row level security and a
decision record. A connector has no idea who is asking.

**27 people writing to the same record all day.**
Concurrency, role based permission, audit.

**A government portal that changes shape.**
Claude can read one RERA PDF beautifully. It cannot watch several thousand project pages
for change, hash them so it does not re-read what has not moved, queue what did, hold the
evidence behind each verdict, and refuse to publish until a person signs. The AI step is
the cheap part of that. The pipeline around it is the work.

**The pricing engine.**
Floor rise, facing premium, parking tier, GST, corpus. One wrong quote to a buyer is a
commercial problem, so it has to be computed and not generated.

## Verdict

Parts of this would have failed the null test, and those parts were correctly not built as
applications. The record itself passes. A family record that 234 competing firms, 27 staff
and a builder all write to, with arbitration and row level security, is not a skill plus a
connector.
