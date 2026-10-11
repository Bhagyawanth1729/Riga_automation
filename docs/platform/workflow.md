# End-to-end workflow

```
idea → scratch.md solve → task.md draft → qa_gate PASS
    → preflight → promote to ready → paste_ready
    → left-pane model run (consistent miss)
    → remaining UI fields → In-App LaTeX check
    → Automated Checks Only → read warnings
    → Quality Review → Accept | Needs Revision | Reject
```

## Time expectation

Riga's Code of Conduct punishes very low handling time. A real item takes a sitting: design, solve twice, write, gate, stump test. Do not batch-generate.

## If models solve it

Change the science, not the English. Add a real constraint (activity, identical particles, failed approximation, stated non-default standard state). Re-verify from scratch.

## If automated checks say your answer is wrong

Believe them until you have recomputed. The gold example in `docs/examples/` shows the density of arithmetic a reviewer expects to see.

## If Needs Revision comes back

Move the folder to `submissions/needs_revision/` (`python3 scripts/promote.py path/to/task.md needs_revision`). Copy the reviewer categories into `task.md` Author Notes. Fix only what was asked plus any gate failures. Re-run models if Problem or Answer changed.

## If Accept comes back

Move to `submissions/accepted/`. That lane is the only place an item is called accepted. Do not invent an accepted file locally.
