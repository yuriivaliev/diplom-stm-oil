# Анализ упаковки: Mobil Super 2000 X1 10W-40 (PGMM _full)

**Дата анализа:** 25.06.2026  
**CASE_ID:** `COMP_MOBIL_SUPER_2000_X1_10W40_SEMI_SYN_4L`  
**Объект:** Канистра 4L, фронт + back  
**Методология:** PGMM (Klepikov 2025) — M_OCCURRENCE → M_CONSTRUCTION → M_SYSTEM → DOMAIN → MAP → S/C/M/K → EVAL + Neuromarketing POV  
**Изображения:** фронт + back (пользователь, 25.06.2026)

```yaml
CASE_TYPE: packaging_visual_metaphor
BRAND: Mobil
LINE: Super 2000 x1
SAE: 10W-40
FORMAT: 4L
VIEW: front + back label
SEGMENT: mid-tier semi-synthetic import (Classic/Protect proxy · 10W-40 legacy · ЮФО coverage)
REGION: european RU proxy (parallel import · EN/TR facing)
CHANNEL: import / EU-facing stock (ExxonMobil Russia exit — EX-01)
PRODUCTION_STAMP: MADE 16-07-21 · S170461 10422
BARCODE: 5 055107 433607
LABEL_CODES: front 819702A · back 823898A
```

**Контекст:** SKU вне текущих матриц этапа 4 (5W-40 mass-mid · 0W-20 premium · 5W-30 ref). Релевантен **Волне 3** СТМ Classic/Protect и **10W-40 legacy / ЮФО** ([03_DR-B](03_DR-B_вязкости_SAE.md)). Семейство Mobil Super — см. [12](12_PGMM_mobil_super_3000_x1_5w_40.md) · [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md). Peer budget 10W-40: [42](42_PGMM_LUKOIL_SUPER_10W-40.md) · [46](46_PGMM_Gazpromneft_Super_10W-40.md). **Не смешивать** с DR-A (доли) / DR-B (SAE-таблицы) в одной строке.

### Artifact vs canonical

| Поле | Artifact (фото · batch 16-07-21) | Canonical (line / operator) | Статус |
|------|----------------------------------|-----------------------------|--------|
| Base oil claim | «Semi-Synthetic Motor Oil» front | Полусинтетическое (Mobil Super 2000 line) | ✅ aligned (artifact) |
| API | **—** front · back **SL/SM/SN/SN PLUS** + CF (quality level) | **SN+** tier (back stack) | 🟡 front lacuna · back modern vs budget peers |
| ACEA | Back **A3/B3** | A3/B3 (artifact) | ✅ back-only |
| OEM | Back: MB 229.1 · VW 501 01/505 00 · **AVTOVAZ** | Artifact OEM grid | ✅ back-only · partial domestic |
| RU supply | EN/TR back · no Cyrillic front | Parallel import (pattern Mobil 5W-40 [18]) | 🟡 import |
| Line tier | «2000» + semi front | Below Super 3000 synthetic tier [12] | ✅ down-tier vs 3000 |

**Triangulation:** operator site **pending** (no EX-Mobil-Super-2000 ID in [04_источники_и_URL.md](04_источники_и_URL.md)); EX-01 = Russia exit context only. Canon row = **artifact back stack** until site verify.

---

## 1. System States

### Information Integrity
- **Lacunae:** API / ACEA / OEM — **только back**; front = chemistry + SAE only; **no Cyrillic**; **no** official RF supply cue; HTHS, drain interval, SAPS — **н/д**; x1 mechanism — **н/д**; QR **present** but destination **н/д** without scan.
- **Redundancy:** «Super» + «2000» + «x1» + semi-synthetic line + «Gasoline & Diesel» — пятислойное кодирование line/tier/fuel scope без API front.
- **Contamination:** Gold droplet graphic = simultaneously «fluid protection», «synthetic molecules», «premium gold» — полисемия в **semi-synthetic** tier without disambiguation.
- **Collonisation:** Mobil global code (red «O», silver jug, x1) colonises **legacy 10W-40** — tier-1 recognition without domestic engineering anchor.

### Logical Coherence
- **Conflict:** «Super 2000» + gold kinetic graphic vs **explicit semi-synthetic** — rhetoric mid-premium vs chemistry honesty (partial mitigation via literal semi line).
- **Contradiction:** Fluid droplet visualization **partially breaks** Mobil Super 3000 solid>fluid norm [12] — but metallic ring source keeps industrial anchor.

### System Dynamics
- **Anomaly:** Back API **SN/SN PLUS** stack — **modern chemistry facing** in 10W-40 legacy segment vs domestic peers **SG/CD** ([42](42_PGMM_LUKOIL_SUPER_10W-40.md), [46](46_PGMM_Gazpromneft_Super_10W-40.md)); yet **API off-front** — Mobil family lacuna shared with [12](12_PGMM_mobil_super_3000_x1_5w_40.md).
- **Potential:** AVTOVAZ on back + 10W-40 front heuristic = **legacy domestic park** partial map; MB/VW = **import-car service** dual narrative.
- **Limit:** Batch **2021** — oldest facing in Mobil Super peer set; EN/TR import label — **no** RU overlay; retail @1.2 m — **н/д**.

### Relational States
- **Compromise:** Down-tier Mobil (2000 semi) vs Super 3000 synthetic armor — shared silver jug + x1, **↓** visual density and metaphor intensity.
- **Parity:** API off-front — Mobil tier-1 norm ([12](12_PGMM_mobil_super_3000_x1_5w_40.md), [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md)).
- **Consensus:** Import parallel supply; back-loaded spec grid — **not** official RU domestic narrative.

---

## 2. M_OCCURRENCE

### 2.1 Manifest

| MOCC_ID | MATERIAL | SEGMENT | SURFACE_FORM | DOMAIN_A_HINT | DOMAIN_B_HINT | MAP_OP | STATUS |
|---------|----------|---------|--------------|---------------|---------------|--------|--------|
| MOCC_MS2_01 | color+logo | header | «Mobil» — blue + **red «O»** | corporate energy | global brand trust | literal | MANIFEST |
| MOCC_MS2_02 | text | header | «Super» large black + red underline swoosh | superlative | line identity | hyperbole | MANIFEST |
| MOCC_MS2_03 | text | core | «2000» silver-outlined numerals | numeric tier heuristic | line rank below 3000 | substitution | MANIFEST |
| MOCC_MS2_04 | text | core | «x1» sub-badge beside 2000 | proprietary sub-line | additive/performance cue | obscuration | MANIFEST |
| MOCC_MS2_05 | text+scale | core | «10W-40» white on **magenta/pink** band | metrology badge | SAE viscosity | literal | MANIFEST |
| MOCC_MS2_06 | text | core | «Semi-Synthetic Motor Oil» | semi-synth lab | base oil honesty | literal | MANIFEST |
| MOCC_MS2_07 | graphic | core-right | Gold droplets spray from metallic ring/engine part | fluid kinetics / atomization | tribology film | projection | MANIFEST |
| MOCC_MS2_08 | text | footer-right | «Gasoline & Diesel» italic white | fuel scope | multi-fuel PVL | literal | MANIFEST |
| MOCC_MS2_09 | text+code | footer-left | «4L» + QR + **819702A** | volume + digital trace | pack + SKU lock | literal | MANIFEST |
| MOCC_MS2_10 | form | carrier | Silver-grey metallic HDPE + integrated handle + grip ridges | industrial jug | utility | literal | MANIFEST |
| MOCC_MS2_11 | form | cap | Black ribbed screw cap | torque/tooling | pour control | literal | MANIFEST |
| MOCC_MS2_12 | text | back-header | «Mobil Super 2000 X1 10W-40» | product identity | SKU lock | literal | MANIFEST |
| MOCC_MS2_13 | text | back-body | Meets: **ACEA A3/B3**; **API SL/SM/SN/SN PLUS** | institutional standards | spec gate (modern) | literal | MANIFEST |
| MOCC_MS2_14 | text | back-body | Approved: **MB 229.1** · **VW 501 01/505 00** · **AVTOVAZ** | OEM heraldry | compliance | literal | MANIFEST |
| MOCC_MS2_15 | text | back-body | ExxonMobil Quality Level **API CF** | operator quality tier | diesel supplement cue | literal | MANIFEST |
| MOCC_MS2_16 | code | back-footer | Barcode 5 055107 433607 · **823898A** | retail trace | supply chain | literal | MANIFEST |
| MOCC_MS2_17 | text | back-body | EN + TR descriptive copy + safety disposal | regulatory disclosure | usage scope | literal | MANIFEST |
| MOCC_MS2_18 | stamp | jug-bottom | MADE 16-07-21 · S170461 10422 | production trace | batch authenticity | literal | MANIFEST |
| MOCC_MS2_19 | icon | back | Small red Pegasus logos | ExxonMobil heritage | corporate seal | literal | MANIFEST |

### 2.2 Latent

| MOCC_ID | HINT | STATUS |
|---------|------|--------|
| MOCC_MS2_L01 | «2000» < «3000» — consumer numeric tier ladder without reading back | LATENT |
| MOCC_MS2_L02 | Red «O» = thermal/attention anchor (Mobil family invariant) | LATENT |
| MOCC_MS2_L03 | x1 = shared sub-brand with Super 3000 — line continuity at lower tier | LATENT |
| MOCC_MS2_L04 | Magenta 10W-40 band = GPN-orange-band analogue — viscosity monolith heuristic | LATENT |
| MOCC_MS2_L05 | Gold droplets = **down-tier fluid metaphor** vs 3000 plasma/armor | LATENT |
| MOCC_MS2_L06 | Silver jug = Mobil shelf block recognition at import price points | LATENT |
| MOCC_MS2_L07 | «Gasoline & Diesel» = explicit multi-fuel vs implied PVL only on budget peers | LATENT |

### 2.3 Lacunae

| MOCC_ID | GAP | STATUS |
|---------|-----|--------|
| MOCC_MS2_LAC01 | API / ACEA on **front** | LACUNA |
| MOCC_MS2_LAC02 | **Cyrillic** / RU localization | LACUNA |
| MOCC_MS2_LAC03 | Official RF supply / importer cue | LACUNA |
| MOCC_MS2_LAC04 | x1 technology explanation | LACUNA |
| MOCC_MS2_LAC05 | ActiPure-class proprietary named additive | LACUNA |
| MOCC_MS2_LAC06 | Eco / DPF / hybrid / fuel-economy front cues | LACUNA |
| MOCC_MS2_LAC07 | Domestic OEM on **front** (AVTOVAZ back-only) | LACUNA |

### 2.4 Negative space

| MOCC_ID | DESCRIPTION | STATUS |
|---------|-------------|--------|
| MOCC_MS2_NS01 | Dark label field upper half — typography-dominant void behind Super/2000 | NEGATIVE_SPACE |
| MOCC_MS2_NS02 | Lower-right graphic zone vs left spec stack — diagonal split (lighter than 3000 full bleed) | NEGATIVE_SPACE |
| MOCC_MS2_NS03 | Back dense multilingual legal wall vs compact spec block — gravity to compliance footer | NEGATIVE_SPACE |

---

## 3. M_CONSTRUCTION

| MCON_ID | PATTERN_LABEL | MOCC_SET | FUNCTION | STATUS | SYSTEM_LINK |
|---------|---------------|----------|----------|--------|-------------|
| MCON_MS2_01 | Numeric Tier Heuristic (2000) | 02, 03, L01 | transaction + line positioning | MANIFEST | MSYS_MS2_01 |
| MCON_MS2_02 | x1 Sub-Line Lockup | 04, L03 | brand continuity + obscuration | MANIFEST | MSYS_MS2_01 |
| MCON_MS2_03 | SAE Front Telemetry | 05, L04 | spec + transaction | MANIFEST | MSYS_MS2_01 |
| MCON_MS2_04 | Semi-Synthetic Literal Honesty | 06 | spec transparency (vs synthetic mask) | MANIFEST | MSYS_MS2_02 |
| MCON_MS2_05 | Gold Fluid Kinetics (down-tier) | 07, L05 | heuristic + projection | MANIFEST | MSYS_MS2_02 |
| MCON_MS2_06 | Multi-Fuel Footer Scope | 08, L07 | transaction widening | MANIFEST | MSYS_MS2_01 |
| MCON_MS2_07 | Mobil Global Brand Transfer | 01, 10, 11, L02, L06 | trust + recognition | MANIFEST | MSYS_MS2_03 |
| MCON_MS2_08 | Back-Loaded Modern Spec Grid | 13, 14, 15 | institutional deferral | MANIFEST | MSYS_MS2_04 |
| MCON_MS2_09 | Import EN/TR Disclosure | 17, LAC02, LAC03 | regulatory compliance | MANIFEST | MSYS_MS2_03 |
| MCON_MS2_10 | API Front Lacuna (Mobil norm) | LAC01 | category norm shared with 3000 | LACUNA | MSYS_MS2_04 |

---

## 4. M_SYSTEM

### MSYS_MS2_01 — Numeric Line Heuristic + Transaction (MANIFEST)
**MCON_SET:** 01, 02, 03, 06  
**GOAL:** Быстрая транзакция «Mobil · Super · 2000 · 10W-40 · semi» через tier number + SAE front + fuel scope — **без** API на фронте.  
**CONFLICT_WITH:** MSYS_MS2_02 (semi honesty vs gold premium graphic)

### MSYS_MS2_02 — Down-Tier Fluid Kinetics (MANIFEST)
**MCON_SET:** 04, 05  
**GOAL:** Полусинтетическая честность + **fluid metaphor** (gold droplets) в облегчённом исполнении vs Super 3000 armor/plasma [12].  
**CONFLICT_WITH:** MSYS_MS2_01 (fluid premium cue vs semi label)

### MSYS_MS2_03 — Mobil Global Brand Transfer + Import Facing (MANIFEST)
**MCON_SET:** 07, 09  
**GOAL:** Tier-1 Mobil recognition (red O, silver jug) на import stock; EN/TR back = EU pipeline signal.  
**CONFLICT_WITH:** MSYS_MS2_04 (global brand vs domestic OEM partial)

### MSYS_MS2_04 — Back-Loaded Compliance Grid (MANIFEST)
**MCON_SET:** 08  
**GOAL:** Modern API SN stack + ACEA A3/B3 + MB/VW/Avtovaz **only on back** — institutional deferral pattern Mobil family.  
**CONFLICT_WITH:** LAC01, LAC07 (invisible @1.2 m front)

---

## 5. DOMAIN

| | Source (A) | Target (B) |
|---|------------|------------|
| **Ontology** | Gold fluid atomization, numeric tier ladder (2000), Mobil corporate energy (red O), import OEM heraldry | Semi-synthetic 10W-40 tribology, API SN-class chemistry, multi-fuel PVL service |
| **Embodiment** | Metallic ring + sprayed droplets, silver HDPE, magenta SAE badge | Invisible oil film, HC+PAO semi blend, wide temp 10W-40 |
| **Affect** | «Global Mobil quality at mid price» anxiety relief for import-dependent buyer | Confidence via brand + number, not front spec |
| **Conflict** | Gold fluid + «Super» **hyperbolise** semi tier; numeric 2000 **implies** synthetic ladder without chemistry proof on front |

---

## 6. MAP (MAP1–MAP10 summary)

| MAP | Profile |
|-----|---------|
| **MAP1** Identity | Mobil Super **2000** x1 — entry Super line below 3000 synthetic [12] |
| **MAP2** Domain | A: fluid kinetics/tier number/global brand → B: semi 10W-40; fidelity **medium-low** (semi honest, metaphor inflated) |
| **MAP3** S | High SAE front; modern API back; OEM back grid; zero front spec |
| **MAP4** C | Silver-grey HDPE 4L; standard ergonomic handle; integrated label wrap |
| **MAP5** M | Shelf: Mobil logo + Super/2000 block; magenta 10W-40 band; silver family recognition |
| **MAP6** K | Vertical stack: logo → Super → 2000/x1 → SAE/semi → graphic/footer; Z-scan to 10W-40 |
| **MAP7** Invariants | Mobil red O; silver jug; x1 badge; SAE colored band; API off-front |
| **MAP8** Shannon | Medium entropy — fewer layers than Super 3000; readable in 2–3 s |
| **MAP9** Context | Legacy PVL · 10W-40 ЮФО proxy · import tier-1 · Classic/Protect wave 3 |
| **MAP10** Local RU | **No** Cyrillic front; EN/TR back; parallel import — **anti** official RU narrative |

**MAP summary:** Rhetoric **6/10** · Fidelity **4/10** (semi honest, gold fluid inflated) · Cognitive load **medium-low** · Obscuration **moderate** (x1 void, API back-only)

---

## 7. S / C / M / K (compressed _full)

### S — Signal structure
- **S1 DomainOfArgument:** Semi-synthetic 10W-40 + Mobil Super tier + multi-fuel scope.
- **S3 Discreteness:** Header brand → core Super/2000 → SAE/semi row → footer fuel/volume/QR.
- **S9 Correlation:** 10W-40 bound to magenta band — strong SAE heuristic (peer pattern [46]).
- **S11 Information:** Low front spec-information; **high** back spec-information (API SN stack) — **split-channel** Mobil norm.

### C — Carrier
- **C1:** HDPE silver-grey metallic; dark label + magenta accent.
- **C2:** 4L jug, integrated side handle — mass retail / sto.
- **C5:** Typography-dominant upper; graphic lower-right secondary.
- **C7:** Multimodal: logo + numerals + text + fluid graphic + QR + barcode.

### M — Medium
- **M6 Noise:** Medium-high category shelf; Mobil silver block + magenta band aid break-through.
- **M10 Comm:** Import retail + service (parallel stock); QR present — digital trace **potential**.
- **M11 Soc:** Price-sensitive owner seeking **global brand** on legacy viscosity; **not** domestic-official buyer.

### K — Composition
- **K1 Structure:** Header (Mobil + Super) → core (2000/x1 + SAE + semi) → footer (4L/QR + fuel + graphic).
- **K3 Tone:** Silver-grey + dark label + magenta + gold droplets + Mobil blue/red.
- **K5 Morph:** Gold droplet spray = dominant K-pattern (**fluid**, not armor).
- **K7 Density:** Medium front; **high** back legal density.
- **K9 Perception:** Scan path: Super/2000 → 10W-40 → semi line → (optional) graphic.

---

## 8. EVAL + STM Blueprint

### EVAL vectors

| Vector | Score | Note |
|--------|-------|------|
| Transaction speed | **High** | Super + 2000 + 10W-40 + semi front = fast filter |
| Trust / institutional | **Medium** | Global Mobil brand; back OEM grid; **import** not official RU |
| Engineering transparency | **Low-medium** | Semi explicit; API SN **back-only**; x1 black box |
| Rhetorical fidelity | **Medium-low** | Gold fluid vs semi; Super hyperbole |
| Premium perception | **Medium** | Above domestic SUPER peers; **below** Super 3000 [12] |
| RU localization | **Low** | EN/TR import facing; no Cyrillic |

### EVAL_AGG
Mobil Super 2000 X1 10W-40 — **import mid-tier** в линейке Mobil Super: shared Mobil DNA (red O, silver jug, x1) at **down-tier** vs [12]; **semi-synthetic honesty** on front; **fluid metaphor** (gold droplets) vs 3000 armor/plasma; **modern API SN stack on back** — **delta ↑** vs domestic budget peers SG/CD ([42](42_PGMM_LUKOIL_SUPER_10W-40.md), [46](46_PGMM_Gazpromneft_Super_10W-40.md)); **API off-front** — shared Mobil white space. AVTOVAZ back = partial **legacy domestic** signal. Для СТМ Classic/Protect — **не копировать** numeric tier ladder without chemistry proof · gold fluid void · import EN-only; **перенять** semi honesty · readable SAE front · **API+OEM front row** · Cyrillic official supply.

### STM blueprint (антидот · Classic/Protect · 10W-40 wave)

| Mobil Super 2000 X1 10W-40 | СТМ (дизайн-вектор) |
|----------------------------|---------------------|
| Super + 2000 numeric hyperbole | **Protect** master name — один claim tier |
| Gold droplet premium graphic | **One metaphor max** — controlled pour line |
| API SN back-only | **API SN/CF front** + ACEA if chemistry matches |
| x1 without explanation | **Named tech + metric** or drop sub-badge |
| EN/TR import facing | **Full Cyrillic** + official RF supply |
| AVTOVAZ/MB/VW back-only | **2–3 OEM front row** (domestic + import mix if segment) |
| Mobil silver import block | **Own color architecture** — не silver clone |

### vs peer comparison (10W-40 budget · point ref)

| | Mobil Super 2000 | LUKOIL SUPER [42] | GPN Super [46] |
|---|------------------|-------------------|----------------|
| **M_SYSTEM** | Down-tier fluid kinetics + import brand | Universal heuristic + mesh armor-lite | Swirl-lite + OEM partial front |
| **API facing** | SN+ **back** | SG/CD **front** | SG/CD **front** |
| **Semi claim** | Front explicit | Front explicit | Front explicit |
| **OEM** | Back MB/VW/Avtovaz | Back domestic | **Front** microtype + back |
| **Supply** | Import parallel | Official RU | Official RU (GPN-03 pending) |
| **Fluid visual** | Gold droplets **yes** | Mesh armor **no** | Orange swirl **yes** |

### vs Mobil Super 3000 x1 5W-40 [12]

| | Super 2000 10W-40 | Super 3000 5W-40 |
|---|-------------------|------------------|
| **Tier** | 2000 semi | 3000 synthetic-implied |
| **Metaphor** | Fluid kinetics (droplets) | Plasma/armor (ring) |
| **SAE cluster** | 10W-40 legacy | 5W-40 mass-mid |
| **Shared** | Silver jug, red O, x1, API off-front |

---

## 9. Issues for discussion

1. **Матрица 10W-40:** Добавить Mobil Super 2000 как **third import tier-1** point-ref рядом с LUKOIL SUPER + GPN Super?
2. **API SN on back vs SG peers:** Modern chemistry facing — достаточен ли back-only для Classic/Protect или СТМ должен **front-load** как differentiation?
3. **Batch 2021:** Актуальный facing 2025/26 — verify label rev / QR destination.
4. **Site triangulation:** Добавить EX-Mobil-Super-2000 в [04](04_источники_и_URL.md) при verify mobil.com product page.
5. **Next passes:** `stm-pgmm-delta` (1L vs 4L) · `stm-odsa` (claims audit front+back).

---

## 10. Связи

- Mobil Super synthetic tier: [12_PGMM_mobil_super_3000_x1_5w_40.md](12_PGMM_mobil_super_3000_x1_5w_40.md) · [18_ODSA_mobil_super_3000_x1_5w_40_4L.md](18_ODSA_mobil_super_3000_x1_5w_40_4L.md)
- Peer budget 10W-40: [42](42_PGMM_LUKOIL_SUPER_10W-40.md) · [46](46_PGMM_Gazpromneft_Super_10W-40.md) · [48](48_ODSA_Gazpromneft_Super_10W-40_4L.md)
- SAE / Classic line: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md) · [05_линейка_SKU_СТМ.md](05_линейка_SKU_СТМ.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Russia context: EX-01 · [04_источники_и_URL.md](04_источники_и_URL.md)

---

*PGMM _full · CASE `COMP_MOBIL_SUPER_2000_X1_10W40_SEMI_SYN_4L` · skill stm-pgmm · ingest 25.06.2026*
