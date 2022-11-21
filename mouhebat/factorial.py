def create_number():
    n = 1
    while True:
        yield n
        n += 1

def factorial(n):
    numb = create_number()
    num = 1;
    while True:
        n1 = next(numb)
        n2 = next(numb)
        if n1 == n:
          n2 = 1
        if n1 > n or n2 > n:
            return num

        num = num * n1 * n2


def factor(n):
    start = 1
    fact = 1
    while start <= n:
        yield fact
        start = start + 1
        fact = fact * start


if __name__ == '__main__':

    inp = input('enter numer =')
    print(f'factorial({inp}) in approach 1 equal to :{factorial(int(inp))}')

    func = factor(int(inp))
    num_fact = 0
    for i in func:
        num_fact = i
    print(f'factorial({inp}) in approach 2 equal to :{num_fact}')