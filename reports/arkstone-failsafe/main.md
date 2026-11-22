---
title: Ark Failsafe Capsule
summary: Two-tier memory doctrine - plain markdown as the eternal failsafe (Tier 1), a disposable offline Memvid search capsule compiled from it (Tier 2). Build script, receipts, and rebuild protocol.
---

# Ark Failsafe Capsule

Settled Oct 27 2026 after a receipts-grade evaluation (landscape survey + live sandbox test) of the second-brain / AI-memory wave that Memvid went viral inside.

## The two-tier doctrine

**Tier 1 - the failsafe, the source of truth:** plain markdown. The notes tree, the ledgers, the letters, the arkstone threads. Append-only, eternal-format, readable by any tool forever, git-able, USB-stick-portable. This was already the architecture; the survey confirmed it is the *correct* one rather than the default one (markdown + SQLite scored 4.93/5.0 against our seven criteria; nothing beat it on stability).

**Tier 2 - the resource:** a disposable Memvid search capsule *compiled from* Tier 1 by `build_capsule.py` (this folder). It holds nothing unique. Fully offline, no docker, local embeddings (all-MiniLM-L6-v2), ~0.1s semantic retrieval. If Memvid dies or breaks format compatibility, rebuild from markdown and lose nothing but the tool.

## Files in this folder

- `build_capsule.py` - the rebuild script (run: `python3 /app/notes/ark-failsafe/build_capsule.py`)
- `capsule/` - ark-capsule.mp4 + index pair + build-receipt.md (dated proof of last good build)
- `landscape-report.md` - the full survey (8 candidates, receipts-grade scoring)
- `hands-on-receipts.md` - the sandbox test log

## Honest receipts from the evaluation

- The advertised `.mv2` single-file format **silently fails** with the local opencv writer (zero-byte ghost). `.mp4` output works. The "single file" is actually a video + index pair.
- Memvid is v0.1.0-era young (maturity risk 2.0/5 in the survey) - which is exactly *why* it is Tier 2 and not Tier 1.
- Mem0 scored 1.0/5 on append-only (it mutates memory silently - anti-doctrine). Graphiti's bi-temporal edges are receipts-grade but not portable the way markdown is.

## Maintenance

The Sunday Arkstone Backup rebuilds the capsule weekly after the entity dump (step 5). If a future session finds the capsule missing or broken: `pip install memvid` if needed, run the script, check build-receipt.md says OK. The markdown is the ark; this is just its search engine.
