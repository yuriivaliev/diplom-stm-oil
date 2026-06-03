---
name: stm-dr-decompose-b
description: >-
  Decomposes the DR-B SAE viscosity Deep Research report into folder structure,
  canon, URL registry, and wiki ingest for MGIMO STM thesis stage 3a. Use when
  the user says декомпозиция DR-B, этап 3a, 02_DR_вязкости, or SAE DR is ready.
disable-model-invocation: true
---

# DR-B decomposition (stage 3a)

## Preconditions

- **2a closed** unless user explicitly overrides.
- Main report: `02_DR_вязкости_спрос/отчёт_DR-B_run1.md` (or agreed run N).
- Read `Cursor/wiki/08_декомпозиция_после_DR.md`, `03_DR-B_вязкости_SAE.md`, `05_линейка_SKU_СТМ.md`.

## Workflow

```
- [ ] Folder hygiene + архив_run/ for old runs
- [ ] B_канон_диплом.md — SAE matrix, 0W-20, China fleet, SKU line; label прокси/tier
- [ ] URL: B_URL_реестр_runN.md + url_ссылки_на_DR_канон.md (verify HTTP where possible)
- [ ] No mineral oil claims; geography ЦФО+СЗФО+ЮФО or federal proxy stated
- [ ] B_сверка_prior_DR.md if hypotheses H1–H4 used
- [ ] Strip cite turn… from canon
- [ ] Wiki: 03, 05, 04 if new IDs; log.md; overview
- [ ] Mark 3a ✅ in 01_этапы; only then stage 4 is unblocked
```

## Hard constraints

- Do not mix DR-A brand tables with DR-B SAE.
- Federal proxy (B2X, Nielsen PDF, Autostat) — never pretend FO-level SAE matrix exists without data.
- SKU default: 5W-30, 5W-40, 0W-20 + 10W-40 semi (ЮФО/legacy); optional 0W-30.

## When 3a is closed

Propose skill `stm-pgmm-odsa` for stage 4.
