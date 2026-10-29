# Edit sheet

`one-record-demo.mp4` is a finished 2 minute 13 second cut at 1920x1080, 30fps.
It plays end to end right now and can be submitted as it stands.

Three of its seven shots are holding slates instead of screen recordings. Each slate
says on screen what to capture and how long to hold it. Replacing a slate is the only
work left.

## What is in the file

| | |
|---|---|
| Runtime | 2:13.30 |
| Format | 1920x1080, 30fps, H.264, AAC 48kHz |
| Size | 4.8 MB |
| Narration | macOS system voice `Aman`, en_IN, 170 words per minute |
| Shots done | 1, 2, 6, 7 and the end card |
| Shots on slates | 3, 4, 5 |

## Timecodes

| In | Out | Card | What it is |
|---|---|---|---|
| 0:00.00 | 0:10.40 | `c1a` | A family decides to buy a flat |
| 0:10.40 | 0:21.65 | `c1b` | By the third call, nobody is winning |
| 0:21.65 | 0:32.89 | `c2a` | There is no common record anywhere |
| 0:32.89 | 0:35.89 | `c2b` | So we gave the family one |
| 0:35.89 | 0:51.75 | `s3` | **SLATE** the family record |
| 0:51.75 | 1:12.60 | `s4` | **SLATE** duplicate, contested, audit log |
| 1:12.60 | 1:33.68 | `s5` | **SLATE** hyderabad.properties and the review desk |
| 1:33.68 | 1:36.18 | `n1` | 9,100 |
| 1:36.18 | 1:42.08 | `n2` | 6,415 |
| 1:42.08 | 1:44.58 | `n3` | 30,000 |
| 1:44.58 | 1:47.08 | `n4` | 27 |
| 1:47.08 | 1:48.96 | `n5` | 74 |
| 1:48.96 | 1:56.26 | `c7a` | Not measured yet |
| 1:56.26 | 2:09.77 | `c7b` | What I can show today |
| 2:09.77 | 2:13.30 | `end` | One record for one family |

## Replacing the three slates

The narration under each slate is already cut to length. Record the screen, trim it to
the duration printed on the slate, and lay it over the slate. Nothing else moves.

| Slate | Record this | Length |
|---|---|---|
| `s3` | One family record in the Lead Engine, scrolled slowly, holding on `client_id` | 15.86s |
| `s4` | A `duplicate` lead, then a `contested` lead, then its `AuditLog` entry | 20.85s |
| `s5` | hyderabad.properties: search, report, sources and dates, then the review desk | 21.08s |

**Blur or replace every real name and phone number before you record.** These are real
families. Use a staging record or blur in post.

## Changing the narration

`vo/shot1.mp3` to `vo/shot7.mp3` are the seven takes as separate files.
`build/s1.txt` to `build/s7.txt` are the words that produced them.

To rebuild a take after editing the text:

```bash
say -v Aman -r 170 -f build/s1.txt -o s1.aiff
```

If a take changes length, its shot's cards have to change with it. `build/build.sh`
holds the card durations and `build/cards.py` draws the cards.

## On the voice

This is the macOS system voice, which is free and runs locally. It is clear and flat,
which is what the script asks for, but it is audibly synthetic.

A studio voice from the ElevenLabs connector was quoted at 605 credits, about ₹1,065,
for shot 1 alone. The full seven takes come to roughly ₹5,000. The cut is built so that
swapping the audio is a file replacement, so this decision can wait until after the
screen captures are in.
