# -*- coding: utf-8 -*-
"""

@author: s_bio
"""

# Librerías del entorno gráfico
import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self, datos):
        self.root = tk.Tk()
        # Tamaño de la ventana
        self.root.geometry('200x100')
        
        self.labelTop = tk.Label(self.root, text = "Seleccione un país")
        self.labelTop.grid(column=0, row=0)
        # Mostrar los datos a seleccionar
        self.comboP = ttk.Combobox(self.root, values = datos)
        self.comboP.grid(column=0, row=1)
        self.comboP.current(1)
        
        self.button = tk.Button(self.root, text ="Seleccionar", command=self.seleccion)
        self.button.grid(column=0, row=2)
        
        self.root.mainloop()
    
    def seleccion(self):
        self.respuesta = self.comboP.get()
        self.root.destroy()