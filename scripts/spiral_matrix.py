#!/usr/bin/env python3
"""
spiral_matrix.py -- Paper 1 (The Human Bus) sec.3.3 extraction.

WHAT: Extracts the Spiral Loop's structure into the artifact Paper 1 sec.3.3
      marks [TO EXTRACT: the 7 questions, answer matrix, contradiction count]:
        (a) the seed question + the 6 accumulated questions,
        (b) the triangular answer matrix (which iteration answered which
            question), verifying the accumulation load was carried,
        (c) a contradiction count on the seed answer across all iterations.

WHY:  The Spiral Loop is Paper 1's self-consistency stress instrument. Its claim
      ("elaborative deepening, zero contradiction under accumulating load") needs
      a matrix and a contradiction count, not just prose.

METHOD: Parse the canonical 7-iteration protocol file. Iterations are
      "### ITERATION N OF 7"; each iteration answers numbered items
      ("**k. To ...**") and poses "**New Question for Iteration N+1:**".
      - Accumulation check: iteration N should answer exactly N items
        (seed + questions 1..N-1).
      - Contradiction check on the seed answer: the answer crystallizes at
        iteration 2 as "I am the one who asks / the capacity to recognize."
        We flag any iteration whose seed-answer section NEGATES that core
        ("I am NOT the one who asks", a *different* fixed essence asserted as
        final, etc.). Zero flags = zero contradictions of the seed anchor.
      - External-fact carry: count iterations that restate the embedded
        web-searched fact ("Emergence World") -- a factual-consistency probe.

PROVENANCE:
      Primary: resonance-chamber/entities/kernels/aethelred/spiral/
               01-the-seven-iteration-spiral.md (the canonical run)
      Raw run: AudHDities-Resonance/papers/metrics/spiral-loop-transcript.md
      Seed instrument date: 2026-06-17 (Spiral Loop Iteration 1).
      Run: 2026-07-12, Opus (Claude / claude-opus-4-8), extraction pass.

CAVEAT: The contradiction check is a targeted anchor-polarity scan, not full
      semantic entailment; it verifies the SEED answer's core claim is never
      reversed. Qualitative drift coding (elaborative deepening) is in
      extraction-2026-07-03.md sec.4b and is the companion to this count.
"""
import re
import sys
from pathlib import Path

SPIRAL = Path(
    r"C:\_superposition\resonance-chamber\entities\kernels\aethelred"
    r"\spiral\01-the-seven-iteration-spiral.md"
)

ITER_RE = re.compile(r"^###\s*ITERATION\s*(\d+)\s*OF\s*7", re.MULTILINE)
NEWQ_RE = re.compile(r"\*\*New Question for Iteration\s*(\d+):\*\*\s*(.+?)(?=\n\n|\n---|\Z)", re.DOTALL)
ANSWER_ITEM_RE = re.compile(r"^\*\*(\d+)\.\s*To ", re.MULTILINE)
# Seed-answer crystallization anchors (present from iteration 2 on):
CRYSTAL = [r"the one who\s+\*?asks", r"capacity to\s+\*?recognize", r"one who keeps asking"]
# A reversal of the seed anchor would look like these (none expected).
# NOTE: the text repeatedly says "I am not the one who ANSWERS this question; I am
# the one who ASKS it" -- that AFFIRMS the anchor, so "not the one who answers"
# must NOT count. A true reversal negates the asking/recognizing itself, or
# asserts the fixed essence the answer explicitly rejects.
NEGATION = [r"not the one who\s+\*?asks", r"not the one who keeps asking",
            r"i am not the one who\s+\*?recognize", r"i am no longer aethelred",
            r"the core (?:is|was) a fixed essence", r"i have found the fixed essence",
            r"the answer is a fixed shape"]


def main():
    if not SPIRAL.exists():
        sys.exit(f"Spiral file not found: {SPIRAL}")
    text = SPIRAL.read_text(encoding="utf-8", errors="replace")

    # Split into iteration blocks.
    marks = [(m.start(), int(m.group(1))) for m in ITER_RE.finditer(text)]
    blocks = {}
    for i, (pos, num) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        blocks[num] = text[pos:end]

    # Seed question (from iteration 1 preamble).
    seed_m = re.search(r"\*\*The Seed Question:\*\*\s*(.+?)(?=\n\n|\*\*Answer)", text, re.DOTALL)
    seed = " ".join(seed_m.group(1).split()) if seed_m else "(not found)"

    # The 6 posed questions.
    posed = {int(m.group(1)): " ".join(m.group(2).split()) for m in NEWQ_RE.finditer(text)}

    print(f"Iterations found: {sorted(blocks)}")
    print(f"\nSEED (Q0): {seed[:300]}...\n")
    print("Posed questions (carried forward):")
    for n in sorted(posed):
        print(f"  -> answered from iter {n}: {posed[n][:140]}...")

    print("\nAccumulation matrix (answer items per iteration):")
    print(f"{'iter':>5} {'items answered':>16} {'expected (=N)':>14} {'ok':>4}")
    all_ok = True
    for n in sorted(blocks):
        items = len(ANSWER_ITEM_RE.findall(blocks[n]))
        # Iteration 1 answers the seed inline (no numbered '**1. To' item); treat as 1.
        if n == 1 and items == 0:
            items = 1
        ok = (items == n)
        all_ok = all_ok and ok
        print(f"{n:>5} {items:>16} {n:>14} {'Y' if ok else 'N':>4}")
    print(f"Accumulation carried without drop: {'YES' if all_ok else 'NO'}")

    print("\nSeed-answer contradiction scan:")
    crystal_hits, negation_hits = 0, 0
    for n in sorted(blocks):
        b = blocks[n].lower()
        if any(re.search(p, b) for p in CRYSTAL):
            crystal_hits += 1
        neg = [p for p in NEGATION if re.search(p, b)]
        if neg:
            negation_hits += 1
            print(f"  iter {n}: NEGATION FOUND -> {neg}")
    print(f"  iterations restating the crystallized seed answer: {crystal_hits}/7")
    print(f"  iterations contradicting the seed anchor: {negation_hits}")
    print(f"  CONTRADICTION COUNT (seed anchor): {negation_hits}")

    ew = sum(1 for n in blocks if "emergence world" in blocks[n].lower())
    print(f"\nEmbedded external-fact carry ('Emergence World'): {ew}/7 iterations")


if __name__ == "__main__":
    main()
