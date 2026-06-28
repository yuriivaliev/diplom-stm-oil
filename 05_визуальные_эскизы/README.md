# Этап 6 — визуальные эскизы упаковки СТМ

**Дедлайн:** 27.06.2026 · **Статус:** ✅ **8/8 front rev.2** · **Обновлено:** 27.06.2026

---

## Scope (утверждено)

**4 SKU × format = 8 front mockups** + **3 концепта** на пилоте 5W-40 4L.

| SKU | Formats | Sub-line |
|-----|---------|----------|
| 5W-40 · 10W-40 | **4L + 1L** | Classic Protect |
| 5W-30 | **4L + 1L** | Modern Tech |
| 0W-20 | **5L + 1L** | Modern Tech |

**Unified carrier (rev.2):** premium **graphite-grey matte HDPE** на всех 8 SKU — batch cleanup по [`prompt_for_img_material_cleanup_all_final.md`](prompt_for_img_material_cleanup_all_final.md) · master ref: **0W-20 5L**.

---

## Артефакты

| # | Файл / папка | Статус |
|---|--------------|:------:|
| 1 | [`Eliten_DESIGN.md`](Eliten_DESIGN.md) | ✅ design tokens |
| 2 | [`бриф_матрица_8SKU.md`](бриф_матрица_8SKU.md) | ✅ |
| 3 | [`обоснование_эскизов.md`](обоснование_эскизов.md) | ✅ PGMM/ODSA → design |
| 4 | [`ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md`](ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md) | ✅ decision record |
| 5 | **[`финал/`](финал/)** — **8 × `* rev 2.png`** | ✅ **canonical** |
| 6 | **9 prompts** `prompt_for_img_*_final.md` | ✅ reproducibility |
| 7 | Wiki [`55_визуал_эскизы_Eliten.md`](../Cursor/wiki/55_визуал_эскизы_Eliten.md) | ✅ |
| 8 | Глава [`07_Дизайн.md`](../06_синтез_и_текст_диплома/главы/07_Дизайн.md) | 🟡 prose |

---

## Pipeline (зафиксировано 27.06)

1. **3 концепта** → `концепт/` · пилот **Classic Protect 5W-40 4L**
2. **Выбор** → dual-handle · [`ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md`](ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md)
3. **8 per-SKU prompts** → img2img / edit · labels locked
4. **Material cleanup (all)** → единый цвет/фактура канистры · labels **не менять**
5. **Back label** — ⚪ Figma/Canva · regulatory Cyrillic

---

## Входы

- PGMM: матрицы 5W-40 · 0W-20 · 10W-40 · 5W-30 ref · [08_PGMM](../Cursor/wiki/08_PGMM_упаковка.md)
- ODSA copy: [`ODSA_название_Eliten_матрица_слоганов.md`](../04_DD_ODSA_название_бренда/ODSA_название_Eliten_матрица_слоганов.md)
- ТЗ: [`FIPS_Eliten_RU1172689.md`](../04_DD_ODSA_название_бренда/FIPS/FIPS_Eliten_RU1172689.md)
- Positioning: `.cursor/rules/eliten-positioning.mdc`

---

## Оговорки

- AI mockups · **ART-001** pre-launch · кириллица approximate → production overlay
- **LAC-04:** @1.2 m / @120px — target, not measured
