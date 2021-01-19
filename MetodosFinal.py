#%%
# Importar la librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import sympy as sp
import tkinter
from tkinter import filedialog

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

# Convertir valores a arreglos numpy
x = np.array( (df[encabeza[0]].values.tolist()), dtype=np.float64 )
y = np.array( (df[encabeza[1]].values.tolist()), dtype=np.float64 )

# AQUI VA LA SELECCION

#%%
# # # # # # # MINIMOS CUADRADOS # # # # # # #
# Calcular la cantidades
n = len (x)
sumax= sum(x)
sumay= sum(y)
sumax2 = sum(x*x)
sumay2 = sum(y*y)
sumaxy = sum(x*y)
promx = sumax / n
promy = sumay / n

# Aplicar las ecuaciones para el calculo de a0 y a1
a1 = ( n*sumaxy - sumax*sumay )/( n*sumax2 - sumax**2 )
a0 = promy - a1*promx

# Generar la ecuacion
xsim = sp.Symbol('x')
ysim = a0 + a1*xsim

print("Ecuacion generada")
sp.pretty_print(ysim)

# Generar los vectores de ajuste
yajuste = a0 + a1*x

# Hallar los errores del ajuste
Sr = sum((y - yajuste)**2)
St = sum( (y - promy)**2 )
Sy_x = np.sqrt(Sr/(n-2))
rcuad = (St - Sr)/St

print("Valor de Sy/x: ", Sy_x)
print("Valor de r   : ", np.sqrt(rcuad))

#%%
# # # # # # # GRAFICACION # # # # # # #
mp.plot(x,y, 'o', label = "Datos")
mp.plot(x, yajuste, label = "Ajuste")
mp.xlabel("x")
mp.ylabel("y")
mp.legend()
mp.show()

#%%
opciones = ["1.-Lineal", 
            "2.-Exponencial",
            "3.-Potencias",
            "4.-Crecimiento",
            "5.-Sigmoidal",
            ]

while True:
    # Mostrar el menu al usuario
    for tmp in opciones:
        print(tmp)
    opc = int(input("Seleccion -> "))
    if opc >= 1 and opc <= 5:
        break

if opc == 1:
    print("Minimos cuadrados de manera lineal")
if opc == 2:
    print("Minimos cuadrados de manera exponencial")
if opc == 3:
    print("Minimos cuadrados de manera de ecuacion de potencias")
if opc == 4:
    print("Minimos cuadrados de manera de crecimiento poblacional")
if opc == 5:
    print("Minimos cuadrados de manera sigmoidal")

# Realizar lo de minimos cuadrados