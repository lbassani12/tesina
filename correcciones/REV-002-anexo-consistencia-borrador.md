# REV-002 — Anexo: verificación de consistencia interna (borrador)

**Alcance:** `main.tex` (1897 líneas). Cap. 3 (Arquitectura, l.512–865), Cap. 4 (Implementación en Odoo, l.866–1428), Cap. 5 (Mapa de procesos, l.1429–1637) y Apéndice (Tipos de datos, l.1683–1897). Cinco chequeos: (1) filtros, (2) puertos y tipos, (3) marcadores `\resp{A}`–`\resp{F}`, (4) referencias cruzadas, (5) tabla de correspondencia §5.3.

**Convención de líneas:** todas las líneas citadas son de `main.tex` tal como está hoy.

---

## Chequeo 1 — Los 7 filtros en caps. 3, 4 y 5

Nombres canónicos esperados: Extracción, Enriquecimiento semántico, Composición de contexto, Invocación generativa, Decodificación, Verificación, Normalización.

| Elemento | Cap. 3 | Cap. 4 | Cap. 5 | Apéndice | Veredicto | Líneas implicadas | Severidad |
|---|---|---|---|---|---|---|---|
| Extracción (nombre) | `\paragraph{Extracción.}` | §4.2.2 "Realización del filtro de Extracción" + `\subsubsection{Extracción}` + tabla l.895 | act. 02.01–02.02; §5.3 l.1579–1583 | firma §A.5 "Extracción" | coincide | 605, 953, 1167, 895, 1476–1477, 1581, 1864 | — |
| Enriquecimiento semántico | `\paragraph{Enriquecimiento semántico (sub-filtro).}` | `\subsubsection{Enriquecimiento semántico}` + tabla l.897 | act. 04.02; §5.3 l.1599 | firma §A.5 usa nombre corto "Enriquecimiento" | coincide (nombre corto en §A.5 y §3.2.9, aceptable) | 617, 1204, 897, 1502, 1599, 1865, 775 | Bajo |
| Composición de contexto | `\paragraph{Composición de contexto (sub-filtro).}` | `\subsubsection{Composición de contexto}` + tabla l.899 | act. 03.02, 04.03; §5.3 l.1589, 1601 | firma §A.5 "Composición" | coincide (nombre corto, ídem) | 626, 1237, 899, 1488, 1503, 1601, 1866, 776 | Bajo |
| Invocación generativa | `\paragraph{Invocación generativa.}` | `\subsubsection{Invocación generativa}` + tabla l.901 | act. 04.04; §5.3 l.1603 | firma §A.5 "Invocación" | coincide (nombre corto, ídem) | 636, 1274, 901, 1504, 1603, 1867, 777 | Bajo |
| Decodificación | `\paragraph{Decodificación.}` | `\subsubsection{Decodificación}` + tabla l.903 | act. 04.05; §5.3 l.1605 | firma §A.5 "Decodificación" | coincide | 645, 1306, 903, 1505, 1605, 1868 | — |
| Verificación | `\paragraph{Verificación.}` | `\subsubsection{Verificación}` + tabla l.905 | act. 03.03, 04.06–04.07; §5.3 l.1591, 1607–1609 | firma §A.5 "Verificación" | coincide | 656, 1341, 905, 1489, 1506–1507, 1607, 1869 | — |
| Normalización | `\paragraph{Normalización.}` | `\subsubsection{Normalización}` + tabla l.907 | act. 03.04, 04.08; §5.3 l.1593, 1611 | firma §A.5 "Normalización" | coincide | 673, 1379, 907, 1490, 1508, 1611, 1870 | — |
| Responsabilidades por filtro (cap3 ↔ cap4) | Extracción A,F; Enriquecimiento C; Composición A,B; Invocación C; Decodificación B,C; Verificación A,B,D; Normalización A,B,D,E | Idénticas en las fichas (`\item Responsabilidades:`) y en tab:impl-correspondencia | En §5.3 se reparten entre la actividad-sistema y la actividad-sintonía del mismo filtro (p. ej. A de Composición pasa a 03.02): compatible | — | coincide | 611, 622, 632, 641, 650, 662, 679 ↔ 1198, 1231, 1268, 1300, 1335, 1373, 1409 ↔ 895–907 | — |
| Orden de presentación de los filtros | canónico | canónico (subsubsections 1167→1379) | canónico (04.02→04.08) | canónico (§A.5) | coincide | — | — |
| Filtro compuesto "Recuperación aumentada" | Definido y usado: agrupa Enriquecimiento + Composición; el tubo 4→5 es "interno" al compuesto | **Nunca mencionado**: los dos sub-filtros se materializan como etapas independientes de `ETAPAS` (estados `enriquecido`, `compuesto`) sin recuperar la noción de filtro compuesto | Nunca mencionado | l.1727 lo menciona ("tubo interno 4→5 del filtro compuesto Recuperación aumentada") | **discrepa** (concepto del cap. 3 sin eco en caps. 4 y 5) | 582, 589, 594, 615, 692 (cap3); 1129–1144 (cap4); 1727 (anexo) | Bajo |
| Conteo "siete filtros" | "los siete filtros" (l.594, con 2 agrupados en el compuesto) | tabla de 7 filas (895–907) | l.1631: "los siete filtros... cada uno exactamente una vez" | l.1876: "las siete firmas" | coincide | 594, 895–907, 1631, 1876 | — |

---

## Chequeo 2 — Puertos (1–14) y tipos de datos (§3.2.3, §3.2.9, Apéndice, cap. 4, §5.3)

Asignación canónica de §3.2.2: 1 entrada-flujo / 2 `Noticia[]` / 3 entrada `Noticia[]` / 4 `Embedding[]` / 5 entrada `Embedding[]` / 6 `Prompt[]` / 7 entrada `Prompt[]` / 8 `RespuestaIAG[]` / 9 entrada `RespuestaIAG[]` / 10 `Análisis[]` / 11 entrada `Análisis[]` / 12 `Veredicto[]` / 13 entrada `Veredicto[]` / 14 `Resultado`.

| Elemento | Cap. 3 | Cap. 4 | Cap. 5 | Apéndice | Veredicto | Líneas implicadas | Severidad |
|---|---|---|---|---|---|---|---|
| Numeración de puertos 1–14 | §3.2.2 (605–679) y §3.2.3 (692–698) | fichas con comentarios `-- puerto N` (1176–1388) y tabla de tubos (909–927) | §5.3: "puertos 1→2 … 13→14" (1581–1611) | "puerto 14" (1822); tubos 2→3 … 12→13 en cada tipo | coincide | 605–698; 895–927, 1176–1388; 1581–1611; 1704–1822 | — |
| Noticia | Tubo 2→3, card. N, "Título, texto, link, medio, fecha, reglas", resp. E,F | `wsf_noticias_resultados` (preexistente), tubo 2→3, resp. E,F | 04: `Noticia[N]`; §5.3 l.1581 | §A.2: tubo 2→3, campos titulo/copete/texto/link/medio/departamento/fechas/reglas_aplicadas (superset compatible con el resumen de §3.2.9) | coincide | 608–610, 774; 911; 1498, 1581; 1701–1722 | — |
| Embedding | Tubo 4→5 (interno), card. N, resp. C,E | `iag.embedding`, 4→5, C,E | 04.02 `Embedding[N]` | §A.3: tubo 4→5, noticia/vector/fecha_registro | coincide | 620, 775; 897, 912; 1502, 1599; 1724–1739 | — |
| Prompt | Tubo 6→7, card. M, resp. B,E | `iag.prompt`, 6→7, B,E | 04.03 `Prompt[M]` | §A.4: tubo 6→7, texto/parametros/noticias/template/fecha | coincide | 629, 776; 913; 1503, 1601; 1741–1759 | — |
| RespuestaIAG | Tubo 8→9, card. M, resp. C,E | `iag.respuesta`, 8→9, C,E | 04.04 `RespuestaIAG[M]` | §A.5.4: tubo 8→9, prompt/texto/fecha | coincide | 639, 777; 914; 1504, 1603; 1763–1778 | — |
| Análisis — **cardinalidad** | §3.2.3 l.696: "Decodificación una `Análisis` por cada respuesta… **preservan M**"; cadena N→N→M→M→**M**→**M**→1 (l.690); §3.2.9 l.778: card. **M**. Pero §3.2.2 l.652: la validación "opera como compuerta: la respuesta que no conforma **no se persiste**" y l.666: compuerta de Decodificación "**descarta** lo que no conforma" | Ficha Decodificación: `Análisis[M']`, "M' <= M: lo que no conforma no se persiste" (l.1315, 1325); tabla l.915 sin card. | 04.05 y §5.3: `Análisis[M']` (l.1505, 1605) | §A.5.5 l.1783: "`Análisis[M]`"; firma §A.5 l.1868: `Análisis[M]`; l.1874: "los M …" | **discrepa**: cap. 4 y cap. 5 usan M'≤M (con descarte); §3.2.3, §3.2.9 y Apéndice usan M y afirman preservación. Contradicción también **interna al cap. 3** (l.652/666 vs. l.690/696/778). Además el registro maestro del cap. 3 (l.843) usa "los M' veredictos", notación no definida ni en §3.2.3 ni en §A.1 | 652, 666, 690, 696, 778, 843; 1315, 1317, 1325, 1350; 1505, 1605; 1783, 1868, 1874 | **Alto** |
| Veredicto — **cardinalidad** | §3.2.3 l.696: `Veredicto[M]`; §3.2.9 l.779: card. M; l.698: "consolida los M Veredicto" | Ficha Verificación: `Veredicto[M']` (l.1351–1353); Normalización exige `Veredicto[M']` (l.1387, 1406) | 04.06 y §5.3: `Veredicto[M']` (l.1506, 1607) | §A.5.6 l.1801: `Veredicto[M]`; firma l.1869–1870: `Veredicto[M]` | **discrepa** (misma raíz que la fila anterior: si Análisis es M', Veredicto —uno por análisis, compuerta blanda— es M', no M) | 696, 698, 779, 843; 1350–1353, 1387, 1406; 1506, 1607; 1801, 1869–1870 | **Alto** (misma causa; se computa como una única discrepancia estructural en el Resumen) |
| Resultado | Puerto 14, registro único sin cardinalidad, resp. B,D,E | `iag.resultado`, tubo 14, B,D,E | 04.08 "Emite el `Resultado`" | §A.5.7 l.1822: "puerto 14… registro único, tipado sin cardinalidad" | coincide | 676, 698, 780; 907, 917; 1508, 1611; 1819–1835 | — |
| Template | §3.2.9: no circula por los tubos ("---"), resp. A,B; "ocho tipos: siete que circulan y uno que se mantiene en el repositorio" (l.762) | `iag.template`, tubo "---", A,B (l.921) | 03.01 con ref. a `anexo:tipo-template` | §A.5.8 l.1840: "no circula por los tubos… entidad del repositorio" | coincide | 762, 781; 921; 1587; 1837–1855 | — |
| Columna "Resp." de §3.2.9 ↔ tabla cap. 4 (l.911–927) | Noticia E,F; Embedding C,E; Prompt B,E; RespuestaIAG C,E; Análisis B,E; Veredicto D,E; Resultado B,D,E; Template A,B | idéntica | — | criterios §A.1 coherentes (E, C+E, B) | coincide | 774–781 ↔ 911–921; 1696–1698 | — |
| Cadena de cardinalidades §3.2.3 | N→N→M→M→M→M→1 (l.690) | implícitamente N→N→M→M→M'→M'→1 | M' en 04.05–04.08 | M en firmas §A.5 | **discrepa** (derivado de las dos filas anteriores) | 690; 1315–1406; 1505–1508; 1864–1874 | (computado arriba) |

---

## Chequeo 3 — Marcadores `\resp{A}`–`\resp{F}`

Definiciones en §1.3 (Tabla `tab:intro-responsabilidades`, l.212–234): **A** Intervención del experto · **B** Independencia del estudio · **C** Frontera generativa · **D** Control editorial · **E** Procedencia · **F** Infraestructura preexistente. El registro maestro `tab:registro-responsabilidades` (cap. 3, l.820–860) repite las seis definiciones con nombres idénticos. Usos contabilizados: cap. 1: 8; cap. 3: 44; cap. 4: 74; cap. 5: 38; apéndice: 10.

| Elemento | Cap. 3 | Cap. 4 | Cap. 5 | Apéndice | Veredicto | Líneas implicadas | Severidad |
|---|---|---|---|---|---|---|---|
| Definiciones A–F (§1.3 ↔ registro maestro) | Nombres y obligaciones idénticos en ambas tablas | — | — | — | coincide | 212–234 ↔ 820–858 | — |
| Semántica de los usos (misma letra = misma obligación) | usos coherentes (p.ej. A=sintonizadores l.727; C=modelos externos l.622, 641) | coherentes (C=proveedor/adaptadores l.1046, 1105; F=delimitación l.940, 999–1001) | coherentes (D=compuerta blanda/revisión; E=copia de configuración, auditoría) | coherentes (E=contrato mínimo/procedencia l.1696; C=identidad del productor fuera l.1697) | coincide | ver detalle | — |
| Registro maestro [D], columna Procesos | l.844: "03.03 criterio y ejecutor; 04.06–04.07; 04.08; 05.01–05.02; 07.01" — **omite 03.04** | — | La tabla §5.3 asigna `\resp{D}` a 03.04 (Sintonía de la Normalización: política sobre observados), coherente con l.679 (Normalización: D) | — | **discrepa**: el registro que pretende consolidar "capítulo por capítulo" no lista 03.04 entre las realizaciones procesales de D | 844 ↔ 1593, 677–679 | **Medio** |
| Actividad 01.01 (Formulación de la pregunta) | registro maestro [B] l.830: no incluye 01.01 | — | Narrativa l.1465: "la responsabilidad `\resp{B}` explica por qué: nada de lo que aquí se decide se programa"; pero la tabla §5.3 l.1571 asigna a 01.01 sólo `\resp{A}` | — | **discrepa** (menor): narrativa y tabla/registro no coinciden en la letra atribuida a 01.01; la semántica de B usada en l.1465 es correcta, lo que falta es reflejarla en la tabla y el registro (o ajustar la narrativa) | 1465 ↔ 1571, 823, 830 | Bajo |
| Reparto A entre filtro y sintonía | Verificación=A,B,D (l.662); Composición=A,B (l.632) | fichas idénticas | En §5.3 la A de cada filtro queda en la actividad de sintonía (03.02, 03.03) y la actividad-sistema conserva B/D: reparto explícito en l.1631 | — | coincide (diseño declarado, no contradicción) | 632, 662 ↔ 1589, 1591, 1601, 1607, 1631 | — |
| Comentario obsoleto sobre el registro | l.793–795 (TODO): "las columnas de los Capítulos 4 y 6 se completan cuando esos capítulos existan", pero la columna Cap. 4 ya está completa | — | — | — | **discrepa** (comentario de mantenimiento, no visible en el PDF) | 793–795 ↔ 822, 829, 836, 843, 850, 857 | Bajo |

---

## Chequeo 4 — Referencias cruzadas

Extracción mecánica: 98 `\label{}`, 68 claves distintas referenciadas vía `\ref/\eqref/\autoref/\cref/\pageref`.

| Elemento | Resultado | Veredicto | Líneas implicadas | Severidad |
|---|---|---|---|---|
| Referencias rotas (`\ref` sin `\label`) | **0** | coincide | — | — |
| Labels duplicados | **0** | coincide | — | — |
| Labels nunca referenciados | **30** (p.ej. `anexo:tipo-analisis` 1781, `anexo:tipo-resultado` 1820, `cap:conclusiones` 1660, `sec:arq-car-analisis` 747, todas las `sec:ej-*` del cap. 6 vacío, `sec:proc-*`, `sec:rsl-*`, `sec:impl-mat-extraccion/enriquecimiento/invocacion`, `sec:impl-pre-noticia/sustrato`) | No es error de compilación; es deuda: secciones definidas que ningún texto cita (varias se citarán cuando se redacten caps. 6–7) | 747, 945, 967, 1160–1275, 1460–1536, 1634, 1642–1660, 270–500, 1781, 1820 | Bajo |
| Labels de caps. 6 y 7 (`sec:ej-*`, `cap:conclusiones`) | existen pero los capítulos están vacíos; el registro maestro los cita como "(por completar)" | coherente con el estado de borrador | 824–859, 1638–1682 | Bajo (informativo) |

---

## Chequeo 5 — Tabla de correspondencia §5.3 (`tab:proc-correspondencia`, l.1549–1628)

| Elemento | Cap. 3 | Cap. 4 | Cap. 5 | Apéndice | Veredicto | Líneas implicadas | Severidad |
|---|---|---|---|---|---|---|---|
| Los 7 procesos (01–07) presentes como bloques de la tabla | — | — | bloques l.1569, 1577, 1585, 1595, 1613, 1619, 1625 | — | coincide | 1569–1627 | — |
| Biyección filtros ↔ actividades: cada filtro exactamente una vez | 7 filtros (§3.2.2) | cada uno con realización nombrada (col. "Realización": `wsfnoticias`, `iag.filtro.*`, 7/7 cubiertos) | Extracción=02.02; Enriquecimiento=04.02; Composición=04.03; Invocación=04.04; Decodificación=04.05; Verificación=04.06 (+04.07 contraparte humana); Normalización=04.08 — declarado y verificado en l.1631 | — | coincide | 1581, 1599–1611, 1631 | — |
| Columna "Realización (Cap. 4)" completa | — | todas las filas remiten a secciones/modelos del cap. 4 que existen (`sec:impl-pre-extraccion`, `sec:impl-mat-estudio`, `sec:impl-mat-composicion`, `sec:impl-mat-verificacion`, `iag.filtro.*`, `iag.template`, `iag.resultado.fila`); las dos filas sin correlato (01.01, 06.01) lo declaran explícitamente | — | — | coincide | 1571–1627 | — |
| Puertos citados en la tabla vs. §3.2.2 | 1→2, 3→4, 5→6, 7→8, 9→10, 11→12, 13→14 | — | idénticos en l.1581–1611 | — | coincide | 605–679 ↔ 1581–1611 | — |
| Tipos citados en la tabla vs. §3.2.9/Apéndice | `Noticia[N]`, `Embedding[N]`, `Prompt[M]`, `RespuestaIAG[M]`, `Análisis[M]`, `Veredicto[M]`, `Resultado` | `Análisis[M']`, `Veredicto[M']` | la tabla usa `Análisis[M']`, `Veredicto[M']` (l.1605, 1607) | `[M]` | **discrepa** (derivado del Chequeo 2: la tabla §5.3 está alineada con cap. 4, no con cap. 3/Apéndice) | 778–779 ↔ 1605–1607 ↔ 1783, 1801 | (computado en Chequeo 2) |
| Enumeración de actividades de l.1631 | — | — | "los cuatro sintonizadores aparecen como actividades propias: 02.01 y 02.03 para Extracción; 03.02, 03.03 y 03.04 para los tres restantes" — **omite 03.01**, que la propia tabla (l.1587) describe como "primera superficie del sintonizador de Composición" (cap. 3 l.729 coincide: el sintonizador de Composición tiene dos superficies) | — | **discrepa** (enumeración incompleta en el texto de cierre) | 1631 ↔ 1587, 729 | Bajo |
| Conteo de actividades en la síntesis §5.4 | — | — | l.1636: "siete procesos y **veintidós** actividades"; el conteo real (itemize de §5.2 y filas de §5.3) es **23**: 01:3 + 02:3 + 03:4 + 04:8 + 05:2 + 06:2 + 07:1 | — | **discrepa** (error numérico en prosa) | 1636 ↔ 1459–1541, 1571–1627 | **Medio** |

---

## Resumen

### Discrepancias por severidad

| Severidad | Cantidad | Detalle |
|---|---|---|
| Crítico | 0 | — |
| Alto | 1 | Cardinalidad M vs. M' de `Análisis`/`Veredicto` (una única falla estructural que abarca §3.2.3, §3.2.9, registro maestro, Apéndice §A.5.5–A.5.6 y firmas §A.5 vs. cap. 4, cap. 5 y tabla §5.3; incluye la contradicción interna del cap. 3 entre l.652/666 y l.690/696/778, y el uso de M' sin definición en l.843) |
| Medio | 2 | (1) "veintidós actividades" vs. 23 reales (l.1636); (2) registro maestro [D] omite 03.04 (l.844 vs. l.1593) |
| Bajo | 6 | (1) "Recuperación aumentada" ausente en caps. 4–5; (2) narrativa de 01.01 invoca B pero la tabla/registro sólo le asignan A (l.1465 vs. 1571/830); (3) enumeración de sintonizadores en l.1631 omite 03.01; (4) nombres cortos de filtros en §A.5/§3.2.9 vs. canónicos; (5) 30 labels nunca referenciados; (6) comentario TODO obsoleto l.793–795 |
| **Total** | **9** | 0 críticos · 1 alto · 2 medios · 6 bajos |

### Chequeos sin hallazgos
- **Chequeo 4 (referencias cruzadas):** 0 refs rotas, 0 labels duplicados sobre 98 labels y 68 claves referenciadas.
- **Chequeo 1 (nombres y responsabilidades de filtros):** los 7 nombres canónicos y sus conjuntos de `\resp` coinciden exactamente entre §3.2.2 y las fichas del cap. 4; el cap. 5 los reparte coherentemente entre actividades.
- **Chequeo 2 (puertos y tipos, salvo cardinalidad M/M'):** numeración 1–14 idéntica en las cuatro vistas; los 8 tipos con productor, tubo y contenido compatibles entre §3.2.9, cap. 4 y Apéndice.
- **Chequeo 5 (biyección §5.3):** verificada — cada filtro aparece exactamente una vez y toda actividad del sistema tiene filtro.

### Top-10 de problemas (ordenados por gravedad)

1. **[Alto] Cardinalidad de `Análisis` y `Veredicto`: M vs. M'.** §3.2.3 (l.690, 696) afirma que Decodificación "preserva M" y da la cadena N→N→M→M→M→M→1; §3.2.9 (l.778–779) tabla card. M; el Apéndice (l.1783, 1801, 1864–1874) firma todo con M. Pero §3.2.2 (l.652, 666) dice que la compuerta de Decodificación **descarta** lo que no conforma, y cap. 4 (l.1315, 1325: "M' <= M: lo que no conforma no se persiste") y cap. 5 (l.1505–1506, 1605, 1607) usan `Análisis[M']`/`Veredicto[M']`. **Fix sugerido:** unificar a M'≤M desde Decodificación (corregir l.690, 696, 778–779, 1783, 1801, 1868–1870, 1874) y definir M' en §3.2.3 y en §A.1.
2. **[Alto, misma raíz] El registro maestro del cap. 3 (l.843) ya usa "los M' veredictos"** — notación que el propio capítulo no define ni admite: evidencia de que la decisión editorial fue M' y las secciones §3.2.3/§3.2.9/Apéndice quedaron desactualizadas.
3. **[Medio] l.1636: "veintidós actividades"** — el mapa documenta y tabula **23** (3+3+4+8+2+2+1). Corregir el numeral (y verificar el PNG `Diagrama-Procesos.png`, cuyo contenido no se pudo inspeccionar desde el .tex).
4. **[Medio] Registro maestro [D] (l.844) omite la actividad 03.04**, a la que §5.3 (l.1593) y §3.2.2 (l.679, Normalización=D) sí asignan control editorial. Agregar "03.04 política sobre observados" a la columna Procesos de D.
5. **[Bajo] El filtro compuesto "Recuperación aumentada"** (l.589, 594, 615, 692; citado también en l.1727 del Apéndice) no vuelve a mencionarse en caps. 4–5: la materialización lo disuelve en dos etapas sin decirlo. Conviene una frase en §4.3.2 o en la tabla l.895–907 que explicite que el compuesto se realiza como dos etapas independientes.
6. **[Bajo] Actividad 01.01:** la narrativa (l.1465) la justifica con `\resp{B}`, pero la tabla §5.3 (l.1571) le asigna sólo `\resp{A}` y el registro [B] (l.830) no la lista. Unificar (agregar B en l.1571 y en el registro, o reformular l.1465).
7. **[Bajo] l.1631:** la enumeración "los cuatro sintonizadores aparecen como actividades propias" omite **03.01**, que la propia tabla (l.1587) y §3.2.6 (l.729) describen como primera superficie del sintonizador de Composición.
8. **[Bajo] Nombres cortos** ("Enriquecimiento", "Invocación", "Composición", "Decodificación") en §3.2.9 (l.775–778) y firmas §A.5 (l.1865–1868) vs. nombres canónicos completos en el resto: inocuo pero conviene una nota de convención en §A.1.
9. **[Bajo] 30 `\label` sin ninguna referencia** (lista en Chequeo 4): en su mayoría se resolverán al redactar caps. 6–7 y la síntesis del cap. 3 (l.793 TODO), pero `sec:arq-car-analisis` (l.747) y `anexo:tipo-analisis`/`anexo:tipo-resultado` merecen citarse ya.
10. **[Bajo] Comentario TODO obsoleto (l.793–795):** anuncia que "las columnas de los Capítulos 4 y 6 se completan cuando esos capítulos existan"; la de Cap. 4 ya está completa. Actualizar el comentario para no inducir a error en futuras revisiones.

**Estado de caps. 6 y 7:** vacíos, como se esperaba; el registro maestro los marca "(por completar)" de forma coherente — no se computa como discrepancia.

---
*Generado por revisión automática (REV-002). No se modificó ningún archivo del repo salvo este informe.*
