from NodoProces import *
c = []
class simpleproce():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def ingresar(self,paso):
        nuevo = nodoproces(paso)
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
            print("Mama esto no jala")
        else:
            while aux is not None:
                b = (aux.paso)
                aux = aux.siguiente 
            return(b)        
    
    def Limpiar(Self):
        aux = Self.primero
        if aux is None:
            print("Lista limpia")
        else:
            while aux is not None:
                Self.primero = aux.siguiente
                
                aux = None 