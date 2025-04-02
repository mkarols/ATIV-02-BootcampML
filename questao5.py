
# 5º Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

#Criei uma função que retorna a lista ordenada em ordem alfabética.

def listaordenada(lista):
    return sorted(lista)  

# Saída:
pessoas = [("Karol", 27), ("Pedro", 27), ("João", 23)]
print(listaordenada(pessoas)) 