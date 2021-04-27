# -*- coding: utf-8 -*-
"""
Método de Gauss-Seidel

@author: NightRoadIx
"""

import numpy as np

# Resolver el sistema de ecuaciones Ax = b
# Matriz A
A = [[3, -0.1, -0.2],
     [0.1, 7, -0.3], 
     [0.3, -0.2, 10]]
# Vector b
b = [7.85, -19.3, 71.4]

# Convertir de listas a arreglos numpy
A = np.array(A, dtype="float")
b = np.array(b, dtype="float")

# Se crea un vector X para guardar los datos
# debe ser del tamaño para calcular las soluciones
X = np.zeros(len(b))
Xant = X.copy()

# Errores (dejar a uno)
epsilon = np.ones(len(b))

# contador
i = 0

# Error o dígitos de precisión
d = 5

print("{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t".format('i', 'x1', 'x2', 'x3', 'epsilon1', 'epsilon2', 'epsilon3'))
# Como colocar para que se repita una y otra vez
while( max(epsilon) > 0.00001 ):
    # Calcular
    X[0] = (b[0] - A[0][1]*X[1] - A[0][2]*X[2]) / A[0][0]
    X[1] = (b[1] - A[1][0]*X[0] - A[1][2]*X[2]) / A[1][1]
    X[2] = (b[2] - A[2][0]*X[0] - A[2][1]*X[1]) / A[2][2]
    
    # Generar un texto con los valores que se van calculando
    print("{:}".format(i), end = "\t")
    
    for tmp in X:
        print("{:6}\t".format( round(tmp, d)), end = "")
    for tmp in epsilon:
        print("{:6}\t".format( round(tmp, d)), end = "")
    
    print("")
    
    # Revisar cuando ya se haya calculado al menos una vez los valores
    if i > 0:
        # Calcular el error
        epsilon[0] = np.abs( (X[0] - Xant[0])/X[0] )
        epsilon[1] = np.abs( (X[1] - Xant[1])/X[1] )
        epsilon[2] = np.abs( (X[2] - Xant[2])/X[2] )
    
    # Copiar el vector de soluciones
    Xant = X.copy()
    
    # Incrementar el contador
    i += 1