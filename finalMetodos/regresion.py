# -*- coding: utf-8 -*-
"""

@author: s_bio
"""

# Archivo con los métodos numéricos para regresión

# Librerías requeridas
import numpy as np
import GaussSeidel as gs

# Regresión polinomial por mínimos cuadrados
def regresion(x, y, m):
    # Datos de ingreso a la matriz
    n = len(x)
    
    sumX = np.zeros(2*m)
    for g in range(2*m):
        sumX[g] = sum(x**(g+1))

    # Insertar n en la posición inicial de sumX
    sumX = np.insert(sumX, 0, n)

    sumXY = np.zeros(m+1)
    for g in range(m+1):
        sumXY[g] = sum((x**g)*y)

    medX = sumX[0] / n
    medY = sumXY[0] / n

    # Con estos datos se genera la matriz y el vector
    A = np.zeros([m+1, m+1])
    for g in range(m+1):
        for s in range(m+1):
            A[g][s] = sumX[s+g]

    b = np.array(sumXY, dtype="float")

    # Enviar la información al programa de solución y obtener los resultados
    coef = gs.GaussSeidel(A, b, 9, False)

    # Con estos coeficientes se obtiene la ecuación
    yPred = 0
    for s in range(0, m+1, 1):
        yPred += coef[s] * x**s
        
    # Bondades del ajuste
    Sr = sum((y - yPred)**2)
    St = sum((y - medY)**2)
    Syx = np.sqrt( Sr/(n-(m+1)) )
    r2 = (St - Sr)/St
    r = np.sqrt(r2)
    
    return (coef, yPred, r, Sr, Syx)
