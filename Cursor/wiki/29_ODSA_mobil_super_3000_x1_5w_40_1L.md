# ODSA — Mobil Super 3000 x1 5W-40 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_SUPER3000_X1_5W40_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md) · base 4L ODSA: [18_…](18_ODSA_mobil_super_3000_x1_5w_40_4L.md)  
**Дата:** 25.06.2026 · **Rev.:** 2 (front + line inherit 4L · **QR presence locked; destination waived**)  
**Формат:** 1L · import base wrap EN + **RU translation sticker** (parallel import, line-level)  
**Статус:** 🟡 **Provisional lock** (front verified · back/overlay **inherit** wiki/18 · back 1L photo n/d)

> **Метод line inherit:** для линейки **Super 3000 x1 5W-40** base back + RU overlay specs **наследуются** из [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) (EVID-M04–M06, M16–M17); delta на фронте — маркер **1L**, **QR + 819697D** (наличие зафиксировано; **назначение не верифицируем** — operator: может вести на сайт с информацией о линейке), отсутствие benefit-icons (mocc_028).

---

## Executive summary (rev. 2 · provisional)

**Канон SKU (visible):** **Mobil Super 3000 x1 5W-40 1L** — front (EVID-MS1D-01–12) + back/overlay (**inherit** EVID-M04–M06, M16–M17 via [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md)).

**QR 819697D:** **присутствует** на фронте (EVID-MS1D-06) · alphanum **819697D** · **назначение/landing не верифицируем** (GAP-MS1D-03 **closed waived**) · operator attestation: **может** содержать ссылку на сайт с информацией о **линейке** Super 3000 x1 — **marketing/line-info**, **не** anti-fraud UX (≠ GPN 3662).

**Cross-face 1L (base front vs inherit back):** **Partial pass** — synthetic + 5W-40 + ACEA A3/B4 согласованы; API/OEM **off front** (inherits F-M02, F-M03 4L).

**Cross-format (1L ↔ 4L):** **Partial** — primary claims aligned; delta: **QR front (1L-only)**, **benefit-icons absent**, carrier morphology, bimodal cognitive load (delta/13).

**vs LUKOIL/GPN 1L:** слабее integrated RF wrap и official supply; **digital:** QR на фронте 1L (line-info affordance, не верифицирован); **слабее** claim layer vs LUKOIL (нет API на фронте).

| Severity rollup (rev. 2) | Count |
|--------------------------|-------|
| Blocker | 0 |
| Major | 3 |
| Moderate | 5 |
| Minor | 4 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-MS1D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L (`mobil_super_3000_x1_5w_40_1l`) |
| ART-MS1D-002 | Document | wiki/13 | PGMM delta 1L |
| ART-MS1D-003 | Document | wiki/18 | ODSA 4L — **канон back + RU overlay** EVID-M04–M06, M16–M17 |
| ART-MS1D-004 | Context (text) | wiki/18 ART-008 | RU overlay attestation (line inherit) |
| ART-MS1D-005 | Context | wiki/18 ART-006–007 | Parallel import; wrap stable since 2022 |
| **ART-MS1D-006** | **Context** | **Оператор 25.06.2026** | **QR 819697D:** наличие подтверждено; **назначение не верифицируем**; может вести на сайт линейки Super 3000 x1 | Internal |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-MS1D-01 | Artifact | ART-MS1D-001 | Mobil Super **3000 x1**; **Fully Synthetic Engine Oil**; **5W-40**; **1L** | A | Active |
| EVID-MS1D-02 | Artifact | ART-MS1D-001 | **ACEA A3/B4** на фронте (footer, белый микротекст) | A | Active |
| EVID-MS1D-03 | Artifact | ART-MS1D-001 | **Gasoline & Diesel** — оранжево-жёлтый footer | A | Active |
| EVID-MS1D-04 | Artifact | ART-MS1D-001 | **API grade не на фронте** | A | Active |
| EVID-MS1D-05 | Artifact | ART-MS1D-001 | **OEM / допуски не на фронте** | A | Active |
| EVID-MS1D-06 | Artifact | ART-MS1D-001 | **QR-код** + alphanum **819697D** — нижний левый чёрный блок рядом с **1L** (**наличие зафиксировано**) | A | Active |
| EVID-MS1D-07 | Artifact | ART-MS1D-001 | Узкий носитель; **7 grip-ridges** на правой грани | A | Active |
| EVID-MS1D-08 | Artifact | ART-MS1D-001 | Плазменное кольцо **усечено** по бокам этикетки | A | Active |
| EVID-MS1D-09 | Artifact | ART-MS1D-001 | **Benefit-icons отсутствуют** (vs типичный 4L) | A | Active |
| EVID-MS1D-10 | Context | ART-MS1D-002 | PGMM: API/1L **ниже ~120 px**; bimodal density | B | Context |
| EVID-MS1D-11 | **Line inherit** | ART-MS1D-003 · [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) **EVID-M04** | Back base: ACEA A3/B3,A3/B4; **API SJ–SN**; FIAT M2; AAE B6 | **A** (4L) · **B** (1L) | Active |
| EVID-MS1D-12 | **Line inherit** | ART-MS1D-003 · **EVID-M05** | Back base OEM: VW, **MB 229.3**, Porsche, Renault, PSA, **AVTOVAZ** | **A** (4L) · **B** (1L) | Active |
| EVID-MS1D-13 | **Line inherit** | ART-MS1D-003 · **EVID-M06** | Back base: ExxonMobil Quality Level **API CF** | **A** (4L) · **B** (1L) | Active |
| EVID-MS1D-14 | **Line inherit** | ART-MS1D-004 · **EVID-M16–M17** | RU overlay: синтетическое; API **CF–SP incl. SN Plus**; OEM + **GM LL-B-025**; **−AVTOVAZ** vs base | **B** | Active |
| EVID-MS1D-15 | Context | ART-MS1D-005 | Parallel import; base **GB+TR**; wrap stable since 2022 | B | Active |
| **EVID-MS1D-16** | **Context** | **ART-MS1D-006** | QR **819697D:** destination **не верифицируем**; operator: **может** → URL с информацией о **линейке** (marketing/line-info, not anti-fraud) | **B** | **Active** |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-MS1D-01 Back label 1L **фото** | **Open** — claims inherit 4L; не верифицировано на 1L unit |
| GAP-MS1D-02 RU overlay on 1L **фото** | **Partial** — line attestation [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) M16–M17 |
| GAP-MS1D-03 QR destination / purpose | **Closed (waived)** — **не верифицируем**; наличие QR + **819697D** зафиксировано (MS1D-06); operator attestation MS1D-16: plausible **line-info URL** |
| GAP-MS1D-04 Batch / barcode 1L | Open |
| GAP-MS1D-05 Digital triangulation | Waived (как 4L GAP-M02) |

---

## Findings Catalogue

### F-MS1D-01 — Positive · Core front claims coherent with 4L line

| Evidence IDs | EVID-MS1D-01; MS1D-02; MS1D-03; MS1D-11 |
| **Observation** | Synthetic + 5W-40 + ACEA A3/B4 + Gasoline&Diesel — согласовано с [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) EVID-M01. |
| **Severity** | Positive · **High** |

---

### F-MS1D-02 — Major · API absent from front (inherits F-M02 4L)

| Evidence IDs | EVID-MS1D-04; MS1D-11; MS1D-13; MS1D-14 |
| **Observation** | Front: no API. Inherit back: SJ–SN + CF. RU overlay: CF–SP. |
| **Interpretation** | Top-up buyer видит brand + viscosity; **нет shelf API proof** без чтения back/overlay. |
| **Severity** | **Major** · **High** |

---

### F-MS1D-03 — Major · OEM stack not on front (inherits F-M03 4L)

| Evidence IDs | EVID-MS1D-05; MS1D-12; MS1D-14 |
| **Severity** | **Major** · **High** |

---

### F-MS1D-04 — Major · Back 1L not photographed — audit B-grade on inherit

| Evidence IDs | GAP-MS1D-01; MS1D-11–MS1D-14 |
| **Observation** | Line inherit from 4L; **not unit-verified** on 1L sample. |
| **Recommendations** | structural: photo back 1L → lock upgrade |
| **Severity** | **Major** · **Medium** |

---

### F-MS1D-05 — Moderate · Two-layer RF (parallel import + RU overlay inherit)

| Evidence IDs | EVID-MS1D-14; MS1D-15; [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) F-M04 |
| **Severity** | **Moderate** · **Medium** |

---

### F-MS1D-06 — Moderate · RU overlay superset vs base back (inherit CR-M05)

| Evidence IDs | EVID-MS1D-11; MS1D-14; [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) F-M13 |
| **Severity** | **Moderate** · **Medium** |

---

### F-MS1D-07 — Moderate · ACEA A3/B3 on back/overlay only — front selective A3/B4

| Evidence IDs | EVID-MS1D-02; MS1D-11; MS1D-14; [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) CR-M01 |
| **Severity** | **Moderate** · **High** |

---

### F-MS1D-08 — Moderate · Benefit-icons absent on 1L (mocc_028)

| Evidence IDs | EVID-MS1D-09; ART-MS1D-002 mocc_028 |
| **Observation** | 4L typically carries benefit pictograms; 1L front — **lacuna**. |
| **Interpretation** | Top-up SKU теряет secondary rationale; только brand + viscosity + ACEA microtype. |
| **Severity** | **Moderate** · **High** |

---

### F-MS1D-09 — Minor · QR + 819697D manifest — destination non-verifiable (mocc_025)

| Evidence IDs | EVID-MS1D-06; **EVID-MS1D-16** |
| **Observation** | QR + **819697D** в нижнем блоке с **1L** — **присутствие подтверждено** на фото. Visible CTA / scan copy **н/д**. |
| **Interpretation** | **Не anti-fraud** (≠ 3662). Operator: QR **может** вести на сайт с информацией о **линейке** Super 3000 x1 — **digital line-info affordance**; landing **не верифицируем** и **не требуется** для lock по решению оператора. Format delta vs 4L (QR только на 1L front в evidence). |
| **Severity** | **Minor** · **Medium** |
| **Recommendations** | governance: для СТМ — явный QR MAP (scan → spec sheet); не считать Mobil QR proof-of-authenticity |

---

### F-MS1D-10 — Moderate · Thumbnail: 1L + QR fail @120px; brand + 5W-40 pass

| Evidence IDs | EVID-MS1D-01; MS1D-06; MS1D-10 |
| **Severity** | **Moderate** · **High** |

---

### F-MS1D-11 — Minor · AVTOVAZ on base back — absent from RU overlay (inherit CR-M06)

| Evidence IDs | EVID-MS1D-12; MS1D-14; [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) F-M14 |
| **Severity** | **Minor** · **Medium** |

---

### F-MS1D-12 — Minor · Gestalt plasma ring cropped — mocc_030

| Evidence IDs | EVID-MS1D-08; ART-MS1D-002 |
| **Severity** | **Minor** · **Medium** |

---

### F-MS1D-13 — Minor · Gasoline & Diesel footer — legibility ↓ at distance

| Evidence IDs | EVID-MS1D-03; MS1D-10 |
| **Severity** | **Minor** · **Medium** |

---

### F-MS1D-14 — Positive · QR on 1L — digital line-info affordance (1L-only vs 4L)

| Evidence IDs | EVID-MS1D-06; **EVID-MS1D-16** |
| **Observation** | 1L-only front element; **не** traceability/anti-fraud layer; plausible **line marketing** channel. |
| **Severity** | Positive · **Medium** (purpose attestation only; URL not verified) |

---

### F-MS1D-15 — Positive · Cross-format primary claims Pass (1L ↔ 4L)

| Evidence IDs | EVID-MS1D-01; MS1D-02; [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) EVID-M01 |
| **Severity** | Positive · **High** |

---

### F-MS1D-16 — Positive · Wrap line stable since 2022 (inherit)

| Evidence IDs | EVID-MS1D-15; [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) F-M10 |
| **Severity** | Positive · **Medium** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-MS1D-01 | Front ACEA ⊂ full ACEA | Open — F-MS1D-07 (inherit CR-M01) |
| CR-MS1D-02 | Front API absent | Open — F-MS1D-02 (inherit CR-M02) |
| CR-MS1D-03 | EN base vs RU overlay | **Closed** — two-layer inherit [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) CR-M03 |
| CR-MS1D-04 | Base back ⊂ RU overlay | Open — F-MS1D-06 (inherit CR-M05) |
| CR-MS1D-05 | AVTOVAZ base vs RU list | Open — F-MS1D-11 (inherit CR-M06) |
| CR-MS1D-06 | 1L QR vs 4L no front QR | **Closed** — format delta; QR = **line-info** affordance (MS1D-16), not split-face defect |

---

## POV-маркировка (rev. 2)

**Information Integrity**
- *Lacunae:* back 1L photo; benefit-icons (mocc_028). ~~QR destination~~ → **closed waived** (MS1D-16).
- *Redundancy:* ACEA + Gasoline&Diesel + Synthetic в нижнем кластере 1L.
- *Contamination:* none on visible front.
- *Collonisation:* RU overlay inherit as RF compliance patch.

**Logical Coherence**
- *Conflicts:* overlay superset (inherit); mild industrial-armor vs portable 1L C-geometry (delta/13).
- *Contradictions:* none split-face proven on unit.

**System Dynamics**
- *Potentials:* QR as **line-info** entry (unverified URL); top-up shelf density.
- *Limits:* API/OEM off-front; thumbnail 1L fail; parallel import.
- *Anomalies:* QR on 1L but not evidenced on 4L front — **format policy**, not error.

**Relational States**
- *Compromise:* DRY brand asset vs secondary claim loss on 1L.
- *Parities:* weaker than LUKOIL 1L (API front); **anti-fraud = none** (как 4L Mobil); QR ≠ GPN 3662-class.

---

## Строка для сводной матрицы (ODSA × PGMM)

| Параметр | Mobil Super 3000 x1 5W-40 **1L** |
|----------|----------------------------------|
| Product line | **Super 3000 x1** |
| API (front / back inherit / RU overlay inherit) | **— / SJ–SN + CF / CF–SP incl. SN Plus** |
| Base oil claim | **Fully Synthetic** (EN front) |
| ACEA | Front **A3/B4** · inherit **A3/B3, A3/B4** |
| OEM (front) | **No** |
| OEM (back/overlay inherit) | VW, MB 229.3, Porsche, Renault, PSA, FIAT, **+ GM LL-B-025** · **− AVTOVAZ** vs base |
| Language (RF) | Base **EN** + **RU overlay inherit** (text B-grade) |
| Label architecture | **Two-layer** (import + sticker inherit) |
| Supply channel | **Parallel import** |
| Anti-fraud UX | **None** (QR = line-info, **не** anti-fraud · MS1D-16) |
| Digital (QR) | **Present** — QR + **819697D** · destination **не верифицируем** · plausible **line marketing URL** |
| Format delta vs 4L | QR front · benefit-icons **absent** · grip vs handle |
| PGMM macro-system | techno_vital_armor (wiki/13) |
| Top ODSA risk | API/OEM off-front · back inherit unphotographed |
| Top СТМ attack | Clean 1L brief: API front + one benefit + **explicit QR → spec** (не line-info-only) |

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · формат **1L** · rev. 2

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | techno_vital_armor («Техно-Витальная Броня») | wiki/13; delta §1 | H |
| 2 | Carrier morphology (PGMM) | Узкая бутылка + **grip-ridges** (7 канавок) | EVID-MS1D-07; delta/13 §2.1 | H |
| 3 | Класс продукта (синт / полусинт) | **Fully Synthetic** (EN front) · RU overlay inherit: синтетическое | EVID-MS1D-01; MS1D-14 | H / M |
| 4 | SAE 5W-40 — legibility | **High** — gold badge; rel. ↑ vs ширина этикетки | EVID-MS1D-01; delta/13 §2.2 | H |
| 5 | API — видимость (front / back) | Front: **—** · Back inherit: **SJ–SN + CF** · RU overlay inherit: **CF–SP** | EVID-MS1D-04; MS1D-11; MS1D-13; MS1D-14; F-MS1D-02 | H / M |
| 6 | ACEA — видимость (front / back) | Front **A3/B4** · inherit **A3/B3 + A3/B4** | EVID-MS1D-02; MS1D-11; MS1D-14 | H / M |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-MS1D-05; F-MS1D-03 | H |
| 8 | OEM / допуски — back / site / overlay | Inherit base: VW, MB 229.3, Porsche, Renault, PSA, **AVTOVAZ**, FIAT · Overlay inherit: +**GM LL-B-025**, **−AVTOVAZ** | EVID-MS1D-12; MS1D-14; F-MS1D-06 | M |
| 9 | Benefit-icons — доказуемость | **Absent** (mocc_028) vs moderate 4L | EVID-MS1D-09; F-MS1D-08 | H |
| 10 | Cross-face consistency | **Partial pass** (front vs inherit back); unit back **n/d** | F-MS1D-04; inherit F-M11 | M |
| 11 | Digital / overlay vs pack gap | **RU overlay superset inherit**; **QR + 819697D present** · destination **не верифицируем** · plausible **line-info URL** (MS1D-16) | MS1D-14; MS1D-06; MS1D-16; F-MS1D-09 | M |
| 12 | Anti-fraud UX | **None** — QR **≠** anti-fraud (line-info affordance only) | EVID-MS1D-06; MS1D-16; vs F-G09 | H |
| 13 | RF supply & языковая модель | **Parallel import** · base **EN** + **RU overlay inherit** | MS1D-15; MS1D-14; F-MS1D-05 | H / M |
| 14 | Обязательная маркировка РФ | Через **importer overlay inherit**; base 1L back **n/d** | GAP-MS1D-01; MS1D-14; F-MS1D-04 | L |
| 15 | Кириллица vs латиница | Base **EN dominant**; RF reader → overlay RU (inherit B-grade) | EVID-MS1D-01; MS1D-14 | M |
| 16 | Thumbnail robustness (~120 px) | **Medium** — brand + 5W-40 OK; **1L + QR fail** | EVID-MS1D-10; F-MS1D-10; delta/13 §2.4 | H |
| 17 | Cognitive load / negative space | **Bimodal** — top rarefied / bottom hyper-dense | delta/13 §2.2 mocc_026–027 | H |
| 18 | Legacy / rev. risk на полке | **Low** — line wrap stable since 2022 (inherit) | MS1D-15; [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md) | H |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | **Provisional lock** — front verified; back/overlay line inherit [18] |
| **DC-EP** | **B** — pending back 1L photo for upgrade to A |
| **Rev.** | **2 provisional** · 25.06.2026 |
| **Pending** | GAP-MS1D-01 back photo · overlay photo on 1L unit |

**DoD:** 🟡 ODSA Mobil 5W-40 1L provisional · matrix row R6 ready · closes LAC-01 partial for Mobil.

---

## Issues for discussion

1. **Lock upgrade:** достаточно ли line inherit [18] для Mobil 1L или нужен unit back photo (как LUKOIL [27](27_ODSA_LUKOIL_LUXE_5W-40_1L.md) rev.2)?
2. ~~**QR 819697D:** сканировать~~ → **Closed waived** — наличие зафиксировано; назначение не верифицируем; operator: plausible line-info URL.
3. **1L QR vs 4L no QR:** format-specific digital policy (line-info on top-up SKU) — **CR-MS1D-06 closed**.
4. **Benefit-icons lacuna:** systematic Mobil DRY failure или acceptable top-up norm?

---

*ODSA rev.2 provisional · CASE `ODSA_MOBIL_SUPER3000_X1_5W40_1L_2026` · ingest 25.06.2026*
