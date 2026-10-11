# Scratch — splice-site-mutation-reading-frame-shift

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

- Integer: 62

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked
- [x] Next-best domain considered and rejected in the justification
- [x] Prompt does not leak the method
- [x] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

- The model may assume exon skipping always causes a frameshift. Here E2 length (90 nt) is a multiple of 3, so skipping it preserves the frame. The model must check the length modulo 3, not assume frameshift.
- The model may miscount the codons in E1 (93 nt = 31 codons, not 30 or 32) and thus misidentify the last codon of E1 and the frame at the junction.
- The model may not verify that E3's length (96 nt) is a multiple of 3, so the stop codon UAA at the end is in-frame in the mutant as well.
- The model may incorrectly think the E1–E3 junction creates a new codon spanning the junction (e.g., `GAA` or `UGG`), but since E1 ends at a codon boundary, the frame is preserved.
- The problem requires careful accounting: 31 codons in E1, then 31 sense codons in E3 before the stop, total 62 amino acids.

## Sequence verification

E1 (93 nt = 31 codons):
AUG GCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AUG
Count: 31 codons × 3 = 93 nt ✓
Last codon: AUG (positions 91-93) ✓

E2 (90 nt = 30 codons):
GCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGC
Count: 30 codons × 3 = 90 nt ✓

E3 (96 nt = 32 codons):
AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU UAA
Count: 32 codons × 3 = 96 nt ✓
Last codon: UAA (stop) ✓

Wild-type: E1(31) + E2(30) + E3(32) = 93 codons total, stop at codon 93
Mutant: E1(31) + E3(32) = 63 codons, stop at codon 62 (31 from E1 + 31 sense from E3 before stop at E3 codon 32)
Answer: 62 ✓