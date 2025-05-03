# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:54:57 2025

@author: Duarte Silva
"""

from graphics import *

class Cubo:
    #Define um cubo com a aresta dada
    def __init__(self, aresta):
        self.aresta = float(aresta)

    #Retorna a aresta do cubo
    def getRadius(self):
        print(f'\nA aresta do cubo é {self.aresta:.2f}')

    #Retorna a área da face do cubo
    def faceArea(self):
        area_face = self.aresta ** 2
        print(f'\nA área de uma das face do cubo é {area_face:.2f}')

    #Retorna a área da superfície do cubo
    def surfaceArea(self):
        area_cubo = 6 * (self.aresta ** 2)
        print(f'\nA área da superfície do cubo é {area_cubo:.2f}')

    #Retorna o volume do cubo
    def volume(self):
        volume = self.aresta ** 3
        print(f'\nO volume do cubo é {volume:.2f}')
        

        #Perspetiva isométrica: profundidade inclinação 1:1; 100% de dimensão
    def draw3I(self, win, start_x=70, start_y=220):
        a = self.aresta

        #Face da Frente do cubo
        face_frente = Rectangle(Point(start_x, start_y), Point(start_x + a , start_y - a))
        face_frente.setFill("lightyellow")
        face_frente.draw(win)

        #Face de Cima
        face_cima = Polygon(
            Point(start_x, start_y - a),
            Point(start_x + a, start_y - a),
            Point(start_x + 2*a, start_y - 2*a),
            Point(start_x + a, start_y - 2*a))
        face_cima.setFill("lightblue")
        face_cima.draw(win)

        #Face Lateral Direita
        lateral = Polygon(
            Point(start_x + a, start_y),
            Point(start_x + a, start_y - a),
            Point(start_x + 2*a, start_y - 2*a),
            Point(start_x + 2*a, start_y - a))
        lateral.setFill("lightgreen")
        lateral.draw(win)


        #Perspetiva dimétrica: profundidade inclinação 3:2; 50% de dimensão
    def draw3D(self, win, start_x=290, start_y=200):
        a = self.aresta
        dx, dy = float(1/2 * a * 3/2), - float(1/2 * a)  
        #1/2*a reduz o comprimento da aresta para metade
        #3/2 dá a inclinação às arestas de acordo com a escala

        #Face da Frente do cubo
        frente = Rectangle(Point(start_x, start_y), Point(start_x + a, start_y - a))
        frente.setFill("lightyellow")
        frente.draw(win)

        #Face de Cima
        topo = Polygon(
            Point(start_x, start_y - a),
            Point(start_x + a, start_y - a),
            Point(start_x + a + dx, start_y - a + dy),
            Point(start_x + dx, start_y - a + dy))
        topo.setFill("lightblue")
        topo.draw(win)

        #Face Lateral Direita
        lateral = Polygon(
            Point(start_x + a, start_y),
            Point(start_x + a, start_y - a),
            Point(start_x + a + dx, start_y - a + dy),
            Point(start_x + a + dx, start_y + dy))
        lateral.setFill("lightgreen")
        lateral.draw(win)