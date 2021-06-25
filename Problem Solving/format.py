print('G', 'F', 'G', sep ='') 
print('G', 'F', 'G') 
print('09','12', sep='-', end='-2016\n') 
print("Python", end = '@')
print("% 7.3o"% (25))   # print octal value using o. 
print("% 10.3E"% (356.08977))   # print exponential value using E. 

color_list = ["Red","Green","White" ,"Black"] 
print( "%s %s"%(color_list[0],color_list[-1])) 

n = (1 * 2 * 3 + 7 +
     8 + 9) 
print(n)
x = {1 + 2 + 3 + 4 + 5 + 6 + 
     7 + 8 + 9} 
print(x)
footballer = ['MESSI', 
          'NEYMAR', 
          'SUAREZ'] 
print(footballer)
sd = ("sd" + \
     "df")
print(sd)
s = 'Hello, world.'  
str(s) 
repr(s)

print("Geeks : % 2d, Portal : % 5.2f" %(1, '05.333')) #  formatted string literals f or F.
print("Total students : % 3d, Boys : % 2d" %(240, 120))  
exam_st_date = (11,12,2014) 
print( "The examination will start from : %i / %i / %i"%exam_st_date) 
animals = 'eels' 
print(f'My hovercraft is full of {animals}.') 
print(f'My hovercraft is full of {animals!r}.') 
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')) 
for x in range(1, 3): 
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)) 
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg')) 
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678} 
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table)) 
print ('{0:.2}'.format(1.0 / 3)) // .33
# .2 defines the precision of the floating point number.
print('{0} and {1}'.format('spam', 'eggs')) 
print('{1} and {0}'.format('spam', 'eggs')) 
a=5
print ("The value of a is: " + str(a))  
b=6
print ("The value of a is: " + b)  # show error


    
# ‘**’ notation.  
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678} 
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)) 
*a, b, c = [1, 2, 3, 4, 5]
print(a)
# output- 
# [1, 2, 3]
fruits = ['apple', 'banana', 'cherry']
d = 'cherry'
if d in fruits:
    print(fruits.index(d))

  
flag = 2; ropes = 3; pole = 4 
print(flag)
print("5"*6)
print (' ' is ' ')
 


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'] 
for f in (set(basket)): 
   print(f) 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"]) 
print(color_list_1.difference(color_list_2)) 
# ok = input(prompt) 
#     if ok in ('y', 'ye', 'yes'):
# if i not in ['G','C','A','T']: 
if 's' in 'geeks':  
       print ("s is part of geeks")  
else : print ("s is not part of geeks")  
input
num1 = int(input("Enter num1: "))   
num2 = int(input("Enter num2: "))   
num3 = num1 * num2  
print("Product is: ", num3)  
x, y = input("Enter a two value: ").split()  
print( x, y)  
print("First number is {} and second number is {}".format(x, y))   
x, y = [int(x) for x in input("Enter two value: ").split()]  
print(x, y)  
x = [int(x) for x in input("Enter multiple value: ").split()]  
print("Number of list is: ", x) 
num1 = float(input())  
num2 = int(input())  
string = str(input()) 
print(num1)
print(num2)
print(string)
def hello():  
    print("hello")  
    print("hello again")  
hello()  
def getInteger():  
    result = int(input("Enter integer: "))  
    return result  
def Main():  
    print("Started") 
    output = getInteger()       
    print(output)  
Main() 
x = list(map(int, input("Enter a multiple value: ").split()))  
print("List of students: ", x) 
num1 = 34 
if(num1>12):  
    print("Num1 is good")  
elif(num1>35):  
    print("Num2 is not gooooo....")  
else:  
    print("Num2 is great")  
print ("I am Not in if") 
cond2 = 1 if 20 > 10 else 0 
print(cond2)
for i in 'geeks':  
    print (i,end=" ")
    print ("\r")  
arr = [2, 3]
summation = 0
for x in arr:  
    summation += x  
print(summation)   # 5
x = None 
y = None 
print (x == y)
print (None == 0)
print (True or False)  
print (False and True)  
print (not True)  
a = [1, 2, 3]  
del a[1]  
print(a) 

def outer():  
    a = 50 
    def inner():  
        nonlocal a   
        a = 60 
    inner()  
    print (a)  
outer()  
def outer():  
    a = 5 
    def inner():  
        a = 10 
    inner()  
    print (a)
outer()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'] 
for f in sorted(set(basket)): 
   print(f) 

for step in range(5):      
    print(step)  



a= list(range(3, 6))          
print(a) 

args = [3, 6] 
b= list(range(*args))           
print(b) 
# __doc__
print(abs.__doc__) 
num = 24
a =str(num).zfill(4) 
print(a)
for x in range(69,81): 
    if x==69: 
        continue 
    print(x) 
import math 
print(dir(math))  

def make_incrementor(n):    
    return lambda x: x + n 
f = make_incrementor(42) 
print(f(0)) # 42
print(f(1)) # 43
 
import keyword  
s = "for" 
if keyword.iskeyword(s):  
        print ( s + " is a python keyword")  
else :  print ( s + " is not a python keyword")  
print (keyword.kwlist) # print list of all keywords 

name = input("Enter your name: ")  
print ("type of name", type(name))  
print("hello", name)  
j = 1 
while(j<= 5):  
     print(j)  
     j = j + 1 
# The else part is executed when the condition in the while statement is false.
i = 0
while i < 3: 
    print (i) 
    i += 1
else: 
    print (0)
x = abs(-7.25)
print(x)  
print(0//2)
print ('cd'.partition('cd')) 

# output-
# ('', 'cd', '')
questions = ['name', 'quest', 'favorite color'] 
answers = ['lancelot', 'the holy grail', 'blue'] 
for q, a in zip(questions, answers): 
   print('What is your {0}?  It is {1}.'.format(q, a))
for i in reversed(range(1, 10, 2)): 
   print(i) 
