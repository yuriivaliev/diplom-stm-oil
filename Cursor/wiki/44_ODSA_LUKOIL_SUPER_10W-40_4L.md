# ODSA — LUKOIL SUPER 10W-40 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_LUKOIL_SUPER_10W40_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [42_PGMM_LUKOIL_SUPER_10W-40.md](42_PGMM_LUKOIL_SUPER_10W-40.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (front + back + site locked)  
**Формат:** 4L · official RF wrap · фронт + оборот + сайт LLK-03  
**Статус:** ✅ **Locked**

> **Контекст:** point-ref **Classic/Protect · ЮФО 10W-40** — вне матриц 5W-40 / 0W-20 / 5W-30. **1 format = 1 row**; 1L → [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md).

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **LUKOIL SUPER 10W-40 4L** — полусинтетическое · **API SG/CD** · domestic OEM (АВТОВАЗ · УМЗ · ЗМЗ).

**Artifact vs canonical:** **Aligned** — фото batch **09.11.22** = site LLK-03; эволюции допуска (SL→SN) **нет**; triangulation **не требует** canon override.

**Cross-face:** **Pass** — API SG/CD + semi-synthetic **согласованы** front ↔ back (EVID-LS-01–06); site LLK-03 **≈ pack** (EVID-LS-08).

**Ключевой gap vs Genesis/LUXE:** SUPER **выигрывает** в budget-honesty (API SG **на фронте**, без маскировки); **проигрывает** в institutional depth (OEM **только back**, ActiPure **без proof**, **нет** ACEA/QR на фото).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 4 |
| Minor | 3 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-LS-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 4L |
| ART-LS-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 4L |
| ART-LS-003 | Document | wiki/42 | PGMM _full 4L (context) |
| ART-LS-004 | Web | [LLK-03](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-super-10w-40) | ProductCard + TDS PDF link |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-LS-01 | Artifact | ART-LS-001 | LUKOIL logo; «**УНИВЕРСАЛЬНОЕ МАСЛО**» + car icon; «**SUPER**»; «**ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» | A | Active |
| EVID-LS-02 | Artifact | ART-LS-001 | Front lockup: **10W-40 · API SG/CD · 4L** | A | Active |
| EVID-LS-03 | Artifact | ART-LS-001 | «**ActiPure**» + «**ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ**» footer | A | Active |
| EVID-LS-04 | Artifact | ART-LS-001 | **OEM / ACEA на фронте не видны** | A | Active |
| EVID-LS-05 | Artifact | ART-LS-002 | Back header: LUKOIL SUPER; **Semi-synthetic engine oil**; **10W-40** red bar | A | Active |
| EVID-LS-06 | Artifact | ART-LS-002 | Back spec: **API SG/CD**; OEM: **ПАО «АВТОВАЗ» · ОАО «ЗМЗ» · ОАО «УМЗ»** | A | Active |
| EVID-LS-07 | Artifact | ART-LS-002 | RU body: полусинтетическое всесезонное; multilang legal + safety | A | Active |
| EVID-LS-08 | Artifact | ART-LS-002 | Barcode **4607161615393**; **EAC**; **4л** | A | Active |
| EVID-LS-09 | Artifact | ART-LS-002 | Production stamp: **09.11.22 · 3970 3 · 22 06894360** (partial legibility) | A | Active |
| EVID-LS-10 | Artifact | ART-LS-002 | **QR / 3662 anti-fraud — не виден** на фото back | A | Active |
| EVID-LS-11 | Web | ART-LS-004 (LLK-03) | Site: полусинтетическое; **API SG/CD**; АВТОВАЗ · УМЗ · ЗМЗ; TDS PDF | A | Active |
| EVID-LS-12 | Context | ART-LS-003 | PGMM: Universal Mass Heuristic + ActiPure void; OEM back-only | B | Context |

### Artifact vs canonical

| Поле | Artifact (фото 09.11.22) | Canonical (LLK-03) | Статус |
|------|--------------------------|---------------------|--------|
| API | **SG/CD** front + back | **SG/CD** | ✅ aligned |
| Base oil | «ПОЛУСИНТЕТИЧЕСКОЕ» front + back EN/RU | Полусинтетическое (site) | ✅ aligned |
| OEM | АВТОВАЗ · ЗМЗ · УМЗ back | АВТОВАЗ · УМЗ · ЗМЗ (site) | ✅ aligned (notation АО/ПАО/ОАО) |
| ActiPure | front footer | н/д расшифровка site/TDS | artifact-only |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-LS-01 ISO/IATF / производитель на back — microtype | **Open** — dense legal; не выделено в crop |
| GAP-LS-02 TDS chemistry (HTHS, drain interval, SAPS) | Open |
| GAP-LS-03 Retail @1.2 m OEM back readability | Open |
| GAP-LS-04 Доля 2022 vs newer facings | Open — н/д |

---

## Findings Catalogue

### F-LS-01 — Positive · Cross-face API / base oil / SAE coherent

| Поле | Значение |
|------|----------|
| **Observation** | Front (EVID-LS-02): **10W-40 · API SG/CD · 4L** + полусинтетика (LS-01). Back (LS-05–06): идентичный API + semi claim. Site (LS-11) = back. |
| **Evidence IDs** | EVID-LS-01; LS-02; LS-05; LS-06; LS-11 |
| **Severity & Confidence** | **Positive** · **High** |

---

### F-LS-02 — Major · OEM-стек не на фронте канистры

| Поле | Значение |
|------|----------|
| **Observation** | Front: «УНИВЕРСАЛЬНОЕ МАСЛО» + car icon — **не** OEM list. Domestic stack (АВТОВАЗ/УМЗ/ЗМЗ) — **только back** (LS-06) и site (LS-11). |
| **Evidence IDs** | EVID-LS-04; LS-06; LS-11 |
| **Impact** | Trust · Revenue (legacy domestic park / ЮФО service) |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | quick: 2–3 domestic OEM microtype на front row; structural: readable OEM band @1.2 m |

---

### F-LS-03 — Moderate · ActiPure® + «инновация» vs API SG/CD chemistry tier

| Поле | Значение |
|------|----------|
| **Observation** | Front (LS-03): «ActiPure» + «ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ» при **API SG/CD** (pre-SN legacy). Rhetoric premium vs chemistry budget — **не split-face error**, но **claim inflation**. |
| **Evidence IDs** | EVID-LS-03; LS-02; LS-06 |
| **Severity & Confidence** | **Moderate** · **High** |
| **Falsification** | TDS или back text с additive chemistry proof |

---

### F-LS-04 — Moderate · ACEA / ILSAC / modern API — absent (expected lacuna)

| Evidence IDs | EVID-LS-04; LS-06; LS-11 |
| **Observation** | Нет ACEA, ILSAC, SN+ на pack или site — **consistent** с legacy 10W-40 segment; **не contradiction**. |
| **Severity** | **Moderate** · **High** (segment disclosure gap) |

---

### F-LS-05 — Positive · API SG/CD на фронте — budget honesty (vs LUXE mask pattern)

| Evidence IDs | EVID-LS-02; cross-ref [16](16_ODSA_LUKOIL_LUXE_5W-40_4L.md) evolution |
| **Observation** | Legacy API **explicit** on front — **no silent upgrade** narrative; white space для СТМ = **honest SN** if chemistry matches, not false «innovation». |
| **Severity** | **Positive** · **High** |

---

### F-LS-06 — Minor · Batch 2022 — label-age shelf risk

| Evidence IDs | EVID-LS-09 |
| **Observation** | Production **09.11.22**; site TDS link active — **no pack evolution detected**; доля старых facings **н/д**. |
| **Severity** | **Minor** · **Medium** |

---

### F-LS-07 — Moderate · ActiPure — named tech без pack-level proof

| Evidence IDs | EVID-LS-03; LS-07; LS-11 |
| **Observation** | Proprietary seal на front; site/TDS — benefits text, **без** additive metric на этикетке. |
| **Severity** | **Moderate** · **Medium** |

---

### F-LS-08 — Minor · Anti-fraud UX — EAC + barcode; QR не на фото

| Evidence IDs | EVID-LS-08; LS-10 |
| **Observation** | EAC + EAN present; **нет** QR «Подробная информация» (vs Genesis [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) LS-06). Site footer mentions QR for Lukoil line generally — **not on this facing**. |
| **Severity** | **Minor** · **Medium** |

---

### F-LS-09 — Positive · Site triangulation ≈ pack (no superset gap)

| Evidence IDs | EVID-LS-11; LS-06 |
| **Severity** | **Positive** · **High** |

---

### F-LS-10 — Positive · Semi-synthetic explicit front + back (rare literal honesty)

| Evidence IDs | EVID-LS-01; LS-05; LS-07; LS-11 |
| **Severity** | **Positive** · **High** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-LS-01 | OEM universal front vs domestic OEM back | **Open** — F-LS-02; intentional back-load, не split-face API error |
| CR-LS-02 | ActiPure «innovation» vs API SG legacy | **Open** — F-LS-03; rhetoric vs chemistry, claims **coherent** on API tier |
| CR-LS-03 | Site vs pack OEM notation (АО vs ПАО/ОАО) | **Closed** — same entities; legal form variant |
| CR-LS-04 | Site vs pack specs | **Closed** — LLK-03 ≈ EVID-LS-06 |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — OEM front, ACEA, ActiPure mechanism, QR. **Redundancy** — universal + car + SUPER + semi (×4). **Contamination** — honeycomb = armor + filter polisemy (PGMM context).

**Logical Coherence:** Cross-face API/semi **Pass**; innovation rhetoric **≠** chemistry tier — **Conflict** (F-LS-03), не packaging defect.

**System Dynamics:** **Anomaly** — API SG **on front** (stronger heuristic than masked LUXE). **Potential** — domestic OEM back for ЮФО/legacy. **Limit** — 2022 batch photo; no @1.2 m retail validation.

**Relational States:** **Consensus** pack = site = artifact canonical. **Compromise** — budget tier retains Lukoil mesh DNA + ActiPure seal.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 4L · rev. 1 locked · **point-ref** (вне матриц 5W-40/0W-20/5W-30)

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Universal Mass Heuristic + Honeycomb Armor Lite + ActiPure Epistemic Black Box + Domestic OEM Sovereignty | wiki/42; EVID-LS-12 | H |
| 2 | Carrier morphology (PGMM) | 4L silver-grey HDPE jug + integrated side handle + red cap | wiki/42; ART-LS-001 | H |
| 3 | Класс продукта (синт / полусинт) | **Полусинтетическое** · API **SG/CD** | EVID-LS-01; LS-02; LS-05–07; LS-11 | H |
| 4 | SAE 10W-40 — legibility | **High** — white on black spec row + back red bar | EVID-LS-02; LS-05 | H |
| 5 | API — видимость (front / back) | **SG/CD · SG/CD** | EVID-LS-02; LS-06 | H |
| 6 | ACEA — видимость (front / back) | **Absent · Absent** (legacy segment) | EVID-LS-04; LS-11 | H |
| 7 | OEM / допуски — front (effective) | **Нет** — universal + car icon only | EVID-LS-04; F-LS-02 | H |
| 8 | OEM / допуски — back / site / overlay | **АВТОВАЗ · УМЗ · ЗМЗ** (domestic stack) | EVID-LS-06; LS-11 | H |
| 9 | Benefit-icons — доказуемость | ActiPure® **named** · oxidation/cold-start **site only** · no tribology icons | EVID-LS-03; LS-11 | M |
| 10 | Cross-face consistency | **Pass** | EVID-LS-02 = LS-06 = LS-11 | H |
| 11 | Digital / overlay vs pack gap | Site **≈ pack** (no superset) | EVID-LS-11 vs LS-06 | H |
| 12 | Anti-fraud UX | **EAC + barcode + batch stamp** · QR **н/д** on photo | EVID-LS-08; LS-09; LS-10 | M |
| 13 | RF supply & языковая модель | Official LLK · integrated Cyrillic front + multilang back | EVID-LS-01; LS-07 | H |
| 14 | Обязательная маркировка РФ | EAC · barcode · batch stamp · producer in legal wall (**ISO/IATF — verify**) | EVID-LS-08; LS-09; GAP-LS-01 | M |
| 15 | Кириллица vs латиница | **Кириллица dominant** front claims + EN «Semi-synthetic» back header | EVID-LS-01; LS-05 | H |
| 16 | Thumbnail robustness (~120 px) | **High** — SUPER + 10W-40 + LUKOIL; ActiPure **marginal** | wiki/42; EVID-LS-02 | H |
| 17 | Cognitive load / negative space | **Medium front / high back** — universal redundancy + dense legal | wiki/42 | H |
| 18 | Legacy / rev. risk на полке | **Low–Moderate** — stable SG/CD wrap; batch 2022 · no SL→SN drift detected | EVID-LS-09; LS-11 | M |

---

## Импликации для СТМ (Classic/Protect · 10W-40)

1. **Перенять:** readable **SAE + API front** + **semi-synthetic honesty** + domestic OEM band (back minimum; **front 2–3** — white space).
2. **Не копировать:** SUPER hyperbole + ActiPure void + mesh armor without fluid antidote.
3. **Attack vector:** honest **SN/CF** tier (if chemistry matches) + named additive **with metric** + OEM front row for ЮФО legacy park.
4. Point-ref — **отдельные строки** 4L / 1L; не смешивать с матрицей 5W-40 mass-mid.

---

## Issues for discussion

1. Создавать ли **ветку матрицы 10W-40** (SUPER + budget peers) для Волны 3?
2. QR adoption на SUPER wrap — verify на свежих facings.
3. Cross-ref 1L: [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md) · PGMM delta [43](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md).

**DoD:** ODSA LUKOIL SUPER 10W-40 **4L — complete** (rev. 1 locked).
