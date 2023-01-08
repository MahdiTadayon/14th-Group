# calculate mean of unknown number of integers(q or quit to stop entering data )
Sum, count = (0, 0) 

while(True):
    try :
        number = input("Please enter an integer (q/quit/Q/Quit) : ")
        if(number.lower() == "q" or number.lower() == "quit") :
            break 
        
        count += 1 
        Sum += int(number) 
        print("Mean of the entered integers : {}".format(float(Sum)/count))

    except ValueError :
        count -= 1 
        print("Invalid input. Try again.")

