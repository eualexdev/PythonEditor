from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QKeyEvent
import pyautogui

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

        self.mouseMoveEvent = lambda __:self.MoveWindows()
        self.mouseDoubleClickEvent = lambda __:self.fullScreen()

    def MoveWindows(self):
        x,y = pyautogui.position()
        if not self.parent.isFullScreen():
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

        self._fullButton = QPushButton(self)
        self._fullButton.setGeometry(self.parent.width()-60,0,30,30)
        self._fullButton.clicked.connect(self.fullScreen)

        self._minimizeButton = QPushButton(self)
        self._minimizeButton.setGeometry(self.parent.width()-90,0,30,30)
        self._minimizeButton.setText("-")
        fontButton.setPointSize(22)
        self._minimizeButton.setFont(fontButton)
        self._minimizeButton.clicked.connect(self.parent.showMinimized)

    def keyPressEvent(self, key: QKeyEvent) -> None:
        if key.key() == Qt.Key_F11:
            self.fullScreen()
            
    def fullScreen(self):
        if not self.parent.isFullScreen():
            self.parent.showFullScreen()
            self._closeButton.setGeometry(self.parent.width()-30,0,30,30)
            self._fullButton.setGeometry(self.parent.width()-60,0,30,30)
            self._minimizeButton.setGeometry(self.parent.width()-90,0,30,30)
        else:
            self.parent.showNormal()
            self._closeButton.setGeometry(self.parent.width()-30,0,30,30)
            self._fullButton.setGeometry(self.parent.width()-60,0,30,30)
            self._minimizeButton.setGeometry(self.parent.width()-90,0,30,30)


    def ConfiguresStyles(self,splashColor):
        self.setStyleSheet(f"""background-color:{splashColor["secondColor"]}""")
        
        self._label.setStyleSheet(f"""color:{splashColor["firstColor"]}""")

        self._closeButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+splashColor["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:#ff0000;
}
""")

        self._fullButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+splashColor["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+splashColor["secondColorSlow"]+""";
}
""")

        self._minimizeButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+splashColor["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+splashColor["secondColorSlow"]+""";
}
""")

