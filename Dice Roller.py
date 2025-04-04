# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 15:42:05 2025

@author: duart
"""

from graphics import GraphWin, Point
from random import randrange
from botaocirc import Botaocircular
from dieview import DieView

def main():
    #create the application window
    win = GraphWin("Dice Roller", 500, 500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    #Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollBotaocircular = Botaocircular(win, Point(3, 3), 1, "Roll Dice")
    rollBotaocircular.activate()
    quitBotaocircular = Botaocircular(win, Point(7, 3), 1, "Quit")

    #Event loop
    pt = win.getMouse()
    while not quitBotaocircular.clicked(pt):
        if rollBotaocircular.clicked(pt):
                value1 = randrange(1, 7)
                die1.setValue(value1)
                value2 = randrange(1, 7)
                die2.setValue(value2)
                quitBotaocircular.activate()
        pt = win.getMouse()

    #close up shop
    win.close()

main()