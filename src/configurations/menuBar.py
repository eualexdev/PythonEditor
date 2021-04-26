from PyQt5.QtWidgets import QFrame, QLabel, QWidget,QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import json

from src.configs.files import Files
from src.configs.types import Package

class ConfigurationMenuBar(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent:QWidget = parent
            

        self.geometryMenu = 250

        self.jsonConfigs = json.loads(Files.Read(Package.jsonLocal+"/configs.json"))
        # self.menuVelocity = self.jsonConfigs["menuVelocity"]
        self.menuVelocity = 2

        self.Configurations()
        self.MenuButtons()
            
    def Configurations(self):
        self.move(0,0)
        self.setMaximumSize(250,9999)
        self.setMinimumSize(250,9999)

    def MenuButtons(self):
        self._menuButton = QPushButton(self)
        self._menuButton.setGeometry(0,0,250,50)
        self._menuButton.clicked.connect(self.AdjustButton)

        self._menuButtonText = QLabel(self._menuButton)
        self._menuButtonText.setGeometry(200,0,50,50)
        self._menuButtonText.setText("×")
        self._menuButtonText.setAlignment(Qt.AlignCenter)
        fontButton = QFont()
        fontButton.setFamily("GungsuhChe")
        fontButton.setPointSize(22)
        self._menuButtonText.setFont(fontButton)

    def AdjustButton(self):
        self._timer = QTimer()
        self._timer.setInterval(0)
        self._timer.start()
        self._timer.timeout.connect(self.zeroMenu)


    def zeroMenu(self):
        if self.parent.parent.isFullScreen():self.menuVelocity = 10
        else:self.menuVelocity = 2
        if self.geometryMenu != 0:
            self.geometryMenu -= self.menuVelocity
            self.setMaximumSize(self.geometryMenu,9999)
            self.setMinimumSize(self.geometryMenu,9999)

    def ConfiguresStyles(self,splashColor):
        self.setStyleSheet(f"""background-color:{splashColor["secondColorPlus"]};""")
        self._menuButtonText.setStyleSheet(f"""background-color: transparent;color: {splashColor["outherColor"]}""")
        self._menuButton.setStyleSheet("""
        QPushButton{
            background-color: """+splashColor["secondColorPlus"]+""";
            color: """+splashColor["firstColor"]+""";
            border:0px;
        }

        QPushButton:hover{
            background-color:"""+splashColor["secondColorSuperPlus"]+""";
        }""")