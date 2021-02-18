# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:18:55 2021

@author: user
"""

def grados_fahrenheit(celcius: float)-> float:
    
    fahrenheit = (celcius*9/5) + 32
    
    return round(fahrenheit, 1)

temp_actual = float(input("Ingrese la temperatura actual en grados Celcius: "))

temp_fahrenheit = grados_fahrenheit(temp_actual)

print(temp_actual,"° Celcius equivalen a", temp_fahrenheit,"° Fahrenheit")