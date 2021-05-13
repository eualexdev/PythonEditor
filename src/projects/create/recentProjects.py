from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

class RecentProjects(QFrame):
    def __init__(self,parent=None) -> None:
        self.parent:QFrame = parent
        super().__init__(parent)

        self.Configures()
        self.Widegts()

    def Widegts(self):
        self.nameIde()


    def nameIde(self):
        self._nameIde = QLabel(self)
        self._nameIde.setText("    Elegant IDE 2021")

        font = QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(True)

        self._nameIde.setFont(font)
        self._nameIde.setGeometry(0,0,400,80)

    def Configures(self):
        self.setMaximumSize(400,600)
        self.setMinimumSize(400,600)

    def ConfigureStyles(self,Coloring):
        self.setStyleSheet(f"""background-color:{Coloring["firstColor"]};""")
        self._nameIde.setStyleSheet(f"""color:{Coloring["secondColor"]};""")