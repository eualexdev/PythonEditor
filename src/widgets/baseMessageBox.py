from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QFrame, QLabel, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QFont
import json

import pyautogui

from src.configs.types import Package
from src.configs.files import Files
from src.configs.funcs import ReadConfigs
from src.configs.langs import GetLang

class BaseMessageBox(QMainWindow):
    def __init__(self,title="",content=""):
        super().__init__()
        self.jsonConfigs = ReadConfigs()
        self.lang = GetLang()
        self.Widgets()
    
    def Widgets(self):
        self.setConfigs() 
        self.WindowBar()
        self.setStyles()

    def setConfigs(self):
        self.setWindowTitle(self.lang["Alerts"]["Alert"])
        self.setMaximumSize(250,150)
        self.setMinimumSize(250,150)

    
    def WindowBar(self):
        self._frame = QFrame(self)
        self._frame.setGeometry(0,0,250,30)
        self._frame.mouseMoveEvent = self.MoveWindows
        self.setWindowFlags(Qt.FramelessWindowHint)
        self._label = QLabel(self._frame)
        self._label.setText(" "+self.lang["Alerts"]["Alert"])
        self._label.setGeometry(0,0,250,30)
        self._label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self._label.setFont(font)
        self._closeButton = QPushButton(self._frame)
        self._closeButton.setGeometry(220,0,30,30)
        self._closeButton.setText("×")
        fontButton = QFont()
        fontButton.setFamily("GungsuhChe")
        fontButton.setPointSize(18)
        # fontButton.
        self._closeButton.setFont(fontButton)
        self._closeButton.clicked.connect(self.close)

    def MoveWindows(self,e):
        x,y = pyautogui.position()
        self.clickPosition = QPoint(x,y)
        if not self.isFullScreen():
            if e.buttons() == Qt.LeftButton:
                self.move(x-125,y-15)
    

    def setStyles(self):
        theme = self.jsonConfigs["theme"]
        Coloring = json.loads(Files.Read(Package.editorThemeLocal+"/"+theme+".json"))["IdeColor"]
        
        self.setStyleSheet(f"""background-color:{Coloring["firstColor"]};border:2px solid {Coloring["secondColor"]};""")
        self._frame.setStyleSheet(f"""background-color:{Coloring["secondColor"]}""")
        self._label.setStyleSheet(f"""background-color:transparent;color:{Coloring["outherColor"]};""")
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
    
    ### Fazer a msg box ###