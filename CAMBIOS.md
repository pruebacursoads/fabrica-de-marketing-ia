# Cambios

## 1.1.0 (2026-11-13)
Aprendido en la prueba "ternos" (Centro de Lima, avatar @me, 2 clips de 10 s): plano fijo, local que parecía un atelier de película, prompts "al aire" y continuidad por último fotograma.
- **Panel**: oficina 3D isométrica (CSS puro, sin internet); nombres de zona pintados en el piso y letreros en la pared; etiquetas compactas. Nueva pestaña **Guía de generación** (prompts con botón copiar, referencias en orden con miniatura, cuadros para subir archivos, vista previa, veredicto de Claude).
- **Servidor local** (`servidor.py`, `iniciar-panel.bat/.sh`): subir archivos arrastrando; se guardan en la carpeta y con el nombre correctos; versión anterior a `_anteriores/`; solo 127.0.0.1.
- **Vigilante** (`vigilar.py`): Claude lee lo que se sube en tiempo real (herramienta Monitor) y responde con `reportar.py revision`.
- `reportar.py`: nuevos comandos `guia`, `medios`, `revision`.
- **Video**: `omni-flash-prompts/references/multi-toma-y-realismo.md` (varias tomas, continuidad por escena sin último fotograma, fotos reales, GPT Image 2.6 o Nano Banana 2). `fm-agente-video` reescrito; `fm-agente-imagenes`, `fm-agente-carruseles`, `fm-agente-revisor`, `fm-director`, `fm-adn`, `fv-editor` actualizados.
- Todos los agentes publican sus prompts y pasos manuales en la Guía (protocolo común, punto 8).
- **Distribución y actualización 100 % desde GitHub:** `publicar.py` (valida que no se cuele nada privado y sube cada mejora), skill `fm-actualizar` (el director avisa de versiones nuevas y las instala con permiso), instaladores que registran la versión instalada, y un Prompt 0 para instalar directo desde el repositorio.
