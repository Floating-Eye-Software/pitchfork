# Pitchfork Codex Log

Concise append-only summaries for Codex sessions.

---

# codex-001 - Core Foundation Planning And Workflow Adoption

**Plan:** `0003-core-foundation`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-20 EDT

## Changes

- Added the Pitchfork Core Foundation plan covering domain models,
  deterministic settlement, persistence interfaces, packaging, and tests.
- Renumbered the existing governance roadmap and RPG specification migration
  plans as `0001` and `0002`, and assigned Core Foundation plan ID `0003`.
- Adopted the canonical FLEY repository workflow with repo-local instructions,
  plan and todo dashboards, workflow documentation, and verification targets.
- Recorded `0003-core-foundation` as ready; the earlier planning documents
  remain todo and no plans were closed.

## Verification

- `make check-work`
- `git diff --check`

## Cross-Repository Follow-up

- Pancakes plans `0006-node-ambience-event-plan` and
  `0007-node-foundation` now refer to `pitchfork:0003-core-foundation` in the
  adjacent Pancakes working tree.
- The organization repository registry now classifies Pitchfork workflow
  adoption as `adopted` in the adjacent `fley-org` working tree.

---

# codex-002 - Local Testing Framework Dependency

**Plan:** `0004-local-testing-framework`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-20 EDT

## Changes

- Distinguished ordinary engineering tests from formal QMS-controlled design
  verification evidence.
- Determined that missing dedicated QMS V&V procedures do not block local
  Pitchfork engineering tests.
- Added Plan `0004-local-testing-framework` for pytest, Hypothesis, suite
  structure, stable Make targets, deterministic isolation, coverage reporting,
  clean-environment setup, and framework verification.
- Marked Plan `0003-core-foundation` blocked on Plan 0004 and added three
  sequenced implementation todos.
- No plan was closed.

## Verification

- `make check-work`
- `git diff --check`

## Cross-Repository Context

- The discovered dependency chain and the repository-workflow/GitHub-QMS
  interface were documented in
  `fley-org/reports/2026-06-20-pancakes-node-sitrep.md` in the adjacent
  `fley-org` working tree.
- Pancakes Plans 0006 and 0007 remain downstream of Pitchfork Plan 0003.
