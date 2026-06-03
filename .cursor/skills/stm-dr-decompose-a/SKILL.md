---
name: stm-dr-decompose-a
description: >-
  Decomposes the DR-A brand-market Deep Research report into folder structure,
  diploma canon, URL registry, and wiki ingest for MGIMO STM thesis stage 2a.
  Use when the user says декомпозиция DR-A, этап 2a, 01_DR_доли, or after
  отчёт_DR-A is ready.
disable-model-invocation: true
---

# DR-A decomposition (stage 2a)

## Preconditions

- Main report exists: `01_DR_доли_производителей_2022-2026/отчёт_DR-A_run2_*.md` (or agreed run N).
- Read `Cursor/wiki/08_декомпозиция_после_DR.md` and `Cursor/wiki/02_DR-A_бренды_рынок.md`.

## Workflow

Copy and track:

```
- [ ] Folder hygiene (one main report; older runs → архив_run/ or *_run1 suffix)
- [ ] A_канон_диплом.md (or update A_рост_и_изменения_РФ_канон.md) — thesis-ready tables + caveats
- [ ] URL: A_URL_реестр_runN.md + url_ссылки_на_DR_канон.md
- [ ] Every number → source ID (S2-*, V1-*, AS-*); S2 ≠ V1 never merged
- [ ] 2024–2026 brand shares: н/д — no interpolation
- [ ] Strip cite turn… artifacts from canon
- [ ] Optional: A_ODSA_чеклист.md, A_сравнение_run1_run2.md
- [ ] Wiki: update Cursor/wiki/02_DR-A_бренды_рынок.md, log.md, overview if needed
- [ ] Mark 2a ✅ in Cursor/wiki/01_этапы_дорожная_карта.md
```

## Hard constraints

- «Прочие» = arithmetic remainder within same source/base — not interpolation.
- STM brand: no invented market share %.
- Kolesa URL slug: `rastushhem`.

## When 2a is closed

Propose updating this skill if filenames differ from template; then user may start **3a** (`stm-dr-decompose-b`).
