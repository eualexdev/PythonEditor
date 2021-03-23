from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow,QFrame, QPushButton,QApplication
from PyQt5.QtCore import QPoint, Qt
import os,json,sys,pyautogui

from src.configs.types import *
from src.configs.files import Files

class SplashScreen(QMainWindow):
    def __init__(self) -> void:
        super().__init__()
        try:
            os.mkdir("./Public")
            os.mkdir("./Public/Editor")
            os.mkdir("./Public/Editor/Themes")
            os.mkdir("./Public/Editor/assets")
            os.mkdir("./Public/data")
            os.mkdir("./Public/json")

        except FileExistsError:
            print("not paths created")

        self.whatBall = 1
        self.jsonConfigs = json.loads(Files.Read(Package.jsonLocal+"/configs.json"))

        Files.isPrymaryExecutation(self.CreateFiles)

        self.Frames()
        self.Buttons()
        self.Labels()
        self.FramesBalls()
        self.setConfigs() # Configurações da SplashScreen

        self.configuresStyles()

    
    def CreateFiles(self):
        Files.Write(Package.jsonLocal+"/configs.json",json.dumps(Data.jsonConfigs,indent=4))

    def Frames(self) -> void:
        self._frame = QFrame(self)
        self._frame2 = QFrame(self)

    def FramesBalls(self):
        self._ball_1 = QFrame(self._frame2)
        self._ball_2 = QFrame(self._frame2)
        self._ball_3 = QFrame(self._frame2)

        self._ball_1.setGeometry(5,10,10,10)
        self._ball_2.setGeometry(20,10,10,10)
        self._ball_3.setGeometry(35,10,10,10)

        self._ball_1.close()
        self._ball_2.close()
        self._ball_3.close()


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.BallAnimated)
        delay = self.jsonConfigs["animationDelay"]
        self.timer.setInterval(delay)
        self.timer.start()

    def BallAnimated(self):
        if (self.whatBall == 1):
            self._ball_1.show()
            self.whatBall += 1

        elif (self.whatBall == 2):
            self._ball_2.show()
            self.whatBall += 1

        elif (self.whatBall == 3):
            self._ball_3.show()
            self.whatBall += 1
        
        elif (self.whatBall == 4):
            self._ball_3.close()
            self.whatBall += 1

        elif (self.whatBall == 5):
            self._ball_2.close()
            self.whatBall += 1
        
        elif (self.whatBall == 6):
            self._ball_1.close()
            self.whatBall = 1

    def Labels(self):
        font = QFont()
        font.setPointSize(30)
        font.setFamily("Segoe Print")
        font.setBold(True)

        self._label = QLabel(self._frame)
        self._label.setText("Python Editor")    
        self._label.setFont(font)
        self._label.setAlignment(QtCore.Qt.AlignCenter)
        self._label.setGeometry(1,80,398,40)
        self._label.setStyleSheet("color:#fff")

    def Buttons(self) -> void:
        self._closeButton = QPushButton(self._frame2)

    def setConfigs(self) -> void:
        # Configurações Da Tela # 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMaximumSize(Int(400),Int(250))
        self.setMinimumSize(Int(400),Int(250))
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.move(QPoint(self.x(),150))

        # Configurações Do Primeiro Frame
        self._frame.setGeometry(Int(0),Int(0),Int(400),Int(250))

        # Configurações do Frameless Window
        self._frame2.setGeometry(int(0),int(0),int(400),int(30))
        self._frame2.mouseMoveEvent = lambda __:self.MoveWindows()
        self._closeButton.setGeometry(int(400-30),0,30,30)
        self._closeButton.setText("×")
        fontButton = QFont()
        fontButton.setFamily("GungsuhChe")
        fontButton.setPointSize(18)
        # fontButton.
        self._closeButton.setFont(fontButton)
        self._closeButton.clicked.connect(lambda:self.close()+sys.exit())

    def MoveWindows(self):
        x,y = pyautogui.position()
        if (x <= 200):x=200
        if (y <= 15):y=15
        self.move(x-200,y-15)

    def configuresStyles(self):
        theme = self.jsonConfigs["theme"]
        splashColor = json.loads(Files.Read(Package.editorThemeLocal+"/"+theme+".json"))["SplashScreenColor"]

 
        self._frame.setStyleSheet(f"""
background-color:{splashColor["firstColor"]};
border:1px solid {splashColor["secondColor"]};        
""")   

        self._frame2.setStyleSheet(f"""
background-color:{splashColor["secondColor"]};      
""")

        self._closeButton.setStyleSheet("""
QPushButton{
    color:"""+splashColor["firstColor"]+";"+"""
    border:0px;
}
QPushButton:hover{
    border:1px solid #ff0000;
    background-color:#ff0000;
}
""")

        self._ball_1.setStyleSheet(f"""background-color:{splashColor["firstColor"]};border-radius:5px;""")
        self._ball_2.setStyleSheet(f"""background-color:{splashColor["firstColor"]};border-radius:5px;""")
        self._ball_3.setStyleSheet(f"""background-color:{splashColor["firstColor"]};border-radius:5px;""")

        self._label.setStyleSheet(f"""color:{splashColor["secondColor"]};border:0px;""")