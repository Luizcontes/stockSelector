import json
import gspread
from numpy import index_exp
import pandas as pd
import libs.validacoes as val

# def getIndexesData():
#     serv_account = gspread.service_account(
#         filename="/home/luizcontes/Projetos/stockSelector/gsheets/service_account.json")
#     planilha = serv_account.open("Cópia de Indices Constituents Support")
#     folha = planilha.worksheet("Major Indices")
#     indices = folha.get_all_records()
#     return indices

""" 
    #   IndexesList
    # Classe criada pra buscar a lista com os indices disponiveis
    # para consulta pelo provedor da API, nesta classe basicamente
    # usamos o retorno da consulta para escolher quais os indices que
    # gostariamos de usar para elaborar nossa estrategia de investimento
 """


class IndexesList(val.Validacoes):

    def __init__(self):
        self.serv_account = gspread.service_account(
            filename="./keys/service_account.json")
        self.planilha = self.serv_account.open(
            "Cópia de Indices Constituents Support")
        self.folha = self.planilha.worksheet("Major Indices")
        self.indices = self.folha.get_all_records()
        self.index_array = self.getIndexesArray()

    def getIndexesArray(self):
        index_array = []
        for i in self.indices:
            index_array.append(i["symbol"])
        return index_array

    def getOptionsDictionary(self, options):
        optionsDictionary = {}
        for option in options:
            optionsDictionary[option] = self.index_array[option-1]
        return optionsDictionary

    def printIndexesList(self):
        indexesList = ''
        for i in self.indices:
            print(
                f'{str(self.indices.index(i)+1).zfill(2)}- {i["symbol"]}\t {str.upper(i["name"])}')
            indexesList += f'{str(self.indices.index(i)+1).zfill(2)}- {i["symbol"]}\t {str.upper(i["name"])}\n'
        return indexesList

    def printOption(self, opcoes):
        for opcao in opcoes:
            print(
                f'{str(opcao).zfill(2)}- {self.folha.cell(opcao+1, 2).value}')

    def getIndexesSize(self):
        return len(self.index_array)

    def getIndexDesc(self, opcao):
        return self.folha.cell(opcao+1, 2).value
