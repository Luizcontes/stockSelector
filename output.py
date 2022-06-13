import xlsxwriter
import pandas as pd
import portfolio as pt

""" #   BIBLIOTECA PARA EXPORTAR PARA EXCEL
    #
    # Esta classe tem por objetivo exportar para um arquivo
    # excel os resultados obtidos a partir do dataframe 
"""
class DocWriter:

    def __init__(self, file='portfolio.xlsx', background_color='#C6C7EF', color='#000000'):
        self.file = 'file/' + file
        self.writer = pd.ExcelWriter(self.file, engine='xlsxwriter')
        pt.finalDF.to_excel(self.writer, 'Portfolio', index=False)
        self.string = self.writer.book.add_format(
            {
                'font_color': color,
                'bg_color': background_color,
                'border': 1
            }
        )
    
        self.stock = self.writer.book.add_format(
            {
                'num_format': '$ 0.00',
                'font_color': color,
                'bg_color': background_color,
                'border': 1,
                'align': 'center'
            }
        )
    
        self.market_cap = self.writer.book.add_format(
            {
                'num_format': '$ ###,### 000,000;$ -###,### 000,000',
                'font_color': color,
                'bg_color': background_color,
                'border': 1,
                'align': 'center'
            }
        )

        self.integer = self.writer.book.add_format(
            {
                'num_format': '0',
                'font_color': color,
                'bg_color': background_color,
                'border': 1,
                'align': 'center'
            }
        )
    """ metodo criado para ajusta a largura das colunas de acordo com
    a largura do texto que preenche o cabecalho """
    def ajustar_linha(self, a):
        
        column_width = max(pt.finalDF[a].astype(str).map(len).max(), len(a))
        return column_width

    """ metodo criado para aplicar toda a formatacao necessaria para
    a criacao do documento com o relatorio final """
    def criar_documento(self):
        sheet = self.writer.sheets['Portfolio'].set_column('A:A', self.ajustar_linha('Ticker'), self.string)
        sheet = self.writer.sheets['Portfolio'].set_column('B:B', self.ajustar_linha('Stock Price'), self.stock)
        sheet = self.writer.sheets['Portfolio'].set_column('C:C', self.ajustar_linha('Market Capitalization'), self.market_cap)
        sheet = self.writer.sheets['Portfolio'].set_column('D:D', self.ajustar_linha('Shares'), self.integer)
        """ print(pt.finalDF.iloc[0,1]) """
        self.writer.save()
