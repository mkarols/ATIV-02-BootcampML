
#9º  Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

# Importa a biblioteca pandas

import pandas as pd

# Suponha que o DataFrame "dados" tenha uma coluna chamada "nota" e seleciona a coluna "nota".

coluna_nota = dados["nota"]

# Filtra linhas onde a nota é maior que 7
notas_altas = dados[dados["nota"] > 7]

# Saída:
print("Coluna 'nota':")
print(coluna_nota) 

print("\nNotas maiores que 7:")
print(notas_altas)