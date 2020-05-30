import random
import turtle

lines = random.randint(0, 100)
linesLength = random.randint(0, 100)
angle = random.randint(0, 360)

for i in range(0, lines):
    turtle.forward(linesLength)
    turtle.right(angle)

turtle.exitonclick()