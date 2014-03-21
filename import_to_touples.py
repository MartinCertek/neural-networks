import operator
from ast import literal_eval
import random


'''

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


digits = []

with open('p_data.txt', 'r') as dataFile:
      for line in dataFile:
        #poriesit spracovanie \n na konci v premennej out_bin
        (inBin, outBin) = line.split('|') 
        outBin = int(outBin)
        inBin = eval(inBin)
        digits.insert(len(digits),((inBin), outBin))  
        #my_choices.insert(len(my_choices)+1, ((5,4),33))
        print inBin
        print outBin
print digits

'''

try:
    # available in Python 2.0 and later
    shuffle = random.shuffle
except AttributeError:
    def shuffle(x):
        for i in xrange(len(x)-1, 0, -1):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = int(random.random() * (i+1))
            x[i], x[j] = x[j], x[i]

xorData = [
             ((0,0), 0),
             ((0,1), 1),
             ((1,0), 1),
             ((1,1), 0),
            ]
print xorData


cards = range(52)
#print cards

shuffle(xorData)
print xorData

