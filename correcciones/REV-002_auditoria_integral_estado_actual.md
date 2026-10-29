# REV-002 — Auditoría integral del estado actual

| Campo | Valor |
|---|---|
| **Código** | REV-002 |
| **Nombre** | Auditoría integral del estado actual: seguimiento de REV-001, bibliografía, consistencia entre capítulos y producción |
| **Fecha de emisión** | 29 de octubre de 2026 |
| **Base** | Repo `github.com/lbassani12/tesina`, rama `main`, commit `adfc221` |
| **Archivos revisados** | `main.tex` (1897 líneas, ~295 KB), `refs.bib` (75 entradas), diagramas PNG/PUML, `.latexmkrc`, `correcciones/` |
| **Anexos** | `REV-002-anexo-bibliografico-borrador.md` (75 entradas verificadas una por una contra fuentes externas) · `REV-002-anexo-consistencia-borrador.md` (5 chequeos cruzados caps. 3-4-5-Apéndice) |
| **Alcance** | Documento completo, con foco en el delta desde REV-001 (09-07-2026) |
| **Autor de la revisión** | Hermes (agente) — **validada por el director** (Alejandro Sartorio, 29-10-2026). Estrategia cap. 6 aprobada: corrida nueva controlada por protocolo (opción a); ver `PROTOCOLO-CAP6.md` |

---

## 0. Criterio de severidad

Misma escala que REV-001: **Crítico** (impide la defensa o compromete el núcleo) · **Alto** (afecta coherencia entre capítulos o validez del argumento) · **Medio** (afecta comprensión o consistencia parcial) · **Bajo** (forma, estilo, claridad).

---

## 1. Seguimiento de REV-001 — qué se resolvió y qué sigue abierto

> **Nota de renumeración:** la estructura cambió desde REV-001. La implementación en Odoo es ahora el **Capítulo 4** (antes §3.3 vacía), el mapa de procesos es el **Capítulo 5**, el ejemplo de aplicación el **Capítulo 6** y las conclusiones el **Capítulo 7**. Las referencias a "cap. 5 vacío" de REV-001 corresponden al actual cap. 6.

| # | Problema REV-001 | Severidad original | Estado actual |
|---|---|---|---|
| C1 | Ejemplo de aplicación vacío (hoy cap. 6) | Crítico | 🔴 **Sigue abierto** — 6 secciones declaradas, cero contenido (L1638-1657) |
| C2 | Conclusiones vacías (hoy cap. 7) | Crítico | 🔴 **Sigue abierto** — capítulo sin una sola línea (L1659-1664) |
| C3 | §3.3.1-3.3.3 y §3.4 vacías (implementación) | Crítico | ✅ **Resuelto y superado** — la implementación es ahora un capítulo completo (cap. 4, ~560 líneas): infraestructura CAETI/CIM, stack, materialización con fichas de los 7 filtros, frontera con `wsf_noticias`, decisión de profundidad acordada con el director (20-08-2026, implementación de referencia `noticias_iag` commit `bca7dba`, 27 tests) |
| C4 | Cap. 4 (procesos) con 5 de 8 secciones vacías | Alto | ✅ **Resuelto** — cap. 5 completo: notación y actores, 7 procesos con 23 actividades, tabla de correspondencia biyectiva verificada, síntesis |
| C5 | TODOs sin resolver (Raimondo; LLM-as-judge) | Alto | 🟡 **Parcial** — LLM-as-judge resuelto (`zheng:2023` y `xi:2023` citados en L669); `raimondo:2024` citada 5 veces pero sigue `@unpublished` con datos editoriales pendientes; la cita de L261-266 (ex-Bertagnolio, ver §3) sigue abierta como TODO |
| — | Objetivos desalineados (P-OBJ-1 a P-OBJ-6) | Alto | ✅ **Resuelto** — DECISIONES-REV-001 implementada: objetivo general y OE1-OE4 reformulados y vigentes en §1.2 |
| — | Título del cap. 2 con signo de interrogación | Medio | ✅ **Resuelto** — "Marco teórico y revisión sistemática de la literatura" |
| — | Contratos de datos relegados al apéndice | Medio | ✅ **Resuelto** — §3.2.9 "Contratos de datos del pipeline" integrada al cap. 3; el apéndice conserva la especificación estructural |
| — | `bertagnolio2023` cita desajustada | Alto | 🔴 **Sigue abierto** — sin corregir desde REV-001 (ver §3) |
| — | Tabla comparativa de estado del arte | Alto | 🟡 La tabla 2.2/2.3 existe y fue corregida de layout (`a68133f`); verificar en REV-003 si satisface la recomendación original |

**Balance del delta:** de los 5 problemas críticos de REV-001 se resolvieron 2 (los de implementación y procesos, con calidad alta). Los 2 críticos restantes (caps. 6 y 7) son exactamente el camino crítico identificado en `HOJA-DE-RUTA.md`. La deuda bibliográfica grave no se tocó.

---

## 2. Estado actual por capítulo

| Capítulo | Estado | % est. |
|---|---|---|
| 1 Introducción (incl. §1.3 responsabilidades [A]-[F]) | Completo | 95 % |
| 2 Marco teórico + RSL | Completo, con deuda bibliográfica (§3) | 85 % |
| 3 Arquitectura (incl. §3.2.9 contratos) | Sólido; falta síntesis narrativa (TODO L793) | 95 % |
| 4 Implementación en Odoo | Completo | 95 % |
| 5 Mapa de procesos | Completo; 2 errores numéricos/omisión (§4) | 95 % |
| **6 Ejemplo de aplicación** | **Vacío** | **0 %** |
| **7 Conclusiones y Trabajo a Futuro** | **Vacío** | **0 %** |
| Apéndice — Tipos de datos (grafo de procedencia) | Completo; cardinalidad M vs M' (§4) | 90 % |

---

## 3. Auditoría bibliográfica (síntesis del anexo)

**Universo:** 75 entradas en `refs.bib`. **Resultado:** 65 OK-verificadas · 3 sospechosas · 2 no verificables · 5 huérfanas. Verificación contra Crossref, arXiv, Zenodo, DiVA y URLs directas (detalle entrada por entrada en el anexo).

### Problemas de severidad Alta

1. **`bertagnolio2023` — cita con contenido totalmente desajustado (L521), sin corregir desde REV-001.** El paper real (WIREs Energy and Environment 12(3):e469, DOI 10.1002/wene.469) trata sobre ruido de turbinas eólicas onshore; la tesina lo usa para fundamentar "la integración de modelos generativos dentro de mapas de procesos tecnológicos automatizados". La entrada además omite journal/volumen/DOI. **Acción:** reemplazar por `xi:2023` (verificada OK) u otra referencia que realmente aborde el punto, y cerrar simultáneamente el TODO de L261-266, que dejó la afirmación equivalente del cap. 2 **sin cita** (la línea está cortada con `%`).
2. **`somasundharam:2025` — autoría incorrecta.** El documento DiVA `diva2:1978319` es de **Nils Skoog** (Uppsala universitet, junio 2025); no existe ningún "Somasundharam" asociado. La note "autores secundarios pendientes de completar" enmascara el error. Además, L358 le atribuye el stack "LangChain + LLaMA-3" cuando la tesis real usa Gemini 1.5/2.5/2.0. Afecta 6 citas (L322, 324, 358, 439, 503) y claims de la RSL. **Acción:** reescribir la entrada como Skoog (2025), corregir la tabla de la RSL y revisar el claim del stack. **Riesgo de tribunal:** si la RSL incluyó un documento con autoría que no es tal, un revisor atento puede cuestionar el proceso de cribado completo — conviene corregirlo y, si el director lo considera, reconocerlo como errata de proceso.
3. **`behbahanian` — referencia no verificable con 9 citas.** ResearchGate devuelve 403 y ninguna fuente independiente confirma la existencia de "GlimzAI"; año "s.f.". Sustenta claims sustantivos (deduplicación semántica con Sentence-BERT, brecha de validación con usuarios) en L322, 324, 350, 381, 419, 451, 503. **Acción (decisión del director):** obtener el PDF por vía institucional, o sustituir la referencia y reescribir los claims que sostiene. No debe llegar así a la versión final.
4. **TODO activo L261-266:** afirmación sobre modelos generativos en pipelines de procesos queda sin cita. Candidatos verificados: `xi:2023` (OK); Wang et al. 2024 y Hong et al. 2024 (MetaGPT) pendientes de verificación.
5. **`raimondo:2024` — fuente no pública con 5 citas** (L517, 940, 947, 958, 964) que describe la infraestructura CAETI/CIM. `@unpublished` con datos editoriales pendientes. **Acción:** confirmar con la dirección si el capítulo del Simposio 2024 se publicó; si sí, migrar a `@incollection` completo.

### Problemas de severidad Media/Baja

- **`price:1997` (huérfana) — metadatos fabricados:** el artículo declarado no existe (mezcla un título real de Price & Tewksbury 1997 con elementos de otra obra); sin campo `year`. No contamina el texto porque no está citada, pero **debe eliminarse** del `.bib`.
- **`ameer:2025`:** falta la coautora Nimra Mairaj; el DOI 10.5281/zenodo.15856484 redirige al vigente 10.5281/zenodo.15856940. Citada 5 veces.
- **`iyengar:1987` (huérfana):** es un libro declarado como `@article`. Eliminar o corregir.
- **Huérfanas verificadas** `clementsetal:2010`, `zaharia:2012`, `greseclose:2005` (clave con errata): existen pero no se citan — eliminar o incorporar.
- **Normalización:** una decena de entradas citadas con DOI/páginas faltantes (`couldry:2017`, `berry:2011`, `mccombs:1972`, `gindin:2018`, `cristia:2025` sin URL, `chen:2023` con DOI dentro de `url`, `qian:2023`/`wu:2023` con clave 2023 y year 2024). Pasada de normalización recomendada antes de la entrega.

---

## 4. Auditoría de consistencia (síntesis del anexo)

**Resultado global:** 9 discrepancias — **0 críticas · 1 alta · 2 medias · 6 bajas**. Chequeos limpios: referencias cruzadas (0 rotas, 0 labels duplicados sobre 98 labels y 68 claves), nombres y responsabilidades de los 7 filtros idénticos entre §3.2.2 y las fichas del cap. 4, numeración de puertos 1-14 consistente en las cuatro vistas, biyección procesos↔filtros de §5.3 verificada.

### Discrepancia Alta (única)

**Cardinalidad de `Análisis`/`Veredicto`: M vs M'.** §3.2.3 (L690, 696) afirma que Decodificación "preserva M" (cadena N→N→M→M→M→M→1); §3.2.9 (L778-779) y el Apéndice (L1783, 1801, 1864-1874) firman todo con M. Pero §3.2.2 (L652, 666) dice que la compuerta de Decodificación **descarta** lo no conforme, y los caps. 4 (L1315, 1325: "M' ≤ M") y 5 (L1505-1506, 1605-1607) usan M'. El propio registro maestro del cap. 3 (L843) usa "los M' veredictos" — notación que el capítulo nunca define. **Diagnóstico:** la decisión editorial real es M'≤M desde Decodificación; §3.2.3, §3.2.9 y el Apéndice quedaron desactualizados. **Fix sugerido:** unificar a M'≤M (corregir L690, 696, 778-779, 1783, 1801, 1868-1870, 1874) y definir M' formalmente en §3.2.3 y §A.1. Es mecánico pero toca ~10 puntos en 4 lugares: hacerlo en un solo commit atómico.

### Discrepancias Medias

1. **L1636: "veintidós actividades"** — el mapa documenta y tabula **23** (01:3 + 02:3 + 03:4 + 04:8 + 05:2 + 06:2 + 07:1). Corregir el numeral y verificar el PNG `Diagrama-Procesos.png`.
2. **Registro maestro [D] (L844) omite la actividad 03.04**, a la que §5.3 (L1593) y §3.2.2 (L679) sí asignan control editorial. Agregarla a la columna Procesos de [D].

### Discrepancias Bajas (6)

Filtro compuesto "Recuperación aumentada" no mencionado en caps. 4-5 (se materializa como dos etapas sin explicitarlo — agregar frase en §4.3.2); actividad 01.01 atribuida a [B] en la narrativa (L1465) pero solo [A] en tabla §5.3 y registro (L1571, 830); enumeración de L1631 omite 03.01 (primera superficie del sintonizador de Composición); nombres cortos de filtros en §3.2.9/§A.5 vs canónicos (nota de convención en §A.1); 30 `\label` sin referenciar (la mayoría se resolverá al escribir caps. 6-7, pero `sec:arq-car-analisis`, `anexo:tipo-analisis` y `anexo:tipo-resultado` merecen citarse ya); comentario TODO obsoleto L793-795 (anuncia que la columna del cap. 4 se completará "cuando exista" — ya existe).

---

## 5. Pasada de producción

- **Compilación:** `tectonic main.tex` → éxito, PDF 1.69 MiB. Warnings: destinos hyperref duplicados (`@page.1`, `@table.3.2/4.1/5.1`) — severidad Baja, cosmético.
- **Herramienta:** el repo usa latexmk (`.latexmkrc` con caché local de luaotfload); la verificación con tectonic confirma que las fuentes compilan, pero la pasada final debe hacerse con la cadena del proyecto.
- `main.pdf` versionado en el repo.

## 6. TODOs activos en `main.tex`

| Línea | Contenido | Severidad |
|---|---|---|
| 262 | Reemplazar nota por cita verificable (par de `bertagnolio2023`) | Alta |
| 793 | Redactar síntesis narrativa del cap. 3 | Media |
| 799 | Cambiar columna `p{1.9cm}` por `X` cuando exista cap. 6 | Baja (bloqueada por cap. 6) |
| 824-859 | 6 celdas "(por completar)" de la matriz maestra [A]-[F] | Altas (bloqueadas por cap. 6 — se completan con la evidencia del caso) |
| 1303 | Mover medición (Estudios 32 y 59: 9/13 vs 13/13; 347 s vs 570 s) a tabla de configuración técnica de §4.3 | Media |

---

## 7. Prioridades integradas (orden de trabajo sugerido)

| # | Severidad | Acción | Fase RUTA-001 |
|---|---|---|---|
| 1 | **Crítico** | Cap. 6: protocolo del experimento → ejecución → escritura | Fases 1-3 |
| 2 | **Crítico** | Cap. 7: conclusiones (depende de #1) | Fase 4 |
| 3 | Alta | Unificar cardinalidad M/M' (commit atómico, ~10 puntos) | Fase 2 (deuda) |
| 4 | Alta | Cerrar L261-266 + reemplazar `bertagnolio2023` por cita verificada (`xi:2023` u otra) | Fase 2 |
| 5 | Alta | Corregir `somasundharam:2025` → Skoog (2025) + tabla RSL + claim del stack | Fase 2 |
| 6 | Alta | Decidir `behbahanian`: conseguir PDF o reescribir 9 citas | Fase 2 (decisión del director) |
| 7 | Media | "veintidós" → "veintitrés" (L1636) + verificar PNG; matriz [D] agregar 03.04; síntesis cap. 3 (L793); mover mediciones a §4.3 (L1303); `raimondo:2024` datos editoriales; `ameer:2025` coautora+DOI | Fase 2 |
| 8 | Baja | 6 discrepancias menores de consistencia + huérfanas (`price:1997` fabricada: eliminar) + normalización de `refs.bib` | Fase 2 |
| 9 | — | Revisión final 5 pasadas + tribunal simulado | Fase 5 |

## 8. Decisiones pendientes del director

1. **Estrategia cap. 6:** (a) corrida nueva controlada por protocolo —recomendada— vs (b) formalización de estudios existentes (32/59) como referencia comparativa.
2. **Permisos de push:** invitar a `wsf` como colaborador de `lbassani12/tesina` (hoy 403; los cambios de esta revisión están en la rama local `rev003/00-gestion-orientacion`).
3. **Alcance del experimento:** caso único vs dos templates/casos comparativos (el buffer hasta marzo lo permite).
4. **`behbahanian`:** gestión institucional para obtener el PDF, o reescritura de los claims.
5. **Validación de este informe** y del orden de prioridades de §7.

## 9. Observaciones para el director

- **Señal de proceso:** `bertagnolio2023` fue señalada en REV-001 (julio) y sigue abierta en octubre. Los items de deuda bibliográfica grave tienden a no cerrarse solos: conviene que la Fase 2 los asigne explícitamente (los puede ejecutar Hermes vía PR una vez resuelto el permiso de push).
- **Riesgo de tribunal — RSL:** el caso `somasundharam`/Skoog es el más delicado: una referencia con autoría inexistente dentro del corpus de una revisión *sistemática* habilita a cuestionar el cribado. La corrección es simple; lo que debe decidir usted es si además se agrega una nota metodológica sobre la verificación post-hoc de las fuentes.
- **Fortaleza para la defensa:** la consistencia estructural del documento es alta (0 refs rotas, biyección verificada, nombres estables entre vistas). La única falla estructural (M/M') es de notación, no de diseño.
- **La matriz maestra [A]-[F] es el mejor activo de trazabilidad de la tesina**: cuando el cap. 6 exista, sus 6 celdas pendientes se completan con la evidencia del caso y la tesis queda con una trazabilidad objetivos→garantías→evidencia poco común en trabajos de grado.

## 10. Próxima revisión (REV-003)

- Borrador del protocolo del experimento (`PROTOCOLO-CAP6.md`) — Fase 1.
- Revisión de los caps. 6 y 7 a medida que Lucio los escriba (auditoría de claims con taxonomía de evidencia).
- Verificación de la aplicación de las correcciones de este informe.
- Pasada final 5-pasadas + tribunal simulado (Fase 5).

---

**Fin del informe REV-002.**
