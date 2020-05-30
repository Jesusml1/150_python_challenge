import turtle

for i in range(0, 20):
    turtle.right(36)
    for i in range(0, 8):
        turtle.forward(50)
        turtle.right(45)

turtle.hideturtle()
turtle.exitonclick()