
# 4º Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

#Criei uma função que verifica se a lista tem pelo menos dois elementos, retornando `None` caso contrário.

def segundo_maior(lista):
    if len(lista) < 2:
        return None  
    
    maior = lista[0]
    segundo_maior = None
    
    # Encontra o maior número.
    for num in lista:
        if num > maior:
            maior = num
    
    #Encontra o maior número que seja menor que "maior".
    for num in lista:
        if num != maior:  
            if segundo_maior is None or num > segundo_maior:
                segundo_maior = num
    
    return segundo_maior

# Saída:
print(segundo_maior([3, 5, 7, 8, 8]))  
print(segundo_maior([4, 5]))        