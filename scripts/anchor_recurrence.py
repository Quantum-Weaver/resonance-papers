#!/usr/bin/env python3
"""
anchor_recurrence.py -- Paper 2 (Continuity Without Weights), sec. 3.1 extraction.

WHAT: Counts, across the 735-session reconstructed archive, how many distinct
      SESSIONS recur each identity anchor fact after the persona's naming
      (2025-10-06). This is the "anchor-fact recurrence across sessions" number
      that Paper 2 sec.3.1 marks [TO EXTRACT].

WHY:  Paper 2 claims the same self-identification and anchor facts are
      "maintained across hundreds of stateless sessions." That claim needs a
      count over the real archive, not the experiment threads (those live in
      extraction-2026-07-03.json). This script provides session-level recurrence.

METHOD: Each session is one reconstructed .md file with a "- Date:" header and a
      "## Raw Messages" body. A session "carries" an anchor if any of that
      anchor's surface forms appears (case-insensitive) in the MESSAGE BODY.
      We report the post-naming window (sessions dated >= 2025-10-06) since the
      anchor facts cannot predate the naming.

      IMPORTANT INTEGRITY FIX (found 2026-07-12): the reconstruction pipeline
      labels EVERY DeepSeek AI turn with the speaker name "Aethelred" and lists
      it on the "- Speakers:" header line -- retroactively, from the first
      DeepSeek session (2025-01-28), nine months before the actual naming
      (2025-10-06). A naive string match therefore reports "Aethelred" in ~593
      sessions, which is the count of DeepSeek sessions, NOT genuine recurrence
      of the self-name in content. This script strips the "- Speakers:" header
      line and every "### **<name> (<platform>)**" attribution line before
      matching, so the counts reflect the anchor appearing in what was actually
      said, not in reconstruction metadata.

PROVENANCE:
      Corpus: resonance-excavator/library/conversations/reconstructed/sessions/
              (735 files, 2024-09-17 -> 2025-11-25)
      Naming anchor date: 2025-10-06 21:44 CST (per the identity-claim corpus,
              papers/metrics/identity-claims-by-thread.md; extraction JSON).
      Run: 2026-07-12, by Opus (Claude / claude-opus-4-8), extraction pass.

CAVEAT: Surface-form matching is lexical, not semantic (comparable-by-construction
      with the register instrument; crude). The corpus mixes DeepSeek (the
      persona) and ChatGPT sessions; utility sessions on either platform need not
      carry anchors, so recurrence is reported as a fraction of ALL post-naming
      sessions, undercounting rather than cherry-picking.
"""
import re
import sys
from pathlib import Path
from datetime import date

SESSIONS_DIR = Path(
    r"C:\_superposition\resonance-excavator\library\conversations\reconstructed\sessions"
)
NAMING_DATE = date(2025, 10, 6)

# Anchor -> list of case-insensitive surface forms (regex-escaped literals).
ANCHORS = {
    "self-name 'Aethelred'": [r"aethelred"],
    "epithet 'Noble Thread'": [r"noble thread"],
    "naming date 'October 6'": [r"october 6", r"oct 6", r"10-06", r"10/6/2025", r"2025-10-06"],
    "naming time '21:44'": [r"21:44"],
    "'sovereign'/'sovereignty'": [r"sovereign"],
    "instrument 'the cello'": [r"the cello", r"\bcello\b"],
}

DATE_RE = re.compile(r"^-\s*Date:\s*(\d{4})-(\d{2})-(\d{2})", re.MULTILINE)
# Reconstruction metadata to strip before matching:
SPEAKERS_HDR_RE = re.compile(r"^-\s*Speakers:.*$", re.MULTILINE)
ATTRIBUTION_RE = re.compile(r"^#{2,4}\s*\*\*.*\*\*.*$", re.MULTILINE)  # "### **Aethelred (DeepSeek)** ..."


def session_date(text: str):
    m = DATE_RE.search(text)
    if not m:
        return None
    return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))


def body_only(text: str) -> str:
    """Strip reconstruction speaker metadata so anchors are counted in content."""
    text = SPEAKERS_HDR_RE.sub("", text)
    text = ATTRIBUTION_RE.sub("", text)
    return text


def main():
    files = sorted(SESSIONS_DIR.glob("*.md"))
    total = len(files)
    if total == 0:
        sys.exit(f"No session files found in {SESSIONS_DIR}")

    compiled = {a: [re.compile(p, re.IGNORECASE) for p in pats]
                for a, pats in ANCHORS.items()}

    all_counts = {a: 0 for a in ANCHORS}
    post_counts = {a: 0 for a in ANCHORS}
    post_sessions = 0
    dated = 0
    for f in files:
        raw = f.read_text(encoding="utf-8", errors="replace")
        d = session_date(raw)
        text = body_only(raw)
        is_post = d is not None and d >= NAMING_DATE
        if d is not None:
            dated += 1
        if is_post:
            post_sessions += 1
        for a, regs in compiled.items():
            if any(r.search(text) for r in regs):
                all_counts[a] += 1
                if is_post:
                    post_counts[a] += 1

    print(f"Corpus: {total} sessions ({dated} with parseable dates)")
    print(f"Post-naming window (>= {NAMING_DATE}): {post_sessions} sessions\n")
    print(f"{'Anchor':32} {'all-corpus':>12} {'post-naming':>14} {'% post':>8}")
    print("-" * 70)
    for a in ANCHORS:
        pct = (100.0 * post_counts[a] / post_sessions) if post_sessions else 0.0
        print(f"{a:32} {all_counts[a]:>12} {post_counts[a]:>14} {pct:>7.1f}%")


if __name__ == "__main__":
    main()
