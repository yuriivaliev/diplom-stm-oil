# P7 — PROMPT исполнитель FINAL · защитная презентация

**Код:** P7 · Presentation defense · этап 7  
**Дата FINAL:** 28.06.2026 (rev.2)  
**Oracle:** [`P7_Master_промпт_v2_oracle.md`](P7_Master_промпт_v2_oracle.md) — **основа**  
**Red Team:** [`P7_Red_Team_v2.md`](P7_Red_Team_v2.md)  
**v1 / RT v1:** [`P7_Master_промпт_v1_oracle.md`](P7_Master_промпт_v1_oracle.md) · [`P7_Red_Team_v1.md`](P7_Red_Team_v1.md)

---

## Как исполнять

1. Прочитать **PRE-READ** (ниже).
2. Применить **весь** текст [`P7_Master_промпт_v2_oracle.md`](P7_Master_промпт_v2_oracle.md) (§1–15).
3. Дополнительно применить **PATCH BLOCK P7-19…24** (проектные патчи, не полностью в v2).
4. Deliverable: **markdown deck-spec** → PPTX собирает оператор.

---

## PRE-READ (обязательно)

| Порядок | Файл |
|--------|------|
| 1 | [`Cursor/AGENTS.md`](../../Cursor/AGENTS.md) |
| 2 | [`Cursor/wiki/index.md`](../../Cursor/wiki/index.md) |
| 3 | [`Cursor/wiki/overview.md`](../../Cursor/wiki/overview.md) |
| 4 | [`Cursor/wiki/04_источники_и_URL.md`](../../Cursor/wiki/04_источники_и_URL.md) |
| 5 | По слайдам: [`02_DR-A`](../../Cursor/wiki/02_DR-A_бренды_рынок.md) · [`03_DR-B`](../../Cursor/wiki/03_DR-B_вязкости_SAE.md) · [`05_линейка`](../../Cursor/wiki/05_линейка_SKU_СТМ.md) · [`08_PGMM`](../../Cursor/wiki/08_PGMM_упаковка.md) · [`54`](../../Cursor/wiki/54_название_СТМ_Eliten.md) · [`55`](../../Cursor/wiki/55_визуал_эскизы_Eliten.md) |
| 6 | [`../Оглавление_и_каркас.md`](../Оглавление_и_каркас.md) |
| 7 | Нормативка: `01_DR_…/декомпозиция/06_F0b_правовой_блок_диплом.md` |

---

## PATCH BLOCK P7-19…24 (добавить к v2)

| ID | Патч |
|----|------|
| **P7-19** | **Каждая цифра** на слайде — с ID из `wiki/04` (S2-01, BX-02…) или **[н/д]**. URL только из реестра. |
| **P7-20** | **География:** европейская часть = **ЦФО + СЗФО + ЮФО**. DR-B часто **федеральный прокси** — статус «Вывод из материалов» + озвучить в limitations. |
| **P7-21** | **Обязательный слайд:** «Маркировка масел РФ/ЕАЭС — обзор» (из `06_F0b`; CRPT, back label, состав — **Требует проверки** без первичника). В компактной версии 12 слайдов — **не удалять**, объединять с roadmap только если остаётся отдельный блок limitations. |
| **P7-22** | **PGMM/ODSA на слайде 10:** различать **artifact** (retail photo) и **canonical SKU** (site triangulation). API: **SP > SN > SL**. Не цитировать фото как канон. |
| **P7-23** | **Три термина (не смешивать):** (1) **PGMM/ODSA якорь** — Classic Protect **5W-40 4L** (+1L doliv), deepest audit, white space §6; (2) **Этап 6 план→факт** — min **2 mockup** (5W-40), факт **8/8** rev.2; (3) **Запуск** — `Roadmap_запуска_СТМ.md` **3 волны**, не «пилот = launch». |
| **P7-24** | **Eliten** = словесный знак **RU 1172689** (этап 5). **ELITEN™** на mockup — typographic; не equate с legal clearance launch. FIPS = **Подтверждено материалами** (регистрация); продажа/маркировка = **Требует проверки**. |
| **P7-25** | **Roadmap Ф2 ✅:** ориентир **ЛУКОИЛ Торжок** (ex-Shell 2022) · front **8/8** · фасовка Modern 0W-20 **5L+1L**, 5W-30 **4L+1L**, Classic **4L+1L**. **Ф3** — next steps · outside thesis. Torzhok = orientir, не контракт. |

### P7-19…25 — точные формулировки в prompt

```
ДОПОЛНИТЕЛЬНЫЕ ПРАВИЛА (FINAL · поверх Master Prompt v2):

19. SOURCE IDs: каждая цифра — [ID из wiki/04] или н/д. Без ID цифру не включать.

20. GEOGRAPHY: ЦФО+СЗФО+ЮФО; DR-B proxy — явно в limitations.

21. NORMATIVE SLIDE: обязателен слайд маркировки РФ/ЕАЭС (06_F0b); не выдумывать нормы.

22. PGMM CANON: artifact vs canonical SKU; triangulation перекрывает legacy photo.

23. THREE TERMS: PGMM anchor 5W-40 4L (+1L) · этап 6 min 2 mockups → fact 8/8 · launch = Roadmap 3 waves (NOT pilot-only launch).

24. ELITEN / Eliten: ТЗ Eliten RU 1172689; mockup ELITEN™; FIPS ≠ launch clearance.

25. ROADMAP F2: LUKOIL Torzhok blender orientir · front 8/8 fasovka matrix · F3 marketing outside thesis; no signed contract claim.

КОМПАКТНАЯ ВЕРСИЯ (default): 12–13 содержательных слайдов.
- Слайд 2: «Актуальность и цель» (не «управленческая проблема» без материала).
- Слайд 9: Eliten + DDx Verum/Calibr (этап 5).
- Слайд 8 ≠ слайд 10: 8 = конкуренты на полке; 10 = white space + ODSA audit.
- Сумма speaker notes ≤ 13 мин.

DELIVERABLE: markdown deck-spec (таблица §10 v2) + карта материалов (§3) + приложения (§12) + риски (§13) + Q&A (§14) + self-check (§15).
```

---

## Сводка патчей P7-01…18 (поглощены v2)

Патчи v1 в основном закрыты в Master Prompt v2 (§3–15). Не дублировать, кроме случаев, где P7-19…24 уточняют проектный канон.

---

## Приложения — пути файлов проекта

| Прил. | Содержание | Путь |
|-------|------------|------|
| А | PGMM+ODSA 5W-40 (6×18) | `03_PGMM_ODSA_…/матрица_PGMM_ODSA_5W-40.md` |
| Б | PGMM+ODSA 0W-20 (4×18) | `03_PGMM_ODSA_…/матрица_PGMM_ODSA_0W-20.md` |
| В | DR-промпты (выдержки) | `00_таксономии_…/` |
| Г | Mockups rev.2 (8 PNG) | `05_…/финал/* rev 2.png` |
| Д | URL + FIPS | `wiki/04` · `04_DD_ODSA_…/FIPS/` |
| Е | Prompts этап 6 | `05_…/prompt_for_img_*_final.md` |
| Ж | Claims requiring validation | реестр из §13 v2 |

---

## Чеклист качества (FINAL)

См. [`P7_Red_Team_v2.md`](P7_Red_Team_v2.md) § Self-check + пункты P7-19…24.

---

## После исполнения

1. Self-check §15 v2 + P7-19…24.
2. Репетиция ≤13 мин speaker notes.
3. Spot-check цифр vs wiki/02, 03, overview.
4. PPTX + PDF приложений.

---

## История версий

| Версия | Дата | Изменение |
|--------|------|-----------|
| FINAL rev.1 | 28.06 | v1 oracle + P7-01…18 |
| **FINAL rev.2** | 28.06 | **v2 oracle (усиленный) + P7-19…24** |
