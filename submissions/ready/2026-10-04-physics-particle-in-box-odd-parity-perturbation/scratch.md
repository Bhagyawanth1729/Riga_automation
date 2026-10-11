# Scratch — particle-in-box-odd-parity-perturbation

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

- Ground state second-order energy shift: $E_1^{(2)} = -28.8\,\mathrm{meV}$ (rounded to 3 sig figs)

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked
- [x] Next-best domain considered and rejected in the justification
- [x] Prompt does not leak the method
- [x] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

- First-order perturbation vanishes exactly by parity; a model may incorrectly compute a non-zero first-order shift or stop at zero.
- The energy denominator $E_1 - E_m$ is negative for all $m>1$; a sign error flips the sign of the answer.
- The matrix element formula has $(m^2-1)^2$ in the denominator; using $(m^2-1)$ or $(m^2-1)^3$ changes the sum significantly.
- The factor of 2 in the second-order formula (some texts write $\frac{1}{2}$ in front of the sum for time-dependent perturbation theory, but the time-independent formula has no 1/2) is a common confusion.
- The sum is dominated by $m=2$; truncating after $m=2$ gives $-28.7\,\mathrm{meV}$, which rounds to the same three significant figures, but a model that includes $m=4,6$ correctly will get the same rounded result.