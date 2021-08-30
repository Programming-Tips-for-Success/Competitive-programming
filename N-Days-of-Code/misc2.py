# What is the output of the following Python 3 code:
def MainProg(f): 
    m = {} 
    def InnerProg(num): 
        if num not in m:          
            m[num] = f(num) 
        return m[num]  
    return InnerProg   
      
@MainProg
def Cal(num): 
    if num == 0: 
        return 1
    else: 
        return num**2*Cal(num-1) 
print(Cal(3))

# 172
# RecursionError
# 81
# 36 -> correct output