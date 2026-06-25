# ODSA — Gazpromneft Super 10W-40 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_GPN_SUPER_10W40_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md](47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md) · base 4L ODSA: [48_…](48_ODSA_Gazpromneft_Super_10W-40_4L.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (front + **back photo locked**)  
**Формат:** 1L · official RF wrap · фронт + оборот  
**Статус:** ✅ **Locked** (photo)

> **Не inherit:** оборот 1L **на фото** (как LUKOIL SUPER 1L [45]). Cross-format с [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md): primary claims **константа**; delta = объём + carrier + anti-fraud lacuna.

**Canonical URL:** [GPN-03](04_источники_и_URL.md) · line-level specs shared with 4L · **pending verify**

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **Gazpromneft Super 10W-40 1L** — полусинтетическое · **API SG/CD** · domestic OEM partial (**AVTOVAZ · ZMZ** front; **ПАО «АВТОВАЗ»** back).

**Cross-face 1L:** **Partial Pass** — front API SG/CD + semi = back (EVID-GS1D-01–07); **ZMZ front / absent back** inherited pattern (CR-GS1D-01).

**Cross-format (1L ↔ 4L):** **Pass** — API / base oil / OEM set **согласованы**; delta: **1L marker**, narrow bottle, **scratch code н/д** on 1L photo, batch **2022** vs 4L **2020**.

**1L-specific:** OEM front microtype **robust @ close range** (F-GS1D-03 Positive); **↓** oil-level strip vs 4L (PGMM context); **↓** scratch authenticity visibility (F-GS1D-07).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 3 |
| Moderate | 4 |
| Minor | 2 |
| Positive | 5 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-GS1D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L |
| ART-GS1D-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 1L |
| ART-GS1D-003 | Document | wiki/47 | PGMM delta 1L |
| ART-GS1D-004 | Document | wiki/48 | ODSA 4L — cross-format ref |
| ART-GS1D-005 | Web | [GPN-03](04_источники_и_URL.md) | Line specs — pending |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-GS1D-01 | Artifact | ART-GS1D-001 | GAZPROMNEFT; «**SUPER**»; «**ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» / «SEMI-SYNTHETIC ENGINE OIL» | A | Active |
| EVID-GS1D-02 | Artifact | ART-GS1D-001 | Front lockup: **10W-40 · API SG/CD · 1L** | A | Active |
| EVID-GS1D-03 | Artifact | ART-GS1D-001 | Footer OEM microtype: «**AVTOVAZ, ZMZ**» | A | Active |
| EVID-GS1D-04 | Artifact | ART-GS1D-001 | Narrow bottle + diagonal grip ridges; **no integrated handle** | A | Active |
| EVID-GS1D-05 | Artifact | ART-GS1D-002 | Back: Super 10W-40; semi-synthetic; **API SG/CD** | A | Active |
| EVID-GS1D-06 | Artifact | ART-GS1D-002 | **ПАО «АВТОВАЗ»**; **СТО 84035624-058-2012** | A | Active |
| EVID-GS1D-07 | Artifact | ART-GS1D-002 | RU application brief: wear, sludge, oxidation; gasoline/diesel ± turbo | A | Active |
| EVID-GS1D-08 | Artifact | ART-GS1D-002 | Barcode **4650063110756** (≠ 4L 4650063110749) | A | Active |
| EVID-GS1D-09 | Artifact | ART-GS1D-002 | **EAC**; **1L**; Made in Russia; Gazpromneft-Lubricants Ltd. | A | Active |
| EVID-GS1D-10 | Artifact | ART-GS1D-002 | Production stamp: **08.09.2022 · 2214116601** | A | Active |
| EVID-GS1D-11 | Artifact | ART-GS1D-002 | **Scratch «Уникальный номер» — не виден** на фото 1L back | A | Active |
| EVID-GS1D-12 | Artifact | ART-GS1D-002 | **ZMZ / УМЗ / AAI — не видны** на back photo | A | Active |
| EVID-GS1D-13 | Cross-format | ART-GS1D-004 · [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) | 4L batch 2020 vs 1L 2022 — same wrap rev. family | B | Active |
| EVID-GS1D-14 | Context | ART-GS1D-003 | PGMM delta: OEM front survives @ doliv; oil-level strip lost; scratch lacuna | B | Context |

### Artifact vs canonical (1L)

| Поле | Artifact (фото 08.09.22) | 4L ref [48] | Статус |
|------|--------------------------|-------------|--------|
| API | **SG/CD** front + back | SG/CD | ✅ cross-format aligned |
| STO | **84035624-058-2012** | 058-2012 | ✅ **same STO** (PGMM delta STO-001 inference **closed**) |
| OEM front | AVTOVAZ · ZMZ | Same | ✅ |
| OEM back | ПАО «АВТОВАЗ» only | Same + AAI on 4L photo | 🟡 AAI **н/д** on 1L crop |
| Scratch code | **Absent on photo** | Present 4L | 🟡 format lacuna or crop |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-GS1D-01 Scratch code on 1L back | **Open** — not visible (vs 4L EVID-GS-09) |
| GAP-GS1D-02 AAI certification on 1L back | **Open** — not in crop; may be below fold |
| GAP-GS1D-03 GPN-03 line-level digital | Open — scrape blocked |
| GAP-GS1D-04 Retail @1.2 m doliv channel | Open |

---

## Findings Catalogue

### F-GS1D-01 — Positive · Cross-face 1L coherent (photo locked)

| Evidence IDs | EVID-GS1D-01; GS1D-02; GS1D-05; GS1D-07 |
| **Observation** | Front SG/CD + semi = back. **No inherit dependency.** |
| **Severity** | **Positive** · **High** |

---

### F-GS1D-02 — Major · ZMZ front · absent back (inherits 4L pattern)

| Evidence IDs | EVID-GS1D-03; GS1D-06; GS1D-12; cross-ref [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) F-GS-02 |
| **Severity** | **Major** · **High** |

---

### F-GS1D-03 — Positive · API SG/CD front robust @ doliv close range

| Evidence IDs | EVID-GS1D-02; cross-ref [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md) F-LS1D-03 |
| **Observation** | Narrow 1L label preserves readable **10W-40 · API SG/CD** lockup — **↑ thumbnail utility** vs OEM microtype. |
| **Severity** | **Positive** · **High** |

---

### F-GS1D-04 — Positive · OEM partial front on 1L (↑ vs LUKOIL SUPER 1L back-only)

| Evidence IDs | EVID-GS1D-03; cross-ref [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md) |
| **Severity** | **Positive** · **High** |

---

### F-GS1D-05 — Major · UMZ absent (domestic stack gap vs LUKOIL)

| Evidence IDs | EVID-GS1D-12; cross-ref [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md) EVID-LS1D-07 |
| **Severity** | **Major** · **High** |

---

### F-GS1D-06 — Moderate · SUPER hyperbole vs API SG (cross-format constant)

| Evidence IDs | EVID-GS1D-01; GS1D-02; [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) F-GS-04 |
| **Severity** | **Moderate** · **High** |

---

### F-GS1D-07 — Major · Scratch authenticity under-delivered on 1L photo

| Evidence IDs | EVID-GS1D-11; cross-ref [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) EVID-GS-09 |
| **Observation** | 4L back has «Уникальный номер» zone; 1L back photo — **not visible**. Crop lacuna vs format omission — **verify** current facing. |
| **Severity** | **Major** · **Medium** |

---

### F-GS1D-08 — Moderate · Anti-fraud UX regression 4L → 1L (photo evidence)

| Evidence IDs | EVID-GS1D-11; GS1D-14 |
| **Severity** | **Moderate** · **Medium** |

---

### F-GS1D-09 — Moderate · No top-up semantic / fill gauge on 1L

| Evidence IDs | EVID-GS1D-04; GS1D-14 |
| **Observation** | PGMM: oil-level strip **lost** vs 4L; no «doliv 1L» claim — channel mismatch for top-up SKU. |
| **Severity** | **Moderate** · **High** |

---

### F-GS1D-10 — Positive · Cross-format API / semi / STO aligned

| Evidence IDs | EVID-GS1D-02; GS1D-05; GS1D-06; GS1D-13 |
| **Severity** | **Positive** · **High** |

---

### F-GS1D-11 — Minor · Batch 2022 newer than 4L photo 2020

| Evidence IDs | EVID-GS1D-10; GS1D-13 |
| **Severity** | **Minor** · **Medium** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-GS1D-01 | ZMZ front vs absent back | **Open** — inherits [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) CR-GS-01 |
| CR-GS1D-02 | 4L scratch code vs 1L photo absent | **Open** — F-GS1D-07; crop vs format |
| CR-GS1D-03 | 4L AAI back vs 1L photo absent | **Open** — may be crop lacuna |
| CR-GS1D-04 | Cross-format OEM/STO/API | **Closed** — aligned |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — scratch 1L; UMZ; AAI on 1L crop; top-up semantics. **Redundancy** — SUPER+swirl+semi **константа**. **Contamination** — swirl **константа**.

**Logical Coherence:** API/semi **Pass**; OEM **Partial** (CR-GS1D-01).

**System Dynamics:** **Potential** — OEM front @ doliv (**↑ vs LUKOIL 1L**). **Limit** — no fill gauge; scratch under-delivered. **Anomaly** — STO **058-2012** same both formats (closes PGMM delta STO drift hypothesis).

**Relational States:** **Parity** with 4L on core claims. **Compromise** — institutional stack compressed on 1L back photo.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 1L · rev. 1 locked · **point-ref**

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Universal + Swirl Lite + Authenticity + OEM partial front (**константа** vs 4L) | wiki/47; EVID-GS1D-14 | H |
| 2 | Carrier morphology (PGMM) | Narrow 1L bottle + grip ridges; **no handle / no oil-level strip** | EVID-GS1D-04; wiki/47 | H |
| 3 | Класс продукта (синт / полусинт) | **Полусинтетическое** · API **SG/CD** | EVID-GS1D-01; GS1D-02; GS1D-05 | H |
| 4 | SAE 10W-40 — legibility | **High** — orange band dominant @ close range | EVID-GS1D-02 | H |
| 5 | API — видимость (front / back) | **SG/CD · SG/CD** | EVID-GS1D-02; GS1D-05 | H |
| 6 | ACEA — видимость (front / back) | **Absent · Absent** | EVID-GS1D-12; [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) | H |
| 7 | OEM / допуски — front (effective) | **AVTOVAZ · ZMZ microtype** — **robust @ doliv** | EVID-GS1D-03; F-GS1D-04 | H |
| 8 | OEM / допуски — back / site / overlay | **ПАО «АВТОВАЗ»** + STO · ZMZ/UMZ/AAI **н/д or absent** | EVID-GS1D-06; GS1D-12 | M |
| 9 | Benefit-icons — доказуемость | Car icon + swirl; wear/sludge **text back** | EVID-GS1D-01; GS1D-07 | M |
| 10 | Cross-face consistency | **Partial Pass** — API/semi Pass; ZMZ split | EVID-GS1D-02 = GS1D-05; CR-GS1D-01 | H |
| 11 | Digital / overlay vs pack gap | **Pending** GPN-03 | GS1D-005 | L |
| 12 | Anti-fraud UX | **EAC + barcode + batch** · scratch **н/д** on 1L photo | EVID-GS1D-08; GS1D-09; GS1D-11 | M |
| 13 | RF supply & языковая модель | Official GPN · Cyrillic front + RU back body | EVID-GS1D-01; GS1D-07; GS1D-09 | H |
| 14 | Обязательная маркировка РФ | **EAC · barcode · batch · 1L · STO** | EVID-GS1D-06; GS1D-08; GS1D-10 | H |
| 15 | Кириллица vs латиница | **Кириллица dominant** front | EVID-GS1D-01 | H |
| 16 | Thumbnail robustness (~120 px) | **High-medium** — SUPER + 10W-40 + API; OEM microtype **marginal @2m** | EVID-GS1D-02; wiki/47 | H |
| 17 | Cognitive load / negative space | **Medium-high** — vertical rescale; back density ↑ on smaller carrier | wiki/47 | H |
| 18 | Legacy / rev. risk на полке | **Low–Moderate** — batch 2022; wrap family stable vs 4L | EVID-GS1D-10; GS1D-13 | M |

---

## Импликации для СТМ (Classic/Protect · 10W-40 · 1L doliv)

1. **Перенять:** readable **SAE+API front** @ doliv + **OEM front row** (GPN partial front **better** than LUKOIL back-only).
2. **Не копировать:** SUPER stack without top-up rationale; scratch regression; ZMZ split.
3. **Attack vector:** **readable OEM band (3 domestic)** + **fill gauge / «точный долив 1L»** + anti-fraud parity 1L=4L.
4. Cross-ref 4L: [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) · peer 1L: [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md).

---

## Issues for discussion

1. **Scratch on 1L:** verify current retail — crop lacuna vs format cut?
2. **AAI on 1L back:** same as 4L below fold?
3. **STO 058-2012:** confirmed both formats — update PGMM delta row 13 if needed.
4. **GPN-03** line verify closes digital gap for both formats.

**DoD:** ODSA GPN Super 10W-40 **1L — complete** (rev. 1 photo locked).
