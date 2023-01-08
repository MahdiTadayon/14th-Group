from random import choice
import sys


def winner(choice1, choice2, rounD):
    concatChoice = choice1 + choice2
    if choice1 == choice2 :
        return 0, 0, rounD-1
    elif 'rp' in concatChoice or 'ps' in concatChoice or 'sr' in concatChoice  :
        return 0, 1, rounD
    elif 'rs' in concatChoice or 'pr' in concatChoice or 'sp' in concatChoice  :
        return 1, 0, rounD

rpsDict ={'r':'Rock', 'p':'Paper', 's':'Scissors'}

while(True):
    print('_' * 50 )
    try:
        numberOfRounds = int(input('Enter number of rounds : '))
        if numberOfRounds < 0 :
            continue
        
    except ValueError:
        print('Enter an integer')
        continue
    computerRate = 0
    playerRate = 0 
    for rounD in range(0, numberOfRounds):
        computerChoice = choice(['r', 'p', 's'])
        print("Computer rate : {} player rate : {}".format(computerRate,playerRate))
        while(True):
            print('_' * 50, '\n' )
            
            while(True):
                try:
                    (cRate, pRate, rounD) = winner(computerChoice, input('Player choice(Rock/Paper/scissor/r/p/s) : ').lower(), rounD)
                    break
                except TypeError: 
                    continue
                except KeyboardInterrupt:
                    print('\n')
                    continue
            print('Computer choice: ', rpsDict[computerChoice] )
            computerRate += cRate
            playerRate += pRate
            break 

    print("Computer rate : {} player rate : {}".format(computerRate,playerRate))
    print('_' * 50 , '\n')
    while(True):
        oneMoreRound  = input("One more round ? (Yes/No): ").lower()
        if 'y' in oneMoreRound:
            break
        elif 'n' in oneMoreRound:   
            sys.exit()  
        else : 
            continue
    
