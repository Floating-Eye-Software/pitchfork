.PHONY: check-work check-plans check-todo check-workflow

PYTHON ?= python3
FLEY_ORG ?= ../fley-org

check-work: check-plans check-todo check-workflow

check-plans:
	@$(PYTHON) $(FLEY_ORG)/scripts/repo_tour.py --check-csv "$(CURDIR)/_work/plans/plans.csv"

check-todo:
	@$(PYTHON) $(FLEY_ORG)/scripts/repo_tour.py --check-csv "$(CURDIR)/_work/todo.csv"

check-workflow:
	@cmp -s "$(FLEY_ORG)/process/repo-workflow.md" _work/repo-workflow.md
	@echo "_work/repo-workflow.md: synced"
