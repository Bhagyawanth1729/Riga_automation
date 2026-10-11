---
id: 2026-10-03-physics-two-electron-quantum-dot-singlet-triplet
status: ready
field: Physics
domain: Quantum Mechanics
subdomain: Identical particles
problem_type: Exact computation
answer_type: Exact scalar
concepts:
  - exchange interaction
  - singlet-triplet splitting
  - lowest Landau level
  - fermion antisymmetry
  - first-order perturbation theory
routing: Automated Checks Only
independently_verified: true
working_title: two-electron-quantum-dot-singlet-triplet
---

## Problem

Two electrons are confined in a two-dimensional isotropic parabolic quantum dot with confinement energy $\hbar\omega_0 = 3.0\ \mathrm{meV}$, subject to a perpendicular magnetic field $B = 4.0\ \mathrm{T}$. The effective mass is $m^* = 0.067\ m_e$ and the dielectric constant is $\varepsilon = 12.9\ \varepsilon_0$.

In the limit $\hbar\omega_c \gg \hbar\omega_0$ (where $\omega_c = eB/m^*$ is the cyclotron frequency), the single-particle states are well approximated by the lowest Landau level (LLL) wavefunctions in symmetric gauge:

$\psi_m(r,\phi) = \frac{1}{\sqrt{2\pi}} \frac{1}{l_B} \frac{(r/l_B)^m}{\sqrt{m!}} e^{-r^2/4l_B^2} e^{im\phi}, \quad m = 0,1,2,\ldots$

where $l_B = \sqrt{\hbar/eB}$ is the magnetic length. The single-particle energy is $\hbar\omega_c/2$, independent of $m$ in the strict LLL limit.

The two-electron Hamiltonian is $H = H_1 + H_2 + e^2/(4\pi\varepsilon|r_1-r_2|)$. At zero temperature, the two-electron ground state configuration (in the non-interacting limit) places one electron in $m=0$ and one in $m=1$.

The Coulomb interaction is treated as a perturbation. For the $m=0$ and $m=1$ orbitals, the direct and exchange integrals are:

$J = \langle\psi_0\psi_1|V|\psi_0\psi_1\rangle = \frac{e^2}{4\pi\varepsilon l_B} \sqrt{\frac{\pi}{2}} \cdot \frac{\sqrt{\pi}}{2}$

$K = \langle\psi_0\psi_1|V|\psi_1\psi_0\rangle = \frac{e^2}{4\pi\varepsilon l_B} \sqrt{\frac{\pi}{8}}$

Compute the singlet-triplet energy splitting $\Delta E = E_{\mathrm{triplet}} - E_{\mathrm{singlet}}$ in meV. Round your answer to three significant figures.

Constants:
- $e^2/(4\pi\varepsilon_0) = 1.44\ \mathrm{eV\cdot nm}$
- $\hbar = 6.582\times 10^{-16}\ \mathrm{eV\cdot s}$
- $m_e = 9.109\times 10^{-31}\ \mathrm{kg}$
- $e = 1.602\times 10^{-19}\ \mathrm{C}$
- $1\ \mathrm{T} = 1\ \mathrm{kg/(C\cdot s)}$

Answer format: a single number in meV (e.g., -12.3 meV). A negative value indicates the triplet is the ground state.

## Domain Explanation

This problem involves two interacting electrons in a magnetic field, requiring the construction of properly antisymmetrized total wavefunctions and the evaluation of Coulomb matrix elements in the lowest Landau level, which are core topics in Quantum Mechanics / Identical particles. The problem also involves the Fock-Darwin spectrum and magnetic-length scaling, which belong to Condensed Matter and Materials Physics / Quantum Hall effect. However, the central challenge is the fermion sign rule linking spin symmetry to spatial symmetry and the resulting exchange-energy sign, not the details of Landau-level physics or quantum Hall phenomenology.

## Step 1

Step 1: Compute the magnetic length $l_B$ and the Coulomb energy scale $e^2/(4\pi\varepsilon l_B)$.
The magnetic length is $l_B = \sqrt{\hbar/eB}$. Using $\hbar = 6.582\times 10^{-16}\ \mathrm{eV\cdot s}$, $e = 1.602\times 10^{-19}\ \mathrm{C}$, $B = 4.0\ \mathrm{T} = 4.0\ \mathrm{kg/(C\cdot s)}$:
$eB = 6.408\times 10^{-19}\ \mathrm{kg/s}$
$\hbar/eB = (6.582\times 10^{-16}) / (6.408\times 10^{-19}) = 1.027\times 10^3\ \mathrm{eV\cdot s^2/kg} = 1.027\times 10^3\ \mathrm{J\cdot s^2/kg}$
Convert $\hbar$ to SI: $\hbar = 6.582\times 10^{-16}\ \mathrm{eV\cdot s} \times 1.602\times 10^{-19}\ \mathrm{J/eV} = 1.054\times 10^{-34}\ \mathrm{J\cdot s}$
$\hbar/eB = 1.054\times 10^{-34} / 6.408\times 10^{-19} = 1.645\times 10^{-16}\ \mathrm{m}^2$
$l_B = \sqrt{1.645\times 10^{-16}} = 1.283\times 10^{-8}\ \mathrm{m} = 12.83\ \mathrm{nm}$.

The Coulomb constant in the material: $e^2/(4\pi\varepsilon) = (e^2/(4\pi\varepsilon_0))/\varepsilon_r = 1.44\ \mathrm{eV\cdot nm} / 12.9 = 0.1116\ \mathrm{eV\cdot nm} = 1.116\times 10^{-10}\ \mathrm{eV\cdot m}$.
Thus $e^2/(4\pi\varepsilon l_B) = 1.116\times 10^{-10}\ \mathrm{eV\cdot m} / 1.283\times 10^{-8}\ \mathrm{m} = 8.700\times 10^{-3}\ \mathrm{eV} = 8.700\ \mathrm{meV}$.

## Step 2

Step 2: Evaluate the exchange integral $K$.
$K = \frac{e^2}{4\pi\varepsilon l_B} \sqrt{\frac{\pi}{8}} = 8.700\ \mathrm{meV} \times \sqrt{0.392699} = 8.700\ \mathrm{meV} \times 0.626657 = 5.452\ \mathrm{meV}$.

(For reference, the direct integral is $J = \frac{e^2}{4\pi\varepsilon l_B} \sqrt{\frac{\pi}{2}} \cdot \frac{\sqrt{\pi}}{2} = 8.700\ \mathrm{meV} \times 1.2533 \times 0.8862 = 9.67\ \mathrm{meV}$, but $J$ cancels in the splitting.)

## Step 3

Step 3: Construct the two-electron states and compute the splitting.
For two electrons, the total wavefunction must be antisymmetric under exchange.
- Spin singlet (antisymmetric): spatial part symmetric $\to \Psi_S = (\psi_0\psi_1 + \psi_1\psi_0)/\sqrt{2}$. First-order energy: $E_S = E_0 + E_1 + J + K$.
- Spin triplet (symmetric): spatial part antisymmetric $\to \Psi_T = (\psi_0\psi_1 - \psi_1\psi_0)/\sqrt{2}$. First-order energy: $E_T = E_0 + E_1 + J - K$.

The singlet-triplet splitting is $\Delta E = E_T - E_S = (J - K) - (J + K) = -2K$.
$\Delta E = -2 \times 5.452\ \mathrm{meV} = -10.904\ \mathrm{meV}$.
Rounded to three significant figures: $-10.9\ \mathrm{meV}$.
The negative sign means $E_{\mathrm{triplet}} < E_{\mathrm{singlet}}$; the ground state is a spin triplet.

Final Answer: $\boxed{-10.9\ \mathrm{meV}}$

## Answer

$-10.9\ \mathrm{meV}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- Fermion antisymmetry requirement: spatial wavefunction symmetry opposite to spin state symmetry. Triplet (symmetric spin) requires antisymmetric spatial wavefunction, so exchange integral *subtracts* from direct integral. Many models incorrectly assume singlet is always lower or drop the exchange term.
- First-order perturbation theory: $\Delta E = E_T - E_S = (J - K) - (J + K) = -2K$. Sign and factor of 2 are critical.
- Magnetic length $l_B = \sqrt{\hbar/eB}$ vs. effective oscillator length $l = \sqrt{\hbar/m^*\omega}$. The problem states LLL approximation, so $l_B$ is correct. Models may incorrectly use $l$.
- The direct integral $J$ is given as a distractor; the answer depends only on $K$.