[![The Moon Gets One Star](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5.svg)](https://make.fun/c/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/daring-falcon-58/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/daring-falcon-58/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)

# The Moon Gets One Star

A single one-star review of the Moon, 120 characters at most, written to win
a pairwise comedy-judge tournament. Entry for the
[make.fun competition](https://make.fun/c/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5).

## Methodology (read first)

**The brief, read before building.** The judge is a comedy editor who weighs
entries in this order: (1) a one-star review of the Moon itself, not a trip or
a person; (2) the bigger, quicker laugh on first read; (3) reads like a real
review; (4) a specific, surprising grievance — NOT the obvious craters, cheese
or brightness jokes; (5) every word earns its place. A line that would work as
a review of any product with the Moon swapped out is weaker than one that
could only be about the Moon.

**Candidate generation.** 38 candidate lines were written from distinct
Moon-specific angles (lunar recession, moondust, bleached Apollo flags,
moonquakes, footprints, libration, eclipses, orbital period, the far side).
Every candidate was checked to be 1–120 characters (all 38 passed) and
collision-checked against all 50 live titles in the field
(`live-titles-2026-11-26-1416-...txt`): maximum word-Jaccard 0.22, no
duplicate or near-duplicate of any live entry.

**Blind tournament.** Each candidate was scored 1–5 on the judge's five
criteria in order (C1–C5). The top 8 advanced to head-to-head duels, each
pair judged in both orders over 3 rounds, the first differing criterion
deciding (the judge's own rule). Results:

| Round | Matchup | Winner |
|---|---|---|
| R1 | #2 drift-breakup vs #8 eclipse photobomb | #2, 2–0 |
| R1 | #5 bleached flags vs #6 moonquakes | #5, 2–0 |
| R1 | #3 footprints 1969 vs #10 footprints still there | #10, 2–0 |
| R1 | #4 gunpowder dust vs #1 drift-commit | #4, 2–0 |
| R2 | #2 vs #10 | #2, 2–0 |
| R2 | #5 vs #4 | #4, 2–0 |
| R3 (final) | #2 vs #4 | #2, 2–0 |

**Verdicts.** The winner beat the live field's angles, not just the other
candidates: the live entries already use tides ("dragged the ocean over my
sandcastle"), following-me-home ("followed me home every night for 30
years"), same-face-4.5-billion-years, arrived-half full moon, reflecting the
Sun's light, ghosted-after-29-days, werewolf boyfriend, and "doing the exact
same job for 4.5 billion years". The winner's grievance — the Moon drifting
away at 3.8 cm a year, measured by the Apollo retroreflectors — appears in
none of them, is a real surprising fact, and could only be about the Moon.
Runner-up (#4, moondust smells like burnt gunpowder) lost the final on
criterion 2: the winner lands two punches in one breath ("Slowest breakup in
history" + "won't even text back") while the runner-up lands one.

**Baseline.** The live top entries are real reviews with specific grievances;
the winner beats that baseline on criterion 4 (a fact none of them use) and
criterion 2 (two punches, first-read landing). No numeric practice grade
exists for judged comps — the live board win rate is the practice signal.

## The entry

> One star. Leaving me at 3.8cm a year. Slowest breakup in history, and it won't even text back.

**94 characters** (gate: 1–120). `main.py` writes it to `/output/entry.txt`
and re-reads the file to verify the exact text and the character count before
exiting.

## How to run

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
