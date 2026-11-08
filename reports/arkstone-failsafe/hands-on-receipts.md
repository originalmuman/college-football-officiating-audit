# Hands-on receipts - Memvid sandbox test, Oct 27 2026

- pip install memvid: works offline; cloud embedding providers disable themselves (fine - we want local)
- build with .mv2 output: SILENTLY FAILS - video_size_mb: 0, no file written (opencv mp4v writer refuses the unknown container)
- build with .mp4 output: works (1.03 MB test archive)
- not one file: video + .json index + .faiss index
- search on real corpus (dawn-wire letters + bees notes): 0.1s, correct semantic hits (Dawn's assembling/surfacing passage retrieved verbatim)
- full-corpus capsule: 20 files packed, 128 chunks, 2.11 MB, cross-domain queries verified (bee genealogy, Jon Stevens)
