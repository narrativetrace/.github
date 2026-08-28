<!-- i18n: source=SECURITY.md lang=es -->

> 🌐 [English](SECURITY.md) · [简体中文](SECURITY.zh-CN.md) · Español · [Português](SECURITY.pt-BR.md) · [Français](SECURITY.fr.md)
>
> _Esta traducción se ofrece por conveniencia. La versión en inglés es la autoritativa._

# Política de seguridad

Esta política se aplica a las bibliotecas de código abierto de NarrativeTrace publicadas
bajo la organización de GitHub [narrativetrace](https://github.com/narrativetrace) (Java,
.NET, TypeScript, Swift, Python). No cubre narrativetrace.ai, NarrativeTrace Pro ni
NarrativeTrace Platform.

## Cómo reportar una vulnerabilidad

**Por favor, no reportes vulnerabilidades de seguridad a través de issues públicos de GitHub.**

Escribe a **contact@empoweragile.com** indicando:

- la biblioteca y la versión afectadas,
- una descripción del problema y de su impacto,
- los pasos para reproducirlo, o una prueba de concepto mínima.

Somos un equipo muy pequeño. Puedes esperar lo siguiente:

| Paso | Objetivo |
|---|---|
| Acuse de recibo de tu reporte | en un plazo de 7 días |
| Triaje inicial y evaluación de la severidad | en un plazo de 14 días |

Los plazos de corrección dependen de la severidad y la complejidad; te mantendremos
informado a medida que avance el trabajo. Por ahora no nos comprometemos a un plazo fijo
de divulgación ni a publicar avisos de seguridad, pero daremos crédito a quienes reporten
en las notas de la versión si así lo desean.

No ofrecemos un programa de recompensas por errores (bug bounty).

## Versiones con soporte

Las bibliotecas de NarrativeTrace están en versiones anteriores a la 1.0. Las correcciones
de seguridad se aplican únicamente a la **última versión publicada** de cada biblioteca.
Las versiones anteriores no tienen soporte; por favor, actualiza antes de reportar.

## Alcance

**Dentro del alcance**: comportamiento de las bibliotecas que contradiga sus garantías
documentadas, por ejemplo:

- que `@NotTraced` (o su equivalente en el runtime) no redacte un valor marcado en
  cualquier salida;
- que las reglas de redacción basadas en nombres (`RedactionPolicy`) no redacten un campo
  cuyo nombre coincida con la lista de exclusión;
- que la biblioteca capture datos más allá de lo que se configuró para capturar;
- análisis o deserialización insegura de archivos de traza o de línea base;
- una verificación de línea base que pueda eludirse de modo que una desviación de
  comportamiento pase la build;
- vulnerabilidades en los plugins de build, agentes o integraciones con frameworks que
  distribuimos.

**Fuera del alcance**: NarrativeTrace registra los datos en tiempo de ejecución del código
que instrumentas. Lo siguiente es comportamiento esperado, no vulnerabilidades:

- valores sensibles que aparecen en las trazas porque pasaron por código instrumentado y
  no estaban marcados con `@NotTraced` ni cubiertos por una regla de redacción;
- archivos de traza o de línea base legibles por terceros debido a los permisos de
  archivo del entorno de ejecución;
- datos sensibles confirmados en el control de versiones dentro de una línea base.

Proteger los archivos de traza y las líneas base, así como decidir qué redactar, es
responsabilidad del operador.

## Puerto seguro

Consideramos autorizada la investigación de seguridad realizada de buena fe y conforme a
esta política. No emprenderemos acciones legales contra los investigadores que:

- hagan un esfuerzo de buena fe por evitar violaciones de la privacidad, destrucción de
  datos e interrupciones del servicio;
- interactúen únicamente con sistemas y datos que les pertenezcan o que tengan permiso
  para probar;
- nos reporten sus hallazgos de forma privada y nos concedan un tiempo razonable para
  responder antes de cualquier divulgación pública.
