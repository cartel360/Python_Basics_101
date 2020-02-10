import turtle

sides = 8
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360/sides)
    for steps in range(sides):
        turtle.forward(50)
        turtle.right(360/sides)
