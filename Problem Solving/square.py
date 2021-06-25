# A square integer is an integer which is the square of an integer, e.g. 1, 4, 9, 16, 25
# find square number between the range and return count
 
# Sample Input

# 2
# 3 9
# 17 24

# Sample Output
# 2
# 0

#algo
# 3
# 1, 2, 3
# 1*1 =1, 2*2 =4, 3*3 =9
# x=1,  1, 4, 
def squares(a, b):
    numOfSquares = 0
    x = 1
    while(x*x < a): 
        x = x+ 1
    while(x*x <= b):
        numOfSquares = numOfSquares + 1
        x = x + 1
    
    
    
    return numOfSquares

print(squares(3, 8))
