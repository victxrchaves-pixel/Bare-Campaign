# Bare — Plan de Implementación Campaña Prelanzamiento RRSS

> **Para quien ejecute este plan:** Completa cada tarea en orden. Cada tarea produce un entregable concreto (copies, briefs, calendarios). Marca cada paso al completarlo.

**Goal:** Producir todos los contenidos, copies y calendarios de la campaña de prelanzamiento de Bare para Instagram y TikTok, con el objetivo de conseguir 200 personas en waitlist en 3 meses.

**Architecture:** 3 fases (Marca → Waitlist → Cierre) · 5 pilares de contenido · tono Manifiesto/Bold · FOMO con números reales.

**Entregables:** Documentos de copy, briefs visuales y calendarios semana a semana listos para producción.

---

## Estructura de archivos

```
Campaign/RRSS/
├── docs/specs/2026-05-01-campana-prelanzamiento-design.md  ← spec aprobado
├── docs/plans/2026-05-01-campana-prelanzamiento.md         ← este archivo
├── Mes1-Marca/
│   ├── 01-brief-identidad-visual.md
│   ├── 02-copies-manifiesto.md
│   ├── 03-brief-teaser-ui.md
│   └── 04-calendario-semanas1-4.md
├── Mes2-Waitlist/
│   ├── 05-copies-explicativo.md
│   ├── 06-copies-fomo.md
│   ├── 07-copies-contraste.md
│   └── 08-calendario-semanas5-8.md
└── Mes3-Cierre/
    ├── 09-copies-urgencia.md
    └── 10-calendario-semanas9-12.md
```

---

## Task 1: Brief de identidad visual

**Archivo:** Crear `Mes1-Marca/01-brief-identidad-visual.md`

- [ ] **Paso 1: Crear el brief visual**

Contenido exacto del archivo:

```markdown
# Brief de Identidad Visual — Bare Campaign

## Paleta
- Fondo principal: #0A0A0A (negro casi puro)
- Texto principal: #FFFFFF (blanco puro)
- Acento: #F5F4F0 (crema, para fondos alternativos)
- Nunca usar grises intermedios como protagonistas

## Tipografía
- Titular: Sans-serif bold condensada (ej. Arial Black, Helvetica Neue Black, o equivalente)
  - Tamaño: lo más grande que quepa con márgenes mínimos
  - Casing: MAYÚSCULAS siempre en declaraciones principales
- Subtítulo/firma: Sans-serif light o regular, tracking amplio (letter-spacing alto)
  - Ejemplo: "bare · waitlist abierta" en versalitas

## Layout
- Márgenes generosos: mínimo 8% del ancho total por lado
- Nunca más de 7 palabras por línea en titulares
- Alineación: izquierda o centrada — nunca justificada
- Sin degradados, sin sombras, sin efectos
- Si hay imagen: blanco y negro, alto contraste, nunca color

## Proporción de formatos
- IG Feed: 1:1 (1080×1080px) o 4:5 (1080×1350px)
- IG Stories / TK: 9:16 (1080×1920px)
- IG Carrusel: 1:1, máximo 7 slides

## Reglas de producción
1. Nunca usar más de 2 fuentes en una pieza
2. El nombre "Bare" siempre en minúscula
3. Nunca añadir ilustraciones decorativas — solo tipografía y UI
4. Si hay un CTA, va en la última línea, separado por un espacio o línea divisoria
5. Ninguna pieza puede parecer un anuncio pagado — aspecto editorial siempre
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes1-Marca/01-brief-identidad-visual.md
git commit -m "feat: add visual identity brief for Bare campaign"
```

---

## Task 2: Banco de copies — Pilar Manifiesto

**Archivo:** Crear `Mes1-Marca/02-copies-manifiesto.md`  
**Uso:** Mes 1 (semanas 1–4) y Mes 3 (semanas 9–12)

- [ ] **Paso 1: Crear el banco de copies**

```markdown
# Copies — Pilar Manifiesto

Reglas de uso:
- Máximo 1 post de Manifiesto cada 2 días en IG feed
- En TK: pueden usarse como texto animado sobre fondo negro, 5–8 segundos
- Nunca añadir explicación debajo — la declaración se sostiene sola
- Firma siempre: "bare" en minúscula, con tracking amplio

---

## Bloque A — Identidad (Mes 1, sin CTA)

### A1
```
NO ES UN PORTFOLIO.
NO ES UN MARKETPLACE.
NO ES INSTAGRAM.

bare
```

### A2
```
UNA SOLA PLATAFORMA.
ACCESO POR REVISIÓN
HUMANA.
NADA MÁS.

bare
```

### A3
```
BARE.
PRONTO.
```
*(usar en la primera semana, antes de revelar nada)*

### A4
```
EL TRABAJO BIEN HECHO
ES ENCONTRABLE
SIN PAGAR POR ELLO.

bare
```

### A5
```
TU TRABAJO ENTRA.
O NO.
LO DECIDE UN EQUIPO,
NO UN ALGORITMO.

bare
```

### A6
```
AQUÍ NO HAY
FRECUENCIA MÍNIMA.
NO HAY LIKES.
NO HAY FEED.

bare
```

### A7
```
EL ACCESO SE GANA
POR LO QUE HACES.
NO POR LO QUE
PUBLICAS.

bare
```

---

## Bloque B — Urgencia (Mes 3, con CTA)

### B1
```
QUEDAN [X] PLAZAS.
BARE ABRE EL [FECHA].

waitlist en bio
```

### B2
```
LA WAITLIST CIERRA
ANTES DEL LANZAMIENTO.

LOS QUE NO ESTÉN
DENTRO, ESPERAN.

bare · link en bio
```

### B3
```
[X] DE 200.
YA CASI.

bare · waitlist en bio
```

### B4
```
ÚLTIMAS SEMANAS.
DESPUÉS, SOLO LISTA
DE ESPERA.

bare · waitlist en bio
```

---

## Para TikTok (adaptación texto animado)

Cada declaración se convierte en texto apareciendo palabra a palabra sobre fondo negro.
Duración: 5–8 segundos por declaración.
Audio: silencio o sonido ambiente mínimo (sin música con letra).
Cierre: "bare" aparece en último frame, permanece 2 segundos.

Copies prioritarios para TK (los más directos):
- A1, A2, A5, B2
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes1-Marca/02-copies-manifiesto.md
git commit -m "feat: add manifiesto copy bank — blocks A and B"
```

---

## Task 3: Brief de Teaser UI

**Archivo:** Crear `Mes1-Marca/03-brief-teaser-ui.md`  
**Uso:** Mes 1 (semanas 1–4) y Mes 3 como fondo de urgencia

- [ ] **Paso 1: Crear el brief**

```markdown
# Brief — Pilar Teaser UI

## Objetivo
Mostrar la interfaz de Bare para generar deseo del producto sin revelar usuarios reales.
No es una demo — es una seducción visual.

## Qué pantallas mostrar (por orden de impacto)

### Pantalla 1 — El buscador vacío
Vista del buscador de creativos con los filtros visibles: disciplina, paleta, técnica, atmósfera.
Sin resultados cargados. Solo la arquitectura del filtro.
Copy superpuesto: "FILTRA POR PALETA. POR TÉCNICA. POR ATMÓSFERA."

### Pantalla 2 — El perfil en blanco
Un perfil de creador vacío, limpio, con la estructura visible.
Proyectos como bloques sin contenido. La arquitectura del portfolio.
Copy superpuesto: "TU TRABAJO. EN UN SOLO LUGAR."

### Pantalla 3 — El archivo
Vista del módulo de inspiración curada. Grilla de referencias, sin imágenes.
Solo la estructura y los metadatos de una referencia (paleta, técnica, contexto).
Copy superpuesto: "INSPIRACIÓN CON CONTEXTO. NO ACUMULACIÓN."

### Pantalla 4 — El acceso
Pantalla del proceso de revisión. El formulario de envío de proyecto.
Copy superpuesto: "ENVÍAS UN PROYECTO. LO REVISAMOS. ENTRAS O NO."

## Tratamiento visual de las pantallas
- Todas en modo oscuro
- Convertir a blanco y negro si el diseño usa color
- Superponer texto en tipografía de campaña (bold, blanco, mayúsculas)
- Añadir firma "bare" en esquina inferior izquierda

## Formatos a producir por pantalla
- 1 post IG feed (1080×1080px)
- 1 story/TK vertical (1080×1920px) — texto animado sobre la pantalla

## Cadencia de publicación
- 1 Teaser UI por semana en Mes 1
- 2 Teaser UI en Mes 3 (como fondo de urgencia con copy de cierre)
- Nunca publicar dos el mismo día
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes1-Marca/03-brief-teaser-ui.md
git commit -m "feat: add teaser UI brief with screen priorities"
```

---

## Task 4: Calendario Mes 1 (Semanas 1–4)

**Archivo:** Crear `Mes1-Marca/04-calendario-semanas1-4.md`

- [ ] **Paso 1: Crear el calendario**

```markdown
# Calendario Mes 1 — Construir Marca
## Semanas 1–4 · Sin CTA de waitlist

Leyenda:
- [M] = Manifiesto
- [UI] = Teaser UI
- [S] = Story

---

## Semana 1 — Aparición

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | [M] Copy A3 "BARE. PRONTO." | [S] Fondo negro, "bare" centrado | — |
| Miércoles | — | [S] Detalle tipografía del logo | [M] A3 animado (5s) |
| Viernes | [UI] Pantalla 1 — Buscador vacío | [S] Zoom al buscador | — |

*Objetivo semana 1: que el nombre Bare empiece a circular sin contexto. Intriga pura.*

---

## Semana 2 — Declaración

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | [M] Copy A1 "NO ES UN PORTFOLIO..." | [S] Repetir copy A1 en formato vertical | [M] A1 animado (7s) |
| Miércoles | [UI] Pantalla 2 — Perfil en blanco | [S] Detalle perfil vacío | — |
| Viernes | [M] Copy A2 "UNA SOLA PLATAFORMA..." | [S] Copy A2 vertical | [M] A2 animado (8s) |

---

## Semana 3 — Profundidad

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | [M] Copy A4 "EL TRABAJO BIEN HECHO..." | [S] A4 vertical | — |
| Miércoles | [UI] Pantalla 3 — Archivo | [S] Zoom metadatos del archivo | [UI] Walkthrough archivo (15s) |
| Viernes | [M] Copy A6 "AQUÍ NO HAY FRECUENCIA MÍNIMA..." | [S] A6 vertical | [M] A6 animado |

---

## Semana 4 — Acceso (anticipo)

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | [M] Copy A5 "TU TRABAJO ENTRA O NO..." | [S] A5 vertical | [M] A5 animado |
| Miércoles | [UI] Pantalla 4 — Proceso de acceso | [S] "La semana que viene, más." | — |
| Viernes | [M] Copy A7 "EL ACCESO SE GANA..." | [S] Countdown 7 días para "algo" | [M] A7 animado |

*Semana 4: empezar a insinuar que algo pasa la semana siguiente (apertura de waitlist). No decirlo explícitamente — solo el Story de Viernes con countdown.*

---

## KPIs a seguir en Mes 1
- Seguidores IG ganados: objetivo +250
- Seguidores TK ganados: objetivo +150
- Alcance total estimado: depende del punto de partida — anotar benchmark semana 1
- Engagement rate objetivo IG: >4%
- Engagement rate objetivo TK: >6%
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes1-Marca/04-calendario-semanas1-4.md
git commit -m "feat: add Mes1 content calendar weeks 1-4"
```

---

## Task 5: Copies — Pilar Explicativo

**Archivo:** Crear `Mes2-Waitlist/05-copies-explicativo.md`  
**Uso:** Mes 2 (semanas 5–8), formato carrusel IG y video TK

- [ ] **Paso 1: Crear copies**

```markdown
# Copies — Pilar Explicativo

## Carrusel IG — "Qué es Bare y cómo funciona" (7 slides)

**Slide 1 (portada):**
```
QUÉ ES BARE
Y CÓMO FUNCIONA
EL ACCESO.
```

**Slide 2:**
```
BARE ES UNA PLATAFORMA
PARA CREADORES VISUALES.

Archivo de inspiración.
Portfolio profesional.
Directorio de contacto.

Todo en un lugar.
```

**Slide 3:**
```
NO ES ABIERTA.

Para entrar, envías
un proyecto.
Lo revisa un equipo.
Entras o no.
```

**Slide 4:**
```
¿QUÉ SE EVALÚA?

La calidad del trabajo.
La coherencia de la propuesta.
Nada más.

No el número de seguidores.
No el tiempo en el sector.
```

**Slide 5:**
```
UNA VEZ DENTRO:

— Tu portfolio organizado
  por proyectos completos.

— Un archivo de referencias
  filtrable por paleta, técnica
  y atmósfera.

— Contacto directo con clientes
  y otros creadores.
  Sin intermediarios.
```

**Slide 6:**
```
LA BÚSQUEDA FUNCIONA
DE OTRA FORMA.

Un cliente busca:
"Ilustración · paleta tierra · 
proceso a mano · atmósfera calmada"

Y encuentra exactamente eso.
No el perfil más seguido.
El trabajo más preciso.
```

**Slide 7 (CTA):**
```
WAITLIST ABIERTA.
30 PLAZAS ESTA SEMANA.

bare · link en bio
```

---

## Video TK — "Por qué la revisión humana" (30–45s)

**Guión:**

[0–5s] Texto en pantalla: "¿Por qué no puede entrar cualquiera?"
[5–15s] Voz en off o texto animado:
"Porque si entra cualquiera, el nivel del conjunto baja.
Y Bare existe exactamente para que eso no pase."
[15–25s] Texto: "Envías un proyecto. Lo revisamos.
No buscamos el más famoso. Buscamos el más riguroso."
[25–35s] Texto: "Si no entras ahora, puedes volver a intentarlo."
[35–45s] CTA: "Waitlist abierta. 30 plazas esta semana. Link en bio."

---

## Video TK — "Qué pasa cuando entras" (20–30s)

**Guión:**

[0–5s] "Esto es lo que tienes cuando entras en Bare."
[5–10s] Pantalla: buscador con filtros
[10–15s] Pantalla: perfil con proyectos
[15–20s] Pantalla: archivo de referencias
[20–25s] "Sin algoritmo. Sin frecuencia mínima. Solo tu trabajo."
[25–30s] CTA: "Waitlist. Link en bio."
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/05-copies-explicativo.md
git commit -m "feat: add explicativo copies — IG carousel and TK scripts"
```

---

## Task 6: Copies — Pilar FOMO / Escasez

**Archivo:** Crear `Mes2-Waitlist/06-copies-fomo.md`  
**Uso:** Mes 2 (semanas 5–8) y Mes 3 (semanas 9–12)

- [ ] **Paso 1: Crear copies**

```markdown
# Copies — Pilar FOMO / Escasez

## Regla de oro
Los números siempre son reales. Nunca publicar un número que no sea el actual.
Actualizar los templates cada semana con datos reales antes de publicar.

---

## Templates de Story IG — Apertura de lote semanal

### Apertura (lunes de cada semana, Mes 2)
```
ABRIMOS LOTE [N].
30 PLAZAS ESTA SEMANA.

[día de cierre, ej: "Cierran el domingo."]

bare · waitlist en bio
```

### Mid-week (miércoles)
```
[X] PLAZAS OCUPADAS.
QUEDAN [30-X].

bare · link en bio
```

### Cierre (domingo)
```
LOTE [N] CERRADO.
[X] PLAZAS OCUPADAS DE 30.

EL PRÓXIMO LOTE,
EL LUNES.

bare
```

---

## Posts IG Feed — Hitos de waitlist

### Al llegar a 50 personas
```
50 DENTRO.

QUEDAN 150 PLAZAS
HASTA EL LANZAMIENTO.

bare · waitlist en bio
```

### Al llegar a 100 personas
```
LA MITAD.

100 CREADORES
YA EN BARE.

100 PLAZAS MÁS.
DESPUÉS, SOLO LISTA
DE ESPERA.

bare · waitlist en bio
```

### Al llegar a 150 personas
```
150.

50 PLAZAS PARA
CERRAR LA WAITLIST.

bare · waitlist en bio
```

---

## Videos TK — FOMO

### "Por qué cerramos la waitlist antes de lanzar" (20s)
[0–5s] "Bare cierra la waitlist antes del lanzamiento."
[5–10s] "No porque esté llena. Porque queremos que el primer día tenga el nivel correcto."
[10–15s] "Los que estén dentro, entran el día 1."
[15–20s] "Los que no, esperan. Waitlist en bio."

### Countdown final (Mes 3, 15s)
[0–5s] "Quedan [X] plazas."
[5–10s] "Bare abre el [fecha]."
[10–15s] "Link en bio."

---

## Cadencia de publicación FOMO

| Semana | Lunes | Miércoles | Domingo |
|---|---|---|---|
| 5–8 (Mes 2) | Story apertura lote | Story mid-week | Story cierre lote |
| 9–11 (Mes 3) | Post feed hito | Story plazas restantes | Story urgencia |
| 12 (última) | Post feed cierre | Story "últimas 24h" | Post cierre oficial |
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/06-copies-fomo.md
git commit -m "feat: add FOMO copy bank with weekly templates"
```

---

## Task 7: Copies — Pilar Contraste

**Archivo:** Crear `Mes2-Waitlist/07-copies-contraste.md`  
**Uso:** Mes 2 únicamente, máximo 1 pieza cada 2 semanas (total: 2 piezas)

- [ ] **Paso 1: Crear copies**

```markdown
# Copies — Pilar Contraste

## Reglas de uso
- MÁXIMO 2 piezas en todo Mes 2 (semana 6 y semana 8)
- Nunca en Mes 1 ni Mes 3
- El problema es el telón de fondo — una frase, no un sermón
- Siempre termina con Bare como respuesta directa

---

## Pieza 1 — Semana 6 (IG feed)

```
TIENES 4 PESTAÑAS
ABIERTAS MIENTRAS
INTENTAS CREAR.

BARE ES UNA.

waitlist en bio
```

**TK (20s):**
[0–5s] "¿Cuántas apps tienes abiertas ahora mismo para gestionar tu trabajo?"
[5–10s] "Pinterest. Behance. Instagram. LinkedIn."
[10–15s] "Bare es una sola."
[15–20s] "Waitlist en bio."

---

## Pieza 2 — Semana 8 (IG feed)

```
EL 78% DEL TIEMPO
DE UN CREADOR VA
A AUTOPROMOCIÓN.

EL 22% A CREAR.

BARE NO LO SOLUCIONA.
PERO LO REDUCE.

waitlist en bio
```

**Nota:** Este copy usa el dato real de Hesmondhalgh (2013) del Marco Teórico.
No inventar datos. Si se actualiza el dato, actualizar el copy.
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/07-copies-contraste.md
git commit -m "feat: add contraste copy — 2 pieces for Mes 2"
```

---

## Task 8: Calendario Mes 2 (Semanas 5–8)

**Archivo:** Crear `Mes2-Waitlist/08-calendario-semanas5-8.md`

- [ ] **Paso 1: Crear el calendario**

```markdown
# Calendario Mes 2 — Revelar + Waitlist
## Semanas 5–8 · Apertura de waitlist en lotes de 30

---

## Semana 5 — Apertura

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | Carrusel "Qué es Bare" (7 slides) | Story apertura Lote 1: "30 plazas esta semana" | Video "Qué pasa cuando entras" (20s) |
| Miércoles | — | Story mid-week: "[X] plazas ocupadas, quedan [Y]" | — |
| Viernes | [M] Copy A5 (recordatorio identidad) | — | Video "Por qué la revisión humana" (40s) |
| Domingo | — | Story cierre Lote 1 | — |

*Acción previa semana 5: publicar Story el domingo de la semana 4 con "Mañana abrimos algo."*

---

## Semana 6 — Contraste + Lote 2

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | — | Story apertura Lote 2 | — |
| Miércoles | [C] Pieza contraste 1 "4 PESTAÑAS ABIERTAS" | Story mid-week plazas | [C] TK contraste 1 (20s) |
| Viernes | [UI] Pantalla 2 perfil (con CTA) | — | — |
| Domingo | — | Story cierre Lote 2 | — |

---

## Semana 7 — Hito 50/100 + Lote 3

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | — | Story apertura Lote 3 | — |
| Miércoles | Post hito (50 o 100 según avance real) | Story mid-week | Video TK "Por qué cerramos antes de lanzar" |
| Viernes | [M] Copy A7 con CTA | — | — |
| Domingo | — | Story cierre Lote 3 | — |

---

## Semana 8 — Contraste 2 + Lote 4 + anticipo Mes 3

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | — | Story apertura Lote 4 | — |
| Miércoles | [C] Pieza contraste 2 "78% autopromoción" | Story mid-week | [C] TK contraste 2 |
| Viernes | Post: "El mes que viene, cerramos." | Story: "Próximo mes, countdown." | TK: anticipo cierre |
| Domingo | — | Story cierre Lote 4 | — |

---

## KPIs a seguir en Mes 2
- Plazas waitlist ocupadas: objetivo 120 al final de semana 8
- Tasa de conversión visita bio → waitlist: registrar desde semana 5
- Lotes agotados en <72h: objetivo 3 de 4 lotes
- Seguidores IG: +400 acumulados desde inicio
- Seguidores TK: +250 acumulados desde inicio
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes2-Waitlist/08-calendario-semanas5-8.md
git commit -m "feat: add Mes2 content calendar weeks 5-8"
```

---

## Task 9: Copies — Urgencia y Cierre

**Archivo:** Crear `Mes3-Cierre/09-copies-urgencia.md`

- [ ] **Paso 1: Crear copies**

```markdown
# Copies — Mes 3: Urgencia y Cierre

## Hitos de comunicación del Mes 3

### Inicio Mes 3 — "Último mes"
**IG Feed:**
```
ÚLTIMO MES
DE WAITLIST.

DESPUÉS DE [FECHA CIERRE],
SOLO LISTA DE ESPERA.

bare · link en bio
```

**TK (15s):**
"Bare cierra la waitlist en [X] semanas.
Después del [fecha], si no estás dentro, esperas.
Link en bio."

---

### Semana 10 — Countdown visible
**Story IG (publicar diariamente):**
```
[X] DÍAS PARA
EL CIERRE.

[Y] PLAZAS RESTANTES.

bare · link en bio
```

**IG Feed:**
```
[X] PLAZAS.
[Y] DÍAS.

bare · waitlist en bio
```

---

### Semana 11 — Últimas 30 plazas
**IG Feed:**
```
ÚLTIMAS 30 PLAZAS.

BARE ABRE EL [FECHA].
LA WAITLIST CIERRA
ANTES.

bare · link en bio
```

**TK (20s):**
"Quedan 30 plazas en la waitlist de Bare.
Después de esto, lista de espera.
La plataforma abre con quien esté dentro.
Link en bio."

---

### Cierre oficial — Día de cierre de waitlist
**IG Feed:**
```
WAITLIST CERRADA.

200 CREADORES
DENTRO.

BARE ABRE EL [FECHA].
```

**Story IG:**
```
CERRADO.
NOS VEMOS EL [FECHA].
```

**TK (15s):**
"La waitlist de Bare está cerrada.
200 creadores dentro.
Bare abre el [fecha].
Gracias."

---

## Reglas de Mes 3
1. Stories diarias desde semana 10 con días y plazas restantes (siempre datos reales)
2. No publicar más de 1 post de feed de urgencia cada 3 días (evitar saturar)
3. El tono se mantiene: sobrio, directo, nunca agresivo ni "¡última oportunidad!"
4. El día del cierre: un solo post. Limpio. Sin celebración excesiva.
```

- [ ] **Paso 2: Commit**

```bash
git add Campaign/RRSS/Mes3-Cierre/09-copies-urgencia.md
git commit -m "feat: add urgency and closing copies for Mes3"
```

---

## Task 10: Calendario Mes 3 (Semanas 9–12)

**Archivo:** Crear `Mes3-Cierre/10-calendario-semanas9-12.md`

- [ ] **Paso 1: Crear el calendario**

```markdown
# Calendario Mes 3 — Cierre y Urgencia
## Semanas 9–12 · Countdown al lanzamiento

---

## Semana 9 — Inicio del countdown

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | Post "Último mes de waitlist" | Story: "quedan [X] plazas" | TK "Cierre en 1 mes" (15s) |
| Miércoles | [UI] Pantalla 1 con copy urgencia | Story: countdown días | — |
| Viernes | [M] Copy B1 (adaptado con fecha real) | Story countdown | [M] B1 animado |

---

## Semana 10 — Subida de tensión

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | Post hito (150 si no se alcanzó antes) | Story diaria: días + plazas | TK countdown (15s) |
| Miércoles | [M] Copy B2 "La waitlist cierra antes..." | Story diaria | — |
| Viernes | [UI] Pantalla 4 proceso acceso + CTA urgente | Story diaria | TK "últimas semanas" |

---

## Semana 11 — Últimas 30 plazas

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | Post "Últimas 30 plazas" | Story diaria | TK "quedan 30 plazas" (20s) |
| Miércoles | [M] Copy B3 "[X] de 200" | Story diaria | — |
| Viernes | Post: "La semana que viene, cerramos." | Story diaria | TK cierre próximo |

---

## Semana 12 — Cierre

| Día | IG Feed | IG Stories | TikTok |
|---|---|---|---|
| Lunes | [M] Copy B4 "Últimas semanas" | Story: "quedan [X] días y [Y] plazas" | TK urgencia máxima (15s) |
| Miércoles | — | Story: "últimas 48h" | TK: "últimas 48h" |
| Jueves | — | Story: "últimas 24h" | — |
| Viernes [CIERRE] | Post cierre oficial "WAITLIST CERRADA. 200 CREADORES DENTRO." | Story cierre | TK cierre (15s) |

---

## KPIs a cerrar en Mes 3
- Waitlist completada: 200 personas ✓
- Último lote agotado antes del día de cierre
- Seguidores IG al cierre: +1.000 desde inicio campaña
- Seguidores TK al cierre: +500 desde inicio campaña
- Tasa de lotes agotados en <72h durante Mes 3: objetivo 100%
```

- [ ] **Paso 2: Commit final**

```bash
git add Campaign/RRSS/Mes3-Cierre/10-calendario-semanas9-12.md
git commit -m "feat: add Mes3 content calendar weeks 9-12"
git push origin main
```

---

## Checklist de prerequisitos antes de publicar

- [ ] Mockups de UI de las 4 pantallas listos y en blanco/negro
- [ ] Landing page / formulario de waitlist operativo
- [ ] Sistema de gestión de plazas configurado (para contar en tiempo real)
- [ ] Cuenta IG y TK creadas con bio y link en bio activos
- [ ] Fecha de lanzamiento aproximada confirmada (necesaria desde Mes 3)
- [ ] Cuenta para actualizar Stories de countdown diariamente en Mes 3
