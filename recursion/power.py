 # find power of any number 
def power(x, y):    
    if y == 0:  
        return 1 
    if y % 2 == 0:  
        return power(x, y // 2) * power(x, y // 2)  
           
    return x * power(x, y // 2) * power(x, y // 2)  
  
a = power(2, 5) 
print(a) 


# using inbuilt method

a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
print(pow(a,b,m))

print(2**4) # 2 raised to power 4