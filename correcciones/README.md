# Carpeta de correcciones

Registro histórico de las revisiones de la tesina de Lucio Bassani.

## Convención de nombres

Cada informe se guarda con el siguiente formato:

```
<codigo>_<nombre-descriptivo>.md
```

- **Código:** `REV-NNN` (correlativo). Ej: `REV-001`, `REV-002`.
- **Nombre:** descripción corta en snake_case.

## Registro

| Código | Nombre | Fecha | Alcance |
|---|---|---|---|
| REV-001 | revisión_integral_estructura_cap2_cap3 | 9-07-2026 | Índice, planteo, caps. 2 y 3 |
| DECISIONES-REV-001 | — | 9-07-2026 | Seguimiento de las 5 decisiones abiertas del REV-001 |

## Convenciones dentro de cada informe

Cada informe debe contener al menos:

1. **Bloque de metadatos** (tabla inicial): código, nombre, fecha, archivos revisados, versión del commit.
2. **Escala de severidad**: Crítico / Alto / Medio / Bajo, con definición.
3. **Secciones temáticas** según el alcance.
4. **Tabla de propuestas de mejora** numerada y con código único (por ejemplo `MT-1`, `RSL-2`, `EA-3`) para poder referenciarlas en conversaciones posteriores.
5. **Resumen ejecutivo** con priorización de pendientes.
6. **Sección final** indicando qué se espera cubrir en la próxima revisión.

## Flujo de trabajo sugerido

1. El director o el tesista piden una revisión indicando el alcance.
2. El agente produce el informe y lo guarda con un nuevo código `REV-NNN`.
3. Se discute la revisión, se priorizan los pendientes.
4. El tesista corrige. Se vuelve a revisar con un nuevo informe (`REV-NNN+1`) cuando haya suficiente progreso.
