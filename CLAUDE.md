# CLAUDE.md

This file provides guidance when working with code in this repository.

## Project

`pkpdbib` is a python library for PK/PD literature and bibliography management:
retrieval of the PDFs of the DOIs of a Zotero export (Better BibTeX JSON) via
scidownl (`pkpdbib.scihub_tools`, CLI `scihub_pdfs`) and access to Zotero
libraries via pyzotero with tag tables in polars (`pkpdbib.zotero_tools`).
Requires python >= 3.13, packaged with hatchling (version is read from
`src/pkpdbib/__init__.py`). Runtime dependencies are `rich`, `scidownl`,
`pyzotero` and `polars`. Keep the footprint small: no new runtime dependency
without need, no pandas. MIT licensed.

The README is a short entry point (description, installation, citation,
license); the content lives in the documentation in `docs/`.

## Commands

```bash
# environment (uv based, uv.lock is committed)
uv sync --extra dev
uv run pre-commit install

# tests (no network, downloads and the zotero client are faked)
pytest
tox r -e py3.15                 # single tox env (py3.13-3.15, lowest)
tox run-parallel                # full matrix + ty + lowest

# lint / format / types
ruff check
ruff format
tox -e ty                       # config in [tool.ty] in pyproject.toml

# documentation (zensical, mkdocstrings), built into the gitignored site/
uv run zensical build --clean
uv run python scripts/llms_txt.py
```

`develop` is the default branch and takes every change through a pull request,
see the rulesets in `.github/rulesets/` and `docs/development.md`, which also
describes the release (`uvx bump-my-version bump ...`, tag on `develop`).
Never commit API keys; examples read them from the environment.
