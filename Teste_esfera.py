# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:01:28 2025

@author: Duarte Silva
"""

from esfera import Esfera

def main():
    radius = input("Introduza o raio da esfera: ")
    teste_esfera = Esfera(radius)

    teste_esfera.getRadius()
    teste_esfera.surfaceArea()
    teste_esfera.volume()

main()