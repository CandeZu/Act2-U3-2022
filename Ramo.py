from ManejadorFlores import ManejadorFlores
from Flores import Flores
class Ramo:
    __tamanio = ''
    __flores =  None
    
    def __init__(self, tamanio):
        self.__tamanio = tamanio
        self.__flores = ManejadorFlores()
        
    def getTamanio(self):
        return self.__tamanio
    
    def AgregarFlor(self, unaFlor):
        self.__flores.agregarFlor(unaFlor)
    
    def __str__(self):
        return "Tamaño: " + self.__tamanio + " Flores: " + self.__flores

    def mostrar(self):
        print("Tamaño:{}".format(self.__tamanio.capitalize()))
        for flor in self.__flores:
            print("".center(20,"-"))
            print(flor)

def getCantFloresNumero(self, numero) ->int:
        cont = 0
        for unaFlor in self.__flores:
            if unaFlor.getNumero() == numero:
                cont += 1
        return cont