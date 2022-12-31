# In a paragraph please find :
#   -total number of words 
#   -total number of unique words 
#   -total number if 'to be' occurrences 
#   -number of each 'to be' words 


paragraph = '''An aim is a goal or objective to achieve in life.
In order to succeed in life, one must have a goal. 
My aim in life is to be a teacher. 
Teaching is a noble and responsible profession. 
I have come to know that the ever-increasing misery and distress, are due to the ignorance and illiteracy of the people of our country. 
So I have decided to spread education among the masses as much as possible within my humble power.
'''.replace('.' ,' ').replace(',' ,' ').replace('-' ,'').lower().split()

print("total number of words : {}".format(len(paragraph)))
print("total number of unique words : {}".format(len(set(paragraph))))


tobeList=list()
numberOfEachTobeWords = [0 ,0 ,0 ,0 ,0]

for item in paragraph:
    if item in ['am' ,'is' ,'are' ,'was' ,'were']:
        tobeList.append(item)
        

        if item == 'am' :
            numberOfEachTobeWords[0] +=1

        elif item == 'is' :
            numberOfEachTobeWords[1] +=1
        
        elif item == 'are' :
            numberOfEachTobeWords[2] +=1
        
        elif item == 'was' :
            numberOfEachTobeWords[3] +=1

        elif item == 'were' :
            numberOfEachTobeWords[4] +=1
        
        
print("total number if 'to be' occurrences : {}".format(len(tobeList)))

print("-" * 50)

print("am  :{:>2} \nis  :{:>2} \nare :{:>2} \nwas :{:>2} \nwere:{:>2}".format(numberOfEachTobeWords[0],numberOfEachTobeWords[1],numberOfEachTobeWords[2],numberOfEachTobeWords[3],numberOfEachTobeWords[4]))
