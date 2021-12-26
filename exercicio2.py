# Escreva um programa que, dada uma matrix 3x3, armazena em cada posição da matriz, 
# a soma dos valores da linha e coluna que definem a posição. 
# Por exemplo, na posição [1][2] você deverá armazenar o valor 1+2 = 3 e assim por diante. 
# Imprima a matriz na tela.

matrix = [[x + y for y in range(3)] for x in range(3)]
print(matrix)