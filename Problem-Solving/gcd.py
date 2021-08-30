
# GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number
# that divides both of them. 
# For example GCD of 20 and 28 is 4
# 20 = 2 *2 * 5
# 28 = 2 * 2*7 


def gcd(a,b):
     
    # Everything divides 0 
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
 
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
a = 20
b = 28
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:

    print('not found')


# Euclidean algorithm, or Euclid's algorithm,

# efficient method for computing the greatest common divisor (GCD) of two integers (​numbers)


def gcd2(a, b):
    if a == 0 :
        return b
     
    return gcd2(b%a, a)

print("gcd(", a , "," , b, ") = ", gcd2(20, 28))