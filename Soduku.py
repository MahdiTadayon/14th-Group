# Draw 9 x 9 Soduku

import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(1)
pensize_list = [3,1,1]

initial_x = -200
initial_y = -200
cell_width = 40
turtle.penup()
soduku_size = 9

for _ in range(10):
    turtle.goto(initial_x, initial_y + (_ * cell_width))
    turtle.pensize(5 if _ % 9 ==0 else pensize_list[_ % 3])
    turtle.pendown()
    turtle.forward(cell_width * soduku_size)
    turtle.penup()

turtle.right(270)

for _ in range(10):
    turtle.goto(initial_x + (_ * cell_width), initial_y)
    turtle.pensize(5 if _ % 9 ==0 else pensize_list[_ % 3])
    turtle.pendown()
    turtle.forward(cell_width * soduku_size)
    turtle.penup()

turtle.done()