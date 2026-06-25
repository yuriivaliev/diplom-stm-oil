# Анализ упаковки: Mobil 1 ESP 5W-30 4L (PGMM _full)

**Дата анализа:** 25.06.2026  
**CASE_ID:** `COMP_MOBIL_1_ESP_5W30_4L`  
**Объект:** Канистра 4L, фронт + back (back — dense legal, мелкий текст **нечитаемо** на фото)  
**Методология:** PGMM (Klepikov 2025) — M_OCCURRENCE → M_CONSTRUCTION → M_SYSTEM → DOMAIN → MAP → S/C/M/K → EVAL + Neuromarketing POV  
**Изображения:** front + back (пользователь, 25.06.2026)

```yaml
CASE_TYPE: packaging_visual_metaphor
BRAND: Mobil / ExxonMobil
LINE: Mobil 1 ESP (Emission System Protection)
SAE: 5W-30
FORMAT: 4L
VIEW: front label + back label (back specs н/д на фото)
SEGMENT: premium synthetic (Mobil 1 sub-line · Low-SAPS / emission-adjacent)
REGION: european RU proxy
CHANNEL: import / parallel (прокси; ODSA не прогонялся)
```

**Контекст:** SKU вне текущих матриц этапа 4 (5W-40 mass-mid · 0W-20 premium). Соседи по 5W-30 point-ref: [30](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md), [32](32_PGMM_Gazpromneft_Premium_C3_5W-30.md). Флагман Mobil 1: [19](19_PGMM_mobil_1_0w_20_5L.md). **Не смешивать** с DR-A (доли) / DR-B (SAE-таблицы) в одной строке.

**Artifact vs canonical:** PGMM — по **видимому** на фото. Канон API/ACEA/OEM — **н/д** без ODSA triangulation; back label на фото **нечитаем**. При будущем ODSA: канон = наивысший допуск по оператору (API **SP > SN**…).

---

## 1. System States

### Information Integrity
- **Lacunae:** API SP / ILSAC / ACEA C2/C3 на фронте — **н/д**; OEM approvals — **н/д** (front); back dense text — **нечитаемо** на фото; HTHS, Noack, drain — **н/д**; кириллица / RU official supply — **н/д** (import-facing).
- **Redundancy:** «ESP EMISSION SYSTEM PROTECTION» + «FOR GASOLINE, DIESEL & HYBRID ENGINES» + «ADVANCED SYNTHETIC TECHNOLOGY» — три оси (aftertreatment / multi-fuel / synthetic tier) без дифференциации механизма на лице.
- **Contamination:** Green network-graph паттерн одновременно читается как «молекулярная сеть», «emission telemetry / IoT grid» и «circuit board» — намеренная полисемия eco-tech.
- **Collonisation:** Категорийный код «серебристый HDPE + крупная вязкость справа + чёрный квадрат „1“» ([19](19_PGMM_mobil_1_0w_20_5L.md), [12](12_PGMM_mobil_super_3000_x1_5w_40.md)) сохранён; ESP отличается **green institutional band** и **network motif** вместо honeycomb 0W-20.

### Logical Coherence
- **Conflict:** «Emission System Protection» (restrictive chemistry / Low-SAPS) vs «FOR GASOLINE, DIESEL & HYBRID» (широкий multi-fuel охват) — совместимо продуктово, но визуально смешивает **regulatory caution** и **universal fit**.
- **Contradiction:** Green eco-institutional cue vs Oracle Red Bull Racing motorsport badge — performance heritage **рядом** с emission framing без явного моста.

### System Dynamics
- **Anomaly:** **«Mobil 1 50 YEARS»** anniversary lockup на фронте — temporal heritage cue, редкий для import SKU в RU retail.
- **Potential:** Explicit **diesel + hybrid** on front — прямой мэппинг на mixed fleet / DPF anxiety сегмент (adjacent к C3 Low-SAPS niche, [32](32_PGMM_Gazpromneft_Premium_C3_5W-30.md)).
- **Limit:** Back label unreadable — полнота claims и OEM grid **н/д** на этом CASE; PGMM back = carrier morphology only.

### Relational States
- **Compromise:** Premium Mobil 1 whitespace vs обязательный green ESP band + right-panel pattern density.
- **Parity:** **Solid > Fluid** — network lattice colonises триbology target (shared with honeycomb 0W-20, armor LUKOIL/GPN).
- **Consensus:** «1» monolith + silver HDPE — межформатный invariant Mobil 1 globally.

---

## 2. M_OCCURRENCE

### 2.1 Manifest

| MOCC_ID | MATERIAL | SEGMENT | SURFACE_FORM | DOMAIN_A_HINT | DOMAIN_B_HINT | MAP_OP | STATUS |
|---------|----------|---------|--------------|---------------|---------------|--------|--------|
| MOCC_ESP_01 | color+text | header | Wordmark «Mobil» blue + red «1» | corporate identity | brand trust | literal | MANIFEST |
| MOCC_ESP_02 | graphic | header | White «1» in black square | monolith/seal | flagship tier | hyperbole | MANIFEST |
| MOCC_ESP_03 | color+text | core | Green bar «ESP EMISSION SYSTEM PROTECTION» | emission regulation / aftertreatment | DPF/TWC / Low-SAPS | projection | MANIFEST |
| MOCC_ESP_04 | logo | core | «Mobil 1 50 YEARS» gold anniversary badge | heritage / longevity | brand equity | literal | MANIFEST |
| MOCC_ESP_05 | text | core | «FOR GASOLINE, DIESEL & HYBRID ENGINES» | multi-fuel powertrain | fleet universality | projection | MANIFEST |
| MOCC_ESP_06 | text | core | «ADVANCED SYNTHETIC TECHNOLOGY ENGINE OIL» | lab/precision | PAO/estol ester base | substitution | MANIFEST |
| MOCC_ESP_07 | text+scale | core-right | «5W-30» oversized white | metrology badge | SAE viscosity | literal | MANIFEST |
| MOCC_ESP_08 | pattern | core-right | Green network / node-link graph on dark field | digital telemetry / molecular graph | emission-system connectivity | metaphor | MANIFEST |
| MOCC_ESP_09 | logo | footer | Oracle Red Bull Racing + Mobil 1 co-brand | F1 motorsport | performance prestige | substitution | MANIFEST |
| MOCC_ESP_10 | icon+text | footer | Hybrid vehicle icon (car + plug) | electrified drivetrain | hybrid cycle | projection | MANIFEST |
| MOCC_ESP_11 | text | footer-right | «4L» | volume metrology | pack size | literal | MANIFEST |
| MOCC_ESP_12 | code | footer-left | QR / datamatrix | digital trace | anti-counterfeit? | latent | MANIFEST |
| MOCC_ESP_13 | form | carrier | Metallic silver-grey HDPE + integrated handle | industrial container | utility | literal | MANIFEST |
| MOCC_ESP_14 | color | cap | Bright green screw cap | eco / ESP line color | line coherence | literal | MANIFEST |
| MOCC_ESP_15 | text+graphic | back-header | «Mobil» logo on back label | corporate | continuity | literal | MANIFEST |
| MOCC_ESP_16 | color+text | back-core | Green product block (text **нечитаемо**) | SKU identity | spec anchor | literal | MANIFEST |
| MOCC_ESP_17 | text | back-core | Dense multilingual legal columns | compliance | regulatory burden | suppression | MANIFEST |
| MOCC_ESP_18 | graphic | back-footer | Barcode + symbols on green patch | retail / disposal | channel ops | literal | MANIFEST |

### 2.2 Latent

| MOCC_ID | HINT | STATUS |
|---------|------|--------|
| MOCC_ESP_L01 | Network graph → catalytic converter / sensor network / OBD diagnostics metaphor | LATENT |
| MOCC_ESP_L02 | Green palette → eco / Low-SAPS without explicit «C3» or «Low SAPS» text on front | LATENT |
| MOCC_ESP_L03 | Diesel explicit → commercial fleet / pickup anxiety relief | LATENT |
| MOCC_ESP_L04 | 50 YEARS → longevity transfer to drain interval (unstated) | LATENT |
| MOCC_ESP_L05 | Red Bull → «ultimate performance» borrowed authority for emission SKU | LATENT |
| MOCC_ESP_L06 | Light upper field + white core → clinical premium (shared with 0W-20 whitespace) | LATENT |

### 2.3 Lacunae

| MOCC_ID | GAP | STATUS |
|---------|-----|--------|
| MOCC_ESP_LAC01 | Fluid / hydrodynamic / pour visualization | LACUNA |
| MOCC_ESP_LAC02 | API SP / SN / ILSAC front mark | LACUNA |
| MOCC_ESP_LAC03 | ACEA C2/C3/C5 explicit on front | LACUNA |
| MOCC_ESP_LAC04 | OEM approvals readable (front; back **нечитаемо**) | LACUNA |
| MOCC_ESP_LAC05 | Cyrillic / official RU supply marker | LACUNA |
| MOCC_ESP_LAC06 | Lab metrics (HTHS, SAPS, Noack, drain km) | LACUNA |
| MOCC_ESP_LAC07 | Back spec grid content — **нечитаемо** on photo | LACUNA |
| MOCC_ESP_LAC08 | «Low SAPS» / «Mid SAPS» explicit wording on front | LACUNA |

### 2.4 Negative space

| MOCC_ID | DESCRIPTION | STATUS |
|---------|-------------|--------|
| MOCC_ESP_NS01 | Upper light-grey band — premium breathing room (~20% label height) | NEGATIVE_SPACE |
| MOCC_ESP_NS02 | Left white text column vs right green pattern panel — asymmetric Z-layout | NEGATIVE_SPACE |
| MOCC_ESP_NS03 | White core field between green ESP bar and footer — claim-stack separation | NEGATIVE_SPACE |

---

## 3. M_CONSTRUCTION

| MCON_ID | PATTERN_LABEL | MOCC_SET | FUNCTION | STATUS | SYSTEM_LINK |
|---------|---------------|----------|----------|--------|-------------|
| MCON_ESP_01 | Emission Network Shield | 08, L01, L02 | heuristic + status | MANIFEST | MSYS_ESP_01 |
| MCON_ESP_02 | ESP Institutional Band | 03, 06 | trust + transaction | MANIFEST | MSYS_ESP_01 |
| MCON_ESP_03 | Multi-Fuel Gateway Stack | 05, 10, L03 | segment expansion | MANIFEST | MSYS_ESP_02 |
| MCON_ESP_04 | Numeric Brand Monolith | 02, 07, 11 | brand + SAE heuristic | MANIFEST | MSYS_ESP_01 |
| MCON_ESP_05 | Heritage + Motorsport Transfer | 04, 09, L04, L05 | status + affect | MANIFEST | MSYS_ESP_03 |
| MCON_ESP_06 | Premium Whitespace Frame | NS01–03, L06 | premium cue | LATENT | MSYS_ESP_01 |
| MCON_ESP_07 | Solid-over-Fluid Norm | LAC01 | category conformity | LACUNA | MSYS_ESP_01 |
| MCON_ESP_08 | Back Legal Wall | 15–18, LAC07 | obscuration + compliance | MANIFEST | MSYS_ESP_01 |

---

## 4. M_SYSTEM

### MSYS_ESP_01 — Emission-Network Hyper-Protection (MANIFEST)
**MCON_SET:** 01, 02, 04, 06, 08  
**GOAL:** Транзакция в premium 5W-30 через **ESP line sovereignty** + network lattice + Mobil 1 monolith; отличие от 0W-20 honeycomb и от mass-mid Super 3000.  
**CONFLICT_WITH:** MSYS_ESP_03 (motorsport vs emission framing)

### MSYS_ESP_02 — Multi-Fuel Hybrid Gateway (MANIFEST)
**MCON_SET:** 03  
**GOAL:** Захват gasoline + **diesel** + hybrid сегмента одним front lockup — снижение fleet-buyer search cost.  
**CONFLICT_WITH:** LAC08 (Low-SAPS chemistry не названа явно)

### MSYS_ESP_03 — Motorsport Heritage Transfer (MANIFEST)
**MCON_SET:** 05  
**GOAL:** Prestige borrow через Oracle Red Bull Racing + 50 YEARS — компенсация import-channel anxiety.  
**CONFLICT_WITH:** MSYS_ESP_01 (eco-emission vs F1 hyperbole)

---

## 5. DOMAIN

| | Source (A) | Target (B) |
|---|------------|------------|
| **Ontology** | Emission-control engineering, digital sensor networks, catalytic aftertreatment, motorsport prestige | Low-/Mid-SAPS full-synthetic tribology, DPF/TWC protection, SAE 5W-30 multi-fuel service |
| **Embodiment** | Green institutional band, node-link lattice, monolithic «1», F1 co-brand | Invisible oil film, SAPS-controlled chemistry, compliant exhaust system |
| **Affect** | Controlled eco-confidence + premium calm | Anxiety relief (DPF clogging, mixed fleet, hybrid compatibility) |
| **Conflict** | Network lattice + F1 **colonise** fluid target — масло как «система связей» и «гоночная мощь», не «поток» | |

---

## 6. MAP (MAP1–MAP10 summary)

| MAP | Profile |
|-----|---------|
| **MAP1** Identity | Mobil 1 ESP sub-line; premium tier; emission-adjacent 5W-30 |
| **MAP2** Domain | A: emission network + heritage/motorsport → B: 5W-30 Low-SAPS tribology; fidelity **medium-low** |
| **MAP3** S | High SAE/brand/ESP signal; low lab-signal; multi-fuel redundancy |
| **MAP4** C | Silver-grey HDPE; green cap; 4L handle-jug; back legal wall dense |
| **MAP5** M | Shelf: green ESP band + large 5W-30 break noise; Mobil 1 family block |
| **MAP6** K | Vertical stack left: logo → ESP bar → claims → footer; right: pattern + 5W-30 |
| **MAP7** Invariants | Solid>Fluid; SAE right-anchor; Mobil blue-red; green = ESP line code |
| **MAP8** Shannon | Medium-high entropy on claims; anniversary + F1 add decorative noise |
| **MAP9** Context | 5W-30 C3/ESP niche — adjacent to GENESIS GC / GPN C3 point-ref; below 0W-20 frontier |
| **MAP10** Local RU | Import-facing; Cyrillic **н/д**; back unreadable — overlay **н/д** |

**MAP summary:** Rhetoric **7/10** · Fidelity **4/10** · Cognitive load **medium** · Obscuration **high** (specs deferred to unreadable back + no API front)

---

## 7. S / C / M / K (compressed _full)

### S — Signal structure
- **S1 DomainOfArgument:** Emission system protection + multi-fuel + synthetic tier + hybrid readiness.
- **S3 Discreteness:** Discrete horizontal bands (ESP green → white claims → footer badges).
- **S9 Correlation:** 5W-30 visually bound to green network panel — correlated heuristic (cf. honeycomb 0W-20).
- **S11 Information:** Low lab-information fraction; high brand/line/emotion fraction.

### C — Carrier
- **C1:** HDPE silver-grey metallic mimicry; green cap as line accent.
- **C2:** 4L jug, integrated handle — mass retail service format.
- **C5:** Typography-dominant left column; pattern secondary on right.
- **C7:** Multimodal: text + icon + F1 logo + QR + back barcode.

### M — Medium
- **M6 Noise:** Category shelf high; green ESP band aids break-through vs white-field competitors.
- **M10 Comm:** Premium auto + marketplace import; multi-fuel text speaks to fleet/sto buyer.
- **M11 Soc:** Global Mobil 1 equity; Red Bull borrows youth/performance; import anxiety **н/д** offset.

### K — Composition
- **K1 Structure:** Header (brand) → core (ESP + claims + viscosity panel) → footer (F1 + hybrid + vol).
- **K3 Tone:** Cool grey + institutional green + Mobil blue/red; restrained vs Super 3000 plasma.
- **K5 Morph:** Network graph = dominant K-pattern on right; black square «1» = secondary icon.
- **K7 Density:** Medium front; **very high** back (legal wall — content **н/д**).
- **K9 Perception:** Scan path: logo → «1» → green ESP → 5W-30 → (F1/hybrid footer).

---

## 8. EVAL + STM Blueprint

### EVAL vectors

| Vector | Score | Note |
|--------|-------|------|
| Transaction speed | High | ESP + 5W-30 + multi-fuel = fast filter for emission-anxious buyer |
| Trust / institutional | Medium | ESP framing strong; no API/OEM front; import unverified |
| Engineering transparency | Low | Back unreadable; no HTHS/SAPS on face |
| Rhetorical fidelity | Medium-low | Network metaphor + F1 vs real Low-SAPS chemistry |
| Premium perception | High | Whitespace + Mobil 1 + anniversary + F1 |
| RU localization | Low | EN-only visible; STM opportunity |

### EVAL_AGG
Mobil 1 ESP 5W-30 — **tier-1 premium point-ref** для 5W-30 emission-adjacent niche: **line-in-name sovereignty** (ESP) + **multi-fuel front** + **green institutional cue** с network solid metaphor. Сильнее GPN/LUKOIL в global brand whitespace; **слабее** в front API/ACEA vs [30](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md) / [32](32_PGMM_Gazpromneft_Premium_C3_5W-30.md). Shared Mobil 1 DNA с [19](19_PGMM_mobil_1_0w_20_5L.md): monolith «1», hybrid badge, synthetic stack — но **ESP green** заменяет honeycomb + dexos1 front strategy.

### STM blueprint (антидот · Modern/Protect proxy · 5W-30)

| Mobil 1 ESP 5W-30 | СТМ (дизайн-вектор) |
|-------------------|---------------------|
| Green network lattice (solid metaphor) | **Fluid-precision** или **clean flat** — один hero cue |
| ESP acronym without C3/API proof | **Named Low-SAPS + API SP + ACEA C2/C3 on front** |
| Multi-fuel hyperbole without SAPS metric | **One hero claim + verifiable SAPS/HTHS** |
| F1 / anniversary decorative noise | **Official supply + lab proof** вместо borrowed prestige |
| EN-only import face | **Integrated Cyrillic** + verified QR |
| OEM **н/д** on front | **Readable OEM band** (VW/BMW/MB proxy) |
| Back-loaded unreadable specs | **Front-loaded fair brief** + fair back |
| 4L only (this CASE) | ~~**4L + 1L** separate briefs~~ → [39](39_PGMM_mobil_1_esp_5w_30_1L_delta.md) ✅ |

### Cross-peer (5W-30 point-ref)

| SKU | M_SYSTEM core | Front spec | STM lesson |
|-----|---------------|------------|------------|
| **Mobil 1 ESP 5W-30** | Emission-network + multi-fuel | **—** API/ACEA | Line sovereignty + import prestige gap |
| LUKOIL GENESIS GC | Hyper-armor + German Cars | SN/CF · C3 | Segment banner + spec front |
| GPN Premium C3 | Spec-in-name + swirl | **SP · C2/C3** | Best front spec lockup in peer set |

---

## 9. Issues for discussion

1. **Back label readability:** Нужен higher-res back или overlay для ODSA — сейчас OEM/API grid **н/д**.
2. **ESP vs C3 naming:** Покупатель RU понимает «ESP» или нужен «C3 / Low SAPS» duet на лице?
3. **vs Mobil 1 0W-20:** ESP (5W-30) vs flagship 0W-20 — cannibalization или complementary SKUs в import shelf?
4. **Red Bull + emission:** Совместимость motorsport badge с DPF narrative — этический/claims риск для СТМ?
5. **Point-ref scope:** Держать вне матриц (как GC/C3) или расширять 5W-30 C3 ветку?
6. ~~**Next passes:** `stm-pgmm-delta` (1L vs 4L)~~ → [39](39_PGMM_mobil_1_esp_5w_30_1L_delta.md) ✅ · ~~**`stm-odsa`** (claims audit 1L+4L)~~ → [40](40_ODSA_mobil_1_esp_5w_30_4L.md) · [41](41_ODSA_mobil_1_esp_5w_30_1L.md) ✅ · optional: rescan 4L back.

---

## 10. Связи

- Mobil 1 flagship: [19_PGMM_mobil_1_0w_20_5L.md](19_PGMM_mobil_1_0w_20_5L.md) · [21_ODSA_mobil_1_0w_20_5L.md](21_ODSA_mobil_1_0w_20_5L.md)
- Mobil mass-mid: [12_PGMM_mobil_super_3000_x1_5w_40.md](12_PGMM_mobil_super_3000_x1_5w_40.md)
- 5W-30 C3 peers: [30](30_PGMM_LUKOIL_GENESIS_Armortech_GC_5W-30.md) · [32](32_PGMM_Gazpromneft_Premium_C3_5W-30.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- SAE контекст: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md)

---

*Ingest wiki/38 · 25.06.2026 · PGMM _full Mobil 1 ESP 5W-30 4L · skill stm-pgmm*
