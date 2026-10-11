# Scratch — singlet–triplet contact degeneracy

## Answer first

Target: coupling $g_\star$ at which the lowest $S=0$ and lowest $S=1$ two-fermion levels are degenerate through $O(g)$.

$$g_\star=\sqrt{\frac{2\pi\hbar^3\omega}{m}}=\hbar\sqrt{\frac{2\pi\hbar\omega}{m}}$$

## Setup

Two identical spin-$1/2$ fermions, 1D HO of frequency $\omega$, mass $m$.
Unperturbed single-particle energies $E_n=\hbar\omega(n+\tfrac12)$, $n=0,1,2,\ldots$
Perturbation $H'=g\,\delta(x_1-x_2)$, treated to first order.
Hamiltonian is spin-independent → total $S$ is a good quantum number; spatial symmetry is fixed by exchange.

## Singlet channel ($S=0$)

Spin antisymmetric ⇒ spatial symmetric.
Lowest spatial state: both particles in $n=0$
$$E^{(0)}_{\mathrm{s}}=\hbar\omega,\qquad
E^{(1)}_{\mathrm{s}}=g\int_{-\infty}^{\infty}|\varphi_0(x)|^4\,\mathrm{d}x.$$

Ground HO orbital: $\varphi_0(x)=(\alpha/\pi)^{1/4}e^{-\alpha x^2/2}$, $\alpha=m\omega/\hbar$.
$$|\varphi_0|^4=\frac{\alpha}{\pi}e^{-2\alpha x^2},\quad
\int|\varphi_0|^4\,\mathrm{d}x=\sqrt{\frac{\alpha}{2\pi}}=\sqrt{\frac{m\omega}{2\pi\hbar}}.$$
So $E_{\mathrm{s}}=\hbar\omega+g\sqrt{m\omega/(2\pi\hbar)}+O(g^2)$.

## Triplet channel ($S=1$)

Spin symmetric ⇒ spatial antisymmetric.
Lowest: one particle in $n=0$, one in $n=1$
$$E^{(0)}_{\mathrm{t}}=2\hbar\omega.$$
Antisymmetric spatial wavefunction vanishes on $x_1=x_2$, so
$\langle\delta(x_1-x_2)\rangle_{\mathrm{t}}=0$ and $E^{(1)}_{\mathrm{t}}=0$.
Thus $E_{\mathrm{t}}=2\hbar\omega+O(g^2)$.

## Degeneracy

$$\hbar\omega+g\sqrt{\frac{m\omega}{2\pi\hbar}}=2\hbar\omega
\implies g=\hbar\omega\sqrt{\frac{2\pi\hbar}{m\omega}}=\sqrt{\frac{2\pi\hbar^3\omega}{m}}.$$

## Expected model misses

1. Ignore exchange: put both channels in $(0,0)$, or allow $(0,0)$ for triplet → wrong $E^{(0)}$ or wrong contact matrix element.
2. Use $\langle\delta\rangle\neq0$ for the triplet Slater state.
3. Wrong $\int|\varphi_0|^4$ (forget the factor $1/\sqrt{2}$, or use 3D formula).
4. Count oscillator quanta as $\hbar\omega$ per orbital instead of $(n+1/2)\hbar\omega$.

## Independent arithmetic check

$\hbar\omega+g\sqrt{\alpha/(2\pi)}=2\hbar\omega$ with $\alpha=m\omega/\hbar$
$\Rightarrow g=\hbar\omega\sqrt{2\pi/\alpha}=\hbar\omega\sqrt{2\pi\hbar/(m\omega)}=\sqrt{2\pi\hbar^3\omega/m}$. ✓
