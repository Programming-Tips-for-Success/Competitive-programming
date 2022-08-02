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
print(a) # [1, 2, 3]
  
flag = 2; ropes = 3; pole = 4 
print(flag)
print("5"*6)
print (' ' is ' ')
 
if 's' in 'geeks':  
       print ("s is part of geeks")  
else : print ("s is not part of geeks")  
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
 
import keyword  
s = "for" 
if keyword.iskeyword(s):  
        print ( s + " is a python keyword")  
else :  print ( s + " is not a python keyword")  
print (keyword.kwlist) # print list of all keywords 
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
 
print(0//2)
print ('cd'.partition('cd'))  # ('', 'cd', '')
