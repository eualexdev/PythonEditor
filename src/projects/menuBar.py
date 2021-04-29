from PyQt5.QtWidgets import QFrame, QLabel, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTimer, Qt

from src.configurations import UiConfiguration
from src.configs.funcs import ReadConfigs
from src.configs.types import Package

class MenuBar(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent:QFrame = parent
        self.Configures()
        self.ButtonsBar()
        self.ConfigurationsButton()

        self._countMenu = False
        self.geometryMenu = 50

        self.jsonConfigs = ReadConfigs()
        # self.menuVelocity = self.jsonConfigs["menuVelocity"]
        self.menuVelocity = 4

    def Configures(self):
        self.setMaximumSize(50,9999)
        self.setMinimumSize(50,9999)


    def ButtonsBar(self):
        self._menuButton = QPushButton(self)
        self._menuButton.setGeometry(0,0,250,50)
        self._menuButton.clicked.connect(self.AdjustButton)

        self._barDifernt = QFrame(self._menuButton)
        self._barDifernt.setGeometry(0,0,4,50)
        self._barDifernt.close()

        self._bar1 = QFrame(self._menuButton)
        self._bar1.setGeometry(8,10,34,5)
        
        self._bar2 = QFrame(self._menuButton)
        self._bar2.setGeometry(8,23,34,5)
        
        self._bar3 = QFrame(self._menuButton)
        self._bar3.setGeometry(8,35,34,5)

        fontButton = QFont()
        fontButton.setFamily("Segoe Print")
        fontButton.setPointSize(14)
        fontButton.setBold(True)

        self._menuButtonLabel = QLabel(self._menuButton)
        self._menuButtonLabel.setGeometry(0,0,250,50)
        self._menuButtonLabel.setText("Menu")
        self._menuButtonLabel.setAlignment(Qt.AlignCenter)
        self._menuButtonLabel.setFont(fontButton)

    def ConfigurationsButton(self):
        self._buttonConfig = QPushButton(self)
        self._frameConfig = QPushButton(self._buttonConfig)
        self._frameConfig.setIcon(QIcon(Package.editorAssetsLocal+"/"+"ConfigureIcon.png"))
        self._frameConfig.setIconSize(QSize(43,43))
        self._borderButton = QPushButton(self._frameConfig)
        self._borderButton.setGeometry(0,0,4,50)
        self._borderButton.close()
        self._frameConfig.setGeometry(0,0,50,50)
        self._timer2 = QTimer()
        self._timer2.timeout.connect(self.moveButtonConfig)
        self._timer2.setInterval(0)
        self._timer2.start()

        self._frameConfig.clicked.connect(self.configureButtonFunction)
        self._buttonConfig.clicked.connect(self.configureButtonFunction)


    def configureButtonFunction(self):
        self.parent._centralFrame.setCentralWidget(UiConfiguration(self.parent))

    def moveButtonConfig(self):self._buttonConfig.setGeometry(0,self.parent.height() - 80,250,50)

    def AdjustButton(self):
        self._timer = QTimer()
        self._timer.setInterval(0)
        self._timer.start()
        if self._countMenu == False:
            self._timer.timeout.connect(self.AddMenu)
            self._countMenu = True
        else:
            self._timer.timeout.connect(self.RemMenu)
            self._countMenu = False

    def AddMenu(self):
        if self.parent.isFullScreen():self.menuVelocity = 10
        else:self.menuVelocity = 2
        if self.geometryMenu != 250:
            self.geometryMenu += self.menuVelocity
            self.setMaximumSize(self.geometryMenu,9999)
            self.setMinimumSize(self.geometryMenu,9999)
    
    def RemMenu(self):
        if self.parent.isFullScreen():self.menuVelocity = 10
        else:self.menuVelocity = 2
        if self.geometryMenu != 50:
            self.geometryMenu -= self.menuVelocity
            self.setMaximumSize(self.geometryMenu,9999)
            self.setMinimumSize(self.geometryMenu,9999)

    def ConfiguresStyles(self,splashColor):
        self.setStyleSheet(f"""background-color: {splashColor["secondColor"]};""")
        self._barDifernt.setStyleSheet(f"""background-color: {splashColor["thirdColor"]};""")
        self._bar1.setStyleSheet(f"""background-color: {splashColor["outherColor"]};""")
        self._bar2.setStyleSheet(f"""background-color: {splashColor["outherColor"]};""")
        self._bar3.setStyleSheet(f"""background-color: {splashColor["outherColor"]};""")

        self._menuButtonLabel.setStyleSheet(f"""background-color:transparent;color:{splashColor["outherColor"]};""")

        self._menuButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+splashColor["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+splashColor["secondColorSlow"]+""";
}
""")

        self._buttonConfig.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+splashColor["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+splashColor["secondColorSlow"]+""";
}
""")

        self._frameConfig.setStyleSheet(f"""background-color:transparent;""")
        self._borderButton.setStyleSheet(f"""background-color:transparent;""")