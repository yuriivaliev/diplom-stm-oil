# Wiki Log — история обновлений

Хронологический журнал **изменений вики** (не заменяет `журнал_проекта.md`).

---

| Дата | Действие | Страницы | Источник |
|------|----------|----------|----------|
| 27.05.2026 | Skills: реестр `09_…` + 4 project skills; правило «предлагать skill после этапа» в AGENTS | 09, AGENTS, `.cursor/skills/` | пользователь |
| 27.05.2026 | Зафиксирован цикл **DR → декомпозиция (2a/3a) → этапы 4+**; гейт в AGENTS, 01, 07 | 08, 01, 06, 07, AGENTS | согласование с пользователем |
| 27.05.2026 | Завершение инфраструктуры: `raw/README`, корневой `README`, `.cursor/rules`, ссылки в index | raw, index | — |
| 27.05.2026 | **Создание вики Cursor** (полный каркас Karpathy-style) | index, overview, 00–07, log | DR-A run2, DR-B run1, журнал, каноны |
| 27.05.2026 | Ingest DR-B run1 + URL verify 18/18 | 03, 04, 05 | `отчёт_DR-B_run1.md`, `B_URL_реестр_run1.md` |
| 27.05.2026 | Ingest DR-A run2 (канон) | 02, 04 | `A_рост_и_изменения_РФ_канон.md`, `A_URL_реестр_run2.md` |
| 27.05.2026 | Фиксация этапов 0–3 ✅ | 01, overview | `журнал_проекта.md` |
| 19.06.2026 | Ingest PGMM-анализ упаковки Лукойл Люкс 5W-40 | 10, index | Чат с пользователем |
| 19.06.2026 | Ingest PGMM-анализ упаковки Gazpromneft Premium N 5W-40 | 11_PGMM_Gazpromneft_Premium_N_5W-40, index | Чат с пользователем |
| 19.06.2026 | Шаблон промпта PGMM Delta + README в `03_PGMM_ODSA_упаковка_конкуренты/` | log, 07 | пользователь |
| 23.06.2026 | **ODSA Autostart** Gazpromneft Premium N 5W-40 4L — CMC v0, Evidence Ledger G01–G09, BP-01 pending | 17, index, README `03_…` | фото оператора + ODSA v1.6.7 |
| 23.06.2026 | **ODSA rev. 1** GPN 5W-40 4L — site triangulation GPN-01, findings F-G01…G10, CR register, matrix row | 17, index, README `03_…` | скрин GPN + operator attestation |
| 23.06.2026 | **Firecrawl MCP** — fix symlink cycle, Home `~/.cursor/mcp.json`, URL-format; troubleshooting в Cursor/README | Cursor/README, setup script, `03_…/README` | сессия MCP |
| 23.06.2026 | **ODSA rev. 2** GPN — GPN-01 verified wiki/04, DC-EP locked, G15/G16; Firecrawl scrape GPN blocked | 04, 17, log | operator + Firecrawl attempt |
| 23.06.2026 | **ODSA Autostart** Mobil Super 3000 x1 5W-40 4L — CMC v0, EVID-M01…M12, ART-001…003, BP-01 pending | 18, index, README `03_…` | фото оператора (3) + ODSA v1.6.7 |
| 23.06.2026 | **ODSA rev. 1** Mobil 5W-40 4L — operator attestation M13 (wrap stable since 2022); Strata pass F-M01…M11; CR register | 18, index | operator attestation |
| 23.06.2026 | **ODSA rev. 2** Mobil — M14/M15: parallel import + RU overlay sticker; F-M04 ↓ Moderate; F-M12; CR-M03 partial | 18, index | operator channel context |
| 23.06.2026 | **ODSA rev. 3 locked** Mobil 5W-40 4L — RU overlay text M16–M17; F-M13/F-M14/F-M15; DC-EP:A; тройка ODSA 4L complete | 18, index, README `03_…` | operator accept as-is + RU specs attestation |

---

## Шаблон новой записи

```markdown
| ГГГГ-ММ-ДД | Ingest / правка | XX, YY | путь к raw-файлу |
```

---

## Следующее ожидаемое обновление

- После этапа **4 (PGMM+ODSA):** новая страница `08_PGMM_упаковка.md` + index.
- После `literature_и_источники.md` sync → правка `04_источники_и_URL.md`.

| 19.06.2026 | Ingest PGMM delta LUKOIL LUXE 5W-40 (1L vs 4L) | 14, index | Чат с пользователем, изображение 1L |
| 19.06.2026 | Ingest PGMM delta Mobil Super 3000 x1 5W-40 (1L vs 4L) | 13, index | Чат с пользователем, изображение 1L |
| 19.06.2026 | Ingest PGMM full Mobil Super 3000 x1 5W-40 (4L) | 12, index | Чат с пользователем |
| 19.06.2026 | Ingest PGMM delta Gazpromneft Premium N 5W-40 (1L vs 4L) | 15, index | Чат с пользователем, изображение 1L |
| 23.06.2026 | ODSA claims audit LUKOIL LUXE 5W-40 4L (front+back) | 16, index | фото SKU + спецификации оператора |
| 23.06.2026 | ODSA LUKOIL rev.2: canonical SN/CF via lukoil-masla.ru; legacy SL front deprecated | 16 | скрин сайта оператора |
| 23.06.2026 | ODSA LUKOIL rev.3: current front photo SN/CF (LUXE SYNTHETIC); evolution SL→SN зафиксирована | 16 | фото фронт оператора |
| 23.06.2026 | **Canonical matrix row** (18 строк ODSA×PGMM) — wiki/16–18 + `ODSA_matrix_row_шаблон.md` | 16, 17, 18, README `03_…` | унификация для сводной матрицы |
| 23.06.2026 | **Матрица PGMM+ODSA 5W-40** (6×18) + wiki `08_PGMM_упаковка.md` | `03_…/матрица_…`, 08, index | transpose wiki/16–18 + PGMM 10–15 |
