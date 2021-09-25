from os import error
from PyQt5 import QtWidgets
from nodo import *
from Simple import *
from nodoLineas import*
from Simplelineas import*
from Interfaz import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from os import startfile
import sys
import xml.etree.ElementTree as et  
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QMessageBox, QDialog
datos = ""
Listacomp = simple()
Listalin = simpleLineas()

class ventana(QMainWindow):
    #Métodos
    def __init__(self):

        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show
        self.ui.actionConfiguraci_n.triggered.connect(self.abrirc)
        self.ui.comboBox.currentIndexChanged.connect(self.elegir)
        self.ui.action_Que_busca_buen_hombre.triggered.connect(self.datos)
    
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

if __name__ == "__main__":

    app=QApplication(sys.argv)
    GUI=ventana()
    GUI.show()
    sys.exit(app.exec_())