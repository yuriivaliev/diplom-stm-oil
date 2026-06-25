---
name: stm-pgmm-delta
description: >-
  Runs PGMM delta analysis comparing two packaging formats of the same SKU
  (e.g. 1L vs 4L, 5L vs 1L) for MGIMO STM stage 4. Requires an existing full
  PGMM wiki report as base. Use when the user says PGMM delta, skill pgmm-delta,
  delta упаковки, 1L vs 4L, сравнение фасовок, or format delta. NOT for new
  competitors (use stm-pgmm) or claims audit (use stm-odsa).
disable-model-invocation: true
---

# PGMM Delta — сравнение форматов упаковки

## Preconditions

- **Full PGMM базового формата** уже в wiki (`BASE_WIKI`).
- Прочитать базовый отчёт целиком перед delta.
- `Cursor/AGENTS.md`, `Cursor/wiki/index.md`.
- Стиль: `neuromarketing-system-instructions`.

## Когда использовать / не использовать

| Ситуация | Действие |
|----------|----------|
| Тот же SKU, другой объём (1L / 4L / 5L) | ✅ Delta |
| Тот же бренд, **другая вязкость** | ❌ Full `stm-pgmm` |
| Новый конкурент | ❌ Full `stm-pgmm` |
| Только другой ракурс того же формата | ❌ Отдельный отчёт не нужен |

## Вход (заполнить)

| Поле | Пример |
|------|--------|
| BRAND | Mobil |
| LINE | Super 3000 x1 |
| SAE | 5W-40 |
| FORMAT_BASE | 4L |
| FORMAT_DELTA | 1L |
| BASE_WIKI | `Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md` |
| OUTPUT_WIKI | `Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md` |
| CASE_ID | `COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA` |

**Изображения:** фронт `FORMAT_DELTA` — обязательно; бок — если морфология канистры отличается.

## Workflow

```
- [ ] 1. CASE_min (CASE_TYPE: packaging_visual_metaphor_delta; BASE_CASE_REF)
- [ ] 2. Delta по блокам: C → K → S → M → MAP → EVAL
- [ ] 3. Наследовать константы: M_SYSTEM, DOMAIN (ссылка на базу)
- [ ] 4. M_CONSTRUCTION: ID из базы + variant-by-format
- [ ] 5. Только новые/изменённые M_OCCURRENCE (_min/_full)
- [ ] 6. Выводы для СТМ: где дизайн «ломается» на delta-формате
- [ ] 7. Таблица FORMAT_BASE vs FORMAT_DELTA (10–15 строк)
- [ ] 8. System States + Issues for discussion
- [ ] 9. Сохранить OUTPUT_WIKI; log.md + index.md
```

**Не дублировать ~90%** базового отчёта — только изменения + перекрёстные ссылки.

### Блоки delta (что сравнивать)

- **C:** геометрия, ручка, материал, пропорции, DoF
- **K:** макет, плотность, negative space, читаемость SAE/объёма
- **S:** сохранилось / деградировало / усилилось
- **M:** полка долива, e-commerce thumbnail (~120 px)
- **MAP:** мэппинги при масштабировании
- **EVAL:** comprehensibility, cognitive load, robustness

### Именование

```
Cursor/wiki/{NN}_PGMM_{brand}_{line}_{sae}_{format}_delta.md
```

Суффикс `_delta` обязателен.

## Чеклист самопроверки

| # | Проверка |
|---|----------|
| BP1 | Базовый full не продублирован |
| BP2 | M_SYSTEM = «константа» или обоснованное изменение |
| BP3 | Таблица base vs delta (10–15 строк) |
| BP4 | Новые MOCC в _min/_full |
| BP5 | System States проставлены |
| BP6 | log.md обновлён |
| BP7 | Нет смешения DR-A/B и PGMM |

## Hard constraints

- **1 format = 1 row** в матрице.
- Не выдумывать claims — только видимое на delta-формате **+ канон SKU** при triangulation.
- **Фото vs канон:** при конфликте API/ACEA между форматами или с сайтом — **наивысший допуск** (API **SP > SN**…); устаревшее фото не понижает канон. Delta описывает **упаковку/макет**; spec-generation в матрице — по сайту оператора.

## Companion skills

| Skill | Когда |
|-------|-------|
| `stm-pgmm` | Если нет базового full-отчёта |
| `stm-odsa` | Claims audit по delta-формату (отдельный прогон) |

## Эталоны

- `Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md`
- `Cursor/wiki/14_PGMM_LUKOIL_LUXE_5W-40_1L_delta.md`
- `Cursor/wiki/15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md`
- Шаблон промпта: `03_PGMM_ODSA_упаковка_конкуренты/PGMM_delta_промпт_шаблон.md`
