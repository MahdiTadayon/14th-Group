from random import randint

switch = ["rock", "paper", "scissor", "r", "p", "s"]
roundCounter = ""
i = True
uWin = 0
cWin = 0
while i:
    roundCounter = input("How much to play?")
    try:
        roundCounter = int(roundCounter)
        i = False
    except ValueError:
        if roundCounter.lower() == "q" or roundCounter.lower() == "quit":
            roundCounter = 0
            i = False
        else:
            print("You must enter a number.")

while uWin < roundCounter and cWin < roundCounter:
    uInput = input("rock? paper? or scissor?").lower()
    if uInput.lower() == "q" or uInput.lower() == "quit":
        roundCounter = 0
    else:
        if uInput == switch[3]:
            uInput = switch[0]
        if uInput == switch[4]:
            uInput = switch[1]
        if uInput == switch[5]:
            uInput = switch[2]

        if uInput == switch[0] or uInput == switch[1] or uInput == switch[2]:
            cInput = randint(0, 2)
            cInput = switch[cInput]
            print("Your choice is '" + uInput + "' and mine is '" + cInput + "'")
            if uInput != cInput:
                if cInput == "rock" and uInput == "paper":
                    uWin += 1
                    print("Your point: " + str(uWin) + " | My point: " + str(cWin))
                elif cInput == "rock" and uInput == "scissor":
                    cWin += 1
                    print("Your point: " + str(uWin) + " | My point: " + str(cWin))
                elif cInput == "paper" and uInput == "scissor":
                    uWin += 1
                    print("Your point: " + str(uWin) + " | My point: " + str(cWin))
                elif cInput == "paper" and uInput == "rock":
                    cWin += 1
                    print("Your point: " + str(uWin) + " | My point: " + str(cWin))
                elif cInput == "scissor" and uInput == "rock":
                    uWin += 1
                    print("Your point: " + str(uWin) + " | My point: " + str(cWin))
                else:
                    cWin += 1
                    print("Your point: " + str(uWin) + " | My point: " + str(cWin))
            else:
                print("""Draw!
""" + "Your point: " + str(uWin) + " | My point: " + str(cWin))
        else:
            print("Please choose between rock, paper and scissor.")
if roundCounter == 0:
    print("Hope to see You again!")
elif uWin == roundCounter:
    print("Hooray! You won, Bye Lucy-lock.")
elif cWin == roundCounter:
    print("Oops! I won, try later newbie :)")
