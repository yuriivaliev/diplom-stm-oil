# ODSA — Mobil 1 ESP 5W-30 (1L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_1_ESP_5W30_1L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [39_PGMM_mobil_1_esp_5w_30_1L_delta.md](39_PGMM_mobil_1_esp_5w_30_1L_delta.md) · base 4L ODSA: [40_…](40_ODSA_mobil_1_esp_5w_30_4L.md)  
**Дата:** 25.06.2026 · **Rev. 1:** locked (front + back photo)  
**Формат:** 1L · import EU wrap · EN/TR/GR back · **parallel import proxy**

> **Отличие от 4L ODSA:** back **читаем** на фото — **primary line canon source** для API SP / ACEA C3 / OEM grid (EVID-ESP1-06…10).

---

## Executive summary (rev. 1 · locked)

**Канон SKU:** **Mobil 1 ESP 5W-30 1L** — advanced full synthetic · **API SP** (Meets SJ→SP) · **ACEA C3** · exceeds **ACEA C2** · German OEM stack on back.

**Cross-face (artifact):** **Partial @ shelf** — front **без** API/ACEA (EVID-ESP1-02); back **full Meets/Approved grid** (EVID-ESP1-06…08). **Within back block: Pass** — API/ACEA/OEM internally coherent.

**Cross-format (1L ↔ 4L):** Front wrap **≈ DRY rescale** (EVID-ESP1-01 vs [40](40_ODSA_mobil_1_esp_5w_30_4L.md) EVID-ESP4-01). Back: **1L readable** vs **4L photo unreadable** — **evidence asymmetry**, not proven SKU divergence (F-ESP1-09).

**vs peers (5W-30 C3):** **Слабее** LUKOIL GC / GPN C3 на **front spec**; **сильнее** на back OEM depth vs GPN microtype; **нет** Cyrillic / official RF.

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 5 |
| Minor | 3 |
| Positive | 4 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-ESP1-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 1L — ESP, multi-fuel, hybrid mid-label, 1L |
| ART-ESP1-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 1L — Meets/Approved grid, bullets, trilingual legal |
| ART-ESP1-003 | Document | wiki/39 | PGMM delta 1L |
| ART-ESP1-004 | Document | [40](40_ODSA_mobil_1_esp_5w_30_4L.md) | ODSA 4L — cross-format ref |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-ESP1-01 | Artifact | ART-ESP1-001 | Mobil **1**; **ESP EMISSION SYSTEM PROTECTION**; **ADVANCED SYNTHETIC TECHNOLOGY ENGINE OIL**; **5W-30**; **1L** | A | Active |
| EVID-ESP1-02 | Artifact | ART-ESP1-001 | **API / ACEA не на фронте** | A | Active |
| EVID-ESP1-03 | Artifact | ART-ESP1-001 | **FOR GASOLINE, DIESEL & HYBRID ENGINES** | A | Active |
| EVID-ESP1-04 | Artifact | ART-ESP1-001 | **ALSO RECOMMENDED FOR HYBRIDS** + blue icon **mid-label** | A | Active |
| EVID-ESP1-05 | Artifact | ART-ESP1-001 | **Mobil 1 50 YEARS** + **Oracle Red Bull Racing** footer | A | Active |
| EVID-ESP1-06 | Artifact | ART-ESP1-002 | Meets: **ACEA C3**; **API SJ/SL/SM/SN/SN PLUS/SP** | A | Active · **canon API** |
| EVID-ESP1-07 | Artifact | ART-ESP1-002 | Approved: **MB 229.31/229.51/229.52**; **VW 504 00/507 00**; **Porsche C30**; **BMW Longlife-04**; **Opel/Vauxhall OV 040 1547-D30/G30** | A | Active |
| EVID-ESP1-08 | Artifact | ART-ESP1-002 | ExxonMobil Quality Level: **Fiat 9.55535-S3**; **ACEA C2** (exceeds) | A | Active |
| EVID-ESP1-09 | Artifact | ART-ESP1-002 | Benefit bullets: cleaning; thermal stability; performance; efficiency; extended drain | A | Active |
| EVID-ESP1-10 | Artifact | ART-ESP1-002 | **5W-30** green badge; **1Le**; barcode **5 407008 073787**; QR «SCAN for more product information» | A | Active |
| EVID-ESP1-11 | Artifact | ART-ESP1-002 | Mold stamp: **MADE 28.02.2024 S420070 03544** | A | Active |
| EVID-ESP1-12 | Artifact | ART-ESP1-002 | Legal langs: **EN / TR / GR(CY)** — **нет RU** | A | Active |
| EVID-ESP1-13 | Context | ART-ESP1-003 | PGMM delta: back unlock; front lacuna; whitespace ↓ | B | Context |
| EVID-ESP1-14 | Context | Оператор 25.06.2026 | Parallel import; not official RF supply | B | Active |
| EVID-ESP1-15 | Context | [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) | Peer front API+ACEA benchmark | B | Context |
| EVID-ESP1-16 | Context | [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) | Peer front SP+C2/C3 benchmark | B | Context |

### Conflict notes

| Conflict | Evidence | Resolution |
|----------|----------|------------|
| Front no API vs back API SP list | ESP1-02 vs ESP1-06 | **Open (CR-ESP1-01)** — deictic split |
| Meets ACEA C3 vs QL exceeds C2 | ESP1-06 vs ESP1-08 | **Closed (CR-ESP1-02)** — exceeds semantics, not downgrade |
| 1L back readable vs 4L back unreadable photo | ESP1-06 vs [40] ESP4-08 | **Open (CR-ESP1-03)** — photo artifact |
| EN front vs TR/GR back (no RU) | ESP1-01 vs ESP1-12 | **Closed (CR-ESP1-04)** — export routing |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-ESP1-01 Digital triangulation (mobil1.com) | **Open** |
| GAP-ESP1-02 RU overlay sticker | **Open** — н/д (cf. Mobil 0W-20) |
| GAP-ESP1-03 QR landing content | Open |
| GAP-ESP1-04 Retail @1.2 m — back invisible on shelf | Open |

---

## Findings Catalogue

### F-ESP1-01 — Major · API / ACEA absent from front; full on back

| Поле | Значение |
|------|----------|
| **Observation** | Front (EVID-ESP1-02): **нет** API/ACEA. Back (EVID-ESP1-06): **API SP-class list + ACEA C3**. |
| **Evidence IDs** | EVID-ESP1-02; ESP1-06; ESP1-15; ESP1-16 |
| **Interpretation** | **Two-step trust** — buyer @ shelf 2 m **не видит** C3 proof; vs GPN/LUKOIL **front lockup**. |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | structural: СТМ 5W-30 C3 1L — **front API SP + ACEA C3** @ doliv arm's length |

---

### F-ESP1-02 — Major · OEM grid back-only — below doliv functional threshold

| Evidence IDs | EVID-ESP1-02; ESP1-07 |
| **Observation** | Full German OEM stack **только back**; front = ESP + multi-fuel only. |
| **Severity** | **Major** · **High** |

---

### F-ESP1-03 — Positive · Back spec block internally coherent (canon locked)

| Evidence IDs | EVID-ESP1-06; ESP1-07; ESP1-08 |
| **Observation** | Meets API through **SP** + ACEA **C3** + Approved OEM + exceeds **C2** — **no internal contradiction**. |
| **Severity** | **Positive** · **High** |

---

### F-ESP1-04 — Positive · API SP in Meets row — highest canon tier

| Evidence IDs | EVID-ESP1-06 |
| **Observation** | **SP** present in Meets list — канон по AGENTS (**SP > SN**). |
| **Severity** | **Positive** · **High** |

---

### F-ESP1-05 — Positive · Institutional back stack + QR + batch stamp

| Evidence IDs | EVID-ESP1-10; ESP1-11 |
| **Severity** | **Positive** · **High** |

---

### F-ESP1-06 — Positive · Hybrid cue repositioned — ↑ salience vs 4L footer

| Evidence IDs | EVID-ESP1-04; wiki/39 MOCC_ESPD_02 |
| **Severity** | **Positive** · **Medium** · still **↓ @120px** |

---

### F-ESP1-07 — Moderate · Generic benefit bullets — no SAPS/HTHS / Low-SAPS naming

| Evidence IDs | EVID-ESP1-09 |
| **Severity** | **Moderate** · **Medium** |

---

### F-ESP1-08 — Moderate · Parallel import · EN/TR/GR · no Cyrillic

| Evidence IDs | EVID-ESP1-12; ESP1-14 |
| **Severity** | **Moderate** · **High** |

---

### F-ESP1-09 — Moderate · Format-dependent back evidence vs 4L photo base

| Evidence IDs | EVID-ESP1-06; [40](40_ODSA_mobil_1_esp_5w_30_4L.md) F-ESP4-02 |
| **Interpretation** | **Not** proof that 4L SKU lacks specs — **photo lacuna** on 4L only. |
| **Severity** | **Moderate** · **High** |

---

### F-ESP1-10 — Moderate · ESP front vs C3 back — naming asymmetry

| Evidence IDs | EVID-ESP1-01; ESP1-06 |
| **Severity** | **Moderate** · **Medium** |

---

### F-ESP1-11 — Moderate · Footer heritage cluster — thumbnail fail

| Evidence IDs | EVID-ESP1-05; wiki/39 MOCC_ESPD_LAC01 |
| **Severity** | **Moderate** · **Medium** |

---

### F-ESP1-12 — Minor · Volume 1L vs 1Le notation

| Evidence IDs | EVID-ESP1-01; ESP1-10 |
| **Severity** | **Minor** · **High** |

---

### F-ESP1-13 — Minor · MB 229.52 on back — cross-ref LUKOIL 229.52 drift

| Evidence IDs | EVID-ESP1-07; [35](35_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_1L.md) |
| **Observation** | **229.52 listed** on Mobil back; LUKOIL GC 1L photo **229.52 not confirmed** — independent OEM rows, not conflict. |
| **Severity** | **Minor** · **Medium** |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-ESP1-01 | Front no API vs back API SP | **Open** — F-ESP1-01 |
| CR-ESP1-02 | Meets C3 vs QL exceeds C2 | **Closed** |
| CR-ESP1-03 | 1L back vs 4L back photo | **Open** — evidence asymmetry |
| CR-ESP1-04 | EN front vs TR/GR back langs | **Closed** — export wrap |

---

## POV-маркировка

**Information Integrity**
- *Lacunae:* API/ACEA front; Low SAPS explicit; Cyrillic; digital TDS.
- *Redundancy:* ESP + multi-fuel + synthetic + hybrid + F1 + 50Y.
- *Unlock:* back OEM/API grid — closes PGMM LAC02–04/LAC07 on 1L ([39](39_PGMM_mobil_1_esp_5w_30_1L_delta.md)).
- *Contamination:* F1 + emission framing (PGMM MSYS conflict).

**Logical Coherence**
- *Conflicts:* front/back deictic split — **Open**, industry pattern for import Mobil.
- *Contradictions:* none within back Meets/Approved block.

**System Dynamics**
- *Potential:* 1L top-up + readable back for informed buyer.
- *Limit:* shelf 2 m = front-only; thumbnail footer heritage fail.
- *Anomaly:* back spec delivery **↑** on 1L vs 4L **photo** base.

**Relational States**
- *Compromise:* DRY rescale vs premium whitespace ([39](39_PGMM_mobil_1_esp_5w_30_1L_delta.md)).
- *Parities:* OEM depth **≈** LUKOIL GC back; front spec **≪** GC/GPN.
- *Consensus:* canon **SP + C3** locked on artifact.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 1L · rev. 1 locked

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Emission-Network + Multi-Fuel Gateway + Motorsport Heritage (**константа**) | wiki/39; EVID-ESP1-13 | H |
| 2 | Carrier morphology (PGMM) | Narrow 1L bottle + grip-ridges + green cap (**≠** 4L jug) | wiki/39; ART-ESP1-001 | H |
| 3 | Класс продукта (синт / полусинт) | **Advanced full synthetic** · **API SP** | EVID-ESP1-01; ESP1-06 | H |
| 4 | SAE 5W-30 — legibility | **High** — rel. scale ↑ on narrow label | EVID-ESP1-01; ESP1-10 | H |
| 5 | API — видимость (front / back) | **— / SP** (SJ→SP Meets row) | EVID-ESP1-02; ESP1-06; F-ESP1-01 | H |
| 6 | ACEA — видимость (front / back) | **— / C3** (+ exceeds **C2** QL) | EVID-ESP1-02; ESP1-06; ESP1-08 | H |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-ESP1-02; F-ESP1-02 | H |
| 8 | OEM / допуски — back / site / overlay | MB 229.31/51/52 · VW 504/507 · BMW LL-04 · Porsche C30 · Opel OV · Fiat S3 | EVID-ESP1-07; ESP1-08 | H |
| 9 | Benefit-icons — доказуемость | **Low–Moderate** — 5 generic bullets back; **no** tribology icons | EVID-ESP1-09 | M |
| 10 | Cross-face consistency | **Partial @ shelf** · **Pass within back** | EVID-ESP1-02; ESP1-06–08; F-ESP1-01 | H |
| 11 | Digital / overlay vs pack gap | **н/д** — no site in wiki/04; RU overlay **н/д** | GAP-ESP1-01; GAP-ESP1-02 | L |
| 12 | Anti-fraud UX | QR «SCAN…» + barcode + batch stamp **2024** · no EAC | EVID-ESP1-10; ESP1-11 | M |
| 13 | RF supply & языковая модель | Parallel import · EN front · EN/TR/GR back · **no Cyrillic** | EVID-ESP1-12; ESP1-14 | H |
| 14 | Обязательная маркировка РФ | **н/д** — no EAC on photo; import proxy | EVID-ESP1-14 | L |
| 15 | Кириллица vs латиница | **EN dominant** front · TR/GR back legal | EVID-ESP1-01; ESP1-12 | H |
| 16 | Thumbnail robustness (~120 px) | **Medium** — «1» + ESP + 5W-30 ✅ · F1/50Y/1L **fail** · API front ✗ | wiki/39; EVID-ESP1-01 | M |
| 17 | Cognitive load / negative space | **Bimodal** — compressed front / dense spec back | wiki/39 | H |
| 18 | Legacy / rev. risk на полке | **Low** — batch **28.02.2024**; SP-class Meets row | EVID-ESP1-11; ESP1-06 | H |

---

## Импликации для СТМ

1. **Attack vector 5W-30 C3 1L:** **front-loaded** API SP + ACEA C3 + named Low-SAPS + **2 OEM icons @120px** — Mobil forces **flip-back** at doliv.
2. **Не копировать:** DRY vertical rescale without 1L-native whitespace; decorative F1/50Y footer on top-up SKU.
3. **Перенять (inverse):** readable back OEM grid depth — but **mirror top-3 on front**.
4. **Cross-peer:** front spec **слабее** [35](35_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_1L.md) / [37](37_ODSA_Gazpromneft_Premium_C3_5W-30_1L.md); back OEM **≈** GC.

---

## Issues for discussion

1. Считать ли Mobil ESP «spec-delivered» на 1L если canon **только на back**? **Rev.1:** Partial @ shelf · Pass for informed buyer.
2. **Line canon for 4L** — [40](40_ODSA_mobil_1_esp_5w_30_4L.md) inherits this back grid — acceptable? **Yes at lock** with rescan optional.
3. Point-ref matrix row — [`матрица_PGMM_ODSA_5W-30.md`](../../03_PGMM_ODSA_упаковка_конкуренты/матрица_PGMM_ODSA_5W-30.md).

**DoD:** ODSA Mobil 1 ESP 5W-30 **1L — complete** (rev. 1 locked · front+back photo).

---

*Ingest wiki/41 · 25.06.2026 · skill stm-odsa · фото 1L front+back*
