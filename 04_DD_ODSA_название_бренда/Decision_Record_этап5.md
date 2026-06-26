# Decision Record — этап 5 (название + copy)

**Дата:** 25.06.2026 · **Обновлено FIPS:** 25.06.2026 · **Метод:** UHAF/DDx + ODSA + ФИПС (вне LLM)

---

## BoundedModel

| Поле | Содержание |
|------|------------|
| **Supported** | **Eliten** — default brand (**RU 1172689**, кл. **04**, статус **действует**) |
| **Supported** | **Verum**, **Calibr** — contrastive DDx cases |
| **Weakened** | Eliten false premium (смягчено positioning «инженерная марка») |
| **Rejected** | Motrade, Ingenum, Kinet; Fluxen/Spektra deferred |
| **Unresolved** | retail @1.2 m (LAC-04); ART-001 per SKU |
| **Prohibited** | LLM ≠ юридическое заключение по ТЗ |

---

## FIPS — Eliten ✅ (25.06.2026)

**Артефакт:** [`FIPS/FIPS_Eliten_RU1172689.md`](FIPS/FIPS_Eliten_RU1172689.md)

| Проверка | Результат |
|----------|-----------|
| RU 1172689 | ✅ действует **03.12.2025 — 08.09.2035** |
| Заявка 2025796734 | ✅ от **08.09.2025** |
| МКТУ **кл. 04** | ✅ **масло моторное** и смазочные/технические масла |
| Blocker | **нет** |
| Правообладатель | ООО «НАРИН НЕФТЬ ГАЗ» — зафиксировать в гл. 5 |

**Eliten replacement trigger:** ~~FIPS blocker~~ — **снят**.

---

## Decision

| Candidate | Brand name | Copy architecture | Action |
|-----------|------------|-------------------|--------|
| **Eliten** | **RECOMMEND with LIMIT** | [`ODSA_название_Eliten_матрица_слоганов.md`](ODSA_название_Eliten_матрица_слоганов.md) | **Proceed этап 6** |
| Verum | RECOMMEND (contrastive) | — | Глава 5 DDx |
| Calibr | RECOMMEND with LIMIT | — | Глава 5 DDx |

---

## Monitoring

- [x] FIPS Eliten — кл. 04, статус, срок (**25.06.2026**)
- [ ] ART-001 этикетка 5W-40 4L + 1L
- [ ] TDS parity (pack = web) per SKU
- [ ] Legibility @1.2 m (LAC-04)
- [ ] Скриншоты ФИПС в `FIPS/*.png` (приложение диплома)

---

## Артефакты этапа 5

| # | Файл | Статус |
|---|------|:------:|
| 1 | Пул 8 имён | ✅ |
| 2 | Triad + funnel | ✅ |
| 3 | `кандидат_01…03` | ✅ |
| 4 | `ODSA_название_Eliten_матрица_слоганов.md` | ✅ |
| 5 | `Decision_Record_этап5.md` | ✅ |
| 6 | Wiki `54_название_СТМ_Eliten.md` | ✅ |
| 7 | **`FIPS/FIPS_Eliten_RU1172689.md`** | ✅ |
| 8 | ТЗ FIPS скриншоты | 🟡 положить в `FIPS/` |
