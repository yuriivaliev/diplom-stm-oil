# Визуальные эскизы Eliten (этап 6)

**Статус:** ✅ **8/8 front rev.2** · unified HDPE · **Обновлено:** 27.06.2026  
**Папка:** [`05_визуальные_эскизы/`](../05_визуальные_эскизы/) · канон: [`финал/`](../05_визуальные_эскизы/финал/)

---

## Scope

| SKU | Formats | Sub-line |
|-----|---------|----------|
| 5W-40 · 10W-40 | 4L + 1L | Classic Protect |
| 5W-30 | 4L + 1L | Modern Tech |
| 0W-20 | **5L + 1L** | Modern Tech |

**Итого:** 8 front mockups (rev.2) + 3 концепта (пилот 5W-40 4L) + **9 prompts** (reproducibility).

---

## Unified carrier (rev.2)

**Graphite-grey matte HDPE** на всех 8 SKU — batch material cleanup без изменения labels.

| Параметр | Значение |
|----------|----------|
| Master ref | **Modern Tech 0W-20 5L** |
| Batch prompt | [`prompt_for_img_material_cleanup_all_final.md`](../05_визуальные_эскизы/prompt_for_img_material_cleanup_all_final.md) |
| Pipeline | per-SKU prompt → material cleanup all |

---

## Выбранный концепт (26.06)

**✅ APPROVED:** dual-handle graphite · dark label · amber oil — decision record:

[`ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md`](../05_визуальные_эскизы/ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md)

Концепты DDx: `концепт/` · superseded pre-rev.2 → `архив/`

---

## Финальная матрица (rev.2 — canonical)

| Файл | SKU | Format |
|------|-----|--------|
| [`ELITEN Classic Protect 5W-40 4l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Classic%20Protect%205W-40%204l%20rev%202.png) | 5W-40 syn | 4L · **dual-handle** |
| [`ELITEN Classic Protect 5W-40 1l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Classic%20Protect%205W-40%201l%20rev%202.png) | 5W-40 syn | 1L |
| [`ELITEN Classic Protect 10W-40 4l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Classic%20Protect%2010W-40%204l%20rev%202.png) | 10W-40 semi | 4L |
| [`ELITEN Classic Protect 10W-40 1l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Classic%20Protect%2010W-40%201l%20rev%202.png) | 10W-40 semi | 1L |
| [`ELITEN Modern Tech 5W-30 4l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Modern%20Tech%205W-30%204l%20rev%202.png) | 5W-30 syn | 4L |
| [`ELITEN Modern Tech 5W-30 1l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Modern%20Tech%205W-30%201l%20rev%202.png) | 5W-30 syn | 1L |
| [`ELITEN Modern Tech 0W-20 5l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Modern%20Tech%200W-20%205l%20rev%202.png) | 0W-20 FS | **5L** · **material master** |
| [`ELITEN Modern Tech 0W-20 1l rev 2.png`](../05_визуальные_эскизы/финал/ELITEN%20Modern%20Tech%200W-20%201l%20rev%202.png) | 0W-20 FS | 1L |

Полный индекс + prompts: [`финал/README.md`](../05_визуальные_эскизы/финал/README.md)

---

## Промпты (27.06)

| SKU · format | File |
|--------------|------|
| 5W-40 · 4L / 1L | `prompt_for_img_5W-40_4L_final.md` · `…_1L_final.md` |
| 10W-40 · 4L / 1L | `prompt_for_img_10W-40_4L_final.md` · `…_1L_final.md` |
| 5W-30 · 4L / 1L | `prompt_for_img_5W-30_4L_final.md` · `…_1L_final.md` |
| 0W-20 · 5L / 1L | `prompt_for_img_0W-20_5L_final.md` · `…_1L_final.md` |
| All · material | `prompt_for_img_material_cleanup_all_final.md` |

---

## Design system

| Токен | Classic Protect | Modern Tech |
|-------|-----------------|-------------|
| Primary | Graphite jug `#4A4F54` · navy `#0D2137` · silver label | Navy `#0D2137` · tech `#3B82F6` |
| Motif | Amber oil **ribbon** · spec band | Grid / precision · optional amber accent |
| Antidote | No armor (LUKOIL/GPN) · **no coolant color (CAT-01)** | No Mobil lattice / Castrol gold |

Полная спека: [`Eliten_DESIGN.md`](../05_визуальные_эскизы/Eliten_DESIGN.md)  
Обоснование: [`обоснование_эскизов.md`](../05_визуальные_эскизы/обоснование_эскизов.md)

---

## Ограничения

- **NEG N-01…N-24:** rhetoric · **international front** · **motor-oil fluid (CAT-01)** · visual antidote — [`Eliten_DESIGN.md` §6](../05_визуальные_эскизы/Eliten_DESIGN.md)
- **Front/back:** RF · EAC · Cyrillic regulatory · legal manufacturer — **back only**
- **ART-001:** pre-launch concept · confidence M
- **AI-CYR:** кириллица в mockup approximate → Figma/Canva final
- **LAC-04:** @1.2 m не измерено · target @120px

---

## Связи

- Этап 5: [54_название_СТМ_Eliten.md](54_название_СТМ_Eliten.md)
- PGMM: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Глава 6: [`07_Дизайн.md`](../06_синтез_и_текст_диплома/главы/07_Дизайн.md)
