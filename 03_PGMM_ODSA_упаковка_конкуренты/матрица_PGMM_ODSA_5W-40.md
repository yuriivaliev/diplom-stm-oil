# Сравнительная матрица PGMM + ODSA — 5W-40 (mass-mid synthetic)

**Этап:** 4 · **Регион:** европейская часть РФ (витрина retail)  
**Дата сборки:** 25.06.2026 · **Rev.** 2  
**Правило строк:** **1 format = 1 row** · 6 строк = 3 бренда × (4L + 1L)  
**Источники:** wiki PGMM [10–15](../Cursor/wiki/) · ODSA 4L [16–18](../Cursor/wiki/) · ODSA 1L [27–29](../Cursor/wiki/) · schema [`ODSA_matrix_row_шаблон.md`](ODSA_matrix_row_шаблон.md)

---

## 0. Scope и ограничения

| Поле | Значение |
|------|----------|
| SAE | **5W-40** only |
| Сегмент | Mass-mid synthetic (не 0W-20 premium) |
| ODSA 4L | Full audit · wiki/16–18 · locked |
| ODSA 1L | LUKOIL [27](../Cursor/wiki/27_ODSA_LUKOIL_LUXE_5W-40_1L.md) ✅ · GPN [28](../Cursor/wiki/28_ODSA_Gazpromneft_Premium_N_5W-40_1L.md) 🟡 · Mobil [29](../Cursor/wiki/29_ODSA_mobil_super_3000_x1_5w_40_1L.md) 🟡 |
| PGMM wiki/10 | **Stale** (legacy SL/semi) — канон claims: ODSA/16 (LUXE SYNTHETIC SN/CF) |
| ODSA schema | **18 строк** canonical (§1–15 claims + §16–18 PGMM delta §6) |

---

## 1. Индекс строк (6 SKU)

| Row | Бренд | Формат | PGMM | ODSA | Ключевой риск |
|-----|-------|--------|------|------|---------------|
| R1 | LUKOIL LUXE | **4L** | [10](../Cursor/wiki/10_PGMM_LUKOIL_LUXE_5W-40.md) | [16](../Cursor/wiki/16_ODSA_LUKOIL_LUXE_5W-40_4L.md) | Legacy SL facings · OEM back-only |
| R2 | LUKOIL LUXE | **1L** | [14](../Cursor/wiki/14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md) | [27](../Cursor/wiki/27_ODSA_LUKOIL_LUXE_5W-40_1L.md) ✅ | API/1L thumbnail fail · back inherit |
| R3 | Gazpromneft Premium N | **4L** | [11](../Cursor/wiki/11_PGMM_Gazpromneft_Premium_N_5W-40.md) | [17](../Cursor/wiki/17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) ✅ | OEM microtype · site superset |
| R4 | Gazpromneft Premium N | **1L** | [15](../Cursor/wiki/15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md) | [28](../Cursor/wiki/28_ODSA_Gazpromneft_Premium_N_5W-40_1L.md) 🟡 | MB **229.5↔229.3** split-face · back ⊂ GPN-01 |
| R5 | Mobil Super 3000 x1 | **4L** | [12](../Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md) | [18](../Cursor/wiki/18_ODSA_mobil_super_3000_x1_5w_40_4L.md) ✅ | API off front · parallel import |
| R6 | Mobil Super 3000 x1 | **1L** | [13](../Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md) | [29](../Cursor/wiki/29_ODSA_mobil_super_3000_x1_5w_40_1L.md) 🟡 | Benefit-icons absent · QR line-info (819697D) |

---

## 2. Блок PGMM (6 строк)

| Row | M_SYSTEM | DOMAIN Source → Target | Ключевая метафора | Лакуны (LACUNA) | EVAL (1 строка) | Импликация для СТМ |
|-----|----------|------------------------|-------------------|-----------------|-----------------|---------------------|
| **R1** LUXE 4L | industrial_hyper_armor + epistemic_void | A: броня/карбон/золото/телеметрия → B: трибология (вытеснена) | Жидкость = металл; щит + золото | Fluid/eco; ActiPure legacy; OEM front | Fidelity **2/10** · rhetoric **9/10** · usability **8/10** (wiki/10;16) | Open engineering + OEM band на фронт; version label при reformulation |
| **R2** LUXE 1L | **= R1** | = R1 | Щит **↑%**; карбон→соты | ActiPure MAP оборван; grip latent | Primary VP OK; secondary ↓; thumb API/1L **fail** (δ14) | Top-up: явный API + 1L + one tech-proof; не DRY без rescale |
| **R3** GPN 4L | cognitive_amortization + institutional_anxiety | A: термокинетика/гегемония → B: HC-synth (скрыт) | 5W-40 heuristic + 3D-swirl; «чёрный ящик» | Engineering in footer; Noack/TBN; fluid | Transaction **high** · transparency **~0** (wiki/11) | Whitespace + manifest OEM; не копировать «пустоту» |
| **R4** GPN 1L | **= R3** | = R3 | Claustrophobic **↑** | OEM/API footer **functionally dead** (δ15) | Top-up **8/10** · overall **6/10** | 1L: крупный 1L + center OEM + breathing zone |
| **R5** Mobil 4L | techno_vital_armor | A: плазменная броня → B: трибология (невидима) | Плазма в кольце-экзоскелете | Eco; fluid; digital; silence | Shannon **optimal** · fidelity **low** · anxiety relief **high** | Native RU + front API/OEM + official supply |
| **R6** Mobil 1L | **= R5** | = R5 | Кольцо cropped; QR **819697D** | Benefit-icons **absent** (mocc_028); bimodal density | Overall **7/10** · top-up **9/10** · robustness **medium** | Clean 1L + explicit QR MAP + icons retained |

---

## 3.0. ODSA transpose — 4L only (18 строк × 3 бренда)

> **Источник:** прямой transpose canonical tables wiki/16, /17, /18 · rev. locked

| # | Параметр | LUKOIL LUXE 4L (R1) | GPN Premium N 4L (R3) | Mobil Super 3000 x1 4L (R5) |
|---|----------|---------------------|------------------------|----------------------------|
| 1 | M_SYSTEM | industrial_hyper_armor + epistemic_void · **H** | cognitive_amortization + institutional_anxiety · **H** | techno_vital_armor · **H** |
| 2 | Carrier morphology | Асимметричная + ручка · **H** | Широкая + ручка · **H** | «Торс» + рёбра · **H** |
| 3 | Класс (синт/полусинт) | **Syn SN/CF** · **H** | **Syn SN/CF** · **H** | **Syn** EN + RU overlay · **H/M** |
| 4 | SAE 5W-40 legibility | **High** · **H** | **High** hyperbolized · **H** | **High** gold badge · **H** |
| 5 | API (front / back) | **SN/CF · SN/CF** · **H** | **SN/CF · SN/CF** · **H** | **— / SJ–SN+CF** (+overlay CF–SP) · **H** |
| 6 | ACEA (front / back) | Front **—** · back A3/B4,B3 · **H** | **A3/B4 · A3/B4** (+B3 site) · **H** | **A3/B4 · +A3/B3** · **H** |
| 7 | OEM front (effective) | **Нет** · **H** | **Microtype** · **H** | **Нет** · **H** |
| 8 | OEM back / site / overlay | Full stack back+site · **H** | Back + **site superset** · **H/M** | Base back + **overlay superset** · **M** |
| 9 | Benefit-icons | Min; ActiPure legacy · **M** | Low swirls · **M** | Moderate 4L · **M** |
| 10 | Cross-face consistency | **Pass** current · **H** | **Pass** · **H** | **Partial** + overlay · **H** |
| 11 | Digital / overlay gap | Site ≈ pack · **H** | **Site superset** · **M** | **Overlay superset** · **M** |
| 12 | Anti-fraud UX | **—** · **H** | **3662.ru** + site · **H** | **None** · **H** |
| 13 | RF supply & язык | Official integrated RU · **H** | Official integrated · **H** | Parallel import EN+TR+RU sticker · **H** |
| 14 | Маркировка РФ | ISO/IATF; EAC **verify** · **M** | EAC+штамп · **H** | Overlay attestation · **M** |
| 15 | Кириллица vs латиница | RU dominant + LUXE EN · **H** | RU dominant · **H** | EN base; RU overlay · **M** |
| 16 | Thumbnail ~120px | **High** · **H** | Med-high · **M** | **High** · **H** |
| 17 | Cognitive load / space | High uniform · **H** | High claustrophobic · **H** | High dense 100% · **H** |
| 18 | Legacy / rev. risk | **Major** SL/semi facings · **M** | **Low** stable wrap · **H** | **Low** since 2022 · **H** |

---

## 3. Блок ODSA — canonical 18 параметров (6 строк · full matrix)

**Легенда Confidence:** H / M / L · **1L:** wiki/27–29

| # | Параметр | R1 LUXE 4L | R2 LUXE 1L | R3 GPN 4L | R4 GPN 1L | R5 Mobil 4L | R6 Mobil 1L |
|---|----------|------------|------------|-----------|-----------|-------------|-------------|
| 1 | M_SYSTEM | industrial_hyper_armor + epistemic_void · **H** · 16 | = R1 · **H** · 27 | cognitive_amortization + institutional_anxiety · **H** · 17 | = R3 · **H** · 28 | techno_vital_armor · **H** · 18 | = R5 · **H** · 29 |
| 2 | Carrier morphology | Асимметричная + ручка · **H** | Узкая + shoulder grip · **H** · 27 | Широкая + ручка · **H** | Узкая + diagonal grip · **H** · 28 | «Торс» + рёбра · **H** | Узкая + grip-ridges · **H** · 29 |
| 3 | Класс (синт/полусинт) | **Syn SN/CF** · **H** | **Syn SN/CF** · **H** · 27 | **Syn SN/CF** · **H** | **Syn SN/CF** · **H** · 28 | **Syn** EN+overlay · **H/M** | **Syn** EN front · **H/M** · 29 |
| 4 | SAE 5W-40 legibility | **High** · **H** | **High** rel.↑ · **H** · 27 | **High** · **H** | **High** · **H** · 28 | **High** · **H** | **High** · **H** · 29 |
| 5 | API (front / back) | **SN/CF · SN/CF** · **H** | **SN/CF · SN/CF** inherit · **H** · 27 | **SN/CF · SN/CF** · **H** | **SN/CF · SN/CF** inherit · **H/M** · 28 | **— / SJ–SN+CF** · **H** | **— / inherit** · **H/M** · 29 |
| 6 | ACEA (front / back) | Front **—** · back A3/B4,B3 · **H** | Front **—** · inherit · **H** · 27 | **A3/B4 · A3/B4** · **H** | **A3/B4 · A3/B4** · **H/M** · 28 | **A3/B4 · +A3/B3** · **H** | Front A3/B4 · inherit · **H/M** · 29 |
| 7 | OEM front (effective) | **Нет** · **H** | **Нет** · **H** · 27 | **Microtype** · **H** | **Microtype** ⊃4L · **H** · 28 | **Нет** · **H** | **Нет** · **H** · 29 |
| 8 | OEM back / site / overlay | Full stack · **H** | Inherit L04 · **H** · 27 | Back + site superset · **H/M** | Inherit; MB 229.5 front · **M** · 28 | Overlay superset · **M** | Inherit · **M** · 29 |
| 9 | Benefit-icons | Min; ActiPure legacy · **M** | Car pictogram only · **H** · 27 | Low swirls · **M** | Low + car · **M** · 28 | Moderate · **M** | **Absent** · **H** · 29 |
| 10 | Cross-face consistency | **Pass** · **H** | **Pass** inherit · **H** · 27 | **Pass** · **H** | **Partial** 229.5↔229.3 · **M** · 28 | **Partial** overlay · **H** | **Partial** inherit · **M** · 29 |
| 11 | Digital / overlay gap | Site ≈ pack · **H** | Inherit · **H** · 27 | Site superset · **M** | Back ⊂ **GPN-01** (6 gaps) · **M** · 28 | Overlay superset · **M** | QR 819697D; URL **verify** · **M** · 29 |
| 12 | Anti-fraud UX | **—** · **H** | **—** · **H** · 27 | **3662.ru** · **H** | 3662 inherit · **M** · 28 | **None** · **H** | **None** (QR≠AF) · **H** · 29 |
| 13 | RF supply & язык | Official RU · **H** | Official · **H** · 27 | Official · **H** | Official · **H** · 28 | Parallel import · **H** | Parallel+overlay · **H/M** · 29 |
| 14 | Маркировка РФ | ISO/IATF; EAC **verify** · **M** | Inherit; EAC **verify** · **M** · 27 | EAC+штамп · **H** | EAC inherit; 1L stamp · **M** · 28 | Overlay attestation · **M** | Overlay inherit; back **n/d** · **L** · 29 |
| 15 | Кириллица vs латиница | RU dominant · **H** | Cyrillic ↑ · **H** · 27 | RU dominant · **H** | RU dominant · **H** · 28 | EN+overlay · **M** | EN+overlay · **M** · 29 |
| 16 | Thumbnail ~120px | **High** · **H** | Med-high; API/1L fail · **H** · 27 | Med-high · **M** | **Medium** · **H** · 28 | **High** · **H** | **Medium** · **H** · 29 |
| 17 | Cognitive load / space | High uniform · **H** | High uniform ↑ · **H** · 27 | Claustrophobic · **H** | High uniform · **H** · 28 | Dense 100% · **H** | **Bimodal** · **H** · 29 |
| 18 | Legacy / rev. risk | **Major** SL/semi · **M** | = R1 line · **M** · 27 | **Low** stable · **H** | MB 229.5 vs 229.3 · **M** · 28 | **Low** · **H** | = R5 · **H** · 29 |

---

## 4. Сводка 4L-only (cross-brand · этапы 5–6)

| Параметр | LUXE 4L | GPN 4L | Mobil 4L |
|----------|---------|--------|----------|
| API front | SN/CF | SN/CF | **—** |
| OEM front effective | No | Microtype | No |
| RF supply | Official | Official | **Parallel import** |
| Anti-fraud | — | **3662.ru** | None |
| Cross-face | Pass (current) | Pass | Partial (+overlay) |
| Digital gap | None | Site superset | Overlay superset |
| PGMM paradigm | Solid/Armor | Obscuration/Density | Plasma/Armor |
| Top STM gap | OEM front + versioning | Readable OEM + channel parity | Native RU + API front + official channel |

---

## 5. Паттерны рынка (mass-mid 5W-40)

1. **Solid > Fluid:** все три бренда вытесняют трибологию метафорами брони, металла или термокинетики — категорийная норма.
2. **Heuristic compression:** SAE **5W-40** — главный shelf-anchor; OEM/API системно **не на фронте** (LUKOIL, Mobil) или **нечитаемо** (GPN microtype).
3. **Channel asymmetry:** GPN **site superset**; Mobil **RU overlay superset** vs photographed base — pack ≠ digital channel.
4. **1L ≠ 4L:** secondary claims (OEM detail, icons, institutional footer) **деградируют** при DRY rescale — отдельный 1L brief обязателен.
5. **Trust stack:** anti-fraud UX только у GPN (3662); white space для СТМ при **official supply**.

---

## 6. White space для СТМ (MECE · Classic/Protect 5W-40)

| Блок | Gap на полке | Действие СТМ |
|------|--------------|--------------|
| **A. Claims architecture** | API/OEM off-front или microtype | **Readable OEM band** + API SN/CF на фронте 4L и 1L |
| **B. Channel integrity** | Site/overlay superset vs pack; GPN back ⊂ GPN-01 | Pack claims = web/TDS (**GPN-01 parity**) или verified QR |
| **C. Format fairness** | 1L теряет secondary layer | Отдельный 1L brief: крупный 1L, center OEM, min. one icon |
| **D. Visual paradigm** | Claustrophobic density vs armor (all) | **Whitespace + fluid/hydro** OR **smart-flat** — не копировать броню |
| **E. Trust & supply** | Mobil parallel; LUKOIL legacy facings | Official RF + proof layer + **version label** при reformulation |
| **F. Language** | Mobil EN+overlay | **Integrated Cyrillic** native wrap |

---

## 7. Риски / lacunae (не видно на фото / не аудировано)

| ID | Lacuna | Строки | Severity |
|----|--------|--------|----------|
| LAC-01 | GPN/Mobil 1L ODSA **provisional** (back photo optional) | R4,R6 | Method · **M** |
| LAC-02 | LUKOIL **legacy SL/semi** facings — доля на полке н/д | R1,R2 | F-L10 · **M** |
| LAC-03 | PGMM wiki/10 **stale** — refresh on EVID-L10 | R1 | **M** |
| LAC-04 | Retail shelf **@1.2 m** — не измерено | all | **L** |
| LAC-05 | Mobil **RU overlay** — attestation без фото на 4L | R5,R6 | F-M04 · **M** |
| LAC-06 | GPN back **⊂ GPN-01** — 6 OEM/ACEA gaps vs «Ключевые характеристики» | R3,R4 | F-G11 · **M** |
| LAC-07 | LUKOIL 1L back **фото** — EAC/штамп verify optional | R2 | **L** |
| LAC-08 | EAC/штамп LUKOIL 4L — verify full back photo | R1 | **L** |

---

## 8. Реестр источников

### PGMM (wiki 10–15)

| Wiki ID | Артефакт |
|---------|----------|
| [10](../Cursor/wiki/10_PGMM_LUKOIL_LUXE_5W-40.md) | PGMM full LUKOIL 4L |
| [11](../Cursor/wiki/11_PGMM_Gazpromneft_Premium_N_5W-40.md) | PGMM full GPN 4L |
| [12](../Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md) | PGMM full Mobil 4L |
| [13](../Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md) | PGMM delta Mobil 1L |
| [14](../Cursor/wiki/14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md) | PGMM delta LUKOIL 1L |
| [15](../Cursor/wiki/15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md) | PGMM delta GPN 1L |

### ODSA

| Wiki ID | Артефакт |
|---------|----------|
| [16](../Cursor/wiki/16_ODSA_LUKOIL_LUXE_5W-40_4L.md) | ODSA LUKOIL 4L ✅ rev.3 |
| [17](../Cursor/wiki/17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) | ODSA GPN 4L ✅ locked |
| [18](../Cursor/wiki/18_ODSA_mobil_super_3000_x1_5w_40_4L.md) | ODSA Mobil 4L ✅ locked |
| [27](../Cursor/wiki/27_ODSA_LUKOIL_LUXE_5W-40_1L.md) | ODSA LUKOIL 1L ✅ locked |
| [28](../Cursor/wiki/28_ODSA_Gazpromneft_Premium_N_5W-40_1L.md) | ODSA GPN 1L 🟡 provisional |
| [29](../Cursor/wiki/29_ODSA_mobil_super_3000_x1_5w_40_1L.md) | ODSA Mobil 1L 🟡 provisional |

**DoD этапа 4 (5W-40 matrix):** ✅ rev.2 · transpose §3.0 + matrix §3 · pending: PGMM/10 refresh · retail @1.2m · GPN/Mobil 1L back photo

---

*Сборка: transpose wiki/16–18 (4L) + wiki/27–29 (1L) + PGMM 10–15 · протокол C rev.2*
