'''

Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.
Complete the Student class by writing the following:
    A Student class constructor, which has 
parameters:
    A string, 
.
A string,
.
An integer,
.
An integer array (or vector) of test scores,
        .
    A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
[Grading.png]
Input Format
The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).
You are not responsible for reading the following input from stdin:
The first line contains
, , and , respectively. The second line contains the number of test scores. The third line of space-separated integers describes
.
Constraints
Output Format
This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.
Sample Input
Heraldo Memelli 8135627
2
100 80
Sample Output
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
Explanation
This student had
scores to average: and . The student's average grade is . An average grade of corresponds to the letter grade , so our calculate() method should return the character'O'.
'''
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber) # you can also use person class
        self.scores=scores
        
    def calculate(self):
        avg=(sum(self.scores))/len(self.scores)
        if avg>=90 and avg<=100:
            return 'O'
        elif avg>=80 and avg<90:
            return 'E'
        elif avg>=70 and avg<80:
            return 'A'
        elif avg>=55 and avg<70:
            return 'P'
        elif avg>=40 and avg<55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

# Another example
class Basic:
    def __init__(self, name):
        self.name = name
    def show(self):
        print( 'Basic ­­ name: %s' % self.name)

class Special(Basic):
    def __init__(self, name, edible):
        Basic.__init__(self, name)
        self.upper = name.upper()
        self.edible = edible

    def show(self):
        Basic.show(self)
        print( 'Special ­­ upper name: %s.' % self.upper)
        if self.edible:
            print( "It's edible.")
        else:
            print( "It's not edible.")

    def edible(self):
        return self.edible
        
class Advanced():
    def __init__(self, name):
        self.name = name
    
    def Description():
        return 'This is an advanced class.'
    
    def ClassDescription(cls):
        return 'This is advanced class: %s' % repr(cls)
    
    Description = staticmethod(Description)
    ClassDescription = classmethod(ClassDescription)

obj1 = Basic('Apricot')
obj1.show()
print( '=' * 30)
obj2 = Special('Peach', 1)
obj2.show()
obj1 = Advanced('Nectarine')
print (obj1.Description())
print (obj1.ClassDescription()) # This is advanced class: <class '__main__.Advanced'>
print ('=' * 30)
print (Advanced.Description())
print  (Advanced.ClassDescription()) # This is advanced class: <class '__main__.Advanced'>

