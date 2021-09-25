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
        self.ui.comboBox.addItem(Listacomp.Agregar())
    
    def abrirc(self):
        global datos
        ruta = QFileDialog.getOpenFileName(self,'abrir archivo','C:\\')
        print(ruta)
        tree = et.parse(ruta[0])
        root = tree.getroot()
        for elemento in root: 
            nombre = elemento.get('nombre')
            for dim in elemento.iter('CantidadLineasProducción'):
                cantidad = dim.text
                for Lis in elemento.iter('ListadoLineasProduccion'):
                    for Lineas in Lis.iter('LineaProduccion'):
                        for cor in Lineas.iter('Numero'):
                            Correlatif = cor.text
                    
                        for cant in Lineas.iter('CantidadComponentes'):
                            cantcomp = cant.text

                        for TiE in Lineas.iter('TiempoEnsamblaje'):
                            Tiempo = TiE.text

                for Lisp in elemento.iter('ListadoProductos'):

                    for Pr in Lisp.iter('Producto'):

                        for nom in Pr.iter('nombre'):
                            nomme = nom.text

                        for cant in Pr.iter('elaboracion'):
                            elab = cant.text
            Listacomp.Agregar(nomme,elab)
            Listalin.Agregar(cantidad,Correlatif,cantcomp,Tiempo)
    


if __name__ == "__main__":

    app=QApplication(sys.argv)
    GUI=ventana()
    GUI.show()
    sys.exit(app.exec_())