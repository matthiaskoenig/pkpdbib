"""Retrieve PDFs based on dois."""

import argparse
from pathlib import Path
from typing import Optional

from scidownl import scihub_download
from pkpdbib.console import console



def dois_from_json(json_path: Path) -> dict[str, str]:
    """Create DOI dict from JSON file.

    JSON file is enerated in zotero 7 with better bibtex via Export Items
    -> BetterBibTeX JSON.
    """
    import json

    dois: dict[str, str] = {}
    with open(json_path, 'r') as file:
        data = json.load(file)
        for item in data["items"]:
            if "DOI" in item:
                dois[item["citationKey"]] = item["DOI"]

    return dois


def scihub_pdf_from_doi(
    doi: str, pdf_path: Path, scihub_url: Optional[str] = None
) -> None:
    """Download PDF from doi."""
    scihub_download(
        keyword=doi, paper_type="doi", out=str(pdf_path), scihub_url=scihub_url
    )


def scihub_pdfs_from_dois(
    dois: dict[str, str], pdf_dir: Path, scihub_url: Optional[str] = None
) -> None:
    """Download PDFs from DOIS."""
    pdf_dir.mkdir(exist_ok=True, parents=True)
    console.rule("PDFs from dois", style="white")
    num_dois = len(dois)
    for k, key in enumerate(dois):
        doi = dois[key]
        pdf_path = pdf_dir / f"{key}.pdf"
        console.print(f"[{k+1}/{num_dois}] {pdf_path} ({doi}")
        if pdf_path.exists():
            continue
        scihub_pdf_from_doi(doi=doi, pdf_path=pdf_path, scihub_url=scihub_url)


def scihub_pdfs(zotero_json_path: Path, scihub_url: Optional[str] = None) -> None:
    """Download missing pdfs for substance."""
    console.print(zotero_json_path)
    dois: dict[str, str] = dois_from_json(json_path=zotero_json_path)

    scihub_pdfs_from_dois(
        dois=dois,
        pdf_dir=zotero_json_path.parent / zotero_json_path.stem,
        scihub_url=scihub_url,
    )


def scihub_pdfs_command() -> None:
    """Download missing pdfs for substance."""
    parser = argparse.ArgumentParser(description="Retrieve PDFs for substance")
    parser.add_argument(
        "--json",
        "-j",
        help="zotero JSON path",
        dest="zotero_json_path",
        type=str,
        required=True,
    )
    parser.set_defaults(func=scihub_pdfs)
    args: argparse.Namespace = parser.parse_args()
    zotero_json_path = Path(args.zotero_json_path)
    args.func(zotero_json_path=zotero_json_path)


if __name__ == "__main__":
    scihub_pdfs_command()
