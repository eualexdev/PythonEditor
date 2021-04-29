import json

from PyQt5.QtCore import qRemovePostRoutine

from src.configs.files import Files
from src.configs.types import Package

def ReadConfigs():
        return json.loads(Files.Read(Package.jsonLocal+"/configs.json"))

