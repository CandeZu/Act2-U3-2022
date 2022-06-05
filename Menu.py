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
            self.__flores.Carga()

            while continuar:
                print("[1] Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que se pondrán en el ramo.")
                print("[2] Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.")
                print("[3] Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.")
                print("[0] Para salir del menu")
                self.__op = int(input("INGRESE OPCION\n"))
                os.system("cls")

                if(self.__op == 1):
                    # codigo = int(input("Ingrese el codigo de la flor: "))
                    # v = self.__flores.BuscarFlor(codigo)
                    # if(v == -1):
                    #     print("No existe la flor")
                    # else:
                    #     tamanio = input("Ingrese el tamaño del ramo: ")
                    #     while (codigo != -1):
                    #         print("Ingrese cantidad de flores a agregar: ")
                    #         cantidad = int(input())
                        
                    #         r = Ramo(tamanio)
                    #         for i in range(cantidad):
                    #             r.AgregarFlor(v)
                    #         codigo = int(input("Ingrese el codigo de la flor: "))

                    #     self.__ramo.AgregarRamo(r)
                    #     print("Ramo agregado")
    
                    self.__ramo.agregarRamo(self.__flores)
                elif(self.__op ==2):
                    self.__flores.MostrarModaFlores()
        
                elif(self.__op ==3):
                    ramo = input("Ingrese el tamaño del ramo: ")
                    self.__ramo.porTamaño(ramo)

                elif(self.__op == 0):
                    continuar = not continuar
                    print("PROGRAMA FINALIZADO")
                else: 
                    print("Opcion incorrecta, ingrese nuevamente")