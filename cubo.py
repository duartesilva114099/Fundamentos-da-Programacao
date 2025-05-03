# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:14:35 2025

@author: Duarte Silva
"""

class Cubo:
    #Define um cubo com a aresta dada
    def __init__(self, aresta):
        self.aresta = eval(aresta)

    # Retorna a aresta do cubo
    def getRadius(self):
        print(f'\nA aresta do cubo é {self.aresta:.2f}')

    # Retorna a área da face do cubo
    def faceArea(self):
        area_face = self.aresta ** 2
        print(f'\nA área de uma das face do cubo é {area_face:.2f}')

    # Retorna a área da superfície do cubo
    def surfaceArea(self):
        area_cubo = 6 * (self.aresta ** 2)
        print(f'\nA área da superfície do cubo é {area_cubo:.2f}')

    # Retorna o volume do cubo
    def volume(self):
        volume = self.aresta ** 3
        print(f'\nO volume do cubo é {volume:.2f}')