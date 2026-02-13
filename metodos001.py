# Librerías a usar
# Pitón numérico, NUMerical PYthon
import numpy as np
# Para graficación matemática
import matplotlib.pyplot as plt

# GRAFICACIÓN
# Crear un vector o arreglo de 100 elementos en el intervalo [0, 5]
x = np.linspace(0, 5, 100)
# Hallar la ecuación a resolver
y = np.exp(-x) - x

# Graficar
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# FUNCIÓN
# y = f(x)
y = lambda x : np.exp(-x) - x

# Intervalo [a, b]
a, b = 0, 5
print(f"Intervalo de búsqueda: [{a:.2f},{b:.2f}]")

# Colocar la precisión buscada
precisión = 1e-2
print(f"Precisión buscada: {precisión:.10f}")

# Iteraciones máximas para evitar que el programa se cicle
k = 100

# Proponer una raíz
x_ant = 1
print("i\ta \tb \txr \terror")
for i in range(k):   #[0, k)
  print(f"{i}\t{a:.4f}\t{b:.4f}\t", end="")
  # Revisar si el intervalo es el bueno
  if y(a) * y(b) < 0:
    # Bisexionar
    m = (a + b) / 2
    # "Octener" el error
    error = abs((m - x_ant)/x_ant)
    # Mostra nueva raíz y el error
    print(f"{m:.4f}\t{error:.4f}")
    # Actualizar la raíz
    x_ant = m
    # Si el error es menor que la precisión, detener
    if error < precisión:
      break
    # Actualizar el intervalo
    if y(a) * y(m) < 0:     # [a, m]
      b = m
    elif y(m) * y(b) < 0:   # [m, b]
      a = m
  else:
    print("El intervalo no es el bueno")
    break
