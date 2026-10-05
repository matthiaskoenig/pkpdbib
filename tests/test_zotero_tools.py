"""Tests of the Zotero utilities, against a fake client without network."""

from typing import Any, cast

import polars as pl
import pytest
from pyzotero import zotero

from pkpdbib.zotero_tools import create_tag_table, get_items, pmid_from_extra


def item(key: str, tags: list[str], doi: str = "", extra: str = "") -> dict[str, Any]:
    """Create a Zotero item as returned by the API."""
    return {
        "key": key,
        "data": {"DOI": doi, "extra": extra, "tags": [{"tag": t} for t in tags]},
    }


class FakeZotero:
    """Fake client which returns the items in pages of two."""

    def __init__(self, items: list[dict[str, Any]]) -> None:
        """Create the fake library with the given items."""
        self.items = items

    def top(self, limit: int | None = None) -> list[dict[str, Any]]:
        """First page of the items."""
        return self.items[: limit or 2]

    def everything(self, first_page: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """All items, following the pages."""
        return first_page + self.items[len(first_page) :]


ITEMS = [
    item("A", ["pkdb", "species:human", "other"], doi="10.1/a", extra="PMID: 123"),
    item("B", ["data:timecourse", "species:rat"]),
    item("C", []),
]


def fake_client() -> zotero.Zotero:
    """Fake client with the items, typed as the client it replaces."""
    return cast("zotero.Zotero", FakeZotero(ITEMS))


def test_get_items_all() -> None:
    """Without a limit all pages are returned."""
    assert get_items(fake_client()) == ITEMS


def test_get_items_limit() -> None:
    """The limit restricts the number of items."""
    assert get_items(fake_client(), limit=1) == ITEMS[:1]


@pytest.mark.parametrize(
    ("extra", "pmid"),
    [
        ("PMID: 27267043 \nPMCID: PMC4895977", "27267043"),
        ("Place: Germany\nPMID: 18538111", "18538111"),
        ("PMCID: PMC4895977", None),
        ("", None),
        (None, None),
    ],
)
def test_pmid_from_extra(extra: str | None, pmid: str | None) -> None:
    """The PubMed id is read from its own line of the extra field."""
    assert pmid_from_extra(extra) == pmid


def test_create_tag_table() -> None:
    """Selected tags are boolean columns, other tags are ignored."""
    df = create_tag_table(ITEMS, tags_set={"pkdb"}, tag_prefixes=["species:", "data:"])

    assert df.columns == [
        "key",
        "doi",
        "pubmed",
        "pkdb",
        "species:human",
        "data:timecourse",
        "species:rat",
    ]
    assert df.schema["pkdb"] == pl.Boolean
    assert df["key"].to_list() == ["A", "B", "C"]
    assert df["doi"].to_list() == ["10.1/a", None, None]
    assert df["pubmed"].to_list() == ["123", None, None]
    assert df["species:human"].to_list() == [True, False, False]
    assert df["species:rat"].to_list() == [False, True, False]


def test_create_tag_table_empty() -> None:
    """A library without items gives an empty table."""
    df = create_tag_table([], tags_set=set(), tag_prefixes=[])
    assert df.columns == ["key", "doi", "pubmed"]
    assert df.height == 0
