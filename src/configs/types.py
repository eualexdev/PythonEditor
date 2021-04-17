
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
        "animationDelay":200
    }

    jsonThemeLight:dict = {
        "SplashScreenColor":{
            "firstColor":"#fff",
            "secondColor":"#0282be",
            "secondColorSlow":"#0290d3",
            "secondColorSuperSlow":"#02afff",
            "thirdColor":"#1E488F"
        }   
    }
    
    jsonThemeDark:dict ={
        "SplashScreenColor":{
            "firstColor":"#11161d",
            "secondColor":"#006b9c",
            "secondColorSlow":"#0079b1",
            "secondColorSuperSlow":"#01a9f7",
            "thirdColor":"#07265c"
        }
    }



