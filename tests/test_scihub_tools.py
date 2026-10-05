"""Tests of the PDF retrieval via Sci-Hub.

The download is replaced by a fake, the tests do not access the network.
"""

from pathlib import Path

import pytest

from pkpdbib import scihub_tools
from pkpdbib.scihub_tools import (
    dois_from_json,
    scihub_pdfs,
    scihub_pdfs_command,
    scihub_pdfs_from_dois,
)


class FakeDownload:
    """Records the downloads and writes a PDF for the DOIs which are available."""

    def __init__(self, unavailable: set[str] | None = None) -> None:
        """Create the fake, the DOIs in `unavailable` give no PDF."""
        self.unavailable = unavailable or set()
        self.calls: list[dict[str, str | None]] = []

    def __call__(
        self,
        keyword: str,
        paper_type: str,
        out: str,
        scihub_url: str | None = None,
    ) -> None:
        """Download with the signature of `scidownl.scihub_download`."""
        self.calls.append(
            {
                "keyword": keyword,
                "paper_type": paper_type,
                "out": out,
                "url": scihub_url,
            }
        )
        if keyword not in self.unavailable:
            Path(out).write_bytes(b"%PDF-1.4")


@pytest.fixture
def fake_download(monkeypatch: pytest.MonkeyPatch) -> FakeDownload:
    """Replace the download of scidownl."""
    fake = FakeDownload(unavailable={"10.1124/dmd.106.013797"})
    monkeypatch.setattr(scihub_tools, "scihub_download", fake)
    return fake


def test_dois_from_json(betterbibtex_json: Path) -> None:
    """Items without a DOI are skipped."""
    dois = dois_from_json(betterbibtex_json)
    assert dois == {
        "limoges2008": "10.5414/cpp46252",
        "waldmeier2007": "10.1124/dmd.106.013797",
    }


def test_scihub_pdfs_from_dois(tmp_path: Path, fake_download: FakeDownload) -> None:
    """Existing PDFs are not downloaded again, missing PDFs are reported."""
    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    (pdf_dir / "existing.pdf").write_bytes(b"%PDF-1.4")
    dois = {
        "existing": "10.1/existing",
        "limoges2008": "10.5414/cpp46252",
        "waldmeier2007": "10.1124/dmd.106.013797",
    }

    missing = scihub_pdfs_from_dois(dois, pdf_dir=pdf_dir, scihub_url="https://x.y")

    assert missing == ["waldmeier2007"]
    assert [c["keyword"] for c in fake_download.calls] == [
        "10.5414/cpp46252",
        "10.1124/dmd.106.013797",
    ]
    assert all(c["paper_type"] == "doi" for c in fake_download.calls)
    assert all(c["url"] == "https://x.y" for c in fake_download.calls)
    assert (pdf_dir / "limoges2008.pdf").exists()


@pytest.mark.usefixtures("fake_download")
def test_scihub_pdfs(betterbibtex_json: Path) -> None:
    """The PDFs are written next to the JSON file into a directory of its name."""
    missing = scihub_pdfs(betterbibtex_json)
    assert missing == ["waldmeier2007"]
    assert (betterbibtex_json.parent / "aliskiren" / "limoges2008.pdf").exists()


def test_scihub_pdfs_command(
    betterbibtex_json: Path, tmp_path: Path, fake_download: FakeDownload
) -> None:
    """The command line interface passes the options on."""
    out = tmp_path / "out"
    scihub_pdfs_command(
        ["-j", str(betterbibtex_json), "-o", str(out), "--scihub-url", "https://x.y"]
    )
    assert (out / "limoges2008.pdf").exists()
    assert {c["url"] for c in fake_download.calls} == {"https://x.y"}


def test_scihub_pdfs_command_requires_json() -> None:
    """The JSON file is a required argument."""
    with pytest.raises(SystemExit):
        scihub_pdfs_command([])
