# Сравнительная матрица PGMM + ODSA — 5W-30 (C3 / ESP point-ref)

**Этап:** 4 · **Регион:** европейская часть РФ (retail / import proxy)  
**Дата сборки:** 25.06.2026 · **Rev.** 1  
**Правило строк:** **1 format = 1 row** · 6 строк = 3 бренда × (4L + 1L)  
**Источники:** wiki PGMM [30–33, 38–39](../Cursor/wiki/) · ODSA [34–37, 40–41](../Cursor/wiki/) · schema [`ODSA_matrix_row_шаблон.md`](ODSA_matrix_row_шаблон.md)

> **Scope:** point-ref **вне** матриц 5W-40 / 0W-20 · C3/ESP niche · **не смешивать** с DR-A (доли) / DR-B (SAE-таблицы).

---

## 0. Scope и ограничения

| Поле | Значение |
|------|----------|
| SAE | **5W-30** only |
| Сегмент | Mid-premium C3 (LUKOIL GC, GPN C3) + premium import ESP (Mobil 1) |
| **≠ 5W-40** | [`матрица_PGMM_ODSA_5W-40.md`](матрица_PGMM_ODSA_5W-40.md) |
| **≠ 0W-20** | [`матрица_PGMM_ODSA_0W-20.md`](матрица_PGMM_ODSA_0W-20.md) |
| ODSA LUKOIL / GPN | Full audit locked · wiki/34–37 |
| ODSA Mobil ESP 4L | Locked · wiki/40 · **4L back photo unreadable** · line canon inherit 1L |
| ODSA Mobil ESP 1L | Locked · wiki/41 · **primary line canon** for API SP / ACEA C3 / OEM |

---

## 1. Индекс строк (6 SKU)

| Row | Бренд | Формат | PGMM | ODSA | Ключевой риск |
|-----|-------|--------|------|------|---------------|
| R1 | LUKOIL GENESIS ARMORTECH GC | **4L** | [30](../Cursor/wiki/30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md) | [34](../Cursor/wiki/34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) ✅ | OEM back-only · batch 2022 |
| R2 | LUKOIL GENESIS ARMORTECH GC | **1L** | [31](../Cursor/wiki/31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md) | [35](../Cursor/wiki/35_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_1L.md) ✅ | 229.52 drift **not confirmed** on 1L photo |
| R3 | Gazpromneft Premium C3 | **4L** | [32](../Cursor/wiki/32_PGMM_Gazpromneft_Premium_C3_5W-30.md) | [36](../Cursor/wiki/36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) ✅ | Photo SP/SN drift · OEM microtype · site superset |
| R4 | Gazpromneft Premium C3 | **1L** | [33](../Cursor/wiki/33_PGMM_Gazpromneft_Premium_C3_5W-30_1L_delta.md) | [37](../Cursor/wiki/37_ODSA_Gazpromneft_Premium_C3_5W-30_1L.md) ✅ | Authenticity deferral absent vs 4L · 2017 photo |
| R5 | Mobil 1 ESP | **4L** | [38](../Cursor/wiki/38_PGMM_mobil_1_esp_5w_30_4L.md) | [40](../Cursor/wiki/40_ODSA_mobil_1_esp_5w_30_4L.md) ✅ | API off front · **4L back unreadable** · import |
| R6 | Mobil 1 ESP | **1L** | [39](../Cursor/wiki/39_PGMM_mobil_1_esp_5w_30_1L_delta.md) | [41](../Cursor/wiki/41_ODSA_mobil_1_esp_5w_30_1L.md) ✅ | Two-step trust · back-only OEM · no Cyrillic |

---

## 2. Блок PGMM (6 строк · compressed)

| Row | M_SYSTEM | Ключевая метафора | EVAL (1 строка) | STM vector |
|-----|----------|-------------------|-----------------|------------|
| **R1** GC 4L | Hyper-Armor + German Cars + Front Standards | Carbon armor + «FOR GERMAN CARS» | Front API/ACEA **strong** · OEM back · fidelity medium-low | Readable OEM front @1.2 m |
| **R2** GC 1L | **= R1** | Armor **↑%** on narrow label | Thumbnail armor OK · OEM still back | 1L-native layout + front OEM icons |
| **R3** GPN C3 4L | Spec-as-Brand + Thermokinetic Swirl | «C3» in name + front SP/C2/C3 | Transaction high · OEM microtype dead | Single-source spec all faces |
| **R4** GPN C3 1L | **= R3** | Claustrophobic rescale | Top-up 8/10 · authenticity gap vs 4L | Front dexos2-equivalent if program |
| **R5** ESP 4L | Emission-Network + Multi-Fuel + F1 Heritage | Green lattice + ESP band | Premium whitespace · **specs н/д** on photo | Front C3/API + fluid hero |
| **R6** ESP 1L | **= R5** | Lattice cropped · back unlock | Back transparency **↑** vs R5 photo | Front-loaded C3 for doliv compare |

---

## 3. ODSA transpose — canonical 18 параметров (6 строк)

**Легенда Confidence:** H / M / L · источник: canonical tables wiki/34–37, 40–41

| # | Параметр | R1 GC 4L | R2 GC 1L | R3 GPN C3 4L | R4 GPN C3 1L | R5 ESP 4L | R6 ESP 1L |
|---|----------|----------|----------|--------------|--------------|-----------|-----------|
| 1 | M_SYSTEM | Hyper-Armor + German Cars · **H** | = · **H** | Spec-as-Brand + Swirl · **H** | = · **H** | Emission-Network + F1 · **H** | = · **H** |
| 2 | Carrier | Asym jug + handle · **H** | Narrow + ridges · **H** | Wide jug · **H** | Narrow + strip · **H** | 4L jug · **H** | Top-up bottle · **H** |
| 3 | Класс | Syn SN/CF · **H** | = · **H** | Syn SP canon · **H** | = · **H** | Syn SP (inherit/canonical) · **H/M** | Syn SP · **H** |
| 4 | SAE legibility | High · **H** | High · **H** | High · **H** | High · **H** | High · **H** | High rel. ↑ · **H** |
| 5 | API front/back | SN/CF · SN/CF · **H** | = · **H** | SP/SN photo · **SP canon** · **H** | SN photo · **SP canon** · **H** | **— / н/д** · **SP canon** · **M** | **— / SP** · **H** |
| 6 | ACEA front/back | C3 · C3 · **H** | = · **H** | C2/C3 · C3 photo · **H** | C3 · C3 · **H** | **— / н/д** · **C3 canon** · **M** | **— / C3** · **H** |
| 7 | OEM front | **Нет** · **H** | **Нет** · **H** | Microtype · **H** | Microtype ↓ · **H** | **Нет** · **H** | **Нет** · **H** |
| 8 | OEM back/site | Full German stack · **H** | Full · **H** | Back + **site superset** · **H/M** | Back + site · **H/M** | **н/д photo** · canon inherit · **M** | Full German stack · **H** |
| 9 | Benefit-icons | DuraMax named · **M** | = · **M** | Swirl low · **M** | = · **M** | Low front · **M** | Bullets back · **M** |
| 10 | Cross-face | **Pass** · **H** | **Pass** · **H** | Photo fail · **Pass canon** · **H** | **Pass canon** · **H** | Partial · **M** | Partial shelf · **H** |
| 11 | Digital gap | Site ≈ pack · **H** | ≈ · **H** | Site superset · **M** | superset · **M** | **н/д** · **L** | **н/д** · **L** |
| 12 | Anti-fraud | QR+EAC · **H** | = · **H** | 3662 deferral · **H** | weaker 1L · **M** | QR only · **M** | QR+stamp · **M** |
| 13 | RF supply | Official RU · **H** | = · **H** | Official · **H** | = · **H** | Import EN · **H** | Import EN/TR/GR · **H** |
| 14 | Маркировка РФ | EAC+ISO · **H** | = · **H** | EAC · **H** | EAC · **H** | **н/д** · **L** | **н/д** · **L** |
| 15 | Кириллица | RU back · EN front · **H** | = · **H** | RU dominant · **H** | = · **H** | EN only · **H** | EN/TR/GR · **H** |
| 16 | Thumbnail | High · **H** | Med-high · **M** | Med-high · **M** | Med · **M** | Med-high · **M** | Medium · **M** |
| 17 | Cognitive load | High · **H** | High · **H** | High claustro · **H** | Bimodal · **H** | Medium front · **H** | Bimodal · **H** |
| 18 | Legacy risk | Batch 2022 · **M** | = · **M** | Photo 2017 · **M** | Photo 2017 · **M** | 4L stamp н/д · **M** | Batch 2024 · **H** |

---

## 4. MECE white space для СТМ (5W-30 C3 proxy)

| Gap (MECE) | Лучший конкурент сейчас | СТМ action |
|------------|-------------------------|------------|
| Front API + ACEA C3 together | GPN C3 (R3/R4) · GC front row (R1/R2) | **Mandatory** on both 4L and 1L |
| Readable OEM @1.2 m | **None** — all back or microtype | Top-3 OEM icons front |
| Official RU + Cyrillic | LUKOIL · GPN | Integrated wrap · EAC |
| Low-SAPS / DPF explicit | GPN back text · GC back RU | Named chemistry + metric |
| Import trust / anti-fraud | GPN 3662 · LUKOIL QR | Verified QR MAP + batch |
| Premium import prestige | Mobil ESP whitespace | **Do not copy** without spec proof |

---

## 5. Связи

- Сводка этапа 4: [08_PGMM_упаковка.md](../Cursor/wiki/08_PGMM_упаковка.md)
- DR-B SAE context: [03_DR-B_вязкости_SAE.md](../Cursor/wiki/03_DR-B_вязкости_SAE.md)
- URL canon: [04_источники_и_URL.md](../Cursor/wiki/04_источники_и_URL.md) · GPN-02 · LLK-01

---

*Rev. 1 · 25.06.2026 · ingest stm-odsa Mobil ESP 4L+1L · completes 5W-30 point-ref cluster*
