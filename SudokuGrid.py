from itertools import product
import turtle 


def turtleSetting(turt):
    turt.penup()
    turt.speed(0)
    turt.hideturtle()


def penColorSize(line, turt):
    if(line==0 or line==9 ):
        turt.penup()
        turt.pen(pencolor='black', pensize=5)
    elif(line==3 or line==6 ):
        turt.penup()
        turt.pen(pencolor='black', pensize=3)
    else :
        turt.penup()
        turt.pen(pencolor='gray', pensize=1)


def setPen(xCor,yCor,turt):
    turt.penup()
    turt.setpos(xCor , yCor)
    turt.pendown()
    turt.forward(360)


def drawGrid(turt):
    for line in range(10):
        penColorSize(line ,turt)
        setPen(-180, 180-40*line, turt)
    turt.penup()
    turt.right(90)
    for line in range(10):
        penColorSize(line ,turt)
        setPen(-180+40*line, 180, turt)
    turt.penup()


def drawDigit(grid , color ,turt):
    for row, col in product(range(9), range(9)):
        if not grid[row][col] == 0  :
            xCor = -168 + col * 40
            yCor = 140 - row * 40 
            turt.up()
            turt.setpos(xCor, yCor)
            turt.pen(pencolor=color, pensize=2)
            turt.down()
            turt.write(grid[row][col], font=('Arial', 25, 'normal'))
            turt.up()


if __name__ == "__main__":
    turtle.tracer(0)

    turt_table = turtle.Turtle()
    turtleSetting(turt_table)
    drawGrid(turt_table)

    turtle.mainloop()