# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Marcos André\Documents\Programas em python\Aplicações Python\Pyqt5 aplicações\Agenda_Tela_Adicao.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Adicao(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 572)
        MainWindow.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"background-color: rgb(0, 117, 175);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AssuntoL = QtWidgets.QLineEdit(self.centralwidget)
        self.AssuntoL.setGeometry(QtCore.QRect(260, 140, 201, 31))
        self.AssuntoL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AssuntoL.setObjectName("AssuntoL")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 140, 141, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 141, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 420, 141, 31))
        self.pushButton.setStyleSheet("background-color: rgb(52, 156, 76);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 151, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.VoltarB = QtWidgets.QPushButton(self.centralwidget)
        self.VoltarB.setGeometry(QtCore.QRect(300, 420, 141, 31))
        self.VoltarB.setStyleSheet("background-color: rgb(52, 156, 76);")
        self.VoltarB.setObjectName("VoltarB")
        self.DataL = QtWidgets.QLineEdit(self.centralwidget)
        self.DataL.setGeometry(QtCore.QRect(260, 180, 201, 31))
        self.DataL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DataL.setObjectName("DataL")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Assunto:"))
        self.label_2.setText(_translate("MainWindow", "Prazo:"))
        self.pushButton.setText(_translate("MainWindow", "Salvar"))
        self.label_3.setText(_translate("MainWindow", "Adicionar compromisso"))
        self.VoltarB.setText(_translate("MainWindow", "Voltar"))
        self.DataL.setText(_translate("MainWindow", "2000/01/01"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Adicao()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())