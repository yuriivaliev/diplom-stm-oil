# ODSA — LUKOIL GENESIS ARMORTECH GC 5W-30 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_LUKOIL_GENESIS_ARMORTECH_GC_5W30_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md)  
**Дата:** 25.06.2026 · **Rev. 1:** locked (front + back + site)  
**Формат:** 4L · фронт + оборот + сайт LLK-01

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **LUKOIL GENESIS ARMORTECH GC 5W-30 4L** — fully synthetic Mid-SAPS · **API SN/CF** · **ACEA C3** · German OEM stack on back.

**Cross-face:** **Pass** — API SN/CF и ACEA C3 **согласованы front ↔ back** (EVID-LG-01–06); site LLK-01 **≈ pack** без superset gap.

**Ключевой gap vs LUXE 5W-40:** Genesis GC **выигрывает** в front standards visibility (API + ACEA C3 на лице); **проигрывает** в OEM front — полный German stack **только back** (F-LG-02).

**Batch note:** штамп **12.10.22** — facing 2022 rev.; retail freshness **verify** (F-LG-07).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 1 |
| Moderate | 3 |
| Minor | 2 |
| Positive | 3 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-LG-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 4L |
| ART-LG-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 4L (full + crop) |
| ART-LG-003 | Document | wiki/30 | PGMM _full 4L (context) |
| ART-LG-004 | Web | [LLK-01](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-genesis-armortech-gc-5w-30) | ProductCard + TDS link |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-LG-01 | Artifact | ART-LG-001 | «FOR GERMAN CARS» + GC shield; «GENESIS»; «ARMORTECH»; «FULLY SYNTHETIC ENGINE OIL»; DuraMax® | A | Active |
| EVID-LG-02 | Artifact | ART-LG-001 | Front lockup: **5W-30 · API SN/CF · ACEA C3 · 4L · GC** | A | Active |
| EVID-LG-03 | Artifact | ART-LG-002 | Back header: LUKOIL GENESIS ARMORTECH GC 5W-30; **API SN/CF · ACEA C3** | A | Active |
| EVID-LG-04 | Artifact | ART-LG-002 | OEM grid: **Porsche C30 · BMW LL-04 · MB 229.51/229.31 · VW 504 00/507 00 · Fiat 9.55535-S3** | A | Active |
| EVID-LG-05 | Artifact | ART-LG-002 | RU body: **синтетическое** Mid-SAPS; DPF/TWC; ООО «ЛЛК-Интернешнл»; Perm; ISO 9001:2015 · IATF 16949:2016 | A | Active |
| EVID-LG-06 | Artifact | ART-LG-002 | QR «Подробная информация»; barcode **4 670027 147055**; EAC; CLP H316/H317/H319; shelf life 5 yr | A | Active |
| EVID-LG-07 | Artifact | ART-LG-002 | Production stamp: **12.10.22 · 3529 2 · 22 06088037** | A | Active |
| EVID-LG-08 | Web | ART-LG-004 (LLK-01) | Site specs = EVID-LG-04; «Синтетическое… ПАО… DuraMax®»; TDS PDF 13.12.2022 | A | Active |
| EVID-LG-09 | Context | ART-LG-003 | PGMM: M_SYSTEM hyper-armor + German Cars; OEM back-only | B | Context |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-LG-01 Retail @1.2 m OEM readability | Open |
| GAP-LG-02 TDS chemistry (SAPS ppm, HTHS) vs pack claims | Open |
| GAP-LG-03 Share of 2022 vs newer facings on shelf | Open — н/д |

---

## Findings Catalogue

### F-LG-01 — Positive · Cross-face API/ACEA/SAE coherent

| Поле | Значение |
|------|----------|
| **Observation** | Front (EVID-LG-02): SN/CF + C3 + 5W-30 + 4L. Back (EVID-LG-03–04): идентичный API/ACEA + полный OEM. Site (EVID-LG-08) = back. |
| **Evidence IDs** | EVID-LG-02; LG-03; LG-04; LG-08 |
| **Severity & Confidence** | **Positive** · **High** |
| **Recommendations** | structural: benchmark для СТМ C3 — front standards lockup |

---

### F-LG-02 — Major · OEM-стек не на фронте канистры

| Поле | Значение |
|------|----------|
| **Observation** | Front: segment banner «FOR GERMAN CARS» + GC badge; **нет** Porsche/BMW/MB/VW/Fiat icons или microtype. OEM grid — только back (EVID-LG-04). |
| **Evidence IDs** | EVID-LG-01; LG-02; LG-04 |
| **Impact** | Trust · Revenue (OEM-driven German service) |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | quick: 2–3 top OEM icons на front row; structural: readable OEM band @1.2 m |

---

### F-LG-03 — Moderate · DuraMax® — claim без pack-level proof

| Поле | Значение |
|------|----------|
| **Observation** | «Innovative technology DuraMax®» на front (EVID-LG-01); на back/TDS — упоминание технологии, **без** расшифровки additive chemistry на этикетке. |
| **Evidence IDs** | EVID-LG-01; LG-05; LG-08 |
| **Severity & Confidence** | **Moderate** · **Medium** |
| **Falsification** | TDS или QR landing с tech proof |

---

### F-LG-04 — Moderate · Mid-SAPS / DPF-TWC — back-only chemistry disclosure

| Evidence IDs | EVID-LG-05 |
| **Observation** | Low-SAPS / aftertreatment compatibility — RU back text; front доминирует armor + «FULLY SYNTHETIC» EN |
| **Severity** | **Moderate** · **Medium** |

---

### F-LG-05 — Minor · EN front vs RU back language split

| Evidence IDs | EVID-LG-01; LG-05 |
| **Observation** | «FULLY SYNTHETIC ENGINE OIL» (EN front) + «синтетическое» (RU back) — **не contradiction**, industry norm для official RU supply |
| **Severity** | **Minor** · **High** |

---

### F-LG-06 — Positive · Front API+ACEA — white space vs mass-mid RU norm

| Evidence IDs | EVID-LG-02; cross-ref [16](16_ODSA_LUKOIL_LUXE_5W-40_4L.md) |
| **Observation** | ACEA C3 **на фронте** — сильнее LUXE 5W-40 (ACEA front —) |
| **Severity** | **Positive** · **High** |

---

### F-LG-07 — Minor · Batch 2022 — label-age shelf risk

| Evidence IDs | EVID-LG-07 |
| **Observation** | Production **12.10.22**; site TDS **13.12.2022** — coherent rev.; доля старых facings на полке **н/д** |
| **Severity** | **Minor** · **Medium** |

---

### F-LG-08 — Positive · Institutional trust stack (QR + EAC + ISO/IATF)

| Evidence IDs | EVID-LG-05; LG-06; LG-08 |
| **Severity** | **Positive** · **High** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-LG-01 | OEM front (banner) vs OEM back (full grid) | **Open** — F-LG-02; intentional back-load, не split-face error |
| CR-LG-02 | Armor visual vs Mid-SAPS chemistry | **Open** — PGMM conflict (wiki/30); ODSA claims **coherent** |
| CR-LG-03 | Site vs pack | **Closed** — LLK-01 ≈ EVID-LG-04 |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — OEM front, SAPS ppm, HTHS. **Redundancy** — FOR GERMAN CARS + ARMORTECH + carbon + GC. **Contamination** — carbon = motorsport + armor (PGMM).

**Logical Coherence:** Cross-face API/ACEA **Pass**; segment banner ≠ OEM list — **не contradiction**.

**System Dynamics:** **Anomaly** — front C3 lockup (vs LUXE). **Potential** — German OEM back depth. **Limit** — 2022 batch photo.

**Relational States:** **Consensus** pack = site. **Compromise** — armor metaphor vs eco-chemistry disclosure.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 4L · rev. 1 locked

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Nominal Hyper-Armor + German Cars Sovereignty + Front Standards Transparency | wiki/30; EVID-LG-09 | H |
| 2 | Carrier morphology (PGMM) | 4L asymmetrical jug + integrated handle + level strip | wiki/30; ART-LG-001 | H |
| 3 | Класс продукта (синт / полусинт) | **Fully synthetic** · API **SN/CF** | EVID-LG-01; LG-02; LG-05; LG-08 | H |
| 4 | SAE 5W-30 — legibility | **High** — oversized white badge | EVID-LG-02 | H |
| 5 | API — видимость (front / back) | **SN/CF · SN/CF** | EVID-LG-02; LG-03 | H |
| 6 | ACEA — видимость (front / back) | **C3 · C3** | EVID-LG-02; LG-03 | H |
| 7 | OEM / допуски — front (effective) | **Нет** — segment banner «FOR GERMAN CARS» + GC badge only | EVID-LG-01; LG-02; F-LG-02 | H |
| 8 | OEM / допуски — back / site / overlay | Porsche C30 · BMW LL-04 · MB 229.51/229.31 · VW 504/507 · Fiat 9.55535-S3 | EVID-LG-04; LG-08 | H |
| 9 | Benefit-icons — доказуемость | DuraMax® **named** · Mid-SAPS/DPF **text back only** · no tribology icons | EVID-LG-01; LG-05 | M |
| 10 | Cross-face consistency | **Pass** | EVID-LG-02 = LG-03–04 = LG-08 | H |
| 11 | Digital / overlay vs pack gap | Site **≈ pack** (no superset) | EVID-LG-08 vs LG-04 | H |
| 12 | Anti-fraud UX | **QR** + EAC + barcode + batch stamp | EVID-LG-06; LG-07 | H |
| 13 | RF supply & языковая модель | Official LLK-International · Perm · integrated RU back + EN front claims | EVID-LG-05; LG-06 | H |
| 14 | Обязательная маркировка РФ | Производитель · ISO/IATF · EAC · CLP · shelf life 5 yr | EVID-LG-05; LG-06 | H |
| 15 | Кириллица vs латиница | EN dominant front («GENESIS», «FULLY SYNTHETIC») · RU back body + KZ footer | EVID-LG-01; LG-05 | H |
| 16 | Thumbnail robustness (~120 px) | **High** — FOR GERMAN CARS + 5W-30 + API/ACEA row | wiki/30; EVID-LG-02 | H |
| 17 | Cognitive load / negative space | **High** — armor triple-code + dense back legal | wiki/30 | H |
| 18 | Legacy / rev. risk на полке | **Low–Moderate** — stable wrap; batch 2022 · newer rev. **verify** | EVID-LG-07 | M |

---

## Импликации для СТМ

1. **Перенять:** front API + ACEA lockup для C3 SKU (Genesis сильнее LUXE/Mobil mass-mid).
2. **Не копировать:** «FOR X CARS» ethnic banner без OEM proof на том же лице.
3. **White space:** 2–3 readable OEM icons на front @1.2 m — Genesis не закрывает.
4. Point-ref 5W-30 C3 — **отдельная строка** вне матриц 5W-40/0W-20.

---

## Issues for discussion

1. Включать ли Genesis GC 4L в будущую **C3-ветку** матрицы?
2. QR landing content — anti-fraud depth vs marketing redirect.
3. Cross-ref GPN Premium C3 — [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) · [37](37_ODSA_Gazpromneft_Premium_C3_5W-30_1L.md) ✅.

**DoD:** ODSA GENESIS ARMORTECH GC 5W-30 **4L — complete** (rev. 1 locked).
