# Pitchfork Testing

Pitchfork implements the provisional FLEY Repository Testing Process in
`../fley-org/process/fley-testing.md` with a repository-local pytest adapter.
These commands provide ordinary engineering feedback; their output is not a
controlled QMS verification record unless an applicable approved process adds
those controls.

## Environment Setup

Use Python 3.10 or newer in a clean virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
```

Conda is an equivalent clean-environment option:

```sh
conda create --prefix .conda-test python=3.10 pip
conda run --prefix .conda-test python -m pip install -e '.[test]'
make test
```

The test command never installs dependencies. Installation is an explicit
environment-setup step. Make automatically uses `.venv/bin/python` or
`.conda-test/bin/python` when the environment contains pytest. Use
`TEST_PYTHON=/path/to/python` to select another prepared environment.

## Commands And Suites

`make test` is the authoritative aggregate local gate. It runs all four
database-independent suites:

* `make test-unit` tests isolated functions, components, or rules;
* `make test-contract` tests repository and public-interface compatibility;
* `make test-property` tests invariants with generated examples;
* `make test-integration` tests local component and process boundaries.

Contract and property describe test purposes that can overlap unit or
integration scope. Pitchfork keeps them selectable because the Core Foundation
plan requires both techniques. Pitchfork currently has no end-to-end suite, so
there is no successful no-op `test-e2e` target.

`make test-cov` runs the aggregate selection with diagnostic coverage.
`make test-report` runs the same selection and writes JUnit XML and execution
metadata under ignored `.test-results/`. Neither changes the assertions or
required selection. Run `make verify-test-adapter` after changing the runner,
selection, reporting, or Make targets.

To reproduce a single failure, pass its node identifier directly:

```sh
PYTHONNOUSERSITE=1 python -m pytest tests/unit/test_test_report.py::test_report_metadata_identifies_execution_environment
```

## Isolation And Generated State

The aggregate suite uses no public network, production service, SQL database,
or developer-specific environment variable. Tests must use pytest temporary
paths and in-memory adapters for mutable state. Time, identifiers, and random
inputs must be injected or controlled when they affect results.

Pytest, coverage, Hypothesis, and reporting may create only these ignored
diagnostic locations:

* `.coverage` and `.test-results/`;
* `.hypothesis/` for retained reproducing examples;
* `.pytest_cache/` and Python `__pycache__/` directories.

Hypothesis prints a reproducing blob for failures and retains examples locally.
When a generated example exposes a material defect, add a focused regression
test or a reviewed version-controlled fixture.

Tests requiring Pancakes, SQLAlchemy, PostgreSQL, a public network, or external
services belong to an explicit target and owning plan outside this aggregate
gate. Tests must never read or modify the root `pitchfork.db` runtime file.

## Fixtures And New Tests

Store shared representative inputs in `tests/fixtures/`. Document each
fixture's scenario, provenance or deterministic generation method, expected
behavior, and relevant format constraints. Include checksums for retained
binary or external-origin files.

Plan 0003 product tests should be placed in the applicable suite and must remain
reachable through `make test`. A required suite must never be changed into an
empty or silently skipped selection.
