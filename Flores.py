class Flores:
    __numero = 0
    __nombre = ""
    __color = ""
    __descripcion = ""

    def __init__(self, numero, nombre, color, descripcion):
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion

    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color
    
    def getDescripcion(self):
        return self.__descripcion
    
    def __str__(self):
        return "Numero: " + self.__numero + " Nombre: " + self.__nombre + " Color: " + self.__color + " Descripcion: " + self.__descripcion
    
