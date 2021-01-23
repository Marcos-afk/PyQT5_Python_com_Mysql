from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from reportlab.pdfgen import canvas
import os, sys

from  Ui_Agenda_Tela_Principal import Ui_Principal
from Ui_Agenda_Tela_Adicao import Ui_Adicao
from Ui_Agenda_Tela_Edicao import Ui_Edicao
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "agenda"
)

class Tela_Principal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_Principal, self).__init__(*args, **argvs)
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.ui.AdicionarB.clicked.connect(self.Chamar_tela_adicao)
        self.ui.PesquisarB.clicked.connect(self.Pesquisar)
        self.ui.ExcluirB.clicked.connect(self.Excluir)
        self.ui.EditarB.clicked.connect(self.Chamar_tela_edicao)
        self.Preencher()
        
    

    def Chamar_tela_adicao(self):
        self.tela = Tela_Adicao()
        self.tela.show()
        self.close()


    def Chamar_tela_edicao(self):
        self.tela = Tela_Edicao()
        self.tela.show()
        self.close()
    
    def Excluir(self):
        linha = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(linha)
        Cursor = banco.cursor()
        try:
            Cursor.execute("SELECT codigo FROM compromissos")
            Dados_Lidos = Cursor.fetchall()
            Id = Dados_Lidos[linha][0]
            Cursor.execute("DELETE FROM compromissos WHERE codigo = " + str(Id))
            banco.commit()
            QMessageBox.about(self, "Sucesso", "Cliente excluido com sucesso!")
            self.Preencher()
        except:
            QMessageBox.about(self, "Erro", "Ocorreu uma exceção!")


    def Preencher(self):
        Cursor = banco.cursor()
        try:
            Comando_Sql = "SELECT * FROM compromissos"
            Cursor.execute(Comando_Sql)
            Dados_Lidos = Cursor.fetchall() 
            self.ui.tableWidget.setRowCount(len(Dados_Lidos))
            self.ui.tableWidget.setColumnCount(4)

            for x in range(0, len(Dados_Lidos)):
                for y in range(0,4):
                    self.ui.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(Dados_Lidos[x][y])))
                
            banco.commit()
        except:
             QMessageBox.about(self, "Erro", "Ocorreu uma exceção!")
    

    def Pesquisar(self):
        if self.ui.PesquisarL.text() != "":
            assunto = self.ui.PesquisarL.text()
            Cursor = banco.cursor()
            try:
                Cursor.execute("SELECT * FROM compromissos WHERE  assunto LIKE '%{}%'" .format(assunto))
                Dados_Lidos = Cursor.fetchall() 
                self.ui.tableWidget.setRowCount(len(Dados_Lidos))
                self.ui.tableWidget.setColumnCount(4)

                for x in range(0, len(Dados_Lidos)):
                    for y in range(0,4):
                        self.ui.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(Dados_Lidos[x][y])))
                
                banco.commit()
            except:
                QMessageBox.about(self,'Erro','Ocorreu uma exceção!')
        else:
             QMessageBox.about(self,'Erro','caixa de pesquisa vázia!')
             self.Preencher()
    

    




class Tela_Adicao(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_Adicao, self).__init__(*args, **argvs)
        self.ui = Ui_Adicao()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Salvar)
        self.ui.VoltarB.clicked.connect(self.Chamar_tela)
    

    def Salvar(self):
        if self.ui.AssuntoL.text()!= "":
            assunto = self.ui.AssuntoL.text()
            data = self.ui.DataL.text()
            Cursor = banco.cursor()
            try:
                Comando_Sql = "INSERT INTO compromissos VALUES (default, default, %s,%s )" 
                dados = (str(data),str(assunto))
                Cursor.execute(Comando_Sql, dados) 
                banco.commit()
                self.ui.DataL.setText("2020/01/01")
                self.ui.AssuntoL.setText("")
                QMessageBox.about(self, "Sucesso", "Compromisso adicionado com sucesso!")
            except:
                QMessageBox.about(self, "Erro", "Ocorreu uma exceção!")
        else:
            QMessageBox.about(self , "Erro","Preencha os campos obrigatorios!")

    def Chamar_tela(self):
        self.tela = Tela_Principal()
        self.tela.show()
        self.close()
    

class Tela_Edicao(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_Edicao, self).__init__(*args, **argvs)
        self.ui = Ui_Edicao()
        self.ui.setupUi(self)
        self.ui.VoltarB.clicked.connect(self.Chamar_telaPrincipal)
        self.ui.PesquisarB_2.clicked.connect(self.Pesquisar_compromisso)
        self.ui.EditarB.clicked.connect(self.Editar_compromisso)

    def Chamar_telaPrincipal(self):
        self.tela = Tela_Principal()
        self.tela.show()
        self.close()

    def Pesquisar_compromisso(self):
        if self.ui.PesquisarL_2.text()!= "":
            codigo = self.ui.PesquisarL_2.text()
            Cursor = banco.cursor()
            try:
                Comando_Sql = "SELECT * FROM  compromissos WHERE codigo  = " + str(codigo)
                Cursor.execute(Comando_Sql)
                Dados_Lidos = Cursor.fetchall()

                if len(Dados_Lidos) == 0:
                      QMessageBox.about(self , "Erro","Código de compromisso não existe no sistema")
                else:
                      for x in range(0,len(Dados_Lidos)):
                        self.ui.DataL.setText(str(Dados_Lidos[x][2]))
                        self.ui.AssuntoL_2.setText(str(Dados_Lidos[x][3]))
                  
                
                banco.commit()
            except:
                QMessageBox.about(self , "Erro","Ocorreu uma execeção")  
        else:
           QMessageBox.about(self , "Erro","Caixa de busca vázia")  

    def Editar_compromisso(self):
        if ((self.ui.AssuntoL_2.text()!="") and (self.ui.PesquisarL_2.text()!="")):
            assunto = self.ui.AssuntoL_2.text()
            nova_data = self.ui.DataL.text()
            codigo = self.ui.PesquisarL_2.text()
            Cursor = banco.cursor()
            try:
                Comando_Sql = "UPDATE compromissos SET assunto = %s, prazo = %s   WHERE codigo = " + str(codigo)
                dados = (str(assunto) , str(nova_data))
                Cursor.execute(Comando_Sql,dados)
                banco.commit()
                self.ui.AssuntoL_2.setText("")
                self.ui.DataL.setText("2000/01/01")
                QMessageBox.about(self , "Sucesso","Compromisso editado com sucesso")
            except:
                QMessageBox.about(self , "Erro","Ocorreu uma execeção")
        else:
            QMessageBox.about(self , "Erro","Não apague o código da barra de pesquisa/Assunto obrigatório")








app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = Tela_Principal()
    window.show()
sys.exit(app.exec_())


