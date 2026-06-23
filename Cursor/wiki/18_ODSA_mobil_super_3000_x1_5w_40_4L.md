# ODSA — Mobil Super 3000 x1 5W-40 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_SUPER3000_X1_5W40_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 (Copilot) · Depth: Compact  
**Связь PGMM:** [12_PGMM_mobil_super_3000_x1_5w_40.md](12_PGMM_mobil_super_3000_x1_5w_40.md) · delta 1L: [13_…](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md)  
**Дата:** 23.06.2026 · **Rev.:** 3 (locked · RU overlay text attestation)  
**Формат:** 4L · base wrap EN/TR + **RU translation sticker** (parallel import)  
**Статус:** ✅ **Locked** (DC-EP:A · operator accept as-is) · optional: GAP-M02 digital · GAP-M06 shelf photo

**Supply channel:** Mobil **официально в РФ не поставляется** (M15); import base + **RU overlay** (M14, M16–M17).

**Canonical URL:** н/д · GAP-M02 waived at lock

---

## Executive summary (rev. 3 · locked)

**Канон SKU** (M01 + M03–M05 + M13 + **M16–M17**): **Mobil Super 3000 x1 5W-40 4L**, синтетическое моторное масло — **согласовано** base (EN «Fully Synthetic») ↔ RU overlay («синтетическое моторное масло»).

**RF channel model:** **двухслойная этикетка** — import base **GB+TR** + RU sticker: **дословный перевод описания** + блок спецификаций (M17). Фото overlay **нет**; текст зафиксирован operator attestation (M16–M17) — **принято at lock**.

**Cross-face (base wrap):** Partial pass — F-M02 (API off front), F-M03 (OEM back-only).

**Overlay vs base:** RU specs **⊃ base** по API/AAE/GM (F-M13); **AVTOVAZ** на base back (M05), **отсутствует** в RU-списке (F-M14).

**vs LUKOIL/GPN:** слабее **integrated native wrap** и **official RF supply**; overlay даёт **более широкий API/OEM list**, чем видимый base back.

| Severity rollup (locked) | Count |
|--------------------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 5 |
| Minor | 3 |
| Positive | 3 |

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
| ART-001 | Artifact (photo) | Оператор 23.06.2026 | Фронт 4L | Public |
| ART-002 | Artifact (photo) | Оператор 23.06.2026 | Оборот base — specs EN/TR | Public |
| ART-003 | Artifact (photo) | autorus.ru 23.06.2026 | 3/4 view; штамп 2022; barcode | Public |
| ART-004 | Document | wiki/12 | PGMM full 4L | Internal |
| ART-005 | Document | wiki/13 | PGMM delta 1L | Internal |
| ART-006 | Context | Оператор 23.06.2026 | Wrap **не менялся с 2022** | Internal |
| ART-007 | Context | Оператор 23.06.2026 | Parallel import; RU sticker applied | Internal |
| **ART-008** | **Context (text)** | **Оператор 23.06.2026** | **RU overlay: описание + specs block** (verbatim attestation) | Internal |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-M01 | Artifact | ART-001 | Mobil Super **3000 x1**; **Fully Synthetic Engine Oil**; **5W-40**; **ACEA A3/B4**; **4L** | A | Active |
| EVID-M02 | Artifact | ART-001 | **API grade не на фронте** | A | Active |
| EVID-M03 | Artifact | ART-002 | EN benefit copy: fully synthetic, demanding conditions | A | Active |
| EVID-M04 | Artifact | ART-002 | Meets: ACEA A3/B3, A3/B4; **API SJ/SL/SM/SN**; FIAT M2; **AAE B6** | A | Active |
| EVID-M05 | Artifact | ART-002 | Approved: VW, **MB 229.3**, Porsche, Renault, PSA, **AVTOVAZ** | A | Active |
| EVID-M06 | Artifact | ART-002 | ExxonMobil Quality Level: **API CF** | A | Active |
| EVID-M07 | Artifact | ART-002 | Base: **GB + TR** | A | Active |
| EVID-M08 | Artifact | ART-002 | Allergen C14-16-18 ALKYL PHENOL | A | Active |
| EVID-M09 | Artifact | ART-003 | MADE 25 10 2022; barcode 505107433584 | B | Active |
| EVID-M10 | Artifact | ART-003 | autorus.ru watermark | B | Context |
| EVID-M11 | Context | ART-004 | PGMM: OEM not shelf-readable front | B | Context |
| EVID-M12 | Context | ART-005 | PGMM delta 1L | B | Context |
| EVID-M13 | Context | ART-006 | Wrap stable since 2022 | B | Active |
| EVID-M14 | Context | ART-007 | RU translation sticker applied | B | Active |
| EVID-M15 | Context | ART-007 | Not official RF supply | B | Active |
| **EVID-M16** | **Context** | **ART-008** | RU: «…**синтетическое моторное масло**… длительный срок службы… защита… широком диапазоне температур» | **B** | **Active** |
| **EVID-M17** | **Context** | **ART-008** | RU specs: API **CF, SJ, SL, SM, SN, SN Plus, SP**; ACEA A3/B3, A3/B4; AAE **B6, B7**; FIAT M2; **GM LL-B-025**; Porsche A40; Renault RN0700/0710; VW 502/505; PSA B71 2296; **MB 229.3** | **B** | **Active** |

### RU overlay specs (canonical attestation · ART-008)

> Mobil Super 3000 X1 5W-40 представляет собой синтетическое моторное масло, обеспечивающее длительный срок службы двигателей в автомобилях различных типов и годов выпуска, а также повышенный уровень их защиты в широком диапазоне температур.
>
> API: CF, SJ, SL, SM, SN, SN Plus, SP · ACEA: A3/B3, A3/B4 · AAE: Group B6, Group B7 · FIAT: 9.55535-M2 · GM: GM-LL-B-025 · Porsche: A40 · Renault: RN0700, RN0710 · VW: 502 00, 505 00 · Peugeot Citroen: B71 2296 · MB: 229.3

### Conflict notes

| Conflict | Evidence | Resolution |
|----------|----------|------------|
| Front ACEA A3/B4 vs back +A3/B3 | M01 vs M04, M17 | **Open (CR-M01)** — selective front |
| Front no API vs back/overlay API | M02 vs M04, M17 | **Open (CR-M02)** — deictic; overlay widens list |
| EN/TR base vs RU overlay | M07 vs M16–M17 | **Closed (CR-M03)** — two-layer by design |
| Base back ⊂ RU overlay specs | M04–M06 vs M17 | **Open (CR-M05)** — overlay superset (F-M13) |
| AVTOVAZ base vs RU list | M05 vs M17 | **Open (CR-M06)** — F-M14 |
| 2022 batch vs current | M09 vs M13 | **Closed (CR-M04)** |

### Data gaps (at lock)

| Gap | Статус |
|-----|--------|
| GAP-M01 Rev. risk | **Closed** |
| GAP-M02 Digital triangulation | **Waived** at lock |
| GAP-M03 RU overlay | **Closed** — M16–M17 text attestation (photo waived) |
| GAP-M04 Operator attestation | **Closed** |
| GAP-M05 TDS | Optional |
| GAP-M06 Retail shelf @1.2 m | Open — н/д |

---

## Findings Catalogue

### F-M01 — Positive · Core claims coherent (syn · 5W-40 · 4L)

| Evidence IDs | EVID-M01; EVID-M03; EVID-M04; **EVID-M16** |
| **Observation** | Synthetic + 5W-40 + 4L — base EN ↔ RU overlay согласовано. |
| **Severity** | Positive · **High** |

---

### F-M02 — Major · API absent from front (base); only on back / RU overlay

| Evidence IDs | EVID-M01; EVID-M02; EVID-M04; EVID-M06; **EVID-M17** |
| **Observation** | Front: no API. Base back: SJ–SN + CF. RU overlay: CF through **SP, SN Plus**. |
| **Interpretation** | Shelf-facing **base front** не даёт API proof; RU overlay компенсирует **only if buyer reads sticker** (typically back/side). |
| **Severity** | **Major** · **High** |

---

### F-M03 — Major · OEM stack not on front base wrap

| Evidence IDs | EVID-M01; EVID-M05; EVID-M11; **EVID-M17** |
| **Observation** | Front: ACEA only. OEM on base back + **full list on RU overlay** (M17). |
| **Severity** | **Major** · **High** |

---

### F-M04 — Moderate · Two-layer label architecture (parallel import)

| Evidence IDs | EVID-M07; EVID-M14; EVID-M15; EVID-M16; EVID-M17 |
| **Observation** | Base EN/TR + RU overlay with verbatim description translation (M16) + specs (M17). |
| **Interpretation** | RF compliance via **importer overlay**, not integrated wrap. Accepted at lock without overlay photo. |
| **Severity** | **Moderate** · **Medium** |

---

### F-M12 — Moderate · Parallel import — no official RF channel

| Evidence IDs | EVID-M14; EVID-M15; EVID-M13 |
| **Severity** | **Moderate** · **Medium** |

---

### F-M13 — Moderate · RU overlay specs superset vs visible base back

| Evidence IDs | EVID-M04; EVID-M05; EVID-M06; **EVID-M17** |
| **Observation** | On RU overlay **only** (not on photographed base back): **API SN Plus, SP**; **AAE Group B7**; **GM LL-B-025**. |
| **Interpretation** | Parity **F-G04 GPN** pattern: secondary layer (overlay) **шире**, чем base label in evidence — deictic gap, not proven split-face defect. |
| **Severity** | **Moderate** · **Medium** |
| **Confounds** | Full base text outside photo crop; overlay = TDS-style superset |
| **Recommendations** | governance: overlay claims ⊆ verifiable base/TDS |

---

### F-M14 — Minor · AVTOVAZ on base back — absent from RU overlay list

| Evidence IDs | EVID-M05; **EVID-M17** |
| **Observation** | Base back: **AVTOVAZ** approved. RU attestation list (M17): **no AVTOVAZ**. |
| **Interpretation** | Possible overlay omission or selective translation; RF Lada-owner may miss OEM proof on RU layer. |
| **Severity** | **Minor** · **Medium** |
| **Confounds** | AVTOVAZ on another overlay zone; attestation incomplete |

---

### F-M05 — Moderate · ACEA A3/B3 — not on front base

| Evidence IDs | EVID-M01; EVID-M04; EVID-M17 |
| **Severity** | **Moderate** · **High** |

---

### F-M06 — Moderate · API framing asymmetry (base EN taxonomy)

| Evidence IDs | EVID-M04; EVID-M06; EVID-M17 |
| **Observation** | Base: «Meets SJ–SN» + separate «Quality Level CF». RU overlay: **flat API list** incl. SN Plus, SP. |
| **Severity** | **Moderate** · **Medium** |

---

### F-M07 — Minor (rev. 3 ↓) · Benefit narrative — RU available on overlay

| Evidence IDs | EVID-M03; **EVID-M16**; EVID-M07 |
| **Observation** | Base back EN prose (M03); RU overlay **full description in Russian** (M16). |
| **Severity** | **Minor** · **Medium** (was Moderate — overlay compensates for RF reader) |

---

### F-M08 — Minor · FIAT 9.55535-M2 vs N2 (competitors)

| Evidence IDs | EVID-M04; EVID-M17 |
| **Severity** | **Minor** |

---

### F-M09 — Minor · Allergen on base import wrap

| Evidence IDs | EVID-M08 |
| **Severity** | **Minor** · compliance flag only |

---

### F-M10 — Positive · Wrap stable since 2022

| Evidence IDs | EVID-M09; EVID-M13; EVID-M01 |
| **Severity** | Positive · **Medium** |

---

### F-M11 — Positive · No split-face API/base/volume defect on base wrap

| Evidence IDs | EVID-M01; EVID-M03; EVID-M04; EVID-M05 |
| **Severity** | Positive · **High** |

---

### F-M15 — Positive (new) · RU overlay restores RF-readable product description

| Evidence IDs | **EVID-M16**; EVID-M14 |
| **Observation** | Operator attestation: дословный RU перевод описания с оригинала. |
| **Severity** | Positive · **Medium** (text-only evidence) |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-M01 | Front ACEA ⊂ full ACEA | Open — F-M05 |
| CR-M02 | Front API absent | Open — F-M02 |
| CR-M03 | EN/TR vs RU RF | **Closed** — two-layer M14–M17 |
| CR-M04 | 2022 batch | **Closed** — M13 |
| CR-M05 | Base back ⊂ RU overlay specs | Open — F-M13 |
| CR-M06 | AVTOVAZ base vs RU list | Open — F-M14 |

---

## POV-маркировка (locked)

**Information Integrity**
- *Lacunae:* overlay photo waived; GAP-M06 shelf; no Mobil RF URL.
- *Redundancy:* RU overlay **duplicates** specs (operator: may mirror original) + **extends** API/OEM.
- *Contamination:* none on base wrap.
- *Collonisation:* importer overlay as RF compliance patch.

**Logical Coherence**
- *Conflicts:* overlay superset (CR-M05) — channel asymmetry, not proven false claim.
- *Contradictions:* AVTOVAZ gap (CR-M06) — minor deictic.

**System Dynamics**
- *Potentials:* СТМ — single-layer RU + front API/OEM + official supply.
- *Limits:* parallel import; overlay content B-grade (no photo).

**Relational States**
- *Compromise:* global base + local RU sticker accepted at lock.
- *Parities:* overlay gives **richer API list** than GPN front line; **weaker integration** than LUKOIL native wrap.

---

## Строка для сводной матрицы (ODSA × PGMM)

| Параметр | Mobil Super 3000 x1 5W-40 4L |
|----------|------------------------------|
| Product line | **Super 3000 x1** |
| API (front base / back base / RU overlay) | **— / SJ–SN + CF / CF–SP incl. SN Plus** |
| Base oil claim | **Fully Synthetic** (EN front + RU overlay) |
| ACEA | Front **A3/B4** · back + overlay **A3/B3, A3/B4** |
| OEM (front base) | **No** |
| OEM (back base) | VW, MB 229.3, Porsche, Renault, PSA, **AVTOVAZ**, FIAT M2 |
| OEM (RU overlay) | VW, MB, Porsche, Renault, PSA, FIAT, **+ GM LL-B-025** · **− AVTOVAZ** vs base |
| Language (RF) | Base **EN+TR** + **RU overlay** (text attestation M16–M17) |
| Label architecture | **Two-layer** (import + sticker) |
| Supply channel | **Parallel import** (not official RF) |
| Anti-fraud UX | **None** |
| Wrap currency | Stable since 2022 |
| PGMM macro-system | Техно-Витальная Броня (wiki/12) |
| Top ODSA risk | Front API/OEM absent · overlay superset unphotographed |
| Top СТМ attack | Single-layer native RU + SN/CF front + official supply |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | Operator: **accept as-is** · no RU overlay photo |
| **DC-EP** | **A** — Packet #1 locked; digital triangulation waived |
| **Rev.** | **3 locked** · 23.06.2026 |
| **Pending optional** | GAP-M02 EU URL · GAP-M06 shelf photo · overlay photo for audit upgrade |

**DoD:** ✅ ODSA Mobil 5W-40 4L locked · matrix row ready · parity wiki/16–17.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · формат 4L · rev. 3

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|--------------|
| 1 | M_SYSTEM (PGMM) | techno_vital_armor («Техно-Витальная Броня») | wiki/12; delta/13 §6 | H |
| 2 | Carrier morphology (PGMM) | «Торс» + рёбра + ручка | wiki/12; delta/13 §6 | H |
| 3 | Класс продукта (синт / полусинт) | **Fully Synthetic** (EN) · RU overlay: **синтетическое** | EVID-M01; M16 | H / M |
| 4 | SAE 5W-40 — legibility | **High** — gold badge, контраст vs чёрный/серебро | EVID-M01; delta/13 §6 | H |
| 5 | API — видимость (front / back) | Front: **—** · Back base: **SJ–SN + CF** · RU overlay: **CF–SP incl. SN Plus** | EVID-M02; M04; M17; F-M02 | H |
| 6 | ACEA — видимость (front / back) | **A3/B4 · A3/B3 + A3/B4** (front selective subset) | EVID-M01; M04; M17; F-M05 | H |
| 7 | OEM / допуски — front (effective) | **Нет** на base front | EVID-M01; M11; F-M03 | H |
| 8 | OEM / допуски — back / site / overlay | Base back: VW, MB 229.3, Porsche, Renault, PSA, **AVTOVAZ**, FIAT · Overlay: +**GM LL-B-025**, **−AVTOVAZ** vs base | EVID-M05; M17; F-M13; F-M14 | M |
| 9 | Benefit-icons — доказуемость | **Moderate** — иконки на 4L типичны; plasma ring = метафора | wiki/12; M01 | M |
| 10 | Cross-face consistency | **Partial pass** (base wrap); overlay = отдельный слой | EVID-M11; F-M11; CR-M03 | H |
| 11 | Digital / overlay vs pack gap | **RU overlay superset** vs photographed base back (API SP, GM, AAE B7) | EVID-M17 vs M04–M06; F-M13 | M |
| 12 | Anti-fraud UX | **None** | EVID-M01–M02; vs F-G09 | H |
| 13 | RF supply & языковая модель | **Parallel import** · base **EN+TR** + **RU overlay sticker** | EVID-M07; M14; M15; M16 | H |
| 14 | Обязательная маркировка РФ | Через **importer overlay** (text attestation); base: allergen, GB+TR | EVID-M08; M16–M17; F-M04 | M |
| 15 | Кириллица vs латиница | Base **EN dominant**; RF reader → **overlay RU** (M16) | EVID-M07; M16 | M |
| 16 | Thumbnail robustness (~120 px) | **High** — Mobil red + 5W-40 gold | delta/13 §6; wiki/12 | H |
| 17 | Cognitive load / negative space | **High uniform dense** — 100% label utilization | wiki/12; delta/13 §6 | H |
| 18 | Legacy / rev. risk на полке | **Low** — wrap stable since 2022 | EVID-M13; M09 | H |

---

## Сводка ODSA × PGMM (тройка конкурентов 4L)

| Параметр | LUKOIL LUXE | GPN Premium N | Mobil Super 3000 x1 |
|----------|-------------|---------------|---------------------|
| API front | SN/CF | SN/CF | **—** |
| RU native | ✅ integrated | ✅ integrated | **overlay sticker** |
| Supply | Official RF | Official RF | **Parallel import** |
| OEM front | No | Microtype | **No** |
| Anti-fraud | — | 3662.ru | **None** |
| Split-face risk | Closed (evolution) | Pass | Pass (base) |
