# Scratch — Para-deuterium mole fraction from nuclear spin statistics

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

Equilibrium mole fraction of para-D$_2$ at 50.0 K, where the ortho/para partition
follows from the exchange symmetry of two spin-1 bosons.

- Deuteron: $I=1$ (boson). Total wavefunction symmetric under nuclear exchange.
- Electronic + vibrational ground states symmetric; rotational parity $(-1)^J$.
- So even $J$ pairs with symmetric nuclear spin (ortho), odd $J$ with antisymmetric (para).
- Spin weights: symmetric $I=2\,(5)+I=0\,(1)=6$; antisymmetric $I=1\,(3)$.
- $\theta_r=43.8$ K, $T=50.0$ K, $x=\theta_r/T=0.876$.
- $Z_{\mathrm{ortho}}=6[1+5e^{-6x}]=6.1565$; $Z_{\mathrm{para}}=3[3e^{-2x}+7e^{-12x}]=1.5614$.
- $y_{\mathrm{para}}=1.5614/(6.1565+1.5614)=0.20231\to 0.202$.

Trap check: the hydrogen pairing (even $J$ para weight 1, odd $J$ ortho weight 3) on the
same sums gives $0.3966$, i.e. $0.397$.

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked: dimensionless mole fraction, three significant figures
- [x] Next-best domain considered and rejected in the justification (Quantum Mechanics / Identical particles)
- [x] Prompt does not leak the method (gives the symmetry facts, not the pairing)
- [x] Skeleton is not the previous drafts (enzyme kinetics; relativistic threshold) or the gold Harned cell

Arithmetic re-run in Python: $Z_{\mathrm{ortho}}=6.15649$, $Z_{\mathrm{para}}=1.56141$,
$y_{\mathrm{para}}=0.20231$, hydrogen-pattern value $0.39655$.

## Why a frontier model should miss this

- Pattern-matching to H$_2$ gives the wrong pairing and the wrong spin weights. The bosonic
  deuteron reverses the pairing and changes the degeneracies, moving the answer from $0.202$
  to about $0.397$.
- Dropping the nuclear-spin degeneracies, or counting the symmetric manifold as 5 instead of 6,
  also misses.
