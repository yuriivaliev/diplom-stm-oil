# Реестр URL — верификация DR-B run1

**Отчёт:** `отчёт_DR-B_run1.md` (Deep Research, Oracle-промпт)  
**Дата верификации:** 27.05.2026  
**Метод:** HTTP GET (User-Agent Mozilla) + сверка с текстом отчёта

---

## Сводка

| Статус | Кол-во | Действие |
|--------|--------|----------|
| ✅ Использовать в дипломе | 16 | Канон URL + tier в сноске |
| 🟡 С оговоркой | 2 | NI-PDF (пересказ Nielsen); B2X = retail-proxy, не синт+полусинт-only |
| 🔴 Заменить | 0 | — |
| ⛔ Не использовать | 0 | Минералка в отчёте **не** включена ✅ |

**Приёмка отчёта (чеклист):** географический прокси промаркирован ✅ · GATE описан ✅ · 0W-20 + Китай ✅ · SKU СТМ 3–5 ✅ · DR-A без таблиц брендов ✅ · Таблица 0 (н/д по target) ✅

---

## Канонический реестр

| ID | Источник | URL (канонический) | HTTP | Сверка с DR | Tier | Примечание |
|----|----------|-------------------|------|-------------|------|------------|
| **S2-01** | Aftermarket-DATA motor_masla | https://www.aftermarket-data.ru/motor_masla | 200 | ✅ 278 млн л, 196 млрд ₽ (контекст 2023) | 2 | SAE на странице — графики; не машиночитаемо в парсере |
| **BX-01** | B2X — структура по вязкостям (Москва+МО) | https://b2x-lubricants.ru/news/Strukturaroznichnykhprodazhmotornykhmaselpovyazkostyam/ | 200 | ✅ 0W-XX 6%→4%; 10W-40 17% | 3 | Промежуточный; не ЦФО+СЗФО+ЮФО целиком |
| **BX-02** | B2X — 1П2023 РФ + ЮФО 10W-40 49% | https://b2x-lubricants.ru/news/10W40naYUgenulevkinaDalnemVostokeStrukturaroznichnykhprodazhmotornykhmaselpovyazkostyamzavisitotregi/ | 200 | ✅ 5W-30 35%, 5W-40 32%, ЮФО 10W-40 49% | 3 | **Федеральный прокси** для H1/H2 |
| **BX-03** | B2X — тренды 2025/2026, 0W-20 лидер роста | https://b2x-lubricants.ru/news/Trendyvyazkosteymotornykhmaseldlyalegkovykhavtomobiley/ | 200 | ✅ directional 2026 | 3 | Промежуточный |
| **NL-01** | Kolesa — Nielsen пересказ | https://www.kolesa.ru/news/na-rastushhem-rynke-motornyx-masel-v-rf-liderstvo-prodolzaiut-uderzivat-rossiiskie-brendy | 200 | ✅ синтетика, тренды (дубль к NI-PDF) | 3 | Tier понижен: пересказ Nielsen |
| **NI-PDF** | PDF-копия слайдов Nielsen (Tenchat CDN) | https://cdn1.tenchat.ru/static/vbc-gostinder/2025-08-22/993e479e-31e6-4e1d-84f0-8e03658ee93a.pdf | 200 | ✅ 5W-40 51%, 5W-30 45,9%; 0W-20 рост | 3 | 🟡 **Не первичный Nielsen**; доли с легенды графика |
| **KL-02** | Kolesa — китайцы после гарантии, вязкости | https://www.kolesa.ru/article/kitaicy-posle-garantii-osobennosti-podbora-komponentov-posle-uxoda-ot-dilera | 200 | ✅ 0W-20, 0W-30, 5W-30, 5W-40 | 3 | Качественно / H4 |
| **KL-03** | Kolesa — LUKOIL HAVAL/TANK/GWM | https://www.kolesa.ru/news/lukoyl-stal-postavshchikom-masel-dlya-avtobrendov-haval-tank-i-pikapov-gwm | 200 | ✅ OEM-контекст | 3 | Не доля SAE |
| **GE-01** | GEELY — оригинальные масла 0W-20 | https://www.geely-motors.com/for-owners/liquid-oil/ | 200 | ✅ API SP, ACEA C5, 0W-20 | 1 | OEM первичный |
| **AS-CH22** | Autostat — 830 тыс. китайских 01.07.2022 | https://m.autostat.ru/news/52353/ | 200 | ✅ 829,8 тыс., 1,8% | 2 | |
| **AS-CH23** | Autostat — парк >1 млн 01.07.2023 | https://m.autostat.ru/news/55463/ | 200 | ✅ 1,08 млн, 2,4% | 2 | |
| **AS-CH24** | Autostat — 4% парка 01.07.2024 | https://m.autostat.ru/news/58146/ | 200 | ✅ 1,86 млн, 4,0% | 2 | |
| **AS-CH25** | Autostat — ~6% парка 2025 | https://m.autostat.ru/news/60807/ | 200 | ✅ 2,65 млн | 2 | |
| **AS-CH26** | Autostat — 3,15 млн, 6,6% 01.01.2026 | https://m.autostat.ru/news/61599/ | 200 | ✅ (в библиографии п.17) | 2 | Промежуточный 2026 |
| **AS-FO** | Autostat — «китайцы» по ФО | https://www.autostat.ru/infographics/60868/ | 200 | ✅ ЦФО 35,1%, СЗФО 12,6%, ЮФО 10,9% → **58,6%** | 2 | **Прямо по европ. части** |
| **AS-MKT** | Autostat — доля китайцев на рынке новых | https://m.autostat.ru/infographics/53924/ | 200 | ✅ 38,1% РФ; Москва 59,6% (янв.2023) | 2 | |
| **AS-R29** | Autostat — 29 регионов >58% | https://m.autostat.ru/news/58061/ | 200 | ✅ контекст продаж | 2 | |
| **AS-F24** | Autostat — прогноз китайцев 2024 | https://m.autostat.ru/news/59099/ | 200 | ✅ 58% 1П2024 | 2 | |

---

## Сверка цифр SAE (claim → страница)

| SAE / метрика | Значение в DR | ID | Подтверждено | Примечание |
|---------------|---------------|-----|--------------|------------|
| 5W-30 | 35% 1П2023 РФ retail | BX-02 | ✅ | Broad retail, не синт-only |
| 5W-40 | 32% 1П2023 РФ retail | BX-02 | ✅ | То же |
| 10W-40 | 49% 1П2023 ЮФО | BX-02 | ✅ | Регион **внутри** европ. части |
| 5W-40 | 51,0% synthetic 12М→май2025 | NI-PDF | 🟡 | С легенды графика; tier 3 |
| 5W-30 | 45,9% synthetic 12М→май2025 | NI-PDF | 🟡 | Σ с 5W-40 + 3,1% residual |
| 0W-20 | +10,1% л, +16,0% ₽ | NI-PDF / NL-01 | 🟡 | Темпы, не доля |
| 0W-XX | 6%→4% Москва+МО | BX-01 | ✅ | Не чистый 0W-20 |
| GATE 1П2023 | 35+32+33=100% | BX-02 | ✅ | |
| Китай парк ЦФО+СЗФО+ЮФО | 58,6% | AS-FO | ✅ | 01.07.2025 |

---

## Маппинг: библиография DR (№1–18) → ID

| № DR | ID |
|------|-----|
| 1 | S2-01 |
| 2 | BX-01 |
| 3 | BX-02 |
| 4 | BX-03 |
| 5 | NL-01 |
| 6 | KL-02 |
| 7 | KL-03 |
| 8 | GE-01 |
| 9–12, 17 | AS-CH22 … AS-CH26 |
| 13 | AS-FO |
| 14 | AS-MKT |
| 15–16 | AS-R29, AS-F24 |
| 18 | NI-PDF |

---

## Риски для диплома (не URL)

| Риск | Рекомендация в тексте |
|------|------------------------|
| Нет SAE по ЦФО+СЗФО+ЮФО в одной таблице | Оставить как в DR: «открытые данные — федеральный/региональный прокси» |
| B2X ≠ синт+полусинт only | Всегда писать «retail-proxy» / «broad retail» |
| Nielsen через Tenchat PDF | «по данным Nielsen (публичная репликация, 12 мес. до мая 2025)» |
| 51%+45,9% только synthetic slice | Не смешивать с 35%/32% 2023 без пояснения границ |

---

## Итог верификации

| Поле | Значение |
|------|----------|
| Отчёт DR | `отчёт_DR-B_run1.md` |
| URL проверено | **18/18** HTTP 200 |
| GATE | Описан в отчёте ✅ |
| 0W-20 + китайский парк | Подтверждены URL ✅ |
| Федеральный прокси | Промаркирован в отчёте ✅ |
| **Готово к диплому** | ✅ **с оговорками** (прокси, tier Nielsen/B2X) |

**Следующий шаг:** перенести ID в `literature_и_источники.md` (раздел B); при верстке главы — сноски **BX-02**, **NI-PDF**, **AS-FO**, **GE-01**.
