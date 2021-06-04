from PyQt5.QtWidgets import QApplication, QMainWindow
from loads import ExecuteFunctionsOfTime

from src.widgets.baseMessageBox import BaseMessageBox
from src.splashscreen import SplashScreen

def Main() -> None :
    App = QApplication([])
    SplashUi = SplashScreen()
    SplashUi = BaseMessageBox()
    SplashUi.show()
    App.exec_()
    
if __name__ == "__main__":
    Main()
