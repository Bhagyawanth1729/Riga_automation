---
id: 2026-10-03-physics-singlet-triplet-contact-degeneracy-g
status: ready
field: Physics
domain: Quantum Mechanics
subdomain: Identical particles
problem_type: Exact computation
answer_type: Exact symbolic expression
concepts:
  - Identical fermions
  - Exchange symmetry
  - Contact interaction
  - First-order perturbation theory
  - Harmonic oscillator
routing: Automated Checks Only
independently_verified: true
working_title: singlet-triplet contact degeneracy g
---

## Problem

Two identical spin-$1/2$ fermions of mass $m$ are confined to a one-dimensional harmonic oscillator of frequency $\omega$. The spin-independent Hamiltonian is
$$H=\frac{p_1^2}{2m}+\frac{p_2^2}{2m}+\frac12 m\omega^2 x_1^2+\frac12 m\omega^2 x_2^2+g\,\delta(x_1-x_2),$$
with $g>0$. Treat the contact term as a first-order perturbation on the non-interacting oscillator. Single-particle levels are $E_n=\hbar\omega\bigl(n+\tfrac12\bigr)$ for $n=0,1,2,\ldots$, with real normalized orbitals $\varphi_n(x)$. Among the eigenstates of the non-interacting problem that are simultaneous eigenstates of total spin $\mathbf{S}^2$, let $E_{\mathrm{s}}(g)$ be the energy of the lowest $S=0$ level and $E_{\mathrm{t}}(g)$ the energy of the lowest $S=1$ level, each retained through $O(g)$. Report the unique positive coupling $g_\star$ at which $E_{\mathrm{s}}(g_\star)=E_{\mathrm{t}}(g_\star)$. Give an exact expression in terms of $\hbar$, $m$, and $\omega$ only.

## Domain Explanation

This problem involves the exchange symmetry of two identical fermions and the spin-spatial correlation forced by the Pauli principle, which are part of Quantum Mechanics and Identical particles.
The problem also involves the first-order perturbative shift from a contact interaction on harmonic-oscillator product states, which is part of Quantum Mechanics and Perturbation theory.
However, the contact matrix element is fixed only after the correct singlet and triplet spatial symmetries are chosen; perturbation theory supplies the expansion, but identical-particle structure selects which states enter.

## Step 1

Step 1
Because $H$ is spin-independent, total spin $S$ labels the unperturbed eigenstates, and the spatial wavefunction must be symmetric for $S=0$ and antisymmetric for $S=1$. The lowest singlet therefore places both particles in the oscillator ground orbital $\varphi_0$, with unperturbed energy
$$E_{\mathrm{s}}^{(0)}=\hbar\omega\Bigl(0+\tfrac12\Bigr)+\hbar\omega\Bigl(0+\tfrac12\Bigr)=\hbar\omega.$$
The lowest triplet cannot occupy $(\varphi_0,\varphi_0)$; its spatial part is the antisymmetrized product of $\varphi_0$ and $\varphi_1$, with
$$E_{\mathrm{t}}^{(0)}=\hbar\omega\Bigl(0+\tfrac12\Bigr)+\hbar\omega\Bigl(1+\tfrac12\Bigr)=2\hbar\omega.$$

## Step 2

Step 2
The first-order contact shifts are $E^{(1)}=g\langle\delta(x_1-x_2)\rangle$. For the symmetric product $\varphi_0(x_1)\varphi_0(x_2)$,
$$\langle\delta(x_1-x_2)\rangle_{\mathrm{s}}=\int_{-\infty}^{\infty}|\varphi_0(x)|^4\,\mathrm{d}x.$$
With $\alpha=m\omega/\hbar$ and $\varphi_0(x)=(\alpha/\pi)^{1/4}e^{-\alpha x^2/2}$, one has $|\varphi_0(x)|^4=(\alpha/\pi)e^{-2\alpha x^2}$, so
$$\int|\varphi_0|^4\,\mathrm{d}x=\frac{\alpha}{\pi}\sqrt{\frac{\pi}{2\alpha}}=\sqrt{\frac{\alpha}{2\pi}}=\sqrt{\frac{m\omega}{2\pi\hbar}}.$$
Thus $E_{\mathrm{s}}^{(1)}=g\sqrt{m\omega/(2\pi\hbar)}$. For the antisymmetric $(\varphi_0,\varphi_1)$ state the spatial wavefunction vanishes at $x_1=x_2$, so $\langle\delta(x_1-x_2)\rangle_{\mathrm{t}}=0$ and $E_{\mathrm{t}}^{(1)}=0$. Through $O(g)$,
$$E_{\mathrm{s}}(g)=\hbar\omega+g\sqrt{\frac{m\omega}{2\pi\hbar}},\qquad E_{\mathrm{t}}(g)=2\hbar\omega.$$

## Step 3

Step 3
Set $E_{\mathrm{s}}(g_\star)=E_{\mathrm{t}}(g_\star)$:
$$\hbar\omega+g_\star\sqrt{\frac{m\omega}{2\pi\hbar}}=2\hbar\omega\implies g_\star=\hbar\omega\sqrt{\frac{2\pi\hbar}{m\omega}}=\sqrt{\frac{2\pi\hbar^3\omega}{m}}.$$
The equivalent radical form $\hbar\sqrt{2\pi\hbar\omega/m}$ is the same object. The positive root required by $g>0$ is unique.

Final Answer: $\boxed{\sqrt{2\pi\hbar^{3}\omega/m}}$

## Answer

$\sqrt{2\pi\hbar^{3}\omega/m}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- Reflex is to put the "ground state" in $(\varphi_0,\varphi_0)$ for both spin channels, or to keep a nonzero contact shift for the triplet. Antisymmetry forces $E_{\mathrm{t}}^{(0)}=2\hbar\omega$ and $\langle\delta\rangle_{\mathrm{t}}=0$, while the singlet sits at $\hbar\omega$ plus $g\sqrt{m\omega/(2\pi\hbar)}$. Equating those is the only route to $g_\star=\sqrt{2\pi\hbar^3\omega/m}$.
- Secondary misses: wrong $\int|\varphi_0|^4$ (dropping the $\sqrt{1/2}$), or counting orbital energies as $n\hbar\omega$ instead of $(n+1/2)\hbar\omega$, both of which move $g_\star$ by a clean algebraic factor.
