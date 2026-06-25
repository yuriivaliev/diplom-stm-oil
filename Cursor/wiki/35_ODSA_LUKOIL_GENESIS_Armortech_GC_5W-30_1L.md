# ODSA — LUKOIL GENESIS ARMORTECH GC 5W-30 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_LUKOIL_GENESIS_ARMORTECH_GC_5W30_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md](31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md) · base 4L ODSA: [34_…](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md)  
**Дата:** 25.06.2026 · **Rev. 1:** locked (front + **back photo** + site)  
**Формат:** 1L · official RF wrap · фронт + оборот (фото) + site LLK-01

> **Отличие от LUXE 1L:** back **не inherit** — фото оборота 1L **привязано** (EVID-LG1D-05–09).

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **LUKOIL GENESIS ARMORTECH GC 5W-30 1L** — front claims = 4L delta **1L**; back **фото-подтверждён** (не line inherit).

**Cross-face 1L:** **Pass** — API SN/CF + ACEA C3 front = back photo.

**Cross-format (1L ↔ 4L):** **Pass** primary claims; OEM stack **идентичен** (229.51/229.31 — **не** 229.52 на данном batch).

**Doliv-channel gap:** OEM **back-only** **усилен** vs 4L — impulse top-up без front OEM (F-LG1D-02).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 3 |
| Minor | 1 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-LG1D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L |
| ART-LG1D-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 1L |
| ART-LG1D-003 | Document | wiki/31 | PGMM delta 1L |
| ART-LG1D-004 | Document | wiki/34 | ODSA 4L — cross-format ref |
| ART-LG1D-005 | Web | [LLK-01](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-genesis-armortech-gc-5w-30) | Line specs (shared card) |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-LG1D-01 | Artifact | ART-LG1D-001 | «FOR GERMAN CARS»; GENESIS; ARMORTECH; «FULLY SYNTHETIC ENGINE OIL»; DuraMax® | A | Active |
| EVID-LG1D-02 | Artifact | ART-LG1D-001 | Front: **5W-30 · API SN/CF · ACEA C3 · 1L · GC** | A | Active |
| EVID-LG1D-03 | Artifact | ART-LG1D-001 | **OEM на фронте не видны** | A | Active |
| EVID-LG1D-04 | Artifact | ART-LG1D-001 | Dimple grip shoulder; narrow top-up profile | A | Active |
| EVID-LG1D-05 | Artifact | ART-LG1D-002 | Back header: API SN/CF · ACEA C3 | A | Active |
| EVID-LG1D-06 | Artifact | ART-LG1D-002 | OEM: **Porsche C30 · BMW LL-04 · MB 229.31/229.51 · VW 504/507 · Fiat 9.55535-S3** | A | Active |
| EVID-LG1D-07 | Artifact | ART-LG1D-002 | RU Mid-SAPS + DPF/TWC; LLK-International; ISO/IATF | A | Active |
| EVID-LG1D-08 | Artifact | ART-LG1D-002 | QR; barcode **4 670027 147048**; EAC; **1L** icon | A | Active |
| EVID-LG1D-09 | Artifact | ART-LG1D-002 | Stamp: **14.02.23 · 1136 2 (A) · 23 02280422** | A | Active |
| EVID-LG1D-10 | Web | ART-LG1D-005 | Line specs = EVID-LG1D-06 | A | Active |
| EVID-LG1D-11 | Context | ART-LG1D-003 | PGMM: vertical rescale 4L asset; carbon crop | B | Context |
| EVID-LG1D-12 | Cross-format | ART-LG1D-004 · [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) | 4L front/back ref EVID-LG-02–04 | B | Active |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-LG1D-01 Site card: 1L vs 4L SKU split | Open — одна line card LLK-01 |
| GAP-LG1D-02 DuraMax readable @ arm's length on 1L | Open — micro-text (PGMM delta) |
| GAP-LG1D-03 MB 229.52 on other 1L batches | Open — **not on EVID-LG1D-06** |

---

## Findings Catalogue

### F-LG1D-01 — Positive · Cross-face Pass (photo-backed, not inherit)

| Evidence IDs | EVID-LG1D-02; LG1D-05; LG1D-06; LG1D-10 |
| **Severity** | **Positive** · **High** |

---

### F-LG1D-02 — Major · OEM back-only — doliv impulse gap

| Поле | Значение |
|------|----------|
| **Observation** | Top-up 1L: front сохраняет segment banner, **без** OEM row; back grid (EVID-LG1D-06) **не виден** при полочном выборе doliv. |
| **Evidence IDs** | EVID-LG1D-03; LG1D-06 |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | quick: 2 OEM icons на front 1L; structural: «doliv-safe C3» semantic |

---

### F-LG1D-03 — Positive · Front standards robust on 1L (vs import 1L norm)

| Evidence IDs | EVID-LG1D-02; cross-ref [29](29_ODSA_mobil_super_3000_x1_5w_40_1L.md) |
| **Observation** | API SN/CF + ACEA C3 **readable** on 1L front after rescale — сильнее import norm; amplifies OEM lacuna (F-LG1D-02) |
| **Severity** | **Positive** · **High** |

---

### F-LG1D-04 — ~~Moderate~~ **Closed** · MB 229.52 drift (PGMM delta hypothesis)

| Поле | Значение |
|------|----------|
| **Observation** | PGMM/31 гипотеза «+229.52 on 1L back». Фото EVID-LG1D-06: **229.31/229.51** — **same as 4L** (EVID-LG-04). |
| **Evidence IDs** | EVID-LG1D-06; [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) EVID-LG-04 |
| **Severity (rev. 1)** | **Closed** · Confidence **High** |
| **Note** | Другие batch rev. могут отличаться — retail audit **open** (GAP-LG1D-03) |

---

### F-LG1D-05 — Moderate · DuraMax® micro-text degradation on 1L

| Evidence IDs | EVID-LG1D-01; LG1D-11 |
| **Severity** | **Moderate** · **Medium** |

---

### F-LG1D-06 — Moderate · No top-up rationale on 1L face

| Evidence IDs | EVID-LG1D-02; LG1D-04 |
| **Observation** | «FOR GERMAN CARS» service rhetoric без «doliv / exact fill» claim |
| **Severity** | **Moderate** · **Medium** |

---

### F-LG1D-07 — Positive · Cross-format claims Pass (1L ↔ 4L)

| Evidence IDs | EVID-LG1D-02; LG1D-06; LG1D-12 |
| **Severity** | **Positive** · **High** |

---

### F-LG1D-08 — Minor · Batch 2023 vs 4L batch 2022

| Evidence IDs | EVID-LG1D-09; [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) EVID-LG-07 |
| **Observation** | Разные production dates — **не split-face**; единый wrap rev. по claims |
| **Severity** | **Minor** · **Medium** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-LG1D-01 | OEM front vs back | **Open** — F-LG1D-02 |
| CR-LG1D-02 | MB 229.52 (PGMM/31) vs photo 229.31/51 | **Closed** — F-LG1D-04 |
| CR-LG1D-03 | Service-jug rhetoric vs 1L top-up | **Open** — PGMM delta conflict |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — OEM front on doliv; DuraMax proof. **Redundancy** — armor triple-code **без ослабления** при rescale.

**Logical Coherence:** Cross-face **Pass**; cross-format OEM **Pass**.

**System Dynamics:** **Potential** — official RU 1L with front C3; **Limit** — back-loaded OEM on impulse channel.

**Relational States:** **Parity** with 4L claims; **Compromise** — DRY rescale vs doliv semantics.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> 1 format = 1 row · rev. 1 locked

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | = 4L · Hyper-Armor + German Cars + Front Standards | wiki/31; EVID-LG1D-11 | H |
| 2 | Carrier morphology (PGMM) | Narrow 1L bottle + dimple grip (≠ 4L jug) | EVID-LG1D-04; wiki/31 | H |
| 3 | Класс продукта (синт / полусинт) | **Fully synthetic** · API **SN/CF** | EVID-LG1D-01; LG1D-02; LG1D-07 | H |
| 4 | SAE 5W-30 — legibility | **High** (rel. ↑ on narrow label) | EVID-LG1D-02 | H |
| 5 | API — видимость (front / back) | **SN/CF · SN/CF** | EVID-LG1D-02; LG1D-05 | H |
| 6 | ACEA — видимость (front / back) | **C3 · C3** | EVID-LG1D-02; LG1D-05 | H |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-LG1D-03; F-LG1D-02 | H |
| 8 | OEM / допуски — back / site / overlay | = 4L stack · **229.31/229.51** (photo) | EVID-LG1D-06; LG1D-10 | H |
| 9 | Benefit-icons — доказуемость | DuraMax® **↓ micro-text**; Mid-SAPS back only | EVID-LG1D-01; LG1D-07; F-LG1D-05 | M |
| 10 | Cross-face consistency | **Pass** | EVID-LG1D-02 = LG1D-05–06 | H |
| 11 | Digital / overlay vs pack gap | Site **≈ pack** | EVID-LG1D-10 | H |
| 12 | Anti-fraud UX | QR + EAC + barcode + stamp | EVID-LG1D-08; LG1D-09 | H |
| 13 | RF supply & языковая модель | Official integrated RU back | EVID-LG1D-07 | H |
| 14 | Обязательная маркировка РФ | Full stack back | EVID-LG1D-07; LG1D-08 | H |
| 15 | Кириллица vs латиница | EN front · RU back (+ KZ) | EVID-LG1D-01; LG1D-07 | H |
| 16 | Thumbnail robustness (~120 px) | **High-medium** — 5W-30 + API/ACEA ✅ · carbon/DuraMax ↓ | wiki/31 §6 | M |
| 17 | Cognitive load / negative space | **High** — armor stack compressed | wiki/31 | H |
| 18 | Legacy / rev. risk на полке | **Low** — stable wrap; batch 2023 | EVID-LG1D-09 | M |

---

## Импликации для СТМ (1L C3 proxy)

1. **Attack vector:** front OEM band (2–3) + top-up semantic — Genesis 1L **не закрывает**.
2. **Не усреднять** с Mobil 1L 5W-40 — Genesis **сильнее** в front API/ACEA on 1L.
3. **Separate matrix row** от 4L (rule: 1 format = 1 row).

---

## Issues for discussion

1. ~~229.52 drift~~ — **closed** on this photo; monitor other batches.
2. Doliv front OEM — industry norm gap or Lukoil choice?
3. Pair with [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) in future C3 point-ref table.

**DoD:** ODSA GENESIS ARMORTECH GC 5W-30 **1L — complete** (rev. 1 locked).
