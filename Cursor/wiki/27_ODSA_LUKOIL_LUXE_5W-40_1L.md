# ODSA — LUKOIL LUXE 5W-40 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_LUKOIL_LUXE_5W40_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md](14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md) · base 4L ODSA: [16_…](16_ODSA_LUKOIL_LUXE_5W-40_4L.md)  
**Дата:** 25.06.2026 · **Rev.:** 2 (front + **back line inherit 4L** + site)  
**Формат:** 1L · official RF wrap · фронт (фото) + оборот (**inherit** wiki/16) + сайт  
**Статус:** ✅ **Locked** (front + line back inherit · оператор: оборот 1L = оборот 4L)

> **Метод back inherit:** для одной линейки **LUXE SYNTHETIC 5W-40** оборотная этикетка **DRY** — claims-блок (API/OEM/ACEA/производитель) **идентичен** 4L ([16](16_ODSA_LUKOIL_LUXE_5W-40_4L.md) EVID-L03–L06); на фронте delta только маркер объёма **1L** vs **4L**.

---

## Executive summary (rev. 2 · locked)

**Канон SKU:** **LUKOIL LUXE SYNTHETIC 5W-40 1L** — front (EVID-L1D-01–08) + back (**inherit** EVID-L03–L06 via [16](16_ODSA_LUKOIL_LUXE_5W-40_4L.md)) + site (EVID-L1D-10).

**Cross-face 1L:** **Pass** — front API SN/CF + синтетика = back inherit L03–L05 = site L09/L1D-10.

**Cross-format (1L ↔ 4L):** **Pass** — primary claims согласованы; delta только C-геометрия и футер **1L**.

**Актуальные findings:** OEM **не на фронте** (F-L1D-02, = F-L03 4L); API/1L **ниже thumbnail** (F-L1D-04/05); legacy facings line risk (F-L1D-09).

| Severity rollup (rev. 2) | Count |
|--------------------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 4 |
| Minor | 2 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-L1D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L (`lukoil_luxe_5w-40_1L`) |
| ART-L1D-002 | Document | wiki/14 | PGMM delta 1L |
| ART-L1D-003 | Document | wiki/16 | ODSA 4L — **канон оборота** EVID-L03–L06 |
| ART-L1D-004 | Web | [lukoil-masla.ru ProductCard](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-luxe-synthetic-5w-40) | Line specs + TDS link |
| ART-L1D-005 | Operator attestation | Оператор 25.06.2026 | Оборот 1L = оборот 4L (same wrap rev.) |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-L1D-01 | Artifact | ART-L1D-001 | LUKOIL logo; **LUXE SYNTHETIC**; золотой корпус; красная крышка | A | Active |
| EVID-L1D-02 | Artifact | ART-L1D-001 | «**УНИВЕРСАЛЬНОЕ МАСЛО**» + иконка легкового авто | A | Active |
| EVID-L1D-03 | Artifact | ART-L1D-001 | «**СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» (кириллица) | A | Active |
| EVID-L1D-04 | Artifact | ART-L1D-001 | Футер: **5W-40 \| API SN/CF \| 1L** | A | Active |
| EVID-L1D-05 | Artifact | ART-L1D-001 | **OEM / ACEA на фронте не видны** | A | Active |
| EVID-L1D-06 | Artifact | ART-L1D-001 | **ActiPure не виден** | A | Active |
| EVID-L1D-07 | Artifact | ART-L1D-001 | Honeycomb texture в тёмном ядре | A | Active |
| EVID-L1D-08 | Artifact | ART-L1D-001 | Shoulder grip-dimples | A | Active |
| EVID-L1D-09 | Context | ART-L1D-002 | PGMM: API/1L **ниже ~120 px** | B | Context |
| EVID-L1D-10 | Web | ART-L1D-004 | Line specs = EVID-L04 (4L) | A | Active |
| EVID-L1D-11 | **Line inherit** | ART-L1D-003 · [16](16_ODSA_LUKOIL_LUXE_5W-40_4L.md) **EVID-L03** | Back 4L: **API SN/CF**; **5W-40** | **A** (4L photo) · **B** (1L inherit) | Active |
| EVID-L1D-12 | **Line inherit** | ART-L1D-003 · **EVID-L04** | Back OEM: ACEA A3/B4,A3/B3; MB 226.5/229.3; VW 502/505; Fiat 9.55535-N2; Renault RN 0700/0710; PSA B71 2296; **АВТОВАЗ** | **A** (4L) · **B** (1L) | Active |
| EVID-L1D-13 | **Line inherit** | ART-L1D-003 · **EVID-L05** | Back: «**синтетическое** моторное масло… API SN/CF» | **A** (4L) · **B** (1L) | Active |
| EVID-L1D-14 | **Line inherit** | ART-L1D-003 · **EVID-L06** | Back: ООО «ЛЛК-Интернешнл»; ISO 9001:2015; IATF 16949:2016 | **A** (4L) · **B** (1L) | Active |
| EVID-L1D-15 | Context | ART-L1D-003 · **EVID-L10** | Front 4L current — cross-format ref | B | Active |
| EVID-L1D-16 | Operator | ART-L1D-005 | Back 1L wrap = back 4L current rev. | B | Active |

### Data gaps (updated)

| Gap | Статус |
|-----|--------|
| GAP-L1D-01 Back label 1L **фото** | **Partial** — claims закрыты inherit; фото 1L back **не привязано** |
| GAP-L1D-02 EAC / штамп / batch на 1L | Open — inherit 4L: EAC **verify** ([16](16_ODSA_LUKOIL_LUXE_5W-40_4L.md) row 14 M) |
| GAP-L1D-03 QR / anti-fraud | **Closed** — нет на front 1L (как 4L current) |
| GAP-L1D-04 Site: 1L vs 4L card | Open — одна line card |

---

## Findings Catalogue

### F-L1D-01 — Positive · Front claim stack coherent with 4L + back inherit

| Evidence IDs | EVID-L1D-01; L1D-03; L1D-04; L1D-11; L1D-13; L1D-15 |
| **Severity** | Positive · **High** |

---

### F-L1D-02 — Major · OEM-стек не на фронте (inherits F-L03 4L)

| Evidence IDs | EVID-L1D-05; L1D-12; L1D-10 |
| **Severity** | **Major** · **High** |

---

### F-L1D-03 — ~~Major~~ **Closed** · Back inherit 4L — cross-face Pass

| Поле | Значение |
|------|----------|
| **Observation** | Оборот 1L **не на фото**, но оператор + [16](16_ODSA_LUKOIL_LUXE_5W-40_4L.md) EVID-L03–L06: API SN/CF, синтетика, OEM stack, ISO/IATF. Front 1L = те же claims. |
| **Evidence IDs** | EVID-L1D-04; L1D-11; L1D-12; L1D-13; L1D-14; L1D-16 |
| **Severity (rev. 2)** | **Closed** · Confidence **High** (line inherit + operator) |
| **Falsification** | Фото back 1L с расхождением vs L03–L06 |

---

### F-L1D-04 — Moderate · API SN/CF на фронте — ниже thumbnail-порога

| Evidence IDs | EVID-L1D-04; L1D-09 |
| **Severity** | **Moderate** · **High** |

---

### F-L1D-05 — Moderate · «1L» subordinate — thumbnail fail

| Evidence IDs | EVID-L1D-04; L1D-09 |
| **Severity** | **Moderate** · **Medium** |

---

### F-L1D-06 — Moderate · ACEA on back inherit only (not front)

| Evidence IDs | EVID-L1D-05; L1D-12; L1D-10 |
| **Severity** | **Moderate** · **High** |

---

### F-L1D-07 — Positive · Car pictogram on 1L

| Evidence IDs | EVID-L1D-02 |
| **Severity** | Positive · **High** |

---

### F-L1D-08 — Positive · ActiPure absent — current SYNTHETIC line

| Evidence IDs | EVID-L1D-06; L1D-15 |
| **Severity** | Positive · **High** |

---

### F-L1D-09 — Major · Legacy SL/semi facings (line)

| Evidence IDs | wiki/16 EVID-L01; L1D-15 |
| **Severity** | **Major** · **Medium** |

---

### F-L1D-10 — Minor · ISO/IATF — back inherit (4L photo); EAC verify

| Evidence IDs | EVID-L1D-14; wiki/16 row 14 |
| **Severity** | **Minor** · **Medium** |

---

### F-L1D-11 — Positive · Cross-face + cross-format consistency

| Поле | Значение |
|------|----------|
| **Observation** | 1L front SN/CF + syn = back inherit L03/L05 = site = 4L front L10. |
| **Evidence IDs** | EVID-L1D-04; L1D-11; L1D-13; L1D-10; L1D-15 |
| **Severity** | **Positive** · **High** |

---

### F-L1D-12 — Minor · Site line card — no 1L-specific pack render verified

| Evidence IDs | EVID-L1D-10; GAP-L1D-04 |
| **Severity** | Minor · **Medium** |

---

## Contradiction Register (rev. 2)

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-L1D-01 | 1L front SN vs stale wiki/10 SL | **Closed** |
| CR-L1D-02 | OEM back only ↔ shelf 1L | **Open** — F-L1D-02 |
| CR-L1D-03 | 1L front vs 1L back | **Closed** — line inherit L03–L06 |
| CR-L1D-04 | Site line card vs pack 1L | **Open** — GAP-L1D-04 |

---

## POV-маркировка (rev. 2)

**Information Integrity:** *Lacunae:* фото back 1L, EAC/штамп batch; *Redundancy:* SYNTHETIC + кириллица + «универсальное»; *Consensus:* inherit 4L back закрывает claims layer.

**Logical Coherence:** *Consensus:* cross-face Pass; *Conflict:* OEM shelf vs back-only — category norm.

**System Dynamics:** *Potential:* gold top-up salience; *Limit:* API/1L @120px.

**Relational States:** *Parity:* claims 1L = 4L line; *Compromise:* DRY back inherit без фото 1L.

---

## Строка для сводной матрицы (ODSA × PGMM) — rev. 2

| Параметр | LUKOIL LUXE 5W-40 1L |
|----------|------------------------|
| Product line | **LUXE SYNTHETIC** |
| API (front / back) | **SN/CF · SN/CF** (back inherit L03) |
| Base oil claim | **Синтетическое** (front + back inherit L05) |
| Cross-format | **Pass** vs 4L L10 |
| OEM on front | **Нет** |
| OEM (back / site) | Back inherit L04 + site: VW, MB, Renault, PSA, Fiat, AVTOVAZ, ACEA |
| Cross-face consistency | **Pass** (line inherit) |
| Thumbnail | LUXE+5W-40 ✅ · API/1L ❌ |
| Legacy shelf risk | SL/semi facings possible |

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Формат 1L · rev. 2 locked (back inherit 4L)

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|--------------|
| 1 | M_SYSTEM (PGMM) | industrial_hyper_armor + epistemic_void | wiki/14; wiki/10 | H |
| 2 | Carrier morphology (PGMM) | Узкая бутылка + shoulder grip; **no handle** | EVID-L1D-08; wiki/14 | H |
| 3 | Класс продукта (синт / полусинт) | **Синтетическое** · API **SN/CF** (front + back inherit) | L1D-03; L1D-04; L1D-11; L1D-13 | H |
| 4 | SAE 5W-40 — legibility | **High** full view · rel. ↑ | EVID-L1D-04; L1D-11; wiki/14 | H |
| 5 | API — видимость (front / back) | **SN/CF · SN/CF** | L1D-04; **L1D-11** (inherit L03) | H |
| 6 | ACEA — видимость (front / back) | Front: **—** · Back: **A3/B4, A3/B3** (inherit L04) | L1D-05; **L1D-12** | H |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-L1D-05; F-L1D-02 | H |
| 8 | OEM / допуски — back / site / overlay | Back inherit L04 + site: VW, MB, Renault, PSA, Fiat, **AVTOVAZ** | L1D-12; L1D-10 | H |
| 9 | Benefit-icons — доказуемость | **Low** — car pictogram; ActiPure absent | L1D-02; L1D-06 | H |
| 10 | Cross-face consistency | **Pass** (front + inherit back) | L1D-04 = L1D-11–13; F-L1D-11 | H |
| 11 | Digital / overlay vs pack gap | Site **≈ pack** (inherit + site) | L1D-10 vs L1D-12 | H |
| 12 | Anti-fraud UX | **—** | EVID-L1D-01 | H |
| 13 | RF supply & языковая модель | **Official RF** · integrated native wrap | L1D-03; L1D-14 | H |
| 14 | Обязательная маркировка РФ | ЛЛК-Интернешнл; ISO/IATF (inherit L06); EAC **verify** | **L1D-14**; wiki/16 | M |
| 15 | Кириллица vs латиница | **Кириллица dominant** + LUXE SYNTHETIC EN | L1D-02; L1D-03 | H |
| 16 | Thumbnail robustness (~120 px) | **Med-high** — LUXE+5W-40 ✅; API/1L **fail** | wiki/14; L1D-09 | H |
| 17 | Cognitive load / negative space | **High uniform** | wiki/14 §2.2 | H |
| 18 | Legacy / rev. risk на полке | **Major** — SL/semi facings (line) | wiki/16 F-L10 | M |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | **Locked** — front photo + back **line inherit** wiki/16 EVID-L03–L06 (operator attestation) |
| **Upgrade path** | Optional: фото back 1L → подтвердить EAC/штамп/batch (GAP-L1D-02) |
| **Rev.** | **2 locked** · 25.06.2026 |

---

## Issues for discussion

1. Фото back 1L — только для EAC/штамп (claims уже закрыты inherit).
2. СТМ 1L: API band + 1L + one OEM icon ([14](14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md) §4.3).
3. URL lukoil-masla.ru → wiki/04.

**DoD:** ODSA LUKOIL 5W-40 1L — **complete** (rev. 2 locked). Pending: GAP-L1D-02 (EAC photo 1L), wiki/04.
