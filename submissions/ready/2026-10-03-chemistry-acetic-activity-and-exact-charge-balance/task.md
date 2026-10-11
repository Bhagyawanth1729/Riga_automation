---
id: 2026-10-03-chemistry-acetic-activity-and-exact-charge-balance
status: ready
field: Chemistry
domain: Acids, Bases, and Aqueous Equilibria
subdomain: Weak acid and weak base equilibria
problem_type: Numerical approximation
answer_type: Concentration or quantity with units
concepts:
  - Thermodynamic acidity constant
  - Single-ion activity coefficients
  - Weak-acid mass balance
  - Exact quadratic root
routing: Automated Checks Only
independently_verified: true
working_title: acetic activity and exact charge balance
---

## Problem

Aqueous acetic acid of analytical concentration $C=1.00\times10^{-3}\,\mathrm{M}$ is prepared with no added strong electrolyte. For
$$\ce{CH3COOH(aq)} \rightleftharpoons \ce{H+(aq) + CH3COO-(aq)}$$
at $25.0\,\mathrm{^\circ C}$ the thermodynamic acidity constant is $K_a^\circ=1.75\times10^{-5}$, referred to the $1\,\mathrm{M}$ standard state for each aqueous solute. At the ionic strength of the equilibrated solution the single-ion activity coefficients may be taken as $\gamma_{\mathrm{H}^+}=\gamma_{\mathrm{Ac}^-}=0.90$ and $\gamma_{\mathrm{HAc}}=1.00$, and held fixed at those values. Autodissociation of water may be neglected. Report the equilibrium free hydrogen-ion concentration $[\mathrm{H}^+]$ in $\mathrm{M}$, rounded to three significant figures.

## Domain Explanation

This problem involves the weak-acid equilibrium of acetic acid together with the charge and mass balances that fix $[\mathrm{H}^+]$, which are part of Acids, Bases, and Aqueous Equilibria and Weak acid and weak base equilibria.
The problem also involves converting between concentrations and activities with given single-ion activity coefficients, which are part of Solutions and Mixtures and Activity and non-ideal solutions.
However, the activity coefficients are supplied data for the acid equilibrium; the object computed is the aqueous free $[\mathrm{H}^+]$ of a weak acid, so the acid–base pair is the core.

## Step 1

Step 1
Write the thermodynamic acidity constant with the $1\,\mathrm{M}$ standard state,
$$K_a^\circ=\frac{a_{\mathrm{H}^+}a_{\mathrm{Ac}^-}}{a_{\mathrm{HAc}}}=\frac{(\gamma_{\mathrm{H}^+}[\mathrm{H}^+])(\gamma_{\mathrm{Ac}^-}[\mathrm{Ac}^-])}{\gamma_{\mathrm{HAc}}[\mathrm{HAc}]},$$
where each activity is $a_i=\gamma_i([i]/c^\circ)$ and $c^\circ=1\,\mathrm{M}$ cancels for every solute. Neglecting autodissociation of water, electroneutrality forces $[\mathrm{H}^+]=[\mathrm{Ac}^-]$. Let $x=[\mathrm{H}^+]$. Mass balance on acetate then gives $[\mathrm{HAc}]=C-x$.

## Step 2

Step 2
Substitute the given activity coefficients and the balances from Step 1 into $K_a^\circ$:
$$\frac{(0.90)(0.90)\,x^2}{(1.00)(C-x)}=1.75\times10^{-5}.$$
With $C=1.00\times10^{-3}\,\mathrm{M}$,
$$0.81\,x^2=1.75\times10^{-5}\,(1.00\times10^{-3}-x),$$
so
$$x^2+(2.160493827\times10^{-5})\,x-2.160493827\times10^{-8}=0.$$
The ratio $x/C$ is not small enough for the replacement $C-x\approx C$ to be consistent with three significant figures, so the quadratic must be retained.

## Step 3

Step 3
The physical root of the quadratic in Step 2 is
$$x=\frac{-2.160493827\times10^{-5}+\sqrt{(2.160493827\times10^{-5})^2+8.641975309\times10^{-8}}}{2}=1.365801\times10^{-4}.$$
Rounded to three significant figures, $[\mathrm{H}^+]=1.37\times10^{-4}\,\mathrm{M}$.

Final Answer: $\boxed{1.37\times10^{-4}\,\mathrm{M}}$

## Answer

$1.37\times10^{-4}\,\mathrm{M}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- Activity coefficients appear in the data but are easy to drop from $Q$, giving $\approx1.24\times10^{-4}\,\mathrm{M}$.
- Independently, $x/C\sim0.14$ makes the small-$x$ root illegal; with activities kept that path gives $\approx1.47\times10^{-4}\,\mathrm{M}$.
