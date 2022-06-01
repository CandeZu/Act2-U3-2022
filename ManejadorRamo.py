class ManejadorRamo:
    __listaRamos = None

    def __init__(self):
        self.__listaRamos = []
    
    def AgregarRamo(self, unRamo):
        self.__listaRamos.append(unRamo)
    
    def Listar(self):
        for unRamo in self.__listaRamos:
            print(unRamo)
    
    