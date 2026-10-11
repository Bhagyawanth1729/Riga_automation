# Scratch — franck-condon-vibronic-progression-displaced-oscillators

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

- Most intense vibronic peak wavenumber: 27000 cm⁻¹
- v'_max = 3
- S = 3.2033

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked
- [x] Next-best domain considered and rejected in the justification
- [x] Prompt does not leak the method
- [x] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

- Forgetting the 2π in ω = 2πcν̃ (using ω = cν̃) gives S ≈ 0.51, v'_max=0, answer 22500
- Forgetting the factor 1/2 in S = μω/(2ħ) (Δr_e)² gives S ≈ 6.41, v'_max=6, answer 31500
- Using h instead of ħ gives the same error as missing 2π (since h = 2πħ), answer 22500
- Assuming the 0-0 transition is always the strongest (a common qualitative misconception) gives 22500
- Unit errors on Δr_e (using Å or cm instead of m) produce wildly incorrect S
- The problem requires careful unit handling (kg, m, J, s, rad) and the correct angular frequency, not just the spectroscopic wavenumber