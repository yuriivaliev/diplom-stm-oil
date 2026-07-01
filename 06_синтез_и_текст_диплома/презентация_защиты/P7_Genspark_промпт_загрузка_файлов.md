# Genspark — промпт при загрузке файлов (v6 + mockups)

**Когда использовать:** вы прикрепляете к Genspark **все материалы разом** — отдельная генерация с новым визуалом, контент из v6.

---

## Что прикрепить (10 файлов)

| # | Файл |
|---|------|
| 1 | `P7_Genspark_промпт_презентация.md` |
| 2 | `P7_deck-spec_v6_terms_governance.md` |
| 3 | `ELITEN_defense_draft_v6.pptx` |
| 4–11 | **8 PNG mockups** из `05_визуальные_эскизы/финал/` |

**Mockups (8 шт.):**
- ELITEN Classic Protect 5W-40 4l rev 2.png
- ELITEN Classic Protect 5W-40 1l rev 2.png
- ELITEN Classic Protect 10W-40 4l rev 2.png
- ELITEN Classic Protect 10W-40 1l rev 2.png
- ELITEN Modern Tech 5W-30 4l rev 2.png
- ELITEN Modern Tech 5W-30 1l rev 2.png
- ELITEN Modern Tech 0W-20 5l rev 2.png
- ELITEN Modern Tech 0W-20 1l rev 2.png

---

## PROMPT (скопировать в Genspark + все вложения)

```
Задача: создать НОВУЮ презентацию (новый визуал Genspark), сохранив КАНОН контента из приложенных файлов.

ВЛОЖЕНИЯ (читай все):
1. ELITEN_defense_draft_v6.pptx — эталон: тексты слайдов, цифры, footnotes, speaker notes (17 слайдов)
2. P7_Genspark_промпт_презентация.md — slide-spec, SPEAKER NOTES CANON, запреты
3. P7_deck-spec_v6_terms_governance.md — правила S2/V1, changelog v6
4. 8 PNG — concept front mockups rev.2 (Classic Protect + Modern Tech)

Согласованный шаблон Genspark: [ВСТАВЬ НАЗВАНИЕ ШАБЛОНА — или напиши «подбери consulting/academic 16:9 сам»]

ФОРМАТ: русский · 16:9 · 17 слайдов · export PPTX with presenter notes

ПРИОРИТЕТ ИСТОЧНИКОВ:
- Цифры и формулировки на экране → из v6.pptx (если расхождение с md — побеждает v6.pptx)
- Speaker notes → ДОСЛОВНО из v6.pptx или таблицы SPEAKER NOTES CANON в md (не цифры 1–17!)
- Визуал/layout → новый шаблон Genspark, но плотность текста как consulting deck (короткие bullet’ы, НЕ длинные абзацы)

СТРУКТУРА 17 СЛАЙДОВ:
00 Титул · 01 Задача · 02 Методология · 03 Слои · 04 DR A · 05 V1 · 06 S2/V1 · 07 DR B · 08 4 SKU · 09 PGMM/ODSA · 10 Бренд · 11 Mockups · 12 Ограничения · 13 Roadmap · A1 · A2 · B

LOCKED (не нарушать):
- Red Team (не Read Team)
- S2(Retail) = уровень · V1(Aftermarket) = тренд · не смешивать · при расхождении S2
- Доли брендов 2024–2026 = н/д
- FIPS RU 1172689 ≠ разрешение на продажу
- Footer слайдов 00–13: «ELITEN · NN» (не ELITEN · 00/01/…)
- Приложение B (чеклист), не C
- Roadmap: Ф1 ✅ · Ф2 ✅ mockups 8/8 · В1–В3 · Ф3 ⬜ GTM
- Footnote слайд бренд: «ТЗ ≠ разрешение на продажу · TDS/back label — pre-launch»

СЛАЙД 05 · V1 — ОБЯЗАТЕЛЬНЫЕ ЦИФРЫ (две колонки, не абзацы):

Заголовок: Deep Research A: тренд aftermarket — динамика брендов
Подзаголовок: V1 aftermarket-proxy · «кто растёт / кто падает» · после изменений 2022 г.

Рост / усиление:
- LUKOIL 13,3% → 15,2%
- ZIC 3,7% → 6,1%
- SINTEC 3,9% → 4,7%
- Rolf 3,4% → 3,9%
- Kixx н/д → 3,1%

Снижение / ослабление:
- Shell 11,7% → 5,6%
- Mobil 5,9% → 3,9%
- Castrol 4,4% → 3,1%
- Total н/д → 2,3%
- G-Energy 3,6% → 2,8%

Footnote: V1 = proxy-динамика, не retail-якорь ёмкости; Gazpromneft 2022: 4,0%

СЛАЙД 11 · MOCKUPS:
- Вставь все 8 приложенных PNG в сетку 4×2 (Classic сверху/слева, Modern справа)
- Подписи SKU под каждым изображением
- Пометка: concept front mockups rev.2 · не финальная этикетка

НЕ ДЕЛАТЬ:
- Строки «Слайд NN / 17» на экране
- Speaker notes = только номера слайдов
- Длинные академические абзацы вместо bullet’ов
- Выдуманные доли 2024–2026
- Luxury / «elite lifestyle» pitch

После генерации:
1. Export PPTX with presenter notes
2. Выведи чеклист: [ ] 17 слайдов [ ] notes полные на всех [ ] V1 с цифрами [ ] 8 mockups на слайде 11 [ ] footer ELITEN · NN
3. Если notes не попали в PPTX — повтори export или вставь из v6.pptx
```

---

## Если шаблон ещё не выбран

Сначала **ЭТАП 1** из `P7_Genspark_промпт_презентация.md`, затем этот промпт с `[ШАБЛОН]`.

Если шаблон уже согласован — сразу этот промпт + 10 файлов.

---

## После export

1. PowerPoint → **View → Notes** — на каждом слайде полный текст (не «1», «2»…)
2. Слайд V1 — две колонки с **→** и процентами
3. Сверка с `ELITEN_defense_draft_v6.pptx`

*Пара: `P7_Genspark_промпт_презентация.md` · канон `ELITEN_defense_draft_v6.pptx`*
