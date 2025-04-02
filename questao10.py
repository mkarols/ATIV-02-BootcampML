
# 10° .Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

# Importa a biblioteca pandas

import pandas as pd

#Remover linhas com valores faltantes
dados_limpos = dados.dropna() 

#Substituir NaN por zero
dados_preenchidos = dados.fillna(0)  

# Mostrar resultados:
print(dados_limpos.head())  
print(dados_preenchidos.head()) 