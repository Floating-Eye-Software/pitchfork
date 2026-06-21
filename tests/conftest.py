"""Shared deterministic and isolated configuration for Pitchfork tests."""

import socket

import pytest
from hypothesis import settings

settings.register_profile(
    "pitchfork",
    deadline=None,
    print_blob=True,
)
settings.load_profile("pitchfork")


@pytest.fixture(autouse=True)
def prohibit_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make undeclared network use fail immediately in the default suites."""

    def blocked(*args: object, **kwargs: object) -> None:
        raise RuntimeError("network access is prohibited in Pitchfork's local test gate")

    monkeypatch.setattr(socket, "create_connection", blocked)
    monkeypatch.setattr(socket.socket, "connect", blocked)
    monkeypatch.setattr(socket.socket, "connect_ex", blocked)
