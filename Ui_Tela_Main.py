from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from reportlab.pdfgen import canvas
import os, sys

from Ui_Cadastro_Clientes import Ui_MainWindow
from Ui_Listar_clientes import Ui_Listar
from Ui_Tela_Update import Ui_Atualizar
from Ui_Tela_Login import Ui_Login
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastroclientes"
)

class Tela_Atualizar(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_Atualizar, self).__init__(*args, **argvs)
        self.ui = Ui_Atualizar()
        self.ui.setupUi(self)
        self.ui.PesquisarID.clicked.connect(self.Pesquisar)
        self.ui.AplicarB.clicked.connect(self.Atualizar)
    
    def Pesquisar(self):
        if self.ui.IDL.text()!= "":
            id =  self.ui.IDL.text()
            Cursor = banco.cursor()
            Comando_Sql = "SELECT * FROM  clientes WHERE id  = " + str(id)
            Cursor.execute(Comando_Sql)
            Dados_Lidos = Cursor.fetchall()

            for x in range(0,len(Dados_Lidos)):
                self.ui.IdA.setText(str(Dados_Lidos[x][0]))
                self.ui.NomeA.setText(str(Dados_Lidos[x][1]))
                self.ui.CpfA.setText(str(Dados_Lidos[x][2]))
                self.ui.DescricaoA.setText(str(Dados_Lidos[x][3]))
                self.ui.SalarioA.setText(str(Dados_Lidos[x][4]))
                self.ui.LojaA.setText(str(Dados_Lidos[x][5]))
         
            banco.commit()
        else:
             QMessageBox.about(self,'Erro','Id inválido')
    
    def Atualizar(self):
        if ((self.ui.CpfA.text() != "") and (self.ui.NomeA.text() != "")):
            id = self.ui.IdA.text()
            nome = self.ui.NomeA.text()
            Cpf = self.ui.CpfA.text()
            descricao = self.ui.DescricaoA.text()
            salario = self.ui.SalarioA.text()
            loja = self.ui.LojaA.text()

            Cursor = banco.cursor()
            Comando_Sql = "UPDATE clientes SET nome = %s, cpf = %s, descricao = %s, salario = %s, loja = %s  WHERE id = " + str(id)
            dados = (str(nome) , str(Cpf) , str(descricao) , str(salario) , str(loja))
            Cursor.execute(Comando_Sql,dados)
            banco.commit()
            self.ui.IdA.setText("")
            self.ui.NomeA.setText("")
            self.ui.CpfA.setText("")
            self.ui.DescricaoA.setText("")
            self.ui.SalarioA.setText("")
            self.ui.LojaA.setText("")
            QMessageBox.about(self,'Sucesso','Dados Atualizados com sucesso!')
        else:
            QMessageBox.about(self,'Erro','Preencha os campos obrigatórios!')
      

    



class Tela_Listar(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_Listar, self).__init__(*args, **argvs)
        self.ui = Ui_Listar()
        self.ui.setupUi(self)
        self.Preencher()
        self.ui.SalvarB.clicked.connect(self.SalvarPDF)
        self.ui.ExcluirB.clicked.connect(self.Excluir)
        self.ui.PesquisarB_2.clicked.connect(self.Preencher)
        self.ui.PesquisarB.clicked.connect(self.Pesquisar)
        self.ui.AtualizarB.clicked.connect(self.Chamar_Atualizar)

    def Preencher(self):
        Cursor = banco.cursor()
        Comando_Sql = "SELECT * FROM clientes"
        Cursor.execute(Comando_Sql)
        Dados_Lidos = Cursor.fetchall() 
        self.ui.tableWidget.setRowCount(len(Dados_Lidos))
        self.ui.tableWidget.setColumnCount(6)

        for x in range(0, len(Dados_Lidos)):
            for y in range(0,6):
                self.ui.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(Dados_Lidos[x][y])))
                
        banco.commit()
    
    def Pesquisar(self):
        if self.ui.PesquisarL.text() != "":
            Cursor = banco.cursor()
            nome = self.ui.PesquisarL.text()
            Cursor.execute("SELECT * FROM clientes WHERE  nome LIKE '%{}%'" .format(nome))
            Dados_Lidos = Cursor.fetchall() 
            self.ui.tableWidget.setRowCount(len(Dados_Lidos))
            self.ui.tableWidget.setColumnCount(6)

            for x in range(0, len(Dados_Lidos)):
                for y in range(0,6):
                    self.ui.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(Dados_Lidos[x][y])))
                
            banco.commit()
        else:
             QMessageBox.about(self,'Erro','Id inválido')


    def SalvarPDF(self):
        Cursor = banco.cursor()
        Comando_Sql = "SELECT * FROM clientes"
        Cursor.execute(Comando_Sql)
        Dados_Lidos = Cursor.fetchall() 
        y = 0

        pdf = canvas.Canvas('Lista_Clientes.pdf')
        pdf.setFont('Times-Bold', 20)
        
        pdf.drawString(200,800 , 'Lista de Clientes: ')
        pdf.setFont('Times-Bold', 10)

        pdf.drawString(10,750 , 'ID')
        pdf.drawString(110,750, 'NOME')
        pdf.drawString(210, 750, 'CPF')
        pdf.drawString(310,750, 'DESCRIÇÃO')
        pdf.drawString(410,750, 'SALÁRIO')
        pdf.drawString(510,750, 'LOJA')

        for i in range(0, len(Dados_Lidos)):
            y = y + 50
            pdf.drawString(10,750 - y, str(Dados_Lidos[i][0]))
            pdf.drawString(110,750 - y, str(Dados_Lidos[i][1]))
            pdf.drawString(210,750 - y, str(Dados_Lidos[i][2]))
            pdf.drawString(310,750 - y, str(Dados_Lidos[i][3]))
            pdf.drawString(410,750 - y, str(Dados_Lidos[i][4]))
            pdf.drawString(510,750 - y, str(Dados_Lidos[i][5]))

        pdf.save()
        QMessageBox.about(self,'Sucesso','PDF gerado com sucesso!')
        

    def Excluir(self):
       linha = self.ui.tableWidget.currentRow()
       self.ui.tableWidget.removeRow(linha)

       Cursor = banco.cursor()
       Cursor.execute("SELECT id FROM clientes")
       Dados_Lidos = Cursor.fetchall()
       Id = Dados_Lidos[linha][0]
       Cursor.execute("DELETE FROM clientes WHERE id = " + str(Id))
       banco.commit()
       QMessageBox.about(self, "Sucesso", "Cliente excluido com sucesso!")

    
    def Chamar_Atualizar(self):
        self.tela = Tela_Atualizar()
        self.tela.show()

        

        
        







class Tela_Principal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_Principal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ListarB.clicked.connect(self.Chamar_Listar)
        self.ui.finalizarB.clicked.connect(self.Salvar)
        self.ui.codigoT.setEnabled(False)
        self.ui.lojaAR.setChecked(True)

    def Chamar_Listar(self):
        self.tela = Tela_Listar()
        self.tela.show()
    

    def Limpar(self):
        self.ui.nomeT.setText("")
        self.ui.descricaoT.setText("")
        self.ui.cpfT.setText("")
        self.ui.salarioT.setText("")
    
    def Salvar(self):
        if ((self.ui.cpfT.text() != "") and (self.ui.nomeT.text() != "")):
                nome = self.ui.nomeT.text()
                desc = self.ui.descricaoT.text()
                cpf = self.ui.cpfT.text()
                salario = self.ui.salarioT.text()

                if self.ui.lojaAR.isChecked():
                    loja = "Loja A"
                elif self.ui.lojaBR.isChecked():
                    loja = "Loja B"
                else:
                    loja = ""
                Cursor = banco.cursor()
                try:
                    Comando_Sql = "INSERT INTO clientes VALUES (default, %s, %s, %s, %s, %s )" 
                    dados = (str(nome), str(cpf), str(desc), str(salario), loja)
                    Cursor.execute(Comando_Sql, dados) 
                    banco.commit()
                    self.Limpar()
                    QMessageBox.about(self, "Sucesso", "Dados cadastrados com sucesso!")
                except:
                     QMessageBox.about(self, "Erro", "CPF já existe no sistema!")
        else:
            QMessageBox.about(self , "Erro","Preencha os campos obrigatorios!")


class Tela_login(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_login, self).__init__(*args, **argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.Logar.clicked.connect(self.Login)



    def Login(self):
            login = self.ui.loginL.text()
            senha = self.ui.senhaL.text()
            Cursor = banco.cursor()
            try:
                
                Cursor.execute("SELECT senha from usuarios WHERE login = '{}'" .format(login))
                senha_Bd = Cursor.fetchall()
                banco.commit()

                if senha == senha_Bd[0][0]:
                    self.Chamar_telaPrincipal()
                else:
                    QMessageBox.about(self , "Erro","Dados incorretos")

            except:
                QMessageBox.about(self , "Erro","Campo Nulo ou usuário incorreto")
                self.ui.loginL.setText("")
                self.ui.senhaL.setText("")
                



    def Chamar_telaPrincipal(self):
        self.tela = Tela_Principal()
        self.tela.show()
        self.close()






app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = Tela_login()
    window.show()

sys.exit(app.exec_())


