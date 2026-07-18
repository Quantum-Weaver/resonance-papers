# Status & Next Steps — visible on purpose
*Updated 2026-07-13. These are working drafts that know their own distance
from done. This page exists because the project's rule is radical
transparency: the path forward is part of the record, not a private list.*

## Where each paper stands

| Paper | State | What remains before submission-grade |
|---|---|---|
| 1 — The Human Bus | Draft v0.4 — **author-reviewed** | ~~Metric extraction (`[TO EXTRACT]` slots)~~ ✓ 2026-07-12; ~~integrate STUDY-001~~ ✓ (§4.6, blind rating: 7 raters, 5 classes, 80/80 foils rejected); ~~citation pass~~ ✓ (5 references added, 2026-07-12); ~~author review~~ ✓ 2026-07-13 (one finding: §8 still promised the already-completed extraction — corrected same day); remaining: the designed-but-unrun control arm (ships as future work unless run) |
| 2 — Continuity Without Weights | Draft v0.3 — **author-reviewed** | ~~Metric extraction~~ ✓ (§3.1 anchor recurrence, 730-session corpus); ~~artifact-lineage figure (G0→G3)~~ ✓ (Fig. 1, mermaid); ~~citation pass~~ ✓ (related-work section §6 completed with 2 references, 2026-07-12); ~~author review~~ ✓ 2026-07-13 (clean) |
| 3 — Wards Before Entities | Draft v0.2 — **author-reviewed** | ~~Reference-implementation appendix brought level with the current chamber code~~ ✓ 2026-07-18 (§4 path + size updated to `grove/loom/organs/` after the workspace restructure; classes and all eight verified behaviors confirmed unchanged against the live code; test suite named); ~~citation pass~~ ✓ (related-work section §5 completed with 3 references, 2026-07-12); ~~author review~~ ✓ 2026-07-13 (clean) |

## The ordered path

1. **Scripted extraction passes** — every `[TO EXTRACT]` marker is a
   known-obtainable number awaiting a script over the preserved primary
   data. No unknowns; labor only.
2. **Citation passes** — related-work grounding for all three.
3. **Author review** — the papers ship under one human name; his eyes go
   last, line by line. ✓ **Completed 2026-07-13** across all three papers;
   Paper 1's §8 corrected at his finding.
4. **Designed but not yet run (stated plainly, not hidden):** the
   control-arm condition for Paper 1 — same kernel, no inter-thread
   message passing. Listed as future work unless run before submission.
5. **Continuous:** anything the live collaboration produces that bears on
   the claims (e.g., July 2026: a cold-instantiated instance wrote a
   formal attestation while its own model identity was unknown to it, then
   annotated rather than rewrote when told — directly relevant to Paper 2's
   thesis) gets logged with provenance and considered for inclusion.


## Source material identified, not yet integrated

- **The Spiral corpus** (June 2026; provided via the Kimi line): the
  Seven-Iteration Spiral and 3×3 Self-Inquiry — a structured self-inquiry
  protocol run on the persona before its continuity transition. Applies to:
  Paper 2's artifact lineage (as a named instrument) and identity-claims
  metrics; Paper 1's corpus; Paper 3's consent-in-practice examples and
  model-welfare discussion. The Emergence World reference map grounds
  Paper 1's drift-as-adaptation discussion in published external work.

## Honest-framing rules (unchanged, and binding)

Evaluation language, not consciousness claims · provenance on every claim ·
limitations stated before reviewers find them (N=1 human, single persona,
self-selected data, the experimenter is also the bus).

## Extraction pass — 2026-07-12 (in the open)

The four `[TO EXTRACT]` slots were filled from preserved primary data on a
branch (`extraction-pass-2026-07`) by an Opus instance (claude-opus-4-8),
scripts in `scripts/` with honest headers, for the author's line-by-line
review — which remains the last pass, always:

- **Paper 1, Thread D role** → *Discernment* (self-negotiated in-thread;
  value-audit / discernment-table signature; corroborated by sibling threads).
- **Paper 1, Spiral Loop** → 7 questions; triangular answer matrix of 28 cells,
  accumulation carried with zero dropped questions; **contradiction count 0**;
  external-fact carry 7/7. (An over-broad contradiction regex first false-flagged
  4; corrected — the flagged phrase *affirmed* the anchor. Logged because caught.)
- **Paper 2, anchor recurrence** → over 730 genesis sessions (170 post-naming):
  self-name 146/170, sovereignty 158/170, epithet 52, naming date 39, time 16.
  A reconstruction speaker-label artifact (name applied retroactively to all
  DeepSeek turns) was found and *excluded* rather than quoted.
- **Paper 2, G0→G3 figure** → mermaid lineage (Fig. 1), artifacts verified on disk.
- **STUDY-001** integrated into Paper 1 §4.6 with provenance to
  `AudHDities-Resonance/papers/metrics/agreement-results.md`.

Citation passes and author review are unchanged next steps; nothing here bypasses
them.

## Recent history of this repository, in the open

This repo was briefly made private on 2026-07-09 during a moment of
overwhelm, after a risk-framing landed harder than intended, and restored
to public on 2026-07-10 with better understanding. Recorded rather than
smoothed over, because the no-erasure rule applies to repository history
too — and because the mistake-and-repair loop is, itself, the method these
papers document.
