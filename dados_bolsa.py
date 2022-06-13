import pandas as pd
import requests
import portfolio as pt
from requests.exceptions import ConnectionError

""" 
    #   BIBLIOTECA PARA BUSCAR DADOS DA BOLSA
    # 
    # Esta biblioteca faz uso de um arquivo CSV que contem a lista
    # das acoes que compoem o indice que se deseja usar para trabalhar
    # os dados e entao fazendo uso de uma API, busca os dados relativos
    # a cada acao 
"""

IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'

""" Funcao que constroi a lista de acoes e os dados de interesse pertencentes
    a estas acoes por pedacos para facilitar a busca desses dados na net"""
def construir_tabela():
    stocks = ler_lista_papeis()
    for symbol_string in dividir_lista(stocks, 100):
        popular_tabela(symbol_string)
            
""" Funcao criada para carregar a lista com os tickers pertencentes
    ao indice com o qual se deseja trabalhar """
def ler_lista_papeis():
    stocks =  pd.read_csv('file/sp_500_stocks.csv')
    return stocks

""" Funcao que mostra a quantidade de acoes contida no indice """
def ler_qtd_papeis():
    return len((pd.read_csv('file/sp_500_stocks.csv')))

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
    data = buscar_dado(symbol_string)
    ticker = symbol_string.split(',')
    ler_papel(data, ticker)    
    

""" Funcao que busca os dados relativos ao pedaco da lista contendo alguns
    papeis, passada como argumento em formato de string """
def buscar_dado(symbol_string):
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote&token={IEX_CLOUD_API_TOKEN}'
    try:
        data = requests.get(batch_api_call_url)
    except ConnectionError:
        print("Erro ao conectar-se a base de dados, o servidor pode ter mudado de endereco")
        exit()
    if(is_response_ok(data)):
        data = data.json()
        return data
    else:
        print("Tivemos problemas ao solicitar dados do servidor", data.status_code)
        exit()

""" Funcao criada para verificar se o retorno do metodo GET retorna
    algum erro que permite que o script continua mas gera algum erro posteriormente
    por nao conter o dado esperado na requisicao"""
def is_response_ok(response):
    if(response.status_code == 200):
        return True
    else:
        return False 

""" Funcao que extrai dos dados das acoes obtidos da API os valoes com
    os quais pretendemos trabalhar para cada ticker extraido do pedaco
    criado a partir da lista de acoes do indice"""
def ler_papel(data, ticker, i=-1):
    if (i == -1):
        i = len(ticker) - 1
    if (i > 0):
        y = i - 1
        ler_papel(data, ticker, y)
        pt.criar_linha(data,ticker[i])
    else:
        pt.criar_linha(data,ticker[i])