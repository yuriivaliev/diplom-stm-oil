# PGMM Delta: Mobil Super 3000 x1 5W-40 — 1L vs 4L

**Дата анализа:** 19 июня 2026 г.  
**Тип отчёта:** packaging_visual_metaphor_delta (не full PGMM)  
**Базовый кейс:** [12_PGMM_mobil_super_3000_x1_5w_40.md](12_PGMM_mobil_super_3000_x1_5w_40.md) (4L)  
**Артефакт:** Mobil Super 3000 x1 SAE 5W-40, 1L — фронтальная этикетка + носитель  
**Методология:** PGMM (Приложение E) + neuromarketing-system-instructions  
**Primary domains (1–23):** D4 Packaging/Carrier · D8 Visual Semiotics · D12 Cognitive Load · D15 Shelf/Retail Context

---

## 0. CASE_min

| Поле | Значение |
|------|----------|
| **CASE_ID** | `COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA` |
| **CASE_TYPE** | `packaging_visual_metaphor_delta` |
| **BASE_CASE_REF** | `Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md` |
| **FORMAT** | 1L (delta vs 4L) |
| **MATERIAL_ID** | `mobil_super_3000_x1_5w_40_1l_front_2026` |
| **SEGMENT_ID** | `label_front_primary` |

---

## 1. Наследование из базы (без дублирования)

### 1.1. M_SYSTEM — **константа**

`msys_techno_vital_armor_001` («Техно-Витальная Броня») — без изменений. См. §1 базового отчёта.

### 1.2. DOMAIN_A / DOMAIN_B — **константа**

- **DOMAIN_B:** трибология, защита ДВС, синтетическая база.  
- **DOMAIN_A:** индустриально-плазменная броня, тяжёлое машиностроение.  

См. [12_PGMM… §1.1](12_PGMM_mobil_super_3000_x1_5w_40.md).

### 1.3. M_CONSTRUCTION — variant-by-format

| ID (база) | Статус на 1L |
|-----------|--------------|
| «Техно-Кинетический Щит» | ✅ сохранён; кольцо/плазма — **усечено по ширине** |
| «Индустриальная Стерильность» | ✅ сохранён; серебристый мат-nositel без изменений |
| «Метрологическая Авторитетность» | 🟡 **variant-by-format:** шильдик 5W-40 сохранён; маркер объёма **4L → 1L** в чёрном микро-блоке |
| «Топология Рацио-Эмоцио» | 🟡 **variant-by-format:** вертикальное сжатие маршрута; эмоциональный блок (низ-право) **уплотнён** |

**POV — Relational States:** parity метафорической системы между форматами; compromise — идентичность бренда vs плотность информации в нижней трети.

---

## 2. Delta по блокам

### 2.1. C — Носитель (Carrier)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Геометрия** | Широкий асимметричный силуэт «мужской торс» (mocc_002) | Узкий вертикальный прямоугольник; левая грань прямая, правая — concave к горловине | **Смена морфологии:** торс → «бутылка долива» |
| **Ручка** | Боковая/интегрированная ручка 4L-формата | **Нет отдельной ручки**; 7 горизонтальных рельефных канавок на правой грани | **Новый affordance:** одноручный захват vs переноска объёмом |
| **Мaterial** | Matte silver-grey PE | Идентично | Константа |
| **Пропорции H:W** | Низкий, устойчивый, широкое основание | Высокий, узкий, «towering» силуэт | **DoF сжат по ширине, растянут по высоте** |
| **DoF (тактильные)** | Рёбра жёсткости + ручка | Рельефные grip-bars; меньшая площадь контакта ладони | Тактильный «экзоскелет» **локализован** на правой грани |
| **Стабильность на полке** | Широкая база, низкий CG | Узкая база, высокий CG; выше риск опрокидывания при выкладке | **System Dynamics — Limit:** формат жертвует устойчивостью ради плотности |

**Вывод (C):** Носитель 1L — не масштаб 4L, а **перекодировка affordance**: с «индустриального бронированного сосуда» на «портативный модуль долива». Метафора mocc_002 (антропоморфный торс) **ослаблена**; усилена utilitarian/portable семантика. Материал и серебристый код синтетики сохранены.

---

### 2.2. K — Композиция (Layout)

| Параметр | 4L (база) | 1L (delta) | Δ |
|----------|-----------|------------|---|
| **Стратегия макета** | Полноформатная этикетка; mocc_020 — гравитационное сжатие по всей площади | **Вертикальная рескейл-копия** 4L-дизайна на узкую этикетку | **K_PATTERN_VERTICAL_COMPRESS** |
| **Negative space** | Экстремально малое «воздуха» (mocc_020) — равномерная плотность | **Бифуркация:** верхняя треть — белое поле вокруг Mobil Super; нижняя треть — **гипер-плотность** | mocc_020 **инвертирован** по оси Y |
| **Иерархия** | Brand → 3000 → 5W-40 → 4L → графика | Идентичная последовательность; **1L** вместо 4L | Константа порядка |
| **Читаемость SAE 5W-40** | Золотая лычка (mocc_010) — высокий контраст | Сохранена; относительный размер **↑** к ширине этикетки | **Усилена** на доливном формате |
| **Читаемость объёма** | «4L» — метрологический якорь полной замены | «1L» — белый на чёрном + QR в том же блоке | **Смена семантики объёма:** maintenance vs full change |
| **QR-код** | н/д в базовом отчёте 4L | Чёрный квадрат, нижний левый угол | **Новый элемент K** — цифровой шлюз |
| **Нижняя графика** | Кольцо/плазма (mocc_001) — полный диаметр | Кольцо **обрезано** по боковым краям этикетки | **Gestalt-усечение** mocc_022 |

**POV — Information Integrity:**  
- *Redundancy:* дублирование «Fully Synthetic» + ACEA + Gasoline&Diesel при сжатии.  
- *Lacuna:* benefit-иконки (fuel economy, wear protection), типичные для 4L, **отсутствуют** на 1L.

**Вывод (K):** Дизайн 1L — **не адаптация, а масштабирование** 4L-макета. Верх сохраняет «воздух» для бренда; низ превращается в **информационный кластер** (QR + 1L + ACEA + синтетика + графика). Читаемость 5W-40 не страдает; читаемость вторичных спецификаций — **деградирует**.

---

### 2.3. S — Сигнальные паттерны

| Статус | Паттерн | Комментарий |
|--------|---------|-------------|
| ✅ **Сохранён** | Mobil blue + Super black + red swoosh | Якорь узнаваемости |
| ✅ **Сохранён** | «3000» italic + gold shadow (mocc_003) | Числовая гипербола |
| ✅ **Сохранён** | Красный «O» (mocc_004) | Термический триггер |
| ✅ **Сохранён** | Золотая лычка 5W-40 (mocc_010) | Военный шильдик |
| ✅ **Сохранён** | Серебро + золото + плазменные искры (mocc_007, mocc_008) | Премиум-palette |
| 🟡 **Усилен** | Вертикальный brand-stack | «Башня» бренда на узком носителе |
| 🔻 **Деградировал** | Заклепки (mocc_006) | Мельче, теряются в thumbnail |
| 🔻 **Деградировал** | 3D-глубина «реактора» (mocc_023) | Плоскость графики сплющена |
| 🔻 **Деградировал** | Benefit-icons / pictograms | Лакуна vs 4L |
| ➕ **Новый** | QR + чёрный info-block | Digital affordance, не в базе 4L |
| ➕ **Новый** | Grip-ridges (тактильный S на C) | Физический сигнал «долив/удобство» |

**Вывод (S):** Высокочастотные бренд-сигналы (цвет, логотип, 5W-40) **robust** к даунскейлу. Низкочастотные индустриальные детали (заклепки, 3D-плазма, benefit-icons) **фильтруются** при сжатии. Появляется **новый сигнальный канал** — QR/цифровой — компенсирующий потерю площади.

---

### 2.4. M — Среда (Medium / контекст потребления)

| Контекст | 4L | 1L | Δ |
|----------|----|----|---|
| **Retail-полка** | Основная полка масел; полная замена | **Полка долива / top-up**; вторичная выкладка у кассы, аксессуаров | **Смена M_CONTEXT** |
| **Плотность выкладки** | ~4–6 facings на п.м. (широкие канистры) | **~10–14 facings** (узкий профиль) | **↑ linear density** |
| **Дистанция считывания** | 1,5–3 м (полка масел) | 0,5–1,5 м (ближняя полка, рука потребителя) | **Ближний контакт** |
| **E-commerce thumbnail** | 4L + 5W-40 + Super — три якоря | Super + 5W-40 читаются; **1L и QR — ниже порога** (~120 px) | **Robustness ↓** для объёма |
| **M_NOISE** | `M_NOISE_HIGH` (база) | Тот же шум, но **меньший visual footprint** → риск «потери» среди 4L-соседей | **Anomaly:** David among Goliaths |

**POV — System Dynamics:**  
- *Potential:* высокая плотность → больше brand impressions на метр полки.  
- *Limit:* малый silhouette area снижает salience в дальнем поле.

**Вывод (M):** 1L живёт в **другой retail-нише** — долив, импульс, companion SKU. На полке основных масел 4L доминирует визуально; 1L выигрывает только в **top-up-секции**. В e-commerce критичны первые 120 px: бренд и вязкость проходят, объём и QR — **нет**.

---

### 2.5. MAP — Мэппинги

| MAP (база 4L) | 1L | Статус |
|---------------|-----|--------|
| Трение → контролируемая плазма (mocc_001) | Сохранён; кольцо усечено | 🟡 **искажение span** — gestalt-completion нагрузка ↑ |
| Синтетика → полированная сталь (mocc_008) | Константа | ✅ |
| SAE → военная лычка (mocc_010) | Константа; **относительный масштаб ↑** | ✅ усилен |
| Объём 4L → «полный цикл обслуживания» | **1L → «точечное пополнение»** | 🔄 **перекодировка MAP объёма** |
| Жидкость → металл (лакуна mocc_015) | Константа | ✅ |
| QR → ? | **MAP не завершён** — нет видимого CTA | ⚠️ **LACUNA MAP** |
| Grip-ridges → ? | **Новый MAP:** удобство/контроль долива | ➕ LATENT |

**POV — Logical Coherence:**  
- *Conflict:* индустриальная «броня» (4L-метафора) vs portable top-up (1L-физика) — **лёгкий диссонанс** без пересборки M_SYSTEM.

**Вывод (MAP):** Ядро метафор («броня + плазма») **масштабируется** без пересмотра. Искажаются: (1) gestalt-кольцо, (2) семантика объёма, (3) отсутствует явный MAP для QR. Новый тактильный MAP (grooves → control) **не интегрирован** в визуальную систему этикетки.

---

### 2.6. EVAL — Оценка малого формата

| Метрика | 4L (база) | 1L (delta) | Δ |
|---------|-----------|------------|---|
| **Comprehensibility** | Оптимальная (база EVAL) | **Высокая** для brand + 5W-40; **средняя** для ACEA/типа топлива | ↓ вторичный слой |
| **Cognitive load** | Высокая плотность (mocc_020) | **Бифурцированная:** низкая (верх) + **пиковая** (низ) | **↑ variance** |
| **Robustness (thumbnail)** | Высокая | **Средняя:** бренд OK, детали графики — **fail** | ↓ |
| **Affective shift** | Anxiety relief через контроль (база) | Сохранён на близкой дистанции; **ослаблен** на 2+ м | ↓ дальнее поле |
| **Structural fidelity** | Низкая (гипербола) | Константа | — |
| **Rhetorical efficiency** | 9/10 (шумная полка) | **7/10** overall; **9/10** в top-up-контексте | context-dependent |

**POV — Relational States:** compromise между **единым brand-asset** (DRY) и **читаемостью** вторичных claims на 1L.

**Вывод (EVAL):** 1L **не ломает** primary value proposition (Mobil Super 3000 5W-40 synthetic). Ломается **secondary layer**: benefit-icons, ACEA, QR, 3D-графика. Для ODSA: оценивать 1L и 4L **раздельными строками** матрицы — иначе cognitive load и robustness будут **усреднены неверно**.

---

## 3. M_OCCURRENCE — только новые и изменённые

> Occurrences базы (mocc_001–008, 010, 014–017, 019–023) без изменений **не дублируются**. Ниже — delta-only.

### 3.1. mocc_024 — Integrated grip grooves

**_min**
```yaml
M_OCC_ID: mocc_024
CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
MATERIAL_ID: mobil_super_3000_x1_5w_40_1l_front_2026
SEGMENT_ID: carrier_body_right
M_OCC_MODALITY_CLASS: visual_tactile
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "right_face", grooves: 7 }
M_OCC_SURFACE_FORM: "7 horizontal recessed grip bars on right body face"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_ergonomics` → TARGET `dom_controlled_pour`; MAP `map_grip_as_precision`; DELIBERATENESS `deliberate`; FUNCTION [`affordance`, `format_signal`]; M_CONSTR link: «Индустриальная Стерильность» (variant-by-format).

---

### 3.2. mocc_025 — QR digital gateway block

**_min**
```yaml
M_OCC_ID: mocc_025
CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
MATERIAL_ID: mobil_super_3000_x1_5w_40_1l_front_2026
SEGMENT_ID: label_bottom_left
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: indexical
M_OCC_SPAN: { region: "bottom_left_black_square" }
M_OCC_SURFACE_FORM: "QR code in black micro-panel adjacent to 1L mark"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** SOURCE `dom_digital_interface` → TARGET `dom_product_auth/spec`; MAP **partial/lacuna** — CTA не виден; FUNCTION [`traceability`]; **конtrast с mocc_017_LACUNA** (отказ от «умной» цифры на 4L) — на 1L цифра **возвращается точечно**, без интеграции в M_SYSTEM.

---

### 3.3. mocc_026 — Vertical compress stacking (изменение mocc_020)

**_min**
```yaml
M_OCC_ID: mocc_026
CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
MATERIAL_ID: mobil_super_3000_x1_5w_40_1l_front_2026
SEGMENT_ID: label_global
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "full_label", axis: "vertical" }
M_OCC_SURFACE_FORM: "4L layout vertically rescaled; bottom third hyper-dense"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: mocc_020 (modified)
```

**_full:** **Инверсия** mocc_020: вместо равномерного «гравитационного сжатия» — **биполярная плотность** (верх rarefied / низ compressed). FUNCTION [`format_adaptation`, `information_stacking`].

---

### 3.4. mocc_027 — Top white breathing zone

**_min**
```yaml
M_OCC_ID: mocc_027
CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
MATERIAL_ID: mobil_super_3000_x1_5w_40_1l_front_2026
SEGMENT_ID: label_top_third
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: configurational
M_OCC_SPAN: { region: "top_third_white_field" }
M_OCC_SURFACE_FORM: "White negative space isolating Mobil Super wordmark"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: NEGATIVE_SPACE
```

**_full:** Противоположность mocc_020 на 4L; создаёт **visual breathing** для brand-lock на малом формате. FUNCTION [`brand_isolation`].

---

### 3.5. mocc_028_LACUNA — Benefit icons absent on 1L

**_min**
```yaml
M_OCC_ID: mocc_028_LACUNA
CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
MATERIAL_ID: mobil_super_3000_x1_5w_40_1l_front_2026
SEGMENT_ID: label_bottom
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: absence
M_OCC_SPAN: { region: "expected_benefit_pictogram_zone" }
M_OCC_SURFACE_FORM: "No fuel economy / wear protection icons (present on 4L variant)"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: medium
STATUS_TAG: LACUNA
```

**_full:** **Усиление** информационного вакуума в зоне product claims; покупатель долива **не получает** benefit-rationale на упаковке.

---

### 3.6. mocc_029 — 1L volume micro-badge

**_min**
```yaml
M_OCC_ID: mocc_029
CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
MATERIAL_ID: mobil_super_3000_x1_5w_40_1l_front_2026
SEGMENT_ID: label_bottom_left
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: propositional
M_OCC_SPAN: { region: "black_panel_white_text" }
M_OCC_SURFACE_FORM: "1L"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: MANIFEST
```

**_full:** MAP `map_1L_as_topup_module` vs base `map_4L_as_service_cycle`; M_CONSTR: «Метрологическая Авторитетность» (variant-by-format).

---

### 3.7. mocc_030 — Truncated plasma ring (delta mocc_001 / mocc_022)

**_min**
```yaml
M_OCC_ID: mocc_030
CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
MATERIAL_ID: mobil_super_3000_x1_5w_40_1l_front_2026
SEGMENT_ID: label_bottom_right
M_OCC_MODALITY_CLASS: visual
M_OCC_REP_LEVEL: iconic
M_OCC_SPAN: { region: "graphic_ring_cropped_lateral" }
M_OCC_SURFACE_FORM: "Metallic ring + golden oil burst, laterally cropped on narrow label"
M_OCC_STATUS_CLASS: confirmed
M_OCC_CONFIDENCE_LEVEL: high
STATUS_TAG: LATENT
BASE_REF: mocc_001, mocc_022 (degraded)
```

**_full:** Gestalt-completion (mocc_022) **нагружена**; «невидимый щит» **неполный** — потенциал для mis-read на thumbnail.

---

## 4. Выводы для СТМ

### 4.1. Где дизайн Mobil «ломается» на 1L

1. **Нижняя треть этикетки** — информационный кластер (QR + 1L + ACEA + synthetic + graphic) без иерархического разделения; cognitive load **пиковый**.
2. **Gestalt-графика** — кольцо/плазма усечено; mocc_022 (невидимый щит) **не срабатывает** на малых разрешениях.
3. **Benefit-layer** — иконки преимуществ выпадают; покупатель долива остаётся только с brand + viscosity.
4. **QR** — цифровой элемент без видимого MAP/CTA; **half-integrated** — не закрывает лакуну mocc_017.
5. **Морфология C** — потеря «торса» (mocc_002); 1L **не несёт** тот же industrial-masculine carrier-code, что 4L.

### 4.2. Лакуны базового формата: усиление / ослабление

| Лакуна (база) | На 1L |
|---------------|-------|
| mocc_014 (эко-слепота) | **Константа** |
| mocc_015 (отказ от гидродинамики) | **Константа** |
| mocc_017 (отказ от «умной» цифры) | **Частично ослаблена** — QR появился, но не интегрирован |
| mocc_019 (отказ от минимализма) | **Константа** внизу; **ослаблена** вверху (mocc_027) |
| Benefit claims (новая) | **Усилена** — mocc_028_LACUNA |

### 4.3. Импликации для ODSA-матрицы

- **Разделять строки 4L и 1L** для Mobil и каждого конкурента с multi-format SKU.
- **Benchmark «Format Robustness Index»:** primary signals survive at 120 px? (Mobil 1L: brand ✅, viscosity ✅, volume ✗, benefits ✗).
- **Benchmark «Top-up Shelf Fit»:** affordance долива (grip, narrow profile, 1L badge) — у Mobil **сильный** physical layer, **слабый** claim layer.
- **Attack vector для СТМ на 1L:** чистый top-up макет — viscosity + 1L + **один** benefit claim; не масштабировать 4L «как есть» (anti-pattern Mobil).
- **Attack vector «умная цифра»:** QR Mobil без CTA — возможность СТМ с **явным** digital MAP (скан → spec/compatibility).

**POV — System Dynamics:** Mobil демонстрирует **DRY-брендинг** (один asset на все форматы) как industry default; лакуны mocc_014–019 **не закрываются** на 1L — окно для СТМ **сохраняется**.

---

## 5. POV-сводка (обязательная маркировка)

| Маркер | Фиксация |
|--------|----------|
| **Information Integrity** | Lacuna: benefit-icons, QR-CTA; Redundancy: ACEA + Gasoline&Diesel + Synthetic в одном кластере; Contamination: нет |
| **Logical Coherence** | Conflict: industrial-armor M_SYSTEM vs portable top-up C-geometry — mild, не блокирующий |
| **System Dynamics** | Potential: shelf density, top-up channel; Limit: thumbnail robustness, gestalt truncation; Anomaly: mocc_020 inversion |
| **Relational States** | Parity: M_SYSTEM между форматами; Compromise: brand DRY vs secondary readability |

---

## 6. Таблица «4L vs 1L» — для матрицы конкурентов (ODSA)

| # | Параметр ODSA | 4L (база) | 1L (delta) | Δ для матрицы |
|---|---------------|-----------|------------|---------------|
| 1 | M_SYSTEM | techno_vital_armor | **константа** | = |
| 2 | Carrier morphology | «Торс» + ручка | Узкая бутылка + grip-ridges | **разные строки** |
| 3 | Label strategy | Full design | Vertical rescale | compress |
| 4 | Negative space | Uniform dense (mocc_020) | Top rarefied / bottom dense | **inverted** |
| 5 | SAE 5W-40 legibility | High (gold badge) | High (rel. ↑) | = / ↑ |
| 6 | Volume marker | 4L | 1L + QR block | **semantic shift** |
| 7 | Benefit icons | Present (typical) | **Absent** (mocc_028) | ↓ claims |
| 8 | Plasma ring graphic | Full gestalt | Laterally cropped | ↓ |
| 9 | QR / digital | н/д | Present, no CTA | partial |
| 10 | Retail context | Main shelf | Top-up shelf | **context split** |
| 11 | Facings density | Low–medium | **High** | ↑ |
| 12 | Thumbnail robustness | High | Medium | ↓ |
| 13 | Cognitive load | High uniform | Bimodal (low top / peak bottom) | ↑ variance |
| 14 | Eco/fluid lacunae | Yes (mocc_014–015) | **Unchanged** | = (attack window) |
| 15 | STM attack on 1L | — | Clean top-up layout + explicit digital MAP | **opportunity** |

---

## 7. Issues for discussion

1. **Единый vs split brand-asset:** DRY-масштабирование 4L→1L — industry norm или systematic failure? Нужен ли отдельный design brief для top-up в ODSA?
2. **QR без CTA:** считать ли mocc_025 «закрытием» mocc_017_LACUNA или cosmetic add-on?
3. **Порог thumbnail:** принять 120 px как стандарт ODSA robustness test для всех конкурентов?
4. **Разделение строк матрицы:** согласовать правило «1 format = 1 row» vs «1 brand = 1 row with format columns».
5. **Верификация 4L:** базовый отчёт 12 построен на 4L без отдельного MATERIAL_ID; нужен ли full PGMM 4L с фото для калибровки delta?
6. **Конкуренты с 1L:** провести symmetric delta для LUKOIL / Gazpromneft / Shell при наличии образцов.

---

*Delta-отчёт · CASE `COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA` · ingest 19.06.2026*
