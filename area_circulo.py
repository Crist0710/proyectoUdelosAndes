# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:24:33 2021

@author: user
"""

def cal_velocidadf(vel_i: float, aceleracion: float, tiempo: float)-> float:
    vel_f = vel_i + (aceleracion*tiempo)
    
    return vel_f

def area_circulo(radio: float)-> float:
    area = 3.1416*(radio**2)
    
    return round(area, 2)


radio_circulo = 2.5

print(area_circulo(radio_circulo))

velocidad_i = 25.5
acel = 5.5
tiempo = 2.5

print(cal_velocidadf(velocidad_i, acel, tiempo))


