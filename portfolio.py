import pandas as pd
import math

""" #   BIBLIOTECA PARA CRIAR E MANIPULAR A TABELA COM OS DADOS DAS ACOES
    #
    # Esta biblioteca utiliza os dados carregados a partir da lista com
    # as acoes pertencentes ao indice que se deseja trabalhar bem como
    # os dados de mercado obtidos para cada acao e gera uma tabela com
    # estes dados que posteriormente sera utilizada para elaborar a 
    # estrategia pretendida
"""

class Portfolio:

    def __init__(self, data):
        self.data = data
        self.missingTicker = 0
        self.finalDF = ''
        self.my_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Shares']
        self.finalDF = pd.DataFrame(columns = self.my_columns)
        pd.set_option('display.max_row', None)

    """ Funcao que criar uma linha para ser inserida na tabela com os dados 
        relativos ao ticker(nome), preco, tamanho da empresa e qtd de 
        acoes a serem obtidos de acordo com a estrategia """
    def criar_linha(self, ticker):
        try:
            price = self.data[ticker]['quote']['latestPrice']
            market_cap = self.data[ticker]['quote']['marketCap']
            stock = pd.DataFrame([[ticker, price, market_cap, 'N/A']], columns = self.my_columns)
            self.inserir_papel(stock)
        except (KeyError, TypeError):
            self.missingTicker += 1
        

    """ Funcao criada para inserir na tabela final, cada acao com seus
        respectivos atributos """
    def inserir_papel(self, stock):
        self.finalDF = pd.concat([self.finalDF, stock], ignore_index=True)
        return self.finalDF

    """ metodo que a partir do valor a ser investido em cada papel
    e o preco de determinado papel, calcula e atualiza a tabela com a
    quantidade de acoes comprar  """
    def adicionar_acoes_qtd(self, tam_posicao):
        for i in range(0, len(self.finalDF.index)):
            try:
                preco_papel = float(self.finalDF.loc[i, 'Stock Price'])
                self.finalDF.loc[i, 'Shares'] = math.floor(tam_posicao/preco_papel)
            except (NameError, TypeError):
                pass
    """ Funcao pra imprimir a tabela final """
    def imprimir_tabela(self):
        print(self.finalDF)


