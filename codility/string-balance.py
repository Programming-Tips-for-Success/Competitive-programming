# A string is called balanced when every letter occurring in the string, appears both in upper- and lowercase. For example, the string "CATattac" is balanced ('a', 'c' and 't' occur in both cases), but "Madam" is not ('d' and 'a' appear only in lowercase). Note that the number of occurrences does not matter.

# Write a function:

# class Solution { public int solution(String S); }

# that, given a string S of length N, returns the length of the shortest balanced fragment of S. If S does not contain any balanced fragments, the function should return -1.

# Examples:

# 1. Given S = "azABaabza", the function should return 5. The shortest balanced fragment of S is "ABaab".

# 2. Given S = "TacoCat", the function should return -1. There is no balanced fragment.

# 3. Given S = "AcZCbaBz", the function should return 8. The shortest balanced fragment is the whole string.

# 4. Given S = "abcdefghijklmnopqrstuvwxyz", the function should return -1.

# Assume that:

# N is an integer within the range [1..200];
# string S consists only of letters ('a'−'z' and/or 'A'−'Z').
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

def doInvert(letter):
    if(letter.isupper()):
        return letter.lower()
    else:
        return letter.upper()

def getEndIndex(scanned, letter, startIndex):
    allOccurance = scanned.get(letter)
    result = -1
    for index in allOccurance:
        if (index >= startIndex):
            result = index
            break
    return result

def solution(S):
    scanned = {}
    isBalanced = {}

    for index, letter in enumerate(S):
        invLetter = doInvert(letter)
        if(isBalanced.__contains__(invLetter)):
            isBalanced[letter] = True
            isBalanced[invLetter] = True
        else:
            isBalanced[letter] = False
        if (scanned.__contains__(invLetter)):
            scanned.get(invLetter).append(index)
        else:
            scanned[invLetter] = [index]
    
    startIndex = -1
    endIndex = -1
    minBalancedString = ""
    tempMinBalancedString = []

    for index, letter in enumerate(S):
        if(isBalanced.get(letter)):
            if(startIndex == -1):
                startIndex = index
            temp = getEndIndex(scanned, letter, startIndex)
            if(temp == -1):
            
                tempMinBalancedString = []
                startIndex = -1
                endIndex = -1
            else:
                endIndex = temp if temp > endIndex else endIndex
                tempMinBalancedString.append(letter)
                         
        else:
    
            tempMinBalancedString = []
            startIndex = -1
            endIndex = -1

        if (index == endIndex):
     
            if ( len(tempMinBalancedString) > len(minBalancedString)):
                minBalancedString = ''.join(tempMinBalancedString)

    if(not minBalancedString):
        return -1
    else:
        return len(minBalancedString)

print(solution('azABaabza'))