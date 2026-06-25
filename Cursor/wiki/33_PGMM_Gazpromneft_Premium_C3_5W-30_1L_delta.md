# PGMM Delta: Gazpromneft Premium C3 5W-30 — 1L vs 4L

**Дата анализа:** 25.06.2026  
**Тип отчёта:** packaging_visual_metaphor_delta (не full PGMM)  
**Базовый кейс:** [32_PGMM_Gazpromneft_Premium_C3_5W-30.md](32_PGMM_Gazpromneft_Premium_C3_5W-30.md) (4L)  
**Артефакт:** Gazpromneft Premium C3 SAE 5W-30, 1L — фронт + back  
**Методология:** PGMM (Klepikov 2025) + neuromarketing-system-instructions  
**Primary domains (1–23):** D4 Packaging/Carrier · D8 Visual Semiotics · D12 Cognitive Load · D15 Shelf/Retail Context

**Контекст:** SKU вне матриц 5W-40 / 0W-20 ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)); **не смешивать** с DR-A/B.

```yaml
CASE_TYPE: packaging_visual_metaphor_delta
BRAND: Gazpromneft
LINE: Premium C3
SAE: 5W-30
FORMAT_BASE: 4L
FORMAT_DELTA: 1L
BASE_CASE_REF: Cursor/wiki/32_PGMM_Gazpromneft_Premium_C3_5W-30.md
PRODUCTION_STAMP: 20.03.2017 · batch 1711022801
BARCODE: 4650063116109
UNIQUE_CODE: GPN-02-01-11-12
CANON_SPEC: API SP · ACEA C2/C3 · dexos2 · MB 229.31/51/52 · VW 505 00/01 · BMW LL-04 · Renault RN17 · Opel · Fiat · Iveco — gazpromneft-oil.com (operator screenshot 25.06.2026)
PHOTO_ARTIFACT: front+back 1L show API SN + ACEA C3 (2017 batch) — **не канон**; rule SP > SN
```

---

## 0. CASE_min

| Поле | Значение |
|------|----------|
| **CASE_ID** | `COMP_GPN_PREMIUM_C3_5W30_1L_DELTA` |
| **CASE_TYPE** | `packaging_visual_metaphor_delta` |
| **BASE_CASE_REF** | `Cursor/wiki/32_PGMM_Gazpromneft_Premium_C3_5W-30.md` |
| **FORMAT** | 1L (delta vs 4L) |
| **MATERIAL_ID** | `gazpromneft_premium_c3_5w30_1l_front_back_2017` |
| **SEGMENT_ID** | `label_front_primary` + `label_back_full` |

---

## 0.1. Канон SKU vs фото-артефакт (triangulation)

**Правило проекта (25.06):** фото канистр из интернета часто **устаревшие**. При конфликте поколений — **канон = наивысший допуск** (API **SP > SN > SL**…). Официальный сайт оператора **перекрывает** legacy label.

| Слой | API / ACEA | Источник |
|------|------------|----------|
| **Canonical SKU** (строка матрицы) | **API SP** · **ACEA C2/C3** · dexos2 + полный OEM stack | gazpromneft-oil.com Premium C3 5W-30 (screenshot 25.06.2026) |
| **Photo artifact** (1L фото) | API **SN** · ACEA **C3** only | Batch **20.03.2017** · front=back SN/C3 |
| **Photo artifact** (4L back) | API **SN** · ACEA C3 | Batch **21.10.2017** ([32](32_PGMM_Gazpromneft_Premium_C3_5W-30.md)) |
| **Photo artifact** (4L front) | API **SP** · ACEA **C2/C3** | Aligns with **canon** |

**Вывод:** расхождение SN (фото 1L/4L back) vs SP (site + 4L front) — **не inter-format stratification**, а **legacy facing + правило SP > SN**. Delta ниже описывает **упаковку и макет** на фото; **spec-generation для матрицы и СТМ** — **API SP + ACEA C2/C3**.

---

## 1. Наследование из базы (без дублирования)

### 1.1. M_SYSTEM — **константа**

- **MSYS_GC3_01** — Spec-as-Brand Cognitive Amortization  
- **MSYS_GC3_02** — Thermokinetic Category Colonisation  
- **MSYS_GC3_03** — Institutional Anxiety & Back-Load  
- **MSYS_GC3_04** — Cross-Face Spec Drift — **на фото 1L:** front SN = back SN (internal parity); **на каноне SKU:** SP front = site = **drift снят** для матрицы

См. [32 §4](32_PGMM_Gazpromneft_Premium_C3_5W-30.md) · [§0.1 triangulation](#01-канон-sku-vs-фото-артефакт-triangulation).

### 1.2. DOMAIN_A / DOMAIN_B — **константа**

- **DOMAIN_A:** industrial thermokinetics (3D swirls) + corporate hegemony (Gazprom, STO) + ACEA class nomenclature  
- **DOMAIN_B:** Low-SAPS full-synthetic tribology, DPF/TWC aftertreatment, SAE 5W-30 C3  

См. [32 §5](32_PGMM_Gazpromneft_Premium_C3_5W-30.md).

### 1.3. M_CONSTRUCTION — variant-by-format

| ID (база) | Статус на 1L |
|-----------|--------------|
| MCON_GC3_01 Spec-in-Name Heuristic | ✅ «PREMIUM C3» + C3 chemistry **константа** |
| MCON_GC3_02 Thermokinetic Swirl Core | 🟡 3D-swirl **усечён** по боковым краям узкой этикетки |
| MCON_GC3_03 Front Standards Lockup | 🟡 на **фото:** SN/C3; **канон:** SP/C2/C3; ➕ **dexos2™ hero** (site + 1L photo) |
| MCON_GC3_04 Microtype OEM Suppression | 🟡 OEM footer **ещё плотнее**; Ford 917A **↑**; Opel/Iveco **↓ absent** |
| MCON_GC3_05 Authenticity Deferral | 🔻 «УНИКАЛЬНАЯ СИСТЕМА ПРОВЕРКИ…» **не на фронте 1L** |
| MCON_GC3_06 Back-Loaded Compliance Wall | ✅ структура **константа**; СТО **183-2015** (≠ 4L **103-2015**) |
| MCON_GC3_07 GPN Family Visual Continuity | ✅ silver HDPE + swirl + grip-ridges **константа** семейства |
| MCON_GC3_08 Solid-over-Fluid Suppression | ✅ лакуна fluid-визуала **константа** |
| MCON_GC3_09 SAE Oversized Anchor | ✅ «5W-30» white on orange **↑ relative salience** |

**POV — Relational States:** parity метафорической системы между форматами; **compromise** — DRY-rescale vs service-jug authority; **artifact note** — 1L photo **2017 SN** ≠ **canon SP** (site rule).

---

## 2. Delta по блокам

### 2.1. C — Носитель (Carrier)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Геометрия** | Широкий 4L-jug, integrated side handle | Узкая вертикальная бутылка; concave правая «плечевая» грань | **Смена морфологии:** service jug → top-up bottle |
| **Ручка** | Интегрированная боковая ручка 4L | **Нет ручки**; **3 диагональные grip-ridges** на правом плече (+ зеркальные у основания — GPN N pattern) | **Новый affordance:** doliv / одноручный захват |
| **Material** | Silver-grey HDPE + embossed G logo | Идентично | Константа |
| **Пропорции H:W** | Низкий, широкое основание, низкий CG | Высокий «towering» силуэт, узкая база | **DoF:** сжатие по ширине, растяжение по высоте |
| **Cap** | Silver textured screw cap | Grey ribbed cap; **асимметричное** смещение на горловине | 🟡 C-асимметрия (наследие [15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md)) |
| **Fill gauge** | н/д на 4L фото | **Translucent vertical strip** с делениями на правой грани | ➕ **новый C-signal** «контроль долива» |
| **Стабильность** | Широкая база 4L | Узкая база, **↑ CG** | **Limit:** риск опрокидывания на doliv-полке |

**Вывод (C):** 1L — **не downscale 4L-jug**, а **перекодировка carrier-code** по тому же шаблону, что Premium N 1L ([15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md)): silver HDPE + grip-ridges + narrow tower. GPN thermokinetic morphology **сохранена**, **institutional service-jug authority** **ослаблена**. Translucent strip — единственный **format-native fluid/control cue** в семействе GPN C3.

---

### 2.2. K — Композиция (Layout)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Стратегия макета** | Vertical stack: logo → PREMIUM C3 → swirl → 5W-30 → API/ACEA → OEM microtype | **Vertical rescale** 4L-макета на узкую этикетку | **K_PATTERN_VERTICAL_RESCALE** |
| **Negative space** | Silver HDPE field (MOCC_GC3_NS01); gap swirl↔footer (NS02) | NS01 **сжат**; NS02 **partial compress** | **↓ breathing room** |
| **Иерархия** | Brand → line → type → viscosity → standards → OEM | Идентичная последовательность | Константа порядка |
| **Читаемость 5W-30** | Oversized white on swirl/orange | Сохранена; **относительный размер ↑** к ширине | **Усилена** |
| **Читаемость объёма** | «4L» — full service cycle | «1L» — top-up / partial fill; **мельче** 5W-30 | **Semantic shift + ↓ legibility** |
| **Spec row front (photo)** | **API SP + ACEA C2/C3** (4L front) | **API SN + ACEA C3** + **dexos2™ hero** | legacy SN on 1L photo |
| **Spec row front (canon)** | **API SP + ACEA C2/C3** | **API SP + ACEA C2/C3** | **=** · site rule SP > SN |
| **OEM footer** | MB 229.51/52 · VW · BMW · Opel · Iveco microtype | MB 229.51 · Ford 917A · VW · BMW LL-04; **без Opel/Iveco** | 🟡 **OEM set delta** + **↓ microtype** |
| **Authenticity cue** | «УНИКАЛЬНАЯ СИСТЕМА ПРОВЕРКИ…» на фронте | **Absent** на фронте 1L | 🔻 **trust deferral lost** |
| **Back density** | Very high (legal + OEM + multilingual) | Тот же asset на **меньшем** носителе | **↑ proportional cognitive load** |

**POV — Information Integrity:**  
- *Redundancy:* «PREMIUM C3» + «C3» + «ACEA C3» + dexos2 — **пятислойное** кодирование сегмента **без ослабления**.  
- *Contamination:* dexos2 (GM ecosystem) **колонизирует** центр swirl-field — новый institutional anchor vs 4L.  
- *Lacuna:* authenticity front deferral **выпала**; OEM microtype **ещё ниже порога**.

**Вывод (K):** GPN **не пересобирает** Premium C3 layout на 1L — **DRY vertical rescale**. Главные потери: **swirl gestalt**, **authenticity front lockup**, **OEM microtype legibility**. На **фото** 1L — legacy **SN/C3** (2017); **канон SKU** — **SP/C2/C3** как на сайте и 4L front. **dexos2** — **константа канона** (site + 1L photo), не «1L-only».

---

### 2.3. S — Сигнальные паттерны

| Статус | Паттерн | Комментарий |
|--------|---------|-------------|
| ✅ **Сохранён** | Blue flame G + GAZPROMNEFT (MOCC_GC3_01) | Межформатный invariant |
| ✅ **Сохранён** | «PREMIUM C3» + spec-in-name (MOCC_GC3_02, L01) | C3 segment gate **robust** |
| ✅ **Сохранён** | «5W-30» oversized (MOCC_GC3_04) | Primary SAE heuristic |
| ✅ **Сохранён** | 3D orange/yellow/blue swirls (MOCC_GC3_06) | Thermokinetic core **partial crop** |
| ✅ **Сохранён** | Car silhouette (MOCC_GC3_07) | Application shorthand |
| ✅ **Сохранён** | API + ACEA front row (MOCC_GC3_05) | **Robust** layout; **photo:** SN/C3 · **canon:** SP/C2/C3 |
| 🟡 **Photo artifact** | Front standards on 1L photo | SN/C3 (2017 batch) — **superseded by canon SP** |
| 🟡 **Канон** | dexos2™ + full OEM (site) | **Present** on current SKU all formats (1L/4L/5L…) |
| ➕ **Новый (photo)** | **dexos2™ center logo** (MOCC_GC3D_04) | Center hero on 1L photo; **also on site canon** |
| ➕ **Новый** | Ford WSS-M2C917-A / «917A» (MOCC_GC3D_08) | **↑** vs 4L OEM row |
| ➕ **Новый** | Diagonal grip-ridges + fill strip (MOCC_GC3D_02, 05) | Top-up control on C |
| ➕ **Новый** | Barcode 4650063116109 | SKU routing 1L |
| 🔻 **Деградировал** | Swirl 3D gestalt (MOCC_GC3_06) | Lateral crop |
| 🔻 **Деградировал** | OEM microtype footer (MOCC_GC3_08) | Below close-read @ 1L |
| 🔻 **Деградировал** | Authenticity deferral front (MOCC_GC3_10) | **Missing** on 1L |
| 🔻 **Absent** | Opel OV0401547 · Iveco 18-1811 (4L front) | **OEM stack narrowed** on 1L |
| 🔻 **Absent on photo** | ACEA C2 on 1L photo front | **Present in canon** (site + 4L front) |

**Вывод (S):** Flagship signals (GPN + PREMIUM C3 + 5W-30 + spec row) **survive** downscale. **dexos2** — **канон SKU**, на 1L photo виден; на 4L base photo **не попал в кадр**, не «1L-only». Secondary layer (OEM microtype, authenticity front) **деградирует**. **SN на фото 1L** — **legacy artifact**, не понижает **канон SP** для матрицы.

---

### 2.4. M — Среда (Medium / контекст потребления)

| Контекст | 4L | 1L | Δ |
|----------|----|----|---|
| **Retail-полка** | Основная / service shelf; full change C3 | **Top-up / companion**; doliv, касса, СТО | **Смена M_CONTEXT** |
| **Плотность выкладки** | ~4–6 facings (широкие jugs) | **~10–14 facings** (узкий профиль) | **↑ linear density** |
| **Дистанция считывания** | 1,2–2,5 m | 0,5–1,2 m (рука потребителя) | **Ближний контакт** |
| **E-commerce thumbnail** | Swirl + 5W-30 + GPN ✅ | GPN + 5W-30 + **dexos2** ✅; 1L, OEM microtype **✗** @120 px | **Medium:** dexos2 **↑** recognition for GM-park buyers |
| **5W-30 C3 context** | Modern park RU service | Тот же buyer; **меньше** service-jug reassurance | **Trust gap ↑** on doliv |
| **RU localization** | Full Cyrillic front + multilingual back | **Константа** — Cyrillic back + EAC + Fryazino MLP | = |
| **Batch temporal** | 4L back 2017 SN (photo artifact) | 1L **20.03.2017** SN on photo | **Canon SP** supersedes both |
| **M_NOISE** | Medium-high (swirl + spec redundancy) | Redundancy **↑** при сжатии; dexos2 **adds** OEM-program noise | **↑ internal noise** |

**POV — System Dynamics:**  
- *Potential:* dexos2 + narrow 1L → **GM/modern-park doliv** niche in official GPN channel.  
- *Limit:* legacy photo facing; authenticity front **removed** on 1L vs 4L.
- *Anomaly:* **site canon SP** vs **photo SN** — типичный retail-photo lag; **не** inter-format product split.

**Вывод (M):** 1L живёт в **doliv-нише** без адаптации claim-layer под top-up (нет «doliv-safe» / fill-gauge **на этикетке**, только на C). **dexos2** — единственный **channel-specific** OEM-program cue, усиливающий e-commerce для GM-совместимого сегмента.

---

### 2.5. MAP — Мэппинги

| MAP (база 4L) | 1L | Статус |
|---------------|-----|--------|
| Spec-in-name → Low-SAPS filter (MCON_GC3_01) | Константа | ✅ **robust** |
| Thermokinetic swirl → tribology (MCON_GC3_02) | Swirl cropped | 🟡 **span ↓** |
| Front API/ACEA → spec gate (MCON_GC3_03) | Photo SN/C3; **canon SP/C2/C3** | 🟡 **photo lag**; **canon =** across formats |
| dexos2 → GM aftertreatment program | **Canon** site + 1L photo | ✅ **SKU-level**, not 1L-only |
| 4L → full service cycle | **1L → top-up module** | 🔄 **перекодировка объёма** |
| OEM microtype → institutional trust (MCON_GC3_04) | **MAP broken** @ microtype threshold | ⚠️ **LACUNA MAP** |
| Authenticity deferral → anti-fraud (MCON_GC3_05) | **Front MAP lost** on 1L | 🔻 |
| Back compliance wall → DPF/TWC proof (MCON_GC3_06) | Present; СТО **183** vs **103** | 🟡 **institutional spec drift** |
| Grip-ridges + fill strip → controlled pour | **New tactile MAP** | ➕ LATENT (not on label) |
| Service jug → authority | **Lost** on 1L | 🔻 carrier MAP ↓ |
| Cross-face spec drift (MSYS_GC3_04) | Photo: SN=SN on 1L; **canon SP** | ✅ **resolved at SKU level** |

**POV — Logical Coherence:**  
- *Conflict (photo only):* legacy SN on 1L/4L back vs SP on site — **closed by SP > SN rule**.  
- *Contradiction:* dexos2 (GM) **перекрывает** swirl center — dual institutional anchors **константа**.

**Вывод (MAP):** Ядро Spec-as-Brand + thermokinetic GPN code **масштабируется**. Искажаются: swirl gestalt, service-jug authority, OEM microtype MAP, authenticity front MAP. **dexos2** — **канон SKU**. **Legacy SN на фото** не создаёт отдельный «1L API tier» — **канон SP** для матрицы.

---

### 2.6. EVAL — Оценка малого формата

| Метрика | 4L (база) | 1L (delta) | Δ |
|---------|-----------|------------|---|
| **Comprehensibility** | High brand + 5W-30 + spec front; low OEM microtype | **High** C3 + 5W-30; photo SN **misleading** vs **canon SP** | canon via site |
| **Cognitive load** | Medium-high (база) | **Bimodal:** front compress / **back peak** on small bottle | **↑ back variance** |
| **Robustness (thumbnail)** | Medium-high (5W-30 + swirl + GPN) | **Medium-high:** GPN + 5W-30 + **dexos2** ✅; 1L, OEM **✗** | ≈ / dexos2 **↑** |
| **Logical coherence (spec)** | Photo: SP front vs SN back | Photo: SN=SN; **Canon: SP site-wide** | **↑ at SKU level** |
| **Premium perception** | Medium (Premium C3 tier) | **Medium** — silver + swirl; no jug | ↓ carrier |
| **RU localization** | High | **High** — константа | = |
| **Trust / institutional** | Medium-high (authenticity deferral front) | **Medium** — no front authenticity; back EAC + MLP | ↓ front trust |
| **Transaction speed (C3 buyer)** | High (C3-in-name + spec row) | **High** @ close range | context-dependent |

**POV — Relational States:** parity M_SYSTEM при **loss of service carrier**; **compromise** DRY asset vs doliv channel.

**Вывод (EVAL):** 1L **не ломает** primary C3 + 5W-30 value proposition. Ломается **service-jug authority**, **OEM microtype**, **authenticity front deferral**. **Канон API SP** один для 1L/4L (site); **раздельные строки матрицы** — по **формату упаковки**, не по API tier. Photo SN — **не понижать** канон.

---

## 3. M_OCCURRENCE — только новые и изменённые

> Occurrences базы (MOCC_GC3_01–18, L01–L06, LAC01–LAC06, NS01–NS03) без изменений **не дублируются**.

### 3.1. MOCC_GC3D_01 — Volume 1L (variant MOCC_GC3_09)

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_01
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_footer_right
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "footer_orange_block_bottom_right" }
M_OCC_SURFACE_FORM: "1L"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_GC3_09 (4L → 1L)
```

**_full:** MAP `4L_service_cycle → 1L_topup_module`; M_CONSTR: MCON_GC3_09 variant-by-format.

---

### 3.2. MOCC_GC3D_02 — Diagonal grip ridges (GPN 1L family pattern)

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_02
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: carrier_body_right
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "right_shoulder", pattern: "3_diagonal_recessed_ridges" }
M_OCC_SURFACE_FORM: "3 diagonal grip channels on shoulder; mirrors Premium N 1L affordance"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_ergonomics` → TARGET `dom_controlled_pour`; cross-ref [15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md) gocc_001; MCON_GC3_07 variant-by-format.

---

### 3.3. MOCC_GC3D_03 — Narrow top-up bottle morphology

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_03
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: carrier_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_bottle_silhouette" }
M_OCC_SURFACE_FORM: "Tall narrow silver bottle; concave right grip; high CG vs 4L jug"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** Carrier-code shift service jug → portable module; FUNCTION [`format_signal`, `channel_topup`].

---

### 3.4. MOCC_GC3D_04 — dexos2™ center hero logo

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_04
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_core_center
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: symbolic
M_OCC_SPAN: { region: "swirl_field_center", text: "dexos2" }
M_OCC_SURFACE_FORM: "dexos2 trademark logo centered on swirl graphic — front + back"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: absent on 4L base photo (32)
```

**_full:** MAP GM OEM-program → Low-SAPS C3 trust; **contaminates** thermokinetic swirl center; MCON_GC3_03 **variant-by-format**; MSYS_GC3_03 **↑ institutional layer**.

---

### 3.5. MOCC_GC3D_05 — Translucent fill-level strip on carrier

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_05
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: carrier_body_right_edge
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "vertical_strip_with_graduations" }
M_OCC_SURFACE_FORM: "Translucent measurement window for remaining volume"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** Partial antidote to MOCC_GC3_LAC01 (fluid visualization) at **carrier** level only; MAP `volume_control → topup_precision`; **not mirrored on label**.

---

### 3.6. MOCC_GC3D_06 — Truncated swirl gestalt

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_06
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_core
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "swirl_lateral_crop" }
M_OCC_SURFACE_FORM: "3D orange/yellow/blue swirls cropped at narrow label edges"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: MOCC_GC3_06 (degraded)
```

**_full:** MCON_GC3_02 span ↓; MSYS_GC3_02 **partial delivery** @ thumbnail.

---

### 3.7. MOCC_GC3D_07 — Legacy API SN on photo (2017 artifact)

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_07
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_footer_spec_row + label_back_header
M_OCC_MODALITY_CLASS: visual_text
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "front_and_back", text: "API SN · ACEA C3" }
M_OCC_SURFACE_FORM: "API SN on 1L photo front+back — 2017 batch; superseded by canon API SP (site)"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
EVID_CLASS: photo_artifact
CANON_OVERRIDE: API SP · ACEA C2/C3 (gazpromneft-oil.com)
BASE_REF: MOCC_GC3_05
```

**_full:** **Not inter-format stratification** — legacy retail photo lag. Rule **SP > SN** project-wide. ODSA: artifact vs canonical claim **split**.

---

### 3.8. MOCC_GC3D_08 — Ford WSS-M2C917-A approval prominence

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_08
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_footer_oem + label_back_oem
M_OCC_MODALITY_CLASS: visual_text
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "oem_row", text: "Ford 917A / WSS-M2C917-A" }
M_OCC_SURFACE_FORM: "Ford approval on front microtype and back header"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: not prominent on 4L base (32)
```

**_full:** OEM MAP **shift** — Ford **↑**, Opel/Iveco **↓ absent** vs 4L front microtype.

---

### 3.9. MOCC_GC3D_09 — STO 84035624-183-2015 (vs 4L 103-2015)

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_09
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_back_header
M_OCC_MODALITY_CLASS: visual_text
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "corporate_spec_row" }
M_OCC_SURFACE_FORM: "СТО 84035624-183-2015"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_GC3_14 (4L: 103-2015)
```

**_full:** **Batch/format institutional spec drift** — verify unified STO across current facings.

---

### 3.10. MOCC_GC3D_10 — Vertical label rescale (DRY asset)

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_10
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", axis: "vertical" }
M_OCC_SURFACE_FORM: "4L Premium C3 layout vertically rescaled to narrow 1L label"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
```

**_full:** GPN family DRY strategy — shared with [15](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md), [31](31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md).

---

### 3.11. MOCC_GC3D_LAC01 — Missing authenticity deferral on 1L front

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_LAC01
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_front
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: absence_of_effect
M_OCC_SPAN: { region: "footer", expected: "authenticity_deferral" }
M_OCC_SURFACE_FORM: "No «УНИКАЛЬНАЯ СИСТЕМА ПРОВЕРКИ…» on 1L front vs 4L MOCC_GC3_10"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LACUNA
BASE_REF: MOCC_GC3_10 (lost on 1L)
```

**_full:** MSYS_GC3_03 **under-delivered** on doliv impulse; **↑ counterfeiting anxiety** vs 4L front.

---

### 3.12. MOCC_GC3D_LAC02 — OEM microtype below doliv threshold

**_min**
```yaml
M_OCC_ID: MOCC_GC3D_LAC02
CASE_ID: COMP_GPN_PREMIUM_C3_5W30_1L_DELTA
MATERIAL_ID: gazpromneft_premium_c3_5w30_1l_front_back_2017
SEGMENT_ID: label_footer_microtype
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: absence_of_effect
M_OCC_SPAN: { region: "oem_footer", context: "topup_close_read_still_fail" }
M_OCC_SURFACE_FORM: "MB/VW/BMW/Ford microtype present but below functional decode threshold"
M_OCC_STATUS_CLASS: inferred
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: LACUNA
BASE_REF: MOCC_GC3_LAC02 (amplified on 1L)
```

**_full:** MCON_GC3_04 **critical degradation** — declarative but non-functional MAP.

---

## 4. Выводы для СТМ

### 4.1. Где дизайн Premium C3 «ломается» на 1L

1. **Service-jug authority** — 4L handle + wide base **→** narrow top-up bottle + grip-ridges; C3 «полная замена» code **ослаблен**.
2. **Thermokinetic swirl gestalt (MCON_GC3_02)** — 3D-swirl **усечён**; dexos2 **захватывает** центр композиции.
3. **OEM microtype (MCON_GC3_04)** — **функционально мёртв** на 1L; paradox back-load **усилен** на doliv.
4. **Authenticity front deferral (MCON_GC3_05)** — **выпал** на 1L vs 4L — trust stack **↓**.
5. **Inter-format spec stratification** — **снято:** канон **API SP** един для 1L/4L (site); photo SN = legacy only.
6. **No top-up rationale on label** — fill strip on C **не мэпится** в K/S; нет «doliv-safe» messaging.
7. **2017 batch on photo** — legacy artifact; **не понижать** канон SP.

### 4.2. Лакуны базового формата: усиление / ослабление

| Лакуна (база 4L) | На 1L |
|------------------|-------|
| MOCC_GC3_LAC01 (fluid visualization) | **Частично ослаблена** — fill strip on C only |
| MOCC_GC3_LAC02 (OEM on front readable) | **Усилена** — microtype **fail** |
| MOCC_GC3_LAC03 (HTHS, Noack, SAPS) | **Константа** |
| MOCC_GC3_LAC04 (DPF/TWC infographic) | **Константа** (text back only) |
| MOCC_GC3_LAC05 (hybrid/eco) | **Константа** |
| MOCC_GC3_LAC06 (official supply front) | **Усилена** — authenticity front **lost** |
| Cross-face spec drift (MSYS_GC3_04) | **Ослаблена** — photo SN=SN on 1L; **canon SP** site-wide |

### 4.3. Импликации для point-ref 5W-30 / СТМ

- **Раздельные строки 4L и 1L** для GPN Premium C3 (правило: 1 format = 1 row).
- **Format Robustness @120 px:** GPN ✅ · PREMIUM C3 ✅ · 5W-30 ✅ · dexos2 ✅ (GM niche) · API/ACEA 🟡 (micro) · OEM microtype ✗ · 1L ✗ · authenticity front ✗.
- **Top-up Shelf Fit:** grip-ridges + fill strip ✅; OEM readable front ✗; top-up claim on label ✗; authenticity front ✗.
- **Attack vector СТМ 1L (C3 proxy):** **не** blind DRY-rescale; **front readable OEM band (2–3)** + **top-up semantic** + **front QR/authenticity** + **single-source spec** front=back=site; **fluid-precision antidote** к swirl; **не копировать** dexos2 unless OEM program exists.
- **Cross-ref:** GPN C3 1L **слабее** LUKOIL GC 1L по front spec legibility; **canon SP/C2/C3** = 4L front = site.

**POV — System Dynamics:** Premium C3 на 1L — **DRY rescale** + **legacy photo SN**; **канон SP** с сайта. Окно СТМ — **readable OEM + authenticity front + top-up semantics**.

---

## 5. POV-сводка (обязательная маркировка)

| Маркер | Фиксация |
|--------|----------|
| **Information Integrity** | Lacuna: OEM microtype + authenticity front; **Canon repair:** SP > SN rule + site triangulation |
| **Logical Coherence** | Photo SN vs canon SP — **closed** by project rule; dexos2 vs swirl **dual anchor** |
| **System Dynamics** | Potential: dexos2 GM doliv; Limit: legacy photos in the wild; **Canon: API SP all formats** |
| **Relational States** | Parity: M_SYSTEM core; Compromise: DRY asset vs service-jug + doliv channel gap |

---

## 6. Таблица «4L vs 1L» — для матрицы конкурентов

| # | Параметр | 4L (база) | 1L (delta) | Δ для матрицы |
|---|----------|-----------|------------|---------------|
| 1 | M_SYSTEM | Spec-in-name + swirl + back-load | **константа** | = |
| 2 | Carrier morphology | 4L jug + handle | Narrow bottle + grip-ridges + fill strip | **разные строки** |
| 3 | Label strategy | Vertical GPN C3 stack | Vertical rescale 4L asset | compress |
| 4 | Front API/ACEA (canon) | **API SP + ACEA C2/C3** | **API SP + ACEA C2/C3** | **=** (site) |
| 4b | Front API/ACEA (photo) | SP/C2/C3 front · SN back | **SN/C3** (2017) | legacy artifact |
| 5 | dexos2™ | **Site canon** | Center on 1L photo | **SKU-level** |
| 6 | 5W-30 legibility | High (oversized) | High (rel. ↑) | = / ↑ |
| 7 | Volume marker | 4L service cycle | 1L top-up | **semantic shift** |
| 8 | Swirl gestalt | Full 3D core | Lateral crop + dexos2 overlay | ↓ decorative / ↑ OEM-program |
| 9 | OEM front | Microtype MB/VW/BMW/Opel/Iveco | Microtype MB/Ford/VW/BMW; **no Opel/Iveco** | set delta + ↓ legibility |
| 10 | Authenticity front | «См. на обороте» deferral | **Absent** | ↓ trust |
| 11 | Front-back spec (canon) | SP site-wide | **SP** | **=** |
| 11b | Front-back spec (photo) | SP front vs SN back | SN=SN on 1L | artifact |
| 12 | СТО corporate spec | 84035624-**103**-2015 (4L back) | 84035624-**183**-2015 | verify drift |
| 13 | RU localization | Cyrillic front + multilingual back | **Константа** + Fryazino MLP | = |
| 14 | Retail context | Main / service shelf | Top-up / companion | **context split** |
| 15 | STM 1L attack | — | OEM band + authenticity front + top-up claim + spec parity | **opportunity** |

---

## 7. Issues for discussion

1. **Legacy photo rule:** зафиксировано в AGENTS + [08_PGMM](08_PGMM_упаковка.md) — **SP > SN** для GPN C3.
2. **dexos2:** **канон SKU** (site), не артефакт 1L-only.
3. **Authenticity front:** deferral на 4L photo, **нет** на 1L photo — packaging delta, не spec.
4. **Point-ref 5W-30:** 1L/4L — **две строки** по формату; **API tier один** (SP).
5. ~~**ODSA pass:** `stm-odsa` 1L~~ → [37](37_ODSA_Gazpromneft_Premium_C3_5W-30_1L.md) ✅ — artifact SN vs **canon SP** в Evidence Ledger.
6. **STO 103 vs 183:** batch artifact; site OEM superset — verify in ODSA.

---

## 8. Связи

- База full: [32_PGMM_Gazpromneft_Premium_C3_5W-30.md](32_PGMM_Gazpromneft_Premium_C3_5W-30.md)
- GPN family 1L pattern: [15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md)
- 5W-30 C3 peer delta: [31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md](31_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30_1L_delta.md)
- GPN mass-mid proxy: [11_PGMM_Gazpromneft_Premium_N_5W-40.md](11_PGMM_Gazpromneft_Premium_N_5W-40.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Next: `stm-odsa` (1L — artifact vs **canon SP**) · site triangulation ✅

---

*Delta-отчёт · CASE `COMP_GPN_PREMIUM_C3_5W30_1L_DELTA` · ingest 25.06.2026 · rev.2 canon SP rule · skill stm-pgmm-delta*
