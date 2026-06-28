# Eliten — design system (этап 6)

**CASE_ID:** `DESIGN_STM_Eliten_PACK_2026`  
**Статус:** ✅ **APPROVED dual-handle** · **Обновлено:** 26.06.2026  
**Мастер-бренд:** Eliten · ТЗ RU 1172689 (словесный)

---

## 1. Design intent

| Ось | Решение |
|-----|---------|
| Позиционирование | Инженерная марка · readable spec · не luxury «elite» |
| Antidote PGMM | Не armor/lattice/gold hyperbole конкурентов |
| White space | A–F из матриц PGMM (readable API/OEM front · local trust on **back**) |
| Архитектура | Master shell → sub-line → SKU proof → format delta |

**✅ Approved carrier (26.06):** dual-handle graphite 4L jug — см. [`ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md`](ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md)

---

## 2. Два визуальных семейства (bimodal)

### Classic Protect · 5W-40 · 10W-40

| Токен | Значение |
|-------|----------|
| Primary | `#1B3A4B` (deep engineering blue) |
| Secondary UI | `#0D2137` (dark navy) — spec band · 4L tab |
| Accent | `#2E7D6E` (protect teal) — **optional UI** · Classic v2 prefers navy |
| Label surface | Silver / brushed `#C8CCD0` · light grey `#E8EAED` |
| Fluid | `#C68642` amber · `#D4A055` honey-gold · warm translucent · viscous **ribbon** |
| Jug surface | `#4A4F54` graphite grey · matte industrial HDPE |
| Carrier | **Dual-handle** · top carry + side grip · cap top-left · emboss **ELITEN** lower body |
| Label ground | Dark navy/black gradient · silver metallic wordmark · amber-gold sub-line |
| Typography | Sans geometric · **ELITEN** wordmark · **CLASSIC PROTECT** caps |
| Motif | Silver **API SN/CF** band · gold accent · amber oil zone bottom · OEM row |
| Tone | Utility · protect · mass-mid · engineering premium (not luxury) |

### Modern Tech · 5W-30 · 0W-20

| Токен | Значение |
|-------|----------|
| Primary | `#0D2137` (dark navy) |
| Accent | `#3B82F6` (tech blue) |
| Secondary | `#94A3B8` (cool grey) |
| Label surface | Cool silver `#B8C4CE` · light cool grey `#E2E8F0` |
| Fluid / motif | **Subtle precision grid** · optional **muted cool fluid line** · **no warm amber ribbon** (≠ Classic) |
| Jug surface | **Cool slate / navy-charcoal** `#3A4556` · `#4A5568` — matte HDPE · **≠ graphite Classic** |
| Carrier | **Same mold** as Classic: dual-handle 4L · narrow 1L · cap top-left · emboss **ELITEN** |
| Label ground | Dark navy + **fine engineering grid** · silver wordmark · **tech-blue sub-line** |
| Typography | Sans geometric · **ELITEN™** · **MODERN TECH** caps |
| Motif | **API SP · ACEA C3** band · **tech-blue accent** · readable OEM row · **no gold** |
| Tone | Engineering spec · turbo/modern · LSPI by spec not rhetoric |

---

## 3. Layout grid (front · all formats)

**Front = international product layer only.** Страна, происхождение, импортёр, EAC, RF, адреса и legal manufacturer — **только back** (вне scope этапа 6).

```text
┌─────────────────────────────┐
│  ELITEN™         [4L/5L/1L]│  ← master + volume badge (metric)
│  Classic Protect / Modern  │  ← sub-line
│  5W-40                       │  ← hero SAE (largest)
│  Fully Synthetic / Semi-Syn  │  ← product type (EN)
├─────────────────────────────┤
│  API SN/CF  │  OEM row       │  ← proof band (readable @120px)
├─────────────────────────────┤
│  [optional batch/QR — no EAC]│  ← trust hint only · not regulatory
└─────────────────────────────┘
```

**Back (не в эскизах этапа 6):** Cyrillic · «Spec на этикетке — официально для РФ» · EAC · importer · address · legal manufacturer.

**ODSA gate:** proof band on **front** for 4L, 5L, **and** 1L (format fairness).

---

## 4. Format deltas

| Format | Carrier | Delta vs 4L |
|--------|---------|-------------|
| **4L** | **Dual-handle** jug | Reference · approved concept · carrier locked front↔back |
| **5L** | Dual-handle jug · **0W-20 only** | Same mold as 4L · **5L** badge · taller fill (RBS 5,6 L) |
| **1L** | Narrow bottle | DRY rescale · hero SAE + OEM row @120px · sub-line smaller |

---

## 5. SKU proof copy (front)

| SKU | Proof-line |
|-----|------------|
| 5W-40 | API SN/CF · OEM band |
| 5W-30 | API SP · ACEA C3 · OEM visible |
| 10W-40 | Semi-Synthetic · API front · OEM band |
| 0W-20 | API SP · ACEA C5 · multi-OEM front |

### 5.1 · OEM matrix — Classic Protect 5W-40 (TDS-pending · ART-001)

**Status:** 🟡 provisional · **Confidence M** · reopen when TDS locked  
**Rule:** front = **compact readable band** · back = **full stack** (GPN-01 parity logic · no superset without proof)

| Layer | Content |
|-------|---------|
| **Front band** | **API SN/CF** · **ACEA A3/B4** |
| **Front OEM row** | MB **229.3** · VW 502 00 / 505 00 · RN 0700 / 0710 · **Porsche A40** · ACEA A3/B4 |
| **Back full** *(concept)* | + BMW LL-01 · GM LL-B-025 · MB 226.5 · Porsche A40 · AVTOVAZ · УМЗ · ACEA A3/B3 · Cyrillic master line · EAC · importer · legal |

**Audit fix (26.06):** mockup **не использует MB 229.5** (GPN 1L contamination pattern · wiki/28 CR-G1D-01).

Источник peer proxy: GPN Premium N 5W-40 · `матрица_PGMM_ODSA_5W-40` §6 · wiki/17 GPN-01.

Источник copy: [`ODSA_название_Eliten_матрица_слоганов.md`](../04_DD_ODSA_название_бренда/ODSA_название_Eliten_матрица_слоганов.md)

### 5.2 · OEM matrix — Classic Protect 10W-40 (TDS-pending · ART-001)

**Status:** 🟡 provisional · **Confidence M** · reopen when TDS locked  
**Rule:** **≠ 5W-40 OEM tier** · front = compact readable band · back = full stack

| Layer | Content |
|-------|---------|
| **Front band** | **API SN/CF** |
| **Front OEM row** | **ACEA A3/B3** · MB **229.1** · VW **501 01 / 505 00** · **AVTOVAZ** · **UMZ** · **ZMZ** |
| **Back full** *(concept)* | + API SL/SM/SN stack if chemistry proof · Cyrillic · EAC · importer · legal |

**Cross-SAE ban (10W-40 front):** **не** MB 229.3 · **не** VW 502 00 · **не** RN 0700/0710 · **не** Porsche A40 · **не** ACEA A3/B4 — это tier **5W-40 syn**.

**Peer proxy:** Mobil Super 2000 x1 10W-40 4L back (wiki/52 EVID-MS2-06–08) · LUKOIL SUPER domestic stack (wiki/44).

**Audit fix (27.06):** operator — API **SN/CF** front; OEM MB/VW = **229.1 / 501 01** (legacy 10W-40), не 5W-40 pair.

### 5.3 · OEM matrix — Modern Tech 5W-30 (TDS-pending · ART-001)

**Status:** 🟡 provisional · **Confidence M** · reopen when TDS locked  
**Rule:** front = **API SP + ACEA C3 together** · readable OEM · **≠ Classic Protect visual shell**

| Layer | Content |
|-------|---------|
| **Front band** | **API SP** · **ACEA C3** |
| **Front OEM row** | MB **229.51** · VW **504 00 / 507 00** · **BMW LL-04** · **Porsche C30** |
| **Back full** *(concept)* | + **dexos2** · Fiat 9.55535-S3 · Renault RN17 · Low-SAPS/DPF copy · Cyrillic · EAC |

**Operator (27.06):** front **без dexos2** · dexos2 → **back only** · 4L draft **accepted as-is** (incl. blue+amber bottom graphic).

**Ban copy/visual:** «German Cars», Hyper-Armor, DuraMax, armor, Mobil green lattice, GPN swirl void.

**Peer proxy:** LUKOIL GENESIS GC (wiki/34) · GPN Premium C3 (wiki/36 GPN-02) · white space §4 `матрица_5W-30`.

**Carrier (operator 27.06):** **same dual-handle / 1L mold** · jug color **cool slate** `#3A4556` · label **Modern Tech shell** (tech blue, grid).

### 5.4 · OEM matrix — Modern Tech 0W-20 (TDS-pending · ART-001)

**Status:** 🟡 provisional · **Confidence M** · reopen when TDS locked  
**Rule:** **≠ 5W-30 C3 tier** · front = **API SP + ACEA C5** · **multi-OEM row** · dexos1 / extended OEM → back if needed

| Layer | Content |
|-------|---------|
| **Front band** | **API SP** · **ACEA C5** |
| **Front OEM row** | **Volvo VCC RBS0-2AE** · **Toyota** · **Honda** · **Hyundai** · **Kia** · **Nissan** |
| **Back full** *(concept)* | + **ILSAC GF-6A** · **dexos1 Gen3** · Fiat · Ford · GM · Cyrillic · EAC · LSPI/TDS |

**Operator (27.06):** **GF-6A** и **dexos1 Gen3** → **back only** · front = API SP · ACEA C5 + multi-OEM row.

**Cross-SAE ban (0W-20 front):** **не** ACEA **C3** · **не** MB 229.51 / BMW LL-04 / VW 504/507 stack (5W-30 tier).

**Peer proxy:** Mobil 1 0W-20 5L (wiki/21) · Castrol EDGE 0W-20 V (wiki/25) · white space §6 `матрица_0W-20`.

**Carrier:** **dual-handle jug + 5L badge** (operator A · 27.06) — **same mold family** as 4L · не отдельный top-only service jug · **1L** = narrow bottle as 5W-30 1L.

**Visual shell:** **same Modern Tech label** as accepted 5W-30 4L/1L (tech blue · grid · blue tech lines · bottom fluid graphic).

---

## 6. Запреты (ODSA + PGMM)

**NEG-чеклист** — единый gate для текста, макета и negative prompt для ИИ.

### 6.1. Риторика и claims

| ID | Запрет | Antidote PGMM |
|----|--------|---------------|
| N-01 | Превосходные степени · «maximum» · «ultimate» · «best» · SUPER-пафос | Mobil/Castrol/LUKOIL hyperbole |
| N-02 | Luxury / false-premium («elite», trophy status) | Castrol gold · HYSPEC institutional |
| N-03 | «Максимальная защита» и аналоги **без lab proof** | ODSA F-MSG · wiki/04 ODSA prohibited |

### 6.2. Текст и читаемость

| ID | Запрет | Antidote PGMM |
|----|--------|---------------|
| N-04 | Mobil-pattern: EN front + **RU regulatory sticker overlay** | PGMM F · clean front/back split |
| N-05 | API/ACEA/OEM **только на обороте** при front copy про spec | Castrol 0W-20 · ODSA blocker |
| N-06 | **Мелкий нечитаемый OEM-текст** (fail @120px) | Microtype OEM rows |
| N-07 | Полусинтетика под видом полного синтетика (10W-40) | ODSA semi→syn lexicon |

### 6.3. Доверие и география

| ID | Запрет | Antidote PGMM |
|----|--------|---------------|
| N-08 | **На front:** «Made in…» · country · origin bragging | Liqui Moly · → back only |
| N-09 | **На front:** US units (qt, gal, fl oz, °F) | Metric L only on front |
| N-10 | **На front:** флаги стран | Decorative sovereignty · → back |
| N-11 | **Поддельные знаки сертификации** · клон 3662 / непроверенные бейджи | PGMM E trust layer |
| N-12 | **Чужие OEM-логотипы** (не в SKU proof matrix) | Decorative OEM clutter |

### 6.4. Визуальная метафора

| ID | Запрет | Antidote PGMM |
|----|--------|---------------|
| N-13 | Золотой кубок · gold institutional carrier | Castrol EDGE 0W-20 |
| N-14 | Броня · щит · крепость | LUKOIL/GPN honeycomb armor-lite |
| N-15 | Соты · hex lattice · biomimetic mesh | Mobil 1 0W-20 |
| N-16 | Агрессивный **racing / motorsport** (EDGE wedge, speed cues) | Castrol · import premium |

### 6.4.1. Fluid / oil color (red-team · CAT-01)

**Red-team:** teal/green fluid на ранних эскизах → риск путаницы с **антифризом / тосолом** на полке РФ.

| ID | Правило | Antidote |
|----|---------|----------|
| N-23 | Fluid **must read as motor oil**: amber · honey-gold · warm translucent · viscous | Category legibility |
| N-24 | **No** green · turquoise · coolant · antifreeze · water · aqua · neon liquid | OЖ / тосол color code |

**Positive prompt (fluid):**

```text
The fluid visual must look like motor oil: amber, honey-gold, warm translucent oil, viscous texture.
```

**Negative prompt (fluid):**

```text
No green liquid, no turquoise liquid, no coolant look, no antifreeze look, no water splash, no aqua wave.
```

Teal `#2E7D6E` — optional Classic UI; **v2 etalon** uses navy `#0D2137`. **Не** заливка «жидкости». Fluid = **controlled ribbon**, not splash.

### 6.5. Front-only geo / legal (international layer)

| ID | Запрет на **front** | Куда |
|----|---------------------|------|
| N-17 | Country · origin · «Made in…» · flags | Back |
| N-18 | RF · EAC · importer · address · legal manufacturer | Back |
| N-19 | Local regulation · Cyrillic supply/regulatory lines | Back |
| N-20 | US units (qt, gal, fl oz, °F) | Back or omit |
| N-21 | Germany / USA / any nationality bragging | Back or omit |
| N-22 | Fake or unverified certification **seals** (EAC clone etc.) | Back only if verified |

### 6.6. Negative prompt для ИИ (copy-paste · full)

```text
International front label only. No country, origin, importer, local regulation, EAC, RF,
Germany, USA, flags, addresses, or legal manufacturer data on the front.
No country-of-origin claims, no "Made in…", no national flags, no RF/EAC/importer/address
information, no US quart/gallon units, no local legal text on the front label.
No superlatives, no "maximum", "ultimate", "best", no luxury claims, no gold trophy,
no armor shield, no honeycomb, no aggressive racing style, no unrelated OEM logos,
no tiny unreadable OEM text, no back-label-only specs.
The fluid visual must look like motor oil: amber, honey-gold, warm translucent oil, viscous texture.
No green liquid, no turquoise liquid, no coolant look, no antifreeze look, no water splash, no aqua wave.
```

---

## 7. Pipeline генерации

1. **Концепт** ×3 — только `Classic Protect 5W-40 4L` → выбор одного (рекомендация: **концепт 02**)
2. **Финал** ×8 — масштабирование shell на матрицу SKU×format
3. **Back label** — Cyrillic · RF supply · EAC · legal · Figma/Canva (вне AI front mockups)

---

## 8. Файловая карта

| Путь | Содержание |
|------|------------|
| `концепт/эскиз_01…03.png` | 3 варианта пилота |
| `финал/*_4L.png` / `*_1L.png` / `*_5L.png` | 8 front mockups |
| `финал/ELITEN_Classic_Protect_5W40_4L_dual_handle_packaging_concept.png` | **✅ APPROVED** 4L etalon |
| [`ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md`](ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md) | Decision record |
| `архив/single_handle_v2/` | Superseded carrier |
| [`обоснование_эскизов.md`](обоснование_эскизов.md) | PGMM/ODSA → решение |
| [`бриф_матрица_8SKU.md`](бриф_матрица_8SKU.md) | Per-SKU brief |
