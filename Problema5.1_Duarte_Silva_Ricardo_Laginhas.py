from graphics import *

def main():
    win = GraphWin("Bola em Movimento", 500, 500)
    win.setBackground("white")
    
    bola = Circle(Point(250, 250), 20)
    bola.setFill("blue")
    bola.draw(win)
    
    raio = 20
    dx, dy = 13, 20
    
    while True:
        if win.checkMouse():      #Se o utilizador clicar, sai
            break
        
        bola.move(dx, dy)
        centro = bola.getCenter()
        
        if centro.getX() + raio >= 500 or centro.getX() - raio <= 0:
            dx = -dx
        if centro.getY() + raio >= 500 or centro.getY() - raio <= 0:
            dy = -dy
        
        update(60)
        
    win.close()

main()
