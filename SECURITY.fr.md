<!-- i18n: source=SECURITY.md lang=fr -->

> 🌐 [English](SECURITY.md) · [简体中文](SECURITY.zh-CN.md) · [Español](SECURITY.es.md) · [Português](SECURITY.pt-BR.md) · Français
>
> _Cette traduction est fournie à titre indicatif. La version anglaise fait foi._

# Politique de sécurité

Cette politique s'applique aux bibliothèques open source NarrativeTrace publiées sous
l'organisation GitHub [narrativetrace](https://github.com/narrativetrace) (Java, .NET,
TypeScript, Swift, Python). Elle ne couvre ni narrativetrace.ai, ni NarrativeTrace Pro,
ni la NarrativeTrace Platform.

## Signaler une vulnérabilité

**Merci de ne pas signaler de vulnérabilités de sécurité via des issues GitHub publiques.**

Envoyez un e-mail à **contact@empoweragile.com** en indiquant :

- la bibliothèque et la version concernées,
- une description du problème et de son impact,
- les étapes pour le reproduire, ou une preuve de concept minimale.

Nous sommes une très petite équipe. Vous pouvez vous attendre à :

| Étape | Objectif |
|---|---|
| Accusé de réception de votre signalement | sous 7 jours |
| Premier triage et évaluation de la gravité | sous 14 jours |

Les délais de correction dépendent de la gravité et de la complexité ; nous vous tiendrons
informé de l'avancement des travaux. Nous ne nous engageons pas, pour le moment, sur un
calendrier de divulgation fixe ni sur la publication d'avis de sécurité, mais nous
créditerons les personnes ayant signalé le problème dans les notes de version si elles le
souhaitent.

Nous ne proposons pas de programme de bug bounty.

## Versions prises en charge

Les bibliothèques NarrativeTrace sont en version antérieure à 1.0. Les correctifs de
sécurité ne sont appliqués qu'à la **dernière version publiée** de chaque bibliothèque.
Les versions antérieures ne sont pas prises en charge — merci de mettre à jour avant de
signaler un problème.

## Périmètre

**Dans le périmètre** — tout comportement des bibliothèques qui contredit leurs garanties
documentées, par exemple :

- `@NotTraced` (ou l'équivalent du runtime) qui ne masque pas une valeur marquée dans
  une sortie, quelle qu'elle soit ;
- des règles de masquage basées sur le nom (`RedactionPolicy`) qui ne masquent pas un
  champ dont le nom correspond à la liste d'exclusion ;
- la bibliothèque qui capture des données au-delà de ce qu'elle a été configurée pour
  capturer ;
- une analyse ou une désérialisation non sûre des fichiers de trace ou de référence ;
- une vérification de référence pouvant être contournée, de sorte qu'une dérive de
  comportement passe le build ;
- des vulnérabilités dans les plugins de build, les agents ou les intégrations de
  frameworks que nous distribuons.

**Hors périmètre** — NarrativeTrace enregistre les données d'exécution du code que vous
instrumentez. Les cas suivants relèvent du comportement attendu et ne constituent pas des
vulnérabilités :

- des valeurs sensibles apparaissant dans les traces parce qu'elles ont transité par du
  code instrumenté sans être marquées `@NotTraced` ni couvertes par une règle de masquage ;
- des fichiers de trace ou de référence lisibles par des tiers en raison des permissions
  de fichiers de l'environnement d'exécution ;
- des données sensibles enregistrées dans le système de gestion de versions au sein d'une
  référence.

La protection des fichiers de trace et des références, ainsi que le choix de ce qui doit
être masqué, relèvent de la responsabilité de l'opérateur.

## Clause de protection (safe harbor)

Nous considérons comme autorisée toute recherche en sécurité menée de bonne foi et
conformément à la présente politique. Nous n'engagerons aucune action en justice contre
les chercheurs qui :

- s'efforcent de bonne foi d'éviter toute atteinte à la vie privée, toute destruction de
  données et toute interruption de service ;
- n'interagissent qu'avec des systèmes et des données qui leur appartiennent ou qu'ils
  sont autorisés à tester ;
- nous communiquent leurs découvertes en privé et nous laissent un délai raisonnable pour
  réagir avant toute divulgation publique.
