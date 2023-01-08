# Rewrite factorial without using recursion 

def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact *= i 
    return fact 


if __name__ == "__main__" :
    while(True):
        try :
            print(factorial(int(input())))
            break 
        except (ValueError, KeyboardInterrupt) :
            pass
