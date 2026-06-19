# PGMM Delta: Gazpromneft Premium N 5W-40 — 1L vs 4L

**Дата анализа:** 19 июня 2026 г.  
**Тип отчёта:** packaging_visual_metaphor_delta (не full PGMM)  
**Базовый кейс:** [11_PGMM_Gazpromneft_Premium_N_5W-40.md](11_PGMM_Gazpromneft_Premium_N_5W-40.md) (4L)  
**Артефакт:** Gazpromneft Premium N SAE 5W-40, 1L — фронтальная этикетка + носитель  
**Методология:** PGMM (Приложение E) + neuromarketing-system-instructions  
**Primary domains (1–23):** D4 Packaging/Carrier · D8 Visual Semiotics · D12 Cognitive Load · D15 Shelf/Retail Context

---

## 0. CASE_min

| Поле | Значение |
|------|----------|
| **CASE_ID** | `COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA` |
| **CASE_TYPE** | `packaging_visual_metaphor_delta` |
| **BASE_CASE_REF** | `Cursor/wiki/11_PGMM_Gazpromneft_Premium_N_5W-40.md` |
| **FORMAT** | 1L (delta vs 4L) |
| **MATERIAL_ID** | `gazpromneft_premium_n_5w40_1l_front_2026` |
| **SEGMENT_ID** | `label_front_primary` |

---

## 1. Наследование из базы (без дублирования)

### 1.1. M_SYSTEM — **константа**

1. `M_SYSTEM_GPN_01_COGNITIVE_AMORTIZATION` (Когнитивная амортизация)  
2. `M_SYSTEM_GPN_02_INSTITUTIONAL_ANXIETY` (Институциональная тревога)  
3. *Lacunar System:* информационная асимметрия («Чёрный ящик») — без пересборки.

См. [§3 базового отчёта](11_PGMM_Gazpromneft_Premium_N_5W-40.md).

### 1.2. DOMAIN_A / DOMAIN_B — **константа**

- **DOMAIN_B (трибология):** базовое HC-синтетическое моторное масло — **визуально вытеснено** (константа).  
- **DOMAIN_A (бленд):** индустриальная термокинетика (горячее/холодное, броня) + социальная гегемония (власть монополии, западная лексика) — без пересборки.

См. [§2 базового отчёта](11_PGMM_Gazpromneft_Premium_N_5W-40.md).

### 1.3. M_CONSTRUCTION — variant-by-format

| ID (база) | Статус на 1L |
|-----------|--------------|
| `MCON_GPN_01` Когнитивная амортизация (гипербола 5W-40 + пустые «Premium/Synthetic») | ✅ сохранён; 5W-40 **↑ относительный масштаб** к ширине этикетки |
| `MCON_GPN_02` Институциональная тревога (логотип Газпромнефти в зените) | ✅ сохранён; корпоративный якорь **robust** в thumbnail |
| `MCON_GPN_03` Металлическая мимикрия (`PATTERN_C_METALLIC_MIMICRY`) | ✅ константа; серебристый HDPE + рёбра жёсткости |
| `MCON_GPN_04` Обфускация допусков (OEM в подвале, нечитаемый шрифт) | 🔻 **variant-by-format:** подвал **ещё плотнее**; допуски MB/VW/Renault **ниже порога** |
| `MCON_GPN_05` Абстрактные термо-свуши (3D fluid graphics) | 🟡 **variant-by-format:** свуши **усечены** по боковым краям узкой этикетки |
| `MCON_GPN_06` Клаустрофобная плотность (`Claustrophobic Density`) | 🟡 **variant-by-format:** **равномерно высокая** по всей вертикали; negative space **≈ 0** |
| `MCON_GPN_07` Z-паттерн / split-complementary (оранжевое ядро vs сине-серебро) | ✅ сохранён; оранжевый блок 5W-40 — финальный якорь Z-маршрута |

**POV — Relational States:** parity метафорической системы между форматами; compromise — единый brand-asset (DRY-rescale) vs физика «бутылки долива» и **критическая** деградация инженерного слоя.

---

## 2. Delta по блокам

### 2.1. C — Носитель (Carrier)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Геометрия** | Широкая асимметричная канистра; агрессивные рёбра жёсткости (`PATTERN_C_METALLIC_MIMICRY`) | Узкая вертикальная «бутылка»; левая грань — плавная кривая (S-contour), правая — concave к горловине | **Смена морфологии:** сосуд замены → модуль долива |
| **Ручка** | Интегрированная боковая/верхняя ручка 4L-формата | **Нет отдельной ручки**; вдавленная боковая зона захвата с **3 диагональными рельефными канавками** на плече и **3 зеркальными** у основания | **Новый affordance:** одноручный захват vs переноска объёмом |
| **Материал** | Серебристый полимер (HDPE), matte metallic finish | Идентично | Константа |
| **Пропорции H:W** | Низкий, устойчивый, широкое основание | Высокий, узкий, «towering» силуэт | **DoF сжат по ширине, растянут по высоте** |
| **Крышка** | Центрированная/типовая 4L | Серая рифлёная; **асимметричное** размещение на верхней плоскости (смещена влево) | ➕ **новая C-асимметрия** — не отражена на K |
| **DoF (тактильные)** | Рёбра жёсткости по корпусу + ручка | Рельефные grip-ridges **локализованы** на правой грани (плечо + база) | Тактильный «экзоскелет» **сегментирован** |
| **Стабильность** | Широкая база, низкий CG | Узкая база, высокий CG | **System Dynamics — Limit:** риск опрокидывания при плотной выкладке |

**Вывод (C):** Носитель 1L — не уменьшенная 4L-канистра, а **перекодировка affordance**: с «индустриального бронированного сосуда» (металлическая мимикрия, ручка) на «портативный серебристый модуль долива». Материал и `PATTERN_C_METALLIC_MIMICRY` сохранены; метафора «деталь двигателя» **ослаблена** за счёт потери масштаба и ручки. Тактильный код **мигрировал** на боковые grip-ridges без визуального дублирования на этикетке.

---

### 2.2. K — Композиция (Layout)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Стратегия макета** | Жёсткая асимметрия, Z-паттерн; `Claustrophobic Density` | Вертикальная **рескейл-копия** 4L-дизайна на узкую этикетку с фигурной вырезкой (curved top-right) | **K_PATTERN_VERTICAL_COMPRESS** (gocc_006) |
| **Negative space** | Экстремально малое «воздуха»; overplotting | **≈ 0** по всей вертикали; белое поле **только** вокруг логотипа и «PREMIUM N» | MCON_GPN_06 **усилен**, не инвертирован (в отличие от Mobil) |
| **Иерархия** | Brand → графика → Premium N → 5W-40 → допуски | Идентичная последовательность; **1L** вместо 4L в оранжевом блоке | Константа порядка |
| **Читаемость SAE 5W-40** | Гиперболизированный якорь (System Dynamics anomaly) | Сохранена; белый жирный на оранжевом; **относительный размер ↑** к ширине | **Усилена** на доливном формате |
| **Читаемость объёма** | «4L» — метрологический якорь полной замены | «1L» — **мелкий** белый текст в правом нижнем углу оранжевого блока | **Семантический сдвиг + ↓ legibility** |
| **Подвал (OEM/API)** | Нечитаем из-за градиента (база §2) | **Гипер-сжат:** API SN/CF, ACEA A3/B4, MB/VW/Renault/Porsche — микрошрифт | **↓ critical degradation** |
| **Новые K-элементы** | — | Иконка легкового авто над «PREMIUM N» (gocc_008) | ➕ пиктограммный шорткат сегмента |
| **QR / digital** | н/д в базе | **Отсутствует** (в отличие от Mobil 1L) | Константа «отказ от умной цифры» |

**POV — Information Integrity:**  
- *Redundancy:* «PREMIUM N» + «Premium» (латиница в названии) + «СИНТЕТИЧЕСКОЕ МАСЛО» + «SYNTHETIC ENGINE OIL» — четырёхслойное дублирование пустой категории.  
- *Lacuna:* инфографика механизма действия, benefit-icons — **константа отсутствия**; на 1L **усилена** за счёт выпадения всего, кроме brand + viscosity.  
- *Collonisation:* категорийные коды (серебро + оранжевые свуши) **не ослаблены** при сжатии.

**Вывод (K):** Макет 1L — **вертикальное масштабирование** 4L без адаптации под top-up. Читаемость 5W-40 **не страдает** — наоборот, усиливается как доля площади. Страдает **весь вторичный слой**: 1L, OEM-допуски, API — **ниже порога** близкого и дистанционного чтения. Плотность **равномерно клаустрофобная** (как LUKOIL, не как Mobil с «белым дыханием»).

---

### 2.3. S — Сигнальные паттерны

| Статус | Паттерн | Комментарий |
|--------|---------|-------------|
| ✅ **Сохранён** | Синий логотип Газпромнефти + белый зенит | Якорь `M_SYSTEM_GPN_02` |
| ✅ **Сохранён** | Оранжево-сине-жёлтые абстрактные свуши (MCON_GPN_05) | Термокинетическая симуляция |
| ✅ **Сохранён** | «PREMIUM N» — чёрный гротеск на белой полосе | Лингвистическое подчинение (западная лексика) |
| ✅ **Сохранён** | Оранжевый блок 5W-40 | Главный heuristic cue (System Dynamics anomaly) |
| ✅ **Сохранён** | Серебристый корпус + metallic mimicry (MCON_GPN_03) | Категорийный mass-market код |
| 🟡 **Усилен** | Относительный масштаб 5W-40 | **↑ salience** на узком носителе |
| 🟡 **Усилен** | Корпоративный логотип как % площади | Institutional anxiety **↑** в thumbnail |
| 🔻 **Деградировал** | 3D-глубина свушей (MCON_GPN_05) | Боковое усечение; gestalt-completion нагружена |
| 🔻 **Деградировал** | OEM-допуски (MB, VW, Renault…) | Микрошрифт; **fail** на 120 px и при близком чтении |
| 🔻 **Деградировал** | Маркер объёма «1L» | Мельче 5W-40 в **10×+**; subordinate |
| 🔻 **Деградировал** | `S_INFO_SIGNAL_FRACTION_INDEX` | **↓ further** — декоративная доля **↑** относительно полезного сигнала |
| ➕ **Новый** | Диагональные grip-ridges на C (gocc_001) | Тактильный S-канал «контроль долива» |
| ➕ **Новый** | Иконка авто (gocc_008) | Единственный benefit-shorthand |
| ➕ **Новый** | Фигурная этикетка (curved corner, gocc_003) | Следование S-contour корпуса |

**Вывод (S):** Высокочастотные сигналы (Газпромнефть, 5W-40, оранжевый блок, серебро) **robust** к даунскейлу. Низкочастотные инженерные детали (OEM, API, объём) **фильтруются** — усиливая лакуну «Чёрного ящика». Тактильный S-канал на C **не интегрирован** в K/S этикетки. Отношение сигнал/шум **ухудшается** vs 4L.

---

### 2.4. M — Среда (Medium / контекст потребления)

| Контекст | 4L | 1L | Δ |
|----------|----|----|---|
| **Retail-полка** | Основная полка масел; полная замена | **Полка долива / top-up**; касса, аксессуары, СТО-импульс | **Смена M_CONTEXT** |
| **Плотность выкладки** | ~4–6 facings на п.м. | **~10–14 facings** (узкий профиль) | **↑ linear density** |
| **Дистанция считывания** | 1,5–3 м (`M_NOISE: very_high`) | 0,5–1,5 м (ближний контакт, рука потребителя) | **Ближний контакт** — но OEM всё равно нечитаем |
| **E-commerce thumbnail** | 4L + 5W-40 + логотип — три якоря | Логотип + 5W-40 + серебро читаются; **1L, API, OEM — ниже порога** (~120 px) | **Robustness ↓** для классификации |
| **M_NOISE** | `very_high` (база §2) | Тот же шум; **меньший visual footprint** → риск «потери» среди 4L-соседей на основной полке | **Anomaly:** David among Goliaths |

**POV — System Dynamics:**  
- *Potential:* высокая плотность facings + узнаваемый оранжевый блок → impressions на метр полки в top-up.  
- *Limit:* малый silhouette + серебро (как Mobil/Shell) → **нет** золотого pop LUKOIL; salience только через оранжевый 5W-40.

**Вывод (M):** 1L живёт в **нише долива**, не конкурируя с 4L на основной полке. В top-up-секции выигрывает **узкий профиль** и **оранжевый heuristic**, но проигрывает **affective differentiation** (серебро = категорийная норма). E-commerce: primary layer (brand + viscosity) проходит; объём, допуски, класс API — **нет**.

---

### 2.5. MAP — Мэппинги

| MAP (база 4L) | 1L | Статус |
|---------------|-----|--------|
| `MAP_OBSCURATION_TO_TRANSACTION_SPEED` (сокрытие → скорость покупки) | Константа; **↑ эффективность** — меньше текста читаемо → быстрее эвристика | ✅ **усилен** |
| Термокинетика → защита ДВС (MCON_GPN_05) | Свуши усечены; gestalt **нагружен** | 🟡 **искажение span** |
| SAE 5W-40 → heuristic anchor (System Dynamics anomaly) | Константа; **относительный масштаб ↑** | ✅ **усилен** |
| Объём 4L → «полный цикл обслуживания» | **1L → «точечное пополнение»** | 🔄 **перекодировка MAP объёма** (gocc_005) |
| Металл → премиальность (MCON_GPN_03) | Константа | ✅ |
| OEM-допуски → инженерная легитимность | **MAP оборван** — текст физически не декодируется | ⚠️ **LACUNA MAP** — декларируется, не считывается |
| Газпром → безопасность/антиконтрафакт (MCON_GPN_02) | Константа; **↑ % площади** | ✅ усилен |
| Grip-ridges → контроль долива | **MAP не интегрирован** в K/S | ➕ LATENT (gocc_001) |
| Premium/Synthetic → качество | Константа (пустые категории) | ✅ — без доказательной базы |

**POV — Logical Coherence:**  
- *Contradiction (константа базы):* абстрактная 3D-графика (50% площади) vs OEM в подвале — на 1L **усилена**: графика сохраняет долю, подвал **ещё менее** читаем.  
- *Conflict:* индустриальная «броня» (4L-метафора) vs portable top-up (1L-физика) — **умеренный диссонанс**, не блокирующий M_SYSTEM.

**Вывод (MAP):** Ядро (`MAP_OBSCURATION_TO_TRANSACTION_SPEED`, гипербола 5W-40, институциональный якорь) **масштабируется и усиливается**. Искажаются: (1) gestalt-свуши, (2) семантика объёма, (3) OEM-MAP **декларирован, но не функционирует**. Тактильный MAP (grooves → control) **не связан** с визуальной системой.

---

### 2.6. EVAL — Оценка малого формата

| Метрика | 4L (база) | 1L (delta) | Δ |
|---------|-----------|------------|---|
| **Comprehensibility** | Высокая для brand + 5W-40; низкая для допусков (база §1) | **Высокая** для brand + 5W-40; **низкая** для API/OEM/1L | ↓ вторичный слой **критичнее** |
| **Cognitive load** | Высокая плотность, overplotting (MCON_GPN_06) | **Равномерно высокая** по всей вертикали; нет «зоны дыхания» | **↑ uniform density** |
| **Robustness (thumbnail)** | Средне-высокая (5W-40 + логотип) | **Средняя:** brand + 5W-40 ✅; 1L, OEM, API — **fail** | ↓ |
| **Affective shift** | Institutional anxiety + transaction speed (база) | Сохранён на близкой дистанции; **ослаблен** на 2+ м (малый footprint) | ↓ дальнее поле |
| **Structural fidelity** | Низкая (гипербола, obscuration) | Константа | — |
| **Rhetorical efficiency** | Высокая для масс-маркета (база EVAL_AGG) | **8/10** в top-up; **6/10** overall (потеря OEM-layer) | context-dependent |

**POV — Relational States:** compromise между **DRY brand-asset** (один макет на все форматы) и **полной потерей** инженерной прозрачности на 1L; parity M_SYSTEM при разной C-геометрии.

**Вывод (EVAL):** 1L **не ломает** primary value proposition (Gazpromneft Premium N 5W-40). Ломается **единственный потенциальный secondary layer** — OEM-допуски, которые и на 4L были в «слепой зоне», на 1L становятся **функционально мёртвыми**. Для ODSA: оценивать 1L и 4L **раздельными строками** — иначе `S_INFO_SIGNAL_FRACTION_INDEX` и cognitive load будут **усреднены неверно**.

---

## 3. M_OCCURRENCE — только новые и изменённые

> Occurrences базы без изменений **не дублируются**. Ниже — delta-only (`gocc_` = Gazpromneft occurrence).

### 3.1. gocc_001 — Diagonal grip ridge pairs

**_min**
```yaml
M_OCC_ID: gocc_001
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: carrier_body_right
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "right_face", zones: ["shoulder_3_ridges", "base_3_ridges"] }
M_OCC_SURFACE_FORM: "3 diagonal recessed grip channels on shoulder + 3 mirrored at base on right body face"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_ergonomics` → TARGET `dom_controlled_pour`; MAP `map_grip_as_precision` — **LATENT**, не отражён на этикетке; FUNCTION [`affordance`, `format_signal`]; M_CONSTR link: MCON_GPN_03 (variant-by-format, hardware layer).

---

### 3.2. gocc_002 — Bottle morphology shift (jug → top-up bottle)

**_min**
```yaml
M_OCC_ID: gocc_002
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: carrier_global
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_carrier", axis: "vertical" }
M_OCC_SURFACE_FORM: "Tall narrow asymmetrical bottle; left S-curve, right vertical with recessed grip; no integrated handle"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** **Перекодировка** affordance 4L → 1L; FUNCTION [`format_adaptation`, `portability_signal`]; mild conflict с MCON_GPN_03 (metallic mimicry «сосуд» vs «бутылка»).

---

### 3.3. gocc_003 — Die-cut label with curved top-right corner

**_min**
```yaml
M_OCC_ID: gocc_003
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: label_perimeter
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "label_top_right_corner", form: "curved_follows_shoulder" }
M_OCC_SURFACE_FORM: "Label die-cut follows S-contour of canister shoulder; curved top-right corner"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
```

**_full:** Gestalt-lock label-to-carrier; FUNCTION [`format_integration`]; уменьшает **usable label area** vs прямоугольник — **↑ compression pressure** на K.

---

### 3.4. gocc_004 — Truncated thermo-swirl graphic (delta MCON_GPN_05)

**_min**
```yaml
M_OCC_ID: gocc_004
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: label_center
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "abstract_swirl_orange_blue_yellow", lateral_crop: true }
M_OCC_SURFACE_FORM: "Multi-color fluid swoosh graphic, laterally cropped on narrow label"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: MCON_GPN_05 (degraded)
```

**_full:** Gestalt-completion нагружена; «термокинетическая энергия» **неполная** на thumbnail; FUNCTION [`decorative_persistence`] — декор сохранён, трибологический MAP **не пострадал** (и так отсутствовал).

---

### 3.5. gocc_005 — 1L micro-badge in orange block

**_min**
```yaml
M_OCC_ID: gocc_005
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: label_orange_block_bottom_right
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "orange_5W40_block", position: "bottom_right" }
M_OCC_SURFACE_FORM: "1L small white text subordinate to 5W-40 numerals"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** MAP `map_1L_as_topup_module` vs base `map_4L_as_service_cycle`; M_CONSTR: MCON_GPN_01 (variant-by-format); **иерархически подчинён** 5W-40 — institutional amortization **приоритизирует вязкость над объёмом**.

---

### 3.6. gocc_006 — Vertical compress stacking (delta MCON_GPN_06)

**_min**
```yaml
M_OCC_ID: gocc_006
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", axis: "vertical" }
M_OCC_SURFACE_FORM: "4L layout vertically rescaled; uniform claustrophobic density top-to-bottom"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: MCON_GPN_06 (amplified)
```

**_full:** FUNCTION [`format_adaptation`, `information_stacking`]; отличие от Mobil: **нет** биполярной редукции negative space — claustrophobic density **равномерна** (как LUKOIL 1L).

---

### 3.7. gocc_007_LACUNA — OEM approvals functionally unreadable

**_min**
```yaml
M_OCC_ID: gocc_007_LACUNA
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: label_footer
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "footer_oem_microtext", readable: false }
M_OCC_SURFACE_FORM: "MB-Approval 229.5, VW 502.00/505.00, Renault RN 0700/0710 etc. — present but below legibility threshold"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LACUNA
BASE_REF: MCON_GPN_04 (amplified)
```

**_full:** **Усиление** лакуны «Чёрного ящика» (база §3); MAP OEM → легитимность **декларирован, не функционирует**; покупатель долива **не получает** engineering proof на упаковке.

---

### 3.8. gocc_008 — Car pictogram above PREMIUM N

**_min**
```yaml
M_OCC_ID: gocc_008
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: label_mid_white_band
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: indexical
M_OCC_SPAN: { region: "above_PREMIUM_N_wordmark" }
M_OCC_SURFACE_FORM: "Small white passenger car icon indicating light-vehicle application"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_mass_market_mobility` → TARGET `dom_application_scope`; FUNCTION [`segment_shorthand`]; **единственный** benefit-pictogram на 1L — частичная компенсация gocc_007_LACUNA.

---

### 3.9. gocc_009 — Asymmetric cap placement

**_min**
```yaml
M_OCC_ID: gocc_009
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: carrier_neck
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "top_surface", position: "left_offset" }
M_OCC_SURFACE_FORM: "Grey ribbed screw cap offset to left on top surface"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: LATENT
```

**_full:** FUNCTION [`pour_ergonomics`]; MAP **не интегрирован** в K; на фронтальном ракурсе **не виден** — thumbnail irrelevant.

---

### 3.10. gocc_010 — NEGATIVE_SPACE near-zero (delta MCON_GPN_06)

**_min**
```yaml
M_OCC_ID: gocc_010
CASE_ID: COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA
MATERIAL_ID: gazpromneft_premium_n_5w40_1l_front_2026
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", whitespace_pct: "~5-8" }
M_OCC_SURFACE_FORM: "Near-zero negative space except logo/PREMIUM N white bands; claustrophobic density amplified vs 4L"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: NEGATIVE_SPACE
BASE_REF: MCON_GPN_06 (amplified)
```

**_full:** Противоположность «Premium Whitespace» из антидот-стратегии СТМ (база §4); FUNCTION [`category_conformity`, `visual_noise_maximisation`].

---

## 4. Выводы для СТМ

### 4.1. Где дизайн Gazpromneft Premium N «ломается» на 1L

1. **OEM-подвал** — допуски MB/VW/Renault **физически присутствуют**, но **не декодируются** (gocc_007_LACUNA); логическое противоречие базы **усилено**.
2. **Маркер объёма** — «1L» **subordinate** к 5W-40; в e-commerce и на полке долива **fail** thumbnail-test — риск ошибочного выбора формата.
3. **Gestalt-графика** — термо-свуши усечены (gocc_004); декоративный шум **сохранён**, полезный сигнал **не добавлен**.
4. **Cognitive uniformity** — claustrophobic density **без «дыхания»** (gocc_010); fatigue при попытке прочитать спецификации в top-up-контексте.
5. **Тактильный MAP** — grip-ridges (gocc_001) **не связаны** с визуальной системой; gestalt C↔K **разорван**.
6. **Отсутствие digital-компенсации** — в отличие от Mobil 1L, **нет QR**; лакуна «умной цифры» **не ослаблена**.

### 4.2. Лакуны базового формата: усиление / ослабление

| Лакуна (база) | На 1L |
|---------------|-------|
| Инфографика механизма действия | **Константа** — отсутствует |
| Визуальное подавление допусков (MCON_GPN_04) | **Усилена** — gocc_007_LACUNA |
| `S_INFO_SIGNAL_FRACTION_INDEX: low` | **Усилена** — декор/шум ↑ относительно полезного сигнала |
| Информационная асимметрия («Чёрный ящик») | **Усилена** — единственный proof-layer (OEM) **мертв** |
| Collonisation категорийными кодами | **Константа** |
| Отказ от «умной» цифры | **Константа** (нет QR, в отличие от Mobil) |
| Benefit-icons / product claims | **Усилена лакуна** — только gocc_008 (иконка авто) |

### 4.3. Импликации для ODSA-матрицы

- **Разделять строки 4L и 1L** для Gazpromneft и каждого конкурента с multi-format SKU.
- **Benchmark «Format Robustness Index»:** primary signals at 120 px? (GPN 1L: логотип ✅, 5W-40 ✅, серебро ✅, 1L ✗, OEM ✗, API ✗).
- **Benchmark «Top-up Shelf Fit»:** grip-ridges + узкий профиль — **сильный** physical layer; claim/engineering layer — **слабее Mobil** (нет QR) и **слабее LUKOIL** (нет золотого pop).
- **Attack vector для СТМ на 1L:** чистый top-up макет — viscosity + **крупный** 1L + **один** верифицируемый OEM/API claim; не масштабировать 4L «как есть» (anti-pattern GPN = Mobil = LUKOIL).
- **Attack vector «инженерная прозрачность»:** GPN прячет допуски **и на 4L, и на 1L** — СТМ может дать **явный** MAP допуска в центре (антидот из базы §4).
- **Сравнение тройки 1L ([13](13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md), [14](14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md), настоящий):** GPN — **максимальная** claustrophobic density, **минимальная** secondary readability; Mobil — bimodal density + QR; LUKOIL — золотой pop + равномерная плотность.

**POV — System Dynamics:** Gazpromneft демонстрирует **экстремальный DRY-rescale** с **усилением** obscuration-стратегии на 1L; лакуны базы **не закрываются** — окно для СТМ **расширяется** на top-up-формате.

---

## 5. POV-сводка (обязательная маркировка)

| Маркер | Фиксация |
|--------|----------|
| **Information Integrity** | Lacuna: OEM unreadable, 1L subordinate, no benefits; Redundancy: Premium + Synthetic ×4 языковых слоя; Collonisation: серебро+оранж — категорийная норма; Contamination: нет |
| **Logical Coherence** | Contradiction (усилена): 3D-графика vs мёртвый OEM-footer; Conflict: metallic-armor M_SYSTEM vs portable bottle C — mild |
| **System Dynamics** | Anomaly: 5W-40 hyperbolization **↑** on 1L; Potential: shelf density, orange heuristic; Limit: thumbnail OEM/1L, narrow CG |
| **Relational States** | Parity: M_SYSTEM; Compromise: DRY asset vs engineering transparency; Consensus: 5W-40 legibility across formats |

---

## 6. Таблица «4L vs 1L» — для матрицы конкурентов (ODSA)

| # | Параметр ODSA | 4L (база) | 1L (delta) | Δ для матрицы |
|---|---------------|-----------|------------|---------------|
| 1 | M_SYSTEM | cognitive_amortization + institutional_anxiety | **константа** | = |
| 2 | Carrier morphology | Широкая канистра + ручка | Узкая бутылка + diagonal grip-ridges | **разные строки** |
| 3 | Label strategy | Full Z-pattern design | Vertical rescale + die-cut curve | compress |
| 4 | Negative space | Claustrophobic (~baseline) | **Near-zero** (gocc_010) | **amplified** |
| 5 | SAE 5W-40 legibility | High (hyperbolized) | High (rel. ↑) | = / ↑ |
| 6 | Volume marker | 4L | 1L micro-badge (subordinate) | **semantic shift + ↓ legibility** |
| 7 | OEM/API footer | Present, poorly readable | **Functionally dead** (gocc_007) | ↓↓ engineering |
| 8 | Thermo-swirl graphic | Full gestalt | Laterally cropped (gocc_004) | ↓ decorative |
| 9 | QR / digital | н/д | **Absent** | = (vs Mobil ↓) |
| 10 | Car pictogram | н/д в базе | Present (gocc_008) | ➕ minimal benefit |
| 11 | Retail context | Main shelf | Top-up shelf | **context split** |
| 12 | Facings density | Low–medium | **High** | ↑ |
| 13 | Thumbnail robustness | Med-high | Medium (brand+viscosity OK) | ↓ secondary |
| 14 | Cognitive load | High uniform | High uniform (no breathing) | = / ↑ |
| 15 | STM attack on 1L | — | Large 1L + center OEM + whitespace | **opportunity ↑** |

---

## 7. Issues for discussion

1. **Верификация 4L-образца:** базовый отчёт 11 построен без отдельного MATERIAL_ID и фото 4L; нужен ли full PGMM 4L с фото для калибровки delta (иконка авто, объём 4L, QR)?
2. **OEM «legal vs functional»:** считать ли наличие микротекста OEM «закрытием» engineering layer или это **performative lacuna**?
3. **Порог thumbnail:** принять 120 px как стандарт ODSA robustness test для всех конкурентов (как в Mobil/LUKOIL delta)?
4. **Правило матрицы:** «1 format = 1 row» vs «1 brand = 1 row with format columns» — согласовать до заполнения ODSA.
5. **Тройное сравнение 1L:** GPN vs Mobil vs LUKOIL — нужен ли сводный benchmark «Top-up Format Robustness» как отдельная wiki-страница?
6. **DRY-rescale как industry anti-pattern:** три конкурента (Mobil, LUKOIL, GPN) масштабируют 4L→1L без split brief — фиксировать как **systematic category failure**?
7. **Иконка авто (gocc_008):** присутствует ли на 4L? Если только на 1L — осознанная **format-specific claim strategy**?

---

*Delta-отчёт · CASE `COMP_Gazpromneft_Premium_N_5W-40_1L_DELTA` · ingest 19.06.2026*
