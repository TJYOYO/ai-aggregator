import os
import glob
from server import mcp


@mcp.tool()
def read_file(path: str) -> str:
    """Read the contents of a file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: file not found: {path}"
    except PermissionError:
        return f"Error: permission denied: {path}"


@mcp.tool()
def write_file(path: str, content: str) -> str:
    """Write content to a file, creating or overwriting it."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Written to {path} ({len(content)} bytes)"


@mcp.tool()
def list_files(directory: str = ".", pattern: str = "*") -> str:
    """List files in a directory, optionally filtered by glob pattern."""
    search = os.path.join(directory, pattern)
    files = glob.glob(search, recursive=True)
    if not files:
        return "(no files found)"
    lines = []
    for f in sorted(files):
        full = os.path.join(os.path.abspath(directory), f) if directory != "." else f
        lines.append(f"{'[DIR]' if os.path.isdir(full) else '[FILE]':6} {f}")
    return "\n".join(lines)


@mcp.tool()
def delete_file(path: str) -> str:
    """Delete a file."""
    try:
        os.remove(path)
        return f"Deleted: {path}"
    except FileNotFoundError:
        return f"Error: file not found: {path}"
    except IsADirectoryError:
        return f"Error: {path} is a directory, use a different tool"
