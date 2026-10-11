# Scratch v6 — Hardest: enzyme 1 is itself feedback-inhibited by P → genuinely simultaneous steady state, two quadratics, double root rejection

## Target answer
[S]_tot = **440 μM** (exact integer — same number as v5, reached through a far deeper chain: the flux itself is now unknown and must be solved, not read off).

## The coupled system (three equations, three unknowns: v, [P], x = [S⁻])
(1) **Feedback-inhibited upstream enzyme** (competitive feedback by P, K_F = 2):
    v = 480 / ( 15(1 + [P]/2) + 30 ),  since Vmax1 = 16, [G] = 30, Km1 = 15 → numerator 16·30 = 480.
(2) **Saturable export:** v = 16[P]/(2 + [P])  →  [P] = 2v/(16 − v).
(3) **Cooperative inhibited consumption:** v = 10 x²/(K′² + x²), K′ = α·4, α = 1 + 3/1 + [P]/2.

## Solving (1)+(2) for the flux
Substitute (2) into (1): v = 480/(45 + 15v/(16 − v))
→ v[45(16−v) + 15v] = 480(16−v)
→ 30v² − 1200v + 7680 = 0 → v² − 40v + 256 = 0 → v = 8 or v = 32.
**Root rejection:** v = 32 > V_e = 16 makes (2) demand [P] < 0; the export plateau is 16, so no real steady state exists at that branch. Hence v = 8 μM/min. — TRUE physical root selection, not cosmetic.

Then [P] = 2·8/8 = 2 μM; self-check: enzyme 1 gives 480/(15·2+30) = 480/60 = 8 ✓.

Then α = 1 + 3 + 1 = 5 → K′ = 20; Hill: 8 = 10x²/(400 + x²) → x² = 1600 → x = 40 (reject −40).
Ionization (pH 6, pKa 7): [S⁻] = S_tot/11 → S_tot = 11·40 = **440**.

## Numbers engineered
- Discriminant 1600 − 1024 = 576 = 24² → roots exactly 8 and 32; spurious root exactly 2× V_e so rejection is unambiguous.
- Baseline flux without feedback = 16·30/45 = 32/3 — non-integer, so a model that drops feedback lands on an ugly number AND finds it exceeds Vmax2=10, correctly sensing collapse but flailing for the fix.

## Distractor map
| Mistake | Consequence |
|---|---|
| Full correct chain | **440** |
| Drop feedback (v = 32/3) | flux > Vmax2 → impossible; model flails / hallucinates |
| Keep wrong root v = 32 | [P] = −4 → negative concentration or nonsense; blocked by physics |
| Linear export assumed | chained errors; no clean closure |
| n=1 Hill | x=80 → 880 |
| Drop ionization | 40 |
| Inverted H–H | 44 |
| α on Vmax | v > plateau → "DNE" hallucination (blocked by prompt) |

Six substantial steps: set up trio → eliminate to flux quadratic → physical root rejection → product & self-check → inhibition factor → Hill quadratic + root rejection → ionization conversion.
