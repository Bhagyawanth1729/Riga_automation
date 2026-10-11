# Scratch — Threshold K0 kinetic energy in associated production

Solve here first. Do not paste this file into Snorkel.

## Answer object (design this before the prompt)

Laboratory kinetic energy of the $K^0$ in $\pi^- + p \to K^0 + \Lambda$ at the
fixed-target threshold for the reaction. Two layers: (i) the threshold invariant, and
(ii) the boost of the at-rest product out of the center-of-momentum frame.

- Rest energies (MeV): $m_{\pi^-}c^2=139.570$, $m_pc^2=938.272$, $m_{K^0}c^2=497.611$, $m_\Lambda c^2=1115.683$.
- $s=(E+m_pc^2)^2-(p_\pi c)^2=m_{\pi^-}^2c^4+m_p^2c^4+2m_pc^2E$.
- Threshold: $s_{\mathrm{th}}=(m_{K^0}c^2+m_\Lambda c^2)^2=(1613.294)^2$.
- $E=(s_{\mathrm{th}}-m_{\pi^-}^2c^4-m_p^2c^4)/(2m_pc^2)=907.457\ \mathrm{MeV}$; $K_\pi=767.887\ \mathrm{MeV}$.
- $\gamma_{\mathrm{CM}}=(E+m_pc^2)/\sqrt{s_{\mathrm{th}}}=(907.457+938.272)/1613.294=1.14407$.
- At threshold $K^0$ is at rest in CM: $K_{K^0}=(\gamma_{\mathrm{CM}}-1)m_{K^0}c^2=0.14407\times497.611=71.69\ \mathrm{MeV}$.
- Rounded: $71.7\ \mathrm{MeV}$.

Independent cross-check: with $\beta_{\mathrm{CM}}=p_\pi c/(E+m_pc^2)=0.48579$, a direct boost
geometry gives the same $\gamma=1.14407$ and the same $71.69\ \mathrm{MeV}$.

## Independent check

- [x] Recomputed every displayed equality with the boxed line hidden
- [x] Units / sig figs / equivalent forms locked: MeV, three significant figures
- [x] Next-best domain considered and rejected in the justification (Relativity)
- [x] Prompt does not leak the method (gives the reaction, masses, and onset condition only)
- [x] Skeleton is not the previous draft (enzyme) or the gold Harned cell (no cell diagram)

## Why a frontier model should miss this

- The reflex answer is the threshold beam energy $K_\pi=767.887\ \mathrm{MeV}$ (or a
  non-relativistic $m_{K^0}c^2$ onset). The question asks for the $K^0$ laboratory kinetic
  energy, which requires the second layer: the CM Lorentz factor and the boost of an
  at-rest product.
- Other failure paths: boosting with the beam Lorentz factor instead of $\gamma_{\mathrm{CM}}$;
  forgetting that at threshold the final state is at rest in the CM.
