from random import randint
from copy import deepcopy
from itertools import product
from time import sleep
import turtle 
import sys


def squareStarter(rowCol): return 0 if rowCol < 3 else 3 if rowCol < 6 else 6 


def digitRemover(digit, posibleDigits): 
    if digit in posibleDigits:  posibleDigits.remove(digit)
    return posibleDigits


def sudokuRule (grid, row, col, posibleDigits):
    for i in range(9):    
        posibleDigits = digitRemover(digit=grid[row][i], posibleDigits)   # row rule
        posibleDigits = digitRemover(digit=grid[i][col], posibleDigits)   # col rule
    for i, j in product(range(squareStarter(row), squareStarter(row)+3), range(squareStarter(col), squareStarter(col)+3)):
        posibleDigits = digitRemover(grid[i][j], posibleDigits)     #square rule 
    
    return posibleDigits


def randomDigitSelecter(posibleDigits): return posibleDigits[randint(0, len(posibleDigits)-1)]


def cellConverter(cell):  # cells ---> 1 to 81 
    row = cell // 9 -1
    col = cell % 9 -1 
    return row, col 

# There is no 16-Clue Sudoku              
# sudoku solver
# generate sudoku table that include more than 16 clues 
def puzzleGenerator(sudokuGrid, sudokuPuzzle, clue=17):    
    randomCellSet = set()       # cells ---> 1 to 81 
    if clue == 0 :
        print("clue must be greater than zero")
        sys.exit(-1)
    while(True):
        randomCellSet.add(randint(1, 81))
        if len(randomCellSet) == clue:
            break 
    for cell in randomCellSet :
        sudokuPuzzle[cellConverter(cell)[0]][cellConverter(cell)[1]] =  sudokuGrid[cellConverter(cell)[0]][cellConverter(cell)[1]]

    return sudokuPuzzle


def sudokuSolver(grid, gridBackUp, backUpEmpty=True):   
    row=0
    backCount = 0
    while(row < 9):
        flag = False 
        col = 0
        while(col < 9):
            if gridBackUp[row][col] != 0 :
                col += 1 
                
            else :
                posibleDigits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                posibleDigits = sudokuRule(grid, row, col, posibleDigits)   
                
                if posibleDigits:
                    grid [row][col] = randomDigitSelecter(posibleDigits)
                    col += 1
                
                else:
                    if backUpEmpty :
                        backCount += 1 
                        row ,col ,grid = comeBack(row, col, backCount, grid, gridBackUp, backUpEmpty) 
                    else :
                        grid = deepcopy(gridBackUp)
                        row = 0 
                    flag = True  
                    break 
        if flag :
            pass
        else : 
            row += 1
            
    return grid


def comeBack (row, col, backCount, grid, gridBackUp, backUpEmpty):                           
    counter = 0                                                             
    while(counter <= backCount ):
        if backUpEmpty:
            grid[row][col] = 0
            if(col == -1):
                if not row==0 :
                    row -= 1 
                col = 8 
            col = col -1 
            counter += 1 
        else :    
            if gridBackUp[row][col] == 0 :
                grid[row][col] = 0 
                col -= 1 
                counter += 1  
                
            else:
                col -= 1
            
            if (col == -1) :
                if not row == 0 :
                    row -= 1 
                col = 8
                
            if (row, col==0, 0) or (row, col) ==(0, -1):
                break 
    
    return row, col, grid 


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

    sudokuGrid= [[0, 0, 0, 0, 0, 0, 0, 0, 0],          
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    sudokuPuzzle = deepcopy(sudokuGrid)
    sudokuGridBackUp = deepcopy(sudokuGrid)
    solvedSudokuGrid = sudokuSolver(sudokuGrid, sudokuGridBackUp, backUpEmpty=True)
    sudokuPuzzle = puzzleGenerator(sudokuGrid, sudokuPuzzle, clue=20)
    sudokuPuzzleBackUp = deepcopy(sudokuPuzzle)
    solvedSudokuPuzzle =  sudokuSolver(sudokuPuzzle, sudokuPuzzleBackUp, backUpEmpty=False)
    
    turtle.tracer(0)
    turt_table = turtle.Turtle()
    turtleSetting(turt_table)
    drawGrid(turt_table)
    
    turt_digit = turtle.Turtle()
    turtleSetting(turt_digit)
    drawDigit(solvedSudokuGrid, 'black', turt_digit)
    sleep(4)
    turt_digit.clear()
    drawDigit(sudokuPuzzleBackUp, 'black', turt_digit)
    sleep(4)
    drawDigit(solvedSudokuPuzzle, 'green', turt_digit)
    drawDigit(sudokuPuzzleBackUp, 'black', turt_digit)
   
    turtle.mainloop()
