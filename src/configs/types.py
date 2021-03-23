
import json

void = None
String = str
Int = int
Float = float
Boll = bool

class Package:
    jsonLocal:str = "./Public/json"    
    dataLocal:str = "./Public/data"
    editorThemeLocal:str = "./Public/Editor/Themes"

class Data:
    jsonConfigs:dict = {
        "version":"1.0.0",
        "theme":"light",
        "animationDelay":500
    }

