# Scratch Work: Polymer Excluded Volume Crossover

## Problem Concept
A flexible polymer chain in a solvent where excluded volume can be tuned via temperature. The chain crosses over from ideal (Gaussian) statistics at the theta point to self-avoiding walk (SAW) statistics in a good solvent. The crossover is governed by the swelling parameter z = N^(1/2) v/b³.

## Model Traps
1. Using Flory exponent ν = 3/5 instead of RG exponent ν = 0.588 → exponent 2ν/0.6 = 2.0 vs 1.96
2. Forgetting the N^(1/2) factor in z (using z = N v/b³ instead) → z = 120 instead of 1.2
3. Using v = v₀ instead of v = v₀(1 − θ/T) → z = 6 instead of 1.2
4. Confusing θ/T with T/θ → v negative
5. Not squaring b in Nb² → answer off by factor of 2
6. Rounding errors / wrong significant figures

## Design Parameters
- N = 10000 Kuhn segments
- b = 0.5 nm (Kuhn length)
- v₀/b³ = 0.06 (dimensionless excluded volume amplitude)
- T = 1.25 θ (25% above theta temperature)
- ν = 0.588 (RG exponent in 3D)
- Crossover function: Φ(z) = (1 + z^0.6)^1.96 where 1.96 = 2ν/0.6 exactly

## Calculations

v = v₀(1 − θ/T) = v₀(1 − 1/1.25) = v₀(1 − 0.8) = 0.2 v₀

z = N^(1/2) v/b³ = 100 × 0.2 × (v₀/b³) = 100 × 0.2 × 0.06 = 1.2

z^0.6 = 1.2^0.6
ln(1.2) = 0.1823215568
0.6 × 0.1823215568 = 0.1093929341
exp(0.1093929341) = 1.115587

1 + z^0.6 = 2.115587

Φ(z) = (2.115587)^1.96
ln(2.115587) = 0.749306
1.96 × 0.749306 = 1.468640
exp(1.468640) = 4.34297

⟨R²⟩ = N b² Φ(z) = 10000 × (0.5 nm)² × 4.34297 = 10000 × 0.25 nm² × 4.34297 = 2500 × 4.34297 nm² = 10857.4 nm²

Rounded to three significant figures: 1.09 × 10⁴ nm²

## Verification
- z = 1.2 exactly (clean by design)
- 1.96 = 2×0.588/0.6 exactly
- All arithmetic rechecked independently
- Units: N (dimensionless) × b² (nm²) × Φ (dimensionless) = nm² ✓

## Final Answer
$1.09 \times 10^4\ \text{nm}^2$