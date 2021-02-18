# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:10:50 2021

@author: user
"""

def velocidad(altura: float)-> float:
    """

    Función pára calcular la velocidad final de un objeto.
    Parametros:
        altura: float
            debe ser un número en decimales
            
    retoro: float
        El valor final de exponer velocidad_f

    """
    
    velocidad_f = (2 * 9.8 * altura)
    velocidad_f = velocidad_f ** (1/2)
    
    return round(velocidad_f, 2)

v_altura = float(input("ingrese la altura de la que cae el objeto: "))
print("la velocidad final del objeto es de: ", (velocidad(v_altura)))