# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 08:10:31 2021

@author: user
"""

def convertir(dia: int):
    """ Calcula la cantidad de días, meses y años a partir del valor día.

    Parametros:
        dia (int): La cantidad de días ingresados.
                   debe ser un número entero.
                   
    Retorno:
        (int): solo en el caso de días, ya que el valor se mantiene.
        
        (float): se valor que retorne, será siempre decimal.

    """

    resul_dias = dia
    resul_mes = dia / 30
    resul_año = dia / 365
    
    return resul_dias, round(resul_mes, 1), round(resul_año, 1)

dias = int(input("ingrese la cantidad de días: "))

print(dias, "días equivalen en días/meses/años asi: ", (convertir(dias)))

help(convertir)
