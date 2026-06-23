# ODSA — Gazpromneft Premium N 5W-40 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_GPN_PREMIUM_N_5W40_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 (Copilot) · Depth: Compact  
**Связь PGMM:** [11_PGMM_Gazpromneft_Premium_N_5W-40.md](11_PGMM_Gazpromneft_Premium_N_5W-40.md) · delta 1L: [15_…](15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md)  
**Дата:** 23.06.2026 · **Rev.:** 2 (GPN-01 locked · Firecrawl ingest attempt)  
**Формат:** 4L · фронт + оборот + официальный сайт  
**Статус:** ✅ **Locked** (DC-EP:A) · pending: GAP-G03 retail shelf photo

**Canonical URL:** [GPN-01](04_источники_и_URL.md) · `https://gazpromneft-oil.ru/ru/products/cars/gazpromneft-premium-n-5w-40` · **verified** 23.06.2026

---

## Executive summary (rev. 2)

**Канон SKU** (EVID-G01 + G04 + G05 + **G10–G12**): **Gazpromneft Premium N Synthetic 5W-40 4L**, **API SN/CF**, «**СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО**» — **согласовано на фронте, обороте и официальном сайте (GPN-01)**.

**Rev. risk закрыт:** оператор **повторно** подтверждает — **упаковка не менялась** (G13, G15); рендер GPN-01 **= ART-001**; штамп 2022 (G07) = валидный proxy текущего wrap.

**Digital triangulation:** specs G11 из operator screenshot (ART-005) = канон GPN-01. Auto-scrape Firecrawl/browser **23.06.2026 failed** (GPN bot-block / proxy timeout) — **не меняет** выводы rev. 1.

**Cross-face consistency:** **Pass** — нет split-face дефекта уровня LUKOIL SL/SN (wiki/16).

**Актуальные findings:** (1) OEM на фронте **есть**, но в **слепой зоне** читаемости (F-G03); (2) **digital superset** — сайт декларирует расширенный OEM-стек (MB 226.5, GM, Porsche, BMW, ACEA A3/B3, УМЗ), **не видимый** на физической этикетке (F-G04); (3) Renault **RN700/RN710** (front + site) vs **RN0700/RN0710** (back) — **нотационная** разница, не конфликт допуска (F-G02, CR-G01 closed).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 3 |
| Minor | 3 |

---

## Configuration (implicit operator consent + data drop)

| BP | Choice | Rationale |
|----|--------|-----------|
| BP-01 | **A** Diagnostic | Claims audit для матрицы этапа 4 |
| BP-02 | **A** Positioning & comms | Claims / proof / channel fit |
| BP-04 | **A** Compact | Parity wiki/16 |
| BP-05 | **B** Mixed | Packet #1 → #2 site triangulation |
| BP-07 | **A** Memo | Executive + Findings catalogue |

---

## Artifact Registry

| ART | Type | Source | Description | Privacy |
|-----|------|--------|-------------|---------|
| ART-001 | Artifact (photo) | Оператор 23.06.2026 | Фронт 4L Premium N 5W-40 | Public |
| ART-002 | Artifact (photo) | Оператор 23.06.2026 | Оборот 4L — specs, код, штамп 2022 | Public |
| ART-003 | Document | wiki/11 | PGMM full 4L | Internal |
| ART-004 | Document | wiki/15 | PGMM delta 1L | Internal |
| **ART-005** | **Artifact (screenshot)** | Оператор 23.06.2026 | Страница GPN-01: рендер + блок «Спецификации» | Public |
| **ART-006** | **Context** | Оператор 23.06.2026 | «Упаковка не менялась» — operator attestation | Internal |
| **ART-007** | **Context** | Firecrawl MCP 23.06.2026 | Scrape GPN-01: proxy/timeout — site bot-protected | Internal |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-G01 | Artifact | ART-001 | «PREMIUM N»; «СИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО»; **API SN/CF**; **ACEA A3/B4**; **5W-40**; **4L** | A | Active |
| EVID-G02 | Artifact | ART-001 | Подвал фронта: MB-Approval **229.3**; Renault **RN700/RN710**; VW 502 00/505 00; PSA B71 2296; **AVTOVAZ** | B | Active |
| EVID-G03 | Artifact | ART-001 | «УНИКАЛЬНАЯ СИСТЕМА ПРОВЕРКИ ПОДЛИННОСТИ (СМ. НА ОБОРОТЕ)» | A | Active |
| EVID-G04 | Artifact | ART-002 | **API SN/CF**; ACEA A3/B4; MB **229.3**; Renault **RN0700/RN0710**; VW 502 00/505 00; PSA B71 2296; ПАО «АВТОВАЗ»; **СТО 84035624-179-2015** | A | Active |
| EVID-G05 | Artifact | ART-002 | Синтетическое всесезонное масло; бензин + дизель; легковые/SUV/LCV | A | Active |
| EVID-G06 | Artifact | ART-002 | «**УНИКАЛЬНЫЙ КОД**»; проверка **3662.ru** | A | Active |
| EVID-G07 | Artifact | ART-002 | Штамп **14 07 2022**; партия **2211089701**; **EAC**; **4L** | A | Active |
| EVID-G08 | Artifact | ART-003 | PGMM: OEM в подвале; heuristic **5W-40**; information asymmetry | B | Context |
| EVID-G09 | Context | ART-004 | Delta 1L: допуски **ниже порога** читаемости | B | Context |
| **EVID-G10** | **Artifact** | **ART-005** | GPN-01: «полностью синтетическое»; рендер канистры **= ART-001**; фасовки 1/4/5/50/205 L | **A** | **Canonical digital** |
| **EVID-G11** | **Artifact** | **ART-005** | GPN-01 specs badges: **ACEA A3/B3**, A3/B4; **API SN**, **API CF**; MB **226.5**, **229.3**; GM LL-B-025; Porsche A40; PSA B71 2296; **Renault RN700**, **RN710**; VW 502 00/505 00; **AO «АВТОВАЗ»**; **УМЗ**; BMW Longlife-01 (<2019) | **A** | Active |
| **EVID-G12** | **Artifact** | **ART-005** | GPN-01: «**100% ГАРАНТИЯ ОТ ПОДДЕЛОК**» + ссылка «Как это возможно?» | A | Active |
| **EVID-G13** | **Context** | **ART-006** | Оператор: **упаковка не менялась** с даты фото | B | Active |
| **EVID-G14** | **Context** | GPN-01 URL | [GPN-01](04_источники_и_URL.md) · verified registry 23.06.2026 | A | Active |
| **EVID-G15** | **Context** | ART-006 + operator 23.06.2026 | Повторное подтверждение: wrap **не менялся**; GPN-01 + screenshot = актуальный канон | B | Active |
| **EVID-G16** | **Context** | ART-007 | Firecrawl `firecrawl_scrape` GPN-01: ERR_TUNNEL / timeout — auto-ingest **н/д** | C | Negative case |

### Conflict notes

| Conflict | Evidence | Resolution |
|----------|----------|------------|
| RN700 vs RN0700 | G02, G04, G11 | **Closed (CR-G01)** — industry zero-padding; site = **RN700/RN710** как front |
| Physical vs digital OEM stack | G02, G04 vs G11 | **Open (CR-G02)** — site **superset**; не противоречие, а channel gap |
| 2022 batch vs current SKU | G07 vs G13, G10 | **Closed** — wrap stable; batch date ≠ relabel |

### Data gaps (updated)

| Gap | Статус |
|-----|--------|
| GAP-G01 Rev. risk | **Closed** — G13 + G10 render match |
| GAP-G02 Digital triangulation | **Closed** — G10–G15 + GPN-01 verified; G16 = scrape blocked, not gap |
| GAP-G03 Retail shelf @1.2 m | Open — н/д |
| GAP-G04 RN nomenclature | **Closed** — CR-G01 |

---

## Findings Catalogue

### F-G01 — Positive · Cross-face core claims coherent

| Поле | Значение |
|------|----------|
| **Observation** | API **SN/CF**, ACEA **A3/B4**, **синтетическое**, **5W-40**, **4L** — на фронте (G01), обороте (G04–G05), сайте (G10–G11). |
| **Evidence IDs** | EVID-G01; EVID-G04; EVID-G05; EVID-G10; EVID-G11 |
| **Severity & Confidence** | Positive · **High** |

---

### F-G02 — Moderate · Renault RN notation: front/site vs back zero-padding

| Поле | Значение |
|------|----------|
| **Observation** | Front + site: **RN700 / RN710**. Back label: **RN0700 / RN0710**. |
| **Evidence IDs** | EVID-G02; EVID-G04; EVID-G11 |
| **Interpretation** | Нотационная вариация одного допуска (leading zero); **не** split-grade. Риск — путаница при OCR/сверке. |
| **Severity & Confidence** | **Moderate** · **High** |
| **Confounds** | Typo on back; regional label variant |
| **Falsification** | Renault approval letter / batch label spec sheet |
| **Recommendations** | structural: унифицировать RN700/RN710 на обороте |

---

### F-G03 — Major · OEM stack on front — present but below shelf-readability threshold

| Поле | Значение |
|------|----------|
| **Observation** | OEM **перечислены** на фронте (G02), но PGMM (G08) фиксирует **микрошрифт + подвал + градиент** → нечитаемо с полки. |
| **Evidence IDs** | EVID-G02; EVID-G08; EVID-G03 |
| **Interpretation** | Formal presence ≠ effective communication; OEM-driven buyer **не получает** proof на фасаде. |
| **Impact** | Revenue · Trust |
| **Severity & Confidence** | **Major** · **High** |
| **Confounds** | Покупатель поднимает канистру; читает оборот |
| **Recommendations** | quick: 2–3 top OEM icons контрастным блоком; structural: OEM-band над 5W-40 |

---

### F-G04 — Major · Digital OEM superset not mirrored on physical label

| Поле | Значение |
|------|----------|
| **Observation** | Site (G11): **ACEA A3/B3**, **MB 226.5**, **GM LL-B-025**, **Porsche A40**, **BMW Longlife-01**, **УМЗ** — **отсутствуют** на видимых faces G01/G04. Physical: MB **229.3**, VW, PSA, Renault, AVTOVAZ only. |
| **Evidence IDs** | EVID-G04; EVID-G11; EVID-G10 |
| **Interpretation** | **Channel asymmetry:** digital channel обещает **шире**, чем упаковка. Не доказанный split-face defect, но **deictic gap** pack ↔ web. |
| **Impact** | Trust · Legitimacy |
| **Severity & Confidence** | **Major** · **Medium** (TDS не приложен) |
| **Confounds** | Полный стек на обороте мелким текстом вне кадра фото |
| **Falsification** | Full flat scan оборота; официальный TDS PDF |
| **Recommendations** | governance: pack claims ⊆ web claims или явная отсылка «полный список на …» |

---

### F-G05 — Moderate · ACEA A3/B3 — digital only

| Evidence IDs | EVID-G01; EVID-G04; EVID-G11 |
| **Observation** | На этикетке только **A3/B4**; сайт добавляет **A3/B3**. |
| **Severity** | **Moderate** · **High** |

---

### F-G06 — Moderate · MB 226.5 — digital only

| Evidence IDs | EVID-G04; EVID-G11 |
| **Observation** | MB **229.3** on pack; MB **226.5** additional on site only. |
| **Severity** | **Moderate** · **Medium** |

---

### F-G07 — Minor · STO 84035624-179-2015 — back only

| Evidence IDs | EVID-G04 |
| **Observation** | Корпоративный СТО на обороте; на фронте и сайте не виден. |
| **Severity** | **Minor** |

---

### F-G08 — Minor · MB-Approval 229.3 vs MB 229.3 — naming variant

| Evidence IDs | EVID-G02; EVID-G04; EVID-G11 |
| **Severity** | **Minor** · same approval |

---

### F-G09 — Positive · Anti-fraud stack triangulated

| Evidence IDs | EVID-G03; EVID-G06; EVID-G12 |
| **Observation** | Front teaser → back code/3662.ru → site «100% гарантия от подделок». |
| **Severity** | Positive · **High** |

---

### F-G10 — Positive · Packaging wrap stable (operator + site render)

| Evidence IDs | EVID-G01; EVID-G07; EVID-G10; EVID-G13 |
| **Observation** | Оператор: wrap unchanged; G10 render = G01; 2022 stamp valid. |
| **Severity** | Positive · **Medium** (no fresh production stamp) |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-G01 | RN700 ↔ RN0700 | **Closed** — notation (F-G02) |
| CR-G02 | Physical OEM ⊂ Digital OEM | **Open** — channel gap (F-G04, F-G05, F-G06) |
| CR-G03 | Front OEM readable ↔ listed | **Open** — readability (F-G03) |

---

## POV-маркировка (rev. 1)

**Information Integrity**
- *Lacunae:* GAP-G03 retail distance; TDS PDF н/д.
- *Redundancy:* anti-fraud triple layer (G03/G06/G12) — functional.
- *Contamination:* none cross-face API/base.
- *Collonisation:* category codes (silver/orange, PGMM) over engineering legibility.

**Logical Coherence**
- *Conflicts:* none API/base/volume.
- *Contradictions:* CR-G02 = **superset**, not contradiction.

**System Dynamics**
- *Anomalies:* 5W-40 heuristic dominance (G08).
- *Potentials:* GPN puts OEM on front (vs LUKOIL back-only) but negates via microtype.
- *Limits:* photo/OCR; digital claims wider than verified on pack.

**Relational States**
- *Compromise:* list OEM on front for compliance, hide in footer for aesthetics.
- *Parities:* with LUKOIL — both SN/CF synthetic A3/B4; GPN **stronger** anti-fraud UX.
- *Consensus:* pack ↔ site on core claims; site extends OEM.

---

## Строка для сводной матрицы (ODSA × PGMM)

| Параметр | Gazpromneft Premium N 5W-40 4L |
|----------|--------------------------------|
| Product line | **Premium N** |
| API (front / back) | **SN/CF · SN/CF** |
| Base oil claim | **Синтетическое** (front + back + site) |
| ACEA (pack) | **A3/B4** |
| ACEA (site only) | **+ A3/B3** |
| OEM on front | **Listed, microtype** (F-G03) |
| OEM (back) | MB 229.3, Renault, VW, PSA, AVTOVAZ, STO |
| OEM (site superset) | + MB 226.5, GM, Porsche, BMW, УМЗ |
| Renault notation | RN700/RN710 (front, site) · RN0700/RN0710 (back) |
| Anti-fraud | 3662.ru + site guarantee |
| Cross-face consistency | **Pass** |
| Digital vs pack | **Site superset** (F-G04) |
| PGMM paradigm | Cognitive amortization + institutional anxiety |
| Wrap stability | **Confirmed** (G13, G10, **G15**) |
| GPN-01 registry | **Verified** wiki/04 |
| Auto-scrape GPN | **Blocked** (G16) — use screenshot/browser |

---

## Импликации для СТМ

1. **Не копировать** «OEM в подвале» — даже GPN формально выводит OEM на фронт, но **не доносит**; СТМ = **readable OEM band**.
2. **Channel parity:** если web декларирует расширенный стек — **pack must match** или явный QR/TDS; иначе trust gap (F-G04).
3. **RN / OEM typography:** единый формат допусков на всех faces.
4. **Anti-fraud:** GPN силён (F-G09) — СТМ нужен эквivalent proof layer, не обязательно 3662-клон.
5. **PGMM antidote** из wiki/11 остаётся в силе: whitespace + open engineering vs GPN density.

---

## Issues for discussion

1. ~~Добавить **GPN-01** в wiki/04~~ → **Closed** rev. 2
2. TDS PDF для F-G04 (confidence Medium → High) — optional
3. **Следующий кейс:** Mobil Super 3000 x1 5W-40 4L ODSA

**DoD:** ✅ ODSA GPN 5W-40 4L — **locked rev. 2** (DC-EP:A). Pending: GAP-G03, TDS optional.

---

## Decision Card — DC-EP (After Packet #2)

**Status:** ✅ **Approved A** (operator + re-attestation 23.06.2026) — audit **locked**.
