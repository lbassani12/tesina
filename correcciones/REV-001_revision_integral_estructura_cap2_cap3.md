# REV-001 — Revisión integral: estructura, planteo, capítulos 2 y 3

| Campo | Valor |
|---|---|
| **Código** | REV-001 |
| **Nombre** | Revisión integral — Estructura, planteo y análisis profundo de capítulos 2 y 3 |
| **Fecha de emisión** | 9 de julio de 2026 |
| **Archivos revisados** | `main.tex` (1125 líneas, 148 KB), `diagrama_arquitectura.tex`, `refs.bib`, 7 figuras PNG/SVG |
| **Rama del repositorio** | `main` |
| **Versión del commit** | primera clonación del repo |
| **Alcance** | Índice completo, planteo del problema, capítulos 2 (Marco teórico + RSL) y 3 (Arquitectura) |
| **Autor de la revisión** | Hermes (agente) — pendiente de validación del director |

---

## 0. Criterio de severidad

Cada hallazgo se clasifica según esta escala:

| Severidad | Significado |
|---|---|
| **Crítico** | Problema que impide la defensa o compromete el núcleo de la tesina |
| **Alto** | Problema que afecta la coherencia entre capítulos o la validez del argumento |
| **Medio** | Problema que afecta la comprensión, consistencia parcial o calidad técnica |
| **Bajo** | Problema menor de forma, estilo, ortografía o claridad |

---

## 1. Revisión de la estructura del índice

### 1.1 Estado por capítulo

| Capítulo | Título actual | Líneas | Estado estimado | % avance |
|---|---|---|---|---|
| 1 | Introducción | 89-167 | Completo, pulible | 85 % |
| 2 | **Análisis bibliográfico?** | 168-338 | Completo, pulible | 80 % |
| 3 | Arquitectura | 339-591 | Sólido el núcleo; vacías las subsecciones 3.3 y 3.4 | 70 % |
| 4 | Mapa de procesos | 592-871 | Parcial; vacías 5 de 8 secciones | 55 % |
| 5 | Ejemplo de aplicación | 872-892 | **Vacío** | 0 % |
| 6 | Conclusiones y Trabajo a Futuro | 893-898 | **Vacío** | 0 % |
| A | Apéndice — Tipos de datos del pipeline | 899-1121 | Completo, muy buena calidad | 95 % |

### 1.2 Observaciones sobre el título del documento

El título actual es *"Una infraestructura técnica y procedimental para el análisis de noticias de portales digitales a través de inteligencia artificial generativa"* (24 palabras). Es extenso pero descriptivo. Como título de tesina es defendible, aunque dos observaciones:
- *"técnica y procedimental"* duplica el alcance que queda claro con *"infraestructura"* (una infraestructura ya es técnica, y la procedimentalidad se manifiesta en el capítulo 4).
- *"a través de"* es ligeramente coloquial en el contexto; *"mediante"* es más académico.

**Sugerencia opcional:** "Framework para el análisis de noticias de portales digitales mediante inteligencia artificial generativa". Es discutible; no es obligatorio cambiarlo.

### 1.3 Signo de interrogación en el título del Capítulo 2 [Medio]

El capítulo 2 se llama literalmente **"Análisis bibliográfico?"** — el signo de interrogación marca indecisión editorial. No puede aparecer así en la versión final. Opciones:
- *"Fundamentos teóricos y estado del arte"*
- *"Marco teórico y revisión sistemática de la literatura"* (recomendado, porque refleja los tres bloques del capítulo: marco teórico + RSL + estado del arte)
- *"Bases conceptuales y antecedentes"*

### 1.4 Estructura jerárquica del documento

**Capítulo 1 — Introducción**
- §1.1 Motivación ✓
- §1.2 Objetivos ✓ (objetivo general + OE1, OE2, OE3)

**Capítulo 2 — [Marco teórico y estado del arte]**
- §2.1 Marco Teórico ✓
- §2.2 Revisión Sistemática de la Literatura
  - §2.2.1 Preguntas de Investigación ✓
  - §2.2.2 Metodología de Búsqueda y Selección ✓
  - §2.2.3 Estudios Incluidos ✓
- §2.3 Estado del Arte
  - §2.3.1 Limitaciones del NLP tradicional ✓
  - §2.3.2 Aplicaciones computacionales del agenda-setting de segundo nivel ✓
  - §2.3.3 Arquitecturas de software con IAG para el procesamiento de noticias ✓
- §2.4 Síntesis Crítica y Brechas en la Investigación ✓
- §2.5 Conclusión del Capítulo ✓

**Capítulo 3 — Arquitectura**
- §3.1 El estilo Tubos y Filtros
  - §3.1.1 Componentes, conectores y patrón estructural ✓
  - §3.1.2 Modelo computacional e invariantes ✓
  - §3.1.3 Justificación del estilo ✓
- §3.2 El framework como sistema de Tubos y Filtros
  - §3.2.1 Vista de conjunto y patrón estructural ✓
  - §3.2.2 Componentes: los filtros del framework ✓
  - §3.2.3 Conectores: tubos tipados ✓
  - §3.2.4 Especializaciones aplicadas ✓
  - §3.2.5 Repositorio común sobre PostgreSQL ✓
  - §3.2.6 Sintonizadores ✓
  - §3.2.7 Verificación de invariantes ✓
  - §3.2.8 Ventajas y limitaciones ✓
- §3.3 Implementación: la solapa en Odoo
  - §3.3.1 Infraestructura preexistente ⚠️ **VACÍO**
  - §3.3.2 Stack tecnológico ⚠️ **VACÍO**
  - §3.3.3 Materialización del mapeo ⚠️ **VACÍO**
- §3.4 Síntesis del capítulo ⚠️ **VACÍO**

**Capítulo 4 — Mapa de procesos**
- §4.1 Proceso general (parcial, figura BPMN incluida pero sin descripción del proceso general)
- §4.2 Recopilación de requerimientos ⚠️ **VACÍO**
- §4.3 Scrapping ✓ (detallado)
- §4.4 Definición de Contexto ✓ (detallado)
- §4.5 Procesamiento IAG ✓ (detallado)
- §4.6 Visualización previa ⚠️ **VACÍO**
- §4.7 Refinamiento iterativo ⚠️ **VACÍO**
- §4.8 Presentación de resultados ⚠️ **VACÍO**
- §4.9 Síntesis del capítulo ⚠️ **VACÍO**

**Capítulo 5 — Ejemplo de aplicación** ⚠️ **TODAS LAS SECCIONES VACÍAS**
- §5.1 Selección del caso
- §5.2 Configuración inicial
- §5.3 Ejecución del scraping
- §5.4 Definición de contexto y template
- §5.5 Resultados del análisis generativo
- §5.6 Discusión

**Capítulo 6 — Conclusiones y Trabajo a Futuro** ⚠️ **COMPLETAMENTE VACÍO**

**Apéndice A — Tipos de datos del pipeline** ✓ (completo)
- §A.1 Notación y criterios de diseño
- §A.2 Noticia
- §A.3 Embedding
- §A.4 Prompt
- §A.5 RespuestaIAG
- §A.6 Análisis
- §A.7 Veredicto
- §A.8 Resultado
- §A.9 Template
- §A.10 Los filtros como transformaciones de estado
- §A.11 La cadena de procedencia

### 1.5 Observaciones generales sobre el índice

**OBS-1 [Alto]:** Los capítulos 5 y 6 están completamente vacíos. Estos capítulos son **indispensables** para la defensa: el capítulo 5 es donde se valida empíricamente que el framework funciona, y el capítulo 6 cierra el trabajo respondiendo a los objetivos. Sin ellos, la tesina no puede defenderse.

**OBS-2 [Alto]:** El capítulo 3 tiene 4 subsecciones vacías (3.3.1, 3.3.2, 3.3.3, 3.4). La implementación en Odoo no está documentada formalmente.

**OBS-3 [Medio]:** El capítulo 4 tiene 5 secciones vacías de 8. Las tres secciones descritas (Scraping, Contexto, IAG) tienen buena calidad pero las anteriores y posteriores no existen.

**OBS-4 [Medio]:** El apéndice A tiene material de tan alta calidad (tipos de datos, formalización de firmas, cadena de procedencia) que probablemente podría integrarse al cuerpo central, dentro del capítulo de Arquitectura como una sección adicional. Relegarlo a apéndice le resta visibilidad.

**OBS-5 [Bajo]:** No hay sección de "Listado de figuras" ni "Listado de tablas" tras el índice. Para una tesina con muchos diagramas técnicos convendría incluirlas.

**OBS-6 [Bajo]:** El orden de secciones en el índice no siempre refleja el orden real del contenido al compilar (por ejemplo, el `\printindex` aparece antes de la tabla de contenidos por `\tableofcontents \printindex` en las líneas 86-87, pero `\printindex` aparece antes de que haya entradas de índice; además, el índice alfabético se mezcla visualmente con la tabla de contenidos).

---

## 2. Análisis del planteo del tema

### 2.1 Motivación (Sección 1.1)

La sección 1.1 presenta el problema de manera progresiva y bien argumentada. Estructura:
1. Describe el escenario actual (proliferación de portales digitales, sociedades hipermediatizadas).
2. Identifica dos limitaciones (atributos ocultos de los discursos; magnitud de los paquetes textuales).
3. Contextualiza en el "giro computacional" de Berry y la semiótica computacional.
4. Presenta al NLP tradicional, sus limitaciones y la promesa de la IAG.
5. Formula la hipótesis: uso de servicios de IAG combinados con técnicas de ciencia de datos.

**Puntos fuertes:**
- Progresión argumental clara (problema → contexto → herramientas existentes → brecha → hipótesis).
- Buen uso de la bibliografía (Luhmann, McCombs, Couldry, Berry, Vaswani).
- Las dos limitaciones identificadas están bien articuladas y son verificables.
- La mención al segundo nivel de *agenda-setting* (atributos, no solo objetos) es crucial y está bien presentada.

**Puntos débiles:**
- **Falta un planteo explícito del problema.** La sección se llama "Motivación" pero funciona parcialmente como planteo del problema. Faltan elementos explícitos como: ¿qué problema *concreto* se resuelve? ¿quién es el usuario afectado? ¿qué soluciones existen ya y por qué fallan? ¿cuál es el vacío específico que esta tesina llena? Todo eso está implícito pero no explicitado.
- **No hay pregunta de investigación explícita.** El texto habla de "hipótesis" pero no formula una pregunta de investigación verificable. Para una tesina en Ciencias de la Computación, es útil tener algo del tipo: *"¿Es posible construir un framework basado en tubos y filtros que integre scraping, embeddings y modelos generativos para el análisis sistemático de noticias, manteniendo trazabilidad, reproducibilidad y control editorial?"*
- **La motivación se mezcla con contenido del marco teórico.** Por ejemplo, McCombs (1972) y la teoría de agenda-setting se presentan en la Motivación y se vuelven a presentar en el Marco Teórico con mayor profundidad. Hay una duplicación parcial. Convendría que la Motivación *mencione* la agenda-setting pero la desarrolle íntegramente en el Capítulo 2.

**Severidad combinada: Medio-Alto.** El contenido es bueno pero la estructura argumental del planteo del problema queda difusa. Un tribunal atento podría preguntar: "¿Cuál es el problema de investigación preciso?" y el tesista tendría que reconstruirlo oralmente desde varios párrafos distribuidos.

### 2.2 Objetivos (Sección 1.2)

**Objetivo general:** *"Crear un framework para automatizar el análisis de noticias digitales a través de inteligencia artificial generativa."*

**OE1:** *"Desarrollar una aplicación informática que permita gestionar el proceso integral de extracción y transformación de datos, análisis y muestra de resultados."*

**OE2:** *"Diseñar e implementar, en la aplicación informática, un proceso que organice las tareas y procedimientos de las etapas de recolección de datos, análisis y visualización."*

**OE3:** *"Diseñar e implementar los procedimientos de acceso a los servicios de IAG guiado por 'prompts'."*

**Problemas detectados:**

| # | Problema | Severidad |
|---|---|---|
| P-OBJ-1 | El objetivo general usa la palabra "framework" sin definirla previamente. En la Introducción nunca se define qué es un framework en este contexto, ni en qué se diferenciaría de un sistema, una plataforma, un pipeline o una biblioteca. Recién en el capítulo 3 se entiende. | Alto |
| P-OBJ-2 | OE1 habla de "aplicación informática" pero la implementación real es un *módulo addon de Odoo*. Esto es un desajuste entre el objetivo formulado y el desarrollo. Un addon de Odoo no es una aplicación en el sentido clásico; es un componente extensible dentro de una plataforma existente. | Alto |
| P-OBJ-3 | OE3 está **subestimado** respecto del contenido real del capítulo 3. Dice "diseñar e implementar los procedimientos de acceso a los servicios de IAG guiado por prompts" pero el capítulo 3 propone un sistema completo de 7 filtros con repositorio común, sintonizadores, compuertas blandas, tipos de datos y cadena de procedencia. La formulación actual no representa el alcance real. | Alto |
| P-OBJ-4 | OE1 y OE2 se superponen parcialmente. OE1 habla de "gestionar el proceso integral de extracción y transformación de datos, análisis y muestra de resultados"; OE2 habla de "organizar las tareas y procedimientos de las etapas de recolección de datos, análisis y visualización". Son prácticamente la misma cosa dicha de dos formas. | Medio |
| P-OBJ-5 | Ningún objetivo menciona **validación empírica**. El capítulo 5 (que debería ser el de validación) está vacío y no hay objetivo específico que lo respalde. Un tribunal puede preguntar: "¿Cómo validás que el framework funciona?" y la respuesta debería estar ya formulada en los objetivos. | Alto |
| P-OBJ-6 | El orden de OE1, OE2, OE3 no es natural respecto del desarrollo. OE1 (la aplicaciónOdoo) se desarrolla en la sección 3.3 y 3.3.3 del capítulo 3; OE3 (los procedimientos de acceso a IAG) es en realidad el núcleo teórico del capítulo 3 (el pipeline de T y F). Conviene reformular para que reflejen el orden real. | Medio |

**Propuesta concreta de reformulación** (discutir con el director):

- **Objetivo general:** Diseñar e implementar un framework basado en el estilo arquitectónico de Tubos y Filtros que automatice el análisis de noticias de portales digitales mediante inteligencia artificial generativa, manteniendo trazabilidad del flujo, control editorial por parte del experto del dominio y reproducibilidad del proceso analítico.

- **OE1:** Diseñar e implementar un módulo *addon* para Odoo Community que integre el ciclo completo de extracción de noticias, composición de prompts, invocación de servicios generativos, verificación de resultados y presentación, satisfaciendo los requisitos de gobernanza editorial y trazabilidad documental identificados en la revisión sistemática.

- **OE2:** Modelar el ciclo de análisis como un mapa de procesos (BPMN) que formalice la secuencia de actividades, los roles intervinientes (experto del dominio, implementador, sistema) y las entradas y salidas de cada etapa, garantizando la reproducibilidad procedimental.

- **OE3:** Caracterizar el pipeline de procesamiento generativo bajo el estilo Tubos y Filtros, especificando los filtros, conectores, sintonizadores y tipos de datos del sistema, y verificando formalmente los invariantes esenciales del estilo sobre el diseño resultante.

- **OE4 (nuevo, sugerido):** Validar el framework mediante un caso de aplicación concreto, analizando noticias de portales digitales regionales en un escenario empírico definible y discutiendo la calidad de los resultados obtenidos.

### 2.3 Coherencia general del planteo

El planteo general es **defendible pero requiere ajustes de formulación**. Los elementos positivos:
- El problema es real y está contextualizado en una tradición de investigación consolidada (agenda-setting, giro computacional).
- La hipótesis (uso de IAG combinada con ciencia de datos) es razonable y se corresponde con la evolución del estado del arte.
- La solución propuesta (framework modular con supervisión humana) es técnicamente defendible.

Los elementos a corregir antes de la defensa:
- Falta una pregunta de investigación explícita.
- Falta una definición operativa de "framework".
- Los objetivos específicos no reflejan el alcance real del desarrollo.
- No hay un objetivo específico de validación.
- El capítulo 2 termina con 5 brechas bien identificadas que **no todos** se recuperan explícitamente en los objetivos. Específicamente: la brecha de "estándares interoperables de anotación" no aparece en ningún OE; la de "calibración de incertidumbre" aparece parcialmente en el filtro de Verificación (cap. 3) pero no como objetivo.

---

## 3. Análisis en profundidad del Capítulo 2

### 3.1 Marco Teórico (Sección 2.1)

**Extensión aproximada:** 19 párrafos densos.
**Citas utilizadas:** Luhmann, McCombs (1972, 1997), Couldry, Carlón, Berry, Meunier, Vaswani, Rey-Mazón, Prades, Bertagnolio.

**Evaluación general: [Bueno — 7.5/10]**

#### Fortalezas

1. **Progresión argumental sólida.** El marco teórico construye una línea que va de la teoría de medios (Luhmann, McCombs) al giro computacional (Berry, Meunier) a las bases técnicas de la IAG (Vaswani). Esta progresión es coherente y justifica por qué el análisis de medios hoy requiere IA.

2. **Uso cuidadoso de las citas.** Las citas son directas, se traducen cuando corresponde (con nota al pie aclaratoria), y se integran argumentalmente en lugar de solo aparecer como apoyo decorativo. Esto es poco común en tesinas de grado y es un punto fuerte.

3. **Conexión con la literatura de agenda-setting de segundo nivel.** El desarrollo del *framing* y de la transmisión de atributos (McCombs 1997) es crucial para la tesina, porque es lo que justifica el uso de IAG: el NLP tradicional puede contar palabras, pero para medir atributos discursivos se necesitan modelos que capturen contexto.

4. **Mención al trabajo de Rey-Mazón.** La inclusión de "Color of Corruption" es pertinente y muestra conocimiento del trabajo antecedente en el grupo de investigación CAETI/CIM.

5. **Distinción entre marco teórico y estado del arte.** El capítulo separa bien las bases conceptuales (sección 2.1) de los trabajos empíricos recientes (sección 2.3), lo cual es correcto metodológicamente.

#### Debilidades y problemas

| # | Problema | Severidad | Detalle |
|---|---|---|---|
| MT-1 | El párrafo sobre Bertagnolio 2023 es problemático | **Alto** | El trabajo citado (*"A roadmap for required technological advancements to further reduce onshore wind turbine noise impact"*) trata sobre ruido de turbinas eólicas, no sobre integración de LLMs en procesos. La cita en línea (que dice "demuestran la viabilidad de incorporar modelos generativos dentro de mapas de procesos tecnológicos automatizados") es **inexacta** para la obra citada. Hay que reemplazar la cita por una referencia que realmente aborde el punto, o eliminar la afirmación. |
| MT-2 | Falta bibliografía fundamental sobre teoría del framing | Medio | El texto menciona a Entman en una sola oración (párrafo 3) pero no lo desarrolla. Entman (1993) es central en la teoría del framing; en una tesina sobre análisis de encuadre mediático mediante IAG, es una cita esperada. |
| MT-3 | Ausencia de bibliografía sobre teoría de sistemas de Luhmann en profundidad | Bajo | Luhmann se menciona solo al inicio con una cita textual, pero la noción de "sistema social funcionalmente diferenciado" no se recupera luego. Si se lo cita, conviene o desarrollarlo más o mencionarlo únicamente de paso. |
| MT-4 | El párrafo sobre Vaswani (Transformer) tiene un error técnico | Medio | El texto dice: "La entrada y la salida del modelo se construyen sobre *embeddings*: representaciones vectoriales aprendidas que codifican unidades lingüísticas en un espacio continuo de alta dimensionalidad." Los embeddings **no son específicos de Transformer**; existían antes (Word2Vec, GloVe, FastText). Lo distintivo de Transformer es el **self-attention mechanism**, no los embeddings. Conviene reformular para no dar a entender que los embeddings son aportes de Vaswani. |
| MT-5 | Se menciona DALL-E 2 en un marco de análisis de noticias | Bajo | La tesina trata exclusivamente de noticias textuales de portales; DALL-E 2 (modelo multimodal de imagen) aparece mencionado al final del párrafo de Transformer como "útil para complementar representaciones visuales del discurso", pero esa línea no se desarrolla nunca. Es un *non sequitur*; conviene eliminarlo o justificarlo si hay un plan para análisis multimodal. |
| MT-6 | El cierre del marco teórico salta abruptamente al BPMN/Prades | Medio | El último párrafo pasa de Transformer + Rey-Mazón a "orquestar las tecnologías mediante estándares de procesos de negocio", citando a Prades (BPMN en manufactura) y Bertagnolio (ruido de turbinas). El salto es temáticamente brusco. Conviene explicitar el puente: "una vez caracterizadas las bases teóricas, la construcción de la infraestructura requiere orquestar las tecnologías; para eso se apela a la formalización de procesos de negocio..." |
| MT-7 | Falta mención a teoría de la comunicación de Hall (codificación/decodificación) | Bajo | En un trabajo sobre análisis mediático con IAG, la teoría de codificación/decodificación de Stuart Hall es pertinente como antecedente conceptual. No es estrictamente necesaria, pero un tribunal de Cs. de la Comunicación (si lo hay) podría notarla ausente. |

### 3.2 Revisión Sistemática de la Literatura (Sección 2.2)

#### 3.2.1 Preguntas de investigación

La RSL se organiza en torno a tres preguntas:
- **PR1:** limitaciones del NLP tradicional frente al análisis discursivo.
- **PR2:** metodologías y herramientas para evaluar el agenda-setting y el impacto mediático.
- **PR3:** brechas estructurales y procedimentales en los pipelines de IAG actuales.

**Evaluación: [Bueno — 8/10]**

Las preguntas están bien formuladas, son mutuamente excluyentes en foco, y cubren bien el dominio. La PR2 es la más amplia de las tres y podría haberse acotado ("¿qué metodologías se usan para medir **computacionalmente** el agenda-setting de segundo nivel?").

#### 3.2.2 Metodología de búsqueda

**Evaluación: [Regular-Bueno — 6.5/10]**

**Puntos fuertes:**
- Sigue explícitamente PRISMA 2020.
- Declara las bases consultadas (SciSpace, SciSpace Library, biblioteca personal, Google Scholar, ArXiv), los conteos por base y los criterios de inclusión/exclusión.
- El diagrama PRISMA existe como figura y está referenciado correctamente.

**Problemas:**

| # | Problema | Severidad | Detalle |
|---|---|---|---|
| RSL-1 | Bases de datos no son las canónicas del área | Alto | No se consultan **IEEE Xplore, ACM Digital Library, Scopus ni Web of Science**, que son las fuentes primarias esperables en Cs. de la Computación. SciSpace y Google Scholar son agregadores útiles pero su confiabilidad bibliográfica es menor; un tribunal puede señalar esto. **Recomendación:** agregar al menos ACM DL y Scopus (aunque sea con consultas acotadas) y justificar por qué SciSpace fue preferida. |
| RSL-2 | "Biblioteca personal del autor" no es una base de datos | Medio | Contabilizada como "base" con n=6. No es una base de datos académica; es una colección ad-hoc. No está mal incluirla como fuente complementaria, pero no debería listarse al mismo nivel que SciSpace o ArXiv. Debería explicitarse que es "fuentes adicionales identificadas por el autor" (snowballing). |
| RSL-3 | Cadena de búsqueda "exacta" no se muestra en el texto | Alto | La sección dice *"La cadena de búsqueda exacta aplicada se detalla en la Figura 2.1"* (el diagrama PRISMA). Si el diagrama efectivamente contiene la cadena, está bien; si no, la cadena no está documentada en ningún lado visible. Verificar. |
| RSL-4 | Periodo 2020-2025 es corto | Medio | La RSL excluye trabajos anteriores a 2020, pero el marco teórico cita a McCombs (1972), Luhmann, Berry (2011), Meunier (2022). Los criterios de exclusión (CE2: "tecnologías pre-transformer u obsoletas") justifican el recorte para la RSL, pero no para el marco teórico. La distinción debería explicitarse. |
| RSL-5 | Cribado realizado por un solo evaluador (el autor) | Medio | En una RSL estándar, el cribado se realiza con dos evaluadores independientes y se mide el acuerdo inter-evaluador (kappa de Cohen). El autor declara *"cuatro fases ejecutadas por el autor"* (singular). Para una tesina de grado esto es aceptable, pero conviene reconocerlo como amenaza a la validez en la propia sección. |
| RSL-6 | Criterio CE5 ("texto completo no disponible públicamente") descarta 54 papers | Bajo | Es un criterio pragmático razonable pero elimina gran parte del corpus. Conviene al menos listar los nombres/títulos de los 54 descartados por CE5, o justificar por qué el acceso restringido los invalida para los propósitos de la tesina. |

#### 3.2.3 Estudios incluidos

Se incluyen 9 estudios, agrupados por PR:
- PR1: milbauer2023, pavlyshenko2024
- PR2: haider2025, sundar2025
- PR3: behbahanian, neupane2025, ameer:2025, begum:2024, somasundharam:2025

**Evaluación: [Regular — 6/10]**

**Puntos fuertes:**
- La Tabla 2.1 (estudios-rsl) es un buen formato: resume estudio, aporte central y limitación.
- La lectura transversal del corpus (líneas 246-248) está bien hecha y muestra un patrón arquitectónico común.
- La identificación de limitaciones transversales es útil.

**Problemas:**

| # | Problema | Severidad | Detalle |
|---|---|---|---|
| EST-1 | behbahanian tiene año "s.f." | Alto | Una RSL formal con PRISMA requiere artículos con fecha verificable. Un artículo sin fecha ("s.f.") no debería incluirse en el conjunto final, o su inclusión debería estar explícitamente justificada. |
| EST-2 | somasundharam:2025 tiene autores secundarios "pendientes de completar" (nota en refs.bib) | Alto | Referencia incompleta. Debe completarse o excluirse. |
| EST-3 | Sundar2025 tiene un error de atribución de autoría | Medio | El primer autor real es **Samuel**, no Sundar, según la nota en `refs.bib` línea 184. El texto de la tesina cita `\citet{sundar2025}` y mostrará "Sundar et al.", que es incorrecto. Hay que renombrar el key a `samuel2025` y actualizar todas las menciones. |
| EST-4 | Distribución muy desigual de estudios | Bajo | PR1 tiene 2 estudios, PR2 tiene 2, PR3 tiene 5. El propio autor lo reconoce ("refleja la madurez relativa de cada línea"). Aceptable, pero un tribunal podría cuestionar por qué PR3 tiene más peso. |
| EST-5 | Falta una columna "caso de aplicación" en la tabla | Bajo | Muchos estudios evaluados se aplican a casos específicos (elecciones US 2024, tema "AI phobia"). Falta una columna que lo haga explícito para comparar dominios. |

### 3.3 Estado del Arte (Sección 2.3)

Tres subsecciones que corresponden a las tres PR. Cada estudio se analiza por separado.

**Evaluación: [Bueno — 7/10]**

**Fortalezas:**
- Estructura limpia que respeta la correspondencia con las PR.
- Análisis individual de cada estudio, no solo una enumeración.
- Buen uso del vocabulario técnico.

**Debilidades:**

| # | Problema | Severidad | Detalle |
|---|---|---|---|
| EA-1 | No hay tabla comparativa de trabajos relacionados | Alto | Es **imprescindible** en una tesina con estado del arte. Una tabla del tipo: Autor (Año) / Problema / Enfoque / Aporte / Limitación / Relación con esta tesina. Actualmente esa información está embebida en el texto y en la tabla de la RSL, pero la RSL no tiene la columna "Relación con esta tesina" que es la que justifica el aporte propio. |
| EA-2 | La subsección 2.3.3 (arquitecturas de software con IAG) se convierte en una enumeración de sistemas | Medio | La descripción de cada sistema es más bien una lista de características técnicas sin crítica comparativa. Falta un párrafo de análisis transversal que compare arquitecturas. |
| EA-3 | No se mencionan trabajos competidores que no calificaron a la RSL | Bajo | Una revisión integral del estado del arte debería mencionar —aunque sea brevemente— los trabajos que existían antes del corte 2020 pero siguen siendo relevantes (p. ej., sistemas de análisis de medios anteriores al Transformer). |

### 3.4 Síntesis Crítica y Brechas (Sección 2.4)

Esta sección es **el mejor aporte del Capítulo 2**. Identifica cinco brechas:
- Escalabilidad y consistencia de anotaciones
- Robustez del scraping
- Trazabilidad en ciencias sociales
- Calibración de incertidumbre
- Gobernanza de publicación y responsabilidad editorial

**Evaluación: [Muy bueno — 8.5/10]**

**Punto fuerte clave:** cada brecha está directamente relacionada con el diseño del capítulo 3 (ver sección siguiente), lo que demuestra coherencia entre revisión y propuesta.

**Problema único:**

| # | Problema | Severidad | Detalle |
|---|---|---|---|
| SC-1 | No todas las brechas se recuperan en los objetivos | Medio | La brecha de "estándares interoperables de anotación" y la de "calibración de incertidumbre" no aparecen en OE1, OE2 ni OE3. Se abordan en el diseño del capítulo 3 pero no están formuladas como objetivos. Esto debilita la trazabilidad. |

### 3.5 Bibliografía del Capítulo 2 — Estado de las entradas

Problemas bibliográficos detectados (repetidos de `refs.bib`):

| Entrada | Problema | Corrección |
|---|---|---|
| `luhmann2000` | Tipado como `@article`, cuando es un libro | Cambiar a `@book` con `publisher = {Stanford University Press}` |
| `carlon:2020` | `journal = {Nueva Editorial Universitaria, San Luis}` — es un libro | `@book` con `publisher` |
| `meunier:2022` | `journal = {Londres: Bloomsbury}` — es un libro | `@book` con `publisher = {Bloomsbury}`, `address = {London}` |
| `tan:1999` | `publisher` contiene un journal mal formateado | Cambiar a `@inproceedings` con `booktitle` correcto |
| `bertagnolio2023` | El paper es sobre ruido de turbinas eólicas, no sobre integración de LLMs en procesos | **Reemplazar por una referencia correcta** sobre el tema |
| `sundar2025` | Key engañoso; primer autor es Samuel | Renombrar a `samuel2025` y actualizar citas |
| `johnyprompt` | Key no sigue convención | Renombrar a `zamfirescu2023` |
| `prompt-eng:2024` | White paper de Google tipado como `@article` | Cambiar a `@misc` o `@techreport` con URL |
| `somasundharam:2025` | Autores secundarios pendientes de completar | Completar o eliminar |
| `behbahanian` | Año s.f. | Justificar o excluir de la RSL |

---

## 4. Análisis en profundidad del Capítulo 3

### 4.1 Evaluación general

El capítulo 3 es **la sección más sólida de toda la tesina**. La caracterización del pipeline como sistema de Tubos y Filtros está hecha con rigor, conocimiento profundo del estilo arquitectónico y buena articulación con la bibliografía fundacional (Garlan & Shaw 1994, Shaw & Garlan 1996) y con el catálogo de Cristia & Pomponio (2025). Las deformaciones (repositorio común + Claim Check + sintonizadores) están justificadas con referencia a Hohpe & Woolf y a la práctica industrial. El apéndice A, que caracteriza los tipos de datos y la cadena de procedencia, es técnicamente impecable y constituye el aporte más original de la tesina.

**Evaluación general: [Muy bueno — 8.5/10]** (sobre la parte no vacía)

### 4.2 Estructura interna

El capítulo está organizado en 4 secciones principales:
- §3.1 El estilo Tubos y Filtros (fundamento teórico del estilo)
- §3.2 El framework como sistema de Tubos y Filtros (aplicación al caso)
- §3.3 Implementación en Odoo (**VACÍO** en sus tres subsecciones)
- §3.4 Síntesis del capítulo (**VACÍO**)

### 4.3 Sección 3.1 — El estilo Tubos y Filtros

**Evaluación: [Muy bueno — 9/10]**

#### 4.3.1 Subsección 3.1.1 — Componentes, conectores y patrón estructural
- Definición clara de filtros y tubos.
- Buena referencia a cristia:2025, garlanshaw:1994, shawgarlan:1996.
- Mención al cierre composicional, que es una propiedad clave y está bien fundamentada.
- Sin problemas de contenido.

#### 4.3.2 Subsección 3.1.2 — Modelo computacional e invariantes
- Los cuatro invariantes esenciales están correctamente enunciados.
- La distinción entre filtros activos y pasivos es precisa.
- **Acierto notable:** la aclaración de que el invariante 3 se refiere al orden de *scheduling* interno y no a las dependencias de flujo. Este es un matiz sutil que muchos trabajos no aclaran.
- La deducción de tres consecuencias (sustituibilidad, auditabilidad lineal, ejecución concurrente) es correcta.

#### 4.3.3 Subsección 3.1.3 — Justificación del estilo
- Esta subsección es la más argumentativa del capítulo y cumple bien su función.
- **Fortaleza principal:** vincula las invariantes del estilo con las necesidades concretas del problema (fragilidad del scraping → sustituibilidad; falta de trazabilidad → auditabilidad lineal; diversidad de casos → composicionalidad).
- **Problema menor [Bajo]:** la subsección menciona al final que el diseño no es una "instancia pura" del estilo sino una "variante heterogénea" con repositorio compartido. Esto se desarrolla en §3.2.5 pero la mención anticipada aquí puede confundir al lector no avisado. Una línea de transición más explícita ayudaría.

### 4.4 Sección 3.2 — El framework como sistema de Tubos y Filtros

**Evaluación: [Muy bueno — 8.5/10]**

#### 4.4.1 Subsección 3.2.1 — Vista de conjunto
- El diagrama (Figura 3.1, `Diagrama-Arquitectura.png`) es técnicamente muy bueno. Muestra los 7 filtros, los 14 puertos, los sintonizadores modulares, el filtro compuesto de Recuperación aumentada, el repositorio común, la fuente (portales) y el sumidero (presentación). La leyenda y la tabla de referencia están completas.
- El texto introductorio describe bien la configuración general y hace una mención al cierre composicional.
- **Problema [Medio]:** se menciona explícitamente que "la iteración del experto del dominio sobre los resultados [...] tiene lugar entre corridas sucesivas del sistema y no como tubo de retorno en la red". Esto es importante y está bien aclarado aquí, pero contradice parcialmente la sección 4.7 del Capítulo 4 ("Refinamiento iterativo") que lo presenta como un paso del proceso. Esta inconsistencia debe reconciliarse (ver Observación Inc1 al inicio del informe).

#### 4.4.2 Subsección 3.2.2 — Los filtros del framework
- Los 7 filtros están especificados con: interfaz (puertos de entrada y salida), sintonizador, acceso al repositorio, y especificación funcional.
- La especificación es minuciosa y técnica. Cada filtro menciona su relación con las brechas del capítulo 2.
- **Problemas:**
  - **[Medio]** El filtro de Verificación tiene una nota TODO pendiente (línea 491): falta citar la literatura de LLM-as-judge / verificación multiagente. Esta es una parte importante del diseño que debe estar fundamentada.
  - **[Bajo]** La especificación del filtro de Decodificación asume que los modelos generativos pueden producir "salida estructurada válida" (JSON conforme al esquema). Esto depende de técnicas como *constrained decoding* (Willard & Louf 2023, JSONSchemaBench 2025, ya citados). La relación podría hacerse explícita.
  - **[Medio]** El filtro de Enriquecimiento semántico está dentro del filtro compuesto "Recuperación aumentada", pero su relación con RAG (Retrieval-Augmented Generation, Lewis et al. 2020) no se explica explícitamente. Lewis et al. está citado pero no se usa para justificar este filtro compuesto. Hay que conectar explícitamente el filtro compuesto con la literatura de RAG.

#### 4.4.3 Subsección 3.2.3 — Conectores: tubos tipados
- Muy sólida. La caracterización de la cardinalidad como parte de la firma del tubo (Tipo[c]) es un aporte conceptual limpio.
- La transición N → N → M → M → M → M → 1 está bien explicada.
- Sin problemas de contenido.

#### 4.4.4 Subsección 3.2.4 — Especializaciones aplicadas
- Las dos especializaciones (pipeline + tubos tipados) están bien justificadas con referencia a la literatura original.
- Sin problemas.

#### 4.4.5 Subsección 3.2.5 — Repositorio común sobre PostgreSQL
- Excelente argumentación del patrón Claim Check con referencia a Hohpe & Woolf y Ritter.
- **Acierto:** la justificación desde la semántica nativa del ORM de Odoo (recordsets referenciales) — esto demuestra que la decisión no es arbitraria sino alineada con la plataforma.
- Sin problemas.

#### 4.4.6 Subsección 3.2.6 — Sintonizadores
- Buen uso de la referencia a Garlan & Shaw (control interface) y a scikit-learn (set_params).
- La decisión de exponer sintonizadores solo en los filtros con decisiones de dominio es defendible.
- La descripción del sintonizador de Composición (el panel de templates) es particularmente útil y se alinea con el aporte OE2/OE3.

#### 4.4.7 Subsección 3.2.7 — Verificación de los invariantes
- Cada invariante se verifica explícitamente. Esto es metodológicamente correcto.
- Sin problemas.

#### 4.4.8 Subsección 3.2.8 — Ventajas y limitaciones
- Muy honesta: reconoce que el diseño no es una instancia pura del estilo, que se pierde el procesamiento incremental, que el verificador humano añade latencia.
- La mención al compromiso (trade-off) entre throughput y rigor editorial es un aporte maduro.
- Sin problemas.

### 4.5 Sección 3.3 — Implementación en Odoo

**Estado: VACÍO** (subsecciones 3.3.1, 3.3.2, 3.3.3)

Esta sección es crítica porque:
- Conecta el diseño abstracto del capítulo 3 con el OE1 (módulo Odoo).
- Responde a la pregunta "¿cómo se materializa esto en código real?".
- Sin ella, la arquitectura queda como una propuesta teórica sin ancla en la implementación.

**Contenido mínimo a desarrollar:**

#### 3.3.1 Infraestructura preexistente del entorno CAETI/CIM
Describe el estado de partida:
- Plataforma Odoo Community existente (versión, módulos actuales).
- Herramienta de scraping existente (spiders, librerías BeautifulSoup/Selenium/Newspaper3k).
- Capa inicial de RAG existente (mencionada en la introducción del capítulo 3 pero sin referencia bibliográfica concreta; tiene TODO pendiente sobre Raimondo Anselmino et al.).

#### 3.3.2 Stack tecnológico
Lista y justifica: Python + Odoo ORM, PostgreSQL, librerías de scraping (BeautifulSoup, Selenium, Newspaper3k), modelo de embedding, modelo generativo (ChatGPT/OpenAI API, o alternativa). Cada elección debe justificarse brevemente.

#### 3.3.3 Materialización: mapeo de filtros y tubos al módulo Odoo
Tabla obligatoria:

| Filtro (cap. 3 abstracto) | Modelo Odoo / Servicio | Puerto entrada (recordset) | Puerto salida (recordset) | Sintonizador (vista) |
|---|---|---|---|---|
| Extracción | `portal.models.Scraper` | flujo del portal | `Noticia[N]` | Vista de configuración de portales |
| Enriquecimiento | `news.models.EmbeddingService` | `Noticia[N]` | `Embedding[N]` | (config. del implementador) |
| Composición | `prompt.models.TemplateComposer` | `Embedding[N]` | `Prompt[M]` | Panel de templates |
| Invocación | `iag.models.LLMInvoker` | `Prompt[M]` | `RespuestaIAG[M]` | (config. del implementador) |
| Decodificación | `analysis.models.Decoder` | `RespuestaIAG[M]` | `Análisis[M]` | (config. del implementador) |
| Verificación | `verification.models.Verifier` | `Análisis[M]` | `Veredicto[M]` | Selector de criterio/ejecutor |
| Normalización | `consolidation.models.Normalizer` | `Veredicto[M]` | `Resultado` | Variables de comparación |

### 4.6 Sección 3.4 — Síntesis del capítulo

**Estado: VACÍO**

Debe contener:
- Recapitulación breve del aporte arquitectónico.
- Explícito cierre con el capítulo siguiente (mapa de procesos): cómo los filtros abstractos se operativizan en procesos BPMN.
- Resumen de las decisiones de diseño que merecen ser tenidas en cuenta en la validación (cap. 5).

---

## 5. Propuestas de mejora concretas

### 5.1 Mejoras para el Capítulo 2

#### 5.1.1 Cambiar el título del capítulo [Medio]
Propuesta: **"Marco teórico y revisión sistemática de la literatura"**. Refleja los tres bloques reales del capítulo.

#### 5.1.2 Corregir la cita a Bertagnolio 2023 [Alto]
El paper citado trata sobre ruido de turbinas eólicas, no sobre integración de LLMs en procesos. Opciones:
- Reemplazarlo por un trabajo que efectivamente aborde integración de LLMs en BPMN o en pipelines de procesos (p. ej., un paper que documente un caso de uso industrial de LLMs orquestados).
- Si la cita es solo de pasada, eliminar el párrafo.

#### 5.1.3 Reformular el párrafo sobre Transformers [Medio]
Texto actual: *"La entrada y la salida del modelo se construyen sobre embeddings: representaciones vectoriales aprendidas que codifican unidades lingüísticas en un espacio continuo de alta dimensionalidad."*

Propuesta de reescritura: *"El Transformer introduce el mecanismo de self-attention, que permite a cada posición de la secuencia atender al contexto completo en paralelo, superando las limitaciones de dependencia de largo alcance de las arquitecturas recurrentes. Los embeddings —representaciones vectoriales densas de unidades lingüásticas— constituyen la interfaz de entrada y salida del modelo; cabe notar que los embeddings eran ya un recurso común en NLP previo al Transformer (Word2Vec, GloVe, FastText), pero su integración con el mecanismo de atención contextual les otorga una riqueza semántica significativamente mayor."*

#### 5.1.4 Eliminar la mención de DALL-E 2 [Bajo]
O suprimirla o justificarla si hay un plan de análisis multimodal. Actualmente es un non sequitur dado el objeto de estudio (noticias textuales de portales).

#### 5.1.5 Agregar Entman (1993) al marco teórico [Medio]
Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51-58.

Es una cita canónica en análisis de framing y la tesina trata parcialmente sobre encuadre mediático. Debe agregarse al marco teórico.

#### 5.1.6 Agregar tabla comparativa al Estado del Arte [Alto]
Incluir una tabla tipo:

| Estudio | Problema | Enfoque | Caso | Aporte | Limitación | Relación con esta tesina |
|---|---|---|---|---|---|---|

Esto reemplaza la dispersión actual del análisis y permite al tribunal ver de un vistazo el aporte propio.

#### 5.1.7 Mejorar la descripción metodológica de la RSL [Medio]
- Reconocer en el texto que la evaluación fue hecha por un solo evaluador (amenaza a la validez).
- Consultar al menos ACM Digital Library y Scopus además de SciSpace/Google Scholar.
- Separar "biblioteca personal" de las bases de datos formales; tratarla como snowballing.
- Mostrar la cadena de búsqueda en el texto, no solo en el diagrama.

#### 5.1.8 Corregir errores bibliográficos [Alto]
Revisar la tabla del punto 3.5 de este informe. Los 10 errores están documentados y la corrección de cada uno es directa.

#### 5.1.9 Vincular las 5 brechas más explícitamente con los objetivos [Alto]
La sección 2.4 ya hace algo de esto en el párrafo final, pero es insuficiente. Conviene agregar una tabla de trazabilidad:

| Brecha | ¿La aborda OE1? | ¿La aborda OE2? | ¿La aborda OE3? | ¿Cómo? |
|---|---|---|---|---|

Esto refuerza la coherencia del argumento central.

### 5.2 Mejoras para el Capítulo 3

#### 5.2.1 Completar la sección 3.3 — Implementación en Odoo [Crítico]
Ver detalle en punto 4.5 de este informe. Sin esta sección, el diseño arquitectónico queda sin anclar en la implementación y el OE1 no queda trazado.

#### 5.2.2 Completar la sección 3.4 — Síntesis del capítulo [Alto]
Debe cerrar el capítulo recapitulando el aporte y dando una transición al capítulo 4.

#### 5.2.3 Resolver los TODO pendientes [Alto]
- **Línea 344:** TODO "citar Raimondo Anselmino et al., Capítulo SIMPOSIO CIENCIAS SOCIALES COMPUTACIONALES 2024". Debe hacerse la cita o eliminar la afirmación.
- **Línea 491:** TODO "citar literatura de LLM-as-judge / verificación multiagente". Si se mantiene el filtro de Verificación con ejecutor de LLMs, se debe citar:
  - Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS*.
  - Liu et al. (2024). A Survey on LLM-as-a-Judge.
  - Si se menciona verificación multiagente: AutoGen (Wu et al. 2023), CAMEL (Li et al. 2023).

#### 5.2.4 Conectar RAG con el filtro compuesto [Medio]
El filtro compuesto "Recuperación aumentada" está compuesto por Enriquecimiento semántico + Composición de contexto. En la sección 3.2.2 se describe cada filtro por separado, pero no se explica explícitamente que la composición de ambos constituye un patrón RAG (Retrieval-Augmented Generation, Lewis et al. 2020). Lewis 2020 está citado en `refs.bib` pero nunca se cita `\citep{lewis:2020}` en el texto principal. Debe hacerse explícito: "los filtros de Enriquecimiento semántico y Composición de contexto, en su composición, instancian el patrón de Recuperación Aumentada (RAG) documentado por \citet{lewis:2020}."

#### 5.2.5 Aclarar la relación entre constrained decoding y el filtro de Decodificación [Medio]
La especificación del filtro de Decodificación asume que la IAG produce salida estructurada válida. Esto depende de constrained decoding (Willard & Louf 2023, Geng et al. 2025 — ya citados). Debe hacerse explícito en la especificación cómo se garantiza esto, o al menos mencionar que se apoya en estas técnicas.

#### 5.2.6 Considerar integrar el apéndice A al cuerpo principal [Medio — decisión del director]
El apéndice A (tipos de datos, firmas funcionales, cadena de procedencia) es técnicamente el aporte más original de la tesina. Relegarlo a apéndice le resta visibilidad. Opciones:
- Dejarlo como apéndice pero reforzar las referencias desde el cap. 3 principal.
- Convertirlo en una sección adicional del capítulo 3 (p. ej. §3.5 "Contratos de datos del pipeline") y mover el apéndice a material complementario.

**Mi recomendación:** dejarlo como apéndice pero agregar una subsección de resumen en el capítulo 3 (§3.2.9) que introduzca los tipos y remita al apéndice. Esto preserva la organización actual pero le da al apéndice mayor visibilidad argumental.

#### 5.2.7 Agregar una subsección de "Limitaciones del diseño" adicional [Bajo]
La sección 3.2.8 ya discute limitaciones, pero podría extenderse con:
- Dependencia de la calidad del scraping (cambios estructurales en portales).
- Costo computacional de invocar LLMs por cada prompt (M promtps × precio por token).
- Riesgo de sesgo del modelo en la etapa de Verificación si el ejecutor es un LLM.

#### 5.2.8 Revisar el orden de presentación de los filtros [Bajo]
El diagrama y el texto presentan: Extracción, Enriquecimiento, Composición, Invocación, Decodificación, Verificación, Normalización. Pero en la especificación del capítulo 3, Verificación se presenta como un filtro "adicional" al final, cuando conceptualmente podría ir antes de Decodificación (primero se verifica la fidelidad al documento empírico, después se estructura). Esto es una decisión de diseño defendible pero debe explicitarse.

---

## 6. Resumen ejecutivo

### 6.1 Estado general de la tesina

| Dimensión | Evaluación |
|---|---|
| Planteo del problema | Bueno; motivación bien argumentada pero falta una pregunta de investigación explícita |
| Objetivos | Regular; desajustes entre formulación y contenido real del desarrollo |
| Marco teórico | Muy bueno; progresión argumental sólida |
| Revisión sistemática | Bueno; PRISMA respetado formalmente, pero bases de datos no canónicas y referencias incompletas |
| Estado del arte | Bueno; faltan tablas comparativas |
| Identificación de brechas | Muy bueno; las 5 brechas están bien articuladas |
| Diseño arquitectónico | Muy bueno; rigor y conocimiento profundo del estilo Tubos y Filtros |
| Apéndice — Tipos de datos | Excelente; aporte más original de la tesina |
| Implementación Odoo | No documentada — secciones vacías |
| Mapa de procesos | Parcial — 5 de 8 secciones vacías |
| Caso de aplicación | Completamente vacío |
| Conclusiones | Completamente vacías |
| Bibliografía | Regular; errores tipográficos serios, una referencia incorrecta (bertagnolio2023), varias incompletas |
| Redacción | Buena en lo general; errores ortográficos reiterados (scrapping, NPL); algunas frases coloquiales |

### 6.2 Prioridades para la próxima etapa

Ordenadas por severidad decreciente:

1. **[Crítico]** Completar el Capítulo 5 (Ejemplo de aplicación) — es la validación empírica.
2. **[Crítico]** Completar el Capítulo 6 (Conclusiones y Trabajo Futuro) — es el cierre.
3. **[Alto]** Completar Capítulo 3.3 y 3.4 — sin esto el diseño queda sin anclar en la implementación.
4. **[Alto]** Completar Capítulo 4.1, 4.2, 4.6, 4.7, 4.8 — sin esto el mapa de procesos es una lista con agujeros.
5. **[Alto]** Corregir los 10 problemas bibliográficos (ver tabla en punto 3.5).
6. **[Alto]** Resolver los TODO pendientes (Raimondo Anselmino; LLM-as-judge).
7. **[Alto]** Reconciliar el mapa de procesos del Capítulo 4 con el pipeline del Capítulo 3 (inc1).
8. **[Alto]** Reformular objetivos para reflejar el alcance real del trabajo.
9. **[Alto]** Agregar tabla comparativa al estado del arte.
10. **[Medio]** Cambiar título del Capítulo 2.
11. **[Medio]** Reformular párrafo sobre Transformers.
12. **[Medio]** Eliminar DALL-E 2 o justificarlo.
13. **[Medio]** Agregar Entman (1993) al marco teórico.
14. **[Medio]** Tabla de trazabilidad entre brechas y objetivos.
15. **[Medio]** Corregir errores ortográficos (scraping, NPL, tildes).
16. **[Bajo]** Agregar listas de figuras y tablas tras el índice.

### 6.3 Aspectos a discutir con el director

1. **¿Se reformulan los objetivos específicos o se mantienen?** Si se reformulan, hay que actualizar también el Capítulo 2.4 para que la trazabilidad entre brechas y objetivos quede explícita.
2. **¿El apéndice A queda como apéndice o se integra al cuerpo central?**
3. **¿Se mantiene la denominación "tesina" o "tesis" en el título del trabajo?** El nombre correcto según la carrera es "tesina", pero el uso de "tesis" en línea 790 es un error puntual a corregir.
4. **¿Qué tan estricto se quiere ser con la RSL formal?** Si se mantiene el estándar PRISMA formal, hay que agregar IEEE/ACM/Scopus; si se acepta como "revisión narrativa con elementos PRISMA", se puede mantener como está pero con una reformulación del lenguaje.
5. **¿Cómo manejar la referencia a Bertagnolio 2023?** Reemplazarla por una referencia correcta es imperativo; eliminar el párrafo es la opción conservadora.

---

## 7. Notas para la próxima revisión (REV-002)

Esta revisión cubre estructura, planteo y capítulos 2 y 3. Para la próxima revisión (REV-002) se sugiere cubrir:
- Análisis en profundidad del Capítulo 4 (mapa de procesos).
- Análisis del capítulo 5 (una vez completado el ejemplo de aplicación).
- Análisis del capítulo 6 (una vez completadas las conclusiones).
- Revisión bibliográfica integral de `refs.bib`.
- Revisión de la coherencia de los diagramas.
- Revisión ortográfica y tipográfica de todo el documento.

**Fin del informe REV-001.**
