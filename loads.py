from PyQt5.QtGui import QRadialGradient
from PyQt5.QtCore import QTimer

def ExecuteFunctionsOfTime(*calback):
    c = 5000
    for i in calback:
            QTimer.singleShot(c,i)
        
    # QTimer.singleShot(8000,calback2)
    