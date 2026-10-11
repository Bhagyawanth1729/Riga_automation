---
id: 2026-10-03-biology-x-linked-pedigree-generation-conditioning
status: ready
field: Biology
domain: Molecular Biology
subdomain: Mutations and molecular consequences
problem_type: Exact computation
answer_type: Exact scalar
concepts:
  - splice-site mutation
  - reading frame
  - exon skipping
  - frameshift
  - premature stop codon
routing: Automated Checks Only
independently_verified: true
working_title: splice-site-mutation-reading-frame-shift
---

## Problem

A eukaryotic gene has three coding exons (E1, E2, E3) separated by two introns (I1, I2). The genomic sequence of the exon–intron boundaries (5'$\to$3') is:

**E1–I1 boundary (donor site):**
`... CAG | GUAAGU ...`
**I1–E2 boundary (acceptor site):**
`... UACAG | G ...`
**E2–I2 boundary (donor site):**
`... CAG | GUAAGU ...`
**I2–E3 boundary (acceptor site):**
`... UACAG | G ...`

The vertical bar `|` marks the exon–intron junction. The mature mRNA is translated in frame 0 starting at the AUG in E1. The coding sequence of each exon (without UTRs) is:

E1 (93 nt):
`AUG GCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AUG`

E2 (90 nt):
`GCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGC`

E3 (96 nt):
`AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU CCU AAU GGU UAA`

A point mutation changes the invariant `GU` at the 5' splice site of intron 1 (the `GU` immediately after the `|` in E1–I1) to `GC`. This mutation completely abolishes splicing at this donor site, causing **exon 2 skipping** (E2 is omitted from the mature mRNA). In the mutant mature mRNA, E1 splices directly to E3; the exon–exon junction occurs precisely at the E1|E3 boundary with no nucleotides added or removed.

The genetic code is standard. Translation terminates at the first in-frame stop codon (UAA, UAG, or UGA). The initiator AUG in E1 is the only start codon.

**Question:** In the mutant mRNA (E1–E3), how many amino acids are incorporated into the polypeptide *before* translation terminates? Count the initiating methionine as amino acid #1. Report the answer as an integer.

## Domain Explanation

This problem involves a splice-site mutation causing exon skipping and a consequent reading-frame analysis that reveals a premature stop codon, which is core to Molecular Biology and Mutations and molecular consequences. The problem also involves the mechanics of translation and the genetic code, which belong to Molecular Biology and Translation. However, the central challenge is tracking the reading frame across a novel exon–exon junction created by the mutation, not the canonical splicing or translation machinery per se.

## Step 1

Step 1: Determine the reading frame at the E1–E3 junction in the mutant mRNA.
The problem states that the mutant mature mRNA joins E1 directly to E3 with no nucleotides added or removed at the E1|E3 boundary. In the wild-type mRNA, the exons are joined E1–E2–E3. E1 is 93 nt. 93 $\div$ 3 = 31 codons exactly, so E1 ends at a codon boundary (frame 0). E2 is 90 nt, also a multiple of 3, so E2 ends at frame 0. E3 begins in frame 0 and its sequence (given) shows the stop codon UAA at the end in frame 0.
In the mutant, E2 (90 nt) is skipped. Because the E1–E3 junction occurs precisely at the E1|E3 boundary with no nucleotides added or removed, and E1 length is 93 $\equiv$ 0 (mod 3), the reading frame at the junction is **still frame 0**. The first nucleotide of E3 becomes the first nucleotide of the next codon after E1's last codon.

## Step 2

Step 2: Write the mutant coding sequence at the E1–E3 junction and translate until a stop codon.
E1 is 93 nt = 31 codons. The given E1 sequence ends with `... AAU GGU CCU AUG`. The last three nucleotides (positions 91–93) are `AUG`, so codon 31 of E1 is `AUG` (Met).
E3 begins with `AAU GGU CCU...`.
The mutant junction sequence (frame 0) is: `... AUG | AAU GGU CCU AAU GGU CCU ...`
Translation in frame 0:
- Codon 31 (last of E1): `AUG` $\to$ Met
- Codon 32 (first of E3): `AAU` $\to$ Asn
- Codon 33: `GGU` $\to$ Gly
- Codon 34: `CCU` $\to$ Pro
- Codon 35: `AAU` $\to$ Asn
- Codon 36: `GGU` $\to$ Gly
- Codon 37: `CCU` $\to$ Pro
... continue until a stop codon appears in frame 0 in E3.

## Step 3

Step 3: Scan E3 in frame 0 for the first in-frame stop codon.
E3 is 96 nt = 32 codons exactly. The given sequence shows the repeating pattern `(AAU GGU CCU)` and terminates with `UAA`. Since 96 $\equiv$ 0 (mod 3), the reading frame is preserved throughout E3. The stop codon UAA occupies the 32nd codon position of E3 (nucleotides 94–96 of E3). Therefore E3 contributes 31 sense codons before the stop.
Translation in the mutant mRNA:
- E1 contributes 31 codons (all sense; codon 1 = initiator Met, codon 31 = last codon of E1).
- E3 contributes 31 sense codons (codons 1–31 of E3) before the in-frame stop at codon 32.
Total amino acids incorporated = 31 + 31 = 62.

Final Answer: $\boxed{62}$

## Answer

$62$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- The model may assume exon skipping always causes a frameshift. Here E2 length (90 nt) is a multiple of 3, so skipping it preserves the frame. The model must check the length modulo 3, not assume frameshift.
- The model may miscount the codons in E1 (93 nt = 31 codons, not 30 or 32) and thus misidentify the last codon of E1 and the frame at the junction.
- The model may not verify that E3's length (96 nt) is a multiple of 3, so the stop codon UAA at the end is in-frame in the mutant as well.
- The model may incorrectly think the E1–E3 junction creates a new codon spanning the junction (e.g., `GAA` or `UGG`), but since E1 ends at a codon boundary, the frame is preserved.
- The problem requires careful accounting: 31 codons in E1, then 31 sense codons in E3 before the stop, total 62 amino acids.