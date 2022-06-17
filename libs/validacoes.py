import re

""" #   VALIDACOES
    #   
    # Esta lib contem funcoes responsaveis por validar os dados
    # fornecidos pelos usuarios bem como os recuperados atraves
    # de apis para que sejam os mais adequados para o tratamento
"""

class Validacoes:

    """ metodo criado para verificar se o valor inserido pelo utilizador
    e um numero float """
    def isFloat(self, num):
        try:
            num = float(num)
            return True
        except ValueError:
            return False

    """ Funcao criada para verificar se o retorno do metodo GET retorna
    algum erro que permite que o script continua mas gera algum erro posteriormente
    por nao conter o dado esperado na requisicao"""
    def is_response_ok(self, response):
        if(response.status_code == 200):
            return True
        else:
            return False 

    def isValidOption(self, option, indexSize):
        if (option <= indexSize):
            return option
        else:
            return False

    def isDecimal(self, str):
        if str.isdecimal():
            return int(str)
        else:
            return False
    
    def splitCompoundTicker(self, indexList):
        tickerList = []
        for t in indexList:
            ticker = str(t).split('.')
            ticker = ticker[0].split(' ')
            tickerList.append((ticker[0]))
        return tickerList
            


