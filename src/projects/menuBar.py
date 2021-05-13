from PyQt5.QtWidgets import QFrame, QLabel, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTimer, Qt

from src.configurations import UiConfiguration
from src.projects.create import UICreateProject

from src.configs.funcs import ReadConfigs
from src.configs.types import Package
from src.configs.langs import GetLang



class MenuBar(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent:QFrame = parent
        
        self._countMenu = False
        self.geometryMenu = 50

        self.jsonConfigs = ReadConfigs()
        self.lang = GetLang()
        # self.menuVelocity = self.jsonConfigs["menuVelocity"]
        self.menuVelocity = 4

        self.Configures()
        self.Buttons()

    def Buttons(self):
        """Todos os botões da parte do menu"""
        self.MenuButton()
        self.ConfigurationsButton()
        self.CreateProjectsButton()

    def Configures(self):
        """Configurações do menu"""
        self.setMaximumSize(50,9999)
        self.setMinimumSize(50,9999)


    def MenuButton(self):
        """Botão de abre o menu"""
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
        # fontButton.setFamily("Segoe Print")
        fontButton.setPointSize(12)
        # fontButton.setBold(True)

        text = "              "+ self.lang["Menu"]["MenuText"]

        self._menuButtonLabel = QLabel(self._menuButton)
        self._menuButtonLabel.setGeometry(0,0,250,50)
        self._menuButtonLabel.setText(text)
        # self._menuButtonLabel.setAlignment(Qt.AlignCenter)
        self._menuButtonLabel.setFont(fontButton)

    def ConfigurationsButton(self):
        """Botão de configurações"""
        self._buttonConfig = QPushButton(self)
        self._buttonConfig.setGeometry(0,self.parent.height() - 80,250,50)
        self._frameConfig = QPushButton(self._buttonConfig)
        self._frameConfig.setIcon(QIcon(Package.editorAssetsLocal+"/"+"ConfigureIcon.png"))
        self._frameConfig.setGeometry(0,0,50,50)
        self._frameConfig.setIconSize(QSize(43,43))
        self._borderButton = QPushButton(self._frameConfig)
        self._borderButton.setGeometry(0,0,4,50)
        self._borderButton.close()
        self._buttonConfigText = QLabel(self._buttonConfig)
        
        text = "             "+self.lang["Menu"]["Menu"]["Configuration"]
        font = QFont()
        font.setPointSize(12)

        self._buttonConfigText.setText(text)
        self._buttonConfigText.setGeometry(0,0,250,50)
        self._buttonConfigText.setFont(font)
        # self._buttonConfigText.setAlignment(Qt.AlignCenter)


        #Removi o sistema de move o botão de configuração para baixos
        # self._timer2 = QTimer()
        # self._timer2.timeout.connect(self.moveButtonConfig)
        # self._timer2.setInterval(0)
        # self._timer2.start()

        self._frameConfig.clicked.connect(lambda: self.parent._centralFrame.setCentralWidget(UiConfiguration(self.parent)))
        self._buttonConfig.clicked.connect(lambda: self.parent._centralFrame.setCentralWidget(UiConfiguration(self.parent))) 

    # def moveButtonConfig(self):
    #     """Move o buttão de configuração"""
    #     self._buttonConfig.setGeometry(0,self.parent.height() - 80,250,50)

    def CreateProjectsButton(self):
        # "Botão de criar os projetos"
        self._buttonProjects = QPushButton(self)
        self._buttonProjects.setGeometry(0,50,250,50)
        self._frameButtonProjects = QPushButton(self._buttonProjects)
        self._frameButtonProjects.setGeometry(0,0,50,50)
        self._frameButtonProjects.setIcon(QIcon(Package.editorAssetsLocal+"/CreateProjects.png"))
        self._frameButtonProjects.setIconSize(QSize(50,50))

        font = QFont()
        font.setPointSize(12)

        text = "              " + self.lang["Menu"]["Menu"]["CreateProjects"]
        self._buttonProjectsText = QLabel(self._buttonProjects)
        self._buttonProjectsText.setText(text)
        self._buttonProjectsText.setFont(font)
        self._buttonProjectsText.setGeometry(0,0,250,50)

        self._buttonProjects.clicked.connect(lambda: self.parent._centralFrame.setCentralWidget(UICreateProject(self.parent)))
        self._frameButtonProjects.clicked.connect(lambda: self.parent._centralFrame.setCentralWidget(UICreateProject(self.parent))) 


    def AdjustButton(self):
        """Coloca e tira os menu"""
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
        """Adiciona o menu"""
        if self.parent.isFullScreen():self.menuVelocity = 5
        else:self.menuVelocity = 1
        if self.geometryMenu != 250:
            self.geometryMenu += self.menuVelocity
            self.setMaximumSize(self.geometryMenu,9999)
            self.setMinimumSize(self.geometryMenu,9999)
    
    def RemMenu(self):
        """Remove o menu"""
        if self.parent.isFullScreen():self.menuVelocity = 5
        else:self.menuVelocity = 1
        if self.geometryMenu != 50:
            self.geometryMenu -= self.menuVelocity
            self.setMaximumSize(self.geometryMenu,9999)
            self.setMinimumSize(self.geometryMenu,9999)

    def ConfiguresStyles(self,Coloring):
        """coloca os estilos"""
        self.setStyleSheet(f"""background-color: {Coloring["secondColor"]};""")
        self._barDifernt.setStyleSheet(f"""background-color: {Coloring["thirdColor"]};""")
        self._bar1.setStyleSheet(f"""background-color: {Coloring["outherColor"]};""")
        self._bar2.setStyleSheet(f"""background-color: {Coloring["outherColor"]};""")
        self._bar3.setStyleSheet(f"""background-color: {Coloring["outherColor"]};""")

        self._menuButtonLabel.setStyleSheet(f"""background-color:transparent;color:{Coloring["outherColor"]};""")

        self._menuButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+Coloring["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+Coloring["secondColorSlow"]+""";
}
""")

        self._buttonConfig.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+Coloring["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+Coloring["secondColorSlow"]+""";
}
""")

        self._frameConfig.setStyleSheet(f"""background-color:transparent;""")
        self._borderButton.setStyleSheet(f"""background-color:transparent;""")
        self._buttonConfigText.setStyleSheet(f"""background-color:transparent;color: {Coloring["outherColor"]};""")

        self._buttonProjects.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+Coloring["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+Coloring["secondColorSlow"]+""";
}
""")

        self._buttonProjectsText.setStyleSheet(f"""background-color:transparent;color:{Coloring["outherColor"]};""")