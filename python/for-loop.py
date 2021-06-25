# range
a = [1, 2, 3, 4]  
for i in range(4):  
    print(a[i])

# direct list
a = [1, 2, 3, 4]  
for i in a:  
    print(i, 'd')

# enumerate process items in a sequence with an index.
for i, v in enumerate(['tic', 'tac', 'toe']): 
   print(i, v) 

collection = [('apple', 'red'), ('banana', 'yello'), ('kiwi',
'green')]
for name, color in collection:
    print ('name: %s,  color: %s' % (name, color, ))

def f(x):
    return x * 3
   
list1 = [11, 22, 33]
list2 = [f(x) for x in list1]
print (list2)
