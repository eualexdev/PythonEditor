from PyQt5.QtWidgets import QFrame, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MenuBar(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent:QFrame = parent
        self.Configures()
        self.ButtonsBar()

        self._countMenu = False

    def Configures(self):
        self.setMaximumSize(55,9999)
        self.setMinimumSize(55,self.height())
    
    def ButtonsBar(self):
        self._menuButton = QPushButton(self)
        self._menuButton.setGeometry(0,0,250,50)
        self._menuButton.clicked.connect(self.AdjustButton)

        self._bar1 = QFrame(self._menuButton)
        self._bar1.setGeometry(10,5,5,40)
        
        self._bar2 = QFrame(self._menuButton)
        self._bar2.setGeometry(25,5,5,40)
        
        self._bar3 = QFrame(self._menuButton)
        self._bar3.setGeometry(40,5,5,40)

        fontButton = QFont()
        fontButton.setFamily("Segoe Print")
        fontButton.setPointSize(18)

        self._menuButtonLabel = QLabel(self._menuButton)
        self._menuButtonLabel.setGeometry(0,0,250,50)
        self._menuButtonLabel.setText("Menu")
        self._menuButtonLabel.setAlignment(Qt.AlignCenter)
        self._menuButtonLabel.setFont(fontButton)

    def AdjustButton(self):
        if self._countMenu == False:
            self.setMaximumSize(250,9999)
            self.setMinimumSize(250,self.height())
            self._countMenu = True
        else:
            self.setMaximumSize(55,9999)
            self.setMinimumSize(55,self.height())
            self._countMenu = False

    def ConfiguresStyles(self,splashColor):
        self.setStyleSheet(f"""background-color: {splashColor["secondColor"]};""")
        self._bar1.setStyleSheet(f"""background-color: {splashColor["firstColor"]};""")
        self._bar2.setStyleSheet(f"""background-color: {splashColor["firstColor"]};""")
        self._bar3.setStyleSheet(f"""background-color: {splashColor["firstColor"]};""")

        self._menuButtonLabel.setStyleSheet(f"""background-color:transparent;color:{splashColor["firstColor"]};""")

        self._menuButton.setStyleSheet("""
QPushButton{
    background-color:transparent;
    color: """+splashColor["firstColor"]+""";
    border:0px;
}

QPushButton:hover{
    background-color:"""+splashColor["secondColorSlow"]+""";
}
""")