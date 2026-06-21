# 0004 Pitchfork Local Testing Adapter

## Status

Done

## Purpose

Establish the repository-local Python testing framework required before the
Pitchfork Core Foundation is implemented.

This plan adopts the provisional FLEY Repository Testing Process at
`../fley-org/process/fley-testing.md` and implements Pitchfork's pytest adapter
to its runner-neutral contract. It defines how developers configure, select,
run, report, and maintain automated tests in this repository. It does not
define controlled QMS verification or validation procedures and does not make
ordinary test output a controlled QMS record.

The FLEY process and this adapter are both provisional. Implementation findings
that apply across materially different repositories should be routed back to
FLEY Org as proposed contract revisions. Pytest-specific behavior remains in
Pitchfork rather than becoming an organization-wide requirement.

## Relationship To Core Foundation

Plan `0003-core-foundation` requires unit, contract, property-based, packaging,
and deterministic replay tests. It is blocked until this plan provides a
working test runner, suite structure, dependency declaration, and stable local
commands.

After this plan is complete, Plan 0003 owns the product test cases and their
acceptance criteria. This plan continues to own shared test configuration and
developer-facing test infrastructure.

## Framework Decisions

Conform to the FLEY process for command stability, strict exit behavior,
selection, isolation, fixture ownership, generated results, and adapter
conformance. Use:

* `pytest` as the test runner;
* `hypothesis` for property-based tests;
* `pytest-cov` and `coverage.py` for diagnostic coverage reporting;
* standard-library temporary paths and in-memory adapters for isolation;
* `python -m pytest` as the canonical direct invocation;
* Make targets as stable, discoverable repository entry points.

Do not introduce a test orchestration service, container requirement, database,
or network dependency for the local Pitchfork engine suites. A Python-version
matrix and hosted CI may be added later after supported package versions are
declared by Plan 0003.

Coverage and test reports are diagnostic engineering outputs. They must not
change test selection, assertions, or exit behavior. A coverage percentage is
not a substitute for requirement coverage, invariant testing, or review, and no
minimum percentage gate is required by this foundation plan.

## Test Layout

Create an explicit suite structure:

```text
tests/
  unit/
  contract/
  property/
  integration/
  fixtures/
```

The FLEY suite model treats unit and integration as execution scopes, while
contract and property describe purposes or techniques that can overlap those
scopes. Pitchfork retains explicit contract and property directories and
targets because Plan 0003 needs those selectors. The initial adapter uses:

* `unit` for isolated domain and rule behavior;
* `contract` for repository and public-interface compatibility;
* `property` for invariants and generated cases;
* `integration` for package-boundary tests that remain local and
  database-independent;
* `fixtures` for version-controlled representative inputs shared by suites.

Pitchfork has no end-to-end suite in this plan. An unsupported `test-e2e`
target must not be added as a successful no-op. If an end-to-end suite becomes
applicable later, its owner must define its environment and aggregate-gate
status explicitly.

Tests requiring Pancakes, SQLAlchemy, PostgreSQL, external services, or network
access belong to the owning Pancakes plan and must not be silently included in
Pitchfork's fast local suite.

## Suite Selection And Commands

Borrow the useful structural ideas from Halfbaked's publication test harness:
version-controlled fixtures, explicit suite selection, narrow commands, an
aggregate gate, and reproducible output. Do not copy its publication-specific
Pandoc or PDF machinery.

Provide these stable targets:

```text
make test-unit
make test-contract
make test-property
make test-integration
make test
make test-cov
make test-report
```

`make test` is the required aggregate local gate and must run every default
database-independent suite. Narrow targets support fast development feedback.
The gate must reject an unexpectedly empty required suite and an empty
aggregate selection. Required runner or plugin dependencies must not be skipped
when unavailable. Make and subprocess failures must propagate unchanged as a
non-zero result.

`make test-cov` runs the same aggregate selection with diagnostic coverage.
`make test-report` runs the same aggregate selection and writes JUnit XML plus
machine-readable execution metadata to a documented ignored results directory.
Neither command may weaken selection or pass/fail behavior. Metadata should
capture the command, start and end time, exit status, Python and runner
versions, platform, repository revision, and dirty-worktree state. These
outputs remain ordinary engineering records unless a higher-level process
controls and retains them.

Use registered pytest markers when markers provide selection. Strict marker and
configuration settings, collection errors, invalid selectors, and warnings
that could hide configuration, collection, or skipped required tests must fail
the command so that misspelled or silently skipped suites cannot create false
confidence. Any warning deliberately permitted by local policy must be narrow
and documented.

## Determinism And Isolation

The framework must:

* avoid order-dependent tests;
* expose random seeds when generated cases fail;
* freeze or inject time rather than reading the wall clock in product tests;
* use temporary directories rather than repository-local runtime files;
* prohibit production database files and implicit network access;
* avoid dependence on developer-specific environment variables;
* make test failures reproducible with a documented direct command;
* leave generated results only in documented ignored locations;
* produce no repository-runtime files and clean up child resources after both
  success and failure;
* behave consistently on repeated execution without relying on retained state.

Hypothesis failures must retain the reproducing example in normal developer
operation. Repository policy for committing a regression example should be
documented: retain it as a focused test or version-controlled fixture when it
protects a material invariant.

## Dependency And Configuration Ownership

Declare test dependencies in `pyproject.toml` under a dedicated test or
development extra. Plan 0004 may establish the minimum project metadata needed
for test installation; Plan 0003 remains responsible for completing production
package metadata and the installable package layout.

Centralize pytest, coverage, and Hypothesis configuration in version-controlled
repository files. Do not require global Python packages or an undocumented
developer environment.

Document setup from a clean virtual environment. Lock-file adoption is a
separate packaging and dependency-management decision and is not required by
this plan.

Document the expected Python environment, dependency installation, every suite
and selector, aggregate membership, fixture ownership, generated-result
location, external-resource boundary, and direct reproduction of one failing
case. Fixtures affecting outcomes must be version controlled or generated
deterministically from version-controlled sources, with provenance and expected
behavior documented where relevant.

## Engineering Tests And Controlled Verification

Routine automated test runs are engineering feedback. They become formal
design-verification evidence only when an applicable, approved design-control
or verification plan identifies the test version, configuration, environment,
acceptance criteria, execution, and retained result as controlled evidence.

Missing dedicated QMS V&V procedures do not block this local framework. Any
future controlled-use profile should invoke these stable commands rather than
replace the repository's test implementation.

## Implementation Phases

### Phase 1 — Configuration And Layout

Add test dependencies and configuration, create the suite directories, define
markers and deterministic defaults, and add the minimum adapter tests needed to
prevent required selections from being empty.

### Phase 2 — Stable Commands

Add narrow Make targets, the aggregate local gate, coverage reporting, JUnit
reporting, and execution metadata. Enforce required non-empty selections and
strict failure propagation.

### Phase 3 — Framework Verification And Documentation

Add a repeatable adapter-conformance check that uses temporary sentinel tests
or configuration and leaves the committed suites passing. Verify collection,
selection, empty-selection rejection, passing and failing exit behavior,
report equivalence, isolation, repeated execution, and clean-environment setup.
Document how Plan 0003 adds tests without bypassing the aggregate gate.

## Verification

Verify the framework itself by demonstrating:

* installation of declared test dependencies in a clean virtual environment;
* correct collection by each narrow suite target;
* complete collection by `make test`;
* rejection of an unexpectedly empty required suite and aggregate selection;
* non-zero exit status for a deliberately failing temporary test;
* zero exit status for the committed framework and product tests;
* rejection of invalid selectors, unknown markers, and configuration errors;
* strict handling of warnings that could invalidate the result;
* creation of coverage output without changing selection or results;
* creation of JUnit XML and execution metadata without changing selection or
  results;
* no undeclared database, network, production, or repository-runtime resources
  used or created by the suite;
* consistent repeated execution without test-order or retained-state
  dependence.

Temporary sentinel tests used to prove failure propagation must not remain in
the committed suite.

## Acceptance Criteria

This plan is complete when:

* a clean local environment can install the declared test dependencies;
* the documented narrow and aggregate commands exist and behave consistently;
* the adapter explicitly adopts the FLEY Repository Testing Process;
* the suite model, aggregate membership, fixtures, generated results, external
  resource boundaries, and ownership boundaries are documented;
* pytest and Hypothesis configuration is deterministic and version controlled;
* build, dependency, configuration, collection, empty-selection, setup,
  execution, and assertion failures cause the aggregate gate to fail;
* coverage reporting is available as a diagnostic command;
* JUnit reporting and execution metadata are available through
  `make test-report`;
* framework verification passes without external services;
* Plan 0003 can add its required tests without further test-infrastructure
  decisions.

## Dependencies

None.

## Verification Of Effectiveness

### Objectives Achieved

Pitchfork now has a pytest adapter to the provisional FLEY testing process with
four non-empty selectable suites, a strict aggregate gate, diagnostic coverage,
JUnit and execution-metadata reporting, network prohibition, deterministic
Hypothesis defaults, documented fixtures and generated state, and a repeatable
adapter-conformance command.

### Evidence

On 2026-06-20, a clean temporary Conda environment using Python 3.10 installed
the declared `.[test]` extra without developer user-site packages. All narrow
targets and the aggregate target passed. `make verify-test-adapter` passed with
six adapter tests across four suites and demonstrated narrow/aggregate
selection equivalence, repeated execution, expected failing and empty-suite
statuses, marker and configuration rejection, coverage/report selection
equivalence, report failure propagation, source-state preservation, and no
change to `pitchfork.db`.

### Residual Risks

The adapter currently exercises test infrastructure rather than product
behavior. Plan 0003 must add meaningful domain, contract, property, packaging,
and replay tests without weakening the aggregate gate. The shared FLEY process
is provisional and may need revision after adapters in other toolchains expose
cross-language requirements.

### Follow-on Actions

After closure approval, mark Plan 0003 ready. Re-run adapter conformance after
material runner, selection, reporting, or target changes, and route genuinely
cross-repository findings to FLEY Org.

### Lessons Learned

A runner-neutral contract can be verified before product implementation by
testing selection and execution semantics directly. Clean-environment checks
must disable Python user-site packages explicitly when Conda is used, because
Conda environments may otherwise inherit undeclared developer packages.

## Follow-on Work

When this plan is complete, mark `0003-core-foundation` ready and implement its
product code and tests through the established commands.
