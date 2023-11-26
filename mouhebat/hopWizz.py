# for num in range(1,100):
#     str_num = 'HopWiz' if not num % 21 else 'Hop' if not num % 3 else 'Wiz' if not num % 7 else str(num)
#     print(str_num)
#
# print('='*40)
# print(list(range(0,100,21)))
# for num in range(1,100):
#     if num in range(0,100,21):
#         print('HopWiz')
#     elif num in range(0,100,3):
#         print('Hop')
#     elif num in range(0,100,7):
#         print('Wiz')
#     else:
#         print(str(num))


import turtle
import time


trt = turtle.Turtle()
# trt.hideturtle()
scr = turtle.Screen()
scr.setup(width=800,height=800,startx=0,starty=0)

for indx in range(9):
    if (indx + 1) % 3 == 0:
        trt.width(3)
    else:
        trt.width(1)
    trt.forward(9*25)
    trt.left(90)
    # trt.width(5)
    trt.forward(25*(indx+1))
    trt.left(90)
    trt.forward(9*25)
    trt.left(90)
    trt.forward(25 * (indx + 1))
    trt.left(90)

time.sleep(4)
# ///////////////////////////////////////////////////
for indx in range(9):
    # trt.right(90)
    trt.forward(25*(indx+1))
    if  indx ==8:
        trt.width(5)
    elif (indx+1) % 3 == 0:
        trt.width(3)
    else:
        trt.width(1)
    trt.left(90)
    trt.forward(9*25)
    trt.right(90)
    trt.forward(25*(indx+1))
    trt.right(90)
    trt.width(5)
    trt.forward(9*25)
# //////////////////////////////////////////////////

# ----------------------------------------------
# for _ in range(5):
#
#     trt.forward(25)
#
#     trt.left(90)
#     trt.forward(25)
#
#     trt.left(90)
#
#     trt.forward(25)
#
#     trt.right(90)
#     trt.forward(25)
#
#     trt.right(90)
#
#     time.sleep(2)
# ----------------------------------------------


turtle.done()
# import turtle
#
# tur = turtle.Turtle() #turtle for writing missing numbers
# tur.speed(0)
# tur.up()
# tur.ht()
#
# pen = turtle.Turtle() #turtle for drawing the whole board and known numbers
# pen.speed(0)
# pen.up()
# pen.ht()
#
# win = turtle.Turtle() #turtle for when you have it correct
# win.ht()
# win.speed(0)
# win.up()
#
# screen = turtle.Screen()
# screen.setup(800,800)
# screen.tracer(0)
#
# LENGTH_BOARD = 600
#
# fontBoard = ("Arial", 14,)
# fontNumbers = ("Arial", 36)
#
# #this is function for writing the known numbers
# def sudokuSetup(x,y,height,length,text,color):
#     pen.goto(x,y)
#     pen.color(color)
#     pen.right(90)
#     pen.forward(height)
#     pen.left(90)
#     pen.backward(LENGTH_BOARD/19)
#     pen.forward(length)
#     pen.write(text, font=fontNumbers, align="center")
#
# #this is function for writing the missing numbers put in by the user
# def sudokuPlay(x,y,height,length,text):
#     #drawing white square/erase previous number
#     tur.goto(x,y)
#     tur.color("white")
#     tur.fillcolor("white")
#     tur.right(90)
#     tur.forward(height-50)
#     tur.left(90)
#     tur.backward(LENGTH_BOARD/19)
#     tur.forward(length-30)
#     tur.down()
#     tur.begin_fill()
#     for i in range(3):
#         tur.forward(60)
#         tur.right(90)
#     tur.forward(60)
#     tur.end_fill()
#     tur.up()
#
#     #going to right position and writing the number
#     tur.goto(x,y)
#     tur.color("dark blue")
#     tur.right(180)
#     tur.forward(height)
#     tur.left(90)
#     tur.backward(LENGTH_BOARD/19)
#     tur.forward(length)
#
#
