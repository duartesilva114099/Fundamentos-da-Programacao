# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:57:12 2025

@author: Duarte Silva
"""

from cubo import Cubo

def main():
    aresta = input("Introduza a aresta do cubo: ")
    cubo = Cubo(aresta)

    cubo.getRadius()
    cubo.faceArea()
    cubo.surfaceArea()
    cubo.volume()

main()