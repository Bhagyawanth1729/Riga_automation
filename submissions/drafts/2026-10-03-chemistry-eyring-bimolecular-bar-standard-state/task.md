---
id: 2026-10-03-chemistry-eyring-bimolecular-bar-standard-state
status: draft
field: Chemistry
domain: Chemical Kinetics
subdomain: Reaction rates
problem_type: Numerical approximation
answer_type: Concentration or quantity with units
concepts:
  - Transition-state theory
  - Termolecular gas-phase rate constant
  - Pressure standard state
  - Eyring prefactor
routing: Automated Checks Only
independently_verified: false
working_title: eyring bimolecular bar standard state
---

## Problem

The elementary gas-phase reaction $\mathrm{A(g)+B(g)+C(g)\to products}$ is studied at $T=500\,\mathrm{K}$. Transition-state theory with unit transmission coefficient is to be used. The standard molar Gibbs energy of activation is $\Delta^\ddagger G^\circ=85.0\,\mathrm{kJ\,mol^{-1}}$, referred to the ideal-gas standard state $p^\circ=1\,\mathrm{bar}=10^5\,\mathrm{Pa}$ for $\mathrm{A}$, $\mathrm{B}$, $\mathrm{C}$, and the activated complex. Take $k_B=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$, $h=6.62607015\times10^{-34}\,\mathrm{J\,s}$, and $R=8.314\,\mathrm{J\,mol^{-1}\,K^{-1}}$. The phenomenological rate law is written in molar concentrations, $\mathrm{d}[\mathrm{P}]/\mathrm{d}t=k_3[\mathrm{A}][\mathrm{B}][\mathrm{C}]$. Report $k_3$ in $\mathrm{m^6\,mol^{-2}\,s^{-1}}$, rounded to three significant figures.

## Domain Explanation

This problem involves the elementary termolecular rate constant from transition-state theory and the connection between that constant and a stated Gibbs energy of activation, which are part of Chemical Kinetics and Reaction rates.
The problem also involves the ideal-gas pressure standard state that defines $\Delta^\ddagger G^\circ$ and the conversion into a concentration-based rate coefficient, which are part of Chemical Thermodynamics and Gibbs free energy.
However, the thermodynamic standard state is auxiliary data for the kinetic object $k_3$; the quantity asked for is a rate constant under a stated rate law.

## Step 1

Step 1
For an elementary termolecular gas reaction the Eyring quotient compares one activated complex to three reactant molecules. With unit transmission coefficient and the ideal-gas standard pressure $p^\circ$, the concentration-based third-order coefficient is
$$k_3=\frac{k_B T}{h}\,e^{-\Delta^\ddagger G^\circ/RT}\left(\frac{RT}{p^\circ}\right)^2.$$
Each factor of $RT/p^\circ$ is a molar volume forced by writing $\Delta^\ddagger G^\circ$ at $1\,\mathrm{bar}$ while $k_3$ multiplies three concentrations. Using no volume factor, a single factor (the bimolecular habit), or $1/c^\circ$ with $c^\circ=1\,\mathrm{mol\,dm^{-3}}$ all change the numerical answer.

## Step 2

Step 2
Substitute the given constants at $T=500\,\mathrm{K}$:
$$\frac{k_B T}{h}=\frac{(1.380649\times10^{-23})(500)}{6.62607015\times10^{-34}}=1.041831\times10^{13}\,\mathrm{s^{-1}}.$$
With $\Delta^\ddagger G^\circ=8.50\times10^4\,\mathrm{J\,mol^{-1}}$,
$$\frac{\Delta^\ddagger G^\circ}{RT}=\frac{8.50\times10^4}{(8.314)(500)}=20.4474,\qquad e^{-\Delta^\ddagger G^\circ/RT}=1.31762\times10^{-9},$$
so
$$\frac{k_B T}{h}\,e^{-\Delta^\ddagger G^\circ/RT}=1.37274\times10^4\,\mathrm{s^{-1}}.$$
One standard-state volume factor is
$$\frac{RT}{p^\circ}=\frac{(8.314)(500)}{10^5}=4.157\times10^{-2}\,\mathrm{m^3\,mol^{-1}},$$
and the termolecular conversion therefore uses
$$\left(\frac{RT}{p^\circ}\right)^2=(4.157\times10^{-2})^2=1.72806\times10^{-3}\,\mathrm{m^6\,mol^{-2}}.$$

## Step 3

Step 3
Multiply the pieces from Step 2:
$$k_3=(1.37274\times10^4\,\mathrm{s^{-1}})(1.72806\times10^{-3}\,\mathrm{m^6\,mol^{-2}})=23.722\,\mathrm{m^6\,mol^{-2}\,s^{-1}}.$$
Rounded to three significant figures, $k_3=23.7\,\mathrm{m^6\,mol^{-2}\,s^{-1}}$.

Final Answer: $\boxed{23.7\,\mathrm{m^6\,mol^{-2}\,s^{-1}}}$

## Answer

$23.7\,\mathrm{m^6\,mol^{-2}\,s^{-1}}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [ ] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- Reflex Eyring is $k=k_B T/h\,e^{-\Delta G^\ddagger/RT}$, ignoring molecularity and standard state, which yields $\sim1.37\times10^4\,\mathrm{s^{-1}}$.
- The bimolecular habit inserts a single $RT/p^\circ$ and returns $\sim571\,\mathrm{m^3\,mol^{-1}\,s^{-1}}$ (wrong order and units).
- Replacing $(RT/p^\circ)^2$ by $(1/c^\circ)^2$ with $c^\circ=1\,\mathrm{M}=10^3\,\mathrm{mol\,m^{-3}}$ gives $\sim1.37\times10^{-2}\,\mathrm{m^6\,mol^{-2}\,s^{-1}}$, appropriate only if $\Delta^\ddagger G^\circ$ had been referred to $1\,\mathrm{M}$.
