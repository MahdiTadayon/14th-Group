number_string = '76,876532,9.356,0,0.23,-234,6,87586,987,-24253285623784,28929864238947,-0.375'
number_string += ','
# Solution 1, with no use of built-in functions__________________________________________
string_dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,  '6': 6, '7': 7, '8': 8, '9': 9}
temp_num = 0
temp_float = 0
sum_total = 0
n_flag = 0
f_flag = 0
pwr = 0

for string in number_string:
    if string in '-':
        n_flag = 1
    elif string in '.':
        f_flag = 1
        pwr = -1
    elif string in ',':
        if n_flag == 1:
            sum_total += (-1) * temp_num + (-1) * temp_float
            temp_num = 0
            temp_float = 0
            n_flag = 0
            f_flag = 0
        else:
            sum_total += temp_num + temp_float
            temp_num = 0
            temp_float = 0
            f_flag = 0
    elif f_flag:
        temp_float = temp_float + string_dic[string] * 10 ** pwr
        pwr -= 1
    else:
        temp_num = temp_num * 10 + string_dic[string]
# sum_total += (-1) * temp_num + (-1) temp_float
print('(1) Sum of Number String is:', '{:,}'.format(sum_total))

# Solution2, Using predefined functions_______________________________________________
sum_total = 0.0
for string in number_string[:-1].split(','):
    sum_total += float(string)
print('(2) Sum of Number String is:', '{:,}'.format(sum_total))

# Solution3, Pythonic_________________________________________________________________
print('(3) Sum of Number String is:', '{:,}'.format(sum(eval(number_string[:-1]))))
