# Gamma — промпт для ELITEN → export .pptx

**Сервис:** [gamma.app](https://gamma.app)  
**Источник контента (канон):** `ELITEN_defense_draft_v6.pptx` · `P7_deck-spec_v6_terms_governance.md`  
**Архив:** `ELITEN_defense_draft_v5.pptx` — только откат  
**Цель:** новый визуал → **Export PPTX** → speaker notes из v6 · mockups вручную

---

## Как использовать (2 этапа)

| Этап | Действие |
|------|----------|
| **1 · Тема** | В Gamma: Create → Presentation → **выбери тему** (Professional / Minimal / Slate / Dark). **Не генерируй контент ELITEN.** Напиши себе название темы. |
| **Согласование** | Убедись, что тема подходит (consulting, не playful). Зафиксируй: «тема согласована: …» |
| **2 · Слайды** | Вставь **PROMPT** ниже → Generate → Export **PowerPoint** |
| **3 · Notes** | Gamma **не гарантирует** speaker notes в export → скопируй из **`v6.pptx`** или таблицы CANON в `P7_deck-spec_v6_terms_governance.md` |
| **4 · Mockups** | Слайд 12 — 8 PNG `05_визуальные_эскизы/финал/* rev 2.png` |

**Параллельный workflow:** `P7_Genspark_промпт_презентация.md` (этап 1 шаблон → этап 2, notes в промпте).

---

## PROMPT (скопировать целиком в Gamma)

```
Создай презентацию на РУССКОМ языке, 17 слайдов, формат presentation deck 16:9.

КОНТЕКСТ: защита итоговой работы ДПО МГИМО «МГИМО НЕЙРО». Тема — концепция запуска СТМ моторных масел ELITEN (синтетика + полусинтетика). Это исследовательско-прикладная работа, НЕ рекламный pitch готового продукта.

СТИЛЬ ВИЗУАЛА:
- Академическая / consulting защита: сдержанно, много воздуха, чёткая типографика
- Инженерный тон, readable spec — без luxury, без «SUPER», без золотых щитов и «брони»
- Не копируй оранжево-серебряную эстетику LUKOIL / Gazpromneft
- Используй нейтральную палитру (graphite, white, один accent — amber или teal)
- Таблицы и диаграммы только где указано; цифры НЕ округлять

ЖЁСТКИЕ ПРАВИЛА КОНТЕНТА (не нарушать):
- «Розничный якорь (S2)» и «Тренд aftermarket (V1)» — РАЗНЫЕ слои; на экране: **S2(Retail)** / **V1(Aftermarket)**
- S2(Retail) = уровень · V1(Aftermarket) = тренд · при расхождении — S2
- Доли брендов 2024–2026 = н/д (не выдумывать)
- FIPS RU 1172689 = регистрация товарного знака, НЕ разрешение на продажу
- Не называть конкретный завод / площадку блендера
- Mockups = concept front, не финальная этикетка
- Не обещать готовый продукт и launch compliance

FOOTER на слайдах 00–13 (мелко): «ELITEN · NN» (00, 01, … 13). Приложения: A1, A2, B.

---

СЛАЙД 1 — Титул
Заголовок: ELITEN — концепция запуска СТМ моторных масел
Подзаголовок: Итоговая работа ДПО МГИМО «МГИМО НЕЙРО»
Строка: Исследование рынка · продуктовая гипотеза · бренд · concept front mockups · roadmap проверки
Badge: исследование + прикладной проект
Мини: Classic Protect + Modern Tech · 5W-40 · 0W-20

СЛАЙД 2 — Управленческая задача
Заголовок: От неопределённости к проверяемой концепции
Цепочка: Изменение рынка после 2022 → Данные и ограничения → Проектные решения → Проверяемая концепция
• Рынок изменился, но данные неоднородны
• СТМ требует доказательной логики, не рекламной декларации
• Цель — концепция запуска с зонами проверки

СЛАЙД 3 — Методология
Заголовок: Методология: управляемый ИИ-workflow
Pipeline: Протокол агента → GPTOracle → Red Team → Deep Research A/B → Декомпозиция + wiki → PGMM + ODSA → Бренд/SKU/mockups → Синтез
Итог: ИИ — не источник истины, а инструмент исследования и прототипирования

СЛАЙД 4 — Слои доказательности
Заголовок: Корпус материалов: слои доказательности
Таблица:
| Слой | Содержание | Не доказывает |
| Deep Research A | рынок · бренды · шоки | SAE |
| Deep Research B | вязкости · спрос · SKU | доли брендов |
| S2(Retail) / V1(Aftermarket) | разные базы | не объединять |
| PGMM / ODSA | упаковка · claims | — |
| Mockups | визуальные концепты | финальная этикетка |

СЛАЙД 5 — Deep Research A: контекст
Заголовок: Deep Research A: рыночный контекст после 2022
Подзаголовок: Retail 2023 — лидеры и шоки
Top-5 retail 2023 (розничный якорь S2):
1. LUKOIL 18,1% · 2. Gazpromneft 10,5% · 3. Rosneft 8,5% · 4. ZIC 5,5% · 5. Shell 4,5%
Карточки:
• Уход ops: Shell · ExxonMobil · Total · Castrol
• Ценовой шок 4L: LUKOIL +110% · Mobil +138% · Shell +124%
• СТМ-возможность: service-first · mass-mid
Footnote: S2 retail 2023 · не прогноз доли СТМ

СЛАЙД 6 — Тренд aftermarket (V1)
Заголовок: Deep Research A: тренд aftermarket — динамика брендов
Подзаголовок: V1 proxy — «кто растёт / кто падает» после изменений 2022 г.
Две колонки:
Рост: LUKOIL 13,3%→15,2% · ZIC 3,7%→6,1% · SINTEC 3,9%→4,7% · Rolf 3,4%→3,9% · Kixx н/д→3,1%
Снижение: Shell 11,7%→5,6% · Mobil 5,9%→3,9% · Castrol 4,4%→3,1% · Total н/д→2,3% · G-Energy 3,6%→2,8%
Footnote: V1 = proxy-динамика, не retail-якорь · Gazpromneft 2022: 4,0%

СЛАЙД 7 — Правило S2/V1
Заголовок: Deep Research A: розничный якорь, тренд aftermarket и правило
Блок V1: Направление · Proxy A-KT→GfK · 2022→11М2023 · V1-01
Блок S2: Уровень · Aftermarket-DATA · S2-01 · 278 млн л · LUKOIL 18,1%
ПРАВИЛО (крупно): S2(Retail) = уровень · V1(Aftermarket) = тренд · не смешивать · при расхождении — S2
Footnote: S2/V1 — коды Deep Research A

СЛАЙД 8 — Deep Research B: SAE
Заголовок: Deep Research B: SAE-логика продуктового выбора
4 карточки:
• 5W-30 ~35% 1П2023 РФ retail · synthetic 45,9% — массовое ядро
• 5W-40 ~32% · synthetic 51,0% — массовое ядро
• 0W-20 fastest growth +10,1% л · +16,0% ₽ — ростовой фронтир
• 10W-40 49% ЮФО · 17% Москва/МО · declining legacy — coverage-SKU
Footnote: 0W-XX Москва/МО 6%→4% · SAE обосновывает продукт, не доли брендов

СЛАЙД 9 — Линейка 4 SKU
Заголовок: ELITEN: гипотеза линейки 4 SKU
Дерево:
ELITEN → Classic Protect (5W-40 synthetic mass core · 10W-40 semi legacy) + Modern Tech (5W-30 core/OEM · 0W-20 growth)
Footnote: TDS · API/ACEA · OEM · FIPS

СЛАЙД 10 — PGMM/ODSA gap
Заголовок: PGMM/ODSA: конкуренты и gap spec-коммуникации
Конкуренты: 5W-40 LUKOIL LUXE · GPN Premium N · Mobil 3000 x1 | 0W-20 Mobil 1 · Castrol EDGE | 10W-40 LUKOIL SUPER · GPN Super · Mobil 2000 x1
Gap: armor-риторика · API/OEM off-front · 1L gap · white space = readable spec + меньше пафоса

СЛАЙД 11 — Бренд
Заголовок: Бренд: ELITEN как инженерный зонтик
Hero: Качественная база + мировые пакеты присадок → выбор SKU под задачу
Почему подходит: не «luxury elite», а engineering / readable spec · IP-blocker снят
Как работает: master → Classic Protect + Modern Tech
Что проверено: DDx (Verum/Calibr) · ТЗ Eliten RU 1172689 — регистрация ФИПС, кл. 04 (моторные масла), действует с 03.12.2025
Classic/Modern: 5W-40/10W-40 · 5W-30/0W-20
Footnote: ТЗ ≠ разрешение на продажу · TDS/back label — pre-launch
Speaker note: ELITEN выбран не как luxury-обещание, а как инженерный зонтик понятного выбора продукта под задачу. Это снимает риск false premium: бренд поддерживается readable spec-логикой, качественной базой и мировыми пакетами присадок как проектной рамкой. Classic Protect отвечает за массовую и legacy-ветку, Modern Tech — за современную SAE/OEM-логику. Verum и Calibr использовались как DDx-альтернативы, а FIPS RU 1172689 вынесен отдельным проверочным слоем.

СЛАЙД 12 — Mockups
Заголовок: Concept front mockups: визуальная система ELITEN
Placeholder grid 2×4: 5W-40 4L/1L · 10W-40 4L/1L · 5W-30 4L/1L · 0W-20 5L/1L
Подписи: graphite HDPE · Classic vs Modern · amber oil ribbon
Footnote (alert): concept front mockups · не финальная этикетка · TDS/back label pending
[NOTE FOR DESIGN: leave image placeholders — user will insert real PNG mockups]

СЛАЙД 13 — Ограничения
Заголовок: Ограничения и зоны проверки
4 блока: Data (доли 2024–26 н/д) · Technical (TDS/API/OEM) · Legal/IP (FIPS/back label) · Commercial (цена/канал)
Footnote: LUKOIL/Gazpromneft сильны — гипотеза присутствия, не подтверждённые доли

СЛАЙД 14 — Roadmap
Заголовок: Roadmap: от концепции к валидации
3 gate: Technical (TDS·рецептура·API) + Legal (FIPS·маркировка) + Commercial (цена·каналы)
Итог: проверяемая концепция — не готовый продукт
Строка: Ф1✅ архитектура · Ф2✅ mockups 8/8 · В1 5W-40+5W-30 · В2 0W-20 · В3 10W-40 ЮФО · Ф3⬜ GTM

СЛАЙД 15 — Приложение A1
Заголовок: Приложение A1: методологический след
Таблица: Постановка задачи (Протокол→план) · Промпт-дизайн (GPTOracle+RT) · Deep Research A (рынок) · Deep Research B (SAE) · Декомпозиция+wiki
Speaker note: Приложение A1 показывает, как компетенции программы переведены в управляемый ИИ-workflow. Сначала — протокол аналитика и план этапов 0–7, затем meta-prompting через GPTOracle и Red Team для Deep Research A и B. Отдельно зафиксирована проверка результатов: декомпозиция, wiki-ingest и разведение фактов, выводов и гипотез. Это ответ комиссии на вопрос, что именно делалось методологически, а не только какой получился рыночный вывод.

СЛАЙД 16 — Приложение A2
Заголовок: Приложение A2: методологический след
Таблица: PGMM · ODSA · DDx+FIPS · 8 mockups rev.2 · Roadmap MECE/CLA/OST/RBS · Синтез концепции
Speaker note: Приложение A2 закрывает прикладной блок программы: PGMM выявил white space в spec-коммуникации, ODSA — риски claims и back label, DDx и проверка FIPS вне LLM обосновали выбор ELITEN. Concept front mockups rev.2 связывают визуальную систему с PGMM/ODSA, а декомпозиция MECE/CLA/OST/RBS перевела отчёты в операционный чеклист. Проект дошёл от desk research до бренда, упаковки и roadmap проверки.

СЛАЙД 17 — Приложение B
Заголовок: Приложение B: сводный чеклист запуска СТМ
1. Продукт: bimodal Classic/Modern · волны В1 5W-40+5W-30 · В2 0W-20 · В3 10W-40 ЮФО
2. R&D: ТЗ 0W-20 Gr.III+PAO API SP · 5W-40 Gr.III API SN · mockups 8/8 · fasovka 5L+1L/4L+1L · площадка = gate (не фиксируем)
3. GTM next steps: коммуникация · регионы · цена · ЦФО/СЗФО 0W-20/5W-30 · ЮФО 10W-40/5W-40
Speaker note: Приложение B — сводный чеклист запуска из декомпозиции Deep Research. Продукт: bimodal Classic Protect / Modern Tech и три волны — 5W-40+5W-30, затем 0W-20, 10W-40 для ЮФО. R&D фиксирует рамки ТЗ и mockups 8/8, без утверждения о готовности к продаже. Маркетинг и дистрибуция — next steps: коммуникация, регионы, цена. Аналитика не осталась набором отчётов, а стала проверяемым планом следующих шагов.
```

---

## PROMPT КОРОТКИЙ (если лимит символов Gamma)

```
17 slides, Russian, 16:9, DPO defense МГИМО НЕЙРО: ELITEN STM motor oils launch concept (not product ad). Style: academic consulting, engineering tone, no luxury. LOCKED numbers: S2 retail 2023 LUKOIL 18,1% 278mln L; V1 proxy trends separate; rule S2=level V1=trend never mix; SAE 5W-30 35% 5W-40 32%; 4 SKU Classic Protect+Modern Tech; PGMM white space readable spec; brand Eliten engineering umbrella+world additive packages; FIPS RU 1172689 not sales permit; limits 2024-26 nd; roadmap validation gates; appendices A1 A2 B. No factory name. Slide 12 mockup placeholders only. Export-ready structure.
```

Затем вставь **полный PROMPT** по частям через «Continue» / редактирование слайдов.

---

## Настройки Gamma (рекомендация)

| Параметр | Значение |
|----------|----------|
| Type | Presentation |
| Language | Russian |
| Theme | Professional / Minimal / Slate |
| Cards per slide | Standard (не «scroll story») |
| Images | Minimal stock; **не** генерировать канистры масла |
| Export | PowerPoint (.pptx) |

---

## После export — чеклист

- [ ] 17 слайдов · приложения **A1, A2, B**
- [ ] S2(Retail) / V1(Aftermarket) **не** в одной таблице
- [ ] **Speaker notes на всех 17** — скопированы из `ELITEN_defense_draft_v6.pptx` или CANON в deck-spec
- [ ] Слайд 11: «мировые пакеты присадок» · сноска ТЗ ≠ продажа
- [ ] Слайд 12: **8 PNG** rev.2
- [ ] Слайд 14: строка Ф1/Ф2/В1–В3
- [ ] Red Team (не Read Team) на слайде методологии
- [ ] Нет завода · FIPS ≠ продажа · н/д 2024–26

---

## Speaker notes после export (Gamma)

Gamma **не переносит** presenter notes надёжно. После export:

1. Открой **`ELITEN_defense_draft_v6.pptx`** и export Gamma side-by-side.
2. В PowerPoint: **View → Notes** на каждом слайде.
3. Скопируй notes из v6 в Gamma-PPTX **или** из таблицы **SPEAKER NOTES CANON** в `P7_deck-spec_v6_terms_governance.md`.

---

## Если Gamma «ломает» layout при export

1. Export PDF для просмотра + править **`ELITEN_defense_draft_v6.pptx`** (Design → тема).
2. Или: Gamma только слайды 1–4 и 10–14; mockups и S2/V1 из **v6**.

---

*Пара: `P7_Genspark_промпт_презентация.md` · канон `ELITEN_defense_draft_v6.pptx` · обновлено 30.06.2026*
