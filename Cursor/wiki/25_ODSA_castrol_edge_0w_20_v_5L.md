# ODSA — Castrol EDGE 0W-20 V (5L): аудит claims на упаковке

**CASE_ID:** `ODSA_CASTROL_EDGE_0W20V_5L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [23_PGMM_castrol_edge_0w_20_v_5L.md](23_PGMM_castrol_edge_0w_20_v_5L.md) · delta 1L: [24_…](24_PGMM_castrol_edge_0w_20_v_1L_delta.md) · ODSA 1L: [26_…](26_ODSA_castrol_edge_0w_20_v_1L.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (locked · front+back)  
**Формат:** 5L · EU base wrap (EN + FR/IT/DE/NL/ES back) · **без RU overlay на фото**  
**Статус:** ✅ **Locked** (DC-EP:A · artifact-only)

**Supply channel:** EU manufacture («MANUFACTURED IN THE EU»); фото с watermark **Top-Castrol.ru** — **RU online retail proxy** / вероятный **parallel import**; официальный RF-channel **н/д**.

**Canonical URL:** `FINDCAROIL.COM` на фронте — **не верифицирован** в [04](04_источники_и_URL.md) (GAP-CE-02)

---

## Executive summary (rev. 1 · locked)

**Канон SKU (visible):** **Castrol EDGE 0W-20 V 5L** — front ↔ back согласованы по **SAE 0W-20 V**, **HYSPEC hybrid**, tri-fuel band; back: **ACEA C5** + **Volvo VCC RBS0-2AE** + OEM grid (Honda, Hyundai, Kia, Nissan, Toyota, Volvo).

**Ключевой дифференциатор vs Mobil 1 ([21](21_ODSA_mobil_1_0w_20_5L.md)):** **HYSPEC front institutional hybrid gate** (vs dexos1 Gen3 badge) + **multi-OEM back grid** (vs GM-centric front OEM); **слабее** — **нет API/ILSAC на видимом back**, **нет OEM на front**, **нет RU overlay**.

**Cross-face (base wrap):** Partial pass — F-CE-02 (API/ILSAC lacuna both faces), F-CE-03 (OEM back-only), F-CE-04 (ACEA back-only); **no split-face defect** on SAE / HYSPEC / volume.

| Severity rollup (locked) | Count |
|--------------------------|-------|
| Blocker | 0 |
| Major | 3 |
| Moderate | 6 |
| Minor | 2 |
| Positive | 4 |

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
| ART-CE-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 5L (watermark Top-Castrol.ru) | Public |
| ART-CE-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 5L — specs + OEM grid + safety block | Public |
| ART-CE-003 | Document | wiki/23 | PGMM full 5L | Internal |
| ART-CE-004 | Context | wiki/21 | Mobil 1 0W-20 ODSA parity | Internal |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-CE-01 | Artifact | ART-CE-001 | **HYSPEC** + «CASTROL'S HYBRID STANDARD» (green wedge) | A | Active |
| EVID-CE-02 | Artifact | ART-CE-001 | Castrol **EDGE**; «UNLOCK THE VERY EDGE OF PERFORMANCE» | A | Active |
| EVID-CE-03 | Artifact | ART-CE-001 | **0W-20 V** white box badge | A | Active |
| EVID-CE-04 | Artifact | ART-CE-001 | **GASOLINE/PETROL • DIESEL • HYBRID** tri-fuel band | A | Active |
| EVID-CE-05 | Artifact | ART-CE-001 | **5L e**; **FINDCAROIL.COM** footer | A | Active |
| EVID-CE-06 | Artifact | ART-CE-001 | **API / ILSAC / ACEA / OEM — не на фронте** | A | Active |
| EVID-CE-07 | Artifact | ART-CE-001 | **QR / datamatrix — н/д** на фронте 5L | A | Active |
| EVID-CE-08 | Artifact | ART-CE-002 | Header: **Castrol EDGE 0W-20 V** | A | Active |
| EVID-CE-09 | Artifact | ART-CE-002 | Narrative: performance + efficiency + **motorsport track testing** | A | Active |
| EVID-CE-10 | Artifact | ART-CE-002 | OEM logos: **Honda, Hyundai, Kia, Nissan, Toyota, Volvo** | A | Active |
| EVID-CE-11 | Artifact | ART-CE-002 | Spec bar: **ACEA C5**; **Volvo VCC RBS0-2AE** | A | Active |
| EVID-CE-12 | Artifact | ART-CE-002 | Safety langs: **EN(GB), FR, IT, DE, NL, ES** — **нет RU** | A | Active |
| EVID-CE-13 | Artifact | ART-CE-002 | Barcode **4 008177 183935**; **5Le**; part **P01FE7E-00** | A | Active |
| EVID-CE-14 | Artifact | ART-CE-002 | Mold stamp: **DE01 0001782188 13/07/23 000571** | A | Active |
| EVID-CE-15 | Artifact | ART-CE-002 | **MANUFACTURED IN THE EU**; Castrol Limited; **bp** logo | A | Active |
| EVID-CE-16 | Artifact | ART-CE-002 | **API / ILSAC — н/д** на видимом back (нечитаемо/отсутствует) | A | Active |
| EVID-CE-17 | Context | ART-CE-003 | PGMM: FluidTitanium / «full synthetic» — **н/д** visible | B | Context |
| EVID-CE-18 | Context | ART-CE-004 | Mobil 1: dexos1 **front** + API **back** — contrast baseline | B | Context |

### Conflict notes

| Conflict | Evidence | Resolution |
|----------|----------|------------|
| HYSPEC hybrid vs tri-fuel diesel | CE-01 vs CE-04 | **Open (CR-CE-01)** — positioning tension |
| Front no OEM vs back OEM grid | CE-06 vs CE-10 | **Open (CR-CE-02)** — deictic front/back split |
| Front no ACEA vs back ACEA C5 | CE-06 vs CE-11 | **Open (CR-CE-03)** |
| 5L e vs 5Le | CE-05 vs CE-13 | **Closed (CR-CE-04)** — notation variant |
| EU langs vs RF reader | CE-12 | **Open (CR-CE-05)** — no RU overlay visible |
| API absent front vs back | CE-06 vs CE-16 | **Closed (CR-CE-06)** — consistent lacuna (not contradiction) |

### Data gaps (at lock)

| Gap | Статус |
|-----|--------|
| GAP-CE-01 RU overlay / importer sticker | **Open** — н/д на фото |
| GAP-CE-02 Digital triangulation (FINDCAROIL.COM) | **Open** — URL not in wiki/04 |
| GAP-CE-03 API SP / ILSAC GF-6A below fold | **Open** — not visible on photo |
| GAP-CE-04 Retail shelf @1.2 m | Open — н/д |
| GAP-CE-05 Operator attestation (wrap stability) | Open — single batch 07/2023 only |

---

## Findings Catalogue

### F-CE-01 — Positive · Core SAE / brand / volume coherent (0W-20 V · 5L)

| Evidence IDs | EVID-CE-03; EVID-CE-08; EVID-CE-13 |
| **Observation** | «0W-20 V» front ↔ back header; 5L e ↔ 5Le aligned. |
| **Severity** | Positive · **High** |

---

### F-CE-02 — Major · API / ILSAC absent from front **and** visible back

| Evidence IDs | EVID-CE-06; EVID-CE-16 |
| **Observation** | Front: no API, no ILSAC. Back (visible zone): **only ACEA C5 + Volvo RBS0-2AE** — no API SP/GF-6A readable. |
| **Interpretation** | **Weaker engineering transparency vs Mobil 1** ([21](21_ODSA_mobil_1_0w_20_5L.md) F-M1-02: API on back). Possible below-fold — GAP-CE-03 open. |
| **Severity** | **Major** · **High** |
| **Recommendations** | structural: СТМ 0W-20 — **API SP + GF-6A on front** |

---

### F-CE-03 — Major · OEM grid back-only — no effective OEM on front

| Evidence IDs | EVID-CE-06; EVID-CE-10 |
| **Observation** | Six OEM logos (Honda…Volvo) **only on back**. Front = HYSPEC institutional, not OEM badges. |
| **Interpretation** | Shelf @1.2 m: buyer sees **hybrid standard**, not Toyota/Honda proof — **weaker vs Mobil dexos1 front** ([21](21_ODSA_mobil_1_0w_20_5L.md) F-M1-03). |
| **Severity** | **Major** · **High** |
| **Recommendations** | structural: **multi-OEM row on front** for 0W-20 СТМ |

---

### F-CE-04 — Moderate · ACEA C5 back-only

| Evidence IDs | EVID-CE-06; EVID-CE-11 |
| **Observation** | **ACEA C5** only on back spec bar (+ Volvo RBS0-2AE). |
| **Severity** | **Moderate** · **High** |

---

### F-CE-05 — Positive · HYSPEC hybrid institutional gate on front

| Evidence IDs | EVID-CE-01; EVID-CE-04 |
| **Observation** | **HYSPEC — CASTROL'S HYBRID STANDARD** top wedge + tri-fuel band incl. HYBRID. |
| **Interpretation** | **Stronger hybrid front cue vs Mobil** secondary footer badge ([21](21_ODSA_mobil_1_0w_20_5L.md)). |
| **Severity** | Positive · **High** |

---

### F-CE-06 — Moderate · HYSPEC hybrid-focus vs tri-fuel universality tension

| Evidence IDs | EVID-CE-01; EVID-CE-04 |
| **Observation** | HYSPEC = hybrid standard; band lists **petrol + diesel + hybrid**. |
| **Interpretation** | Segment dilution — cf. PGMM MSYS_CE_01 ↔ MSYS_CE_03 conflict ([23](23_PGMM_castrol_edge_0w_20_v_5L.md)). |
| **Severity** | **Moderate** · **Medium** |

---

### F-CE-07 — Moderate · EU single-layer wrap — no RU overlay / Cyrillic

| Evidence IDs | EVID-CE-12; GAP-CE-01 |
| **Observation** | Back langs EN/FR/IT/DE/NL/ES; **no Cyrillic**; no importer overlay on photo. |
| **Interpretation** | RF reader without overlay → **compliance gap** vs LUKOIL/GPN native wrap; vs Mobil **two-layer** ([21](21_ODSA_mobil_1_0w_20_5L.md) F-M1-06). |
| **Severity** | **Moderate** · **Medium** |

---

### F-CE-08 — Moderate · Parallel import proxy channel (Top-Castrol.ru)

| Evidence IDs | ART-CE-001; EVID-CE-15 |
| **Observation** | EU manufacture + RU retailer watermark; official Castrol RF supply **н/д**. |
| **Severity** | **Moderate** · **Medium** |

---

### F-CE-09 — Moderate · Full synthetic / base-oil claim not explicit on visible faces

| Evidence IDs | EVID-CE-02; EVID-CE-17 |
| **Observation** | EDGE flagship line; no «full synthetic» / FluidTitanium on visible front/back. |
| **Interpretation** | Class inferred from ACEA C5 + 0W-20 V + EDGE tier — **not pack-proven**. |
| **Severity** | **Moderate** · **Medium** |

---

### F-CE-10 — Moderate · Anti-fraud UX — barcode only; no QR on 5L front

| Evidence IDs | EVID-CE-07; EVID-CE-13 |
| **Observation** | EAN + batch stamp; **no QR** on 5L front (vs 1L — QR present, [26](26_ODSA_castrol_edge_0w_20_v_1L.md)). |
| **Severity** | **Moderate** · **Low** |

---

### F-CE-11 — Moderate · Digital vs pack gap — FINDCAROIL.COM not triangulated

| Evidence IDs | EVID-CE-05 |
| **Observation** | URL on front; **not scraped** (wiki/04 gap). |
| **Severity** | **Moderate** · **Low** |

---

### F-CE-12 — Minor · Volume notation 5L e vs 5Le

| Evidence IDs | EVID-CE-05; EVID-CE-13 |
| **Severity** | **Minor** · **High** |

---

### F-CE-13 — Minor · Part code P01FE7E-00 (5L back) vs P01FE74-00 (1L front)

| Evidence IDs | EVID-CE-13; [26](26_ODSA_castrol_edge_0w_20_v_1L.md) |
| **Observation** | Format-level SKU code variant — not claims conflict. |
| **Severity** | **Minor** · **Medium** |

---

### F-CE-14 — Positive · Back OEM + ACEA C5 stack coherent with 0W-20 segment

| Evidence IDs | EVID-CE-10; EVID-CE-11 |
| **Observation** | JP/KR OEM row + ACEA C5 + Volvo RBS0-2AE — aligned with DR-B 0W-20 / China-hybrid proxy ([03](03_DR-B_вязкости_SAE.md)). |
| **Severity** | Positive · **Medium** |

---

### F-CE-15 — Positive · Cross-face SAE / HYSPEC / brand — no split-face defect

| Evidence IDs | EVID-CE-01; EVID-CE-03; EVID-CE-08; EVID-CE-13 |
| **Severity** | Positive · **High** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-CE-01 | HYSPEC hybrid vs tri-fuel diesel | Open — F-CE-06 |
| CR-CE-02 | OEM front absent vs back grid | Open — F-CE-03 |
| CR-CE-03 | ACEA C5 back-only | Open — F-CE-04 |
| CR-CE-04 | 5L e vs 5Le | **Closed** |
| CR-CE-05 | EU wrap vs RF reader | Open — F-CE-07 |
| CR-CE-06 | API lacuna both faces | **Closed** — consistent absence, not contradiction |

---

## POV-маркировка (locked · rev. 1)

**Information Integrity**
- *Lacunae:* API/ILSAC visible **both faces**; full synthetic chemistry **н/д**; RU overlay **н/д**; digital triangulation n/d.
- *Redundancy:* EDGE hyperbole + HYSPEC + tri-fuel + motorsport back — semantic performance stack without tribology proof on front.
- *Contamination:* «EDGE» polisemia (blade/motorsport/line name) — intentional ([23](23_PGMM_castrol_edge_0w_20_v_5L.md)).
- *Collonisation:* gold HDPE → premium tier without explicit gold claim.

**Logical Coherence**
- *Conflicts:* HYSPEC hybrid vs tri-fuel diesel (CR-CE-01).
- *Contradictions:* none on SAE / volume / brand identity.

**System Dynamics**
- *Potentials:* СТМ — **HYSPEC-style hybrid badge + API/OEM front + Cyrillic official supply**.
- *Limits:* back-loaded OEM; API lacuna; EU-only langs.

**Relational States**
- *Compromise:* institutional hybrid front vs universal tri-fuel band.
- *Parities:* **Stronger hybrid front** than Mobil secondary badge; **weaker OEM front** than Mobil dexos1; **weaker API transparency** than Mobil back.
- *Consensus:* Castrol red-green + EDGE lockup — line invariant.

---

## Строка для сводной матрицы (ODSA × PGMM)

| Параметр | Castrol EDGE 0W-20 V 5L |
|----------|-------------------------|
| Product line | **Castrol EDGE** (flagship) |
| API (front / back visible) | **— / —** (н/д visible; GAP-CE-03 below fold) |
| ILSAC | **— / —** |
| Base oil claim | **н/д explicit** (EDGE tier + ACEA C5 imply syn) |
| ACEA | **— / C5** |
| OEM (front) | **No — HYSPEC only** (institutional hybrid, not OEM logos) |
| OEM (back) | Honda, Hyundai, Kia, Nissan, Toyota, Volvo + **Volvo VCC RBS0-2AE** |
| Hybrid claim | **HYSPEC front + tri-fuel band** |
| Language (RF) | **EU langs only** — RU overlay **н/д** |
| Label architecture | **Single-layer** EU wrap |
| Supply channel | **EU manufacture · parallel import proxy** (Top-Castrol.ru) |
| Anti-fraud UX | **Barcode + batch stamp**; QR **н/д** 5L front |
| Batch | **13/07/2023** DE01 0001782188 |
| PGMM macro-system | HYSPEC Hybrid Gate + Edge Hyperbole + Back-Loaded OEM (wiki/23) |
| Top ODSA risk | **API/ILSAC lacuna** · **OEM back-only** · **no RU** |
| Top СТМ attack | **API SP + GF-6A + ACEA C5 front** + **multi-OEM front** + official Cyrillic supply |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | Artifact-only lock · front+back photos |
| **DC-EP** | **A** |
| **Rev.** | **1 locked** · 25.06.2026 |
| **Pending optional** | GAP-CE-01 RU overlay · GAP-CE-02 FINDCAROIL.COM · GAP-CE-03 API below fold |

**DoD:** ✅ ODSA Castrol EDGE 0W-20 V 5L rev.1 locked · pair with [21](21_ODSA_mobil_1_0w_20_5L.md).

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · формат 5L · rev. 1

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|--------------|
| 1 | M_SYSTEM (PGMM) | hyspec_hybrid_gate + edge_hyperbole + back_loaded_oem | wiki/23 | H |
| 2 | Carrier morphology (PGMM) | 5L gold jug + integrated handle + red ribbed cap | wiki/23 | H |
| 3 | Класс продукта (синт / полусинт) | **Full syn implied** (EDGE + ACEA C5) — **not explicit on pack** | EVID-CE-11; CE-17; F-CE-09 | M |
| 4 | SAE 0W-20 — legibility | **High** — white box badge front + back header | EVID-CE-03; CE-08 | H |
| 5 | API — видимость (front / back) | Front: **—** · Back visible: **—** (GAP-CE-03) | EVID-CE-06; CE-16; F-CE-02 | H / M |
| 6 | ACEA — видимость (front / back) | Front: **—** · Back: **C5** | EVID-CE-06; CE-11 | H |
| 7 | OEM / допуски — front (effective) | **No OEM logos** — HYSPEC hybrid institutional only | EVID-CE-01; F-CE-03 | H |
| 8 | OEM / допуски — back / site / overlay | Honda, Hyundai, Kia, Nissan, Toyota, Volvo; Volvo RBS0-2AE | EVID-CE-10; CE-11 | H |
| 9 | Benefit-icons — доказуемость | **Moderate** — HYSPEC wedge + tri-fuel text (no icons) | EVID-CE-01; CE-04; wiki/23 | M |
| 10 | Cross-face consistency | **Partial pass** — SAE/HYSPEC OK; API/OEM/ACEA back-loaded | F-CE-15; CR-CE-02–03 | H |
| 11 | Digital / overlay vs pack gap | **Open** — FINDCAROIL.COM not triangulated | EVID-CE-05; F-CE-11 | L |
| 12 | Anti-fraud UX | **Barcode + batch**; QR **н/д** 5L | EVID-CE-13; CE-07; F-CE-10 | M |
| 13 | RF supply & языковая модель | **EU wrap** · parallel import proxy · **no RU overlay visible** | EVID-CE-12; F-CE-07–08 | M |
| 14 | Обязательная маркировка РФ | **н/д** on artifact — GAP-CE-01 | GAP-CE-01 | L |
| 15 | Кириллица vs латиница | **Latin only** (EU langs) | EVID-CE-12 | H |
| 16 | Thumbnail robustness (~120 px) | **High** — HYSPEC wedge + 0W-20 V box | wiki/23 | H |
| 17 | Cognitive load / negative space | **Medium** — premium white field front; dense back | wiki/23 | H |
| 18 | Legacy / rev. risk на полке | **Low–Medium** — 2023 batch; API stack **н/д visible** | EVID-CE-14 | M |

---

## Issues for discussion

1. **API below fold:** Нужен zoom back label или второй ракурс для закрытия GAP-CE-03?
2. **0W-20 matrix:** Добавить Castrol × Mobil rows в отдельную `матрица_0W-20` или достаточно point ref в [08](08_PGMM_упаковка.md)?
3. **HYSPEC vs tri-fuel:** Retail test — покупатель читает hybrid или universal band?
4. **RU overlay:** Есть ли кириллический sticker на импортном SKU в РФ?
5. **FINDCAROIL.COM:** Верифицировать в wiki/04 и triangulation rev.2?
