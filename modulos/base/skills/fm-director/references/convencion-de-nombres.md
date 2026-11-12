# Convención de nombres (para poder cruzar anuncios con ventas)

Con un cliente real los nombres de campaña de la hoja de ventas no coincidían con los de Meta y hubo que mapearlos a mano. Con esta convención desde el día 1 el cruce es automático.

## Campañas
`VENTAS-WA | <producto o línea> | <AAAA-MM>`
Ej.: `VENTAS-WA | Cuchareables | 2026-11`

## Conjuntos de anuncios
`<audiencia> | <ubicación>`
Ej.: `Amplia Advantage+ | Lima`

## Anuncios
`A<NN> | <ángulo> | <formato> | <gancho corto>`
Ej.: `A03 | Precio justo | Video 9x16 | Por qué cuesta lo que cuesta`

- `NN` es un número correlativo que nunca se reutiliza.
- Formatos: `Video 9x16`, `Imagen 4x5`, `Carrusel`, `Flyer 1x1`.
- **La misma clave `A03`** se usa en la hoja de ventas (columna "Anuncio") y en el nombre del archivo creativo.

## Hoja de ventas mínima (Google Sheets)
`Fecha · Cliente · Producto · Monto (S/) · Canal (WhatsApp/Web/Tienda) · Anuncio (A03…) · Estado (pagado/pendiente)`

Con "Anuncio" bien llenado, el tablero puede mostrar ventas reales por anuncio, no solo conversaciones.

## Archivos y carpetas
`Entregables/AAAA-MM-DD-tema/<área>/NN-nombre-corto.ext` (sin tildes ni espacios dentro de los nombres de archivo; sí en los títulos de adentro).
