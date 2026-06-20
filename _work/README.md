# Pitchfork Work Area

This directory contains maintainer-facing plans, workflow dashboards, working
notes, and Codex session records for Pitchfork.

## Authority

Pitchfork owns shared domain contracts, accounting and settlement semantics,
resource-state transitions, projection derivation, and database-independent
persistence interfaces. Pancakes owns node applications and physical
persistence; deployment belongs in `site-ops`; organization-level coordination
belongs in `fley-org`; controlled procedures and reviews belong in `fley-qms`.

## Workflow Files

- `repo-workflow.md` is the point-of-work copy of the canonical FLEY workflow.
- `plans/plans.csv` tracks multi-step Pitchfork work fronts.
- `plans/*.md` contains plan scope, constraints, and acceptance criteria.
- `todo.csv` tracks executable tasks.
- `todo.md` provides expanded task context when needed.
- `codex-log.md` records concise, durable Codex session findings.

## Verification

Run:

```sh
make check-work
```

This validates the workflow dashboards and canonical workflow copy.
