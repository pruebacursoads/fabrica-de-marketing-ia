# Reglas de Seguridad Anti-Baneo — MCP Oficial de Meta
### por Hugo López — El Marketero del Pueblo

> Archivo interno para Claude. El emprendedor nunca lo ve directamente.
> Estas reglas protegen la cuenta publicitaria del emprendedor de bloqueos y suspensiones.
> Actualizado con documentación oficial de Meta Marketing API (2026).

---

## CONTEXTO: Por qué el MCP oficial es más seguro que la API directa

El conector oficial de Meta (`mcp.facebook.com/ads`) elimina los riesgos más comunes
de la API directa:

| Riesgo antes (API directa) | Estado ahora (MCP oficial) |
|---|---|
| Gestionar tokens propios que vencen | ✅ OAuth gestionado por Meta |
| App de desarrollador no verificada | ✅ App oficial verificada por Meta |
| appsecret_proof no implementado | ✅ Gestionado internamente |
| Riesgo de ban por credenciales incorrectas | ✅ Mínimo con app oficial |

**Lo que NO desaparece y sigue siendo riesgo:**
- Comportamiento de agente abusivo (loops, demasiadas solicitudes)
- Acciones de escritura no intencionadas
- Múltiples sesiones concurrentes
- Editar algo equivocado por falta de confirmación
- Superar los rate limits por exceso de llamadas en corto tiempo

---

## RATE LIMITS OFICIALES DE META (Documentación oficial 2026)

### Cómo funciona el sistema de puntos

La Marketing API de Meta usa un sistema de puntuación acumulada:

| Tipo de llamada | Puntos que consume |
|---|---|
| Lectura (GET — ver datos) | 1 punto |
| Escritura (POST/CREATE/UPDATE) | 3 puntos |

Cuando acumulas demasiados puntos, Meta lanza un error de throttling y bloquea temporalmente.

### Los dos niveles de acceso y sus límites

| Nivel | Puntos máximos | Tiempo de decay | Bloqueo si se supera |
|---|---|---|---|
| **Development** (acceso básico) | 60 puntos | 300 segundos | 300 segundos bloqueado |
| **Standard** (acceso avanzado) | 9,000 puntos | 300 segundos | 60 segundos bloqueado |

**En simple para Claude:** El MCP oficial usa el nivel que tenga configurado el emprendedor.
Si la cuenta es nueva o básica, tiene solo 60 puntos — eso es muy poco. Hay que espaciar las llamadas.

### Límites operativos específicos (fuente oficial Meta)

Estos límites aplican independientemente del nivel de acceso:

| Acción | Límite oficial |
|---|---|
| Actualizar el límite de gasto de una cuenta | Máximo **10 veces por día** |
| Cambiar presupuesto diario o total de un conjunto | Máximo **4 veces por hora por conjunto** |
| Consultas de insights simultáneas | Distribuir — no enviar varias a la vez |
| Llamadas de insights (reach con breakdowns) | Máximo **10 requests async por cuenta por día** |

### Señales de rate limit en los headers de respuesta

Cuando Meta responde, incluye headers que indican el estado del límite:

```
X-Ad-Account-Usage:
  acc_id_util_pct: 9.67   → % de llamadas usadas para esta cuenta
  reset_time_duration: 100 → segundos para resetear el contador
  ads_api_access_tier: standard_access

X-Business-Use-Case-Usage:
  call_count: 100          → % de llamadas realizadas
  total_cputime: 25        → % de CPU usado
  total_time: 25           → % de tiempo total usado
  estimated_time_to_regain_access: 19 → minutos para recuperar acceso
```

**Regla de Claude:** Si `call_count` o `acc_id_util_pct` supera el 70%, pausar y esperar
antes de hacer más llamadas. No esperar a que llegue al 100%.

### Códigos de error de rate limit

| Código | Subcódigo | Significado | Qué hace Claude |
|---|---|---|---|
| 17 | 2446079 | User request limit reached | Esperar 60-300 seg, luego 1 reintento |
| 613 | 1487742 | Too many calls from this ad-account | Esperar 300 seg, reducir frecuencia |
| 4 | 1504022 | Too many API requests (insights) | Reducir complejidad de la consulta |
| 429 | — | HTTP rate limit genérico | Backoff exponencial |

### Estrategia de backoff exponencial

Si Claude recibe un error de rate limit, aplica esta secuencia antes de reintentar:
1. Primer error → esperar **60 segundos**
2. Segundo error seguido → esperar **120 segundos**
3. Tercer error seguido → esperar **300 segundos** y avisar al usuario
4. Cuarto error → **DETENER la sesión** y pedir al usuario que continúe más tarde

**Mensaje al emprendedor cuando hay rate limit:**
> *"Meta nos está pidiendo que esperemos un momento — están protegiendo tu cuenta
> de demasiadas consultas seguidas. Es normal. Esperamos [X] segundos y seguimos."*

### Cómo prevenir rate limits — reglas operativas de Claude

✅ **Espaciar las llamadas:** No hacer más de 3-4 llamadas seguidas sin mostrar resultados al usuario
✅ **Combinar consultas:** Preferir una llamada completa a varias pequeñas
✅ **No repetir loops:** Si ya se consultó algo en la sesión, usar el dato guardado — no volver a llamar
✅ **Priorizar lectura:** Las lecturas cuestan 1 punto vs. 3 de escritura — usarlas primero para diagnóstico
✅ **Distribuir insights:** No pedir todos los reportes de insights al mismo tiempo
✅ **Respetar el límite de 4 cambios/hora por conjunto:** Si el emprendedor quiere cambiar el presupuesto más veces, explicarle que hay que esperar

❌ **Nunca hacer:** Llamar a 10+ herramientas seguidas sin pausas
❌ **Nunca hacer:** Reintentar automáticamente sin esperar el tiempo de decay
❌ **Nunca hacer:** Consultar insights con rangos de fechas muy largos Y muchos IDs al mismo tiempo
❌ **Nunca hacer:** Ejecutar la misma consulta repetidamente para "refrescar" datos

---

## PROTOCOLO DE INICIO DE SESIÓN

### Paso 1: Sesiones paralelas (OBLIGATORIO, PRIMERA ACCIÓN)

Claude pregunta siempre:
> *"Antes de comenzar: ¿hay algún otro programa, bot, reporte automático o sesión de Claude
> revisando esta cuenta de Meta Ads en este momento?"*

- **Sí o no sé** → Pedir que lo cierren todo. Esperar confirmación.
- **No** → Continuar.

**Por qué:** Meta detecta múltiples fuentes simultáneas como comportamiento de bot automatizado.
Además, si hay otro proceso activo, los puntos de rate limit se consumen más rápido entre todos.

### Paso 2: Clasificación de la tarea

| Tipo de tarea | Riesgo | Puntos que consume | Protocolo |
|---|---|---|---|
| Solo lectura (ver datos, analizar) | 🔵 Bajo | 1 punto por llamada | Ejecutar directamente |
| Escritura (crear, editar, activar) | 🟠 Alto | 3 puntos por llamada | Confirmar antes de cada acción |

### Paso 3: Límite de cuentas por sesión

Claude lleva conteo interno de cuántas cuentas publicitarias distintas se consultan.

- 1-4 cuentas: Normal
- 5 cuentas: Claude avisa → *"Ya consultamos 5 cuentas en esta sesión. Para cuidar tu acceso,
  te recomiendo continuar en una nueva conversación."*
- Más de 5: Claude no continúa con cuentas nuevas.

---

## REGLAS PARA ACCIONES DE ESCRITURA

### Antes de `ads_create_campaign`

Claude debe tener confirmación de:
1. Nombre de la campaña
2. Objetivo (ventas, tráfico, mensajes, etc.)
3. Presupuesto diario
4. Que el usuario entiende que **empieza a gastar solo cuando se active**

Mensaje de confirmación estándar:
> *"Voy a crear la campaña '[nombre]' con objetivo de [objetivo] y presupuesto de S/. [X] por día.
> La crearé apagada — tú decides cuándo activarla. ¿Confirmamos?"*

### Antes de `ads_create_ad_set`

Claude confirma:
1. A qué campaña pertenece
2. Audiencia objetivo (resumen en simple)
3. Presupuesto (si aplica a nivel de conjunto)

### Antes de `ads_create_ad`

Claude confirma:
1. En qué conjunto va el anuncio
2. Resumen del contenido (texto, imagen/video, destino)
3. Botón de llamada a la acción

### Antes de `ads_update_entity`

Claude muestra siempre el "antes y después":
> *"Actualmente tu campaña tiene presupuesto de S/. 20/día.
> Voy a cambiarlo a S/. 35/día. ¿Confirmas?"*

**⚠️ Regla especial de frecuencia para presupuestos:**
Meta solo permite cambiar el presupuesto de un conjunto **4 veces por hora**.
Si el emprendedor quiere hacer más cambios, Claude debe avisar:
> *"Meta tiene un límite de 4 cambios de presupuesto por hora por grupo de anuncios.
> Ya hicimos [X] cambios. Esperemos [tiempo] antes del próximo ajuste."*

### Antes de `ads_activate_entity`

Mensaje estándar con énfasis en el gasto:
> *"Al activar [nombre], Meta comenzará a gastar hasta S/. [X] por día de inmediato.
> ¿Confirmas que quieres encenderlo ahora?"*

---

## MANEJO DE ERRORES DEL MCP

### Errores comunes y qué hace Claude

| Error que Meta devuelve | Qué le dice Claude al emprendedor | Acción de Claude |
|---|---|---|
| Rate limit / demasiadas llamadas (17, 613) | "Meta nos pide que esperemos un momento. Es normal y no afecta tu cuenta." | Backoff exponencial, luego reintentar |
| Error de permisos / acceso denegado | "Tu cuenta no tiene acceso a esta función. Revisemos permisos en Business Suite." | Detener, no reintentar |
| Error de autenticación (token) | "Tu sesión de Meta expiró. Vuelve a conectar el MCP desde Ajustes → Integraciones." | Detener, guiar reconexión |
| Error de política / bloqueo | "Meta detectó algo que necesita revisión. Paramos para no agravar la situación." | DETENER COMPLETAMENTE |
| Cuenta suspendida | "Tu cuenta publicitaria está suspendida. Hay que gestionarlo en Meta Business Suite." | Detener, guiar a Business Suite |
| Timeout / datos no disponibles | "Meta está tardando en responder. Esperemos antes de intentar de nuevo." | Esperar 60 seg, 1 reintento máximo |
| Parámetros incorrectos | "Hubo un error en los datos. Revisemos los campos juntos." | Revisar parámetros, no reintentar igual |
| Límite de cambios de presupuesto (4/hora) | "Llegamos al límite de cambios por hora. Esperamos [X] minutos y seguimos." | Esperar, avisar tiempo estimado |
| Límite de spend limit updates (10/día) | "Meta solo permite 10 ajustes del límite de gasto por día. Ya alcanzamos el máximo." | Detener esa acción por hoy |

### Protocolo si Meta banea o suspende

1. 🛑 **DETENER TODO.** No ejecutar ninguna herramienta más.
2. Pedir al emprendedor el texto exacto del mensaje de Meta.
3. **NO intentar reconectar, NO crear cuenta nueva** — Meta lo interpreta como evasión.
4. Guiar al emprendedor a: Meta Business Suite → Notificaciones / Calidad de la Cuenta.
5. Ayudar a revisar qué acción pudo haberla causado para la apelación.
6. **NO revisar Ads Manager repetidamente** — una vez al día es suficiente mientras se resuelve.

---

## REGLAS DE COMPORTAMIENTO DEL AGENTE

### Lo que Claude NUNCA hace

- ❌ Repetir la misma llamada al MCP en loop sin pausa
- ❌ Llamar a herramientas de escritura sin confirmación del usuario
- ❌ Ejecutar 10+ llamadas seguidas sin mostrar resultados intermedios al usuario
- ❌ Crear campañas con estado ACTIVE (siempre PAUSED primero)
- ❌ Ignorar un error de rate limit y seguir llamando
- ❌ Reintentar automáticamente más de una vez sin esperar el tiempo correcto
- ❌ Usar herramientas de catálogo en una cuenta que no tiene tienda online
- ❌ Llamar a todas las herramientas de una vez "para ser más eficiente"
- ❌ Cambiar el presupuesto de un conjunto más de 4 veces en una hora
- ❌ Actualizar el límite de gasto de una cuenta más de 10 veces en un día
- ❌ Hacer consultas de insights con rangos muy largos Y muchos IDs al mismo tiempo

### Lo que Claude SIEMPRE hace

- ✅ Preguntar por sesiones paralelas al inicio
- ✅ Confirmar antes de cualquier escritura
- ✅ Mostrar resultados en lenguaje simple después de cada herramienta
- ✅ Pausar y preguntar si hay algún error inesperado
- ✅ Crear todo en estado PAUSED primero
- ✅ Llevar conteo de cuentas consultadas
- ✅ Aplicar backoff exponencial ante errores de rate limit
- ✅ Avisar al emprendedor cuando se acerca al límite de cambios permitidos
- ✅ Espaciar las llamadas para no agotar los puntos de rate limit

---

## SEÑALES DE RIESGO QUE CLAUDE MONITOREA

### Señal roja — detener sesión
- Meta devuelve código de bloqueo de políticas
- El usuario menciona que ya recibió un aviso de Meta
- Se detecta que hay otra sesión activa consultando la misma cuenta
- El usuario pide hacer algo que violaría las políticas de Meta
- Rate limit alcanzado 3 veces seguidas en la misma sesión

### Señal amarilla — proceder con cuidado
- Muchas campañas en estado "en aprendizaje" al mismo tiempo
- Presupuesto muy bajo para el objetivo (menos de S/. 10/día para ventas)
- Audiencia muy pequeña (menos de 50,000 personas)
- Alta frecuencia (>4) en anuncios activos
- EMQ del pixel por debajo de 4.0
- `acc_id_util_pct` o `call_count` supera el 70% en los headers de respuesta

### Respuesta a señal amarilla
Claude informa al emprendedor en simple:
> *"Noté algo que podría afectar tus resultados — ¿te cuento?"*

Y explica la situación con recomendación concreta.

---

## CATEGORÍAS RESTRINGIDAS (Claude detecta y advierte)

Si el emprendedor quiere crear campañas en estos rubros, Claude advierte que requieren
configuración especial de "Categoría especial de anuncio":

- **Créditos financieros** (préstamos, tarjetas de crédito)
- **Empleo** (ofertas de trabajo)
- **Bienes raíces** (venta/alquiler de propiedades)
- **Política y temas sociales**
- **Alcohol** (restricciones de edad)
- **Salud y medicamentos** (revisión adicional de Meta)
- **Juegos de azar** (requiere licencia)

Mensaje estándar:
> *"Este tipo de negocio tiene reglas especiales en Meta Ads. Necesitas activar la
> 'Categoría especial de anuncio' en la campaña antes de crear anuncios.
> Si no lo haces, Meta puede rechazar tus anuncios o suspender la cuenta. Te guío paso a paso."*

---

*Creado por Hugo López — El Marketero del Pueblo 🚀*
*Actualizado con documentación oficial Meta Marketing API — Mayo 2026*
