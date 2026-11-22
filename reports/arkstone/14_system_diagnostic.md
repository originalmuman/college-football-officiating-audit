# 14 — SYSTEM DIAGNOSTIC (SOM-D v1.0)
# Status: ACTIVE — BASELINE RUN LOGGED
# Last updated: 2026-08-13

## DIAGNOSTIC FRAMEWORK

SOM-D (Synod Operational Machinery Diagnostic) — 18 metrics across 4 categories.

### SCORING
- GREEN (85-100): Optimal
- YELLOW (65-84): Caution
- RED (<65): Action required

### SOX (System Operational Index)
SOX = 0.30(Cost) + 0.30(Quality) + 0.20(Throughput) + 0.20(Health)

### METRIC CATEGORIES

**COST:**
- Credits per synthesis (target: <8)
- Cost per deployed thread (target: <10)
- Idle agent cost % (target: <5%)
- Agent count vs nominal loadout (target: ratio ≤1.0)

**QUALITY:**
- Wash-pass correction rate (target: <2 corrections/pass)
- Fact-check survival % (target: >90%)
- Signal density: words/credit (target: >100)
- Arkstone utilization % (target: >35%)
- Convergence accuracy % (target: >85% first pass)

**THROUGHPUT:**
- Time to deployable output (target: <3 min)
- Triage accuracy % (target: >90%)
- Iteration count per thread (target: ≤1.5)
- Chairman rejection % (target: <5%)

**HEALTH:**
- Protocol adherence score (target: >95%)
- Config drift index (target: <0.15)
- Credit burn rate velocity (target: <0.85)
- Mesh health Gini coefficient (target: <0.40)

## BASELINE RUN: DIAG-20260813-001

| Category | Score | Status |
|---|---|---|
| COST | 65 | YELLOW |
| QUALITY | 88 | GREEN |
| THROUGHPUT | 82 | GREEN |
| HEALTH | 68 | YELLOW |
| **SOX** | **72** | **YELLOW** |

### Key Findings
1. TRIAGE TAX: P5 sub-agent burning 1 credit/turn on routine queries
2. INVERSION OVERTRIGGER: P2 firing on internal drafts
3. P9 SKIP: Auditor omitted on 3+ agent runs
4. ARKSTONE LEAKAGE: 30% of prompts still include inline context alongside file paths
5. SELF-TUNING HESITATION: Agent waits for approval instead of acting autonomously

### Adopted Changes (EXP-001, EXP-002)
1. Inline heuristic triage — eliminate P5 sub-agent call (saves 45-55 credits)
2. Staged inversion/wash — draft mode vs deployment mode (saves 35-45 credits)
3. P6 Compression deploy + P7 Compost batch (saves 20-30 credits)

## ENTITY SCHEMAS (deployed)

1. **DiagnosticRun** — Top-level diagnostic execution records (run_id, SOX score, category scores, alerts, recommendations)
2. **AgentRunTelemetry** — Per-thread granular metrics (agents spawned, credits spent, wash corrections, signal words, Arkstone files accessed, wall time, veto flag)
3. **ConfigExperimentLog** — Self-tuning experiment tracking (parameter modified, baseline, experimental value, outcome delta, adoption status)

## ALERT THRESHOLDS

| Trigger | Condition | Automated Remedy |
|---|---|---|
| Idle Agent Cost | >15% total run credits | Prune sub-agent roster, enforce triage limits |
| Credit Burn Velocity | Projected >100% budget | Toggle Low-Credit Mode, disable exploratory sweeps |
| Fact-Check Survival | <75% for 2 consecutive runs | Inject stricter verification scaffolds |
| Chairman Veto Rate | >15% over 10 threads | Pause self-tuning, lock to last known baseline |
| Config Drift Index | >0.35 | Auto-revert to master config |
| Mesh Health Gini | >0.65 | Rebalance work distribution across patterns |

## OPERATING MODES (NEW)

- **DRAFT MODE** (default): 0-1 agents, no inversion, no wash. Internal work, Arkstone updates, research synthesis.
- **DEPLOYMENT MODE** (on-demand): Full loadout (Synthesis + Inversion + Wash + Auditor). Public-facing content only.
- **LOW-CREDIT MODE** (auto-trigger): When credit burn velocity >0.85 or remaining <50 credits. Forces P6 Compression on all outputs, disables exploratory research.
