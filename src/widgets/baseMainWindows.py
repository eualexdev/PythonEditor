######################################

######################################

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow,QFrame, QPushButton,QApplication,QComboBox
from PyQt5.QtCore import QPoint, Qt
import os,json,sys,pyautogui

from src.configs.types import Package
from src.configs.langs import GetLang
from src.configs.funcs import ReadConfigs
from src.configs.files import Files

class BaseMainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
    
        self.jsonConfigs = ReadConfigs()
        self.lang = GetLang()
        self.Frames()
        self.Buttons()
        self.setConfigs() 
        
        self.theme = self.jsonConfigs["theme"]
        Coloring = json.loads(Files.Read(Package.editorThemeLocal+"/"+self.theme+".json"))["IdeColor"]
        # self.Coloring = Coloring

        self._frame.setStyleSheet("""
QFrame {
    background-color:"""+f"""{Coloring["firstColor"]};"""+"""
    border:2px solid """+f"""{Coloring["secondColor"]};"""+"""    
}
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

    
    #Frames da Tela
    def Frames(self) -> None:
        self._frame = QFrame(self)
        self._frame2 = QFrame(self)

    #Buttons da tela
    def Buttons(self) -> None:
        self._closeButton = QPushButton(self._frame2)
        
    def setConfigs(self) -> None:
        # Configurações Da Tela # 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMaximumSize(int(),int(250))
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
        self._closeButton.clicked.connect(self.close)

    # Movo a tela
    def MoveWindows(self,e):
        x,y = pyautogui.position()
        self.clickPosition = QPoint(x,y)
        if not self.isFullScreen():
            if e.buttons() == Qt.LeftButton:
                if (x <= 200):x=200
                if (y <= 15):y=15
                self.move(x-200,y-15)
    