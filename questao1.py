
#1º Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

#Criei a função 'numerosimpares', que recebe uma lista e armazena os números em outra lista (ímpares) vazia.

def numerosimpares(lista): 
    impares = [] 

# Para cada número na lista , verificar se o número é ímpar e retornar a lista final.
    for num in lista:  
        if num % 2 == 1: 
            impares.append(num)
           
    return impares

#Saída:
print(numerosimpares([1, 2, 3, 4, 5, 6, 7, 8, 9]))  
print(numerosimpares([9, 10, 13, 16, 19, 21])) 


