# ODSA — Mobil 1 ESP 5W-30 (4L): аудит claims на упаковке

**CASE_ID:** `ODSA_MOBIL_1_ESP_5W30_4L_2026`  
**Методология:** ODSA Audit Packet v1.6.7 · Depth: Compact  
**Связь PGMM:** [38_PGMM_mobil_1_esp_5w_30_4L.md](38_PGMM_mobil_1_esp_5w_30_4L.md) · delta 1L: [39_…](39_PGMM_mobil_1_esp_5w_30_1L_delta.md) · ODSA 1L: [41_…](41_ODSA_mobil_1_esp_5w_30_1L.md)  
**Дата:** 25.06.2026 · **Rev. 1:** locked (front photo + back photo **unreadable** + line canon inherit 1L)  
**Формат:** 4L · import-facing EU wrap · **parallel import proxy**  
**Canonical URL:** н/д · GAP-ESP4-02 digital triangulation open

**Supply channel:** Mobil **официально в РФ не поставляется** (EVID-ESP4-15); import EN-facing front; RU overlay **н/д** на фото.

---

## Executive summary (rev. 1 · locked)

**Канон SKU (line-level):** **Mobil 1 ESP 5W-30 4L** — advanced full synthetic · **API SP** · **ACEA C3** (exceeds C2) · German OEM stack — **inherited** from readable 1L back [41](41_ODSA_mobil_1_esp_5w_30_1L.md) (EVID-ESP1-06…10) per AGENTS canon rule; **не** извлечено с фото 4L back.

**Cross-face (4L photo artifact):** **Partial / н/д** — front без API/ACEA (EVID-ESP4-02); back dense label **нечитаем** (EVID-ESP4-08). **Не Blocker** — format-dependent photo quality, не зафиксированный split-grade на SKU.

**Cross-face (line canon):** **Pass @ canon** — front «Advanced Synthetic» + back grid 1L (API SP + ACEA C3 + OEM) — **assumed same wrap**; confidence **Medium** до rescan 4L back.

**Ключевые gaps vs LUKOIL GC / GPN C3:** (1) **API/ACEA off front** (F-ESP4-01); (2) **4L back evidence lacuna** (F-ESP4-02); (3) **no Cyrillic / no official RF** (F-ESP4-03); (4) **ESP acronym vs C3 norm** on face (F-ESP4-04).

| Severity rollup | Count |
|-----------------|-------|
| Blocker | 0 |
| Major | 2 |
| Moderate | 4 |
| Minor | 2 |
| Positive | 3 |

---

## Artifact Registry

| ART | Type | Source | Description |
|-----|------|--------|-------------|
| ART-ESP4-001 | Artifact (photo) | Оператор 25.06.2026 | Фронт 4L — ESP band, multi-fuel, 5W-30, 4L, F1, hybrid |
| ART-ESP4-002 | Artifact (photo) | Оператор 25.06.2026 | Оборот 4L — dense legal; **spec block нечитаем** |
| ART-ESP4-003 | Document | wiki/38 | PGMM _full 4L (context) |
| ART-ESP4-004 | Document | wiki/39 | PGMM delta 1L — back unlock ref |
| ART-ESP4-005 | Document | [41](41_ODSA_mobil_1_esp_5w_30_1L.md) | ODSA 1L — line canon source |

---

## Evidence Ledger (EOM)

| EVID | Source class | Source | Excerpt / observation | Reliability | Status |
|------|--------------|--------|----------------------|-------------|--------|
| EVID-ESP4-01 | Artifact | ART-ESP4-001 | Mobil **1**; **ESP EMISSION SYSTEM PROTECTION**; **ADVANCED SYNTHETIC TECHNOLOGY ENGINE OIL**; **5W-30**; **4L** | A | Active |
| EVID-ESP4-02 | Artifact | ART-ESP4-001 | **API / ACEA / ILSAC не на фронте** | A | Active |
| EVID-ESP4-03 | Artifact | ART-ESP4-001 | **FOR GASOLINE, DIESEL & HYBRID ENGINES** | A | Active |
| EVID-ESP4-04 | Artifact | ART-ESP4-001 | **Mobil 1 50 YEARS** anniversary badge | A | Active |
| EVID-ESP4-05 | Artifact | ART-ESP4-001 | **Oracle Red Bull Racing** + Mobil 1 co-brand | A | Active |
| EVID-ESP4-06 | Artifact | ART-ESP4-001 | Hybrid icon **«FOR HYBRIDS»** footer | A | Active |
| EVID-ESP4-07 | Artifact | ART-ESP4-001 | QR / datamatrix footer-left | A | Active |
| EVID-ESP4-08 | Artifact | ART-ESP4-002 | Back: Mobil logo + green bands + barcode zone; **API/OEM text нечитаемо** | A | Active · **lacuna** |
| EVID-ESP4-09 | Context | ART-ESP4-003 | PGMM: back unreadable; API/ACEA lacuna front | B | Context |
| EVID-ESP4-10 | Context | ART-ESP4-004 | Delta: 1L back unlock SP/C3/OEM; 4L photo asymmetry | B | Active |
| EVID-ESP4-11 | Cross-format | ART-ESP4-005 | Line canon: API **SP**; ACEA **C3**; MB 229.31/51/52; VW 504/507; BMW LL-04; Porsche C30; Opel OV…; Fiat S3; exceeds **C2** | B | **Canonical line** |
| EVID-ESP4-12 | Context | wiki/21 | Mobil 1 0W-20 ODSA — parallel import + overlay pattern | B | Context |
| EVID-ESP4-13 | Context | [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) | Peer: front API+ACEA on LUKOIL GC | B | Context |
| EVID-ESP4-14 | Context | [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) | Peer: front SP+C2/C3 on GPN C3 | B | Context |
| EVID-ESP4-15 | Context | Оператор 25.06.2026 | Not official RF supply; import channel | B | Active |

### Conflict notes

| Conflict | Evidence | Resolution |
|----------|----------|------------|
| Front no API vs line canon SP | ESP4-02 vs ESP4-11 | **Open (CR-ESP4-01)** — deictic front/back split |
| 4L back unreadable vs 1L back full grid | ESP4-08 vs ESP4-11 | **Open (CR-ESP4-02)** — photo artifact; **not** inter-SKU grade split |
| Emission ESP vs F1 badge | ESP4-01 vs ESP4-05 | **Open (CR-ESP4-03)** — positioning tension (PGMM MSYS_ESP_01↔03) |
| «ESP» vs ACEA C3 canon | ESP4-01 vs ESP4-11 | **Open (CR-ESP4-04)** — line acronym vs normative class on back |

### Data gaps

| Gap | Статус |
|-----|--------|
| GAP-ESP4-01 Rescan 4L back @ readable resolution | **Open** — symmetric ODSA optional |
| GAP-ESP4-02 Digital triangulation (mobil1.com / TDS) | **Open** — URL not in wiki/04 |
| GAP-ESP4-03 RU overlay / importer sticker | **Open** — н/д on photo (cf. Mobil 0W-20 [21](21_ODSA_mobil_1_0w_20_5L.md)) |
| GAP-ESP4-04 Retail shelf @1.2 m | Open — н/д |
| GAP-ESP4-05 Production stamp 4L batch | Open — back unreadable |

---

## Findings Catalogue

### F-ESP4-01 — Major · API / ACEA absent from front (4L)

| Поле | Значение |
|------|----------|
| **Observation** | Front (EVID-ESP4-02): **нет** API, ACEA, ILSAC. Line canon (EVID-ESP4-11): **API SP + ACEA C3** on back (1L artifact). |
| **Evidence IDs** | EVID-ESP4-02; ESP4-11; ESP4-13; ESP4-14 |
| **Interpretation** | **Back-loaded spec strategy** — слабее LUKOIL GC и GPN C3 с front lockup. Shelf @2 m = **ESP + 5W-30 heuristic only**. |
| **Severity & Confidence** | **Major** · **High** |
| **Recommendations** | structural: СТМ C3 — **API SP + ACEA C3 on front** |

---

### F-ESP4-02 — Major · 4L back spec block unreadable on photo

| Поле | Значение |
|------|----------|
| **Observation** | ART-ESP4-002: legal wall + green footer visible; **Meets/Approved rows не декодируются**. |
| **Evidence IDs** | EVID-ESP4-08; ESP4-10 |
| **Interpretation** | **Evidence lacuna** на формате 4L; line canon **borrowed** from 1L back — governance risk if facings differ. |
| **Severity & Confidence** | **Major** (evidence) · **Closed at line canon** · **Medium** |
| **Recommendations** | governance: rescan 4L back; structural: fair spec **all faces** |

---

### F-ESP4-03 — Moderate · Parallel import — EN front, no Cyrillic, no official RF

| Evidence IDs | EVID-ESP4-01; ESP4-15; ESP4-12 |
| **Observation** | EN-facing front; **кириллица н/д**; channel = import proxy (pattern Mobil Super 3000 / Mobil 1 0W-20). |
| **Severity** | **Moderate** · **High** |

---

### F-ESP4-04 — Moderate · «ESP» line code vs C3/Low-SAPS norm on RU shelf

| Evidence IDs | EVID-ESP4-01; ESP4-11; ESP4-13 |
| **Observation** | Front sovereignty = **ESP acronym** + emission framing; **нет** «C3» / «Low SAPS» on face; canon C3 **back-only** (1L). |
| **Severity** | **Moderate** · **Medium** |

---

### F-ESP4-05 — Moderate · Multi-fuel + hybrid front — segment-aligned, chemistry unstated

| Evidence IDs | EVID-ESP4-03; ESP4-06 |
| **Observation** | Gasoline + **diesel** + hybrid explicit; **без** SAPS/HTHS / DPF metrics on front. |
| **Severity** | **Moderate** · **Medium** |

---

### F-ESP4-06 — Moderate · Red Bull + 50 YEARS vs emission framing

| Evidence IDs | EVID-ESP4-04; ESP4-05; wiki/38 MSYS_ESP_03 |
| **Severity** | **Moderate** · **Medium** · PGMM conflict carry-over |

---

### F-ESP4-07 — Minor · No effective OEM on front

| Evidence IDs | EVID-ESP4-02; ESP4-11 |
| **Observation** | Full OEM grid **line canon back-only**; front = brand + ESP + multi-fuel only. |
| **Severity** | **Minor** · **High** |

---

### F-ESP4-08 — Minor · Digital triangulation waived

| Evidence IDs | GAP-ESP4-02 |
| **Severity** | **Minor** · **Medium** |

---

### F-ESP4-09 — Positive · Core identity coherent on front (syn · 5W-30 · 4L · ESP line)

| Evidence IDs | EVID-ESP4-01 |
| **Severity** | **Positive** · **High** |

---

### F-ESP4-10 — Positive · QR + batch infrastructure partial (anti-fraud)

| Evidence IDs | EVID-ESP4-07 |
| **Observation** | QR present; landing content **н/д**; weaker than GPN 3662 / LUKOIL QR depth. |
| **Severity** | **Positive** · **Medium** |

---

### F-ESP4-11 — Positive · Line canon OEM depth (inherited 1L) — on par with GC back

| Evidence IDs | EVID-ESP4-11; ESP4-13 |
| **Observation** | MB 229.31/51/52 · VW 504/507 · BMW LL-04 · Porsche C30 — **comparable** to [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) back grid. |
| **Severity** | **Positive** · **Medium** (inheritance caveat) |

---

## Contradiction Register

| CR-ID | Conflict | Status |
|-------|----------|--------|
| CR-ESP4-01 | Front no API vs line canon SP | **Open** — F-ESP4-01 |
| CR-ESP4-02 | 4L back unreadable vs 1L back grid | **Open** — F-ESP4-02; photo artifact |
| CR-ESP4-03 | Emission ESP vs F1 heritage | **Open** — PGMM; not claims split |
| CR-ESP4-04 | ESP acronym vs C3 canon | **Open** — naming vs chemistry class |

---

## POV-маркировка

**Information Integrity**
- *Lacunae:* 4L back specs; digital TDS; RU overlay; Low SAPS explicit; OEM front.
- *Redundancy:* ESP + multi-fuel + synthetic + hybrid + F1 + 50Y — high decorative stack.
- *Contamination:* Network lattice + F1 borrow eco-emission frame (PGMM).
- *Collonisation:* Mobil 1 monolith «1» + green ESP band — category Mobil 1 family code.

**Logical Coherence**
- *Conflicts:* 4L photo cross-face **н/д** — not graded as API contradiction.
- *Contradictions:* CR-ESP4-03 positioning only.

**System Dynamics**
- *Anomaly:* 4L back unreadable vs 1L back readable — **photo artifact**, flagged in [39](39_PGMM_mobil_1_esp_5w_30_1L_delta.md).
- *Potential:* Multi-fuel + diesel explicit — fleet/DPF anxiety segment.
- *Limits:* Import channel; no site triangulation.

**Relational States**
- *Compromise:* Premium whitespace + dense footer heritage cluster.
- *Parities:* With Mobil 1 0W-20 — API off front; **weaker** than dexos1 front on 0W-20.
- *Consensus:* Line canon SP/C3 via 1L back — **Medium** until 4L rescan.

---

## Унифицированная таблица ODSA×PGMM (canonical · 18 строк)

> Схема: [`ODSA_matrix_row_шаблон.md`](../../03_PGMM_ODSA_упаковка_конкуренты/ODSA_matrix_row_шаблон.md) · 4L · rev. 1 locked

| # | Параметр | Значение | Evidence | Confidence |
|---|----------|----------|----------|------------|
| 1 | M_SYSTEM (PGMM) | Emission-Network Hyper-Protection + Multi-Fuel Gateway + Motorsport Heritage | wiki/38; EVID-ESP4-09 | H |
| 2 | Carrier morphology (PGMM) | 4L silver HDPE jug + integrated handle + green cap | wiki/38; ART-ESP4-001 | H |
| 3 | Класс продукта (синт / полусинт) | **Advanced full synthetic** · canon **API SP** (line inherit) | EVID-ESP4-01; ESP4-11 | H / M |
| 4 | SAE 5W-30 — legibility | **High** — oversized white on green network panel | EVID-ESP4-01 | H |
| 5 | API — видимость (front / back) | **— / н/д photo** · **Canon: — / SP** | EVID-ESP4-02; ESP4-08; ESP4-11; F-ESP4-01 | H / M |
| 6 | ACEA — видимость (front / back) | **— / н/д photo** · **Canon: — / C3** (+ exceeds C2) | EVID-ESP4-02; ESP4-08; ESP4-11 | H / M |
| 7 | OEM / допуски — front (effective) | **Нет** | EVID-ESP4-02; F-ESP4-07 | H |
| 8 | OEM / допуски — back / site / overlay | Photo **н/д** · **Line canon (1L):** MB 229.31/51/52 · VW 504/507 · BMW LL-04 · Porsche C30 · Opel OV · Fiat S3 | EVID-ESP4-08; ESP4-11 | M |
| 9 | Benefit-icons — доказуемость | **Low** — generic performance implied; **no** pack bullets on 4L photo | EVID-ESP4-03; ESP4-06; wiki/38 | M |
| 10 | Cross-face consistency | Photo 4L: **Partial / н/д** · **Line canon: Pass** | EVID-ESP4-02; ESP4-08; ESP4-11; F-ESP4-02 | M |
| 11 | Digital / overlay vs pack gap | **н/д** — no verified URL; RU overlay **н/д** | GAP-ESP4-02; GAP-ESP4-03 | L |
| 12 | Anti-fraud UX | QR present · landing **н/д** · no EAC · batch stamp **н/д** on 4L back photo | EVID-ESP4-07; ESP4-08 | M |
| 13 | RF supply & языковая модель | Parallel import · **EN front** · Cyrillic **н/д** | EVID-ESP4-01; ESP4-15 | H |
| 14 | Обязательная маркировка РФ | **н/д** on photo — no EAC visible; import proxy | EVID-ESP4-08; ESP4-15 | L |
| 15 | Кириллица vs латиница | **EN dominant** front; back langs **нечитаемы** | EVID-ESP4-01; ESP4-08 | M |
| 16 | Thumbnail robustness (~120 px) | **Med-high** — «1» + green ESP + 5W-30 ✅ · F1/50Y 🟡 · API ✗ | wiki/38; EVID-ESP4-01 | M |
| 17 | Cognitive load / negative space | **Medium** front · **very high** back legal wall (content н/д) | wiki/38 | H |
| 18 | Legacy / rev. risk на полке | **Low–Moderate** — 1L batch **2024** (line); 4L stamp **н/д**; wrap stability **verify** | ESP4-11; GAP-ESP4-05 | M |

---

## Импликации для СТМ

1. **Не копировать:** back-loaded API/OEM without front mirror; ESP acronym-only without C3/Low-SAPS proof.
2. **Перенять (inverse):** premium whitespace discipline on 4L jug — но **добавить** front spec row как GPN/LUKOIL.
3. **White space:** front **API SP + ACEA C3 + 2–3 OEM icons**; drop F1/50Y decorative noise on C3 SKU.
4. **Governance:** rescan 4L back before citing pack-level OEM in диплом — сейчас **line inherit** only.

---

## Issues for discussion

1. **Rescan 4L back** — закрыть GAP-ESP4-01 или принять line inherit at lock? **Принято at rev.1** with Medium confidence.
2. **Point-ref 5W-30 matrix** — включить Mobil ESP 4L+1L в [`матрица_PGMM_ODSA_5W-30.md`](../../03_PGMM_ODSA_упаковка_конкуренты/матрица_PGMM_ODSA_5W-30.md).
3. Cross-ref peers: [34](34_ODSA_LUKOIL_GENESIS_Armortech_GC_5W-30_4L.md) · [36](36_ODSA_Gazpromneft_Premium_C3_5W-30_4L.md) · [21](21_ODSA_mobil_1_0w_20_5L.md).

**DoD:** ODSA Mobil 1 ESP 5W-30 **4L — complete** (rev. 1 locked · back photo lacuna documented).

---

*Ingest wiki/40 · 25.06.2026 · skill stm-odsa · фото 4L front+back*
