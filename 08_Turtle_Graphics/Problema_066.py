import turtle
import random

turtle.pensize(3)

for i in range(0, 8):
    color = random.choice(["blue", "yellow", "red", "purple", "pink", "green"])
    turtle.color(color)
    turtle.forward(50)
    turtle.right(45)

turtle.hideturtle()
turtle.exitonclick()