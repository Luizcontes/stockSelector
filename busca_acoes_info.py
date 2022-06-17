from keys.iexcloud import IEX_CLOUD_API_TOKEN as token
import libs.validacoes as val
import requests

class BuscaAcoes(val.Validacoes):

    """ Funcao que busca os dados relativos ao pedaco da lista contendo alguns
    papeis, passada como argumento em formato de string """
    def buscar_dado(self, stocksList):
        batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={stocksList}&types=quote&token={token}'
        try:
            data = requests.get(batch_api_call_url)
        except ConnectionError:
            print("Erro ao conectar-se a base de dados, o servidor pode ter mudado de endereco")
            exit()
        if(self.is_response_ok(data)):
            data = data.json()
            return data
        else:
            print("Tivemos problemas ao solicitar dados do servidor", data.status_code)
            exit()