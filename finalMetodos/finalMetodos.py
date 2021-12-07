# -*- coding: utf-8 -*-
"""

@author: s_bio
"""

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import regresion as rs

# Cargar la información en Python
df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

# Obtener los nombres de las columnas
nombreColumnas = list(df.columns)

# Lista de los países
paises = list( df["location"].unique() )


#%%
# Obtener los datos de un solo país en particular

particular = df[ df["location"] == 'Mexico' ].fillna(0)

#%%

# Fechas
fechas = particular["date"].tolist()
# Datos numéricos del total
x = np.array([tmp for tmp in range(len(fechas))])
# Obtener los casos totales de Coronavirus
casosTotales = np.array(particular["total_cases"])

#%%
# Graficar con los números
plt.plot(fechas, casosTotales, 'b-')
plt.xticks(ticks = fechas[::50], rotation=80)
plt.grid()
plt.show()

#%%
# Graficar con las fechas
plt.plot(fechas, casosTotales, 'b-')
plt.xticks(ticks = fechas[::50], rotation=80)
plt.grid()
plt.show()

#%%
# Obtener la regresión polinomial con m = 1
coef, yPred, r, Sr, Syx = rs.regresion(x[0:50], casosTotales[500:550], 1)

# Graficar los datos
plt.plot(fechas[500:550], casosTotales[500:550], 'b-')
plt.plot(fechas[500:550], yPred, 'r-')
plt.xticks(ticks = fechas[500:550:5], rotation=80)
plt.grid()
plt.show()

# Pendiente de crecimiento
print("Crecimiento: {}".format(coef[1]))
# Hallar el ángulo de crecimiento
# La función tangente regresa el valor en radianes, por lo que se
# utiliza degrees para obtener el valor en grados
print("Ángulo: {}°".format(np.degrees(np.arctan(coef[1]))))








