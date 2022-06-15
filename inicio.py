import math
import os
from turtle import clear
import dados_bolsa as sp500
import portfolio as pt
import output as out
import indexes_list as ind

""" #   INICIAR
    #   
    # Este arquivo contem as funcoes basicas para montar um portfolio
    # utilizando as bibliotecas criadas para requisitar e trata
    # os dados das acoes de uma determinada bolsa de valores
"""

""" metodo criado para verificar se o valor inserido pelo utilizador
e um numero float """
def isFloat(num):
    try:
        num = float(num)
        return True
    except ValueError:
        return False

""" metodo para obter o valor a ser investido em cada acao que compoem
o indice """
def obter_tamanho_posicao(port, qtd):
    tamanho = float(port)/float(qtd)
    return tamanho

""" metodo que a partir do valor a ser investido em cada papel
e o preco de determinado papel, calcula e atualiza a tabela com a
quantidade de acoes comprar  """
def adicionar_acoes_qtd(tam_posicao):
    for i in range(0, len(pt.finalDF.index)):
        preco_papel = float(pt.finalDF.loc[i, 'Stock Price'])
        pt.finalDF.loc[i, 'Shares'] = math.floor(tam_posicao/preco_papel)

""" metodo criado para chamar a biblioteca que obtem a cotacao das acoes
e construir uma tabela com estes dados """
def gerar_portfolio(port, opcoes):
    global quantidade_acoes
    global tamanho_posicao
    quantidade_acoes = sp500.ler_qtd_papeis()
    tamanho_posicao = obter_tamanho_posicao(port, quantidade_acoes)
    sp500.construir_tabela()
    adicionar_acoes_qtd(tamanho_posicao)

def imprimir_informacoes():
    os.system("clear")
    print("Valor do porfolio: USD", "{:.2f}".format(portfolio_size))
    print("Quantidade de acoes contidas no indice: ", quantidade_acoes)
    print("Tamanho medio de cada posicao USD", "{:.2f}".format(tamanho_posicao))

""" Metodo criado para exibir opcoes ao utilizador e fazer chamada as
bibliotecas para a correta execucao do script """
def iniciar(opcoes):
    while True:
        global portfolio_size
        portfolio_size = input('\nInsira o valor a investir para cada indice: ')
        if(isFloat(portfolio_size)):
            portfolio_size = float(portfolio_size)
            break
        else:
            print('Favor inserir um numero valido')
    gerar_portfolio(portfolio_size, opcoes)
    imprimir_informacoes()
    print("Portfolio gerado com sucesso...\n")
    x = ''
    while (x != '0' or x != '1'):
        print("Pressione:\n(0) para imprimir na tela\n(1) para gerar um arquivo")
        x = input()
        if(x == '0'):
            pt.imprimir_tabela()
            break
        elif (x == '1'):
            out.DocWriter().criar_documento()
            break
        else:
            os.system('clear')
            print("Entre a opcao correta...")
            x = 'a'

def isValidOption(option):
    if (option <= indList.getIndexesSize()):
        return True
    else:
        return False

def createOptionsTuple(optionsString):
    tmp = ''
    optionsArray = []
    for option in optionsString:
        if (not option.isspace()):
            tmp += option
        else:
            if (tmp.isdecimal()):
                if(isValidOption(int(tmp))):
                    optionsArray.append(int(tmp))
                    tmp = ''
                else:
                    break
            else:
                break
    if (tmp.isdecimal() and isValidOption(int(tmp))):
        # if(isValidOption(int(tmp))):
        optionsArray.append(int(tmp))
        optionsTuple = tuple(optionsArray)
        return optionsTuple
    else:
        print("Por favor insirar uma opcao correta...")
        x = input()
        os.system('clear')

def iniciar2():
    print("\nEscolha quais indices gostaria de utilizar para elaborar")
    print("a sua estrategia de investimento (separados por espaco)")
    print("Ex: 5 9 23")
    optionsString = input()
    optionsTuple = createOptionsTuple(optionsString)
    return optionsTuple
    
def main():
    while True:
        print("\t*****StOcK sElEcToR*****\n")
        indList.printIndexesList()
        opcoes = iniciar2()
        os.system('clear')
        print("\nIndices escolhidos para elaborar estrategia:")
        indList.printOption(opcoes)
        iniciar(opcoes)
"""         optionDic = {}
        for opcao in opcoes:
            optionDic[opcao] = indList.index_array[opcao-1]
        print(optionDic) """

# iniciar()
indList = ind.IndexesList()
main()



