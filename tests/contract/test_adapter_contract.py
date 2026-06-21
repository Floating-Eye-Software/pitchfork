from pathlib import Path


REQUIRED_TARGETS = {
    "test-unit",
    "test-contract",
    "test-property",
    "test-integration",
    "test",
    "test-cov",
    "test-report",
}


def test_makefile_declares_stable_test_targets() -> None:
    makefile = Path("Makefile").read_text(encoding="utf-8")

    missing = {target for target in REQUIRED_TARGETS if f"{target}:" not in makefile}
    assert not missing


def test_pytest_uses_strict_configuration() -> None:
    configuration = Path("pyproject.toml").read_text(encoding="utf-8")

    assert '"--strict-config"' in configuration
    assert '"--strict-markers"' in configuration
    assert '"-W", "error"' in configuration
