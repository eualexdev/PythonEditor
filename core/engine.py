# functions of Elegant Ide
# core.engine

import sys
import os

def Os_Error() -> None:pass

platform = "Windows, Linux, Mac"
def GetPlatform() -> platform:
    platform = sys.platform
    if platform in {'linux', 'linux2', 'darwin'}:
        return "unix"
    elif os.name == "nt" or os.environ.get('OS', '') != 'Windows_NT' or platform in {'win32', 'cygwin', 'msys'}:
        return "windows"
    return platform