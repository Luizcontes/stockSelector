from keys.finnhub import key
import libs.validacoes as val
import requests

class BuscaIndex(val.Validacoes):

    def __init__(self, indice):
        self.stocksListJSON = self.ler_json_papeis(indice)
        self.qtdPapeis = self.ler_qtd_papeis()
        self.stocksList = self.stocksListString()

    def ler_json_papeis(self, ticker):
        apiURL = 'https://finnhub.io/api/v1/index/constituents?'
        symbol = f'symbol={ticker}'
        token = f'&token={key}'
        req = apiURL + symbol + token

        try:
            resp = requests.get(req)
        except ConnectionError:
            print("Erro ao conectar-se a base de dados, o servidor pode ter mudado de endereco")
            exit()
        if(self.is_response_ok(resp)):
            stocksListJSON = self.splitCompoundTicker(resp.json()['constituents'])
            return stocksListJSON

    def stocksListString(self):
        stocksList = ','.join(self.stocksListJSON)
        return stocksList
    
    def ler_qtd_papeis(self):
        return len(self.stocksListJSON)