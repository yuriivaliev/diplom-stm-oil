# ODSA — message architecture: Eliten (4 SAE × bimodal)

**CASE_ID:** `ODSA_STM_Eliten_MESSAGE_ARCH_2026`  
**Master positioning:** Eliten — инженерная марка на качественной базе и мировых пакетах присадок; понятный выбор под задачу: PVL → будущие pro-линейки  
**Этап:** 5 · **Статус:** ✅ locked (pre-launch copy)  
**Дата:** 25.06.2026  
**Метод:** ODSA Audit Packet v1.6.7 · PGMM white space §6 (матрицы 5W-40 / 5W-30 / 0W-20 / 10W-40)

> **Правило:** один poetic hero на все SAE **не используется**. Архитектура: master → sub-line → SKU proof → 1L doliv.

---

## 0. Frame

| Поле | Значение |
|------|----------|
| Мастер-бренд | **Eliten** · RU **1172689** (с 03.12.2025) |
| Регион | Европейская часть РФ |
| Линейки | **Classic/Protect** (5W-40 syn, 10W-40 semi) · **Modern/Tech** (5W-30 syn, 0W-20 FS) |
| Severity profile | Product + legitimacy/trust |
| Confidence ceiling (pre-launch) | **M** без ART-001 (фото этикетки СТМ) |

### Evidence Ledger (контекст)

| EVID | Источник |
|------|----------|
| EVID-RM-01 | `Roadmap_запуска_СТМ.md` — bimodal + волны |
| EVID-RM-02 | Roadmap §Фаза 3 — 0W-20 / 5W-40 месседжи (directional) |
| EVID-PGMM-540 | `матрица_PGMM_ODSA_5W-40.md` §6 |
| EVID-PGMM-530 | `матрица_PGMM_ODSA_5W-30.md` §4 |
| EVID-PGMM-0W20 | `матрица_PGMM_ODSA_0W-20.md` §6 |
| EVID-PGMM-10W40 | `матрица_PGMM_ODSA_10W-40.md` §6 |
| EVID-DDX-03 | DDx funnel этап 3 — Eliten false-premium LIMIT |

---

## 1. Message architecture (4 уровня)

### Уровень 1 — Master (все SKU)

**Позиционирование:** инженерная марка · качественная база · мировые пакеты присадок · выбор под задачу (PVL → pro future).

**RU:** «Spec на этикетке — официально для РФ.»

| Claim | Evidence | Confidence |
|-------|----------|:----------:|
| Readable spec on pack | PGMM white space A (all clusters) | M |
| Official RF supply | PGMM white space E · Roadmap | M |
| Integrated Cyrillic wrap | PGMM white space F | M |

**ODSA gate:** Blocker, если copy обещает spec front, а макет — back-only / microtype.

---

### Уровень 2 — Sub-line

| Sub-line | SKU | Sub-line promise (RU) |
|----------|-----|------------------------|
| **Classic Protect** | 5W-40 syn · 10W-40 semi | «Защита двигателя — по readable spec, не по пафосу.» |
| **Modern Tech** | 5W-30 syn · 0W-20 FS | «Инженерная spec для современного мотора — на передней этикетке.» |

**Roadmap mapping (directional, не дословный front):**

- Classic: «Maximum Engine Protection» → **перефразировано** ODSA-safe (без «максимальная» без lab).
- Modern 0W-20: «Engineered for Asian Turbo» → **support/TDS**, не front hero без named OEM + LSPI on pack.

---

## 2. SKU matrix — hero + proof + 1L doliv

### 2.1 · 5W-40 synthetic · Classic Protect · волна 1 · пилот

| Слой | RU copy |
|------|---------|
| Hero | **Eliten Classic Protect 5W-40** |
| Proof-line | **API SN/CF и OEM — на передней этикетке.** |
| Support | Защита двигателя — по факту, не по пафосу. |
| **1L doliv** | **1L · doliv · spec на фронте, как у 4L.** |

| Claim | Evidence | Confidence |
|-------|----------|:----------:|
| API SN front 4L+1L | EVID-PGMM-540 §6A | M |
| OEM readable band | EVID-PGMM-540 §6A · LAC-04 @1.2 m | M |
| Not armor rhetoric | EVID-PGMM-540 §6D | M |

**White space:** A, C, D, E, F.

---

### 2.2 · 5W-30 synthetic · Modern Tech · волна 1 · core balance

| Слой | RU copy |
|------|---------|
| Hero | **Eliten Modern Tech 5W-30** |
| Proof-line | **API SP · ACEA C3 — на фронте. OEM — на виду.** |
| Support | Баланс мотора и DPF — без spec-in-name пафоса. |
| **1L doliv** | **1L · C3 / API SP на передней этикетке.** |

| Claim | Evidence | Confidence |
|-------|----------|:----------:|
| Front API + ACEA C3 together | EVID-PGMM-530 §4 | M |
| Readable OEM @1.2 m (gap vs peers) | EVID-PGMM-530 §4 | M |
| Low-SAPS / DPF named | EVID-PGMM-530 §4 | M |

**Запрет copy:** «German Cars», «Hyper-Armor» (паттерн LUKOIL GC).

---

### 2.3 · 0W-20 full synthetic · Modern Tech · волна 2

| Слой | RU copy |
|------|---------|
| Hero | **Eliten Modern Tech 0W-20** |
| Proof-line | **API SP · ACEA C5 · multi-OEM — на передней этикетке.** |
| Support | Для современного турбо · LSPI — по spec, не по lattice/gold. |
| **1L doliv** | **1L · hero SAE + OEM @120px** (service fill 5,6 L → 5L+1L) |

| Claim | Evidence | Confidence |
|-------|----------|:----------:|
| API SP + ACEA C5 front | EVID-PGMM-0W20 §6A | M |
| Multi-OEM front row | EVID-PGMM-0W20 §6B · DR-B GEELY proxy | M |
| LSPI / turbo | EVID-RM-02 · RBS doc.10 | L–M (lab TBD) |

**«Asian Turbo»:** только back / TDS / site, пока нет OEM+LSPI на front photo.

---

### 2.4 · 10W-40 semi-synthetic · Classic Protect · волна 3 · ЮФО

| Слой | RU copy |
|------|---------|
| Hero | **Eliten Classic Protect 10W-40** |
| Proof-line | **Полусинтетика · API на фронте · domestic OEM на виду.** |
| Support | Без SUPER-пафоса — честный tier на этикетке. |
| **1L doliv** | **1L · API на фронте — spec doliv, как у 4L.** |

| Claim | Evidence | Confidence |
|-------|----------|:----------:|
| Semi honesty (не synthetic premium) | EVID-PGMM-10W40 §6B | M |
| API tier-honest front | EVID-PGMM-10W40 §6A | M |
| Domestic OEM stack (AVTOVAZ·UMZ·ZMZ) | EVID-PGMM-10W40 §6F | M |

**Запрет copy:** «SUPER», synthetic premium lexicon при semi chemistry.

---

## 3. Сводная таблица (copy-paste)

| SAE | Chemistry | Sub-line | Sub-line promise | SKU proof-line |
|-----|-----------|----------|------------------|----------------|
| 5W-40 | synthetic | Classic Protect | Защита по readable spec | API SN/CF + OEM на фронте |
| 5W-30 | synthetic | Modern Tech | Инженерная spec на фронте | API SP + ACEA C3 + OEM на виду |
| 0W-20 | full synthetic | Modern Tech | То же | API SP + ACEA C5 + multi-OEM |
| 10W-40 | semi-synthetic | Classic Protect | Защита без пафоса | Semi · API front · domestic OEM |

**Master (all):** Spec на этикетке — официально для РФ.

---

## 4. ODSA severity rollup (copy layer)

| Severity | Запрет |
|----------|--------|
| **Blocker** *(conditional)* | OEM/API в слогане при unreadable front макете |
| **Major** | «Максимальная защита», «лучшее масло», «калибровано под ваш мотор» |
| **Major** | 10W-40: synthetic/premium lexicon при semi |
| **Major** | «Подлинное vs суррогаты» без chain-of-custody |
| **Moderate** | «Asian Turbo» на 0W-20 front без OEM scope |
| **Positive** | Descriptive spec-front antidote PGMM white space |

---

## 5. Findings (cross-SAE)

| ID | Finding | Severity |
|----|---------|----------|
| F-MSG-01 | Convergent copy на «readable spec» — differentiation = имя sub-line + visual + spec row | Moderate · info |
| F-MSG-02 | 5W-30 ≠ 0W-20 hero — C3/DPF vs turbo/multi-OEM | Positive |
| F-MSG-03 | 1L brief обязателен для каждого SAE (PGMM format fairness) | Major if skipped |
| F-MSG-04 | Pre-launch confidence **M** — ART-001 + TDS parity для **H** | Moderate |

---

## 6. Decision Record (copy)

| Поле | Значение |
|------|----------|
| **Candidate** | Message architecture Eliten (4 SAE) |
| **Decision** | **RECOMMEND with LIMIT** |
| **Allowed** | Master + sub-line + SKU proof + 1L doliv as above |
| **Prohibited** | Single hero all SAE; superlatives; semi→syn lexicon |
| **Monitoring** | ART-001 per SKU; legibility @1.2 m; pack=TDS |
| **Reopen trigger** | FIPS blocker on Eliten; reformulation without version label |

---

## 7. Связи

- DDx финалисты: [`кандидат_01_Eliten.md`](кандидат_01_Eliten.md) · contrastive 02–03
- Wiki: [`54_название_СТМ_Eliten.md`](../Cursor/wiki/54_название_СТМ_Eliten.md)
- PGMM сводка: [`08_PGMM_упаковка.md`](../Cursor/wiki/08_PGMM_упаковка.md)
