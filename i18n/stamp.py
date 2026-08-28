#!/usr/bin/env python3
"""Record the current English block hashes for a translation, marking it up to date.

Run locally after translating. Refuses to stamp a translation that fails the
structural or glossary checks, so a broken translation can never be marked fresh.

Usage:  python i18n/stamp.py [--root DIR] [--lang LANG ...] [FILE ...]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check import check_one  # noqa: E402
from i18nlib import block_hashes, load_json, split_blocks, state_path, translated_path  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--config", default="i18n/config.json")
    ap.add_argument("--lang", action="append", help="only these languages (default: all)")
    ap.add_argument("files", nargs="*", help="source files to stamp (default: all)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    config = load_json(root / args.config)
    glossary = load_json(root / str(Path(args.config).with_name("glossary.json")))
    files = args.files or config["files"]
    langs = args.lang or list(config["languages"])

    failed = 0
    for source in files:
        src_text = (root / source).read_text(encoding="utf-8")
        blocks = split_blocks(src_text)
        for lang in langs:
            errors = check_one(root, source, lang, config, glossary, check_stale=False)
            label = translated_path(source, lang)
            if errors:
                failed += 1
                print(f"REFUSED  {label}")
                for e in errors:
                    print(f"         {e}")
                continue
            sp = state_path(root, source, lang)
            sp.parent.mkdir(parents=True, exist_ok=True)
            sp.write_text(json.dumps({
                "source": source,
                "lang": lang,
                "source_sha256": hashlib.sha256(src_text.encode("utf-8")).hexdigest(),
                "blocks": block_hashes(blocks),
            }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"stamped  {label}  ({len(blocks)} blocks)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
