from PyQt5.QtWidgets import QMainWindow,QFrame
from PyQt5.QtCore import Qt
import os
import json

from src.configs.types import *
from src.configs.files import Files

class SplashScreen(QMainWindow):
    def __init__(self) -> void:
        super().__init__()
        try:
            os.mkdir("./Public")
            os.mkdir("./Public/assets")
            os.mkdir("./Public/data")
            os.mkdir("./Public/json")

        except FileExistsError:
            print("not paths created")


        Files.isPrymaryExecutation(self.CreateFiles)

        self.Frame()
        self.setConfigs() # Configurações da SplashScreen

    
    def CreateFiles(self):
        Files.Write(Package.jsonLocal+"/configs.json",json.dumps(Data.jsonConfigs))

    def Frame(self) -> void:
        self._frame = QFrame(self)
    
    def setConfigs(self) -> void:
        # Configurações Da Tela # 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(Int(40),Int(40),Int(400),Int(250))
        self.setMaximumSize(Int(400),Int(250))
        self.setMinimumSize(Int(400),Int(250))
            

        # Configurações Do Frame #
        self._frame.setGeometry(Int(0),Int(0),Int(400),Int(250))
        self._frame.setStyleSheet("background-color:green;border:1px solid #000;")