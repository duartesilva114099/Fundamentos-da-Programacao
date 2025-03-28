from graphics import *
import time

def main():
    win = GraphWin("Bola em Movimento", 500, 500)
    win.setBackground("white")
    
    raio = 20
    x, y = 250, 250  # Começa no meio
    bola = Circle(Point(x, y), raio)
    bola.setFill("blue")
    bola.draw(win)
    
    dx, dy = 13, 20
    
    while True:
        bola.move(dx, dy)
        centro = bola.getCenter()
        x, y = centro.getX(), centro.getY()
        
        if x + raio >= 500 or x - raio <= 0:
            dx = -dx
        if y + raio >= 500 or y - raio <= 0:
            dy = -dy
        
        update(30)
        time.sleep(0.01)
    
    win.getMouse()
    win.close()

main()
