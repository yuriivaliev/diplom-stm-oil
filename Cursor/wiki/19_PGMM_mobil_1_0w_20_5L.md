# Анализ упаковки: Mobil 1 0W-20 5L (PGMM _full)

**Дата анализа:** 25.06.2026  
**CASE_ID:** `COMP_MOBIL_1_0W20_5L`  
**Объект:** Канистра 5L, фронтальная этикетка  
**Методология:** PGMM (Klepikov 2025) — M_OCCURRENCE → M_CONSTRUCTION → M_SYSTEM → DOMAIN → MAP → S/C/M/K → EVAL + Neuromarketing POV  
**Изображение:** фронт SKU (пользователь, 25.06.2026)

```yaml
CASE_TYPE: packaging_visual_metaphor
BRAND: Mobil / ExxonMobil
LINE: Mobil 1 (flagship full synthetic)
SAE: 0W-20
FORMAT: 5L
VIEW: front label
SEGMENT: premium synthetic (global tier-1)
REGION: european RU proxy
CHANNEL: import / parallel (прокси; ODSA не прогонялся)
```

**Контекст DR-B:** 0W-20 — ростовой фронтир synthetic (+10,1% л, +16% ₽, NI-PDF); рекомендуемый SKU СТМ ([03](03_DR-B_вязкости_SAE.md), [05](05_линейка_SKU_СТМ.md)). **Не смешивать** с матрицей 5W-40 mass-mid ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)).

---

## 1. System States

### Information Integrity
- **Lacunae:** API SP / ILSAC GF-6A на фронте — **н/д** (нечитаемо/отсутствует); ACEA C5/C6 — **н/д**; HTHS, Noack, ресурс — **н/д**; кириллица / RU-канал — **н/д** (import-facing).
- **Redundancy:** Тройной performance-stack («TOP PERFORMANCE» → «ULTIMATE PROTECTION» → «ADVANCED SYNTHETIC») + отдельный «ADVANCED FUEL ECONOMY» — семантическое дублирование «лучшести» без дифференциации механизма.
- **Contamination:** Honeycomb-паттерн одновременно читается как «молекулярная решётка», «аэрокосмический композит» и «пчелиные соты» — намеренная полисемия, не ошибка.
- **Collonisation:** Категорийный код «серебристый HDPE + крупная вязкость справа» ([12](12_PGMM_mobil_super_3000_x1_5w_40.md)) сохранён; флагман отличается **whitespace** и **OEM-бейджем**, но остаётся в семействе Mobil-silver.

### Logical Coherence
- **Conflict:** «ULTIMATE ENGINE PROTECTION» (абсолют) vs «ADVANCED FUEL ECONOMY» (экономия = меньше viscous drag) — совместимо трибологически, но риторически разные оси (броня vs эффiciency).
- **Contradiction:** «MODERN ENGINES» + hybrid badge vs отсутствие eco/fluid-метафор — modernity заявлена текстом, не визуализирована текучестью.

### System Dynamics
- **Anomaly:** **dexos1 GEN 3 (GM APPROVED)** на фронте — редкость для Mobil в РФ-контексте (cf. Mobil Super 3000: API off front, [18](18_ODSA_mobil_super_3000_x1_5w_40_4L.md)).
- **Potential:** Hybrid + 0W-20 + fuel economy = прямой мэппинг на рост китайского парка и GEELY OEM ([03](03_DR-B_вязкости_SAE.md)).
- **Limit:** Без back label / overlay — полнота claims **н/д**; PGMM только по видимому фронту.

### Relational States
- **Compromise:** Премиальный whitespace vs обязательный shelf-heuristic (крупный 0W-20, чёрная плашка performance).
- **Parity:** С honeycomb Mobil 1 делит категорийную норму **Solid > Fluid** с LUKOIL/GPN/Super 3000 ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)).
- **Consensus:** «1» как монолитный brand icon — межформатный invariant линейки Mobil 1 globally.

---

## 2. M_OCCURRENCE

### 2.1 Manifest

| MOCC_ID | MATERIAL | SEGMENT | SURFACE_FORM | DOMAIN_A_HINT | DOMAIN_B_HINT | MAP_OP | STATUS |
|---------|----------|---------|--------------|---------------|---------------|--------|--------|
| MOCC_M1_01 | color+text | header | Wordmark «Mobil» blue + red «1» | corporate identity | brand trust | literal | MANIFEST |
| MOCC_M1_02 | graphic | header | White «1» in black square | monolith/seal | flagship tier | hyperbole | MANIFEST |
| MOCC_M1_03 | text | core | Black bar «TOP PERFORMANCE FOR MODERN ENGINES» | modern powertrain | spec compliance | projection | MANIFEST |
| MOCC_M1_04 | text | core | «ULTIMATE ENGINE PROTECTION» | armor/fortress | anti-wear | hyperbole | MANIFEST |
| MOCC_M1_05 | text | core | «ADVANCED SYNTHETIC TECHNOLOGY ENGINE OIL» | lab/precision | PAO/estol ester base | substitution | MANIFEST |
| MOCC_M1_06 | text | core | «ADVANCED FUEL ECONOMY» | efficiency engineering | low HTHS / friction | projection | MANIFEST |
| MOCC_M1_07 | text+scale | core-right | «0W-20» oversized | metrology badge | SAE viscosity | literal | MANIFEST |
| MOCC_M1_08 | pattern | core-right | Honeycomb / hex mesh dark grey | biomimetic lattice | molecular structure | metaphor | MANIFEST |
| MOCC_M1_09 | logo | footer | dexos1™ GEN 3 (GM APPROVED) | institutional OEM | GM spec gate | literal | MANIFEST |
| MOCC_M1_10 | icon+text | footer-left | «ALSO RECOMMENDED FOR HYBRIDS» + plug-car | electrified drivetrain | Atkinson/hybrid cycle | projection | MANIFEST |
| MOCC_M1_11 | text | footer-right | «5L» | volume metrology | pack size | literal | MANIFEST |
| MOCC_M1_12 | code | footer-left | QR/matrix datamatrix | digital trace | anti-counterfeit? | latent | MANIFEST |
| MOCC_M1_13 | form | carrier | Metallic silver HDPE + grip ridges | industrial container | utility | literal | MANIFEST |

### 2.2 Latent

| MOCC_ID | HINT | STATUS |
|---------|------|--------|
| MOCC_M1_L01 | Honeycomb → molecular packing / structural integrity (beehive ↔ polymer lattice) | LATENT |
| MOCC_M1_L02 | «Modern engines» codes Turbo-GDI, low-SAPS, hybrid without naming | LATENT |
| MOCC_M1_L03 | Black square «1» → premium seal / app-icon morphology | LATENT |
| MOCC_M1_L04 | Fuel economy bridges eco and performance for 0W-20 buyer | LATENT |
| MOCC_M1_L05 | Light grey upper field → clinical premium (vs Super 3000 steel gradient) | LATENT |

### 2.3 Lacunae

| MOCC_ID | GAP | STATUS |
|---------|-----|--------|
| MOCC_M1_LAC01 | Fluid / hydrodynamic / pour visualization | LACUNA |
| MOCC_M1_LAC02 | API SP / ILSAC front mark | LACUNA |
| MOCC_M1_LAC03 | ACEA C5/C6, OEM beyond GM (VW, BMW, etc.) | LACUNA |
| MOCC_M1_LAC04 | Cyrillic / official RU supply marker | LACUNA |
| MOCC_M1_LAC05 | Lab metrics (HTHS, Noack, drain interval) | LACUNA |
| MOCC_M1_LAC06 | Anti-fraud explicit layer (cf. GPN 3662.ru) | LACUNA |

### 2.4 Negative space

| MOCC_ID | DESCRIPTION | STATUS |
|---------|-------------|--------|
| MOCC_M1_NS01 | Upper light-grey band — deliberate premium breathing room (~25% label height) | NEGATIVE_SPACE |
| MOCC_M1_NS02 | Left text column vs right honeycomb — asymmetric balance, Z-scan anchor | NEGATIVE_SPACE |

---

## 3. M_CONSTRUCTION

| MCON_ID | PATTERN_LABEL | MOCC_SET | FUNCTION | STATUS | SYSTEM_LINK |
|---------|---------------|----------|----------|--------|-------------|
| MCON_M1_01 | Lattice Performance Shield | 08, L01 | heuristic + status | MANIFEST | MSYS_M1_01 |
| MCON_M1_02 | Modernity Claim Stack | 03–06 | trust + transaction | MANIFEST | MSYS_M1_01 |
| MCON_M1_03 | Numeric Brand Monolith | 02, 07 | brand + SAE heuristic | MANIFEST | MSYS_M1_01 |
| MCON_M1_04 | OEM Authority Front | 09 | institutional trust | MANIFEST | MSYS_M1_02 |
| MCON_M1_05 | Hybrid Frontier Badge | 10 | segment expansion | MANIFEST | MSYS_M1_03 |
| MCON_M1_06 | Premium Whitespace Frame | NS01, NS02, L05 | premium cue | LATENT | MSYS_M1_01 |
| MCON_M1_07 | Solid-over-Fluid Norm | LAC01 | category conformity | LACUNA | MSYS_M1_01 |

---

## 4. M_SYSTEM

### MSYS_M1_01 — Bio-Lattice Hyper-Performance (MANIFEST)
**MCON_SET:** 01, 02, 03, 06, 07  
**GOAL:** Транзакция в premium-0W-20 через stacked performance claims + biomimetic lattice; отличие от mass-mid «плазменной брони» Super 3000.  
**CONFLICT_WITH:** MSYS_M1_03 (eco-modern без eco-визуала)

### MSYS_M1_02 — Institutional OEM Sovereignty (MANIFEST)
**MCON_SET:** 04  
**GOAL:** Доверие через dexos1 Gen3 на фронте — снижение anxiety при import-канале.  
**CONFLICT_WITH:** LAC04 (нет RU official supply на лице)

### MSYS_M1_03 — Eco-Modern Gateway (LATENT)
**MCON_SET:** 05, 06; MOCC 06, 10  
**GOAL:** Захват hybrid / fuel-economy сегмента без «зелёного» дизайна.  
**CONFLICT_WITH:** LAC01 (fluid/eco imagery suppressed)

---

## 5. DOMAIN

| | Source (A) | Target (B) |
|---|------------|------------|
| **Ontology** | Biomimetic engineering, aerospace honeycomb composites, modern powertrain ecology | Low-viscosity full-synthetic tribology, hybrid/Atkinson-cycle engines |
| **Embodiment** | Rigid lattice, monolithic «1», institutional OEM badge | Invisible oil film, SAPS-controlled chemistry, SAE 0W-20 |
| **Affect** | Controlled confidence, premium calm | Anxiety relief (engine longevity + fuel cost) |
| **Conflict** | Solid lattice **colonises** fluid target — масло как «структура», не «поток» | |

---

## 6. MAP (MAP1–MAP10 summary)

| MAP | Profile |
|-----|---------|
| **MAP1** Identity | Global flagship Mobil 1; premium tier above Super 3000 |
| **MAP2** Domain | A: lattice/modernity → B: 0W-20 tribology; fidelity **medium** (better than Super 3000 rhetoric, worse than lab literal) |
| **MAP3** S | High SAE/brand signal; low lab-signal; claim-stack redundancy |
| **MAP4** C | Silver HDPE metallic mimicry; 5L handle-jug; QR latent channel |
| **MAP5** M | Shelf @1.2m: 0W-20 + «1» square break noise; less claustrophobic than Super 3000 |
| **MAP6** K | Asymmetric Z-layout; split grey field + dark honeycomb |
| **MAP7** Invariants | Solid>Fluid; SAE right-anchor; Mobil blue-red |
| **MAP8** Shannon | Medium-high entropy on claims; OEM badge = high-trust low-noise anchor |
| **MAP9** Context | 0W-20 growth + China park proxy; hybrid badge aligned with DR-B |
| **MAP10** Local RU | Import-facing; Cyrillic lacuna; overlay **н/д** on this photo |

**MAP summary:** Rhetoric **7/10** · Fidelity **5/10** · Cognitive load **medium-low** (cleaner than Super 3000) · Obscuration **moderate** (OEM front, API absent)

---

## 7. S / C / M / K (compressed _full)

### S — Signal structure
- **S1 DomainOfArgument:** Engine protection + fuel economy + modern/hybrid powertrains.
- **S3 Discreteness:** Discrete blocks (bar → claims → viscosity → badges).
- **S9 Correlation:** 0W-20 visually bound to honeycomb zone — correlated heuristic.
- **S11 Information:** Low lab-information fraction; high brand/OEM fraction.

### C — Carrier
- **C1:** HDPE, silver metallic ink/foil mimicry.
- **C2:** 5L jug, integrated handle, grip ridges — mass retail affordance.
- **C5:** Typography-dominant encoding; pattern secondary.
- **C7:** Multimodal: text + icon + OEM logo + QR.

### M — Medium
- **M6 Noise:** Category shelf very high; whitespace strategy reduces internal noise vs [12](12_PGMM_mobil_super_3000_x1_5w_40.md).
- **M10 Comm:** Premium auto channel + marketplace; hybrid badge speaks to informed buyer.
- **M11 Soc:** Global brand equity; import/parallel anxiety partially offset by dexos1.

### K — Composition
- **K1 Structure:** Header (brand) → core (claims + viscosity) → footer (OEM + hybrid + vol).
- **K3 Tone:** Cool grey + black + Mobil blue/red; restrained vs Super 3000 plasma.
- **K5 Morph:** Honeycomb = dominant K-pattern; square «1» = secondary icon.
- **K7 Density:** Medium — premium whitespace vs Super 3000 «gravitational compression».
- **K9 Perception:** Scan path: logo → «1» → black bar → 0W-20 → dexos1.

---

## 8. EVAL + STM Blueprint

### EVAL vectors

| Vector | Score | Note |
|--------|-------|------|
| Transaction speed | High | 0W-20 + «1» + dexos1 = fast shortlist for hybrid/modern SAE buyer |
| Trust / institutional | Medium-high | GM badge front; import channel unverified on this view |
| Engineering transparency | Low-medium | Better OEM front than Super 3000; still no API/HTHS |
| Rhetorical fidelity | Medium | Lattice metaphor less hyperbolic than plasma armor |
| Premium perception | High | Whitespace + flagship lockup |
| RU localization | Low | EN-only visible; STM opportunity |

### EVAL_AGG
Mobil 1 0W-20 — **premium reference** для SAE-фронтира: biomimetic solid metaphor + **OEM-on-front** + hybrid/fuel-economy stack. Сильнее в institutional trust, чем Super 3000 5W-40; слабее в RU-channel и lab transparency. Для СТМ 0W-20 — **не копировать lattice**, но **перенять OEM-front + hybrid-ready claims** с полной кириллицей и official supply.

### STM blueprint (антидот для 0W-20 SKU)

| Mobil 1 0W-20 | СТМ 0W-20 (дизайн-вектор) |
|---------------|---------------------------|
| Honeycomb lattice (solid metaphor) | **Fluid-precision** или **clean flat** — whitespace без «сот» |
| EN-only import face | **Integrated Cyrillic** + API SP + ACEA C5 on front |
| GM-only OEM front | **Multi-OEM row** (GEELY/VW/Toyota proxy per DR-B) |
| Claim stack без механизма | **One hero claim + lab proof** (HTHS, SAPS, drain km) |
| QR без явного anti-fraud | **Verified QR** + official supply mark |
| Hybrid badge secondary | **0W-20 + China/OEM** as primary segment story |
| 5L only (this CASE) | **4L + 1L** separate briefs ([stm-pgmm-delta](../.cursor/skills/stm-pgmm-delta/SKILL.md)) |

---

## 9. Issues for discussion

1. **Back label / RU overlay:** Есть ли overlay на импортном SKU? Без него ODSA и claims audit неполны.
2. **API SP front:** Отсутствие на фронте — сознательный premium minimalism или regional variant?
3. **0W-20 matrix scope:** Включать ли Mobil 1 в отдельную матрицу 0W-20 (наряду с 5W-40 ×3) или достаточно point reference для этапа 5–6?
4. **Format delta:** 1L / 4L Mobil 1 0W-20 — нужен ли `stm-pgmm-delta` pass?
5. **Retail validation:** Honeycomb + whitespace — читается ли @1.2 m vs Super 3000 на полке (LAC-03 из [08](08_PGMM_упаковка.md))?

---

## 10. Связи

- SAE контекст: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md)
- SKU СТМ: [05_линейка_SKU_СТМ.md](05_линейка_SKU_СТМ.md)
- Mobil mass-mid proxy: [12_PGMM_mobil_super_3000_x1_5w_40.md](12_PGMM_mobil_super_3000_x1_5w_40.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Delta 1L: [20_PGMM_mobil_1_0w_20_1L_delta.md](20_PGMM_mobil_1_0w_20_1L_delta.md)
- Next: `stm-odsa` (claims audit) · `stm-pgmm-delta` (4L, если образец)

---

*Ingest wiki/19 · 25.06.2026 · PGMM _full Mobil 1 0W-20 5L · skill stm-pgmm*
