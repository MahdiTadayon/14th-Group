# Range to generate: range(2.3, 3.78, 0.01)

def decimal_F(start, end):
    start, end =2.3, 3.78
    while start < end:
         start += 0.01
         yield '{:.2f}'.format(start)

if __name__ == '__main__':
    for i in decimal_F(2.3, 3.8):
        print(i)



#--------------------------------------------

# Range to generate: range(c, x, 2)
def alphabet(start = 'A', end = 'X', step = 2):
    alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in range(alphabet.index(start), alphabet.index(end), step):
        yield alphabet[char]


for item in alphabet('C', 'X'):
    print(item)