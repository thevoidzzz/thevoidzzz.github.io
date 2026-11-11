# ARCHITECTURE — Página estática

Estado: Aprobada
Fecha: 2026-11-11

Este documento manda sobre este repositorio. Las decisiones caras de revertir están en [los ADR](../adr/README.md).

## Qué es

Una página HTML. No es un producto, no tiene API, no llama a un modelo y no tiene base de datos. No crea un codespace. Quien cree un codespace de 2 núcleos en otro repositorio paga esa máquina.

GitHub Pages sirve la raíz de `main`. `index.html` es la página. No hay build.

## Qué puede decir

El texto en inglés repite cifras que un comando ya imprimió, omisiones incluidas, y el orden de una demo local. Una cifra que ningún comando imprimió no entra. Un quinto producto no entra.

## Qué queda fuera

Un servidor, un formulario, un cliente HTTP, una clave, un modelo de pago, AWS, y un codespace creado desde aquí.
