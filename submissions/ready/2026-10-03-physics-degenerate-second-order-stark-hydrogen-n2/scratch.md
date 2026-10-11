# Scratch — degenerate-second-order-stark-hydrogen-n2

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

- Four energy shifts in meV: -0.159, 1.76e-7, 1.76e-7, 0.159

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked
- [x] Next-best domain considered and rejected in the justification
- [x] Prompt does not leak the method
- [x] Skeleton is not the previous draft or the gold Harned cell

## Why a frontier model should miss this

- The model may apply non-degenerate perturbation theory directly to the unperturbed states, missing that $|2s\rangle$ and $|2p_0\rangle$ are coupled at first order and must be diagonalized first.
- The model may think the first-order Stark effect vanishes entirely for $n=2$ (true for ground state, false for $n=2$).
- The model may use the polarizabilities of the unperturbed states without weighting by the composition of the first-order eigenstates.
- The model may forget that $|2p_{\pm1}\rangle$ have zero first-order shift and their total shift is purely second-order.
- The model may confuse the polarizability formula sign or units.
- The scale separation is extreme: first-order shifts ~0.16 meV, second-order shifts ~10⁻⁶ meV. A model that drops second-order entirely gets the wrong ordering (the two $|2p_{\pm1}\rangle$ states would appear degenerate at 0 meV, but they're actually slightly positive). The problem explicitly asks for second order.
- The polarizabilities given differ in the constant term (31/36, 101/36, 13/36), a subtle trap; the exact formulas and decimal approximations are now mutually consistent.
- The mixing rule for the second-order shifts of the hybrid states is explicitly stated, removing the ambiguity flagged in the previous version.