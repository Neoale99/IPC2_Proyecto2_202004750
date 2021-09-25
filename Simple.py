from nodo import *
c = []
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
            print("Mama esto no jala")
        else:
            while aux is not None:
                b = (aux.pro)
                c.append(b)
                aux = aux.siguiente 
        return(c)        
    
    def Comparar(self,nombre):
        aux = self.primero

        if aux is None:
            print("Mama esto no jala")
            return(None)
        else:
            while aux is not None:
                if aux.pro == nombre:
                    print(aux.elaboracion)
                    c = aux.elaboracion
                    
                    return(c)
                else : 
                    aux = aux.siguiente
                
                        