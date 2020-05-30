import turtle

# turtle.shape("arrow")
# Tres cuadrados seguidos

turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()


turtle.penup()
turtle.forward(75)
turtle.pendown()

turtle.color("black", "blue")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()


turtle.penup()
turtle.forward(75)
turtle.pendown()

turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()


turtle.exitonclick()