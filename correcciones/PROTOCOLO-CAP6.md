# PROTOCOLO-CAP6 — Experimento del Ejemplo de Aplicación (Capítulo 6)

| Campo | Valor |
|---|---|
| **Código** | PROTOCOLO-CAP6 |
| **Fecha** | 29 de octubre de 2026 |
| **Estado** | Borrador — marco validado por el director (estrategia (a): corrida nueva controlada). Pendiente: validación de DEC-1 a DEC-6 |
| **Objetivo vinculado** | OE4 — validar el framework mediante un caso de aplicación concreto, analizando calidad de resultados y limitaciones (escalabilidad, fidelidad documental, costo computacional) |
| **Documentos base** | REV-002 (estado del documento), RUTA-001 (fases), cap. 4 de `main.tex` (materialización), addon `noticias_iag` (implementación de referencia, commit `bca7dba`, 27 tests) |
| **Secciones del cap. 6 que alimenta** | 6.1 Selección del caso · 6.2 Configuración inicial · 6.3 Ejecución del scraping · 6.4 Contexto y template · 6.5 Resultados · 6.6 Discusión |

---

## 1. Objetivo del experimento

Producir evidencia empírica de una corrida completa y real del framework sobre noticias de portales digitales regionales, suficiente para:

1. Escribir el Capítulo 6 con datos reales y trazables (ningún número sin artefacto que lo respalde).
2. Completar las 6 celdas "(por completar)" de la matriz maestra [A]-[F] con la realización en el caso.
3. Discutir las limitaciones en los tres términos del OE4: **escalabilidad**, **fidelidad documental** y **costo computacional**.

**Alcance epistemológico:** es un estudio de caso instrumental sobre una ejecución real, no un experimento controlado de efectividad pedagógica o analítica. Verbos permitidos en el capítulo: "demuestra factibilidad bajo las condiciones probadas", "documenta", "identifica". Prohibidos: "prueba la efectividad", "demuestra que el framework mejora X" (sin grupo de control no hay inferencia causal).

## 2. Diseño general

- **Unidad de análisis:** un *estudio* (template + sintonizadores) sobre un corpus de noticias del repositorio institucional.
- **Corrida A (principal):** caso único definido en §3.
- **Corrida B (opcional, DEC-6):** mismo corpus, template distinto → evidencia directa de [B] independencia del estudio (el framework no cambia; cambia solo la declaración del estudio).
- **Referencia comparativa:** Estudios 32 y 59 preexistentes (conformidad 9/13 sin restricción de esquema vs 13/13 con restricción; 347 s vs 570 s). Se citan como antecedente en condiciones no equivalentes, nunca como medición propia.
- **Secuencia anti-anclaje:** el revisor humano verifica ANTES de conocer los veredictos del juez generativo (reduce sesgo de anclaje; habilita comparar ambos juicios en §6.6).

## 3. Definición del caso (decisiones pendientes)

| ID | Decisión | Quién propone | Quién valida | Recomendación |
|---|---|---|---|---|
| **DEC-1** | Portales y período del corpus (portales ya monitorizados en el entorno CAETI/CIM) | Lucio | Alejandro | Período acotado y reciente (ej. 2-4 semanas), portales de prioridad activa |
| **DEC-2** | Tamaño del corpus (N noticias) | Lucio | Alejandro | N = 40-80: suficiente para composiciones M>1 y análisis de conformidad; acota costo y tiempo de revisión humana. El N exacto lo fija el recorte temporal real |
| **DEC-3** | Pregunta de análisis y template (objetivo, instrucciones, variables, esquema JSON de respuesta) | Lucio | Alejandro | Alineado al marco teórico (agenda-setting de segundo nivel / atributos del discurso). El esquema debe ser lo bastante restrictivo para evaluar conformidad, lo bastante abierto para no trivializar el análisis |
| **DEC-4** | Revisor humano (control editorial [D]) y rúbrica de fidelidad | Lucio/Alejandro | Alejandro | Opciones: Lucio con rúbrica explícita (documentada en §6.4), o experto de dominio CAETI si está disponible. La rúbrica se define ANTES de revisar |
| **DEC-5** | Proveedor y modelos (generativo + embedding), con versión y fecha | Lucio | Alejandro | Registrar modelo exacto y fecha de corrida; presupuestar costo estimado antes de ejecutar (§7) |
| **DEC-6** | ¿Corrida B (segundo template sobre el mismo corpus)? | Hermes/Alejandro | Alejandro | Recomendada si el presupuesto lo permite: ~1x costo adicional de corrida A, evidencia fuerte para [B] y OE3 |

## 4. Configuración técnica fijada

- **Entorno:** Odoo del entorno CAETI/CIM con el addon `noticias_iag`. Registrar el commit exacto usado en la corrida (referencia: `bca7dba` o posterior).
- **Extracción [F]:** scraper institucional preexistente, sin modificaciones. El corpus se recorta por portal+período desde el repositorio; registrar el estado del repositorio antes de la corrida (total de noticias del período).
- **Modo de salida estructurada:** con restricción de esquema activada (evidencia de Estudios 32/59: eleva la conformidad). Registrar la política de degradación del adaptador y si se activó.
- **Verificación [D]:** doble juicio — JuezGenerativo (LLM-as-a-judge, criterio y ejecutor por sintonizador) + revisor humano sobre el 100% de los análisis, en la secuencia anti-anclaje del §2.
- **Normalización:** condición de inclusión declarada en el estudio; variable de comparación registrada.
- **Sintonizadores [A]:** capturar los cuatro (Extracción no aplica si el corpus es recorte; Composición, Verificación, Normalización) con sus valores exactos.

## 5. Procedimiento de ejecución (paso a paso)

0. **Precondiciones:** portales activos y monitorizados; acceso al entorno; DEC-1..5 validadas y congeladas por escrito.
1. **Recorte del corpus:** exportar `corpus.csv` (id de noticia, portal, fecha, título, URL). Registrar fecha/hora del recorte.
2. **Creación del estudio:** template + sintonizadores. Exportar configuración (sin credenciales) y capturar pantallas de las solapas [A].
3. **Composición:** ejecutar el filtro; registrar M unidades generadas y los prompts emitidos (exportar desde el repositorio).
4. **Invocación:** registrar tiempos de comienzo/fin por unidad, respuestas crudas, fallas y reintentos (el informe del filtro ya los captura — exportarlo).
5. **Decodificación:** registrar conformidad M'/M y motivos de cada rechazo.
6. **Revisión humana:** aplicar la rúbrica a los M' análisis → `veredictos_revisor.csv` (antes de ver al juez).
7. **Verificación generativa:** ejecutar JuezGenerativo → `veredictos_juez.csv` (estado, confianza, sustento).
8. **Normalización:** ejecutar con la condición de inclusión → `Resultado` consolidado.
9. **Procedencia [E]:** exportar el grafo; auditoría de reconstrucción Resultado→Noticia sobre el 100% del corpus (factible con N≤80).
10. **Cierre:** `notas_ejecucion.md` con incidentes y decisiones sobre la marcha (fecha/hora cada una).

Cualquier desviación del protocolo (cambiar un sintonizador a mitad de corrida, reejecutar un filtro) se registra en `notas_ejecucion.md` y se reporta al director antes de continuar.

## 6. Captura de evidencia

Carpeta `EVIDENCIA-CAP6/` en el repo (rama de trabajo de Lucio):

```
EVIDENCIA-CAP6/
├── configuracion.md          # configuración técnica completa (sin credenciales) + commit del addon
├── corpus.csv                # noticias del recorte
├── prompts/                  # prompts emitidos (uno por unidad M)
├── respuestas/               # respuestas crudas del generativo
├── analisis/                 # análisis decodificados (JSON por unidad)
├── veredictos_revisor.csv    # rúbrica humana (estado, observación)
├── veredictos_juez.csv       # juez generativo (estado, confianza, sustento)
├── resultado.json            # Resultado consolidado de Normalización
├── procedencia.json          # grafo exportado
├── metricas.csv              # tiempos por filtro, tokens, costos, M'/M
└── notas_ejecucion.md        # incidentes y decisiones (fecha/hora)
```

**Regla de oro de la evidencia:** ningún número del Capítulo 6 que no apunte a un archivo de esta carpeta.

## 7. Métricas y criterios de aceptación

| Dimensión OE4 | Métrica | Fuente | Criterio |
|---|---|---|---|
| Fidelidad documental | Conformidad estructural M'/M | `metricas.csv` + `analisis/` | Reportar el valor real; referencia: 13/13 con restricción (Estudio 59). Sin umbral mínimo exigido — se documenta lo ocurrido |
| Fidelidad documental | Concordancia revisor humano ↔ juez generativo | ambos CSV | Porcentaje de acuerdo + descripción cualitativa de desacuerdos. Con N≤80 **no** reclamar significancia estadística; kappa solo como descriptivo |
| Fidelidad documental | Reconstrucción de procedencia | `procedencia.json` | 100% de los resultados del auditorio reconstruibles hasta sus noticias |
| Escalabilidad | Tiempos por filtro y totales; distribución sobre M | `metricas.csv` | Descriptivo de la corrida — **sin extrapolación** a otros volúmenes |
| Costo computacional | Tokens entrada/salida, costo total, costo por noticia y por unidad M | `metricas.csv` + factura del proveedor | Comparación referencial con Estudios 32/59 |

**Criterios de aceptación de la corrida:** (i) completa sin intervenciones manuales fuera de las previstas por el diseño (sintonizadores, revisor); (ii) evidencia §6 capturada completa; (iii) el `Resultado` es interpretable según los criterios declarados por el estudio. **Un resultado analíticamente "pobre" del generativo NO invalida la corrida**: el capítulo documenta el comportamiento real del framework, y eso incluye análisis de calidad variable — es material de §6.6, no un fracaso.

**Estimación de costo previa (DEC-5):** antes de ejecutar, calcular `M × (tokens promedio prompt + tokens respuesta) × precio modelo` con los precios vigentes y reportarlo al director. Si excede el presupuesto acordado, reducir N o M y registrar el cambio.

## 8. Amenazas a la validez (documentar en §6.6)

- **Constructo:** la rúbrica operacionaliza "fidelidad documental"; el juez generativo puede compartir sesgos con el modelo que produjo los análisis (mitigación parcial: revisor humano primero, comparación explícita).
- **Interna:** corrida única sin control; el revisor humano conoce el template que él/Lucio definió (no es ciego al diseño).
- **Externa:** portales, período y tema únicos — los resultados no se generalizan a otros corpus ni plataformas; la validación es de factibilidad bajo estas condiciones.
- **Conclusión:** N acotado; la concordancia se describe, no se testa inferencialmente.
- **Fiabilidad:** configuración exacta + procedencia + commit del addon permiten replicación; el proveedor/modelo puede cambiar con el tiempo (por eso se registran versión y fecha).

## 9. Roles y cronograma estimado

| Actor | Responsabilidad |
|---|---|
| **Lucio** | Propone DEC-1..DEC-5, ejecuta el procedimiento §5, captura evidencia §6, escribe el cap. 6 |
| **Hermes** | Acompaña paso a paso vía Telegram, revisa borradores con auditoría de claims, arma tablas/figuras **solo desde la evidencia capturada**, registra decisiones |
| **Alejandro** | Valida este protocolo y las DEC, aprueba el costo estimado (DEC-5), valida el cap. 6 terminado |

**Secuencia:** validación de DEC (2-3 días) → ejecución (1-2 días + incidentes) → evidencia verificada → escritura del cap. 6 (2 semanas, Fase 3 de RUTA-001) → cap. 7 (Fase 4).

## 10. Mapeo protocolo → secciones del capítulo 6

| Sección cap. 6 | Contenido | Fuente de evidencia |
|---|---|---|
| 6.1 Selección del caso | DEC-1..3 justificadas; por qué este caso es informativo para OE4 | `configuracion.md`, `corpus.csv` |
| 6.2 Configuración inicial | Estudio, template, sintonizadores [A], configuración técnica [C] | `configuracion.md` + pantallas |
| 6.3 Ejecución del scraping | Recorte del corpus sobre la infraestructura [F] (el scraping es preexistente: se documenta el recorte, no una corrida de extracción nueva) | `corpus.csv`, estado del repositorio |
| 6.4 Definición de contexto y template | Composición: M unidades, prompts; revisión humana con rúbrica [D] | `prompts/`, rúbrica |
| 6.5 Resultados del análisis generativo | Conformidad M'/M, análisis, veredictos (juez vs revisor), Resultado consolidado, tiempos y costos | `analisis/`, ambos CSV, `resultado.json`, `metricas.csv` |
| 6.6 Discusión | Interpretación dentro del alcance; limitaciones y amenazas §8; referencia a Estudios 32/59; lecciones para trabajo futuro (cap. 7) | Todo lo anterior + `notas_ejecucion.md` |

Y la matriz maestra [A]-[F]: cada celda "(por completar)" recibe la realización concreta del caso (configuración del estudio, instancia del template, proveedor/modelo/costo, calidad y fidelidad observadas, reconstrucción de procedencia, ejecución del recorte).

---

**Próximo paso:** Lucio propone DEC-1..DEC-5 (puede consultarlo con el bot por Telegram); Hermes registra las propuestas en ORIENTACION-LUCIO.md y las eleva a Alejandro para validación. Con las DEC congeladas, se ejecuta §5.
