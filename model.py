from entity import *
from io import open
from os.path import exists
from os import remove, rename

# clase producto file


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
        added = False
        try:
            fichero = open(self.__archivo, 'a')
            datos = produ.codigo+'#'+produ.nombre+'#'+produ.categoria + \
                '#'+str(produ.precio)+'#'+str(produ.cantidad)+'\n'
            # validar codigo de produ
            produ = self.buscar(produ.codigo)
            if produ == None:
                fichero.write(datos)
                added = True
        except IOError as e:
            print('Error :', e)
        finally:
            fichero.close()
        return added

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
        archivo_fuente = None
        archivo_destino = None
        try:
            archivo_fuente = open(self.__archivo, "r", encoding="utf8")
            archivo_destino = open(self.__temporal, "w", encoding="utf8")
            lineas_fuente = archivo_fuente.readlines()
            separador = "#"
            for linea_fuente in lineas_fuente:
                datos = linea_fuente.split(separador)
                if datos[0] == produ.codigo:
                    nueva_linea = produ.codigo+"#"+produ.nombre+"#"+produ.categoria + \
                        '#'+str(produ.precio)+'#'+str(produ.cantidad)+'\n'
                    archivo_destino.write(nueva_linea)
                else:
                    archivo_destino.write(linea_fuente)
        except IOError as e:
            print("Error : ", e)
        finally:
            archivo_fuente.close()
            archivo_destino.close()
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)

    def eliminar(self, produ):
        archivo_fuente = None
        archivo_destino = None
        try:
            archivo_fuente = open(self.__archivo, "r", encoding="utf8")
            archivo_destino = open(self.__temporal, "w", encoding="utf8")
            lineas_fuente = archivo_fuente.readlines()
            separador = "#"
            for linea_fuente in lineas_fuente:
                dato = linea_fuente.split(separador)
                if dato[0] == produ.codigo:
                    pass
                else:
                    archivo_destino.write(linea_fuente)
        except IOError as e:
            print("Error : ", e)
        finally:
            archivo_fuente.close()
            archivo_destino.close()
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)

# FIN MODEL.PY
