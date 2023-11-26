# Q(1) Random Paragraph
# Questions:
#   (1) Extract # of words
#   (2) Extract # of unique words
#   (3) Extract # of to-be verbs
#   (4) Extract # of to-be verbs' occurrence
print('Random Paragraph'.center(75, "_"))
my_paragraph = """It is not only writers who can benefit from this free online tool. If you are a programmer who is
working on a project where blocks of text are needed, this tool can be a great way to get that. It is a good way to
test your programming and that the tool being created is working well. Above are a few examples of how the random
paragraph generator can be beneficial. The best way to see if this random paragraph picker will be useful for your
intended purposes is to give it a try. Generate a number of paragraphs to see if they are beneficial to your current
project. If you do find this paragraph tool useful, please do us a favor and let us know how you are using it. It is
greatly beneficial for us to know the different ways this tool is being used so we can improve it with updates. This is
especially true since there are times when the generators we create get used in completely unanticipated ways from when
we initially created them. If you have the time, please send us a quick note on what you would like to see changed or
added to make it better in the future."""

# Question1
parag_lines = my_paragraph.splitlines()
char_list = []
for line in parag_lines:
    for char in line.split(' '):
        if ',' in char or '.' in char:
            char_list.append(char[:len(char)-1])
        else:
            char_list.append(char)
    else:
        continue
print(f'There are {len(char_list)} words in this paragraph.')
print('='*75)

# Question2
char_set = set(char_list)
print(f'From {len(char_list)} words, {len(char_set)} words are unique.')
print('='*75)

# Question3
to_be_verbs = ('Am', 'Is', 'Are', 'Was', 'Were')
to_be_dic = {'Am': 0, 'Is': 0, 'Are': 0, 'Was': 0, 'Were': 0}
for char in char_list:
    if char.capitalize() == to_be_verbs[0]:
        to_be_dic[to_be_verbs[0]] += 1
    elif char.capitalize() == to_be_verbs[1]:
        to_be_dic[to_be_verbs[1]] += 1
    elif char.capitalize() == to_be_verbs[2]:
        to_be_dic[to_be_verbs[2]] += 1
    elif char.capitalize() == to_be_verbs[3]:
        to_be_dic[to_be_verbs[3]] += 1
    elif char.capitalize() == to_be_verbs[4]:
        to_be_dic[to_be_verbs[4]] += 1
print(f'Total number of to-be verbs used in this paragraph: {sum(to_be_dic.values())}')
print('='*75)
print(f'Total number of \'Am\' used in this paragraph: {to_be_dic["Am"]}')
print(f'Total number of \'Is\' used in this paragraph: {to_be_dic["Is"]}')
print(f'Total number of \'Are\' used in this paragraph: {to_be_dic["Are"]}')
print(f'Total number of \'Was\' used in this paragraph: {to_be_dic["Was"]}')
print(f'Total number of \'Were\' used in this paragraph: {to_be_dic["Were"]}')


# Q2: Sample CSV File
print('Random Paragraph'.center(75, "_"))
my_csv = """laura@example.com;2070;Laura;Grey
craig@example.com;4081;Craig;Johnson
mary@example.com;9346;Mary;Jenkins
jamie@example.com;5079;Jamie;Smith"""
# print(my_csv)
my_csv_list = my_csv.splitlines()
login_email = list()
identifier = list()
first_name = list()
last_name = list()
print(my_csv_list)
# for item in my_csv_list:
#     for i in range(len(item.split(';'))):
#         login_email.append(item.split(';')[i])
#         identifier.append(item.split(';')[i + 1])
#         first_name.append(item.split(';')[i + 2])
#         last_name.append(item.split(';')[i + 3])
#         break
for item in my_csv_list:
    login_email.append(item.split(';')[0])
    identifier.append(item.split(';')[1])
    first_name.append(item.split(';')[2])
    last_name.append(item.split(';')[3])
print(login_email)
print(identifier)
print(first_name)
print(last_name)

