# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:44:15 2021

@author: user
"""
# 
def zona_oscura(area1: int, area2: float)->float:
    area_final = area1 - area2
    
    return round(area_final, 2)

def area_circulo(lado: int)-> float:
    circulo = 3.1416*(lado/2)**2
    
    return circulo

def area_cuadrado(lado: int)-> int:
    cuadrado = lado*lado
    
    return cuadrado

lado_cuadrado = int(input("ingrese el lado del cuadrado: "))

area_oscura = zona_oscura(area_cuadrado(lado_cuadrado), area_circulo(lado_cuadrado))

print("El área de la zona oscura de un cuadrado con un lado de valor", lado_cuadrado,
      "es de", area_oscura)
