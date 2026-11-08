# Build receipt
- **Date:** 2026-11-01T11:35:43
- **Files packed:** 25 (skipped: 0)
- **Chunks:** 297 | backend: opencv | codec: mp4v
- **Capsule size:** 4.91 MB video + 0.33 MB index
- **Status:** OK

Query pattern (any future session):
```python
from memvid import MemvidRetriever
r = MemvidRetriever('/app/notes/ark-failsafe/capsule/ark-capsule.mp4', '/app/notes/ark-failsafe/capsule/ark-capsule-index.json')
r.search('<question>', top_k=3)
```