def fib(n):
    previous, current = 0, 0
    for i in range(n + 1):
        if i == 0:
            previous = i
            print(previous)
        elif i == 1:
            current = i
            print(current)
        else:
            previous, current = current, previous + current
            print(current)


if __name__ == '__main__':
    fib(2)
