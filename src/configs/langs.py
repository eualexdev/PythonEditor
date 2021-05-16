from src.configs.funcs import ReadConfigs

def GetLang():
    lang = ReadConfigs()["lang"]
    if lang in {"pt-br","en-es"}:
        if lang == "pt-br":
            return Languages.pt_br
        elif lang == "en-eua":
            return Languages.en_eua
    else:
        return Languages.en_eua

class Languages:
    pt_br = {
        "type":"pt-br",
        "Menu":{
            "MenuText":"Menu",
            "Configs":{
                "ConfigureMenu":"Menu De Configurações",
                "ThemeButton":"Muda o Tema"
            },
            "Menu":{
                "CreateProjects":"Cria Projeto",
                "Configuration":"Configurações"
            }
        }
    }

    en_eua = {
        "type":"en-eua",
        "Menu":{
            "MenuText":"Box Menu",
            "Configs":{
                "ConfigureMenu":"Configuration Menu",
                "ThemeButton":"Change the Theme"
            },
            "Menu":{
                "CreateProjects":"Create Project",
                "Configuration":"Configuration"
            }
        }
    }