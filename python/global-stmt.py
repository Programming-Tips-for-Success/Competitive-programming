a = 10 
def read():  
    print (a)  
def mod1():  
    global a   # important to add if you want to use global variable
    a = a + 1
    print (a) 
def mod2():  
    a = 15 
    print (a) 
read() 
mod1()
mod2()