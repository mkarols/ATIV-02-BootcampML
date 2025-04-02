
# 2º Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

#Criei a função 'numerosprimos', que recebe uma lista e armazena os números em outra lista (primos) vazia.

def numerosprimos(lista): 
    primos = [] 
 
#Percorre a lista, ignora números menores que 2, conta divisores e adiciona à lista apenas os números que possuem exatamente dois divisores.

    for num in lista: 
        if num < 2: 
            continue  
        
        divisores = 0  
        
        for divisor in range(1, num + 1): 
            if num % divisor == 0:
                divisores += 1  
      
        if divisores == 2:  
            primos.append(num)
    
    return primos 

#Saída:
print(numerosprimos([2, 3, 9, 11, 18, 37]))  