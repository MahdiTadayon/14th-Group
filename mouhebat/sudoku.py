import turtle
import time
import random


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

pos = [12,25+12,50+12,75+12,100+12,125+12,150+12,175+12,200+12]

# initilize turtle and screen
def initMainTurtle():
    trt = turtle.Turtle()
    trt.hideturtle()
    scr = turtle.Screen()
    scr.setup(width=800,height=800,startx=0,starty=0)
    return trt

# create table sudoku
def sudokuTable(trt):
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





# initilize sudoku
def initSudokuNumber(sudokuArr):
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
    return sudokuArr

# get empty for set sudoku number
def get_empty(sudokuTable):
    for i in range(len(sudokuTable)):
        for j in range(len(sudokuTable)):
            if (sudokuTable[i][j] == 0):
                return (i,j)
    return None

def setNumberSodoku(sudokuArr):
    find = get_empty(sudokuArr)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(sudokuArr, i, (row, col)):
            sudokuArr[row][col] = i

            if setNumberSodoku(sudokuArr):
                return True

            sudokuArr[row][col] = 0

    return False

def valid(sudokuArr, num, pos):
    # Check row
    for i in range(len(sudokuArr[0])):
        if sudokuArr[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sudokuArr)):
        if sudokuArr[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if sudokuArr[i][j] == num and (i,j) != pos:
                return False

    return True

def printSudokuArr(sudokuArr):
    for i in range(len(sudokuArr)):
        print(sudokuArr[i])
    print("="*40)

def printSudokuTable(sudokuArr):
    for i in range(len(sudokuArr)):
        for j in range(len(sudokuArr)):
            setNumberSudokuTableTurtle(i,j,sudokuArr[i][j])

def setNumberSudokuTableTurtle(i,j,num):
    trtNum = turtle.Turtle()
    trtNum.hideturtle()
    trtNum.up()
    trtNum.goto( pos[j] , pos[i])
    trtNum.down()
    trtNum.write(num)

if  __name__== '__main__':
    trt = initMainTurtle()
    sudokuTable(trt)
    sudokuArr = initSudokuNumber(sudokuArr)
    printSudokuArr(sudokuArr)
    setNumberSodoku(sudokuArr)
    printSudokuArr(sudokuArr)
    printSudokuTable(sudokuArr)
    turtle.done()




