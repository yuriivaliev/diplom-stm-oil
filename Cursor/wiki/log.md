# Wiki Log — история обновлений

Хронологический журнал **изменений вики** (не заменяет `журнал_проекта.md`).

---

| Дата | Действие | Страницы | Источник |
|------|----------|----------|----------|
| 25.06.2026 | **Синхронизация + каркас этап 7:** Eliten, 2 матрицы; 9 stubs `06_…/главы/`; README, overview, 01, AGENTS, журнал | 01, 08, index, overview, AGENTS, `06_…` | пользователь |
| 25.06.2026 | **Матрица 0W-20 rev.1** (4×18); wiki/19–26; dual-cluster в 08 | 08, 19–26, `03_…/матрица_0W-20` | skill stm-pgmm-odsa |
| 27.05.2026 | Зафиксирован цикл **DR → декомпозиция (2a/3a) → этапы 4+**; гейт в AGENTS, 01, 07 | 08, 01, 06, 07, AGENTS | согласование с пользователем |
| 27.05.2026 | Завершение инфраструктуры: `raw/README`, корневой `README`, `.cursor/rules`, ссылки в index | raw, index | — |
| 27.05.2026 | **Создание вики Cursor** (полный каркас Karpathy-style) | index, overview, 00–07, log | DR-A run2, DR-B run1, журнал, каноны |
| 27.05.2026 | Ingest DR-B run1 + URL verify 18/18 | 03, 04, 05 | `отчёт_DR-B_run1.md`, `B_URL_реестр_run1.md` |
| 27.05.2026 | Ingest DR-A run2 (канон) | 02, 04 | `A_рост_и_изменения_РФ_канон.md`, `A_URL_реестр_run2.md` |
| 27.05.2026 | Фиксация этапов 0–3 ✅ | 01, overview | `журнал_проекта.md` |
| 19.06.2026 | Ingest PGMM-анализ упаковки Лукойл Люкс 5W-40 | 10, index | Чат с пользователем |
| 19.06.2026 | Ingest PGMM-анализ упаковки Gazpromneft Premium N 5W-40 | 11, index | Чат с пользователем |
| 19.06.2026 | Ingest PGMM full Mobil Super 3000 x1 5W-40 (4L) | 12, index | Чат с пользователем |
| 19.06.2026 | Ingest PGMM delta Mobil Super 3000 x1 5W-40 (1L vs 4L) | 13, index | Чат с пользователем, изображение 1L |
| 19.06.2026 | Ingest PGMM delta LUKOIL LUXE 5W-40 (1L vs 4L) | 14, index | Чат с пользователем, изображение 1L |
| 19.06.2026 | Ingest PGMM delta Gazpromneft Premium N 5W-40 (1L vs 4L) | 15, index | Чат с пользователем, изображение 1L |
| 19.06.2026 | Шаблон промпта PGMM Delta + README в `03_PGMM_ODSA_упаковка_конкуренты/` | log, 07 | пользователь |
| 23.06.2026 | ODSA claims audit LUKOIL LUXE 5W-40 4L (front+back) | 16, index | фото SKU + спецификации оператора |
| 23.06.2026 | ODSA LUKOIL rev.2: canonical SN/CF via lukoil-masla.ru; legacy SL front deprecated | 16 | скрин сайта оператора |
| 23.06.2026 | ODSA LUKOIL rev.3: current front photo SN/CF (LUXE SYNTHETIC); evolution SL→SN зафиксирована | 16 | фото фронт оператора |
| 23.06.2026 | **ODSA Autostart** Gazpromneft Premium N 5W-40 4L — CMC v0, Evidence Ledger G01–G09, BP-01 pending | 17, index, README `03_…` | фото оператора + ODSA v1.6.7 |
| 23.06.2026 | **ODSA rev. 1** GPN 5W-40 4L — site triangulation GPN-01, findings F-G01…G10, CR register, matrix row | 17, index, README `03_…` | скрин GPN + operator attestation |
| 23.06.2026 | **ODSA rev. 2** GPN — GPN-01 verified wiki/04, DC-EP locked, G15/G16; Firecrawl scrape GPN blocked | 04, 17, log | operator + Firecrawl attempt |
| 23.06.2026 | **ODSA Autostart** Mobil Super 3000 x1 5W-40 4L — CMC v0, EVID-M01…M12, ART-001…003, BP-01 pending | 18, index, README `03_…` | фото оператора (3) + ODSA v1.6.7 |
| 23.06.2026 | **ODSA rev. 1** Mobil 5W-40 4L — operator attestation M13 (wrap stable since 2022); Strata pass F-M01…M11; CR register | 18, index | operator attestation |
| 23.06.2026 | **ODSA rev. 2** Mobil — M14/M15: parallel import + RU overlay sticker; F-M04 ↓ Moderate; F-M12; CR-M03 partial | 18, index | operator channel context |
| 23.06.2026 | **ODSA rev. 3 locked** Mobil 5W-40 4L — RU overlay text M16–M17; F-M13/F-M14/F-M15; DC-EP:A; тройка ODSA 4L complete | 18, index, README `03_…` | operator accept as-is + RU specs attestation |
| 23.06.2026 | **Firecrawl MCP** — fix symlink cycle, Home `~/.cursor/mcp.json`, URL-format; troubleshooting в Cursor/README | Cursor/README, setup script, `03_…/README` | сессия MCP |
| 23.06.2026 | **Canonical matrix row** (18 строк ODSA×PGMM) — wiki/16–18 + `ODSA_matrix_row_шаблон.md` | 16, 17, 18, README `03_…` | унификация для сводной матрицы |
| 25.06.2026 | **Матрица PGMM+ODSA 5W-40 rev.2** — §3.0 transpose 18×3 (wiki/16–18) + matrix 6×18 + ODSA 1L [27–29] | `03_…/матрица_5W-40`, 08 | PGMM/10 refresh pending |
| 23.06.2026 | **Синхронизация статусов** + каркас `06_синтез_…/Оглавление_и_каркас.md` + папки 04, 05 | index, 01, 07, overview, README, AGENTS, журнал | дедлайн 27.06 |
| 25.06.2026 | **Skill `stm-pgmm-odsa`** — PGMM full + delta workflow; `.cursor/skills/stm-pgmm-odsa/` | 09, `.cursor/skills/` | чат: skill-PGMM |
| 25.06.2026 | **Split skills этап 4:** `stm-pgmm`, `stm-pgmm-delta`, `stm-odsa`; `stm-pgmm-odsa` → роутер | 09, AGENTS, `.cursor/skills/` | пользователь |
| 25.06.2026 | **PGMM _full** Mobil 1 0W-20 5L — новая SAE-ветка 0W-20; wiki/19 + 08_PGMM §0W-20 | 19, 08, index | skill stm-pgmm, фото фронт |
| 25.06.2026 | **PGMM delta** Mobil 1 0W-20 1L vs 5L — MOCC_M1D_01…LAC01; таблица 5L vs 1L | 20, index | skill stm-pgmm-delta, фото 1L фронт |
| 25.06.2026 | **ODSA rev.1 locked** Mobil 1 0W-20 5L — front+back; dexos1 Gen3 front; API/ILSAC back-only; 18-row matrix | 21, 08, index | skill stm-odsa, фото 5L front+back |
| 25.06.2026 | **ODSA rev.1 provisional** Mobil 1 0W-20 1L — front-only; UA/TR/ISR/AR; back n/d | 22, index | skill stm-odsa, фото 1L front |
| 25.06.2026 | **ODSA rev.2 locked** Mobil 1 0W-20 5L — RU overlay text attestation; two-layer RF; overlay ≈ base back | 21, 08, index | operator RU sticker text |
| 25.06.2026 | **ODSA rev.2 provisional** Mobil 1 0W-20 1L — inherit line overlay from wiki/21 | 22, index | operator attestation |
| 25.06.2026 | **Матрица PGMM+ODSA 0W-20** (4×18) Mobil 1 + Castrol EDGE × 5L/1L + wiki/08 §0W-20 | `03_…/матрица_0W-20`, 08 | Castrol stm-odsa pending |
| 25.06.2026 | **PGMM _full** Castrol EDGE 0W-20 V 5L — front+back; HYSPEC hybrid gate; OEM back grid; wiki/23 + 08_PGMM §0W-20 | 23, 08, index | skill stm-pgmm, фото фронт+back |
| 25.06.2026 | **PGMM delta** Castrol EDGE 0W-20 V 1L vs 5L — MOCC_CED_01…LAC01; HYSPEC header robust @ thumbnail; таблица 5L vs 1L | 24, 23, index | skill stm-pgmm-delta, фото 1L фронт |
| 25.06.2026 | **ODSA rev.1 locked** Castrol EDGE 0W-20 V 5L — front+back; HYSPEC front; API lacuna both faces; OEM back-only; 18-row matrix | 25, 08, index | skill stm-odsa, фото 5L front+back |
| 25.06.2026 | **ODSA rev.1 provisional** Castrol EDGE 0W-20 V 1L — front-only; QR front; back n/d; line inherit from wiki/25 | 26, index | skill stm-odsa, фото 1L front |
| 25.06.2026 | **ODSA rev.1 provisional** LUKOIL LUXE 5W-40 1L — front+site; SN/CF front; cross-format pass vs 4L; back n/d; 18-row matrix | 27, `03_…/матрица_5W-40`, index | skill stm-odsa, фото 1L front |
| 25.06.2026 | **ODSA rev.2 locked** LUKOIL LUXE 5W-40 1L — back **line inherit** wiki/16 EVID-L03–L06; cross-face Pass; matrix R2 updated | 27, `03_…/матрица_5W-40`, 08, index | operator: оборот 1L = 4L |
| 25.06.2026 | **ODSA rev.1 provisional** GPN Premium N 5W-40 1L — front+site; OEM stack ⊃4L front; MB **229.5** vs 229.3; microtype; back n/d | 28, `03_…/матрица_5W-40`, index | skill stm-odsa, фото 1L front |
| 25.06.2026 | **ODSA rev.2 line-locked** GPN Premium N 5W-40 1L — back inherit wiki/17 (4L); SN/CF cross-face Pass; MB split-face 229.5↔229.3; 3662 inherit | 28, `03_…/матрица_5W-40` | operator: оборот 1L = 4L template |
| 25.06.2026 | **GPN-01 canonical + back parity rule** — «Ключевые характеристики» = канон; back **must** = site stack; F-G11 (4L) · F-G1D-16 (1L) · 6 gaps on physical back | 17 §rev.3, 28 rev.3, 04, `03_…/матрица_5W-40` | operator: сайт производителя |
| 25.06.2026 | **ODSA rev.1 provisional** Mobil Super 3000 x1 5W-40 1L — front verified; QR+819697D; benefit-icons absent; back/overlay inherit wiki/18; matrix R6 | 29, `03_…/матрица_5W-40`, index | skill stm-odsa, фото 1L front |
| 25.06.2026 | **ODSA rev.2** Mobil Super 3000 x1 1L — QR 819697D **presence locked**; destination **waived** (line-info URL attestation); anti-fraud **None**; matrix R6 rows 11–12 | 29, `03_…/матрица_5W-40` | operator attestation |

## Шаблон новой записи

```markdown
| ГГГГ-ММ-ДД | Ingest / правка | XX, YY | путь к raw-файлу |
```

---

## Следующее ожидаемое обновление

- **Этап 5:** `04_…/кандидат_Eliten.md` + 2 DDx · wiki `09_название_СТМ.md`
- **Этап 6:** эскизы Classic 5W-40 в `05_…/`
- **Этап 7:** наполнение stubs → Word/PDF до **27.06**
