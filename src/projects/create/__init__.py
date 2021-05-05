from PyQt5.QtWidgets import QWidget,QHBoxLayout
import json

from src.projects.create.cProject import UIFormProjects
from src.configs.files import Files
from src.configs.types import Package
from src.configs.funcs import ReadConfigs

class UICreateProject(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.parent:QWidget = parent
        self.jsonConfigs = ReadConfigs()

        self.Configures()
        self.ConfiguresStyles()

    

    def Configures(self):
        self._uiFormProjects = UIFormProjects(self)

        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.addWidget(self._uiFormProjects)
        self.setLayout(hbox)

    def ConfiguresStyles(self):
        theme = self.jsonConfigs["theme"]
        Coloring = json.loads(Files.Read(Package.editorThemeLocal+"/"+theme+".json"))["IdeColor"]

        self._uiFormProjects.ConfiguresStyles(Coloring)