from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
import pyautogui

from src.configs.types import Package

class WindowsBar(QFrame):
    def __init__(self, parent = None) -> None:
        super().__init__()
        self.parent:QWidget = parent
        self.Configures()
        self.Labels()
        self.Buttons()

    def Configures(self):
        self.setGeometry(0,0,self.parent.width(),30)
        self.setMaximumSize(9999,30)
        self.setMinimumSize(9999,30)

        # self.mouseMoveEvent = lambda __:self.MoveWindows()
        self.mouseMoveEvent = self.MoveWindows
        # self.mouseDoubleClickEvent = lambda __:self.fullScreen()

    def MoveWindows(self,e):
        x,y = pyautogui.position()
        x,y = pyautogui.position()
        if not self.parent.isFullScreen():
            if e.buttons() == Qt.LeftButton:
                self.parent.move(x-self.parent.width()/2,y-5)

    def Labels(self):
        fontLabel = QFont()
        fontLabel.setFamily("Segoe Print")
        fontLabel.setPointSize(10)
        fontLabel.setBold(True)

        self._label = QLabel(self)
        self._label.setGeometry(5,0,80,30)
        self._label.setText("Elegant IDE")
        self._label.setAlignment(Qt.AlignVCenter)
        self._label.setFont(fontLabel)

    def Buttons(self):
        fontButton = QFont()
        fontButton.setFamily("GungsuhChe")
        fontButton.setPointSize(18)

        self._closeButton = QPushButton(self)
        self._closeButton.setGeometry(self.parent.width()-30,0,30,30)
        self._closeButton.setText("×")
        self._closeButton.setFont(fontButton)
        self._closeButton.clicked.connect(self.parent.close)

        # Removi o botão full screen

        # self._fullButton = QPushButton(self)
        # self._fullButton.setGeometry(self.parent.width()-60,0,30,30)
        # self._fullButton.setIcon(QIcon(Package.editorAssetsLocal+"/Fullscreen.png"))
        # self._fullButton.setIconSize(QSize(15.5,15.5))
        # self._fullButton.clicked.connect(self.fullScreen)
        # # ageita os icone fullscreen porque ta um pouco ruim

        self._minimizeButton = QPushButton(self)
        self._minimizeButton.setGeometry(self.parent.width()-60,0,30,30)
        self._minimizeButton.setText("-")
        fontButton.setPointSize(25)
        self._minimizeButton.setFont(fontButton)
        self._minimizeButton.clicked.connect(self.parent.showMinimized)

    # def keyPressEvent(self, key: QKeyEvent) -> None:
    #     if key.key() == Qt.Key_F11:
    #         self.fullScreen()
            

    # verifica se um bug na hora de mover a tela

    # def fullScreen(self):
    #     if not self.parent.isFullScreen():
    #         self.parent.showFullScreen()
    #         self._closeButton.setGeometry(self.parent.width()-30,0,30,30)
    #         self._fullButton.setGeometry(self.parent.width()-60,0,30,30)
    #         self._minimizeButton.setGeometry(self.parent.width()-90,0,30,30)
    #         self._fullButton.setIcon(QIcon(Package.editorAssetsLocal+"/Minimize.png"))
    #         self._fullButton.setIconSize(QSize(17,17))
    #     else:
    #         self.parent.showNormal()
    #         self._closeButton.setGeometry(self.parent.width()-30,0,30,30)
    #         self._fullButton.setGeometry(self.parent.width()-60,0,30,30)
    #         self._minimizeButton.setGeometry(self.parent.width()-90,0,30,30)
    #         self._fullButton.setIcon(QIcon(Package.editorAssetsLocal+"/Fullscreen.png"))
    #         self._fullButton.setIconSize(QSize(15.5,15.5))



    def ConfiguresStyles(self,Coloring):
        self.setStyleSheet(f"""background-color:{Coloring["secondColor"]}""")
        
        self._label.setStyleSheet(f"""color:{Coloring["outherColor"]}""")

        self._closeButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+Coloring["outherColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:#ff0000;
}
""")

#         self._fullButton.setStyleSheet("""
# QPushButton{
#     background-color:transparent;
#     color: """+Coloring["outherColor"]+""";
#     border:0px;
# }

# QPushButton:hover{
#     background-color:"""+Coloring["secondColorSlow"]+""";
# }
# """)

        self._minimizeButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+Coloring["outherColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+Coloring["secondColorSlow"]+""";
}
""")

