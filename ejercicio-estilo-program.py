# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:40:11 2021

@author: user
"""

def valor_circulo(radio: float, area: float)-> float:
    """

    Función pára calcular el valor de un circulo.
    Parametros:
        radio: float
            debe ser un número en decimales
        área: float
            debe ser un número en decimales
            
    retoro: float
        El valor final de multiplicar base por área

    """
    
    base = 3.1416 * (radio**2)
    
    return round(base * area, 2)

valor_radio = 2
valor_area = 4

print(valor_circulo(valor_radio, valor_area))