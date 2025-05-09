from graphics import *

class GrupoGrafico:
    def __init__(self, ancora): # guardamos uma cópia interna do ponto âncora
        self.ancora = Point(ancora.getX(), ancora.getY())
        self.objetos = []

    def retornaAncora(self): # retorna um clone do ponto âncora, e o mesmo é encapsulado
        return Point(self.ancora.getX(), self.ancora.getY())

    def AdicionaObjeto(self, objeto): 
        # adiciona qualquer objeto que suporte move, draw e undraw com o duck typing do python
        self.objetos.append(objeto)

    def move(self, dx, dy): # move o ponto âncora e todos os objetos do grupo
        self.ancora.move(dx, dy)
        for obj in self.objetos:
            obj.move(dx, dy)

    def desenha(self, win): # desenha todos os objetos no GraphWin passado
        for obj in self.objetos:
            obj.draw(win)

    def apaga(self): # remove todos os objetos da janela
        for obj in self.objetos:
            obj.undraw()


def main():
    win = GraphWin("Exemplo de GrupoGráfico", 500, 500)
    win.setCoords(0, 0, 500, 500)

    # 1. criamos o grupo com um ponto âncora inicial
    ancora = Point(250, 250)
    face = GrupoGrafico(ancora)

    # 2. construímos os componentes da cara em volta do ponto âncora
    #    (usando coordenadas absolutas baseadas no ponto âncora)
    cx, cy = ancora.getX(), ancora.getY()
    
    cabeça = Circle(Point(cx, cy), 50)
    cabeça.setFill("yellow")
    face.AdicionaObjeto(cabeça)

    olho_esquerdo = Circle(Point(cx - 15, cy + 10), 8)
    olho_esquerdo.setFill("black")
    olho_direito = Circle(Point(cx + 15, cy + 10), 8)
    olho_direito.setFill("black")
    face.AdicionaObjeto(olho_esquerdo)
    face.AdicionaObjeto(olho_direito)

    boca = Line(Point(cx - 20, cy - 15), Point(cx + 20, cy - 15))
    face.AdicionaObjeto(boca)

    face.desenha(win)

    # 4. a cada clique, desloca o grupo para que o âncora fique na posição do clique
    while True:
        clique = win.getMouse()            # espera o clique
        antiga = face.retornaAncora()      # posição atual do âncora
        dx = clique.getX() - antiga.getX()
        dy = clique.getY() - antiga.getY()
        face.move(dx, dy)

if __name__ == "__main__":
    main()

