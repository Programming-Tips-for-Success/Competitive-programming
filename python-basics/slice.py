# You are given an immutable string, and you want to make changes to it.


# To print elements-

abc = ['x', 'y', 'z']
print(abc[:])  # To print the whole array-

# To print substring-
str = 'sun'
print(str[:2] ) # upto 1 index o/p -> su
print(str[2:]) # start from 2 index  -> n
print(str[-2])  # u
print(str[-2:])  # un
print(str[::-1]) # nus (reverse the string)

x = [1, 2, 3, 4]   
print(x[1:3])  # 1 and go upto the index 2    # [2, 3]
print(x[::-1]) # [4, 3, 2, 1]

string = "abracadabra"
# You can access an index by:
print (string[5]) # a

# What if you would like to assign a value?

# string[5] = 'k' 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# How would you approach this?
#     One solution is to convert the string to a list and then change the value.

string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print (string) # abrackdabra

    # Another approach is to slice the string and join it back.

string = string[:5] + "k" + string[6:]
print (string) # abrackdabra

