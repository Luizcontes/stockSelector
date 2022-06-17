import busca_index_info as bi
import busca_acoes_info as ba
import secrets
import pandas as pd
import requests
import portfolio as pt
from requests.exceptions import ConnectionError
from keys.iexcloud import IEX_CLOUD_API_TOKEN as token
import libs.validacoes as val

""" 
    #   BIBLIOTECA PARA BUSCAR DADOS DA BOLSA
    # 
    # Esta biblioteca faz uso de um arquivo CSV que contem a lista
    # das acoes que compoem o indice que se deseja usar para trabalhar
    # os dados e entao fazendo uso de uma API, busca os dados relativos
    # a cada acao 
"""

class DadosBolsa(bi.BuscaIndex, ba.BuscaAcoes):
    
    def __init__(self, portSize, indice):
        super().__init__(indice)
        self.portSize = portSize
        self.tamanhoPosicao = self.obter_tamanho_posicao()
        self.data = self.buscar_dado(self.stocksList)
        self.port = pt.Portfolio(self.data)
    
    """ Funcao que extrai dos dados das acoes obtidos da API os valoes com
        os quais pretendemos trabalhar para cada ticker extraido do pedaco
        criado a partir da lista de acoes do indice"""
    def ler_papel2(self, i=-1):
        if (i == -1):
            i = len(self.stocksListJSON) - 1
        if (i > 0):
            y = i - 1
            self.ler_papel2(y)
            self.port.criar_linha(self.stocksListJSON[i])
        else:
            self.port.criar_linha(self.stocksListJSON[i])
        self.port.adicionar_acoes_qtd(self.tamanhoPosicao)
        
    """ Funcao que constroi a lista de acoes e os dados de interesse pertencentes
        a estas acoes por pedacos para facilitar a busca desses dados na net"""
    def construir_tabela(self):
        stocks = DadosBolsa.ler_lista_papeis(self)
        for symbol_string in DadosBolsa.dividir_lista(stocks, 100):
            DadosBolsa.popular_tabela(symbol_string)
                
    """ Funcao utilizada para dividir a lista de acoes em pedacos de 100
        papeis para fazer uma busca em lotes(fazer um metodo get para cada acao
        tornaria o processo extremamente lento, os provedores de API`s inclusive
        incentivam o uso de funcoes bash para consumir menos recursos) """
    def dividir_lista(lst, n):
        arr = []
        str = ""
        count = 0
        length = len(lst)
        pedacos = int(length/n)
        i = 0
        start = 0
        while(i <= pedacos):
            for l in lst['TICKER'][start:n]:
                if (count%100==0):
                    str = l
                else:
                    str = ','.join([str,l])
                count+=1
            arr.append(str)
            i += 1
            start += 100
            n += 100
        return arr

    """ Funcao utilizada para carregar o pedaco de dados e inserir na tabela
        que compoem a lista de acoes do indice que se pretende trabalhar """
    def popular_tabela(symbol_string):
        data = DadosBolsa.buscar_dado(symbol_string)
        ticker = symbol_string.split(',')
        DadosBolsa.ler_papel(data, ticker)    
        
    """ Funcao que extrai dos dados das acoes obtidos da API os valoes com
        os quais pretendemos trabalhar para cada ticker extraido do pedaco
        criado a partir da lista de acoes do indice"""
    def ler_papel(data, ticker, i=-1):
        if (i == -1):
            i = len(ticker) - 1
        if (i > 0):
            y = i - 1
            DadosBolsa.ler_papel(data, ticker, y)
            pt.criar_linha(data,ticker[i])
        else:
            pt.criar_linha(data,ticker[i])
    
    """ metodo para obter o valor a ser investido em cada acao que compoem
    o indice """
    def obter_tamanho_posicao(self):
        tamanho = float(self.portSize)/float(self.qtdPapeis)
        return tamanho





