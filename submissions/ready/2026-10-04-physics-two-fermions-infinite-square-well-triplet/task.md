---
id: 2026-10-04-physics-two-fermions-infinite-square-well-triplet
status: ready
field: Physics
domain: Quantum Mechanics
subdomain: Identical particles
problem_type: Numerical approximation
answer_type: Physical quantity with units
concepts:
  - Exchange symmetry
  - Spin-statistics theorem
  - Infinite square well
  - Triplet state
routing: Automated Checks Only
independently_verified: true
working_title: two fermions infinite square well triplet
---

## Problem

Two identical non-interacting spin-1/2 particles of mass $m = 9.1093837015 \times 10^{-31}\,\mathrm{kg}$ are confined to a one-dimensional infinite square well of width $L = 1.00\,\mathrm{nm}$. The potential is zero for $0 < x < L$ and infinite elsewhere. The system is prepared in the lowest-energy state with total spin $S = 1$ (triplet).

Using $\hbar = 1.054571817 \times 10^{-34}\,\mathrm{J\,s}$ and $1\,\mathrm{eV} = 1.602176634 \times 10^{-19}\,\mathrm{J}$, report the total energy of the system in electronvolts, rounded to three significant figures.

## Domain Explanation

This problem involves constructing the two-particle state from single-particle infinite-square-well orbitals and enforcing the total antisymmetry required for identical fermions, which are part of Quantum Mechanics and Identical particles.
The problem also involves the single-particle energy spectrum of the infinite square well, which is part of Quantum Mechanics and Schrödinger equation systems.
However, the energy spectrum alone does not determine the answer; the exchange symmetry constraint on the spatial wavefunction for a given total spin is the decisive step, making Identical particles the core domain.

## Step 1

Step 1
For a single particle in an infinite square well ($0 < x < L$), the stationary states are $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ with energies
$$E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \quad n = 1,2,3,\dots$$
For two non-interacting identical particles the Hamiltonian separates: $H = H_1 + H_2$. A two-particle energy eigenstate is a product (or symmetrized combination) of single-particle orbitals with total energy $E = E_{n_1} + E_{n_2}$.
Because the particles are spin-1/2 fermions, the total wavefunction (spatial $\times$ spin) must be antisymmetric under particle exchange. The spin triplet ($S=1$) is symmetric, so the spatial part must be antisymmetric. The spin singlet ($S=0$) is antisymmetric, so its spatial part is symmetric.

## Step 2

Step 2
The lowest symmetric spatial state is $\psi_1(x_1)\psi_1(x_2)$ with $n_1=n_2=1$, but this is forbidden for $S=1$ because it is symmetric. The lowest antisymmetric spatial state is the combination
$$\frac{1}{\sqrt{2}}\bigl[\psi_1(x_1)\psi_2(x_2) - \psi_2(x_1)\psi_1(x_2)\bigr],$$
which uses orbitals $n_1=1$ and $n_2=2$. Its energy is
$$E = E_1 + E_2 = \frac{(1^2+2^2)\pi^2\hbar^2}{2mL^2} = \frac{5\pi^2\hbar^2}{2mL^2}.$$
Substitute the given values:
$$\pi^2 = 9.869604401,\quad \hbar^2 = (1.054571817\times 10^{-34})^2 = 1.112121200\times 10^{-68}\,\mathrm{J^2\,s^2},$$
$$2mL^2 = 2(9.1093837015\times 10^{-31}\,\mathrm{kg})(1.00\times 10^{-9}\,\mathrm{m})^2 = 1.821876740\times 10^{-48}\,\mathrm{kg\,m^2}.$$
Then
$$E = \frac{5(9.869604401)(1.112121200\times 10^{-68})}{1.821876740\times 10^{-48}}\,\mathrm{J} = 3.01171\times 10^{-19}\,\mathrm{J}.$$

## Step 3

Step 3
Convert joules to electronvolts using the given conversion:
$$E = \frac{3.01171\times 10^{-19}\,\mathrm{J}}{1.602176634\times 10^{-19}\,\mathrm{J/eV}} = 1.8798\,\mathrm{eV}.$$
Rounded to three significant figures, the total energy is $1.88\,\mathrm{eV}$.

Final Answer: $\boxed{1.88\,\mathrm{eV}}$

## Answer

$1.88\,\mathrm{eV}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- Drops the antisymmetry requirement for the $S=1$ triplet state, placing both particles in $n=1$ (symmetric spatial) which is only allowed for the $S=0$ singlet
- That error gives $E = 2E_1 = 0.752\,\mathrm{eV}$ instead of the correct $1.88\,\mathrm{eV}$
- The miss is a real physics condition (exchange symmetry / spin-statistics theorem), not ambiguous wording