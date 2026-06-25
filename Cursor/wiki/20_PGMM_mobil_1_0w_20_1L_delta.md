# PGMM Delta: Mobil 1 0W-20 — 1L vs 5L

**Дата анализа:** 25.06.2026  
**Тип отчёта:** packaging_visual_metaphor_delta (не full PGMM)  
**Базовый кейс:** [19_PGMM_mobil_1_0w_20_5L.md](19_PGMM_mobil_1_0w_20_5L.md) (5L)  
**Артефакт:** Mobil 1 SAE 0W-20, 1L — фронтальная этикетка + носитель  
**Методология:** PGMM (Приложение E) + neuromarketing-system-instructions  
**Primary domains (1–23):** D4 Packaging/Carrier · D8 Visual Semiotics · D12 Cognitive Load · D15 Shelf/Retail Context

**Контекст DR-B:** 0W-20 — SAE-фронтир ([03](03_DR-B_вязкости_SAE.md)); **не смешивать** с матрицей 5W-40 mass-mid ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)).

---

## 0. CASE_min

| Поле | Значение |
|------|----------|
| **CASE_ID** | `COMP_MOBIL_1_0W20_1L_DELTA` |
| **CASE_TYPE** | `packaging_visual_metaphor_delta` |
| **BASE_CASE_REF** | `Cursor/wiki/19_PGMM_mobil_1_0w_20_5L.md` |
| **FORMAT** | 1L (delta vs 5L) |
| **MATERIAL_ID** | `mobil_1_0w_20_1l_front_2026` |
| **SEGMENT_ID** | `label_front_primary` |

---

## 1. Наследование из базы (без дублирования)

### 1.1. M_SYSTEM — **константа**

- **MSYS_M1_01** — Bio-Lattice Hyper-Performance  
- **MSYS_M1_02** — Institutional OEM Sovereignty  
- **MSYS_M1_03** — Eco-Modern Gateway  

См. [19_PGMM… §4](19_PGMM_mobil_1_0w_20_5L.md). Конфликт MSYS_M1_01 ↔ MSYS_M1_03 (solid lattice vs eco-modern без eco-визуала) **не разрешается** на 1L — сохраняется.

### 1.2. DOMAIN_A / DOMAIN_B — **константа**

- **DOMAIN_A:** biomimetic lattice, aerospace honeycomb, modern powertrain ecology  
- **DOMAIN_B:** low-viscosity full-synthetic tribology, hybrid/Atkinson-cycle engines  

См. [19_PGMM… §5](19_PGMM_mobil_1_0w_20_5L.md).

### 1.3. M_CONSTRUCTION — variant-by-format

| ID (база) | Статус на 1L |
|-----------|--------------|
| MCON_M1_01 Lattice Performance Shield | 🟡 honeycomb **усечён** по боковым краям; gestalt lattice ↓ |
| MCON_M1_02 Modernity Claim Stack | 🟡 **vertical compress:** 4 строки claims в узкой колонке |
| MCON_M1_03 Numeric Brand Monolith | ✅ «1» + 0W-20 сохранены; **относительный масштаб ↑** к ширине |
| MCON_M1_04 OEM Authority Front | 🟡 dexos1 **↓** ниже порога thumbnail (~120 px) |
| MCON_M1_05 Hybrid Frontier Badge | 🟡 иконка plug-car **↓**; текст «HYBRIDS» читается только близко |
| MCON_M1_06 Premium Whitespace Frame | 🔻 **деградация:** верхняя светло-серая полоса (MOCC_M1_NS01) **сжата** |
| MCON_M1_07 Solid-over-Fluid Norm | ✅ лакуна fluid-визуала **константа** |

**POV — Relational States:** parity метафорической системы между форматами; **compromise** — premium whitespace (ключевой дифференциатор Mobil 1 vs Super 3000) **жертвуется** ради DRY-масштабирования макета.

---

## 2. Delta по блокам

### 2.1. C — Носитель (Carrier)

| Параметр | 5L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Геометрия** | Широкий 5L-jug, integrated handle | Узкая вертикальная бутылка; concave правая грань к горловине | **Смена морфологии:** service jug → top-up bottle |
| **Ручка** | Интегрированная ручка 5L | **Нет ручки**; 7+ горизонтальных grip-ridges на правой грани | **Новый affordance:** одноручный захват vs переноска объёмом |
| **Material** | Metallic silver HDPE + grip ridges | Идентично | Константа |
| **Пропорции H:W** | Низкий, широкое основание, низкий CG | Высокий «towering» силуэт, узкая база | **DoF:** сжатие по ширине, растяжение по высоте |
| **Cap** | Крупная серая ribbed cap (прокси) | Ribbed screw cap, пропорционально меньше | Константа семантики |
| **Стабильность** | Широкая база | Узкая база, **↑ CG** | **Limit:** риск опрокидывания на top-up-полке |

**Вывод (C):** 1L — не downscale 5L-jug, а **перекодировка carrier-code**: с «premium service container» на «portable top-up module». Silver metallic + grip-ridges сохраняют семейство Mobil-silver ([19](19_PGMM_mobil_1_0w_20_5L.md), [12](12_PGMM_mobil_super_3000_x1_5w_40.md)), но **institutional mass-retail authority** 5L-jug **ослаблена**.

---

### 2.2. K — Композиция (Layout)

| Параметр | 5L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Стратегия макета** | Asymmetric Z-layout; ~25% premium whitespace сверху (MOCC_M1_NS01) | **Vertical rescale** 5L-макета на узкую этикетку | **K_PATTERN_VERTICAL_RESCALE** |
| **Negative space** | Deliberate premium breathing room (~25% label height) | Верх **сжат**; нижняя треть — кластер dexos1 + hybrid + 1L + QR + regional codes | MOCC_M1_NS01 **деградирован** |
| **Иерархия** | Brand → «1» → black bar → claims → 0W-20 → footer | Идентичная последовательность | Константа порядка |
| **Читаемость 0W-20** | Oversized, high-contrast на honeycomb | Сохранена; **относительный размер ↑** к ширине | **Усилена** |
| **Читаемость объёма** | «5L» — full service cycle | «1L» — top-up / partial fill | **Semantic shift** |
| **Regional micro-text** | **н/д** на базе 5L | «UA \| TR \| ISR \| AR» в footer | **Новый K-noise** |
| **QR** | MOCC_M1_12 latent | QR + red arrow icon, footer-right | Константа элемента; **↓** читаемость |
| **Honeycomb zone** | Полный hex mesh справа | **Lateral crop** по краям этикетки | Gestalt lattice **неполный** |

**POV — Information Integrity:**  
- *Redundancy:* claim-stack (4 performance lines) без дифференциации — **усиливается** при сжатии.  
- *Contamination:* regional codes добавляют **export-channel** шум без RU-localization.  
- *Lacuna:* premium whitespace — **ослабление** deliberate premium cue.

**Вывод (K):** Mobil 1 на 1L **не пересобирает** premium-layout, а **масштабирует** 5L asset. Главная потеря — **MCON_M1_06 Premium Whitespace Frame**: то, что отличало Mobil 1 от «gravitational compression» Super 3000 ([19 §7 K7](19_PGMM_mobil_1_0w_20_5L.md)), на 1L **частично схлопывается**. Primary scan path (logo → «1» → 0W-20) **robust**; footer institutional layer — **деградирует**.

---

### 2.3. S — Сигнальные паттерны

| Статус | Паттерн | Комментарий |
|--------|---------|-------------|
| ✅ **Сохранён** | Mobil blue-red wordmark + black square «1» | Межформатный invariant ([19 MOCC_M1_01–02](19_PGMM_mobil_1_0w_20_5L.md)) |
| ✅ **Сохранён** | Black bar «TOP PERFORMANCE FOR MODERN ENGINES» | High-contrast anchor |
| ✅ **Сохранён** | Honeycomb / hex mesh (MOCC_M1_08) | Усечён, но узнаваем |
| ✅ **Сохранён** | «0W-20» oversized white on dark mesh | **Robust** primary heuristic |
| 🟡 **Усилен** | Vertical brand monolith stack | «Башня» flagship на узком носителе |
| 🔻 **Деградировал** | Premium whitespace (MOCC_M1_NS01) | Premium calm ↓ |
| 🔻 **Деградировал** | dexos1 GEN 3 badge (MOCC_M1_09) | Below thumbnail threshold |
| 🔻 **Деградировал** | Hybrid plug-car badge (MOCC_M1_10) | Icon ↓; текст — только близко |
| 🔻 **Деградировал** | Claim stack lines 2–4 (protection / synthetic / fuel economy) | Merge в visual block |
| ➕ **Новый** | Regional origin codes UA\|TR\|ISR\|AR | Export routing; **не** RU supply signal |
| ➕ **Новый** | Grip-ridges (тактильный S на C) | Top-up affordance |

**Вывод (S):** Flagship primary signals (brand monolith + 0W-20 + honeycomb silhouette) **survive** downscale. **Institutional + eco-modern secondary layer** (dexos1, hybrid, whitespace) **фильтруется** на дистанции и в e-commerce thumbnail. Regional codes — **новый low-trust noise** для RU-buyer без кириллицы.

---

### 2.4. M — Среда (Medium / контекст потребления)

| Контекст | 5L | 1L | Δ |
|----------|----|----|---|
| **Retail-полка** | Основная полка; full change / service | **Top-up / companion**; касса, аксессуары, импульс | **Смена M_CONTEXT** |
| **Плотность выкладки** | ~3–5 facings (широкие jugs) | **~10–14 facings** (узкий профиль) | **↑ linear density** |
| **Дистанция считывания** | 1,2–2,5 m (premium shelf) | 0,5–1,2 m (рука потребителя) | **Ближний контакт** |
| **E-commerce thumbnail** | «1» + 0W-20 + honeycomb — три якоря | Brand + 0W-20 ✅; dexos1 / hybrid / 1L **✗** @120 px | **Robustness ↓** footer |
| **0W-20 segment context** | Hybrid/modern SAE buyer ([03](03_DR-B_вязкости_SAE.md)) | Тот же buyer; **меньше** institutional reassurance на лице | **Trust gap ↑** на import 1L |
| **M_NOISE** | Medium (whitespace снижает internal noise) | Whitespace ↓ + regional micro-text ↑ | **Internal noise ↑** |

**POV — System Dynamics:**  
- *Potential:* 0W-20 growth + China/hybrid park — 1L как **entry SKU** для trial/top-up.  
- *Limit:* import-facing + EN-only + малый footer = **anxiety ↑** vs 5L service jug.  
- *Anomaly:* dexos1 on front **сохранён**, но **не читается** — paradox of presence without perception.

**Вывод (M):** 1L живёт в **другой retail-нише**, но Mobil **не адаптирует** claim-layer под top-up (нет «top-up safe» / «exact fill» rationale). Для 0W-20 СТМ: 1L — **канал первого контакта** с сегментом; упаковка должна компенсировать **import anxiety** кириллицей и official supply, которых у Mobil 1L **нет**.

---

### 2.5. MAP — Мэппинги

| MAP (база 5L) | 1L | Статус |
|---------------|-----|--------|
| Lattice → molecular integrity (MOCC_M1_08, L01) | Honeycomb cropped | 🟡 **span ↓** — gestalt-completion load ↑ |
| Claim stack → modern/hybrid tribology (MCON_M1_02) | 4 lines compressed | 🟡 fidelity **medium → medium-low** |
| «1» monolith → flagship tier (MOCC_M1_02) | Константа; rel. scale ↑ | ✅ **усилен** |
| 0W-20 → SAE heuristic (MOCC_M1_07) | Константа | ✅ |
| 5L → full service cycle | **1L → top-up module** | 🔄 **перекодировка объёма** |
| dexos1 → institutional trust (MSYS_M1_02) | Present but **unreadable** small | ⚠️ **MAP present / perception absent** |
| Hybrid badge → eco-modern gateway (MSYS_M1_03) | Icon ↓ | 🟡 **latent only** at shelf distance |
| QR → traceability (MOCC_M1_12) | Present; CTA **н/д** | ⚠️ **LACUNA MAP** (как Super 3000 1L, [13](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md)) |
| Regional codes → export routing | **Новый MAP:** multi-market SKU | ➕ **не** RU localization |
| Grip-ridges → controlled pour | **Новый MAP** (tactile) | ➕ LATENT; не интегрирован в label |

**POV — Logical Coherence:**  
- *Conflict:* Premium flagship M_SYSTEM (whitespace + lattice calm) vs **compressed** 1L layout — ** mild brand dilution**, не блокирующий.  
- *Contradiction:* «ULTIMATE PROTECTION» + top-up 1L volume — rhetorically compatible, но **service semantics** расходятся.

**Вывод (MAP):** Ядро Bio-Lattice Hyper-Performance **масштабируется**. Искажаются: (1) honeycomb gestalt, (2) premium whitespace MAP, (3) institutional OEM perception, (4) volume semantics. QR и regional codes **не закрывают** LAC04 (Cyrillic) и LAC06 (anti-fraud) из базы.

---

### 2.6. EVAL — Оценка малого формата

| Метрика | 5L (база) | 1L (delta) | Δ |
|---------|-----------|------------|---|
| **Comprehensibility** | High (premium clean layout) | **High** brand + 0W-20; **low** dexos1/hybrid/API | ↓ institutional layer |
| **Cognitive load** | Medium-low (база EVAL) | **Bimodal:** верх clean / **низ — peak cluster** | **↑ variance** |
| **Robustness (thumbnail)** | High | **Medium:** «1» + 0W-20 OK; honeycomb partial; footer **fail** | ↓ |
| **Premium perception** | High (whitespace + flagship) | **Medium-high** — whitespace loss | ↓ |
| **RU localization** | Low (база) | **Lower** — regional codes без кириллицы | ↓ |
| **Transaction speed (0W-20 buyer)** | High | **High** @ close range; **medium** @ shelf 2m | context-dependent |
| **Trust / institutional** | Medium-high (dexos1 front) | **Medium-low** — badge present, unreadable | ↓ |

**POV — Relational States:** compromise между **global DRY brand asset** и **premium whitespace promise**; parity M_SYSTEM при **loss of premium carrier morphology**.

**Вывод (EVAL):** 1L **не ломает** primary 0W-20 value proposition (flagship «1» + viscosity). Ломается **premium differentiation** vs Super 3000 и **institutional footer**. Для ODSA/матрицы 0W-20: **1L и 5L — раздельные строки**; усреднение cognitive load **некорректно**.

---

## 3. M_OCCURRENCE — только новые и изменённые

> Occurrences базы (MOCC_M1_01–13, L01–L05, LAC01–06, NS01–02) без изменений **не дублируются**.

### 3.1. MOCC_M1D_01 — Volume 1L (variant MOCC_M1_11)

**_min**
```yaml
M_OCC_ID: MOCC_M1D_01
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: label_footer_right
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "footer_right_white_on_dark" }
M_OCC_SURFACE_FORM: "1L"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
BASE_REF: MOCC_M1_11 (5L → 1L)
```

**_full:** MAP `5L_service_cycle → 1L_topup_module`; M_CONSTR: MCON_M1_03 variant-by-format.

---

### 3.2. MOCC_M1D_02 — Regional market routing codes

**_min**
```yaml
M_OCC_ID: MOCC_M1D_02
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: label_footer_micro
M_OCC_MODALITY_CLASS: visual_text
M_OCC_REP_LEVEL: indexical
M_OCC_SPAN: { region: "footer_bottom", text: "UA | TR | ISR | AR" }
M_OCC_SURFACE_FORM: "Pipe-separated regional market codes"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_export_routing` → TARGET `dom_multi_market_SKU`; **не** MAP на RU official supply; **усиливает** LAC04. FUNCTION [`channel_signal`, `noise`]; **новый** vs база 5L (н/д на фронте 5L).

---

### 3.3. MOCC_M1D_03 — Grip grooves without handle

**_min**
```yaml
M_OCC_ID: MOCC_M1D_03
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: carrier_body_right
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "right_face", grooves: "horizontal_recessed_bars" }
M_OCC_SURFACE_FORM: "Horizontal grip ridges on right body; no integrated handle"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_ergonomics` → TARGET `dom_controlled_pour`; MAP `grip_as_topup_control`; contrast vs 5L integrated handle ([19 §7 C2](19_PGMM_mobil_1_0w_20_5L.md)).

---

### 3.4. MOCC_M1D_04 — Narrow top-up bottle morphology

**_min**
```yaml
M_OCC_ID: MOCC_M1D_04
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: carrier_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_bottle_silhouette" }
M_OCC_SURFACE_FORM: "Tall narrow bottle; concave right flank; high CG vs 5L jug"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** **Carrier-code shift** from service jug to portable module; FUNCTION [`format_signal`, `channel_topup`].

---

### 3.5. MOCC_M1D_05 — Truncated honeycomb lattice (delta MOCC_M1_08)

**_min**
```yaml
M_OCC_ID: MOCC_M1D_05
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: label_core_right
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "honeycomb_zone_lateral_crop" }
M_OCC_SURFACE_FORM: "Hex mesh cropped at label lateral edges"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: MOCC_M1_08 (degraded)
```

**_full:** Gestalt lattice **incomplete**; MCON_M1_01 span ↓; thumbnail: honeycomb **partial read**.

---

### 3.6. MOCC_M1D_06 — Premium whitespace compression (delta MOCC_M1_NS01)

**_min**
```yaml
M_OCC_ID: MOCC_M1D_06
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: label_upper_band
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "upper_light_grey", height_pct: "<15% vs ~25% base" }
M_OCC_SURFACE_FORM: "Compressed light-grey breathing band above wordmark"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: NEGATIVE_SPACE
BASE_REF: MOCC_M1_NS01 (degraded)
```

**_full:** MCON_M1_06 **partial failure** on 1L; premium calm ↓ vs 5L and vs Super 3000 compression norm.

---

### 3.7. MOCC_M1D_07 — Vertical label rescale pattern

**_min**
```yaml
M_OCC_ID: MOCC_M1D_07
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", axis: "vertical" }
M_OCC_SURFACE_FORM: "5L front layout vertically rescaled to narrow 1L label"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
```

**_full:** DRY brand asset strategy; FUNCTION [`format_adaptation`]; anti-pattern reference for СТМ 0W-20 1L brief.

---

### 3.8. MOCC_M1D_LAC01 — Institutional footer below perception threshold

**_min**
```yaml
M_OCC_ID: MOCC_M1D_LAC01
CASE_ID: COMP_MOBIL_1_0W20_1L_DELTA
MATERIAL_ID: mobil_1_0w_20_1l_front_2026
SEGMENT_ID: label_footer
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: absence_of_effect
M_OCC_SPAN: { region: "dexos1_hybrid_zone", threshold: "~120px_thumbnail" }
M_OCC_SURFACE_FORM: "dexos1 + hybrid badge present physically but fail shelf/thumbnail read"
M_OCC_STATUS_CLASS: inferred
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: LACUNA
```

**_full:** **Paradox:** MOCC_M1_09–10 MANIFEST on pack, **LATENT** in medium; MSYS_M1_02–03 **under-delivered** on 1L.

---

## 4. Выводы для СТМ

### 4.1. Где дизайн Mobil 1 «ломается» на 1L

1. **Premium whitespace (MCON_M1_06)** — ключевой дифференциатор Mobil 1 vs Super 3000 **схлопывается**; flagship calm → compressed flagship.
2. **Footer institutional layer** — dexos1 + hybrid **физически есть**, perceptually **отсутствуют** @ thumbnail / 2 m.
3. **Honeycomb gestalt** — lattice metaphor **усечён**; Bio-Lattice system **ослаблен** без пересборки.
4. **Claim stack (4 lines)** — semantic redundancy **↑** при сжатии; нет single-hero claim для top-up.
5. **Carrier morphology** — потеря 5L-jug authority; 1L не несёт «service container» code.
6. **RU channel** — regional export codes **вместо** кириллицы/official supply; **усиливает** LAC04 базы.

### 4.2. Лакуны базового формата: усиление / ослабление

| Лакуна (база 5L) | На 1L |
|------------------|-------|
| MOCC_M1_LAC01 (fluid visualization) | **Константа** |
| MOCC_M1_LAC02 (API SP front) | **Константа** |
| MOCC_M1_LAC04 (Cyrillic / RU supply) | **Усилена** — export codes без RU |
| MOCC_M1_LAC06 (anti-fraud explicit) | **Константа** — QR без CTA |
| Premium whitespace (NS01) | **Усилена деградация** — MOCC_M1D_06 |
| Institutional trust (dexos1 front) | **Paradox lacuna** — MOCC_M1D_LAC01 |

### 4.3. Импликации для ODSA-матрицы (0W-20 ветка)

- **Раздельные строки 5L и 1L** для Mobil 1 0W-20 (правило: 1 format = 1 row).
- **Format Robustness @120 px:** brand ✅ · 0W-20 ✅ · honeycomb 🟡 · dexos1 ✗ · hybrid ✗ · 1L ✗.
- **Top-up Shelf Fit:** grip-ridges + narrow profile ✅; claim layer ✗.
- **Attack vector СТМ 0W-20 1L:** **не** rescale 5L/premium layout; **single hero** (0W-20 + hybrid-ready) + **Cyrillic OEM row** + **official supply** + **explicit QR MAP**; whitespace **сохранить** even on 1L.
- **Cross-ref mass-mid:** паттерн DRY-rescale совпадает с Mobil Super 3000 1L ([13](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md)) — industry default, **не** premium exception.

**POV — System Dynamics:** Mobil 1 0W-20 на 1L **сохраняет** SAE-heuristic и flagship monolith, но **не закрывает** RU/import lacunae базы — окно для СТМ **расширяется** на top-up канале.

---

## 5. POV-сводка (обязательная маркировка)

| Маркер | Фиксация |
|--------|----------|
| **Information Integrity** | Lacuna: institutional footer perception, RU supply, API front; Redundancy: 4-line claim stack; Contamination: export regional codes vs RU buyer |
| **Logical Coherence** | Conflict: premium whitespace promise vs compressed 1L; mild, не блокирующий |
| **System Dynamics** | Potential: 0W-20 entry SKU, shelf density; Limit: thumbnail footer fail, CG stability; Anomaly: dexos1 present/unread |
| **Relational States** | Parity: M_SYSTEM; Compromise: DRY asset vs premium whitespace + institutional delivery |

---

## 6. Таблица «5L vs 1L» — для матрицы конкурентов (ODSA)

| # | Параметр | 5L (база) | 1L (delta) | Δ для матрицы |
|---|----------|-----------|------------|---------------|
| 1 | M_SYSTEM | Bio-Lattice + OEM + Eco-Modern | **константа** | = |
| 2 | Carrier morphology | 5L jug + handle | Narrow bottle + grip-ridges | **разные строки** |
| 3 | Label strategy | Premium asymmetric Z | Vertical rescale 5L asset | compress |
| 4 | Premium whitespace | ~25% upper band | **<15%** compressed | ↓ flagship cue |
| 5 | 0W-20 legibility | High (oversized) | High (rel. ↑) | = / ↑ |
| 6 | Volume marker | 5L service cycle | 1L top-up | **semantic shift** |
| 7 | Honeycomb lattice | Full gestalt | Lateral crop | ↓ |
| 8 | dexos1 GEN3 front | Readable @ shelf | Present, **unreadable** small | ↓ trust delivery |
| 9 | Hybrid badge | Secondary readable | Icon-only @ distance | ↓ |
| 10 | Claim stack | 4 lines, medium-low load | 4 lines, **peak load** bottom | ↑ redundancy |
| 11 | QR / digital | Latent | Present, no CTA | partial |
| 12 | RU localization | Low (EN import) | **Lower** + export codes | ↓ |
| 13 | Retail context | Main / service shelf | Top-up / companion | **context split** |
| 14 | Thumbnail robustness | High | Medium (footer fail) | ↓ |
| 15 | STM 0W-20 1L attack | — | Whitespace + Cyrillic OEM + hero claim + QR MAP | **opportunity** |

---

## 7. Issues for discussion

1. **Premium on 1L:** обязан ли flagship whitespace **сохраняться** на top-up или допустим industry DRY-rescale?
2. **dexos1 paradox:** считать ли OEM-on-front «delivered» на 1L, если badge **не проходит** thumbnail test?
3. **Regional codes UA|TR|ISR|AR:** variant для export batch или стандарт импортного 1L в РФ?
4. **Матрица 0W-20:** включать ли Mobil 1 1L как отдельную строку рядом с 5L ([19](19_PGMM_mobil_1_0w_20_5L.md)) или достаточно delta-reference?
5. **Symmetric delta:** нужен ли Mobil 1 **4L** delta для полноты 0W-20 line ([05](05_линейка_SKU_СТМ.md) рекомендует 4L+1L)?
6. **ODSA pass:** запускать ли `stm-odsa` на 1L отдельно (back label / RU overlay **н/д** на этом фото)?

---

## 8. Связи

- База full: [19_PGMM_mobil_1_0w_20_5L.md](19_PGMM_mobil_1_0w_20_5L.md)
- Аналог delta (mass-mid): [13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md)
- SAE / SKU: [03](03_DR-B_вязкости_SAE.md), [05](05_линейка_SKU_СТМ.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Next: `stm-odsa` (1L claims) · `stm-pgmm-delta` (Mobil 1 4L, если образец)

---

*Delta-отчёт · CASE `COMP_MOBIL_1_0W20_1L_DELTA` · ingest 25.06.2026 · skill stm-pgmm-delta*
