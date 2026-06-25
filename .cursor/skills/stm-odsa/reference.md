# ODSA reference — Evidence, Findings, Matrix row

Источник: ODSA Audit Packet v1.6.7 · эталоны wiki/16–18.

---

## Evidence Ledger (EOM)

| Колонка | Содержание |
|---------|------------|
| EVID | `EVID-G01`, `EVID-L10` |
| Source class | Artifact / Context / Operator |
| Source | ART-001, photo, URL ID |
| Excerpt | Дословно или наблюдение |
| Reliability | A / B / C |
| Status | Active / Deprecated / Stale / Context |

**Source classes:** Artifact (фото этикетки), Context (PGMM wiki, operator text), Operator attestation.

---

## Findings (F-*)

| Поле | Обязательно |
|------|-------------|
| Observation | Что видно / не видно |
| Evidence IDs | EVID-* |
| Severity & Confidence | Blocker/Major/Moderate/Minor/Positive · H/M/L |
| Interpretation | Split-face vs channel gap vs notation |
| Recommendations | quick / structural / governance |
| Falsification | Что опровергнет finding |

---

## Contradiction Register (CR-*)

| Status | Значение |
|--------|----------|
| Open | Требует triangulation |
| Closed | Разрешено (notation, evolution, operator) |

---

## Canonical matrix row (18 строк)

Из `ODSA_matrix_row_шаблон.md`:

| # | Параметр | Слой |
|---|----------|------|
| 1 | M_SYSTEM (PGMM) | PGMM |
| 2 | Carrier morphology | PGMM |
| 3 | Класс продукта (syn/semi) | ODSA |
| 4 | SAE — legibility | ODSA+PGMM |
| 5 | API front/back | ODSA |
| 6 | ACEA front/back | ODSA |
| 7 | OEM front (effective) | ODSA |
| 8 | OEM back/site/overlay | ODSA |
| 9 | Benefit-icons доказуемость | ODSA+PGMM |
| 10 | Cross-face consistency | ODSA |
| 11 | Digital vs pack gap | ODSA |
| 12 | Anti-fraud UX | ODSA |
| 13 | RF supply & язык | ODSA |
| 14 | Обязательная маркировка РФ | ODSA |
| 15 | Кириллица vs латиница | ODSA |
| 16 | Thumbnail robustness (~120px) | PGMM delta |
| 17 | Cognitive load / negative space | PGMM |
| 18 | Legacy / rev. risk на полке | ODSA |

Confidence: H / M / L · Evidence: EVID-* / PGMM wiki / «на фото» / «н/д».

---

## POV-маркировка (обязательно)

**Information Integrity:** Lacunae, Redundancy, Contamination, Collonisation

**Logical Coherence:** Conflicts, Contradictions

**System Dynamics:** Anomalies, Potentials, Limits

**Relational States:** Compromises, Parities, Consensuses

---

## Пример CASE_ID

```
ODSA_LUKOIL_LUXE_5W40_4L_2026
ODSA_GPN_PREMIUM_N_5W40_4L_2026
```

---

## Triangulation checklist

- [ ] Front API/base oil claim
- [ ] Back full spec block
- [ ] Site product card (URL in wiki/04)
- [ ] Operator: wrap unchanged?
- [ ] PGMM link (optional context EVID)
- [ ] Delta format — separate ODSA run if needed
