from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import json

from src.configs.files import Files
from src.configs.types import Package
from src.projects.windowBar import WindowsBar
from src.projects.menuBar import MenuBar

class UiProjects(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.jsonConfigs = json.loads(Files.Read(Package.jsonLocal+"/configs.json"))
        

        self.Configures()
        self.WindowsBar()
        self.Div()
        self.ConfguresStyles()

        self.setLayout(self._vbox)


    def Configures(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMaximumSize(1000,600)
        self.setMinimumSize(1000,600)
        self._vbox = QVBoxLayout()
        self._vbox.setContentsMargins(0,0,0,0)
        self._vbox.setSpacing(0)

    def WindowsBar(self):
        self._windowsBar = WindowsBar(self)
        self._vbox.addWidget(self._windowsBar)

    def Div(self):
        self._div = QFrame()
        hbox = QHBoxLayout()
        self._menuBar = MenuBar(self)
        l = QLabel()
        l.setText("Eai")
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self._menuBar)
        hbox.addWidget(l)
        # a label 
        self._div.setLayout(hbox)
        self._vbox.addWidget(self._div)

    def ConfguresStyles(self):
        theme = self.jsonConfigs["theme"]
        splashColor = json.loads(Files.Read(Package.editorThemeLocal+"/"+theme+".json"))["SplashScreenColor"]


        self._div.setStyleSheet(f"""background-color:{splashColor["firstColor"]};""")

        self._windowsBar.ConfiguresStyles(splashColor)
        self._menuBar.ConfiguresStyles(splashColor)


def OpenUiProjects(self):
    ProjectsUi = UiProjects()
    ProjectsUi.show()
    self.timer.stop()
    self.close()