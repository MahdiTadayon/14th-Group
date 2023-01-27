# solution 1
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# solution 2-------------------------------------
def factorial2(n):
    if n <= 1:
        yield 1
    else:
        yield n * factorial(n-1)

 # -----------------------------------------
if __name__ == '__main__':


    print(factorial(10))         # solution 1

    for valu in factorial2(10):  # solution 2
        print(valu)

#solution 3 --------------------------------------
def fact(n):
    num, rusult = 1, 1

    for _ in range(1,n):
        num = num + 1
       # yield num
        rusult = rusult * num
        yield rusult

for i in fact(10):
    print(i)
#-----------------------------------------
