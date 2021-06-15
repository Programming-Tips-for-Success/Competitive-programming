'''
Question
 Jadoo, the Space Alien has befriended Koba upon landing on Earth. Since then, he wishes Koba to be more like him. In order to do so, he decides to slowly transcribe Koba's DNA into RNA. But he has to write a very shortcode in order to do the transcription so as not to make Koba aware of the change.
The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
G --> C
C --> G
T --> A
A --> U
Input: The input will always be a string of characters.
Output: The output should always be a string of characters. In the case of invalid input, you should output Invalid input as a string.
Rules: Your code should not consist of any numerical characters             (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and the length of your code should be             <= 103. If your code consists of numerical characters, then your score is zero irrespective of your code length or test cases satisfied. If your code is devoid of numerical characters and is of length > 103 then you score 50%.
SAMPLE INPUT  
C
SAMPLE OUTPUT  
G
 
Python program
 
'''
DString=input('Please enter code')
OutString=''
flag='T'
for i in DString:
   if i not in ['G','C','A','T']:
       print('Invalid Input')  
       flag='F'
       break
   else:
           if i=='G':
               OutString+='C'
           elif i=='C':
               OutString+='G'
           elif i=='T':
               OutString+='A'
           elif i=='A':
               OutString+='U'
if flag=='T':
   print(OutString)
