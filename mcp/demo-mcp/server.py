from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    """
    return a + b


@mcp.tool()
def hello(name: str) -> str:
    return f"Hello {name}"


import tools  # noqa: E402,F401


if __name__ == "__main__":
    mcp.run()