# Answer formatting (V1.3)

Last solution step:

```
Final Answer: $\boxed{AUC}$
```

Answer box:

```
$AUC$
```

Rules:

- The two payloads must match **exactly**.
- Answer box: wrap in `$...$` only. Never `\boxed`.
- If the prompt omitted units, put them in the answer.
- If the answer is parametric, the prompt must name the allowed symbols.
- If a decimal is required, the prompt must give rounding (decimal places or significant figures). Without that instruction, a model's rounding is not an error.
- Unique object, possibly several equivalent written forms. `DNE` is illegal.
- Notation in the answer must have been introduced in the prompt.

Worked numeric example (gold Harned cell):

- Last step: `Final Answer: $\boxed{0.455\,\mathrm{V}}$`
- Answer box: `$0.455\,\mathrm{V}$`
