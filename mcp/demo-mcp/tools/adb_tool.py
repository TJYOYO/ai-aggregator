import subprocess
from server import mcp


def _run_adb(args: list[str]) -> str:
    """Run an adb command and return stdout."""
    result = subprocess.run(
        ["adb"] + args,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return f"Error: {result.stderr.strip()}"
    return result.stdout.strip() or "(empty)"


@mcp.tool()
def adb_devices() -> str:
    """List connected Android devices."""
    return _run_adb(["devices", "-l"])


@mcp.tool()
def adb_shell(device_id: str, command: str) -> str:
    """Run a shell command on an Android device."""
    return _run_adb(["-s", device_id, "shell", command])


@mcp.tool()
def adb_screenshot(device_id: str, save_path: str = "/sdcard/screenshot.png") -> str:
    """Take a screenshot on the device and pull it to the local machine."""
    remote_path = save_path
    local_file = "screenshot.png"
    _run_adb(["-s", device_id, "shell", "screencap", "-p", remote_path])
    return _run_adb(["-s", device_id, "pull", remote_path, local_file])


@mcp.tool()
def adb_install(device_id: str, apk_path: str) -> str:
    """Install an APK on an Android device."""
    return _run_adb(["-s", device_id, "install", apk_path])


@mcp.tool()
def adb_uninstall(device_id: str, package_name: str) -> str:
    """Uninstall a package from an Android device."""
    return _run_adb(["-s", device_id, "uninstall", package_name])
