# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 07:52:20 2021

@author: user
"""

def convert_fahrenheit(grados:int)-> float:
    resultado = (grados*9/5)+32
    
    return resultado

grados_Celcius = int(input("¿Cuantos grados C desea convertir a F? "))

print(convert_fahrenheit(grados_Celcius))