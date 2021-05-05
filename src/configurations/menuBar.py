from PyQt5.QtWidgets import QFrame, QLabel, QWidget,QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

# Ageita o Menu que carrega animação mesmo já estano carregada

from src.configs.files import Files
from src.configs.types import Package
from src.configs.funcs import ReadConfigs
from src.configs.langs import GetLang

class ConfigurationMenuBar(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent:QWidget = parent
            
        self.geometryMenu = 250
        self.geometryMenuRevese = 0

        self.jsonConfigs = ReadConfigs()
        self.lang = GetLang()

        # self.menuVelocity = self.jsonConfigs["menuVelocity"]
        self.menuVelocity = 2
        self.Configurations()
        self.MenuButtons()

    def Configurations(self):
        self._timerMenu = QTimer()
        self._timerMenu.timeout.connect(self.ResizeMenu)
        self._timerMenu.setInterval(0)
        self._timerMenu.start()

    def ResizeMenu(self):
        if self.parent.parent.isFullScreen():self.menuVelocity = 5
        else:self.menuVelocity = 1
        if self.geometryMenuRevese <= 250:
            self.setMaximumSize(self.geometryMenuRevese,9999)
            self.setMinimumSize(self.geometryMenuRevese,9999)
            self.geometryMenuRevese += self.menuVelocity


    def MenuButtons(self):
        self._menuButton = QPushButton(self)
        self._menuButton.setGeometry(0,0,250,50)
        self._menuButton.clicked.connect(self.AdjustButton)

        text = "   " + self.lang["Menu"]["Configs"]["ConfigureMenu"]
        leftTextFont = QFont()
        leftTextFont.setPointSize(12)

        self._menuButtonLeftText = QLabel(self._menuButton)
        self._menuButtonLeftText.setGeometry(0,0,250,50)
        self._menuButtonLeftText.setAlignment(Qt.AlignVCenter)
        self._menuButtonLeftText.setText(text)
        self._menuButtonLeftText.setFont(leftTextFont)
        
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
        global controls
        if self.parent.parent.isFullScreen():self.menuVelocity = 5
        else:self.menuVelocity = 1
        # ageita a velocidade do menu
        if self.geometryMenu > 0:
            self.setMaximumSize(self.geometryMenu,9999)
            self.setMinimumSize(self.geometryMenu,9999)
            if self.parent.parent.isFullScreen() and self.geometryMenu == self.menuVelocity:
                self.geometryMenu -= self.menuVelocity
                self.setMaximumSize(self.geometryMenu,9999)
                self.setMinimumSize(self.geometryMenu,9999)
            else:
                self.geometryMenu -= self.menuVelocity
                self.setMaximumSize(self.geometryMenu,9999)
                self.setMinimumSize(self.geometryMenu,9999)
                print(self.geometryMenu)

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
        self._menuButtonLeftText.setStyleSheet(f"""background-color: transparent;color: {splashColor["outherColor"]}""")
