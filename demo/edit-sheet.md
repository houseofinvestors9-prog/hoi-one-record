# Edit sheet

`one-record-demo.mp4` is a finished 2 minute 57 second cut at 1920x1080, 30fps.
It plays end to end right now and can be submitted as it stands.

Three of its nine shots are holding slates instead of screen recordings. Each slate
says on screen what to capture and how long to hold it. Replacing a slate is the only
work left.

## What is in the file

| | |
|---|---|
| Runtime | 2:57.10 |
| Format | 1920x1080, 30fps, H.264, AAC 48kHz |
| Size | 6.3 MB |
| Narration | ElevenLabs `eleven_v3`, voice Krishna, Indian English |
| Pace | Read at 148 words per minute, cut at 1.16x to 172 |
| Shots done | 0, 1, 2, 3, 7, 8 and the end card |
| Shots on slates | 4, 5, 6 |

## Timecodes

| In | Out | Card | What it is |
|---|---|---|---|
| 0:00.00 | 0:04.60 | `c0a` | Two firms. The same buyer. One commission |
| 0:04.60 | 0:09.45 | `c0b` | Nobody wrote down who won |
| 0:09.45 | 0:25.39 | `c1a` | A family decides to buy a flat |
| 0:25.39 | 0:37.86 | `c1b` | By the third call, nobody is winning |
| 0:37.86 | 0:52.11 | `c2a` | There is no common record anywhere |
| 0:52.11 | 0:55.31 | `c2b` | So we gave the family one |
| 0:55.31 | 0:58.37 | `n1` | 9,100 |
| 0:58.37 | 1:03.72 | `n2` | 6,415 |
| 1:03.72 | 1:29.31 | `s3` | **SLATE** the family record |
| 1:29.31 | 1:55.10 | `s4` | **SLATE** duplicate, contested, audit log |
| 1:55.10 | 2:21.58 | `s5` | **SLATE** hyderabad.properties and the review desk |
| 2:21.58 | 2:24.49 | `n3` | 30,000 |
| 2:24.49 | 2:27.40 | `n4` | 27 |
| 2:27.40 | 2:29.58 | `n5` | 74 |
| 2:29.58 | 2:45.42 | `c7b` | What I can show today |
| 2:45.42 | 2:53.92 | `c7a` | Not measured yet |
| 2:53.92 | 2:57.10 | `end` | One record for one family |

## Replacing the three slates

The narration under each slate is already cut to length. Record the screen, trim it to
the duration printed on the slate, and lay it over the slate. Nothing else moves.

| Slate | Record this | Length |
|---|---|---|
| `s3` | One family record in the Lead Engine, scrolled slowly, holding on `client_id` | 25.59s |
| `s4` | A `duplicate` lead, then a `contested` lead, then its `AuditLog` entry | 25.79s |
| `s5` | hyderabad.properties: search, report, sources and dates, then the review desk | 26.48s |

On `s4`, hold the audit log on screen through the line "a log that nobody can edit,
including me." That is the strongest sentence in the video and it should not land on a
cutaway.

**Blur or replace every real name and phone number before you record.** These are real
families. Use a staging record or blur in post.

## Changing the narration

`vo/shot0.mp3` to `vo/shot8.mp3` are the nine takes as separate files, already at the
1.16x pace used in the cut. `build/s0.txt` to `build/s8.txt` are the words that produced
them.

Regenerating a take means another ElevenLabs run on voice `YQtsYmgUhr7KoZq3GePF` with
model `eleven_v3`, then the same speed correction:

```bash
ffmpeg -i new-take.mp3 -af "atempo=1.16" -ar 48000 -ac 2 shot1.wav
```

If a take changes length, its shot's cards have to change with it. `build/build.sh`
holds the card durations and `build/cards.py` draws the cards.

## On the pace

Krishna reads the script at 148 words per minute. That is slower than a person pitching,
and at that speed the cut ran 3:25, past the three minute cap in the script's own
production notes. The whole narration is sped to 1.16x, which puts it at 172 words per
minute and the cut at 2:57.

This is pitch corrected, so the voice does not sound higher. The takes were checked for
dead air first and had almost none, 1.2 seconds across all nine, so speed was the only
lever that did not mean cutting words.
