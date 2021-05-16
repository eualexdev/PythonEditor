######################################

######################################

from os import error, path
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow,QFrame, QPushButton,QApplication
from PyQt5.QtCore import QPoint, Qt
import os,json,sys,pyautogui

from src.configs.types import Package
from src.configs.funcs import ReadConfigs
from src.configs.files import Files

#SplashScreen Da Ide
class ChangeTheme(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
    

        self.jsonConfigs = ReadConfigs()
        
        ######################################
        # Executa os Objetos da SplashScreen #
        ######################################
        self.Frames()
        self.Buttons()
        self.setConfigs() 
        self.configuresStyles()
        ######################################



    #Frames da Tel
    def Frames(self) -> None:
        self._frame = QFrame(self)
        self._frame2 = QFrame(self)

    # Labels da Tela
        

    #Buttons da tela
    def Buttons(self) -> None:
        self._closeButton = QPushButton(self._frame2)
        
    #Progress Bar
    
    #Evento de Aumenta a valor progress bar

    # Configurações da SplashScreeen
    def setConfigs(self) -> None:
        # Configurações Da Tela # 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMaximumSize(int(400),int(250))
        self.setMinimumSize(int(400),int(250))
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.move(QPoint(self.x(),150))

        # Configurações Do Primeiro Frame
        self._frame.setGeometry(int(0),int(0),int(400),int(250))

        # Configurações do Frameless Window
        self._frame2.setGeometry(int(0),int(0),int(400),int(30))
        # self._frame2.mouseMoveEvent = lambda __:self.MoveWindows()
        self._frame2.mouseMoveEvent = self.MoveWindows
        self._closeButton.setGeometry(int(400-30),0,30,30)
        self._closeButton.setText("×")
        fontButton = QFont()
        fontButton.setFamily("GungsuhChe")
        fontButton.setPointSize(18)
        # fontButton.
        self._closeButton.setFont(fontButton)
        self._closeButton.clicked.connect(lambda:self.close()+sys.exit())

    # Movo a tela
    def MoveWindows(self,e):
        x,y = pyautogui.position()
        self.clickPosition = QPoint(x,y)
        if not self.isFullScreen():
            if e.buttons() == Qt.LeftButton:
                if (x <= 200):x=200
                if (y <= 15):y=15
                self.move(x-200,y-15)

    # Stilos da Aplicação
    def configuresStyles(self):
        theme = self.jsonConfigs["theme"]
        Coloring = json.loads(Files.Read(Package.editorThemeLocal+"/"+theme+".json"))["IdeColor"]

        self._frame.setStyleSheet(f"""
background-color:{Coloring["firstColor"]};
/*border:1px solid {Coloring["secondColor"]}; */       
""")   

        self._frame2.setStyleSheet(f"""
background-color:{Coloring["secondColor"]};      
""")

        self._closeButton.setStyleSheet("""
QPushButton{
    color:"""+Coloring["outherColor"]+";"+"""
    border:0px;
}
QPushButton:hover{
    border:1px solid #ff0000;
    background-color:#ff0000;
}
""")