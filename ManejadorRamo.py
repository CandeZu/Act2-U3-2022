from Ramo import Ramo
from ManejadorFlores import ManejadorFlores
import os
from typing import List
class ManejadorRamo:
    __ramosVendidos = None

    def __init__(self):
        self.__ramosVendidos = []
    
    def agregarRamo(self,ListaFlores):
        tamaño = input("Ingrese tamaño del ramo\n").capitalize()
        NuevoRamo = Ramo(tamaño)
        listadoFlores = ListaFlores.getLista()

        dato = int(input("Ingrese nro de flor que desea(0 para finalizar)\n"))
        os.system("cls")

        while (dato != 0):
            indice = ListaFlores.BuscarFlor(dato)
            if (indice != -1):
                cantidad = int(input("Ingrese cantidad que desea de esa flor\n"))
                for i in range(cantidad):
                    listadoFlores[indice].contarFlorPedida()
                    NuevaFlor = listadoFlores[indice]
                    NuevoRamo.AgregarFlor(NuevaFlor)
            else:
                print("Flor no encontrada")

            dato = int(input("Ingrese siguiente flor a agregar(0 para finaliar)\n"))
            os.system("cls")

        if isinstance(NuevoRamo,Ramo):
            NuevoRamo.mostrar()
            input("ENTER PARA CONTINUAR")
            os.system("cls")
            self.__ramosVendidos.append(NuevoRamo)
        else:
            print("{} no es un ramo".format(NuevoRamo))

        
    def porTamaño(self,tamañoPorTeclado):
        ant = None
        for ramo in self.__ramosVendidos:
            if(ramo.getTamaño() == tamañoPorTeclado.capitalize()):
                for flores in ramo.getLista():
                    if(ant != flores):
                        print("".center(20,"-"))
                        print(flores)
                        ant = flores
