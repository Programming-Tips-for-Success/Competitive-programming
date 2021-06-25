 
'''
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S
SAMPLE INPUT  
abcdE

Output Format
Print the resultant String on a single line.
SAMPLE OUTPUT  
ABCDe

Constraints
1≤|S|≤100 where S denotes the length of string S.
'''
st=input()
str=[]
for i in st:
   if i==i.upper():
       str.append(i.lower())
   else :
       str.append(i.upper())
   result = "".join(str)
print(result)
 
# I have hope!! This will be helpful to you !!!  
# Stay tuned for the next blog!!!!
 
 