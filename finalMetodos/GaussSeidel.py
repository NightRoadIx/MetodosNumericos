# -*- coding: utf-8 -*-
"""

@author: s_bio
"""

#%%
import numpy as np

# Se genera la función que recibe la matriz A, el vector b y los dígitos de
# precisión d para obtener la solución
# Además, de un "switch" para mostrar información
def GaussSeidel(A, b, d, chou = False):
    # Cantidad de incógnitas
    N = len(b)
    # Se crea un vector X para guardar los datos
    # debe ser del tamaño para calcular las soluciones
    X = np.zeros(N)
    Xant = X.copy()
    
    # Errores (dejar a uno)
    epsilon = np.ones(N)
    
    # contador
    i = 0
    
    # Calcular el error mínimo a partir del dígito de precisión
    epsi = float(1 / (10**d))
    
    # Como colocar para que se repita una y otra vez
    # Tomando en cuenta que el valor máximo del vector de errores sea menor
    # al valor indicado por los dígitos e precisión
    # Y también que no pase de cierto número de iteraciones para que no se
    # cicle
    if chou:
        print("{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t".format('i', 'x1', 'x2', 'x3', 'epsilon1', 'epsilon2', 'epsilon3'))
    while( (max(epsilon) > epsi) and (i < 5000) ):
        
        # Calcular
        for n in range(0, N, 1):   #[0, N)
            # Suma
            suma = 0
            for j in range(0, N):
                if (j != n):
                    suma += A[n][j]*X[j]
            # Ecuación como tal
            X[n] = (b[n] - (suma) ) / A[n][n]
        
        if chou:
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
            for s in range(0,N,1):
                epsilon[s] = np.abs( (X[s] - Xant[s])/X[s] )
        
        # Copiar el vector de soluciones
        Xant = X.copy()
        
        # Incrementar el contador
        i += 1
    
    return X