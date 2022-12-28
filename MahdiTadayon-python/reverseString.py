string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# solution 1 
print("".join(list(reversed(string))))
# solution 2 
print(string[-1: -(len(string)+1): -1])
# solution 3 ---> using for loop 
for i in range(len(string)-1, -1, -1):
    print(string[i],end="")

print("")



