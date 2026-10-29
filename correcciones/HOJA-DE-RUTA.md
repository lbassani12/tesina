# HOJA-DE-RUTA — Finalización de la tesina de Lucio Bassani

| Campo | Valor |
|---|---|
| **Código** | RUTA-001 |
| **Fecha** | 29 de octubre de 2026 |
| **Autor** | Hermes (agente) — validada por el director Alejandro Sartorio |
| **Alcance** | Plan completo hasta la defensa de la tesina |
| **Repo tesina** | github.com/lbassani12/tesina (clon local: `/Users/asartorio/tesina`) |
| **Defensa objetivo** | Primeros días de marzo de 2027 (~18 semanas desde esta fecha) |

---

## 1. Estado actual (diagnóstico 29-10-2026, commit `adfc221`)

| Capítulo | Estado |
|---|---|
| 1 Introducción (incl. §1.3 responsabilidades transversales [A]-[F]) | ✅ Completo |
| 2 Marco teórico + RSL | ✅ Completo |
| 3 Arquitectura (incl. §3.2.9 contratos de datos) | ✅ ~95% (falta síntesis narrativa: TODO L793) |
| 4 Implementación del framework en Odoo | ✅ Completo (fichas de los 7 filtros, frontera wsfnoticias) |
| 5 Mapa de procesos (BPMN + correspondencia biyectiva) | ✅ Completo |
| **6 Ejemplo de aplicación** | 🔴 **Vacío — solo títulos de sección** |
| **7 Conclusiones y Trabajo a Futuro** | 🔴 **Vacío** |
| Apéndice — Tipos de datos del pipeline | ✅ Completo (grafo de procedencia) |

- Objetivos OE1–OE4 de DECISIONES-REV-001: **implementados**.
- Paper CONAIISI 2026: **presentado y aprobado** (pista cerrada).
- La matriz maestra de responsabilidades [A]-[F] tiene 6 celdas "(por completar)" que dependen del cap. 6.
- **Camino crítico único: cap. 6 (validación empírica, OE4) → cap. 7 (conclusiones) → matriz maestra.**

## 2. Fases

| Fase | Contenido | Responsable | Duración est. | Estado |
|---|---|---|---|---|
| **0** | Auditoría REV-002 del estado actual (claims, bibliografía, consistencia, compilación) | Hermes | 2-3 días | ✅ Completa — informe emitido y validado por el director (29-10-2026) |
| **1** | Protocolo del experimento del cap. 6 (caso, corpus, template, modelo, evidencia a capturar, criterios) | Hermes propone, Alejandro valida, Lucio opina | 1 semana | 🔶 En curso — `PROTOCOLO-CAP6.md` borrado; pendientes DEC-1..DEC-6 |
| **2** | Ejecución empírica del protocolo ‖ limpieza de deuda técnica vía PRs (TODOs, bibliografía, cardinalidades M/M') | Lucio ‖ Hermes | 2 semanas | Pendiente |
| **3** | Escritura del cap. 6 (Lucio escribe, Hermes guía y revisa con auditoría de claims) + celdas de la matriz maestra | Lucio + Hermes | 2 semanas | Pendiente |
| **4** | Cap. 7 Conclusiones (respuesta a OE1-OE4 con evidencia, limitaciones, amenazas a la validez, trabajo futuro) | Lucio + Hermes | 1 semana | Pendiente |
| **5** | Revisión final 5 pasadas + tribunal simulado + materiales de defensa | Hermes + Alejandro + Lucio | 1-2 semanas | Pendiente |

**Buffer:** ~8 semanas de holgura hasta marzo 2027 → permite dos ciclos de revisión completos y un experimento más robusto (segundo template o caso comparativo) si el director lo desea.

## 3. Roles

- **Lucio (tesista):** autor. Ejecuta el experimento real, escribe caps. 6 y 7, decide sobre su texto.
- **Alejandro (director):** decisiones académicas de fondo, validación de decisiones marcadas, merge de PRs, influencia la orientación vía reportes diarios.
- **Hermes (agente):** auditoría, propuestas técnicas, guía de escritura, producción LaTeX/editorial, registro de decisiones y reportes. Nunca reemplaza la autoría.

## 4. Convenciones de trabajo en el repo

- `main` = versión canónica (mergean Lucio/Alejandro).
- Ramas de revisión: `revNNN/NN-tema` con PRs atómicos por tema.
- Informes y gestión: `correcciones/` (REV-NNN, DECISIONES-REV-NNN, RUTA-NNN, ORIENTACION-LUCIO).
- **Bloqueo activo (29-10-2026):** el usuario GitHub `wsf` no tiene permiso de push en `lbassani12/tesina` (403). **Acción requerida:** que Lucio invite a `wsf` como colaborador (Settings → Collaborators and teams). Mientras tanto, los cambios de Hermes quedan en ramas locales sin poder abrir PRs.

## 5. Hallazgos REV-002 (anexos completos, 29-10-2026)

**Bibliografía** (`correcciones/REV-002-anexo-bibliografico-borrador.md`): 75 entradas — 65 OK verificadas, 3 sospechosas, 2 no verificables, 5 huérfanas. Graves:
1. `bertagnolio2023` sigue desajustada (paper de turbinas eólicas citado para LLMs) — señalada en REV-001, sin corregir.
2. `somasundharam:2025`: el documento real es de **Nils Skoog** (Uppsala) y el stack declarado en la tesina no coincide — afecta 6 citas y la tabla RSL.
3. `behbahanian`: no verificable, año s.f., sustenta claims en 9 citas.
4. `price:1997`: metadatos fabricados (huérfana — eliminar).
5. TODO activo L261-266: afirmación sin cita.

**Consistencia** (`correcciones/REV-002-anexo-consistencia-borrador.md`): 9 discrepancias — 0 críticas, 1 alta (cardinalidad `Análisis`/`Veredicto`: M en §3.2.3/§3.2.9/Apéndice vs M' en caps. 4-5; unificar a M'≤M desde Decodificación), 2 medias ("veintidós actividades" son 23; matriz [D] omite actividad 03.04), 6 bajas. Referencias cruzadas: 0 rotas. Biyección §5.3: verificada.

**Producción:** compila limpio con tectonic (solo warnings hyperref de destinos duplicados, severidad Baja).

**TODOs activos en main.tex:** L261-266 (cita), L793 (síntesis cap. 3), L799 (formato columna matriz), L1303 (mover mediciones Estudios 32/59 a tabla §4.3).

## 6. Decisiones pendientes del director

1. **Estrategia cap. 6:** ✅ **Decidida (29-10-2026):** (a) corrida nueva controlada por protocolo; Estudios 32/59 como referencia comparativa. Ver `PROTOCOLO-CAP6.md`.
2. **Permiso de push:** invitar a `wsf` como colaborador de `lbassani12/tesina` (o definir workflow fork+PR).
3. **Alcance del experimento:** un caso simple vs dos templates/casos comparativos (aprovechando el buffer).

## 7. Riesgos

| Riesgo | Mitigación |
|---|---|
| Acceso al entorno CAETI/CIM y presupuesto del proveedor generativo | Acotar corpus en el protocolo; medir costo por corrida antes de escalar |
| Dedicación real de Lucio en semanas de cursado/exámenes | Hoja de ruta con holgura; revisiones semanales de avance |
| Referencia `behbahanian` imposible de conseguir | Decidir tempranamente: sustituirla o reescribir los claims que sostiene (9 citas) |
| Permiso de push no resuelto | Cambios en ramas locales + entrega por Telegram hasta que se resuelva |
