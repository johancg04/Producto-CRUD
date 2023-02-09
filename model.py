from entity import *
from io import open
from os.path import exists
from os import remove, rename


class ProductoFile:
    # construir
    def __init__(self):
        self.__archivo = 'Productos.txt'
        self.__temporal = 'Temporal.txt'
        if not exists(self.__archivo):
            fichero = open(self.__archivo, 'w')
            fichero.close()
            print('Archivo creado con exito')
    # persistencia

    def adicionar(self, produ):
        fichero = None
        sw = False
        try:
            fichero = open(self.__archivo, 'a')
            datos = produ.codigo+'#'+produ.nombre+'#'+produ.categoria + \
                '#'+str(produ.precio)+'#'+str(produ.cantidad)+'\n'
            # validar codigo de produ
            produ = self.buscar(produ.codigo)
            if produ == None:
                fichero.write(datos)
            else:
                sw = True
        except IOError as e:
            print('Error :', e)
        finally:
            fichero.close()
        return sw

    def listar(self):
        fichero = None
        productos = []
        try:
            fichero = open(self.__archivo, 'r', encoding='utf8')
            lineas = fichero.readlines()
            for linea in lineas:
                campos = linea.replace('\n', '').split('#')
                producto = {'codigo': campos[0], 'nombre': campos[1],
                            'categoria': campos[2], 'precio': campos[3], 'cantidad': campos[4]}
                productos.append(producto)
        except IOError as e:
            print('Error :', e)
        finally:
            fichero.close()
        return productos

    def buscar(self, id):
        fichero = None
        producto = None
        try:
            fichero = open(self.__archivo, 'r', encoding='utf8')
            lineas = fichero.readlines()
            for linea in lineas:
                campos = linea.split('#')
                cod = campos[0]
                if cod == id:
                    producto = campos
                    break
        except IOError as e:
            print('Error :', e)
        finally:
            fichero.close()
        return producto

    def actualizar(self, produ):
        fuente = None
        destino = None
        try:
            fuente = open(self.__archivo, "r", encoding="utf8")
            destino = open(self.__temporal, "w", encoding="utf8")
            lineas = fuente.readlines()
            separador = "#"
            for linea in lineas:
                dato = linea.split(separador)
                if dato[0] == produ.codigo:
                    datos = produ.codigo+"#"+produ.nombre+"#"+produ.categoria + \
                        '#'+str(produ.precio)+'#'+str(produ.cantidad)+'\n'
                    destino.write(datos)
                else:
                    destino.write(linea)
        except IOError as e:
            print("Error : ", e)
        finally:
            fuente.close()
            destino.close()
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)

    def eliminar(self, produ):
        fuente = None
        destino = None
        try:
            fuente = open(self.__archivo, "r", encoding="utf8")
            destino = open(self.__temporal, "w", encoding="utf8")
            lineas = fuente.readlines()
            separador = "#"
            for linea in lineas:
                dato = linea.split(separador)
                if dato[0] == produ.codigo:
                    pass
                else:
                    destino.write(linea)
        except IOError as e:
            print("Error : ", e)
        finally:
            fuente.close()
            destino.close()
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)
