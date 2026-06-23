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
      "url": "https://mcp.firecrawl.dev/${KEY}/v2/mcp"
    }
  }
}
EOF

cp "$WORKSPACE_MCP" "$DIPLOMA_MCP"
chmod 600 "$WORKSPACE_MCP" "$DIPLOMA_MCP" 2>/dev/null || true

# Home MCP (все workspace)
HOME_MCP="$HOME/.cursor/mcp.json"
mkdir -p "$(dirname "$HOME_MCP")"
cp "$WORKSPACE_MCP" "$HOME_MCP"
chmod 600 "$HOME_MCP" 2>/dev/null || true

# Workspace subfolder 03_PGMM_… (симлинк; путь ../../ — не ../, иначе цикл)
SUB03="$(cd "$(dirname "$0")/../03_PGMM_ODSA_упаковка_конкуренты" && pwd)"
SUB03_MCP_DIR="$SUB03/.cursor"
SUB03_MCP="$SUB03_MCP_DIR/mcp.json"
if [[ -d "$SUB03" ]]; then
  mkdir -p "$SUB03_MCP_DIR"
  ln -sf "../../.cursor/mcp.json" "$SUB03_MCP"
fi

echo "Готово:"
echo "  $WORKSPACE_MCP"
echo "  $DIPLOMA_MCP"
echo "  $HOME_MCP"
[[ -L "$SUB03_MCP" ]] && echo "  $SUB03_MCP -> ../../.cursor/mcp.json"
echo "Перезапустите Cursor или: Settings → Tools & MCP → Refresh."
