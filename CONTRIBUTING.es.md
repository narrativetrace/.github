<!-- i18n: source=CONTRIBUTING.md lang=es -->

> 🌐 [English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md) · Español · [Português](CONTRIBUTING.pt-BR.md) · [Français](CONTRIBUTING.fr.md)
>
> _Esta traducción se ofrece por conveniencia. La versión en inglés es la autoritativa._

# Cómo contribuir a NarrativeTrace

Gracias por tu interés en NarrativeTrace. Este documento se aplica a todos los repositorios
de la organización [narrativetrace](https://github.com/narrativetrace). Cada repositorio de
biblioteca tiene su propio `CONTRIBUTING.md` (o `README.md`) con las instrucciones de
compilación y pruebas para ese runtime.

## Qué aceptamos

- **Los pull requests pequeños son bienvenidos**: correcciones de errores, correcciones de
  documentación, mejoras en las pruebas y pequeñas mejoras autocontenidas.
- **Cambios más grandes: abre primero una discusión.** Antes de invertir un esfuerzo
  considerable, abre una GitHub Discussion (o un issue) en el repositorio correspondiente
  describiendo el problema y el enfoque que propones. Así se evita trabajo en vano si el
  cambio no encaja con la dirección del proyecto.
- **Los cambios a nivel de diseño requieren discusión.** El formato de traza, la semántica
  de la línea base, el comportamiento de redacción y el modelo de anotaciones son contratos
  compartidos por todos los runtimes (Java, .NET, TypeScript, Swift, Python). Los cambios
  en ellos deben acordarse en una discusión antes de escribir cualquier código, porque
  tienen que aplicarse de forma consistente en todas las implementaciones.

## Cómo reportar errores

Abre un issue en el repositorio correspondiente con:

- la biblioteca y la versión,
- la versión del runtime o de la plataforma (JDK, .NET, Node, Swift, Python),
- una reproducción mínima,
- el comportamiento esperado frente al comportamiento real.

**Los problemas de seguridad no deben reportarse como issues públicos.** Consulta
[SECURITY.md](SECURITY.es.md).

## Developer Certificate of Origin

Todas las contribuciones deben estar firmadas conforme al
[Developer Certificate of Origin](https://developercertificate.org/) (Certificado de Origen
del Desarrollador, DCO). Al firmar, certificas que escribiste la contribución o que, de
otro modo, tienes derecho a enviarla bajo la licencia
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) del proyecto.

Añade la firma a cada commit con `git commit -s`, que agrega una línea como esta:

```
Signed-off-by: Your Name <your.email@example.com>
```

Usa tu nombre real y una dirección de correo electrónico que funcione. Los pull requests
con commits sin firmar no pueden fusionarse.

## Mensajes de commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <short summary>

<optional body explaining what and why>
```

Tipos habituales: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`, `ci`,
`chore`. Marca los cambios incompatibles (breaking changes) con `!` después del tipo
(`feat!:`) y descríbelos en el cuerpo del mensaje.

## Ramas

Crea la rama a partir de `main` y usa un nombre corto y descriptivo con el tipo de commit
como prefijo:

```
feat/value-references
fix/redaction-map-keys
docs/annotations-guide
```

## Pull requests

- Mantén cada PR centrado en un solo cambio.
- Incluye pruebas para los cambios de comportamiento; actualiza la documentación cuando
  corresponda.
- Asegúrate de que la build y las pruebas pasen en local antes de abrir el PR (consulta la
  guía de contribución del propio repositorio para saber cómo).
- Referencia el issue o la discusión relacionados en la descripción del PR.
- Responde con diligencia a los comentarios de la revisión; somos un equipo pequeño y las
  revisiones pueden tardar un poco.

## Licencia

Al contribuir, aceptas que tus contribuciones se licencian bajo la
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), la misma licencia que
el proyecto.
