from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
import json

from src.projects.create.recentProjects import RecentProjects

from src.configs.files import Files
from src.configs.types import Package
from src.configs.funcs import ReadConfigs

class UICreateProject(QFrame):
    def __init__(self,parent=None):
        super().__init__()
        self.parent:QFrame = parent

        self.jsonConfigs = ReadConfigs()


        self.Configure()
        self.Widgets()
        self.ConfiguresStyles()

    def Configure(self):pass
        # self.setMaximumSize(800,600)
        # self.setMinimumSize(800,600)

    def Widgets(self):
        self.Separators()
        self.SetWidgets()

    def Separators(self):
        self.hboxSep = QHBoxLayout()
        self._sep1 = QFrame()
        self._sep2 = QFrame()
        self.hboxSep.setContentsMargins(0,0,0,0)
        self.hboxSep.setSpacing(0)
        self.hboxSep.addWidget(self._sep1)
        self.hboxSep.addWidget(self._sep2)
        self.setLayout(self.hboxSep)

    def SetWidgets(self):
        self._recentProjects = RecentProjects(self._sep1)
        

    def ConfiguresStyles(self):
        theme = self.jsonConfigs["theme"]
        Coloring = json.loads(Files.Read(Package.editorThemeLocal+"/"+theme+".json"))["IdeColor"]

        self.setStyleSheet(f"""background-color:{Coloring["firstColor"]};""")
        self._sep1.setStyleSheet(f"""background-color:{Coloring["firstColor"]};""")
        self._sep2.setStyleSheet(f"""background-color:{Coloring["firstColor"]};""")

        self._recentProjects.ConfigureStyles(Coloring)