# Task 3: One-Score Game Records & Outcome Correlation (2016-2025)
Generated: Sept 6, 2026, morning compute | Source: ESPN schedule API (70 team-seasons, 935 games) | Data file: one_score_games.csv

## Career One-Score Records (margin <= 8, 2016-2025)
| Program | Overall | One-score | 1S% | Road one-score |
|---|---|---|---|---|
| Georgia | 117-21 | 25-11 | 69% | **9-1** |
| Alabama | 121-19 | 23-11 | 68% | 13-6 |
| Clemson | 112-26 | 28-13 | 68% | 11-6 |
| Ohio State | 115-17 | 17-8 | 68% | 6-3 |
| Michigan | 96-31 | 22-11 | 67% | 9-6 |
| Notre Dame | 101-29 | 22-17 | 56% | 4-5 |
| **Penn State** | 94-36 | 20-23 | **47%** | 8-11 |

## The Quality Confound (stated up front)
Good teams win close games because they are good. Most career rates here (56-69%) are inside the expected band for programs of this caliber. The signal is NOT "X wins close games" — it is DEVIATION FROM QUALITY. Three deviations survive that test:

## FLAG 1 — Penn State: the only program under .500, and the crater matches the receipts
PSU is 47% career in one-score games — the only sub-.500 program in the sample, 10+ points below every peer. Road: 8-11. And in their two weakest seasons the crater is extreme: 2025 = 1-5 (17%), 2021 = 2-4 (33%).
The ledger context: PSU is the program on the wrong side of BOTH documented Big Ten admissions — 2005 two-seconds (time added for Michigan, walk-off) and 2014 (Vonn Bell INT + play-clock FG, Big Ten admitted both next day). The authorship lineage's two historical nodes both have PSU as the victim; the decade's one-score data shows the same program bleeding in exactly the game class where authorship lives. Receipts and statistics point at the same door. NOT proof of causation — a correlation flag the crew-layer analysis must now test.

## FLAG 2 — Michigan 2024-2025: mediocre seasons with ELITE close-game records (the inverse-quality anomaly)
Every other program's mediocre seasons crater in one-score games (PSU 2025: 17%, ND 2016: 12%, Clemson 2025: 25%, PSU 2021: 33%). Michigan's two mediocre seasons did the OPPOSITE:
- 2024: 8-5 overall, avg margin 2.1 → one-score 5-1 (83%)
- 2025: 9-4 overall, avg margin 7.2 → one-score 3-0 (100%), road 2-0
No other program in the 70-season dataset posts back-to-back mediocre seasons with 83%+ close-game records. And the pattern is LIVE, not historical: week 1 of 2026, Michigan — a 27.5-point favorite with a new-look roster — won a one-score game over a MAC program on a restored second after the clock hit zero. That's three consecutive seasons of overperformance vs. quality, ending in the documented event.

## FLAG 3 — Georgia road one-score: 9-1 (90%)
Road close-game winning at 90% across a decade is exceptional — road one-score is the hardest cell in the table for everyone else (Alabama 13-6, Clemson 11-6, Michigan 9-6, PSU 8-11). Logged alongside the Williamson receipt: SEC validated 9 of 11 complaints against the crew that officiated Georgia at Auburn (Oct 2025), permanently banned the lead referee, result stood. Flag, not conclusion — but road one-score is where an officiating edge would show first (no crowd, no schedule excuse, sample small).

## What would falsify each flag
- FLAG 1: crew-level analysis shows PSU's one-score losses distributed randomly across crews/conferences (then it's performance, not authorship)
- FLAG 2: Michigan's 2024-25 close wins show no common crew/conference thread; average quality-adjusted
- FLAG 3: Georgia's road wins explained by defense/quality (avg margin says Georgia 2017-2025 was elite — 9-1 may be quality). This flag is the weakest of the three.

## API backlog (honest gaps)
- Final AP ranks not joined (outcome proxy = W-L + bowl status)
- Penalty differentials NOT in this report — requires ~935-game ESPN summary fetch (running now, results in task1b report)
- No quality adjustment (SRS/margin-weighted) yet — next compute pass
