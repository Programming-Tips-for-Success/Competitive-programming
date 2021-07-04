# topics to cover
# Basic BST
# AVL tree
# red black tree


# Binary Search Tree: 
# It is a tree that allows fast search, insert, delete on sorted data. It also allows finding the closest item. Every node has a maximum of two children.
# A node’s left child must have a value less than its parent’s value and the node’s right child must have a value greater than its parent value. A BST is a great choice for storing data that may need to be sorted. 
# properties: 
# The left subtree of a node contains only nodes with keys lesser than the node’s key. 
# The right subtree of a node contains only nodes with keys greater than the node’s key. 
# The left and right subtree each must also be a binary search tree. 
# There must be no duplicate nodes. 
# The above properties of the Binary Search Tree provide ordering among keys so that the operations like search, minimum and maximum can be done fast. 
# If there is no order, then we may have to compare every key to search a give.

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

# level-order traversal (breadth first search -bfs), visits each level of a tree's nodes from left to right, top to bottom. 
# you can also implement this with queue
# traverse each level of the tree from the root downward, and process the nodes at each level from left to right. 
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