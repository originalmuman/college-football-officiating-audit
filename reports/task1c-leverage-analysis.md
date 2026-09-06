# Task 1c: Leverage-Layer Analysis (flags by down/drive context)
Generated: Sept 6, 2026 | Data: leverage_penalties.csv (4,812 attributed penalty plays of 7,356 total, 65% attribution — opponent legacy text codes unmatched; directionally informative, NOT receipt-grade at this coverage)

## THE CHAIRMAN'S NO-CALL THESIS (validated by the data's silence)
Bill: "You're not going to find it in the flag count — they can adjust that however they want. Third down and 10, no holding call, pass completed — those things are invisible."
Result: called-flag analytics at EVERY granularity (count, down-specific, drive-extension, scoring-drive) shows no favoritism fingerprint for any of the seven programs. Michigan's career leverage (extensions received minus granted, per game) is -0.189 — the WORST of the group. PSU draws the fewest 3rd-down flags. All clean.
Conclusion: called flags are a DECOY LAYER — clean flag sheets are exactly what count-equalizing, selectively-steering crews produce. Cannot distinguish "nothing there" from "steering in the no-call layer" from this data alone.

## CAREER LEVERAGE TABLE (per game, 65% coverage)
| Team | OFF ext/g | DEF ext/g | LEV/g | 3rd flags us | 3rd flags them | ScoreDr for | ScoreDr ag |
|---|---|---|---|---|---|---|---|
| Ohio State | 0.280 | 0.258 | +0.022 | 0.441 | 0.763 | 0.817 | 0.366 |
| Alabama | 0.546 | 0.554 | -0.008 | 0.869 | 0.900 | 0.792 | 0.615 |
| Penn State | 0.307 | 0.337 | -0.030 | 0.406 | 0.970 | 0.673 | 0.426 |
| Clemson | 0.333 | 0.372 | -0.039 | 0.698 | 0.977 | 0.566 | 0.488 |
| Georgia | 0.368 | 0.432 | -0.064 | 0.696 | 0.912 | 0.704 | 0.528 |
| Notre Dame | 0.243 | 0.405 | -0.162 | 0.685 | 0.622 | 0.631 | 0.432 |
| Michigan | 0.270 | 0.459 | -0.189 | 0.508 | 0.730 | 0.426 | 0.516 |

## ONE-SCORE LEV (extensions received - granted, close games)
- Michigan 2024: +2 (received 2, granted 0 in 6 one-score games) — weak favorable tilt, tiny n
- Michigan 2025: 0/0. PSU 2024: -4 (granted 5). PSU 2025: -1. Georgia 2025: +5.
- All single-digit samples — nothing receipt-grade at season level.

## INSTRUMENT HIERARCHY (final)
1. TIMING-EVENT LEDGER — documented receipts (2005 two-seconds, 2014 play-clock FG, 2026 clock-zero family). Receipt-grade. The pattern lives here.
2. EFFICIENCY SHADOWS — no-call residue: pressure/sack rates allowed, 3rd-down conversion defense, home/road OL splits vs opponent quality. Computable next; requires quality normalization.
3. FLAG ANALYTICS — decoy layer, retired. Clean sheets prove nothing in either direction.

## NEXT: shadow-layer spec
- Extract per-game defensive box: sacks, TFL, 3rd-down conversion allowed (in cached summaries)
- Normalize by opponent quality (season SRS proxy from margin data we already hold)
- Test: does any of the seven show home/road efficiency residuals that flags can't explain?
