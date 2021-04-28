# -*- coding: utf-8 -*-
"""
Mínimos cuadrados

@author: NightRoadIx
"""

import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

# Ingreso de datos
df = pd.read_csv('Datos.csv')
x = np.array(df["x"].tolist(), dtype="float")
y = np.array(df["y"].tolist(), dtype="float")

# Cálculo de los valores
n = len(x)
sumX = sum(x)
sumY = sum(y)
sumXY = sum(x*y)
sumX2 = sum(x**2)
sumY2 = sum(y**2)
medX = sumX / n
medY = sumY / n

# Cálculo de los coeficientes
a1 = (n*sumXY - sumX*sumY) / (n*sumX2 - (sumX**2))
a0 = medY - a1*medX

# Generar el vector con los valores predichos
yPred = a0 +a1*x

# Calcular los criterios de la bondad del ajuste
# Calcular el valor de r
r = (n*sumXY - sumX*sumY) / (np.sqrt(n*sumX2 - (sumX**2))*np.sqrt(n*sumY2 - (sumY**2)))
# Calcular el valor de Sr
Sr = sum((y - a0 - a1*x)**2)

# Obtener la gráfica de los datos
mp.plot(x, y, 'b.')
mp.plot(x, yPred, 'r-')
mp.xlabel('Eje x')
mp.ylabel('Eje y')
mp.grid()
mp.show()

print("Bondad del ajuste")
print("r = {:}".format(round(r,4)))
print("Sr = {:}".format(round(Sr,4)))





