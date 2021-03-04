import numpy as np
import matplotlib.pyplot as plt

# Definir la función factorial para el cálculo del mismo
# Recibe el número a calcular
def factorial(n):
    resultado = 1
    if n >= 1:
        for i in range(1, n+1):
            resultado *= i
    return resultado


# Ingreso de datos
print("*** Serie de Taylor para aproximar exp(x) ***")
terminos = int(input("Cuantos términos: "))
x = float(input("Valor de x: "))

# Se inicia el valor de la aproximación a cero
aproximacion = 0
# Aquí se va a efectuar la suma de los términos que va de 0 a n
for tmp in range(0, terminos):
    # Con esto se va acumulando la aproximación
    aproximacion += (x**tmp) / factorial(tmp)
    # y aquí se muestran los términos generados
    # sólo para observalos
    print("x^" + str(tmp) + " / " + str(tmp) + "!")

# Y se muestra entonces los valores aproximados y real
print("Valor de aproximación: {:4.4}".format(aproximacion))
print("Valor real: {:4.4}".format( np.exp(x) ) )