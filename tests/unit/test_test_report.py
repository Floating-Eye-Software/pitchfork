from scripts.run_test_report import build_metadata


def test_report_metadata_identifies_execution_environment() -> None:
    metadata = build_metadata(["python", "-m", "pytest"], "start", 0)

    assert metadata["schema_version"] == 1
    assert metadata["command"] == ["python", "-m", "pytest"]
    assert metadata["started_at"] == "start"
    assert metadata["exit_status"] == 0
    assert metadata["python"]
    assert metadata["platform"]
    assert metadata["tools"]["pytest"] != "unavailable"
    assert metadata["repository"]["revision"] != "unavailable"
