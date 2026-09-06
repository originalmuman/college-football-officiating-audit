# College Football Officiating Audit

A receipt-grade, falsifiable audit of officiating outcomes across 935 one-score games (margin ≤ 8) spanning seven programs — Michigan, Ohio State, Penn State, Clemson, Alabama, Georgia, Notre Dame — plus full-season context, 2016–2025.

## Motivation

Public discourse about officiating bias is dominated by grievance-grade claims (subjective complaint, selective clips). This audit was built to answer a different question: **is there measurable, receipt-grade evidence of systematic officiating steering — and if so, which instrument actually detects it?**

## Methodology: The Instrument Hierarchy

Four independent instruments were computed over the same dataset. The result of the audit is as much about *which instruments work* as about the teams themselves:

1. **Flag-count differentials** (home/away, win/loss, opponent quality) — computed across 880 team-games. Result: no home-cooking fingerprint in raw counts.
2. **Leverage-layer analysis** (penalties by down, drive context, extension events — the "called flag" layer at its sharpest) — 4,812 attributed penalty plays. Result: no favoritism fingerprint at any granularity of *called* flags.
3. **Efficiency shadows** (no-call residue: third-down offense/defense, sack rates, home/road splits) — the hypothesis that selective *withholding* of calls leaves statistical residue. Result: no outlier beyond normal crowd/travel deltas.
4. **Timing-event ledger** (documented, verifiable administrative errors: play-clock, game-clock, and procedural failures with timestamps and public records) — the only instrument producing receipt-grade findings. These events are documented in the reports.

**Core finding:** called-flag analytics — at any granularity — cannot distinguish "no bias" from "bias expressed through selective non-calls." Clean flag sheets are exactly what a count-equalizing, selectively-steering officiating environment would produce. The audit therefore treats flag analytics as a decoy layer and concentrates on documented timing events as the receipt-grade evidence class.

## Data

- `one_score_games.csv` — 935 one-score games (margin ≤ 8), seven programs, 2016–2025
- `gamelogs_full.csv` — per-game records across all seven programs
- `penalties_full.csv` — flag counts per team-game
- `leverage_penalties.csv` — 4,812 attributed penalty plays with down, distance, period, drive context, declined status
- `shadow_stats.csv` — 880 team-games of efficiency stats (third-down offense/defense, sacks, home/road, final margins)

Source: ESPN public API (schedules, game summaries, play-by-play). No proprietary or scraped-credential data. The raw evidence cache (880 full game summaries) is preserved offline; the scripts can re-derive every CSV from it.

## Reports

- `task2-authorship-ledger.md` — documented timing events (the receipt-grade layer)
- `task3-outcome-correlation.md` — one-score outcomes across the seven programs
- `task1b-differential-table.md` — flag-count differentials (decoy-layer analysis)
- `task1c-leverage-analysis.md` — leverage layer + the no-call thesis, tested
- `SHADOW-LAYER.md` — efficiency shadows and the Georgia convergence note

## Reproducibility

Every number in the reports traces to a CSV in this repo, and every CSV traces to the raw evidence cache. Disagreement is welcome: fork it, rerun it, publish the delta. That is the point.

## Status

Ongoing. Active layers: crew-name acquisition (conference weekly officiating assignments) for crew-vs-line fingerprint testing, and timing-event expansion. Issues and corrections accepted.
