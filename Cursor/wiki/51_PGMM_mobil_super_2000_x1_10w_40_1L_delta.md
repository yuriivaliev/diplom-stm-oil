# PGMM Delta: Mobil Super 2000 x1 10W-40 — 1L vs 4L

**Дата анализа:** 25.06.2026  
**Тип отчёта:** packaging_visual_metaphor_delta (не full PGMM)  
**Базовый кейс:** [50_PGMM_mobil_super_2000_x1_10w_40.md](50_PGMM_mobil_super_2000_x1_10w_40.md) (4L)  
**Артефакт:** Mobil Super 2000 x1 SAE 10W-40, 1L — фронт + back  
**Методология:** PGMM (Klepikov 2025) + neuromarketing-system-instructions  
**Primary domains (1–23):** D4 Packaging/Carrier · D8 Visual Semiotics · D12 Cognitive Load · D15 Shelf/Retail Context

**Контекст:** SKU вне матриц 5W-40 / 0W-20 / 5W-30 ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)); point-ref **Classic/Protect · ЮФО 10W-40**; **не смешивать** с DR-A/B.

```yaml
CASE_TYPE: packaging_visual_metaphor_delta
BRAND: Mobil
LINE: Super 2000 x1
SAE: 10W-40
FORMAT_BASE: 4L
FORMAT_DELTA: 1L
BASE_CASE_REF: Cursor/wiki/50_PGMM_mobil_super_2000_x1_10w_40.md
PRODUCTION_STAMP: MADE 25-11-2022 · S2B8931 05789
BARCODE: 5 055107 433614
LABEL_CODES: front 819701B · back 830790
```

### Artifact vs canonical

| Поле | Artifact (фото 1L · batch 25-11-22) | Artifact (база 4L · batch 16-07-21) | Canonical (line) | Статус |
|------|-------------------------------------|-------------------------------------|------------------|--------|
| Base oil | «Semi-Synthetic Motor Oil» front | Идентично | Полусинтетическое Mobil Super 2000 | ✅ aligned |
| API | **—** front · back **SL/SM/SN/SN PLUS** + CF | **—** front · back SN stack | **SN+** tier | ✅ cross-format parity · 🟡 front lacuna |
| ACEA | Back **A3/B3** | Back A3/B3 | A3/B3 | ✅ back-only |
| OEM | Back: MB 229.1 · VW 501 01/505 00 · **AVTOVAZ** | Back MB/VW/Avtovaz | Artifact OEM grid | ✅ back-only |
| Volume | **1L** front + «1Le» back | **4L** front + back | Format SKU | ✅ variant-by-format |
| RU supply | EN/TR back · no Cyrillic | EN/TR import | Parallel import (EX-01) | 🟡 import |

**Triangulation:** operator site **pending** (no EX-Mobil-Super-2000 ID in [04_источники_и_URL.md](04_источники_и_URL.md)); canon row = **artifact back stack** until site verify. Batch **2022 (1L)** vs **2021 (4L base)** — 1L facing **новее**; spec grid **без деградации** vs база.

---

## 0. CASE_min

| Поле | Значение |
|------|----------|
| **CASE_ID** | `COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA` |
| **CASE_TYPE** | `packaging_visual_metaphor_delta` |
| **BASE_CASE_REF** | `Cursor/wiki/50_PGMM_mobil_super_2000_x1_10w_40.md` |
| **FORMAT** | 1L (delta vs 4L) |
| **MATERIAL_ID** | `mobil_super_2000_x1_10w40_1l_front_back_2022` |
| **SEGMENT_ID** | `label_front_primary` + `label_back_full` |

---

## 1. Наследование из базы (без дублирования)

### 1.1. M_SYSTEM — **константа**

- **MSYS_MS2_01** — Numeric Line Heuristic + Transaction  
- **MSYS_MS2_02** — Down-Tier Fluid Kinetics  
- **MSYS_MS2_03** — Mobil Global Brand Transfer + Import Facing  
- **MSYS_MS2_04** — Back-Loaded Compliance Grid  

См. [50 §4](50_PGMM_mobil_super_2000_x1_10w_40.md). Конфликт MSYS_MS2_01 ↔ MSYS_MS2_02 (numeric tier + gold fluid vs semi honesty) **не разрешается** на 1L — сохраняется.

### 1.2. DOMAIN_A / DOMAIN_B — **константа**

- **DOMAIN_A:** gold fluid atomization, numeric tier ladder (2000), Mobil corporate energy (red O), import OEM heraldry  
- **DOMAIN_B:** semi-synthetic 10W-40 tribology, API SN-class chemistry, multi-fuel PVL service  

См. [50 §5](50_PGMM_mobil_super_2000_x1_10w_40.md).

### 1.3. M_CONSTRUCTION — variant-by-format

| ID (база) | Статус на 1L |
|-----------|--------------|
| MCON_MS2_01 Numeric Tier Heuristic (2000) | ✅ «2000» + «Super» **robust**; vertical «tower» ↑ |
| MCON_MS2_02 x1 Sub-Line Lockup | ✅ «x1» sub-badge **сохранён** |
| MCON_MS2_03 SAE Front Telemetry | ✅ **10W-40** magenta band **robust**; относительный масштаб ↑ |
| MCON_MS2_04 Semi-Synthetic Literal Honesty | ✅ «Semi-Synthetic Motor Oil» **константа** |
| MCON_MS2_05 Gold Fluid Kinetics (down-tier) | 🟡 gold droplets + metallic ring **lateral crop** |
| MCON_MS2_06 Multi-Fuel Footer Scope | 🟡 «Gasoline & Diesel» **↓ micro-text** |
| MCON_MS2_07 Mobil Global Brand Transfer | ✅ red O + silver HDPE **константа** |
| MCON_MS2_08 Back-Loaded Modern Spec Grid | ✅ API SN stack + ACEA + OEM **константа** по составу |
| MCON_MS2_09 Import EN/TR Disclosure | ✅ EN/TR back **константа** |
| MCON_MS2_10 API Front Lacuna (Mobil norm) | ✅ **усилена** vs budget peers [43][47] с API SG front |

**POV — Relational States:** parity метафорической системы между форматами; **compromise** — service-jug authority (4L handle) **жертвуется** без пересборки claim-layer; **parity** с Mobil Super family DRY-rescale ([13](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md), [39](39_PGMM_mobil_1_esp_5w_30_1L_delta.md)).

---

## 2. Delta по блокам

### 2.1. C — Носитель (Carrier)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Геометрия** | Широкий 4L-jug, asymmetrical «service» силуэт | Узкая вертикальная бутылка; concave правая грань к горловине | **Смена морфологии:** service jug → top-up bottle |
| **Ручка** | Интегрированная боковая ручка 4L (MOCC_MS2_10) | **Нет ручки**; 7 горизontальных рельефных канавок на правой грани + горизontальные indentations слева | **Новый affordance:** doliv / одноручный захват |
| **Material** | Silver-grey metallic HDPE | Идентично | Константа |
| **Пропорции H:W** | Низкий, широкое основание, низкий CG | Высокий «towering» силуэт, узкая база | **DoF:** сжатие по ширине, растяжение по высоте |
| **Cap** | Black ribbed screw cap | Black ribbed screw cap (пропорционально меньше) | Константа семантики |
| **Стабильность** | Широкая база 4L | Узкая база, **↑ CG** | **Limit:** риск опрокидывания на doliv-полке |

**Вывод (C):** 1L — не downscale 4L-jug, а **перекодировка carrier-code**: с «import service container» на «portable top-up module». Mobil family morphology (silver HDPE + black cap + dark label) **сохранена**, но **institutional mass-retail authority** 4L-jug **ослаблена** — pattern идентичен Super 3000 x1 1L [13] и Mobil 1 ESP 1L [39].

---

### 2.2. K — Композиция (Layout)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Стратегия макета** | Vertical stack: logo → Super → 2000/x1 → SAE/semi → graphic/footer | **Vertical rescale** 4L-макета на узкую этикетку | **K_PATTERN_VERTICAL_RESCALE** |
| **Negative space** | Dark field upper half (MOCC_MS2_NS01); diagonal graphic split (NS02) | NS01 **partial compress**; NS02 **graphic zone narrowed** | **↓ breathing room** в core |
| **Иерархия** | Brand → Super → 2000/x1 → SAE/semi → footer | Идентичная последовательность | Константа порядка |
| **Читаемость 10W-40** | Prominent white on magenta band | Сохранена; **относительный размер ↑** к ширине | **Усилена** |
| **Читаемость объёма** | «4L» + QR + **819702A** — full service cycle | «1L» + QR + **819701B** — top-up | **Semantic shift + SKU lock variant** |
| **Semi-synthetic line** | Readable mid-label | Present; **↓** @ shelf 2m | 🟡 |
| **Back density** | High (legal + spec + multilingual) | Тот же asset на **меньшем** носителе | **↑ proportional cognitive load** |

**POV — Information Integrity:**  
- *Redundancy:* Super + 2000 + x1 + semi + Gasoline&Diesel — **без ослабления** при сжатии.  
- *Contamination:* gold droplets = fluid + premium + synthetic cue — **константа** в semi tier.  
- *Lacuna:* dark breathing room (NS01) **частично схлопнут**; API front **константа**.

**Вывод (K):** Mobil **не пересобирает** Super 2000 layout на 1L — **DRY vertical rescale** (industry + Mobil family norm). Primary scan path (Super/2000 → 10W-40 → semi) **robust**. Secondary: «Gasoline & Diesel» + gold graphic **under-delivered** @ 2m; footer cluster (QR + 1L + code) **уплотнён**.

---

### 2.3. S — Сигнальные паттерны

| Статус | Паттерн | Комментарий |
|--------|---------|-------------|
| ✅ **Сохранён** | Mobil blue + red «O» (MOCC_MS2_01) | Якорь узнаваемости |
| ✅ **Сохранён** | «Super» black + red underline (MOCC_MS2_02) | Line identity |
| ✅ **Сохранён** | «2000» silver-outlined + «x1» (MOCC_MS2_03–04) | Numeric tier heuristic |
| ✅ **Сохранён** | Magenta «10W-40» band (MOCC_MS2_05) | Primary SAE heuristic |
| ✅ **Сохранён** | «Semi-Synthetic Motor Oil» (MOCC_MS2_06) | Chemistry honesty |
| ✅ **Сохранён** | Silver jug + black cap (MOCC_MS2_10–11) | Mobil shelf block |
| 🟡 **Усилен** | Vertical brand-stack «tower» | Super/2000 **dominant** на узком носителе |
| 🔻 **Деградировал** | Gold droplet spray + metallic ring (MOCC_MS2_07) | **Lateral crop**; gestalt fluid kinetics **incomplete** |
| 🔻 **Деградировал** | «Gasoline & Diesel» footer (MOCC_MS2_08) | Micro-text @ thumbnail |
| 🔻 **Деградировал** | Integrated 4L handle affordance | **Absent** — service-jug signal lost |
| ➕ **Новый (C→S)** | Grip-ridges + left indentations | Тактильный сигнал «doliv/control» |
| 🟡 **Variant** | QR + 1L + **819701B** (vs 819702A 4L) | SKU lock; QR **rescaled** not new to line |

**Вывод (S):** Высокочастотные бренд-сигналы (Mobil, Super, 2000, 10W-40, semi) **robust** к даунскейлу. Низкочастотные fluid-kinetic детали (gold droplets, multi-fuel footer) **фильтруются**. **Differentiator vs LUKOIL/GPN Super 1L [43][47]:** API **still off-front** — lacuna **усиливается** на doliv-полке, где domestic peers front-load SG/CD.

---

### 2.4. M — Среда (Medium / контекст потребления)

| Контекст | 4L | 1L | Δ |
|----------|----|----|---|
| **Retail-полка** | Основная полка масел; full drain | **Полка долива / top-up**; companion SKU | **Смена M_CONTEXT** |
| **Плотность выкладки** | ~4–6 facings (широкие канистры) | **~10–14 facings** (узкий профиль) | **↑ linear density** |
| **Дистанция считывания** | 1,5–3 m | 0,5–1,5 m (ближняя полка, рука) | **Ближний контакт** |
| **E-commerce thumbnail** | Mobil + Super/2000 + 10W-40 | Mobil + Super/2000 + 10W-40 ✅; **1L + QR + semi line 🟡**; gold graphic **✗** @120 px | **Robustness ≈ 4L** primary · **↓** secondary |
| **M_NOISE** | Medium-high category shelf | Меньший visual footprint → риск «потери» среди 4L silver blocks | **Anomaly:** David among Goliaths |
| **10W-40 legacy context** | ЮФО / aging fleet service | Тот же buyer; **меньше** service-jug reassurance | **Trust gap ↑** on doliv |

**POV — System Dynamics:**  
- *Potential:* высокая плотность → больше Mobil impressions на метр doliv-полки.  
- *Limit:* малый silhouette + **no handle** снижает service-authority vs 4L и vs domestic 1L peers с front API.

**Вывод (M):** 1L живёт в **doliv-нише** — импульс, companion SKU, import top-up. На основной полке 4L silver block **dominant**; 1L выигрывает только в **top-up-секции** через brand tower + magenta SAE band. E-commerce: brand + viscosity **pass** @120 px; volume, QR, fluid graphic — **fail**.

---

### 2.5. MAP — Мэппинги

| MAP (база 4L) | 1L | Статус |
|---------------|-----|--------|
| Fluid atomization → tribology film (MOCC_MS2_07) | Сохранён; droplets **усечены** | 🟡 **искажение span** — gestalt-completion ↑ |
| Numeric 2000 → line rank below 3000 | Константа | ✅ |
| SAE magenta band → viscosity monolith | Константа; **относительный масштаб ↑** | ✅ **усилен** |
| Semi label → chemistry honesty | Константа | ✅ |
| 4L → «полный цикл обслуживания» | **1L → «точечное пополнение»** | 🔄 **перекодировка MAP объёма** |
| 4L handle → service authority | **Absent** — portable module only | 🔄 **MAP carrier shift** |
| QR → digital trace | QR **rescaled**; CTA **н/д** без scan | 🟡 **partial/lacuna** |
| Grip-ridges → ? | **Новый MAP:** control/pour precision | ➕ **LATENT** — не интегрирован в label M_SYSTEM |
| API SN back → modern chemistry | Константа back-only | ✅ · **front lacuna persists** |

**POV — Logical Coherence:**  
- *Conflict:* gold fluid premium cue (DOMAIN_A) vs portable top-up C-geometry — **mild**, не блокирующий; shared with Super 3000 1L [13].  
- *Contradiction:* **none new** — semi honesty vs gold graphic **константа**.

**Вывод (MAP):** Ядро метафор (numeric tier + fluid kinetics + Mobil global brand) **масштабируется** без пересмотра M_SYSTEM. Искажаются: (1) gestalt gold droplets, (2) семантика объёма/handle, (3) QR без явного MAP. Тактильный MAP (grooves → control) **не связан** с визуальной системой этикетки.

---

### 2.6. EVAL — Оценка малого формата

| Метрика | 4L (база) | 1L (delta) | Δ |
|---------|-----------|------------|---|
| **Comprehensibility** | High (Super/2000/10W-40/semi) | **High** brand + SAE + semi; **low** API/OEM (back-only) | ↓ spec layer @ doliv |
| **Cognitive load** | Medium front / high back | **Bimodal:** medium front stack + **peak** footer cluster (QR+1L+graphic) | **↑ variance** |
| **Robustness (thumbnail)** | Medium-high | **Medium:** Mobil + 10W-40 OK; 1L/QR/droplets **fail** @120 px | ↓ |
| **Trust / institutional** | Medium (import + back OEM) | **Medium-low** on doliv — **no handle**, **no front spec**, import EN/TR | **↓ vs 4L** |
| **Engineering transparency** | Low-medium (semi front; API back) | **Low** — lacuna **↑** vs domestic 1L with API SG front [43][47] | **↓ competitive** |
| **Rhetorical efficiency** | 7/10 (semi honest, gold inflated) | **6/10** overall; **8/10** in top-up brand-filter context | context-dependent |

**POV — Relational States:** compromise между **единым Mobil brand-asset** (DRY) и **doliv-spec readability**; **anti-parity** с budget RU peers на front API row.

**Вывод (EVAL):** 1L **не ломает** primary value proposition (Mobil Super 2000 10W-40 semi). Ломается **secondary layer**: fluid graphic gestalt, multi-fuel footer, service-jug authority. **Critical gap vs LUKOIL/GPN Super 1L:** API SN+ **invisible on front** while peers show SG/CD — СТМ attack window **widens** on 1L row.

---

## 3. M_OCCURRENCE — только новые и изменённые

> Occurrences базы (MOCC_MS2_01–19, L01–L07, LAC01–07, NS01–03) без изменений **не дублируются**.

### 3.1. MOCC_MS2D_01 — Right-face grip grooves

**_min**
```yaml
M_OCC_ID: MOCC_MS2D_01
CASE_ID: COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA
MATERIAL_ID: mobil_super_2000_x1_10w40_1l_front_back_2022
SEGMENT_ID: carrier_body_right
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "right_face", grooves: 7 }
M_OCC_SURFACE_FORM: "7 horizontal recessed grip bars on right body face"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_ergonomics` → TARGET `dom_controlled_pour`; MAP `map_grip_as_precision`; DELIBERATENESS `deliberate`; FUNCTION [`affordance`, `format_signal`]; M_CONSTR link: MCON_MS2_07 (variant-by-format).

---

### 3.2. MOCC_MS2D_02 — Left-face horizontal indentations

**_min**
```yaml
M_OCC_ID: MOCC_MS2D_02
CASE_ID: COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA
MATERIAL_ID: mobil_super_2000_x1_10w40_1l_front_back_2022
SEGMENT_ID: carrier_body_left
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "left_face", indentations: 5 }
M_OCC_SURFACE_FORM: "5 horizontal molded indentations on left body face"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** Bilateral grip system complementing MOCC_MS2D_01; **substitutes** 4L integrated handle (MOCC_MS2_10 base); FUNCTION [`affordance`, `anti-slip`]; STATUS **MANIFEST**.

---

### 3.3. MOCC_MS2D_03 — 1L volume + SKU lock variant

**_min**
```yaml
M_OCC_ID: MOCC_MS2D_03
CASE_ID: COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA
MATERIAL_ID: mobil_super_2000_x1_10w40_1l_front_back_2022
SEGMENT_ID: label_footer_left
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "footer_left_cluster" }
M_OCC_SURFACE_FORM: "1L + QR + label code 819701B (base 4L: 819702A)"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_MS2_09 (variant-by-format)
```

**_full:** MAP `map_1L_as_topup_module` vs base `map_4L_as_service_cycle`; M_CONSTR: MCON_MS2_03 + MCON_MS2_06 (variant-by-format); barcode delta **433614** vs base **433607**.

---

### 3.4. MOCC_MS2D_04 — Vertical rescale layout

**_min**
```yaml
M_OCC_ID: MOCC_MS2D_04
CASE_ID: COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA
MATERIAL_ID: mobil_super_2000_x1_10w40_1l_front_back_2022
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", axis: "vertical" }
M_OCC_SURFACE_FORM: "4L Super 2000 layout vertically rescaled; footer cluster hyper-dense"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
```

**_full:** **K_PATTERN_VERTICAL_RESCALE** — Mobil family DRY norm [13][39]; FUNCTION [`format_adaptation`, `information_stacking`]; **inverts** partial MOCC_MS2_NS01 (dark field compress).

---

### 3.5. MOCC_MS2D_05 — Truncated gold fluid graphic

**_min**
```yaml
M_OCC_ID: MOCC_MS2D_05
CASE_ID: COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA
MATERIAL_ID: mobil_super_2000_x1_10w40_1l_front_back_2022
SEGMENT_ID: label_bottom_right
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "graphic_droplets_cropped_lateral" }
M_OCC_SURFACE_FORM: "Gold droplet spray from metallic ring, laterally cropped on narrow label"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: MOCC_MS2_07 (degraded)
```

**_full:** Gestalt fluid kinetics **incomplete**; MSYS_MS2_02 fidelity **↓** @ thumbnail; FUNCTION [`metaphor_degradation`]; **conflict** with semi honesty **unchanged** but **less visible**.

---

### 3.6. MOCC_MS2D_LAC01 — Service handle affordance absent

**_min**
```yaml
M_OCC_ID: MOCC_MS2D_LAC01
CASE_ID: COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA
MATERIAL_ID: mobil_super_2000_x1_10w40_1l_front_back_2022
SEGMENT_ID: carrier_body
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: absence
M_OCC_SPAN: { region: "expected_4L_handle_zone" }
M_OCC_SURFACE_FORM: "No integrated side handle (present on 4L base MOCC_MS2_10)"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LACUNA
```

**_full:** **Усиление** service-authority gap on doliv format; domestic budget 1L peers also **handleless** — **parity** on C; **Mobil import** loses **both** handle **and** front API vs GPN/LUKOIL.

---

### 3.7. MOCC_MS2D_LAC02 — Dark breathing zone partial compress

**_min**
```yaml
M_OCC_ID: MOCC_MS2D_LAC02
CASE_ID: COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA
MATERIAL_ID: mobil_super_2000_x1_10w40_1l_front_back_2022
SEGMENT_ID: label_upper_core
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "MOCC_MS2_NS01_zone" }
M_OCC_SURFACE_FORM: "Typography-dominant dark void behind Super/2000 partially compressed"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: NEGATIVE_SPACE
BASE_REF: MOCC_MS2_NS01 (modified)
```

**_full:** Brand isolation **↓** vs 4L; Super/2000 stack **denser** — **↑** vertical brand tower effect.

---

## 4. Выводы для СТМ

### 4.1. Где дизайн Mobil «ломается» на 1L

1. **Footer cluster** — QR + 1L + code + Gasoline&Diesel + cropped graphic без иерархического разделения; cognitive load **пиковый** в нижней трети.
2. **Gestalt fluid graphic** — gold droplets **усечены**; MSYS_MS2_02 **under-delivered** @ thumbnail и @ 2m.
3. **Service authority** — потеря 4L handle + import EN/TR + **no front API** = **triple trust deficit** на doliv vs LUKOIL/GPN Super 1L [43][47].
4. **API front lacuna** — **усиливается** на 1L: domestic peers front-load SG/CD; Mobil SN+ **only back** — buyer долива **не видит** modern chemistry edge.
5. **QR** — rescaled from 4L; **no visible CTA** — half-integrated digital trace.

### 4.2. Лакуны базового формата: усиление / ослабление

| Лакуна (база) | На 1L |
|---------------|-------|
| MOCC_MS2_LAC01 (API/ACEA off-front) | **Усилена** vs domestic 1L peers |
| MOCC_MS2_LAC02 (Cyrillic) | **Константа** |
| MOCC_MS2_LAC03 (official RF supply) | **Константа** |
| MOCC_MS2_LAC04 (x1 explanation) | **Константа** |
| MOCC_MS2_LAC07 (domestic OEM front) | **Константа** — AVTOVAZ back-only |
| Service handle (4L-only) | **Новая LACUNA** MOCC_MS2D_LAC01 |
| Fluid graphic gestalt | **Деградация** MOCC_MS2D_05 |

### 4.3. Импликации для ODSA-матрицы

- **Разделять строки 4L и 1L** — правило «1 format = 1 row» ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)).
- **Format Robustness Index @120 px:** Mobil Super 2000 1L — brand ✅ · 10W-40 ✅ · semi 🟡 · 1L ✗ · API ✗ · OEM ✗.
- **Top-up Shelf Fit:** physical grip layer **strong**; claim layer **weak** vs LUKOIL/GPN Super 1L.
- **Attack vector для СТМ Classic/Protect 1L:** front row **API SN/CF + ACEA A3/B3** + **2–3 OEM** (Avtovaz + import) + Cyrillic — **anti-pattern** Mobil DRY rescale without spec front-load.
- **Attack vector «doliv trust»:** named semi tech + **one** benefit claim + visible 1L — не копировать gold-fluid void + numeric 2000 hyperbole.

**POV — System Dynamics:** Mobil демонстрирует **DRY-брендинг** Super line как family default; lacuna API front **не закрывается** на 1L — окно для СТМ **расширяется** относительно budget RU peers.

---

## 5. POV-сводка (обязательная маркировка)

| Маркер | Фиксация |
|--------|----------|
| **Information Integrity** | Lacuna: API/OEM front, handle, QR-CTA; Redundancy: Super+2000+x1+semi+Gasoline&Diesel; Contamination: gold fluid polisemy **константа** |
| **Logical Coherence** | Conflict: gold premium graphic vs semi label **константа**; portable C vs service metaphor **mild** |
| **System Dynamics** | Potential: doliv shelf density, brand tower; Limit: thumbnail robustness, trust vs domestic 1L; Anomaly: batch 2022 newer than 4L base 2021 |
| **Relational States** | Parity: M_SYSTEM между форматами; Compromise: DRY brand vs doliv spec readability; **Anti-parity** vs LUKOIL/GPN 1L on front API |

---

## 6. Таблица «4L vs 1L» — для матрицы конкурентов (ODSA)

| # | Параметр ODSA | 4L (база) | 1L (delta) | Δ для матрицы |
|---|---------------|-----------|------------|---------------|
| 1 | M_SYSTEM | MSYS_MS2_01–04 down-tier fluid kinetics | **константа** | = |
| 2 | Carrier morphology | Wide jug + integrated handle | Narrow bottle + grip-ridges | **разные строки** |
| 3 | Label strategy | Full design | Vertical rescale (DRY) | compress |
| 4 | Negative space | Dark upper field (NS01) | Partial compress (MS2D_LAC02) | ↓ breathing |
| 5 | SAE 10W-40 legibility | High (magenta band) | High (rel. ↑) | = / ↑ |
| 6 | Semi-synthetic claim | Front explicit | Front explicit | = |
| 7 | Volume marker | 4L + QR + 819702A | 1L + QR + 819701B | **semantic shift** |
| 8 | Gold fluid graphic | Full gestalt | Laterally cropped (MS2D_05) | ↓ |
| 9 | API facing | **Back SN+** only | **Back SN+** only | = · **↓ vs peers** |
| 10 | OEM facing | Back MB/VW/Avtovaz | Back MB/VW/Avtovaz | = |
| 11 | Cyrillic / RU supply | Absent | Absent | = |
| 12 | Retail context | Main shelf | Top-up shelf | **context split** |
| 13 | Facings density | Low–medium | **High** | ↑ |
| 14 | Thumbnail robustness | Medium-high | Medium | ↓ |
| 15 | STM attack on 1L | — | Front API+OEM + clean doliv layout | **opportunity ↑** |

---

## 7. Issues for discussion

1. **Batch delta:** 1L batch **2022** vs 4L base **2021** — считать ли delta чисто format-driven или смешанным с label-rev drift?
2. **API SN front on 1L:** достаточно ли back-only для import buyer на doliv-полке или СТМ должен **front-load** как primary differentiation vs Mobil **and** LUKOIL/GPN?
3. **Symmetric ODSA:** запустить `stm-odsa` для Mobil Super 2000 1L (отдельный прогон) — cross-face audit + doliv gap?
4. **Peer matrix row:** добавить Mobil Super 2000 **1L delta** в [08_PGMM_упаковка.md](08_PGMM_упаковка.md) Wave 3 table рядом с LUKOIL/GPN 1L delta?
5. **Site triangulation:** EX-Mobil-Super-2000 в [04](04_источники_и_URL.md) — verify 1L/4L SKU parity on mobil.com.
6. **QR destination:** scan 819701B batch QR — закрыть MAP lacuna MOCC_MS2D_03?

---

## 8. Связи

- База 4L: [50_PGMM_mobil_super_2000_x1_10w_40.md](50_PGMM_mobil_super_2000_x1_10w_40.md)
- Mobil Super family delta: [13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md)
- Peer budget 10W-40 delta: [43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md) · [47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md](47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)

---

*Delta-отчёт · CASE `COMP_MOBIL_SUPER2000_X1_10W40_1L_DELTA` · skill stm-pgmm-delta · ingest 25.06.2026*
