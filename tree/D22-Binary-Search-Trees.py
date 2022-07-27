'''
Objective
Today, we're working with Binary Search Trees (BSTs). 

Task
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer,

, pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
The first line contains an integer,
, denoting the number of nodes in the tree.
Each of the subsequent lines contains an integer,

, denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input

7
3
5
2
1
4
6
7

Sample Output

3

Explanation

The input forms the following BST:

[BST.png]

The longest root-to-leaf path is shown below:

[Longest RTL.png]

There are
nodes in this path that are connected by edges, meaning our BST's . Thus, we print as our answer.
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root==None or (root.left==None and root.right==None):
            return 0
        else:
            return (1+max(self.getHeight(root.left),self.getHeight(root.right)))


    def levelOrder(self,root):      
        l=[root]
        for current in l:
            if current:
                print(current.data, end=' ')
                l.extend([current.left,current.right])

    def search(self, root,key):
     
        # Base Cases: root is null or key is present at root
        if root is None or root.data == key:
            return root
    
        # Key is greater than root's key
        if root.data < key:
            return self.search(root.right,key)
    
        # Key is smaller than root's key
        return self.search(root.left,key)

    def minValue(self, node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current.data


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)

height=myTree.getHeight(root)
print('height', height)       

myTree.levelOrder(root)

# Sample Input dfs example

# 6
# 3
# 5
# 4
# 7
# 2
# 1

# Sample Output

# 3 2 5 1 4 7 

# Search in Binary Search Tree
searchNo=int(input('enter no. for search'))
a = myTree.search(root, searchNo)
print('searched number', a, a.data)

# With this we can do fast search, minimum and maximum elem

minValue = myTree.minValue(root)
print('minValue', minValue)