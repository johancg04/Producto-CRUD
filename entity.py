# clase para definir los productos
class Producto:
    # Construccion
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad
    # prop.lectura

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__categoria

    @property
    def precio(self):
        return self.__precio

    @property
    def cantidad(self):
        return self.__cantidad

    # prop.asignacion
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
