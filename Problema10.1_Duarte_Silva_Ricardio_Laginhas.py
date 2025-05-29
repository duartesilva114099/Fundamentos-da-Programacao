from graphics import *
import random

def main():
    # Criar janela gráfica com título e dimensões específicas
    win = GraphWin("Jogo Monte", 400, 300)
    win.setCoords(0, 0, 400, 300)  # Definir sistema de coordenadas para facilitar posicionamento

    buttons = []
    labels = ["Porta 1", "Porta 2", "Porta 3"]
    button_width = 100
    button_height = 50
    spacing = 20
    start_x = 50
    y = 150

    # Criar 3 botões retangulares com seus respectivos rótulos posicionados horizontalmente
    for i in range(3):
        x1 = start_x + i*(button_width + spacing)
        rect = Rectangle(Point(x1, y), Point(x1 + button_width, y + button_height))
        rect.setFill("lightgray")
        rect.draw(win)
        
        label = Text(rect.getCenter(), labels[i])
        label.setSize(14)
        label.draw(win)

        # Guardar o retângulo e o texto para detectar cliques e manipular depois
        buttons.append((rect, labels[i]))

    # Escolher aleatoriamente qual porta será a vencedora
    winning_index = random.randint(0, 2)
    winning_label = labels[winning_index]

    # Texto de instruções para o utilizador no topo da janela
    instructions = Text(Point(200, 250), "Clica numa das portas!")
    instructions.setSize(16)
    instructions.draw(win)

    # Loop para detectar clique do utilizador e identificar qual porta foi clicada
    while True:
        click = win.getMouse()
        x, y_click = click.getX(), click.getY()

        clicked_index = None
        # Verificar em qual botão o clique ocorreu comparando coordenadas do clique com o retângulo
        for i, (rect, label) in enumerate(buttons):
            p1 = rect.getP1()
            p2 = rect.getP2()
            if p1.getX() <= x <= p2.getX() and p1.getY() <= y_click <= p2.getY():
                clicked_index = i
                break

        if clicked_index is not None:
            break  # Parar o loop quando um botão válido for clicado

    instructions.undraw()  # Remover as instruções após o clique válido

    # Mostrar mensagem de resultado conforme o botão clicado ser o vencedor ou não
    if clicked_index == winning_index:
        result_msg = Text(Point(200, 250), "Ganhaste! 🎉")
    else:
        result_msg = Text(Point(200, 250), f"Perdeste! A porta correta era a porta {winning_label}.")
    result_msg.setSize(16)
    # Cor do texto verde se ganhou, vermelho se perdeu
    result_msg.setTextColor("red" if clicked_index != winning_index else "green")
    result_msg.draw(win)

    # Destacar visualmente a porta vencedora em verde
    buttons[winning_index][0].setFill("lightgreen")
    # Se perdeu, destacar a porta clicada em vermelho para feedback
    if clicked_index != winning_index:
        buttons[clicked_index][0].setFill("red")

    # Mensagem para indicar que o utilizador pode clicar para fechar a janela
    close_msg = Text(Point(200, 30), "Clica em algum lugar para sair")
    close_msg.setSize(12)
    close_msg.draw(win)

    win.getMouse()  # Esperar clique final para fechar
    win.close()

main()

