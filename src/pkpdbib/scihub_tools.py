"""Retrieve the PDFs of DOIs via Sci-Hub.

The DOIs are read from a Zotero export in the Better BibTeX JSON format
(`Export Items...` -> `Better BibTeX JSON`), the PDFs are named by the citation
keys of the items.
"""

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from scidownl import scihub_download

from pkpdbib.console import console


def dois_from_json(json_path: Path) -> dict[str, str]:
    """Read the DOIs of a Better BibTeX JSON export of Zotero.

    Items without a DOI are skipped.

    Args:
        json_path: path of the Better BibTeX JSON file.

    Returns:
        The DOIs by the citation keys of the items.
    """
    data = json.loads(json_path.read_text(encoding="utf-8"))
    return {
        item["citationKey"]: item["DOI"]
        for item in data["items"]
        if item.get("DOI") and item.get("citationKey")
    }


def scihub_pdf_from_doi(
    doi: str, pdf_path: Path, scihub_url: str | None = None
) -> None:
    """Download the PDF of a DOI.

    Args:
        doi: DOI of the publication, e.g., `10.1145/3375633`.
        pdf_path: path the PDF is written to.
        scihub_url: Sci-Hub domain to use; by default the best available domain
            of scidownl, see `scidownl domain.update`.
    """
    scihub_download(
        keyword=doi,
        paper_type="doi",
        out=str(pdf_path),
        scihub_url=scihub_url,  # ty: ignore[invalid-argument-type]
    )


def scihub_pdfs_from_dois(
    dois: dict[str, str], pdf_dir: Path, scihub_url: str | None = None
) -> list[str]:
    """Download the PDFs of DOIs which are not in the directory yet.

    Args:
        dois: DOIs by the keys the PDFs are named after, `<key>.pdf`.
        pdf_dir: directory of the PDFs, created if it does not exist.
        scihub_url: Sci-Hub domain to use, see `scihub_pdf_from_doi`.

    Returns:
        The keys for which no PDF exists after the download.
    """
    pdf_dir.mkdir(exist_ok=True, parents=True)
    console.rule("PDFs from DOIs", style="white")
    missing: list[str] = []
    for k, (key, doi) in enumerate(dois.items()):
        pdf_path = pdf_dir / f"{key}.pdf"
        console.print()
        console.rule(
            f"[{k + 1}/{len(dois)}] {pdf_path} ({doi})",
            style="bold white",
            align="left",
        )
        if pdf_path.exists():
            continue
        scihub_pdf_from_doi(doi=doi, pdf_path=pdf_path, scihub_url=scihub_url)
        if not pdf_path.exists():
            missing.append(key)

    if missing:
        console.print(
            f"No PDF for {len(missing)}/{len(dois)} DOIs: {', '.join(missing)}",
            style="warning",
        )
    return missing


def scihub_pdfs(
    zotero_json_path: Path,
    pdf_dir: Path | None = None,
    scihub_url: str | None = None,
) -> list[str]:
    """Download the missing PDFs of a Better BibTeX JSON export of Zotero.

    Args:
        zotero_json_path: path of the Better BibTeX JSON file.
        pdf_dir: directory of the PDFs; by default the directory named after
            the JSON file next to it, i.e., `<substance>/` for `<substance>.json`.
        scihub_url: Sci-Hub domain to use, see `scihub_pdf_from_doi`.

    Returns:
        The citation keys for which no PDF exists after the download.
    """
    console.print(zotero_json_path)
    if pdf_dir is None:
        pdf_dir = zotero_json_path.parent / zotero_json_path.stem
    return scihub_pdfs_from_dois(
        dois=dois_from_json(json_path=zotero_json_path),
        pdf_dir=pdf_dir,
        scihub_url=scihub_url,
    )


def scihub_pdfs_command(argv: Sequence[str] | None = None) -> None:
    """Command line interface `scihub_pdfs`, see `scihub_pdfs`.

    Args:
        argv: command line arguments, by default `sys.argv[1:]`.
    """
    parser = argparse.ArgumentParser(
        prog="scihub_pdfs",
        description=(
            "Download the missing PDFs of a Better BibTeX JSON export of Zotero."
        ),
    )
    parser.add_argument(
        "--json",
        "-j",
        help="path of the Better BibTeX JSON file",
        dest="zotero_json_path",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "--out",
        "-o",
        help="directory of the PDFs, by default named after the JSON file",
        dest="pdf_dir",
        type=Path,
        default=None,
    )
    parser.add_argument(
        "--scihub-url",
        help="Sci-Hub domain to use, by default the best domain of scidownl",
        dest="scihub_url",
        default=None,
    )
    args = parser.parse_args(argv)
    scihub_pdfs(
        zotero_json_path=args.zotero_json_path,
        pdf_dir=args.pdf_dir,
        scihub_url=args.scihub_url,
    )


if __name__ == "__main__":
    scihub_pdfs_command()
