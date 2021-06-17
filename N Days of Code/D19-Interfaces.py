'''
Objective
Today, we're learning about Interfaces. Check out the Tutorial tab for learning materials and an instructional video!
Task
The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the editor below.
Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. The implementation for the divisorSum(n) method must return the sum of all divisors of
.
Input Format
A single line containing an integer,
.
Constraints
Output Format
You are not responsible for printing anything to stdout. The locked template code in the editor below will call your code and print the necessary output.
Sample Input
6
Sample Output
I implemented: AdvancedArithmetic
12
Explanation
The integer
is evenly divisible by , , , and . Our divisorSum method should return the sum of these numbers, which is . The Solution class then prints on the first line, followed by the sum returned by divisorSum (which is ) on the second line.
'''
class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        div=list()
        for i in range(1,n+1):
            if n%i == 0:
                div.append(i)
        return sum(div)
    def add(self, num1, num2):  
        return num1 + num2 
    def subtract(self, num1, num2):  
        return num1 - num2  
    def multiply(self, num1, num2):  
        return num1 * num2  
    def divide(self, num1, num2):  
        return num1 / num2  


print("Please select operation -\n"  
        "1. Add\n"  
        "2. Subtract\n"   
        "3. Multiply\n"   
        "4. Divide\n"
        "5. divisorSum")  
select = input("Select operations form 1, 2, 3, 4, 5 :")  
number_1 = int(input("Enter first number: "))  
number_2 = int(input("Enter second number: "))  

my_calculator = Calculator()

if select == '1':  
    print(number_1, "+", number_2, "=",  
                    my_calculator.add(number_1, number_2))  
elif select == '2':  
    print(number_1, "-", number_2, "=",  
                    my_calculator.subtract(number_1, number_2))  
elif select == '3':  
    print(number_1, "*", number_2, "=",  
                    my_calculator.multiply(number_1, number_2))    
elif select == '4':  
    print(number_1, "/", number_2, "=",  
                    my_calculator.divide(number_1, number_2))
elif select == '5':  
    print(number_1,   
                    my_calculator.divisorSum(number_1))  
else:  
    print("Invalid input") 


print("I implemented: " + type(my_calculator).__bases__[0].__name__)


