import pandas as pd

""" #   BIBLIOTECA PARA CRIAR E MANIPULAR A TABELA COM OS DADOS DAS ACOES
    #
    # Esta biblioteca utiliza os dados carregados a partir da lista com
    # as acoes pertencentes ao indice que se deseja trabalhar bem como
    # os dados de mercado obtidos para cada acao e gera uma tabela com
    # estes dados que posteriormente sera utilizada para elaborar a 
    # estrategia pretendida
"""

my_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Shares']
finalDF = pd.DataFrame(columns = my_columns)

pd.set_option('display.max_row', None)

""" Funcao que criar uma linha para ser inserida na tabela com os dados 
    relativos ao ticker(nome), preco, tamanho da empresa e qtd de 
    acoes a serem obtidos de acordo com a estrategia """
def criar_linha(data, ticker):
    price = data[ticker]['quote']['latestPrice']
    market_cap = data[ticker]['quote']['marketCap']
    stock = pd.DataFrame([[ticker, price, market_cap, 'N/A']], columns = my_columns)
    inserir_papel(stock)

""" Funcao criada para inserir na tabela final, cada acao com seus
    respectivos atributos """
def inserir_papel(stock):
    global finalDF
    finalDF = pd.concat([finalDF, stock], ignore_index=True)
    return finalDF

""" Funcao pra imprimir a tabela final """
def imprimir_tabela():
    print(finalDF)


