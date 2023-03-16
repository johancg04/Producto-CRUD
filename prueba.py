from controller import *
from entity import *


class Prueba:
    produ = Producto("P009", "Armario", 'Hogar', 12.0, 3)
    controller = ProductoController()
    message = controller.procesarProducto(produ, ADD)
    print(message)


# ejecutar prueba
p = Prueba()
