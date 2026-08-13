# DECISIONES-REV-001 — Seguimiento y acciones derivadas

| Campo | Valor |
|---|---|
| **Documento origen** | REV-001 |
| **Fecha de decisiones** | 9 de julio de 2026 |
| **Tomador de decisiones** | Director (Alejandro Sartorio) |
| **Estado** | Pendiente de implementación por el tesista |

Este documento registra las decisiones tomadas sobre las 5 preguntas abiertas del informe REV-001 (§6.3), con las acciones concretas que de ellas se desprenden y el contenido listo para pegar en `main.tex`.

---

## Decisión 1: Reformulación de objetivos específicos

**Pregunta original:** ¿Se reformulan los OE1/OE2/OE3 para reflejar el alcance real del trabajo?

**Respuesta del director:** Sí.

### Justificación

Los objetivos actuales tienen tres problemas que el REV-001 ya documentó (ver P-OBJ-1 a P-OBJ-4 y P-OBJ-6 en REV-001 §2.2):

1. OE1 declara "aplicación informática" pero el desarrollo es un *addon* de Odoo.
2. OE2 y OE1 se superponen en alcance.
3. OE3 está sustancialmente subestimado: dice "procedimientos de acceso a IAG guiado por prompts" cuando el capítulo 3 propone un pipeline completo de 7 filtros con repositorio común, tipos de datos y cadena de procedencia.
4. No hay objetivo específico de validación empírica, aunque el capítulo 5 (cuando exista) será el caso de aplicación.

### Objetivos reformulados (contenido listo para `main.tex`)

Reemplazar la sección 1.2 del actual `main.tex` (líneas ~122-167) por:

---

#### Objetivo general

> Diseñar e implementar un framework basado en el estilo arquitectónico de Tubos y Filtros que automatice el análisis de noticias de portales digitales mediante inteligencia artificial generativa, manteniendo trazabilidad del flujo de datos, control editorial por parte del experto del dominio y reproducibilidad del proceso analítico.

#### Objetivos específicos

> **[OE1:]** Diseñar e implementar un módulo *addon* para Odoo Community que integre el ciclo completo de extracción de noticias, composición de *prompts* mediante *templates* parametrizables, invocación de servicios generativos, verificación editorial de resultados y consolidación analítica, satisfaciendo los requisitos de gobernanza y trazabilidad documental identificados en la revisión sistemática.
>
> **[OE2:]** Modelar el ciclo de análisis como un mapa de procesos (BPMN) que formalice la secuencia de actividades, los roles intervinientes —experto del dominio, implementador, sistema— y las entradas y salidas de cada etapa, garantizando la reproducibilidad procedimental y la correspondencia biyectiva entre los pasos del proceso y los filtros de la arquitectura propuesta.
>
> **[OE3:]** Caracterizar el pipeline de procesamiento generativo bajo el estilo arquitectónico de Tubos y Filtros, especificando los filtros, conectores, sintonizadores y tipos de datos del sistema, y verificando formalmente los invariantes esenciales del estilo sobre el diseño resultante.
>
> **[OE4:]** Validar el framework mediante un caso de aplicación concreto sobre noticias de portales digitales regionales, analizando la calidad de los resultados obtenidos y discutiendo las limitaciones de la propuesta en términos de escalabilidad, fidelidad documental y costo computacional.

---

### Ajustes correlativos requeridos

Una vez adoptada esta reformulación, hay que actualizar también:

1. **§2.4 (Síntesis Crítica y Brechas):** agregar al cierre una tabla de trazabilidad brechas ↔ objetivos:

| Brecha (§2.4) | Objetivo que la atiende |
|---|---|
| Escalabilidad y consistencia de anotaciones | OE3 (tipos de datos) + OE1 (consolidación) |
| Robustez del scraping | OE3 (§3.2.2: sustituibilidad del filtro de Extracción) |
| Trazabilidad en ciencias sociales | OE1 (módulo con trazabilidad) + OE3 (cadena de procedencia) |
| Calibración de incertidumbre | OE3 (filtro de Verificación que cuantifica confianza) |
| Gobernanza editorial *human-in-the-loop* | OE1 (verificación editorial en módulo) + OE3 (compuerta blanda) |

2. **§3.4 (Síntesis del cap. 3, a redactar):** mencionar explícitamente cómo los tres primeros OE quedan satisfechos por el diseño presentado.

3. **Cap. 5 (a redactar):** corresponde directamente al OE4.

4. **Cap. 6 (a redactar):** debe responder a cada uno de los 4 objetivos, uno por párrafo.

5. **Objetivo general actual (línea 603-608, dentro del capítulo 4):** reformular coherentemente.

---

## Decisión 2: Apéndice A — tipos de datos

**Pregunta original:** ¿El apéndice A queda como apéndice o se integra al cuerpo principal?

**Respuesta del director:** Se mantiene como apéndice.

### Acciones derivadas

La decisión se respeta. Para compensar la menor visibilidad, se ejecuta la recomendación alternativa del REV-001 (§5.2.6):

> Agregar una subsección §3.2.9 en el capítulo 3 titulada **"Contratos de datos del pipeline"** (o similar), que introduzca brevemente los ocho tipos (Noticia, Embedding, Prompt, RespuestaIAG, Análisis, Veredicto, Resultado, Template), muestre la tabla resumida de cardinalidades y remita al Apéndice A para el detalle.

Contenido sugerido para §3.2.9 (aprox. 30-40 líneas de LaTeX):

```latex
\subsection{Contratos de datos del pipeline}
\label{sec:arq-car-contratos}

El pipeline transporta por los tubos \textit{recordsets} tipados cuyo contenido
reside en el repositorio común (Subsección~\ref{sec:arq-car-repositorio}). El
framework define ocho tipos ---siete que circulan por los tubos y uno que se
mantiene en el repositorio como ancla de la definición del estudio---, cada uno
con su firma de procedencia y su cardinalidad. Estos tipos constituyen los
contratos de datos del sistema: fijan qué produce cada filtro y qué puede
esperar el siguiente, con independencia de la plataforma sobre la que el
framework se materialice.

\begin{table}[H]
  \centering
  \caption{Tipos de datos del pipeline y cardinalidades.}
  \label{tab:tipos-resumen}
  \footnotesize
  \begin{tabularx}{\textwidth}{@{}l l l l X@{}}
    \toprule
    \textbf{Tipo}     & \textbf{Producido por}  & \textbf{Tubo}      & \textbf{Card.} & \textbf{Contenido principal} \\
    \midrule
    Noticia           & Extracción              & 2$\to$3            & $N$            & Título, texto, link, medio, fecha, reglas \\
    Embedding         & Enriquecimiento         & 4$\to$5 (interno)  & $N$            & Vector + ref. a noticia \\
    Prompt            & Composición de contexto & 6$\to$7            & $M$            & Texto del prompt, parámetros, refs. a noticias y template \\
    RespuestaIAG      & Invocación              & 8$\to$9            & $M$            & Respuesta cruda del modelo + ref. al prompt \\
    Análisis          & Decodificación          & 10$\to$11          & $M$            & Estructura analítica validada + ref. a respuesta \\
    Veredicto         & Verificación            & 12$\to$13          & $M$            & Estado, confianza, sustento + ref. al análisis \\
    Resultado         & Normalización           & 14 (salida)        & 1              & Producto consolidado + refs. a veredictos \\
    Template          & (repositorio)           & ---                & ---            & Objetivo, instrucciones, esquema de respuesta \\
    \bottomrule
  \end{tabularx}
\end{table}

Dos criterios transversales gobiernan el diseño de estos contratos:
(i)~cada tipo contiene únicamente la carga útil que algún filtro posterior
consume, junto con la procedencia del dato, y
(ii)~donde el contenido dipende del caso analítico, el framework fija el sobre
y delega el esquema interno al \textit{template} del estudio. La aplicación
uniforme de ambos criterios, así como la especificación detallada de cada tipo,
se presentan en el Apéndice~\ref{anexo:tipos}.

Leídos en conjunto, los siete tipos que circulan por los tubos forman una
\textit{cadena de procedencia} que recorre el pipeline en sentido inverso: desde
el Resultado final puede reconstruirse qué veredictos lo componen, sobre qué
análisis se pronuncia cada uno, de qué respuestas crudas provienen, con qué
\textit{prompts} se generaron, sobre qué noticias se apoyó cada composición y de
qué portal fue extraída cada noticia. Esta propiedad estructural del sistema de
tipos materializa, a nivel del dato, la auditabilidad lineal que motivó la
elección del estilo (Subsección~\ref{sec:arq-estilo-justificacion}).
```

**Acción:** el tesista puede pegar este fragmento después de §3.2.8 y antes de §3.3, cuando esté redactando las secciones vacías.

---

## Decisión 3: Ampliación de bases de datos en la RSL

**Pregunta original:** ¿Se amplían las bases de datos de la RSL a IEEE Xplore, ACM Digital Library, Scopus?

**Respuesta del director:** Sí.

### Justificación

La consulta exclusiva a SciSpace, Google Scholar y ArXiv (todas agregadores, ninguna curada editorialmente) es la vulnerabilidad metodológica más clara de la RSL actual. Un tribunal de Ciencias de la Computación lo va a señalar. IEEE Xplore y ACM DL son las dos fuentes primarias de ingeniería de software y de sistemas; Scopus indexa ambos y además cubre revistas europeas que pueden contener trabajos sobre BPMN + IA.

### Procedimiento propuesto

**No es necesario rehacer la RSL desde cero.** Basta con ejecutar consultas complementarias en las tres bases nuevas y sumar los resultados al corpus. El recuento final se actualizará en el diagrama PRISMA.

### Cadenas de búsqueda sugeridas

Las cadenas se derivan de las tres PR y de los términos clave ya usados en la búsqueda original. Se ajustan a la sintaxis de cada base:

#### Cadena 1 — IEEE Xplore

IEEE usa sintaxis布尔 (boolean) con `AND` / `OR` / `"...""`:

```
("news" OR "digital journalism" OR "media" OR "newspaper")
AND ("large language model" OR "LLM" OR "generative AI" OR "GPT" OR "ChatGPT")
AND ("scraping" OR "web scraping" OR "extraction" OR "crawling")
AND ("embedding" OR "semantic" OR "vector")
```

Limitar a: Artículos de revista + Conferencias, 2020-2025.

#### Cadena 2 — ACM Digital Library

ACM DL acepta sintaxis similar. Ejecutar dos consultas para aumentar recall:

```
(news OR "digital journalism" OR media) AND ("large language model" OR LLM OR GPT)
```
```
("agenda setting" OR framing OR bias) AND (LLM OR "generative AI")
```

#### Cadena 3 — Scopus

Scopus usa `TITLE-ABS-KEY(...)`:

```
TITLE-ABS-KEY (
  ( "news*" OR "media" OR "journalism" )
  AND ( "large language model*" OR LLM OR GPT OR "generative AI" )
  AND ( scrap* OR extract* )
)
AND LIMIT-TO ( DOCTYPE , "ar" OR "cp" )
AND LIMIT-TO ( PUBYEAR , 2020-2025 )
```

### Procedimiento operativo para el tesista

1. Ejecutar cada cadena en sus respectivas bases, registrar el conteo de resultados en cada base.
2. Exportar a BibTeX (IEEE Xplore, ACM DL y Scopus tienen export nativo) y consolidar en `refs.bib`.
3. Ejecutar cribado por título+resumen (aplicar CI1-CI5, CE1-CE5 del §2.2.2) sobre los resultados nuevos.
4. Los que califiquen, sumarlos a la Tabla 2.1 (estudios-rsl) y a las secciones 2.3.x del Estado del Arte.
5. Actualizar el diagrama PRISMA (`prisma_diagram.png`) con los nuevos conteos **antes** de la deduplicación. Recrear con `gen_prisma.py` si aplica.
6. Actualizar el párrafo del §2.2.2 que lista bases consultadas y conteos por base.

### Qué NO hacer

- No es obligatorio consultar **Web of Science** además de Scopus — Scopus es prácticamente superconjunto de WoS para este dominio; añadirlo tendría rendimiento decreciente.
- No hace falta incluir IEEE Xplore y ACM DL como fuentes **primarias** si Scopus ya los indexa (la mayoría de los trabajos están en los tres). Para el tribunal, la prueba de que se usó Scopus basta; IEEE/ACM DL dan redundancia útil pero no son estrictamente necesarios. **Recomendación conservadora:** usar **Scopus + IEEE Xplore** (dos fuentes nuevas); ACM DL es opcional.

### Costo estimado

Ejecutar las tres consultas, exportar y consolidar: 1-2 horas. Cribado de títulos+resumen: 2-3 horas. Integración al texto: 2-3 horas. **Total: ~6 horas de trabajo del tesista.**

---

## Decisión 4: Reemplazo de la cita a Bertagnolio 2023

**Pregunta original:** ¿Cómo se reemplaza la referencia a Bertagnolio 2023 (sobre ruido de turbinas eólicas, mal utilizada para respaldar integración de LLMs en procesos)?

### Diagnóstico preciso

La cita aparece en el §2.1 (Marco Teórico), línea 190 del `main.tex`:

> *"Disponer de modelos generativos no alcanza, sin embargo, para construir una infraestructura utilizable: es necesario orquestar las tecnologías mediante estándares de procesos de negocio. Trabajos como el de \citet{PRADES2013115} establecen metodologías para implementar flujos de trabajo en BPMN de acuerdo con el estándar ANSI/ISA-95. Investigaciones recientes, como la de \citet{bertagnolio2023}, demuestran la viabilidad de incorporar modelos generativos dentro de mapas de procesos tecnológicos automatizados."*

La afirmación que necesita sustento es: *"la viabilidad de incorporar modelos generativos dentro de mapas de procesos tecnológicos automatizados"*. Bertagnolio 2023 no trata eso en absoluto.

### Opciones de reemplazo (ordenadas por preferencia)

#### Opción A — Usar un trabajo que sí trata la integración de LLMs en procesos [RECOMENDADO]

Buscar en Google Scholar / ACM DL / ArXiv con la cadena:

```
"large language model" AND ("workflow" OR "BPMN" OR "process automation" OR "orchestration")
```

Trabajos canónicos del área (publicados entre 2023-2025) —hay que verificar disponibilidad y cita específica*:

1. **Xi et al. (2023)**. *The Rise and Potential of Large Language Model Based Agents: A Survey.* ArXiv:2309.07864. — Amplia encuesta sobre agentes LLM orquestados en flujos de trabajo. Cita directa sobre la integración de LLMs en pipelines automatizados.

2. **Wang et al. (2024)**. *Voyager: An Open-Ended Embodied Agent with Large Language Models.* ArXiv:2305.16291. — Demuestra orquestación de un LLM en un pipeline modular de tareas con memoria y verificación (similar en espíritu al estilo de Tubos y Filtros).

3. **Hong et al. (2024)**. *MetaGPT: Meta Programming for Multi-Agent Collaborative Framework.* ArXiv:2308.00352. — Orquestación de múltiples agentes LLM con roles y flujos de trabajo estructurados.

4. **Dastjerdi & Buyya (2012)** (si se quiere algo anterior a LLM pero sobre orquestación de servicios). *Service-Oriented Architecture for Autonomous Service Operations.*

*Verificación obligatoria:* antes de citar cualquiera de estos en la tesina, hay que descargar el paper, confirmar que efectivamente respalda la afirmación exacta, y agregarlo a `refs.bib` con datos completos (autores, título correcto, doi, año).

#### Opción B — Dividir el párrafo en dos

Si no se encuentra un reemplazo directo y el tesista quiere conservar la afirmación, puede reestructurarse así:

> *"Disponer de modelos generativos no alcanza, sin embargo, para construir una infraestructura utilizable: es necesario orquestar las tecnologías mediante estándares de procesos de negocio. Trabajos como el de \citet{PRADES2013115} establecen metodologías para implementar flujos de trabajo en BPMN de acuerdo con el estándar ANSI/ISA-95, proporcionando un vocabulario formal para especificar cada etapa del proceso. La literatura reciente sobre agentes basados en modelos de lenguaje —\citet{x...:2023}— ha extendido este principio al diseño orquestado de modelos generativos dentro de pipelines modulares, combinando invocación del modelo, verificación de resultados y composición de etapas de procesamiento."*

Donde `x...:2023` es el trabajo que el tesista seleccione tras buscar.

#### Opción C — Eliminar la frase completa (opción conservadora)

Si no se encuentra un reemplazo verificable o el tiempo apremia, el párrafo puede quedarse solo con la referencia a Prades (que sí es precisa) y eliminar la oración sobre Bertagnolio:

> *"Disponer de modelos generativos no alcanza, sin embargo, para construir una infraestructura utilizable: es necesario orquestar las tecnologías mediante estándares de procesos de negocio. Trabajos como el de \citet{PRADES2013115} establecen metodologías para implementar flujos de trabajo en BPMN de acuerdo con el estándar ANSI/ISA-95, proporcionando un vocabulario formal para especificar cada etapa del proceso y los roles intervinientes."*

Esto es técnicamente correcto y no requiere respaldo adicional, pero debilita levemente el puente conceptual hacia el capítulo 4 (mapa de procesos).

### Recomendación

**Opción A, con la lista de candidatos arriba.** El tesista debe:

1. Buscar los 4 papers propuestos (o equivalentes) en ArXiv / Google Scholar.
2. Verificar que cada uno respalda efectivamente la afirmación.
3. Seleccionar el más pertinente (probablemente Xi et al. 2023 o Hong et al. 2024).
4. Agregarlo a `refs.bib` con datos verificados.
5. Reemplazar `\citet{bertagnolio2023}` por la nueva clave.
6. Eliminar la entrada `bertagnolio2023` de `refs.bib` (ya no se usará).

**No se debe** inventar una cita, ni forzar una referencia que no corresponda. Si la búsqueda no arroja candidatos útiles, proceder con la Opción C.

---

## Decisión 5: Título

**Pregunta original:** ¿Cuál es el título sugerido?

### Opciones evaluadas

| # | Título | Palabras | Observación |
|---|---|---|---|
| 1 | Framework para el análisis de noticias de portales digitales mediante inteligencia artificial generativa | 15 | Directo, conservador, mantiene los conceptos clave |
| 2 | Análisis automatizado de noticias digitales mediante inteligencia artificial generativa: diseño e implementación de un framework modular | 16 | Formato título:subtítulo, más académico pero más largo |
| 3 | Infraestructura modular para el análisis de noticias digitales mediante inteligencia artificial generativa | 13 | Conserva "infraestructura" pero "modular" puede sonar reductivo frente al diseño de Tubos y Filtros |
| 4 | Diseño e implementación de un framework para el análisis de noticias de portales digitales mediante inteligencia artificial generativa | 18 | Añade "Diseño e implementación" — más preciso respecto al aporte real, pero más largo |

### Recomendación: **Opción 1**

> **Framework para el análisis de noticias de portales digitales mediante inteligencia artificial generativa**

### Justificación de la opción 1

1. **Concisión:** 15 palabras frente a las 24 actuales. Reduce ~38 % la extensión sin perder contenido semántico.

2. **Precisión del término "framework":** el aporte central del capítulo 3 es efectivamente un *framework* — un sistema estructurado bajo un estilo arquitectónico específico (Tubos y Filtros) que provee contratos de datos extensibles y puntos de parametrización. Usar "framework" en el título es técnicamente exacto y se alinea con la reformulación del objetivo general (decisión 1).

3. **Conservación de los conceptos clave:** quedan todos los términos necesarios para entender el tema: marco de trabajo, noticias, portales, IA generativa.

4. **Defendibilidad ante tribunal:** el término "framework" es estándar en la literatura de ingeniería de software (no es una elección reductiva ni promocional); está justificado por el diseño arquitectónico del capítulo 3.

5. **Eliminación de redundancias del título actual:**
   - *"técnica y procedimental"* era redundante (una infraestructura es técnica por definición; lo procedimental queda cubierto por el diseño del pipeline).
   - *"a través de"* → sustituido por *"mediante"* (registro más académico).

### Implementación

Cambiar en `main.tex`:

1. **Línea 30 (titlepage LaTeX):**

```latex
\title{\textbf{Framework para el análisis de noticias de portales digitales mediante inteligencia artificial generativa}\\
\large Tesina de grado
}
```

2. **Línea 49 (titlebox):**

```latex
{\huge\bfseries
  Framework para el análisis de noticias de portales digitales a través de inteligencia artificial generativa\par}
```

(En este segundo, "a través de" puede dejarse si el tesista prefiere la formulación menos comprimida para la portada.)

### Alternativa

Si el tesista o director prefieren mantener "infraestructura" (concepto presente en el primer párrafo del documento), la Opción 3 es válida:

> **Infraestructura modular para el análisis de noticias digitales mediante inteligencia artificial generativa**

---

## Resumen de acciones derivadas

| Acción | Responsable | Prioridad | Tiempo est. |
|---|---|---|---|
| Actualizar `main.tex` con los objetivos reformulados (§1.2) | Tesista | Alta | 1 h |
| Agregar tabla de trazabilidad brechas↔objetivos al §2.4 | Tesista | Alta | 30 min |
| Agregar tabla comparativa de estudios al §2.3 | Tesista | Alta | 2 h |
| Ejecutar búsquedas complementarias en Scopus + IEEE Xplore | Tesista | Alta | 6 h total |
| Actualizar diagrama PRISMA con nuevos conteos | Tesista | Alta | 1 h |
| Buscar y verificar reemplazo para Bertagnolio 2023 | Tesista | Alta | 2 h |
| Cambiar título en las dos ocurrencias de `main.tex` | Tesista | Baja | 10 min |
| Agregar subsección §3.2.9 "Contratos de datos del pipeline" | Tesista | Media | 1 h |
| Corregir referencias mal tipadas en `refs.bib` (10 entradas) | Tesista | Alta | 1-2 h |
| Corregir errores ortográficos (scrapping → scraping, NPL → NLP, tildes) | Tesista | Media | 30 min |

**Todas estas acciones deben completarse antes de avanzar a la revisión de los capítulos 4, 5 y 6** (que son los capítulos pendientes en el próximo informe REV-002).

---

**Fin del documento de decisiones.**
