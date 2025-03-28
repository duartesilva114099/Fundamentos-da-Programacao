# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 14:41:34 2025

@author: Duarte Silva
"""

#Problema 4.2

from graphics import *

def rosto():
    win = GraphWin ("Face feliz", 500, 500)
    
    cabeca = Circle(Point(250,250),150)          #Desenhar a cabeça
    cabeca.setFill("#CD853F")
    cabeca.draw(win)
    
    nariz = Polygon(Point(250, 200), Point(220, 270), Point(280, 270))    #Desenhar o nariz
    nariz.setFill("orange")
    nariz.draw(win)
    
    olho_esq = Circle(Point(200, 180), 40)       #Desenhar os olhos
    olho_esq.setFill("white")
    olho_esq.draw(win)

    olho_dir = Circle(Point(300, 180), 40)
    olho_dir.setFill("white")
    olho_dir.draw(win)
    
    pupila_esq = Circle(Point(200, 180), 10)      #Desenhar as pupilas   
    pupila_esq.setFill("black")
    pupila_esq.draw(win)
    pupila_dir = Circle(Point(300, 180), 10)
    pupila_dir.setFill("black")
    pupila_dir.draw(win)
    
    boca = Oval(Point(180, 380), Point(320, 320))      #Desenhar a boca
    boca.setFill("red")
    boca.draw(win)
    
    win.getMouse()
    win.close()
    
rosto()
input("\n---------Prima enter para fechar o programa---------")
