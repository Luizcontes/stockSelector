import os
import dados_bolsa as db
import portfolio as pt
import output as out
import indexes_list as ind
import libs.validacoes as val
import indexes_list as ind

""" #   MAIN
    #   
    # Este arquivo contem as funcoes basicas para montar um carteira
    # utilizando as bibliotecas criadas para requisitar e trata
    # os dados das acoes de uma determinada bolsa de valores
"""
class Main(val.Validacoes):

    def __init__(self):
        self.indList = ind.IndexesList()
        self.indexSize = self.indList.getIndexesSize()
        # self.indexesList = self.indList.printIndexesList()

    # metodo para obter o valor a ser investido em cada acao que compoem
    # o indice
    # def obter_tamanho_posicao(port, qtd):
    #     tamanho = float(port)/float(qtd)
    #     return tamanho

    # metodo que a partir do valor a ser investido em cada papel
    # e o preco de determinado papel, calcula e atualiza a tabela com a
    # quantidade de acoes comprar 
    # def adicionar_acoes_qtd(tam_posicao):
    #     for i in range(0, len(pt.finalDF.index)):
    #         preco_papel = float(pt.finalDF.loc[i, 'Stock Price'])
    #         pt.finalDF.loc[i, 'Shares'] = math.floor(tam_posicao/preco_papel)

    """ metodo criado para chamar a biblioteca que obtem a cotacao das acoes
    e construir uma tabela com estes dados """
    def gerar_carteira(self, portSize, indCart):
        # for key, ind in opcoes.items():
        carteira = db.DadosBolsa(portSize, indCart)
        carteira.ler_papel2()
        return carteira
            
        # Main.adicionar_acoes_qtd(tamanho_posicao)

    def imprimir_informacoes(self, portSize, qtdAcoes, missTicker, tamPosicao, ind):
        os.system("clear")
        print("Indice escolhido: ", ind)
        print("Valor do porfolio: USD", "{:.2f}".format(portSize))
        print("Quantidade de acoes contidas no indice: ", qtdAcoes)
        print("Quantidade de acoes com dados inexistentes: ", missTicker)
        print("Tamanho medio de cada posicao USD", "{:.2f}".format(tamPosicao))

    def opcoes1(self):
        print("\nEscolha quais indices gostaria de utilizar para elaborar")
        print("a sua estrategia de investimento (separados por espaco)")
        print("Ex: 5 9 23")

    """ Metodo criado para exibir opcoes ao utilizador e fazer chamada as
    bibliotecas para a correta execucao do script """

    def createOptionsTuple(self):
        optionsString = input()
        optionsList = optionsString.split()
        optionsArray = map(self.isDecimal, optionsList)
        optionsArray = [self.isValidOption(option, self.indexSize) for option in optionsArray]
        return tuple(optionsArray)
    
    def printQqcoisa():
        print("teste print qqcoisa")

    def main(self):
        while True:
            print("\t*****StOcK sElEcToR*****\n")
            self.indList.printIndexesList()
            self.opcoes1()
            opcoes = self.createOptionsTuple()
            # print(opcoes)
            if False in opcoes:
                print("Por favor insirar uma opcao correta...")
                x = input()
                os.system('clear')
            else:
                break
        os.system('clear')
        print("\nIndices escolhidos para elaborar estrategia:")
        self.indList.printOption(opcoes)
        optDic = self.indList.getOptionsDictionary(opcoes)
        
        while True:
            # global portfolio_size
            portfolio_size = input('\nInsira o valor a investir para cada indice: ')
            if(self.isFloat(portfolio_size)):
                portfolio_size = float(portfolio_size)
                break
            else:
                print('Favor inserir um numero valido')

        for key, ind in optDic.items():
            c = self.gerar_carteira(portfolio_size, ind)
            self.imprimir_informacoes(c.portSize, c.qtdPapeis, c.port.missingTicker, c.tamanhoPosicao, ind)
            print("Portfolio gerado com sucesso...\n")
            x = ''
            while (x != '0' or x != '1'):
                print("Pressione:\n(0) para imprimir na tela\n(1) para gerar um arquivo")
                x = input()
                if(x == '0'):
                    c.port.imprimir_tabela()
                    x = input("Pressione qualquer tecla para continuar...")
                    break
                elif (x == '1'):
                    indexDesc = self.indList.getIndexDesc(key)
                    out.DocWriter(c.port.finalDF, indexDesc).criar_documento()
                    break
                else:
                    os.system('clear')
                    print("Entre a opcao correta...")
                    x = 'a'

m = Main()
m.main()

