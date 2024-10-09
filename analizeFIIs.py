import pandas as pd

tabela = pd.read_csv("arquivo.csv")
"""
-> Dados sobre FIIs pegos no site: https://www.fundamentus.com.br/fii_resultado.php

-> Vou usa as informacoes mais relevantes sobre FIIs: DY, P/VP, LIQUIDEZ
-> Excluirei colunas desnecessarias, ou com pouca importancia
-> Logica dos filtros: liquidez ideal >= 1.5mi/2 ; P/VP > 0.96 ; DY acima de 0,6 - 0,8
-> O resultado final retorna os dados em .csv e .xlsx

"""

# ADD DEF

#def formatar(valor):
#   
#    valor = valor.replace('%', '').strip()  
#    valor = valor.replace(',', '.') 

coluna_desnecessaria = ["Aluguel_por_m2", "Preço_do_m2", "Qtd_de_imóveis"]
tabela = tabela.drop(columns=coluna_desnecessaria)

# filtragem:
tabela['Liquidez'] = tabela['Liquidez'].str.replace('.', '').astype(int)
tabela = tabela[tabela['Liquidez'] > 2000000]

tabela['P/VP'] = tabela['P/VP'].str.replace(',', '.').astype(float)
tabela = tabela[tabela['P/VP'] > 0.96]

tabela['Dividend_Yield'] = tabela['Dividend_Yield'].str.replace(
    '%', '').str.replace(',', '.').astype(float)
tabela = tabela[tabela['Dividend_Yield'] >= 0.7]

# conversao final
tabela.to_csv('tabela_final.csv', index=False)
tabela.to_excel('tabela_final.xlsx', index=False)
