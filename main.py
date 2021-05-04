from PyQt5.QtWidgets import QApplication, QMainWindow
from loads import ExecuteFunctionsOfTime

from install import Install

from src.splashscreen import SplashScreen


def Main() -> None :
    Install() # Instalador

    App = QApplication([])
    SplashUi = SplashScreen()    
    SplashUi.show()
    App.exec_()
    
if __name__ == "__main__":
    Main()