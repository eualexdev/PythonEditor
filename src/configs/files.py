from src.configs.types import Package,void

class Files():
    @staticmethod 
    def Create(filename):
        try:
            fs = open(filename,"rt",encoding="utf-8")
            print(filename+" - Já Existe")
        except:
            fs = open(filename,"wt+",encoding="utf-8")
            print(filename+" - Created")
    
    @staticmethod 
    def Write(filename,code):
        Files.Create(filename)
        fs = open(filename,"at",encoding="utf-8")
        fs.write(code)
        print(filename+" - Writed")
    
    @staticmethod    
    def Clear(filename,code=""):
        Files.Create(filename)
        fs = open(filename,"wt+",encoding="utf-8").write(code)
        print(filename+" - Clear")

    @staticmethod
    def Read(filename):
        Files.Create(filename)
        fs = open(filename,"rt",encoding="utf-8")
        print(filename+" - Readed")
        return fs.read()

    @staticmethod    
    def isPrymaryExecutation(func) -> void:
        Files.Create(Package.dataLocal+"/data.txt")
        if(Files.Read(Package.dataLocal+"/data.txt") == ""):
            func()
            Files.Write(Package.dataLocal+"/data.txt","#include <stades>")