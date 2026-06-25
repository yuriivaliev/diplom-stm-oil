# ODSA — Mobil 1 0W-20 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_1_0W20_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [20_PGMM_mobil_1_0w_20_1L_delta.md](20_PGMM_mobil_1_0w_20_1L_delta.md) · base 5L ODSA: [21_…](21_ODSA_mobil_1_0w_20_5L.md)  
**Дата:** 25.06.2026 · **Rev.:** 2 (front + RU overlay line attestation)  
**Формат:** 1L · import base wrap (UA \| TR \| ISR \| AR) + **RU translation sticker** (line-level)  
**Статус:** 🟡 **Provisional lock** (front + overlay text · **back base n/d**)

**RU overlay:** наследуется из [21](21_ODSA_mobil_1_0w_20_5L.md) rev.2 (Mobil 1 0W-20 line attestation) — **не подтверждено фото на 1L**.

---

## Executive summary (rev. 2 · provisional)

**Канон SKU (visible):** **Mobil 1 0W-20 1L** — front **match 5L**; **RU overlay** (line attestation from wiki/21) даёт API/ACEA/ILSAC/OEM на кириллице.

**Front parity vs 5L:** ✅ claim stack · ✅ dexos1 Gen3 · ✅ hybrid · ❌ API/ILSAC/ACEA on base front.

**RF channel:** **Two-layer** (import + RU sticker) — **assumed same text as 5L** (B-grade); back base **н/д**.

| Severity rollup (provisional) | Count |
|-------------------------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 5 |
| Minor | 1 |
| Positive | 3 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-M1D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L |
| ART-M1D-002 | Document | wiki/20 | PGMM delta 1L |
| ART-M1D-003 | Document | wiki/21 | ODSA 5L + RU overlay attestation (line ref) |
| ART-M1D-004 | Context (text) | Оператор 25.06.2026 | RU overlay — **inherit** wiki/21 ART-M1-006 | Internal |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-M1D-01 | Artifact | ART-M1D-001 | Mobil **1**; **ADVANCED SYNTHETIC TECHNOLOGY ENGINE OIL**; **0W-20**; **1L** | A | Active |
| EVID-M1D-02 | Artifact | ART-M1D-001 | Claim stack: TOP PERFORMANCE · ULTIMATE PROTECTION · FUEL ECONOMY | A | Active |
| EVID-M1D-03 | Artifact | ART-M1D-001 | **dexos1™ GM APPROVED-GEN 3** (footer; **smaller vs 5L**) | A | Active |
| EVID-M1D-04 | Artifact | ART-M1D-001 | **ALSO RECOMMENDED FOR HYBRIDS** | A | Active |
| EVID-M1D-05 | Artifact | ART-M1D-001 | **API / ACEA / ILSAC не на фронте** | A | Active |
| EVID-M1D-06 | Artifact | ART-M1D-001 | Regional: **UA \| TR \| ISR \| AR** | A | Active |
| EVID-M1D-07 | Artifact | ART-M1D-001 | QR + red Mobil icon footer | A | Active |
| EVID-M1D-08 | Context | ART-M1D-002 | PGMM: dexos1/hybrid **↓ @120px** | B | Context |
| **EVID-M1D-09** | **Context** | **ART-M1D-004** | RU overlay description (inherit [21](21_ODSA_mobil_1_0w_20_5L.md) M18) | **B** | **Active** |
| **EVID-M1D-10** | **Context** | **ART-M1D-004** | RU overlay specs API/ACEA/ILSAC/OEM (inherit M19) | **B** | **Active** |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-M1D-01 Back label 1L (base) | **Open** |
| GAP-M1D-02 Batch / barcode 1L | Open |
| GAP-M1D-03 RU overlay on 1L | **Partial** — line attestation; photo n/d |

---

## Findings Catalogue (compact)

### F-M1D-01 — Positive · Front claim stack coherent with 5L line

| Evidence IDs | EVID-M1D-01; EVID-M1D-02 |
| **Severity** | Positive · **High** |

### F-M1D-02 — Major · API / ILSAC / ACEA absent from front

| Evidence IDs | EVID-M1D-05 |
| **Severity** | **Major** · **High** (inherits pattern [21](21_ODSA_mobil_1_0w_20_5L.md) F-M1-02) |

### F-M1D-03 — Major · Back label n/d — full claims audit incomplete

| Evidence IDs | GAP-M1D-01 |
| **Severity** | **Major** · **High** |
| **Recommendations** | structural: photo back 1L for lock upgrade |

### F-M1D-04 — Positive · dexos1 Gen3 on front (effective OEM)

| Evidence IDs | EVID-M1D-03 |
| **Severity** | Positive · **Medium** (size ↓ vs 5L) |

### F-M1D-05 — Moderate · Two-layer RF — RU overlay (line attestation)

| Evidence IDs | **EVID-M1D-09**; **EVID-M1D-10** |
| **Observation** | Same RU sticker text as 5L line ([21](21_ODSA_mobil_1_0w_20_5L.md)); **not photo-verified on 1L**. |
| **Severity** | **Moderate** · **Medium** |

### F-M1D-06 — Moderate · Thumbnail OEM/hybrid legibility ↓ vs 5L

| Evidence IDs | EVID-M1D-03; EVID-M1D-04; EVID-M1D-08 |
| **Severity** | **Moderate** · **Medium** |

### F-M1D-07 — Moderate · Top-up format — no handle; service jug codes absent

| Evidence IDs | wiki/20 §2.1 |
| **Severity** | **Moderate** · **Low** |

### F-M1D-08 — Minor · QR latent; no anti-fraud copy

| Evidence IDs | EVID-M1D-07 |
| **Severity** | **Minor** |

---

### F-M1D-09 — Positive · RU overlay (line) — hybrid + JP/KR narrative

| Evidence IDs | **EVID-M1D-09** |
| **Severity** | Positive · **Medium** (B-grade inherit) |

---

## POV-маркировка (provisional · rev. 2)

**Information Integrity** — *Lacunae:* back base n/d; overlay not photo-bound to 1L.  
**Logical Coherence** — *Conflicts:* none if line attestation holds.  
**System Dynamics** — *Limits:* 1L top-up; dexos1 @120px.  
**Relational States** — *Compromise:* DRY rescale + sticker layer ([20](20_PGMM_mobil_1_0w_20_1L_delta.md)).

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Формат 1L · rev. 2 provisional

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|--------------|
| 1 | M_SYSTEM (PGMM) | bio_lattice_hyper_performance (inherited) | wiki/20 | H |
| 2 | Carrier morphology (PGMM) | 1L vertical bottle; grip ridges; **no handle** | wiki/20 | H |
| 3 | Класс продукта (синт / полусинт) | **Advanced Synthetic** (front) | EVID-M1D-01 | H |
| 4 | SAE 0W-20 — legibility | **High** @ full view · **Medium** @120px | EVID-M1D-01; wiki/20 | M |
| 5 | API — видимость (front / back) | Front base: **—** · Back base: **н/д** · RU overlay: **SJ→SP incl. EC+RC** (line) | EVID-M1D-05; M1D-10 | M |
| 6 | ACEA — видимость (front / back) | Front: **—** · Overlay: **C5** (line) | EVID-M1D-10 | M |
| 7 | OEM / допуски — front (effective) | **Yes — dexos1 Gen 3** (small badge) | EVID-M1D-03 | M |
| 8 | OEM / допуски — back / site / overlay | Overlay (line): Ford, GM, FCA, FIAT — см. [21](21_ODSA_mobil_1_0w_20_5L.md) M19 | EVID-M1D-10 | M |
| 9 | Benefit-icons — доказуемость | **Low-Moderate** — hybrid icon ↓ size | EVID-M1D-04; wiki/20 | M |
| 10 | Cross-face consistency | **Partial** — front OK; back base n/d | GAP-M1D-01 | L |
| 11 | Digital / overlay vs pack gap | **Line attestation** — assume ≈5L (no 1L photo) | EVID-M1D-10 | L |
| 12 | Anti-fraud UX | **QR only** | EVID-M1D-07 | M |
| 13 | RF supply & языковая модель | **Parallel import** + **RU overlay** (line) | EVID-M1D-09; M1D-10 | M |
| 14 | Обязательная маркировка РФ | Через **importer overlay** (line attestation) | EVID-M1D-09 | M |
| 15 | Кириллица vs латиница | Base **EN**; RF → **overlay RU** | EVID-M1D-09 | M |
| 16 | Thumbnail robustness (~120 px) | **Medium** — 0W-20 OK; dexos1/hybrid **↓** | wiki/20; EVID-M1D-08 | M |
| 17 | Cognitive load / negative space | **High** — whitespace compressed vs 5L | wiki/20 | H |
| 18 | Legacy / rev. risk на полке | **n/d** (no batch) | GAP-M1D-02 | L |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | Provisional — front + line overlay attestation |
| **Upgrade path** | Back 1L photo + overlay on 1L photo → rev.3 full lock |
| **Rev.** | **2 provisional** · 25.06.2026 |

---

## Issues for discussion

1. Back 1L — тот же EU spec block, что 5L, или regional variant?
2. СТМ 1L brief: сохранять **API+OEM front** при сжатом макете ([20](20_PGMM_mobil_1_0w_20_1L_delta.md) § STM)?
