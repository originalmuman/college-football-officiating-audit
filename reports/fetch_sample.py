#!/usr/bin/env python3
"""Fetch per-game penalty data for Big Ten flagships (Michigan, Ohio State, Penn State)
seasons 2023-2025 from ESPN's public JSON API. Dedupes shared games by event id."""
import json, time, urllib.request, csv, os

TEAMS = {"130": "Michigan", "194": "Ohio State", "213": "Penn State"}
SEASONS = [2023, 2024, 2025]
BASE = "https://site.api.espn.com/apis/site/v2/sports/football/college-football"
OUT = os.path.dirname(os.path.abspath(__file__))

def get(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "curl/7.81.0"})
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if i == retries - 1:
                print("FAIL", url, e)
                return None
            time.sleep(2)

# 1. collect (event_id, season, team_id) pairs from schedules
events = {}  # event_id -> {"season": s, "teams": set of our team ids that played it}
for tid in TEAMS:
    for s in SEASONS:
        for st_type in (2, 3):
            d = get(f"{BASE}/teams/{tid}/schedule?season={s}&seasontype={st_type}")
            if not d: continue
            for ev in d.get("events", []):
                eid = ev["id"]
                if eid not in events:
                    events[eid] = {"season": s, "teams": set(), "name": ev.get("name")}
                events[eid]["teams"].add(tid)
            time.sleep(0.4)
print(f"unique games: {len(events)}")

# 2. fetch each game summary, extract penalties + home/away
rows = []
cache_path = os.path.join(OUT, "summaries_cache.json")
cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
for i, (eid, meta) in enumerate(sorted(events.items())):
    if eid in cache:
        d = cache[eid]
    else:
        d = get(f"{BASE}/summary?event={eid}")
        if d is None: continue
        cache[eid] = d
        if i % 20 == 0: json.dump(cache, open(cache_path, "w"))
        time.sleep(0.5)
    if "boxscore" not in d: continue
    # penalties per team
    pens = {}
    for t in d["boxscore"].get("teams", []):
        for st in t.get("statistics", []):
            if st.get("name") == "totalPenaltiesYards":
                dv = st.get("displayValue", "")
                parts = dv.split("-")
                pens[str(t["team"]["id"])] = (parts[0], parts[1] if len(parts) > 1 else "")
    # header: competitors with homeAway, score
    hdr = d.get("header", {})
    comps = hdr.get("competitions", [{}])[0].get("competitors", [])
    for tid, tname in TEAMS.items():
        if tid not in meta["teams"]: continue
        me = next((c for c in comps if str(c.get("team", {}).get("id")) == tid), None)
        opp = next((c for c in comps if str(c.get("team", {}).get("id")) != tid), None)
        if not me or not opp: continue
        if str(me["team"]["id"]) not in pens or str(opp["team"]["id"]) not in pens:
            continue
        nsite = hdr.get("competitions", [{}])[0].get("neutralSite", False)
        rows.append({
            "season": meta["season"], "team": tname, "team_id": tid,
            "date": hdr.get("competitions", [{}])[0].get("date", "")[:10],
            "opponent": opp["team"].get("displayName", ""), "opponent_id": opp["team"]["id"],
            "homeAway": me.get("homeAway", ""), "neutral": nsite,
            "team_score": me.get("score", ""), "opp_score": opp.get("score", ""),
            "team_pen": pens[str(me["team"]["id"])][0], "team_pen_yds": pens[str(me["team"]["id"])][1],
            "opp_pen": pens[str(opp["team"]["id"])][0], "opp_pen_yds": pens[str(opp["team"]["id"])][1],
        })
json.dump(cache, open(cache_path, "w"))
with open(os.path.join(OUT, "sample_gamelogs.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print(f"rows written: {len(rows)}")
