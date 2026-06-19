# PGMM Delta — шаблон промпта (Cursor Agent)

**Назначение:** сравнительный анализ **альтернативного формата упаковки** (например 1L vs 4L) того же SKU без повторного полного PGMM.

**Oracle не нужен** — промпт самодостаточен для Cursor Agent mode.

**Методология:** PGMM (Klepikov) + neuromarketing-system-instructions · база — wiki-отчёт full PGMM.

---

## Когда использовать

| Ситуация | Действие |
|----------|----------|
| Тот же бренд/SKU, другой объём (1L / 4L / 5L) | ✅ Delta (этот шаблон) |
| Тот же бренд, другая вязкость (5W-30 vs 5W-40) | 🟡 Delta + проверка M_SYSTEM |
| Новый конкурент с нуля | ❌ Полный PGMM (отдельный чат, без delta) |
| Только другой ракурс того же формата | ❌ Не нужен отдельный отчёт |

---

## Подготовка (заполнить перед копированием)

| Поле | Пример (Mobil) | Ваше значение |
|------|----------------|---------------|
| `{{BRAND}}` | Mobil | |
| `{{LINE}}` | Super 3000 x1 | |
| `{{SAE}}` | 5W-40 | |
| `{{FORMAT_DELTA}}` | 1L | |
| `{{FORMAT_BASE}}` | 4L | |
| `{{BASE_WIKI}}` | `Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md` | |
| `{{OUTPUT_WIKI}}` | `Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md` | |
| `{{CASE_ID}}` | `COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA` | |
| `{{IMAGE}}` | прикрепить в чат | |

**Изображения (рекомендация):**
1. Фронтальная этикетка `{{FORMAT_DELTA}}` — обязательно.
2. Вид сбоку (форма канистры, ручка) — желательно, если морфология отличается от `{{FORMAT_BASE}}`.

**Где запускать:** новый чат Cursor → **Agent mode** → прикрепить изображение + вставить блок PROMPT ниже.

---

## Блок PROMPT (копировать целиком)

```
Задача: Delta-анализ упаковки {{BRAND}} {{LINE}} SAE {{SAE}}, {{FORMAT_DELTA}} по PGMM.

Контекст проекта:
- Читай Cursor/AGENTS.md и Cursor/wiki/index.md
- Базовый отчёт ({{FORMAT_BASE}}): {{BASE_WIKI}}
- Методология: PGMM (Приложение E: M_OCCURRENCE, M_CONSTRUCTION, M_SYSTEM) + neuromarketing-system-instructions
- Это НЕ полный PGMM с нуля, а сравнительная дельта {{FORMAT_DELTA}} vs {{FORMAT_BASE}}

Вход:
- [ПРИКРЕПИ ИЗОБРАЖЕНИЕ КАНИСТРЫ {{FORMAT_DELTA}}]
- Продукт: {{BRAND}} {{LINE}} SAE {{SAE}}, объём {{FORMAT_DELTA}}

Сделай:
1. Зафиксируй CASE_min:
   - CASE_ID: {{CASE_ID}}
   - CASE_TYPE: packaging_visual_metaphor_delta
   - BASE_CASE_REF: {{BASE_WIKI}}
   - FORMAT: {{FORMAT_DELTA}} (delta vs {{FORMAT_BASE}})

2. Сравни с базой {{FORMAT_BASE}} и опиши только изменения (Delta) по блокам:
   - C (носитель: геометрия, ручка, материал, пропорции, DoF)
   - K (макет, плотность, negative space, читаемость SAE / объёма)
   - S (сигнальные паттерны: что сохранилось / деградировало / усилилось)
   - M (среда: полка долива, плотность выкладки, e-commerce thumbnail)
   - MAP (какие мэппинги сохранены, какие искажены при масштабировании)
   - EVAL (comprehensibility, cognitive load, robustness в малом формате)

3. Наследуй без переписывания (только ссылка на базу):
   - M_SYSTEM (если не изменился — одна строка «константа»)
   - DOMAIN_A / DOMAIN_B (если константа)
   - M_CONSTRUCTION (перечисли ID из базы + отметь variant-by-format)

4. Экстрагируй только новые или изменённые M_OCCURRENCE:
   - формат _min и _full (MATERIAL_ID, SEGMENT_ID, MODALITY_CLASS, REP_LEVEL, SPAN, SURFACE_FORM, STATUS_CLASS, CONFIDENCE_LEVEL)
   - явно помечай: MANIFEST / LATENT / LACUNA / NEGATIVE_SPACE
   - не дублируй occurrences из базового отчёта без изменений

5. Сформируй выводы для СТМ:
   - где дизайн {{BRAND}} «ломается» на {{FORMAT_DELTA}}
   - какие лакуны базового формата усиливаются или ослабевают
   - импликации для сравнительной матрицы брендов (ODSA)

Deliverables:
- Сохрани отчёт: {{OUTPUT_WIKI}}
- Обнови Cursor/wiki/log.md (дата, ingest delta)
- В конце отчёта: таблица «{{FORMAT_BASE}} vs {{FORMAT_DELTA}}» (10–15 строк) для матрицы конкурентов

Ограничения:
- Не дублируй ~90% базового отчёта {{FORMAT_BASE}} — только delta + перекрёстные ссылки
- Явно маркируй: Information Integrity / Logical Coherence / System Dynamics / Relational States
- Issues for discussion — отдельным блоком в конце
- Не смешивать DR-A (доли брендов) и PGMM (упаковка) в одной таблице

После каждого логического блока — краткий вывод (2–4 предложения).
```

---

## Пример: Mobil Super 3000 x1 5W-40 (1L vs 4L)

Готовый промпт с подставленными значениями — для копирования без правки полей:

```
Задача: Delta-анализ упаковки Mobil Super 3000 x1 SAE 5W-40, 1L по PGMM.

Контекст проекта:
- Читай Cursor/AGENTS.md и Cursor/wiki/index.md
- Базовый отчёт (4L): Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md
- Методология: PGMM (Приложение E: M_OCCURRENCE, M_CONSTRUCTION, M_SYSTEM) + neuromarketing-system-instructions
- Это НЕ полный PGMM с нуля, а сравнительная дельта 1L vs 4L

Вход:
- [ПРИКРЕПИ ИЗОБРАЖЕНИЕ 1L КАНИСТРЫ]
- Продукт: Mobil Super 3000 x1 SAE 5W-40, объём 1L

Сделай:
1. Зафиксируй CASE_min:
   - CASE_ID: COMP_MOBIL_SUPER3000_X1_5W40_1L_DELTA
   - CASE_TYPE: packaging_visual_metaphor_delta
   - BASE_CASE_REF: Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md
   - FORMAT: 1L (delta vs 4L)

2. Сравни с базой 4L и опиши только изменения (Delta) по блокам:
   - C (носитель: геометрия, ручка, материал, пропорции, DoF)
   - K (макет, плотность, negative space, читаемость SAE 5W-40 / 1L)
   - S (сигнальные паттерны: что сохранилось / деградировало / усилилось)
   - M (среда: полка долива, плотность выкладки, e-commerce thumbnail)
   - MAP (какие мэппинги сохранены, какие искажены при масштабировании)
   - EVAL (comprehensibility, cognitive load, robustness в малом формате)

3. Наследуй без переписывания (только ссылка на базу):
   - M_SYSTEM (если не изменился — одна строка «константа»)
   - DOMAIN_A / DOMAIN_B (если константа)
   - M_CONSTRUCTION (перечисли ID из базы + отметь variant-by-format)

4. Экстрагируй только новые или изменённые M_OCCURRENCE:
   - формат _min и _full
   - явно помечай: MANIFEST / LATENT / LACUNA / NEGATIVE_SPACE
   - не дублируй occurrences из базового отчёта без изменений

5. Сформируй выводы для СТМ:
   - где дизайн Mobil «ломается» на 1L
   - какие лакуны базового формата усиливаются или ослабевают
   - импликации для сравнительной матрицы брендов (ODSA)

Deliverables:
- Сохрани отчёт: Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md
- Обнови Cursor/wiki/log.md
- В конце отчёта: таблица «4L vs 1L» (10–15 строк) для матрицы конкурентов

Ограничения:
- Не дублируй ~90% базового отчёта 4L — только delta + перекрёстные ссылки
- Явно маркируй: Information Integrity / Logical Coherence / System Dynamics / Relational States
- Issues for discussion — отдельным блоком в конце

После каждого логического блока — краткий вывод (2–4 предложения).
```

---

## Именование выходных wiki-файлов

```
Cursor/wiki/{NN}_PGMM_{brand}_{line}_{sae}_{format}_delta.md
```

| Компонент | Правило |
|-----------|---------|
| `NN` | Следующий свободный номер в wiki (сейчас: 13 для Mobil 1L) |
| `brand` | lowercase, без пробелов (`mobil`, `lukoil`) |
| `format` | `1L`, `4L` и т.д. |
| `_delta` | Обязательный суффикс для delta-отчётов |

---

## Чеклист самопроверки (перед закрытием задачи)

| # | Проверка |
|---|----------|
| BP1 | Базовый full-отчёт не продублирован — только delta |
| BP2 | M_SYSTEM либо «константа», либо обоснованное изменение |
| BP3 | Таблица {{FORMAT_BASE}} vs {{FORMAT_DELTA}} есть (10–15 строк) |
| BP4 | Новые M_OCCURRENCE в формате _min/_full |
| BP5 | POV-маркеры (Integrity / Coherence / Dynamics / Relational) проставлены |
| BP6 | `log.md` обновлён |
| BP7 | Issues for discussion — отдельный блок |
| BP8 | Нет смешения DR-A/B и PGMM |

---

## Связанные файлы

| Файл | Роль |
|------|------|
| `PGMM.md` / `PGMM.txt` | Первичник методологии |
| `Cursor/wiki/10_PGMM_*.md` … | Примеры full PGMM |
| `Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md` | База для Mobil delta |
| `Cursor/AGENTS.md` | Правила ingest в wiki |

---

*Шаблон создан: 19.06.2026 · этап 4 PGMM/ODSA*
