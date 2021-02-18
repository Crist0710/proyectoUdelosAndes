# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 07:58:08 2021

@author: user
"""

def convertir_fahrenheit(grados: int)-> float:
    resultado = (grados*9/5) + 32
    
    return round(resultado, 1)

grados_celcius = int(input("¿Cuantos grados C desea convertir a grados F? "))

print(grados_celcius, "grados Celcius equivalen a", (convertir_fahrenheit(grados_celcius)), "grados Fahrenheit")