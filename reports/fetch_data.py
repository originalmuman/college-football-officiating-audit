#!/usr/bin/env python3
"""Fetch sports-reference CFB data via Wayback Machine and parse to JSON."""
import requests, time, json, os, re, sys
from bs4 import BeautifulSoup

YEARS = list(range(2016, 2026))
CONFS = ['sec','acc','big-ten','big-12','pac-12','american','independent','mwc','mac','sun-belt','cusa']
TEAMS = {'michigan':'Michigan','ohio-state':'Ohio State','penn-state':'Penn State',
         'alabama':'Alabama','georgia':'Georgia','clemson':'Clemson','notre-dame':'Notre Dame'}
WB = 'https://web.archive.org/web/20260301id_/https://www.sports-reference.com/cfb/'
OUT = '/app/conversations/6a3ddebce7bbd796cd3467f1/ledger-audit/data'
os.makedirs(OUT, exist_ok=True)

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) research-historical-data-pull'})

def fetch(path, tries=4):
    cache = os.path.join(OUT, path.replace('/', '_'))
    if os.path.exists(cache):
        return open(cache, encoding='utf-8', errors='replace').read()
    for i in range(tries):
        try:
            r = s.get(WB + path, timeout=90)
            if r.status_code == 200 and len(r.text) > 5000:
                open(cache, 'w', encoding='utf-8').write(r.text)
                time.sleep(0.8)
                return r.text
        except Exception:
            time.sleep(4)
    print('FAIL', path, file=sys.stderr)
    return None

def txt(c):
    return c.get_text(strip=True) if c else ''

def parse_standings(html, conf, year):
    soup = BeautifulSoup(html, 'html.parser')
    t = soup.find('table', id='standings')
    rows = []
    if not t or not t.find('tbody'):
        return rows, ''
    for r in t.find('tbody').find_all('tr'):
        d = {c.get('data-stat'): c for c in r.find_all(['th','td'])}
        rows.append({'conf': conf, 'year': year,
                     'school': txt(d.get('school_name')),
                     'w': txt(d.get('wins')), 'l': txt(d.get('losses')),
                     'srs': txt(d.get('srs')), 'sos': txt(d.get('sos')),
                     'ap_pre': txt(d.get('rank_pre')), 'ap_high': txt(d.get('rank_min')),
                     'ap_final': txt(d.get('rank_final')), 'notes': txt(d.get('notes'))})
    m = re.search(r'Champion:?\s*<[^>]*>([^<]+)', html)
    champ = m.group(1).strip() if m else ''
    return rows, champ

def parse_schedule(html, slug, year):
    soup = BeautifulSoup(html, 'html.parser')
    t = soup.find('table', id='schedule')
    games = []
    if not t or not t.find('tbody'):
        return games
    for r in t.find('tbody').find_all('tr'):
        d = {c.get('data-stat'): c for c in r.find_all(['th','td'])}
        try:
            pf = int(txt(d.get('points'))); pa = int(txt(d.get('opp_points')))
        except (ValueError, TypeError):
            continue
        oppa = d.get('opp_name')
        href = oppa.find('a').get('href') if oppa and oppa.find('a') else ''
        games.append({'year': year, 'team': slug,
                      'g': txt(d.get('g')), 'date': txt(d.get('date_game')),
                      'opp': txt(oppa), 'opp_href': href,
                      'loc': txt(d.get('game_location')), 'res': txt(d.get('game_result')),
                      'pts': pf, 'opp_pts': pa,
                      'notes': txt(d.get('notes'))})
    return games

def main():
    data = {'standings': [], 'champions': {}, 'schedules': {}}
    for y in YEARS:
        for c in CONFS:
            h = fetch(f'conferences/{c}/{y}.html')
            if not h:
                print('MISSING conf', c, y, file=sys.stderr)
                continue
            rows, champ = parse_standings(h, c, y)
            data['standings'].extend(rows)
            if champ:
                data['champions'][f'{c}-{y}'] = champ
            print(f'conf {c} {y}: {len(rows)} teams', flush=True)
    for slug in TEAMS:
        for y in YEARS:
            h = fetch(f'schools/{slug}/{y}-schedule.html')
            if not h:
                print('MISSING sched', slug, y, file=sys.stderr)
                continue
            g = parse_schedule(h, slug, y)
            data['schedules'][f'{slug}-{y}'] = g
            print(f'sched {slug} {y}: {len(g)} games', flush=True)
    with open(os.path.join(OUT, 'parsed.json'), 'w') as f:
        json.dump(data, f)
    n = sum(len(v) for v in data['schedules'].values())
    print('DONE. standings rows:', len(data['standings']), 'games:', n)

if __name__ == '__main__':
    main()
