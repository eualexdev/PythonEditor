from loads import ExecuteFunctionsOfTime
from src.splashscreen import SplashScreen
from PyQt5.QtWidgets import QApplication


def Main() -> None :
    App = QApplication([])
    SplashUi = SplashScreen()
    # ExecuteFunctionsOfTime(SplashUi.close)
    SplashUi.show()
    App.exec()
if __name__ == "__main__":
    Main()