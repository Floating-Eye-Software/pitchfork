from hypothesis import given
from hypothesis import strategies as st

from scripts.run_test_report import build_metadata


@given(exit_status=st.integers(min_value=0, max_value=255))
def test_report_metadata_preserves_every_process_status(exit_status: int) -> None:
    metadata = build_metadata(["pytest"], "start", exit_status)

    assert metadata["exit_status"] == exit_status
