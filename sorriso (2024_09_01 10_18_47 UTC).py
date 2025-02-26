import turtle

# Configura a tela
screen = turtle.Screen()
screen.bgcolor("white")

# Cria uma tartaruga
pen = turtle.Turtle()
pen.speed(3)

# Função para desenhar um círculo
def draw_circle(color, radius, x, y):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Desenha o rosto
draw_circle("yellow", 100, 0, 0)

# Desenha os olhos
draw_circle("white", 20, -35, 50)
draw_circle("white", 20, 35, 50)

# Desenha as pupilas
draw_circle("black", 10, -35, 60)
draw_circle("black", 10, 35, 60)

# Desenha a boca
pen.penup()
pen.goto(-40, -20)
pen.pendown()
pen.color("black")
pen.right(90)
pen.circle(40, 180)  # Desenha um arco


# Desenha o nariz
pen.penup()
pen.goto(0, -30)
pen.pendown()
pen.color("black")
pen.right(45)
pen.forward(20)
pen.left(90)
pen.forward(40)


# Finaliza
pen.hideturtle()
screen.mainloop()


