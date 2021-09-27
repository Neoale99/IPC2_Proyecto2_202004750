from nodosim import *
c = []
class simplesim():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def ingresar(self,nombre,pro):
        nuevo = nodosimulación(nombre,pro)
        if self.primero is None:
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo