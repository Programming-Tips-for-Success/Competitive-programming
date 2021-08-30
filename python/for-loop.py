# range
a = [1, 2, 3, 4]  
for i in range(4):  
    print(a[i])

for step in range(5):      
    print(step)  

a= list(range(3, 6))          
print(a) 

# direct list
a = [1, 2, 3, 4]  
for i in a:  
    print(i, 'd')

arr = [2, 3]
summation = 0
for x in arr:  
    summation += x  
print(summation)   # 5

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

questions = ['name', 'quest', 'favorite color'] 
answers = ['lancelot', 'the holy grail', 'blue'] 
for q, a in zip(questions, answers): 
   print('What is your {0}?  It is {1}.'.format(q, a))

a = ['Hacker', 'Earth','1','2', 'Python', 'Language', '10']
a_to_dictionary = dict(zip(a[0::2], a[1::2]))
print(a_to_dictionary)