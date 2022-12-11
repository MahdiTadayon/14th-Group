import turtle
import time
import random


trt = turtle.Turtle()
# trt.hideturtle()
scr = turtle.Screen()
scr.setup(width=800,height=800,startx=0,starty=0)



for indx in range(5):
    if (indx + 1) % 2 == 0 and (indx + 1) > 2:
        trt.width(3)
    else:
        trt.width(1)
    trt.forward(9*25)
    trt.left(90)
    trt.width(5)
    trt.forward(25)
    trt.left(90)
    if  indx == 4:
        trt.width(5)
    elif (indx +1) % 2 == 0 and (indx + 1)==2:
        trt.width(3)
    else:
        trt.width(1)
    trt.forward(9*25)
    trt.right(90)
    if indx != 4:
        trt.width(3)
        trt.forward(25)
        trt.right(90)


for indx in range(9):
    trt.right(90)
    trt.forward(25*(indx+1))
    if  indx ==8:
        trt.width(5)
    elif (indx+1) % 3 == 0:
        trt.width(3)
    else:
        trt.width(1)
    trt.left(90)
    trt.backward(9*25)
    trt.left(90)
    trt.forward(25*(indx+1))
    trt.right(90)
    trt.width(5)
    trt.forward(9*25)
# //////////////////////////////////////////////////

pos = [12,25+12,50+12,75+12,100+12,125+12,150+12,175+12,200+12]
sudokuArr=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

# initilize sudoku
for num in range(1,10):
    trtNum = turtle.Turtle()
    trtNum.hideturtle()
    trtNum.up()
    y = random.randint(0, 8)
    trtNum.goto(pos[num-1],pos[y])
    print(f'sudokuArr[{num-1}][{y}]={num}')
    sudokuArr[num-1][y] = num
    trtNum.down()
    trtNum.write(num)



turtle.done()
sudokuNumber = [1,2,3,4,5,6,7,8,9]

def get_empty(sudokuTable):
    for i in range(len(sudokuTable)):
        for j in range(len(sudokuTable)):
            if (sudokuTable[i][j] == 0):
                return (i,j)

