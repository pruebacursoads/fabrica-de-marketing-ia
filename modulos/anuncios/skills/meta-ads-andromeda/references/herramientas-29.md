# Referencia Detallada: Las 29 Herramientas del MCP de Meta Ads
### por Hugo López — El Marketero del Pueblo

> Este archivo es para uso interno de Claude. Contiene el detalle técnico de cada herramienta.
> El emprendedor nunca ve este archivo directamente.

---

## GRUPO 1: Creación y gestión de campañas

### 1. `ads_create_campaign`
**Qué hace:** Crea una campaña publicitaria nueva en la cuenta.

**Cuándo usarla:**
- El emprendedor quiere empezar a pautar un producto/servicio nuevo
- Necesita una estructura nueva separada de campañas existentes

**Parámetros clave que Claude debe preguntar al usuario (en simple):**
- ¿Qué quieres lograr? (ventas, visitas a web, mensajes, reconocimiento de marca, leads)
  → esto define el `objective`: OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_AWARENESS
- ¿Cuánto quieres gastar por día?
  → `daily_budget` en centavos (ej: S/. 20 = 2000 centavos)
- ¿Cómo se llama esta campaña?
  → `name`

**Regla crítica:** Siempre crear con `status: PAUSED`. Nunca `ACTIVE` directo.

**Señal de éxito para el emprendedor:** "Tu campaña '[nombre]' fue creada y está lista. Está apagada por ahora — avisame cuando quieras activarla."

---

### 2. `ads_create_ad_set`
**Qué hace:** Crea un conjunto de anuncios dentro de una campaña. Define el presupuesto, la audiencia, el horario y las ubicaciones.

**Cuándo usarla:** Justo después de crear la campaña, o cuando el emprendedor quiere llegar a un público diferente con la misma campaña.

**Parámetros clave (en simple):**
- ¿A quién le quieres mostrar el anuncio? (edad, género, país, ciudad, intereses)
  → `targeting`
- ¿Cuánto quieres gastar? (si no se definió en la campaña)
  → `daily_budget`
- ¿Dónde quieres que aparezca? (Facebook, Instagram, Reels, Stories, etc.)
  → `placements`
- ¿Qué quieres que haga la gente al ver el anuncio? (comprar, hacer clic, dejar datos)
  → `optimization_goal`

**Regla crítica:** `status: PAUSED` siempre al crear.

---

### 3. `ads_create_ad`
**Qué hace:** Crea el anuncio en sí: el contenido visual y el texto que ve la gente.

**Cuándo usarla:** Cuando ya existe el conjunto y se tienen los creativos listos (imagen o video + texto + enlace).

**Parámetros clave (en simple):**
- ¿Cuál es el texto principal del anuncio?
- ¿Cuál es el título o headline?
- ¿A qué página quieres que vayan cuando hagan clic?
- ¿Qué botón quieres? (Comprar, Más información, Contactar, etc.)
- ¿Cuál es el ID de la imagen o video?

**Nota para Claude:** Si el emprendedor no sabe el ID del creativo, guiarlo a subir la imagen primero desde Ads Manager o preguntar si tiene la URL de la imagen.

---

### 4. `ads_update_entity`
**Qué hace:** Edita cualquier campaña, conjunto o anuncio existente.

**Cuándo usarla:**
- Cambiar el presupuesto de una campaña
- Cambiar el texto de un anuncio
- Cambiar la audiencia de un conjunto
- Pausar o activar manualmente

**Regla crítica:** Confirmar siempre qué entidad se va a editar y qué campo. Mostrar "antes" y "después" al usuario antes de ejecutar.

**Ejemplo de confirmación correcta:**
> "Voy a cambiar el presupuesto diario de tu campaña 'Venta de Zapatos' de S/. 20 a S/. 35. ¿Confirmas?"

---

### 5. `ads_activate_entity`
**Qué hace:** Activa (enciende) una campaña, conjunto o anuncio que estaba pausado.

**Cuándo usarla:** Cuando el emprendedor confirma que quiere que algo empiece a gastar.

**Regla crítica:**
- Solo ejecutar con confirmación explícita
- Recordar al usuario que **a partir de ese momento empieza el gasto**
- Mencionar el presupuesto diario que se activará

**Ejemplo de mensaje correcto:**
> "Al activar esta campaña, Meta comenzará a gastar hasta S/. 35 por día. ¿Confirmas que la activo ahora?"

---

## GRUPO 2: Insights, benchmarks y rendimiento

### 6. `ads_get_insights`
**Qué hace:** Obtiene las métricas de rendimiento: gasto, alcance, clics, conversiones, ROAS, etc.

**Cuándo usarla:** Es la herramienta más usada. Para cualquier reporte de resultados.

**Parámetros clave:**
- Período de tiempo: últimos 7 días, 14 días, 30 días, o rango personalizado
- Nivel: campaña, conjunto de anuncios, o anuncio individual
- Métricas a mostrar (Claude selecciona las relevantes según el objetivo)

**Métricas más importantes según objetivo:**
- Ventas → ROAS, costo por compra, valor de compra
- Tráfico → CPC, CTR, clics en enlace
- Mensajes → costo por mensaje, mensajes enviados
- Leads → costo por lead, leads generados
- Reconocimiento → alcance, impresiones, CPM, frecuencia

---

### 7. `ads_get_creative_insights`
**Qué hace:** Compara el rendimiento de diferentes creativos (imágenes/videos) entre sí.

**Cuándo usarla:** Cuando el emprendedor quiere saber qué imagen o video funcionó mejor.

**Cómo presentarlo:** Tabla simple con creativo, CTR, y costo por resultado. Destacar el ganador claramente.

---

### 8. `ads_get_benchmarks`
**Qué hace:** Compara las métricas del emprendedor con el promedio de negocios similares en su sector.

**Cuándo usarla:**
- Cuando el emprendedor pregunta "¿estoy yendo bien?"
- Para contextualizar si un CTR de 1% es bueno o malo en su industria

**Cómo presentarlo:** "Tu CTR es del 2.1%. El promedio de negocios como el tuyo es 1.4%. Estás por encima del promedio 🎯"

---

### 9. `ads_get_delivery_insights`
**Qué hace:** Muestra por qué un anuncio se está entregando poco, de forma irregular, o con costos altos.

**Cuándo usarla:**
- El emprendedor dice "mis anuncios no llegan a nadie"
- Un conjunto de anuncios tiene presupuesto pero gasta muy poco
- Los costos subieron de repente sin cambiar nada

**Problemas comunes que detecta:**
- Audiencia muy pequeña o restrictiva
- Anuncio rechazado o en revisión
- Competencia alta en la subasta
- Presupuesto muy bajo para la audiencia objetivo

---

### 10. `ads_get_audience_insights`
**Qué hace:** Muestra el perfil de quién está viendo los anuncios: edad, género, ubicación, dispositivo.

**Cuándo usarla:**
- Para afinar la segmentación
- Para saber si se está llegando al público correcto
- Para detectar si la audiencia está concentrada en un solo segmento

---

### 11. `ads_get_reach_frequency`
**Qué hace:** Muestra cuántas personas únicas vieron el anuncio y cuántas veces en promedio lo vieron.

**Cuándo usarla:**
- Cuando el emprendedor sospecha que "le está apareciendo mucho a la misma gente"
- Para evaluar si hay fatiga de audiencia

**Señal de alerta:** Frecuencia mayor a 4 en 7 días = la gente ya está cansada del anuncio. Sugerencia: renovar el creativo o ampliar la audiencia.

---

### 12. `ads_get_pacing`
**Qué hace:** Analiza cómo se está distribuyendo el gasto del presupuesto a lo largo del día.

**Cuándo usarla:**
- El presupuesto se agota muy rápido (antes del mediodía)
- El emprendedor quiere entender si Meta está gastando bien su plata

---

## GRUPO 3: Cuentas, páginas y activos

### 13. `ads_get_ad_accounts`
**Qué hace:** Lista todas las cuentas publicitarias a las que tiene acceso el usuario conectado.

**Cuándo usarla:** Al inicio de TODA sesión. Claude la llama automáticamente para saber desde qué cuenta trabajar.

**Cómo presentarlo:** Si hay solo una cuenta, confirmar con el usuario que es la correcta. Si hay varias, preguntar cuál usar.

---

### 14. `ads_get_ad_entities`
**Qué hace:** Lista todas las campañas, conjuntos de anuncios y anuncios de una cuenta, con sus estados.

**Cuándo usarla:**
- Para mapear todo lo que existe en la cuenta
- Para encontrar una campaña específica antes de editarla
- Para el diagnóstico inicial

**Límite de sesión:** Claude lleva conteo mental de cuántas cuentas distintas se han consultado. Al llegar a 5 cuentas diferentes, avisar al usuario que lo mejor es continuar en otra sesión.

---

### 15. `ads_get_pages_for_business`
**Qué hace:** Lista las páginas de Facebook conectadas al Business Manager.

**Cuándo usarla:** Al crear un anuncio — se necesita el ID de la página de Facebook del emprendedor.

---

## GRUPO 4: Catálogo de productos

### 16. `ads_catalog_create`
**Qué hace:** Crea un catálogo de productos nuevo en Meta.

**Cuándo usarla:** Cuando el emprendedor tiene una tienda online y quiere hacer anuncios de catálogo (Dynamic Product Ads / Advantage+ Catalog).

**Pregunta al usuario:** ¿Tienes una tienda online? ¿Cuántos productos tienes? ¿Ya tienes un feed de productos (archivo XML, CSV o conexión directa)?

---

### 17. `ads_catalog_get_catalogs`
**Qué hace:** Lista todos los catálogos de productos existentes en la cuenta.

**Cuándo usarla:** Al inicio del trabajo con catálogos para ver qué existe.

---

### 18. `ads_catalog_get_details`
**Qué hace:** Muestra los detalles de configuración de un catálogo específico.

**Cuándo usarla:** Para revisar si el catálogo está bien configurado (qué tipo de productos, permisos, configuración de feed).

---

### 19. `ads_catalog_get_diagnostics`
**Qué hace:** Muestra errores y advertencias del catálogo: productos rechazados, campos faltantes, imágenes que no cumplen especificaciones.

**Cuándo usarla:**
- Cuando los productos no aparecen en los anuncios
- Cuando Meta dice que hay "errores en el catálogo"
- Como parte del diagnóstico rutinario

**Cómo presentarlo:** "Encontré 12 productos con problemas. El error más común es que les falta el precio. Te explico cómo corregirlo."

---

### 20. `ads_catalog_get_feed_rules`
**Qué hace:** Muestra las reglas configuradas para el feed automático de productos.

**Cuándo usarla:** Cuando el catálogo no se actualiza automáticamente o los datos de productos no coinciden.

---

### 21. `ads_catalog_get_product_details`
**Qué hace:** Muestra todos los datos de un producto específico dentro del catálogo.

**Cuándo usarla:** Cuando un producto específico no aparece en los anuncios o tiene datos incorrectos.

---

### 22. `ads_catalog_get_product_feed_details`
**Qué hace:** Muestra el estado del feed (archivo o conexión que actualiza el catálogo): cuándo fue la última actualización, cuántos productos se procesaron, si hubo errores.

**Cuándo usarla:** Cuando el inventario no se actualiza o los precios están desactualizados en los anuncios.

---

### 23. `ads_catalog_get_product_set_products`
**Qué hace:** Lista los productos que pertenecen a un conjunto específico de productos.

**Cuándo usarla:** Para verificar qué productos se van a mostrar en un grupo de anuncios de catálogo.

---

### 24. `ads_catalog_get_product_sets`
**Qué hace:** Lista todos los conjuntos de productos dentro de un catálogo.

**Cuándo usarla:** Para ver cómo están agrupados los productos (por categoría, precio, disponibilidad, etc.).

---

### 25. `ads_catalog_get_products`
**Qué hace:** Lista todos los productos del catálogo con sus estados.

**Cuándo usarla:** Para hacer un inventario completo: cuántos productos están aprobados, rechazados, o pendientes.

**Cómo presentarlo:** "Tu catálogo tiene 340 productos. De esos, 312 están aprobados, 18 están rechazados y 10 están pendientes de revisión."

---

## GRUPO 5: Pixel y calidad de seguimiento

### 26. `ads_get_dataset_details`
**Qué hace:** Muestra la información de tu pixel o dataset: ID, nombre, con qué cuentas está conectado.

**Cuándo usarla:** Al inicio del diagnóstico de tracking para confirmar que el pixel existe y está vinculado a la cuenta.

**En simple para el emprendedor:** "Tu píxel se llama [nombre] y está conectado a tu cuenta publicitaria. Todo bien por ahí."

---

### 27. `ads_get_dataset_quality`
**Qué hace:** Muestra el EMQ (Event Match Quality) — qué tan bien Meta puede identificar a las personas que llegan a tu web para optimizar los anuncios.

**Cuándo usarla:**
- El costo por resultado está subiendo sin razón clara
- Quieres saber si el pixel está funcionando bien

**Escala de calidad:**
- 6.0 - 10.0 → Excelente
- 4.0 - 5.9 → Bueno
- 2.0 - 3.9 → Regular — se puede mejorar
- Menos de 2.0 → Malo — hay que revisar el pixel

**En simple:** "El pixel está capturando bien a tus visitantes. Esto ayuda a Meta a encontrar más personas como tus compradores."

---

### 28. `ads_get_dataset_stats`
**Qué hace:** Muestra cuántos eventos llegaron al pixel en un período: PageView, ViewContent, AddToCart, Purchase, Lead, etc.

**Cuándo usarla:**
- Para confirmar que el pixel está activo y recibiendo datos
- Para ver si hay descalce entre las ventas reales y las que Meta registra

---

### 29. `ads_get_errors`
**Qué hace:** Muestra los errores recientes del pixel o dataset: eventos duplicados, datos faltantes, eventos que no se pueden procesar.

**Cuándo usarla:**
- Hay advertencias en Events Manager
- Los eventos no aparecen o aparecen duplicados
- Como parte del diagnóstico cuando el pixel "no funciona"

---

## COMBINACIONES DE HERRAMIENTAS MÁS FRECUENTES

### Diagnóstico completo de cuenta (10-15 min)
`ads_get_ad_accounts` → `ads_get_ad_entities` → `ads_get_insights` (30 días) → `ads_get_delivery_insights` → `ads_get_dataset_quality`

### Reporte semanal rápido (3-5 min)
`ads_get_insights` (últimos 7 días) → `ads_get_creative_insights` → comparar con `ads_get_benchmarks`

### Antes de crear una campaña nueva
`ads_get_pages_for_business` → `ads_catalog_get_catalogs` (si es tienda) → `ads_get_dataset_details` → crear en orden: campaña → conjunto → anuncio

### Diagnóstico de catálogo con problemas
`ads_catalog_get_catalogs` → `ads_catalog_get_diagnostics` → `ads_catalog_get_products` → `ads_get_errors`

---

*Creado por Hugo López — El Marketero del Pueblo 🚀*
