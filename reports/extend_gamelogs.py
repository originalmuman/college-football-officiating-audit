#!/usr/bin/env python3
"""Extend gamelog pull: 7 programs x seasons 2016-2025 via ESPN public API.
- Schedules cached as data/schedq_{tid}_{season}_{stype}.json
- Game summaries appended to summaries_cache.json (dumped every 20 new fetches)
- Rows appended incrementally to gamelog_rows.jsonl so partial progress survives
- Final CSV: gamelogs_full.csv (sample_gamelogs.csv rows + new rows), deduped
"""
import json, time, urllib.request, csv, os, sys

OUT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(OUT, "data")
BASE = "https://site.api.espn.com/apis/site/v2/sports/football/college-football"

# ESPN team ids (Georgia=61 on ESPN; 52 is Georgia's sports-reference id but Florida State on ESPN)
TEAMS = {"130": "Michigan", "194": "Ohio State", "213": "Penn State",
         "333": "Alabama", "61": "Georgia", "228": "Clemson", "87": "Notre Dame"}
SEASONS = list(range(2016, 2026))

def get(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "curl/7.81.0"})
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if i == retries - 1:
                print("FAIL", url, e, flush=True)
                return None
            time.sleep(2)

def sched_path(tid, s, st):
    return os.path.join(DATA, "schedq_%s_%s_%s.json" % (tid, s, st))

def fetch_schedule(tid, s, st):
    p = sched_path(tid, s, st)
    if os.path.exists(p):
        try:
            return json.load(open(p))
        except Exception:
            pass
    d = get("%s/teams/%s/schedule?season=%s&seasontype=%s" % (BASE, tid, s, st))
    if d and ("events" in d or "team" in d):
        json.dump(d, open(p, "w"))
        time.sleep(0.4)
    return d

def main():
    cache_path = os.path.join(OUT, "summaries_cache.json")
    cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
    rows_path = os.path.join(OUT, "gamelog_rows.jsonl")
    log_path = os.path.join(OUT, "extend_log.txt")

    def log(msg):
        with open(log_path, "a") as f:
            f.write(msg + "\n")
        print(msg, flush=True)

    done = set()
    if os.path.exists(rows_path):
        for line in open(rows_path):
            try:
                r = json.loads(line)
                done.add((r["team_id"], str(r["season"])))
            except Exception:
                pass

    total_new = 0
    for tid, tname in TEAMS.items():
        for s in SEASONS:
            if (tid, str(s)) in done:
                log("SKIP %s %s (already done)" % (tname, s))
                continue
            evs = {}
            for st in (2, 3):
                d = fetch_schedule(tid, s, st)
                if not d:
                    continue
                for ev in d.get("events", []):
                    evs[ev["id"]] = ev.get("name", "")
            if not evs:
                log("NO EVENTS %s %s" % (tname, s))
                continue
            season_rows = []
            for eid in evs:
                d = cache.get(eid)
                if d is None:
                    d = get("%s/summary?event=%s" % (BASE, eid))
                    if d is None:
                        continue
                    cache[eid] = d
                    total_new += 1
                    if total_new % 20 == 0:
                        json.dump(cache, open(cache_path, "w"))
                    time.sleep(0.45)
                if "boxscore" not in d or "header" not in d:
                    continue
                pens = {}
                for t in d["boxscore"].get("teams", []):
                    for stt in t.get("statistics", []):
                        if stt.get("name") == "totalPenaltiesYards":
                            dv = stt.get("displayValue", "").split("-")
                            pens[str(t["team"]["id"])] = (dv[0], dv[1] if len(dv) > 1 else "")
                comps = d["header"].get("competitions", [{}])[0].get("competitors", [])
                me = next((c for c in comps if str(c.get("team", {}).get("id")) == tid), None)
                opp = next((c for c in comps if str(c.get("team", {}).get("id")) != tid), None)
                if not me or not opp:
                    continue
                if str(me["team"]["id"]) not in pens or str(opp["team"]["id"]) not in pens:
                    continue
                season_rows.append({
                    "season": s, "team": tname, "team_id": tid,
                    "date": d["header"].get("competitions", [{}])[0].get("date", "")[:10],
                    "opponent": opp["team"].get("displayName", ""),
                    "opponent_id": opp["team"].get("id"),
                    "homeAway": me.get("homeAway", ""),
                    "neutral": d["header"].get("competitions", [{}])[0].get("neutralSite", False),
                    "team_score": me.get("score", ""), "opp_score": opp.get("score", ""),
                    "team_pen": pens[str(me["team"]["id"])][0],
                    "team_pen_yds": pens[str(me["team"]["id"])][1],
                    "opp_pen": pens[str(opp["team"]["id"])][0],
                    "opp_pen_yds": pens[str(opp["team"]["id"])][1],
                })
            with open(rows_path, "a") as f:
                for r in season_rows:
                    f.write(json.dumps(r) + "\n")
            log("%s %s: %s events, %s rows w/ penalties" % (tname, s, len(evs), len(season_rows)))
            json.dump(cache, open(cache_path, "w"))
    json.dump(cache, open(cache_path, "w"))
    log("FETCH PHASE DONE. new summaries fetched: %s" % total_new)

    fieldnames = ["season", "team", "team_id", "date", "opponent", "opponent_id",
                  "homeAway", "neutral", "team_score", "opp_score",
                  "team_pen", "team_pen_yds", "opp_pen", "opp_pen_yds"]
    seen = set()
    all_rows = []
    def key(r):
        return (str(r["team_id"]), str(r["season"]), str(r["date"]), str(r["opponent_id"]))
    sample = os.path.join(OUT, "sample_gamelogs.csv")
    if os.path.exists(sample):
        with open(sample) as f:
            for r in csv.DictReader(f):
                k = key(r)
                if k not in seen:
                    seen.add(k)
                    all_rows.append(r)
    for line in open(rows_path):
        r = json.loads(line)
        k = key(r)
        if k not in seen:
            seen.add(k)
            all_rows.append(r)
    with open(os.path.join(OUT, "gamelogs_full.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_rows)
    log("FINAL CSV gamelogs_full.csv: %s rows" % len(all_rows))

if __name__ == "__main__":
    main()
