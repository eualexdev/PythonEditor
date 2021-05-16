from typing import Collection
from PyQt5.QtWidgets import QFrame

class BaseProjects(QFrame):
    def __init__(self,parent=None) -> None:
        self.parent:QFrame = parent
        super().__init__(parent)

        self.Configures()
        self.Widegts()

    def Widegts(self):
        pass

    def Configures(self):
        self.setMaximumSize(400,600)
        self.setMinimumSize(400,600)

    def ConfigureStyles(self,Coloring):
        self.setStyleSheet(f"""background-color:{Coloring["firstColor"]};""")