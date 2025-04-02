
#3º Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

# Criei umaa função 'elementos' e criei uma lista vazia 'novalista' para armazenar os elementos que estão em apenas uma das listas.
def elementos(lista1, lista2):
    novalista = []
    
    # Adiciona números da lista1 que não estão na lista2
    for num in lista1:
        if num not in lista2:
            novalista.append(num)
    
    # Adiciona números da lista2 que não estão na lista1
    for num in lista2:
        if num not in lista1:
            novalista.append(num)
    
    return novalista

# Saída:
print(elementos([10, 20, 30, 40], [40, 50, 60])) 