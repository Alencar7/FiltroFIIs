# Filtro de FIIs
## Descrição
Filtro de FIIs é uma aplicação desenvolvida em Python para auxiliar na análise e filtragem de Fundos de Investimento Imobiliário (FIIs). O objetivo é fornecer uma ferramenta prática para investidores que desejam identificar FIIs com base em critérios específicos, como rentabilidade, preço, dividend yield, ou outros indicadores financeiros. O projeto foi criado como parte do aprendizado em Python, aplicando conceitos de manipulação de dados, automação e, possivelmente, integração com APIs ou web scraping para obtenção de dados financeiros.
##Tecnologias Utilizadas
Python 3: Linguagem principal do projeto.

Pandas (se aplicável): Para manipulação e análise de dados.

Requests/BeautifulSoup (se aplicável): Para web scraping de dados de FIIs.

Matplotlib/Seaborn (se aplicável): Para visualização de dados.

Jupyter Notebook (opcional): Para desenvolvimento interativo ou testes.

## Funcionalidades
Filtragem de FIIs com base em critérios como dividend yield, P/VP, ou liquidez.

Exibição de resultados em formato tabular ou gráfico.

Possível integração com fontes de dados externas, como sites financeiros ou APIs (ex.: Status Invest, Fundamentus).

Interface simples via console ou, futuramente, interface gráfica.

## Como Executar
Siga os passos abaixo para rodar a aplicação localmente:
Pré-requisitos:
Python 3.8 ou superior instalado.

Git para clonar o repositório.

Bibliotecas Python necessárias (instale via pip):
``` bash

pip install pandas requests beautifulsoup4 matplotlib seaborn
```
Clonar o Repositório:
```bash

git clone https://github.com/Alencar7/FiltroFIIs.git
cd FiltroFIIs
```
## Configurar o Ambiente (se necessário):
Crie um ambiente virtual:
```bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
Executar o Script Principal:
Navegue até o diretório do script principal (ex.: main.py ou similar):
```bash

python main.py
```
Siga as instruções no console para definir os filtros ou visualizar os resultados.

Caso o projeto inclua notebooks, execute:
bash

jupyter notebook

Abra o arquivo .ipynb correspondente no navegador.

Estrutura do Repositório
src/: Contém os scripts Python principais, incluindo a lógica de filtragem e manipulação de dados.

## Exemplo de Uso
O projeto foi desenvolvido com o intuito de filtrar os melhores Fundos de Investimento Imobiliário (FIIs) 
com base em critérios financeiros definidos pelo usuário, como dividend yield, preço por cota, ou P/VP (preço sobre valor patrimonial). 
Abaixo está um exemplo de como usar o script para filtrar FIIs com dividend yield superior a 8% e P/VP inferior a 1.0, exibindo os resultados de forma organizada:
```
python

# Exemplo de filtragem de FIIs com dividend yield acima de 8%
import pandas as pd

dados_fiis = pd.read_csv('fiis.csv')
filtro = dados_fiis[dados_fiis['dividend_yield'] > 8]
print(filtro[['ticker', 'dividend_yield', 'p_vp']])
```

Contato
Desenvolvedor: Adriano de Alencar

GitHub: Alencar7

E-mail: contato.adealencar@gmail.com

