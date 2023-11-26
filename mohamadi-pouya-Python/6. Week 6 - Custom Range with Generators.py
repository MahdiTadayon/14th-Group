# Range to generate: range(2.3, 3.78, 0.01)
# Solution 1
def decimal(start, end, step=0.01):
    current_dec = start
    for flt in range(int((end - start)/step)):
        current_dec += step
        yield '{:.2f}'.format(current_dec)


# Solution 2
def decimal2(start, end, step=0.01):
    while start <= end:
        yield '{:.2f}'.format(start)
        start += step


# Range to generate: range(c, x, 2)
def alphabet_range(start='A', end='Z', step=1):
    alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for alpha in range(alphabet_string.index(start.capitalize()), alphabet_string.index(end.capitalize()), step):
        yield alphabet_string[alpha]


if __name__ == '__main__':
    for i in decimal(2.3, 3.78, 0.01):
        print(i)
    for i in decimal(2.3, 3.78, 0.01):
        print(i)
    for element in alphabet_range('c', 'x', 2):
        print(element)
