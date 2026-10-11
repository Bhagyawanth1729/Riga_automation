---
id: 2026-10-03-chemistry-para-deuterium-mole-fraction-from-nuclear-spin-s
status: ready
field: Chemistry
domain: Physical Chemistry and Spectroscopy
subdomain: Statistical mechanics
problem_type: Numerical approximation
answer_type: Numerical scalar approximation
concepts:
  - Nuclear spin statistics
  - Ortho- and para-deuterium
  - Rotational partition function
  - Exchange symmetry
routing: Automated Checks Only
independently_verified: true
working_title: Para-deuterium mole fraction from nuclear spin statistics
---

## Problem

The two deuterons in D$_2$ are spin-1 bosons. Exchange of the two nuclei multiplies the rotational wavefunction by $(-1)^J$, while the electronic and vibrational ground states are symmetric under the same exchange. Treat D$_2$ as a rigid rotor with rotational term values $E_J=\theta_r J(J+1)$ and $\theta_r=43.8\,\mathrm{K}$; vibration and electronic excitation are frozen out at the working temperature. A catalyst equilibrates the two nuclear-spin species: call ortho-D$_2$ the species with symmetric nuclear-spin wavefunction (total spin 0 or 2) and para-D$_2$ the species with antisymmetric nuclear-spin wavefunction (total spin 1). At $50.0\,\mathrm{K}$, report the equilibrium mole fraction of para-D$_2$, rounded to three significant figures.

## Domain Explanation

This problem involves the exchange symmetry of two spin-1 nuclei and the resulting partition of the rotational levels of a homonuclear diatomic into ortho and para species, which are part of Physical Chemistry and Spectroscopy and Statistical mechanics.
The problem also involves the rule that the total wavefunction of identical bosons is symmetric under exchange, which is part of Quantum Mechanics and Identical particles.
However, the symmetry rule is only the constraint; the object computed is a rotational-state population ratio, so the physical-chemistry pair is the core.

## Step 1

Step 1
Interchange of the two deuterons must leave the total wavefunction unchanged, because each deuteron is a boson. The electronic and vibrational ground states are symmetric under this exchange, so the product of the rotational and nuclear-spin factors must itself be symmetric. A rotational state of quantum number $J$ carries exchange parity $(-1)^J$, so even $J$ pairs with symmetric nuclear spin and odd $J$ with antisymmetric nuclear spin. Two spin-1 nuclei have six symmetric spin states, with total spin $I=2$ (five states) or $I=0$ (one state), and three antisymmetric states with $I=1$. Therefore ortho-D$_2$ (symmetric spin, sixfold) occupies even $J$, and para-D$_2$ (antisymmetric spin, threefold) occupies odd $J$.

## Step 2

Step 2
With $x=\theta_r/T=43.8/50.0=0.876$, the partition sums are
$$Z_{\mathrm{ortho}}=6\sum_{J\ \mathrm{even}}(2J+1)e^{-xJ(J+1)},\qquad
Z_{\mathrm{para}}=3\sum_{J\ \mathrm{odd}}(2J+1)e^{-xJ(J+1)}.$$
Retaining $J\leq3$ (the $J=4$ term is $1.3\times10^{-6}$),
$$Z_{\mathrm{ortho}}=6\left[1+5e^{-6x}\right]=6\left[1+5(5.216\times10^{-3})\right]=6.1565,$$
$$Z_{\mathrm{para}}=3\left[3e^{-2x}+7e^{-12x}\right]=3\left[3(0.17342)+7(2.72\times10^{-5})\right]=1.5614.$$

## Step 3

Step 3
The equilibrium mole fraction of para-D$_2$ is the fraction of molecules in the odd-$J$, antisymmetric-spin levels, so
$$y_{\mathrm{para}}=\frac{Z_{\mathrm{para}}}{Z_{\mathrm{ortho}}+Z_{\mathrm{para}}}
=\frac{1.5614}{6.1565+1.5614}=0.20231,$$
which rounds to $0.202$.

Final Answer: $\boxed{0.202}$

## Answer

$0.202$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- The reflex is the hydrogen pattern: even $J$ para with weight 1 and odd $J$ ortho with weight 3. Deuterium is a boson with nuclear spin 1, so the pairing reverses and the weights become 6 (symmetric) and 3 (antisymmetric). The hydrogen pairing evaluated on the same partition sums returns $0.397$, nearly a factor of two away from the correct $0.202$.
- A second failure path is dropping the nuclear-spin degeneracy altogether (weights 1) or double-counting the symmetric manifold as five states instead of six.
