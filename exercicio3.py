# Escreva um programa que lê 2 matrizes A e B, cada uma com 3 linhas e 2 colunas. 
# Construir uma matriz C de mesma dimensão (3x2) onde C é formada pela soma dos elementos da matriz A 
# com os elementos da matriz B (exemplo: C[1][1] = A[1][1] + B[1][1]).
# Apresentar ao final as 3 matrizes (A, B e C).

from random import seed
from random import randint

seed()

matrixA = [[randint(0,100) for y in range(2)] for x in range(3)]
matrixB = [[randint(0,100) for y in range(2)] for x in range(3)]
matrixC = [[matrixA[x][y] + matrixB[x][y] for y in range(2)] for x in range(3)]
print(matrixA)
print(matrixB)
print(matrixC)