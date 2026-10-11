# Scratch — two-electron-quantum-dot-singlet-triplet

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

- ΔE = E_triplet - E_singlet = -2K
- K = (e²/4πεl_B) √(π/8)
- l_B = √(ℏ/eB)
- Given: ℏω₀ = 3.0 meV, B = 4.0 T, m* = 0.067 m_e, ε = 12.9 ε₀
- Constants: e²/(4πε₀) = 1.44 eV·nm, ℏ = 6.582×10⁻¹⁶ eV·s, m_e = 9.109×10⁻³¹ kg, e = 1.602×10⁻¹⁹ C
- Compute: l_B, then K, then ΔE

## Independent check

- [ ] Recomputed every displayed equality with the boxed line hidden
- [ ] Units / sig figs / equivalent forms locked
- [ ] Next-best domain considered and rejected in the justification
- [ ] Prompt does not leak the method
- [ ] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

- Fermion antisymmetry requirement: spatial wavefunction symmetry opposite to spin state symmetry. Triplet (symmetric spin) requires antisymmetric spatial wavefunction, so exchange integral *subtracts* from direct integral. Many models incorrectly assume singlet is always lower or drop the exchange term.
- First-order perturbation theory: ΔE = E_T - E_S = (J - K) - (J + K) = -2K. Sign and factor of 2 are critical.
- Magnetic length l_B = √(ℏ/eB) vs. effective oscillator length l = √(ℏ/m*ω). The problem states LLL approximation, so l_B is correct. Models may incorrectly use l.
- The direct integral J is given as a distractor; the answer depends only on K.

## Step-by-step solution

**Step 1: Magnetic length and Coulomb energy scale**
l_B = √(ℏ/eB) = √(1.055×10⁻³⁴ J·s / (1.602×10⁻¹⁹ C × 4.0 kg/(C·s))) = 1.283×10⁻⁸ m = 12.83 nm
e²/(4πε) = (e²/(4πε₀))/ε_r = 1.44 eV·nm / 12.9 = 0.1116 eV·nm = 1.116×10⁻¹⁰ eV·m
e²/(4πεl_B) = 1.116×10⁻¹⁰ eV·m / 1.283×10⁻⁸ m = 8.700×10⁻³ eV = 8.700 meV

**Step 2: Exchange integral K**
K = (e²/4πεl_B) √(π/8) = 8.700 meV × √(0.392699) = 8.700 × 0.626657 = 5.452 meV

**Step 3: Singlet-triplet splitting**
For two electrons in orbitals m=0 and m=1:
- Singlet (antisymmetric spin): spatial symmetric → E_S = E₀ + E₁ + J + K
- Triplet (symmetric spin): spatial antisymmetric → E_T = E₀ + E₁ + J - K
ΔE = E_T - E_S = -2K = -2 × 5.452 meV = -10.904 meV
Rounded to three significant figures: -10.9 meV
Negative ΔE means triplet is lower in energy (ground state).

## Final Answer
ΔE = -10.9 meV (triplet ground state)