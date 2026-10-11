# Scratch — two fermions infinite square well triplet

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

- Two spin-1/2 fermions (electrons) in 1D infinite square well, width L = 1.00 nm
- Non-interacting, so H = H₁ + H₂
- Single-particle energies: E_n = n²π²ℏ²/(2mL²)
- Total spin S=1 → triplet → symmetric spin wavefunction → spatial part MUST be antisymmetric
- Lowest antisymmetric spatial state: n₁=1, n₂=2 (or vice versa) with (ψ₁ψ₂ - ψ₂ψ₁)/√2
- Total energy = E₁ + E₂ = (1²+2²)π²ℏ²/(2mL²) = 5π²ℏ²/(2mL²)
- Plug in numbers → 1.88 eV (3 sig figs)

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked
- [x] Next-best domain considered and rejected in the justification
- [x] Prompt does not leak the method
- [x] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

- Drops the antisymmetry requirement for S=1 triplet: puts both particles in n=1 (which is symmetric spatial, only allowed for S=0 singlet)
- Or thinks S=1 allows symmetric spatial, giving E = 2E₁ = 0.751 eV instead of 1.88 eV
- The miss is a real physics condition (exchange symmetry), not ambiguous wording