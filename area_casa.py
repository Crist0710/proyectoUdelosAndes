# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:24:29 2021

@author: user
"""

def area_cuadrado(lado:int)-> int:
    
    return lado*lado


def area_triangulo(base: int, altura: int)-> float:
    
    return (base*altura)/2


def area_casa(frente: int, techo: int)-> float:
    
    cuadrado = area_cuadrado(frente)
    triangulo = area_triangulo(frente, techo)
    
    return cuadrado + triangulo


medida_frente = 7
medida_techo = 5

resultado = area_casa(medida_frente, medida_techo)

print("El area de una casa con", medida_frente, "metros de frente y un techo de"
      , medida_techo,"metros de alto es: ", round(resultado, 2), "metros")