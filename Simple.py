from nodo import *
class simple():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def ingresar(self,pro,elaboracion):
        nuevo = nodo(pro,elaboracion)
        if self.primero is None:
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo
    
    def Agregar(self):
        aux = self.primero
        if aux is None:
            print()
        else:
            while aux is not None:
                b = (aux.pro)
                aux = aux.siguiente 
                return(b)