# functions of Elegant Ide
# core.engine

import sys
import os

try:
    import ctypes
except : pass

def Os_Error() -> None:pass

def GetPlatform() -> None:
    platform = sys.platform
    if platform in {'linux', 'linux2', 'darwin'}:
        return "unix"
    elif os.name == "nt" or os.environ.get('OS', '') != 'Windows_NT' or platform in {'win32', 'cygwin', 'msys'}:
        return "windows"
    return None

def IsAdm() -> bool:
    return ctypes.windll.shell32.IsUserAnAdmin() == 1
