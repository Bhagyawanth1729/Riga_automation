---
id: 2026-10-10-biology-splice-junction-translation
status: ready
field: Biology
domain: Molecular Biology
subdomain: RNA processing
problem_type: Transformation between representations
answer_type: Biological sequence
concepts:
  - pre-mRNA splicing
  - reading frame
  - translation
routing: Automated Checks Only
independently_verified: true
working_title: splice-junction translation
---

## Problem

An alternatively spliced transcript is written 5′→3′ as two exons separated by one intron:

`exon 1: CCCAUGGAAU`

`intron: GUAUAGCUCC`

`exon 2: CCGAAUGGUGA`

Splicing removes the entire intron and joins the two exon strings directly; no nucleotide is added at the junction. Translation begins at the first AUG in the mature mRNA and proceeds in that reading frame until the first in-frame stop codon. Use the following codon assignments: AUG = Met (M), GAA = Glu (E), UCC = Ser (S), UGG = Trp (W), and UGA = stop. Report the resulting peptide as its one-letter amino-acid sequence, omitting the stop symbol.

What peptide sequence is produced?

## Domain Explanation

This problem involves intron removal and exon joining, which are part of Molecular Biology and RNA processing.
The problem also involves codon reading and peptide synthesis, which are part of Molecular Biology and Translation.
However, translation supplies the decoding convention after the splice; the central scientific operation is determining the mature RNA reading frame created by RNA processing.

## Step 1

Step 1: Remove the intron and join the exon sequences exactly at the stated splice junction. The mature mRNA is therefore `CCCAUGGAAUCCGAAUGGUGA`; the intronic `UAG` is absent and cannot act as a stop codon.

## Step 2

Step 2: Locate the first start codon in the mature sequence. It begins at the fourth nucleotide, so the translation frame is partitioned as `AUG | GAA | UCC | GAA | UGG | UGA`. The `UCC` codon is formed across the exon junction, which is why the frame must be set after splicing rather than by translating the unspliced string.

## Step 3

Step 3: Apply the supplied codon assignments to the codons in Step 2. They give Met–Glu–Ser–Glu–Trp followed by UGA, so the requested one-letter peptide sequence is `MESEW`.

Final Answer: $\boxed{\mathrm{MESEW}}$

## Answer

$\mathrm{MESEW}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [ ] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- The intron contains a tempting stop codon, and the exon 1/exon 2 junction creates the UCC codon. A model that translates the precursor, or carries exon 1's frame through the splice without rebuilding the mature RNA, will return a different peptide.
