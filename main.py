from PyQt5.QtWidgets import QApplication, QMainWindow
from loads import ExecuteFunctionsOfTime

from src.splashscreen import SplashScreen
from src.projects import UiProjects


def Main() -> None :
    App = QApplication([])
    SplashUi = SplashScreen()
    ProjectsUi = UiProjects()

    ExecuteFunctionsOfTime(
        ProjectsUi.show,
        SplashUi.close
    )
    
    SplashUi.show()
    App.exec()

if __name__ == "__main__":
    Main()