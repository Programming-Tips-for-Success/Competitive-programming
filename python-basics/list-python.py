nums = []     
nums.append(21)  
nums.append(40.5)  
nums.append("String")  
print(nums) 

nums.insert(0,1) # index, value
print(nums) 

# To add two lists together, creating a new list, use the + operator. 
a = [11, 22, 33,]
b = [44, 55]
c = a + b
print(c)

# To add the items in one  list to an existing list, use the extend() method.
a.extend(b)
print(a)

abc = ['x', 'y', 'z']
abc.remove("z")
print(abc)

stack = ['a', 'b', 'c'] 
print(stack.pop()) 
print(stack) 

que = ['a', 'b', 'c'] 
print(que.pop(0)) 
print(que) 



