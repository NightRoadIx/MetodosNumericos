# -*- coding: utf-8 -*-
"""
Mínimos cuadrados

@author: NightRoadIx
"""

#%%
# Importar la librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import tkinter
from tkinter import filedialog
import sympy as sp

import solMatrix as sm

#%%
# # # # # # # APERTURA DEL ARCHIVO # # # # # # #
# Quitamos la ventana del manejador de GUI Tkinter
root = tkinter.Tk()
# Se cierra
root.withdraw()

# Abre el explorador de archivos y guarda la seleccion en la variable
file_path = filedialog.askopenfilename(title = "Seleccionar archivo CSV", 
                                       filetypes = (("Archivos CSV","*.csv"),
                                                    ("Todos los archivos","*.*")))


#%%
# Leer los datos de un archivo
df = pd.read_csv(file_path)

# Ver los primeros datos de la tabla
print(df.head())

# Obtener los nombres de las columnas
encabeza = list(df.columns.values.tolist())

x = np.array(df["x"].tolist(), dtype="float")
y = np.array(df["y"].tolist(), dtype="float")

#%%
# Aquí mostrar la gráfica de los datos
mp.plot(x,y, 'o', label = "Datos")
mp.xlabel("x")
mp.ylabel("y")
mp.legend()
mp.grid()
mp.show()

#%%
# Obtener el número de datos disponibles
n = len(x)
# Selección de grado de polinomio a ajustar
while True:
    m = int(input('Ingresar el grado del polinomio: '))
    # [1, 8]
    if ( ((m >= 1) and (m <= 8)) and (m < n) ):
        break
    print('Error {:} no esta en el intervalo [1,8]'.format(m) )

#%%
# Una vez que se tiene el grado del polinomio, crear los datos para generar
# el ajuste por mínimos cuadrados
# Generar las sumas de x
equis = []
for tmp in range(1, 2*m+1):
    equis.append( sum(x**tmp) )
# Agregar el valor de n al arreglo
equis.insert(0, n)

# Generar las sumas del producto xy
equisye = []
for tmp in range(0, m+1):
    equisye.append( sum((x**tmp)*y) )

# Medias de x, y
x_med = np.mean(x)
y_med = np.mean(y)

#%%
# Generar el sistema de ecuaciones que se enviará
# Crear la matriz de 0's (m+1) x (m+1)
A = [[0 for tmp in range(m+1)] for tmp2 in range(m+1)]

for tmp1 in range(0, m+1):
    cnt = tmp1
    for tmp2 in range(0, m+1):
        #print(equis[cnt], end=" ")
        A[tmp1][tmp2] = equis[cnt]
        #print(A[tmp1][tmp2], end=" ")
        cnt += 1
    #print("")

# Resolver el sistema    
solucion = sm.resolverMatriz(np.array(A), np.array(equisye))

#%%
# La solución contiene los coeficientes de la ecuación
yPred = 0
i = 0
for tmp in solucion:
    yPred += tmp * (x**i)
    i += 1

#%% 
# Las gráficas finales
mp.plot(x, y, 'b.', label = "Datos")
mp.plot(x, yPred, 'r-', label = "Ajuste")
mp.xlabel('Eje x')
mp.ylabel('Eje y')
mp.legend()
mp.grid()
mp.show()