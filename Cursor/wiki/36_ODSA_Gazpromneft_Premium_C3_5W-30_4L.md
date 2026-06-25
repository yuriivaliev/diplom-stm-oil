# ODSA — Gazpromneft Premium C3 5W-30 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_GPN_PREMIUM_C3_5W30_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [32_PGMM_Gazpromneft_Premium_C3_5W-30.md](32_PGMM_Gazpromneft_Premium_C3_5W-30.md) · delta 1L: [33_…](33_PGMM_Gazpromneft_Premium_C3_5W-30_1L_delta.md)  
**Дата:** 25.06.2026 · **Rev. 1:** locked (front + back + site triangulation)  
**Формат:** 4L · фронт + оборот + официальный сайт  
**Canonical URL:** [GPN-02](04_источники_и_URL.md) · operator screenshot 25.06.2026 (= PGMM ingest)

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **Gazpromneft Premium C3 5W-30 4L** — fully synthetic Low-SAPS · **API SP** · **ACEA C2/C3** · **dexos2™** · расширенный OEM stack на сайте (GPN-02).

**Cross-face (фото-артефакт):** **Fail на batch 2017** — front **API SP + ACEA C2/C3** (EVID-GC3-02) vs back **API SN + ACEA C3** (EVID-GC3-06). **Closed на уровне SKU** правилом **SP > SN** + triangulation GPN-02 (F-GC3-01, CR-GC3-01).

**Cross-face (канон):** **Pass** — **API SP + ACEA C2/C3** front = site = target wrap rev.

**Ключевые gaps:** (1) OEM на фронте **перечислены**, но **microtype** — ниже порога @1.2 m (F-GC3-02); (2) **digital superset** — сайт декларирует полный OEM stack (Renault RN17, Fiat, MB 229.31/52…), **не зеркалится** на видимых faces фото (F-GC3-03); (3) **legacy facing** на фото — batch **21.10.2017** (F-GC3-07).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 3 |
| Moderate | 4 |
| Minor | 2 |
| Positive | 3 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-GC3-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 4L — API SP, ACEA C2/C3, OEM microtype, authenticity deferral |
| ART-GC3-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 4L — API SN, ACEA C3, OEM grid, штамп 21.10.2017 |
| ART-GC3-003 | Document | wiki/32 | PGMM _full 4L (context) |
| ART-GC3-004 | Document | wiki/33 | PGMM delta 1L (cross-format ref) |
| ART-GC3-005 | Artifact (screenshot) | Оператор 25.06.2026 · PGMM ingest | GPN-02: «Ключевые характеристики» Premium C3 5W-30 |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-GC3-01 | Artifact | ART-GC3-001 | «PREMIUM C3»; «СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО»; **5W-30**; **4L**; GPN logo | A | Active |
| EVID-GC3-02 | Artifact | ART-GC3-001 | Front lockup: **API SP** · **ACEA C2/C3** | A | Active |
| EVID-GC3-03 | Artifact | ART-GC3-001 | OEM microtype: **MB 229.51/229.52** · **VW 505 00/505 01** · **BMW Longlife-04** · **Opel OV0401547** · **Iveco 18-1811 SC1** | B | Active |
| EVID-GC3-04 | Artifact | ART-GC3-001 | «УНИКАЛЬНАЯ СИСТЕМА ПРОВЕРКИ ПОДЛИННОСТИ (СМ. НА ОБОРОТЕ)» | A | Active |
| EVID-GC3-05 | Artifact | ART-GC3-001 | 3D orange/yellow/blue swirl + car icon | A | Active |
| EVID-GC3-06 | Artifact | ART-GC3-002 | Back header: Premium C3 5W-30; **API SN** · **ACEA C3** | A | Active · **photo artifact** |
| EVID-GC3-07 | Artifact | ART-GC3-002 | OEM row: **MB 229.51** · **VW 502 00/505 00/505 01** · **BMW Longlife-04** · **СТО 84035624-103-2015** | A | Active |
| EVID-GC3-08 | Artifact | ART-GC3-002 | RU+EN body: fully synthetic; gasoline + diesel + DPF/TWC; low SAPS | A | Active |
| EVID-GC3-09 | Artifact | ART-GC3-002 | Barcode **4 650063 115330**; **EAC**; www.gazpromneft-oil.com | A | Active |
| EVID-GC3-10 | Artifact | ART-GC3-002 | Production stamp: **21.10.2017** · batch **171110840/** | A | Active |
| EVID-GC3-11 | Artifact | ART-GC3-005 (GPN-02) | Site canon: **API SP** · **ACEA C2/C3** · **dexos2**; MB **229.31/51/52** · VW **505 00/01** · BMW **LL-04** · Renault **RN17** · Opel · Fiat · Iveco **18-1811 SC1** | A | **Canonical digital** |
| EVID-GC3-12 | Context | ART-GC3-003 | PGMM: spec-in-name; OEM microtype suppression; MSYS_GC3_01–03 | B | Context |
| EVID-GC3-13 | Context | [GPN-02](04_источники_и_URL.md) | URL registry · verified via operator screenshot 25.06.2026 | A | Active |

### Conflict notes

| Conflict | Evidence | Resolution |
|----------|----------|------------|
| API SP (front photo) vs SN (back photo) | GC3-02 vs GC3-06 | **Closed (CR-GC3-01)** — legacy batch 2017; **canon SP** (GPN-02) supersedes |
| ACEA C2/C3 (front) vs C3-only (back photo) | GC3-02 vs GC3-06 | **Closed** — same evolution rule; **canon C2/C3** |
| VW 505 (front microtype) vs 502/505 (back) | GC3-03 vs GC3-07 | **Open (CR-GC3-02)** — notation/set variant, not split-grade |
| Physical pack vs digital OEM | GC3-03/07 vs GC3-11 | **Open (CR-GC3-03)** — site superset (F-GC3-03) |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-GC3-01 Retail @1.2 m OEM readability | Open — н/д |
| GAP-GC3-02 TDS PDF chemistry (SAPS ppm, HTHS) | Open — н/д |
| GAP-GC3-03 Share of 2017 vs current facings on shelf | Open — н/д |
| GAP-GC3-04 Auto-scrape GPN-02 | **Closed** — operator screenshot (= PGMM); scrape blocked pattern as GPN-01 |

---

## Findings Catalogue

### F-GC3-01 — Major · Photo cross-face API/ACEA drift (legacy artifact)

| Поле | Значение |
|------|----------|
| **Observation** | Front (EVID-GC3-02): **API SP + ACEA C2/C3**. Back photo (EVID-GC3-06): **API SN + ACEA C3**. Batch **21.10.2017**. |
| **Evidence IDs** | EVID-GC3-02; GC3-06; GC3-10; GC3-11 |
| **Interpretation** | **Product evolution** (SN→SP) + partial relabel on back of same physical unit — **не** inter-SKU split. **Канон SKU = API SP + ACEA C2/C3** (GPN-02). |
| **Severity & Confidence** | **Major** (artifact) · **Closed at canon** · **High** |
| **Recommendations** | governance: single-source spec front=back=site; structural: relabel back on reformulation |

---

### F-GC3-02 — Major · OEM stack on front — present but below shelf-readability

| Поле | Значение |
|------|----------|
| **Observation** | OEM **перечислены** в microtype footer (EVID-GC3-03), но PGMM (EVID-GC3-12) фиксирует **suppression** → нечитаемо @1.2 m. |
| **Evidence IDs** | EVID-GC3-03; GC3-12 |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | quick: 2–3 top OEM icons; structural: readable OEM band above 5W-30 |

---

### F-GC3-03 — Major · Digital OEM superset not mirrored on physical label (photo)

| Поле | Значение |
|------|----------|
| **Observation** | Site GPN-02 (EVID-GC3-11): **dexos2**, **Renault RN17**, **Fiat**, **MB 229.31**, full VW stack — **отсутствуют или сужены** на faces GC3-03/07. |
| **Evidence IDs** | EVID-GC3-03; GC3-07; GC3-11 |
| **Interpretation** | Channel asymmetry pack ↔ web; усиливается back parity rule из wiki/17. |
| **Severity & Confidence** | **Major** · **Medium** (TDS н/д) |

---

### F-GC3-04 — Moderate · dexos2 — site canon, absent on 4L photo faces

| Evidence IDs | EVID-GC3-11; GC3-02; GC3-06 |
| **Observation** | dexos2™ на GPN-02; **не виден** на фото front/back 4L (batch 2017). На 1L photo — present (cross-ref [37](37_ODSA_Gazpromneft_Premium_C3_5W-30_1L.md)). |
| **Severity** | **Moderate** · **High** |

---

### F-GC3-05 — Moderate · ACEA C2 — front photo + canon vs back photo C3-only

| Evidence IDs | EVID-GC3-02; GC3-06; GC3-11 |
| **Severity** | **Moderate** · **High** · closed at canon |

---

### F-GC3-06 — Moderate · СТО 84035624-103-2015 — back only; drift vs 1L STO 183

| Evidence IDs | EVID-GC3-07; [37](37_ODSA_Gazpromneft_Premium_C3_5W-30_1L.md) EVID-GC3D-09 |
| **Observation** | Корпоративный СТО на обороте; **разные номера** 103 (4L photo) vs 183 (1L photo) — batch/format institutional drift |
| **Severity** | **Moderate** · **Medium** |

---

### F-GC3-07 — Minor · Batch 2017 — legacy facing shelf risk

| Evidence IDs | EVID-GC3-10 |
| **Severity** | **Minor** · **Medium** |

---

### F-GC3-08 — Minor · VW 502 00 on back vs 505 on front microtype

| Evidence IDs | EVID-GC3-03; GC3-07 |
| **Severity** | **Minor** · **Medium** · notation/set variant |

---

### F-GC3-09 — Positive · Front API SP + ACEA C2/C3 lockup (vs GPN Premium N norm)

| Evidence IDs | EVID-GC3-02; cross-ref [17](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) |
| **Severity** | **Positive** · **High** |

---

### F-GC3-10 — Positive · Anti-fraud deferral front → back (GPN family pattern)

| Evidence IDs | EVID-GC3-04; cross-ref [17](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) EVID-G03 |
| **Severity** | **Positive** · **High** |

---

### F-GC3-11 — Positive · Cross-face coherent at canon SKU level

| Evidence IDs | EVID-GC3-02; GC3-11; F-GC3-01 |
| **Observation** | После triangulation **SP + C2/C3** — единый claim для матрицы |
| **Severity** | **Positive** · **High** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-GC3-01 | API SP (front photo) vs SN (back photo) | **Closed** — evolution + canon (F-GC3-01) |
| CR-GC3-02 | VW 502/505 notation front vs back | **Open** — set variant |
| CR-GC3-03 | Physical OEM ⊂ Digital OEM (GPN-02) | **Open** — F-GC3-03 |
| CR-GC3-04 | Front OEM listed vs readable | **Open** — F-GC3-02 |

---

## POV-маркировка

**Information Integrity**
- *Lacunae:* dexos2 on 4L photo; TDS; retail @1.2 m.
- *Redundancy:* «PREMIUM C3» + ACEA C2/C3 + «СИНТЕТИЧЕСКОЕ» — четырёхслойное C3-кодирование.
- *Contamination:* thermokinetic swirl over Low-SAPS chemistry (PGMM).
- *Collonisation:* «C3» in line name borrows normative ACEA authority.

**Logical Coherence**
- *Conflicts:* photo SP/SN — **closed at canon**.
- *Contradictions:* CR-GC3-03 = superset gap, not API/base contradiction.

**System Dynamics**
- *Anomalies:* spec-in-name «C3» — rare RU heuristic.
- *Potentials:* front SP/C2/C3 — white space vs mass-mid.
- *Limits:* 2017 photo batch; OEM microtype dead zone.

**Relational States**
- *Compromise:* list OEM on front, hide in footer.
- *Parities:* with Premium N — shared GPN swirl + anti-fraud; **stronger** front spec row.
- *Consensus:* canon SP/C2/C3 via GPN-02.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 4L · rev. 1 locked

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Spec-as-Brand + Thermokinetic Swirl + Institutional Back-Load | wiki/32; EVID-GC3-12 | H |
| 2 | Carrier morphology (PGMM) | 4L silver HDPE jug + integrated handle + embossed G logo | wiki/32; ART-GC3-001 | H |
| 3 | Класс продукта (синт / полусинт) | **Синтетическое** · API **SP** (canon) | EVID-GC3-01; GC3-08; GC3-11 | H |
| 4 | SAE 5W-30 — legibility | **High** — oversized white on orange | EVID-GC3-01 | H |
| 5 | API — видимость (front / back) | Photo: **SP · SN** · **Canon: SP · SP** | EVID-GC3-02; GC3-06; GC3-11; F-GC3-01 | H |
| 6 | ACEA — видимость (front / back) | Photo: **C2/C3 · C3** · **Canon: C2/C3 · C2/C3** | EVID-GC3-02; GC3-06; GC3-11 | H |
| 7 | OEM / допуски — front (effective) | **Listed, microtype** — формально есть, **нечитаемо** @1.2 m | EVID-GC3-03; F-GC3-02 | H |
| 8 | OEM / допуски — back / site / overlay | Back photo: MB 229.51, VW 502/505, BMW LL-04, STO 103 · Site **superset**: +229.31/52, Renault RN17, Opel, Fiat, Iveco, dexos2 | EVID-GC3-07; GC3-11; F-GC3-03 | H / M |
| 9 | Benefit-icons — доказуемость | **Low** — thermokinetic swirls + car icon; DPF/TWC **text back only** | EVID-GC3-05; GC3-08; wiki/32 | M |
| 10 | Cross-face consistency | Photo: **Fail** (SP/SN) · **Canon: Pass** | EVID-GC3-02; GC3-06; GC3-11; F-GC3-01 | H |
| 11 | Digital / overlay vs pack gap | **Site superset** — dexos2 + extended OEM vs photo pack | EVID-GC3-11 vs GC3-03/07; F-GC3-03 | M |
| 12 | Anti-fraud UX | Front deferral «см. на обороте» + EAC + batch stamp + site pattern (3662 family) | EVID-GC3-04; GC3-09; GC3-10; F-GC3-10 | H |
| 13 | RF supply & языковая модель | Official RU · Cyrillic front + multilingual back · gazpromneft-oil.com | EVID-GC3-01; GC3-08; GC3-09 | H |
| 14 | Обязательная маркировка РФ | **EAC** · штамп · партия · barcode · 4L | EVID-GC3-09; GC3-10 | H |
| 15 | Кириллица vs латиница | **Кириллица dominant** front type row; PREMIUM C3 латиница | EVID-GC3-01 | H |
| 16 | Thumbnail robustness (~120 px) | **Med-high** — GPN + 5W-30 + swirl; OEM microtype **↓** | wiki/32; F-GC3-02 | M |
| 17 | Cognitive load / negative space | **Medium-high** front · **very high** back legal wall | wiki/32 | H |
| 18 | Legacy / rev. risk на полке | **Moderate** — photo batch **2017**; current wrap **SP** on site + 4L front photo | EVID-GC3-10; GC3-11; F-GC3-07 | M |

---

## Импликации для СТМ

1. **Перенять:** front **API + ACEA C2/C3** row для C3 SKU — GPN C3 сильнее Premium N и on par с GENESIS GC.
2. **Не копировать:** OEM microtype footer; photo-era cross-face drift — СТМ = **single-source spec** all faces.
3. **White space:** readable OEM band (MB/VW/BMW top-3) + **dexos2-equivalent** only if program exists.
4. Point-ref 5W-30 C3 — **отдельная строка** от 5W-40/0W-20 матриц.

---

## Issues for discussion

1. Добавить **GPN-02** verbatim block в wiki/04 — **done** rev. 1 ingest.
2. Back parity vs GPN-02 full stack — governance как wiki/17 F-G11?
3. Pair with [37](37_ODSA_Gazpromneft_Premium_C3_5W-30_1L.md) in C3 point-ref table.

**DoD:** ✅ ODSA GPN Premium C3 5W-30 **4L — locked rev. 1**.
