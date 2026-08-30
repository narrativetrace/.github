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
otro modo, tienes derecho a enviarla bajo la licencia de entrada descrita en la
sección Licencia más abajo.

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

NarrativeTrace se licencia en tres partes, y cada repositorio marca a cuál pertenece
cada artefacto:

- la **API y el formato de salida** (`narrativetrace-api` y sus equivalentes, la
  especificación del formato, la rúbrica de claridad) son estándares abiertos bajo la
  [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0);
- el **runtime** es gratuito, también en producción, y de código disponible bajo la
  [Business Source License 1.1](https://mariadb.com/bsl11/); cada versión pasa a Apache 2.0 cuatro años
  después de su publicación;
- **NarrativeTrace Pro** es comercial y no se desarrolla en estos repositorios.

**Licencia de entrada de las contribuciones.** Al contribuir, licencias tu contribución
a Empower Agile y a todo receptor del proyecto bajo la
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), sin importar qué parte del proyecto toque. Esto es lo que
permite que una contribución al runtime se distribuya hoy bajo la Business Source
License, pase a Apache 2.0 en su fecha de conversión y se incluya en las ediciones
comerciales — mientras conservas el copyright y todos los derechos que Apache 2.0 te da
para usar tu propio trabajo en otro lugar. Las contribuciones a la API y al formato son
simplemente Apache 2.0 de entrada y Apache 2.0 de salida.

La firma DCO en cada commit es tu certificación de esa concesión; no se requiere ningún
acuerdo de contribuidor aparte. Las contribuciones a la documentación se licencian bajo
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
