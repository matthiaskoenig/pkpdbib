"""Table of the tags of a Zotero group library.

Needs a Zotero API key with read access to the
library in the environment variable `ZOTERO_API_KEY`:

```bash
ZOTERO_API_KEY=<key> uv run python examples/zotero_tags.py
```
"""

import os

from pkpdbib.zotero_tools import create_tag_table, create_zot_client, get_items

# group library of the glucose literature
LIBRARY_ID: int = 4979949

CUSTOM_TAGS: set[str] = {
    "has_simulation",
    "pkdb",
}
CUSTOM_TAG_PREFIXES: list[str] = [
    "data:",
    "group:",
    "species:",
    "timecourse:",
]


if __name__ == "__main__":
    zot = create_zot_client(
        api_key=os.environ["ZOTERO_API_KEY"],
        library_id=LIBRARY_ID,
        library_type="group",
    )
    items = get_items(zot)
    df = create_tag_table(items, tags_set=CUSTOM_TAGS, tag_prefixes=CUSTOM_TAG_PREFIXES)
    df.write_csv("zotero_tags.csv")
