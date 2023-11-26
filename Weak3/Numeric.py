numercString = '34,0.454543545,-34.33,4,5,3456789'
number = ''
sum = 0
for char in numercString:
    if char in '0123456789-.':
        number += char
    else:
        sum = float(number)
        number = ''
sum += float(number)
print(sum)
#+++++++++++++++++++++++++++++++++++

