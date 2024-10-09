import pandas as pd

# Adiciona o arquivo do excel

# Lê o arquivo .xlsx
arquivo_excel = pd.read_excel('arquivo.xlsx')

# Converte para .csv
arquivo_excel.to_csv('arquivo.csv', index=False)
