# demo-mcp

A minimal [FastMCP](https://github.com/jlowin/fastmcp) server demo with two example tools.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Install

```bash
uv sync
```

## Usage

### MCP Server

```bash
uv run python server.py
```

### Tools

| Tool | Parameters | Description |
|------|-----------|-------------|
| `add` | `a: int, b: int` | Add two numbers |
| `hello` | `name: str` | Return a greeting |

### Entry Point

```bash
uv run python main.py
```


### VS Code config

Windows全局配置 `C:\Users\tianjin\AppData\Roaming\Code\User\mcp.json`：

```json
{
  "servers": {
    "demo-mcp": {
      "type": "stdio",
      "command": "C:\\Users\\tianjin\\.local\\bin\\uv.exe",
      "args": ["run", "python", "server.py"],
      "cwd": "D:\\AI\\ai-aggregator\\mcp\\demo-mcp"
    }
  }
}
```

或项目级 `.vscode/mcp.json`（`command` 可简写为 `"uv"`，`cwd` 用 `${workspaceFolder}`）。