---
id: 2026-10-04-chemistry-harned-cell-activity-trap
status: ready
field: Chemistry
domain: Electrochemistry
subdomain: Nernst equation
problem_type: Exact computation
answer_type: Concentration or quantity with units
concepts:
  - Nernst equation for concentration cells
  - Mean activity coefficients in non-ideal solutions
  - Reaction quotient with activities vs concentrations
  - Silver/silver-ion electrode
  - Thermodynamic vs practical potential
routing: Automated Checks Only
independently_verified: true
working_title: harned-cell-activity-trap
---

## Problem

A silver concentration cell is constructed at 298.15 K:

$$\ce{Ag(s)|AgNO3(aq, m1 = 0.0100 mol kg^{-1}, \gamma_{\pm,1} = 0.904)||AgNO3(aq, m2 = 0.100 mol kg^{-1}, \gamma_{\pm,2} = 0.732)|Ag(s)}$$

The left compartment contains silver nitrate at molality $m_1 = 0.0100\ \mathrm{mol\ kg^{-1}}$ with mean activity coefficient $\gamma_{\pm,1} = 0.904$. The right compartment contains silver nitrate at molality $m_2 = 0.100\ \mathrm{mol\ kg^{-1}}$ with mean activity coefficient $\gamma_{\pm,2} = 0.732$. Both solutions are aqueous and the salt bridge contains saturated $\ce{KNO3}$ (junction potential negligible).

Given: $R = 8.314462618\ \mathrm{J\ mol^{-1}\ K^{-1}}$, $F = 96485.33212\ \mathrm{C\ mol^{-1}}$, $T = 298.15\ \mathrm{K}$. Compute the cell potential $E_{\mathrm{cell}}$ in volts to four decimal places.

## Domain Explanation

This problem involves a concentration cell with a silver electrode and non-ideal aqueous silver nitrate electrolyte, where the reaction quotient must be evaluated using mean activity coefficients, which are part of Electrochemistry and the Nernst equation subdomain. The problem also involves the thermodynamic definition of activity for a 1:1 electrolyte and the relation between mean activity and individual ion activity, which are part of Chemical Thermodynamics and the Activity and non-ideal solutions subdomain. However, the core of the problem is the correct application of the Nernst equation to a concentration cell with non-ideal solutions, making Electrochemistry / Nernst equation the primary classification.

## Step 1

Step 1
Write the half-reactions and the overall cell reaction. The right electrode is the cathode (higher $\ce{Ag+}$ activity) and the left is the anode. Reduction at the cathode: $\ce{Ag+(m2) + e- -> Ag(s)}$. Oxidation at the anode: $\ce{Ag(s) -> Ag+(m1) + e-}$. Overall cell reaction: $\ce{Ag+(m1) -> Ag+(m2)}$. The reaction quotient is $Q = a_{\ce{Ag+}}(m_2) / a_{\ce{Ag+}}(m_1)$. For a 1:1 electrolyte $\ce{AgNO3}$, the mean activity $a_{\pm} = \gamma_{\pm} m$ equals the individual ion activity $a_{\ce{Ag+}}$ (and $a_{\ce{NO3-}}$) because $a_{\pm} = (a_{\ce{Ag+}} a_{\ce{NO3-}})^{1/2}$ and electroneutrality gives $a_{\ce{Ag+}} = a_{\ce{NO3-}}$. Thus $a_{\ce{Ag+}}(m_i) = \gamma_{\pm,i} m_i$.

## Step 2

Step 2
Apply the Nernst equation at 298.15 K. For the one-electron overall reaction, $n = 1$.
$$E_{\mathrm{cell}} = E^{\circ}_{\mathrm{cell}} - \frac{RT}{F} \ln Q$$
Since the electrodes are identical, $E^{\circ}_{\mathrm{cell}} = 0$. Therefore
$$E_{\mathrm{cell}} = \frac{RT}{F} \ln \frac{a_{\ce{Ag+}}(m_2)}{a_{\ce{Ag+}}(m_1)} = \frac{RT}{F} \ln \frac{\gamma_{\pm,2} m_2}{\gamma_{\pm,1} m_1}$$
Substitute the given values:
$$\frac{\gamma_{\pm,2} m_2}{\gamma_{\pm,1} m_1} = \frac{0.732 \times 0.100}{0.904 \times 0.0100} = \frac{0.0732}{0.00904} = 8.097345\ldots$$

## Step 3

Step 3
Compute $RT/F$ at 298.15 K:
$$\frac{RT}{F} = \frac{8.314462618 \times 298.15}{96485.33212} = 0.02569257\ \mathrm{V}$$
Then
$$E_{\mathrm{cell}} = 0.02569257 \times \ln(8.097345) = 0.02569257 \times 2.091536 = 0.053737\ \mathrm{V}$$
Rounded to four decimal places: $0.0537\ \mathrm{V}$. (If concentrations were used instead of activities, the ratio would be $0.100/0.0100 = 10$, giving $0.02569257 \times \ln(10) = 0.05916\ \mathrm{V}$, which is incorrect.)

Final Answer: $\boxed{0.0537\ \mathrm{V}}$

## Answer

$0.0537\ \mathrm{V}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [ ] Hid the boxed line and recomputed every displayed equality
- [ ] `python3 scripts/qa_gate.py` PASS
- [ ] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- Activity coefficients given but dropped from Q; model uses concentrations (0.100/0.0100 = 10) instead of activities (0.0732/0.00904 = 8.097), yielding 0.0592 V instead of 0.0537 V