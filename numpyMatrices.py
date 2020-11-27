import numpy as np

# Python no posee un tipo incorporado de datos para manejar matrices
# por lo que en general se utilizan listas de listas para el manejo 
# de matrices
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

# NOTA: Se debe recordar que las listas en Python inician en el índice 0

# Imprimir la matriz
print("A = ", A)
# Imprimir la segunda fila
print("A[1] = ", A[1])
# Tercer elemento de la segunda fila
# Se maneja [fila][columna]
print("A[1][2] = ", A[1][2])
# También hay que recordar que se puede utilizar índices negativos
# Último elemento de la primera fila
print("A[0][-1] = ", A[0][-1])

#%%
# Asignar una columna de la matriz a una lista
# Se genera una lista vacía
columna = []
# Ahora se recorre sobre toda la lista
for fila in A:
    # Añadir los valores a la lista generada
    columna.append(fila[2])
    # Observar que sucede si se imprime la variable fila
    print(fila)

print("3er columna = ", columna)

#%%
# Esto indica que se puede recorrer sobre toda la matriz o revisar elemento
# por elemento
for fila in A:
    for columna in fila:
        print(" * ", columna)

#%%
# Convertir a un arreglo numpy y del tipo flotante
A2 = np.array(A, dtype = float)
# Verificar 
type(A2)

# Así ya se puede hacer operaciones
A3 = A2 + A2
print(A3)
print("")

# Ahora mostrar una de las filas
print(A3[0])
print("")

# Mostrar una de las columnas
print(A3[:,0])
print("")

# Una forma de obtener una submatriz
print(A3[1:3, 1:3])
print("")

# Generar un vector 
B = np.array([0, 1, 2])
B2 = np.array([0, 1, 2, 3])
# Añadirlo como vector columna a la matriz
A4 = np.c_[A2, B]
# Mostrar
print(A4)

