# ODSA — Gazpromneft Super 10W-40 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_GPN_SUPER_10W40_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [46_PGMM_Gazpromneft_Super_10W-40.md](46_PGMM_Gazpromneft_Super_10W-40.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (front + back photo locked · GPN-03 scrape blocked)  
**Формат:** 4L · official RF wrap · фронт + оборот  
**Статус:** ✅ **Locked** (photo) · 🟡 **GPN-03 pending** (site auto-scrape blocked)

> **Контекст:** point-ref **Classic/Protect · ЮФО 10W-40** — вне матриц 5W-40 / 0W-20 / 5W-30. **1 format = 1 row**; 1L → [49](49_ODSA_Gazpromneft_Super_10W-40_1L.md).

**Canonical URL:** [GPN-03](04_источники_и_URL.md) · `https://gazpromneft-oil.ru/ru/products/all/gazpromneft-super-10w-40` · **pending verify** 25.06.2026 · Firecrawl **ERR_TUNNEL** (pattern GPN-01/02)

---

## Executive summary (rev. 1 · photo locked)

**Канон SKU (artifact):** **Gazpromneft Super 10W-40 4L** — полусинтетическое · **API SG/CD** · domestic OEM partial (**AVTOVAZ · ZMZ** front microtype; **ПАО «АВТОВАЗ»** back).

**Artifact vs canonical (site):** **Aligned on photo** — нет эволюции SL→SN; triangulation **не требует** canon override по правилу наивысшего допуска (legacy SG tier stable). **Digital:** GPN-03 **н/д** (scrape blocked) — канон site = PGMM context: полусинтетическое универсальное · API SG/CD.

**Cross-face:** **Partial Pass** — API SG/CD + semi-synthetic + SAE **согласованы** front ↔ back (EVID-GS-01–07); **OEM split:** **ZMZ front · absent back** (F-GS-02); **UMZ absent** pack-wide vs peer LUKOIL (F-GS-03).

**Ключевой delta vs LUKOIL SUPER [44]:** GPN **↑ OEM partial front** (AVTOVAZ·ZMZ microtype); **↓ domestic stack depth** (no UMZ; ZMZ back-lacuna); **↑ institutional anti-fraud** (scratch «Уникальный номер» + AAI back); **↓** batch age (**2020** vs LUKOIL 2022).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 4 |
| Minor | 3 |
| Positive | 5 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-GS-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 4L Super 10W-40 |
| ART-GS-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 4L — specs, AAI, STO, scratch code, штамп 2020 |
| ART-GS-003 | Document | wiki/46 | PGMM _full 4L (context) |
| ART-GS-004 | Web | [GPN-03](04_источники_и_URL.md) | Product page — **scrape blocked** 25.06.2026 |
| ART-GS-005 | Context | Firecrawl MCP 25.06.2026 | `ERR_TUNNEL_CONNECTION_FAILED` — auto-ingest **н/д** |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-GS-01 | Artifact | ART-GS-001 | GAZPROMNEFT logo; «**SUPER**»; «**ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» / «SEMISYNTHETIC ENGINE OIL» | A | Active |
| EVID-GS-02 | Artifact | ART-GS-001 | Front lockup: **10W-40 · API SG/CD · 4L** | A | Active |
| EVID-GS-03 | Artifact | ART-GS-001 | Orange/yellow/blue angular swirl-lite graphic + white car icon | A | Active |
| EVID-GS-04 | Artifact | ART-GS-001 | Footer OEM microtype: «**AVTOVAZ, ZMZ**» | A | Active |
| EVID-GS-05 | Artifact | ART-GS-002 | Back header: Super 10W-40; semi-synthetic RU/EN; **API SG/CD** | A | Active |
| EVID-GS-06 | Artifact | ART-GS-002 | Back spec: **ПАО «АВТОВАЗ»**; **Сертифицировано ААИ**; **СТО 84035624-058-2012** | A | Active |
| EVID-GS-07 | Artifact | ART-GS-002 | RU + multilingual body: полусинтетическое всесезонное; бензин/дизель ± turbo; wear/sludge claims | A | Active |
| EVID-GS-08 | Artifact | ART-GS-002 | Barcode **4650063110749**; **EAC**; **4L** | A | Active |
| EVID-GS-09 | Artifact | ART-GS-002 | «**Уникальный номер**» scratch authenticity zone | A | Active |
| EVID-GS-10 | Artifact | ART-GS-002 | Production stamp: **23.07.2020 · 2015073801** | A | Active |
| EVID-GS-11 | Artifact | ART-GS-002 | ООО «Газpromneft-Lubricants» · Moscow · **www.gazpromneft-oil.ru** | A | Active |
| EVID-GS-12 | Artifact | ART-GS-002 | **ZMZ / УМЗ на обороте не видны** | A | Active |
| EVID-GS-13 | Artifact | ART-GS-002 | **ACEA / ILSAC / modern API — absent** | A | Active |
| EVID-GS-14 | Context | ART-GS-003 | PGMM: swirl-lite M_SYSTEM; OEM partial front; oil-level strip | B | Context |
| EVID-GS-15 | Context | ART-GS-004 | GPN-03 URL registered wiki/04; site title per PGMM: полусинтетическое универсальное | C | **Pending digital** |
| EVID-GS-16 | Context | ART-GS-005 | Firecrawl scrape GPN-03: tunnel error — negative case | C | Negative case |

### Artifact vs canonical

| Поле | Artifact (фото 23.07.20) | Canonical (GPN-03 · pending) | Статус |
|------|--------------------------|------------------------------|--------|
| API | **SG/CD** front + back | **SG/CD** (PGMM/site title context) | ✅ aligned (photo) |
| Base oil | «ПОЛУСИНТЕТИЧЕСКОЕ» front + back EN/RU | Полусинтетическое универсальное (site title · pending) | ✅ aligned |
| OEM front | **AVTOVAZ · ZMZ** microtype | н/д verify | artifact-only |
| OEM back | **ПАО «АВТОВАЗ»** only | н/д verify | 🟡 **ZMZ lacuna** vs front |
| UMZ | **Absent** pack | н/д | artifact-only · gap vs LUKOIL |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-GS-01 GPN-03 digital triangulation | **Open** — Firecrawl blocked; manual screenshot optional |
| GAP-GS-02 Retail @1.2 m OEM microtype readability | Open |
| GAP-GS-03 TDS chemistry (HTHS, drain, SAPS) | Open |
| GAP-GS-04 Batch 2020 vs newer facings share | Open — **oldest** in 10W-40 peer pair |
| GAP-GS-05 Scratch-code verification channel (3662 vs unique number) | Open — differs from Premium N pattern |

---

## Findings Catalogue

### F-GS-01 — Positive · Cross-face API / base oil / SAE coherent

| Поле | Значение |
|------|----------|
| **Observation** | Front (GS-02): **10W-40 · API SG/CD · 4L** + полусинтетика (GS-01). Back (GS-05–07): идентичный API + semi claim. |
| **Evidence IDs** | EVID-GS-01; GS-02; GS-05; GS-07 |
| **Severity & Confidence** | **Positive** · **High** |

---

### F-GS-02 — Major · ZMZ on front · absent on back (split-face OEM)

| Поле | Значение |
|------|----------|
| **Observation** | Front (GS-04): **AVTOVAZ, ZMZ** microtype. Back (GS-06, GS-12): **ПАО «АВТОВАЗ»** only — **ZMZ not listed**. |
| **Evidence IDs** | EVID-GS-04; GS-06; GS-12 |
| **Impact** | Trust · Compliance (legacy domestic park · ZMZ engines) |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | quick: mirror ZMZ on back header; structural: unified OEM band all faces |
| **Falsification** | Back photo showing ZMZ; or site GPN-03 listing ZMZ back-only |

---

### F-GS-03 — Major · Domestic OEM stack incomplete vs peer (no UMZ)

| Поле | Значение |
|------|----------|
| **Observation** | GPN Super: AVTOVAZ (+ ZMZ front only). LUKOIL SUPER [44]: **АВТОВАЗ · УМЗ · ЗМЗ** back + site. **UMZ absent** on GPN pack. |
| **Evidence IDs** | EVID-GS-04; GS-06; GS-12; cross-ref [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) EVID-LS-06 |
| **Severity & Confidence** | **Major** · **High** (ЮФО / legacy segment) |

---

### F-GS-04 — Moderate · «SUPER» hyperbole vs API SG/CD legacy tier

| Поле | Значение |
|------|----------|
| **Observation** | «SUPER» + thermokinetic swirl-lite (GS-03) при **API SG/CD** — rhetoric premium vs chemistry budget. **Не split-face error** — claim inflation (parallel [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) F-LS-03 ActiPure). |
| **Evidence IDs** | EVID-GS-01; GS-02; GS-03 |
| **Severity & Confidence** | **Moderate** · **High** |

---

### F-GS-05 — Moderate · ACEA / ILSAC / modern API — absent (expected lacuna)

| Evidence IDs | EVID-GS-13 |
| **Observation** | Нет ACEA, ILSAC, SN+ — **consistent** с legacy 10W-40 segment. |
| **Severity** | **Moderate** · **High** (segment disclosure gap) |

---

### F-GS-06 — Positive · API SG/CD на фронте — budget honesty

| Evidence IDs | EVID-GS-02; cross-ref [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) F-LS-05 |
| **Observation** | Legacy API **explicit** on front — no silent upgrade narrative. |
| **Severity** | **Positive** · **High** |

---

### F-GS-07 — Positive · Semi-synthetic explicit front + back

| Evidence IDs | EVID-GS-01; GS-05; GS-07 |
| **Severity** | **Positive** · **High** |

---

### F-GS-08 — Positive · OEM partial front-load (delta vs LUKOIL back-only)

| Evidence IDs | EVID-GS-04; cross-ref [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) F-LS-02 |
| **Observation** | Domestic OEM **formally on front** — **↑ vs LUKOIL**; но **microtype @1.2 m fail** (GAP-GS-02). |
| **Severity** | **Positive** · **Medium** |

---

### F-GS-09 — Moderate · GPN-03 site triangulation blocked

| Evidence IDs | EVID-GS-15; GS-16 |
| **Observation** | Auto-scrape failed; digital claims **н/д** — cannot confirm site ≈ pack or superset gap. |
| **Severity** | **Moderate** · **Medium** |

---

### F-GS-10 — Positive · Institutional anti-fraud stack (scratch + AAI + STO)

| Evidence IDs | EVID-GS-09; GS-06; GS-08 |
| **Observation** | «Уникальный номер» scratch zone + **AAI** certification + **СТО 84035624-058-2012** — **↑ vs LUKOIL SUPER** (no scratch on photo [44]). |
| **Severity** | **Positive** · **High** |

---

### F-GS-11 — Minor · Batch 2020 — oldest facing in peer pair

| Evidence IDs | EVID-GS-10; cross-ref [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) EVID-LS-09 (2022) |
| **Severity** | **Minor** · **Medium** |

---

### F-GS-12 — Minor · Anti-fraud channel ≠ Premium N 3662.ru pattern

| Evidence IDs | EVID-GS-09; cross-ref [17](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) |
| **Observation** | Scratch «Уникальный номер» — **not** 3662.ru QR flow; verification UX **н/д** on photo. |
| **Severity** | **Minor** · **Medium** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-GS-01 | ZMZ front vs absent back | **Open** — F-GS-02; split-face OEM partial |
| CR-GS-02 | SUPER/swirl rhetoric vs API SG legacy | **Open** — F-GS-04; rhetoric vs chemistry, not API defect |
| CR-GS-03 | GPN domestic OEM ⊂ LUKOIL domestic OEM | **Open** — F-GS-03; segment gap, not contradiction |
| CR-GS-04 | Site vs pack specs | **Open** — GPN-03 pending (F-GS-09) |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — UMZ; ZMZ back; ACEA; GPN-03 digital; @1.2 m OEM. **Redundancy** — SUPER + semi + swirl + car + 10W-40 (×5). **Contamination** — swirl thermokinetics **colonises** semi-synthetic chemistry (PGMM context). **Collonisation** — GPN budget code over engineering legibility.

**Logical Coherence:** Cross-face API/semi **Pass**; OEM **Partial** (CR-GS-01). SUPER rhetoric **≠** chemistry tier — **Conflict** (F-GS-04).

**System Dynamics:** **Anomaly** — OEM **partial front** (↑ vs LUKOIL). **Potential** — scratch authenticity + AAI institutional stack. **Limit** — batch 2020; GPN-03 blocked; no retail @1.2 m.

**Relational States:** **Consensus** front ↔ back on core API/semi. **Compromise** — list ZMZ front, omit back. **Parity** with LUKOIL SUPER on API SG honesty; **delta** on OEM front-load vs stack depth.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 4L · rev. 1 locked · **point-ref**

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Universal Mass Heuristic + Thermokinetic Swirl Lite + Institutional Anxiety (scratch) + Domestic OEM Partial Front-Load | wiki/46; EVID-GS-14 | H |
| 2 | Carrier morphology (PGMM) | 4L silver-grey HDPE jug + integrated handle + oil-level strip | wiki/46; ART-GS-001 | H |
| 3 | Класс продукта (синт / полусинт) | **Полусинтетическое** · API **SG/CD** | EVID-GS-01; GS-02; GS-05–07 | H |
| 4 | SAE 10W-40 — legibility | **High** — oversized white on orange band | EVID-GS-02 | H |
| 5 | API — видимость (front / back) | **SG/CD · SG/CD** | EVID-GS-02; GS-05 | H |
| 6 | ACEA — видимость (front / back) | **Absent · Absent** (legacy segment) | EVID-GS-13 | H |
| 7 | OEM / допуски — front (effective) | **AVTOVAZ · ZMZ microtype** — listed, **@1.2 m fail** | EVID-GS-04; F-GS-08 | H |
| 8 | OEM / допуски — back / site / overlay | Back: **ПАО «АВТОВАЗ»** + AAI + STO · **ZMZ/УМЗ absent** · Site **pending** | EVID-GS-06; GS-12; GS-15 | H / L |
| 9 | Benefit-icons — доказуемость | Car icon + swirl **without** tribology proof; wear/sludge **text back only** | EVID-GS-03; GS-07 | M |
| 10 | Cross-face consistency | **Partial Pass** — API/semi Pass; **OEM ZMZ split** | EVID-GS-02 = GS-05; CR-GS-01 | H |
| 11 | Digital / overlay vs pack gap | **Pending** — GPN-03 scrape blocked | EVID-GS-15; GS-16; F-GS-09 | L |
| 12 | Anti-fraud UX | **Scratch «Уникальный номер» + EAC + barcode + batch** · ≠ 3662.ru | EVID-GS-09; GS-08; GS-10 | H |
| 13 | RF supply & языковая модель | Official GPN-Lubricants · Cyrillic front + multilang back | EVID-GS-01; GS-07; GS-11 | H |
| 14 | Обязательная маркировка РФ | **EAC · barcode · batch · 4L · STO · AAI** | EVID-GS-06; GS-08; GS-10 | H |
| 15 | Кириллица vs латиница | **Кириллица dominant** front + EN semi line back header | EVID-GS-01; GS-05 | H |
| 16 | Thumbnail robustness (~120 px) | **High** — SUPER + 10W-40 + GPN; OEM microtype **marginal** | wiki/46; EVID-GS-02 | H |
| 17 | Cognitive load / negative space | **Medium front / high back** — swirl redundancy + dense legal | wiki/46 | H |
| 18 | Legacy / rev. risk на полке | **Moderate** — stable SG/CD wrap; batch **2020** oldest peer · site verify pending | EVID-GS-10; GS-15 | M |

---

## Импликации для СТМ (Classic/Protect · 10W-40)

1. **Перенять:** readable **SAE + API front** + **semi-synthetic honesty** + **readable domestic OEM band** (front **and** back parity).
2. **Не копировать:** SUPER hyperbole + swirl void + ZMZ front/back split.
3. **Attack vector:** honest **SN/CF** (if chemistry matches) + **full domestic stack** (AVTOVAZ·UMZ·ZMZ) readable @1.2 m + named additive metric.
4. **Institutional layer:** GPN scratch-code **strong** — СТМ needs equivalent proof, not necessarily clone.
5. Point-ref — **отдельные строки** 4L / 1L; cross-ref peer [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md).

---

## Issues for discussion

1. **GPN-03 verify:** manual screenshot / browser ingest to close CR-GS-04.
2. **10W-40 matrix branch:** включать GPN Super + LUKOIL SUPER как point-ref pair?
3. **ZMZ back lacuna:** intentional front-tease or label defect — verify fresh facings.
4. Cross-ref 1L: [49](49_ODSA_Gazpromneft_Super_10W-40_1L.md) · PGMM delta [47](47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md).

**DoD:** ODSA GPN Super 10W-40 **4L — complete** (rev. 1 photo locked). Pending: GPN-03 digital, GAP-GS-02 retail distance.
