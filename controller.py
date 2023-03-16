from model import *
from entity import *
from util import *


class ProductoController:
    def __init__(self):
        self.__prodFile = ProductoFile()

    def listaProductos(self):
        return self.__prodFile.listar()

    def buscarProducto(self, id):
        return self.__prodFile.buscar(id)

    def procesarProducto(self, produ, opcion):
        if opcion == ADD:
            ok = self.__prodFile.adicionar(produ)
            if ok == False:
                return "Producto registrado con exito"
            else:
                return "Codigo de producto existente"
        if opcion == UPD:
            self.__prodFile.actualizar(produ)
            return "Producto actualizado con exito"
        if opcion == DEL:
            self.__prodFile.eliminar(produ)
            return "Producto eliminado con exito"
