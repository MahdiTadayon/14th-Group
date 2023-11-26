
import math
def is_prime(n):
    if n % 2 == 0 and n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for n in range(1,1000):
    if is_prime(n) == True:
        print (n,"Prime")
    elif is_prime(n) == False:
       print(n,'not prime')

