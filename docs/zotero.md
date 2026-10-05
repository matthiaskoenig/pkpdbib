# Zotero libraries

`pkpdbib.zotero_tools` provides programmatic access to [Zotero](https://www.zotero.org) libraries via [pyzotero](https://pyzotero.readthedocs.io) and creates tables of the tags of their items with [polars](https://pola.rs). It needs the optional `zotero` extra:

```bash
pip install "pkpdbib[zotero]"
```

## Access

Access needs an API key with read access to the library, created at [zotero.org/settings/keys/new](https://www.zotero.org/settings/keys/new). The id of a group library is found by opening the page of the group via [zotero.org/groups](https://www.zotero.org/groups) and hovering over the link to the group settings, it is the integer after `/groups/`.

Keep the API key out of the source code, e.g., in an environment variable:

```python
import os

from pkpdbib.zotero_tools import create_zot_client, get_items

zot = create_zot_client(
    api_key=os.environ["ZOTERO_API_KEY"],
    library_id=4979949,
    library_type="group",
)
items = get_items(zot)  # all top level items
```

## Tag tables

The curation of a library is recorded in the tags of its items, e.g., `pkdb` for items curated in [PK-DB](https://pk-db.com) or `species:human`. `create_tag_table` creates a table with one row per item and one boolean column per selected tag, in addition to the DOI and the PubMed id of the item:

```python
from pkpdbib.zotero_tools import create_tag_table

df = create_tag_table(
    items,
    tags_set={"pkdb", "has_simulation"},
    tag_prefixes=["species:", "data:"],
)
df.write_csv("tags.csv")
```

A complete example is [`examples/zotero_tags.py`](https://github.com/matthiaskoenig/pkpdbib/blob/develop/examples/zotero_tags.py). See the [API reference](api/zotero_tools.md) for all functions.
