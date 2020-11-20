import numpy as np

# Resolver el sistema de ecuaciones Ax = b
# Matriz A
A = [[2, -1, 3],
     [2, 2, 3], 
     [-2, 3, 0]]
# Vector b
b = [5,7,-3]

# Convertir de listas a arreglos numpy
A = np.array(A, dtype="float")
b = np.array(b, dtype="float")

# Se puede unir para generar la matriz A|b
C = np.c_[A, b]

# TODO: Est parte debe automatizarse con el uso de for o while
# El truco es hacer las operaciones una a una siguiendo el algoritmo
# Se ataca la primera columna
C[1] = (- C[1][0] / C[0][0]) * C[0] + C[1]
C[2] = (- C[2][0] / C[0][0]) * C[0] + C[2]

# Se ataca la segunda columna
C[2] = (- C[2][1] / C[1][1]) * C[1] + C[2]

# en este punto ya se tiene una matriz triangular

# Se hace la sustitución hacia atrás
# primero se crea un vector del tamaño con las variables
solucion = np.zeros(len(b), dtype="float")
# TODO: Esta sección también de automatizarse
# comenzar la sustitución hacia atrás
solucion[2] = C[2][3] / C[2][2]

solucion[1] = (C[1][3] - (C[1][2] * solucion[2])) / C[1][1]

solucion[0] = (C[0][3] - (C[0][1] * solucion[1] + C[0][2] * solucion[2] ) ) / C[0][0]