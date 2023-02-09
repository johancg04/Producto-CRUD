from controller import *
from entity import *


class Prueba:
    produ = Producto("P001", "Armario", 'Hogar', 12.0, 3)
    obj = ProductoController()
    msg = obj.procesarProducto(produ, 1)
    print(msg)


# prueba
p = Prueba()
