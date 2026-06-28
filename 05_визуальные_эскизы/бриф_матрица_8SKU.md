# Бриф эскизов — матрица 8 front (4 SKU × format)

**Этап:** 6 · **Бренд:** Eliten · **Обновлено:** 26.06.2026 (audit rev.)

---

## Scope

| # | SKU | Sub-line | Format | PGMM matrix | ODSA proof |
|---|-----|----------|--------|-------------|------------|
| 1 | **5W-40** syn | Classic Protect | **4L** | `матрица_5W-40` §6 | API SN/CF + OEM front |
| 2 | **5W-40** syn | Classic Protect | **1L** | §6C format fairness | doliv · spec as 4L |
| 3 | **5W-30** syn | Modern Tech | **4L** | `матрица_5W-30` §4 | API SP · ACEA C3 · OEM |
| 4 | **5W-30** syn | Modern Tech | **1L** | delta 1L | C3 / SP front |
| 5 | **10W-40** semi | Classic Protect | **4L** | `матрица_10W-40` §6 | API front · domestic OEM |
| 6 | **10W-40** semi | Classic Protect | **1L** | delta 1L | semi lexicon · doliv |
| 7 | **0W-20** FS | Modern Tech | **5L** | `матрица_0W-20` §4 | API SP · ACEA C5 · multi-OEM |
| 8 | **0W-20** FS | Modern Tech | **1L** | §4C · RBS 5,6 L fill | hero SAE + OEM @120px |

**Не в scope этапа 6:** back label · TDS layout · shelf render @1.2 m (LAC-04).

---

## Общие требования (все 8)

| ID | Требование | Источник |
|----|------------|----------|
| G-01 | Master **Eliten** + sub-line + hero **SAE** | ODSA arch |
| G-02 | **Readable proof band** на фронте | PGMM A · ODSA blocker |
| G-03 | **International front only** — no RF/EAC/origin/legal on front | Eliten_DESIGN §3 · N-17…N-22 |
| G-04 | Trust layer (batch/QR optional, not 3662/EAC clone) | PGMM E · back for regulatory |
| G-05 | Whitespace / fluid — **not** armor | PGMM D |
| G-06 | 1L = отдельный brief, не уменьшенный 4L | PGMM C |
| G-07 | **NEG checklist** N-01…N-24 · AI negative prompt | [`Eliten_DESIGN.md`](Eliten_DESIGN.md) §6 |
| G-08 | **Motor-oil fluid only** — amber/honey-gold · controlled ribbon · no coolant (CAT-01) | Eliten_DESIGN §6.4.1 · N-23/N-24 |
| G-09 | **OEM matrix** per SKU · TDS-pending · no MB 229.5 on 5W-40 | Eliten_DESIGN §5.1 |

---

## Per-SKU notes

### Classic Protect · 5W-40 (✅ APPROVED etalon)

- **Approved:** [`ELITEN_Classic_Protect_5W40_4L_dual_handle_packaging_concept.png`](финал/ELITEN_Classic_Protect_5W40_4L_dual_handle_packaging_concept.png)
- Note: [`ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md`](ELITEN_Classic_Protect_5W40_dual_handle_packaging_note.md)
- Carrier: **dual-handle** graphite · cap top-left · emboss ELITEN
- Label: dark navy · silver ELITEN · gold CLASSIC PROTECT · amber oil bottom
- Front OEM: MB 229.3 · VW · RN · Porsche A40 · ACEA A3/B4

### Classic Protect · 10W-40

- Semi-synthetic — **не** syn gold cues
- Proof: **Semi-Synthetic** · **API SN/CF** · OEM front (**≠ 5W-40 tier**)
- OEM front: **ACEA A3/B3** · **MB 229.1** · **VW 501 01/505 00** · **AVTOVAZ · UMZ · ZMZ**
- **Ban:** MB 229.3 · VW 502 00 · RN · Porsche · ACEA A3/B4 (5W-40 only)
- Peer: wiki/52 Mobil Super 2000 back · [`Eliten_DESIGN.md`](Eliten_DESIGN.md) §5.2
- Same Classic color tokens as 5W-40

### Modern Tech · 5W-30

- **Carrier:** same dual-handle 4L / 1L mold · jug **cool slate `#3A4556`** (≠ Classic graphite)
- **Label shell:** navy + **tech blue `#3B82F6`** · **grid motif** · **no amber ribbon**
- Sub-line: **MODERN TECH** · no «German Cars» / Hyper-Armor
- Front: **API SP · ACEA C3 together** + OEM readable
- OEM: **MB 229.51 · VW 504/507 · BMW LL-04 · Porsche C30** front · **dexos2 back**
- Prompt: [`prompt_ModernTech_5W-30.md`](prompt_ModernTech_5W-30.md)

### Modern Tech · 0W-20 · 5L + 1L

- **5L:** dual-handle + **5L badge** (same mold as 4L · operator A) · **1L** narrow bottle
- **Label shell:** same as accepted Modern Tech 5W-30 (tech blue · grid)
- Front: **API SP · ACEA C5** · multi-OEM row · §5.4
- OEM front: **RBS0-2AE · Toyota · Honda · Hyundai · Kia · Nissan** · **GF-6A · dexos1 → back**
- Antidote: no Mobil lattice · no Castrol HYSPEC/gold
- Prompt: [`prompt_ModernTech_0W-20.md`](prompt_ModernTech_0W-20.md)

---

## Концепт → финал

| Этап | Арtefact | Count |
|------|----------|-------|
| A | `концепт/эскиз_01…03.png` | 3 · **5W-40 4L only** |
| B | Выбор **эскиз_02** (рекомендация) | 1 |
| C | `финал/*.png` | 8 · scale design system |

См. [`Eliten_DESIGN.md`](Eliten_DESIGN.md)
