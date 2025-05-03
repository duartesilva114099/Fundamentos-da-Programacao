# -*- coding: utf-8 -*-
"""
Created on Fri May  2 10:21:02 2025

@author: Duarte Silva
"""

class Esfera:
    #Cria uma esfera com o raio pedido
    def __init__(self, radius):
        self.radius = float(radius)

    #Retorna o raio da esfera
    def getRadius(self):
        print(f'\nO raio da esfera é {self.radius:.2f}')

    #Retorna a área da superfície da esfera
    def surfaceArea(self):
        area_superficie = 4 * 3.14159 * (self.radius ** 2)
        print(f'\nA área da superfície da esfera é {area_superficie:.2f}')

    #Retorna o volume da esfera
    def volume(self):
        volume = (4 / 3) * 3.14159 * (self.radius ** 3)
        print(f'\nO volume da esfera é {volume:.2f}')