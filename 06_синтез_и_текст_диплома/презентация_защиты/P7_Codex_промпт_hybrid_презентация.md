# Codex — промпт: hybrid презентация защиты (v6 + Genspark)

**Задача:** собрать **финальный PPTX для защиты** — контент и speaker notes из v6, визуал/mockups из Genspark academic-review.

**Выходной файл:** `ELITEN_defense_hybrid_v7.pptx` (в этой же папке)  
**Не перезаписывать:** `ELITEN_defense_draft_v6.pptx` · `ELITEN_defense_Genspark_academic-review_final.pptx`

---

## PROMPT (скопировать в Codex целиком)

```
Роль: инженер артефактов P7 — сборка защитной презентации ELITEN (ДПО МГИМО).

Рабочая папка:
/Users/yurii.valiev/Desktop/МГИМО/Дипломная работа ДПО МГИМО/диплом_СТМ_автомасла/06_синтез_и_текст_диплома/презентация_защиты/

Прочитай перед работой:
- P7_deck-spec_v6_terms_governance.md (правила S2/V1, CANON notes, XML-fix)
- Cursor/AGENTS.md — жёсткие ограничения (S2≠V1, 2024–2026 н/д)

ВХОДНЫЕ ФАЙЛЫ:
1. ELITEN_defense_draft_v6.pptx          — КАНОН: тексты слайдов, footnotes, speaker notes (17)
2. ELITEN_defense_Genspark_academic-review_final.pptx — ДОНОР: academic-review визуал, mockups 8 PNG, V1-таблица с цифрами
3. P7_deck-spec_v6_terms_governance.md   — спецификация и SPEAKER NOTES CANON

ЦЕЛЬ:
Создать ELITEN_defense_hybrid_v7.pptx — готов к репетиции защиты 14–15 мин.

СТРАТЕГИЯ СБОРКИ (рекомендуемая):
A. Скопировать ELITEN_defense_draft_v6.pptx → ELITEN_defense_hybrid_v7.pptx (база = v6)
B. Из Genspark-файла перенести ТОЛЬКО:
   - слайд 11 (mockups): 8 embedded images + сетка 4×2 (сохранить PNG из ppt/media)
   - опционально: theme/layout фона с Genspark на титул (00) — если не ломает notes
C. Speaker notes: 100% из v6 — ДОСЛОВНО, все 17 слайдов (не цифры 1–17)
D. On-screen текст слайдов 00–13: оставить из v6 (плотность consulting deck). НЕ раздувать Genspark-абзацами.

АЛЬТЕРНАТИВА (если проще):
- База = v6.pptx
- Только вставить 8 PNG mockups на слайд mockups v6 из 05_визуальные_эскизы/финал/* rev 2.png
- Notes не трогать

LOCKED — НЕ МЕНЯТЬ СМЫСЛ И ЦИФРЫ:
- Red Team (не Read Team)
- S2(Retail) = уровень · V1(Aftermarket) = тренд · не смешивать · при расхождении S2
- S2 retail 2023: 278 млн л; Top-5: LUKOIL 18,1% · Gazpromneft 10,5% · Rosneft 8,5% · ZIC 5,5% · Shell 4,5%
- V1 слайд 05 — две колонки с точными % (из v6 или Genspark — они совпадают):
  LUKOIL 13,3%→15,2% · ZIC 3,7%→6,1% · SINTEC 3,9%→4,7% · Rolf 3,4%→3,9% · Kixx н/д→3,1%
  Shell 11,7%→5,6% · Mobil 5,9%→3,9% · Castrol 4,4%→3,1% · Total н/д→2,3% · G-Energy 3,6%→2,8%
  Footnote: V1 = proxy-динамика, не retail-якорь; Gazpromneft 2022: 4,0%
- Доли 2024–2026 = н/д (не выдумывать)
- FIPS RU 1172689 ≠ разрешение на продажу
- Footnote бренд: «ТЗ ≠ разрешение на продажу · TDS/back label — pre-launch»
- Footer 00–13: «ELITEN · NN»
- Roadmap: Ф1 ✅ · Ф2 ✅ mockups 8/8 · В1 5W-40+5W-30 · В2 0W-20 · В3 10W-40 ЮФО · Ф3 ⬜ GTM
- Приложения: A1, A2, B (не C)

XML / PPTX БЕЗОПАСНОСТЬ (обязательно):
- В notes/slide XML: «R&D» → «R&amp;D»; все «&» экранировать
- Уникальные shape id на каждом слайде (no duplicate p:cNvPr id)
- После правок: python xml.etree.ElementTree.fromstring на все ppt/**/*.xml
- Сохранить .bak перед записью: ELITEN_defense_hybrid_v7.pptx.bak

ПРОВЕРКА (выполни и выведи отчёт):
1. 17 слайдов
2. Speaker notes: len > 200 символов на каждом из 17; slide 17 notes содержит «R&D» (parsed text)
3. Mockups slide: 8 images (a:blip count ≥ 8)
4. V1 slide: содержит «13,3%» и «11,7%»
5. Нет «Read Team»; есть «Red Team»
6. XML parse errors = 0
7. Сравнение notes hybrid vs v6: exact match 17/17

ДОКУМЕНТАЦИЯ:
- Добавь строку в презентация_защиты/README.md про hybrid_v7
- Краткая запись в журнал_проекта.md (дата, артефакт, что перенесено из Genspark)

НЕ ДЕЛАТЬ:
- git commit / push без явной просьбы пользователя
- Менять unrelated файлы
- Удалять v6 или Genspark исходники
```

---

## Краткая версия (если лимит контекста)

```
Собери ELITEN_defense_hybrid_v7.pptx в презентация_защиты/:
база = ELITEN_defense_draft_v6.pptx (контент + notes 17 слайдов).
Из ELITEN_defense_Genspark_academic-review_final.pptx перенеси слайд mockups (8 PNG).
Проверь XML (&amp; для R&D), notes = v6 дословно, V1 цифры, footer ELITEN · NN.
Отчёт: 17 slides · notes match · 8 images · 0 XML errors.
Spec: P7_deck-spec_v6_terms_governance.md
```

---

## Mockups (если копируешь из папки, не из Genspark)

`05_визуальные_эскизы/финал/`:
- ELITEN Classic Protect 5W-40 4l rev 2.png
- ELITEN Classic Protect 5W-40 1l rev 2.png
- ELITEN Classic Protect 10W-40 4l rev 2.png
- ELITEN Classic Protect 10W-40 1l rev 2.png
- ELITEN Modern Tech 5W-30 4l rev 2.png
- ELITEN Modern Tech 5W-30 1l rev 2.png
- ELITEN Modern Tech 0W-20 5l rev 2.png
- ELITEN Modern Tech 0W-20 1l rev 2.png

---

## Критерий «готово к защите»

| Проверка | OK |
|----------|:--:|
| 17 слайдов | ☐ |
| Notes = v6 (17/17) | ☐ |
| 8 mockups на слайде 11 | ☐ |
| V1 с % → | ☐ |
| PowerPoint открывает без «Восстановить» | ☐ |
| Репетиция ≤15 мин по notes | ☐ |

*Пара: v6 канон · Genspark academic-review · P7_deck-spec_v6*
