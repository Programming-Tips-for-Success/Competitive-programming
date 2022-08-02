"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Sample Input -  string consisting of space separated words.

this is a string

Sample Output

this-is-a-string

"""

def split_and_join(line):
    return "-".join(line.split(" "))


line = input()
result = split_and_join(line)
print(result)


# string methods

#  split usage

a = "this is a string"
b = a.split(" ") # a is converted to a list of strings.
print (b)

print('The happy cat ran home.'.upper()) # 'THE HAPPY CAT RAN HOME.'
print('The happy cat ran home.'.find('cat')) # 10
print('The happy cat ran home.'.find('kitten')) # -­1
print('The happy cat ran home.'.replace('cat', 'dog')) # The happy dog ran home.

print('0e32'.strip('0')) # e32

#  The rstrip() method strips whitespace off the right side of a string:
s1 = 'some text   \n d'
s2 = s1.rstrip()
print(s2)

# The center(n) method centers a string within a padded string of width n:
s1 = 'Dave'
s2 = s1.center(20)
print(s2)
