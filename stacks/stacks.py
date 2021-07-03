# topics to cover
# Stack/Queue operations in O(1) time, combining stack and Queue
# Applying stack/queue in Binary tree-based
# Matrix problem solved using stack
# Note: Direct questions is not asked in this Topic. Always application based on stack/queue


# problem statement
# Balanced Brackets: Given a mathematical operation, find out if the
# brackets are placed such that the equation is valid. There are 3
# types of brackets: (,[,{. For example, ([4*{2+3}]) is balanced, but
# {[3} is unbalanced.

# use stack for brackets validation
# parenthesis check

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
print(q.isValid("()[]{"))
print(q.isValid("([4*{2+3}])"))
print(q.isValid("{[3}"))



