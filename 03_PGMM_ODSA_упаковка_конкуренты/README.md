# PGMM / ODSA — упаковка конкурентов

Папка этапа **4** диплома: визуально-метафорический анализ упаковки моторных масел (PGMM) для сравнительной матрицы и ODSA.

---

## Быстрый старт

| Задача | Файл |
|--------|------|
| **Delta-анализ** (1L vs 4L, тот же SKU) | [`PGMM_delta_промпт_шаблон.md`](PGMM_delta_промпт_шаблон.md) |
| Методология PGMM (первичник) | `PGMM.md`, `PGMM.txt` |
| Готовые отчёты | `Cursor/wiki/10_PGMM_*.md`, `11_…`, `12_…` |
| Правила агента | `Cursor/AGENTS.md` |

---

## Workflow

```
Full PGMM (новый конкурент)
  → новый чат + изображение + методология PGMM
  → Cursor/wiki/NN_PGMM_{brand}_{sae}.md
  → обновить Cursor/wiki/log.md

Delta PGMM (другой формат того же SKU)
  → PGMM_delta_промпт_шаблон.md (заполнить поля)
  → новый чат Agent mode + изображение
  → Cursor/wiki/NN_PGMM_{brand}_{sae}_{format}_delta.md
  → обновить log.md
```

**Oracle / GPToracle** для PGMM не используется (в отличие от DR-A/B в `00_таксономии_и_промпты_аналитика/`).

---

## Скрипты

| Скрипт | Назначение |
|--------|------------|
| `scripts/txt_to_pgmm_md.py` | Конвертация PGMM.txt → PGMM.md |

---

## Wiki-отчёты (канон)

| ID | Бренд | Формат |
|----|-------|--------|
| 10 | LUKOIL LUXE 5W-40 | full |
| 11 | Gazpromneft Premium N 5W-40 | full |
| 12 | Mobil Super 3000 x1 5W-40 | full (4L) |
| 13 | Mobil Super 3000 x1 5W-40 | delta 1L — ⏳ ожидает прогон |
