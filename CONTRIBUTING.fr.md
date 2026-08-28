<!-- i18n: source=CONTRIBUTING.md lang=fr -->

> 🌐 [English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md) · [Español](CONTRIBUTING.es.md) · [Português](CONTRIBUTING.pt-BR.md) · Français
>
> _Cette traduction est fournie à titre indicatif. La version anglaise fait foi._

# Contribuer à NarrativeTrace

Merci de l'intérêt que vous portez à NarrativeTrace. Ce document s'applique à tous les
dépôts de l'organisation [narrativetrace](https://github.com/narrativetrace). Chaque dépôt
de bibliothèque possède son propre `CONTRIBUTING.md` (ou `README.md`) avec les
instructions de build et de test propres à ce runtime.

## Ce que nous acceptons

- **Les petites pull requests sont les bienvenues** — corrections de bugs, corrections de
  documentation, améliorations des tests, petites évolutions autonomes.
- **Changements plus importants : ouvrez d'abord une discussion.** Avant d'investir un
  effort conséquent, ouvrez une GitHub Discussion (ou une issue) dans le dépôt concerné
  en décrivant le problème et l'approche que vous proposez. Cela évite un travail inutile
  si le changement ne correspond pas à la direction du projet.
- **Les changements de conception exigent une discussion.** Le format de trace, la
  sémantique des références, le comportement de masquage et le modèle d'annotations sont
  des contrats partagés par tous les runtimes (Java, .NET, TypeScript, Swift, Python).
  Toute modification doit être convenue dans une discussion avant d'écrire la moindre
  ligne de code, car elle doit être appliquée de manière cohérente dans chaque
  implémentation.

## Signaler des bugs

Ouvrez une issue dans le dépôt concerné en indiquant :

- la bibliothèque et sa version,
- la version du runtime ou de la plateforme (JDK, .NET, Node, Swift, Python),
- une reproduction minimale,
- le comportement attendu et le comportement observé.

**Les problèmes de sécurité ne doivent pas être signalés via des issues publiques.** Voir
[SECURITY.md](SECURITY.fr.md).

## Developer Certificate of Origin

Toutes les contributions doivent être signées conformément au
[Developer Certificate of Origin](https://developercertificate.org/) (DCO, certificat
d'origine du développeur). En signant, vous certifiez que vous êtes l'auteur de la
contribution, ou que vous disposez par ailleurs du droit de la soumettre sous la licence
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) du projet.

Ajoutez une signature à chaque commit avec `git commit -s`, qui ajoute une ligne de la
forme :

```
Signed-off-by: Your Name <your.email@example.com>
```

Utilisez votre vrai nom et une adresse e-mail valide. Les pull requests contenant des
commits non signés ne peuvent pas être fusionnées.

## Messages de commit

Nous utilisons [Conventional Commits](https://www.conventionalcommits.org/) :

```
<type>(<optional scope>): <short summary>

<optional body explaining what and why>
```

Types courants : `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`, `ci`,
`chore`. Signalez les changements incompatibles avec un `!` après le type (`feat!:`) et
décrivez-les dans le corps du message.

## Branches

Créez votre branche à partir de `main` et donnez-lui un nom court et descriptif, préfixé
par le type de commit :

```
feat/value-references
fix/redaction-map-keys
docs/annotations-guide
```

## Pull requests

- Limitez chaque PR à un seul changement.
- Ajoutez des tests pour les changements de comportement ; mettez à jour la documentation
  lorsque c'est pertinent.
- Assurez-vous que le build et les tests passent en local avant d'ouvrir la PR (consultez
  le guide de contribution du dépôt pour savoir comment faire).
- Référencez l'issue ou la discussion associée dans la description de la PR.
- Restez réactif aux retours de revue ; nous sommes une petite équipe et les revues
  peuvent prendre un peu de temps.

## Licence

En contribuant, vous acceptez que vos contributions soient placées sous la
[licence Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0), la même licence que
celle du projet.
