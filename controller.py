from model import *
from entity import *
from util import *


class ProductoController:
    def __init__(self):
        self.__obj = ProductoFile()

    def listaProductos(self):
        return self.__obj.listar()

    def buscarProducto(self, id):
        return self.__obj.buscar(id)

    def procesarProducto(self, produ, opcion):
        self.__msg = None
        if opcion == ADD:
            ok = self.__obj.adicionar(produ)
            if ok == False:
                self.__msg = "Producto registrado con exito"
            else:
                self.__msg = "Codigo de producto existente"
        if opcion == UPD:
            self.__obj.actualizar(produ)
            self.__msg = "Producto actualizado con exito"
        if opcion == DEL:
            self.__obj.eliminar(produ)
            self.__msg = "Producto eliminado con exito"
        return self.__msg
