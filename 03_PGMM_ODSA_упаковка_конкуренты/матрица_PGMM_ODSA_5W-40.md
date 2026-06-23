# Сравнительная матрица PGMM + ODSA — 5W-40 (mass-mid synthetic)

**Этап:** 4 · **Регион:** европейская часть РФ (витрина retail)  
**Дата сборки:** 23.06.2026  
**Правило строк:** **1 format = 1 row** · 6 строк = 3 бренда × (4L + 1L)  
**Источники:** wiki PGMM [10–15](../Cursor/wiki/) · ODSA [16–18](../Cursor/wiki/) · canonical schema [`ODSA_matrix_row_шаблон.md`](ODSA_matrix_row_шаблон.md)

---

## 0. Scope и ограничения

| Поле | Значение |
|------|----------|
| SAE | **5W-40** only |
| Сегмент | Mass-mid synthetic (не 0W-20 premium) |
| ODSA 4L | Full audit · wiki/16–18 · locked |
| ODSA 1L | **Не прогонялся отдельно** — строки 1L построены из PGMM delta (13–15) + экстраполяция 4L ODSA · Confidence **M/L** где нет фото-claims |
| PGMM wiki/10 | **Stale** (legacy SL/semi) — в матрице для LUKOIL 4L указан канон ODSA (LUXE SYNTHETIC SN/CF) |

---

## 1. Индекс строк (6 SKU)

| Row | Бренд | Формат | PGMM | ODSA 4L/1L | Ключевой риск |
|-----|-------|--------|------|------------|---------------|
| R1 | LUKOIL LUXE | **4L** | [10](../Cursor/wiki/10_PGMM_LUKOIL_LUXE_5W-40.md) | [16](../Cursor/wiki/16_ODSA_LUKOIL_LUXE_5W-40_4L.md) | Legacy SL facings · OEM back-only |
| R2 | LUKOIL LUXE | **1L** | [14](../Cursor/wiki/14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md) | delta + R1 | ActiPure ↓ · API/1L thumbnail fail |
| R3 | Gazpromneft Premium N | **4L** | [11](../Cursor/wiki/11_PGMM_Gazpromneft_Premium_N_5W-40.md) | [17](../Cursor/wiki/17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) | OEM microtype · site superset |
| R4 | Gazpromneft Premium N | **1L** | [15](../Cursor/wiki/15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md) | delta + R3 | OEM layer **functionally dead** |
| R5 | Mobil Super 3000 x1 | **4L** | [12](../Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md) | [18](../Cursor/wiki/18_ODSA_mobil_super_3000_x1_5w_40_4L.md) | API off front · parallel import |
| R6 | Mobil Super 3000 x1 | **1L** | [13](../Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md) | delta + R5 | Benefit-icons **absent** · QR lacuna |

---

## 2. Блок PGMM (6 строк)

| Row | M_SYSTEM | DOMAIN Source → Target | Ключевая метафора | Лакуны (LACUNA) | EVAL (1 строка) | Импликация для СТМ |
|-----|----------|------------------------|-------------------|-----------------|-----------------|---------------------|
| **R1** LUXE 4L | industrial_hyper_armor + epistemic_void | A: броня/карбон/золото/телеметрия → B: трибология (вытеснена) | Жидкость = металл; щит + золото | Эко/жидкость; ActiPure void; OEM на фасаде | Fidelity **2/10** · риторика **9/10** · юзабилити **8/10** (wiki/10; ODSA refresh L10) | Open engineering + OEM band на фронт; version bump при reformulation |
| **R2** LUXE 1L | **= R1** (константа) | = R1 | Щит **↑%** площади; карбон→соты | ActiPure MAP **оборван**; grip MAP latent | Primary VP сохранён; secondary layer ↓; thumbnail API/1L **fail** (delta/14) | Top-up SKU: явный API + 1L + один tech-proof; не DRY без rescale |
| **R3** GPN 4L | cognitive_amortization + institutional_anxiety | A: термокинетика + гегемония → B: HC-synth (скрыт) | 5W-40 heuristic + 3D-swirl; «чёрный ящик» | Инженерия в подвале; Noack/TBN; fluid | Транзакционно **высоко** · инженерная прозрачность **~0** (wiki/11) | Whitespace + manifest OEM; не копировать «пустоту» без веса Газпрома |
| **R4** GPN 1L | **= R3** | = R3 | Claustrophobic **↑**; near-zero air | OEM/API footer **functionally dead** (delta/15) | 8/10 top-up · 6/10 overall; uniform density ↑ | 1L: крупный 1L + center OEM + breathing zone |
| **R5** Mobil 4L | techno_vital_armor | A: плазменная броня → B: трибология (невидима) | Плазма в кольце-экзоскелете | Эко; гидродинамика; цифра; минимализм (wiki/12) | Shannon **оптимально** · fidelity **низкая** · anxiety relief **высокий** | Single-layer native RU + front API/OEM + official supply |
| **R6** Mobil 1L | **= R5** | = R5 | Кольцо cropped; QR без CTA MAP | Benefit-icons **absent** (mocc_028); bimodal density (delta/13) | 7/10 overall · 9/10 top-up; robustness **medium** | Clean top-up layout + explicit digital MAP + icons retained |

---

## 3. Блок ODSA — canonical 18 параметров (transpose)

**Легенда Confidence:** H / M / L · **1L:** источник «delta/13–15 + R*» если нет отдельного ODSA

| # | Параметр | R1 LUXE 4L | R2 LUXE 1L | R3 GPN 4L | R4 GPN 1L | R5 Mobil 4L | R6 Mobil 1L |
|---|----------|------------|------------|-----------|-----------|-------------|-------------|
| 1 | M_SYSTEM | industrial_hyper_armor + epistemic_void · **H** · wiki/10;16 | = R1 · **H** · delta/14 | cognitive_amortization + institutional_anxiety · **H** · 11;17 | = R3 · **H** · delta/15 | techno_vital_armor · **H** · 12;18 | = R5 · **H** · delta/13 |
| 2 | Carrier morphology | Асимметричная + ручка · **H** | Узкая бутылка + shoulder grip · **H** · δ14 | Широкая + ручка · **H** | Узкая + diagonal grip · **H** · δ15 | «Торс» + рёбра · **H** | Узкая + grip-ridges · **H** · δ13 |
| 3 | Класс (синт/полусинт) | **Syn SN/CF** · **H** · L10 | **Syn SN/CF** (assumed) · **M** · verify δ14 | **Syn SN/CF** · **H** · G01 | **Syn SN/CF** (assumed) · **M** · δ15 | **Syn** EN + RU overlay · **H/M** · M01 | **Syn** (assumed) · **M** · δ13 |
| 4 | SAE 5W-40 legibility | **High** · **H** | **High** (rel.↑) · **H** · δ14 | **High** hyperbolized · **H** | **High** · **H** · δ15 | **High** gold badge · **H** | **High** · **H** · δ13 |
| 5 | API (front / back) | **SN/CF · SN/CF** · **H** | Front **verify** · back SN/CF · **M** · δ14 | **SN/CF · SN/CF** · **H** | Footer **dead** · **L** · δ15 | **— / SJ–SN+CF** (+overlay CF–SP) · **H** | Front **—** · **M** · δ13 |
| 6 | ACEA (front / back) | Front **—** · back A3/B4,B3 · **H** | Back only assumed · thumb **fail** · **M** | **A3/B4 · A3/B4** (+B3 site) · **H** | A3/B4 assumed · OEM dead · **M** | **A3/B4 · +A3/B3** · **H** | Front A3/B4 · icons ↓ · **M** · δ13 |
| 7 | OEM front (effective) | **Нет** · **H** · F-L03 | **Нет** · **H** | **Microtype** (нечитаемо) · **H** · F-G03 | **Dead** · **L** · δ15 | **Нет** base · **H** | **Нет** · **H** |
| 8 | OEM back / site / overlay | Full stack back+site · **H** · L04 | Degraded read · **M** · δ14 | Back + **site superset** · **H/M** · F-G04 | **Functionally dead** · **L** | Base back + overlay superset · **M** · F-M13 | Back degraded · **M** · δ13 |
| 9 | Benefit-icons | Min (current); ActiPure legacy · **M** | ActiPure **absent** · **H** · δ14 | Low (swirls) · **M** | Low + car pictogram · **M** · δ15 | Moderate 4L · **M** | **Absent** · **H** · mocc_028 |
| 10 | Cross-face consistency | **Pass** current · **H** | **Verify** API · **M** | **Pass** · **H** | Pass assumed · **M** | **Partial** + overlay · **H** | Partial · **M** |
| 11 | Digital / overlay gap | Site ≈ pack · **H** | = R1 · **H** | **Site superset** · **M** · F-G04 | = R3 · **M** | **Overlay superset** · **M** · F-M13 | = R5 · **M** |
| 12 | Anti-fraud UX | **—** · **H** | **—** · **M** | **3662.ru** + site · **H** | 3662 **verify** 1L · **M** | **None** · **H** | None · **H** |
| 13 | RF supply & язык | Official integrated RU · **H** | Official · **H** | Official integrated · **H** | Official · **H** | Parallel import EN+TR+RU sticker · **H** | Parallel + overlay · **H** |
| 14 | Маркировка РФ | ISO/IATF back; EAC **verify** · **M** | **Verify** · **M** | EAC+штамп · **H** · G07 | **Verify** · **M** | Overlay attestation · **M** · F-M04 | Overlay · **M** |
| 15 | Кириллица vs латиница | RU dominant + LUXE EN · **H** | Cyrillic bands ↑ · **H** · δ14 | RU dominant · **H** | RU dominant · **M** | EN base; RU overlay · **M** | EN base; overlay · **M** |
| 16 | Thumbnail ~120px | **High** · **H** | Med-high (LUXE+5W-40 OK) · **H** · δ14 | Med-high · **M** | **Medium** OEM fail · **M** · δ15 | **High** · **H** | **Medium** · **M** · δ13 |
| 17 | Cognitive load / space | High uniform · **H** | High uniform ↑ · **H** · δ14 | High claustrophobic · **H** | High uniform · **H** · δ15 | High dense 100% · **H** | **Bimodal** low top/peak bottom · **H** · δ13 |
| 18 | Legacy / rev. risk | **Major** SL/semi facings · **M** · F-L10 | = R1 · **M** | **Low** stable wrap · **H** · G13 | = R3 · **H** | **Low** since 2022 · **H** | = R5 · **H** |

---

## 4. Сводка 4L-only (cross-brand · для этапа 5–6)

| Параметр | LUXE 4L | GPN 4L | Mobil 4L |
|----------|---------|--------|----------|
| API front | SN/CF | SN/CF | **—** |
| OEM front effective | No | Microtype | No |
| RF supply | Official | Official | **Parallel import** |
| Anti-fraud | — | **3662.ru** | None |
| Cross-face | Pass (current) | Pass | Partial (+overlay) |
| Digital gap | None | Site superset | Overlay superset |
| PGMM paradigm | Solid/Armor | Obscuration/Density | Plasma/Armor |
| Top STM gap | OEM front + versioning | Readable OEM + channel parity | Native RU + API front + official channel |

---

## 5. Паттерны рынка (mass-mid 5W-40)

1. **Solid > Fluid:** все три бренда в PGMM вытесняют трибологию/жидкость метафорами брони, металла или термокинетики — категорийная норма, не дифференциатор.
2. **Heuristic compression:** SAE **5W-40** — главный shelf-anchor; OEM/API системно **не на фронте** (LUKOIL, Mobil) или **формально есть, но нечитаемо** (GPN).
3. **Инженерная асимметрия:** digital (GPN site) или importer overlay (Mobil) часто **шире**, чем physical label — channel gap F-G04 / F-M13.
4. **1L = другой продукт коммуникации:** при сохранении M_SYSTEM secondary claims (OEM, icons, API detail) **деградируют** на 1L — DRY rescale без пересборки brief.
5. **Trust stack:** только GPN строит anti-fraud UX (3662); LUKOIL/Mobil — пробел для СТМ при сохранении official supply.

---

## 6. White space для СТМ (MECE)

| Блок | Gap на полке | Действие СТМ |
|------|--------------|--------------|
| **A. Claims architecture** | API/OEM off-front или microtype | **Readable OEM band** + API SN/CF на фронте 4L и 1L |
| **B. Channel integrity** | Site/overlay superset vs pack | Pack claims = web/TDS; или явный QR → verified sheet |
| **C. Format fairness** | 1L теряет secondary layer | Отдельный 1L brief: крупный 1L, center OEM, min. one icon |
| **D. Visual paradigm** | Claustrophobic density (GPN/Mobil) vs armor (all) | **Whitespace + fluid/hydro** OR **smart-flat** — не копировать броню |
| **E. Trust & supply** | Mobil parallel; LUKOIL legacy facings | Official RF + optional proof layer (не обязательно 3662-клон) + **version label** при reformulation |
| **F. Language** | Mobil EN+overlay | **Integrated Cyrillic** native wrap |

---

## 7. Риски / lacunae (не видно на фото / не аудировано)

| ID | Lacuna | Затронутые строки | Severity |
|----|--------|-------------------|----------|
| LAC-01 | **ODSA 1L не прогонялся** — строки R2,R4,R6 = PGMM delta + extrapolation | R2,R4,R6 | Method · **M** |
| LAC-02 | LUKOIL **legacy SL/semi** facings — доля на полке н/д | R1,R2 | F-L10 · **M** |
| LAC-03 | PGMM wiki/10 **stale** (SL/semi) — visual layer частично valid | R1 | F-L04 · **M** |
| LAC-04 | Retail shelf @1.2 m — не измерено | all | GAP-G03, GAP-M06 · **L** |
| LAC-05 | Mobil **RU overlay** — text attestation без фото | R5,R6 | F-M04 · **M** |
| LAC-06 | GPN **TDS PDF** — site superset не верифицирован документом | R3,R4 | F-G04 · **M** |
| LAC-07 | LUKOIL 1L **API SL vs SN** на одной линейке — verify batch | R2 | delta/14 · **M** |
| LAC-08 | EAC/штамп LUKOIL 4L — verify на полном фото оборота | R1 | GAP · **L** |

---

## 8. Реестр источников

| Wiki ID | Артефакт |
|---------|----------|
| [10](../Cursor/wiki/10_PGMM_LUKOIL_LUXE_5W-40.md) | PGMM full LUKOIL 4L |
| [11](../Cursor/wiki/11_PGMM_Gazpromneft_Premium_N_5W-40.md) | PGMM full GPN 4L |
| [12](../Cursor/wiki/12_PGMM_mobil_super_3000_x1_5w_40.md) | PGMM full Mobil 4L |
| [13](../Cursor/wiki/13_PGMM_mobil_super_3000_x1_5w_40_1L_delta.md) | PGMM delta Mobil 1L |
| [14](../Cursor/wiki/14_PGMM_LUKOIL_LUXE_5W-40_5w_40_1L_delta.md) | PGMM delta LUKOIL 1L |
| [15](../Cursor/wiki/15_PGMM_Gazpromneft_Premium_N_5W-40_1L_delta.md) | PGMM delta GPN 1L |
| [16](../Cursor/wiki/16_ODSA_LUKOIL_LUXE_5W-40_4L.md) | ODSA LUKOIL 4L |
| [17](../Cursor/wiki/17_ODSA_Gazpromneft_Premium_N_5W-40_4L.md) | ODSA GPN 4L |
| [18](../Cursor/wiki/18_ODSA_mobil_super_3000_x1_5w_40_4L.md) | ODSA Mobil 4L |

**DoD этапа 4 (matrix):** ✅ черновик матрицы 6×18 · pending: ODSA 1L optional pass · PGMM/10 refresh · retail @1.2m

---

*Сборка: transpose canonical tables wiki/16–18 + PGMM 10–15 · протокол C rev.1*
