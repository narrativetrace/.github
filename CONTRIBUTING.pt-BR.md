<!-- i18n: source=CONTRIBUTING.md lang=pt-BR -->

> 🌐 [English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md) · [Español](CONTRIBUTING.es.md) · Português · [Français](CONTRIBUTING.fr.md)
>
> _Esta tradução é disponibilizada por conveniência. A versão em inglês é a oficial._

# Contribuindo com o NarrativeTrace

Obrigado pelo seu interesse no NarrativeTrace. Este documento se aplica a todos os repositórios
da organização [narrativetrace](https://github.com/narrativetrace). Cada repositório de
biblioteca tem seu próprio `CONTRIBUTING.md` (ou `README.md`) com instruções de build e de
testes para aquele runtime.

## O que aceitamos

- **Pull requests pequenos são bem-vindos** — correções de bugs, correções na documentação, melhorias
  em testes, pequenas melhorias autocontidas.
- **Mudanças maiores: abra uma discussão primeiro.** Antes de investir um esforço significativo,
  abra uma GitHub Discussion (ou uma issue) no repositório relevante descrevendo o
  problema e a abordagem que você propõe. Isso evita trabalho desperdiçado caso a mudança não
  se encaixe na direção do projeto.
- **Mudanças de design exigem discussão.** O formato de rastro, a semântica de linha de base,
  o comportamento de redação e o modelo de anotações são contratos compartilhados por todos os
  runtimes (Java, .NET, TypeScript, Swift, Python). Mudanças neles precisam ser acordadas
  em uma discussão antes de qualquer código ser escrito, porque precisam ser aplicadas de forma consistente
  em todas as implementações.

## Reportando bugs

Abra uma issue no repositório relevante informando:

- biblioteca e versão,
- versão do runtime/plataforma (JDK, .NET, Node, Swift, Python),
- uma reprodução mínima,
- comportamento esperado vs. comportamento observado.

**Problemas de segurança não devem ser reportados como issues públicas.** Consulte
[SECURITY.md](SECURITY.pt-BR.md).

## Developer Certificate of Origin

Todas as contribuições devem ser assinadas sob o
[Developer Certificate of Origin](https://developercertificate.org/) (DCO, Certificado de Origem do Desenvolvedor). Ao assinar,
você certifica que escreveu a contribuição ou que, de outra forma, tem o direito de submetê-la
sob a licença [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
do projeto.

Adicione a assinatura a cada commit com `git commit -s`, que acrescenta uma linha como:

```
Signed-off-by: Your Name <your.email@example.com>
```

Use seu nome real e um endereço de e-mail válido. Pull requests com commits não assinados
não podem ser mesclados.

## Mensagens de commit

Usamos o [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <short summary>

<optional body explaining what and why>
```

Tipos comuns: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`, `ci`,
`chore`. Marque mudanças incompatíveis (breaking changes) com `!` após o tipo (`feat!:`) e descreva-as no
corpo da mensagem.

## Branches

Crie a branch a partir de `main` e use um nome curto e descritivo, prefixado com o tipo do commit:

```
feat/value-references
fix/redaction-map-keys
docs/annotations-guide
```

## Pull requests

- Mantenha cada PR focado em uma única mudança.
- Inclua testes para mudanças de comportamento; atualize a documentação quando for relevante.
- Certifique-se de que o build e os testes passam localmente antes de abrir o PR (consulte o
  guia de contribuição do próprio repositório para saber como).
- Referencie a issue ou discussão relacionada na descrição do PR.
- Responda ao feedback da revisão; somos uma equipe pequena e as revisões podem levar algum
  tempo.

## Licença

Ao contribuir, você concorda que suas contribuições são licenciadas sob a
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), a mesma licença
do projeto.
