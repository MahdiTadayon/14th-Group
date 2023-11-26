myParagraph = """ Rather than building all of it is functionality into it is core,
Python was designed to be highly extensible via modules.
This compact modularity has made it particularly popular as
a means of adding programmable interfaces to existing applications.
Van Rossum is vision of a small core language with a large standard library
and easily extensible interpreter stemmed from his frustrations
with ABC, which espoused the opposite approach."""

myParagraph = myParagraph.lower()
toBeVerb = {'am', 'is', 'are', 'was', 'were'}
myParagraph = myParagraph.split(' ')
#myParagraph = set(myParagraph)
# count of
print("number Of MyPragraph is :{}".format(len(myParagraph)))

# count of tobe verb
count = 0
for char in myParagraph:
    if char in toBeVerb:
        count += 1
print('number of to be verb is :', count)
# number of repeated word

print('number of repeated word is :')
p_dict = {}
for word in myParagraph:
    if word in p_dict:
        p_dict[word] += 1
    else:
        p_dict[word] = 1
for key in p_dict:
    if p_dict[key] != 1:
        print(key, p_dict[key])





