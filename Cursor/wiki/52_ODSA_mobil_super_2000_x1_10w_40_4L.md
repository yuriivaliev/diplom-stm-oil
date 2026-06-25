# ODSA — Mobil Super 2000 x1 10W-40 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_SUPER2000_X1_10W40_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [50_PGMM_mobil_super_2000_x1_10w_40.md](50_PGMM_mobil_super_2000_x1_10w_40.md) · delta 1L: [51_…](51_PGMM_mobil_super_2000_x1_10w_40_1L_delta.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (front + back photo locked)  
**Формат:** 4L · import base wrap EN/TR · фронт + оборот  
**Статус:** ✅ **Locked** (photo) · 🟡 **digital pending** (no EX-Mobil-Super-2000 in wiki/04)

> **Контекст:** point-ref **Classic/Protect · ЮФО 10W-40** — вне матриц 5W-40 / 0W-20 / 5W-30. **1 format = 1 row**; 1L → [53](53_ODSA_mobil_super_2000_x1_10w_40_1L.md).

**Canonical URL:** н/д · EX-01 (Russia exit context only)

---

## Executive summary (rev. 1 · photo locked)

**Канон SKU (artifact):** **Mobil Super 2000 x1 10W-40 4L** — **Semi-Synthetic Motor Oil** · **API SN/SN PLUS** (back stack) + **CF** (quality level) · **ACEA A3/B3** (back) · OEM back: **MB 229.1 · VW 501 01/505 00 · AVTOVAZ**.

**Artifact vs canonical (site):** Site triangulation **н/д** — канон row = **artifact back stack** until verify. Нет эволюции SL→SP на фото; **SN PLUS** = наивысший видимый API tier.

**Cross-face (4L base wrap):** **Partial Pass** — semi-synthetic + SAE + 4L **согласованы** front ↔ back (F-MS2-01 Positive); **API/ACEA/OEM off-front** (F-MS2-02, F-MS2-03 Major); **нет split-face API defect** (front silent ≠ back contradicts).

**vs LUKOIL/GPN Super [44][48]:** **↑ modern chemistry** (API SN+ back vs SG/CD front); **↓ shelf spec transparency** (API off-front); **↓ RF integration** (EN/TR import · no Cyrillic · no official supply · no anti-fraud).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 5 |
| Minor | 3 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-MS2-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 4L |
| ART-MS2-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 4L — specs EN/TR, barcode, штамп 2021 |
| ART-MS2-003 | Document | wiki/50 | PGMM _full 4L (context) |
| ART-MS2-004 | Context | [EX-01](04_источники_и_URL.md) | ExxonMobil Russia exit — parallel import context |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-MS2-01 | Artifact | ART-MS2-001 | Mobil **Super 2000 x1**; **Semi-Synthetic Motor Oil**; **10W-40** magenta band; **Gasoline & Diesel** | A | Active |
| EVID-MS2-02 | Artifact | ART-MS2-001 | Front: **API / ACEA / OEM — absent** | A | Active |
| EVID-MS2-03 | Artifact | ART-MS2-001 | **4L** + QR + label code **819702A** | A | Active |
| EVID-MS2-04 | Artifact | ART-MS2-001 | Gold droplet graphic + metallic ring (fluid kinetics) | A | Active |
| EVID-MS2-05 | Artifact | ART-MS2-002 | Back header: Mobil Super 2000 X1 **10W-40** | A | Active |
| EVID-MS2-06 | Artifact | ART-MS2-002 | Meets: **ACEA A3/B3**; **API SL/SM/SN/SN PLUS** | A | Active |
| EVID-MS2-07 | Artifact | ART-MS2-002 | Approved: **MB-Approval 229.1**; **VW 501 01/505 00**; **AVTOVAZ (Lada Cars)** | A | Active |
| EVID-MS2-08 | Artifact | ART-MS2-002 | ExxonMobil Quality Level: **API CF** | A | Active |
| EVID-MS2-09 | Artifact | ART-MS2-002 | EN + TR descriptive copy; safety **MALEIC ANHYDRIDE**; disposal instructions | A | Active |
| EVID-MS2-10 | Artifact | ART-MS2-002 | Barcode **5 055107 433607**; back label **823898A** | A | Active |
| EVID-MS2-11 | Artifact | ART-MS2-002 | Production stamp: **MADE 16-07-21 · S170461 10422** | A | Active |
| EVID-MS2-12 | Artifact | ART-MS2-002 | Copyright © 2019 ExxonMobil; **www.mobil.com** | A | Active |
| EVID-MS2-13 | Artifact | ART-MS2-001–002 | **Cyrillic / EAC / importer / RU overlay — absent** | A | Active |
| EVID-MS2-14 | Context | ART-MS2-003 | PGMM: API off-front Mobil family norm; gold fluid vs semi honesty | B | Context |
| EVID-MS2-15 | Context | ART-MS2-004 | Not official RF supply (parallel import) | B | Active |

### Artifact vs canonical

| Поле | Artifact (фото · batch 16-07-21) | Canonical (line / site) | Статус |
|------|-----------------------------------|---------------------------|--------|
| Base oil | «Semi-Synthetic Motor Oil» front | Полусинтетическое Mobil Super 2000 | ✅ aligned |
| API | **—** front · back **SL–SN PLUS** + CF | **SN+** tier (back stack) | 🟡 front lacuna · back modern |
| ACEA | Back **A3/B3** | A3/B3 (artifact) | ✅ back-only |
| OEM | Back: MB 229.1 · VW · **AVTOVAZ** | Artifact OEM grid | ✅ back-only |
| RU supply | EN/TR · no Cyrillic | Parallel import (EX-01) | 🟡 import |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-MS2-01 Digital triangulation (mobil.com product page) | **Open** — no URL ID in wiki/04 |
| GAP-MS2-02 Retail @1.2 m front spec readability | Open |
| GAP-MS2-03 QR destination / anti-fraud channel | Open — QR present, CTA **н/д** |
| GAP-MS2-04 TDS chemistry (HTHS, drain, SAPS) | Open |
| GAP-MS2-05 Batch 2021 vs current facings share | Open — **older** vs 1L batch 2022 |

---

## Findings Catalogue

### F-MS2-01 — Positive · Core claims coherent (semi · 10W-40 · 4L)

| Поле | Значение |
|------|----------|
| **Observation** | Front: semi-synthetic + 10W-40 + 4L + Gasoline & Diesel (MS2-01, MS2-03). Back: identical product ID + semi claim EN/TR (MS2-05, MS2-09). |
| **Evidence IDs** | EVID-MS2-01; MS2-03; MS2-05 |
| **Severity & Confidence** | **Positive** · **High** |

---

### F-MS2-02 — Major · API absent from front; modern stack back-only

| Поле | Значение |
|------|----------|
| **Observation** | Front: **no API** (MS2-02). Back: **SL/SM/SN/SN PLUS** + separate **CF** quality level (MS2-06, MS2-08). |
| **Interpretation** | Deictic Mobil family pattern [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) — **not** split-face contradiction; **Major** for shelf @1.2 m vs domestic peers with **SG/CD front** [44][48]. |
| **Evidence IDs** | EVID-MS2-02; MS2-06; MS2-08 |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | structural: СТМ — API SN/CF **front row** on 10W-40 Classic/Protect |

---

### F-MS2-03 — Major · OEM / ACEA stack not on front

| Поле | Значение |
|------|----------|
| **Observation** | Front: no ACEA, no OEM. Back: ACEA A3/B3 + MB/VW/AVTOVAZ (MS2-06, MS2-07). **AVTOVAZ back-only** — domestic legacy signal invisible @ shelf. |
| **Evidence IDs** | EVID-MS2-02; MS2-06; MS2-07 |
| **Severity & Confidence** | **Major** · **High** |

---

### F-MS2-04 — Moderate · Parallel import — EN/TR base, no Cyrillic

| Поле | Значение |
|------|----------|
| **Observation** | Back GB + TR copy (MS2-09); **no Cyrillic** pack-wide (MS2-13); EX-01 parallel import context (MS2-15). **No RU overlay** attestation (unlike Super 3000 [18]). |
| **Evidence IDs** | EVID-MS2-09; MS2-13; MS2-15 |
| **Severity & Confidence** | **Moderate** · **High** |

---

### F-MS2-05 — Moderate · Modern API SN+ vs legacy 10W-40 segment rhetoric

| Поле | Значение |
|------|----------|
| **Observation** | Back API **SN/SN PLUS** — **↑ chemistry tier** vs budget peers **SG/CD** [44][48]; yet front carries **«Super 2000»** numeric hyperbole + gold fluid graphic (MS2-04) without chemistry proof on front. |
| **Evidence IDs** | EVID-MS2-04; MS2-06; cross-ref [44][48] |
| **Severity & Confidence** | **Moderate** · **High** |
| **Interpretation** | Competitive **anomaly** — modern chemistry hidden on shelf-facing face |

---

### F-MS2-06 — Moderate · API taxonomy asymmetry (Meets vs Quality Level CF)

| Поле | Значение |
|------|----------|
| **Observation** | Back: «Meets … SL–SN PLUS» + separate «ExxonMobil Quality Level: **API CF**» — dual taxonomy (MS2-06, MS2-08). |
| **Evidence IDs** | EVID-MS2-06; MS2-08 |
| **Severity & Confidence** | **Moderate** · **Medium** |

---

### F-MS2-07 — Moderate · No anti-fraud UX

| Поле | Значение |
|------|----------|
| **Observation** | QR present (MS2-03) but **no** scratch code / EAC / importer attestation / 3662.ru pattern. vs GPN scratch [48] · LUKOIL institutional back. |
| **Evidence IDs** | EVID-MS2-03; MS2-13 |
| **Severity & Confidence** | **Moderate** · **High** |

---

### F-MS2-08 — Positive · Semi-synthetic explicit front + back

| Evidence IDs | EVID-MS2-01; MS2-09 |
| **Severity** | **Positive** · **High** |

---

### F-MS2-09 — Positive · No split-face API/base/volume defect

| Evidence IDs | EVID-MS2-01; MS2-05; MS2-06 |
| **Observation** | Front silent on API ≠ back contradicts — **Pass** on internal consistency. |
| **Severity** | **Positive** · **High** |

---

### F-MS2-10 — Positive · AVTOVAZ on back — partial domestic OEM signal

| Evidence IDs | EVID-MS2-07; cross-ref [44] EVID-LS-06 |
| **Observation** | AVTOVAZ listed back-only — **↑ vs import-only narrative** but **↓ vs LUKOIL/GPN** (domestic stack + front OEM on GPN). |
| **Severity** | **Positive** · **Medium** |

---

### F-MS2-11 — Minor · Batch 2021 — older facing vs 1L 2022

| Evidence IDs | EVID-MS2-11; cross-ref [53](53_ODSA_mobil_super_2000_x1_10w_40_1L.md) |
| **Severity** | **Minor** · **Medium** |

---

### F-MS2-12 — Minor · x1 sub-badge — technology claim unexplained

| Evidence IDs | EVID-MS2-01; wiki/50 MOCC_MS2_LAC04 |
| **Severity** | **Minor** · **Medium** |

---

### F-MS2-13 — Minor · Safety allergen MALEIC ANHYDRIDE on back only

| Evidence IDs | EVID-MS2-09 |
| **Severity** | **Minor** · compliance flag |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-MS2-01 | Front API absent vs back SN+ stack | **Open** — F-MS2-02; deictic pattern, not split-face |
| CR-MS2-02 | Gold fluid premium graphic vs semi label | **Open** — rhetoric vs chemistry (PGMM MSYS_MS2_01↔02) |
| CR-MS2-03 | Modern API SN+ vs legacy 10W-40 segment peers | **Open** — competitive positioning, not pack defect |
| CR-MS2-04 | Site vs pack specs | **Open** — GAP-MS2-01 digital pending |
| CR-MS2-05 | 4L MB 229.1 vs 1L back photo | **Open** — cross-format; see [53](53_ODSA_mobil_super_2000_x1_10w_40_1L.md) CR-MS2D-01 |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — API/ACEA/OEM front; Cyrillic; RF supply; anti-fraud; QR CTA; digital site. **Redundancy** — Super + 2000 + x1 + semi + Gasoline&Diesel + gold graphic. **Contamination** — gold droplets colonise semi-synthetic tier. **Collonisation** — Mobil global code over legacy 10W-40 domestic segment.

**Logical Coherence:** Cross-face semi/SAE/volume **Pass**; API/OEM **Partial** (deictic). Gold fluid vs semi **Conflict** (PGMM).

**System Dynamics:** **Anomaly** — SN+ chemistry back vs SG/CD front peers. **Potential** — tier-1 Mobil recognition on import price. **Limit** — batch 2021; no official RF channel; no retail @1.2 m data.

**Relational States:** **Consensus** front ↔ back on product identity. **Compromise** — modern specs deferred to back. **Anti-parity** vs LUKOIL/GPN on front API row and RF integration.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 4L · rev. 1 locked · **point-ref**

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Down-Tier Fluid Kinetics + Numeric Line Heuristic (2000) + Mobil Global Brand Transfer + Back-Loaded Modern Spec Grid | wiki/50; EVID-MS2-14 | H |
| 2 | Carrier morphology (PGMM) | 4L silver-grey HDPE jug + integrated handle + grip ridges | wiki/50; ART-MS2-001 | H |
| 3 | Класс продукта (синт / полусинт) | **Semi-Synthetic** · API **SN/SN PLUS** (back) + **CF** | EVID-MS2-01; MS2-06; MS2-08 | H |
| 4 | SAE 10W-40 — legibility | **High** — white on magenta band | EVID-MS2-01 | H |
| 5 | API — видимость (front / back) | **— / SL–SN PLUS + CF** | EVID-MS2-02; MS2-06; MS2-08; F-MS2-02 | H |
| 6 | ACEA — видимость (front / back) | **— / A3/B3** | EVID-MS2-02; MS2-06 | H |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-MS2-02; F-MS2-03 | H |
| 8 | OEM / допуски — back / site / overlay | Back: **MB 229.1 · VW 501 01/505 00 · AVTOVAZ** · Site **pending** | EVID-MS2-07; GAP-MS2-01 | H / L |
| 9 | Benefit-icons — доказуемость | Gold droplet graphic **without** tribology proof; Gasoline&Diesel **literal** | EVID-MS2-04; MS2-01 | M |
| 10 | Cross-face consistency | **Partial Pass** — semi/SAE Pass; API/OEM deictic | EVID-MS2-09; F-MS2-09; CR-MS2-01 | H |
| 11 | Digital / overlay vs pack gap | **Pending** — no mobil.com verify; no RU overlay | GAP-MS2-01; MS2-13 | L |
| 12 | Anti-fraud UX | **QR only** — no scratch / EAC / importer proof | EVID-MS2-03; MS2-13; F-MS2-07 | H |
| 13 | RF supply & языковая модель | **Parallel import** · **EN+TR** base · **no Cyrillic** | EVID-MS2-09; MS2-13; MS2-15 | H |
| 14 | Обязательная маркировка РФ | **Absent** on import base (no EAC · no importer block visible) | EVID-MS2-13 | H |
| 15 | Кириллица vs латиница | **EN dominant** · TR secondary · **no Cyrillic** | EVID-MS2-09; MS2-13 | H |
| 16 | Thumbnail robustness (~120 px) | **Medium-high** — Mobil + Super/2000 + 10W-40; API/OEM **fail** | wiki/50 | H |
| 17 | Cognitive load / negative space | **Medium front / high back** — dark field + dense legal EN/TR | wiki/50 | H |
| 18 | Legacy / rev. risk на полке | **Moderate** — batch **2021**; stable wrap family; site **pending** | EVID-MS2-11; GAP-MS2-01 | M |

---

## Импликации для СТМ (Classic/Protect · 10W-40)

1. **Перенять:** semi-synthetic **honesty** on front · readable **SAE 10W-40** band · modern chemistry if product matches.
2. **Attack vector:** **API SN/CF + ACEA A3/B3 front** + **AVTOVAZ + import OEM row** + **full Cyrillic** + official RF supply — закрыть **triple gap** vs Mobil import (no front spec · no Cyrillic · no anti-fraud).
3. **Не копировать:** numeric 2000 hyperbole · gold fluid void · API back-only · EN-only import facing.
4. Point-ref — **отдельные строки** 4L / 1L; cross-ref peers [44][48].

---

## Issues for discussion

1. **EX-Mobil-Super-2000:** add to wiki/04 + verify mobil.com product card.
2. **10W-40 matrix branch:** include Mobil Super 2000 as third import tier-1 point-ref?
3. **Cross-format MB 229.1:** 4L has MB Approved · 1L photo **absent** — label rev or format trim? See [53](53_ODSA_mobil_super_2000_x1_10w_40_1L.md).
4. Cross-ref 1L: [53](53_ODSA_mobil_super_2000_x1_10w_40_1L.md) · PGMM delta [51](51_PGMM_mobil_super_2000_x1_10w_40_1L_delta.md).

**DoD:** ODSA Mobil Super 2000 x1 10W-40 **4L — complete** (rev. 1 photo locked). Pending: digital triangulation, GAP-MS2-02 retail distance.
