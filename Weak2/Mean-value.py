sumOfValues = 0
count = 0
while True:
    inp = input('Enter a Number:')
    if inp.lower() == 'q' or inp.lower() == 'quit':
        break
    if not inp.isdigit():
        continue
    else:
        sumOfValues = sumOfValues + int(inp)
        count += 1
mean = sumOfValues / count
print(mean)
print("="*100)


