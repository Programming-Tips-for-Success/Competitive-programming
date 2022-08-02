# global usage
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

# nonlocal usage
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