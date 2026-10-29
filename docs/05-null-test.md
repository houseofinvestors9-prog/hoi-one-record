# The null test

> Before you commit, build the cheapest version of your idea with the tools you already
> have: a skill, an MCP connector, a scheduled trigger. If that version is good enough to
> provide the desired output, pick a different problem.

Run honestly, against each piece.

## Where a generic assistant is enough, and we use one

These were built as skills and scheduled triggers, and they stayed that way because that
is all they needed to be:

- The weekly Terrace 35 ad review. Pulls Meta spend and compares it against lead quality
  in the sheet. A connector plus a scheduled prompt. No app was built for it.
- The weekly market signal scan for an advisory engagement. Web search, four lanes, append
  to a status file.

Naming these matters. If the answer to the null test is "a skill already does it", the
right move is to use the skill and not build. We did that, repeatedly.

## Where it is not enough

**Identity across 234 firms that do not trust each other.**
A skill cannot hold the attribution window, decide which of two claims on the same phone
number is the owner, enforce that a partner reads only their own rows, and leave a log an
arbitrator can defend. That needs multi tenant state, row level security and a decision
record. A connector has no notion of who is asking.

**Twenty seven people writing to the same record all day.**
Concurrency, role based permission, audit. Not a prompt.

**Reading a government portal that changes shape.**
A generic assistant can read one RERA PDF beautifully. It cannot watch several thousand
project pages for change, hash them to avoid re-reading, queue what moved, hold the
evidence behind each verdict, and refuse to publish until a person signs. The AI step is
the cheap part. The pipeline around it is the work.

**The pricing engine.**
Floor rise, facing premium, parking tier, GST, corpus. One wrong quote to a buyer is a
commercial problem. This has to be computed, not generated.

## The honest verdict

Pieces of this would have failed the null test and were correctly not built as apps.
The spine would not. A family record that 234 competing firms, 27 staff and a builder all
write to, with attribution arbitration and row level security, is not a skill plus a
connector, and no amount of prompting makes it one.
