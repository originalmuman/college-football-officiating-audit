import json, subprocess, os

def query(name, prompt, tools):
    body = json.dumps({
        "model": "grok-4.6",
        "input": [{"role": "user", "content": prompt}],
        "tools": tools
    })
    cmd = ["curl", "-s", "--max-time", "150", "https://api.x.ai/v1/responses",
           "-H", "Authorization: Bearer " + os.environ["XAI_API_KEY"],
           "-H", "Content-Type: " + "application/json", "-d", body]
    try:
        r = json.loads(subprocess.run(cmd, capture_output=True, text=True, timeout=160).stdout)
        texts = []
        for item in r.get("output", []):
            if isinstance(item, dict):
                for c in item.get("content", []):
                    if isinstance(c, dict) and c.get("text"):
                        texts.append(c["text"])
        out = "\n".join(texts) if texts else json.dumps(r)[:300]
    except Exception as e:
        out = "SWEEP FAIL: " + str(e)
    with open(name + ".md", "w") as f:
        f.write(out)
    print(f"=== {name} ===")
    print(out[:1100])
    print()

X = [{"type": "x_search"}, {"type": "web_search"}]

query("4-oregon-pattern", "Search X and the web: Oregon football officiating controversies. Documented cases where Oregon benefited from contested calls: the 2006 Oklahoma onside kick game, the 2022 Washington State down-indicator game, the 2025 Fiesta Bowl Miami pass interference no-call vs Ole Miss, and tonight's September 5 2026 Boise State game (missed kick-catch interference, missed PIs). Any other cases fans cite? Is there a running fan narrative that Oregon gets favorable officiating? Quote the loudest posts with reach numbers.", X)
query("5-convergence-check", "Search X and the web: is anyone publicly building a DATABASE or longitudinal statistical study of college football officiating bias — tracking penalty differentials by team over multiple years, referee crew records against the spread, or league admissions of officiating errors? Look for: academic papers on CFB officiating bias, data-journalism projects, fan databases, betting-analysis sites tracking CFB referee crews the way Covers tracks NBA referees. Who has done the closest work, and what does it cover?", X)
query("6-carrier-trajectory", "Search X: current engagement numbers (views, likes, reposts) on Jason Whitlock's post about the Michigan-Western Michigan ending ('one of the biggest crimes in sports history') and Landon Tengwall's post linking it to the 2005 Michigan-Penn State two-seconds game. Also find: what are the biggest NEW posts or threads about the Michigan clock controversy in the last few hours — any national media, coaches, or notable accounts amplifying it? Who is defending the call vs. attacking it?", X)
