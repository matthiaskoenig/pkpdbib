# Installation

`pkpdbib` requires python >= 3.13 and is available from [pypi](https://pypi.org/project/pkpdbib/). It is tested on Linux, macOS and Windows.

## With uv

[uv](https://docs.astral.sh/uv/) is the recommended way to install the package. In a project it is added as a dependency:

```bash
uv add pkpdbib
```

The `scihub_pdfs` command can also be used without installing the package into an environment:

```bash
uvx --from pkpdbib scihub_pdfs -j aliskiren.json
```

## With pip

```bash
pip install pkpdbib
```

## Extras

The core package only depends on `rich` and `scidownl`. The [Zotero utilities](zotero.md) need the optional `zotero` extra, which adds `pyzotero` and `polars`:

```bash
pip install "pkpdbib[zotero]"
```

Without the extra, the import of `pkpdbib.zotero_tools` fails with a message naming the extra.

## Development version

The current state of the `develop` branch is installed directly from GitHub:

```bash
uv add "pkpdbib @ git+https://github.com/matthiaskoenig/pkpdbib.git@develop"
```

or, with pip,

```bash
pip install git+https://github.com/matthiaskoenig/pkpdbib.git@develop
```

To work on the repository itself, with the test and documentation tooling, see [Development](development.md).
