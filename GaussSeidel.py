# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import numpy as np

'''
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
'''
'''
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

# Ahora pedir la cantidad de dígitos de precisión
while True:
    d = int(input('Ingresar los dígitos de precisión (> 0): '))
    # Verificar que son más de 1 dígito de precisión
    if d > 0:
        break
# Calcular el error mínimo a partir del dígito de precisión
epsi = float(1 / (10**d))

print("{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t{:6}\t".format('i', 'x1', 'x2', 'x3', 'epsilon1', 'epsilon2', 'epsilon3'))
# Como colocar para que se repita una y otra vez
while( max(epsilon) > epsi ):
    
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
    
    # Revisar cuando ya se haya calculado al menos una vez los valores
    if i > 0:
        # Calcular el error
        for s in range(0,N,1):
            epsilon[s] = np.abs( (X[s] - Xant[s])/X[s] )
    
    # Copiar el vector de soluciones
    Xant = X.copy()
    
    # Incrementar el contador
    i += 1
    
print("Las soluciones: ")
print(X)
'''
# Se genera la función que recibe la matriz A, el vector b y los dígitos de
# precisión d para obtener la solución
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

'''
solucion = GaussSeidel(A, b, 5)

print(solucion)
'''