# PGMM reference — поля и чеклисты (этап 4)

Источник: `03_PGMM_ODSA_упаковка_конкуренты/PGMM.md` (Klepikov 2025).

---

## M_OCCURRENCE (_full)

| Поле | Содержание |
|------|------------|
| `MOCC_ID` | Уникальный ID (`MOCC_GPN_01`) |
| `MATERIAL_ID` | Текст / графика / цвет / форма / negative space |
| `SEGMENT_ID` | Зона макета (header, core, footer, cap) |
| `MODALITY_CLASS` | visual / textual / multimodal |
| `REP_LEVEL` | literal / schematic / abstract |
| `SPAN` | Координаты или описание области |
| `SURFACE_FORM` | Слово, знак, паттерн, градиент |
| `DOMAIN_A_HINT` | Source-domain |
| `DOMAIN_B_HINT` | Target-domain |
| `MAP_OP_HINT` | projection / suppression / hyperbole / substitution |
| `STATUS_CLASS` | MANIFEST / LATENT / LACUNA / NEGATIVE_SPACE |
| `CONFIDENCE_LEVEL` | high / medium / low |
| `LINK_MCON` | Связь с M_CONSTRUCTION |

---

## M_CONSTRUCTION

| Поле | Содержание |
|------|------------|
| `MCON_ID` | `MCON_01` … |
| `PATTERN_LABEL` | Краткое имя |
| `MOCC_SET` | Список MOCC_ID |
| `FUNCTION` | heuristic / trust / obscuration / status / spec |
| `STATUS_CLASS` | MANIFEST / LATENT / LACUNA / NEGATIVE_SPACE |
| `SYSTEM_LINK` | M_SYSTEM_ID |

---

## M_SYSTEM

| Поле | Содержание |
|------|------------|
| `MSYS_ID` | `MSYS_BRAND_01` |
| `LABEL` | Имя системы |
| `MCON_SET` | Входящие конструкции |
| `GOAL` | Транзакция / доверие / статус / сокрытие |
| `CONFLICT_WITH` | Другая MSYS или DOMAIN_B |
| `STATUS_CLASS` | MANIFEST / LATENT / LACUNA |

---

## Блоки DOMAIN → K (_full)

**DOMAIN:** A (source) vs B (target); конфликт, колонизация.

**MAP:** MAP1–MAP10; fidelity, rhetoric, cognitive load.

**S:** S1–S11; signal/noise, subchannels.

**C:** C1–C9; HDPE, geometry, affordances.

**M:** M1–M11; shelf noise, e-com thumb, social context.

**K:** K1–K10; layout, color, density, scan path.

**EVAL:** 6 векторов + EVAL_AGG + таблица «конкурент → СТМ antidote».

---

## System States (обязательно)

1. **Information Integrity:** Lacunae, Redundancy, Contamination, Collonisation
2. **Logical Coherence:** Conflicts, Contradictions
3. **System Dynamics:** Anomalies, Potentials, Limits
4. **Relational States:** Compromises, Parities, Consensuses

---

## Пример CASE_min

```yaml
CASE_ID: COMP_GPN_PREMIUM_N_5W40_4L
CASE_TYPE: packaging_visual_metaphor
BRAND: Gazpromneft
LINE: Premium N
SAE: 5W-40
FORMAT: 4L
VIEW: front label
SEGMENT: mass-mid synthetic
REGION: european RU proxy
```
