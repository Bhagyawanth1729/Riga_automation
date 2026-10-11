# Scratch — acetic activity and exact charge balance

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

$[\mathrm{H}^+]=1.37\times10^{-4}\,\mathrm{M}$ (three significant figures)

## Solve

Thermodynamic $K_a^\circ$:
$$K_a^\circ=\frac{a_{\mathrm{H}^+}a_{\mathrm{Ac}^-}}{a_{\mathrm{HAc}}}=\frac{(\gamma_{\mathrm{H}^+}[\mathrm{H}^+])(\gamma_{\mathrm{Ac}^-}[\mathrm{Ac}^-])}{\gamma_{\mathrm{HAc}}[\mathrm{HAc}]}$$
with standard state $1\,\mathrm{M}$.

Neglect water: $[\mathrm{H}^+]=[\mathrm{Ac}^-]=x$, $[\mathrm{HAc}]=C-x$, $C=1.00\times10^{-3}\,\mathrm{M}$.
$$\frac{(0.90)(0.90)\,x^2}{(1.00)(C-x)}=1.75\times10^{-5}$$
$$0.81\,x^2=1.75\times10^{-5}(C-x)$$
$$x^2+(2.160493827\times10^{-5})x-2.160493827\times10^{-8}=0$$
$$x=\frac{-b+\sqrt{b^2+4\cdot2.160493827\times10^{-8}}}{2}=1.365801\times10^{-4}$$
Three sig figs: $1.37\times10^{-4}\,\mathrm{M}$.

Wrong paths (for stump design):
- drop $\gamma$, exact quadratic: $1.24\times10^{-4}$
- keep $\gamma$, illegal small-$x$: $1.47\times10^{-4}$
- drop $\gamma$, small-$x$: $1.32\times10^{-4}$

$x/C\approx0.137$, so $C-x\approx C$ is not legal to three figures.

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked
- [x] Next-best domain considered and rejected in the justification
- [x] Prompt does not leak the method
- [x] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

Activity coefficients are stated, then commonly dropped from $Q$; independently, $x/C\sim0.14$ makes the small-$x$ root illegal at three significant figures. Either miss alone changes the third digit.
