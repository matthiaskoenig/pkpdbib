# PDF retrieval

`pkpdbib.scihub_tools` downloads the PDFs of the DOIs of a [Zotero](https://www.zotero.org) export via [scidownl](https://github.com/Tishacy/SciDownl). The export uses the Better BibTeX JSON format of the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin, the PDFs are named by the citation keys of the items.

!!! warning
    Only download publications you are entitled to access. Check the copyright law of your country and the terms of your institution before using Sci-Hub.

## Export from Zotero

1. Open the Zotero library and select the items without a PDF attachment.
2. Right click -> `Export Items...` -> format `Better BibTeX JSON`.
3. Save the export as `<substance>.json`, e.g., `aliskiren.json`.

## Command line

Update the list of the available Sci-Hub domains once, then download the PDFs:

```bash
scidownl domain.update
scihub_pdfs -j aliskiren.json
```

The PDFs are written to the directory `aliskiren/` next to the JSON file, e.g., `aliskiren/limoges2008.pdf`. PDFs which exist already are not downloaded again, so the command can be repeated after a partial run. The DOIs for which no PDF could be retrieved are listed at the end.

| option | description |
| --- | --- |
| `-j`, `--json` | path of the Better BibTeX JSON file, required |
| `-o`, `--out` | directory of the PDFs, by default named after the JSON file |
| `--scihub-url` | Sci-Hub domain to use, by default the best domain of scidownl |

## Python

```python
from pathlib import Path

from pkpdbib.scihub_tools import dois_from_json, scihub_pdfs

# DOIs by citation key, items without DOI are skipped
dois = dois_from_json(Path("aliskiren.json"))

# download the missing PDFs, returns the keys without PDF
missing = scihub_pdfs(Path("aliskiren.json"))
```

See the [API reference](api/scihub_tools.md) for all functions.
