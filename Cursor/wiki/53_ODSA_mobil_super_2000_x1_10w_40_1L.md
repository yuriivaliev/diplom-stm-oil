# ODSA — Mobil Super 2000 x1 10W-40 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_SUPER2000_X1_10W40_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [51_PGMM_mobil_super_2000_x1_10w_40_1L_delta.md](51_PGMM_mobil_super_2000_x1_10w_40_1L_delta.md) · base 4L ODSA: [52_…](52_ODSA_mobil_super_2000_x1_10w_40_4L.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (front + **back photo locked**)  
**Формат:** 1L · import base wrap EN/TR · фронт + оборот  
**Статус:** ✅ **Locked** (photo)

> **Не inherit:** оборот 1L **на фото** (pattern [45][49]). Cross-format с [52](52_ODSA_mobil_super_2000_x1_10w_40_4L.md): primary claims **mostly aligned**; delta = объём + carrier + **spec grid asymmetry** (MB 229.1 · AAE B7 · API SJ).

**Canonical URL:** н/д · line-level specs shared with 4L · **pending verify**

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **Mobil Super 2000 x1 10W-40 1L** — **Semi-Synthetic Engine Oil** · **API SN/SN PLUS** (back stack, incl. **SJ**) + **CF** · **ACEA A3/B3** · **AAE Group B7** · OEM back: **VW 501 01/505 00 · AVTOVAZ** — **MB 229.1 absent on 1L photo** (present on 4L [52]).

**Cross-face 1L:** **Partial Pass** — semi + SAE + 1L **согласованы** front ↔ back; **API/ACEA/OEM off-front** (inherited Major); **no split-face API contradiction**.

**Cross-format (1L ↔ 4L):** **Partial Pass** — semi/API tier **aligned**; **delta:** **MB 229.1 lacuna** on 1L back (CR-MS2D-01); **+AAE B7 · +API SJ** on 1L; batch **2022** vs 4L **2021**; carrier morphology + doliv context.

**1L-specific · doliv gap:** API SN+ **invisible on front** while domestic peers **SG/CD front** [45][49] — **attack window widens** on top-up shelf (F-MS2D-05).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 3 |
| Moderate | 5 |
| Minor | 3 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-MS2D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L |
| ART-MS2D-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 1L — specs EN/TR, barcode, штамп 2022 |
| ART-MS2D-003 | Document | wiki/51 | PGMM delta 1L |
| ART-MS2D-004 | Document | wiki/52 | ODSA 4L — cross-format ref |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-MS2D-01 | Artifact | ART-MS2D-001 | Mobil **Super 2000 x1**; **Semi-Synthetic Motor Oil**; **10W-40** magenta band; **Gasoline & Diesel** | A | Active |
| EVID-MS2D-02 | Artifact | ART-MS2D-001 | Front: **API / ACEA / OEM — absent** | A | Active |
| EVID-MS2D-03 | Artifact | ART-MS2D-001 | **1L** + QR + label code **819701B** | A | Active |
| EVID-MS2D-04 | Artifact | ART-MS2D-001 | Narrow bottle + grip grooves; **no integrated handle** | A | Active |
| EVID-MS2D-05 | Artifact | ART-MS2D-002 | Back header: Mobil Super 2000 X1 **10W-40**; **1Le** | A | Active |
| EVID-MS2D-06 | Artifact | ART-MS2D-002 | Meets: **ACEA A3/B3**; **API SJ/SL/SM/SN/SN PLUS**; **AAE (STO 003) Group B7** | A | Active |
| EVID-MS2D-07 | Artifact | ART-MS2D-002 | Approved: **VW 501 01 / 505 00**; **AVTOVAZ (Lada Cars)** — **MB 229.1 not listed** | A | Active |
| EVID-MS2D-08 | Artifact | ART-MS2D-002 | ExxonMobil Quality Level: **API CF** | A | Active |
| EVID-MS2D-09 | Artifact | ART-MS2D-002 | EN + TR descriptive copy; safety **MALEIC ANHYDRIDE** | A | Active |
| EVID-MS2D-10 | Artifact | ART-MS2D-002 | Barcode **5 055107 433614**; back label **830790** | A | Active |
| EVID-MS2D-11 | Artifact | ART-MS2D-002 | Production stamp: **MADE 25-11-2022 · S2B8931 05789** | A | Active |
| EVID-MS2D-12 | Artifact | ART-MS2D-002 | Data matrix + recycling symbol + shield «5»; **EAC / Cyrillic / importer — absent** | A | Active |
| EVID-MS2D-13 | Cross-format | ART-MS2D-004 · [52](52_ODSA_mobil_super_2000_x1_10w_40_4L.md) | 4L back: **MB 229.1** Approved · no AAE B7 · API from **SL** (no SJ) | A | Active |
| EVID-MS2D-14 | Context | ART-MS2D-003 | PGMM delta: DRY rescale; API front lacuna ↑ vs LUKOIL/GPN 1L | B | Context |

### Artifact vs canonical (1L)

| Поле | Artifact (фото 25-11-22) | 4L ref [52] | Статус |
|------|--------------------------|-------------|--------|
| API | **—** front · back **SJ–SN PLUS** + CF | — / SL–SN PLUS + CF | ✅ tier aligned · 🟡 **+SJ** on 1L |
| ACEA | Back **A3/B3** | A3/B3 | ✅ |
| OEM back | **VW · AVTOVAZ** | **MB 229.1 · VW · AVTOVAZ** | 🟡 **MB lacuna** on 1L |
| AAE B7 | **Present** 1L | **Absent** 4L photo | 🟡 cross-format delta |
| Base oil | Semi front + back | Same | ✅ |
| Batch | **2022** | **2021** | 🟡 newer facing |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-MS2D-01 MB 229.1 cross-format | **Open** — 4L has · 1L absent; label rev or format trim? |
| GAP-MS2D-02 Digital triangulation | **Open** — shared with [52] |
| GAP-MS2D-03 QR destination | Open |
| GAP-MS2D-04 Retail @ doliv distance | Open |
| GAP-MS2D-05 AAE B7 significance for RF buyer | Open — CIS standard, back-only |

---

## Findings Catalogue

### F-MS2D-01 — Positive · Cross-face semi / SAE / volume coherent (1L)

| Evidence IDs | EVID-MS2D-01; MS2D-03; MS2D-05 |
| **Severity** | **Positive** · **High** |

---

### F-MS2D-02 — Major · API absent from front (inherited · ↑ severity on doliv)

| Поле | Значение |
|------|----------|
| **Observation** | Front: **no API** (MS2D-02). Back: **SJ–SN PLUS** + CF (MS2D-06, MS2D-08). vs LUKOIL/GPN Super 1L: **SG/CD front** [45][49]. |
| **Evidence IDs** | EVID-MS2D-02; MS2D-06; cross-ref [45][49] F-GS1D-02 |
| **Severity & Confidence** | **Major** · **High** |
| **Interpretation** | Doliv buyer at 0.5–1.5 m **cannot see** modern SN+ edge without turning pack |

---

### F-MS2D-03 — Major · OEM / ACEA off-front; AVTOVAZ back-only

| Evidence IDs | EVID-MS2D-02; MS2D-06; MS2D-07 |
| **Severity** | **Major** · **High** |

---

### F-MS2D-04 — Major · MB 229.1 on 4L · absent on 1L back photo (cross-format OEM asymmetry)

| Поле | Значение |
|------|----------|
| **Observation** | 4L [52] EVID-MS2-07: **MB-Approval 229.1** in Approved block. 1L photo (MS2D-07): **MB not listed** — only VW + AVTOVAZ. |
| **Evidence IDs** | EVID-MS2D-07; MS2D-13 |
| **Severity & Confidence** | **Major** · **High** |
| **Confounds** | Label rev 2021→2022; format-specific OEM trim; crop occlusion |
| **Falsification** | 1L back photo showing MB 229.1; site listing MB for both formats |

---

### F-MS2D-05 — Moderate · Doliv competitive gap — front API vs domestic 1L peers

| Evidence IDs | EVID-MS2D-02; MS2D-14; cross-ref [45][49] |
| **Observation** | Mobil 1L: brand tower + 10W-40 robust; **API/OEM fail @ doliv**. LUKOIL/GPN 1L: **API SG/CD front**. |
| **Severity** | **Moderate** · **High** |

---

### F-MS2D-06 — Moderate · Cross-format spec delta (+SJ · +AAE B7 · −MB)

| Evidence IDs | EVID-MS2D-06; MS2D-13 |
| **Observation** | 1L back **superset** on API list (adds **SJ**) and **AAE B7**; **subset** on OEM (no MB). Batch 2022 vs 2021. |
| **Severity** | **Moderate** · **Medium** |
| **Interpretation** | Likely **label revision drift**, not proven false claim — requires site/line canon |

---

### F-MS2D-07 — Moderate · Parallel import EN/TR · no Cyrillic (inherited)

| Evidence IDs | EVID-MS2D-09; MS2D-12 |
| **Severity** | **Moderate** · **High** |

---

### F-MS2D-08 — Moderate · No anti-fraud UX on doliv format

| Evidence IDs | EVID-MS2D-03; MS2D-12 |
| **Observation** | QR rescaled; no scratch / EAC / importer — **↓ vs GPN 4L scratch** [48] |
| **Severity** | **Moderate** · **High** |

---

### F-MS2D-09 — Moderate · Gold fluid graphic truncated on narrow label

| Evidence IDs | EVID-MS2D-01; wiki/51 MOCC_MS2D_05 |
| **Severity** | **Moderate** · **Medium** (PGMM fidelity ↓ @ thumbnail) |

---

### F-MS2D-10 — Positive · Semi-synthetic explicit front + back

| Evidence IDs | EVID-MS2D-01; MS2D-09 |
| **Severity** | **Positive** · **High** |

---

### F-MS2D-11 — Positive · No split-face API/base/volume defect on 1L wrap

| Evidence IDs | EVID-MS2D-01; MS2D-05; MS2D-06 |
| **Severity** | **Positive** · **High** |

---

### F-MS2D-12 — Positive · Grip affordance — tactile doliv signal (carrier-level)

| Evidence IDs | EVID-MS2D-04; wiki/51 MOCC_MS2D_01–02 |
| **Observation** | Horizontal grip grooves substitute 4L handle — **physical UX ↑** without claim-layer improvement |
| **Severity** | **Positive** · **Medium** |

---

### F-MS2D-13 — Positive · SAE 10W-40 band robust @ vertical rescale

| Evidence IDs | EVID-MS2D-01; wiki/51 |
| **Severity** | **Positive** · **High** |

---

### F-MS2D-14 — Minor · Batch 2022 newer than 4L base 2021

| Evidence IDs | EVID-MS2D-11; MS2D-13 |
| **Severity** | **Minor** · **Medium** |

---

### F-MS2D-15 — Minor · Footer cluster density (QR + 1L + code + Gasoline&Diesel + cropped graphic)

| Evidence IDs | EVID-MS2D-03; wiki/51 MOCC_MS2D_04 |
| **Severity** | **Minor** · **Medium** |

---

### F-MS2D-16 — Minor · x1 unexplained on doliv format

| Evidence IDs | EVID-MS2D-01 |
| **Severity** | **Minor** · **Medium** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-MS2D-01 | MB 229.1 on 4L · absent 1L back | **Open** — F-MS2D-04; cross-format OEM asymmetry |
| CR-MS2D-02 | Front API absent vs back SN+ | **Open** — inherited deictic [52] CR-MS2-01 |
| CR-MS2D-03 | AAE B7 + API SJ on 1L only | **Open** — label rev drift (F-MS2D-06) |
| CR-MS2D-04 | Gold fluid vs semi on doliv | **Open** — inherited PGMM conflict |
| CR-MS2D-05 | Site vs pack | **Open** — digital pending |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — API/OEM front; MB on 1L; Cyrillic; anti-fraud; QR CTA. **Redundancy** — Super+2000+x1+semi+Gasoline&Diesel **without rescale relief**. **Contamination** — gold droplets **truncated** but polisemy **constant**. **Collonisation** — Mobil brand tower on doliv without spec front-load.

**Logical Coherence:** Cross-face product ID **Pass**; OEM cross-format **Partial** (CR-MS2D-01).

**System Dynamics:** **Anomaly** — SN+ chemistry hidden on doliv shelf vs SG front peers. **Potential** — high facings density + brand recognition. **Limit** — triple trust deficit (no handle authority · no front spec · import EN/TR).

**Relational States:** **Parity** with 4L on M_SYSTEM + API deictic pattern. **Anti-parity** vs LUKOIL/GPN 1L on front API. **Compromise** — DRY brand asset vs doliv spec readability.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 1L · rev. 1 locked · **point-ref · doliv context**

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Down-Tier Fluid Kinetics + Numeric Line Heuristic (2000) + Mobil Global Brand Transfer + Back-Loaded Modern Spec Grid — **константа** vs 4L | wiki/51; EVID-MS2D-14 | H |
| 2 | Carrier morphology (PGMM) | Narrow 1L bottle + grip grooves + indentations · **no handle** | EVID-MS2D-04; wiki/51 | H |
| 3 | Класс продукта (синт / полусинт) | **Semi-Synthetic** · API **SN/SN PLUS** (back, incl. SJ) + **CF** | EVID-MS2D-01; MS2D-06; MS2D-08 | H |
| 4 | SAE 10W-40 — legibility | **High** — magenta band **↑ relative scale** on narrow label | EVID-MS2D-01 | H |
| 5 | API — видимость (front / back) | **— / SJ–SN PLUS + CF** | EVID-MS2D-02; MS2D-06; F-MS2D-02 | H |
| 6 | ACEA — видимость (front / back) | **— / A3/B3** (+ **AAE B7** back) | EVID-MS2D-06 | H |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-MS2D-02 | H |
| 8 | OEM / допуски — back / site / overlay | Back: **VW · AVTOVAZ** · **MB 229.1 absent vs 4L** · Site pending | EVID-MS2D-07; MS2D-13; F-MS2D-04 | H / M |
| 9 | Benefit-icons — доказуемость | Gold droplets **truncated**; Gasoline&Diesel **↓ micro-text** | EVID-MS2D-01; F-MS2D-09 | M |
| 10 | Cross-face consistency | **Partial Pass** — semi/SAE/1L Pass; API/OEM deictic | F-MS2D-11; CR-MS2D-02 | H |
| 11 | Digital / overlay vs pack gap | **Pending** — no site verify | GAP-MS2D-02 | L |
| 12 | Anti-fraud UX | **QR only** — no EAC / scratch / importer | EVID-MS2D-03; MS2D-12 | H |
| 13 | RF supply & языковая модель | **Parallel import** · EN+TR · **no Cyrillic** | EVID-MS2D-09; MS2D-12 | H |
| 14 | Обязательная маркировка РФ | **Absent** (no EAC · no importer visible) | EVID-MS2D-12 | H |
| 15 | Кириллица vs латиница | **EN dominant** · TR secondary · **no Cyrillic** | EVID-MS2D-09 | H |
| 16 | Thumbnail robustness (~120 px) | **Medium** — Mobil + 10W-40 ✅ · 1L/QR/API/OEM **fail** @120 px | wiki/51 §4.2 | H |
| 17 | Cognitive load / negative space | **Bimodal** — medium front stack + **peak** footer cluster | wiki/51; F-MS2D-15 | H |
| 18 | Legacy / rev. risk на полке | **Moderate** — batch **2022**; spec grid **≠ 4L 2021** (MB/AAE/SJ) | EVID-MS2D-11; MS2D-13 | M |

---

## Импликации для СТМ (Classic/Protect · 10W-40 · 1L doliv)

1. **Attack vector (primary):** front row **API SN/CF + ACEA A3/B3** + **AVTOVAZ** readable @ doliv distance — закрыть gap vs Mobil **and** LUKOIL/GPN 1L.
2. **Attack vector (doliv trust):** named semi tech + **one** benefit + visible **1L** — не копировать Mobil DRY rescale without spec front-load.
3. **Не копировать:** footer cluster hyper-density · gold-fluid truncation · numeric 2000 void · cross-format OEM inconsistency pattern.
4. **Institutional:** СТМ needs RF anti-fraud equivalent — Mobil QR **without CTA** = half-integrated digital trace.

---

## Issues for discussion

1. **MB 229.1 cross-format:** verify fresh 1L facings — intentional trim or photo/batch artifact?
2. **AAE B7 on 1L:** relevant for RF Classic/Protect positioning or import-only CIS cue?
3. **Symmetric matrix row:** add Mobil Super 2000 1L to Wave 3 table in [08_PGMM_упаковка.md](08_PGMM_упаковка.md)?
4. Cross-ref 4L: [52](52_ODSA_mobil_super_2000_x1_10w_40_4L.md) · PGMM [50](50_PGMM_mobil_super_2000_x1_10w_40.md) · [51](51_PGMM_mobil_super_2000_x1_10w_40_1L_delta.md).

**DoD:** ODSA Mobil Super 2000 x1 10W-40 **1L — complete** (rev. 1 photo locked). Pending: digital triangulation, MB cross-format verify.
