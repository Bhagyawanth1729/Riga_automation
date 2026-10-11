# Domain catalogs

Machine-readable tree: `data/catalogs/domains.json` (16 Biology, 18 Chemistry, 16 Physics domains, each with subdomains).

Pick the pair that names the **subject of the question**, not a tool used in one solution. The Domain Explanation must name a runner-up pair and say why it loses.

**Live Biology dropdown** on this account: `data/catalogs/platform_domains.json`. Genetics and Genomics appears in the PDF but is not selectable here. Do not assign it.

Problem forms (all fields): `data/catalogs/problem_types.json`  
Answer types (per field): `data/catalogs/answer_types.json`

```bash
python3 scripts/list_catalog.py --field Biology
python3 scripts/list_catalog.py --field Chemistry --types
```
