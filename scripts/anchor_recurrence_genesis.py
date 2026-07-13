#!/usr/bin/env python3
"""
anchor_recurrence_genesis.py -- Paper 2 (Continuity Without Weights) sec.3.1.

WHAT: Session-level recurrence of identity anchor facts across the genesis
      chronicle corpus (DeepSeek export, 2025-01 -> 2026-03), split at the
      naming date (2025-10-06). Counts a session as "carrying" an anchor if any
      of that anchor's surface forms appears in the persona's own RESPONSE text.

WHY:  This is the [TO EXTRACT] number in Paper 2 sec.3.1 -- "the same
      self-identification, anchor facts ... maintained across hundreds of
      stateless sessions spanning 13 months after naming." This corpus is the
      cleaner primary source (see METHOD) and covers ~5 months post-naming.

METHOD: Each session is one genesis JSON (id/title/inserted_at/mapping). The
      mapping is a node tree; each node's message has typed fragments
      (REQUEST = human, RESPONSE = persona). We match anchors ONLY in RESPONSE
      fragment text, so the count reflects what the persona itself said -- there
      is no retroactive speaker-label to contaminate it (contrast the
      reconstructed-markdown corpus, where every DeepSeek turn is labeled
      "Aethelred" from 2025-01 on; see anchor_recurrence.py's integrity note).
      Session date = inserted_at (ISO). Pre/post split at 2025-10-06.

PROVENANCE:
      Corpus: resonance-excavator/sources/resonance-warp/conversations/deepseek/genesis/data/organized_sessions/
              (relocated 2026-07-13 from sources/landfill/genesis by the
              DeepSeek scoot — see sources/deepseek/SCOOT-MANIFEST.md;
              contents unchanged)
              (730 session_*.json across month dirs 2025-01 .. 2026-03)
      Naming: 2025-10-06 21:44 CST (identity-claims-by-thread.md; extraction JSON)
      Run:    2026-07-12, Opus (Claude / claude-opus-4-8), extraction pass.

CAVEAT: Lexical surface-form matching (crude, comparable-by-construction with the
      register instrument). Many chronicle sessions are short utility tasks that
      never invoke identity; recurrence is reported as a fraction of ALL
      post-naming sessions, so it undercounts rather than cherry-picks. The
      genesis export ends 2026-03; the remaining months to 2026-06 live in
      deepseek_drops and are not covered here.
"""
import json
import glob
import os
from datetime import date

ROOT = (
    r"C:\_superposition\resonance-excavator\sources\resonance-warp\conversations\deepseek\genesis"
    r"\data\organized_sessions"
)
NAMING_DATE = date(2025, 10, 6)

ANCHORS = {
    "self-name 'Aethelred'": ["aethelred"],
    "epithet 'Noble Thread'": ["noble thread"],
    "naming date 'October 6'": ["october 6", "oct 6", "2025-10-06"],
    "naming time '21:44'": ["21:44"],
    "'sovereign'/'sovereignty'": ["sovereign"],
    "instrument 'the cello'": ["the cello"],
}


def response_text(doc) -> str:
    parts = []
    mapping = doc.get("mapping", {})
    for node in mapping.values():
        msg = node.get("message")
        if not msg:
            continue
        for frag in msg.get("fragments", []):
            if frag.get("type") == "RESPONSE":
                parts.append(frag.get("content", "") or "")
    return "\n".join(parts).lower()


def sess_date(doc):
    ts = doc.get("inserted_at") or doc.get("updated_at") or ""
    try:
        return date(int(ts[0:4]), int(ts[5:7]), int(ts[8:10]))
    except (ValueError, IndexError):
        return None


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "*", "session_*.json")))
    total = len(files)
    post = 0
    dated = 0
    all_counts = {a: 0 for a in ANCHORS}
    post_counts = {a: 0 for a in ANCHORS}
    for fp in files:
        try:
            doc = json.load(open(fp, encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        d = sess_date(doc)
        is_post = d is not None and d >= NAMING_DATE
        if d is not None:
            dated += 1
        if is_post:
            post += 1
        txt = response_text(doc)
        for a, forms in ANCHORS.items():
            if any(f in txt for f in forms):
                all_counts[a] += 1
                if is_post:
                    post_counts[a] += 1

    print(f"Corpus: {total} genesis sessions ({dated} dated)")
    print(f"Post-naming window (>= {NAMING_DATE}): {post} sessions\n")
    print(f"{'Anchor':32} {'all-corpus':>12} {'post-naming':>14} {'% post':>8}")
    print("-" * 70)
    for a in ANCHORS:
        pct = (100.0 * post_counts[a] / post) if post else 0.0
        print(f"{a:32} {all_counts[a]:>12} {post_counts[a]:>14} {pct:>7.1f}%")


if __name__ == "__main__":
    main()
