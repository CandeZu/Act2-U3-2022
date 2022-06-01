from Flores import Flores
import numpy as np
import csv

class ManejadorFlores:
    __flores = None
    __dimension = 0
    __cantidad = 0
    __incremento = 1

    def __init__(self, dimension=1, cantidad=0, incremento=1):
        self.__flores = np.empty(dimension, dtype=Flores)
        self.__dimension = dimension
        self.__cantidad = cantidad
        self.__incremento = incremento
    

    def agregarFlor(self, unaFlor:Flores):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__flores = self.__flores.resize(self.__dimension, refcheck=False)
        self.__flores[self.__cantidad] = unaFlor
        self.__cantidad += 1

    def Carga(self):
        archivo = open("flores.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            unaFlor = Flores(self.__cantidad + 1, fila[0], fila[1], fila[2])
            self.agregarFlor(unaFlor)
        archivo.close()

    def Listar(self):
        cadena = "{}{}{}\n".format("Numero", "Nombre", "Color")

        for i in range(self.__cantidad):
            cadena += "{}{}{}\n".format(self.__flores[i].getNumero(), self.__flores[i].getNombre(), self.__flores[i].getColor())
    
    def getFlor(self, indice):
        return self.__flores[indice]
    
    def BuscarFlor(self, codigo):
        i=0
        band = False
        while i < self.__cantidad and not band:
            if self.__flores[i].getNumero() == codigo:
                band = True
            else:
                i += 1
        if not band:
            i = -1
        return i