from graphics import *
import random

def main():
    win = GraphWin("Jogo Monte", 400, 300)
    win.setCoords(0, 0, 400, 300)

    # Draw buttons as rectangles and labels
    buttons = []
    labels = ["Porta 1", "Porta 2", "Porta 3"]
    button_width = 100
    button_height = 50
    spacing = 20
    start_x = 50
    y = 150

    for i in range(3):
        x1 = start_x + i*(button_width + spacing)
        rect = Rectangle(Point(x1, y), Point(x1 + button_width, y + button_height))
        rect.setFill("lightgray")
        rect.draw(win)
        
        label = Text(rect.getCenter(), labels[i])
        label.setSize(14)
        label.draw(win)

        buttons.append((rect, labels[i]))

    # Randomly select the winning door
    winning_index = random.randint(0, 2)
    winning_label = labels[winning_index]

    # Instructions
    instructions = Text(Point(200, 250), "Clica numa das portas!")
    instructions.setSize(16)
    instructions.draw(win)

    # Wait for user click and detect which button clicked
    while True:
        click = win.getMouse()
        x, y_click = click.getX(), click.getY()

        clicked_index = None
        for i, (rect, label) in enumerate(buttons):
            p1 = rect.getP1()
            p2 = rect.getP2()
            if p1.getX() <= x <= p2.getX() and p1.getY() <= y_click <= p2.getY():
                clicked_index = i
                break

        if clicked_index is not None:
            break  # Valid button clicked, exit loop and check win/loss

    # Clear instructions text
    instructions.undraw()

    # Show result message
    if clicked_index == winning_index:
        result_msg = Text(Point(200, 250), "Ganhaste! 🎉")
    else:
        result_msg = Text(Point(200, 250), f"Perdeste! A porta correta era a porta {winning_label}.")
    result_msg.setSize(16)
    result_msg.setTextColor("red" if clicked_index != winning_index else "green")
    result_msg.draw(win)

    # Highlight the winning door (green)
    buttons[winning_index][0].setFill("lightgreen")
    # Highlight the clicked door (red if lost)
    if clicked_index != winning_index:
        buttons[clicked_index][0].setFill("red")

    # Prompt user to click anywhere to close
    close_msg = Text(Point(200, 30), "Clica em algum lugar para sair")
    close_msg.setSize(12)
    close_msg.draw(win)

    win.getMouse()
    win.close()

main()
