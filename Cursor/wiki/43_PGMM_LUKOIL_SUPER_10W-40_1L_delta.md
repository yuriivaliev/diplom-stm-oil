# PGMM Delta: LUKOIL SUPER 10W-40 — 1L vs 4L

**Дата анализа:** 25.06.2026  
**Тип отчёта:** packaging_visual_metaphor_delta (не full PGMM)  
**Базовый кейс:** [42_PGMM_LUKOIL_SUPER_10W-40.md](42_PGMM_LUKOIL_SUPER_10W-40.md) (4L)  
**Артефакт:** LUKOIL SUPER SAE 10W-40, 1L — фронт + back  
**Методология:** PGMM (Klepikov 2025) + neuromarketing-system-instructions  
**Primary domains (1–23):** D4 Packaging/Carrier · D8 Visual Semiotics · D12 Cognitive Load · D15 Shelf/Retail Context

**Контекст:** SKU вне матриц 5W-40 / 0W-20 / 5W-30 ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)); point-ref **Classic/Protect · ЮФО 10W-40**; **не смешивать** с DR-A/B.

```yaml
CASE_TYPE: packaging_visual_metaphor_delta
BRAND: LUKOIL
LINE: SUPER
SAE: 10W-40
FORMAT_BASE: 4L
FORMAT_DELTA: 1L
BASE_CASE_REF: Cursor/wiki/42_PGMM_LUKOIL_SUPER_10W-40.md
PRODUCTION_STAMP: 07.08.22 · batch 2403 1 (B) · 22 06808014
BARCODE: 4607161615366
```

### Artifact vs canonical

| Поле | Artifact (фото 07.08.22) | Canonical (матрица / site) | Статус |
|------|--------------------------|----------------------------|--------|
| API | **SG/CD** front + back | **SG/CD** (LLK-03) | ✅ aligned |
| Base oil | «ПОЛУСИНТЕТИЧЕСКОЕ» front | Полусинтетическое (site) | ✅ aligned |
| OEM | АВТОВАЗ · УМЗ · ЗМЗ back | АВТОВАЗ · УМЗ · ЗМЗ | ✅ aligned |
| Volume | **1L** front + back | 1L SKU | ✅ aligned |

**Triangulation:** [lukoil-masla.ru …/lukoil-super-10w-40](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-super-10w-40) · **LLK-03**.

---

## 0. CASE_min

| Поле | Значение |
|------|----------|
| **CASE_ID** | `COMP_LUKOIL_SUPER_10W40_1L_DELTA` |
| **CASE_TYPE** | `packaging_visual_metaphor_delta` |
| **BASE_CASE_REF** | `Cursor/wiki/42_PGMM_LUKOIL_SUPER_10W-40.md` |
| **FORMAT** | 1L (delta vs 4L) |
| **MATERIAL_ID** | `lukoil_super_10w40_1l_front_back_2022` |
| **SEGMENT_ID** | `label_front_primary` + `label_back_full` |

---

## 1. Наследование из базы (без дублирования)

### 1.1. M_SYSTEM — **константа**

- **MSYS_LS_01** — Universal Mass-Market Heuristic  
- **MSYS_LS_02** — Honeycomb Armor Lite  
- **MSYS_LS_03** — ActiPure Epistemic Black Box  
- **MSYS_LS_04** — Domestic OEM Sovereignty  

См. [42 §4](42_PGMM_LUKOIL_SUPER_10W-40.md). Конфликт MSYS_LS_01 ↔ MSYS_LS_03 (universal/SUPER hyperbole vs SG legacy chemistry) **не разрешается** на 1L — сохраняется.

### 1.2. DOMAIN_A / DOMAIN_B — **константа**

- **DOMAIN_A:** honeycomb filter lattice, car-icon mobility, «SUPER» superlative, domestic factory heraldry  
- **DOMAIN_B:** semi-synthetic 10W-40 tribology, API SG/CD legacy chemistry, Avtovaz-era engine protection  

См. [42 §5](42_PGMM_LUKOIL_SUPER_10W-40.md).

### 1.3. M_CONSTRUCTION — variant-by-format

| ID (база) | Статус на 1L |
|-----------|--------------|
| MCON_LS_01 Universal Mass Heuristic | ✅ «УНИВЕРСАЛЬНОЕ МАСЛО» + car icon **robust** |
| MCON_LS_02 SUPER Hyperbole Lockup | ✅ «SUPER» white italic **dominant**; vertical «tower» ↑ |
| MCON_LS_03 SAE+API Front Telemetry | ✅ **10W-40 + API SG/CD front сохранены** — budget-tier strength |
| MCON_LS_04 Honeycomb Armor Lite | 🟡 red mesh bands **lateral crop** на узкой этикетке |
| MCON_LS_05 ActiPure Epistemic Seal | 🟡 «ActiPure» + «ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ» **↓** micro-text |
| MCON_LS_06 Semi-Synthetic Literal Claim | ✅ «ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО» **константа** |
| MCON_LS_07 Domestic OEM Back-Load | 🟡 OEM grid **константа** по составу; **↑ proportional back density** |
| MCON_LS_08 Lukoil Budget Family Continuity | ✅ silver-grey HDPE + red cap + mesh **константа** |
| MCON_LS_09 Solid-over-Fluid Suppression | ✅ лакуна fluid-визуала **константа** |
| MCON_LS_10 Legacy API Honesty | ✅ API SG/CD **без маскировки** front — **robust** vs LUXE SL→SN drift |

**POV — Relational States:** parity метафорической системы между форматами; **compromise** — service-jug authority (4L) **жертвуется** без пересборки claim-layer под top-up; **parity** с Lukoil DRY-rescale family ([31](31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md), [14](14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md)).

---

## 2. Delta по блокам

### 2.1. C — Носитель (Carrier)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Геометрия** | Широкий 4L-jug, integrated side handle | Узкая вертикальная бутылка; concave правая «плечевая» грань | **Смена морфологии:** service jug → top-up bottle |
| **Ручка** | Интегрированная боковая ручка 4L | **Нет ручки**; круглые dimple-grip на правой грани + горизонтальные рidges слева | **Новый affordance:** doliv / одноручный захват |
| **Material** | Silver-grey metallic HDPE | Идентично (back фото **темнее** — освещение / угол) | Константа |
| **Пропорции H:W** | Низкий, широкое основание, низкий CG | Высокий «towering» силуэт, узкая база | **DoF:** сжатие по ширине, растяжение по высоте |
| **Cap** | Red screw cap + vertical grip ridges | Red cap + vertical grip ridges (пропорционально меньше) | Константа семантики |
| **Стабильность** | Широкая база 4L | Узкая база, **↑ CG** | **Limit:** риск опрокидывания на doliv-полке |

**Вывод (C):** 1L — не downscale 4L-jug, а **перекодировка carrier-code**: с «service container universal semi» на «portable top-up module». Lukoil budget-family morphology (silver HDPE + red cap + mesh label) **сохранена**, но **institutional mass-retail authority** 4L-jug **ослаблена** — аналог Genesis/LUXE 1L pattern.

---

### 2.2. K — Композиция (Layout)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Стратегия макета** | Vertical stack: logo → universal → SUPER → specs → ActiPure → 4L | **Vertical rescale** 4L-макета на узкую этикетку | **K_PATTERN_VERTICAL_RESCALE** |
| **Negative space** | Black field за «SUPER» (MOCC_LS_NS01); red mesh stratification (NS02) | Black core **сжат**; mesh bands **уже** | NS01/NS02 **partial compress** |
| **Иерархия** | Brand → universal → SUPER → semi → specs → ActiPure → 4L | Идентичная последовательность | Константа порядка |
| **Читаемость 10W-40** | Prominent white on black | Сохранена; **относительный размер ↑** к ширине | **Усилена** |
| **Читаемость объёма** | «4L» — full service cycle | «1L» — top-up / partial fill | **Semantic shift** |
| **ActiPure footer** | Readable close-range | Present; **↓** к close-read threshold @ shelf 2m | 🟡 |
| **Back density** | Very high (legal + OEM + multilingual) | Тот же asset на **меньшем** носителе | **↑ proportional cognitive load** |

**POV — Information Integrity:**  
- *Redundancy:* universal + car icon + SUPER + semi-synthetic — **без ослабления** при сжатии.  
- *Contamination:* honeycomb = tech + armor + filter — **константа**.  
- *Lacuna:* black breathing room (NS01) **частично схлопнут**.

**Вывод (K):** Lukoil **не пересобирает** SUPER layout на 1L, а **масштабирует** 4L asset (industry DRY). Главная потеря — **mesh gestalt completeness** и ActiPure legibility @ distance. Primary scan path (SUPER → 10W-40 → API SG/CD) **robust** — **сильнее**, чем у import tier-1 1L без front API ([20](20_PGMM_mobil_1_0w_20_1L_delta.md)).

---

### 2.3. S — Сигнальные паттерны

| Статус | Паттерн | Комментарий |
|--------|---------|-------------|
| ✅ **Сохранён** | LUKOIL red square + wordmark (MOCC_LS_01) | Межформатный invariant |
| ✅ **Сохранён** | «УНИВЕРСАЛЬНОЕ МАСЛО» + car icon (MOCC_LS_02–03) | Universal gate **robust** @ thumbnail |
| ✅ **Сохранён** | «SUPER» large white italic (MOCC_LS_04) | Budget hyperbole **dominant** |
| ✅ **Сохранён** | «10W-40» prominent (MOCC_LS_06) | Primary SAE heuristic |
| ✅ **Сохранён** | «API SG/CD» front (MOCC_LS_07) | **Front standards lockup survives** — budget honesty |
| ✅ **Сохранён** | «ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО» (MOCC_LS_05) | Semi-synthetic literal **константа** |
| 🟡 **Усилен** | Vertical SUPER + mesh monolith stack | «Башня» budget tier на узком носителе |
| 🔻 **Деградировал** | Honeycomb mesh gestalt (MOCC_LS_08) | Lateral crop |
| 🔻 **Деградировал** | ActiPure® micro-line (MOCC_LS_09) | Below close-read threshold @ 2m |
| 🔻 **Деградировал** | Red mesh stratification bands (MOCC_LS_NS02) | Compressed |
| ➕ **Новый** | Circular dimple grip (тактильный S на C) | Top-up pour control |
| ➕ **Новый** | Barcode 4607161615366 | SKU routing 1L (≠ 4L 4607161615393) |
| ➕ **Новый** | Horizontal grip ridges left face | Secondary tactile affordance |

**Вывод (S):** Budget primary signals (SUPER + 10W-40 + API SG/CD front + universal) **survive** downscale **лучше import 1L norm**. Secondary layer (ActiPure, full mesh gestalt) **фильтруется** на дистанции. Domestic OEM grid **физически полон** на back, но **не на фронте** — paradox сохраняется и **усиливается** на doliv-канале.

---

### 2.4. M — Среда (Medium / контекст потребления)

| Контекст | 4L | 1L | Δ |
|----------|----|----|---|
| **Retail-полка** | Основная / service shelf; universal semi full change | **Top-up / companion**; doliv, аксессуары, СТО-касса | **Смена M_CONTEXT** |
| **Плотность выкладки** | ~4–6 facings (широкие jugs) | **~10–14 facings** (узкий профиль) | **↑ linear density** |
| **Дистанция считывания** | 1,2–2,5 m | 0,5–1,2 m (рука потребителя) | **Ближний контакт** |
| **E-commerce thumbnail** | SUPER + 10W-40 + LUKOIL ✅ | SUPER + 10W-40 + LUKOIL ✅; ActiPure / 1L **✗** @120 px | **Robustness ↑** vs Mobil 1L (no front API) |
| **10W-40 legacy context** | ЮФО / aging fleet service | Тот же buyer; **меньше** service-jug reassurance | **Trust gap ↑** на doliv |
| **RU localization** | Full Cyrillic front + back + EAC | **Константа** — Cyrillic back сохранён | **≠ Mobil import 1L** |
| **M_NOISE** | Medium (universal redundancy) | Universal redundancy **↑** при сжатии; back wall **↑** load/bottle area | **Internal noise ↑** |

**POV — System Dynamics:**  
- *Potential:* 1L как **entry / top-up SKU** для legacy 10W-40 segment в RU official channel (ЮФО proxy).  
- *Limit:* OEM back-only + dense back на малом формате = **anxiety ↑** при impulse doliv без back-read.  
- *Anomaly:* Front API SG/CD **delivered** on 1L — **лучше** category norm для budget tier и **лучше** Mobil 1L institutional layer.

**Вывод (M):** 1L живёт в **другой retail-нише**, но Lukoil **не адаптирует** claim-layer под top-up (нет «top-up safe» / «exact 1L fill» rationale). **RU Cyrillic back** — конкурентное преимущество vs import 1L на doliv-канале.

---

### 2.5. MAP — Мэппинги

| MAP (база 4L) | 1L | Статус |
|---------------|-----|--------|
| Honeycomb mesh → filter/armor tribology (MCON_LS_04) | Mesh cropped | 🟡 **span ↓** — gestalt-completion load ↑ |
| «SUPER» superlative → budget protection (MCON_LS_02) | Константа | ✅ **robust** |
| Universal + car icon → any-car applicability (MCON_LS_01) | Константа | ✅ |
| API SG/CD front → spec gate (MCON_LS_03) | Константа | ✅ **robust** — budget honesty MAP |
| 4L → full service cycle | **1L → top-up module** | 🔄 **перекодировка объёма** |
| ActiPure® → innovation hyperbole (MSYS_LS_03) | Micro-text ↓ | 🟡 **latent only** @ shelf |
| OEM back grid → domestic trust (MCON_LS_07) | Present (АВТОВАЗ/УМЗ/ЗМЗ) | ✅ back; ⚠️ front gap |
| Dimple grip → controlled pour | **Новый MAP** (tactile) | ➕ LATENT; не на label |
| Service jug → authority | **Lost** on 1L | 🔻 carrier MAP ↓ |
| Semi-synthetic literal → chemistry honesty (MCON_LS_06) | Константа | ✅ |

**POV — Logical Coherence:**  
- *Conflict:* «УНИВЕРСАЛЬНОЕ» + top-up 1L — rhetorically compatible (budget owner may buy doliv), но **service semantics** (4L cycle vs 1L partial) **не артикулированы**.  
- *Contradiction:* «ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ ActiPure» + **API SG/CD** — **константа** на обоих форматах; conflict **не усиливается** на 1L.

**Вывод (MAP):** Ядро Universal Mass Heuristic + Honeycomb Armor Lite **масштабируется**. Искажаются: (1) mesh gestalt, (2) service-jug authority MAP, (3) volume semantics. Front legacy API MAP **не ломается** — ключевое отличие budget Lukoil от masked-spec LUXE tier.

---

### 2.6. EVAL — Оценка малого формата

| Метрика | 4L (база) | 1L (delta) | Δ |
|---------|-----------|------------|---|
| **Comprehensibility** | High (SUPER + 10W-40 + API front) | **High** SUPER + 10W-40 + API SG/CD; ActiPure **low** | ↓ secondary only |
| **Cognitive load** | Medium (база) | **Bimodal:** front clean / **back peak** on small bottle | **↑ back variance** |
| **Robustness (thumbnail)** | High | **High-medium:** SUPER + 10W-40 + LUKOIL ✅ | ↓ vs 4L, **↑ vs Mobil 1L** |
| **Premium perception** | Low (budget tier) | **Low** — mesh crop, no jug | ↓ carrier; **= tier** |
| **RU localization** | High (Cyrillic front+back) | **High** — константа | = |
| **Transaction speed (budget buyer)** | High | **High** @ close range; **high** @ shelf 2m (10W-40 front) | context-dependent |
| **Trust / institutional** | Medium (OEM back) | **Medium-low** — OEM back-only on doliv impulse | ↓ |

**POV — Relational States:** parity M_SYSTEM при **loss of service carrier morphology**; **compromise** DRY asset vs top-up channel needs.

**Вывод (EVAL):** 1L **не ломает** primary 10W-40 / universal semi value proposition. Ломается **service-jug authority** и **mesh gestalt completeness**. Для point-ref Classic/Protect: **1L и 4L — раздельные строки**; усреднение cognitive load **некорректно**.

---

## 3. M_OCCURRENCE — только новые и изменённые

> Occurrences базы (MOCC_LS_01–18, L01–L06, LAC01–LAC07, NS01–NS03) без изменений **не дублируются**.

### 3.1. MOCC_LSD_01 — Volume 1L (variant MOCC_LS_10)

**_min**
```yaml
M_OCC_ID: MOCC_LSD_01
CASE_ID: COMP_LUKOIL_SUPER_10W40_1L_DELTA
MATERIAL_ID: lukoil_super_10w40_1l_front_back_2022
SEGMENT_ID: label_core_spec_row
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "spec_row_white_box" }
M_OCC_SURFACE_FORM: "1L"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_LS_10 (4L → 1L)
```

**_full:** MAP `4L_service_cycle → 1L_topup_module`; M_CONSTR: MCON_LS_03 variant-by-format.

---

### 3.2. MOCC_LSD_02 — Circular dimple grip without handle

**_min**
```yaml
M_OCC_ID: MOCC_LSD_02
CASE_ID: COMP_LUKOIL_SUPER_10W40_1L_DELTA
MATERIAL_ID: lukoil_super_10w40_1l_front_back_2022
SEGMENT_ID: carrier_body_right
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "right_shoulder", pattern: "raised_circular_dimples" }
M_OCC_SURFACE_FORM: "Circular dimple grip zone; no integrated handle"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_ergonomics` → TARGET `dom_controlled_pour`; MAP `grip_as_topup_control`; contrast vs 4L integrated handle ([42 §7 C2](42_PGMM_LUKOIL_SUPER_10W-40.md)).

---

### 3.3. MOCC_LSD_03 — Narrow top-up bottle morphology

**_min**
```yaml
M_OCC_ID: MOCC_LSD_03
CASE_ID: COMP_LUKOIL_SUPER_10W40_1L_DELTA
MATERIAL_ID: lukoil_super_10w40_1l_front_back_2022
SEGMENT_ID: carrier_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_bottle_silhouette" }
M_OCC_SURFACE_FORM: "Tall narrow bottle; concave right shoulder; high CG vs 4L jug"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** **Carrier-code shift** from service jug to portable module; FUNCTION [`format_signal`, `channel_topup`].

---

### 3.4. MOCC_LSD_04 — Truncated honeycomb mesh (delta MOCC_LS_08)

**_min**
```yaml
M_OCC_ID: MOCC_LSD_04
CASE_ID: COMP_LUKOIL_SUPER_10W40_1L_DELTA
MATERIAL_ID: lukoil_super_10w40_1l_front_back_2022
SEGMENT_ID: label_core
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "mesh_zone_lateral_crop" }
M_OCC_SURFACE_FORM: "Red honeycomb/mesh pattern cropped at label lateral edges"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: MOCC_LS_08 (degraded)
```

**_full:** MCON_LS_04 span ↓; MSYS_LS_02 **partial delivery** on thumbnail.

---

### 3.5. MOCC_LSD_05 — Vertical label rescale pattern

**_min**
```yaml
M_OCC_ID: MOCC_LSD_05
CASE_ID: COMP_LUKOIL_SUPER_10W40_1L_DELTA
MATERIAL_ID: lukoil_super_10w40_1l_front_back_2022
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", axis: "vertical" }
M_OCC_SURFACE_FORM: "4L front layout vertically rescaled to narrow 1L label"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
```

**_full:** DRY brand asset strategy; FUNCTION [`format_adaptation`]; Lukoil SUPER **inherits** industry default ([31](31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md), [14](14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md)).

---

### 3.6. MOCC_LSD_06 — Barcode 1L SKU routing

**_min**
```yaml
M_OCC_ID: MOCC_LSD_06
CASE_ID: COMP_LUKOIL_SUPER_10W40_1L_DELTA
MATERIAL_ID: lukoil_super_10w40_1l_front_back_2022
SEGMENT_ID: label_back_footer
M_OCC_MODALITY_CLASS: visual_text
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "barcode", code: "4607161615366" }
M_OCC_SURFACE_FORM: "EAN-13 4607161615366 (1L); ≠ 4L 4607161615393"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_LS_16 (format variant)
```

**_full:** Retail routing; **не** spec drift — chemistry aligned across formats.

---

### 3.7. MOCC_LSD_LAC01 — OEM front gap on doliv impulse

**_min**
```yaml
M_OCC_ID: MOCC_LSD_LAC01
CASE_ID: COMP_LUKOIL_SUPER_10W40_1L_DELTA
MATERIAL_ID: lukoil_super_10w40_1l_front_back_2022
SEGMENT_ID: label_front
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: absence_of_effect
M_OCC_SPAN: { region: "front_oem_row", context: "topup_impulse_no_back_flip" }
M_OCC_SURFACE_FORM: "Domestic OEM stack on back only; front has universal+car not Avtovaz/UMZ/ZMZ"
M_OCC_STATUS_CLASS: inferred
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: LACUNA
BASE_REF: MOCC_LS_LAC02 (amplified on 1L channel)
```

**_full:** **Paradox усилен:** MSYS_LS_04 **under-delivered** on doliv, где back-read **маловероятен**.

---

## 4. Выводы для СТМ

### 4.1. Где дизайн SUPER «ломается» на 1L

1. **Service-jug authority** — 4L integrated handle + wide base **→** narrow top-up bottle; «universal full service» code **ослаблен**.
2. **Honeycomb gestalt (MCON_LS_04)** — mesh **усечён**; Armor Lite **partial** @ thumbnail.
3. **OEM front gap (LAC02)** — **усилен** на doliv-канале: domestic stack back-only **не работает** при impulse buy.
4. **Universal redundancy** — УНИВЕРСАЛЬНОЕ + car + SUPER + semi **без ослабления** при сжатии → cognitive noise **↑**.
5. **Back wall density** — тот же legal+OEM asset на **меньшем** носителе → proportional load **↑**.
6. **No top-up rationale** — нет «doliv-safe» / «exact fill» messaging для 1L.
7. **ActiPure micro-degradation** — innovation seal **↓** @ shelf distance (конфlict с SG chemistry **константа**).

### 4.2. Лакуны базового формата: усиление / ослабление

| Лакуна (база 4L) | На 1L |
|------------------|-------|
| MOCC_LS_LAC01 (fluid visualization) | **Константа** |
| MOCC_LS_LAC02 (OEM on front) | **Усилена** — doliv impulse |
| MOCC_LS_LAC03 (ACEA / modern API) | **Константа** (legacy segment) |
| MOCC_LS_LAC04 (ActiPure proof) | **Усилена деградация** — micro-text |
| MOCC_LS_LAC05 (QR / digital trace) | **Константа** — н/д на фото обоих форматов |
| MOCC_LS_LAC06 (eco / DPF / hybrid) | **Константа** |
| MOCC_LS_LAC07 (official supply front cue) | **Константа** |

### 4.3. Импликации для point-ref Classic/Protect / СТМ

- **Раздельные строки 4L и 1L** для SUPER (правило: 1 format = 1 row).
- **Format Robustness @120 px:** LUKOIL ✅ · SUPER ✅ · 10W-40 ✅ · API SG/CD ✅ · mesh 🟡 · ActiPure ✗ · 1L ✗.
- **Top-up Shelf Fit:** dimple grip + narrow profile ✅; OEM front row ✗; top-up claim ✗; semi-synthetic honesty ✅.
- **Attack vector СТМ 1L (Classic/Protect · 10W-40):** **не** копировать SUPER hyperbole stack; **перенять** readable SAE+API front + **domestic OEM band (2–3 front)** + **semi-synthetic honesty** + **fluid-precision antidote** к mesh; **добавить** top-up semantic («точный долив 1L»).
- **Cross-ref:** SUPER 1L **сильнее** Mobil 1L по front API + RU back — **не усреднять** с import norm в матрице.

**POV — System Dynamics:** SUPER на 1L **сохраняет** universal + SAE + API SG/CD front — **лучше import norm** для budget legacy. Окно СТМ — **OEM front row + top-up semantics + fluid metaphor + honest SN-tier** (если chemistry matches), **не** копирование «SUPER» hyperbole + ActiPure void.

---

## 5. POV-сводка (обязательная маркировка)

| Маркер | Фиксация |
|--------|----------|
| **Information Integrity** | Lacuna: OEM front on doliv; Redundancy: universal quadruple-code; Contamination: mesh polisemy **константа** |
| **Logical Coherence** | Conflict: universal service rhetoric vs 1L top-up **не артикулирован**; SUPER/ActiPure vs SG **константа** |
| **System Dynamics** | Potential: RU official 1L doliv · ЮФО legacy; Limit: back-only OEM on impulse; Anomaly: front API SG **robust** on 1L |
| **Relational States** | Parity: M_SYSTEM; Compromise: DRY asset vs service-jug authority + doliv channel gap |

---

## 6. Таблица «4L vs 1L» — для матрицы конкурентов

| # | Параметр | 4L (база) | 1L (delta) | Δ для матрицы |
|---|----------|-----------|------------|---------------|
| 1 | M_SYSTEM | Universal + Armor Lite + ActiPure + Domestic OEM | **константа** | = |
| 2 | Carrier morphology | 4L jug + handle | Narrow bottle + dimple grip | **разные строки** |
| 3 | Label strategy | Vertical budget stack | Vertical rescale 4L asset | compress |
| 4 | Universal + car icon | «УНИВЕРСАЛЬНОЕ МАСЛО» + car | **константа** | = / robust |
| 5 | 10W-40 legibility | High (white on black) | High (rel. ↑) | = / ↑ |
| 6 | API SG/CD front | Readable | **константа** | = (**≠ Mobil 1L**) |
| 7 | Semi-synthetic claim | Explicit front | **константа** | = |
| 8 | Volume marker | 4L service cycle | 1L top-up | **semantic shift** |
| 9 | Honeycomb mesh | Full gestalt | Lateral crop | ↓ |
| 10 | OEM approvals | Back: АВТОВАЗ/УМЗ/ЗМЗ | Back: **константа** | = |
| 11 | OEM front row | Absent (universal only) | Absent | **lacuna ↑** on doliv |
| 12 | ActiPure® | Readable close-range | Micro-text ↓ | ↓ |
| 13 | RU localization | Cyrillic front+back + EAC | **константа** | = |
| 14 | Retail context | Main / service shelf | Top-up / companion | **context split** |
| 15 | Thumbnail robustness | High | High-medium | ↓ slight |
| 16 | STM 1L attack | — | OEM front + top-up claim + fluid antidote + honest API tier | **opportunity** |

---

## 7. Issues for discussion

1. **10W-40 matrix branch:** включать ли SUPER 1L/4L как две строки в будущей Classic/Protect ветке?
2. **OEM front on 1L:** сознательный back-load для budget или упущение для doliv-канала (ЮФО)?
3. **vs LUXE 1L delta:** общий Lukoil DRY-rescale pattern — SUPER **проще** (нет gold/carbon tier drift).
4. **Batch drift:** 4L 09.11.22 vs 1L 07.08.22 — facing consistency; QR adoption **н/д** на обоих фото.
5. ~~**Next pass:** `stm-odsa`~~ → [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md) · [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) ✅

---

## 8. Связи

- База full: [42_PGMM_LUKOIL_SUPER_10W-40.md](42_PGMM_LUKOIL_SUPER_10W-40.md)
- Lukoil mass-mid proxy: [10_PGMM_LUKOIL_LUXE_5W-40.md](10_PGMM_LUKOIL_LUXE_5W-40.md) · [14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md](14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md)
- Lukoil mid-premium ref: [30](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md) · [31](31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md)
- Аналог delta (import): [13](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md) · [20](20_PGMM_mobil_1_0w_20_1L_delta.md)
- SAE / Classic line: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md) · [05_линейка_SKU_СТМ.md](05_линейка_SKU_СТМ.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)

---

*Delta-отчёт · CASE `COMP_LUKOIL_SUPER_10W40_1L_DELTA` · ingest 25.06.2026 · skill stm-pgmm-delta*
