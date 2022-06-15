import json
import gspread
from numpy import index_exp
import pandas as pd

# def getIndexesData():
#     serv_account = gspread.service_account(
#         filename="/home/luizcontes/Projetos/stockSelector/gsheets/service_account.json")
#     planilha = serv_account.open("Cópia de Indices Constituents Support")
#     folha = planilha.worksheet("Major Indices")
#     indices = folha.get_all_records()
#     return indices

""" 
    # Classe criada pra buscar a lista com os indices disponiveis
    # para consulta pelo provedor da API, nesta classe basicamente
    # usamos o retorno da consulta para escolher quais os indices que
    # gostariamos de usar para elaborar nossa estrategia de investimento
 """
class IndexesList:

    def __init__(self):
        self.serv_account = gspread.service_account(
        filename="./gsheets/service_account.json")
        self.planilha = self.serv_account.open("Cópia de Indices Constituents Support")
        self.folha = self.planilha.worksheet("Major Indices")
        self.indices = self.folha.get_all_records()
        self.index_array = self.getIndexesArray()

    def getIndexesArray(self):
        index_array = []
        for i in self.indices:
            index_array.append(i["symbol"])
        return index_array

    def addZero(self, i):
        addZero = ""
        if (i+1 < 10):
            addZero = 0
        else:
            addZero = ""
        return addZero

    def printIndexesList(self):
        for i in self.indices:
            print(f'{self.addZero(self.indices.index(i))}{self.indices.index(i)+1}- {i["symbol"]}\t {str.upper(i["name"])}')
    
    def printOption(self, opcoes):
        for opcao in opcoes:
            print(f'{self.addZero(opcao)}{opcao}- {self.folha.cell(opcao+1, 2).value}')
        
    def getIndexesSize(self):
        return len(self.index_array) 