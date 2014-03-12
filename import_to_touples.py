import operator
from ast import literal_eval

result = []
with open('newfile.txt', 'r') as f:
    for line in f:
        result.extend(literal_eval(line.strip(',')))

#for i in result:
#    print i

tupleCopy = result[:256]
print tupleCopy

new_list = []

'''
for item in result:
    new_list.append(item[1])
'''
#new_list = map(operator.itemgetter(1), result)

#print result
#print new_list