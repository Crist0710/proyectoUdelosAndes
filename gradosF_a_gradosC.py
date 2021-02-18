# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 07:43:56 2021

@author: user
"""

def convert_celcius(grados:int)-> float:
    resultado = (grados - 32)*5/9
    
    return resultado

grados_Fahrenheit = int(input("¿Cuantos grados F desea convertir a C? "))

print(convert_celcius(grados_Fahrenheit))