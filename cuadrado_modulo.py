# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:29:20 2021

@author: user
"""

def perimetro_cuadrado(lado: int)-> int:
    perimetro = lado*4
    
    return perimetro

def area_cuadrado(lado: int)-> int:
    area = lado*lado
    
    return area

lado_cuadrado = int(input("Ingrese el valor del lado del cuadrado: "))

print("El perimetro de un cuadrado con lado", lado_cuadrado, "es de: ", perimetro_cuadrado(lado_cuadrado), 
      "y su área es de: ", area_cuadrado(lado_cuadrado))