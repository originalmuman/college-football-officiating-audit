# Task 1b: Penalty Differential Report (2016-2025)
Generated: Sept 6, 2026 | Data: penalties_full.csv (935 team-games, 98.7% coverage, ESPN summary API + consensus lines)
pen_diff = flags drawn minus flags against. Negative = favorable. 1S = one-score games.

## CAREER PROFILE (flags per game)
| Team | PF/g | PA/g | Career net | Home net | Away net | 1S net | non-1S net |
|---|---|---|---|---|---|---|---|
| Ohio State | 5.96 | 4.86 | +1.10 | +1.05 | +1.18 | +0.24 | +1.31 |
| Alabama | 6.18 | 5.59 | +0.59 | -0.12 | +1.66 | +2.09 | +0.11 |
| Notre Dame | 5.52 | 5.65 | -0.13 | -0.64 | +0.54 | 0.00 | -0.19 |
| Michigan | 4.97 | 5.32 | -0.35 | -0.39 | -0.30 | +0.15 | -0.53 |
| Georgia | 5.26 | 5.69 | -0.43 | -0.86 | +0.10 | +0.11 | -0.62 |
| Penn State | 4.78 | 5.68 | -0.90 | -1.29 | -0.37 | -0.56 | -1.08 |
| Clemson | 5.30 | 6.41 | -1.11 | -1.19 | -1.00 | -1.66 | -0.88 |

## FINDING 1 (NEGATIVE — valuable): No home-cooking signature in flag counts
Across all seven programs, home and away flag differentials are nearly identical (e.g., Michigan home -0.39 vs away -0.30). The naive "officials favor the home team in flags" hypothesis is NOT supported at this tier. Whatever home advantage exists, it does not show in flag counts for elite programs.

## FINDING 2 (REDIRECTION — the instrument correction): The PSU crater is invisible in flag counts
Penn State's decade one-score crater (47%) shows NO flag-count deficit — in fact their career flag differential is FAVORABLE (-0.90). The audit's own documented receipts (2005 two-seconds, 2014 play-clock FG, 2026 clock-zero) are ALL TIMING/ADMINISTRATIVE events, not penalty calls. Conclusion: flag counts are the WRONG INSTRUMENT for this pattern. The authorship lives in clock administration, review rulings, and timing events — exactly what the qualitative event ledger documents. The quantitative layer redirects: build the TIMING-EVENT layer, not more flag analytics.

## FINDING 3 (WEAK SIGNAL): Michigan close-game flag tilt 2024-25
2024: one-score pen diff -1.83 (drew ~2 fewer flags than opponents in one-score games) while going 5-1. 2025: -0.67 while going 3-0. Small samples (6 and 3 one-score games), favorable direction, NOT receipt-grade alone — logged beside the one-score overperformance (Task 3 Flag 2). 2023 note: Michigan's title year shows 3.0 PF/g and net -2.07 — the most favorable single-team-season in the dataset (champion discipline is the null explanation; cannot distinguish from counts).

## BONUS (unplanned): Consensus betting lines captured for all 935 games
The extraction also captured consensus spread/total/moneylines per game (line_details, spread, over_under, our_ml, opp_ml columns) — the betting join for the crew-level anomaly analytics is now sitting in the same CSV, waiting only on crew names (conference weekly assignments / RefMetrics lane).

## Next layer (per the redirection)
1. TIMING-EVENT extraction: final-minute scoring plays, reviews, clock events from the cached summaries (scoringPlays + drives keys are already in the 436MB cache — no refetch needed)
2. Crew names: Big Ten/SEC weekly crew assignments (public) — join to this CSV
3. Then: crew vs. line anomalies, the falsifiable fingerprint test
