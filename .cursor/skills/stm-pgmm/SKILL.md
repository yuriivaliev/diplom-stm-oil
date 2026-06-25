---
name: stm-pgmm
description: >-
  Runs full PGMM (_full) analysis of competitor motor-oil packaging labels for
  MGIMO STM thesis stage 4. Extracts M_OCCURRENCE, M_CONSTRUCTION, M_SYSTEM,
  then DOMAIN, MAP, S, C, M, K, EVAL; saves wiki report. Use when the user says
  PGMM, skill pgmm, skill-PGMM, full PGMM, анализ этикетки, M_OCCURRENCE,
  новый конкурент, or attaches packaging image for first-time SKU analysis.
  NOT for format delta (use stm-pgmm-delta) or claims audit (use stm-odsa).
disable-model-invocation: true
---

# PGMM Full — упаковка конкурента (этап 4)

## Preconditions

- **2a + 3a** закрыты → `Cursor/wiki/08_декомпозиция_после_DR.md`.
- Прочитать: `Cursor/AGENTS.md`, `Cursor/wiki/index.md`, `Cursor/wiki/08_PGMM_упаковка.md`.
- Методология: `03_PGMM_ODSA_упаковка_конкуренты/PGMM.md` (или `PGMM.pdf`).
- Стиль: skill `neuromarketing-system-instructions` (System States, issues for discussion).
- **Не смешивать** PGMM с DR-A (доли) / DR-B (SAE) в одной таблице.

## Workflow

```
- [ ] 0. CASE_min: CASE_ID, бренд, линейка, SAE, объём, ракурс, изображение
- [ ] 1. M_OCCURRENCE — manifest (атомарно, _full)
- [ ] 2. M_OCCURRENCE — lacunar / latent / negative space
- [ ] 3. M_CONSTRUCTION — manifest + ревизия
- [ ] 4. M_CONSTRUCTION — lacunar / latent / negative space
- [ ] 5. M_SYSTEM — manifest
- [ ] 6. M_SYSTEM — lacunar / latent / negative space
- [ ] 7. DOMAIN (A → B)
- [ ] 8. MAP (MAP1–MAP10)
- [ ] 9. S (S1–S11)
- [ ] 10. C (C1–C9)
- [ ] 11. M (M1–M11)
- [ ] 12. K (K1–K10)
- [ ] 13. EVAL + EVAL_AGG + STM blueprint
- [ ] 14. System States (4 категории)
- [ ] 15. Issues for discussion
- [ ] 16. Markdown → Cursor/wiki/
- [ ] 17. log.md + index.md (+ 08_PGMM при новом конкуренте)
```

**Порядок обязателен:** M-уровни → DOMAIN → S/C/M/K → MAP → EVAL.

### Глубина

- По умолчанию **_full** (как wiki/10–12).
- **_min** — только по явной просьбе пользователя.
- Пошагово — один блок за сообщение, если пользователь ведёт диалог.

### Вход

- Фронт этикетки — **обязательно**; back/бок — по необходимости.
- Метаданные: бренд, линейка, SAE, объём, сегмент.

### Именование

```
Cursor/wiki/{NN}_PGMM_{brand}_{line}_{sae}.md
```

`{NN}` — следующий свободный номер в `wiki/index.md`. snake_case, латиница.

### Структура отчёта

1. Метаданные (CASE_ID, объект, дата)
2. System States
3. M_OCCURRENCE
4. M_CONSTRUCTION
5. M_SYSTEM
6. DOMAIN → MAP → S → C → M → K
7. EVAL + STM blueprint (антидот для СТМ)
8. Issues for discussion

Поля и чеклисты — [reference.md](reference.md).

### Wiki ingest

1. `Cursor/wiki/log.md`
2. `Cursor/wiki/index.md` (новая страница)
3. `Cursor/wiki/08_PGMM_упаковка.md` (новый конкурент / SAE-ветка)

## Hard constraints

- Не интерполировать доли брендов 2024–2026 из DR-A.
- Не выдумывать API/OEM — только видимое + «н/д» / «нечитаемо».
- **Фото vs канон:** при конфликте поколений — **канон SKU = наивысший допуск** (API **SP > SN > SL**…); triangulation с сайта оператора перекрывает legacy label. В отчёте: artifact (фото) vs canonical (матрица) **раздельно**.
- **1 format = 1 row** в матрице; не усреднять форматы.
- URL — только из `wiki/04_источники_и_URL.md`.

## Next steps (другие skills)

| После full PGMM | Skill |
|-----------------|-------|
| Другой объём (1L vs 4L) | `stm-pgmm-delta` |
| Аудит claims | `stm-odsa` |

## Эталоны

- `Cursor/wiki/10_PGMM_LUKOIL_LUXE_5W-40.md`
- `Cursor/wiki/11_PGMM_Gazpromneft_Premium_N_5W-40.md`
- `Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md`
