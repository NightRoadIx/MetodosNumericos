# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:15:05 2021

@author: NightRoadIx
"""
#%%
import numpy as np

# Resolver el sistema de ecuaciones Ax = b
# TODO: Ingresar los valores por medio de un archivo CSV
# Matriz A
A = [[3, -0.1, -0.2],
     [0.1, 7, -0.3], 
     [0.3, -0.2, 10]]
# Vector b
b = [7.85, -19.3, 71.4]

# Convertir de listas a arreglos numpy
A = np.array(A, dtype="float")
b = np.array(b, dtype="float")

# TODO: Determinar si el sistema tiene solución con el determinante

# TODO: Revisar que los valores de la diagonal, ninguna sea cero
#%%
# Cantidad de incógnitas
N = len(b)
# Se crea un vector X para guardar los datos
# debe ser del tamaño para calcular las soluciones
X = np.zeros(N)
Xant = X.copy()

# Errores (dejar a uno)
epsilon = np.ones(N)

#%%
# contador
i = 0

#TODO: Colocar que el usuario ingrese los dígitos de precisión
# Esto ya esta en el programa de bisección
# Error o dígitos de precisión
d = 5

print("{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t".format('i', 'x1', 'x2', 'x3', 'epsilon1', 'epsilon2', 'epsilon3'))
# Como colocar para que se repita una y otra vez
while( max(epsilon) > 0.00001 ):
    
    # Calcular
    for n in range(0, N, 1):   #[0, N)
        # Suma
        suma = 0
        for j in range(0, N):
            if (j != n):
                suma += A[n][j]*X[j]
        # Ecuación como tal
        X[n] = (b[n] - (suma) ) / A[n][n]
    
    # Generar un texto con los valores que se van calculando
    print("{:}".format(i), end = "\t")
    
    for tmp in X:
        print("{:6}\t".format( round(tmp, d)), end = "")
    for tmp in epsilon:
        print("{:6}\t".format( round(tmp, d)), end = "")
    
    print("")
    
    # TODO: Generalizar la parte de los errores
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
    
print("Las soluciones: ")
print(X)
