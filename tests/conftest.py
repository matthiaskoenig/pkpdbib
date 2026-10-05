"""Shared fixtures of the tests."""

from pathlib import Path

import pytest

DATA_DIR: Path = Path(__file__).parent / "data"


@pytest.fixture
def betterbibtex_json(tmp_path: Path) -> Path:
    """Copy of the Better BibTeX JSON export in a temporary directory."""
    path = tmp_path / "aliskiren.json"
    path.write_bytes((DATA_DIR / "betterbibtex.json").read_bytes())
    return path
