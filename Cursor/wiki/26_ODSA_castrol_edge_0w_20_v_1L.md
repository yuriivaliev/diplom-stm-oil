# ODSA — Castrol EDGE 0W-20 V (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_CASTROL_EDGE_0W20V_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [24_PGMM_castrol_edge_0w_20_v_1L_delta.md](24_PGMM_castrol_edge_0w_20_v_1L_delta.md) · base 5L ODSA: [25_…](25_ODSA_castrol_edge_0w_20_v_5L.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (front-only)  
**Формат:** 1L · EU base wrap · **back n/d**  
**Статус:** 🟡 **Provisional lock** (front · **back base n/d**)

**Line attestation:** back specs **assume ≈5L** ([25](25_ODSA_castrol_edge_0w_20_v_5L.md)) — **not photo-verified on 1L**.

---

## Executive summary (rev. 1 · provisional)

**Канон SKU (visible):** **Castrol EDGE 0W-20 V 1L** — front **match 5L** claim stack (HYSPEC + EDGE + 0W-20 V + tri-fuel); **➕ QR + P01FE74-00** on footer (vs 5L front).

**Front parity vs 5L:** ✅ HYSPEC · ✅ EDGE · ✅ 0W-20 V · ✅ tri-fuel · ❌ API/ACEA/OEM · ➕ **QR present**.

**RF channel:** EU-facing single-layer — **assumed same as 5L** (no RU overlay on photo).

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
| ART-CED-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L (watermark Top Castrol) |
| ART-CED-002 | Document | wiki/24 | PGMM delta 1L |
| ART-CED-003 | Document | wiki/25 | ODSA 5L + back spec reference |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-CED-01 | Artifact | ART-CED-001 | **HYSPEC** + «CASTROL'S HYBRID STANDARD» | A | Active |
| EVID-CED-02 | Artifact | ART-CED-001 | Castrol **EDGE**; «UNLOCK THE VERY EDGE OF PERFORMANCE» | A | Active |
| EVID-CED-03 | Artifact | ART-CED-001 | **0W-20 V** white box badge | A | Active |
| EVID-CED-04 | Artifact | ART-CED-001 | **GASOLINE/PETROL • DIESEL • HYBRID** | A | Active |
| EVID-CED-05 | Artifact | ART-CED-001 | **1Le**; **FINDCAROIL.COM** | A | Active |
| EVID-CED-06 | Artifact | ART-CED-001 | **QR + P01FE74-00** footer-left | A | Active |
| EVID-CED-07 | Artifact | ART-CED-001 | **API / ACEA / OEM — не на фронте** | A | Active |
| EVID-CED-08 | Context | ART-CED-002 | PGMM: HYSPEC header **robust @120px** | B | Context |
| EVID-CED-09 | Context | ART-CED-003 | 5L back: ACEA C5 + OEM grid (line inherit) | **B** | **Active** (assumed) |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-CED-01 Back label 1L (base) | **Open** |
| GAP-CED-02 Batch / barcode 1L back | Open |
| GAP-CED-03 RU overlay on 1L | Open |
| GAP-CED-04 QR destination / anti-fraud copy | Open |

---

## Findings Catalogue (compact)

### F-CED-01 — Positive · Front claim stack coherent with 5L line

| Evidence IDs | EVID-CED-01; EVID-CED-02; EVID-CED-03 |
| **Severity** | Positive · **High** |

### F-CED-02 — Major · API / ILSAC / ACEA absent from front

| Evidence IDs | EVID-CED-07 |
| **Severity** | **Major** · **High** (inherits [25](25_ODSA_castrol_edge_0w_20_v_5L.md) F-CE-02 pattern)

### F-CED-03 — Major · Back label n/d — full claims audit incomplete

| Evidence IDs | GAP-CED-01 |
| **Severity** | **Major** · **High** |
| **Recommendations** | structural: photo back 1L for lock upgrade |

### F-CED-04 — Positive · HYSPEC hybrid gate preserved @ 1L scale

| Evidence IDs | EVID-CED-01; EVID-CED-08 |
| **Observation** | Header wedge **not sacrificed** vs Mobil dexos1 footer shrink ([20](20_PGMM_mobil_1_0w_20_1L_delta.md)). |
| **Severity** | Positive · **High** |

### F-CED-05 — Moderate · QR on 1L front — digital trace ↑ vs 5L

| Evidence IDs | EVID-CED-06 |
| **Observation** | QR + batch code **on front** (PGMM MOCC delta vs 5L LAC08). |
| **Severity** | **Moderate** · **Medium** (destination n/d)

### F-CED-06 — Moderate · Thumbnail — HYSPEC + 0W-20 robust; tri-fuel ↓

| Evidence IDs | EVID-CED-08; wiki/24 |
| **Severity** | **Moderate** · **Medium** |

### F-CED-07 — Moderate · Top-up format — grip bottle; no service jug codes

| Evidence IDs | wiki/24 §2.1 |
| **Severity** | **Moderate** · **Low** |

### F-CED-08 — Moderate · EU single-layer — no Cyrillic visible

| Evidence IDs | EVID-CED-07; [25](25_ODSA_castrol_edge_0w_20_v_5L.md) F-CE-07 |
| **Severity** | **Moderate** · **Medium** |

### F-CED-09 — Minor · Part code P01FE74-00 (1L) vs P01FE7E-00 (5L back)

| Evidence IDs | EVID-CED-06; [25](25_ODSA_castrol_edge_0w_20_v_5L.md) F-CE-13 |
| **Severity** | **Minor** |

### F-CED-10 — Positive · Line inherit — ACEA C5 + OEM grid assumed from 5L back

| Evidence IDs | **EVID-CED-09** |
| **Severity** | Positive · **Medium** (B-grade inherit)

---

## POV-маркировка (provisional · rev. 1)

**Information Integrity** — *Lacunae:* back base n/d; QR destination n/d; RU overlay n/d.  
**Logical Coherence** — *Conflicts:* none if line attestation holds.  
**System Dynamics** — *Limits:* 1L top-up; tri-fuel band ↓ @ distance.  
**Relational States** — *Compromise:* vertical rescale preserves HYSPEC ([24](24_PGMM_castrol_edge_0w_20_v_1L_delta.md)).

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Формат 1L · rev. 1 provisional

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|--------------|
| 1 | M_SYSTEM (PGMM) | hyspec_hybrid_gate + edge_hyperbole (inherited) | wiki/24 | H |
| 2 | Carrier morphology (PGMM) | 1L gold grip-bottle; **no jug handle** | wiki/24 | H |
| 3 | Класс продукта (синт / полусинт) | **Full syn implied** — not explicit front | EVID-CED-02; CED-09 | M |
| 4 | SAE 0W-20 — legibility | **High** @ full view · **Medium** @120px | EVID-CED-03; wiki/24 | M |
| 5 | API — видимость (front / back) | Front: **—** · Back: **н/д** · Line (5L): **— visible** | EVID-CED-07; CED-09 | L |
| 6 | ACEA — видимость (front / back) | Front: **—** · Line inherit: **C5** (5L back) | EVID-CED-09 | M |
| 7 | OEM / допуски — front (effective) | **No — HYSPEC only** | EVID-CED-01 | H |
| 8 | OEM / допуски — back / site / overlay | Line inherit: Honda…Volvo ([25](25_ODSA_castrol_edge_0w_20_v_5L.md)) | EVID-CED-09 | M |
| 9 | Benefit-icons — доказуемость | **Moderate** — HYSPEC wedge text | EVID-CED-01; wiki/24 | M |
| 10 | Cross-face consistency | **Partial** — front OK; back **n/d** | GAP-CED-01 | L |
| 11 | Digital / overlay vs pack gap | **QR front** — destination n/d | EVID-CED-06 | L |
| 12 | Anti-fraud UX | **QR + batch code front** (↑ vs 5L) | EVID-CED-06 | M |
| 13 | RF supply & языковая модель | **EU wrap** · parallel import assumed | [25](25_ODSA_castrol_edge_0w_20_v_5L.md) | M |
| 14 | Обязательная маркировка РФ | **н/д** | GAP-CED-03 | L |
| 15 | Кириллица vs латиница | **Latin only** on front | EVID-CED-01 | H |
| 16 | Thumbnail robustness (~120 px) | **Medium–High** — HYSPEC + 0W-20 **robust** | wiki/24; EVID-CED-08 | M |
| 17 | Cognitive load / negative space | **Medium** — white field ↓ vs 5L | wiki/24 | H |
| 18 | Legacy / rev. risk на полке | **n/d** (no batch on back photo) | GAP-CED-02 | L |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | Provisional — front only |
| **Upgrade path** | Back 1L photo → rev.2 full lock |
| **Rev.** | **1 provisional** · 25.06.2026 |

---

## Issues for discussion

1. Back 1L — тот же EU spec block, что 5L, или regional variant?
2. QR on 1L — ведёт на FINDCAROIL.COM или отдельный trace?
3. СТМ 1L brief: **HYSPEC-style badge + API/OEM front** при сжатом макете ([24](24_PGMM_castrol_edge_0w_20_v_1L_delta.md) § STM)?
