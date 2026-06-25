# ODSA — Mobil 1 0W-20 (5L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_1_0W20_5L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [19_PGMM_mobil_1_0w_20_5L.md](19_PGMM_mobil_1_0w_20_5L.md) · delta 1L: [20_…](20_PGMM_mobil_1_0w_20_1L_delta.md) · ODSA 1L: [22_…](22_ODSA_mobil_1_0w_20_1L.md)  
**Дата:** 25.06.2026 · **Rev.:** 2 (locked · RU overlay text attestation)  
**Формат:** 5L · import base wrap (EU langs back) + **RU translation sticker**  
**Статус:** ✅ **Locked** (DC-EP:A · operator accept as-is) · optional: GAP-M1-02 digital · overlay photo waived

**Supply channel:** Mobil **официально в РФ не поставляется**; **parallel import** + **RU overlay sticker** (M18–M19, operator 25.06.2026). Фото overlay **нет** — текст принят at lock (cf. [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) rev.3).

**Canonical URL:** н/д · `www.mobil1.com` на back — **не верифицирован** в [04](04_источники_и_URL.md) (GAP-M1-02)

---

## Executive summary (rev. 2 · locked)

**Канон SKU** (M01 + M07–M09 + **M18–M19**): **Mobil 1 0W-20 5L**, синтетическое моторное масло — согласовано base front ↔ base back ↔ **RU overlay** (описание + specs).

**RF channel model:** **двухслойная этикетка** — import base (EU langs) + RU sticker: **описание применения + блок спецификаций** (M18–M19). Фото overlay **нет**; текст зафиксирован operator attestation — **принято at lock**.

**Ключевой дифференциатор vs Super 3000 ([18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md)):** **dexos1 Gen3 на фронте base** + **полный API/ILSAC/ACEA на RU overlay** (vs API off front у Super 3000).

**Cross-face (base wrap):** Partial pass — F-M1-02 (API/ILSAC off front), F-M1-04/F-M1-05 (ACEA/OEM stack back-only on base).

**Overlay vs base back:** **Pass** — specs **≈ base**; API notation **granular** (Energy Conserving / Resource Conserving splits) без новых классов (F-M1-16 Minor).

| Severity rollup (locked) | Count |
|--------------------------|-------|
| Blocker | 0 |
| Major | 1 |
| Moderate | 7 |
| Minor | 3 |
| Positive | 5 |

---

## Configuration (locked)

| BP | Choice |
|----|--------|
| BP-01 | **A** Diagnostic |
| BP-02 | **B** Positioning & comms |
| BP-03 | **C** Product SKU · micro |
| BP-04 | **A** Compact |
| BP-05 | **B** Mixed |
| BP-07 | **A** Memo |
| BP-08 | **A** Standard |

---

## Artifact Registry

| ART | Type | Source | Description | Privacy |
|-----|------|--------|-------------|---------|
| ART-M1-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 5L | Public |
| ART-M1-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 5L — specs + safety block | Public |
| ART-M1-003 | Document | wiki/19 | PGMM full 5L | Internal |
| ART-M1-004 | Document | wiki/20 | PGMM delta 1L | Internal |
| ART-M1-005 | Context | wiki/18 | Mobil Super 3000 ODSA parity | Internal |
| **ART-M1-006** | **Context (text)** | **Оператор 25.06.2026** | **RU overlay: описание + specs block** (verbatim attestation) | Internal |
| ART-M1-007 | Context | Оператор 25.06.2026 | Parallel import; RU sticker applied for RF | Internal |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-M1-01 | Artifact | ART-M1-001 | Mobil **1**; **ADVANCED SYNTHETIC TECHNOLOGY ENGINE OIL**; **0W-20**; **5L** | A | Active |
| EVID-M1-02 | Artifact | ART-M1-001 | Performance stack: TOP PERFORMANCE · ULTIMATE PROTECTION · ADVANCED FUEL ECONOMY | A | Active |
| EVID-M1-03 | Artifact | ART-M1-001 | **dexos1™ GM APPROVED — GEN 3** (front badge) | A | Active |
| EVID-M1-04 | Artifact | ART-M1-001 | **ALSO RECOMMENDED FOR HYBRIDS** + plug-car icon | A | Active |
| EVID-M1-05 | Artifact | ART-M1-001 | **API / ILSAC / ACEA не на фронте** | A | Active |
| EVID-M1-06 | Artifact | ART-M1-001 | QR / datamatrix footer-left | A | Active |
| EVID-M1-07 | Artifact | ART-M1-002 | Meets: **ILSAC GF-6A**; **API SJ/SL/SM/SN/SN Plus/SP/SP Resource Conserving**; **ACEA C5**; Ford WSS-M2C962-A1; Chrysler MS-6395 | A | Active |
| EVID-M1-08 | Artifact | ART-M1-002 | Approved: **GM dexos1™ Gen 3** (License **D340BSDE015**) | A | Active |
| EVID-M1-09 | Artifact | ART-M1-002 | ExxonMobil Quality Level: **GM 6094M**; Ford WSS-M2C947-A/B1; **FIAT 9.55535-CR1** | A | Active |
| EVID-M1-10 | Artifact | ART-M1-002 | Benefit bullets (4): thermal/oxidation stability; low-temp; extended drain; startup protection | A | Active |
| EVID-M1-11 | Artifact | ART-M1-002 | Safety langs: **EN(GB), F, BG, CZ, D, DK, E, EST** — **нет RU** | A | Active |
| EVID-M1-12 | Artifact | ART-M1-002 | Barcode **5 407008 073374**; volume **5Le**; **0W-20** badge | A | Active |
| EVID-M1-13 | Artifact | ART-M1-002 | Mold stamp: **0433269 27/03/2024 000350 EMB76476A** | A | Active |
| EVID-M1-14 | Artifact | ART-M1-002 | **UL Validated** seal; QR «SCAN for more product information» | A | Active |
| EVID-M1-15 | Artifact | ART-M1-002 | **www.mobil1.com** (back footer) | B | Active |
| EVID-M1-16 | Context | ART-M1-003 | PGMM: API/ACEA lacuna on front confirmed | B | Context |
| EVID-M1-17 | Context | ART-M1-005 | Super 3000: API off front; no OEM front — contrast baseline | B | Context |
| **EVID-M1-18** | **Context** | **ART-M1-006** | RU: «…**современных высокоэффективных американских двигателей с турбонаддувом**… GM, Ford, Chrysler, Fiat… **японских и корейских**… **SAE 0W-20**… **гибридных автомобилей**…» | **B** | **Active** |
| **EVID-M1-19** | **Context** | **ART-M1-006** | RU specs: API **SJ, SL, SM, SM EC, SN, SN RC, SN Plus, SN Plus RC, SP, SP RC**; **ACEA C5**; **ILSAC GF-6A**; FIAT **9.55535-CR1**; Ford **947-A, 947-B1, 962-A1**; GM **6094M, dexos1 Gen3**; FCA **MS-6395** | **B** | **Active** |
| EVID-M1-20 | Context | ART-M1-007 | RU translation sticker applied for RF market | B | Active |
| EVID-M1-21 | Context | ART-M1-007 | Not official RF supply | B | Active |

### RU overlay specs (canonical attestation · ART-M1-006)

> Mobil 1 0W-20 разработано для современных высокоэффективных американских двигателей с турбонаддувом, устанавливаемых на бензиновые и гибридные автомобили General Motors, Ford, Chrysler и Fiat, а также для японских и корейских автомобилей, где требуется класс вязкости SAE 0W-20 и спецификации, которым соответствует данное масло. Mobil 1 0W-20 удовлетворяет требованиям, предъявляемым к гибридным автомобилям, и рекомендуется для применения в них.
>
> API: SJ, SL, SM, SM Energy Conserving, SN, SN Resource Conserving, SN Plus, SN Plus Resource Conserving, SP, SP Resource Conserving · ACEA: C5 · ILSAC: GF-6A · FIAT: 9.55535-CR1 · Ford: WSS-M2C947-A, WSS-M2C947-B1, WSS-M2C962-A1 · GM: 6094M, GM dexos1 Gen3 · Fiat Chrysler Automotive: MS-6395

### Conflict notes

| Conflict | Evidence | Resolution |
|----------|----------|------------|
| Front no API vs back API SP+ | M1-05 vs M1-07 | **Open (CR-M1-01)** — deictic front/back split |
| dexos1 Gen3 front vs back Approved | M1-03 vs M1-08 | **Closed (CR-M1-02)** — consistent Gen 3 |
| Front no ACEA vs back ACEA C5 | M1-05 vs M1-07 | **Open (CR-M1-03)** |
| 5L front vs 5Le back | M1-01 vs M1-12 | **Closed (CR-M1-04)** — notation variant |
| EU langs vs RF market | M1-11 vs M18–M20 | **Closed (CR-M1-05)** — two-layer by design |
| Base back vs RU overlay specs | M1-07–M09 vs M19 | **Closed (CR-M1-06)** — coherent; notation granularity only |
| RU hybrid narrative vs front badge | M1-04 vs M18 | **Closed (CR-M1-07)** — reinforcing |

### Data gaps (at lock)

| Gap | Статус |
|-----|--------|
| GAP-M1-01 RU overlay / importer sticker | **Closed** — M18–M19 text attestation (photo waived) |
| GAP-M1-02 Digital triangulation (mobil1.com) | **Open** — URL not in wiki/04 |
| GAP-M1-03 Retail shelf @1.2 m | Open — н/д |
| GAP-M1-04 Operator attestation (wrap stability) | Open — single batch 2024 only |
| GAP-M1-05 TDS PDF | Optional |
| GAP-M1-06 RU overlay photo | **Waived** at lock |

---

## Findings Catalogue

### F-M1-01 — Positive · Core claims coherent (syn · 0W-20 · 5L)

| Evidence IDs | EVID-M1-01; EVID-M1-07; EVID-M1-12 |
| **Observation** | «Advanced Synthetic Technology» front ↔ API SP-class + ILSAC GF-6A back; 0W-20 + 5L/5Le aligned. |
| **Severity** | Positive · **High** |

---

### F-M1-02 — Major · API / ILSAC absent from front (base); on back / RU overlay

| Evidence IDs | EVID-M1-05; EVID-M1-07; **EVID-M1-19** |
| **Observation** | Front base: no API, no ILSAC. Back base: full API SJ→SP RC + **GF-6A**. RU overlay: **flat API list** incl. EC/RC variants + **GF-6A**. |
| **Interpretation** | Shelf-facing **base front** не даёт API proof; RU overlay компенсирует **only if buyer reads sticker** (typically back/side). |
| **Severity** | **Major** · **High** |
| **Recommendations** | structural: СТМ 0W-20 — **API SP + GF-6A on front** |

---

### F-M1-03 — Positive · GM dexos1 Gen 3 on front (effective OEM shelf proof)

| Evidence IDs | EVID-M1-03; EVID-M1-08 |
| **Observation** | Front: **dexos1™ GM APPROVED — GEN 3**. Back: Approved with license **D340BSDE015**. |
| **Interpretation** | **Upgrade vs Super 3000** ([18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) F-M03): institutional badge **consumer-visible @ shelf**. |
| **Severity** | Positive · **High** |

---

### F-M1-04 — Moderate · ACEA C5 back-only

| Evidence IDs | EVID-M1-05; EVID-M1-07 |
| **Observation** | **ACEA C5** only on back spec block. |
| **Severity** | **Moderate** · **High** |

---

### F-M1-05 — Moderate · Extended OEM / QL stack back-only

| Evidence IDs | EVID-M1-07; EVID-M1-09 |
| **Observation** | Back: Ford WSS-M2C962-A1, Chrysler MS-6395, Ford WSS-M2C947-A/B1, FIAT 9.55535-CR1, GM 6094M — **not on front** (front = dexos1 only). |
| **Severity** | **Moderate** · **Medium** |

---

### F-M1-06 — Moderate · Two-layer label architecture (parallel import)

| Evidence IDs | EVID-M1-11; EVID-M1-18; EVID-M1-19; EVID-M1-20; EVID-M1-21 |
| **Observation** | Base EU langs + **RU overlay** with description (M18) + specs (M19). |
| **Interpretation** | RF compliance via **importer overlay**, not integrated wrap. Accepted at lock without overlay photo. |
| **Severity** | **Moderate** · **Medium** |

---

### F-M1-06b — Moderate · Parallel import — no official RF channel

| Evidence IDs | EVID-M1-20; EVID-M1-21; EVID-M1-13 |
| **Severity** | **Moderate** · **Medium** |

---

### F-M1-07 — Moderate · Hybrid + fuel economy front — segment-aligned (DR-B)

| Evidence IDs | EVID-M1-02; EVID-M1-04 |
| **Observation** | Hybrid badge + fuel economy claim + 0W-20 — aligned with 0W-20 growth / China-hybrid proxy ([03](03_DR-B_вязкости_SAE.md)). |
| **Severity** | **Moderate** · **Medium** (positioning Positive; claims not lab-verified on pack) |

---

### F-M1-08 — Minor · Volume notation 5L vs 5Le

| Evidence IDs | EVID-M1-01; EVID-M1-12 |
| **Severity** | **Minor** · **High** |

---

### F-M1-09 — Minor (rev. 2 ↓) · Benefit narrative — RU available on overlay

| Evidence IDs | EVID-M1-10; EVID-M1-11; **EVID-M1-18** |
| **Observation** | Base back EN bullets (M10); RU overlay **full description in Russian** incl. hybrid use case (M18). |
| **Severity** | **Minor** · **Medium** (was standalone EN-only gap) |

---

### F-M1-10 — Positive · Cross-face dexos1 / synthetic / SAE / volume — no split-face defect

| Evidence IDs | EVID-M1-01; EVID-M1-03; EVID-M1-07; EVID-M1-08; EVID-M1-12 |
| **Severity** | Positive · **High** |

---

### F-M1-11 — Positive · Current formulation facing (2024 batch)

| Evidence IDs | EVID-M1-13; EVID-M1-07 |
| **Observation** | GF-6A + API SP + dexos1 Gen3 = **current-gen** stack; no legacy SL/SN-only signal. |
| **Severity** | Positive · **Medium** |

---

### F-M1-12 — Moderate · Anti-fraud UX — QR latent only

| Evidence IDs | EVID-M1-06; EVID-M1-14 |
| **Observation** | QR present; no GPN-style **3662.ru** or explicit anti-counterfeit copy. |
| **Severity** | **Moderate** · **Medium** |

---

### F-M1-13 — Moderate · Digital vs pack gap — not triangulated

| Evidence IDs | EVID-M1-15 |
| **Observation** | mobil1.com on label; **not scraped** (wiki/04 gap). Overlay specs **not tested** vs site. |
| **Severity** | **Moderate** · **Low** |

---

### F-M1-14 — Positive · RU overlay restores RF-readable product description + specs

| Evidence IDs | **EVID-M1-18**; **EVID-M1-19**; EVID-M1-20 |
| **Observation** | Operator attestation: RU описание применения + **полный блок API/ACEA/ILSAC/OEM** на кириллице. |
| **Severity** | Positive · **Medium** (text-only evidence) |

---

### F-M1-15 — Positive · RU overlay hybrid narrative aligns with front badge

| Evidence IDs | EVID-M1-04; **EVID-M1-18** |
| **Observation** | Front: «ALSO RECOMMENDED FOR HYBRIDS». RU: «удовлетворяет требованиям… **гибридных автомобилей**». |
| **Severity** | Positive · **Medium** |

---

### F-M1-16 — Minor · API notation granularity overlay vs base taxonomy

| Evidence IDs | EVID-M1-07; **EVID-M1-19** |
| **Observation** | Base: «Meets … API SJ/SL/SM/SN/SN Plus/SP/SP Resource Conserving». RU overlay: **flat list** with **SM Energy Conserving**, **SN Resource Conserving**, etc. |
| **Interpretation** | Notation expansion, **not new API classes** — cf. closed CR-M1-06 (vs Super 3000 overlay **superset** F-M13). |
| **Severity** | **Minor** · **Medium** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-M1-01 | Front API/ILSAC absent | Open — F-M1-02 |
| CR-M1-02 | dexos1 Gen3 front ↔ back | **Closed** |
| CR-M1-03 | ACEA C5 back-only | Open — F-M1-04 |
| CR-M1-04 | 5L vs 5Le | **Closed** |
| CR-M1-05 | EU wrap vs RF reader | **Closed** — two-layer M18–M20 |
| CR-M1-06 | Base back ↔ RU overlay specs | **Closed** — notation only (F-M1-16) |
| CR-M1-07 | Hybrid front ↔ RU narrative | **Closed** — F-M1-15 |

---

## POV-маркировка (locked · rev. 2)

**Information Integrity**
- *Lacunae:* overlay photo waived; digital triangulation n/d; API/ILSAC front lacuna on base.
- *Redundancy:* RU overlay **duplicates** specs + **extends** API notation granularity (EC/RC splits).
- *Contamination:* none on base wrap.
- *Collonisation:* importer overlay as RF compliance patch (cf. Super 3000 [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md)).

**Logical Coherence**
- *Conflicts:* none on spec identity — overlay **≈ base back** (CR-M1-06 closed).
- *Contradictions:* none on Gen3 / 0W-20 / hybrid.

**System Dynamics**
- *Potentials:* СТМ — **single-layer RU + API SP front + official supply**.
- *Limits:* parallel import; overlay content B-grade (no photo).

**Relational States**
- *Compromise:* global base + local RU sticker accepted at lock.
- *Parities:* **Stronger OEM front** than Super 3000; overlay gives **richer RU spec block** than base EN back alone; **weaker integration** than LUKOIL/GPN native wrap.

---

## Строка для сводной матрицы (ODSA × PGMM)

| Параметр | Mobil 1 0W-20 5L |
|----------|------------------|
| Product line | **Mobil 1** (flagship) |
| API (front base / back base / RU overlay) | **— / SJ→SP RC / SJ→SP incl. EC+RC variants** |
| ILSAC | **— / GF-6A / GF-6A** |
| Base oil claim | **Advanced Synthetic Technology** (front) |
| ACEA | **— / C5 / C5** |
| OEM (front base) | **Yes — dexos1 Gen 3** |
| OEM (back base / RU overlay) | GM dexos1 Gen3 + Ford WSS ×3 + FCA MS-6395 + FIAT CR1 + GM 6094M |
| Hybrid claim | **Front badge + RU narrative** |
| Language (RF) | Base **EN+EU** + **RU overlay** (text attestation M18–M19) |
| Label architecture | **Two-layer** (import + sticker) |
| Supply channel | **Parallel import** (not official RF) |
| Anti-fraud UX | **QR only** |
| Batch | **27/03/2024** EMB76476A |
| PGMM macro-system | Bio-Lattice Hyper-Performance + OEM Sovereignty (wiki/19) |
| Top ODSA risk | API/ILSAC off **base front** · two-layer RF |
| Top СТМ attack | Single-layer native RU + **API SP + GF-6A front** + official supply |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | Operator: **accept as-is** · no RU overlay photo |
| **DC-EP** | **A** |
| **Rev.** | **2 locked** · 25.06.2026 |
| **Pending optional** | GAP-M1-02 mobil1.com · GAP-M1-03 shelf · overlay photo for audit upgrade |

**DoD:** ✅ ODSA Mobil 1 0W-20 5L rev.2 locked · parity channel model with wiki/18.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · формат 5L · rev. 2

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|--------------|
| 1 | M_SYSTEM (PGMM) | bio_lattice_hyper_performance + oem_sovereignty | wiki/19 | H |
| 2 | Carrier morphology (PGMM) | 5L silver jug + integrated handle + grip ridges | wiki/19 | H |
| 3 | Класс продукта (синт / полусинт) | **Advanced Synthetic** (full syn class claim) | EVID-M1-01; M1-07; M18 | H / M |
| 4 | SAE 0W-20 — legibility | **High** — oversized white on honeycomb/black | EVID-M1-01; M1-12 | H |
| 5 | API — видимость (front / back) | Front base: **—** · Back base: **SJ→SP RC** · RU overlay: **SJ→SP incl. EC+RC** | EVID-M1-05; M1-07; M19; F-M1-02 | H |
| 6 | ACEA — видимость (front / back) | Front: **—** · Back + overlay: **C5** | EVID-M1-05; M1-07; M19 | H |
| 7 | OEM / допуски — front (effective) | **Yes — dexos1™ Gen 3 GM APPROVED** | EVID-M1-03; F-M1-03 | H |
| 8 | OEM / допуски — back / site / overlay | Base + overlay: Ford 947-A/B1, 962-A1; FCA MS-6395; FIAT CR1; GM 6094M; dexos1 Gen3 | EVID-M1-07; M1-09; M19 | H / M |
| 9 | Benefit-icons — доказуемость | **Moderate** — hybrid icon + claim stack; RU hybrid narrative | EVID-M1-04; M18; wiki/19 | M |
| 10 | Cross-face consistency | **Partial pass** (base wrap); overlay = отдельный слой | F-M1-10; CR-M1-05 | H |
| 11 | Digital / overlay vs pack gap | **Notation granularity only** — overlay ≈ base back (no superset) | EVID-M1-19 vs M07–M09; F-M1-16 | M |
| 12 | Anti-fraud UX | **QR latent only** | EVID-M1-14; F-M1-12 | M |
| 13 | RF supply & языковая модель | **Parallel import** · base **EN+EU** + **RU overlay sticker** | EVID-M1-11; M18–M20; F-M1-06 | H |
| 14 | Обязательная маркировка РФ | Через **importer overlay** (text attestation M18–M19) | EVID-M1-18; M19; F-M1-06 | M |
| 15 | Кириллица vs латиница | Base **EN dominant**; RF reader → **overlay RU** | EVID-M1-18; M20 | M |
| 16 | Thumbnail robustness (~120 px) | **High** — «1» square + 0W-20 anchor | wiki/19 | H |
| 17 | Cognitive load / negative space | **Medium-low** — premium whitespace vs Super 3000 | wiki/19 | H |
| 18 | Legacy / rev. risk на полке | **Low** — 2024 batch GF-6A/SP/Gen3 current stack | EVID-M1-13; F-M1-11 | M |

---

## Issues for discussion

1. **0W-20 matrix:** Расширять ли отдельную матрицу 0W-20 или достаточно point reference для этапов 5–6?
2. **API front policy:** Mobil 1 deliberately hides API on base front — premium trade-off vs СТМ transparency?
3. **Digital verify:** Добавить mobil1.com в wiki/04 и прогнать triangulation rev.3?
4. **Overlay photo:** Upgrade audit reliability B→A if sticker photographed?
