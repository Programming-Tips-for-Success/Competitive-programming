# @ decorator name
# the @staticmethod is a built-in decorator that defines a static method in the class in Python. A static method doesn't receive any reference argument whether it is called by an instance of a class or by the class itself.

# @classmethod 
# It can access class attributes, but not the instance attributes.	
# @staticmethod
# It cannot access either class attributes or instance attributes.
class Student:
    name = 'unknown' # class attribute
    
    def __init__(self):
        self.age = 20  # instance attribute

# it cannot have self or cls parameter.
    @staticmethod
    def tostring():
        print('Student Class')

(Student.tostring()) # 'Student Class'
(Student().tostring()) # 'Student Class'
std = Student()
(std.tostring()) # 'Student Class'

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