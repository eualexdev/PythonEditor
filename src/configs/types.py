class Package:
    apiURlImg:str = "https://elegant-ide-api.netlify.app/img/"
    dataLocal:str = "./Public/data"
    jsonLocal:str = "./Public/json"
    editorThemeLocal:str = "./Public/Editor/Themes"
    editorAssetsLocal:str = "./Public/Editor/Assets"
    editorLangsLocal:str = "./Public/Editor/Language"
    

class Data:

    jsonConfigs:dict = {
        "version":"1.0.0",
        "theme":"light",
        "animationDelay":200,
        "menuVelocity":4,
        "lang":"pt-br"
    }

    jsonThemeLight:dict = {
        "IdeColor":{
            "outherColor":"#fff",
            "firstColor":"#fff",
            "secondColorSuperPlus":"#005f8b",
            "secondColorPlus":"#0274a8",
            "secondColor":"#0282be",
            "secondColorSlow":"#0290d3",
            "secondColorSuperSlow":"#02afff",
            "thirdColor":"#1E488F"
        }   
    }
    
    jsonThemeDark:dict ={
        "IdeColor":{
            "outherColor":"#fff",
            "firstColor":"#11161d",
            "secondColorSuperPlus":"#004666",
            "secondColorPlus":"#025981",
            "secondColor":"#006b9c",
            "secondColorSlow":"#0079b1",
            "secondColorSuperSlow":"#01a9f7",
            "thirdColor":"#07265c"
        }
    }



