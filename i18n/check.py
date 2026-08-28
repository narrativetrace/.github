#!/usr/bin/env python3
"""Verify that every translation exists, matches the structure of its English
source, respects the glossary, and is not stale.

Usage:  python i18n/check.py [--root DIR] [--config i18n/config.json] [--no-stale]

Exit code 1 on any problem. Never modifies files.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18nlib import (  # noqa: E402
    check_glossary, check_preamble, compare_structure, load_json, parse_header,
    split_blocks, stale_blocks, state_path, translated_path,
)


def check_one(root: Path, source: str, lang: str, config: dict, glossary: dict, check_stale: bool) -> list[str]:
    src_path, tr_path = root / source, root / translated_path(source, lang)
    if not src_path.exists():
        return [f"source file {source} does not exist"]
    if not tr_path.exists():
        return [f"missing translation {translated_path(source, lang)}"]

    src_text, tr_text = src_path.read_text(encoding="utf-8"), tr_path.read_text(encoding="utf-8")
    src_blocks = split_blocks(src_text)
    header, tr_blocks = parse_header(split_blocks(tr_text))

    errors: list[str] = []
    if header is None:
        errors.append("missing header comment: <!-- i18n: source=... lang=... -->")
    elif header["source"] != source or header["lang"] != lang:
        errors.append(f"header says source={header['source']} lang={header['lang']}, expected source={source} lang={lang}")

    errors += check_preamble(tr_blocks, source, lang, config)
    errors += compare_structure(src_blocks, tr_blocks, list(config["languages"]))
    errors += check_glossary(src_text, tr_text, lang, glossary)

    if check_stale:
        sp = state_path(root, source, lang)
        if not sp.exists():
            errors.append(f"no state file {sp.relative_to(root)}; run i18n/stamp.py after translating")
        else:
            recorded = load_json(sp).get("blocks", [])
            stale = stale_blocks(src_blocks, recorded)
            if stale:
                errors.append(f"{len(stale)} of {len(src_blocks)} blocks stale (English changed since last stamp):")
                for idx in stale:
                    errors.append(f"    block {idx:>3}  [{src_blocks[idx].kind}] {src_blocks[idx].summary()}")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repository root")
    ap.add_argument("--config", default="i18n/config.json", help="config path relative to root")
    ap.add_argument("--glossary", default=None, help="glossary path relative to root (default: next to config)")
    ap.add_argument("--no-stale", action="store_true", help="skip staleness check (structure + glossary only)")
    ap.add_argument("files", nargs="*", help="limit to these source files")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    config = load_json(root / args.config)
    glossary = load_json(root / (args.glossary or str(Path(args.config).with_name("glossary.json"))))
    files = args.files or config["files"]

    failed = 0
    for source in files:
        for lang in config["languages"]:
            errors = check_one(root, source, lang, config, glossary, not args.no_stale)
            label = translated_path(source, lang)
            if errors:
                failed += 1
                print(f"FAIL  {label}")
                for e in errors:
                    print(f"      {e}")
            else:
                print(f"ok    {label}")
    total = len(files) * len(config["languages"])
    print(f"\n{total - failed}/{total} translations ok")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
