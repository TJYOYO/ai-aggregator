import subprocess
import os
from server import mcp


def _run_git(args: list[str], cwd: str | None = None) -> str:
    """Run a git command and return stdout."""
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd or os.getcwd(),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return f"Error: {result.stderr.strip()}"
    return result.stdout.strip() or "(empty)"


@mcp.tool()
def git_status(repo_path: str = ".") -> str:
    """Show the working tree status of a git repository."""
    return _run_git(["status", "--short", "--branch"], cwd=repo_path)


@mcp.tool()
def git_log(repo_path: str = ".", max_count: int = 10) -> str:
    """Show git commit logs."""
    return _run_git(
        ["log", f"--max-count={max_count}", "--oneline", "--decorate"], cwd=repo_path
    )


@mcp.tool()
def git_diff(repo_path: str = ".", staged: bool = False) -> str:
    """Show changes between commits or working tree."""
    args = ["diff"]
    if staged:
        args.append("--staged")
    return _run_git(args, cwd=repo_path)


@mcp.tool()
def git_branch(repo_path: str = ".") -> str:
    """List branches in a git repository."""
    return _run_git(["branch", "--all"], cwd=repo_path)


@mcp.tool()
def git_commit(repo_path: str, message: str) -> str:
    """Stage all changes and commit with the given message."""
    _run_git(["add", "-A"], cwd=repo_path)
    return _run_git(["commit", "-m", message], cwd=repo_path)


@mcp.tool()
def git_sync_squash_push(
    repo_path: str = ".",
    message: str = "squash merge",
    squash_count: int = 2,
) -> str:
    """Pull, stage & commit new changes, squash recent commits, then force push."""
    lines: list[str] = []

    # 1. git pull
    r = _run_git(["pull"], cwd=repo_path)
    lines.append(f"[pull] {r}")

    # 2. check for new/changed files  
    status = _run_git(["status", "--porcelain"], cwd=repo_path)
    if status and status != "(empty)":
        lines.append("[add] staging all changes")
        _run_git(["add", "-A"], cwd=repo_path)
        r = _run_git(["commit", "-m", message], cwd=repo_path)
        lines.append(f"[commit] {r}")
    else:
        lines.append("[add] no changes to stage")

    # 3. squash recent N commits into one
    if squash_count > 1:
        r = _run_git(
            ["reset", "--soft", f"HEAD~{squash_count}"], cwd=repo_path
        )
        if r.startswith("Error"):
            lines.append(f"[squash] {r}")
        else:
            r = _run_git(["commit", "-m", message], cwd=repo_path)
            lines.append(f"[squash] {squash_count} commits -> 1: {r}")

    # 4. force push
    branch = _run_git(["branch", "--show-current"], cwd=repo_path)
    r = _run_git(["push", "-f", "origin", branch], cwd=repo_path)
    lines.append(f"[push -f] {r}")

    return "\n".join(lines)
