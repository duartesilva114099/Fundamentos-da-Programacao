# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:34:16 2025

@author: Duarte Silva
"""

from graphics import*
from cubo_perspetivas import Cubo

def main():
    win = GraphWin("Cubo Isométrico e Dimétrico", 500, 300)
    cubo = Cubo(80)

    cubo.draw3I(win)
    cubo.draw3D(win)

    Text(Point(250, 280), "Clique para sair").draw(win)
    win.getMouse()
    win.close()

main()