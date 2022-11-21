import random
print('Welcome to my game \nmy game\'s name is RPS ')
print('first choose number for play count of game ')
print('You can choose 3 items for play game : Rock and Paper and Scissor')
print('for exit game choose q or quit')
i = 0;
dict = {'R':1 , 'P':2 , 'S':3}
dictRandom = {1:'Rock' , 2:'Paper' , 3:'Scissor'}
inpCountGame = ''
repeatGame = True

while True:
    PRS = 0;
    if repeatGame == True:
        cntWinRPS = 0
        cntWinRPSRandom = 0
        inpCountGame = input('enter number for count of game :')
        if ((not inpCountGame.isdigit()) or int(inpCountGame)<=0) :
            continue;

    inpRPS = input('choose Rock or Paper or Scissor or (q or quit for exit):')

    if inpRPS in 'Rock':
        PRS = dict['R']
    elif inpRPS in 'Paper':
        PRS = dict['P']
    elif inpRPS in 'Scissor':
        PRS = dict['S']
    elif inpRPS in 'quit':
        break;
    else:
        continue

    randomPRS = random.randint(1, 3)
    print(f'Game choosed {dictRandom[randomPRS]} ')
    if PRS ==1 and randomPRS ==2:
        cntWinRPSRandom +=1
        print(f"Game has won.count of game { cntWinRPSRandom }")
    elif PRS == 2 and randomPRS == 3:
        cntWinRPSRandom += 1
        print(f"Game has won.count of game {cntWinRPSRandom}")
    elif PRS == 3 and randomPRS == 1:
        cntWinRPSRandom += 1
        print(f"Game has won.count of game {cntWinRPSRandom}")
    elif  randomPRS ==1 and PRS ==2:
        cntWinRPS +=1
        print(f"you have won.count of You {cntWinRPS}")
    elif randomPRS == 2 and PRS == 3:
        cntWinRPS += 1
        print(f"you have won.count of You {cntWinRPS}")
    elif randomPRS == 3 and PRS == 1:
        cntWinRPS += 1
        print(f"you have won.count of You {cntWinRPS}")



    if cntWinRPSRandom == int(inpCountGame):
        repeatGame = True
        print("Game has won this palying")
    elif cntWinRPS == int(inpCountGame):
        repeatGame = True
        print("you have won this palying")
    else:
        repeatGame = False

    if repeatGame == True:
        inpCon = ''
        while True:
            inpCon =  input('would you like to continue game?(y/n)')
            if inpCon.lower() in 'yn':
                break;
        if inpCon.lower() in 'y':
            continue
        elif inpCon.lower() in 'n':
            break






