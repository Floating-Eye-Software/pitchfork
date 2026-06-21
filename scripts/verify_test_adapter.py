"""Exercise the Pitchfork adapter's FLEY testing-process contract."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
SUITES = ("unit", "contract", "property", "integration")
TEST_PATHS = tuple(f"tests/{suite}" for suite in SUITES)
COLLECTED = re.compile(r"^tests/.+::.+$")


def run(command: list[str], *, expected: set[int] = {0}) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["PYTHONNOUSERSITE"] = "1"
    environment.pop("PYTEST_ADDOPTS", None)
    result = subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode not in expected:
        detail = "\n".join(part for part in (result.stdout, result.stderr) if part)
        raise RuntimeError(
            f"expected exit {sorted(expected)}, got {result.returncode}: {' '.join(command)}\n{detail}"
        )
    return result


def collect(paths: tuple[str, ...]) -> set[str]:
    result = run([sys.executable, "-m", "pytest", *paths, "--collect-only", "-q"])
    selected = {line for line in result.stdout.splitlines() if COLLECTED.match(line)}
    if not selected:
        raise RuntimeError(f"required selection is empty: {' '.join(paths)}")
    return selected


def file_digest(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def repository_state() -> str:
    return run(["git", "status", "--porcelain", "--untracked-files=all"]).stdout


def verify_temporary_failures() -> None:
    with tempfile.TemporaryDirectory(prefix="pitchfork-adapter-") as directory:
        temporary = Path(directory)
        failing = temporary / "test_failing_sentinel.py"
        failing.write_text("def test_failing_sentinel():\n    assert False\n", encoding="utf-8")
        run([sys.executable, "-m", "pytest", str(failing)], expected={1})
        run(
            [sys.executable, "scripts/run_test_report.py", str(failing)],
            expected={1},
        )
        failure_metadata = json.loads(
            (ROOT / ".test-results" / "execution.json").read_text(encoding="utf-8")
        )
        if failure_metadata["exit_status"] != 1:
            raise RuntimeError("test-report did not retain its failing exit status")

        unknown_marker = temporary / "test_unknown_marker.py"
        unknown_marker.write_text(
            "import pytest\n@pytest.mark.misspelled\ndef test_marker():\n    pass\n",
            encoding="utf-8",
        )
        run(
            [sys.executable, "-m", "pytest", str(unknown_marker), "--strict-markers"],
            expected={2},
        )

        empty = temporary / "empty"
        empty.mkdir()
        run([sys.executable, "-m", "pytest", str(empty)], expected={5})

        invalid_config = temporary / "pytest.ini"
        invalid_config.write_text("[pytest]\nunknown_pitchfork_option = true\n", encoding="utf-8")
        run(
            [
                sys.executable,
                "-m",
                "pytest",
                "--collect-only",
                "--strict-config",
                "-c",
                str(invalid_config),
                str(failing),
            ],
            expected={4},
        )


def verify_reporting(expected_count: int) -> None:
    coverage = run(["make", "test-cov", f"TEST_PYTHON={sys.executable}"])
    if f"collected {expected_count} items" not in coverage.stdout:
        raise RuntimeError("coverage did not preserve the aggregate selection")

    run(["make", "test-report", f"TEST_PYTHON={sys.executable}"])
    junit = ElementTree.parse(ROOT / ".test-results" / "junit.xml").getroot()
    reported = sum(int(suite.attrib["tests"]) for suite in junit.iter("testsuite"))
    if reported != expected_count:
        raise RuntimeError(
            f"report selected {reported} tests; aggregate selected {expected_count}"
        )
    if not (ROOT / ".test-results" / "execution.json").is_file():
        raise RuntimeError("test-report did not produce execution metadata")


def main() -> int:
    before_status = repository_state()
    database = ROOT / "pitchfork.db"
    before_database = file_digest(database)

    narrow = {suite: collect((f"tests/{suite}",)) for suite in SUITES}
    aggregate = collect(TEST_PATHS)
    narrow_union = set().union(*narrow.values())
    if aggregate != narrow_union:
        raise RuntimeError("aggregate selection differs from the union of narrow suites")

    run(["make", "test", f"TEST_PYTHON={sys.executable}"])
    run(["make", "test", f"TEST_PYTHON={sys.executable}"])
    verify_temporary_failures()
    verify_reporting(len(aggregate))

    if file_digest(database) != before_database:
        raise RuntimeError("adapter verification modified pitchfork.db")
    if repository_state() != before_status:
        raise RuntimeError("adapter verification changed repository source state")

    print(f"adapter conformance passed: {len(aggregate)} tests across {len(SUITES)} suites")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
