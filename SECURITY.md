> 🌐 English · [简体中文](SECURITY.zh-CN.md) · [Español](SECURITY.es.md) · [Português](SECURITY.pt-BR.md) · [Français](SECURITY.fr.md)

# Security Policy

This policy applies to the open-source NarrativeTrace libraries published under the
[narrativetrace](https://github.com/narrativetrace) GitHub organization (Java, .NET,
TypeScript, Swift, Python). It does not cover narrativetrace.ai, NarrativeTrace Pro,
or the NarrativeTrace Platform.

## Reporting a vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Email **contact@empoweragile.com** with:

- the affected library and version,
- a description of the issue and its impact,
- steps to reproduce, or a minimal proof of concept.

We are a very small team. You can expect:

| Step | Target |
|---|---|
| Acknowledgement of your report | within 7 days |
| Initial triage and severity assessment | within 14 days |

Fix timelines depend on severity and complexity; we will keep you informed as work
progresses. We do not currently commit to a fixed disclosure timeline or to publishing
advisories, but we will credit reporters in release notes if they wish.

We do not offer a bug bounty.

## Supported versions

NarrativeTrace libraries are pre-1.0. Security fixes are made only to the **latest
released version** of each library. Earlier versions are not supported — please
upgrade before reporting.

## Scope

**In scope** — behavior of the libraries that contradicts their documented guarantees,
for example:

- `@NotTraced` (or the runtime's equivalent) failing to redact a marked value in any
  output;
- name-based redaction rules (`RedactionPolicy`) failing to redact a field whose name
  matches the deny-list;
- the library capturing data outside what it was configured to capture;
- unsafe parsing or deserialization of trace or baseline files;
- a baseline check that can be bypassed so behavioral drift passes the build;
- vulnerabilities in the build plugins, agents, or framework integrations we ship.

**Out of scope** — NarrativeTrace records the runtime data of the code you instrument.
The following are expected behavior, not vulnerabilities:

- sensitive values appearing in traces because they were passed through instrumented
  code and were not marked `@NotTraced` or covered by a redaction rule;
- trace or baseline files being readable by others because of the operating
  environment's file permissions;
- sensitive data committed to version control inside a baseline.

Protecting trace files and baselines, and choosing what to redact, is the
responsibility of the operator.

## Safe harbor

We consider security research conducted in good faith and in accordance with this
policy to be authorized. We will not pursue legal action against researchers who:

- make a good-faith effort to avoid privacy violations, data destruction, and
  service disruption;
- only interact with systems and data they own or have permission to test;
- report findings to us privately and give us reasonable time to respond before any
  public disclosure.
