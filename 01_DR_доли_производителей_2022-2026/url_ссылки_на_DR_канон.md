# URL из ChatGPT DR → канон для диплома

**Исходник:** `url_ссылки на DR.xlsx` (экспорт ссылок из чата Deep Research).  
**Обработка:** 27.05.2026 — сопоставление с `A_URL_реестр_run2.md`.  
**Правило:** в дипломе — колонка **URL для сноски** (без `utm_source`, `srsltid`).

---

## Сводка импорта из xlsx

| Результат | Кол-во |
|-----------|--------|
| Совпадает с верификацией, использовать как есть | 11 |
| ChatGPT URL тот же, но **тема/страница неверны** | 2 |
| ChatGPT дал **мусорный URL** — заменён | 2 |
| Добавлен URL, которого не было в xlsx | 3 |

**Вывод:** экспорт ChatGPT **не дал** отдельной ссылки на «доли континентов» — снова `54390` (статья про **цены**, не 71%/46%).

---

## Таблица (источник DR → сноска диплома)

| № | Источник (из DR) | URL в xlsx (ChatGPT) | Статус | URL для сноски (канон) | ID |
|---|------------------|----------------------|--------|------------------------|-----|
| 1 | Aftermarket-DATA LCV 2023 | aftermarket-data.ru/motor_masla?utm_source=… | ✅ | https://www.aftermarket-data.ru/motor_masla | S2-01 |
| 2 | A-KT / GfK | a-kt.ru/…/rynok-motornykh-masel…?utm_source=… | ✅ | https://a-kt.ru/articles/rynok-motornykh-masel-my-budem-zhit-teper-po-novomu | V1-01 |
| 3 | АВТОСТАТ 300 млн л | autostat.ru/news/43499/ | ✅ | https://www.autostat.ru/news/43499/ | AS-01 |
| 4 | Mordor Intelligence | mordorintelligence.com/…?utm_source=… | 🟡 403 | https://www.mordorintelligence.com/ru/industry-reports/russia-automotive-engine-oils-market | CTX-01 |
| 5 | АВТОСТАТ «континенты» | **infographics/54390/** | 🔴 не та статья | *см. AS-05 для цен*; континенты — **URL не найден в xlsx** | AS-02 / AS-05 |
| 6 | АВТОСТАТ импортёры 2024 | infographics/60301/ | ✅ | https://www.autostat.ru/infographics/60301/ | AS-03 |
| 7 | Shell media statements | shell.com/media-statements… | 🟡 общий | https://shell.gcs-web.com/news-releases/news-release-details/shell-announces-intent-withdraw-russian-oil-and-gas | SH-03 |
| 8 | Reuters Shell–LUKOIL | reuters.com/…?utm_source=… | 🟡 paywall | https://www.reuters.com/business/energy/shell-sells-russian-retail-business-lukoil-2022-05-12/ | SH-02 |
| 9 | ExxonMobil РФ | **bing.com/search?…** | ⛔ мусор | https://corporate.exxonmobil.com/news/news-releases/2022/0301_exxonmobil-to-discontinue-operations-at-sakhalin-1_make-no-new-investments-in-russia | EX-01 |
| 10 | Castrol / Известия | iz.ru/1330440/… | ✅ | https://iz.ru/1330440/2022-05-05/castrol-ostanovil-postavki-motornogo-masla-v-rossiiu | CA-01 |
| 11 | TotalEnergies | totalenergies.com/…?utm_source=… | ✅ | https://totalenergies.com/newsroom/russia-totalenergies-shares-its-principles-conduct/?lang=eng | TO-01 |
| 12 | Motul | mymotul.ru?srsltid=… | ✅ | https://mymotul.ru/ | MO-01 |
| 13 | Честный знак | честныйзнак.рф/…/marking/?utm_source=… | 🟡 | https://честныйзнак.рф/business/projects/autofluids/marking/ + https://docs.crpt.ru/gismt/…автозапчасти/ | MK-05 / MK-04 |
| 14 | Парк по ФО | infographics/55594/ | ✅ | https://www.autostat.ru/infographics/55594/ | AS-04 |
| 15 | SINTEC AGR | sintecgroup.ru/…agr/ | ✅ | https://sintecgroup.ru/news/sintec_lubricants_postavila_svyshe_500_tysyach_litrov_avtomasel_pod_brendom_agr/ | STM-01 |
| 16 | Kolesa / Nielsen | kolesa.ru/…rastush**h**em… | ✅ | https://www.kolesa.ru/news/na-rastushhem-rynke-motornyx-masel-v-rf-liderstvo-prodolzaiut-uderzivat-rossiiskie-brendy | NL-01 |
| 17 | LIQUI MOLY пресс | 800 млн sales PR | 🔴 не уход из РФ | https://www.liqui-moly.com/en/us/company/about-us/company-history.html | LM-02 |
| 18 | Коммерсантъ MZD | kommersant.ru/doc/7713657 | ✅ | https://www.kommersant.ru/doc/7713657 | KM-01 |
| 19 | Autonews / ЦРПТ — 81% отечеств. масла+жидкости | — (добавлено 16.06.2026) | ✅ | https://www.autonews.ru/news/69b159ea9a7947d9d5b8eb61 | **CZ-01** |

**CZ-01:** доля **отечественного vs импортного** предложения по данным маркировки (масла **+** автожидкости, **единицы SKU**), **не** brand share и **не** литры. Tier 2 (РБК Autonews → пресс-служба ЦРПТ).

---

## Что исправить в xlsx (опционально)

1. **Строка 9 Exxon** — заменить Bing на EX-01 URL.  
2. **Строка 5 «континенты»** — либо переименовать в «цены 54390» (AS-05), либо вставить URL из клика по `turn9view0` в чате DR.  
3. **Строка 17 LIQUI MOLY** — заменить на LM-02.  
4. **Строка 7 Shell** — заменить на SH-03.  
5. Удалить во всех ячейках: `?utm_source=chatgpt.com`, `srsltid=…`.

---

## Копировать в список литературы (кратко)

```
[1] Aftermarket-DATA. Моторные масла для легковых и LCV. Февр. 2024. URL: https://www.aftermarket-data.ru/motor_masla (дата обращения: 27.05.2026).
[2] A-KT. Рынок моторных масел: «Мы будем жить теперь по-новому». 22.03.2024. URL: https://a-kt.ru/articles/rynok-motornykh-masel-my-budem-zhit-teper-po-novomu (27.05.2026).
…
```

Полный реестр с HTTP-проверкой: `A_URL_реестр_run2.md`.

---

## Пакет 2 — ваш скриншот (строки 9–18), проверка 27.05.2026

| № | URL из ChatGPT | Вердикт | URL для диплома (канон) | ID |
|---|----------------|---------|-------------------------|-----|
| 9 | bing.com/…ExxonMobil+Russia… | ⛔ **не источник** | https://corporate.exxonmobil.com/news/news-releases/2022/0301_exxonmobil-to-discontinue-operations-at-sakhalin-1_make-no-new-investments-in-russia | EX-01 |
| 10 | iz.ru/…castrol…?utm_source=… | ✅ | https://iz.ru/1330440/2022-05-05/castrol-ostanovil-postavki-motornogo-masla-v-rossiiu | CA-01 |
| 11 | totalenergies.com/…?utm_source=… | ✅ | https://totalenergies.com/newsroom/russia-totalenergies-shares-its-principles-conduct/?lang=eng | TO-01 |
| 12 | mymotul.ru?srsltid=…&utm_source=… | ✅ | https://mymotul.ru/ | MO-01 |
| 13 | честныйзнак.рф/…/marking/?utm_source=… | 🟡 403 у бота; **в браузере ок** | https://честныйзнак.рф/business/projects/autofluids/marking/ | MK-05 |
| 14 | autostat.ru/infographics/55594/ | ✅ | https://www.autostat.ru/infographics/55594/ | AS-04 |
| 15 | sintecgroup.ru/…agr/?utm_source=… | ✅ | https://sintecgroup.ru/news/sintec_lubricants_postavila_svyshe_500_tysyach_litrov_avtomasel_pod_brendom_agr/ | STM-01 |
| 16 | kolesa.ru/…rastushhem…?utm_source=… | ✅ | https://www.kolesa.ru/news/na-rastushhem-rynke-motornyx-masel-v-rf-liderstvo-prodolzaiut-uderzivat-rossiiskie-brendy | NL-01 |
| 17 | liqui-moly.com/…800-million…?srsltid=… | 🔴 **не про уход из РФ** | https://www.liqui-moly.com/en/us/company/about-us/company-history.html | LM-02 |
| 18 | kommersant.ru/doc/7713657?utm_source=… | ✅ | https://www.kommersant.ru/doc/7713657 | KM-01 |

### Кратко по каждой строке скриншота

**9 Exxon (Bing)** — заменить на EX-01; в xlsx вставить corporate URL.

**10 Castrol** — рабочая; остановка поставок 05.05.2022; tier 2.

**11 TotalEnergies** — рабочая; principles of conduct по России; tier 1.

**12 Motul** — рабочая; канал РФ; tier 3; убрать `srsltid` и utm.

**13 Честный знак** — откройте у себя в Chrome; дубль для нормативки: https://docs.crpt.ru/gismt/Инструкция_по_маркировке_тг_автозапчасти/ (MK-04).

**14 Парк по ФО** — рабочая; ЦФО 28,6%, СЗФО 10,2%, ЮФО 10,1%; парк на 01.07.2023; прокси для «европейской части».

**15 SINTEC AGR** — рабочая; 500+ тыс. л, 300+ СТО; кейс СТМ tier 1.

**16 Kolesa** — рабочая; Nielsen 06.2024–05.2025; tier 3; slug **rastushhem** верный.

**17 LIQUI MOLY** — PR про выручку €800 млн **не** заменяет тезис «уход из РФ» → только **LM-02** history.

**18 Коммерсантъ** — рабочая; Mazda / бренд **MZD** для РФ; tier 2.

---

## Все 18 URL — готовый блок для списка литературы (без utm)

```
https://www.aftermarket-data.ru/motor_masla
https://a-kt.ru/articles/rynok-motornykh-masel-my-budem-zhit-teper-po-novomu
https://www.autostat.ru/news/43499/
https://www.mordorintelligence.com/ru/industry-reports/russia-automotive-engine-oils-market
https://www.autostat.ru/infographics/54390/
https://www.autostat.ru/infographics/60301/
https://shell.gcs-web.com/news-releases/news-release-details/shell-announces-intent-withdraw-russian-oil-and-gas
https://www.reuters.com/business/energy/shell-sells-russian-retail-business-lukoil-2022-05-12/
https://corporate.exxonmobil.com/news/news-releases/2022/0301_exxonmobil-to-discontinue-operations-at-sakhalin-1_make-no-new-investments-in-russia
https://iz.ru/1330440/2022-05-05/castrol-ostanovil-postavki-motornogo-masla-v-rossiiu
https://totalenergies.com/newsroom/russia-totalenergies-shares-its-principles-conduct/?lang=eng
https://mymotul.ru/
https://честныйзнак.рф/business/projects/autofluids/marking/
https://www.autostat.ru/infographics/55594/
https://sintecgroup.ru/news/sintec_lubricants_postavila_svyshe_500_tysyach_litrov_avtomasel_pod_brendom_agr/
https://www.kolesa.ru/news/na-rastushhem-rynke-motornyx-masel-v-rf-liderstvo-prodolzaiut-uderzivat-rossiiskie-brendy
https://www.liqui-moly.com/en/us/company/about-us/company-history.html
https://www.kommersant.ru/doc/7713657
https://www.autonews.ru/news/69b159ea9a7947d9d5b8eb61
```

**Не внесено в блок:** отдельный URL «континенты 71%/46%» — в экспорте ChatGPT не найден (ошибочно 54390).
