import tkinter as tk


def left_click(event):
    global points_clicked
    points_clicked.append((event.x, event.y))
    if len(points_clicked) == 2:
        draw_rectangle(points_clicked)
        calculate_data(points_clicked)
        points_clicked = []


def draw_rectangle(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    canvas.delete("all")
    canvas.create_rectangle(x1, y1, x2, y2, outline="white", width=1)


def calculate_data(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    width, height = abs(x2 - x1), abs(y2 - y1)
    label.config(text=f"Perímetro = {2 * (width + height)} pixeis  |  Área = {width * height} pixeis quadrados")


points_clicked = []

app = tk.Tk()
app.state('zoomed')
app.title("Desenhar Retângulos")

canvas = tk.Canvas(app, bg="black")
canvas.pack(fill="both", expand=True)
canvas.bind("<Button-1>", left_click)

label = tk.Label(app, text="Carrega em dois pontos para desenhar um retângulo.")
label.pack()

app.mainloop()