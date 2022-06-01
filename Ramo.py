from ManejadorFlores import ManejadorFlores
from Flores import Flores
class Ramo:
    __tamanio = 0
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


