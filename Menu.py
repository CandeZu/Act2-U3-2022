import os
from ManejadorFlores import ManejadorFlores
from Flores import Flores
from Ramo import Ramo
from ManejadorRamo import ManejadorRamo

class Menu:
    __flores = None
    __ramo = None
    __op = 0

    def __init__(self, op= 0):
        self.__op = op
        self.__flores = ManejadorFlores()
        self.__ramo = ManejadorRamo()


    def opciones(self):
            os.system("cls")
            continuar = True


            while continuar:
                print("[1] Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que se pondrán en el ramo.")
                print("[2] Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.")
                print("[3] Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.")
                print("[0] Para salir del menu")
                self.__op = int(input("INGRESE OPCION\n"))
                os.system("cls")

                if(self.__op == 1):
                    print("Seleccione la flor que desea agregar al ramo")
                    flor = input(flor)
    
                elif(self.__op ==2):

        
                elif(self.__op ==3):

                elif(self.__op == 0):
                    continuar = not continuar
                    print("PROGRAMA FINALIZADO")
                else: 
                    print("Opcion incorrecta, ingrese nuevamente")