# Сравнительная матрица PGMM + ODSA — 10W-40 (budget / legacy semi)

**Этап:** 4 · **Регион:** европейская часть РФ (retail + ЮФО proxy)  
**Дата сборки:** 25.06.2026 · **Rev.** 1  
**Правило строк:** **1 format = 1 row** · 6 строк = 3 бренда × (4L + 1L)  
**Источники:** wiki PGMM [42–43, 46–47, 50–51](../Cursor/wiki/) · ODSA 4L [44, 48, 52](../Cursor/wiki/) · ODSA 1L [45, 49, 53](../Cursor/wiki/) · schema [`ODSA_matrix_row_шаблон.md`](ODSA_matrix_row_шаблон.md)

---

## 0. Scope и ограничения

| Поле | Значение |
|------|----------|
| SAE | **10W-40** only |
| Сегмент | Budget / legacy **semi-synthetic** (Classic/Protect · Волна 3 · ЮФО proxy) |
| ODSA 4L | Full audit · wiki/44, 48, 52 · ✅ locked |
| ODSA 1L | wiki/45, 49, 53 · ✅ locked (photo) |
| PGMM | Full 4L [42, 46, 50] · delta 1L [43, 47, 51] |
| ODSA schema | **18 строк** canonical (§1–15 claims + §16–18 PGMM delta §6) |
| Канон vs фото | API **SG/CD** (RU peers) vs **SN+ back** (Mobil) — **artifact=canonical** на фото; site verify **pending** (GPN-03, GAP-MS2-01) |

**Не смешивать** с матрицами **5W-40** mass-mid synthetic · **0W-20** premium · **5W-30** ref.

---

## 1. Индекс строк (6 SKU)

| Row | Бренд | Формат | PGMM | ODSA | Ключевой риск |
|-----|-------|--------|------|------|---------------|
| R1 | LUKOIL SUPER | **4L** | [42](../Cursor/wiki/42_PGMM_LUKOIL_SUPER_10W-40.md) | [44](../Cursor/wiki/44_ODSA_LUKOIL_SUPER_10W-40_4L.md) ✅ | OEM back-only · ActiPure void · SUPER vs SG |
| R2 | LUKOIL SUPER | **1L** | [43](../Cursor/wiki/43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md) | [45](../Cursor/wiki/45_ODSA_LUKOIL_SUPER_10W-40_1L.md) ✅ | OEM front lacuna ↑ doliv · mesh crop · ActiPure micro |
| R3 | Gazpromneft Super | **4L** | [46](../Cursor/wiki/46_PGMM_Gazpromneft_Super_10W-40.md) | [48](../Cursor/wiki/48_ODSA_Gazpromneft_Super_10W-40_4L.md) ✅ | ZMZ front/back split · GPN-03 pending · batch 2020 |
| R4 | Gazpromneft Super | **1L** | [47](../Cursor/wiki/47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md) | [49](../Cursor/wiki/49_ODSA_Gazpromneft_Super_10W-40_1L.md) ✅ | Scratch lacuna 1L · oil-level strip lost · ZMZ split inherit |
| R5 | Mobil Super 2000 x1 | **4L** | [50](../Cursor/wiki/50_PGMM_mobil_super_2000_x1_10w_40.md) | [52](../Cursor/wiki/52_ODSA_mobil_super_2000_x1_10w_40_4L.md) ✅ | API off-front · import EN/TR · no EAC |
| R6 | Mobil Super 2000 x1 | **1L** | [51](../Cursor/wiki/51_PGMM_mobil_super_2000_x1_10w_40_1L_delta.md) | [53](../Cursor/wiki/53_ODSA_mobil_super_2000_x1_10w_40_1L.md) ✅ | MB 229.1 lacuna vs 4L · doliv gap vs RU peers front API |

---

## 2. Блок PGMM (6 строк)

| Row | M_SYSTEM | DOMAIN Source → Target | Ключевая метафора | Лакуны (LACUNA) | EVAL (1 строка) | Импликация для СТМ |
|-----|----------|------------------------|-------------------|-----------------|-----------------|---------------------|
| **R1** SUPER 4L | universal_mass_heuristic + honeycomb_armor_lite + actipure_black_box + domestic_oem_sovereignty | A: mesh/superlative/universal/car-icon → B: semi 10W-40 · API SG/CD · Avtovaz-era | SUPER + honeycomb mesh + «УНИВЕРСАЛЬНОЕ» | Fluid/eco; OEM front; ACEA/SN+; ActiPure proof; QR | Rhetoric **7/10** · fidelity **3/10** · transaction **high** · RU **high** (wiki/42) | Readable SAE+API front + **domestic OEM band** (front 2–3) · semi honesty · fluid antidote · no SUPER void |
| **R2** SUPER 1L | **= R1** | = R1 | Mesh **crop**; universal banner **robust** | Service-jug authority lost; OEM front **absent** | Primary VP OK; mesh ↓; thumb **high-medium**; trust ↓ doliv (δ43) | 1L brief: front API + **top-up claim** + one benefit; не DRY без spec front-load |
| **R3** GPN Super 4L | universal_mass_heuristic + thermokinetic_swirl_lite + institutional_anxiety + oem_partial_front | A: SUPER/swirl/GPN hegemony → B: semi 10W-40 · API SG/CD | SUPER + orange swirl-lite + oil-level strip | ACEA; UMZ back; readable OEM @1.2m; fluid; GPN-03 | Transaction **high** · transparency **low-medium** · rhetoric **low** · RU **high** (wiki/46) | Readable OEM front **and** back parity · scratch-equivalent trust · no swirl void |
| **R4** GPN Super 1L | **= R3** | = R3 | Swirl **crop**; OEM microtype **robust @ doliv** | Oil-level strip **absent**; scratch **н/д** photo; STO drift | Primary OK; **↑ vs LUKOIL 1L** on OEM front; service utility ↓ (δ47) | 1L: OEM front row readable + fill gauge + top-up claim |
| **R5** Mobil 2000 4L | down_tier_fluid_kinetics + numeric_line_heuristic_2000 + mobil_brand_transfer + back_loaded_spec_grid | A: gold droplets/2000/x1 → B: semi 10W-40 · API SN+ back | Super/2000 + magenta 10W-40 + gold fluid spray | API/ACEA/OEM front; Cyrillic; RF supply; anti-fraud | Transaction **high** · rhetoric **medium-low** · RU **low** · import trust **medium** (wiki/50) | API+OEM **front** + Cyrillic official · semi honesty · no gold void · no numeric tier ladder |
| **R6** Mobil 2000 1L | **= R5** | = R5 | Gold droplets **truncated**; 10W-40 band **↑%** | API front lacuna **↑ vs R2/R4**; MB **absent vs R5** | Primary brand+SAE OK; spec layer **fail @ doliv**; thumb **medium** (δ51) | **Attack window:** front API row closes gap vs LUKOIL/GPN 1L **and** Mobil deictic pattern |

---

## 3.0. ODSA transpose — 4L only (18 строк × 3 бренда)

> **Источник:** прямой transpose canonical tables wiki/44, /48, /52 · rev. 1 locked

| # | Параметр | LUKOIL SUPER 4L (R1) | GPN Super 4L (R3) | Mobil Super 2000 x1 4L (R5) |
|---|----------|----------------------|-------------------|----------------------------|
| 1 | M_SYSTEM | Universal + armor lite + ActiPure + OEM back · **H** | Universal + swirl lite + scratch anxiety + OEM partial front · **H** | Down-tier fluid kinetics + 2000 heuristic + back spec grid · **H** |
| 2 | Carrier morphology | 4L silver HDPE + handle + red cap · **H** | 4L silver HDPE + handle + **oil-level strip** · **H** | 4L silver HDPE + handle + grip ridges · **H** |
| 3 | Класс (синт/полусинт) | **Semi** · API **SG/CD** · **H** | **Semi** · API **SG/CD** · **H** | **Semi** · API **SN+ back** + CF · **H** |
| 4 | SAE 10W-40 legibility | **High** white/black + back red bar · **H** | **High** oversized orange band · **H** | **High** magenta band · **H** |
| 5 | API (front / back) | **SG/CD · SG/CD** · **H** | **SG/CD · SG/CD** · **H** | **— / SL–SN PLUS + CF** · **H** |
| 6 | ACEA (front / back) | **Absent · Absent** · **H** | **Absent · Absent** · **H** | **— / A3/B3** · **H** |
| 7 | OEM front (effective) | **Нет** · **H** | **AVTOVAZ·ZMZ microtype** · **@1.2m fail** · **H** | **Нет** · **H** |
| 8 | OEM back / site / overlay | **АВТОВАЗ·УМЗ·ЗМЗ** · site ≈ pack · **H** | **АВТОВАЗ** back · **ZMZ/УМЗ absent** · GPN-03 **pending** · **H/L** | **MB·VW·AVTOVAZ** back · site **pending** · **H/L** |
| 9 | Benefit-icons | ActiPure named · site-only proof · **M** | Car + swirl · wear text back · **M** | Gold droplets · Gasoline&Diesel literal · **M** |
| 10 | Cross-face consistency | **Pass** · **H** | **Partial Pass** — ZMZ split · **H** | **Partial Pass** — API deictic · **H** |
| 11 | Digital / overlay gap | Site **≈ pack** · **H** | GPN-03 **pending** · **L** | Site **pending** · **L** |
| 12 | Anti-fraud UX | EAC + barcode + batch · QR **н/д** · **M** | **Scratch code** + EAC + barcode · **H** | **QR only** · no EAC/scratch · **H** |
| 13 | RF supply & язык | Official LLK · Cyrillic · **H** | Official GPN · Cyrillic · **H** | **Parallel import** EN+TR · **H** |
| 14 | Маркировка РФ | EAC · barcode · batch · ISO **verify** · **M** | EAC · barcode · batch · STO · AAI · **H** | **Absent** on import base · **H** |
| 15 | Кириллица vs латиница | Cyrillic dominant · **H** | Cyrillic dominant · **H** | **EN dominant** · no Cyrillic · **H** |
| 16 | Thumbnail ~120px | **High** · ActiPure marginal · **H** | **High** · OEM microtype marginal · **H** | **Medium-high** · API/OEM fail · **H** |
| 17 | Cognitive load / space | Medium front / high back · **H** | Medium front / high back · **H** | Medium front / high back · **H** |
| 18 | Legacy / rev. risk | Stable SG/CD · batch 2022 · **M** | Stable SG/CD · batch **2020** · **M** | SN+ back vs SG peers · batch **2021** · **M** |

---

## 3. Блок ODSA — canonical 18 параметров (6 строк · full matrix)

**Легенда Confidence:** H / M / L

| # | Параметр | R1 SUPER 4L | R2 SUPER 1L | R3 GPN Super 4L | R4 GPN Super 1L | R5 Mobil 2000 4L | R6 Mobil 2000 1L |
|---|----------|-------------|-------------|-----------------|-----------------|------------------|------------------|
| 1 | M_SYSTEM | universal + armor lite + ActiPure + OEM back · **H** · 44 | = R1 · **H** · 45 | universal + swirl lite + scratch + OEM partial · **H** · 48 | = R3 · **H** · 49 | fluid kinetics + 2000 + back grid · **H** · 52 | = R5 · **H** · 53 |
| 2 | Carrier morphology | 4L jug + handle · **H** | Narrow + dimple grip · **H** · 45 | 4L + handle + oil-level strip · **H** | Narrow + grip ridges · **no strip** · **H** · 49 | 4L + grip ridges · **H** | Narrow + grooves · **H** · 53 |
| 3 | Класс (синт/полусинт) | **Semi · SG/CD** · **H** | **Semi · SG/CD** · **H** · 45 | **Semi · SG/CD** · **H** | **Semi · SG/CD** · **H** · 49 | **Semi · SN+ back** · **H** | **Semi · SN+ back** · **H** · 53 |
| 4 | SAE 10W-40 legibility | **High** · **H** | **High** rel.↑ · **H** · 45 | **High** orange band · **H** | **High** · **H** · 49 | **High** magenta · **H** | **High** rel.↑ · **H** · 53 |
| 5 | API (front / back) | **SG/CD · SG/CD** · **H** | **SG/CD · SG/CD** · **H** · 45 | **SG/CD · SG/CD** · **H** | **SG/CD · SG/CD** · **H** · 49 | **— / SN+ + CF** · **H** | **— / SN+ + CF** · **H** · 53 |
| 6 | ACEA (front / back) | **Absent · Absent** · **H** | **Absent · Absent** · **H** · 45 | **Absent · Absent** · **H** | **Absent · Absent** · **H** · 49 | **— / A3/B3** · **H** | **— / A3/B3 + AAE B7** · **H** · 53 |
| 7 | OEM front (effective) | **Нет** · **H** | **Нет** · **H** · 45 | **AVTOVAZ·ZMZ microtype** · **H** | **Microtype robust @ doliv** · **H** · 49 | **Нет** · **H** | **Нет** · **H** · 53 |
| 8 | OEM back / site / overlay | **АВТОВАЗ·УМЗ·ЗМЗ** · **H** | Inherit full stack · **H** · 45 | **АВТОВАЗ** · ZMZ/УМЗ **absent** · GPN-03 **L** · 48 | ZMZ split inherit · **M** · 49 | **MB·VW·AVTOVAZ** · **H/L** | **VW·AVTOVAZ** · **MB absent vs R5** · **M** · 53 |
| 9 | Benefit-icons | ActiPure named · **M** | ActiPure **micro** · **M** · 45 | Car + swirl · **M** | Car + swirl · **M** · 49 | Gold droplets · **M** | Droplets **truncated** · **M** · 53 |
| 10 | Cross-face consistency | **Pass** · **H** | **Pass** · **H** · 45 | **Partial** ZMZ split · **H** | **Partial** inherit · **H** · 49 | **Partial** deictic · **H** | **Partial** · **H** · 53 |
| 11 | Digital / overlay gap | Site ≈ pack · **H** | Inherit · **H** · 45 | GPN-03 **pending** · **L** | GPN-03 **pending** · **L** · 49 | Site **pending** · **L** | Site **pending** · **L** · 53 |
| 12 | Anti-fraud UX | EAC + batch · **M** | EAC + batch · **M** · 45 | **Scratch + EAC** · **H** | Scratch **н/д** 1L photo · **M** · 49 | **QR only** · **H** | **QR only** · **H** · 53 |
| 13 | RF supply & язык | Official · **H** | Official · **H** · 45 | Official · **H** | Official · **H** · 49 | Parallel import · **H** | Parallel · **H** · 53 |
| 14 | Маркировка РФ | EAC · ISO **verify** · **M** | EAC inherit · **M** · 45 | EAC · STO · AAI · **H** | EAC · STO · **H** · 49 | **Absent** import · **H** | **Absent** · **H** · 53 |
| 15 | Кириллица vs латиница | Cyrillic · **H** | Cyrillic · **H** · 45 | Cyrillic · **H** | Cyrillic · **H** · 49 | EN+TR · **H** | EN+TR · **H** · 53 |
| 16 | Thumbnail ~120px | **High** · **H** | High-medium · **H** · 45 | **High** · **H** | High-medium · **H** · 49 | Medium-high · **H** | **Medium** · **H** · 53 |
| 17 | Cognitive load / space | Med front / high back · **H** | **Bimodal** · **H** · 45 | Med front / high back · **H** | Med-high vertical · **H** · 49 | Med front / high back · **H** | **Bimodal** footer · **H** · 53 |
| 18 | Legacy / rev. risk | SG/CD stable · **M** | Batch 07.08.22 · **M** · 45 | Batch **2020** · **M** | Batch **2022** · **M** · 49 | Batch **2021** · **M** | MB cross-format · **M** · 53 |

---

## 4. Сводка 4L-only (cross-brand · этапы 5–6)

| Параметр | LUKOIL SUPER 4L | GPN Super 4L | Mobil 2000 4L |
|----------|-----------------|--------------|---------------|
| API front | **SG/CD** | **SG/CD** | **—** |
| API back tier | SG/CD | SG/CD | **SN+ modern** |
| OEM front | No | **Microtype** (illegible @1.2m) | No |
| OEM back depth | **Full domestic** (AVTOVAZ·UMZ·ZMZ) | **Partial** (AVTOVAZ; ZMZ split) | **Import mix** (MB·VW·AVTOVAZ) |
| RF supply | Official | Official | **Parallel import** |
| Anti-fraud | EAC+batch | **Scratch code** | QR only |
| ACEA | Absent | Absent | A3/B3 back |
| PGMM paradigm | Mesh armor-lite | Swirl-lite | Gold fluid kinetics |
| Top STM gap | OEM **front** band · ActiPure metric | OEM **readable** front+back · GPN-03 | API+OEM **front** · Cyrillic · EAC |

---

## 5. Паттерны рынка (budget 10W-40 · legacy semi)

1. **Semi honesty on front** — все три бренда явно пишут полусинтетику; категорийная норма budget tier.
2. **SAE 10W-40 front heuristic** — сильнее, чем API/OEM: magenta/orange/black band = primary shelf filter (ЮФО / aging fleet proxy).
3. **API SG/CD vs SN+ split** — domestic RU peers **front-load legacy SG/CD**; Mobil **hides modern SN+ on back** — двойной white space (honesty vs modernity).
4. **Solid > Fluid (semi tier)** — mesh (LUKOIL) · swirl (GPN) · gold droplets (Mobil) подавляют fluid tribology; SUPER hyperbole shared.
5. **1L doliv asymmetry** — RU peers сохраняют **API SG/CD front** на 1L; Mobil **усиливает** API lacuna — отдельный attack vector для СТМ Classic/Protect top-up SKU.

---

## 6. White space для СТМ (MECE · Classic/Protect · 10W-40 · Волна 3)

| Блок | Gap на полке | Действие СТМ |
|------|--------------|--------------|
| **A. Claims architecture** | Mobil API off-front; GPN OEM microtype; LUKOIL OEM back-only | **Readable front row:** SAE + API (tier-honest) + 2–3 domestic OEM @1.2 m |
| **B. Chemistry honesty** | SUPER/ActiPure/swirl vs SG tier rhetoric | **Protect** naming — один claim tier; semi label = visual **without** hyperbole inflation |
| **C. Format fairness (1L)** | Service-jug cues lost; Mobil doliv spec fail | Отдельный 1L brief: **1L marker + front API + top-up claim**; не DRY rescale без spec |
| **D. Visual paradigm** | Mesh / swirl / gold void | **One metaphor max** — controlled pour / smart-flat; fluid-precision antidote |
| **E. Trust & supply** | Mobil import · GPN scratch-only · LUKOIL no digital | Official RF + **EAC + verified QR/TDS** parity; institutional layer без копирования scratch clone |
| **F. Domestic vs import OEM** | LUKOIL full back · GPN partial · Mobil import grid | **Full domestic stack readable** (AVTOVAZ·UMZ·ZMZ) if ЮФО segment + optional import OEM row |

---

## 7. Риски / lacunae (не видно на фото / не аудировано)

| ID | Lacuna | Строки | Severity |
|----|--------|--------|----------|
| LAC-10W-01 | **GPN-03** site scrape blocked — digital gap open | R3,R4 | CR-GS-04 · **M** |
| LAC-10W-02 | **GAP-MS2-01** Mobil Super 2000 site card — no EX-ID in wiki/04 | R5,R6 | **M** |
| LAC-10W-03 | **MB 229.1 cross-format** — 4L yes · 1L photo absent | R5 vs R6 | CR-MS2D-01 · **M** |
| LAC-10W-04 | GPN **scratch code** on 1L — photo lacuna | R4 | **M** |
| LAC-10W-05 | GPN **UMZ** absent vs LUKOIL back stack | R3,R4 | F-GS-03 · **M** |
| LAC-10W-06 | Retail shelf **@1.2 m** — OEM microtype not measured | all | **L** |
| LAC-10W-07 | Batch facings **2020–2022** — 2025/26 shelf share н/д | all | **M** |
| LAC-10W-08 | LUKOIL ISO/IATF in legal wall — **verify** full back | R1,R2 | GAP-LS-01 · **L** |

---

## 8. Реестр источников

### PGMM (wiki 42–43, 46–47, 50–51)

| Wiki ID | Артефакт |
|---------|----------|
| [42](../Cursor/wiki/42_PGMM_LUKOIL_SUPER_10W-40.md) | PGMM full LUKOIL SUPER 4L |
| [43](../Cursor/wiki/43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md) | PGMM delta LUKOIL SUPER 1L |
| [46](../Cursor/wiki/46_PGMM_Gazpromneft_Super_10W-40.md) | PGMM full GPN Super 4L |
| [47](../Cursor/wiki/47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md) | PGMM delta GPN Super 1L |
| [50](../Cursor/wiki/50_PGMM_mobil_super_2000_x1_10w_40.md) | PGMM full Mobil Super 2000 4L |
| [51](../Cursor/wiki/51_PGMM_mobil_super_2000_x1_10w_40_1L_delta.md) | PGMM delta Mobil Super 2000 1L |

### ODSA (wiki 44–45, 48–49, 52–53)

| Wiki ID | Артефакт |
|---------|----------|
| [44](../Cursor/wiki/44_ODSA_LUKOIL_SUPER_10W-40_4L.md) | ODSA LUKOIL SUPER 4L ✅ locked |
| [45](../Cursor/wiki/45_ODSA_LUKOIL_SUPER_10W-40_1L.md) | ODSA LUKOIL SUPER 1L ✅ locked |
| [48](../Cursor/wiki/48_ODSA_Gazpromneft_Super_10W-40_4L.md) | ODSA GPN Super 4L ✅ locked |
| [49](../Cursor/wiki/49_ODSA_Gazpromneft_Super_10W-40_1L.md) | ODSA GPN Super 1L ✅ locked |
| [52](../Cursor/wiki/52_ODSA_mobil_super_2000_x1_10w_40_4L.md) | ODSA Mobil Super 2000 4L ✅ locked |
| [53](../Cursor/wiki/53_ODSA_mobil_super_2000_x1_10w_40_1L.md) | ODSA Mobil Super 2000 1L ✅ locked |

**DoD этапа 4 (10W-40 matrix):** ✅ rev.1 · transpose §3.0 + matrix §3 · pending: GPN-03 · Mobil site · MB cross-format verify · retail @1.2m

---

*Сборка: transpose wiki/44, 48, 52 (4L) + wiki/45, 49, 53 (1L) + PGMM 42–43, 46–47, 50–51 · протокол C · Classic/Protect Волна 3*
