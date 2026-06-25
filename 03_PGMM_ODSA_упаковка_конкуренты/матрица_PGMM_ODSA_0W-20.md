# Сравнительная матрица PGMM + ODSA — 0W-20 (premium synthetic · SAE-фронтир)

**Этап:** 4 · **Регион:** европейская часть РФ (retail / import proxy)  
**Дата сборки:** 25.06.2026  
**Правило строк:** **1 format = 1 row** · 4 строки = 2 бренда × (5L + 1L)  
**Источники:** wiki PGMM [19–20, 23–24](../Cursor/wiki/) · ODSA [21–22, 25–26](../Cursor/wiki/) · schema [`ODSA_matrix_row_шаблон.md`](ODSA_matrix_row_шаблон.md)

---

## 0. Scope и ограничения

| Поле | Значение |
|------|----------|
| SAE | **0W-20** only (Castrol: **0W-20 V**) |
| Сегмент | Premium / upper-mainstream full synthetic (Modern/Tech линейка СТМ) |
| **≠ 5W-40** | **Не смешивать** с [`матрица_PGMM_ODSA_5W-40.md`](матрица_PGMM_ODSA_5W-40.md) (mass-mid Classic/Protect) |
| ODSA Mobil 5L | Full audit · wiki/21 · **rev.2 locked** |
| ODSA Mobil 1L | **Provisional** · wiki/22 · front-only · back **н/д** |
| ODSA Castrol 5L | Full audit · wiki/25 · **rev.1 locked** |
| ODSA Castrol 1L | **Provisional** · wiki/26 · front-only · back **н/д** |
| Фасовка СТМ (RBS) | Целевая **5L+1L** для 0W-20; конкуренты в матрице — **5L+1L** (не 4L) |

---

## 1. Индекс строк (4 SKU)

| Row | Бренд | Формат | PGMM | ODSA | Ключевой риск |
|-----|-------|--------|------|------|---------------|
| R1 | Mobil 1 | **5L** | [19](../Cursor/wiki/19_PGMM_mobil_1_0w_20_5L.md) | [21](../Cursor/wiki/21_ODSA_mobil_1_0w_20_5L.md) ✅ locked | Parallel import · API off front · two-layer RF |
| R2 | Mobil 1 | **1L** | [20](../Cursor/wiki/20_PGMM_mobil_1_0w_20_1L_delta.md) | [22](../Cursor/wiki/22_ODSA_mobil_1_0w_20_1L.md) 🟡 provisional | Back **н/д** · dexos1 **↓ @120px** · whitespace compressed |
| R3 | Castrol EDGE | **5L** | [23](../Cursor/wiki/23_PGMM_castrol_edge_0w_20_v_5L.md) | [25](../Cursor/wiki/25_ODSA_castrol_edge_0w_20_v_5L.md) ✅ locked | API lacuna both faces · OEM **back-only** · EU EN · no RU overlay |
| R4 | Castrol EDGE | **1L** | [24](../Cursor/wiki/24_PGMM_castrol_edge_0w_20_v_1L_delta.md) | [26](../Cursor/wiki/26_ODSA_castrol_edge_0w_20_v_1L.md) 🟡 provisional | Back **н/д** · QR front · HYSPEC **preserved @120px** |

---

## 2. Блок PGMM (4 строки)

| Row | M_SYSTEM | DOMAIN Source → Target | Ключевая метафора | Лакуны (LACUNA) | EVAL (1 строка) | Импликация для СТМ |
|-----|----------|------------------------|-------------------|-----------------|-----------------|---------------------|
| **R1** Mobil 5L | bio_lattice_hyper_performance + oem_sovereignty + eco_modern_gateway | A: honeycomb lattice / monolith «1» / modern ecology → B: 0W-20 tribology / hybrid Atkinson | Biomimetic **solid lattice** + stacked performance claims | Fluid/eco viz; **API SP front**; Cyrillic; lab metrics (wiki/19) | Rhetoric **7/10** · fidelity **5/10** · premium whitespace **high** · RU **low** (wiki/19) | **Fluid-precision** / clean flat; **API SP+GF-6A+ACEA C5 front**; multi-OEM front; Cyrillic official supply |
| **R2** Mobil 1L | **= R1** (константа) | = R1 | Lattice **lateral crop**; claim stack **peak load** bottom | dexos1 **unreadable @120px**; premium whitespace **↓**; UA\|TR export codes (delta/20) | Thumbnail **medium**; institutional delivery **↓** vs 5L; top-up context (delta/20) | 1L brief: **hero 0W-20 + OEM row readable @120px**; preserve whitespace; explicit QR MAP |
| **R3** Castrol 5L | hyspec_hybrid_gate + edge_hyperbole + tri_fuel_TAM + back_loaded_oem | A: cutting EDGE / gold trophy / HYSPEC wedge / motorsport → B: 0W-20 V tribology / ACEA C5 / hybrid | **Gold solid** + institutional **HYSPEC** hybrid gate | **OEM front**; API SP visible; Cyrillic; fluid viz; on-pack QR (wiki/23) | Rhetoric **8/10** · fidelity **4/10** · OEM shelf **back-only** · RU **low** (wiki/23) | Own **hybrid-spec badge** + lab proof; **multi-OEM front row**; не gold/edge hyperbole; verified QR |
| **R4** Castrol 1L | **= R3** (константа) | = R3 | HYSPEC header **preserved**; gold jug authority **↓** on narrow bottle | Back OEM/ACEA **invisible** front-only; tri-fuel **↓ @2m**; RU **константа** (delta/24) | Thumbnail **high-medium** (HYSPEC+EDGE+0W-20); **↑ hybrid cue** vs Mobil 1L (delta/24) | Header hybrid lockup + **Cyrillic OEM** + QR MAP; segment-focused (not tri-fuel dilution) |

---

## 3. Блок ODSA — canonical 18 параметров (transpose)

**Легенда Confidence:** H / M / L · **Castrol R3:** wiki/25 locked · **R4:** wiki/26 provisional

| # | Параметр | R1 Mobil 5L | R2 Mobil 1L | R3 Castrol 5L | R4 Castrol 1L |
|---|----------|-------------|-------------|---------------|---------------|
| 1 | M_SYSTEM | bio_lattice + oem_sovereignty · **H** · 19;21 | = R1 · **H** · 20 | hyspec + edge + back_oem · **H** · 23;25 | = R3 · **H** · 24;26 |
| 2 | Carrier morphology | 5L silver jug + handle + grip · **H** | 1L narrow bottle + grip-ridges · **H** · δ20 | 5L gold jug + handle · **H** · 25 | 1L narrow + upper grip · **H** · 26 |
| 3 | Класс (синт/полусинт) | **Advanced Synthetic** · **H** · 21 M1-07 | **Advanced Synthetic** front · **H** · 22 | **Full syn implied** (EDGE+C5) · **M** · 25 F-CE-09 | = R3 assumed · **M** · 26 |
| 4 | SAE 0W-20 legibility | **High** oversized · **H** · 21 | **High** full · **Medium @120px** · **M** · 22;δ20 | **High** white box 0W-20 V · **H** · 25 | **High** rel.↑ · **M** · 26 |
| 5 | API (front / back) | Front **—** · Back **SJ→SP RC** + overlay **SJ→SP EC+RC** · **H** · 21 | Front **—** · Back **н/д** · overlay line · **M** · 22 | Front **—** · Back visible **—** (GAP-CE-03) · **H/M** · 25 F-CE-02 | Front **—** · Back **н/д** · line inherit · **L** · 26 |
| 6 | ACEA (front / back) | Front **—** · Back+overlay **C5** · **H** · 21 | Front **—** · overlay **C5** line · **M** · 22 | Front **—** · Back **C5** · **H** · 25 | Front **—** · inherit R3 **C5** · **M** · 26 |
| 7 | OEM front (effective) | **Yes — dexos1 Gen3 GM** · **H** · 21 F-M1-03 | **Yes — dexos1** small · **unreadable @120px** · **M** · 22;δ20 | **No — HYSPEC only** · **H** · 25 F-CE-03 | **No — HYSPEC only** · **H** · 26 |
| 8 | OEM back / site / overlay | Ford/GM/FCA/FIAT + overlay stack · **H/M** · 21 | Overlay line (inherit 21) · **M** · 22 | Honda…Volvo + RBS0-2AE · **H** · 25 | Line inherit R3 · **M** · 26 |
| 9 | Benefit-icons | **Moderate** hybrid icon + stack · **M** · 21 | **Low-Moderate** hybrid **↓** · **M** · 22 | **Moderate** HYSPEC + tri-fuel text · **M** · 25 | HYSPEC **preserved** · tri-fuel **↓ @2m** · **M** · 26 |
| 10 | Cross-face consistency | **Partial** base + overlay layer · **H** · 21 | **Partial** back n/d · **L** · 22 GAP-M1D-01 | **Partial** SAE/HYSPEC OK · API/OEM back-loaded · **H** · 25 | Partial front-only · **L** · 26 |
| 11 | Digital / overlay gap | Overlay ≈ base back (notation only) · **M** · 21 | Line attestation ≈5L · **L** · 22 | FINDCAROIL.COM not triangulated · **L** · 25 | QR front · destination **n/d** · **L** · 26 |
| 12 | Anti-fraud UX | **QR latent only** · **M** · 21 | **QR only** · **M** · 22 | **Barcode + batch**; QR **н/д** 5L front · **M** · 25 | **QR + batch front** · **M** · 26 |
| 13 | RF supply & язык | **Parallel import** EN+EU + **RU overlay** · **H** · 21 | Parallel + overlay line · **M** · 22 | **EU wrap** · parallel import proxy · **M** · 25 | EU EN assumed · **M** · 26 |
| 14 | Маркировка РФ | Via **importer overlay** attestation · **M** · 21 | Overlay line · **M** · 22 | **н/д** on artifact · **L** · 25 GAP-CE-01 | **н/д** · **L** · 26 |
| 15 | Кириллица vs латиница | Base **EN**; RF → overlay **RU** · **M** · 21 | Base **EN** + export codes · **M** · 22 | **Latin only** EU langs · **H** · 25 | = R3 · **H** · 26 |
| 16 | Thumbnail ~120px | **High** «1» + 0W-20 · **H** · 19;21 | **Medium** footer fail · **M** · 22;δ20 | **High** HYSPEC + 0W-20 · **H** · 25 | **High-medium** HYSPEC+EDGE · **M** · 26 |
| 17 | Cognitive load / space | **Medium-low** premium whitespace · **H** · 19 | **High** compressed vs 5L · **H** · δ20 | **Medium** gold density · **H** · 25 | White room **↓** · **M** · 26 |
| 18 | Legacy / rev. risk | **Low** GF-6A/SP/Gen3 stack · **M** · 21 | **n/d** no batch · **L** · 22 | **Low–Medium** 2023 batch · API **н/д visible** · **M** · 25 | **n/d** no back batch · **L** · 26 |

---

## 4. Сводка 5L-only (cross-brand · Modern/Tech)

| Параметр | Mobil 1 5L | Castrol EDGE 5L |
|----------|------------|-----------------|
| API front | **—** | **—** (visible back **—**) |
| API back | **SJ→SP RC** + overlay | **н/д visible** (GAP-CE-03) |
| OEM front effective | **Yes — dexos1 Gen3** | **No** (back grid) |
| ACEA visible | Back+overlay **C5** | Back **C5** |
| Hybrid cue | Secondary footer badge | **HYSPEC front institutional** |
| RF supply | Parallel import + RU overlay | EU EN import |
| PGMM paradigm | Bio-lattice solid | Gold EDGE + HYSPEC wedge |
| Top STM gap (0W-20) | Cyrillic + **API SP front** + multi-OEM front | **OEM front row** + API front + Cyrillic official |

---

## 5. Паттерны рынка (premium 0W-20)

1. **Solid > Fluid (константа категории):** Mobil (honeycomb lattice) и Castrol (gold/EDGE wedge) **вытесняют** трибологию/текучесть — та же норма, что mass-mid 5W-40, но с **premium whitespace** (Mobil) или **gold institutional** (Castrol).
2. **Hybrid gate на фронте:** оба SKU адресуют modern/hybrid парк; Castrol (**HYSPEC**) сильнее institutional delivery, Mobil (**dexos1 Gen3**) — единственный **effective OEM-on-front** в паре 5L.
3. **API SP / GF-6A системно off-front:** на видимых faces обоих брендов — **white space для СТМ Modern/Tech** (явный API+ACEA на фронте).
4. **5L ≠ 1L (DRY rescale):** Mobil 1L **ломает** premium whitespace и dexos1 @ thumbnail; Castrol 1L **сохраняет** HYSPEC header — **format-fairness** различается по бренду.
5. **RU-channel lacuna:** оба конкурента в прокси **EN/EU-facing**; Mobil частично закрывает **RU overlay** (two-layer RF); Castrol — **окно для official Cyrillic supply** СТМ.

---

## 6. White space для СТМ (MECE · линейка Modern/Tech · 0W-20)

| Блок | Gap на полке (0W-20) | Действие СТМ |
|------|----------------------|--------------|
| **A. Claims architecture** | API SP / GF-6A / ACEA C5 **off-front** у tier-1 import | **Readable API+ACEA+top OEM band** на фронте 5L и 1L |
| **B. Hybrid / OEM story** | Mobil: GM-only front; Castrol: hybrid strong but OEM back-only | **Multi-OEM front row** (GEELY/Toyota/Honda proxy per DR-B) + **one hybrid spec badge** with lab proof |
| **C. Format fairness** | Mobil 1L DRY-rescale ↓ institutional delivery; Castrol 1L ↑ HYSPEC but back gap | Отдельный **1L brief**: hero SAE + OEM @120px + whitespace; **5L service jug** per RBS (5,6 L fill) |
| **D. Visual paradigm** | Lattice vs gold hyperbole — оба solid | **Fluid-precision / smart-flat** — не lattice, не trophy gold |
| **E. Trust & supply** | Parallel import (Mobil); EU pack (Castrol); weak on-pack anti-fraud | **Official RF supply** + verified QR/TDS parity (pack = web) |
| **F. Language** | EN-dominant + sticker layer | **Integrated Cyrillic** native wrap (не EN+overlay) |

---

## 7. Риски / lacunae (не видно на фото / не аудировано)

| ID | Lacuna | Затронутые строки | Severity |
|----|--------|-------------------|----------|
| LAC-0W01 | Castrol **1L back label н/д** — ODSA provisional | R4 | GAP-CED-01 · **M** |
| LAC-0W02 | Mobil 1L **back label н/д** — ODSA provisional | R2 | GAP-M1D-01 · **M** |
| LAC-0W03 | Castrol **API SP / GF-6A** below fold on back — не верифицирован zoom | R3 | LAC02 · **M** |
| LAC-0W04 | Castrol **RU overlay** — н/д на EU photo | R3,R4 | LAC04 · **M** |
| LAC-0W05 | Retail shelf **@1.2 m** — не измерено (premium pair) | all | MAP5 · **L** |
| LAC-0W06 | Mobil 1L **overlay on 1L photo** — line attestation only | R2 | F-M1D · **M** |
| LAC-0W07 | Castrol **QR asymmetry** 1L front vs 5L front lacuna | R3,R4 | δ24 issue · **L** |
| LAC-0W08 | **СТМ target 5L+1L** vs competitor 5L+1L — нет 4L row in matrix (by design) | scope | RBS doc.10 · **info** |

---

## 8. Реестр источников

| Wiki ID | Артефакт |
|---------|----------|
| [19](../Cursor/wiki/19_PGMM_mobil_1_0w_20_5L.md) | PGMM full Mobil 1 0W-20 5L |
| [20](../Cursor/wiki/20_PGMM_mobil_1_0w_20_1L_delta.md) | PGMM delta Mobil 1 0W-20 1L |
| [21](../Cursor/wiki/21_ODSA_mobil_1_0w_20_5L.md) | ODSA Mobil 1 0W-20 5L · rev.2 locked |
| [22](../Cursor/wiki/22_ODSA_mobil_1_0w_20_1L.md) | ODSA Mobil 1 0W-20 1L · rev.2 provisional |
| [23](../Cursor/wiki/23_PGMM_castrol_edge_0w_20_v_5L.md) | PGMM full Castrol EDGE 0W-20 V 5L |
| [24](../Cursor/wiki/24_PGMM_castrol_edge_0w_20_v_1L_delta.md) | PGMM delta Castrol EDGE 0W-20 V 1L |
| [25](../Cursor/wiki/25_ODSA_castrol_edge_0w_20_v_5L.md) | ODSA Castrol EDGE 0W-20 V 5L · rev.1 locked |
| [26](../Cursor/wiki/26_ODSA_castrol_edge_0w_20_v_1L.md) | ODSA Castrol EDGE 0W-20 V 1L · rev.1 provisional |

**Cross-ref mass-mid:** [`матрица_PGMM_ODSA_5W-40.md`](матрица_PGMM_ODSA_5W-40.md) · wiki [10–18](../Cursor/wiki/)

**DoD этапа 4 (0W-20 matrix):** ✅ 4×18 complete · pending: Mobil 1L back · Castrol 1L back · API below fold zoom · retail @1.2m

---

*Сборка: transpose wiki/21–22, 25–26 canonical rows + PGMM 19–20, 23–24 · rev.2 · 25.06.2026*
