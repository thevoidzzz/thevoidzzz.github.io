# ADR-0001: La página se queda estática

Estado: Accepted
Fecha: 2026-11-11

## Context

Este repositorio existe para publicar una página. Un servidor que llamara a otros procesos sería otro producto: tendría un contrato, un fallo de red y un sitio donde esconder una clave.

## Decision

La página es un HTML estático. GitHub Pages la sirve desde la raíz de `main`. No hay API, ni formulario, ni cliente HTTP, ni base de datos. El texto solo repite cifras que un comando ya imprimió. Este repositorio no crea un codespace.

## Alternatives

**Un servicio que consulte a los demás en vivo.** Descartado: sería un quinto producto, y la página dejaría de poder publicarse sin claves y sin procesos levantados.

**Generar el HTML en el build.** Descartado: no hay una transformación que justifique un paso de build. El archivo que se lee es el que se publica.

## Trade-offs

Se gana una página que no depende de un proceso. Se paga que una cifra nueva no aparece sola: hay que copiarla de una corrida impresa.

## Consequences

Un formulario, un `fetch` o un endpoint nuevo piden otro ADR. Mientras tanto, el test de la página falla si aparece un formulario o un cliente HTTP.
