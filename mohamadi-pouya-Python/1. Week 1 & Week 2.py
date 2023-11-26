# _________Ex1: Hop-Wiz Game_____________
print('Hop-Wiz Game'.center(60, '_'))
# Solution1
result_list = list()
for num in range(1, 100):
#     result_list.append('Hop-Wiz' if num % 15 == 0 else 'Hop' if num % 3 == 0 else 'Wiz' if num % 5 == 0 else str(num))
    result_list.append('Hop-Wiz' if num in range(0, 100, 15) else 'Hop' if num in range(0, 100, 3) else 'Wiz' if num in range(0, 100, 5) else str(num))
print(result_list)

# this one is better in terms of performance
# Solution2
hop_wiz = []
hop = []
wiz = []
for num in range(1, 100):
    if num in range(0, 1000, 15):
        hop_wiz.append(num)
        print('Hop-Wiz')
    elif num in range(0, 1000, 3):
        hop.append(num)
        print('Hop')
    elif num in range(0, 1000, 5):
        wiz.append(num)
        print('Wiz')
    else:
        print(num)
print(hop_wiz)
print(hop)
print(wiz)


# use else (for) instead
# _________Ex2: Prime Numbers_____________
print('Prime Numbers'.center(60, '_'))
# # Solution1
prime_numbers = []
for num in range(2, 1000):
    modulos = 0
    for num2 in range(1, num):
        if not num % num2:
            modulos += 1
    if modulos < 2:
        prime_numbers.append(num)
print('Prime Numbers below 1000:', prime_numbers)

# Solution2
# prime_numbers = []
# for num in range(2, 1000):
#     for num2 in range(2, num):
#         if num % num2 == 0:
#             break
#     else:
#         prime_numbers.append(num)
# print('Prime Numbers below 1000:', prime_numbers)


# _________Ex3: Backwards Iteration_____________
print('Backwards Iteration'.center(60, '_'))
# Solution1
english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(english_alphabet[::-1])
print(english_alphabet[-1:-26:-1])

# Solution2
reversed_alphabet = ''
for char in english_alphabet:
    reversed_alphabet = char + reversed_alphabet
print(reversed_alphabet)

# Solution3
reversed_word = ''
for i in range(1, len(english_alphabet)+1):
    reversed_word += english_alphabet[-i]
print(reversed_word)


# _________Ex4: Odd-Even Iterator_____________
print('Odd-Even Iterator'.center(60, '_'))
# Left_to_right
odd_char = ''
even_char = ''
for even, odd in zip(english_alphabet[::2], english_alphabet[1::2]):
    odd_char += odd
    even_char += even
print(even_char)
print(odd_char)

# Right_to_left
odd_char_r = ''
even_char_r = ''
for odd, even in zip(english_alphabet[::-2], english_alphabet[-2::-2]):
    odd_char_r += odd
    even_char_r += even
print(even_char_r)
print(odd_char_r)


# _________Ex5: User Input - Int. Num_____________
print('User Input - Int. Num'.center(60, '_'))
while True:
    inp = input('Enter your number:')
    if not inp.lstrip('-').isnumeric():
#         print('Please Enter only an Integer!')
        continue
    # this will produce error on other cases
    elif isinstance(int(inp), int):
        print(f'Your Integer is: {int(inp)}')
        break

# _________Ex6: Mean Value_____________
print('Mean Value'.center(60, '_'))
counter = 0
sum_inp = 0
while True:
    user_inp = input('Enter your numbers to get the mean:')
    
#     if user_inp.lower() == 'q' or user_inp.lower() == 'quit':
    if user_inp.lower() in ('q', 'quit'):
        break
    elif not user_inp.lstrip('-').isdigit():
        print('Please Enter a Valid Number!')
        continue
    else:
        counter += 1
        sum_inp += int(user_inp)
print(sum_inp/counter if counter else 'No Entries! Closing Off')
