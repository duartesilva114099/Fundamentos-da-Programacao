# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:11:27 2025

@author: Duarte Silva
"""

from graphics import *
from math import sin, cos, pi

def main():
    
    escala = 5 #1 metro= 5 pixeis
    
    #Criar a janela
    win = GraphWin("Bala de canhão", 900, 500)
    win.setBackground("white")

    #Texto de entrada
    Text(Point(150, 20),"Insira o ângulo de lançamento em graus:").draw(win)
    angulo = Entry(Point(310, 22), 3)
    angulo.draw(win)
    angulo.setText("45")
    
    Text(Point(93, 50), "Velocidade inicial (m/s):").draw(win)
    velocidade = Entry(Point(195, 52), 3)
    velocidade.setText("40")
    velocidade.draw(win)
    
    Text(Point(67, 80), "Altura inicial (m):").draw(win)
    altura = Entry(Point(145, 82), 3)
    altura.setText("0")
    altura.draw(win)
    
    Text(Point(188, 110), "Intervalo de tempo entre os cálculos de posição (s):").draw(win)
    tempo = Entry(Point(388, 112), 4)
    tempo.setText("0.05")
    tempo.draw(win)
    
    # Botão para começar
    disparar = Rectangle(Point(600, 60), Point(700, 100))
    disparar.setFill("red")
    disparar.draw(win)
    texto_disparar = Text(Point(650, 80), "Disparar").draw(win)
    
    #Botão para sair
    botao_sair = Rectangle(Point(380, 450), Point (520, 490))
    botao_sair.setFill("lightgrey")
    botao_sair.draw(win)
    Text(Point(450, 470), "Clique para sair").draw(win)
    
    bala = None
    distancia = None

    while True: 
        #Clique exatamente dentro do botão disparar
        while True:
            clique = win.getMouse()     #Começa após clicar
            if 600 <= clique.getX() <= 700 and 60 <= clique.getY() <=100:
                break #clicar dentro do botão
                
                #Apenas fecha a janela se clicarem dentro do botão sair
            elif 380 <= clique.getX() <= 520 and 450 <= clique.getY() <= 490:
                win.close()
                return #terminar o programa     
        
        if bala:                    #apagar balas
            bala.undraw()
           
        if distancia:
            distancia.undraw()      #Apagar valores anteriores da distância percorrida
            
        #Lê o valor que o utilizador quer
        angulo_escolhido = float(angulo.getText())
        velocidade_escolhida = float(velocidade.getText())
        altura_escolhida = float(altura.getText())    
        tempo_escolhido = float(tempo.getText())   
        
        radianos = (angulo_escolhido * pi)/180      # Converte o ângulo para radianos
        
        #Posições e velocidades iniciais
        posicao_x = 0
        posicao_y = altura_escolhida
        velocidade_x = velocidade_escolhida * cos(radianos)
        velocidade_y = velocidade_escolhida * sin(radianos)
        
        #Desenhar o solo
        solo = Line(Point(0, 300), Point(900, 300))
        solo.draw(win)
        
        bala = Circle(Point(posicao_x, 300 - posicao_y * escala), 5)  #Cria a bala na posição inicial
        bala.setFill("black")
        bala.draw(win)
        
        #Disparo animado da bola
        while posicao_y >= 0 and posicao_x < 900/escala:     #A bola está acima do solo e dentro da janela 
            #Posição vai atualizando
            ultimo_x = posicao_x
            ultimo_y = posicao_y
            
            posicao_x += velocidade_x * tempo_escolhido
            nova_velocidade_y = velocidade_y - tempo_escolhido * 9.81     #Velocidade vertical menos aceleração gravítica
            posicao_y += tempo_escolhido * (velocidade_y + nova_velocidade_y)/2
            velocidade_y = nova_velocidade_y
            
            dx = posicao_x - ultimo_x
            dy = posicao_y - ultimo_y
            
            bala.move(dx * escala,-dy * escala) #Dá o movimento à bala   
            
            update(35)  #número de frames por segundo
            
        distancia = Text(Point(450, 420), f"Distancia percorrida: {posicao_x:.1f} m")
        distancia.setTextColor("Blue")
        distancia.draw(win)

main()        