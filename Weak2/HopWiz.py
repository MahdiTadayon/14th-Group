for num in range(100):
  x = 'HopWiz' if not num %  15 else 'Hop' if not num % 3 else 'Wiz' if not num % 5 else str(num)
  print(x)

print('+' * 50)

for number in range(1,100):
    if not number % 15 :
        print('HopWiz')
    elif not number % 3:
        print('Hop')
    elif  not number % 5:
        print('Wiz')
    else: print(number)