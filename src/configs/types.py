
import json

void = None
String = str
Int = int
Float = float
Boll = bool

class Package:
    apiURlImg:str = "https://elegant-ide-api.netlify.app/img/"
    dataLocal:str = "./Public/data"
    jsonLocal:str = "./Public/json"
    editorThemeLocal:str = "./Public/Editor/Themes"
    editorAssetsLocal:str = "./Public/Editor/Assets"
class Data:

    jsonConfigs:dict = {
        "version":"1.0.0",
        "theme":"light",
        "animationDelay":200,
        "menuVelocity":4
    }

    jsonThemeLight:dict = {
        "SplashScreenColor":{
            "outherColor":"#fff",
            "firstColor":"#fff",
            "secondColor":"#0282be",
            "secondColorSlow":"#0290d3",
            "secondColorSuperSlow":"#02afff",
            "thirdColor":"#1E488F"
        }   
    }
    
    jsonThemeDark:dict ={
        "SplashScreenColor":{
            "outherColor":"#fff",
            "firstColor":"#11161d",
            "secondColor":"#006b9c",
            "secondColorSlow":"#0079b1",
            "secondColorSuperSlow":"#01a9f7",
            "thirdColor":"#07265c"
        }
    }



