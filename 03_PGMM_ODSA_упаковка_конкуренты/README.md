# PGMM / ODSA — упаковка конкурентов

Папка этапа **4** диплома: визуально-метафорический анализ упаковки моторных масел (PGMM) для сравнительной матрицы и ODSA.

---

## Быстрый старт

| Задача | Файл |
|--------|------|
| **Delta-анализ** (1L vs 4L, тот же SKU) | [`PGMM_delta_промпт_шаблон.md`](PGMM_delta_промпт_шаблон.md) |
| **Canonical ODSA matrix row** (18 строк × SKU) | [`ODSA_matrix_row_шаблон.md`](ODSA_matrix_row_шаблон.md) |
| **Сводная матрица PGMM+ODSA 5W-40** (6 SKU) | [`матрица_PGMM_ODSA_5W-40.md`](матрица_PGMM_ODSA_5W-40.md) |
| **Сводная матрица PGMM+ODSA 0W-20** (4 SKU) | [`матрица_PGMM_ODSA_0W-20.md`](матрица_PGMM_ODSA_0W-20.md) |
| **Сводная матрица PGMM+ODSA 10W-40** (6 SKU) | [`матрица_PGMM_ODSA_10W-40.md`](матрица_PGMM_ODSA_10W-40.md) |
| Wiki-сводка этапа 4 | [`Cursor/wiki/08_PGMM_упаковка.md`](../Cursor/wiki/08_PGMM_упаковка.md) |
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

## MCP (Firecrawl)

Конфиг: `../.cursor/mcp.json` (ключ локально, не в git).  
Симлинк: `.cursor/mcp.json` → `../../.cursor/mcp.json` (не `../` — иначе циклическая ссылка).

**Формат:** `https://mcp.firecrawl.dev/{fc-ключ}/v2/mcp` (обновлено 23.06.2026).

**Локальный Agent:** Settings → **Tools & MCP** (не Cloud) → Refresh / Reload Window.  
**Cloud Agent:** Settings → **Cloud** → Add Custom MCP → JSON из `../.cursor/mcp.cloud.example.json`.

Ключ: https://www.firecrawl.dev/app/api-keys

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
| 13 | Mobil Super 3000 x1 5W-40 | delta 1L |
| 14 | LUKOIL LUXE 5W-40 | delta 1L |
| 15 | Gazpromneft Premium N 5W-40 | delta 1L |

### ODSA (claims audit)

| ID | Бренд | Формат | Статус |
|----|-------|--------|--------|
| 16 | LUKOIL LUXE 5W-40 | 4L | ✅ |
| 17 | Gazpromneft Premium N 5W-40 | 4L | ✅ |
| 18 | Mobil Super 3000 x1 5W-40 | 4L | ✅ |
