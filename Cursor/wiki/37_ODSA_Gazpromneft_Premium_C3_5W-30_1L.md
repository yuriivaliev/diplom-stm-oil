# ODSA — Gazpromneft Premium C3 5W-30 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_GPN_PREMIUM_C3_5W30_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [33_PGMM_Gazpromneft_Premium_C3_5W-30_1L_delta.md](33_PGMM_Gazpromneft_Premium_C3_5W-30_1L_delta.md) · base 4L ODSA: [36_…](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md)  
**Дата:** 25.06.2026 · **Rev. 1:** locked (front + back photo + site)  
**Формат:** 1L · фронт + оборот (фото) + GPN-02

> **Отличие от GPN Premium N 1L:** back **не inherit** — фото оборота 1L **привязано** (EVID-GC3D-05–10).

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **Gazpromneft Premium C3 5W-30 1L** — **API SP** · **ACEA C2/C3** · **dexos2™** (GPN-02).

**Cross-face (фото):** **Pass** — front **API SN + ACEA C3** = back photo **SN + C3** (EVID-GC3D-02, GC3D-05). **Canon override:** **API SP + ACEA C2/C3** (F-GC3D-01).

**Cross-format (1L ↔ 4L):** **Pass** at canon; photo-era **SN** on both 1L faces vs **SP** on 4L front — **legacy artifact**, not inter-format API tier.

**Doliv-channel gaps:** OEM microtype **↓ fail** (F-GC3D-02); authenticity front deferral **absent** vs 4L (F-GC3D-03); no top-up claim on label (F-GC3D-04).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 4 |
| Minor | 2 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-GC3D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L — SN/C3, dexos2 hero, Ford 917A |
| ART-GC3D-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 1L — SN/C3, OEM grid, штамп 20.03.2017 |
| ART-GC3D-003 | Document | wiki/33 | PGMM delta 1L |
| ART-GC3D-004 | Document | wiki/36 | ODSA 4L — cross-format ref |
| ART-GC3D-005 | Artifact (screenshot) | GPN-02 · operator 25.06.2026 | Site canon Premium C3 5W-30 |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-GC3D-01 | Artifact | ART-GC3D-001 | «PREMIUM C3»; «СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО»; **5W-30**; **1L** | A | Active |
| EVID-GC3D-02 | Artifact | ART-GC3D-001 | Front: **API SN** · **ACEA C3** · **dexos2™** center logo | A | Active · **photo artifact** |
| EVID-GC3D-03 | Artifact | ART-GC3D-001 | OEM microtype: **MB 229.51** · **Ford 917A** · **VW 502 00/505 00/505 01** · **BMW Longlife-04** | B | Active |
| EVID-GC3D-04 | Artifact | ART-GC3D-001 | Diagonal **grip-ridges** + **translucent fill strip** on carrier | A | Active |
| EVID-GC3D-05 | Artifact | ART-GC3D-002 | Back header: **API SN** · **ACEA C3** · dexos2 | A | Active |
| EVID-GC3D-06 | Artifact | ART-GC3D-002 | OEM: MB 229.51 · Ford WSS-M2C917-A · VW 502/505 · BMW LL-04 · **СТО 84035624-183-2015** | A | Active |
| EVID-GC3D-07 | Artifact | ART-GC3D-002 | RU+EN: energy-saving synthetic; DPF/TWC; **Gazpromneft MLP** Fryazino | A | Active |
| EVID-GC3D-08 | Artifact | ART-GC3D-002 | Barcode **4 650063 116109**; unique code **GPN-02-01-11-12**; **EAC**; RB2C1030093 | A | Active |
| EVID-GC3D-09 | Artifact | ART-GC3D-002 | Production stamp: **20.03.2017** · batch **1711022801** | A | Active |
| EVID-GC3D-10 | Artifact | ART-GC3D-005 (GPN-02) | Site: **API SP** · **ACEA C2/C3** · dexos2 · full OEM stack | A | **Canonical digital** |
| EVID-GC3D-11 | Context | ART-GC3D-003 | PGMM: DRY vertical rescale; authenticity front **lost** on 1L | B | Context |
| EVID-GC3D-12 | Cross-format | ART-GC3D-004 · [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) | 4L ref EVID-GC3-02–07 | B | Active |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-GC3D-01 Site card: 1L vs 4L SKU split | Open — одна line card GPN-02 |
| GAP-GC3D-02 Opel/Iveco on 1L vs 4L front microtype | Open — set delta |
| GAP-GC3D-03 Current 2025/26 facing vs 2017 photo | Open — retail audit |

---

## Findings Catalogue

### F-GC3D-01 — Major · Legacy API SN on photo — superseded by canon SP

| Поле | Значение |
|------|----------|
| **Observation** | Front+back photo: **API SN + ACEA C3** (EVID-GC3D-02, GC3D-05). GPN-02: **API SP + ACEA C2/C3**. Batch **20.03.2017**. |
| **Evidence IDs** | EVID-GC3D-02; GC3D-05; GC3D-09; GC3D-10 |
| **Interpretation** | **Not inter-format stratification** — retail photo lag. **Canon SP > SN** project-wide. Cross-face **Pass on photo** (SN=SN). |
| **Severity & Confidence** | **Major** (artifact) · **Closed at canon** · **High** |

---

### F-GC3D-02 — Major · OEM microtype below doliv functional threshold

| Поле | Значение |
|------|----------|
| **Observation** | Top-up 1L: OEM listed (EVID-GC3D-03) but **microtype** — below decode @ arm's length; back grid (GC3D-06) **не виден** при doliv impulse. |
| **Evidence IDs** | EVID-GC3D-03; GC3D-06; GC3D-11 |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | quick: 2 OEM icons front 1L; structural: top-up semantic + readable OEM band |

---

### F-GC3D-03 — Moderate · Authenticity front deferral absent vs 4L

| Evidence IDs | EVID-GC3D-01; [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) EVID-GC3-04 |
| **Observation** | 4L front: «УНИКАЛЬНАЯ СИСТЕМА ПРОВЕРКИ…»; **1L front: absent** |
| **Severity** | **Moderate** · **High** |

---

### F-GC3D-04 — Moderate · No top-up rationale on 1L label

| Evidence IDs | EVID-GC3D-01; GC3D-04 |
| **Observation** | Fill strip on **carrier** only; нет «doliv» / controlled-pour claim on K/S |
| **Severity** | **Moderate** · **Medium** |

---

### F-GC3D-05 — Moderate · dexos2 center hero — canon SKU signal

| Evidence IDs | EVID-GC3D-02; GC3D-05; GC3D-10 |
| **Observation** | dexos2™ **centered on swirl** front+back; **= GPN-02**; not «1L-only» artifact |
| **Severity** | **Moderate** · **Positive channel** · **High** |

---

### F-GC3D-06 — Moderate · Ford 917A ↑ vs 4L OEM row

| Evidence IDs | EVID-GC3D-03; GC3D-06; [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) EVID-GC3-03 |
| **Observation** | Ford WSS-M2C917-A prominent on 1L; Opel/Iveco **absent** vs 4L front microtype |
| **Severity** | **Moderate** · **Medium** |

---

### F-GC3D-07 — Minor · STO 183-2015 (1L) vs 103-2015 (4L photo)

| Evidence IDs | EVID-GC3D-06; [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) EVID-GC3-07 |
| **Severity** | **Minor** · **Medium** |

---

### F-GC3D-08 — Minor · Batch 2017 — legacy facing

| Evidence IDs | EVID-GC3D-09 |
| **Severity** | **Minor** · **Medium** |

---

### F-GC3D-09 — Positive · Cross-face Pass on photo (SN=SN, C3=C3)

| Evidence IDs | EVID-GC3D-02; GC3D-05 |
| **Severity** | **Positive** · **High** |

---

### F-GC3D-10 — Positive · dexos2 triangulated front + back + site

| Evidence IDs | EVID-GC3D-02; GC3D-05; GC3D-10 |
| **Severity** | **Positive** · **High** |

---

### F-GC3D-11 — Positive · Cross-format canon Pass (1L ↔ 4L API tier)

| Evidence IDs | EVID-GC3D-10; [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) EVID-GC3-11 |
| **Observation** | **API SP + ACEA C2/C3** един для 1L/4L по GPN-02 |
| **Severity** | **Positive** · **High** |

---

### F-GC3D-12 — Positive · Front 5W-30 + C3 segment readable on 1L after rescale

| Evidence IDs | EVID-GC3D-01; GC3D-02 |
| **Severity** | **Positive** · **High** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-GC3D-01 | Photo SN vs canon SP | **Closed** — F-GC3D-01 |
| CR-GC3D-02 | OEM front vs back (doliv) | **Open** — F-GC3D-02 |
| CR-GC3D-03 | Authenticity 4L front vs 1L absent | **Open** — F-GC3D-03 |
| CR-GC3D-04 | ACEA C2 on canon vs C3-only on photo | **Closed** — canon C2/C3 |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — OEM front effective; authenticity front; top-up claim. **Redundancy** — PREMIUM C3 + C3 + dexos2 + ACEA. **Contamination** — dexos2 **colonises** swirl center.

**Logical Coherence:** Photo cross-face **Pass**; canon SP **closed** evolution gap.

**System Dynamics:** **Potential** — dexos2 GM doliv niche; **Limit** — 2017 photos in wild.

**Relational States:** **Parity** M_SYSTEM with 4L; **Compromise** — DRY rescale vs service-jug authority lost.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> 1 format = 1 row · rev. 1 locked

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | = 4L · Spec-as-Brand + Swirl + Back-Load | wiki/33; EVID-GC3D-11 | H |
| 2 | Carrier morphology (PGMM) | Narrow 1L bottle + grip-ridges + fill strip (≠ 4L jug) | EVID-GC3D-04; wiki/33 | H |
| 3 | Класс продукта (синт / полусинт) | **Синтетическое** · API **SP** (canon) | EVID-GC3D-01; GC3D-07; GC3D-10 | H |
| 4 | SAE 5W-30 — legibility | **High** (rel. ↑ on narrow label) | EVID-GC3D-01; GC3D-02 | H |
| 5 | API — видимость (front / back) | Photo: **SN · SN** · **Canon: SP · SP** | EVID-GC3D-02; GC3D-05; GC3D-10; F-GC3D-01 | H |
| 6 | ACEA — видимость (front / back) | Photo: **C3 · C3** · **Canon: C2/C3 · C2/C3** | EVID-GC3D-02; GC3D-05; GC3D-10 | H |
| 7 | OEM / допуски — front (effective) | **Listed, microtype** — **нечитаемо** @ doliv | EVID-GC3D-03; F-GC3D-02 | H |
| 8 | OEM / допуски — back / site / overlay | Back: MB 229.51, Ford 917A, VW 502/505, BMW LL-04, STO 183 · Site = GPN-02 full stack | EVID-GC3D-06; GC3D-10 | H / M |
| 9 | Benefit-icons — доказуемость | dexos2 **named center** · DPF/TWC **text back** · swirl **cropped** | EVID-GC3D-02; GC3D-07; wiki/33 | M |
| 10 | Cross-face consistency | Photo: **Pass** (SN=SN) · **Canon: Pass** (SP) | EVID-GC3D-02; GC3D-05; GC3D-10 | H |
| 11 | Digital / overlay vs pack gap | Site **superset** vs 2017 photo (SP, C2, extended OEM) | EVID-GC3D-10 vs GC3D-02/06 | M |
| 12 | Anti-fraud UX | Back code **GPN-02-01-11-12** + EAC + batch · **no front deferral** | EVID-GC3D-08; GC3D-09; F-GC3D-03 | M |
| 13 | RF supply & языковая модель | Official **Gazpromneft MLP** Fryazino · Cyrillic front + multilingual back | EVID-GC3D-07 | H |
| 14 | Обязательная маркировка РФ | EAC · license RB2C1030093 · shelf life 5 yr · 1L | EVID-GC3D-08; GC3D-07 | H |
| 15 | Кириллица vs латиница | Cyrillic type row + EN back body | EVID-GC3D-01; GC3D-07 | H |
| 16 | Thumbnail robustness (~120 px) | **Med-high** — GPN + 5W-30 + **dexos2** ✅ · OEM microtype ✗ · 1L ✗ | wiki/33 §6; F-GC3D-02 | M |
| 17 | Cognitive load / negative space | **High** — compressed rescale + dense back | wiki/33 | H |
| 18 | Legacy / rev. risk на полке | **Moderate** — batch **2017**; canon SP on GPN-02 | EVID-GC3D-09; GC3D-10 | M |

---

## Импликации для СТМ (1L C3 proxy)

1. **Attack vector:** readable OEM band (2–3) + **front QR/authenticity** + top-up semantic — GPN C3 1L **не закрывает**.
2. **Не копировать:** blind DRY-rescale without doliv claims; dexos2 unless OEM program exists.
3. **Separate matrix row** от 4L; **API tier один** (SP canon).

---

## Issues for discussion

1. Authenticity front gap 1L vs 4L — packaging delta or oversight?
2. STO 103 vs 183 — unified corporate spec on current facings?
3. Pair with [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) + [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) in C3 point-ref.

**DoD:** ✅ ODSA GPN Premium C3 5W-30 **1L — locked rev. 1**.
