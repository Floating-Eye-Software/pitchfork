"""Run the aggregate pytest selection and retain engineering diagnostics."""

from __future__ import annotations

import importlib.metadata
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RESULTS_DIR = Path(".test-results")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else "unavailable"


def _version(distribution: str) -> str:
    try:
        return importlib.metadata.version(distribution)
    except importlib.metadata.PackageNotFoundError:
        return "unavailable"


def build_metadata(command: list[str], started_at: str, exit_status: int) -> dict[str, object]:
    return {
        "schema_version": 1,
        "command": command,
        "started_at": started_at,
        "ended_at": _now(),
        "exit_status": exit_status,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "tools": {
            "coverage": _version("coverage"),
            "hypothesis": _version("hypothesis"),
            "pytest": _version("pytest"),
            "pytest-cov": _version("pytest-cov"),
        },
        "repository": {
            "revision": _git("rev-parse", "HEAD"),
            "dirty": bool(_git("status", "--short", "--untracked-files=no")),
        },
    }


def main(arguments: list[str]) -> int:
    if not arguments:
        print("no test paths supplied", file=sys.stderr)
        return 2

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        "-m",
        "pytest",
        *arguments,
        f"--junitxml={RESULTS_DIR / 'junit.xml'}",
    ]
    started_at = _now()
    result = subprocess.run(command, check=False)
    metadata = build_metadata(command, started_at, result.returncode)
    (RESULTS_DIR / "execution.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
