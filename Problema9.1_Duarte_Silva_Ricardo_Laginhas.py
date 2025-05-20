# -*- coding: utf-8 -*-
"""
Created on Mon May 19 23:27:01 2025

@author: duart
"""

from graphics import *

def dentro_do_retangulo(p, retangulo):      #função para ver se o ponto p está dentro do retângulo
    p1 = retangulo.getP1()                  #canto oposto ao canto p2
    p2 = retangulo.getP2()                  #canto oposto ao canto p1
    return (p1.getX() <= p.getX() <= p2.getX()) and (p1.getY() <= p.getY() <= p2.getY())

def regressao_linear(pontos):
    n = len(pontos)     #conta quantos pontos foram fornecidos
    if n < 2:
        return None  #Se forem menos de 2 pontos, não é possível calcular a reta

    sum_x = sum(p.getX() for p in pontos)       #soma dos valores x
    sum_y = sum(p.getY() for p in pontos)       #soma dos valores 
    sum_x2 = sum(p.getX()**2 for p in pontos)   #soma dos quadrados de x
    sum_xy = sum(p.getX()*p.getY() for p in pontos)  #soma da multiplicação de x por y

    #Calcula a média dos valoes
    media_x = sum_x / n
    media_y = sum_y / n

    #Calcula o denominador e numerador para o coeficiente angular da reta
    numerador = sum_xy - n * media_x * media_y
    denominador = sum_x2 - n * media_x**2

    if denominador == 0:
        return None  #Se o denominador for zero, não é possível calcular a reta

    m = numerador / denominador
    b = media_y - m * media_x
    return m, b

def main():
    win = GraphWin("Regressão Linear", 600, 400)        #Cria a janela grafica

    #Cria um retângulo no canto inferior esquerdo
    retangulo = Rectangle(Point(10, 360), Point(110, 390))  
    retangulo.setFill("lightgray")
    retangulo.draw(win)
    Text(retangulo.getCenter(), "Concluído").draw(win)

    pontos = []
    textos = []
    
    while True:     #Espera o clique do usuário
        p = win.getMouse()
        if dentro_do_retangulo(p, retangulo):
            break
        
        # Desenha ponto
        ponto = Circle(p, 3)            #Cria um círculo com centro em p e raio 3
        ponto.setFill("blue")           #Cor do círculo
        ponto.draw(win)                 #Mostrar o círculo na janela
        pontos.append(p)        #Adicioanr o ponto criado à lista pontos

        # Exibe contagem dos pontos
        if textos:
            for t in textos:
                t.undraw()      #Remove o texto da janela para atualizar
            textos.clear()      #Apaga os dados da lista textos
            
        #Contagem dos pontos desenahdos
        contagem = Text(Point(300, 15), f"Pontos coletados: {len(pontos)}")
        contagem.draw(win)
        textos.append(contagem)

    if len(pontos) < 2: #Verifica se há pelo menos 2 pontos senão exige mensagem de erro
        Text(Point(300, 200), "Número insuficiente de pontos para regressão linear.").setTextColor("red").draw(win)
        win.getMouse()
        win.close()
        return

    # Calcula regressão
    resultado = regressao_linear(pontos)
    if resultado is None:
        Text(Point(300, 200), "Erro no cálculo da regressão.").setTextColor("red").draw(win)
        win.getMouse()
        win.close()
        return
    
    m, b = resultado

    # Calcula pontos para a linha da regressão
    x_min, x_max = 0, 600
    y_min, y_max = m * x_min + b, m * x_max + b

    #Cria a reta de regressão com espessura 2
    reta = Line(Point(x_min, y_min), Point(x_max, y_max))
    reta.setOutline("red")
    reta.setWidth(2)
    reta.draw(win)

    # Mensagem final para sair
    Text(Point(300, 380), "Clique para sair").draw(win)
    win.getMouse()
    win.close()

if __name__ == "__main__":      #main() só é executado quando o arquivo for executado diretamente, e não quando fro chamado como módulo
    main()