import os
import socket
import subprocess
import sys
from pathlib import Path

import pytest


def test_empty_temporary_suite_is_rejected(tmp_path: Path) -> None:
    environment = os.environ.copy()
    environment.pop("PYTEST_ADDOPTS", None)
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(tmp_path)],
        check=False,
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 5


def test_default_suite_prohibits_network() -> None:
    with pytest.raises(RuntimeError, match="network access is prohibited"):
        socket.create_connection(("example.com", 80))
