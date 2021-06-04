import json

from src.configs.files import Files
from src.configs.types import Package

def ReadConfigs():
        return json.loads(Files.Read(Package.jsonLocal+"/configs.json"))

def MudeTheme(theme):
        configs = ReadConfigs()
        configs["theme"] = theme
        configs = json.dumps(configs,indent=4)
        Files.Clear(Package.jsonLocal+"/configs.json",configs)
        