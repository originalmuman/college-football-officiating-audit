#!/usr/bin/env python3
"""Compute per-program per-season penalty differentials, home/away splits,
one-score-game splits and records; merge with sports-reference standings (SRS,
AP final). Writes analysis_output.json for report generation."""
import csv, json, os
from collections import defaultdict

OUT = os.path.dirname(os.path.abspath(__file__))
rows = []
with open(os.path.join(OUT, "gamelogs_full.csv")) as f:
    for r in csv.DictReader(f):
        try:
            r["season"] = int(r["season"]); r["team_score"] = int(r["team_score"])
            r["opp_score"] = int(r["opp_score"]); r["team_pen"] = int(r["team_pen"])
            r["team_pen_yds"] = int(r["team_pen_yds"]); r["opp_pen"] = int(r["opp_pen"])
            r["opp_pen_yds"] = int(r["opp_pen_yds"])
            r["neutral"] = (str(r["neutral"]).lower() == "true")
        except (ValueError, TypeError):
            continue
        rows.append(r)

# sports-reference standings for context (SRS, AP final, W-L)
st = {}
data = json.load(open(os.path.join(OUT, "data", "parsed.json")))
for r in data["standings"]:
    st[(r["school"], r["year"])] = r

def fnum(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return None

results = {}
by_ts = defaultdict(list)
for r in rows:
    by_ts[(r["team"], r["season"])].append(r)

for (team, season), games in sorted(by_ts.items()):
    g = {"season": season, "team": team,
         "games": len(games),
         "wins": sum(1 for r in games if r["team_score"] > r["opp_score"]),
         "losses": sum(1 for r in games if r["team_score"] < r["opp_score"]),
         "ties": sum(1 for r in games if r["team_score"] == r["opp_score"])}
    # overall penalty differentials
    g["pen_diff"] = sum(r["opp_pen"] - r["team_pen"] for r in games)
    g["pen_yds_diff"] = sum(r["opp_pen_yds"] - r["team_pen_yds"] for r in games)
    g["team_pen_pg"] = round(sum(r["team_pen"] for r in games) / len(games), 2)
    g["opp_pen_pg"] = round(sum(r["opp_pen"] for r in games) / len(games), 2)
    # venue splits (exclude neutral-site games from home/away)
    home = [r for r in games if not r["neutral"] and r["homeAway"] == "home"]
    away = [r for r in games if not r["neutral"] and r["homeAway"] == "away"]
    neut = [r for r in games if r["neutral"]]
    for label, subset in (("home", home), ("away", away), ("neutral", neut)):
        g[label + "_n"] = len(subset)
        if subset:
            g[label + "_pen_diff"] = sum(r["opp_pen"] - r["team_pen"] for r in subset)
            g[label + "_pen_yds_diff"] = sum(r["opp_pen_yds"] - r["team_pen_yds"] for r in subset)
            g[label + "_pen_diff_pg"] = round(sum(r["opp_pen"] - r["team_pen"] for r in subset) / len(subset), 2)
    # one-score games (margin <= 8)
    close = [r for r in games if abs(r["team_score"] - r["opp_score"]) <= 8]
    g["one_score_n"] = len(close)
    g["one_score_w"] = sum(1 for r in close if r["team_score"] > r["opp_score"])
    g["one_score_l"] = sum(1 for r in close if r["team_score"] < r["opp_score"])
    g["one_score_pen_diff"] = sum(r["opp_pen"] - r["team_pen"] for r in close)
    ch = [r for r in close if not r["neutral"] and r["homeAway"] == "home"]
    ca = [r for r in close if not r["neutral"] and r["homeAway"] == "away"]
    g["one_score_home_w"] = sum(1 for r in ch if r["team_score"] > r["opp_score"])
    g["one_score_home_l"] = sum(1 for r in ch if r["team_score"] < r["opp_score"])
    g["one_score_away_w"] = sum(1 for r in ca if r["team_score"] > r["opp_score"])
    g["one_score_away_l"] = sum(1 for r in ca if r["team_score"] < r["opp_score"])
    # season point margin
    g["avg_margin"] = round(sum(r["team_score"] - r["opp_score"] for r in games) / len(games), 2)
    # close-game avg margin
    if close:
        g["one_score_avg_margin"] = round(sum(r["team_score"] - r["opp_score"] for r in close) / len(close), 2)
    # sports-reference context
    s = st.get((team, season), {})
    g["sr_w"] = s.get("w"); g["sr_l"] = s.get("l")
    g["srs"] = fnum(s.get("srs")); g["sos"] = fnum(s.get("sos"))
    g["ap_final"] = s.get("ap_final") or None
    g["ap_pre"] = s.get("ap_pre") or None
    results[f"{team}-{season}"] = g

with open(os.path.join(OUT, "analysis_output.json"), "w") as f:
    json.dump(results, f, indent=1)

# quick integrity report
print("team-seasons:", len(results))
print("total game rows:", len(rows))
missing = [(t, y) for t in ["Michigan", "Ohio State", "Penn State", "Alabama", "Georgia", "Clemson", "Notre Dame"]
           for y in range(2016, 2026) if f"{t}-{y}" not in results]
print("missing team-seasons:", missing)
lowcov = [(k, v["games"]) for k, v in results.items() if v["games"] < 10]
print("low-coverage (<10 games):", lowcov)
