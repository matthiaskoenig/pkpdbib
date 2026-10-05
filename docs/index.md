# pkpdbib

![pkpdbib logo](images/favicon/pkpdbib-100x100-300dpi.png){ align=left width=100 }

`pkpdbib` is a collection of python utilities for working with pharmacokinetics/pharmacodynamics (PK/PD) literature and bibliographies. It supports the curation of the literature of [PK-DB](https://pk-db.com) and of the PK/PD models built on it.

Features include

- **[PDF retrieval](pdfs.md)** - the PDFs of the DOIs of a [Zotero](https://www.zotero.org) export (Better BibTeX JSON), via the `scihub_pdfs` command
- **[Zotero libraries](zotero.md)** - programmatic access to a Zotero library and a table of the tags of its items

The source code is available from [github.com/matthiaskoenig/pkpdbib](https://github.com/matthiaskoenig/pkpdbib). If you have any questions or issues please [open an issue](https://github.com/matthiaskoenig/pkpdbib/issues).

## Quickstart

```bash
pip install pkpdbib
scidownl domain.update
scihub_pdfs -j aliskiren.json
```

See [Installation](installation.md) and [PDF retrieval](pdfs.md) for the details.

## How to cite

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11076700.svg)](https://doi.org/10.5281/zenodo.11076700)

If you use `pkpdbib` please cite the archived software on [Zenodo](https://doi.org/10.5281/zenodo.11076700). The DOI always resolves to the latest version, the citation metadata is in [CITATION.cff](https://github.com/matthiaskoenig/pkpdbib/blob/develop/CITATION.cff).

## License

- Source code: [LGPLv3](https://opensource.org/licenses/LGPL-3.0)
- Documentation: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

## Funding

Matthias König is supported by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151 "QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach)" by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA).

Matthias König was supported by the Federal Ministry of Education and Research (BMBF, Germany) within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054) and within ATLAS by grant number 031L0304B.
