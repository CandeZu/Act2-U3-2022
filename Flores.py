class Flores:
    __numero = 0
    __nombre = ""
    __color = ""
    __descripcion = ""
    __cantidadPedida = 0

    def __init__(self, numero, nombre, color, descripcion, cantidadPedida=0):
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion
        self.__cantidadPedida = cantidadPedida
    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color
    
    def getDescripcion(self):
        return self.__descripcion
    
    def __str__(self):
        return ("Flor nro {}:\nNombre:{}\nColor:{}\nDescripcion:{}".format(self.__numero,self.__nombre,self.__color,self.__descripcion))
    
    def contarFlorPedida(self):
        self.__cantidadPedida += 1
    
    def getCantidadPedida(self):
        return self.__cantidadPedida
    
    def __gt__(self,otro):
        return self.__cantidadPedida< otro.getCantidadPedida()