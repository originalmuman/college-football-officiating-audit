# Red-Team Pass 001 — Hostile Methodology Review

**Date:** 2026-09-06
**Design:** The audit methodology was submitted, without framing or author identity, to three independent frontier models (Google Gemini 3.5 Flash, MiniMax M3, xAI Grok 4.3), each instructed to act as a hostile statistician hired to defend the conference. The models share no training lineage coordination. Their unedited critiques are below, followed by the convergence analysis.

**Why publish the attack:** An audit that publishes only its own conclusions invites the accusation of cherry-picking. Publishing the strongest available hostile critique alongside the data is the receipt-grade discipline this ledger runs on. Where the critiques land, the methodology changes. Where they converge, we report it.

---

## Hostile Critique — GEMINI

This audit is a masterclass in p-hacking and confirmation bias, designed to manufacture a scandal where none exists. Let’s dismantle this pseudo-science.

**1. Selection Bias:** Conditioning your sample on one-score games is classic *collider bias*. Close games are fundamentally different—coaches take more risks, players fatigue, and play-calling shifts. Furthermore, selecting seven elite, talent-rich programs introduces severe survivorship and selection bias. You cannot infer systemic league-wide officiating patterns from a non-random, highly skewed subset of elite matchups. 

**2. The Multiple-Testing Nightmare:** With 935 games sliced by seven teams, 11 seasons, and dozens of arbitrary "high-leverage" situations (e.g., "third-down in the red zone in the fourth quarter"), you are running hundreds of independent hypothesis tests. Under a standard $\alpha = 0.05$, you are mathematically guaranteed to find false positives. Without a strict Bonferroni or Benjamini-Hochberg correction, your "discoveries" are just statistical noise masquerading as "steering."

**3. "Shadow Stats" Fallacy:** Attributing third-down conversion rates to "withheld calls" is a post-hoc ergo propter hoc absurdity. Third-down success is heavily confounded by offensive/defensive line talent mismatches, defensive scheme, quarterback pressure rates, and weather. Claiming a successful conversion is a "trace" of a missed holding call—without actual proof of a penalty—is unscientific, circular reasoning.

**4. The Crew/Betting Line Delusion:** Joining crew names to closing lines is a correlation nightmare. Crews are not randomly assigned; the conference assigns its highest-rated crews to the most volatile, high-profile, and heavily bet games. Any "market fingerprint" you find is a proxy for game selection, injury reports, and public betting sentiment, not referee bias.

**5. What Would Convince Me:** To survive scrutiny, you must present a pre-registered, double-blind study. You need independent, certified officials grading *every* snap of a randomized sample of all FBS games (not just close ones), comparing actual missed-call rates against a baseline. This must control for team-level EPA (Expected Points Added) and player-tracking data, using a Bonferroni-corrected significance threshold of $p < 0.001$. 

Until then, your audit is nothing but a statistical witch hunt.

---

## Hostile Critique — MINIMAX

**1. Selection bias.** 935 one-score games is not a random sample—it's a conditional one where the *outcome* (close margin) is itself potentially caused by officiating influence. Conditioning on the outcome biases toward finding no effect (Berkson's bias). Worse, 70 team-seasons across 7 hand-picked blue-bloods overrepresents the exact population the auditor suspects. If you pick programs *because* you expect anomalies, your null carries zero inferential weight—Bayes factor collapses. Effect sizes, p-values, all uninterpretable.

**2. Multiple testing.** Dozens of leverage windows (Q4, 3rd-and-long, red zone, two-minute, goal-line, OT, 4th quarter only, final 5 min, final 2 min, final possession…) crossed with penalty types (15+) crossed with teams = thousands of implicit tests. At α=0.05, ~5% false-positive floor before correction. The auditor reports *no* anomaly, which with this test count is statistically unremarkable—it's the expected null. You can't claim "no signal" when your search space guarantees noise.

**3. Shadow stats confounders.** Third-down conversion rate is driven by offensive line talent, QB play, defensive scheme, down/distance, field position, game script, and weather—officiating is a tiny, late-arriving perturbation. A non-call on one play doesn't cause a conversion; it slightly shifts EPA. Power is microscopic. "Drives where a hold/no-call occurred" suffers from selection-on-the-treatment: you're comparing apples to a counterfactual you never observe. Without random assignment, the downstream trace is endogenous. The IV is gone; the replacement is noise.

**4. Crew-name join is theatrical.** Crews rotate, crews are small-N units (often <30 games in sample), closing lines already incorporate public injury/news info, and market efficiency means *any* exploitable crew effect would be arbitraged away pre-kickoff. Detecting a post-hoc crew fingerprint on already-priced games is finding ghosts in a martingale. Confounders: weather, home field, rest, QB availability, and the auditor's own look-ahead bias once crew names are in the dataframe.

**5. What would convince me.** A pre-registered design: all FBS games 2015-2025 (~5,000+), no outcome conditioning, random or fixed effects for crew/game/team, a *single* pre-specified leverage window with justified power calculation (need ~40%+ effect on conversion to detect), random-forest or causal-forest matching on play-level covariates, and a placebo test on NBA crews. Without that, publish nothing.

---

## Hostile Critique — GROK

1. Selection bias: Restricting to one-score games conditions on a post-treatment outcome if officiating affects margins, truncating the distribution and biasing estimates toward zero or sign-flipping effects. The seven programs were chosen precisely because anomalies were suspected; this is post-hoc selection without pre-registered controls or the other 120+ FBS teams, so any “null” or anomaly is conditional on the auditor’s priors and cannot generalize.

2. Multiple testing: 935 games yield hundreds of leverage slices (late-game 3rd-and-long, red-zone 1st down, two-minute drill, etc.). Even at α=0.05, dozens of tests produce 5–15 expected false positives before any correction. Post-hoc redefinition of “high-leverage” windows turns the exercise into unchecked p-hacking; FDR control or pre-commitment to a single index would be required.

3. Shadow stats confounders: Third-down conversion and drive continuation are dominated by talent differentials, offensive-line quality, defensive scheme, weather, and fatigue. A non-call on holding is mechanically correlated with better offensive lines, which also convert more third downs; the proxy therefore captures team strength far more than officiating. No within-game or within-drive fixed effects isolate the officiating channel.

4. Crew/closing-line join: Crews are assigned by conference, experience, and geography, not randomly. Betting lines already embed public narratives, injuries, rest, and motivation; any residual “fingerprint” is unidentified without exogenous crew variation (e.g., weather-induced travel shocks or documented rotation rules). Small per-crew samples further guarantee spurious correlations.

5. Design that survives: Pre-register on all FBS games 2015–2025, include matched control conferences, use crew randomization instruments or difference-in-differences around documented assignment rule changes, apply multiplicity correction, and report minimum detectable effects for leverage events given observed variance.

---

## Convergence Analysis (secretariat)

**All three hostile panels independently attacked the same five points:**

1. **Outcome conditioning.** The one-score sample conditions on a post-treatment variable — if officiating affects margins, conditioning on close games truncates the effect (collider/Berkson bias, named by two of three panels).
2. **Post-hoc program selection.** Seven programs chosen on suspicion nulls carry no inferential weight in this frame.
3. **Multiple testing.** Hundreds of implicit leverage slices at α=0.05 guarantee false positives without pre-registration and FDR/Bonferroni control. MiniMax's sharpest line: "You can't claim 'no signal' when your search space guarantees noise."
4. **Shadow-stat confounding.** Third-down conversion is dominated by talent; Grok's strongest point — offensive lines that convert more also hold more and get held less. The proxy captures team strength, not officiating.
5. **The crew × closing-line join is confounded.** Crews are non-randomly assigned (best crews → biggest games); markets price known information pre-kickoff; per-crew samples are small-N.

**All three panels converged on the same demand:** pre-registration of a single leverage index, expansion beyond one-score conditioning, multiplicity correction, and matched controls.

**The gift inside the attack:** the market-efficiency objection inverts into a superior instrument. If markets are efficient and crew effects are real, closing lines already embed them — so the falsifiable test is not outcomes-vs-line residuals but **line movement in response to crew assignment announcements**. If the market prices crews, that is third-party evidence the effect is real, measurable without any outcome claim by this audit.

**What survives unattacked:** the historical lineage events (2005 Michigan two-seconds, 2014 Big Ten admitted errors, 2026 Week 1 clock-zero) are documented events, not statistical inferences. The published null result stands as a null. The retired-instrument decision (flag counts) was independently endorsed by all three panels' framing.

**Methodology changes adopted from this pass:** (1) pre-registered leverage index before any further public claim; (2) population statistics on all games, one-score set as focus subset only; (3) crew-join target changed from outcome residuals to announcement-response line movement; (4) this pass and all future red-team passes are part of the public record.
