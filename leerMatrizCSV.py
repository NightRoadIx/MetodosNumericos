import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

# Leer el archivo .csv
df = pd.read_csv('archivo.csv')

# Convertir a un arreglo tipo numpy los datos leídos
# Aquí se leern los valores de la tabla del archivo .csv
# se convierten a una lista y luego se convierten a un arreglo numpy
x2 = np.array(df.values.tolist())
# Obtener el tamaño del arreglo leído (número de filas y columnas)
fil, col = x2.shape

# Obtener la matriz A
A = x2[0:fil, 0:fil]
# Obtener el vector b
b = x2[:,fil]

# A PARTIR DE AQUÍ YA SE PUEDE TRABAJAR CON LA MATRIZ A Y EL VECTOR b