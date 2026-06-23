# Cursor — LLM Wiki диплома «СТМ автомасла»

**Паттерн:** [Andrej Karpathy — LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)  
**Назначение:** единая скомпилированная база знаний для работы в **Cursor** и других агентах.  
**Сырьё (raw):** отчёты DR, промпты, реестры — в папках `01_DR_…`, `02_DR_…`, `00_…` (см. `raw/README.md`).

---

## Как пользоваться

1. **Агент (Cursor):** в начале сессии читать `AGENTS.md` → `wiki/index.md` → нужные страницы.
2. **Человек:** открыть `wiki/index.md` как оглавление.
3. **После каждого DR:** декомпозиция в папке DR (`wiki/08_декомпозиция_после_DR.md`) → ingest в wiki + `log.md`.
4. **Этапы 4+** — только после ✅ **2a** и **3a** (см. `wiki/01_этапы_дорожная_карта.md`).
5. **Skills** — повторяемые этапы: `wiki/09_skills_реестр.md`, вызов `используй skill <name>`.
6. **Firecrawl MCP** — верификация URL, scrape источников для DR (см. ниже).

---

## Firecrawl MCP

Веб-скрейпинг и проверка источников через [Firecrawl MCP](https://docs.firecrawl.dev/mcp-server).

**Установка (один раз):**

1. Получить ключ: https://www.firecrawl.dev/app/api-keys  
2. Из корня workspace (папка «Дипломная работа ДПО МГИМО»):

```bash
# вариант A: интерактивно
bash диплом_СТМ_автомасла/.cursor/setup-firecrawl-mcp.sh

# вариант B: из переменной окружения
export FIRECRAWL_API_KEY=fc-ваш_ключ
bash диплом_СТМ_автомасла/.cursor/setup-firecrawl-mcp.sh
```

3. **Cursor → Settings → Tools & MCP** (локально, не вкладка Cloud) — сервер `firecrawl` с зелёной точкой.  
4. **Developer: Reload Window** после правки `mcp.json`.

**Формат (актуальный):** `https://mcp.firecrawl.dev/{fc-ключ}/v2/mcp` — см. [Firecrawl MCP docs](https://docs.firecrawl.dev/mcp-server).

**Шаблон без ключа:** `../.cursor/mcp.json.example` (в git).  
**Файл с ключом:** `../../.cursor/mcp.json` + симлинк в `03_PGMM_…/.cursor/mcp.json` — **не коммитить**.

**Cloud Agent:** локальный `mcp.json` не подхватывается. В **Settings → Cloud → Add Custom MCP** вставить JSON из `../.cursor/mcp.cloud.example.json` (подставить ключ).

**Troubleshooting (23.06.2026):**

| Симптом | Причина | Fix |
|---------|---------|-----|
| Workspace MCP пуст | Симлинк `../.cursor/mcp.json` из `03_…/.cursor/` → **цикл** | `../../.cursor/mcp.json` (скрипт setup создаёт) |
| Home MCP пуст | `~/.cursor/mcp.json` был `{}` | setup копирует конфиг в Home |
| Firecrawl Error | Старый Bearer-формат | URL: `https://mcp.firecrawl.dev/{fc-ключ}/v2/mcp` |

**Когда использовать в дипломе:** проверка URL из `wiki/04_источники_и_URL.md`, scrape страниц для декомпозиции DR (2a/3a). **GPN-01:** сайт блокирует bot/curl — для ODSA использовать operator screenshot (ART-005) или browser MCP.

**Альтернатива (нужен Node.js 22+):** см. комментарий в `mcp.json.example` — локальный `npx firecrawl-mcp`.

---

## Структура

```
Cursor/
├── AGENTS.md          ← правила для ИИ (обязательно)
├── README.md          ← этот файл
├── wiki/
│   ├── index.md       ← каталог всех страниц
│   ├── log.md         ← журнал обновлений вики
│   ├── overview.md    ← синтез в 1 страницу
│   └── …              ← тематические страницы
└── raw/
    └── README.md      ← указатели на файлы-источники
```

---

## Связь с дипломом

Корень проекта: `../` (`диплом_СТМ_автомасла/`).  
Точка входа для дипломной работы: **`../README.md`** (ссылается сюда).
