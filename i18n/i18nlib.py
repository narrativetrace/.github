"""Shared helpers for the NarrativeTrace documentation i18n tooling.

Stdlib only. Splits Markdown into blocks, compares the structure of a source
document with a translation, and tracks per-block staleness via a JSON sidecar
in ``i18n/state/``.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

HEADER_RE = re.compile(r"^<!--\s*i18n:\s*source=(?P<source>\S+)\s+lang=(?P<lang>\S+)\s*-->\s*$")
LINK_RE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s")
LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})")


@dataclass
class Block:
    kind: str  # heading | paragraph | list | table | quote | code | html
    text: str
    meta: str = ""  # heading level, list item count, table dims, ...

    def hash(self) -> str:
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()[:16]

    def signature(self) -> str:
        return f"{self.kind}:{self.meta}" if self.meta else self.kind

    def summary(self, width: int = 60) -> str:
        first = self.text.strip().splitlines()[0] if self.text.strip() else ""
        return first if len(first) <= width else first[: width - 1] + "…"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def translated_path(source: str, lang: str) -> str:
    p = Path(source)
    return str(p.with_name(f"{p.stem}.{lang}{p.suffix}"))


def state_path(root: Path, source: str, lang: str) -> Path:
    file_id = source.replace("/", "__").removesuffix(".md")
    return root / "i18n" / "state" / f"{file_id}.{lang}.json"


def split_blocks(text: str) -> list[Block]:
    lines = text.splitlines()
    blocks: list[Block] = []
    i, n = 0, len(lines)

    def flush(kind: str, buf: list[str], meta: str = "") -> None:
        if buf:
            blocks.append(Block(kind, "\n".join(buf), meta))

    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = FENCE_RE.match(line)
        if m:
            fence = m.group(1)
            buf = [line]
            i += 1
            while i < n and not lines[i].startswith(fence):
                buf.append(lines[i])
                i += 1
            if i < n:
                buf.append(lines[i])
                i += 1
            flush("code", buf)
            continue
        if line.startswith("<!--"):
            buf = [line]
            while "-->" not in buf[-1] and i + 1 < n:
                i += 1
                buf.append(lines[i])
            i += 1
            flush("html", buf)
            continue
        hm = HEADING_RE.match(line)
        if hm:
            blocks.append(Block("heading", line, str(len(hm.group(1)))))
            i += 1
            continue
        if line.lstrip().startswith("|"):
            buf = []
            while i < n and lines[i].lstrip().startswith("|"):
                buf.append(lines[i])
                i += 1
            rows = [r for r in buf if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
            cols = buf[0].strip().strip("|").count("|") + 1
            flush("table", buf, f"{len(rows)}x{cols}")
            continue
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i])
                i += 1
            flush("quote", buf)
            continue
        if LIST_RE.match(line):
            buf = []
            items = 0
            while i < n and lines[i].strip() and (LIST_RE.match(lines[i]) or lines[i].startswith((" ", "\t"))):
                if LIST_RE.match(lines[i]) and not lines[i].startswith((" ", "\t")):
                    items += 1
                buf.append(lines[i])
                i += 1
            flush("list", buf, str(items))
            continue
        buf = []
        while i < n and lines[i].strip() and not HEADING_RE.match(lines[i]) and not FENCE_RE.match(lines[i]) \
                and not lines[i].startswith((">", "<!--")) and not lines[i].lstrip().startswith("|") \
                and not LIST_RE.match(lines[i]):
            buf.append(lines[i])
            i += 1
        flush("paragraph", buf)
    return blocks


def parse_header(blocks: list[Block]) -> tuple[dict | None, list[Block]]:
    """Return (header dict or None, blocks without the i18n header comment)."""
    if blocks and blocks[0].kind == "html":
        m = HEADER_RE.match(blocks[0].text.strip())
        if m:
            return m.groupdict(), blocks[1:]
    return None, blocks


def links(text: str) -> list[str]:
    return LINK_RE.findall(text)


def normalize_link(url: str, langs: list[str]) -> str:
    """Strip a language suffix from relative markdown links: SECURITY.es.md -> SECURITY.md."""
    if "://" in url or url.startswith(("mailto:", "#")):
        return url
    for lang in langs:
        url = re.sub(rf"\.{re.escape(lang)}\.md(#.*)?$", r".md\1", url)
    return url


def compare_structure(src: list[Block], tr: list[Block], langs: list[str]) -> list[str]:
    errors: list[str] = []
    if len(src) != len(tr):
        errors.append(f"block count differs: source has {len(src)}, translation has {len(tr)}")
    for idx, (a, b) in enumerate(zip(src, tr)):
        if a.signature() != b.signature():
            errors.append(f"block {idx} ({a.summary()!r}): expected {a.signature()}, got {b.signature()}")
            continue
        if a.kind == "code" and a.text != b.text:
            errors.append(f"block {idx}: code block was modified; code blocks must be byte-identical")
        if idx == 0 and a.kind == "quote":
            continue  # language switcher: validated by check_preamble, links legitimately differ
        la = sorted(normalize_link(u, langs) for u in links(a.text))
        lb = sorted(normalize_link(u, langs) for u in links(b.text))
        if la != lb:
            errors.append(f"block {idx} ({a.summary()!r}): links differ\n    source:      {la}\n    translation: {lb}")
    if len(src) > len(tr):
        for idx in range(len(tr), len(src)):
            errors.append(f"block {idx} ({src[idx].summary()!r}) missing from translation")
    elif len(tr) > len(src):
        for idx in range(len(src), len(tr)):
            errors.append(f"block {idx} ({tr[idx].summary()!r}) has no counterpart in source")
    return errors


def check_glossary(src_text: str, tr_text: str, lang: str, glossary: dict) -> list[str]:
    errors: list[str] = []
    for term in glossary.get("keep", []):
        a, b = src_text.count(term), tr_text.count(term)
        if a != b:
            errors.append(f"glossary term {term!r} appears {a}x in source but {b}x in translation")
    for term, targets in glossary.get("translate", {}).items():
        canonical = targets.get(lang)
        if canonical and re.search(rf"\b{re.escape(term)}\b", src_text, re.IGNORECASE) \
                and canonical.lower() not in tr_text.lower():
            errors.append(f"source uses {term!r} but translation never uses canonical {canonical!r}")
    return errors


def check_preamble(tr_blocks: list[Block], source: str, lang: str, config: dict) -> list[str]:
    """Translations must start with a blockquote linking back to the English source."""
    errors: list[str] = []
    if not tr_blocks or tr_blocks[0].kind != "quote":
        errors.append("translation must start with the language switcher blockquote")
        return errors
    quote_links = [normalize_link(u, list(config["languages"])) for u in links(tr_blocks[0].text)]
    if Path(source).name not in [Path(u).name for u in quote_links]:
        errors.append(f"language switcher must link back to the English source {Path(source).name}")
    return errors


def block_hashes(blocks: list[Block]) -> list[str]:
    return [b.hash() for b in blocks]


def stale_blocks(src: list[Block], recorded: list[str]) -> list[int]:
    current = block_hashes(src)
    if len(current) != len(recorded):
        return list(range(len(current)))
    return [i for i, (a, b) in enumerate(zip(current, recorded)) if a != b]
