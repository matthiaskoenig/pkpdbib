"""Programmatic access to Zotero libraries.

- documentation of pyzotero: https://pyzotero.readthedocs.io
- API key: https://www.zotero.org/settings/keys/new
- group id: open the page of the group via https://www.zotero.org/groups and
  hover over the link to the group settings, the id is the integer after
  `/groups/`.
"""

import re
from collections.abc import Iterable
from typing import Any

import polars as pl
from pyzotero import zotero

from pkpdbib.console import console

PMID_PATTERN = re.compile(r"^PMID:\s*(\d+)\s*$", re.MULTILINE)


def create_zot_client(
    api_key: str, library_id: int, library_type: str = "group"
) -> zotero.Zotero:
    """Create a Zotero client bound to a library.

    The item methods of the client only operate on this library.

    Args:
        api_key: Zotero API key with read access to the library.
        library_id: id of the user or group library.
        library_type: `group` or `user`.

    Returns:
        The client.
    """
    return zotero.Zotero(library_id, library_type, api_key)


def get_items(
    zot: zotero.Zotero, show: bool = False, limit: int | None = None
) -> list[dict[str, Any]]:
    """Get the top level items of the library.

    Args:
        zot: client of the library, see `create_zot_client`.
        show: print the items to the console.
        limit: maximal number of items; all items if `None`.

    Returns:
        The items as returned by the Zotero API.
    """
    # the API returns the items in pages, `everything` follows all pages
    items: list[dict[str, Any]] = (
        zot.top(limit=limit) if limit else zot.everything(zot.top())
    )

    if show:
        for k, item in enumerate(items):
            console.rule(title=f"Item {k + 1}", align="left", style="white")
            console.print(item)
    return items


def pmid_from_extra(extra: str | None) -> str | None:
    """Get the PubMed id from the `extra` field of a Zotero item.

    Args:
        extra: `extra` field with one `key: value` per line, e.g.,
            `PMID: 27267043` and `PMCID: PMC4895977`.

    Returns:
        The PubMed id or `None`.
    """
    if not extra:
        return None
    match = PMID_PATTERN.search(extra)
    return match.group(1) if match else None


def create_tag_table(
    items: Iterable[dict[str, Any]],
    tags_set: Iterable[str],
    tag_prefixes: Iterable[str],
) -> pl.DataFrame:
    """Create a table of the items with the selected tags.

    A tag is selected if it is in `tags_set` or starts with one of the
    `tag_prefixes`. Every selected tag is a boolean column, which is `True` for
    the items with the tag.

    Args:
        items: items of a library, see `get_items`.
        tags_set: tags to select.
        tag_prefixes: prefixes of the tags to select, e.g., `"species:"`.

    Returns:
        The table with the columns `key`, `doi`, `pubmed` and one column per
        selected tag.
    """
    tags_set = set(tags_set)
    tag_prefixes = tuple(tag_prefixes)

    rows: list[dict[str, Any]] = []
    tag_columns: dict[str, None] = {}
    for item in items:
        data = item["data"]
        row: dict[str, Any] = {
            "key": item["key"],
            "doi": data.get("DOI") or None,
            "pubmed": pmid_from_extra(data.get("extra")),
        }
        for tag in (t["tag"] for t in data.get("tags", [])):
            if tag in tags_set or tag.startswith(tag_prefixes):
                row[tag] = True
                tag_columns[tag] = None
        rows.append(row)

    schema: dict[str, Any] = {"key": pl.String, "doi": pl.String, "pubmed": pl.String}
    schema.update(dict.fromkeys(tag_columns, pl.Boolean))
    df = pl.DataFrame(rows, schema=schema).with_columns(
        pl.col(list(tag_columns)).fill_null(False)
    )
    console.print(df)
    return df
