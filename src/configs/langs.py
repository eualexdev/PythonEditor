from src.configs.funcs import ReadConfigs

def GetLang():
    lang = ReadConfigs()["lang"]
    if lang in {"pt-br","en-es"}:
        if lang == "pt-br":
            return Languages.pt_br
        elif lang == "en-es":
            return Languages.en_es
    else:
        return Languages.en_es

class Languages:
    pt_br = {
        "type":"pt-br",
        "Menu":{
            "Configs":{
                "ConfigureMenu":"Menu De Configurações"
            },
            "Menu":{
                "Configuration":"Configurações"
            }
        }
    }

    en_es = {
        "type":"en-es",
        "Menu":{
            "Configs":{
                "ConfigureMenu":"Configuration Menu"
            },
            "Menu":{
                "Configuration":"Configuration"
            }
        }
    }