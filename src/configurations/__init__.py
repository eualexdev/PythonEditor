from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget
import json

from src.configs.files import Files
from src.configs.types import Package
from src.configs.funcs import ReadConfigs
from src.configurations.menuBar import ConfigurationMenuBar

class UiConfiguration(QWidget):
    def __init__(self,parent:QWidget=None):
        super().__init__()
        self.parent:QWidget = parent
        
        
        self.jsonConfigs =  ReadConfigs()

        self.Configuration()
        self.ConfiguresStyles()
        self.setLayout(self.hbox)

    def Configuration(self):
        self.hbox = QHBoxLayout()
        self.hbox.setContentsMargins(0,0,0,0)
        self.hbox.setSpacing(0)

        self.cmenuBar = ConfigurationMenuBar(self)

        self.hbox.addWidget(self.cmenuBar)
        self.hbox.addWidget(QLabel())

    def ConfiguresStyles(self):
        theme = self.jsonConfigs["theme"]
        splashColor = json.loads(Files.Read(Package.editorThemeLocal+"/"+theme+".json"))["SplashScreenColor"]

        self.cmenuBar.ConfiguresStyles(splashColor)