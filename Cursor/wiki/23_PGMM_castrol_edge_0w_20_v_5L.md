# Анализ упаковки: Castrol EDGE 0W-20 V 5L (PGMM _full)

**Дата анализа:** 25.06.2026  
**CASE_ID:** `COMP_CASTROL_EDGE_0W20V_5L`  
**Объект:** Канистра 5L, фронт + тыл этикетки  
**Методология:** PGMM (Klepikov 2025) — M_OCCURRENCE → M_CONSTRUCTION → M_SYSTEM → DOMAIN → MAP → S/C/M/K → EVAL + Neuromarketing POV  
**Изображения:** фронт + back SKU (пользователь, 25.06.2026; watermark Top-Castrol.ru на фронте — фото ритейлера, не элемент SKU)

```yaml
CASE_TYPE: packaging_visual_metaphor
BRAND: Castrol / BP
LINE: EDGE (flagship full synthetic)
SAE: 0W-20 V
FORMAT: 5L
VIEW: front + back label
SEGMENT: premium synthetic (global tier-1)
REGION: european RU proxy
CHANNEL: EU manufacture · RU online retail proxy (Top-Castrol.ru photo)
```

**Контекст DR-B:** 0W-20 — ростовой фронтир synthetic (+10,1% л, +16% ₽, NI-PDF); ACEA C5 + Toyota/Honda OEM grid aligned с китайским парком и GEELY proxy ([03](03_DR-B_вязкости_SAE.md), [05](05_линейка_SKU_СТМ.md)). **Не смешивать** с матрицей 5W-40 mass-mid ([08_PGMM_упаковка.md](08_PGMM_упаковка.md)).

---

## 1. System States

### Information Integrity
- **Lacunae:** API SP / ILSAC GF-6A — **н/д** на видимом back (нечитаемо/отсутствует); HTHS, Noack, drain interval — **н/д**; кириллица / RU-overlay — **н/д** на EU-facing pack; FluidTitanium / «full synthetic» chemistry — **н/д** на видимых ракурсах.
- **Redundancy:** Тройной performance-stack («EDGE» → «UNLOCK THE VERY EDGE OF PERFORMANCE» → motorsport back) + HYSPEC hybrid + tri-fuel band (petrol/diesel/hybrid) — семантическое дублирование «максимума» без механизма на фронте.
- **Contamination:** «EDGE» одновременно читается как razor/cutting edge, motorsport boundary и brand line name — намеренная полисемия; золотой HDPE колонизирует «gold standard» без явного gold-claim.
- **Collonisation:** Категорийный код «крупная вязкость + цветной HDPE» сохранён; Castrol отличается **gold carrier + green HYSPEC wedge** vs Mobil silver + honeycomb ([19](19_PGMM_mobil_1_0w_20_5L.md)).

### Logical Coherence
- **Conflict:** «EDGE OF PERFORMANCE» (абсолют, power) vs ACEA C5 / Volvo RBS0-2AE (low-SAPS eco spec) — совместимо трибологически, но риторически power vs eco-compliance.
- **Contradiction:** HYSPEC «hybrid standard» front vs отсутствие eco/fluid-визуала — hybrid заявлен institutional badge, не текучестью.

### System Dynamics
- **Anomaly:** **HYSPEC** как собственный hybrid-spec lockup на фронте — сильнее institutional hybrid cue, чем secondary badge Mobil «ALSO RECOMMENDED FOR HYBRIDS» ([19](19_PGMM_mobil_1_0w_20_5L.md)).
- **Potential:** OEM grid Honda/Toyota/Nissan/Hyundai/Kia + Volvo — прямой мэппинг на японский и китайский парк; ACEA C5 = GEELY proxy ([03](03_DR-B_вязкости_SAE.md)).
- **Limit:** OEM **на back**, не на front — shelf heuristic без flip; PGMM back расширяет institutional layer, но retail @1.2 m = front-only.

### Relational States
- **Compromise:** Премиальный gold + green wedge vs обязательный tri-fuel compatibility band (petrol/diesel/hybrid) — расширение TAM без сегментной фокусировки.
- **Parity:** С Mobil 1 делит норму **Solid > Fluid** и **0W-20 right/center anchor** в premium 0W-20.
- **Consensus:** Castrol red-green logo + «EDGE» line lockup — межформатный invariant глобальной линейки EDGE.

---

## 2. M_OCCURRENCE

### 2.1 Manifest

| MOCC_ID | MATERIAL | SEGMENT | SURFACE_FORM | DOMAIN_A_HINT | DOMAIN_B_HINT | MAP_OP | STATUS |
|---------|----------|---------|--------------|---------------|---------------|--------|--------|
| MOCC_CE_01 | color+logo | header | Castrol red-green wordmark | corporate identity | brand trust | literal | MANIFEST |
| MOCC_CE_02 | graphic+text | header-left | HYSPEC wedge + «CASTROL'S HYBRID STANDARD» | institutional spec | hybrid powertrain gate | literal | MANIFEST |
| MOCC_CE_03 | graphic | header-left | Green diagonal speed stripes on wedge | motorsport motion | performance boundary | metaphor | MANIFEST |
| MOCC_CE_04 | text | core | «EDGE» oversized silver/white typography | cutting edge / blade | performance frontier | hyperbole | MANIFEST |
| MOCC_CE_05 | text | core | «UNLOCK THE VERY EDGE OF PERFORMANCE» | unlock/access | latent engine power | projection | MANIFEST |
| MOCC_CE_06 | text+scale | core | «0W-20 V» white box badge | metrology | SAE viscosity + Castrol V-line | literal | MANIFEST |
| MOCC_CE_07 | text | footer-band | «GASOLINE/PETROL • DIESEL • HYBRID» | tri-fuel universality | multi-powertrain compatibility | substitution | MANIFEST |
| MOCC_CE_08 | text | footer-right | «FINDCAROIL.COM» | digital channel | spec lookup / e-com | literal | MANIFEST |
| MOCC_CE_09 | text | footer-left | «5L e» volume mark | volume metrology | pack size | literal | MANIFEST |
| MOCC_CE_10 | form | carrier | Gold/bronze metallic HDPE + red ribbed cap | precious metal / trophy | premium tier | metaphor | MANIFEST |
| MOCC_CE_11 | text | back-header | «Castrol EDGE 0W-20 V» repeat lockup | brand continuity | SKU identity | literal | MANIFEST |
| MOCC_CE_12 | text | back-core | Performance + efficiency + motorsport testing narrative | track validation | epistemic proof | projection | MANIFEST |
| MOCC_CE_13 | logo-grid | back-core | OEM row: Honda, Hyundai, Kia, Lexus, Nissan, Toyota, Volvo | institutional authority | OEM approval | literal | MANIFEST |
| MOCC_CE_14 | text | back-footer | **ACEA C5** ; **Volvo VCC RBS0-2AE** | regulatory spec | low-SAPS / eco tribology | literal | MANIFEST |
| MOCC_CE_15 | text | back-footer | «MANUFACTURED IN THE EU» + Castrol Holding Europe B.V. | origin trace | supply legitimacy | literal | MANIFEST |
| MOCC_CE_16 | code | back-footer | EAN 4 008177 183935 + batch DE01…13/07/23 | logistics trace | anti-counterfeit latent | literal | MANIFEST |
| MOCC_CE_17 | logo | back-footer | BP logo (BP Lubricants UK Limited) | parent corporate | institutional backing | literal | MANIFEST |

### 2.2 Latent

| MOCC_ID | HINT | STATUS |
|---------|------|--------|
| MOCC_CE_L01 | Gold HDPE → «gold standard» premium without explicit gold claim | LATENT |
| MOCC_CE_L02 | Diagonal green stripes → velocity vector / checkered-flag fragment | LATENT |
| MOCC_CE_L03 | «V» suffix in 0W-20 V → Castrol Viscosity line / Volvo synergy (RBS0-2AE) | LATENT |
| MOCC_CE_L04 | «UNLOCK» → gamification / hidden potential in engine | LATENT |
| MOCC_CE_L05 | Tri-fuel band expands buyer universe vs Mobil hybrid-only secondary cue | LATENT |
| MOCC_CE_L06 | Motorsport back narrative legitimises front hyperbole epistemically | LATENT |

### 2.3 Lacunae

| MOCC_ID | GAP | STATUS |
|---------|-----|--------|
| MOCC_CE_LAC01 | Fluid / hydrodynamic / pour visualization | LACUNA |
| MOCC_CE_LAC02 | API SP / ILSAC GF-6A (front + visible back) | LACUNA |
| MOCC_CE_LAC03 | OEM logos **on front** (only back grid) | LACUNA |
| MOCC_CE_LAC04 | Cyrillic / official RU supply marker | LACUNA |
| MOCC_CE_LAC05 | Lab metrics (HTHS, Noack, SAPS, drain km) | LACUNA |
| MOCC_CE_LAC06 | FluidTitanium / full synthetic chemistry name on visible faces | LACUNA |
| MOCC_CE_LAC07 | Anti-fraud explicit layer (cf. GPN 3662.ru) | LACUNA |
| MOCC_CE_LAC08 | QR / verified digital trace on pack | LACUNA |

### 2.4 Negative space

| MOCC_ID | DESCRIPTION | STATUS |
|---------|-------------|--------|
| MOCC_CE_NS01 | White central field behind EDGE — premium breathing room (~30% label height) | NEGATIVE_SPACE |
| MOCC_CE_NS02 | Back label white panel vs gold HDPE surround — clinical spec zone | NEGATIVE_SPACE |
| MOCC_CE_NS03 | Asymmetric wedge (left) vs viscosity box (center-bottom) — Z-scan anchor | NEGATIVE_SPACE |

---

## 3. M_CONSTRUCTION

| MCON_ID | PATTERN_LABEL | MOCC_SET | FUNCTION | STATUS | SYSTEM_LINK |
|---------|---------------|----------|----------|--------|-------------|
| MCON_CE_01 | HYSPEC Hybrid Sovereignty | 02, 03 | institutional trust + segment | MANIFEST | MSYS_CE_01 |
| MCON_CE_02 | Edge Hyperbole Stack | 04, 05, 12, L04, L06 | heuristic + status | MANIFEST | MSYS_CE_02 |
| MCON_CE_03 | Viscosity Hero Badge | 06, L03 | transaction + SAE heuristic | MANIFEST | MSYS_CE_02 |
| MCON_CE_04 | Tri-Fuel Universality Band | 07, L05 | transaction expansion | MANIFEST | MSYS_CE_03 |
| MCON_CE_05 | Gold Trophy Carrier | 10, L01 | premium cue + status | MANIFEST | MSYS_CE_02 |
| MCON_CE_06 | Back OEM Authority Grid | 13, 14 | institutional trust | MANIFEST | MSYS_CE_04 |
| MCON_CE_07 | Motorsport Epistemic Bridge | 12, L06 | trust (track → street) | MANIFEST | MSYS_CE_02 |
| MCON_CE_08 | Digital Lookup Footer | 08 | channel + latent trust | MANIFEST | MSYS_CE_05 |
| MCON_CE_09 | Solid-over-Fluid Norm | LAC01 | category conformity | LACUNA | MSYS_CE_02 |
| MCON_CE_10 | Front OEM Lacuna | LAC03 | obscuration (spec behind flip) | LACUNA | MSYS_CE_04 |

---

## 4. M_SYSTEM

### MSYS_CE_01 — HYSPEC Hybrid Institutional Gate (MANIFEST)
**MCON_SET:** 01  
**GOAL:** Дифференциация в 0W-20 через **собственный hybrid standard** на фронте — снижение anxiety hybrid/modern buyer без «зелёного» fluid-дизайна.  
**CONFLICT_WITH:** MSYS_CE_03 (tri-fuel dilutes hybrid focus)

### MSYS_CE_02 — Edge-of-Performance Hyperbole (MANIFEST)
**MCON_SET:** 02, 03, 05, 07, 09  
**GOAL:** Транзакция в premium-0W-20 через абсолютную performance риторику + gold carrier + motorsport back-bridge.  
**CONFLICT_WITH:** MSYS_CE_04 (eco ACEA C5 on back only)

### MSYS_CE_03 — Tri-Fuel TAM Expansion (MANIFEST)
**MCON_SET:** 04  
**GOAL:** Расширение адресуемого парка (petrol + diesel + hybrid) на одном SKU.  
**CONFLICT_WITH:** MSYS_CE_01 (hybrid specificity vs universal band)

### MSYS_CE_04 — Back-Loaded OEM Sovereignty (MANIFEST)
**MCON_SET:** 06, 10  
**GOAL:** Institutional trust через 7-brand OEM grid + ACEA C5 + Volvo RBS0-2AE — для informed buyer после flip или pre-research.  
**CONFLICT_WITH:** LAC03 (shelf @1.2 m не видит OEM)

### MSYS_CE_05 — Digital Spec Channel (LATENT)
**MCON_SET:** 08  
**GOAL:** Перенос полноты claims на FINDCAROIL.COM — channel asymmetry (cf. GPN site superset pattern в [08_PGMM_упаковка.md](08_PGMM_упаковка.md)).  
**CONFLICT_WITH:** LAC07, LAC08 (no on-pack verified digital)

---

## 5. DOMAIN

| | Source (A) | Target (B) |
|---|------------|------------|
| **Ontology** | Cutting edge, motorsport boundary, gold trophy, hybrid institutional gate (HYSPEC) | Low-viscosity full-synthetic tribology, SAPS-controlled ACEA C5 chemistry, hybrid/Atkinson-cycle engines |
| **Embodiment** | Rigid wedge, diagonal velocity stripes, gold solid carrier | Invisible oil film, low HTHS fluid, SAE 0W-20 V |
| **Affect** | Adrenaline confidence, premium warmth (gold) | Anxiety relief (OEM longevity + fuel efficiency) |
| **Conflict** | Solid edge/gold **colonises** fluid target — масло как «граница/металл», не «поток» | |

---

## 6. MAP (MAP1–MAP10 summary)

| MAP | Profile |
|-----|---------|
| **MAP1** Identity | Global flagship Castrol EDGE; premium tier; BP parent on back |
| **MAP2** Domain | A: edge/motorsport/gold → B: 0W-20 tribology; fidelity **medium-low** (hyperbole > lab) |
| **MAP3** S | High SAE/EDGE/HYSPEC signal; medium OEM (back-only); API lacuna |
| **MAP4** C | Gold HDPE metallic; 5L jug + handle; red cap contrast; EU batch trace |
| **MAP5** M | Shelf @1.2m: gold + green wedge + 0W-20 break noise; OEM invisible without flip |
| **MAP6** K | Diagonal wedge + central EDGE typography; green footer band |
| **MAP7** Invariants | Solid>Fluid; SAE center-bottom; Castrol red-green |
| **MAP8** Shannon | Medium entropy (fewer stacked bars than Mobil); HYSPEC = high-trust anchor |
| **MAP9** Context | 0W-20 growth + Japan/China park; ACEA C5 = GEELY proxy |
| **MAP10** Local RU | EU pack; Top-Castrol.ru photo; Cyrillic lacuna; overlay **н/д** |

**MAP summary:** Rhetoric **8/10** · Fidelity **4/10** · Cognitive load **medium** · Obscuration **moderate-high** (OEM back-only, API absent visible)

---

## 7. S / C / M / K (compressed _full)

### S — Signal structure
- **S1 DomainOfArgument:** Performance edge + hybrid standard + tri-fuel compatibility + OEM (back).
- **S3 Discreteness:** Discrete blocks (HYSPEC wedge → EDGE → viscosity → fuel band → back grid).
- **S9 Correlation:** 0W-20 V bound to white box; HYSPEC wedge correlated with hybrid narrative.
- **S11 Information:** Low lab-information fraction; high brand/institutional fraction on back.

### C — Carrier
- **C1:** HDPE, gold/bronze metallic effect; red ribbed cap.
- **C2:** 5L jug, integrated handle — mass retail affordance.
- **C5:** Typography-dominant (EDGE); wedge graphic secondary.
- **C7:** Multimodal: text + OEM logo grid + BP parent + EAN.

### M — Medium
- **M6 Noise:** Category shelf high; gold distinguishes from Mobil silver cluster.
- **M10 Comm:** EU manufacture + RU online retail proxy; FINDCAROIL.COM digital escape.
- **M11 Soc:** Global Castrol equity; F1/motorsport heritage latent in copy.

### K — Composition
- **K1 Structure:** Front: wedge → brand → EDGE → viscosity → tri-fuel. Back: narrative → OEM grid → specs.
- **K3 Tone:** Gold + Castrol green + red accents; warmer than Mobil cool grey.
- **K5 Morph:** Diagonal wedge = dominant K-pattern; EDGE typography = secondary icon.
- **K7 Density:** Medium front; high density back (multilingual + OEM grid).
- **K9 Perception:** Scan path: HYSPEC wedge → Castrol → EDGE → 0W-20 → green band.

---

## 8. EVAL + STM Blueprint

### EVAL vectors

| Vector | Score | Note |
|--------|-------|------|
| Transaction speed | High | Gold + EDGE + 0W-20 + HYSPEC = fast shortlist for hybrid/modern SAE buyer |
| Trust / institutional | Medium-high | Strong back OEM grid + ACEA C5; front OEM lacuna |
| Engineering transparency | Low-medium | ACEA/Volvo on back; API/HTHS н/д visible |
| Rhetorical fidelity | Medium-low | Edge hyperbole + motorsport bridge; less biomimetic than Mobil lattice |
| Premium perception | High | Gold carrier + flagship EDGE lockup |
| RU localization | Low | EU EN-facing; STM opportunity |

### EVAL_AGG
Castrol EDGE 0W-20 V — **premium reference #2** для SAE-фронтира (после Mobil 1 [19](19_PGMM_mobil_1_0w_20_5L.md)): **HYSPEC hybrid gate на фронте** (сильнее Mobil secondary badge) + **gold solid metaphor** + **back-loaded multi-OEM**. Слабее в front OEM/API и RU-channel. Для СТМ 0W-20 — **не копировать gold/edge hyperbole**, но **перенять hybrid-standard front lockup + multi-OEM front row** с кириллицей и official supply.

### STM blueprint (антидот для 0W-20 SKU)

| Castrol EDGE 0W-20 V | СТМ 0W-20 (дизайн-вектор) |
|----------------------|---------------------------|
| Gold HDPE + edge hyperbole | **Fluid-precision** или **clean flat** — не trophy gold |
| HYSPEC wedge (strong hybrid) | **Own eco/hybrid spec badge** front — но с lab proof, не только institutional |
| OEM grid **back-only** | **Multi-OEM row on front** (Toyota/Honda/GEELY proxy) |
| API SP н/д visible | **API SP + GF-6A + ACEA C5 on front** |
| Tri-fuel universal band | **Segment-focused** (0W-20 modern/hybrid) vs diluted TAM |
| FINDCAROIL.COM escape | **Verified QR** + pack = web parity |
| Motorsport narrative без механизма | **One hero claim + tribology proof** (HTHS, SAPS, drain km) |
| 5L only (this CASE) | **1L** ✅ [24](24_PGMM_castrol_edge_0w_20_v_1L_delta.md); **4L** — если образец |

### Cross-ref premium 0W-20 pair

| Dimension | Mobil 1 0W-20 5L | Castrol EDGE 0W-20 V 5L |
|-----------|------------------|-------------------------|
| Carrier | Silver HDPE | Gold HDPE |
| Dominant metaphor | Honeycomb lattice | Cutting EDGE + speed wedge |
| Hybrid cue | Secondary footer badge | **HYSPEC front institutional** |
| OEM front | dexos1 Gen3 **front** | **н/д front** (back grid) |
| API visible | н/д front | н/д visible |
| ACEA | н/д front | **C5 back** |
| Digital | QR latent | FINDCAROIL.COM |

---

## 9. Issues for discussion

1. **RU overlay:** Есть ли кириллический overlay на импортном SKU? Без него ODSA неполон.
2. **API SP / GF-6A:** На полной back label ниже fold — нужен zoom или ODSA pass.
3. **0W-20 matrix:** Включать Castrol EDGE в отдельную матрицу 0W-20 (Mobil + Castrol × formats)?
4. **HYSPEC vs tri-fuel band:** Противоречие hybrid-focus vs universal — retail test?
5. **Format delta:** 1L ✅ [24](24_PGMM_castrol_edge_0w_20_v_1L_delta.md); 4L — если образец
6. **Next:** ODSA ✅ [25](25_ODSA_castrol_edge_0w_20_v_5L.md) · delta 1L ODSA: [26](26_ODSA_castrol_edge_0w_20_v_1L.md)

---

## 10. Связи

- SAE контекст: [03_DR-B_вязкости_SAE.md](03_DR-B_вязкости_SAE.md)
- SKU СТМ: [05_линейка_SKU_СТМ.md](05_линейка_SKU_СТМ.md)
- Mobil 0W-20 pair: [19](19_PGMM_mobil_1_0w_20_5L.md) · [21](21_ODSA_mobil_1_0w_20_5L.md)
- Сводка этапа 4: [08_PGMM_упаковка.md](08_PGMM_упаковка.md)
- Next: ODSA ✅ [25](25_ODSA_castrol_edge_0w_20_v_5L.md) · [26](26_ODSA_castrol_edge_0w_20_v_1L.md) · delta 1L: [24](24_PGMM_castrol_edge_0w_20_v_1L_delta.md)

---

*Ingest wiki/23 · 25.06.2026 · PGMM _full Castrol EDGE 0W-20 V 5L · skill stm-pgmm*
