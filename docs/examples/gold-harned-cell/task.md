---
id: gold-harned-cell
status: ready
field: Chemistry
domain: Electrochemistry
subdomain: Nernst equation
problem_type: Numerical approximation
answer_type: Concentration or quantity with units
concepts:
  - Harned cell
  - Mean ionic activity
  - Nernst equation
  - Hydrogen fugacity
routing: Quality Review
independently_verified: true
working_title: Harned cell potential at 298.15 K
---

## Problem

The cell $\mathrm{Pt}(s)\mid \mathrm{H}_2(g,\,0.500\,\mathrm{bar})\mid \mathrm{HCl}(aq,\,m=0.0100\,\mathrm{mol\,kg^{-1}})\mid \mathrm{AgCl}(s)\mid \mathrm{Ag}(s)$ is held at $298.15\,\mathrm{K}$. At this molality the mean ionic activity coefficient of $\mathrm{HCl}$ is $\gamma_\pm=0.904$. Take $E^\circ(\mathrm{AgCl}/\mathrm{Ag},\mathrm{Cl}^-)=0.2223\,\mathrm{V}$, $p^\circ=1\,\mathrm{bar}$, $R=8.314462618\,\mathrm{J\,K^{-1}\,mol^{-1}}$, and $F=96485.3321\,\mathrm{C\,mol^{-1}}$. Treat $\mathrm{H}_2$ as ideal and the condensed phases as having unit activity. Report the cell potential in volts, rounded to three decimal places.

## Domain Explanation

This problem involves writing the cell reaction and evaluating the Nernst equation with a measured mean ionic activity coefficient and a nonstandard hydrogen pressure, which are part of Electrochemistry and Nernst equation.
The problem also involves the relation $\Delta G=-nFE$ and the definition of chemical activities, which are part of Chemical Thermodynamics and Gibbs free energy.
However, the asked object is the cell potential itself; the thermodynamic identity is only the background for the Nernst form and is not the calculation being performed.

## Step 1

Step 1
The spontaneous cell reaction consistent with the written cell (left-hand electrode oxidation) is
$$\tfrac{1}{2}\mathrm{H}_2(g)+\mathrm{AgCl}(s)\to \mathrm{Ag}(s)+\mathrm{H}^+(aq)+\mathrm{Cl}^-(aq).$$
One electron is transferred, so $n=1$. With unit activity for $\mathrm{Ag}$ and $\mathrm{AgCl}$,
$$E=E^\circ-\frac{RT}{F}\ln\left(\frac{a_{\mathrm{H}^+}\,a_{\mathrm{Cl}^-}}{(f_{\mathrm{H}_2}/p^\circ)^{1/2}}\right).$$
Ideal hydrogen at the stated pressure gives $f_{\mathrm{H}_2}/p^\circ=0.500$. For $1{:}1$ $\mathrm{HCl}$, $a_{\mathrm{H}^+}a_{\mathrm{Cl}^-}=(\gamma_\pm m/m^\circ)^2$ with $m^\circ=1\,\mathrm{mol\,kg^{-1}}$.

## Step 2

Step 2
Substitute the given molality and activity coefficient:
$$\gamma_\pm m/m^\circ=0.904\times 0.0100=9.04\times 10^{-3},$$
$$a_{\mathrm{H}^+}a_{\mathrm{Cl}^-}=(9.04\times 10^{-3})^2=8.17216\times 10^{-5}.$$
The reaction quotient is then
$$Q=\frac{8.17216\times 10^{-5}}{\sqrt{0.500}}=1.15586\times 10^{-4}.$$
At $298.15\,\mathrm{K}$,
$$\frac{RT}{F}=\frac{(8.314462618)(298.15)}{96485.3321}=0.0256926\,\mathrm{V},$$
and $\ln Q=\ln(1.15586\times 10^{-4})=-9.06547$.

## Step 3

Step 3
The logarithmic term is
$$-\frac{RT}{F}\ln Q=(0.0256926)(9.06547)=0.23291\,\mathrm{V}.$$
Adding the given standard potential,
$$E=0.2223+0.23291=0.45521\,\mathrm{V},$$
which rounds to three decimal places as $0.455\,\mathrm{V}$. The same arithmetic with $2.303RT/F$ and $\log_{10}Q$ reproduces this value to the requested rounding.

Final Answer: $\boxed{0.455\,\mathrm{V}}$

## Answer

$0.455\,\mathrm{V}$

## Author Notes

Independent check recomputed $RT/F$, $Q$, $\ln Q$, and the sum.
Frontier models often (i) drop $\gamma_\pm$, (ii) put $p_{\mathrm{H}_2}$ in the numerator, (iii) use $n=2$, or (iv) treat $0.0100\,\mathrm{m}$ as molarity in $c/c^\circ$ without activity.
