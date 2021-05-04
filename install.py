from core.engine import getPlatform
from core.windows import WindowsClass

platform_os = getPlatform()
def Install():
    global platform_os
    if platform_os == "win":
        WindowsClass.Install()