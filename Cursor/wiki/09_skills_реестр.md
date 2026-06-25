# Реестр Cursor Skills — диплом СТМ

**Обновлено:** 25.06.2026

---

## Правило (для агента)

Когда этап **существенно проработан** (отчёт DR, декомпозиция, ingest в wiki, согласование):

1. **Предложить пользователю** создать skill с именем и одной фразой «зачем».
2. После согласия (или явного «создай skill») — положить в **`.cursor/skills/<name>/SKILL.md`** (project scope).
3. Записать строку в таблицу ниже + краткая запись в [log.md](log.md).

Не создавать skill молча — всегда **предложение** в конце сессии по этапу.

---

## Реестр

| Skill | Этап | Статус | Запуск |
|-------|------|:------:|--------|
| [stm-diploma-wiki](../../.cursor/skills/stm-diploma-wiki/SKILL.md) | Вики, запросы по диплому | ✅ | «используй skill stm-diploma-wiki» |
| [stm-dr-decompose-a](../../.cursor/skills/stm-dr-decompose-a/SKILL.md) | **2a** декомпозиция DR-A | ✅ | «skill stm-dr-decompose-a» |
| [stm-dr-decompose-b](../../.cursor/skills/stm-dr-decompose-b/SKILL.md) | **3a** декомпозиция DR-B | ✅ | «skill stm-dr-decompose-b» |
| [stm-dr-prompt-pipeline](../../.cursor/skills/stm-dr-prompt-pipeline/SKILL.md) | 1 — таксономия → FINAL | ✅ | «skill stm-dr-prompt-pipeline» + код A/B/C |
| [stm-pgmm](../../.cursor/skills/stm-pgmm/SKILL.md) | **4** PGMM full | ✅ | «skill stm-pgmm» / «skill pgmm» |
| [stm-pgmm-delta](../../.cursor/skills/stm-pgmm-delta/SKILL.md) | **4** PGMM delta (форматы) | ✅ | «skill stm-pgmm-delta» / «skill pgmm-delta» |
| [stm-odsa](../../.cursor/skills/stm-odsa/SKILL.md) | **4** ODSA claims audit | ✅ | «skill stm-odsa» / «skill odsa» |
| [stm-pgmm-odsa](../../.cursor/skills/stm-pgmm-odsa/SKILL.md) | 4 — роутер → pgmm / delta / odsa | ✅ | legacy: «skill stm-pgmm-odsa» |
| stm-thesis-synthesis | 7 синтез | ⚪ предложить после 7 | — |

Путь от корня диплома: `.cursor/skills/<name>/SKILL.md`.

---

## Очередь предложений (сейчас)

| Когда закроете | Предложить skill |
|----------------|------------------|
| **2a** ✅ | обновить `stm-dr-decompose-a` (добавить ваши имена файлов канона) |
| **3a** ✅ | обновить `stm-dr-decompose-b` |
| Этап **4** PGMM/ODSA | ✅ `stm-pgmm`, `stm-pgmm-delta`, `stm-odsa` (split 25.06) |
| Этап **5** название | `stm-brand-name-odsa` |
| Этап **7** | `stm-thesis-synthesis` |

---

## См. также

- [08_декомпозиция_после_DR.md](08_декомпозиция_после_DR.md)
- [06_методология_протокол_аналитика.md](06_методология_протокол_аналитика.md)
- `Cursor/AGENTS.md` — раздел «Skills»
