from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFrame

class UIFormProjects(QFrame):
    def __init__(self,parent=None):
        super().__init__()
        self.parent:QFrame = parent

        self.Configure()

    def Configure(self):
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)

    def ConfiguresStyles(self,Coloring):
        self.setStyleSheet(f"""background-color:{Coloring};""")