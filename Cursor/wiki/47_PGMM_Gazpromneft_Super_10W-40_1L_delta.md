# PGMM Delta: Gazpromneft Super 10W-40 — 1L vs 4L

**Дата анализа:** 25.06.2026  
**Тип отчёта:** packaging_visual_metaphor_delta (не full PGMM)  
**Базовый кейс:** [46_PGMM_Gazpromneft_Super_10W-40.md](46_PGMM_Gazpromneft_Super_10W-40.md) (4L)  
**Артефакт:** Gazpromneft Super SAE 10W-40, 1L — фронт + back  
**Методология:** PGMM (Klepikov 2025) + neuromarketing-system-instructions  
**Primary domains (1–23):** D4 Packaging/Carrier · D8 Visual Semiotics · D12 Cognitive Load · D15 Shelf/Retail Context

**Контекст:** SKU вне матриц 5W-40 / 0W-20 / 5W-30 ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)); point-ref **Classic/Protect · ЮФО 10W-40**; **не смешивать** с DR-A/B.

```yaml
CASE_TYPE: packaging_visual_metaphor_delta
BRAND: Gazpromneft
LINE: Super
SAE: 10W-40
FORMAT_BASE: 4L
FORMAT_DELTA: 1L
BASE_CASE_REF: Cursor/wiki/46_PGMM_Gazpromneft_Super_10W-40.md
PRODUCTION_STAMP: 08.09.2022 · batch 2214110601 M
BARCODE: 4650063110756
STO_BACK: СТО 84035624-001-2012
```

### Artifact vs canonical

| Поле | Artifact (фото 08.09.22) | Canonical (site / operator) | Статус |
|------|--------------------------|----------------------------|--------|
| API | **SG/CD** front + back | **SG/CD** (site · GPN-03 pending) | ✅ aligned (photo) |
| Base oil | «ПОЛУСИНТЕТИЧЕСКОЕ» front | Полусинтетическое (site title) | ✅ aligned |
| OEM front | **AVTOVAZ · ZMZ** microtype | АВТОВАЗ (site); ZMZ front-only on photo | 🟡 partial |
| OEM back | **ПАО «АВТОВАЗ»** | АВТОВАЗ (site) | 🟡 ZMZ **н/д** on back |
| STO | **001-2012** back (1L) | н/д site verify | 🟡 ≠ 4L **058-2012** — batch/format drift |
| Volume | **1L** front + back | 1L SKU | ✅ aligned |

**Triangulation:** [gazpromneft-oil.ru …/gazpromneft-super-10w-40](https://gazpromneft-oil.ru/ru/products/all/gazpromneft-super-10w-40) · **GPN-03 pending**. Batch **2022** on 1L **newer** than 4L photo **2020** — facing parity не гарантирована между форматами.

---

## 0. CASE_min

| Поле | Значение |
|------|----------|
| **CASE_ID** | `COMP_GPN_SUPER_10W40_1L_DELTA` |
| **CASE_TYPE** | `packaging_visual_metaphor_delta` |
| **BASE_CASE_REF** | `Cursor/wiki/46_PGMM_Gazpromneft_Super_10W-40.md` |
| **FORMAT** | 1L (delta vs 4L) |
| **MATERIAL_ID** | `gazpromneft_super_10w40_1l_front_back_2022` |
| **SEGMENT_ID** | `label_front_primary` + `label_back_full` |

---

## 1. Наследование из базы (без дублирования)

### 1.1. M_SYSTEM — **константа**

- **MSYS_GS_01** — Universal Mass-Market Heuristic  
- **MSYS_GS_02** — Thermokinetic Swirl Lite  
- **MSYS_GS_03** — Institutional Anxiety & Authenticity  
- **MSYS_GS_04** — Domestic OEM Partial Front-Load  

См. [46 §4](46_PGMM_Gazpromneft_Super_10W-40.md). Конфликт MSYS_GS_01 ↔ MSYS_GS_02 («SUPER» + swirl vs SG legacy chemistry) **не разрешается** на 1L — сохраняется.

### 1.2. DOMAIN_A / DOMAIN_B — **константа**

- **DOMAIN_A:** thermokinetic orange flow, «SUPER» superlative, GPN corporate hegemony, domestic factory heraldry (Avtovaz/ZMZ)  
- **DOMAIN_B:** semi-synthetic 10W-40 tribology, API SG/CD legacy chemistry, universal PVL service  

См. [46 §5](46_PGMM_Gazpromneft_Super_10W-40.md).

### 1.3. M_CONSTRUCTION — variant-by-format

| ID (база) | Статус на 1L |
|-----------|--------------|
| MCON_GS_01 Universal Mass Heuristic | ✅ SUPER + semi line + car icon **robust** |
| MCON_GS_02 SUPER Hyperbole Lockup | ✅ «SUPER» black bold **dominant**; vertical tower ↑ |
| MCON_GS_03 SAE+API Front Telemetry | ✅ **10W-40 + API SG/CD front сохранены** — budget-tier strength |
| MCON_GS_04 Thermokinetic Swirl Lite | 🟡 orange/yellow/blue swirl **lateral crop** на узкой этикетке |
| MCON_GS_05 Semi-Synthetic Literal Claim | ✅ «ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО» **константа** |
| MCON_GS_06 Domestic OEM Partial Front-Load | ✅ **AVTOVAZ · ZMZ microtype front сохранён** — **↑ vs LUKOIL SUPER 1L** (OEM back-only) |
| MCON_GS_07 Authenticity Back-Load | 🟡 scratch «Уникальный код» **н/д** on 1L photo; EAC + barcode **константа** |
| MCON_GS_08 GPN Budget Family Continuity | ✅ silver HDPE + swirl + grip-ridges **константа** семейства |
| MCON_GS_09 Solid-over-Fluid Suppression | ✅ лакуна fluid-визуала **константа** |
| MCON_GS_10 Legacy API Honesty | ✅ API SG/CD **без маскировки** front — **robust** |
| MCON_GS_11 Oil-Level Utility Strip | 🔻 translucent strip **н/д** on 1L photo (present on 4L) |

**POV — Relational States:** parity метафорической системы между форматами; **compromise** — DRY-rescale 4L asset vs service-jug authority; **parity** с GPN Premium N/C3 1L morphology ([15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md), [33](33_PGMM_Gazpromneft_Premium_C3_5W-30_1L_delta.md)).

---

## 2. Delta по блокам

### 2.1. C — Носитель (Carrier)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Геометрия** | Широкий 4L-jug, integrated side handle | Узкая вертикальная бутылка; concave левая «плечевая» грань под захват | **Смена морфологии:** service jug → top-up bottle |
| **Ручка** | Интегрированная боковая ручка 4L | **Нет отдельной ручки**; concave grip-zone + **3 диагональные ridges** на плече и у основания (GPN 1L pattern) | **Новый affordance:** doliv / одноручный захват |
| **Material** | Silver-grey metallic HDPE + embossed G logo | Идентично; embossed G **н/д** on front photo angle | Константа |
| **Пропорции H:W** | Низкий, широкое основание, низкий CG | Высокий «towering» силуэт, узкая база | **DoF:** сжатие по ширине, растяжение по высоте |
| **Cap** | Silver screw cap + vertical grip ridges | Silver cap + vertical grip ridges (пропорционально меньше) | Константа семантики |
| **Fill gauge** | Translucent oil-level strip (4L) | **н/д** on 1L photo | 🔻 **format utility cue lost** |
| **Стабильность** | Широкая база 4L | Узкая база, **↑ CG** | **Limit:** риск опрокидывания на doliv-полке |

**Вывод (C):** 1L — **не downscale 4L-jug**, а **перекодировка carrier-code** по шаблону GPN family 1L: silver HDPE + diagonal grip-ridges + narrow tower ([15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md)). **Institutional service-jug authority** 4L **ослаблена**; **потеря** oil-level strip — regression vs 4L utility affordance.

---

### 2.2. K — Композиция (Layout)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Стратегия макета** | Vertical stack: logo → SUPER → semi → swirl → 10W-40/API → OEM microtype → 4L | **Vertical rescale** 4L-макета на узкую этикетку | **K_PATTERN_VERTICAL_RESCALE** |
| **Negative space** | Silver HDPE field (MOCC_GS_NS01); orange band isolating 10W-40 (NS02) | NS01 **сжат**; NS02 **partial compress** | **↓ breathing room** |
| **Иерархия** | Brand → SUPER → semi → swirl → specs → OEM → 4L | Идентичная последовательность | Константа порядка |
| **Читаемость 10W-40** | Prominent white on orange band | Сохранена; **относительный размер ↑** к ширине | **Усилена** |
| **Читаемость объёма** | «4L» — full service cycle | «1L» — top-up; **мельче** vs 10W-40 band | **Semantic shift + ↓ legibility** |
| **OEM microtype front** | AVTOVAZ · ZMZ footer | **Константа** (сохранён под orange band) | ✅ **robust vs peer LUKOIL** |
| **Back density** | High (legal + STO/AAI + multilingual + scratch code) | Тот же asset class на **меньшем** носителе; scratch zone **н/д** | **↑ proportional load**; authenticity layer **↓** |

**POV — Information Integrity:**  
- *Redundancy:* SUPER + semi-synthetic + car icon + swirl + 10W-40 — **без ослабления** при сжатии.  
- *Contamination:* swirl-lite thermokinetics **константа**.  
- *Lacuna:* silver breathing room (NS01) **частично схлопнут**; scratch-code back **н/д** on 1L photo.

**Вывод (K):** GPN **не пересобирает** SUPER layout на 1L — **DRY vertical rescale** (industry + GPN family norm). Primary scan path (SUPER → 10W-40 → API SG/CD) **robust**. Secondary: OEM microtype **survives** (delta **+** vs LUKOIL SUPER 1L); authenticity scratch **under-delivered** on 1L photo vs 4L.

---

### 2.3. S — Сигнальные паттерны

| Статус | Паттерн | Комментарий |
|--------|---------|-------------|
| ✅ **Сохранён** | Blue flame G + GAZPROMNEFT wordmark (MOCC_GS_01) | Межформатный invariant |
| ✅ **Сохранён** | «SUPER» large bold black (MOCC_GS_02) | Budget hyperbole **dominant** |
| ✅ **Сохранён** | «10W-40» white on orange band (MOCC_GS_04) | Primary SAE heuristic |
| ✅ **Сохранён** | «API SG/CD» front (MOCC_GS_05) | **Front standards lockup survives** |
| ✅ **Сохранён** | «ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО» (MOCC_GS_03) | Semi-synthetic literal **константа** |
| ✅ **Сохранён** | AVTOVAZ · ZMZ front microtype (MOCC_GS_08) | **Domestic OEM partial front-load robust on 1L** |
| ✅ **Сохранён** | Small white car silhouette (MOCC_GS_07) | PVL universal icon |
| 🟡 **Усилен** | Vertical SUPER + swirl monolith stack | «Башня» budget tier на узком носителе |
| 🔻 **Деградировал** | Orange swirl gestalt (MOCC_GS_06) | Lateral crop |
| 🔻 **Деградировал** | Translucent oil-level strip (MOCC_GS_12) | **Absent** on 1L photo |
| 🔻 **Деградировал** | Scratch «Уникальный код» back (MOCC_GS_17) | **н/д** on 1L photo |
| ➕ **Новый** | Diagonal grip-ridges on C (тактильный S) | Top-up pour control — GPN 1L family |
| ➕ **Новый** | Barcode 4650063110756 | SKU routing 1L (≠ 4L 4650063110749) |
| ➕ **Новый** | STO **001-2012** back | ≠ 4L **058-2012** — cross-format STO drift |

**Вывод (S):** Budget primary signals (SUPER + 10W-40 + API SG/CD + semi-synthetic) **survive** downscale. **Differentiator vs LUKOIL SUPER 1L:** OEM microtype **on front** — partial delivery **↑**. Secondary losses: swirl gestalt, oil-level strip, scratch authenticity on 1L photo.

---

### 2.4. M — Среда (Medium / контекст потребления)

| Контекст | 4L | 1L | Δ |
|----------|----|----|---|
| **Retail-полка** | Основная / service shelf | **Top-up / companion**; doliv, аксессуары, СТО-касса | **Смена M_CONTEXT** |
| **Плотность выкладки** | ~4–6 facings (широкие jugs) | **~10–14 facings** (узкий профиль) | **↑ linear density** |
| **Дистанция считывания** | 1,2–2,5 m | 0,5–1,2 m (рука потребителя) | **Ближний контакт** |
| **E-commerce thumbnail** | SUPER + 10W-40 + GPN ✅ | SUPER + 10W-40 + GPN ✅; OEM microtype **🟡** @120 px; 1L **✗** | **Robustness ≈ 4L** primary layer |
| **10W-40 legacy context** | ЮФО / aging fleet service | Тот же buyer; **меньше** service-jug reassurance | **Trust gap ↑** on doliv |
| **RU localization** | Full Cyrillic front + back + EAC | **Константа** | = |
| **M_NOISE** | Medium (swirl + SUPER redundancy) | Redundancy **↑** при сжатии; back wall **↑** load/bottle area | **Internal noise ↑** |

**POV — System Dynamics:**  
- *Potential:* 1L + **OEM front microtype** = **stronger domestic heuristic @ thumbnail** than LUKOIL SUPER 1L on doliv-канале.  
- *Limit:* No top-up rationale; scratch authenticity **↓** on 1L photo; service-jug authority **lost**.  
- *Anomaly:* Front API SG/CD + OEM microtype **both delivered** on 1L — **above import norm**, **above LUKOIL SUPER 1L** on OEM front.

**Вывод (M):** 1L в **doliv-нише**; GPN **не адаптирует** claim-layer под top-up (нет «doliv-safe» / «exact 1L fill»). **OEM partial front** — **конкурентное преимущество** vs LUKOIL back-only на impulse channel.

---

### 2.5. MAP — Мэппинги

| MAP (база 4L) | 1L | Статус |
|---------------|-----|--------|
| Swirl-lite → thermokinetic tribology (MCON_GS_04) | Swirl cropped | 🟡 **span ↓** |
| «SUPER» superlative → budget protection (MCON_GS_02) | Константа | ✅ **robust** |
| Semi-synthetic literal → chemistry honesty (MCON_GS_05) | Константа | ✅ |
| API SG/CD front → spec gate (MCON_GS_03) | Константа | ✅ **robust** |
| 4L → full service cycle | **1L → top-up module** | 🔄 **перекодировка объёма** |
| OEM microtype front → domestic park (MCON_GS_06) | **Константа** | ✅ **↑ vs LUKOIL 1L** |
| Scratch code → anti-fraud (MCON_GS_07) | **н/д** on 1L photo | 🔻 **MAP under-delivered** |
| Oil-level strip → pour control (MCON_GS_11) | **Lost** on 1L | 🔻 |
| Service jug → authority | **Lost** on 1L | 🔻 carrier MAP ↓ |
| Grip-ridges → controlled pour | **Новый MAP** (tactile) | ➕ LATENT |
| STO back → domestic standards | **001-2012** (≠ 058-2012 on 4L) | 🟡 **cross-format drift** |

**POV — Logical Coherence:**  
- *Conflict:* «SUPER» hyperbole + top-up 1L — service rhetoric **не артикулирована** (shared with LUKOIL).  
- *Contradiction:* Swirl thermokinetics vs semi-synthetic chemistry — **константа**; не усиливается на 1L.

**Вывод (MAP):** Ядро Universal Mass Heuristic + Swirl Lite **масштабируется**. Искажаются: swirl gestalt, service-jug authority, volume semantics, oil-level + scratch MAP. **Уникальный delta:** OEM front microtype **не ломается** на 1L — **reinforced** vs peer.

---

### 2.6. EVAL — Оценка малого формата

| Метрика | 4L (база) | 1L (delta) | Δ |
|---------|-----------|------------|---|
| **Comprehensibility** | High (SUPER + 10W-40 + API front) | **High** SUPER + 10W-40 + API SG/CD; OEM microtype **medium** @ close range | ↓ slight @ 2m on OEM |
| **Cognitive load** | Medium (front) / high (back) | **Bimodal:** front clean / **back peak** on small bottle | **↑ back variance** |
| **Robustness (thumbnail)** | High | **High-medium:** SUPER + 10W-40 + GPN ✅; OEM **🟡** | ≈ 4L primary |
| **Premium perception** | Low (budget tier) | **Low** — swirl crop, no jug | ↓ carrier; **= tier** |
| **RU localization** | High (Cyrillic + domestic OEM) | **High** — OEM front **↑** vs LUKOIL | **↑ vs peer** |
| **Transaction speed (budget buyer)** | High | **High** @ close range; OEM microtype **bonus** @ thumbnail | context-dependent |
| **Trust / institutional** | Medium-high (scratch + STO back) | **Medium** — scratch **↓** on photo; EAC + barcode **константа** | ↓ slight |

**POV — Relational States:** parity M_SYSTEM при **loss of service carrier + oil-level strip**; **compromise** DRY asset vs doliv channel; **anomaly** — OEM front partial load **survives** where LUKOIL fails.

**Вывод (EVAL):** 1L **не ломает** primary 10W-40 / semi-synthetic value proposition. Ломается **service-jug authority**, **oil-level utility**, **scratch authenticity layer** (on photo). **Win vs LUKOIL SUPER 1L:** OEM front microtype + front API stack **both robust**.

---

## 3. M_OCCURRENCE — только новые и изменённые

> Occurrences базы (MOCC_GS_01–19, L01–L07, LAC01–LAC08, NS01–NS04) без изменений **не дублируются**.

### 3.1. MOCC_GSD_01 — Volume 1L (variant MOCC_GS_09)

**_min**
```yaml
M_OCC_ID: MOCC_GSD_01
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: label_core_orange_band
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "orange_band_footer" }
M_OCC_SURFACE_FORM: "1L"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_GS_09 (4L → 1L)
```

**_full:** MAP `4L_service_cycle → 1L_topup_module`; M_CONSTR: MCON_GS_03 variant-by-format.

---

### 3.2. MOCC_GSD_02 — Diagonal grip-ridges without integrated handle

**_min**
```yaml
M_OCC_ID: MOCC_GSD_02
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: carrier_body_left_shoulder
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "shoulder_and_base", pattern: "diagonal_ridges_x3" }
M_OCC_SURFACE_FORM: "3 diagonal grip ridges top + 3 bottom; concave grip zone; no integrated handle"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_ergonomics` → TARGET `dom_controlled_pour`; GPN 1L family pattern ([15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md)); contrast vs 4L integrated handle ([46 §7 C2](46_PGMM_Gazpromneft_Super_10W-40.md)).

---

### 3.3. MOCC_GSD_03 — Narrow top-up bottle morphology

**_min**
```yaml
M_OCC_ID: MOCC_GSD_03
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: carrier_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_bottle_silhouette" }
M_OCC_SURFACE_FORM: "Tall narrow bottle; concave left grip; high CG vs 4L jug"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** **Carrier-code shift** service jug → portable module; FUNCTION [`format_signal`, `channel_topup`].

---

### 3.4. MOCC_GSD_04 — Truncated swirl-lite (delta MOCC_GS_06)

**_min**
```yaml
M_OCC_ID: MOCC_GSD_04
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: label_core
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "swirl_zone_lateral_crop" }
M_OCC_SURFACE_FORM: "Orange/yellow/blue angular flow shapes cropped at label lateral edges"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: MOCC_GS_06 (degraded)
```

**_full:** MCON_GS_04 span ↓; MSYS_GS_02 **partial delivery** on thumbnail.

---

### 3.5. MOCC_GSD_05 — Vertical label rescale pattern

**_min**
```yaml
M_OCC_ID: MOCC_GSD_05
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", axis: "vertical" }
M_OCC_SURFACE_FORM: "4L front layout vertically rescaled to narrow 1L label"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
```

**_full:** DRY brand asset; FUNCTION [`format_adaptation`]; inherits GPN family norm + LUKOIL SUPER DRY pattern ([43](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md)).

---

### 3.6. MOCC_GSD_06 — Barcode 1L SKU routing

**_min**
```yaml
M_OCC_ID: MOCC_GSD_06
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: label_back_footer
M_OCC_MODALITY_CLASS: visual_text
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "barcode", code: "4650063110756" }
M_OCC_SURFACE_FORM: "EAN-13 4650063110756 (1L); ≠ 4L 4650063110749"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_GS_16 (format variant)
```

**_full:** Retail routing; chemistry aligned across formats (API SG/CD).

---

### 3.7. MOCC_GSD_07 — STO cross-format drift (001 vs 058)

**_min**
```yaml
M_OCC_ID: MOCC_GSD_07
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: label_back_header
M_OCC_MODALITY_CLASS: visual_text
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "sto_line" }
M_OCC_SURFACE_FORM: "СТО 84035624-001-2012 (1L) vs 058-2012 (4L photo)"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: MANIFEST
BASE_REF: MOCC_GS_14 (variant)
```

**_full:** **Cross-format artifact drift** — verify GPN-03 / operator whether format-linked or batch-linked; **не** spec chemistry drift.

---

### 3.8. MOCC_GSD_LAC01 — Oil-level strip absent on 1L

**_min**
```yaml
M_OCC_ID: MOCC_GSD_LAC01
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: carrier_body
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: absence_of_effect
M_OCC_SPAN: { region: "translucent_strip", context: "4L_had_fill_gauge" }
M_OCC_SURFACE_FORM: "No visible oil-level strip on 1L photo (present on 4L)"
M_OCC_STATUS_CLASS: inferred
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: LACUNA
BASE_REF: MOCC_GS_12 (lost)
```

**_full:** **Regression** on doliv format where pour-control cue **most relevant**; contrast [33](33_PGMM_Gazpromneft_Premium_C3_5W-30_1L_delta.md) where 1L **gains** fill strip.

---

### 3.9. MOCC_GSD_LAC02 — Scratch authenticity zone н/д on 1L photo

**_min**
```yaml
M_OCC_ID: MOCC_GSD_LAC02
CASE_ID: COMP_GPN_SUPER_10W40_1L_DELTA
MATERIAL_ID: gazpromneft_super_10w40_1l_front_back_2022
SEGMENT_ID: label_back_footer
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: absence_of_effect
M_OCC_SPAN: { region: "scratch_code_zone", context: "4L_had_unique_code" }
M_OCC_SURFACE_FORM: "Уникальный код scratch zone not visible on 1L back photo"
M_OCC_STATUS_CLASS: inferred
M_OCC_CONFIDENCE_LEVEL: low
STATUS_TAG: LACUNA
BASE_REF: MOCC_GS_17 (under-delivered)
```

**_full:** MSYS_GS_03 **partial failure** on 1L photo; verify current facing — may be crop/angle lacuna vs format omission.

---

## 4. Выводы для СТМ

### 4.1. Где дизайн GPN Super «ломается» на 1L

1. **Service-jug authority** — 4L handle + wide base **→** narrow top-up bottle; institutional mass-retail code **ослаблен**.
2. **Swirl gestalt (MCON_GS_04)** — angular flow **усечён**; Thermokinetic Swirl Lite **partial** @ thumbnail.
3. **Oil-level strip (MCON_GS_11)** — **потерян** on 1L vs present on 4L — **regression** for doliv channel.
4. **Scratch authenticity (MCON_GS_07)** — **under-delivered** on 1L photo vs 4L back stack.
5. **SUPER + swirl redundancy** — без ослабления при сжатии → cognitive noise **↑**.
6. **Back wall density** — legal+STO asset на **меньшем** носителе → proportional load **↑**.
7. **No top-up rationale** — нет «doliv-safe» / «exact 1L fill» messaging.

### 4.2. Лакуны базового формата: усиление / ослабление

| Лакуна (база 4L) | На 1L |
|------------------|-------|
| MOCC_GS_LAC01 (fluid visualization) | **Константа** |
| MOCC_GS_LAC02 (OEM readable @1.2 m) | **Частично ослаблена** — microtype survives but **↓** @ 2m |
| MOCC_GS_LAC03 (ACEA / modern API) | **Константа** |
| MOCC_GS_LAC04 (proprietary additive) | **Константа** |
| MOCC_GS_LAC05 (HTHS / drain km) | **Константа** |
| MOCC_GS_LAC06 (eco / DPF) | **Константа** |
| MOCC_GS_LAC07 (explicit universal banner) | **Константа** — semi line only |
| MOCC_GS_LAC08 (UMZ on photo) | **Константа** — ZMZ front-only; UMZ **н/д** |

### 4.3. Импликации для point-ref Classic/Protect / СТМ

- **Раздельные строки 4L и 1L** для GPN Super (правило: 1 format = 1 row).
- **Format Robustness @120 px:** GPN ✅ · SUPER ✅ · 10W-40 ✅ · API SG/CD ✅ · OEM microtype 🟡 · swirl 🟡 · 1L ✗.
- **Top-up Shelf Fit:** grip-ridges + narrow profile ✅; OEM front microtype ✅ (**↑ vs LUKOIL**); oil-level strip ✗; top-up claim ✗; semi-synthetic honesty ✅.
- **Attack vector СТМ 1L (Classic/Protect · 10W-40):** **не** копировать SUPER hyperbole + swirl void; **перенять** readable SAE+API front + **readable domestic OEM band (2–3 front, not microtype)** + semi-synthetic honesty + **oil-level / pour-control cue on 1L** + top-up semantic («точный долив 1L»).
- **Cross-ref peer:** GPN Super 1L **↑ OEM front** vs [43](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md) LUKOIL; **↓** oil-level utility vs GPN 4L and GPN Premium C3 1L.

**POV — System Dynamics:** GPN Super на 1L **сохраняет** front API + **partial OEM front** — **лучше LUKOIL SUPER 1L** на domestic heuristic @ doliv. Окно СТМ — **readable OEM band + fill gauge + top-up semantics + fluid antidote**, **не** копирование SUPER + swirl stack.

---

## 5. POV-сводка (обязательная маркировка)

| Маркер | Фиксация |
|--------|----------|
| **Information Integrity** | Lacuna: oil-level strip lost; scratch code н/д; Redundancy: SUPER+swirl+semi **константа**; Contamination: swirl thermokinetics **константа** |
| **Logical Coherence** | Conflict: SUPER service rhetoric vs 1L top-up **не артикулирован**; swirl vs SG chemistry **константа** |
| **System Dynamics** | Potential: OEM front microtype @ doliv thumbnail; Limit: service-jug + fill gauge lost; Anomaly: **OEM front survives** vs LUKOIL back-only |
| **Relational States** | Parity: M_SYSTEM; Compromise: DRY asset vs doliv utility gaps; **Delta vs peer:** GPN **↑ OEM front**, LUKOIL **↑ universal banner + ActiPure** |

---

## 6. Таблица «4L vs 1L» — для матрицы конкурентов

| # | Параметр | 4L (база) | 1L (delta) | Δ для матрицы |
|---|----------|-----------|------------|---------------|
| 1 | M_SYSTEM | Universal + Swirl Lite + Authenticity + OEM partial front | **константа** | = |
| 2 | Carrier morphology | 4L jug + handle + oil-level strip | Narrow bottle + grip-ridges; **no strip** | **разные строки** |
| 3 | Label strategy | Vertical budget stack | Vertical rescale 4L asset | compress |
| 4 | SUPER hyperbole | Dominant front | **константа** | = |
| 5 | 10W-40 legibility | High (orange band) | High (rel. ↑) | = / ↑ |
| 6 | API SG/CD front | Readable | **константа** | = |
| 7 | Semi-synthetic claim | Explicit front | **константа** | = |
| 8 | OEM front | AVTOVAZ · ZMZ microtype | **константа** | = (**↑ vs LUKOIL 1L**) |
| 9 | Volume marker | 4L service cycle | 1L top-up | **semantic shift** |
| 10 | Swirl-lite gestalt | Full angular flow | Lateral crop | ↓ |
| 11 | Oil-level strip | Present (4L) | **Absent** (1L photo) | ↓ |
| 12 | Scratch authenticity | Back unique code (4L) | **н/д** (1L photo) | ↓ |
| 13 | STO back | 058-2012 | **001-2012** | 🟡 drift |
| 14 | Batch facing | 2020 | **2022** | newer 1L photo |
| 15 | Retail context | Main / service shelf | Top-up / companion | **context split** |
| 16 | Thumbnail robustness | High | High-medium | ↓ slight |
| 17 | STM 1L attack | — | Readable OEM band + fill gauge + top-up claim + fluid antidote | **opportunity** |

---

## 7. Issues for discussion

1. **10W-40 matrix branch:** включать ли GPN Super 1L/4L как две строки в Classic/Protect ветке (пара с LUKOIL SUPER)?
2. **OEM front microtype @1.2 m:** GPN partial front-load on 1L — достаточен ли для ЮФО vs СТМ readable OEM band?
3. **Oil-level strip regression:** сознательное упрощение budget 1L или facing drift — verify vs Premium C3 1L (strip present)?
4. **STO 001 vs 058:** format-linked или batch-linked — закрыть при GPN-03 triangulation.
5. **Scratch code on 1L:** crop lacuna или format omission — verify current retail facing.
6. ~~**Next pass:** `stm-odsa` (4L+1L)~~ → [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) · [49](49_ODSA_Gazpromneft_Super_10W-40_1L.md) ✅ · cross-ref [43](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md) peer delta.

---

## 8. Связи

- База full: [46_PGMM_Gazpromneft_Super_10W-40.md](46_PGMM_Gazpromneft_Super_10W-40.md)
- Peer budget 10W-40 delta: [43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md)
- GPN family 1L deltas: [15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md) · [33](33_PGMM_Gazpromneft_Premium_C3_5W-30_1L_delta.md)
- GPN family full: [11](11_PGMM_Gazpromneft_Premium_N_5W-40.md) · [32](32_PGMM_Gazpromneft_Premium_C3_5W-30.md)
- SAE / Classic line: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md) · [05_линейка_SKU_СТМ.md](05_линейка_SKU_СТМ.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)

---

*Delta-отчёт · CASE `COMP_GPN_SUPER_10W40_1L_DELTA` · ingest 25.06.2026 · skill stm-pgmm-delta*
