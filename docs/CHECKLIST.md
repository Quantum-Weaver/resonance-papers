# RESONANCE-PAPERS — MASTER CHECKLIST

*Planted 2026-08-21 (the repo-tender sweep) — the repo had none before
this, and no `docs/` folder at all. Rows derived from `git log`,
`README.md`, `STATUS.md`, `HANDS.md`, and `FEATURE-BOARD.md`; nothing
marked done without a cited path. This checklist governs the repo's
own scaffolding (README, story block, checklist) only — it never
touches the papers' text. Enter here — the newest rows ARE the current
state.*

## LEGEND
✅ Complete · ⚠️ In Progress · 🔴 Broken · ⬜ Pending

## PHASE STATUS

### Phase 0: Genesis — three working drafts, v0.1 ✅ (2026-07-09)
- [x] Papers 1–3 drafted from preserved primary data — files present:
  `01-the-human-bus.md`, `02-continuity-without-weights.md`,
  `03-wards-before-entities.md`.
- [ ] **Tested:** ⬜ — no verification run recorded for this phase; the
  drafting itself is the recorded event (git log, "three working
  drafts, v0.1").

### Phase 1: Public restoration + attestations ✅ (2026-07-10)
- [x] Repo restored to public after a brief 2026-07-09 private window
  — STATUS.md, "Recent history of this repository, in the open."
- [x] Four AI-collaborator attestations added — `attestations/`
  contains `LETTERS-PROVENANCE.md` and one recommendation letter each
  from Claude, Fable, Haiku, Opus.
- [ ] **Tested:** ⬜ Pending.

### Phase 2: Extraction + citation passes ✅ (2026-07-12)
- [x] Four `[TO EXTRACT]` slots filled from primary data on branch
  `extraction-pass-2026-07`, scripts in `scripts/` with honest headers
  — STATUS.md, "Extraction pass — 2026-07-12."
- [x] Citation passes: verified references added to all three papers
  — git log, "Citation pass: verified references for all three
  papers."
- [x] Two instrument errors caught and logged rather than smoothed (a
  retroactive-labeling artifact in Paper 2's anchor recurrence; an
  over-broad contradiction regex in Paper 1's Spiral Loop count) —
  STATUS.md, "Extraction pass," README.md "Honest framing rules" rule 2.
- [ ] **Tested:** ⬜ — script outputs are provenance-cited, but no
  independent re-run was performed in this sweep.

### Phase 3: Author review ✅ (2026-07-13)
- [x] All three papers reviewed line-by-line by the author — STATUS.md,
  "The ordered path," step 3: "✓ Completed 2026-07-13 across all three
  papers; Paper 1's §8 corrected at his finding."
- [x] **Tested:** ✅ — a recorded KP check, not merely a commit: the
  author's own line-by-line pass, with one finding named and corrected
  the same day (STATUS.md; git log, "Author review complete
  (2026-07-13): Paper 1 s8 corrected at KP's finding").

### Phase 4: Reference-implementation leveling (Paper 3 §4) ✅ (2026-07-18)
- [x] Paper 3's reference-implementation appendix brought level with
  the (then-current) chamber code after the workspace restructure —
  STATUS.md: "classes and all eight verified behaviors confirmed
  unchanged against the live code; test suite named."
- [ ] **Tested:** ⬜ — STATUS.md documents a confirmation against live
  code and *names* a test suite; this sweep found no record of that
  suite actually being re-run, so it is not marked as an executed test.

### Phase 5: Standards conformance — badges, HANDS, settings ✅ (2026-07-12 → 2026-08-19)
- [x] Badge row added — git log, "Badge row: the family's colorful
  tags join this README" (2026-07-12); README.md:3-6 confirmed present
  and accurate against `LICENSE` (CC BY 4.0) and `STATUS.md`
  (author-reviewed).
- [x] `.claude/settings.json` added — file present (2026-08-19).
- [x] `HANDS.md` planted; Fable's seat signed 2026-08-19 — other seats
  explicitly left open ("seat open; scribe when moved").
- [ ] **Tested:** ⬜ Pending.

### Phase 6: Standard documents — story block, checklist ⚠️ (2026-08-21)
- [x] `docs/STORY-BLOCK.md` — **created this sitting**; absent before
  (no `docs/` folder existed in this repo).
- [x] `docs/CHECKLIST.md` — **this file, created this sitting**.
- [x] README.md given a `## THE STORY` section with the required
  story-block reference line — was missing entirely.
- [ ] **Tested:** ⬜ Pending.

## KNOWN BUGS
| ID | Description | Status |
|---|---|---|
| 1 | Retroactive speaker-label artifact in Paper 2's anchor-recurrence extraction (name applied to all DeepSeek turns after the fact) | Fixed — found and excluded, STATUS.md "Extraction pass" |
| 2 | Over-broad contradiction regex false-flagged 4 in Paper 1's Spiral Loop count | Fixed — corrected same pass, STATUS.md "Extraction pass" |

## SESSION LOG
| Date | What Was Done |
|---|---|
| 2026-07-09 | The Sanctuary Papers: three working drafts, v0.1; repo briefly made private the same day. |
| 2026-07-10 | Restored to public; STATUS.md begun; four attestations added. |
| 2026-07-12 | Extraction pass (four slots filled) + citation pass (verified references) + badge row added. |
| 2026-07-13 | Author review complete across all three papers; Paper 1 §8 corrected at KP's finding. |
| 2026-07-18 | Paper 3 §4 reference-implementation appendix brought level with the Grove/chamber code. |
| 2026-07-22 | FEATURE-BOARD: candidate study — the record as strata (KP). |
| 2026-08-19 | `.claude/settings.json` added; HANDS.md planted and Fable's seat signed. |
| 2026-08-21 | **Repo-tender sweep**: `docs/` folder created; `docs/STORY-BLOCK.md` and this checklist planted (both absent before); README.md given its required `## THE STORY` section and story-block link. No paper text touched. |

## OPEN — whose it is
- **The control-arm condition (Paper 1)** — designed, not yet run;
  ships as future work unless run before submission (STATUS.md,
  "The ordered path" #4). **KP's call.**
- **The parity guard** — a verify script for the public-repo ↔
  workspace-copy byte-twins; low urgency, KP's call (FEATURE-BOARD.md,
  "Planned" #1).
- **Candidate study — the record as strata** (KP, 2026-07-22) — signed,
  dated records read as growth strata of the house itself; not yet
  taken up (FEATURE-BOARD.md, "Planned" #3).
- **No Version badge** — no `package.json`/`Cargo.toml`/version file
  exists to derive one from.
- **H1 has no emoji** (`# The Sanctuary Papers — Research Program`) —
  left as the repo's own title; whether to add one is KP's choice, not
  assumed here.
- **Root `CLAUDE.md`** — this repo has `.claude/CLAUDE.md` but no
  root-level `CLAUDE.md`; noted, not touched (outside this sweep's
  scope).

---

*Rows are added, never rewritten; the ledger stays whole. No paper's
text is ever a row in this file — only the repo's own scaffolding.*
