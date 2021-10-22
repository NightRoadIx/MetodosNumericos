# -*- coding: utf-8 -*-
"""
Creado por mi

"""

import numpy as np
import matplotlib.pyplot as mp

# TODO: Cambiar a leer por un archivo CSV

# Estos son los datos a analizar
# Recuerden que estos datos NO son lineales
x = np.array([1,2,3,4,5], dtype="float")
y = np.array([0.5, 1.7, 3.4, 5.7, 8.4], dtype="float")

# Armar y Mostrar la gráfica
# Esto solamente muestra los puntos de los datos
mp.plot(x, y, "r.")
# Títulos de los ejes
mp.xlabel("x")
mp.ylabel("y")
# Se coloca una rejilla en la gráfica
mp.grid()
# Mostrar la gráfica
mp.show()

# TODO: Aquí deben de colocar un menú donde se pueda seleccionar
# que tipo de transformación se va a hacer
# Pueden revisar:
# https://www.it-swarm-es.com/es/python/crear-un-menu-en-python/1043095475/

# Este es la transformación que se observó en el ejemplo
# La transformación se realiza para una ecuación de potencias
# Transformar el eje x
# Recordar que se tiene que hacer la transformación con logaritmo base10
x_new = np.log10(x)     # Esto efectua el log10 en cada elemento del vector
# Transformar el eje y
y_new = np.log10(y)

# Aquí ya se tienen las nuevas cantidades, entonces podrán ver
# que esto ya se torno lineal
mp.plot(x_new, y_new, "b.")
mp.xlabel("log10(x)")
mp.ylabel("log10(y)")
mp.grid()
mp.show()

# Se calculan los valores de la regresión lineal #
n = len(x_new)
sumX = sum(x_new)
sumY = sum(y_new)
sumXY = sum(x_new*y_new)
sumX2 = sum(x_new**2)
sumY2 = sum(y_new**2)
medX = sumX / n
medY = sumY / n

# Cálculo de los coeficientes
a1 = (n*sumXY - sumX*sumY) / (n*sumX2 - (sumX**2))
a0 = medY - a1*medX

# Generar el vector con los valores predichos
# OJO: Revisar que todo es con los x, y nuevos
y_newPred = a0 +a1*x_new

# Calcular los criterios de la bondad del ajuste
# Calcular el valor de r
r = (n*sumXY - sumX*sumY) / (np.sqrt(n*sumX2 - (sumX**2))*np.sqrt(n*sumY2 - (sumY**2)))
# Calcular el valor de Sr
Sr = sum((y_new - a0 - a1*x_new)**2)

# Obtener la gráfica de los datos
# OJO: Este es de los datos "transformados"
mp.plot(x_new, y_new, 'b.')
mp.plot(x_new, y_newPred, 'r-')
mp.xlabel('log10(x)')
mp.ylabel('log10(y)')
mp.grid()
mp.show()

print("Bondad del ajuste")
print("r = {:}".format(round(r,4)))
print("Sr = {:}".format(round(Sr,4)))

# Aquí termina el método #

# Ahora, se tiene que ir de vuelta, y "destransformar" los datos
# En este caso la ecuación original es y = alfa x^beta
alfa = 10**a0
beta = a1

# Obtener el Ypredicho con los datos "originales"
yPred = alfa * x**beta

# Graficar, ahora si los datos "originales"
mp.plot(x, y, 'r.')
mp.plot(x, yPred, 'b-')
mp.xlabel('x')
mp.ylabel('y')
mp.grid()
mp.show()
