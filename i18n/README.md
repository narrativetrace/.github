# Documentation translations

English is the source of truth. Every other language is a derived file that is
checked in CI for structure, glossary use, and staleness. Nothing in CI generates
text; translations are produced locally.

| Source | Translations |
|---|---|
| `profile/README.md` | `profile/README.<lang>.md` |
| `SECURITY.md` | `SECURITY.<lang>.md` |
| `CONTRIBUTING.md` | `CONTRIBUTING.<lang>.md` |

Languages and files are listed in `config.json`; terms that must stay verbatim
or use a canonical translation are in `glossary.json`.

## When you change an English file

```sh
python3 i18n/check.py            # tells you which blocks of which translations are stale
# ... update the affected paragraphs in each translation ...
python3 i18n/stamp.py SECURITY.md   # re-verifies structure, then marks translations current
git add -A && git commit -s
```

`stamp.py` refuses to mark a translation current if its structure or glossary
check fails, so a broken translation can never turn CI green.

## Translation file format

```markdown
<!-- i18n: source=SECURITY.md lang=es -->
> 🌐 [English](SECURITY.md) · [简体中文](SECURITY.zh-CN.md) · Español · [Português](SECURITY.pt-BR.md) · [Français](SECURITY.fr.md)
>
> _Esta traducción se ofrece por conveniencia. La versión en inglés es la autoritativa._

# Política de seguridad
...
```

Rules enforced by `check.py`:

- same sequence of blocks (headings with the same level, lists with the same
  number of items, tables with the same dimensions, paragraphs, quotes, code);
- code blocks byte-identical to the source;
- same links, except that relative links may point to the localized sibling
  (`SECURITY.md` → `SECURITY.es.md`);
- `keep` glossary terms appear exactly as often as in the source;
- if the source uses a `translate` glossary term, the translation uses its
  canonical form;
- the first block is the language switcher, linking back to the English file.

## Staleness tracking

`state/<file>.<lang>.json` records a hash of every block of the English source
at the time the translation was last stamped. `check.py` compares those with
the current source and reports exactly which blocks changed, so only those
paragraphs need retranslating.
