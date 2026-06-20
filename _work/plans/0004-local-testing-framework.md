# 0004 Local Testing Framework

## Status

Ready

## Purpose

Establish the repository-local Python testing framework required before the
Pitchfork Core Foundation is implemented.

This plan defines how developers configure, select, run, and maintain automated
tests in this repository. It does not define controlled QMS verification or
validation procedures and does not make ordinary test output a controlled QMS
record.

## Relationship To Core Foundation

Plan `0003-core-foundation` requires unit, contract, property-based, packaging,
and deterministic replay tests. It is blocked until this plan provides a
working test runner, suite structure, dependency declaration, and stable local
commands.

After this plan is complete, Plan 0003 owns the product test cases and their
acceptance criteria. This plan continues to own shared test configuration and
developer-facing test infrastructure.

## Framework Decisions

Use:

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

Coverage is diagnostic evidence about exercised code. A coverage percentage is
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

The initial local framework uses:

* `unit` for isolated domain and rule behavior;
* `contract` for repository and public-interface compatibility;
* `property` for invariants and generated cases;
* `integration` for package-boundary tests that remain local and
  database-independent;
* `fixtures` for version-controlled representative inputs shared by suites.

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
```

`make test` is the required aggregate local gate and must run every default
database-independent suite. Narrow targets support fast development feedback.
Coverage reporting must not alter test selection or outcomes.

Use registered pytest markers when markers provide selection. Unknown markers,
collection warnings, and configuration warnings must fail the test command so
that misspelled or silently skipped suites cannot create false confidence.

## Determinism And Isolation

The framework must:

* avoid order-dependent tests;
* expose random seeds when generated cases fail;
* freeze or inject time rather than reading the wall clock in product tests;
* use temporary directories rather than repository-local runtime files;
* prohibit production database files and implicit network access;
* avoid dependence on developer-specific environment variables;
* make test failures reproducible with a documented direct command.

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

Add test dependencies and configuration, create the suite directories, and
define markers and deterministic defaults.

### Phase 2 — Stable Commands

Add narrow Make targets, the aggregate local gate, and coverage reporting.
Ensure command failures propagate correctly.

### Phase 3 — Framework Verification And Documentation

Verify collection, selection, passing and failing exit behavior, isolation, and
clean-environment setup. Document how Plan 0003 adds tests without bypassing the
aggregate gate.

## Verification

Verify the framework itself by demonstrating:

* installation of declared test dependencies in a clean virtual environment;
* correct collection by each narrow suite target;
* complete collection by `make test`;
* non-zero exit status for a deliberately failing temporary test;
* zero exit status for the committed framework and product tests;
* rejection of unknown markers and configuration warnings;
* creation of coverage output without changing test results;
* no database, network, or repository-runtime files created by the suite.

Temporary sentinel tests used to prove failure propagation must not remain in
the committed suite.

## Acceptance Criteria

This plan is complete when:

* a clean local environment can install the declared test dependencies;
* the documented narrow and aggregate commands exist and behave consistently;
* the suite structure and ownership boundaries are documented;
* pytest and Hypothesis configuration is deterministic and version controlled;
* warnings, collection errors, and test failures cause the aggregate gate to
  fail;
* coverage reporting is available as a diagnostic command;
* framework verification passes without external services;
* Plan 0003 can add its required tests without further test-infrastructure
  decisions.

## Dependencies

None.

## Follow-on Work

When this plan is complete, mark `0003-core-foundation` ready and implement its
product code and tests through the established commands.
