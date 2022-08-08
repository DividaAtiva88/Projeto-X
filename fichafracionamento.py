#validar valor de entrada e saida#
#verificador de tributo#
#subtrair taxa do valor origem#
#discriminar valor imposto e taxa#
#Separar em parcelas de acordo com o ano origem#
#débito restante zerado#
#Tributo 01 não tem taxa#
#Tributo 02 tem taxa#
#Podem haver outros tributos#
#Find by id tabela/listar tabela#
#banco de dados não relacional#
#Kivy/Tkinter para interface grafica#


import csv
import math
with open('tabelataxas.csv') as tabela:
    tabela_csv = csv.reader(tabela, delimiter=',')
    for i, linha in enumerate(tabela_csv):
        if i ==0:
            print("Cabeçalho" + str(linha))
        else:
                print("Valor:" + str(linha))
    

#servidor = str(input("Funcionário"))
#proc = float(input("Processo"))
#lancOri1 = int(input("Lançamento origem 01"))
#lancOri2 = int(input("Lançamento origem 02"))
#lancOri3 = int(input("Lançamento origem 03"))
#metragemOri = float(input("Metragem Origem"))
#anotar = str(input("Observações"))

#tributo = int(input("Tributo"))
#certificadoDA = int(input("CDA"))
#valorImposto = float(input("Valor do imposto"))
#valorTaxa = float(input("Valor da taxa"))
#
#reduz = valorImposto - valorTaxa
#print(f"O valor do imposto real é de R${reduz}")

#base = float(input("Ano base"))

#fracionamento = fracionamento()