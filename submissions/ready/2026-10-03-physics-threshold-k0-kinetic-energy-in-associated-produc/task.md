---
id: 2026-10-03-physics-threshold-k0-kinetic-energy-in-associated-produc
status: ready
field: Physics
domain: Nuclear and Particle Physics
subdomain: Nuclear reactions
problem_type: Numerical approximation
answer_type: Physical quantity with units
concepts:
  - Relativistic kinematics
  - Invariant mass
  - Fixed-target threshold
  - Lorentz boost
  - Associated production
routing: Automated Checks Only
independently_verified: true
working_title: Threshold K0 kinetic energy in associated production
---

## Problem

A $\pi^-$ beam is directed onto a liquid-hydrogen target at rest. The associated-production reaction
$$\pi^- + p \to K^0 + \Lambda$$
has a sharp energy onset. Use the rest energies $m_{\pi^-}c^2=139.570\,\mathrm{MeV}$, $m_pc^2=938.272\,\mathrm{MeV}$, $m_{K^0}c^2=497.611\,\mathrm{MeV}$, and $m_\Lambda c^2=1115.683\,\mathrm{MeV}$. At the beam energy where the reaction first becomes energetically allowed, report the kinetic energy of the $K^0$ in the laboratory frame, in MeV, rounded to three significant figures.

## Domain Explanation

This problem involves the invariant-mass condition for a fixed-target reaction at threshold and the Lorentz transformation of the products from the center-of-momentum frame to the laboratory, which are part of Nuclear and Particle Physics and Nuclear reactions.
The problem also involves four-momentum conservation and the relativistic energy-momentum relation, which are part of Relativity and Relativistic momentum and energy.
However, the relativistic formalism is the tool here; the object computed is a nuclear-reaction threshold observable, so the item belongs to the nuclear pair.

## Step 1

Step 1
Let the incident pion have total energy $E$ in the laboratory, where the proton is at rest. Four-momentum conservation gives the invariant
$$s=(E+m_pc^2)^2-(p_\pi c)^2=m_{\pi^-}^2c^4+m_p^2c^4+2m_pc^2E,$$
using $E^2-(p_\pi c)^2=m_{\pi^-}^2c^4$. At threshold the products carry no kinetic energy in the center-of-momentum frame, so $s$ equals the square of the total rest energy of the final state, $(m_{K^0}c^2+m_\Lambda c^2)^2$.

## Step 2

Step 2
Set $s_{\mathrm{th}}=(m_{K^0}c^2+m_\Lambda c^2)^2=(1613.294\,\mathrm{MeV})^2$. Solving the invariant for the beam energy,
$$E=\frac{s_{\mathrm{th}}-m_{\pi^-}^2c^4-m_p^2c^4}{2m_pc^2}
=\frac{(1613.294)^2-(139.570)^2-(938.272)^2}{2(938.272)}\,\mathrm{MeV}=907.457\,\mathrm{MeV},$$
so the threshold beam kinetic energy is $K_\pi=E-m_{\pi^-}c^2=767.887\,\mathrm{MeV}$. The center-of-momentum frame moves in the laboratory with Lorentz factor
$$\gamma_{\mathrm{CM}}=\frac{E+m_pc^2}{\sqrt{s_{\mathrm{th}}}}=\frac{907.457+938.272}{1613.294}=1.14407.$$

## Step 3

Step 3
At threshold the $K^0$ is at rest in the center-of-momentum frame, so it has no momentum there and its laboratory energy is the boosted rest energy $\gamma_{\mathrm{CM}}m_{K^0}c^2$. Its laboratory kinetic energy is therefore
$$K_{K^0}=(\gamma_{\mathrm{CM}}-1)m_{K^0}c^2=(1.14407-1)(497.611\,\mathrm{MeV})=71.69\,\mathrm{MeV},$$
which rounds to $71.7\,\mathrm{MeV}$. A treatment that stops at the threshold beam energy, or that carries the outgoing $K^0$ non-relativistically, does not give this number.

Final Answer: $\boxed{71.7\,\mathrm{MeV}}$

## Answer

$71.7\,\mathrm{MeV}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed every displayed equality
- [x] `python3 scripts/qa_gate.py` PASS
- [x] `python3 scripts/preflight.py` PASS
Why a frontier model should miss this:
- The reaction threshold is only the first layer. Many replies compute $K_\pi=767.887\,\mathrm{MeV}$ (or apply a non-relativistic $K=m_{K^0}c^2$ threshold) and stop, because the standard reflex is "threshold = beam energy." The question asks for the $K^0$ laboratory kinetic energy, which needs the center-of-momentum Lorentz factor $\gamma_{\mathrm{CM}}=(E+m_pc^2)/\sqrt{s_{\mathrm{th}}}=1.14407$ and the boost of the at-rest product.
- Secondary miss paths: using the beam $\gamma$ instead of $\gamma_{\mathrm{CM}}$, or forgetting that at threshold the products are at rest in the center-of-momentum frame. Cross-check by an explicit boost with $\beta_{\mathrm{CM}}=p_\pi c/(E+m_pc^2)$ reproduces $71.69\,\mathrm{MeV}$.
