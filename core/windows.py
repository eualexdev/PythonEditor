import os,sys

from src.configs.files import Files
from src.configs.direct import Direct

class WindowsClass:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def Install():
        if not Files.Exists("Public"):
            print("O comando foi adicionado na variavel de ambiente")
        else:
            print("Já foi instalado")