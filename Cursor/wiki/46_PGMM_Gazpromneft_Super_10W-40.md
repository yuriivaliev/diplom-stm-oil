# Анализ упаковки: Gazpromneft Super 10W-40 (PGMM _full)

**Дата анализа:** 25.06.2026  
**CASE_ID:** `COMP_GPN_SUPER_10W40_SEMI_SYN_4L`  
**Объект:** Канистра 4L, фронт + back  
**Методология:** PGMM (Klepikov 2025) — M_OCCURRENCE → M_CONSTRUCTION → M_SYSTEM → DOMAIN → MAP → S/C/M/K → EVAL + Neuromarketing POV  
**Изображения:** фронт + back (пользователь, 25.06.2026)

```yaml
CASE_TYPE: packaging_visual_metaphor
BRAND: Gazpromneft
LINE: Super
SAE: 10W-40
FORMAT: 4L
VIEW: front + back label
SEGMENT: budget / legacy semi-synthetic (Classic/Protect proxy · ЮФО coverage)
REGION: european RU proxy (official RU supply)
CHANNEL: official RU (Gazpromneft-Lubricants Ltd)
PRODUCTION_STAMP: 23.07.2020 · batch 2015073801
BARCODE: 4650063110749
```

**Контекст:** SKU вне текущих матриц этапа 4 (5W-40 mass-mid · 0W-20 premium · 5W-30 ref). Релевантен **Волне 3** СТМ Classic/Protect и **10W-40 legacy / ЮФО** ([03_DR-B](03_DR-B_вязкости_SAE.md)). Прямой peer: [42_PGMM_LUKOIL_SUPER_10W-40.md](42_PGMM_LUKOIL_SUPER_10W-40.md). Семейство GPN — см. [11](11_PGMM_Gazpromneft_Premium_N_5W-40.md) · [32](32_PGMM_Gazpromneft_Premium_C3_5W-30.md). **Не смешивать** с DR-A (доли) / DR-B (SAE-таблицы) в одной строке.

### Artifact vs canonical

| Поле | Artifact (фото 23.07.20) | Canonical (site / operator) | Статус |
|------|--------------------------|----------------------------|--------|
| API | **SG/CD** front + back | **SG/CD** (site product page · pending GPN-03 verify) | ✅ aligned (photo) |
| Base oil claim | «ПОЛУСИНТЕТИЧЕСКОЕ» front | Полусинтетическое всесезонное универсальное (site title) | ✅ aligned |
| OEM | **AVTOVAZ · ZMZ** microtype front; ПАО «АВТОВАЗ» back | АВТОВАЗ (site + back); ZMZ front-only on photo | 🟡 partial — **UMZ н/д** on photo; site verify pending |
| STO | СТО 84035624-058-2012 back | н/д on site scrape (timeout) | artifact-only until GPN-03 |

**Triangulation:** [gazpromneft-oil.ru …/gazpromneft-super-10w-40](https://gazpromneft-oil.ru/ru/products/all/gazpromneft-super-10w-40) · **GPN-03 pending** (verify wiki/04 при ODSA). Batch **2020** — facing 2025/26 verify.

---

## 1. System States

### Information Integrity
- **Lacunae:** ACEA/ILSAC/modern API SN+ — **отсутствуют**; HTHS, drain interval, SAPS — **н/д**; механизм «минимальное шламообразование» — текст back без инфографики; **UMZ** — **н/д** on photo (vs LUKOIL SUPER back stack).
- **Redundancy:** «SUPER» + «ПОЛУСИНТЕТИЧЕСКОЕ» + car icon + orange swirl + «10W-40» — четырёхслойное кодирование budget universal; API SG/CD дублируется front/back.
- **Contamination:** GPN category code (серебро + оранжево-синие свуши) колонизирует budget 10W-40 — визуально «дешевле Premium N», но в той же thermokinetic family ([11](11_PGMM_Gazpromneft_Premium_N_5W-40.md)).
- **Collonisation:** Thermokinetic orange swirl **colonises** semi-synthetic fluid chemistry; «SUPER» hyperbole **colonises** API SG/CD legacy tier.

### Logical Coherence
- **Conflict:** «SUPER» superlative + GPN institutional weight vs **API SG/CD** (pre-SN legacy) — rhetoric premium vs chemistry budget (shared paradox with [42](42_PGMM_LUKOIL_SUPER_10W-40.md)).
- **Contradiction:** Semi-synthetic explicit on front vs dominant **solid/swirl** visual — fluid chemistry подавлена термокинетической графикой (GPN norm: solid > fluid).

### System Dynamics
- **Anomaly:** **Domestic OEM microtype on front** (AVTOVAZ · ZMZ) — **сильнее**, чем LUKOIL SUPER (OEM back-only); **слабее**, чем readable OEM band @1.2 m.
- **Potential:** Authenticity scratch-code on back + EAC + official Moscow manufacturer — institutional trust stack для budget tier; barcode retail minimum.
- **Limit:** Batch **2020** — oldest facing in 10W-40 peer pair; site scrape blocked (pattern GPN-01/02); retail @1.2 m — н/д.

### Relational States
- **Compromise:** Budget tier vs сохранение GPN swirl-DNA (down-tier execution vs Premium N 3D core).
- **Parity:** Solid > Fluid — общая норма с GPN N/C3 и LUKOIL armor family ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)).
- **Consensus:** Official RU supply; Cyrillic front; domestic OEM narrative — **не** import/German Cars identity.

---

## 2. M_OCCURRENCE

### 2.1 Manifest

| MOCC_ID | MATERIAL | SEGMENT | SURFACE_FORM | DOMAIN_A_HINT | DOMAIN_B_HINT | MAP_OP | STATUS |
|---------|----------|---------|--------------|---------------|---------------|--------|--------|
| MOCC_GS_01 | color+logo | header | Blue flame «G» + «GAZPROMNEFT» wordmark | corporate energy monopoly | brand trust | literal | MANIFEST |
| MOCC_GS_02 | text | core | «SUPER» large bold black caps | superlative | line identity | hyperbole | MANIFEST |
| MOCC_GS_03 | text | core | «ПОЛУСИНТЕТИЧЕСКОЕ МОТОРНОЕ МАСЛО» / «SEMISYNTHETIC ENGINE OIL» | semi-synth lab | base oil type | literal | MANIFEST |
| MOCC_GS_04 | text+scale | core | «10W-40» oversized white on orange band | metrology | SAE viscosity | literal | MANIFEST |
| MOCC_GS_05 | text | core | «API SG/CD» | institutional API | spec gate (legacy) | literal | MANIFEST |
| MOCC_GS_06 | graphic | core | Orange/yellow/blue angular flow shapes (swirl-lite) | thermokinetic energy | tribology hidden | substitution | MANIFEST |
| MOCC_GS_07 | icon | core | Small white car silhouette outline | mobility icon | PVL universal | schematic | MANIFEST |
| MOCC_GS_08 | text | footer | OEM microtype: «AVTOVAZ, ZMZ» | domestic OEM | legacy park compliance | literal | MANIFEST |
| MOCC_GS_09 | text | footer | «4L» | volume metrology | pack size | literal | MANIFEST |
| MOCC_GS_10 | form | carrier | Silver-grey metallic HDPE + integrated handle + embossed G logo | industrial metallurgy | utility jug | literal | MANIFEST |
| MOCC_GS_11 | form | cap | Silver screw cap | torque/tooling | pour control | literal | MANIFEST |
| MOCC_GS_12 | form | carrier-side | Translucent oil-level strip (amber fill visible) | metrology affordance | pour/doliv control | literal | MANIFEST |
| MOCC_GS_13 | text | back-header | «Super 10W-40» + semi-synthetic RU/EN | product identity | SKU lock | literal | MANIFEST |
| MOCC_GS_14 | text | back-header | «API SG/CD» + ПАО «АВТОВАЗ» + AAI + СТО 84035624-058-2012 | institutional compliance | domestic standards | literal | MANIFEST |
| MOCC_GS_15 | text | back-core | RU + multilingual application brief (gasoline/diesel, turbo, wear, sludge) | regulatory disclosure | usage scope | literal | MANIFEST |
| MOCC_GS_16 | code | back-footer | Barcode 4650063110749 + EAC + «4L» | retail / conformity | supply chain | literal | MANIFEST |
| MOCC_GS_17 | text+code | back-footer | «Уникальный код» scratch authenticity zone | anti-fraud institution | supply security | literal | MANIFEST |
| MOCC_GS_18 | text | back-footer | ООО «Газpromneft-Lubricants» · Moscow · www.gazpromneft-oil.ru | manufacturer identity | official RU supply | literal | MANIFEST |
| MOCC_GS_19 | stamp | back-footer | 23.07.2020 · 2015073801 | production trace | batch authenticity | literal | MANIFEST |

### 2.2 Latent

| MOCC_ID | HINT | STATUS |
|---------|------|--------|
| MOCC_GS_L01 | «SUPER» = budget-tier hyperbole (below Premium N/C3 nominal premium) | LATENT |
| MOCC_GS_L02 | Orange swirl-lite = down-tier inherit of Premium N thermokinetic M_SYSTEM | LATENT |
| MOCC_GS_L03 | Car icon = shorthand «any car» — no segment gate (vs GENESIS «German Cars») | LATENT |
| MOCC_GS_L04 | Silver HDPE + G logo emboss = GPN mass SKU recognition at distance | LATENT |
| MOCC_GS_L05 | Front OEM microtype = domestic park heuristic without readable band | LATENT |
| MOCC_GS_L06 | Oil-level strip = utility affordance rare on front-facing PGMM corpus | LATENT |
| MOCC_GS_L07 | AAI certification back = domestic engineering institution (parallel to STO) | LATENT |

### 2.3 Lacunae

| MOCC_ID | GAP | STATUS |
|---------|-----|--------|
| MOCC_GS_LAC01 | Fluid / pour / hydrodynamic visualization | LACUNA |
| MOCC_GS_LAC02 | Readable OEM band on front (@1.2 m) — microtype only | LACUNA |
| MOCC_GS_LAC03 | ACEA / ILSAC / modern API SN+ | LACUNA |
| MOCC_GS_LAC04 | Proprietary additive brand (vs LUKOIL ActiPure) | LACUNA |
| MOCC_GS_LAC05 | HTHS, Noack, drain km numeric | LACUNA |
| MOCC_GS_LAC06 | Eco / DPF / hybrid / fuel-economy cues | LACUNA |
| MOCC_GS_LAC07 | Explicit «универсальное» front banner (vs LUKOIL explicit universal) | LACUNA |
| MOCC_GS_LAC08 | UMZ on photo (present on LUKOIL SUPER back) | LACUNA |

### 2.4 Negative space

| MOCC_ID | DESCRIPTION | STATUS |
|---------|-------------|--------|
| MOCC_GS_NS01 | Silver HDPE field around label — category «metallic jug» breathing room (shared GPN code) | NEGATIVE_SPACE |
| MOCC_GS_NS02 | Orange band isolating 10W-40 — viscosity monolith anchor (shared with GPN N pattern) | NEGATIVE_SPACE |
| MOCC_GS_NS03 | Back dense legal wall vs compact spec header — gravity to footer compliance | NEGATIVE_SPACE |
| MOCC_GS_NS04 | Gap between swirl core and OEM microtype — information hierarchy split | NEGATIVE_SPACE |

---

## 3. M_CONSTRUCTION

| MCON_ID | PATTERN_LABEL | MOCC_SET | FUNCTION | STATUS | SYSTEM_LINK |
|---------|---------------|----------|----------|--------|-------------|
| MCON_GS_01 | Universal Mass Heuristic | 02, 03, 04, 05, 07, L03 | transaction + segment flattening | MANIFEST | MSYS_GS_01 |
| MCON_GS_02 | SUPER Hyperbole Lockup | 02, L01 | status + heuristic | MANIFEST | MSYS_GS_01 |
| MCON_GS_03 | SAE+API Front Telemetry | 04, 05, 14 | spec + transaction | MANIFEST | MSYS_GS_01 |
| MCON_GS_04 | Thermokinetic Swirl Lite | 06, L02, L04 | heuristic + brand parity | MANIFEST | MSYS_GS_02 |
| MCON_GS_05 | Semi-Synthetic Literal Claim | 03 | spec honesty (explicit) | MANIFEST | MSYS_GS_01 |
| MCON_GS_06 | Domestic OEM Partial Front-Load | 08, L05 | institutional + transaction | MANIFEST | MSYS_GS_04 |
| MCON_GS_07 | Authenticity Back-Load | 17, L07 | trust + anxiety reduction | MANIFEST | MSYS_GS_03 |
| MCON_GS_08 | GPN Budget Family Continuity | 01, 06, 10, L02 | brand architecture | LATENT | MSYS_GS_02 |
| MCON_GS_09 | Solid-over-Fluid Suppression | LAC01, LAC06 | category norm | LACUNA | MSYS_GS_02 |
| MCON_GS_10 | Legacy API Honesty | 05, LAC03 | spec transparency | LATENT | MSYS_GS_01 |
| MCON_GS_11 | Oil-Level Utility Strip | 12, L06 | pour affordance | MANIFEST | MSYS_GS_01 |

---

## 4. M_SYSTEM

### MSYS_GS_01 — Universal Mass-Market Heuristic (MANIFEST)
**MCON_SET:** 01, 02, 03, 05, 11  
**GOAL:** Максимально быстрая транзакция «полусинт · 10W-40 · legacy API» через SUPER + SAE/API front + semi-synthetic line.  
**CONFLICT_WITH:** MSYS_GS_02 (swirl vs spec literacy)

### MSYS_GS_02 — Thermokinetic Swirl Lite (MANIFEST)
**MCON_SET:** 04, 08  
**GOAL:** Наследие GPN «energy swirl» в budget execution — упрощённые orange shapes vs 3D Premium N; пробой полки через GPN family block.  
**CONFLICT_WITH:** DOMAIN_B (fluid semi-synthetic chemistry)

### MSYS_GS_03 — Institutional Anxiety & Authenticity (MANIFEST)
**MCON_SET:** 07, 14  
**GOAL:** Снять страх контрафакта (unique scratch code) + делегировать STO/AAI/АВТОВАЗ proof на back header.  
**CONFLICT_WITH:** MSYS_GS_01 (front transaction speed vs back-loaded trust)

### MSYS_GS_04 — Domestic OEM Partial Front-Load (MANIFEST)
**MCON_SET:** 06  
**GOAL:** Front microtype AVTOVAZ · ZMZ — **сильнее LUKOIL SUPER** (back-only), но **слабее readable OEM band**; ЮФО/legacy park signal @ thumbnail.  
**CONFLICT_WITH:** LAC02 (illegibility @1.2 m)

---

## 5. DOMAIN

| | Source (A) | Target (B) |
|---|------------|------------|
| **Ontology** | Thermokinetic orange flow, «SUPER» superlative, GPN corporate hegemony, domestic factory heraldry (Avtovaz/ZMZ) | Semi-synthetic 10W-40 tribology, API SG/CD legacy chemistry, universal PVL service |
| **Embodiment** | Angular swirl shapes, silver metal jug, scratch-code security | Invisible oil film, HC+PAO blend, wide temp range |
| **Affect** | «Подойдёт отечественному парку» anxiety relief for budget owner / aging fleet | Confidence in universal fit without reading back label |
| **Conflict** | Swirl-lite thermokinetics **colonises** fluid; «SUPER» **hyperbolises** SG-tier chemistry; GPN institutional code **overweights** budget product |

---

## 6. MAP (MAP1–MAP10 summary)

| MAP | Profile |
|-----|---------|
| **MAP1** Identity | GPN budget sub-line Super; entry tier below Premium N/C3 |
| **MAP2** Domain | A: thermokinetics/superlative/domestic OEM → B: legacy semi 10W-40; fidelity **low** (honest API, inflated metaphor) |
| **MAP3** S | High SAE + API front; domestic OEM **partial front** + back; zero modern spec signal |
| **MAP4** C | Silver-grey HDPE 4L; oil-level strip; embossed G logo; integrated handle |
| **MAP5** M | Shelf: orange 10W-40 band + SUPER break; GPN silver family block vs grey jug |
| **MAP6** K | Vertical stack: logo → SUPER → semi line → swirl → 10W-40/API → OEM microtype; Z-scan to viscosity |
| **MAP7** Invariants | Solid>Fluid; GPN silver+swirl-lite; SAE orange band; SUPER hyperbole; API SG front |
| **MAP8** Shannon | Medium entropy — fewer layers than Premium N; readable in 2–3 s |
| **MAP9** Context | Legacy PVL · ЮФО 10W-40 proxy · Classic/Protect wave 3 · peer [42](42_PGMM_LUKOIL_SUPER_10W-40.md) |
| **MAP10** Local RU | Full Cyrillic front; domestic OEM; official Moscow; authenticity back; no import overlay |

**MAP summary:** Rhetoric **7/10** · Fidelity **3/10** (API honest, swirl inflated) · Cognitive load **medium-low** · Obscuration **moderate** (OEM microtype; swirl substitution)

---

## 7. S / C / M / K (compressed _full)

### S — Signal structure
- **S1 DomainOfArgument:** Universal engine protection + semi-synthetic 10W-40 + legacy API + domestic OEM hint.
- **S3 Discreteness:** Horizontal bands — brand / SUPER / type / swirl / viscosity+API / OEM footer.
- **S9 Correlation:** 10W-40 bound to white type on orange band — strong SAE heuristic (GPN family pattern).
- **S11 Information:** Medium-low spec-information (API SG front); OEM **partial front** + back; **no** ACEA/modern API.

### C — Carrier
- **C1:** HDPE silver-grey metallic; embossed G logo on body.
- **C2:** 4L jug, integrated side handle + top grip; oil-level strip — pour affordance.
- **C5:** Typography-dominant; swirl-lite graphic secondary.
- **C7:** Multimodal: logo + swirl + car icon + text + barcode + EAC + scratch code + multilingual back.

### M — Medium
- **M6 Noise:** Medium-high category shelf; orange 10W-40 band aids break-through at budget price point.
- **M10 Comm:** Retail + traditional trade (ЮФО proxy); authenticity scratch-code back.
- **M11 Soc:** Aging fleet / price-sensitive owner; GPN institutional weight vs LUKOIL red DNA.

### K — Composition
- **K1 Structure:** Header (brand) → core (SUPER + semi + swirl + specs) → footer (OEM microtype + 4L).
- **K3 Tone:** Silver + orange/yellow/blue swirl-lite + black SUPER + white type — split-complementary GPN code (budget).
- **K5 Morph:** Angular flow shapes = dominant K-pattern (down-tier vs Premium N 3D interlock).
- **K7 Density:** Medium front; **high** back legal density.
- **K9 Perception:** Scan path: SUPER → 10W-40 → API SG/CD → (optional) GPN logo.

---

## 8. EVAL + STM Blueprint

### EVAL vectors

| Vector | Score | Note |
|--------|-------|------|
| Transaction speed | **High** | SUPER + 10W-40 + API front = fast budget filter |
| Trust / institutional | **Medium-high** | GPN weight + EAC + authenticity code + STO/AAI back |
| Engineering transparency | **Low-medium** | API SG explicit (honest legacy); no ACEA; OEM microtype |
| Rhetorical fidelity | **Low** | SUPER + swirl vs SG semi-synthetic |
| Premium perception | **Low** | Below Premium N/C3; correct for budget tier |
| RU localization | **High** | Cyrillic front; domestic OEM; official Moscow supply |

### EVAL_AGG
Gazpromneft Super 10W-40 — **budget anchor** линейки GPN: shared **thermokinetic swirl-lite DNA** с Premium N, но **без** Premium/C3 spec front; **explicit semi-synthetic** + **10W-40 front heuristic** + **API SG/CD без маскировки**; **domestic OEM partial front** (AVTOVAZ · ZMZ microtype) — **delta vs LUKOIL SUPER** (OEM back-only). Authenticity scratch-code = **GPN institutional layer** absent on LUKOIL SUPER photo. Для СТМ Classic/Protect — **не копировать** SUPER hyperbole + swirl void; **перенять** readable SAE+API front + **readable domestic OEM band** + semi-synthetic honesty + fluid-precision antidote.

### STM blueprint (антидот · Classic/Protect · 10W-40 wave)

| GPN Super 10W-40 | СТМ (дизайн-вектор) |
|------------------|---------------------|
| SUPER + swirl hyperbole stack | **Protect** master name — один claim tier, no superlative inflation |
| Thermokinetic swirl-lite | **One metaphor max** — fluid line или smart-flat |
| OEM microtype front (illegible) | **Readable OEM front row** (2–3 domestic if ЮФО segment) |
| Authenticity back-only | **Front QR + official supply** lockup |
| Solid>Fluid swirl norm | **Controlled pour / viscosity cue** |
| GPN silver metallic mimicry | **Matte clinical white/black** или controlled accent — no «engine part» dead metaphor |
| Batch 2020 facing | **Version label** при reformulation |
| No proprietary proof (vs ActiPure) | **Named additive + verifiable metric** (HTHS / drain km) |

### vs peer LUKOIL SUPER 10W-40 (point ref)

| Параметр | LUKOIL SUPER [42] | **GPN Super** |
|----------|-------------------|---------------|
| **M_SYSTEM key** | Universal heuristic + mesh armor-lite + ActiPure + OEM back | **Swirl-lite + institutional anxiety + OEM partial front** |
| Visual DNA | Red/black honeycomb mesh | **Silver/orange GPN swirl-lite** |
| Universal cue | «УНИВЕРСАЛЬНОЕ МАСЛО» front | Semi-synthetic line only |
| Proprietary tech | ActiPure® footer | **None** (STO + AAI back) |
| OEM front | **No** | **Microtype AVTOVAZ · ZMZ** |
| Authenticity | QR н/д on photo | **Scratch unique code back** |
| API | SG/CD front+back | SG/CD front+back |
| Batch | 2022 | **2020** (older) |

---

## 9. Issues for discussion

1. **Матрица 10W-40:** Добавить пару **LUKOIL SUPER + GPN Super** в ветку Classic/Protect или держать point reference до Волны 3?
2. **OEM front delta:** GPN partial front-load vs LUKOIL back-only — достаточен ли microtype для ЮФО @1.2 m?
3. **GPN-03 triangulation:** Site verify API/OEM stack; добавить URL в [04_источники_и_URL.md](04_источники_и_URL.md).
4. **Batch 2020:** Актуальный facing 2025/26 — verify label rev / authenticity system parity with Premium N (3662.ru pattern).
5. ~~**Next pass:** `stm-pgmm-delta` (1L)~~ → [47](47_PGMM_Gazpromneft_Super_10W-40_1L_delta.md) ✅ · ~~**Next:** `stm-odsa` (4L+1L)~~ → [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) · [49](49_ODSA_Gazpromneft_Super_10W-40_1L.md) ✅

---

## 10. Связи

- Peer budget 10W-40: [42_PGMM_LUKOIL_SUPER_10W-40.md](42_PGMM_LUKOIL_SUPER_10W-40.md) · [44_ODSA_LUKOIL_SUPER_10W-40_4L.md](44_ODSA_LUKOIL_SUPER_10W-40_4L.md) · ODSA: [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md) · [49](49_ODSA_Gazpromneft_Super_10W-40_1L.md)
- GPN family: [11_PGMM_Gazpromneft_Premium_N_5W-40.md](11_PGMM_Gazpromneft_Premium_N_5W-40.md) · [32_PGMM_Gazpromneft_Premium_C3_5W-30.md](32_PGMM_Gazpromneft_Premium_C3_5W-30.md)
- SAE / Classic line: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md) · [05_линейка_SKU_СТМ.md](05_линейка_SKU_СТМ.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Site triangulation: GPN-03 pending · [04_источники_и_URL.md](04_источники_и_URL.md)

---

*PGMM _full · CASE `COMP_GPN_SUPER_10W40_SEMI_SYN_4L` · skill stm-pgmm · ingest 25.06.2026*
