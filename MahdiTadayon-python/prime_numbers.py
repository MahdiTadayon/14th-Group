# prime numbers(1 - 1000) ---> for and else 
# solution 1 
for number in range(2, 1000):
    for divisor in range(2, number):
        if not number % divisor :  
            break 
    else:
        print(number) 


# solution 2
for number in range(2, 1000):
    for divisor in range(2, number):
        if number in range(0, number+1, divisor):
            break 
    else:
        print(number) 
