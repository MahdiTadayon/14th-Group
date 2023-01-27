# Drow 9*9 soduko
import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.up()
turtle.goto(-200, 200)
x, y = turtle.position()
turtle.down()
#drow row
row_num = 0
for row in range(10):
    row_num += 1
    turtle.pensize(5) if row in range(0, 10, 9) else turtle.pensize(3) if row in range(0, 9, 3) else turtle.pensize(1)
    turtle.fd(450)
    turtle.up()
    turtle.goto(x, y - 50 * row_num)
    turtle.down()
# drow clomun & row
turtle.up()
turtle.goto(x, y)
turtle.right(90)
turtle.down()
clo_num = 0
for clo in range(10):
    clo_num += 1
    turtle.pensize(5) if clo in range(0, 10, 9) else turtle.pensize(3) if clo in range(0, 9, 3) else turtle.pensize(1)
    turtle.fd(450)
    turtle.up()
    turtle.goto(x+50*clo_num, y )
    turtle.down()
turtle.up()
turtle.goto(x, y)
turtle.pensize(5)
turtle.down()
# part 2 of sudoko table








