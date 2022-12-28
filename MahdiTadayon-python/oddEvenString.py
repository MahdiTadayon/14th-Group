# for loop to iterate between odd elements and even elements 

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# solution 1 ---> using for loop
for even in range(0,len(string),2):
    print(string[even],end="")

print("")
for odd in range(1,len(string),2):
    print(string[odd],end="")

print("")


# solution 2 ---> without loop 
print("evenString : ", string[0:len(string):2])
print("oddString  : ", string[1:len(string):2])