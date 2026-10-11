# Create the beam-splitter Bayesian-posterior submission and validate it
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config'))

from src.models.problem import RigaProblem, SolutionStep, Classification, Subject, Difficulty, ReasoningType
from src.validators.riga_validator import RigaValidator
from domain_registry import DOMAIN_REGISTRY

prompt = (r"A single photon is injected into input mode 1 of a Mach"
          r"--Zehnder interferometer built from two identical lossless 50:50 beam splitters. "
          r"Each beam splitter transforms the input creation operators $(a_1^\dagger, a_2^\dagger)$ "
          r"into output operators $(b_1^\dagger, b_2^\dagger)$ by "
          r"$b_1^\dagger = \frac{1}{\sqrt{2}}(a_1^\dagger + i a_2^\dagger)$ and "
          r"$b_2^\dagger = \frac{1}{\sqrt{2}}(i a_1^\dagger + a_2^\dagger)$. "
          r"Between the two beam splitters, a phase shifter in internal mode 2 applies a "
          r"phase factor $e^{i\phi}$ to the one-photon component occupying that mode, where "
          r"$\phi$ is chosen once, uniformly at random, from the set $\left\{0, \frac{\pi}{2}\right\}$ "
          r"and is not revealed to the experimenter. The detectors at the two output ports are "
          r"ideal photon-number-resolving detectors with unit efficiency. In a single realization "
          r"of the experiment, exactly one photon is detected at output port 1 and no photon is "
          r"detected at output port 2. Given this measurement outcome, compute the posterior "
          r"probability that $\phi = 0$. Express the answer as a fraction in lowest terms.")

p1 = (r"Step 1" + "\n" +
      r"The input state is $a_1^\dagger|0\rangle = |1_1 0_2\rangle$. Applying the beam-splitter "
      r"1 transformation to $a_1^\dagger$ gives $\frac{1}{\sqrt{2}}(b_1^\dagger + i b_2^\dagger)|0\rangle$, "
      r"i.e. the internal-mode state is $\frac{1}{\sqrt{2}}\left(|1_1 0_2\rangle + i |0_1 1_2\rangle\right)$.")

p2 = (r"Step 2" + "\n" +
      r"The phase shifter maps $|0_1 1_2\rangle \to e^{i\phi}|0_1 1_2\rangle$, so the state entering "
      r"beam splitter 2 is $\frac{1}{\sqrt{2}}\left(b_1^\dagger + i e^{i\phi} b_2^\dagger\right)|0\rangle$. "
      r"Inverting the beam-splitter transformation for beam splitter 2 with output-mode operators "
      r"$(c_1^\dagger, c_2^\dagger)$ gives $b_1^\dagger = \frac{1}{\sqrt{2}}(c_1^\dagger - i c_2^\dagger)$ "
      r"and $b_2^\dagger = \frac{1}{\sqrt{2}}(c_2^\dagger - i c_1^\dagger)$. Substituting and collecting "
      r"the coefficient of $c_1^\dagger$ yields the output-port-1 amplitude "
      r"$A_1(\phi) = \frac{1}{2}\left(1 + e^{i\phi}\right)$, so the conditional detection probability is "
      r"$P(1_1 \mid \phi) = |A_1(\phi)|^2 = \frac{1}{4}\left(2 + 2\cos\phi\right) = \cos^2\frac{\phi}{2}$.")

p3 = (r"Step 3" + "\n" +
      r"Evaluating, $P(1_1 \mid \phi = 0) = \cos^2 0 = 1$ and "
      r"$P(1_1 \mid \phi = \tfrac{\pi}{2}) = \cos^2\tfrac{\pi}{4} = \frac{1}{2}$. Because the hidden "
      r"phase is a classical random variable (each hidden branch is itself coherent, so amplitudes are "
      r"squared within a branch before mixing), the posterior is a Bayesian update over the two branches "
      r"with uniform priors: $P(\phi = 0 \mid 1_1) = \frac{P(1_1 \mid \phi=0)}{P(1_1 \mid \phi=0) + "
      r"P(1_1 \mid \phi=\frac{\pi}{2})} = \frac{1}{1 + \frac{1}{2}} = \frac{2}{3}$." + "\n\n" +
      r"Final Answer: $\boxed{\frac{2}{3}}$")

prob = RigaProblem(
    title="Hidden-phase Mach-Zehnder Bayesian posterior",
    prompt_latex=prompt,
    solution_steps=[SolutionStep(1, p1), SolutionStep(2, p2), SolutionStep(3, p3)],
    answer=r"$\frac{2}{3}$",
    classification=Classification(
        subject=Subject.PHYSICS,
        domain="Quantum Mechanics",
        subdomain="Quantum optics",
        domain_explanation=("This problem involves single-photon Fock states, beam-splitter "
                            "unitaries, and a Bayesian posterior over a hidden quantum phase, "
                            "which are part of Physics, Quantum Mechanics. The problem also "
                            "involves interferometric phase optics, which is part of Physics, "
                            "Optics. However, the optical elements enter only through their "
                            "unitary action on quantum states and the core task is quantum "
                            "amplitude interference plus Bayesian inference, so Quantum "
                            "Mechanics is the more appropriate domain."),
        difficulty=Difficulty.HARD,
        reasoning_types=[ReasoningType.MULTI_STEP_DEDUCTION, ReasoningType.QUANTITATIVE_REASONING,
                         ReasoningType.CONCEPTUAL_SYNTHESIS],
        problem_type="Derivation with exact numeric result",
        answer_type="Exact rational number",
        concepts=["Beam splitter unitary", "Single-photon Fock states",
                  "Multipath interference", "Hidden-variable Bayesian inference"],
    ),
    author_notes=("Authoring pattern 1.1 (bridge QM + Bayesian inference) + 1.4 (hidden "
                  "iterated stage; classical-probability shortcut gives 1/2 not 2/3). "
                  "Verify on >=2 frontier models in the platform and mark stumps_verified."),
    stumps_verified=False,
)

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'data', 'problems', 'hidden_phase_mach_zehnder.json')
prob.to_json(out)
print('wrote', out)

v = RigaValidator(domain_registry=DOMAIN_REGISTRY)
issues = v.validate(prob)
for i in issues:
    print(f"[{i.severity}] {i.category.value}: {i.message}")
    if i.suggestion:
        print("   -> " + i.suggestion)
print('errors:', sum(1 for i in issues if i.severity == 'error'))
