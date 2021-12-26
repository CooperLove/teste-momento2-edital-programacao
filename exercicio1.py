# Faça um programa que preencha um vetor com 6 valores distintos digitados pelo usuário.
# Em seguida, exiba o maior e o menor valor do vetor, indicando em qual posição eles se encontram.
# Depois, imprima os itens no vetor em ordem crescente.
import math

print("Informe os 6 valores desejados para preencher o vetor.")
values = [] # Vetor de números.
max = -math.inf # Valor máximo.
min = math.inf # Valor minimo.

# Organiza o vetor em ordem crescente
def sortArray (array: list):
    i = 0
    for x in array:
        for y in range (i, len(array)):
            if array[i] > array[y]:
                array[i], array[y] = array[y], array[i]
        i = i + 1
    return array

# Seta os valores min e max de acordo com que o usuário vai informando os valores.
# Não sendo necessário percorrer o vetor novamente após os 6 valores serem definidos.
def setMinMax (number): 
    global max 
    max = number if number > max else max
    global min 
    min = number if number < min else min

n = 0
# While para pegar os 6 valores do usuário.
while n < 6:
    userInput = input("Valor "+str(n)+": ")
    try: # Caso o valor seja um número, ele é adicionado no vetor.
        number = int(userInput)
        values.append(number)
        setMinMax(number)
        n = n + 1
    except: # Caso contrário é informado ao usuário que os valores devem ser apenas números.
        print("Digite apenas números")
        

print("Os valores escolhidos foram: "+str(values))
print("O menor valor é: "+str(min)+" na posição "+str(values.index(min)))
print("O maior valor é: "+str(max)+" na posição "+str(values.index(max)))
values = sortArray(values)
print("Vetor em ordem crescente: "+str(values))
