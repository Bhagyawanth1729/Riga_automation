# LaTeX (V1.3 appendix)

Source: PDF pages 98–104.

## Allowed / forbidden

- `$...$` and `$$...$$` allowed. `\(...\)` and `\[...\]` forbidden.
- `mhchem` (`\ce{}`) supported. `chemfig` not supported.
- No unnecessary braces. Escape visible set braces: `\{1,2,3\}`.
- Polynomials: descending exponents.
- Fractions: `\frac{}{}`, simplified unless context needs otherwise.
- Units: `9.8\,\text{m/s}^2` or `\mathrm`.
- Use `\leq` not `<=`. Define uncommon symbols.
- No `\item` lists. No `**bold**` on steps. No KaTeX-only macros (`\lang`; use `\langle`).
- Rounding: the prompt must state it, or the model's rounding is not an error.
- Do not use LaTeX for non-math formatting (bullets, titles).

## Conversion table (accepted forms)

| Category | Write | Not |
|---|---|---|
| Fractions | `\frac{1}{2}`, `\frac{1}{2+3}` | `1/2` as the displayed answer |
| Roots | `\sqrt{2}`, `\sqrt[3]{8}`, `x^{\frac{1}{2}}` | `sqrt(2)` |
| Infinity | `\infty` | |
| Exponents | `2^{3}`, `e^{2}` | `2^3` when more than one token |
| Constants | `\pi`, `e`, `i`, `\phi` | `pi` |
| Trig / log | `\sin(\pi/2)`, `\ln(2)`, `\log_{10}(100)`, `\log_{2}{x}` | `sin(pi/2)` |
| Sets | `\{1, 2, 3\}`, `\emptyset`, `\mathbb{R}`, `\mathbb{Z}`, `\mathbb{Q}`, `\mathbb{N}` | `{1, 2, 3}` |
| Membership | `x \in A`, `x \notin A`, `A \cup B`, `A \cap B`, `A \setminus B` | |
| Quantifiers | `\forall x \in A`, `\exists x \in A` | |
| Combinatorics | `\binom{5}{2}`, `{}_5P_2`, `5!` | `C(5,2)` |
| Integrals | `\int_{0}^{1} f(x) \, dx`, `\iint_{R} f(x,y) \, dx \, dy`, `\oint_{C} f(z) \, dz` | |
| Matrices | `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` | `[[a,b],[c,d]]` |
| Transpose / det | `A^{T}`, `\det(A)`, `\mathbf{I}` | |
| Approx | `\sqrt{2} \approx 1.414` (only if the prompt ordered the rounding) | |
| Vectors | `\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}` | |

Coordinates and intervals may be written in math mode as $(3,4)$, $(0,1)$, $[0,1]$. Do **not** wrap them in `\(...\)` or `\[...\]` even though the PDF conversion table shows that forbidden form — project rule on page 98 wins.
