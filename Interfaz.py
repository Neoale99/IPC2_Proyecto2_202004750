# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 571))
        self.label.setAutoFillBackground(False)
        pixmap = QPixmap('fondo.jpg')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 251, 571))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        pixmap = QPixmap('barrita.jpg')
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 141, 16))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 251, 561))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(30, 25, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-image: url( boton.jpg);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 70, 121, 22))
        self.comboBox.setAutoFillBackground(True)
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-image: url(boton.jpg);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 121, 221))
        self.label_6.setAutoFillBackground(True)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 60, 291, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 21))
        self.menubar.setObjectName("menubar")
        self.menuCargar = QtWidgets.QMenu(self.menubar)
        self.menuCargar.setObjectName("menuCargar")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfiguraci_n = QtWidgets.QAction(MainWindow)
        self.actionConfiguraci_n.setObjectName("actionConfiguraci_n")
        self.actionReporte_simulaciones = QtWidgets.QAction(MainWindow)
        self.actionReporte_simulaciones.setObjectName("actionReporte_simulaciones")
        self.actionSimulacion = QtWidgets.QAction(MainWindow)
        self.actionSimulacion.setObjectName("actionSimulacion")
        self.action_Que_busca_buen_hombre = QtWidgets.QAction(MainWindow)
        self.action_Que_busca_buen_hombre.setObjectName("action_Que_busca_buen_hombre")
        self.menuCargar.addAction(self.actionConfiguraci_n)
        self.menuCargar.addAction(self.actionSimulacion)
        self.menuReportes.addAction(self.actionReporte_simulaciones)
        self.menuAyuda.addAction(self.action_Que_busca_buen_hombre)
        self.menubar.addAction(self.menuCargar.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.label_6.setWordWrap(True)
        self.retranslateUi(MainWindow)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Datos")
        self.msg.setText("""   ╔ Datos del estudiante:
   ║ Nombre: Pedro Alejandro Zetino Páez                          
   ║ Edad: 19                                                     
   ║ Carnet: 202004750                                                
   ║ Aflicción: No he ganado inter 1                                   
   ║ ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠
   ╠ Datos de la aplicación: 
   ║ Esta aplicación fue desarrollada para                   
   ║ manejar la máquina ensambladora creada                   
   ║ por Digital Intelligence, S.A y lograr                   
   ║ un manejo eficiente de la misma                          
   
        """)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Producto"))
        self.label_5.setText(_translate("MainWindow", "Componentes"))
        self.pushButton.setText(_translate("MainWindow", "Seleccionar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Procesos"))
        self.menuCargar.setTitle(_translate("MainWindow", "Cargar"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionConfiguraci_n.setText(_translate("MainWindow", "Configuracion"))
        self.actionReporte_simulaciones.setText(_translate("MainWindow", "Reporte simulaciones"))
        self.actionSimulacion.setText(_translate("MainWindow", "Simulacion"))
        self.action_Que_busca_buen_hombre.setText(_translate("MainWindow", "┬┐Que busca buen hombre? "))

