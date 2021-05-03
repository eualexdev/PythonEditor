# Instalador Elegant Ide

from core.engine import (
    GetPlatform,
    IsAdm
)

from core.platform import (
    Windows,
    Unix
)

def Install():
    """Coloca o a Ide no Path"""

    adm = IsAdm()
    platform = GetPlatform()

    if platform == "windows":
        Windows(adm)

Install()