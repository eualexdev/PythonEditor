from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow,QFrame, QProgressBar, QPushButton,QApplication
from PyQt5.QtCore import QPoint, Qt,QTimer
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
            os.mkdir("./Public/Editor/language")
            os.mkdir("./Public/data")
            os.mkdir("./Public/json")

        except FileExistsError:
            print("not paths created")

        Files.isPrymaryExecutation(self.CreateFiles)

        self.jsonConfigs = json.loads(Files.Read(Package.jsonLocal+"/configs.json"))


        self.Frames()
        self.Buttons()
        self.Labels()
        self.progressBar()
        self.setConfigs() # Configurações da SplashScreen

        self.configuresStyles()

    
    def CreateFiles(self):
        Files.Write(Package.jsonLocal+"/configs.json",json.dumps(Data.jsonConfigs,indent=4))
        Files.Write(Package.editorThemeLocal+"/light.json",json.dumps(Data.jsonThemeLight,indent=4))
        Files.Write(Package.editorThemeLocal+"/dark.json",json.dumps(Data.jsonThemeDark,indent=4))

    def Frames(self) -> void:
        self._frame = QFrame(self)
        self._frame2 = QFrame(self)

    
    def Labels(self):
        font = QFont()
        font.setPointSize(40)
        font.setFamily("Segoe Print")
        font.setBold(True)

        self._label = QLabel(self._frame)
        self._label.setText("Elegant Ide")    
        self._label.setFont(font)
        self._label.setAlignment(Qt.AlignCenter)
        self._label.setGeometry(1,70,398,80)
        self._label.setStyleSheet("color:#fff")

        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        self._label_2 = QLabel(self._frame)
        self._label_2.setText("V"+self.jsonConfigs["version"])
        self._label_2.setFont(font)
        self._label_2.setGeometry(5,220,130,30)

        font3 = QFont()
        font3.setFamily("Nirmala UI")
        font3.setPointSize(8)
        font3.setBold(True)

        self._label_3 = QLabel(self)
        self._label_3.setFont(font3)
        self._label_3.setGeometry(370,225,30,20)

    def Buttons(self) -> void:
        self._closeButton = QPushButton(self._frame2)
        
    def progressBar(self):
        self.v = 0
        font = QFont()
        font.setPointSize(1)
        self._progress = QProgressBar(self)
        self._progress.setGeometry(0,245,400,5)
        self._progress.setFont(font)
        self._progress.setValue(self.v)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.updateProgressBar)
        self.timer2.setInterval(40)
        self.timer2.start()

    def updateProgressBar(self):
        self._label_3.setText(str(self.v)+"%")
        if (self.v != 100):
            self.v += 1
            print(self.v)
        else:pass
        self._progress.setValue(self.v)

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
/*border:1px solid {splashColor["secondColor"]}; */       
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
        self._label.setStyleSheet(f"""color:{splashColor["secondColor"]};border:0px;""")
        self._label_2.setStyleSheet(f"""color:{splashColor["secondColor"]};border:0px;""")
        self._label_3.setStyleSheet(f"""color:{splashColor["secondColor"]};border:0px;""")

        self._progress.setStyleSheet("""
QProgressBar{
    border:0px ;
    color: transparent;
    background-color: """+ splashColor["secondColorSuperSlow"] + """;
}
QProgressBar::chunk{
    background-color: """+splashColor["secondColor"]+""";
}
""")