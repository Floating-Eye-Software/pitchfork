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

---

# codex-003 - Pitchfork Test Adapter Implementation

**Plan:** `0004-local-testing-framework`
**Priority:** P1
**Status:** closed
**Timestamp:** 2026-06-20 22:14 EDT

## Changes

- Added minimum project metadata and a dedicated test extra for pytest,
  Hypothesis, coverage, and pytest-cov.
- Added non-empty unit, contract, property, and integration adapter suites with
  strict pytest configuration, deterministic Hypothesis behavior, and default
  network prohibition.
- Added stable narrow and aggregate Make targets, diagnostic coverage, JUnit
  reporting, execution metadata, and adapter-conformance verification.
- Documented clean virtual-environment and Conda setup, suite ownership,
  fixtures, generated outputs, isolation, direct reproduction, and the QMS
  boundary.
- Completed todos `todo-001` through `todo-003`; the user subsequently
  approved Plan 0004 closure and Plan 0003 unblocking.

## Verification

- Clean temporary Conda environment with Python 3.10 and
  `PYTHONNOUSERSITE=1`: `python -m pip install -e '.[test]'`
- `make test-unit test-contract test-property test-integration test`
- `make test-cov`
- `make test-report`
- `make verify-test-adapter`: six tests across four suites
- `make check-work`
- `git diff --check`

## Residual Risk

- The current suites verify adapter behavior only. Plan 0003 must add product
  tests while preserving the established aggregate gate.
- The shared FLEY testing process remains provisional pending experience from
  other repository adapters.

---

# codex-004 - Local Testing Framework Closure

**Plan:** `0004-local-testing-framework`
**Priority:** P1
**Status:** closed
**Timestamp:** 2026-06-20 22:29 EDT

## Closure

- The user approved closure after reviewing the implemented adapter and its
  conformance evidence.
- Marked Plan 0004 done and retained all three implementation todos as done.
- Marked Plan 0003 ready now that its declared testing-framework dependency is
  complete.
- Established `.conda-test` as the ignored local environment used by bare
  `make test`; the environment itself is not committed.

## Verification

- `make test`
- `make verify-test-adapter`
- `make test-cov`
- `make test-report`
- `make check-work`
- `git diff --check`

## Follow-on Work

- Execute Plan `0003-core-foundation` and add product tests through the stable
  aggregate gate.
- Route only genuinely cross-repository adapter findings back to the
  provisional FLEY testing process.

---

# codex-005 - Core Foundation Design Draft Alignment

**Plan:** `0003-core-foundation`
**Priority:** P1
**Status:** ready
**Timestamp:** 2026-06-21 01:58 EDT

## Changes

- Added the initial Core Foundation design directory, planning drafts,
  requirements and rationale, and risk register supplied by the user.
- Reconciled Plan 0003 with those drafts and the established Pitchfork testing
  adapter without modifying the design drafts themselves.
- Added requirements and risk review, architecture review, implementation,
  verification, validation, traceability, and release-readiness phases.
- Added explicit immutable-event and immutable-result semantics, package import
  safety, documented errors, rollback and failure injection, projection
  reconstruction, and concurrent duplicate-protection obligations.
- Identified eight design inputs that must be resolved and recorded before the
  initial Lone Honk rule and public interface are implemented.
- Clarified that draft repository design-control language does not itself
  establish controlled QMS approval or evidence; applicable controlled
  procedures remain owned by `fley-qms`.

## Verification

- `make test`
- `make verify-test-adapter`
- `make check-work`
- `git diff --check`

## Follow-on Work

- Begin Plan 0003 with requirements and risk review rather than immediately
  fixing public interfaces in code.
- Resolve the numeric representation, event schema, migration resource,
  `red_moon` derivation, API/result shape, duplicate semantics, supported
  Python versions, and Pancakes concurrency contract.

---

# codex-006 - Repository Boundary Content Cleanup

**Plan:** `0001-pancakes-governance-and-architecture-roadmap`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Moved Pancakes product, governance, node, service-exchange, recipe, grimoire,
  mentor, guide, and ecosystem-doctrine material into the Pancakes repository.
- Moved Pitchfork contract architecture and its explanatory reader into
  Pitchfork documentation and updated current indexes and cross-repository
  references.
- Routed the Financial and Budgeting Client notes and the Pancakes/ISO
  9001/GIFI feasibility notes into the Fley Org project nursery.
- Routed the former `refs/` inputs into Pancakes design inputs and removed the
  now-empty `refs/` and `_work/drafts/` directories.
- Included the maintainer-staged removal of obsolete Pitchfork `_work`
  material.

## Verification

- `make check-work`
- `git diff --check`
- remaining `_work` inventory review

## Follow-on Work

- Continue Pitchfork Plan 0003 using the retained core foundation design and
  contract documents.
- Reconcile or close Pitchfork Plan 0001 after its remaining lifecycle and
  repository-boundary deliverables are reviewed.

---

# codex-007 - Private Organization Transfer

**Plan:** none
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Recorded the completed private transfer to
  `git@github.com:Floating-Eye-Software/pitchfork.git`.
- Updated the local `origin` and verified authenticated access to `main` at
  commit `60bd048`.
- Kept the repository private; ownership transfer does not satisfy or bypass a
  future public-readiness and visibility review.
