# -*- coding: utf-8 -*-
"""
@author: NightRoadIx
"""

# Manejo de grandes cantidades de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

# Cargar el enlace a descargar
enlace = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
# Mi recomendación es bajar el archivo y colocar después la dirección local
# donde se encuentra el archivo

# Obtener los datos directamente con la librería pandas
df = pd.read_csv(enlace)

#%%

# Obtener la lista de los países disponiblees
listaPaises = df["location"].unique().astype(str).tolist()

# Pedir al usuario que escoja algún país
while True:
    # Ingresar datos
    pais = input("País a analizar: ")
    # comparar si la cadena se encuentra en la lista
    if pais in listaPaises:
        # Crear la cadena de análisis
        # fillna(0) funciona para rellenar los valores que están como NA 
        # (esto es que no existen o tienen algún valor) con 0
        subdf = df[df['location'] == pais].fillna(0)
        break
    print("<El país no fue hallado>")
    
# Una vez hallado el país, se procede a analizar
# Por ejemplo, ver el total de casos
# Para un mejor análisis, se convierte en un arreglo numpy
y = np.array(subdf['total_cases'].tolist())

#%%
# Graficar entonces estos valores
mp.plot(y, 'r-')
mp.xlabel('Datos')
mp.ylabel('Total Casos')
mp.grid()
mp.show()

#%%
# Obtener un "pedazo de los datos"
mp.plot(y[400:500], 'r-')
mp.xlabel('Datos')
mp.ylabel('Total Casos')
mp.grid()
mp.show()

