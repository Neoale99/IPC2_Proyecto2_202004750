from os import error
from simplesim import simplesim
from PyQt5 import QtWidgets
from nodo import *
from NodoProces import*
from nodosim import *
from Simpleproce import *
from Simple import *
from nodoLineas import*
from Simplelineas import*
from Interfaz import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from os import startfile, system
import re as re 
import sys
import xml.etree.ElementTree as et  
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QMessageBox, QDialog
datos = ""
listasim = simplesim()
Listacomp = simple()
Listalin = simpleLineas()
Listaproc = simpleproce()
class ventana(QMainWindow):
    #Métodos
    def __init__(self):

        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show
        self.ui.actionConfiguraci_n.triggered.connect(self.abrirc)
        self.ui.actionSimulacion.triggered.connect(self.simular)
        self.ui.comboBox.currentIndexChanged.connect(self.elegir)
        self.ui.action_Que_busca_buen_hombre.triggered.connect(self.datos)
        self.ui.actionReporte_simulaciones.triggered.connect(self.graph)
    def abrirc(self):
        global datos
        ruta = QFileDialog.getOpenFileName(self,'abrir archivo','C:\\')
        tree = et.parse(ruta[0])
        root = tree.getroot()
        for elemento in root: 
            nombre = elemento.get('maquina')
            #print(Nodoterreno.nombre)
            
            
            for dim in elemento.iter('CantidadLineasProduccion'):
                cantidad = elemento.text.strip()
            for lptm in elemento.iter('ListadoLineasProduccion'):
                print()
            for lptm3 in elemento.iter('LineaProduccion'):
                
                for dim2 in lptm3.iter('Numero'):
                    Correlatif = dim2.text.strip()
                for dim2 in lptm3.iter('CantidadComponentes'):
                    cantcomp = dim2.text.strip()
                for dim2 in lptm3.iter('TiempoEnsamblaje'):
                    Tiempo = dim2.text.strip()
                Listalin.ingresar(cantidad,Correlatif,cantcomp,Tiempo)
                
            for lptm2 in elemento.iter('ListadoProductos'):
                print("")
            for lptm4 in elemento.iter('Producto'):
                cantidad = lptm4.text.strip()
                for dim3 in lptm4.iter('nombre'):
                    nomme = dim3.text.strip()
                for dim3 in lptm4.iter('elaboracion'):
                    elab = dim3.text.strip()
                Listacomp.ingresar(nomme,elab)     

                   
        self.ui.comboBox.addItems(Listacomp.Agregar())                    
 
    def elegir(self):
        comp = Listacomp.Comparar(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))
        self.ui.label_6.setText(comp)
    
    def datos(self):
        self.ui.msg.exec_()

    def graph(self):
        comp = Listacomp.Comparar(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))
        x = comp.replace("p","")
  
        separar = re.compile("L[0-9]+C[0-9]+")
        
        paso = separar.search(x)
        i = 0
        b = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        a = b.replace(" ","")

        print(a)
        graphviz='''
        digraph L{
        node[shape=cylinder fillcolor="#FFEDBB" style =filled]
    
        subgraph cluster_p{
        fontsize = 50
        label= " '''+a+''' "
        bgcolor = "lavender"
        edge[dir = "one"]


        '''
        try:
            for i in  range(len(x)):
                
                if paso.group() != None:
                    i +=1
                    paso = separar.search(x)
                    si = paso.group()
                    x = x.replace(si,"")
                    Listaproc.ingresar(si)
                
                graphviz +="nodo1_"+str(i)+"[label= "+Listaproc.Agregar()+",fillcolor=cyan,group=1]\n"
                
        except:
            print()  

        graphviz +=  "{rank=same;"
        u = 0
        while u<i-1:
            u += 1
            if u == i-1:
                
                graphviz += "nodo1_"+str(u)+"}"
                
            else: 
                  
                graphviz+="nodo1_"+str(u)+"->"
                
                
        
        graphi = """
                   
            }

        }
        """
        graphviz += "\n"+graphi
        f= open(''+a+'.dot','w')
        f.write(graphviz)
        f.close()
        system('dot -Tpng '+a+'.dot -o '+a+'.png')
        system('cd ./'+a+'.png')
        startfile(''+a+'.png')
    
    def simular(self):

        ruta = QFileDialog.getOpenFileName(self,'abrir archivo','C:\\')
        tree = et.parse(ruta[0])
        root = tree.getroot()
        for elemento in root: 
            nombre = elemento.get('maquina')
            #print(Nodoterreno.nombre)
            
            
            for dim in elemento.iter('Nombre'):
                cantidad = dim.text.replace(" ","")
            for lptm in elemento.iter('ListadoProductos'):
                simuladores = lptm.text.replace(" ","")
                for prr in lptm.iter('Producto'):
                    prod = prr.text.replace(" ","")
                    listasim.ingresar(cantidad.strip(),prod.strip())

if __name__ == "__main__":

    app=QApplication(sys.argv)
    GUI=ventana()
    GUI.show()
    sys.exit(app.exec_())