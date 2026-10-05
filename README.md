![pkpdbib logo](https://github.com/matthiaskoenig/pkpdbib/raw/develop/docs/images/favicon/pkpdbib-100x100-300dpi.png)

# pkpdbib: python utilities for PK/PD literature
[![GitHub Actions CI/CD Status](https://github.com/matthiaskoenig/pkpdbib/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/matthiaskoenig/pkpdbib/actions/workflows/ci-cd.yml)
[![Documentation](https://img.shields.io/badge/docs-pkpdbib-008080.svg)](https://matthiaskoenig.github.io/pkpdbib)
[![Version](https://img.shields.io/pypi/v/pkpdbib.svg)](https://pypi.org/project/pkpdbib/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pkpdbib.svg)](https://pypi.org/project/pkpdbib/)
[![LGPLv3 License](https://img.shields.io/pypi/l/pkpdbib.svg)](https://opensource.org/licenses/LGPL-3.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11076700.svg)](https://doi.org/10.5281/zenodo.11076700)

`pkpdbib` is a collection of python utilities for working with pharmacokinetics/pharmacodynamics (PK/PD) literature and bibliographies.

Features include

- **PDF retrieval** - the PDFs of the DOIs of a [Zotero](https://www.zotero.org) export (Better BibTeX JSON) via the `scihub_pdfs` command
- **Zotero libraries** - programmatic access to a Zotero library and a table of the tags of its items (optional `zotero` extra)

The documentation is available at [https://matthiaskoenig.github.io/pkpdbib](https://matthiaskoenig.github.io/pkpdbib).

If you have any questions or issues please [open an issue](https://github.com/matthiaskoenig/pkpdbib/issues).

## Installation
`pkpdbib` is available from [pypi](https://pypi.org/project/pkpdbib/) and can be installed via

```bash
pip install pkpdbib
```

The Zotero utilities need the optional `zotero` extra:

```bash
pip install "pkpdbib[zotero]"
```

See the [installation guide](https://matthiaskoenig.github.io/pkpdbib/installation/) for the develop version and the [development guide](https://matthiaskoenig.github.io/pkpdbib/development/) for setting up a development environment.

## Quickstart
Open the Zotero library, select the items without a PDF attachment and export them via right click -> `Export items...` -> `Better BibTeX JSON` to `<substance>.json`. Then run

```bash
scidownl domain.update
scihub_pdfs -j <substance>.json
```

The PDFs are written to the directory `<substance>/` next to the JSON file, named by the citation keys.

## How to cite
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11076700.svg)](https://doi.org/10.5281/zenodo.11076700)

If you use `pkpdbib` please cite the archived software on [Zenodo](https://doi.org/10.5281/zenodo.11076700), see also [CITATION.cff](CITATION.cff):

> König, M. (2024). *pkpdbib: python utilities for PK/PD literature and bibliography management* (Version 0.1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.11076700

```bibtex
@software{konig_pkpdbib,
  author    = {König, Matthias},
  title     = {pkpdbib: python utilities for PK/PD literature and bibliography management},
  year      = {2024},
  version   = {0.1.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.11076700},
  url       = {https://doi.org/10.5281/zenodo.11076700},
}
```

## License
- Source Code: [LGPLv3](https://opensource.org/licenses/LGPL-3.0)
- Documentation: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

## Funding
Matthias König is supported by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151 "QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach)" by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA).

Matthias König was supported by the Federal Ministry of Education and Research (BMBF, Germany) within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054) and within ATLAS by grant number 031L0304B.

© 2021-2026 Matthias König, [https://livermetabolism.com](https://livermetabolism.com)
