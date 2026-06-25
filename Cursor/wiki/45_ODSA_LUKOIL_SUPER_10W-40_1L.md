# ODSA — LUKOIL SUPER 10W-40 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_LUKOIL_SUPER_10W40_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md) · base 4L ODSA: [44_…](44_ODSA_LUKOIL_SUPER_10W-40_4L.md)  
**Дата:** 25.06.2026 · **Rev.:** 1 (front + **back photo locked** + site)  
**Формат:** 1L · official RF wrap · фронт + оборот + сайт LLK-03  
**Статус:** ✅ **Locked**

> **Не inherit:** оборот 1L **на фото** (не line inherit как LUXE 1L). Cross-format с [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md): primary claims **константа**; delta = объём + carrier + back density.

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **LUKOIL SUPER 10W-40 1L** — полусинтетическое · **API SG/CD** · domestic OEM (АВТОВАЗ · УМЗ · ЗМЗ).

**Cross-face 1L:** **Pass** — front API SG/CD + semi = back (EVID-LS1D-01–07) = site (EVID-LS1D-11).

**Cross-format (1L ↔ 4L):** **Pass** — API / base oil / OEM set **согласованы**; delta только **1L vs 4L** marker + carrier morphology.

**1L-specific gap:** OEM **back-only** **усилен** на doliv-канале (F-LS1D-02); front API SG **robust** @ close range (F-LS1D-03 Positive).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 5 |
| Minor | 2 |
| Positive | 5 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-LS1D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L |
| ART-LS1D-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 1L |
| ART-LS1D-003 | Document | wiki/43 | PGMM delta 1L |
| ART-LS1D-004 | Document | wiki/44 | ODSA 4L — cross-format ref |
| ART-LS1D-005 | Web | [LLK-03](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-super-10w-40) | ProductCard (line specs) |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-LS1D-01 | Artifact | ART-LS1D-001 | LUKOIL logo; «**УНИВЕРСАЛЬНОЕ МАСЛО**» + car icon; «**SUPER**»; «**ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» | A | Active |
| EVID-LS1D-02 | Artifact | ART-LS1D-001 | Front lockup: **10W-40 · API SG/CD · 1L** | A | Active |
| EVID-LS1D-03 | Artifact | ART-LS1D-001 | «**ActiPure**» + «**ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ**» — **micro-text** @ distance | A | Active |
| EVID-LS1D-04 | Artifact | ART-LS1D-001 | **OEM / ACEA на фронте не видны** | A | Active |
| EVID-LS1D-05 | Artifact | ART-LS1D-001 | Circular dimple grip; narrow bottle morphology | A | Active |
| EVID-LS1D-06 | Artifact | ART-LS1D-002 | Back: LUKOIL SUPER; **Semi-synthetic**; **10W-40**; **API SG/CD** | A | Active |
| EVID-LS1D-07 | Artifact | ART-LS1D-002 | OEM: **ПАО «АВТОВАЗ» · ОАО «УМЗ» · ПАО «ЗМЗ»** | A | Active |
| EVID-LS1D-08 | Artifact | ART-LS1D-002 | Barcode **4607161615366** (EAN-13; ≠ 4L 4607161615393) | A | Active |
| EVID-LS1D-09 | Artifact | ART-LS1D-002 | **EAC**; **1л**; multilang legal | A | Active |
| EVID-LS1D-10 | Artifact | ART-LS1D-002 | Production stamp: **07.08.22 · 2403 1 (B) · 22 06808014** | A | Active |
| EVID-LS1D-11 | Web | ART-LS1D-005 (LLK-03) | Line specs = [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) EVID-LS-11 | A | Active |
| EVID-LS1D-12 | Context | ART-LS1D-003 | PGMM delta: front API robust; OEM front lacuna ↑ on doliv | B | Context |
| EVID-LS1D-13 | Cross-format | ART-LS1D-004 · [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) | 4L batch 09.11.22 vs 1L 07.08.22 — same wrap rev. family | B | Active |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-LS1D-01 ISO/IATF on 1L back microtype | Open |
| GAP-LS1D-02 QR on 1L back | Open — not visible (as 4L) |
| GAP-LS1D-03 Site: separate 1L product card | Open — one line card LLK-03 |

---

## Findings Catalogue

### F-LS1D-01 — Positive · Cross-face 1L coherent (photo locked)

| Evidence IDs | EVID-LS1D-01; LS1D-02; LS1D-06; LS1D-07; LS1D-11 |
| **Observation** | Front SG/CD + semi = back = site. **No inherit dependency.** |
| **Severity** | **Positive** · **High** |

---

### F-LS1D-02 — Major · OEM back-only — amplified on doliv / impulse channel

| Поле | Значение |
|------|----------|
| **Observation** | Domestic OEM (LS1D-07) **only back**; front = universal + car (LS1D-04). На doliv-канале back-read **маловероятен** — inherits F-LS-02 with **↑ impact**. |
| **Evidence IDs** | EVID-LS1D-04; LS1D-07; LS1D-12 |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | structural: **2–3 OEM front** for 1L Classic/Protect SKU |

---

### F-LS1D-03 — Positive · Front API SG/CD survives 1L downscale

| Evidence IDs | EVID-LS1D-02; LS1D-12; cross-ref [29](29_ODSA_mobil_super_3000_x1_5w_40_1L.md) |
| **Observation** | Budget primary lockup **robust** @ close range and **better** than import 1L norm (no front API). |
| **Severity** | **Positive** · **High** |

---

### F-LS1D-04 — Moderate · ActiPure micro-degradation @ shelf distance

| Evidence IDs | EVID-LS1D-03; LS1D-12 |
| **Observation** | Innovation seal **below close-read threshold** @ ~2 m; conflict with SG chemistry **константа** (F-LS-03). |
| **Severity** | **Moderate** · **Medium** |

---

### F-LS1D-05 — Moderate · Universal service rhetoric vs 1L top-up semantics

| Evidence IDs | EVID-LS1D-01; LS1D-02; wiki/43 §2.5 |
| **Observation** | «УНИВЕРСАЛЬНОЕ МАСЛО» + 4L-equivalent claim stack; **нет** «doliv / exact 1L fill» rationale. |
| **Severity** | **Moderate** · **Medium** |

---

### F-LS1D-06 — Moderate · Back legal density ↑ proportional on small bottle

| Evidence IDs | EVID-LS1D-06; LS1D-09; wiki/43 §2.2 |
| **Severity** | **Moderate** · **High** |

---

### F-LS1D-07 — Positive · Cross-format claims Pass (1L ↔ 4L)

| Evidence IDs | EVID-LS1D-06; LS1D-07; [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) EVID-LS-06 |
| **Observation** | API SG/CD · semi · OEM set **aligned**; only volume marker differs. |
| **Severity** | **Positive** · **High** |

---

### F-LS1D-08 — Positive · RU Cyrillic back on 1L doliv SKU

| Evidence IDs | EVID-LS1D-09; LS1D-06 |
| **Severity** | **Positive** · **High** |

---

### F-LS1D-09 — Minor · Batch 07.08.22 vs 4L 09.11.22 — same wrap family

| Evidence IDs | EVID-LS1D-10; LS1D-13 |
| **Severity** | **Minor** · **Medium** |

---

### F-LS1D-10 — Major · ActiPure innovation vs API SG (inherits 4L)

| Evidence IDs | EVID-LS1D-03; LS1D-02; [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) F-LS-03 |
| **Severity** | **Major** · **High** (rhetoric tier) |

---

### F-LS1D-11 — Positive · Separate EAN routing 1L vs 4L

| Evidence IDs | EVID-LS1D-08; [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) EVID-LS-08 |
| **Observation** | Distinct barcodes; **no spec drift** between formats. |
| **Severity** | **Positive** · **High** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-LS1D-01 | OEM front vs back (1L doliv) | **Open** — F-LS1D-02 |
| CR-LS1D-02 | Universal 4L-style claims vs 1L volume | **Open** — F-LS1D-05; not API error |
| CR-LS1D-03 | ActiPure vs SG | **Open** — inherits CR-LS-02 |
| CR-LS1D-04 | 1L vs 4L primary specs | **Closed** — Pass (F-LS1D-07) |

---

## POV-маркировка

**Information Integrity:** **Lacunae** — OEM front on doliv; ActiPure proof; top-up semantics. **Redundancy** — universal quadruple-code **константа** при сжатии. **Contamination** — mesh crop (PGMM) **≠** claims layer.

**Logical Coherence:** Cross-face **Pass**; universal vs 1L volume **Conflict** without articulation.

**System Dynamics:** **Potential** — RU official 1L doliv + front API. **Limit** — back-only OEM on impulse. **Anomaly** — front SG **stronger** than import 1L category norm.

**Relational States:** **Parity** primary claims 1L↔4L. **Compromise** — DRY label rescale vs service-jug authority loss.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 1L · rev. 1 locked · **point-ref**

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Universal Mass Heuristic + Armor Lite + ActiPure + Domestic OEM (**константа** vs 4L) | wiki/43; EVID-LS1D-12 | H |
| 2 | Carrier morphology (PGMM) | Narrow top-up bottle + dimple grip; **no handle** | EVID-LS1D-05; wiki/43 §2.1 | H |
| 3 | Класс продукта (синт / полусинт) | **Полусинтетическое** · API **SG/CD** | EVID-LS1D-01; LS1D-02; LS1D-06; LS1D-11 | H |
| 4 | SAE 10W-40 — legibility | **High** — rel. size ↑ vs label width | EVID-LS1D-02; wiki/43 §2.2 | H |
| 5 | API — видимость (front / back) | **SG/CD · SG/CD** | EVID-LS1D-02; LS1D-06 | H |
| 6 | ACEA — видимость (front / back) | **Absent · Absent** | EVID-LS1D-04; LS1D-11 | H |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-LS1D-04; F-LS1D-02 | H |
| 8 | OEM / допуски — back / site / overlay | **АВТОВАЗ · УМЗ · ЗМЗ** | EVID-LS1D-07; LS1D-11 | H |
| 9 | Benefit-icons — доказуемость | ActiPure **micro** · site benefits only | EVID-LS1D-03; LS1D-11 | M |
| 10 | Cross-face consistency | **Pass** (1L photo locked) | EVID-LS1D-02 = LS1D-06 = LS1D-11 | H |
| 11 | Digital / overlay vs pack gap | Site **≈ pack** | EVID-LS1D-11 | H |
| 12 | Anti-fraud UX | **EAC + barcode + batch** · QR **н/д** | EVID-LS1D-08; LS1D-09 | M |
| 13 | RF supply & языковая модель | Official RF · Cyrillic front + back | EVID-LS1D-01; LS1D-09 | H |
| 14 | Обязательная маркировка РФ | EAC · barcode · batch · legal wall (**ISO — verify**) | EVID-LS1D-08; LS1D-10 | M |
| 15 | Кириллица vs латиница | Cyrillic dominant front + EN back header | EVID-LS1D-01; LS1D-06 | H |
| 16 | Thumbnail robustness (~120 px) | **High-medium** — SUPER + 10W-40 ✅ · ActiPure/1L **✗** @120 px | wiki/43 §4.3 | H |
| 17 | Cognitive load / negative space | **Bimodal** — clean front / **peak back** on small bottle | wiki/43 §2.6 | H |
| 18 | Legacy / rev. risk на полке | **Low–Moderate** — SG/CD stable; batch 07.08.22 | EVID-LS1D-10 | M |

---

## Импликации для СТМ 1L (Classic/Protect · 10W-40)

1. **Перенять:** front **SAE + API** + semi honesty (SUPER 1L **сильнее** Mobil 1L norm).
2. **Attack:** **OEM front row (2–3)** + **top-up semantic** («точный долив 1L») + fluid antidote — окна, которые SUPER **не закрывает**.
3. **Не копировать:** SUPER hyperbole stack + ActiPure void on doliv SKU.
4. **Format rule:** 1L и 4L — **раздельные строки**; не усреднять cognitive load.

---

## Issues for discussion

1. Сознательный **OEM back-load** для budget 1L или channel gap?
2. Включать SUPER 1L/4L в **будущую ветку 10W-40**?
3. Cross-ref 4L: [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) · PGMM [42](42_PGMM_LUKOIL_SUPER_10W-40.md) · [43](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md).

**DoD:** ODSA LUKOIL SUPER 10W-40 **1L — complete** (rev. 1 locked).
