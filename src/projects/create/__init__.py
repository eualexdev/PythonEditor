from PyQt5.QtWidgets import QLabel, QWidget

class UICreateProject(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.parent:QWidget = parent
        self.q1 = QLabel(self)
        self.q1.setText("Teste")