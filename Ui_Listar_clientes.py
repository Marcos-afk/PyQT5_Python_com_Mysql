# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Marcos André\Documents\Programas em python\Aplicações Python\Pyqt5 aplicações\Listar_clientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Listar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 592)
        MainWindow.setStyleSheet("background-color: rgb(0, 167, 81);\n"
"font: 75 14pt \"Times New Roman\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 221, 41))
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 591, 371))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.ExcluirB = QtWidgets.QPushButton(self.centralwidget)
        self.ExcluirB.setGeometry(QtCore.QRect(370, 440, 111, 31))
        self.ExcluirB.setStyleSheet("background-color: rgb(171, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ExcluirB.setObjectName("ExcluirB")
        self.AtualizarB = QtWidgets.QPushButton(self.centralwidget)
        self.AtualizarB.setGeometry(QtCore.QRect(240, 440, 121, 31))
        self.AtualizarB.setStyleSheet("background-color: rgb(0, 53, 159);\n"
"color: rgb(255, 255, 255);")
        self.AtualizarB.setObjectName("AtualizarB")
        self.SalvarB = QtWidgets.QPushButton(self.centralwidget)
        self.SalvarB.setGeometry(QtCore.QRect(490, 440, 131, 31))
        self.SalvarB.setStyleSheet("background-color: rgb(167, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.SalvarB.setObjectName("SalvarB")
        self.PesquisarB = QtWidgets.QPushButton(self.centralwidget)
        self.PesquisarB.setGeometry(QtCore.QRect(190, 510, 101, 31))
        self.PesquisarB.setStyleSheet("background-color: rgb(0, 179, 179);\n"
"color: rgb(255, 255, 255);")
        self.PesquisarB.setObjectName("PesquisarB")
        self.PesquisarL = QtWidgets.QLineEdit(self.centralwidget)
        self.PesquisarL.setGeometry(QtCore.QRect(20, 510, 151, 31))
        self.PesquisarL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PesquisarL.setObjectName("PesquisarL")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 480, 241, 20))
        self.label_2.setStyleSheet("font: 75 italic 9pt \"Times New Roman\";\n"
"background-color: rgb(111, 111, 166);")
        self.label_2.setObjectName("label_2")
        self.PesquisarB_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PesquisarB_2.setGeometry(QtCore.QRect(300, 510, 131, 31))
        self.PesquisarB_2.setStyleSheet("background-color: rgb(0, 179, 179);\n"
"color: rgb(255, 255, 255);")
        self.PesquisarB_2.setObjectName("PesquisarB_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Lista de clientes no sistema"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DESCRIÇÃO"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SALÁRIO"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "LOJA"))
        self.ExcluirB.setText(_translate("MainWindow", "Excluir"))
        self.AtualizarB.setText(_translate("MainWindow", "Atualizar"))
        self.SalvarB.setText(_translate("MainWindow", "Salvar em  PDF"))
        self.PesquisarB.setText(_translate("MainWindow", "Pesquisar"))
        self.label_2.setText(_translate("MainWindow", "*Digite o nome do Usuário que deseja encontrar"))
        self.PesquisarB_2.setText(_translate("MainWindow", "Mostrar Todos"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Listar()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())