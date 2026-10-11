# Scratch — Tight-binding Michaelis-Menten initial rate

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

Initial rate of product formation under the quasi-steady-state approximation for a
three-step Michaelis-Menten mechanism, with the bounds on enzyme and substrate mass
kept exactly.

- Given: $k_1=2.0\times10^7\ \mathrm{M^{-1}s^{-1}}$, $k_{-1}=7.0\ \mathrm{s^{-1}}$, $k_2=3.0\ \mathrm{s^{-1}}$, $[E]_{\mathrm{tot}}=9.0\ \mu M$, $[S]_{\mathrm{tot}}=10.0\ \mu M$.
- $K_M=(k_{-1}+k_2)/k_1=10/2.0\times10^7=5.0\times10^{-7}\ \mathrm{M}=0.50\ \mu M$.
- QSSA: $([E]_{\mathrm{tot}}-x)([S]_{\mathrm{tot}}-x)=K_M x$; in $\mu M$, $(9.0-x)(10.0-x)=0.50x$.
- $x^2-19.5x+90=0$; $x=(19.5\pm4.5)/2=12.0$ or $7.5\ \mu M$. Physical root $x=7.5\ \mu M$.
- $v_0=k_2x=3.0\times7.5=22.5\ \mu M\,s^{-1}$.

Naive excess-substrate closed form: $3.0\times9.0\times10.0/(0.50+10.0)=25.7\ \mu M\,s^{-1}$.
Rapid-equilibrium variant uses $K_S=k_{-1}/k_1=0.35\ \mu M$, also wrong.

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked: $\mu M\,s^{-1}$, three significant figures, terminating decimal
- [x] Next-best domain considered and rejected in the justification (Chemical Kinetics)
- [x] Prompt does not leak the method (gives the mechanism and QSSA only)
- [x] Skeleton is not the previous draft or the gold Harned cell (no cell diagram, no Nernst)

Arithmetic re-run independently with Python:
$K_M=5.0\times10^{-7}\ \mathrm{M}$; discriminant $=19.5^2-4(90)=20.25$; roots $7.5$ and $12.0$;
$v_0=22.5\ \mu M\,s^{-1}$; naive form $=25.714\ldots\ \mu M\,s^{-1}$.

## Why a frontier model should miss this

- The standard Michaelis-Menten equation $v_0=k_2[E]_{\mathrm{tot}}[S]_{\mathrm{tot}}/(K_M+[S]_{\mathrm{tot}})$
  assumes the enzyme-bound substrate is negligible against total substrate. That assumption is
  illegal here because $[E]_{\mathrm{tot}}\sim[S]_{\mathrm{tot}}\sim K_M$; the model must solve the
  joint enzyme/substrate mass balance (a quadratic). Blind use of the closed form gives 25.7, not 22.5.
- Secondary failure: mixing the rapid-equilibrium constant $K_S=k_{-1}/k_1$ with the steady-state
  constant $K_M=(k_{-1}+k_2)/k_1$.
