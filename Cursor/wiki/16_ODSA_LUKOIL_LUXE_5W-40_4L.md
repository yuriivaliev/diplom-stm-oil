# ODSA — LUKOIL LUXE 5W-40 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_LUKOIL_LUXE_5W40_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 (Copilot) · Depth: Compact  
**Связь PGMM:** [10_PGMM_LUKOIL_LUXE_5W-40.md](10_PGMM_LUKOIL_LUXE_5W-40.md)  
**Дата:** 23.06.2026 · **Rev. 3:** 23.06.2026 (фронт SN/CF подтверждён фото)  
**Формат:** 4L · фронт + оборот + сайт производителя

---

## Executive summary (rev. 3)

**Канон текущего SKU** (EVID-L10 + L09 + L03–L05): **LUKOIL LUXE Synthetic 5W-40 4L**, **API SN/CF**, «**СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» — **согласовано на фронте, обороте и официальном сайте**.

**CR-L01 / CR-L02 закрыты:** EVID-L01 (API SL/CF, полусинтетика, ActiPure) — **предшествующая ревизия** в рамках эволюции линейки LUXE 5W-40, не ошибка split-face текущего SKU.

**Методологическая рамка:** в рамках одного продуктового имени допустима **эволюция допуска** (SL→SN) и базы (semi→syn) при relabeling; для аудита фиксируется **rev. date / визуальный маркер** (LUXE **SYNTHETIC** vs legacy без SYNTHETIC).

**Актуальные findings:** OEM на физическом фронте канистры по-прежнему **не видны с полки** (F-L03); **ActiPure** — риск только для legacy-остатков (F-L05 ↓); **transitional inventory risk** — на полке возможны обе ревизии (F-L10, new).

| Severity rollup (rev. 2) | Count |
|--------------------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 3 |
| Minor | 3 |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-L01 | Artifact | Фото фронт 4L (legacy) | «ПОЛУСИНТЕТИЧЕСКОЕ»; **API SL/CF**; ActiPure | C | **Deprecated** — устаревшая ревизия |
| EVID-L02 | Artifact | EVID-L01 | ActiPure + «ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ» | C | Deprecated (legacy front) |
| EVID-L03 | Artifact | Фото оборот 4L | **API SN/CF**; 5W-40 | A | Active |
| EVID-L04 | Artifact | EVID-L03 | API SN/CF; ACEA A3/B4, A3/B3; MB 226.5/229.3; VW 502 00/505 00; Fiat 9.55535-N2; Renault RN 0700/0710; PSA B71 2296; ПАО «АВТОВАЗ» | A | Active |
| EVID-L05 | Artifact | EVID-L03 | «**синтетическое** моторное масло… API SN/CF» | A | Active |
| EVID-L06 | Artifact | EVID-L03 | ООО «ЛЛК-Интернешнл»; ISO 9001:2015, IATF 16949:2016 | A | Active |
| EVID-L07 | Context | Оператор (текст запроса) | Спецификации = EVID-L04 | B | Active |
| EVID-L08 | Artifact | [10_PGMM_LUKOIL_LUXE_5W-40.md](10_PGMM_LUKOIL_LUXE_5W-40.md) | PGMM: «Полусинтетика, API SL» | B | **Stale** — требует refresh |
| EVID-L09 | Artifact | [lukoil-masla.ru ProductCard](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-luxe-synthetic-5w-40) | «LUXE **SYNTHETIC**»; рендер **API SN/CF**; specs = EVID-L04 | A | Canonical |
| EVID-L10 | Artifact | Фото фронт 4L (current) | «LUXE **SYNTHETIC**»; «**СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**»; **API SN/CF**; 5W-40; 4L | A | **Active — primary shelf face** |

### Conflict note (resolved)

| Conflict | Evidence for | Resolution |
|----------|--------------|------------|
| SL front vs SN back | EVID-L01 vs L03–L10 | **Product evolution** SL→SN; current wrap **consistent** (L10 = L03–L05 = L09) |
| PGMM semi vs ODSA syn | EVID-L08 vs L10 | PGMM on legacy rev.; **re-run PGMM on EVID-L10** recommended |

### Product evolution log (operator consensus)

| Rev. | Front marker | API | Base oil claim | Status |
|------|--------------|-----|----------------|--------|
| Legacy | LUXE (без SYNTHETIC); ActiPure | SL/CF | Полусинтетическое | EVID-L01 · снято с производства / остатки |
| **Current** | LUXE **SYNTHETIC** | **SN/CF** | Синтетическое | EVID-L10 · канон |

> Эволюция допуска в рамках одного продуктового имени — **нормальный industry pattern**; не классифицируется как packaging defect при согласованном current wrap.

### Data gaps (updated)

| Gap | Статус |
|-----|--------|
| GAP-L01 Ревизия фронт+оборот | **Closed** — EVID-L10 front = EVID-L03–L05 back |
| GAP-L02 TDS / ActiPure | Open (ActiPure irrelevant для current SYNTHETIC line?) |
| GAP-L03 OEM certificates | Open |
| GAP-L04 Доля legacy SL на полке РФ | Open — н/д |

---

## Findings Catalogue

### F-L01 — ~~Blocker~~ **Closed** · API SL vs SN — legacy front, не split-face

| Поле | Значение |
|------|----------|
| **Observation** | EVID-L01: API SL/CF (legacy). EVID-L10 (current front), L03–L05, L09: **API SN/CF** — согласовано. |
| **Evidence IDs** | EVID-L01; EVID-L03; EVID-L04; EVID-L09; **EVID-L10** |
| **Interpretation** | Эволюция допуска SL→SN в рамках LUXE 5W-40; **current wrap coherent**. Риск — только **legacy inventory** (F-L10). |
| **Severity (rev. 2)** | ~~Blocker~~ → **Closed** · Confidence **High** |
| **Recommendations** | governance: при аудите фиксировать дату/ревизию этикетки; не смешивать legacy и current в одной строке матрицы |

---

### F-L02 — **Closed** · Semi vs Syn — та же ревизионная смена

| Evidence IDs | EVID-L01; EVID-L05; EVID-L09; **EVID-L10** |
| **Resolution** | Канон: **синтетическое** (front L10 + back + site). Legacy — полусинтетика. |
| **Severity** | Closed |

---

### F-L03 — Major · OEM-стек не на фронте канистры (current SKU)

| Поле | Значение |
|------|----------|
| **Observation** | OEM-список (EVID-L04) на обороте и на сайте (EVID-L09); на **текущем фронте** (EVID-L10) — только API SN/CF, 5W-40, 4L. |
| **Evidence IDs** | EVID-L04; EVID-L09; **EVID-L10** |
| **Impact** | Revenue · Trust (OEM-driven выбор) |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | quick: 1–2 top OEM icons на фронт канистры |

---

### F-L04 — Major · PGMM wiki/10 contaminated (stale SKU)

| Поле | Значение |
|------|----------|
| **Observation** | Wiki/10: API SL, semi, ActiPure (legacy rev.). Канон (L10): **LUXE SYNTHETIC, SN/CF**. |
| **Evidence IDs** | EVID-L08; EVID-L09; **EVID-L10** |
| **Interpretation** | PGMM-анализ визуала **частично валиден** (armor paradigm), но **product claims layer устарел**. |
| **Severity & Confidence** | **Major** (methodological) · **High** |
| **Recommendations** | Re-run PGMM full на фото/рендер **LUXE SYNTHETIC**; обновить wiki/10 |

---

### F-L05 — Moderate → **Minor (legacy only)** · ActiPure

| Observation | ActiPure на **legacy** фронте (EVID-L02). На каноне LUXE **SYNTHETIC** (L09) — брендинг сменён. |
| **Severity (rev. 2)** | **Minor** · только для остатков legacy |

---

### F-L06 — Moderate · «УНИВЕРСАЛЬНОЕ МАСЛО» — legacy front

| Note | На current site — «СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО»; F-L06 applies to EVID-L01 legacy only |

---

### F-L07 — Moderate · ACEA A3/B3 + A3/B4

| Evidence IDs | EVID-L04; EVID-L09 |
| Unchanged |

---

### F-L08 — Minor · ISO/IATF

| Evidence IDs | EVID-L06 |

---

### F-L09 — Minor · 5W-40 / 4L / API SN — консистентны (positive)

| Evidence IDs | EVID-L03; EVID-L04; EVID-L09; **EVID-L10** |
| **Observation** | 5W-40, 4L, **API SN/CF** согласованы на **front + back + site** |

---

### F-L10 — Major · Transitional inventory / dual-revision shelf risk

| Поле | Значение |
|------|----------|
| **Observation** | Одновременно в обращении legacy (SL/semi/ActiPure, EVID-L01) и current (SN/synthetic, EVID-L09). |
| **Evidence IDs** | EVID-L01; EVID-L09; EVID-L10 |
| **Interpretation** | Покупатель на полке может получить **разный продукт** при одном брендовом имени «LUXE 5W-40». |
| **Impact** | Trust · Safety · Legitimacy |
| **Severity & Confidence** | **Major** · **Medium** (доля legacy н/д) |
| **Confounds** | Разные SKU в одной линейке (LUXE semi vs LUXE Synthetic — отдельные карточки на сайте) |
| **Falsification** | Retail audit: % facings SL vs SN; дата производства на канистрах |
| **Recommendations** | governance: для СТМ — явное versioning на этикетке при reformulation |

---

## Contradiction Register (rev. 2)

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-L01 | API SL ↔ API SN | **Closed** — evolution; current front **SN/CF** (L10) |
| CR-L02 | Semi ↔ Syn | **Closed** — evolution; current front **SYNTHETIC** (L10) |
| CR-L03 | OEM back only ↔ shelf | **Open** — F-L03 |
| CR-L04 | PGMM/10 ↔ canonical SKU | **Open** — F-L04, needs PGMM refresh |

---

## POV-маркировка (rev. 2)

**Information Integrity:** **Contamination** снята для current SKU (L09); **остаётся** в PGMM/10 и legacy photo. **Lacunae:** GAP-L03, GAP-L04.

**Logical Coherence:** CR-L01/02 closed; canonical claims **coherent** (SN + synthetic + OEM list).

**System Dynamics:** **Anomaly** → **transition** semi→syn relabel; **Potential** для СТМ — явный API/OEM на фронте при смене рецептуры.

**Relational States:** **Consensus** оператор + site + back = SN/CF.

---

## Строка для сводной матрицы (ODSA × PGMM) — rev. 3

| Параметр | LUKOIL LUXE 5W-40 4L (current) |
|----------|--------------------------------|
| Product line | **LUXE SYNTHETIC** |
| API (front / back) | **SN/CF · SN/CF** |
| Base oil claim | **Синтетическое** (front + back) |
| Approval evolution | SL/CF semi → SN/CF syn (legacy EVID-L01) |
| OEM on front | **Нет** |
| OEM (back / site) | VW, MB, Renault, PSA, Fiat, AVTOVAZ, ACEA |
| Legacy shelf risk | SL/semi/ActiPure facings possible (F-L10) |
| Cross-face consistency | **Pass** |
| PGMM wiki/10 | **Stale** — refresh on EVID-L10 |
| PGMM paradigm (visual) | Solid/Armor — likely persists |

---

## Импликации для СТМ (rev. 2)

1. При reformulation — **version bump** на этикетке, не silent relabel.
2. OEM на **физический фронт** канистры (LUKOIL не делает — white space для СТМ).
3. Обновить **PGMM full** под LUXE Synthetic перед финальной матрицей.
4. В матрице — строка **canonical SN**; footnote **legacy SL** если retail audit найдёт остатки.

---

## Issues for discussion

1. Перепрогон **PGMM full** на EVID-L10 (LUXE SYNTHETIC front).
2. В матрице: одна строка **current** + footnote legacy evolution vs отдельная строка legacy.
3. URL lukoil-masla.ru → wiki/04 после верификации.

**DoD:** ODSA LUKOIL 5W-40 4L — **complete** (rev. 3). Pending: PGMM/10 refresh, GAP-L03–04.
