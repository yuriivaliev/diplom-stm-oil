# Унифицированная таблица ODSA×PGMM (canonical schema)

**Назначение:** одинаковый блок в конце каждого ODSA-отчёта (wiki/16–18+) для сборки `матрица_PGMM_ODSA_*.md`.

**Формат:** 18 строк · колонки `# | Параметр | Значение | Evidence | Confidence`  
**Confidence:** H / M / L · **Evidence:** EVID-* / PGMM wiki / «видно на фото» / «н/д»

| # | Параметр | Слой |
|---|----------|------|
| 1 | M_SYSTEM (PGMM) | PGMM |
| 2 | Carrier morphology (PGMM) | PGMM |
| 3 | Класс продукта (синт / полусинт) | ODSA |
| 4 | SAE 5W-40 — legibility | ODSA + PGMM |
| 5 | API — видимость (front / back) | ODSA |
| 6 | ACEA — видимость (front / back) | ODSA |
| 7 | OEM / допуски — front (effective) | ODSA |
| 8 | OEM / допуски — back / site / overlay | ODSA |
| 9 | Benefit-icons — доказуемость | ODSA + PGMM |
| 10 | Cross-face consistency | ODSA |
| 11 | Digital / overlay vs pack gap | ODSA |
| 12 | Anti-fraud UX | ODSA |
| 13 | RF supply & языковая модель | ODSA |
| 14 | Обязательная маркировка РФ | ODSA |
| 15 | Кириллица vs латиница | ODSA |
| 16 | Thumbnail robustness (~120 px) | PGMM (delta §6) |
| 17 | Cognitive load / negative space | PGMM |
| 18 | Legacy / rev. risk на полке | ODSA |

> Delta 1L: те же параметры — отдельные строки матрицы («1 format = 1 row»).
