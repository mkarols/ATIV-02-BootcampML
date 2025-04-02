
# 8º Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

# Importa a biblioteca pandas
import pandas as pd

# Lê o arquivo CSV e mostra as 5 primeiras linhas
print(pd.read_csv("dados.csv").head(5))