# Build receipt
- **Date:** 2026-11-15T11:40:17
- **Files packed:** 25 (skipped: 0)
- **Chunks:** 757 | backend: opencv | codec: mp4v
- **Capsule size:** 12.41 MB video + 0.88 MB index
- **Status:** OK

Query pattern (any future session):
```python
from memvid import MemvidRetriever
r = MemvidRetriever('/app/notes/ark-failsafe/capsule/ark-capsule.mp4', '/app/notes/ark-failsafe/capsule/ark-capsule-index.json')
r.search('<question>', top_k=3)
```