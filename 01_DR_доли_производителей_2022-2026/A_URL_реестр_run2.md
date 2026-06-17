# Реестр URL — верификация DR-A run2 (27.05.2026)

**Метод:** HTTP + заголовок страницы + ключевые слова в HTML (скрипт).  
**Дата обращения для диплома:** 27.05.2026.  
**Связь:** `отчёт_DR-A_run2_GPT55_instant.md`, табл. 8.  
**Импорт из ChatGPT:** `url_ссылки на DR.xlsx` → сводка `url_ссылки_на_DR_канон.md` (27.05.2026).

### Результат сверки с xlsx

| Проблема в xlsx | Канон |
|-----------------|-------|
| ExxonMobil → **bing.com/search** | **EX-01** corporate.exxonmobil.com |
| «Континенты» → **54390** (цены) | **AS-05** для цен; **AS-02** континенты — URL в xlsx **не исправлен** |
| LIQUI MOLY → PR 800 млн € | **LM-02** company-history |
| Shell → media-statements | **SH-03** gcs-web 08.03.2022 |
| `utm_source=chatgpt.com` везде | Удалять в сносках |

---

## Сводка

| Статус | Кол-во | Действие |
|--------|--------|----------|
| ✅ Использовать в дипломе | 13 | URL + tier в сноске |
| 🟡 Открыть вручную в браузере | 5 | Блокировка ботов / таймаут |
| 🔴 Заменить / убрать | 4 | См. таблицу исправлений |
| ⛔ Не использовать | 2 | Битая ссылка / неверная тема |

---

## Канонический реестр (для диплома)

| ID | Источник | URL (канонический) | HTTP | Сверка с DR | Tier | Примечание |
|----|----------|-------------------|------|-------------|------|------------|
| **S2-01** | Aftermarket-DATA — retail 2023 | https://www.aftermarket-data.ru/motor_masla | 200 | ✅ 278 млн л, 196 млрд ₽, LUKOIL 18,1% | 2 | Основной S2 |
| **V1-01** | A-KT — GfK aftermarket | https://a-kt.ru/articles/rynok-motornykh-masel-my-budem-zhit-teper-po-novomu | 200 | ✅ доли 2022 / 11М2023 | 3 | ≠ retail; пересказ GfK |
| **AS-01** | АВТОСТАТ — 300 млн л 2019 | https://www.autostat.ru/news/43499/ | 200 | ✅ якорь ёмкости | 2 | Контекст CAGR |
| **AS-03** | АВТОСТАТ — импортёры 2024 | https://www.autostat.ru/infographics/60301/ | 200 | ✅ топ-3 SK, GS, Shell; 71% = **15 импортёров** | 2 | 🚩 не «континенты» |
| **AS-04** | АВТОСТАТ — парк по ФО | https://www.autostat.ru/infographics/55594/ | 200* | ✅ ЦФО 28,6%, СЗФО 10,2%, ЮФО 10,1% | 2 | Прокси региона; парк 01.07.2023 |
| **AS-05** | АВТОСТАТ — цены масел 2021–2023 | https://www.autostat.ru/infographics/54390/ | 200 | ✅ шок цен +110% LUKOIL | 2 | **Не** доли континентов |
| **EX-01** | ExxonMobil — выход из РФ | https://corporate.exxonmobil.com/news/news-releases/2022/0301_exxonmobil-to-discontinue-operations-at-sakhalin-1_make-no-new-investments-in-russia | 200 | ✅ | 1 | Корпоративный |
| **SH-03** | Shell — withdraw Russia 08.03.2022 | https://shell.gcs-web.com/news-releases/news-release-details/shell-announces-intent-withdraw-russian-oil-and-gas | 🟡 | ✅ lubricants ops | 1 | Таймаут у скрипта — открыть в браузере |
| **SH-02** | Reuters — продажа Shell → LUKOIL | https://www.reuters.com/business/energy/shell-sells-russian-retail-business-lukoil-2022-05-12/ | 🟡 401 | ✅ | 1 | Paywall/бот; дата 12.05.2022 |
| **SH-02alt** | Shell sale (зеркало/обзор) | https://royaldutchshellplc.com/2022/05/12/shell-signs-agreement-to-sell-retail-and-lubricants-businesses-in-russia/ | — | ✅ 411 АЗС | 3 | Если Reuters недоступен |
| **CA-01** | Известия — Castrol | https://iz.ru/1330440/2022-05-05/castrol-ostanovil-postavki-motornogo-masla-v-rossiiu | 200 | ✅ | 2 | СМИ |
| **TO-01** | TotalEnergies — Russia | https://totalenergies.com/newsroom/russia-totalenergies-shares-its-principles-conduct/?lang=eng | 200 | ✅ | 1 | |
| **MO-01** | Motul Russia | https://mymotul.ru/ | 200 | ✅ канал | 3 | Убрать `?srsltid=…` из сноски |
| **STM-01** | SINTEC — AGR 500 тыс л | https://sintecgroup.ru/news/sintec_lubricants_postavila_svyshe_500_tysyach_litrov_avtomasel_pod_brendom_agr/ | 200 | ✅ | 1 | СТМ кейс |
| **NL-01** | Kolesa.ru — Nielsen | https://www.kolesa.ru/news/na-rastushhem-rynke-motornyx-masel-v-rf-liderstvo-prodolzaiut-uderzivat-rossiiskie-brendy | 200 | ✅ синтетика ~60%; ТОП‑5 синт.: LUKOIL 1-й; +2% кат. | 3 | 06.2024–05.2025; пересказ Nielsen |
| **LM-02** | LIQUI MOLY — stop Russia | https://www.liqui-moly.com/en/us/company/about-us/company-history.html | 200 | ✅ «stopped business with Russia» | 1 | **Заменяет** LM-01 |
| **KM-01** | Коммерсантъ — MZD | https://www.kommersant.ru/doc/7713657 | 200 | ✅ Mazda / MZD | 2 | СТМ кейс |
| **MK-04** | ЦРПТ — инструкция маркировки ТГ | https://docs.crpt.ru/gismt/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F_%D0%BF%D0%BE_%D0%BC%D0%B0%D1%80%D0%BA%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B5_%D1%82%D0%B3_%D0%B0%D0%B2%D1%82%D0%BE%D0%B7%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8/ | 200 | ✅ нормативный контур | 1 | Вместо битых crpt.ru/news |
| **MK-05** | Честный знак — раздел (браузер) | https://честныйзнак.рф/business/projects/autofluids/marking/ | 🟡 | ✅ сроки маркировки | 1 | DDoS-Guard у ботов; открыть вручную |
| **CTX-01** | Mordor Intelligence | https://www.mordorintelligence.com/ru/industry-reports/russia-automotive-engine-oils-market | 🟡 403 | контекст 470 млн л | 3 | Cloudflare; только с оговоркой «оценка из отчёта» |
| **CZ-01** | Autonews.ru — ЦРПТ, 81% отечеств. | https://www.autonews.ru/news/69b159ea9a7947d9d5b8eb61 | 200* | ✅ 81% РФ / 19% импорт; 140+34 млн ед. | 2 | WebFetch 16.06.2026; масла+жидкости; не brand share |

\* AS-04 подтверждён через WebFetch; скрипт давал timeout.

---

## Исправления к вашей таблице URL

| Было в реестре пользователя | Вердикт | Что поставить в диплом |
|----------------------------|---------|-------------------------|
| Kolesa `…rastush**c**hem…` | ⛔ **404** | **NL-01:** `…rastush**h**em…` |
| LIQUI MOLY press 800 млн | 🔴 тема не та | **LM-02** company-history (уход из РФ) |
| АВТОСТАТ `54390` как «континенты» | 🔴 **неверная тема** | **AS-05** (цены) или найти turn9 из чата DR |
| Shell `media-statements.html` | 🟡 слишком общий | **SH-03** gcs-web 08.03.2022 |
| `crpt.ru/news/1/2155/` | ⛔ **404** | **MK-04** docs.crpt.ru + **MK-05** в браузере |
| Motul с `srsltid` | 🟡 лишний параметр | https://mymotul.ru/ |

---

## 🔴 Критично: «доли континентов» 71% / 46% (Европа / Азия)

**Ваш URL `infographics/54390/` — это материал про снижение цен**, не про континенты импорта.

Проверено по тексту страницы: заголовок «На рынке моторных масел эксперты отметили начавшееся **снижение цен**»; есть +110% LUKOIL, Mobil, Shell — **полезно для шока 2022**, но **не для 71%/46%**.

**Цифры 71%/46%/53% (2021–2022 по континентам)** в open web **не привязаны** к найденному публичному URL. В DR они идут из `turn9view0` (24.10.2024).

**Не путать с AS-03:** в [60301](https://www.autostat.ru/infographics/60301/) **71%** — это доля **15 крупнейших импортёров** в объёме импорта **2024**, не доля Европы в 2021.

### Что сделать (5 мин, без токенов DR)

1. В **исходном чате** Deep Research Instant кликнуть сноску `turn9view0` → скопировать реальный URL → внести в строку **AS-02** ниже.  
2. Если URL не открывается: в дипломе писать *«по данным АВТОСТАТ (окт. 2024, платный/закрытый контур)»* или снизить tier до 3 с пометкой «не верифицирован open URL 27.05.2026».  
3. Для **ценового шока** использовать **AS-05** (54390) — верифицирован.

```
AS-02 (континенты 2021–2022): URL = _________  ← из ChatGPT turn9view0
```

---

## Ручная доверка (2 мин в браузере)

Откройте только если скрипт дал 🟡:

- [ ] SH-03 Shell gcs-web  
- [ ] SH-02 Reuters (или SH-02alt)  
- [ ] MK-05 честныйзнак.рф  
- [ ] CTX-01 Mordor (опционально)  
- [ ] AS-02 континенты — из чата DR  

---

## Маппинг на табл. 8 отчёта DR

| № табл. 8 DR | ID реестра |
|--------------|------------|
| 1 Aftermarket-DATA | S2-01 |
| 2 Автостат 300 млн | AS-01 |
| 3 A-KT | V1-01 |
| 4 «Континенты» | AS-02 ⚠ или turn9 |
| 5 Импортёры 2024 | AS-03 |
| 6–9 Shell / Reuters / Exxon / Total | SH-03, SH-02, EX-01, TO-01 |
| 10 LIQUI MOLY | **LM-02** (не 800 млн PR) |
| 11 Kolesa Nielsen | NL-01 |
| 12 Честный знак | MK-04 + MK-05 |
| 13 Коммерсантъ MZD | KM-01 |
| 14 SINTEC AGR | STM-01 |
| 15 Парк ФО | AS-04 |
| 16 ЦРПТ 81% отечеств. (Autonews) | **CZ-01** |

---

**Следующий шаг:** вставить канонические URL в `literature_и_источники.md` и при верстке главы «Рынок» — сноски по ID (S2-01, V1-01, …).
