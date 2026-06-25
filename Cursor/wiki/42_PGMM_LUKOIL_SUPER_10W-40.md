# Анализ упаковки: LUKOIL SUPER 10W-40 (PGMM _full)

**Дата анализа:** 25.06.2026  
**CASE_ID:** `COMP_LUKOIL_SUPER_10W40_SEMI_SYN_4L`  
**Объект:** Канистра 4L, фронт + back  
**Методология:** PGMM (Klepikov 2025) — M_OCCURRENCE → M_CONSTRUCTION → M_SYSTEM → DOMAIN → MAP → S/C/M/K → EVAL + Neuromarketing POV  
**Изображения:** фронт + back (пользователь, 25.06.2026)

```yaml
CASE_TYPE: packaging_visual_metaphor
BRAND: LUKOIL
LINE: SUPER
SAE: 10W-40
FORMAT: 4L
VIEW: front + back label
SEGMENT: budget / legacy semi-synthetic (Classic/Protect proxy · ЮФО coverage)
REGION: european RU proxy (official RU supply)
CHANNEL: official RU (LLK-International)
PRODUCTION_STAMP: 09.11.22 · batch 3970 5 187 · 22 06894360
BARCODE: 4607161615393
```

**Контекст:** SKU вне текущих матриц этапа 4 (5W-40 mass-mid · 0W-20 premium · 5W-30 ref). Релевантен **Волне 3** СТМ Classic/Protect и **10W-40 legacy / ЮФО** ([03_DR-B](../Cursor/wiki/03_DR-B_вязкости_SAE.md)). Семейство LUKOIL — см. [10](10_PGMM_LUKOIL_LUXE_5W-40.md) · [30](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md). **Не смешивать** с DR-A (доли) / DR-B (SAE-таблицы) в одной строке.

### Artifact vs canonical

| Поле | Artifact (фото 09.11.22) | Canonical (матрица / site) | Статус |
|------|--------------------------|----------------------------|--------|
| API | **SG/CD** front + back | **SG/CD** | ✅ aligned |
| Base oil claim | «ПОЛУСИНТЕТИЧЕСКОЕ» front | Полусинтетическое (site) | ✅ aligned |
| OEM | АВТОВАЗ · УМЗ · ЗМЗ back | АВТОВАЗ · УМЗ · ЗМЗ (LLK-03) | ✅ aligned |
| ActiPure | front footer | н/д расшифровка site | artifact-only detail |

**Triangulation:** [lukoil-masla.ru …/lukoil-super-10w-40](https://lukoil-masla.ru/ru/products/ProductCard/lukoil-super-10w-40) · **LLK-03** (verify wiki/04 при ODSA).

---

## 1. System States

### Information Integrity
- **Lacunae:** OEM (АВТОВАЗ/УМЗ/ЗМЗ) — **только back**; ACEA/ILSAC — **отсутствуют**; HTHS, drain interval, SAPS — **н/д**; ActiPure® — **без proof**; QR на фото **не виден** (vs Genesis/LUXE back stack).
- **Redundancy:** «УНИВЕРСАЛЬНОЕ МАСЛО» + car icon + «SUPER» + semi-synthetic line — четырёхкратное кодирование «массового универсала»; API SG/CD дублируется front/back.
- **Contamination:** Honeycomb/mesh pattern = одновременно «технологичность», «броня-lite» и «соты/фильтр» — полисемия в budget-tier без disambiguation.
- **Collonisation:** Lukoil corporate code (красный квадрат + тёмный HDPE + mesh) колонизирует budget 10W-40 — визуально «дешевле LUXE», но в той же armor-family.

### Logical Coherence
- **Conflict:** «SUPER» hyperbole + «ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ ActiPure» vs **API SG/CD** (pre-SN legacy) — rhetoric premium vs chemistry budget.
- **Contradiction:** Semi-synthetic explicit on front vs dominant **solid/mesh** visual — fluid chemistry подавлена сеткой.

### System Dynamics
- **Anomaly:** **10W-40 on front** (не только back) — сильнее heuristic, чем у части 5W-40 tier-1 (API off-front); при этом **API SG** — один из старейших facing в линейке Lukoil retail.
- **Potential:** Domestic OEM stack (АВТОВАЗ/УМЗ/ЗМЗ) — прямой мэппинг на **legacy domestic park** / ЮФО service; barcode + EAC = retail trust minimum.
- **Limit:** Batch **2022** — facing 2025/26 verify; нет retail @1.2 m validation; back QR zone **н/д** на фото.

### Relational States
- **Compromise:** Budget tier vs сохранение Lukoil visual DNA (red + black + mesh) — «LUXE без золота и карбона».
- **Parity:** Solid > Fluid — общая норма с [10](10_PGMM_LUKOIL_LUXE_5W-40.md), [30](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md) ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)).
- **Consensus:** Official RU supply; EAC back; domestic OEM back-load — **не** German/import narrative.

---

## 2. M_OCCURRENCE

### 2.1 Manifest

| MOCC_ID | MATERIAL | SEGMENT | SURFACE_FORM | DOMAIN_A_HINT | DOMAIN_B_HINT | MAP_OP | STATUS |
|---------|----------|---------|--------------|---------------|---------------|--------|--------|
| MOCC_LS_01 | color+logo | header | Red square «LUK» + «LUKOIL» black | corporate energy | brand trust | literal | MANIFEST |
| MOCC_LS_02 | text | header | «УНИВЕРСАЛЬНОЕ МАСЛО» small caps | category universal | mass applicability | hyperbole | MANIFEST |
| MOCC_LS_03 | icon | header | Red circle + white car silhouette | mobility icon | PVL universal | schematic | MANIFEST |
| MOCC_LS_04 | text | core | «SUPER» large white italic caps | superlative | line identity | hyperbole | MANIFEST |
| MOCC_LS_05 | text | core | «ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО» | semi-synth lab | base oil type | literal | MANIFEST |
| MOCC_LS_06 | text+scale | core | «10W-40» prominent white | metrology | SAE viscosity | literal | MANIFEST |
| MOCC_LS_07 | text | core | «API SG/CD» | institutional API | spec gate (legacy) | literal | MANIFEST |
| MOCC_LS_08 | pattern | core | Red honeycomb / mesh texture bands | filter lattice / armor mesh | tribology hidden | substitution | MANIFEST |
| MOCC_LS_09 | text+® | footer | «ActiPure» + «ИННОВАЦИОННАЯ ТЕХНОЛОГИЯ» | proprietary tech | additive package | obscuration | MANIFEST |
| MOCC_LS_10 | text | footer | «4L» | volume metrology | pack size | literal | MANIFEST |
| MOCC_LS_11 | form | carrier | Silver-grey metallic HDPE + integrated handle | industrial jug | utility | literal | MANIFEST |
| MOCC_LS_12 | form | cap | Red screw cap + vertical grip ridges | torque/tooling | pour control | literal | MANIFEST |
| MOCC_LS_13 | text | back-header | «LUKOIL SUPER» + semi-synthetic EN/RU | product identity | SKU lock | literal | MANIFEST |
| MOCC_LS_14 | text | back-core | «10W-40» red bar band | SAE anchor | viscosity heuristic | literal | MANIFEST |
| MOCC_LS_15 | text | back-core | OEM: ПАО «АВТОВАЗ» · ОАО «УМЗ» · ПАО «ЗМЗ» | domestic OEM | legacy park compliance | literal | MANIFEST |
| MOCC_LS_16 | code | back-footer | Barcode 4607161615393 + EAC | retail / conformity | supply chain | literal | MANIFEST |
| MOCC_LS_17 | text | back-body | Multilingual legal + application (RU + EN + …) | regulatory disclosure | usage scope | literal | MANIFEST |
| MOCC_LS_18 | stamp | jug-bottom | 09.11.22 · 3970 5 187 · 22 06894360 | production trace | batch authenticity | literal | MANIFEST |

### 2.2 Latent

| MOCC_ID | HINT | STATUS |
|---------|------|--------|
| MOCC_LS_L01 | «SUPER» = budget-tier hyperbole (below LUXE/GENESIS nominal armor) | LATENT |
| MOCC_LS_L02 | Honeycomb = lightweight inherit of LUXE carbon armor family | LATENT |
| MOCC_LS_L03 | Car icon = shorthand «any car» vs GENESIS «German Cars» segment gate | LATENT |
| MOCC_LS_L04 | Silver-grey jug + red cap = Lukoil mass SKU recognition at distance | LATENT |
| MOCC_LS_L05 | ActiPure = shared epistemic seal across LUXE → SUPER → budget continuity | LATENT |
| MOCC_LS_L06 | «УНИВЕРСАЛЬНОЕ» = explicit anti-segmentation (ЮФО / aging fleet) | LATENT |

### 2.3 Lacunae

| MOCC_ID | GAP | STATUS |
|---------|-----|--------|
| MOCC_LS_LAC01 | Fluid / pour / hydrodynamic visualization | LACUNA |
| MOCC_LS_LAC02 | OEM on **front** (domestic stack back-only) | LACUNA |
| MOCC_LS_LAC03 | ACEA / ILSAC / modern API SN+ | LACUNA |
| MOCC_LS_LAC04 | ActiPure mechanism / lab metric | LACUNA |
| MOCC_LS_LAC05 | QR / digital trace on visible back (vs newer Lukoil SKUs) | LACUNA |
| MOCC_LS_LAC06 | Eco / DPF / hybrid / fuel-economy cues | LACUNA |
| MOCC_LS_LAC07 | Explicit «official supply» front cue | LACUNA |

### 2.4 Negative space

| MOCC_ID | DESCRIPTION | STATUS |
|---------|-------------|--------|
| MOCC_LS_NS01 | Black central field behind «SUPER» — monolith anchor, less premium than LUXE gold void | NEGATIVE_SPACE |
| MOCC_LS_NS02 | Red mesh bands vs black core — horizontal stratification (lighter than GENESIS silver/carbon split) | NEGATIVE_SPACE |
| MOCC_LS_NS03 | Back dense legal wall vs small spec bar — gravity to footer compliance | NEGATIVE_SPACE |

---

## 3. M_CONSTRUCTION

| MCON_ID | PATTERN_LABEL | MOCC_SET | FUNCTION | STATUS | SYSTEM_LINK |
|---------|---------------|----------|----------|--------|-------------|
| MCON_LS_01 | Universal Mass Heuristic | 02, 03, 04, L03, L06 | transaction + segment flattening | MANIFEST | MSYS_LS_01 |
| MCON_LS_02 | SUPER Hyperbole Lockup | 04, L01 | status + heuristic | MANIFEST | MSYS_LS_01 |
| MCON_LS_03 | SAE+API Front Telemetry | 06, 07, 14 | spec + transaction | MANIFEST | MSYS_LS_01 |
| MCON_LS_04 | Honeycomb Armor Lite | 08, L02 | heuristic + brand parity | MANIFEST | MSYS_LS_02 |
| MCON_LS_05 | ActiPure Epistemic Seal | 09, L05 | obscuration + trust | MANIFEST | MSYS_LS_03 |
| MCON_LS_06 | Semi-Synthetic Literal Claim | 05 | spec honesty (rare explicit) | MANIFEST | MSYS_LS_01 |
| MCON_LS_07 | Domestic OEM Back-Load | 15 | institutional deferral | MANIFEST | MSYS_LS_04 |
| MCON_LS_08 | Lukoil Budget Family Continuity | 01, 11, 12, L04 | brand architecture | LATENT | MSYS_LS_02 |
| MCON_LS_09 | Solid-over-Fluid Suppression | LAC01, LAC06 | category norm | LACUNA | MSYS_LS_02 |
| MCON_LS_10 | Legacy API Honesty (no mask) | 07, LAC03 | spec transparency (inverse of LUXE mask) | LATENT | MSYS_LS_01 |

---

## 4. M_SYSTEM

### MSYS_LS_01 — Universal Mass-Market Heuristic (MANIFEST)
**MCON_SET:** 01, 02, 03, 06, 10  
**GOAL:** Максимально быстрая транзакция «любое авто · 10W-40 · полусинт» через УНИВЕРСАЛЬНОЕ + SUPER + SAE/API front.  
**CONFLICT_WITH:** MSYS_LS_03 (innovation claim vs SG chemistry)

### MSYS_LS_02 — Honeycomb Armor Lite (MANIFEST)
**MCON_SET:** 04, 08  
**GOAL:** Наследие Lukoil «solid protection» в budget execution — mesh вместо carbon/gold LUXE; пробой полки без premium cost.  
**CONFLICT_WITH:** MSYS_LS_01 (universal flat vs armor metaphor)

### MSYS_LS_03 — ActiPure Epistemic Black Box (MANIFEST)
**MCON_SET:** 05  
**GOAL:** Proprietary tech anchor без раскрытия — сквозная стратегия LUKOIL retail ([10](10_PGMM_LUKOIL_LUXE_5W-40.md)).  
**CONFLICT_WITH:** MSYS_LS_10 (legacy API visible — partial transparency)

### MSYS_LS_04 — Domestic OEM Sovereignty (MANIFEST)
**MCON_SET:** 07  
**GOAL:** Back-loaded compliance для **отечественного парка** (ВАЗ/УМЗ/ЗМЗ) — ЮФО/legacy service narrative.  
**CONFLICT_WITH:** LAC02 (OEM invisible @1.2 m front)

---

## 5. DOMAIN

| | Source (A) | Target (B) |
|---|------------|------------|
| **Ontology** | Honeycomb filter lattice, car-icon mobility, «SUPER» superlative, domestic factory heraldry | Semi-synthetic 10W-40 tribology, API SG/CD legacy chemistry, Avtovaz-era engine protection |
| **Embodiment** | Rigid mesh, red/black mass-market shield | Invisible oil film, HC+PAO blend, wide temp range |
| **Affect** | «Подойдёт всем» anxiety relief for budget owner / aging fleet | Confidence in universal fit without reading back label |
| **Conflict** | Armor-lite mesh **colonises** fluid; «SUPER/innovation» **hyperbolises** SG-tier chemistry | |

---

## 6. MAP (MAP1–MAP10 summary)

| MAP | Profile |
|-----|---------|
| **MAP1** Identity | LUKOIL budget sub-line SUPER; entry tier below LUXE/GENESIS |
| **MAP2** Domain | A: mesh/superlative/universal → B: legacy semi 10W-40; fidelity **low** (honest API, dishonest «innovation») |
| **MAP3** S | High SAE + API front; domestic OEM back; zero modern spec signal |
| **MAP4** C | Silver-grey HDPE 4L; standard ergonomic handle; integrated label wrap |
| **MAP5** M | Shelf: large SUPER + 10W-40 break; red/black contrast vs grey jug body |
| **MAP6** K | Vertical stack: logo → universal → SUPER → specs → ActiPure; Z-scan to 10W-40 |
| **MAP7** Invariants | Solid>Fluid; Lukoil red; mesh texture; SAE prominent; ActiPure footer |
| **MAP8** Shannon | Medium entropy — fewer layers than LUXE/GENESIS; readable in 2–3 s |
| **MAP9** Context | Legacy PVL · ЮФО 10W-40 proxy · Classic/Protect wave 3 |
| **MAP10** Local RU | Full Cyrillic front; domestic OEM back; official RU; no import overlay |

**MAP summary:** Rhetoric **7/10** · Fidelity **3/10** (API honest, metaphor inflated) · Cognitive load **medium-low** · Obscuration **moderate** (ActiPure)

---

## 7. S / C / M / K (compressed _full)

### S — Signal structure
- **S1 DomainOfArgument:** Universal engine protection + semi-synthetic 10W-40 + legacy API.
- **S3 Discreteness:** Horizontal bands — universal header / SUPER core / spec row / ActiPure footer.
- **S9 Correlation:** 10W-40 bound to white type on black — strong SAE heuristic.
- **S11 Information:** Medium-low spec-information (API SG front); OEM information back-only; **no** ACEA/modern API.

### C — Carrier
- **C1:** HDPE silver-grey metallic; black/red label zones.
- **C2:** 4L jug, integrated side handle — mass retail / sto.
- **C5:** Typography-dominant; mesh pattern secondary texture.
- **C7:** Multimodal: logo + icon + text + pattern + barcode + EAC.

### M — Medium
- **M6 Noise:** Medium-high category shelf; SUPER white-on-black aids break-through at budget price point.
- **M10 Comm:** Retail + traditional trade (ЮФО proxy); barcode-led POS.
- **M11 Soc:** Aging fleet / price-sensitive owner; **anti** premium-German identity vs [30](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md).

### K — Composition
- **K1 Structure:** Header (brand + universal + icon) → core (SUPER + semi + specs) → footer (ActiPure + 4L).
- **K3 Tone:** Black + red mesh + silver-grey jug + white type.
- **K5 Morph:** Honeycomb mesh = dominant K-pattern (lighter than LUXE carbon).
- **K7 Density:** Medium front; **high** back legal density.
- **K9 Perception:** Scan path: SUPER → 10W-40 → API SG/CD → (optional) ActiPure.

---

## 8. EVAL + STM Blueprint

### EVAL vectors

| Vector | Score | Note |
|--------|-------|------|
| Transaction speed | **High** | SUPER + 10W-40 + API front = fast budget filter |
| Trust / institutional | **Medium** | Domestic OEM back; EAC; **no** QR/digital layer on photo |
| Engineering transparency | **Low-medium** | API SG explicit (honest legacy); ActiPure black box; no ACEA |
| Rhetorical fidelity | **Low** | SUPER + «инновация» vs SG semi-synthetic |
| Premium perception | **Low** | Below LUXE/GENESIS; correct for budget tier |
| RU localization | **High** | Cyrillic front; domestic OEM; official Perm supply |

### EVAL_AGG
LUKOIL SUPER 10W-40 — **budget anchor** линейки Lukoil: shared ActiPure + mesh armor DNA с LUXE, но **без** gold/carbon premium; **explicit universal** + **10W-40 front heuristic**; **API SG/CD без маскировки** (в отличие от LUXE SL→SN drift). Domestic OEM back = **ЮФО/legacy** signal. Для СТМ Classic/Protect — **не копировать** SUPER hyperbole + ActiPure void; **перенять** readable SAE+API front + **domestic OEM band** (если целевой парк) + **semi-synthetic honesty** + fluid-precision antidote к mesh.

### STM blueprint (антидот · Classic/Protect · 10W-40 wave)

| LUKOIL SUPER 10W-40 | СТМ (дизайн-вектор) |
|---------------------|---------------------|
| SUPER + universal hyperbole stack | **Protect** или neutral master name — один claim tier |
| Honeycomb mesh armor-lite | **One metaphor max** — fluid line или smart-flat |
| ActiPure® без proof | **Named additive + verifiable metric** (HTHS / drain km) |
| API SG/CD legacy facing | **Honest API SN/CF** (если chemistry matches) — no false «innovation» |
| Domestic OEM back-only | **2–3 OEM front row** (Avtovaz-class if segment = ЮФО) |
| Solid>Fluid mesh norm | **Controlled pour / viscosity cue** |
| 2022 batch facing | **Version label** при reformulation |

---

## 9. Issues for discussion

1. **Матрица 10W-40:** Создавать ли отдельную ветку матрицы (SUPER + GPN/Rosneft budget peers) или держать как point reference до Волны 3?
2. **vs LUXE 5W-40:** SUPER — deliberate down-tier (mesh vs carbon, SG vs SN, universal vs implied premium) — cannibalization или channel separation?
3. **ЮФО proxy:** PGMM domestic OEM back — достаточен ли для Classic/Protect positioning без regional front cue?
4. **Batch 2022:** Актуальный facing 2025/26 — verify label rev / QR adoption.
5. ~~**Next passes:** `stm-pgmm-delta` (1L)~~ → [43](43_PGMM_LUKOIL_SUPER_10W-40_1L_delta.md) ✅ · ~~`stm-odsa`~~ → [44](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) · [45](45_ODSA_LUKOIL_SUPER_10W-40_1L.md) ✅

---

## 10. Связи

- Lukoil mass-mid proxy: [10_PGMM_LUKOIL_LUXE_5W-40.md](10_PGMM_LUKOIL_LUXE_5W-40.md) · [16_ODSA_LUKOIL_LUXE_5W-40_4L.md](16_ODSA_LUKOIL_LUXE_5W-40_4L.md)
- Lukoil mid-premium ref: [30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md)
- SAE / Classic line: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md) · [05_линейка_SKU_СТМ.md](05_линейка_SKU_СТМ.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Site triangulation: LLK-03 · [04_источники_и_URL.md](04_источники_и_URL.md)

---

*PGMM _full · CASE `COMP_LUKOIL_SUPER_10W40_SEMI_SYN_4L` · skill stm-pgmm · ingest 25.06.2026*
