# Enlaces y mini-guías (para que el emprendedor nunca se pierda)

**Regla:** cada vez que el alumno deba ir a un sitio, dale (1) el enlace exacto, (2) 2-3 pasos cortos y (3) la oferta: "si quieres, lo hacemos juntos: dime qué ves en pantalla". Los menús de Meta y Google cambian seguido: si no ve el botón, pídele que describa su pantalla (o que la comparta) y guíalo. Si un enlace falla, que lo busque por el nombre.

## Dónde se crea cada cosa
| Para qué | Dónde | Enlace |
|---|---|---|
| Hablar con Claude | Claude | https://claude.ai |
| Generar **imágenes y flyers** (Nano Banana 2 **o GPT Image 2.6**, el que tengas) | Gemini, Google AI Studio o ChatGPT | https://gemini.google.com · https://aistudio.google.com · https://chatgpt.com |
| Generar **clips de video** (Omni Flash, avatar @me) | Google Flow | https://labs.google/fx/tools/flow |
| Crear y gestionar **anuncios** | Administrador de anuncios de Meta | https://adsmanager.facebook.com |
| Cuenta, páginas, permisos | Meta Business Suite / Configuración | https://business.facebook.com |
| Revisar **Pixel y eventos** (compras) | Administrador de eventos | https://business.facebook.com/events_manager2 |
| Ver qué anuncios hace la competencia | Biblioteca de anuncios | https://www.facebook.com/ads/library |
| Reglas de publicidad de Meta | Normas de anuncios | https://transparency.meta.com/policies/ad-standards |
| Vender por **WhatsApp** (catálogo, respuestas rápidas) | WhatsApp Business | https://business.whatsapp.com |
| Optimizar anuncios a **compras por WhatsApp** | Guía oficial | https://whatsappbusiness.com/resources/resource-library/down-funnel-optimizations-whatsapp/ |
| Tipografías gratis | Google Fonts | https://fonts.google.com |
| Hoja de ventas | Google Sheets | https://sheets.google.com |

## Mini-guías de 3 pasos
**Generar una imagen (Nano Banana 2 o GPT Image 2.6):** 1) abre Gemini en https://gemini.google.com (o ChatGPT si usas GPT Image 2.6) 2) adjunta las referencias en el **orden** que indica tu **Guía de generación** (pestaña del Panel) 3) pega el prompt y elige formato 9:16 (video) o 4:5 (feed). Pide siempre en español. Para que se vea real, usa **fotos reales de tu local o producto** como referencia: la IA las mejora y reencuadra, no las inventa.

**Subir lo que generaste:** en la pestaña **Guía de generación** arrastra el archivo al cuadro de su paso (se guarda solo en tu computadora y Claude lo revisa). Si el panel no tiene subida, doble clic en `Panel/iniciar-panel.bat`.

**Generar un clip (Omni Flash en Flow):** 1) abre https://labs.google/fx/tools/flow 2) crea un proyecto y carga las referencias en el orden indicado (tu avatar se invoca con `@me`) 3) pega el prompt del clip, duración indicada, y descarga el MP4 a la carpeta `Tomas/` o `Entregables/.../video/clips/`. Si el clip sale con texto o música generados, vuelve a generarlo: el texto y la música se ponen en la edición.

**Abrir tu Administrador de anuncios:** 1) entra a https://adsmanager.facebook.com 2) arriba a la izquierda elige tu **cuenta publicitaria** 3) pulsa **Crear**. Antes confirma que ves tu Página y tu WhatsApp conectados (Configuración del negocio).

**Ver si tu Pixel y tus compras llegan a Meta:** 1) https://business.facebook.com/events_manager2 2) elige tu conjunto de datos (Pixel) 3) mira "Eventos recibidos" y busca **Purchase/Compra**. Para ventas cerradas por **WhatsApp** no necesitas la API de Conversiones: marca cada compra como **"Pagado"** en la bandeja de Business Suite (ver la guía de abajo).

**Conectar WhatsApp a Meta Business Suite y habilitar "compras por mensajes":** 1) conecta tu número de WhatsApp Business en https://business.facebook.com (bandeja de entrada) 2) activa el **uso compartido de datos** de WhatsApp hacia Meta 3) marca como **"Pagado"** (o pedido completado) a ~10 clientes que lleguen de anuncios; en tu siguiente conjunto aparecerá "Maximizar el número de compras a través de mensajes". Guía completa: `meta-ads-andromeda/references/guia-whatsapp-y-prueba-de-anuncios.md`.

**Probar anuncios en igualdad de condiciones:** en cada anuncio usa el **impulso de la entrega** (un % del presupuesto diario del conjunto durante 7 días). Misma guía.

## Cosas que el alumno NO debe hacer
- Pegar claves, contraseñas o tokens en el chat. Si algo las pide, el director indica el lugar exacto donde pegarlas.
- "Publicar en la web" una hoja con datos de clientes. Compartir con permiso por correo, o con un script con clave.
- Usar músicas, logos o fotos que no sean suyos o con licencia.

## Para subir de nivel
- **Video pro:** módulo Video (Fábrica de Video) del mismo paquete.
- **Tablero de métricas de TikTok:** plantilla pública https://github.com/pruebacursoads/tablero-tiktok-plantilla
- **Landing, CRM de WhatsApp y dashboard de ventas:** los entrega el profesor en la clase (ver `docs/` del paquete); no se instalan solos.
