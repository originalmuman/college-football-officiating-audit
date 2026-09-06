# Shadow Layer: Efficiency Shadows (No-Call Residue)

## Hypothesis

If officiating steering operates through selective *non-calls* (a hold not thrown on 3rd-and-10, pass interference swallowed in a one-score fourth quarter), the residue should surface in efficiency statistics: third-down conversion rates, sack rates allowed, and home/road splits that called flags cannot explain.

## Data

880 team-games, seven programs, 2016–2025. Third-down offense/defense, sacks taken/forced, home/road, final margins, and one-score flags. Source: ESPN public API summaries (preserved in offline cache).

## Results

Career home-road deltas, third-down offense (percentage points):

| Team | 3rd HOME | 3rd ROAD | Δ | Sacks H/g | Sacks R/g |
|---|---|---|---|---|---|
| Georgia | 48.8 | 43.3 | +5.5 | 0.97 | 1.49 |
| Michigan | 44.1 | 39.7 | +4.4 | 1.51 | 1.58 |
| Notre Dame | 46.4 | 42.6 | +3.8 | 1.37 | 1.96 |
| Clemson | 45.6 | 42.1 | +3.5 | 1.35 | 1.79 |
| Ohio State | 49.4 | 46.7 | +2.7 | 1.49 | 1.50 |
| Alabama | 49.2 | 47.3 | +1.9 | 1.76 | 1.98 |
| Penn State | 41.3 | 42.7 | -1.4 | 1.73 | 1.69 |

All seven programs sit inside the normal crowd/travel home-advantage band. **No Michigan anomaly**: its 2024 (+5.2) and 2025 (+4.7) home-road deltas match its decade norm (+4.4), and sack-protection splits are flat.

The only value that leaves the band is **Georgia's +5.5 career home-road third-down delta**, the largest of the seven — noteworthy in combination with (a) its 9-1 one-score road record and (b) a documented timing-event receipt. Three weak signals from three independent instruments, each individually explainable by opponent-quality confounds. **Logged as a convergence, not a claim.** The next test (spread-adjusted residuals) will either raise or dissolve it.

## Conclusion

The shadow layer joins flag counts and leverage analysis as instruments that return clean readings. The audit's evidence therefore concentrates in the timing-event ledger — documented, verifiable administrative errors — as the only receipt-grade finding class.

Ongoing: spread-adjusted efficiency residuals (lines preserved in shadow_stats.csv) and crew-vs-line fingerprint testing pending crew-name acquisition.
