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

# These are the feet of the turtle
turtle.goto(-100, -150)
rectangle(50, 20, 'blue')
turtle.goto(-30, -150)
rectangle(50, 20, 'blue')

# These are the legs of the turtle
turtle.goto(-25, -50)
rectangle(15, 100, 'grey')
turtle.goto(-55, -50)
rectangle(-15, 100, 'grey')

# These are part of the body of the turtle
turtle.goto(-90, 100)
rectangle(100, 150, 'red')

# These are the legs of the turtle
turtle.goto(-150, 70)
rectangle(60, 15, 'grey')
turtle.goto(-150, 110)
rectangle(15, 40, 'grey')

turtle.goto(10, 70)
rectangle(60, 15, 'grey')
turtle.goto(55, 110)
rectangle(15, 40, 'grey')

# This is the neck of the turtle
turtle.goto(-50, 120)
rectangle(15, 20, 'grey')

# This is the head of the turtle
turtle.goto(-85, 170)
rectangle(80, 50, 'red')

# These are the eyes of the turtle
turtle.goto(-60, 160)
rectangle(30, 10, 'white')
turtle.goto(-55, 155)
rectangle(5, 5, 'black')
turtle.goto(-40, 155)
rectangle(5, 5, 'black')

# These are the mouth of the turtle
turtle.goto(-65, 135)
rectangle(40, 5, 'black')
