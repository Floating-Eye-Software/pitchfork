.PHONY: check-work check-plans check-todo check-workflow \
	test-unit test-contract test-property test-integration test test-cov \
	test-report verify-test-adapter

PYTHON ?= python3
FLEY_ORG ?= ../fley-org
TEST_PYTHON ?= $(if $(wildcard .venv/bin/pytest),.venv/bin/python,$(if $(wildcard .conda-test/bin/pytest),.conda-test/bin/python,$(PYTHON)))
TEST_PATHS = tests/unit tests/contract tests/property tests/integration

check-work: check-plans check-todo check-workflow

check-plans:
	@$(PYTHON) $(FLEY_ORG)/scripts/repo_tour.py --check-csv "$(CURDIR)/_work/plans/plans.csv"

check-todo:
	@$(PYTHON) $(FLEY_ORG)/scripts/repo_tour.py --check-csv "$(CURDIR)/_work/todo.csv"

check-workflow:
	@cmp -s "$(FLEY_ORG)/process/repo-workflow.md" _work/repo-workflow.md
	@echo "_work/repo-workflow.md: synced"

test-unit:
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) -m pytest tests/unit

test-contract:
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) -m pytest tests/contract

test-property:
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) -m pytest tests/property

test-integration:
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) -m pytest tests/integration

test:
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) -m pytest $(TEST_PATHS)

test-cov:
	@mkdir -p .test-results
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) -m pytest $(TEST_PATHS) --cov --cov-report=term-missing --cov-report=xml

test-report:
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) scripts/run_test_report.py $(TEST_PATHS)

verify-test-adapter:
	@PYTHONNOUSERSITE=1 $(TEST_PYTHON) scripts/verify_test_adapter.py
