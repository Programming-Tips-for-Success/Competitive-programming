# word problems

# Given a dictionary of 50,000 words. Given a phrase without spaces, add spaces to make it a proper sentence.
# input:  thequickbrownfoxjumpoverlazydog	 
# output: the quick brown fox jump over lazy dog 


# A recursive program to print all possible
# partitions of a given string into dictionary
# words
 
# A utility function to check whether a word
# is present in dictionary or not.  An array of
# strings is used for dictionary.  Using array
# of strings for dictionary is definitely not
# a good idea. We have used for simplicity of
# the program
def dictionaryContains(word):
    dictionary = {"mobile", "samsung", "sam", "sung", "man",
                  "mango", "icecream", "and", "go", "i", "love", "ice", "cream"}
    return word in dictionary
 
# Prints all possible word breaks of given string
def wordBreak(string):
   
    # Last argument is prefix
    wordBreakUtil(string, len(string), "")
 
# Result store the current prefix with spaces
# between words
def wordBreakUtil(string, n, result):
 
    # Process all prefixes one by one
    for i in range(1, n + 1):
       
        # Extract substring from 0 to i in prefix
        prefix = string[:i]
         
        # If dictionary conatins this prefix, then
        # we check for remaining string. Otherwise
        # we ignore this prefix (there is no else for
        # this if) and try next
        if dictionaryContains(prefix):
           
            # If no more elements are there, print it
            if i == n:
 
                # Add this element to previous prefix
                result += prefix
                print(result)
                return
            wordBreakUtil(string[i:], n - i, result+prefix+" ")
 

# print("First Test:")
# wordBreak("iloveicecreamandmango")

# print("\nSecond Test:")
# wordBreak("ilovesamsungmobile")
# Time Complexity: O(nn). Because there are nn combinations in The Worst Case.
# Auxiliary Space: O(n2). Because of the Recursive Stack of wordBreakUtil(…) function in The Worst Case.

'''
You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3   TOTAL unique STRINGs
2 1 1  number of occurrences for each distinct word according to their appearance in the input.

Explanation

There are distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
'''



from collections import OrderedDict
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.
# it will return tuple
n = int(input())
l=OrderedDict()
for _ in range(n):
    s=input()
    try:
        l[s]+=1
    except:
        l[s]=1
print(len(l))
for e in l.keys():
    print(l[e],end=' ')

ordinary_dictionary = {}
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5
print(ordinary_dictionary)

ordinary_dictionary = OrderedDict()
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5
print(ordinary_dictionary) #OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])