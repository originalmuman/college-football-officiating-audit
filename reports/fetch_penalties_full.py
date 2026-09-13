#!/usr/bin/env python3
"""Fetch per-game penalty data for all 7 programs, 2016-2025, via ESPN summary API.
Incremental cache + CSV writes. Modeled on fetch_sample.py (which proved the source)."""
import json, time, urllib.request, csv, os, re

TEAMS = {"130": "Michigan", "194": "Ohio State", "213": "Penn State", "228": "Clemson",
         "333": "Alabama", "61": "Georgia", "87": "Notre Dame"}
SEASONS = list(range(2016, 2026))
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
                return None
            time.sleep(2)

# collect events from cached schedq files first (no refetch)
events = {}
import glob
for fp in glob.glob(os.path.join(OUT, "data", "schedq_*.json")):
    m = re.match(r"schedq_(\d+)_(\d{4})_(\d)\.json", os.path.basename(fp))
    if not m: continue
    tid, yr = m.group(1), int(m.group(2))
    if tid not in TEAMS: continue
    try: f = json.load(open(fp))
    except Exception: continue
    if f.get("status") != "success": continue
    for ev in f.get("events", []):
        eid = ev["id"]
        if eid not in events:
            events[eid] = {"season": yr, "teams": set()}
        events[eid]["teams"].add(tid)

print(f"unique games to fetch: {len(events)}", flush=True)

cache_path = os.path.join(OUT, "summaries_cache.json")
cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
csv_path = os.path.join(OUT, "penalties_full.csv")

def write_csv(rows):
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["event_id","season","team_id","team","ha","opponent","opp_id","team_score","opp_score","team_pen","team_pen_yds","opp_pen","opp_pen_yds","margin","one_score"])
        w.writerows(rows)

rows = []
done_ids = set()
for i, (eid, meta) in enumerate(sorted(events.items())):
    if eid in cache:
        d = cache[eid]
    else:
        d = get(f"{BASE}/summary?event={eid}")
        if d is None: continue
        cache[eid] = d
        if i % 25 == 0: json.dump(cache, open(cache_path, "w"))
        time.sleep(0.6)
    if "boxscore" not in d: continue
    comps = d.get("header", {}).get("competitions", [])
    if not comps: continue
    comp = comps[0]
    pens = {}
    for t in d["boxscore"].get("teams", []):
        for st in t.get("statistics", []):
            if st.get("name") == "totalPenaltiesYards":
                dv = st.get("displayValue", "").split("-")
                pens[str(t["team"]["id"])] = (dv[0].strip(), dv[1].strip() if len(dv) > 1 else "")
    for c in comp.get("competitors", []):
        tid = str(c["team"]["id"])
        if tid not in TEAMS: continue
        opp = next((o for o in comp.get("competitors", []) if str(o["team"]["id"]) != tid), None)
        if not opp: continue
        try:
            ours = int(c.get("score", {}).get("displayValue", "0") or 0)
            theirs = int(opp.get("score", {}).get("displayValue", "0") or 0)
        except Exception: continue
        tp = pens.get(tid, ("", "")); op = pens.get(str(opp["team"]["id"]), ("", ""))
        margin = ours - theirs
        rows.append([eid, meta["season"], tid, TEAMS[tid], c.get("homeAway", ""),
                     opp["team"].get("abbreviation", ""), str(opp["team"]["id"]),
                     ours, theirs, tp[0], tp[1], op[0], op[1], margin, abs(margin) <= 8])
    if i % 50 == 0:
        write_csv(rows)
        print(f"progress: {i}/{len(events)} games, {len(rows)} rows", flush=True)

write_csv(rows)
json.dump(cache, open(cache_path, "w"))
print(f"DONE: {len(rows)} penalty rows written to {csv_path}", flush=True)
