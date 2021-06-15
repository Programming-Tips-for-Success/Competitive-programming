# use stack for brackets validation
# Input: s = "()[]{}"
# Output: true
class Solution:
    def isValid(self, s: str) -> bool:
        open = ["{", "[", "("]
        close = ["}", "]", ")"]
        stack = []

        if type(s) == int:
            return False

        for i in s:
            if i in open:
                stack.append(i)
            if i in close:
                pos =  close.index(i)
                if(len(stack) > 0 and open[pos] == stack[-1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

q = Solution() 
print(q.isValid("()[]{}"))

