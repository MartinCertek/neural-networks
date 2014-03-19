import operator
from ast import literal_eval

result = []
my_choicess=[
          ((1,1), 11),
           ((1,2), 12),
           ((1,4), 14),
]
my_choices=[]

i = 0
with open('newfile.txt', 'r') as f:
    for line in f:
    	print line.strip()
    	i += 1
    	result.insert(i,line)
#print result

my_choices.insert(0, ((2,3),13))
my_choices.insert(len(my_choices)+1, ((5,4),33))
my_choices.insert(len(my_choices)+1, ((4,4),33))

print my_choices

my_choices = []

'''
myList = []
result = []
with open('newfile.txt', 'r') as f:
    for line in f:
    	print line.strip()
        #result.extend(literal_eval(line.strip()))
        myList.append(line)

    
print(myList)
#for i in result:
#    print i

#tupleCopy = result[:256]
#print tupleCopy

#new_list = []


for item in result:
    new_list.append(item[1])

#new_list = map(operator.itemgetter(1), result)

#print result
#print new_list


f = open("newfile.txt","r") #opens file with name of "test.txt"
myList = []
for line in f:
    myList.append(line)
print(myList)

'''