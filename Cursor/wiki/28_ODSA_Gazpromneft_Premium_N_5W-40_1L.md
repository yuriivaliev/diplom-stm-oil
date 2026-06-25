# ODSA — Gazpromneft Premium N 5W-40 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_GPN_PREMIUM_N_5W40_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md) · base 4L ODSA: [17_…](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md)  
**Дата:** 25.06.2026 · **Rev.:** 3 (front A + back inherit B + **GPN-01 canonical back parity**)  
**Формат:** 1L · official RF wrap · фронт (фото) + оборот (**line inherit** 4L) + сайт  
**Статус:** 🟡 **Line-locked rev.3** · pending: photo back 1L verify · CR-G1D-01 (MB 229.5)

**Canonical URL:** [GPN-01](04_источники_и_URL.md) · см. § **Ключевые характеристики** · [17](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) § governance

**Back inherit rule (rev. 2–3):** содержание оборота 1L = **тот же wrap-template**, что у 4L ([17](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) ART-002, EVID-G04–G07), с заменой **4L → 1L** на штампе. **Rev.3:** back **должен** = GPN-01 «Ключевые характеристики» ([17](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) § governance) — фактически **inherit ⊂ canonical** (6 gaps).

---

## Executive summary (rev. 3 · line-locked)

**Канон line-level (GPN-01 «Ключевые характеристики»):** полностью синтетическое · **5W-40** · API **SN, CF** · ACEA **A3/B3, A3/B4** · OEM: BMW LL-01, GM LL-B-025, MB **226.5+229.3**, Porsche A40, PSA, Renault RN0700/RN0710, VW 502/505, AVTOVAZ, **УМЗ** — **должны быть на задней этикетке** всех фasовок ([17](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) § governance).

**Канон SKU 1L (artifact):** Premium N Synthetic **5W-40 1L** · front: SN/CF · ACEA A3/B4 · OEM microtype incl. **MB 229.5** (⚠ not on GPN-01).

**Back (inherit 4L):** SN/CF · A3/B4 · MB **229.3** · VW, Renault, PSA, AVTOVAZ, STO, 3662 — **не закрывает** 6 позиций GPN-01 (A3/B3, 226.5, BMW, GM, Porsche, УМЗ).

**Cross-face (1L):** **Partial** — core Pass; **MB 229.5↔229.3**; front частично закрывает site gaps, но **не на back**; **229.5 ∉ site**.

| Severity rollup (rev. 3) | Count |
|--------------------------|-------|
| Blocker | 0 |
| Major | 5 |
| Moderate | 5 |
| Minor | 2 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-G1D-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L Premium N 5W-40 |
| ART-G1D-002 | Document | wiki/15 | PGMM delta 1L |
| ART-G1D-003 | Document | wiki/17 | ODSA 4L — **источник back inherit** |
| ART-G1D-004 | Web | [GPN-01](04_источники_и_URL.md) | **«Ключевые характеристики»** + anti-fraud |
| **ART-G1D-005** | **Line inherit** | wiki/17 ART-002 | Оборот 4L → template 1L |
| **ART-G1D-006** | **Web canonical** | GPN-01 · operator 25.06.2026 | Verbatim блок «Ключевые характеристики» |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-G1D-01 | Artifact | ART-G1D-001 | GAZPROMNEFT logo; **PREMIUM N**; «**СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» + «SYNTHETIC ENGINE OIL» | A | Active |
| EVID-G1D-02 | Artifact | ART-G1D-001 | Оранжевый блок: **5W-40** (dominant) + **1L** (subordinate, bottom-right) | A | Active |
| EVID-G1D-03 | Artifact | ART-G1D-001 | Подвал: **API SN/CF** · **ACEA A3/B4** | A | Active |
| EVID-G1D-04 | Artifact | ART-G1D-001 | Подвал OEM: **MB-Approval 229.5**; **VW 502.00/505.00**; **Renault RN 0700/0710**; **BMW LL-01**; **Porsche A40**; **PSA B71 2296**; **GM-LL-B-025**; **AVTOVAZ** | A | Active |
| EVID-G1D-05 | Artifact | ART-G1D-001 | Иконка легкового авто над «PREMIUM N» | A | Active |
| EVID-G1D-06 | Artifact | ART-G1D-001 | Текст anti-fraud («УНИКАЛЬНАЯ СИСТЕМА…») на фронте 1L **не виден** (vs 4L G03) | A | Active |
| EVID-G1D-07 | Artifact | ART-G1D-001 | OEM/API подвал — **микрошрифт**; @~120 px **fail** | A | Active |
| EVID-G1D-08 | Context | ART-G1D-002 | PGMM: vertical rescale; claustrophobic density ↑ | B | Context |
| EVID-G1D-09 | Context | ART-G1D-003 | 4L front OEM: MB **229.3**, RN700/RN710, VW, PSA, AVTOVAZ | B | Cross-format ref |
| **EVID-G1D-13** | **Line inherit** | **ART-G1D-005** ← wiki/17 G04 | Back: **API SN/CF**; **ACEA A3/B4**; MB **229.3**; Renault **RN0700/RN0710**; VW 502 00/505 00; PSA B71 2296; ПАО «АВТОВАЗ»; **СТО 84035624-179-2015** | **B** | **Back inherit** |
| **EVID-G1D-14** | **Line inherit** | **ART-G1D-005** ← wiki/17 G05 | Back: синтетическое всесезонное; бензин + дизель; легковые/SUV/LCV | **B** | **Back inherit** |
| **EVID-G1D-15** | **Line inherit** | **ART-G1D-005** ← wiki/17 G06 | Back: «**УНИКАЛЬНЫЙ КОД**»; проверка **3662.ru** | **B** | **Back inherit** |
| **EVID-G1D-16** | **Line inherit** | **ART-G1D-005** ← wiki/17 G07 | Back: штамп даты; партия; **EAC**; объём **1L** (expected field; 4L photo = 4L) | **B** | **Back inherit** |
| EVID-G1D-11 | Context | ART-G1D-004 | GPN-01 site (inherit wiki/17 G11) | A | Line inherit |
| **EVID-G1D-18** | **Artifact** | **ART-G1D-006** | **«Ключевые характеристики»** GPN-01 verbatim — см. [17 §canonical](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) | **A** | **Canonical site** |
| EVID-G1D-12 | Context | ART-G1D-003 | 4L front anti-fraud teaser → back code | B | Line inherit |
| **EVID-G1D-17** | **Context** | Operator 25.06.2026 | Оборот 1L = wrap 4L; объём **1L** на штампе | B | Active |
| **EVID-G1D-19** | **Context** | Operator 25.06.2026 | **Back parity rule:** GPN-01 stack **must** be on back label (all formats) | B | **Governance** |

### Data gaps (updated rev. 2)

| Gap | Статус |
|-----|--------|
| GAP-G1D-01 Back label 1L photo | **Open** — inherit закрывает **content**; фото 1L back optional verify |
| GAP-G1D-02 Batch / штамп / EAC на 1L | **Closed (inherit B)** — EVID-G1D-16; verify photo optional |
| GAP-G1D-03 Anti-fraud 3662 на 1L | **Closed (inherit B)** — EVID-G1D-15; front teaser absent (F-G1D-08) |
| GAP-G1D-04 MB 229.5 front vs 229.3 back/site | **Open** — CR-G1D-01; **229.5 ∉ GPN-01** |
| GAP-G1D-05 Back vs GPN-01 canonical | **Open** — 6 gaps on inherit back (F-G1D-16) |

---

## Canonical site · back label requirement

> Полный текст и compliance-таблица 4L: [17_ODSA … § governance](17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md)

**Правило:** задняя этикетка **1L** = полный стек GPN-01 (объём **1 л**). **Факт (inherit B):** = back 4L template → **те же 6 gaps**, что у 4L.

| Missing on back inherit (1L) | On GPN-01 | On 1L front only |
|------------------------------|-----------|------------------|
| ACEA A3/B3 | ✅ required | ❌ |
| MB 226.5 | ✅ required | ❌ |
| BMW LL-01 | ✅ required | ✅ microtype |
| GM LL-B-025 | ✅ required | ✅ microtype |
| Porsche A40 | ✅ required | ✅ microtype |
| УМЗ | ✅ required | ❌ |
| MB **229.5** | ❌ **not in canon** | ✅ front — **contamination** |

---

## Findings Catalogue

### F-G1D-01 — Positive · Core claims coherent (front + inherited back)

| Поле | Значение |
|------|----------|
| **Observation** | API **SN/CF**, ACEA **A3/B4**, синтетика — front (G1D-01, G1D-03) + back inherit (G1D-13, G1D-14). |
| **Evidence IDs** | EVID-G1D-01; G1D-03; G1D-13; G1D-14 |
| **Severity & Confidence** | **Positive** · **High** (back **M** on inherit) |

---

### F-G1D-02 — Major · Cross-format OEM stack differs (1L front ⊃ 4L front)

| Evidence IDs | EVID-G1D-04; G1D-09; G1D-11 |
| **Severity** | **Major** · **High** (unchanged rev.1) |

---

### F-G1D-03 — Major · MB-Approval 229.5 (1L front) — **not in GPN-01 canonical**

| Поле | Значение |
|------|----------|
| **Observation** | Front **229.5** (G1D-04). GPN-01 canon: **226.5 + 229.3** only (G18). Back inherit: **229.3** (G1D-13). |
| **Evidence IDs** | EVID-G1D-04; G1D-13; **G1D-18** |
| **Severity & Confidence** | **Major** · **High** |
| **Interpretation** | **Contamination** vs site canon + split-face vs back. |

---

### F-G1D-16 — Major · Back inherit (1L) не содержит полный стек GPN-01

| Поле | Значение |
|------|----------|
| **Observation** | По правилу back parity (G19) — inherit back **не содержит** 6 позиций GPN-01 (см. § compliance). Часть OEM **только на front 1L** (BMW, GM, Porsche) — **wrong face**. |
| **Evidence IDs** | EVID-G1D-13; **G1D-18**; **G1D-19**; wiki/17 F-G11 |
| **Severity & Confidence** | **Major** · **High** (inherit B) |
| **Recommendations** | СТМ: **full GPN-01 stack on back**, readable; front — без «лишних» MB |

---

### F-G1D-04 — Major · OEM on front — listed, microtype (legibility fail)

| Evidence IDs | EVID-G1D-04; G1D-07; G1D-08 |
| **Severity** | **Major** · **High** |

---

### F-G1D-05 — ~~Major · Back n/d~~ → **Closed rev.2** · Back line inherit applied

| Поле | Значение |
|------|----------|
| **Observation** | Back content from wiki/17 (G04–G07) → G1D-13…G1D-16; operator attestation G1D-17. |
| **Evidence IDs** | EVID-G1D-13…G1D-17 |
| **Severity** | **Closed** · replaced by F-G1D-03 split-face + F-G1D-14 |

---

### F-G1D-06 — Moderate · «1L» subordinate — thumbnail fail

| Evidence IDs | EVID-G1D-02; G1D-08 |
| **Severity** | **Moderate** · **High** |

---

### F-G1D-07 — Moderate · API/ACEA footer — below thumbnail threshold

| Evidence IDs | EVID-G1D-03; G1D-07 |
| **Severity** | **Moderate** · **High** |

---

### F-G1D-08 — Moderate · Anti-fraud: back 3662 (inherit) but front teaser absent on 1L

| Evidence IDs | EVID-G1D-06; G1D-15; G1D-12 |
| **Observation** | Back inherit: 3662.ru + unique code (G15). 1L front: **no** «УНИКАЛЬНАЯ СИСТЕМА…» (G06). 4L chain: front teaser → back (G12). |
| **Severity** | **Moderate** · **Medium** |
| **Recommendations** | quick: restore front teaser on 1L or QR on front |

---

### F-G1D-09 — Moderate · Renault RN notation (front zero-padding)

| Evidence IDs | EVID-G1D-04; G1D-13 |
| **Observation** | Front RN 0700/0710; back inherit RN0700/RN0710 — **notation aligned** (CR closed). |
| **Severity** | **Moderate** · **High** |

---

### F-G1D-10 — Minor · STO 84035624-179-2015 — back inherit only

| Evidence IDs | EVID-G1D-13 |
| **Severity** | **Minor** · **Medium** (inherit B) |

---

### F-G1D-11 — Minor · Site superset vs pack — partial closure on 1L front

| Evidence IDs | EVID-G1D-04; G1D-11; G1D-13 |
| **Observation** | 1L front adds BMW/Porsche/GM vs back inherit; site still adds MB **226.5**, **УМЗ**, ACEA **A3/B3**. |
| **Severity** | **Minor** · **Medium** |

---

### F-G1D-12 — Positive · Car pictogram

| Evidence IDs | EVID-G1D-05 |
| **Severity** | Positive · **High** |

---

### F-G1D-13 — Positive · 1L front OEM wider than 4L front (limited readability)

| Evidence IDs | EVID-G1D-04; G1D-09 |
| **Severity** | Positive · **Medium** |

---

### F-G1D-14 — Positive · Anti-fraud stack — back inherit triangulated with site

| Evidence IDs | EVID-G1D-15; wiki/17 G12; G1D-11 |
| **Observation** | 3662.ru + site «100% гарантия» = line Pass (inherit B). |
| **Severity** | Positive · **Medium** |

---

### F-G1D-15 — Major · Front OEM ⊃ back OEM (within 1L SKU)

| Поле | Значение |
|------|----------|
| **Observation** | 1L front lists **BMW LL-01, Porsche A40, GM-LL-B-025**; back inherit (4L template) **не содержит** — только MB 229.3, VW, Renault, PSA, AVTOVAZ, STO. |
| **Evidence IDs** | EVID-G1D-04; G1D-13; G1D-11 |
| **Interpretation** | **Front-heavy asymmetry** — не site superset, а **intra-SKU** gap front vs back. |
| **Severity & Confidence** | **Major** · **Medium** (inherit B) |
| **Falsification** | Photo back 1L with full OEM block |

---

## Contradiction Register (rev. 2)

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-G1D-01 | MB **229.5** (1L front) ↔ **229.3** (back inherit + site) | **Open** — F-G1D-03 · split-face |
| CR-G1D-02 | 1L front OEM ⊃ 4L front OEM | **Open** — format wrap |
| CR-G1D-03 | 1L front OEM ⊃ 1L back inherit | **Open** — F-G1D-15 |
| CR-G1D-04 | PGMM «OEM dead» ↔ text present | **Closed** |
| CR-G1D-05 | Site MB 229.3 ↔ 1L front 229.5 | **Open** · **229.5 ∉ GPN-01** |
| CR-G1D-07 | Back inherit ⊂ GPN-01 canonical | **Open** — F-G1D-16; extends CR-G02 wiki/17 |
| CR-G1D-06 | RN front vs back (1L) | **Closed** — notation (G1D-04 vs G1D-13) |

---

## POV-маркировка (rev. 2)

**Information Integrity:** *Lacunae:* photo back 1L optional; *Redundancy:* Premium/Synthetic ×4; *Contamination:* **MB 229.5** front vs 229.3 back inherit; *Collonisation:* category silver+orange.

**Logical Coherence:** *Conflict:* front OEM superset vs back inherit subset; *Contradiction:* CR-G1D-01 split-face MB.

**System Dynamics:** *Anomaly:* 1L front **richer** OEM list than 4L front **and** than inherited back; *Potential:* format-specific front refresh; *Limit:* inherit B-grade until photo verify.

**Relational States:** *Parity:* core SN/CF synthetic line-wide; *Compromise:* inherit back for speed vs photo verify; *Consensus:* 3662 + site anti-fraud line.

---

## Строка для сводной матрицы (ODSA × PGMM) — rev. 2

| Параметр | Gazpromneft Premium N 5W-40 1L |
|----------|--------------------------------|
| Product line | **Premium N** |
| API (front / back) | **SN/CF · SN/CF** (back inherit B) |
| Base oil claim | **Синтетическое** (front + back inherit) |
| ACEA (front / back) | **A3/B4 · A3/B4** (+ A3/B3 site only) |
| OEM on front | **Listed, microtype** — ⊃ back inherit |
| OEM (back inherit) | MB **229.3**, VW, Renault, PSA, AVTOVAZ, STO |
| Cross-face (1L) | **Partial** — MB 229.5 vs 229.3; front OEM ⊃ back |
| Anti-fraud | **3662.ru** back inherit; front teaser **absent** |
| Маркировка РФ | **EAC + штамп** inherit B; volume **1L** expected |
| Thumbnail | Brand+5W-40 ✅ · 1L/API/OEM ❌ |
| Digital gap | Back **⊂ GPN-01** (6 gaps); front 229.5 **off canon** |

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · формат 1L · rev. 2 line-locked

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|--------------|
| 1 | M_SYSTEM (PGMM) | cognitive_amortization + institutional_anxiety | wiki/15; wiki/11 | H |
| 2 | Carrier morphology (PGMM) | Узкая бутылка + diagonal grip-ridges | EVID-G1D-01; wiki/15 | H |
| 3 | Класс продукта (синт / полусинт) | **Синтетическое** · API **SN/CF** | EVID-G1D-01; G1D-03; G1D-13 | H |
| 4 | SAE 5W-40 — legibility | **High** — hyperbolized; rel. ↑ | EVID-G1D-02; wiki/15 | H |
| 5 | API — видимость (front / back) | **SN/CF · SN/CF** (back inherit B) | EVID-G1D-03; G1D-13 | H / M |
| 6 | ACEA — видимость (front / back) | **A3/B4 · A3/B4** (+ A3/B3 site) | EVID-G1D-03; G1D-13; G1D-11 | H / M |
| 7 | OEM / допуски — front (effective) | **Listed, microtype** — ⊃ back; unreadable @shelf | EVID-G1D-04; G1D-07; F-G1D-04 | H |
| 8 | OEM / допуски — back / site / overlay | Back inherit: MB 229.3, VW, Renault, PSA, AVTOVAZ, STO · Front adds BMW/Porsche/GM · Site: +226.5, УМЗ | G1D-13; G1D-04; G1D-11; F-G1D-15 | M |
| 9 | Benefit-icons — доказуемость | **Low** — car pictogram + swirls | EVID-G1D-05; wiki/15 | M |
| 10 | Cross-face consistency | **Partial** — core Pass; **MB 229.5↔229.3**; front OEM ⊃ back | G1D-04; G1D-13; F-G1D-03; F-G1D-15 | M |
| 11 | Digital / overlay vs pack gap | Back inherit **⊂ GPN-01** (6 gaps); front 229.5 off canon; BMW/GM/Porsche front-only | G1D-13; G1D-18; G1D-19; F-G1D-16 | M |
| 12 | Anti-fraud UX | **3662.ru** back inherit + site; front teaser **absent** on 1L | G1D-15; G1D-06; F-G1D-14 | M |
| 13 | RF supply & языковая модель | **Official RF** · integrated RU | EVID-G1D-01; G1D-14 | H |
| 14 | Обязательная маркировка РФ | **EAC + штамп + партия** inherit B; **1L** on stamp (expected) | EVID-G1D-16; G1D-17 | M |
| 15 | Кириллица vs латиница | **Кириллица dominant** + PREMIUM N EN | EVID-G1D-01 | H |
| 16 | Thumbnail robustness (~120 px) | **Medium** — brand+5W-40 ✅; 1L/API/OEM fail | EVID-G1D-07; wiki/15 | H |
| 17 | Cognitive load / negative space | **High uniform** — near-zero whitespace | wiki/15 §2.2 | H |
| 18 | Legacy / rev. risk на полке | **Moderate** — MB split-face 229.5 vs 229.3; inherit until photo | F-G1D-03; CR-G1D-01 | M |

---

## Lock record

| Field | Value |
|-------|--------|
| **Decision** | **Line-locked rev.3** — GPN-01 canonical + back parity rule |
| **Upgrade path** | Photo back 1L · align back = GPN-01 · remove 229.5 |
| **Rev.** | **3 line-locked** · 25.06.2026 |

---

## Issues for discussion

1. Back 1L = **full GPN-01 stack** (project rule) — текущий inherit **fail** 6 позиций.
2. **MB 229.5** — убрать или верифицировать; **не в каноне** сайта.
3. СТМ: back = GPN-01 readable; front — viscosity + brand, не «перенос» OEM с back.

**DoD:** ODSA GPN 5W-40 1L — **rev.3 line-locked**. Canonical GPN-01 + back parity rule зафиксированы.
