---
name: stm-pgmm-odsa
description: >-
  Router for stage-4 packaging analysis. Delegates to stm-pgmm (full PGMM),
  stm-pgmm-delta (format comparison), or stm-odsa (claims audit). Use only when
  the user says stm-pgmm-odsa without specifying which pass.
disable-model-invocation: true
---

# PGMM / ODSA — роутер (этап 4)

Skill **разделён** на три отдельных. Выбери нужный:

| Задача | Skill | Вызов |
|--------|-------|-------|
| Новый конкурент / SKU, full PGMM | [stm-pgmm](../stm-pgmm/SKILL.md) | `используй skill stm-pgmm` |
| 1L vs 4L / другой объём | [stm-pgmm-delta](../stm-pgmm-delta/SKILL.md) | `используй skill stm-pgmm-delta` |
| Аудит claims (API/OEM) | [stm-odsa](../stm-odsa/SKILL.md) | `используй skill stm-odsa` |

**Рекомендуемая цепочка:** `stm-pgmm` → `stm-pgmm-delta` (если есть) → `stm-odsa`.

Сводка этапа 4: `Cursor/wiki/08_PGMM_упаковка.md`.
