---
name: stm-odsa
description: >-
  Runs ODSA claims audit of motor-oil packaging (front/back/site triangulation)
  for MGIMO STM stage 4. Builds Evidence Ledger, Findings, Contradiction Register,
  and canonical 18-row matrix row. Use when the user says ODSA, skill odsa, claims
  audit, API OEM этикетка, Evidence Ledger, cross-face consistency. NOT for
  metaphorical PGMM (use stm-pgmm) or format delta (use stm-pgmm-delta).
disable-model-invocation: true
---

# ODSA — аудит claims на упаковке (этап 4)

## Preconditions

- Методология: **ODSA Audit Packet v1.6.7**.
- `Cursor/AGENTS.md`, `Cursor/wiki/index.md`, `Cursor/wiki/04_источники_и_URL.md`.
- Связанный PGMM (если есть): ссылка в шапке отчёта, **не дублировать** метафорический слой.
- Стиль: `neuromarketing-system-instructions` (POV-маркировка).

## Вход

| Артефакт | Обязательность |
|----------|----------------|
| Фото **front** | ✅ |
| Фото **back** | ✅ для API/OEM/маркировки РФ |
| Сайт оператора / TDS | 🟡 triangulation |
| PGMM wiki | 🟡 контекст (EVID as Context) |
| Operator attestation | 🟡 wrap stability, channel |

## Workflow (реvisions)

```
- [ ] 0. CASE_ID, SKU, формат, дата
- [ ] 1. Autostart: CMC v0, первичный Evidence Ledger (G01…)
- [ ] 2. Rev.1: Findings F-*, Contradiction Register CR-*
- [ ] 3. Triangulation: site (verified URL из wiki/04)
- [ ] 4. Rev.N locked: severity rollup, DC-EP, gaps closed
- [ ] 5. POV-маркировка (Integrity / Coherence / Dynamics / Relational)
- [ ] 6. Canonical matrix row (18 строк) — см. reference.md
- [ ] 7. Issues for discussion
- [ ] 8. OUTPUT_WIKI + log.md + index.md
```

### Именование

```
Cursor/wiki/{NN}_ODSA_{Brand}_{Line}_{SAE}_{format}.md
```

Пример: `16_ODSA_LUKOIL_LUXE_5W-40_4L.md`.

### Структура отчёта

1. Executive summary + severity rollup
2. Evidence Ledger (EVID-*, Source class, Reliability, Status)
3. Conflict notes + Product evolution log (если SL→SN и т.п.)
4. Findings Catalogue (F-*: Observation, Evidence, Severity, Recommendations)
5. Contradiction Register (CR-*: Open/Closed)
6. POV-маркировка
7. **Строка для сводной матрицы** (18 параметров)
8. Issues for discussion

Детали полей — [reference.md](reference.md).

## Severity scale

| Level | Пример |
|-------|--------|
| Blocker | Противоречие API front vs back (same SKU) |
| Major | OEM listed but unreadable; digital superset vs pack |
| Moderate | ACEA/API site-only; notation variants |
| Minor | STO back-only; naming variants |
| Positive | Cross-face coherent; anti-fraud triangulated |

## Hard constraints

- **Не выдумывать** API/OEM — только artifact + «н/д» / «нечитаемо».
- URL только из `wiki/04_источники_и_URL.md`; новые — верифицировать, добавить в 04.
- **1 format = 1 row** в матрице; 4L ≠ 1L.
- Не смешивать DR-A доли и ODSA claims.
- PGMM stale vs ODSA current → пометить EVID **Stale**, рекомендовать refresh PGMM.

## Wiki ingest

1. `Cursor/wiki/log.md`
2. `Cursor/wiki/index.md`
3. Обновить `03_…/матрица_PGMM_ODSA_*.md` при новой строке

## Companion skills

| Skill | Когда |
|-------|-------|
| `stm-pgmm` | Метафорический слой до/параллельно ODSA |
| `stm-pgmm-delta` | ODSA для delta-формата — отдельный прогон |

## Эталоны

- `Cursor/wiki/16_ODSA_LUKOIL_LUXE_5W-40_4L.md`
- `Cursor/wiki/17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md`
- `Cursor/wiki/18_ODSA_mobil_super_3000_x1_5w_40_4L.md`
- Schema: `03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md`
