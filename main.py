import turtle


def rectangle(horizontal, vertical, color):
    turtle.pendown()
    turtle.pensize(1)
    turtle.color(color)
    turtle.begin_fill()
    for counter in range(1, 3):
        turtle.forward(horizontal)
        turtle.right(90)
        turtle.forward(vertical)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


turtle.penup()
turtle.speed('slow')
