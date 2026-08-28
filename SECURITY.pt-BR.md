<!-- i18n: source=SECURITY.md lang=pt-BR -->

> 🌐 [English](SECURITY.md) · [简体中文](SECURITY.zh-CN.md) · [Español](SECURITY.es.md) · Português · [Français](SECURITY.fr.md)
>
> _Esta tradução é disponibilizada por conveniência. A versão em inglês é a oficial._

# Política de segurança

Esta política se aplica às bibliotecas de código aberto do NarrativeTrace publicadas na
organização [narrativetrace](https://github.com/narrativetrace) no GitHub (Java, .NET,
TypeScript, Swift, Python). Ela não cobre o narrativetrace.ai, o NarrativeTrace Pro
nem a NarrativeTrace Platform.

## Como reportar uma vulnerabilidade

**Por favor, não reporte vulnerabilidades de segurança por meio de issues públicas no GitHub.**

Envie um e-mail para **contact@empoweragile.com** informando:

- a biblioteca e a versão afetadas,
- uma descrição do problema e do seu impacto,
- os passos para reproduzir, ou uma prova de conceito mínima.

Somos uma equipe muito pequena. Você pode esperar:

| Etapa | Prazo |
|---|---|
| Confirmação de recebimento do seu relato | em até 7 dias |
| Triagem inicial e avaliação de severidade | em até 14 dias |

Os prazos de correção dependem da severidade e da complexidade; manteremos você informado
conforme o trabalho avançar. No momento, não nos comprometemos com um prazo fixo de divulgação
nem com a publicação de advisories, mas daremos crédito a quem reportar nas notas de release, se assim desejar.

Não oferecemos programa de bug bounty.

## Versões com suporte

As bibliotecas do NarrativeTrace estão em versão anterior à 1.0. As correções de segurança são feitas apenas na **versão
mais recente lançada** de cada biblioteca. Versões anteriores não têm suporte — por favor,
atualize antes de reportar.

## Escopo

**Dentro do escopo** — comportamento das bibliotecas que contradiga as garantias documentadas,
por exemplo:

- `@NotTraced` (ou o equivalente do runtime) deixar de redigir um valor marcado em qualquer
  saída;
- regras de redação baseadas em nome (`RedactionPolicy`) deixarem de redigir um campo cujo nome
  corresponde à lista de bloqueio;
- a biblioteca capturar dados além do que foi configurada para capturar;
- parsing ou desserialização insegura de arquivos de rastro ou de linha de base;
- uma verificação de linha de base que possa ser contornada, permitindo que um desvio de comportamento passe no build;
- vulnerabilidades nos plugins de build, agentes ou integrações com frameworks que distribuímos.

**Fora do escopo** — o NarrativeTrace registra os dados em tempo de execução do código que você instrumenta.
Os itens a seguir são comportamento esperado, não vulnerabilidades:

- valores sensíveis aparecerem em rastros porque passaram por código instrumentado
  e não foram marcados com `@NotTraced` nem cobertos por uma regra de redação;
- arquivos de rastro ou de linha de base poderem ser lidos por terceiros por causa das permissões de
  arquivo do ambiente de execução;
- dados sensíveis enviados ao controle de versão dentro de uma linha de base.

Proteger os arquivos de rastro e as linhas de base, e escolher o que redigir, é
responsabilidade do operador.

## Porto seguro (safe harbor)

Consideramos autorizada a pesquisa de segurança conduzida de boa-fé e em conformidade com esta
política. Não tomaremos medidas legais contra pesquisadores que:

- façam um esforço de boa-fé para evitar violações de privacidade, destruição de dados e
  interrupção de serviços;
- interajam apenas com sistemas e dados que possuam ou que tenham permissão para testar;
- nos reportem as descobertas de forma privada e nos concedam um prazo razoável para responder antes de qualquer
  divulgação pública.
