from PyQt5.QtGui import QRadialGradient
from PyQt5.QtCore import QTimer

def ExecuteFunctionsOfTime(calback1,calback2):
    QTimer.singleShot(8000,calback1)
    QTimer.singleShot(8000,calback2)
    