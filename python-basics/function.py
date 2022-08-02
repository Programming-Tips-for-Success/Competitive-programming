
# function usage
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

# Argument lists and keyword argument lists
def testArgLists_1(*args, **kwargs):
    print ('args:', args)
    print ('kwargs:', kwargs)
testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')

args = [3, 6] 
b= list(range(*args))           
print(b) 