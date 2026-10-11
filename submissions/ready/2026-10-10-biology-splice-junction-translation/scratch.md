# Scratch — splice-junction translation

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

- Mature RNA: `CCCAUGGAAUCCGAAUGGUGA`
- Reading frame: `AUG | GAA | UCC | GAA | UGG | UGA`
- Peptide: `MESEW`

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked
- [x] Next-best domain considered and rejected in the justification
- [x] Prompt does not leak the method
- [x] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

- The intron contains `UAG`, while the mature exon junction creates `UCC`. Translating before splicing or retaining the precursor frame produces a plausible but wrong peptide.
