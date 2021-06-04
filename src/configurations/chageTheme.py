######################################

######################################

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton,QComboBox
from PyQt5.QtCore import Qt

from src.configs.types import Package
from src.configs.funcs import MudeTheme
from src.configs.files import Files
from src.widgets.baseMainWindows import BaseMainWindow
import json

class ChangeTheme(BaseMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.themes = self.jsonConfigs["*themes"]

        self.selectTheme()
        self.configuresStyles()
#         self.jsonConfigs = ReadConfigs()
#         self.lang = GetLang()
#         self.themes = self.jsonConfigs["*themes"]
        

#         ######################################
#         # Executa os Objetos da SplashScreen #
#         ######################################
#         self.Frames()
#         self.Buttons()
#         self.selectTheme()
#         self.setConfigs() 
#         self.configuresStyles()
#         ######################################



#     #Frames da Tela
#     def Frames(self) -> None:
#         self._frame = QFrame(self)
#         self._frame2 = QFrame(self)

#     #Buttons da tela
#     def Buttons(self) -> None:
#         self._closeButton = QPushButton(self._frame2)
        
#     # Configurações da SplashScreeen
#     def setConfigs(self) -> None:
#         # Configurações Da Tela # 
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.setMaximumSize(int(),int(250))
#         self.setMinimumSize(int(400),int(250))
#         self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
#         self.move(QPoint(self.x(),150))

#         # Configurações Do Primeiro Frame
#         self._frame.setGeometry(int(0),int(0),int(400),int(250))

#         # Configurações do Frameless Window
#         self._frame2.setGeometry(int(0),int(0),int(400),int(30))
#         # self._frame2.mouseMoveEvent = lambda __:self.MoveWindows()
#         self._frame2.mouseMoveEvent = self.MoveWindows
#         self._closeButton.setGeometry(int(400-30),0,30,30)
#         self._closeButton.setText("×")
#         fontButton = QFont()
#         fontButton.setFamily("GungsuhChe")
#         fontButton.setPointSize(18)
#         # fontButton.
#         self._closeButton.setFont(fontButton)
#         self._closeButton.clicked.connect(self.close)

#     # Movo a tela
#     def MoveWindows(self,e):
#         x,y = pyautogui.position()
#         self.clickPosition = QPoint(x,y)
#         if not self.isFullScreen():
#             if e.buttons() == Qt.LeftButton:
#                 if (x <= 200):x=200
#                 if (y <= 15):y=15
#                 self.move(x-200,y-15)
    
    def selectTheme(self):
        self._label = QLabel(self._frame)
        self._label.setGeometry(0,30,400,80)
        font = QFont()
        font.setPointSize(20)
        self._label.setFont(font)
        self._label.setText(self.lang["Menu"]["Configs"]["SelectTheme"])
        self._label.setAlignment(Qt.AlignCenter)
        self._selectTheme = QComboBox(self._frame)
        self._selectTheme.setGeometry(20,110,360,50)
        self._selectTheme.addItems(self.themes)
        self._buttonSelect = QPushButton(self._frame)
        self._buttonSelect.setGeometry(0,180,400,40)
        self._buttonSelect.clicked.connect(self.MudeTheme)

    def MudeTheme(self):
        MudeTheme(self._selectTheme.currentText())

        # Sistema de baseMainWindow funcionado de boa!!!!!

#     # Stilos da Aplicação
    def configuresStyles(self):
        Coloring = json.loads(Files.Read(Package.editorThemeLocal+"/"+self.theme+".json"))["IdeColor"]

        self._label.setStyleSheet(f"""color:{Coloring["secondColor"]};""")