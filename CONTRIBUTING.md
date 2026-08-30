> 🌐 English · [简体中文](CONTRIBUTING.zh-CN.md) · [Español](CONTRIBUTING.es.md) · [Português](CONTRIBUTING.pt-BR.md) · [Français](CONTRIBUTING.fr.md)

# Contributing to NarrativeTrace

Thanks for your interest in NarrativeTrace. This document applies to every repository
in the [narrativetrace](https://github.com/narrativetrace) organization. Each library
repository has its own `CONTRIBUTING.md` (or `README.md`) with build and test
instructions for that runtime.

## What we accept

- **Small pull requests are welcome** — bug fixes, documentation fixes, test
  improvements, small self-contained enhancements.
- **Larger changes: open a discussion first.** Before investing significant effort,
  open a GitHub Discussion (or an issue) in the relevant repository describing the
  problem and your proposed approach. This avoids wasted work if the change does not
  fit the project's direction.
- **Design-level changes require discussion.** The trace format, baseline semantics,
  redaction behavior, and the annotation model are contracts shared across all
  runtimes (Java, .NET, TypeScript, Swift, Python). Changes to them must be agreed
  in a discussion before any code is written, because they need to land consistently
  in every implementation.

## Reporting bugs

Open an issue in the relevant repository with:

- library and version,
- runtime/platform version (JDK, .NET, Node, Swift, Python),
- a minimal reproduction,
- expected vs. actual behavior.

**Security issues must not be reported as public issues.** See
[SECURITY.md](SECURITY.md).

## Developer Certificate of Origin

All contributions must be signed off under the
[Developer Certificate of Origin](https://developercertificate.org/) (DCO). By signing
off, you certify that you wrote the contribution or otherwise have the right to submit
it under the inbound license described in the License section below.

Add a sign-off to every commit with `git commit -s`, which appends a line like:

```
Signed-off-by: Your Name <your.email@example.com>
```

Use your real name and a working email address. Pull requests with unsigned commits
cannot be merged.

## Commit messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <short summary>

<optional body explaining what and why>
```

Common types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`, `ci`,
`chore`. Mark breaking changes with `!` after the type (`feat!:`) and describe them in
the body.

## Branches

Branch from `main` and use a short, descriptive name prefixed with the commit type:

```
feat/value-references
fix/redaction-map-keys
docs/annotations-guide
```

## Pull requests

- Keep each PR focused on one change.
- Include tests for behavioral changes; update documentation where relevant.
- Make sure the build and tests pass locally before opening the PR (see the
  repository's own contributing guide for how).
- Reference the related issue or discussion in the PR description.
- Be responsive to review feedback; we are a small team and reviews may take a little
  time.

## License

NarrativeTrace is licensed in three parts, and each repository marks which part an
artifact belongs to:

- the **API and output format** (`narrativetrace-api` and its equivalents, the format
  specification, the clarity rubric) are open standards under the
  [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0);
- the **runtime** is free to use, including in production, and source-available under
  the [Business Source License 1.1](https://mariadb.com/bsl11/); each release converts
  to Apache 2.0 four years after its publication;
- **NarrativeTrace Pro** is commercial and is not developed in these repositories.

**Inbound license for contributions.** By contributing, you license your contribution
to Empower Agile and to every recipient of the project under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), regardless of which
part of the project it touches. This is what lets a runtime contribution be distributed
under the Business Source License today, become Apache 2.0 on its conversion date, and
be included in commercial editions — while you keep the copyright and every right
Apache 2.0 gives you to use your own work elsewhere. Contributions to the API and
format are simply Apache 2.0 in and Apache 2.0 out.

The DCO sign-off on each commit is your certification of that grant; no separate
contributor agreement is required. Documentation contributions are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
