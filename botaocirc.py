# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 14:36:10 2025

@author: duart
"""
#botaocirc.py

from graphics import *

class BotaoCircular:
    #Botão circular com funcionalidades similares à classe Button
    
    def __init__(self, win, centro, raio, etiqueta):
        #Criar botão circular      
        self.win = win
        self.centro = centro
        self.raio = raio
        
        self.circle = Circle(centro, raio)   #Desenhar o botão
        self.circle.setFill('gray')          #Cor de preenchimento do botão desativado
        self.circle.draw(win)
        
        self.etiqueta = Text(centro, etiqueta)     #Desenhar a etiqueta
        self.etiqueta.draw(win)
        
        self.deactivate()   #Desativa o botão imediatamente a seguir a ser criado
    
    def clicked(self, p):
        #Retorna True se o botão estiver ativo e p estiver dentro do círculo (equação da distância entre 2 pontos no plano)
        return (self.active and 
               (p.getX() - self.centro.getX())**2 + (p.getY() - self.centro.getY())**2 <= self.raio**2) 
    
    
    def getLabel(self):
        #Mostra a etiqueta do botão
        return self.etiqueta.getText()
    
    def activate(self):
        #Ativa o botão
        self.etiqueta.setFill('black')  #Etiqueta fica preta
        self.circle.setWidth(2)     #Borda do botão circular fica mais espessa
        self.active = True
    
    def deactivate(self):
        #Desativa o botão
        self.etiqueta.setFill('darkgrey')   #Etiqueta fica cinzenta escura
        self.circle.setWidth(1)         #Borda do botão fica menos espessa
        self.active = False

    def update(self, etiqueta):
        self.etiqueta.setText(etiqueta)  # Atualiza o texto sem recriar o objeto sem precisar remover ou desenhar de novo
