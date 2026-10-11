---
field: Biology
domain: Biochemistry and Metabolism
subdomain: Enzyme Kinetics
difficulty: Hard
problem_type: Exact computation
answer_type: Exact scalar
solution_concepts:
  - cooperative Hill kinetics
  - competitive inhibition of allosteric enzymes
  - saturating Michaelis-Menten transport and its inversion
  - end-product inhibition with product steady state
  - Henderson-Hasselbalch ionization equilibria
concepts_raw: cooperative Hill kinetics, competitive inhibition of allosteric enzymes, saturating Michaelis-Menten transport and its inversion, end-product inhibition with product steady state, Henderson-Hasselbalch ionization equilibria
---

# Problem Statement

A two-enzyme metabolic pathway is reconstituted in a well-mixed cell-free extract buffered at pH 6.00. The metabolite S is produced from the upstream precursor G by enzyme 1 and is converted by enzyme 2 into a product P, which is then exported from the compartment by a **saturable transporter**. Small-molecule concentrations greatly exceed enzyme and transporter concentrations, so free-ligand concentrations may be used throughout. The system is observed to reach a genuine steady state in which both $[S]_{\mathrm{tot}}$ and $[P]$ are constant in time.

**Upstream production.** Enzyme 1 produces total S at the rate

$$v_1 = \frac{V_{\max,1}\,[G]}{K_{m,1} + [G]}$$

with $V_{\max,1} = 12\ \mu\text{M}\,\text{min}^{-1}$, $K_{m,1} = 15\ \mu\text{M}$, and $[G]$ is clamped at $30\ \mu\text{M}$ by continuous replenishment. The flux $v_1$ refers to total S across all ionic forms.

**Ionization of S.** S is a weak acid in rapid equilibrium with its conjugate base:

$$\text{SH} \rightleftharpoons \text{S}^- + \text{H}^+, \qquad \mathrm{p}K_a = 7.00,$$

with pH held fixed by the buffer and protonation equilibration much faster than turnover. Enzyme 2 binds **only the deprotonated form S⁻**; SH is catalytically invisible to enzyme 2 but counts toward the total pool $[S]_{\mathrm{tot}} = [\text{SH}] + [\text{S}^-]$.

**Cooperative consumption with two competitive inhibitors.** Enzyme 2 is a homodimeric allosteric enzyme obeying a Hill-type rate law with Hill coefficient $n_H = 2$:

$$v_2 = \frac{V_{\max,2}\,[\text{S}^-]^2}{K'^{\,2} + [\text{S}^-]^2}, \qquad K' = \alpha\,K_{0.5}, \qquad \alpha = 1 + \frac{[I]}{K_I} + \frac{[P]}{K_P},$$

where competitive inhibitors shift the half-saturation constant $K_{0.5} = 4\ \mu\text{M}$ by the factor $\alpha$, leaving $V_{\max,2} = 10\ \mu\text{M}\,\text{min}^{-1}$ unchanged. An external inhibitor I is present at $[I] = 3\ \mu\text{M}$, $K_I = 1\ \mu\text{M}$, and the product P additionally acts as a competitive end-product inhibitor, $K_P = 2\ \mu\text{M}$.

**Saturable product export.** P is removed by a membrane transporter that itself follows Michaelis–Menten kinetics with capacity $V_e = 16\ \mu\text{M}\,\text{min}^{-1}$ and $K_e = 2\ \mu\text{M}$:

$$\frac{d[P]}{dt} = v_2 \;-\; \frac{V_e\,[P]}{K_e + [P]},$$

starting from $[P] = 0$.

Determine the steady-state value of $[S]_{\mathrm{tot}}$.

**Answer format:** Give $[S]_{\mathrm{tot}}$ as an exact number in $\mu\text{M}$ (no rounding needed). Because a steady state is stated to exist, "does not exist" is not an acceptable answer; do not include units in the answer field.

# Worked Solution

Step 1: Compute the upstream production flux. With $[G]$ clamped, $v_1$ is constant:
$$v_1 = \frac{12 \times 30}{15 + 30} = 8\ \mu\text{M}\,\text{min}^{-1}.$$

Step 2: Find the steady-state product concentration set by the saturable transporter. At steady state, S balance forces $v_2 = v_1 = 8\ \mu\text{M}\,\text{min}^{-1}$, and $d[P]/dt = 0$ requires
$$8 = \frac{16\,[P]}{2 + [P]} \quad\Longrightarrow\quad 8(2 + [P]) = 16\,[P] \quad\Longrightarrow\quad 16 = 8\,[P] \quad\Longrightarrow\quad [P] = 2\ \mu\text{M}.$$
(The transporter can sustain this because $8 < V_e = 16$.)

Step 3: Assemble the combined competitive-inhibition factor. The two independent competitive inhibitors contribute additively to $\alpha$:
$$\alpha = 1 + \frac{3}{1} + \frac{2}{2} = 5, \qquad K' = \alpha K_{0.5} = 5 \times 4 = 20\ \mu\text{M},$$
with the saturation plateau $V_{\max,2} = 10$ unchanged, as required for competitive inhibition.

Step 4: Relate the active species S⁻ to the total pool. From the Henderson–Hasselbalch relation at pH 6.00 with $\mathrm{p}K_a = 7.00$:
$$\frac{[\text{S}^-]}{[\text{SH}]} = 10^{\mathrm{pH}-\mathrm{p}K_a} = \frac{1}{10} \quad\Longrightarrow\quad [\text{S}^-] = \frac{[S]_{\mathrm{tot}}}{1 + 10} = \frac{[S]_{\mathrm{tot}}}{11}.$$

Step 5: Impose the cooperative steady-state balance $v_1 = v_2$ and solve the resulting quadratic. Writing $x = [\text{S}^-]$:
$$8 = \frac{10\,x^2}{20^2 + x^2} \quad\Longrightarrow\quad 8\,(400 + x^2) = 10\,x^2 \quad\Longrightarrow\quad 3200 = 2\,x^2 \quad\Longrightarrow\quad x^2 = 1600.$$
Rejecting the unphysical negative root gives $x = [\text{S}^-] = 40\ \mu\text{M}$.

Step 6: Convert to the total substrate pool and check consistency:
$$[S]_{\mathrm{tot}} = 11 \times 40 = 440\ \mu\text{M}, \qquad 8 < V_{\max,2} = 10,$$
so the required flux lies below the enzyme's plateau and the stated steady state is internally consistent.
Final Answer: $\boxed{440}$

# Answer

$440$

# Domain Justification

This problem belongs to Biochemistry and Metabolism because it requires the rigorous, simultaneous application of cooperative allosteric kinetics, dual competitive and end-product inhibition, inversion of a saturable transport law with a feasibility condition, metabolite ionization equilibria, and pathway-level steady-state flux balancing — the integrated quantitative machinery that defines modern enzyme kinetics and metabolic regulation.

# Classification

- **Problem Type:** Exact computation
- **Answer Type:** Exact scalar
- **Solution Concepts:** cooperative Hill kinetics, competitive inhibition of allosteric enzymes, saturating Michaelis-Menten transport and its inversion, end-product inhibition with product steady state, Henderson-Hasselbalch ionization equilibria
