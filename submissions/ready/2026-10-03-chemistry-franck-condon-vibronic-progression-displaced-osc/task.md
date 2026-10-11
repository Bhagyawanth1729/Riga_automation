---
id: 2026-10-03-chemistry-franck-condon-vibronic-progression-displaced-osc
status: ready
field: Chemistry
domain: Physical Chemistry and Spectroscopy
subdomain: Electronic spectroscopy
problem_type: Exact computation
answer_type: Exact scalar
concepts:
  - Franck-Condon principle
  - Huang-Rhys parameter
  - Vibronic progression
  - Displaced harmonic oscillator
  - Poisson distribution
routing: Automated Checks Only
independently_verified: true
working_title: franck-condon-vibronic-progression-displaced-oscillators
---

## Problem

A diatomic molecule exhibits an electronic absorption band system. The ground and excited electronic states are both well described by harmonic oscillators with the **same** vibrational frequency $\tilde{\nu} = 1500\ \mathrm{cm^{-1}}$. The equilibrium bond length increases by $\Delta r_e = 0.120\ \mathrm{\AA}$ upon excitation. The purely electronic (0-0) transition lies at $\tilde{\nu}_{00} = 22500\ \mathrm{cm^{-1}}$. The transition dipole moment is independent of nuclear coordinates (Condon approximation). The reduced mass of the molecule is $\mu = 10.0\ \mathrm{u}$.

Under these conditions the relative intensities of the vibronic peaks $v''=0 \to v'$ follow a Poisson distribution governed by the Huang–Rhys parameter
$$S = \frac{\mu \omega}{2\hbar} (\Delta r_e)^2,$$
where $\omega = 2\pi c\tilde{\nu}$ is the angular vibrational frequency. The Franck–Condon factor for the $0\to v'$ transition is $\mathrm{FCF}(v') = e^{-S} S^{v'}/v'!$. The wavenumber of the $v'$ peak is $\tilde{\nu}_{v'} = \tilde{\nu}_{00} + v'\tilde{\nu}$.

Constants:
- $1\ \mathrm{u} = 1.66053906660\times 10^{-27}\ \mathrm{kg}$
- $c = 2.99792458\times 10^{10}\ \mathrm{cm\ s^{-1}}$
- $\hbar = 1.054571817\times 10^{-34}\ \mathrm{J\ s}$
- $1\ \mathrm{\AA} = 10^{-10}\ \mathrm{m}$

**Question:** Compute the wavenumber (in $\mathrm{cm^{-1}}$) of the most intense vibronic peak in the absorption spectrum. Round your answer to the nearest integer.

Answer format: a single integer in $\mathrm{cm^{-1}}$ (e.g., 27000).

## Domain Explanation

This problem involves the Franck–Condon principle and the Poisson-distributed vibronic progression of a displaced harmonic oscillator, which are core topics in Physical Chemistry and Spectroscopy / Electronic spectroscopy. The problem also involves the quantum harmonic oscillator and dimensionless displacement parameters, which belong to Quantum Mechanics / Wavefunctions and probability. However, the asked object is the position of the absorption maximum in a molecular electronic spectrum; the oscillator physics is only the means to compute the Huang–Rhys parameter, not the primary subject.

## Step 1

Step 1: Compute the Huang–Rhys parameter $S$.
The angular frequency is $\omega = 2\pi c\tilde{\nu} = 2\pi (2.99792458\times 10^{10}\ \mathrm{cm\ s^{-1}})(1500\ \mathrm{cm^{-1}}) = 2.8254\times 10^{14}\ \mathrm{rad\ s^{-1}}$.
The reduced mass is $\mu = 10.0\ \mathrm{u} = 10.0 \times 1.66053906660\times 10^{-27}\ \mathrm{kg} = 1.66054\times 10^{-26}\ \mathrm{kg}$.
The displacement is $\Delta r_e = 0.120\ \mathrm{\AA} = 1.20\times 10^{-11}\ \mathrm{m}$.
Substitute into $S = \frac{\mu \omega}{2\hbar} (\Delta r_e)^2$:
$$
S = \frac{(1.66054\times 10^{-26}\ \mathrm{kg})(2.8254\times 10^{14}\ \mathrm{rad\ s^{-1}})}{2(1.054571817\times 10^{-34}\ \mathrm{J\ s})} (1.20\times 10^{-11}\ \mathrm{m})^2.
$$
Compute the prefactor: $\frac{\mu\omega}{2\hbar} = \frac{4.6917\times 10^{-12}}{2.1091\times 10^{-34}} = 2.2245\times 10^{22}\ \mathrm{m^{-2}}$.
Then $S = (2.2245\times 10^{22})(1.44\times 10^{-22}) = 3.2033$.

## Step 2

Step 2: Determine the vibrational quantum number $v'_{\mathrm{max}}$ of the most intense peak.
For a Poisson distribution $P(v') = e^{-S} S^{v'}/v'!$, the maximum occurs at $v'_{\mathrm{max}} = \lfloor S \rfloor$ (the greatest integer less than or equal to $S$).
Since $S = 3.2033$, we have $v'_{\mathrm{max}} = 3$.
(Check: $\mathrm{FCF}(2) \propto S^2/2! = 5.13$, $\mathrm{FCF}(3) \propto S^3/3! = 5.48$, $\mathrm{FCF}(4) \propto S^4/4! = 4.38$; $v'=3$ is indeed the maximum.)

## Step 3

Step 3: Compute the wavenumber of the $v'=3$ peak.
The peak positions are $\tilde{\nu}_{v'} = \tilde{\nu}_{00} + v'\tilde{\nu}$.
For $v'=3$:
$$
\tilde{\nu}_{\mathrm{max}} = 22500\ \mathrm{cm^{-1}} + 3 \times 1500\ \mathrm{cm^{-1}} = 22500 + 4500 = 27000\ \mathrm{cm^{-1}}.
$$
Rounded to the nearest integer, the answer is $27000\ \mathrm{cm^{-1}}$.

Final Answer: $\boxed{27000}$

## Answer

$27000$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [ ] Hid the boxed line and recomputed every displayed equality
- [ ] `python3 scripts/qa_gate.py` PASS
- [ ] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- Forgetting the $2\pi$ in $\omega = 2\pi c\tilde{\nu}$ (using $\omega = c\tilde{\nu}$) gives $S \approx 0.51$, $v'_{\mathrm{max}}=0$, answer $22500$.
- Forgetting the factor $1/2$ in $S = \frac{\mu\omega}{2\hbar}(\Delta r_e)^2$ gives $S \approx 6.41$, $v'_{\mathrm{max}}=6$, answer $31500$.
- Using $h$ instead of $\hbar$ gives the same error as missing $2\pi$ (since $h = 2\pi\hbar$), answer $22500$.
- Assuming the $0$-$0$ transition is always the strongest (a common qualitative misconception) gives $22500$.
- Unit errors on $\Delta r_e$ (using $\mathrm{\AA}$ or $\mathrm{cm}$ instead of $\mathrm{m}$) produce wildly incorrect $S$.
- The problem requires careful unit handling (kg, m, J, s, rad) and the correct angular frequency, not just the spectroscopic wavenumber.