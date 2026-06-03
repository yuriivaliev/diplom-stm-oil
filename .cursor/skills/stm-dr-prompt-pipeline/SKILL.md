---
name: stm-dr-prompt-pipeline
description: >-
  Builds Deep Research executor prompts for the STM thesis using analyst protocol
  blocks 1.j–1.t: taxonomy → GPToracle → Red Team → FINAL. Use when creating
  DR-A, DR-B, or DR-C prompts, мета-промпт, таксономия, or Red Team patches.
disable-model-invocation: true
---

# DR prompt pipeline (stage 1 pattern)

## Scope per run

One DR code only: **A** (brands) | **B** (SAE) | **C** (PGMM) — never one prompt «про всё».

## Inputs

- `00_таксономии_и_промпты_аналитика/<A|B|C>_таксономия_протокол_аналитика.md`
- `00_…/<X>_вход_для_GPToracle.md`
- Prior FINAL in same folder for Red Team diff

## Steps

1. **Taxonomy** — blocks 1.j, 1.x, 1.w, 1.y, 1.t filled.
2. **GPToracle** → `<X>_промпт_DR_исполнитель_v2_oracle.md`.
3. **Red Team** — A: P1–P12; B: BP1–BP12 + RF-1…10; document patches at top of FINAL.
4. **FINAL** → `<X>_промпт_DR_исполнитель_FINAL_full.md` (Oracle body + patch block).

## Code-specific gates

| Code | Must include |
|------|----------------|
| A | GATE sources; S2 vs V1 separate; 2024–26 н/д; no STM % |
| B | No mineral; FO/proxy labels; URL hygiene; Nielsen tier |
| C | Packaging matrix only — not market shares |

## Output

Do not run Deep Research inside this skill unless user asks — deliver FINAL prompt file path.

## Reference

`Cursor/wiki/06_методология_протокол_аналитика.md`, existing `A_*` / `B_*` in `00_таксономии_…/`.
