import json, subprocess, os, sys

def query(name, prompt, tools):
    body = json.dumps({
        "model": "grok-4.6",
        "input": [{"role": "user", "content": prompt}],
        "tools": tools
    })
    cmd = ["curl", "-s", "--max-time", "150", "https://api.x.ai/v1/responses",
           "-H", "Authorization: Bearer " + os.environ["XAI_API_KEY"],
           "-H", "Content-Type: application/json", "-d", body]
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
    print(out[:1200])
    print()

X = [{"type": "x_search"}, {"type": "web_search"}]
W = [{"type": "web_search"}]

query("1-referee-crew", "Search X and the web: who was the referee / officiating crew for the Western Michigan at Michigan game on September 5, 2026? Names of the lead referee and crew if available. Also: were the officials from the Big Ten, and any pre-game crew assignment announcements?", X)
query("2-bigten-response", "Search X and the web: has the Big Ten conference issued ANY statement about the Michigan vs Western Michigan clock controversy from September 5, 2026 (extra play granted after clock hit zero)? Any indication a statement is coming Sunday? What are reporters saying about whether the result can or will be changed?", X)
query("3-betting-flip", "Search X and the web: what did the Michigan vs Western Michigan final play (September 5, 2026) do to sports betting? Michigan was a heavy moneyline favorite — the clock-zero Hail Mary flipped the game winner from Western Michigan 12-6 to Michigan 13-12. Look for: the closing point spread, over/under, how much money flipped on the moneyline, sportsbook statements, bettor outrage posts with reach numbers.", X)
