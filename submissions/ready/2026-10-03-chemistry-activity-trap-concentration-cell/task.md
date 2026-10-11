---
id: 2026-10-03-chemistry-activity-trap-concentration-cell
status: ready
field: Chemistry
domain: Electrochemistry
subdomain: Nernst equation
problem_type: Exact computation
answer_type: Numerical scalar approximation
concepts:
  - Concentration cell
  - Nernst equation
  - Activity coefficients
  - Ionic strength effects
routing: Automated Checks Only
independently_verified: true
working_title: activity-trap-concentration-cell
---

## Problem

A silver-silver ion concentration cell is constructed at 298.15 K:

$$\ce{Ag(s)|AgNO3(aq, 0.0100 M) + KNO3(aq, 0.0900 M)||AgNO3(aq, 0.100 M) + KNO3(aq, 0.900 M)|Ag(s)}$$

The mean ionic activity coefficients of $\ce{Ag+}$ at 298.15 K in the two compartments are experimentally determined as:

- Compartment 1 (left): $\gamma_{\pm,1} = 0.78$
- Compartment 2 (right): $\gamma_{\pm,2} = 0.65$

Assume the junction potential is negligible. Compute the cell potential $E_{\text{cell}}$ in volts, and report the answer as a decimal rounded to four significant figures.

Use $R = 8.31446\ \mathrm{J\ mol^{-1}\ K^{-1}}$, $F = 96485.3\ \mathrm{C\ mol^{-1}}$, and $RT/F = 0.025693\ \mathrm{V}$ at 298.15 K.

## Domain Explanation

This problem involves a concentration cell with non-ideal solutions where activity coefficients differ between compartments, which is a core application of the Nernst equation in Electrochemistry.
The problem also involves calculation of ionic strength and its effect on activity coefficients, which falls under Solutions and Mixtures / Activity and non-ideal solutions.
However, the ionic strengths and activity coefficients are given directly as experimental data; the problem does not require deriving them from Debye-Hueckel theory or other models, so the non-ideal solutions subdomain is secondary.

## Step 1

Step 1
Write the Nernst equation for the silver-silver ion concentration cell. The overall cell reaction is the transfer of $\ce{Ag+}$ from the right compartment (higher concentration) to the left compartment (lower concentration): $\ce{Ag+(aq, right) -> Ag+(aq, left)}$. The reaction quotient $Q$ is expressed in terms of activities: $Q = a_{\ce{Ag+},\text{left}} / a_{\ce{Ag+},\text{right}}$. For a concentration cell with identical electrodes, $E^\circ_{\text{cell}} = 0$, so the Nernst equation reduces to $E_{\text{cell}} = -\frac{RT}{F} \ln Q = \frac{RT}{F} \ln \frac{a_{\ce{Ag+},\text{right}}}{a_{\ce{Ag+},\text{left}}}$. The activity of $\ce{Ag+}$ in each compartment is $a_{\ce{Ag+}} = \gamma_{\pm} [\ce{Ag+}]$, where $\gamma_{\pm}$ is the mean ionic activity coefficient and $[\ce{Ag+}]$ is the molar concentration. The number of electrons transferred is $n = 1$.

## Step 2

Step 2
Substitute the given concentrations and activity coefficients. Compartment 1 (left): $[\ce{Ag+}]_1 = 0.0100\ \mathrm{M}$, $\gamma_{\pm,1} = 0.78$, so $a_1 = 0.78 \times 0.0100 = 0.00780$. Compartment 2 (right): $[\ce{Ag+}]_2 = 0.100\ \mathrm{M}$, $\gamma_{\pm,2} = 0.65$, so $a_2 = 0.65 \times 0.100 = 0.0650$. The activity ratio is $a_2/a_1 = 0.0650 / 0.00780 = 8.3333...$. Using $RT/F = 0.025693\ \mathrm{V}$ at 298.15 K, compute $E_{\text{cell}} = 0.025693 \times \ln(8.3333...) = 0.025693 \times 2.12026 = 0.054476\ \mathrm{V}$.

## Step 3

Step 3
Round the result to four significant figures as requested. $0.054476\ \mathrm{V}$ rounds to $0.05448\ \mathrm{V}$.

Final Answer: $\boxed{0.05448\ \mathrm{V}}$

## Answer

$0.05448\ \mathrm{V}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- The model will likely use concentrations directly in the Nernst equation ($E = \frac{RT}{F} \ln \frac{[\ce{Ag+}]_2}{[\ce{Ag+}]_1} = 0.025693 \ln(10) = 0.05916\ \mathrm{V}$) and drop the activity coefficients given in the problem. This is the "activity/fugacity present in the data but dropped from Q" stump pattern.