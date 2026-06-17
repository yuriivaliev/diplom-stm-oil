#!/usr/bin/env bash
# Создаёт .cursor/mcp.json для Firecrawl MCP (ключ не коммитится в git).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
WORKSPACE_MCP="$ROOT/.cursor/mcp.json"
DIPLOMA_MCP="$(cd "$(dirname "$0")" && pwd)/mcp.json"

if [[ -n "${FIRECRAWL_API_KEY:-}" ]]; then
  KEY="$FIRECRAWL_API_KEY"
else
  read -rsp "Firecrawl API key (fc-...): " KEY
  echo
fi

if [[ -z "$KEY" || "$KEY" == *"YOUR_API_KEY"* || "$KEY" == *"REPLACE_WITH"* ]]; then
  echo "Ошибка: укажите реальный ключ Firecrawl." >&2
  exit 1
fi

mkdir -p "$(dirname "$WORKSPACE_MCP")"

cat > "$WORKSPACE_MCP" <<EOF
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer ${KEY}"
      }
    }
  }
}
EOF

cp "$WORKSPACE_MCP" "$DIPLOMA_MCP"
chmod 600 "$WORKSPACE_MCP" "$DIPLOMA_MCP" 2>/dev/null || true

echo "Готово:"
echo "  $WORKSPACE_MCP"
echo "  $DIPLOMA_MCP"
echo "Перезапустите Cursor или: Settings → Tools & MCP → Refresh."
