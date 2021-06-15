# interiewers indirectly ask this
# “given a binary tree.” Other times it’s implicit, like “we want to track the number of books associated with each author.”''

class treeNode():  
  
    def __init__(self, data):  
        self.key = data 
        self.left = None
        self.right = None
class treeSolution():          
    def inorder(self, temp): 
    
        if (not temp): 
            return
        
        self.inorder(temp.left)  
        print(temp.key,end = " ") 
        self.inorder(temp.right)  
    
    def insert(self, temp,key): 
    
        q = []  
        q.append(temp)  
        while (len(q)):  
            temp = q[0]  
            q.pop(0)  
    
            if (not temp.left): 
                temp.left = treeNode(key)  
                break
            else: 
                q.append(temp.left)  
    
            if (not temp.right): 
                temp.right = treeNode(key)  
                break
            else: 
                q.append(temp.right)
    def insertData(self, data, temp):
        if temp.key:
            if data < temp.key:
                if temp.left is None:
                    temp.left = treeNode(data)
                else:
                    self.insertData(data, temp.left)
            elif data > temp.key:
                if temp.right is None:
                    temp.right = treeNode(data)
                else:
                    self.insertData(data, temp.right)
        else:
            self.data = data  
    def deleteDeepest(self, root,d_node): 
        q = [] 
        q.append(root) 
        while(len(q)): 
            temp = q.pop(0) 
            if temp is d_node: 
                temp = None
                return
            if temp.right: 
                if temp.right is d_node: 
                    temp.right = None
                    return
                else: 
                    q.append(temp.right) 
            if temp.left: 
                if temp.left is d_node: 
                    temp.left = None
                    return
                else: 
                    q.append(temp.left) 
    
    # function to delete element in binary tree  
    def deletion(self, root, key): 
        if root == None : 
            return None
        if root.left == None and root.right == None: 
            if root.key == key :  
                return None
            else : 
                return root 
        key_node = None
        q = [] 
        q.append(root) 
        while(len(q)): 
            temp = q.pop(0) 
            if temp.key == key: 
                key_node = temp 
            if temp.left: 
                q.append(temp.left) 
            if temp.right: 
                q.append(temp.right) 
        if key_node :  
            x = temp.key 
            self.deleteDeepest(root,temp) 
            key_node.key = x 
        return root
    tree = [None] * 10
    
    
    def root(self, key):
        if self.tree[0] != None:
            print("Tree already had root")
        else:
            self.tree[0] = key
    
    
    def set_left(self, key, parent):
        if self.tree[parent] == None:
            print("Can't set child at", (parent * 2) + 1, ", no parent found")
        else:
            self.tree[(parent * 2) + 1] = key
    
    
    def set_right(self, key, parent):
        if self.tree[parent] == None:
            print("Can't set child at", (parent * 2) + 2, ", no parent found")
        else:
            self.tree[(parent * 2) + 2] = key
    
    
    def print_tree(self):
        for i in range(10):
            if self.tree[i] != None:
                print(self.tree[i], end="")
            else:
                print("-", end="")
        print()
    # find value the tree
    def findval(self, lkpval, node):
        if lkpval < node.key:
            if node.left is None:
                return str(lkpval)+" Not Found"
            return node.left.findval(lkpval)
        elif lkpval > node.key:
            if node.right is None:
                return str(lkpval)+" Not Found"
            return node.right.findval(lkpval)
        else:
            print(str(node.key) + ' is found')  
     # inorder tree traversal - by using recursion and iterative approach
    def printInorder(self, root): 
    
        if root: 
    
            # First recur on left child 
            self.printInorder(root.left) 
    
            # then print the data of node 
            print(root.key), 
    
            # now recur on right child 
            self.printInorder(root.right) 
    
    # A function to do postorder tree traversal 
    def printPostorder(self, root): 
    
        if root: 
    
            # First recur on left child 
            self.printPostorder(root.left) 
    
            # the recur on right child 
            self.printPostorder(root.right) 
    
            # now print the data of node 
            print(root.key), 
    
    
    # A function to do preorder tree traversal 
    def printPreorder(self, root): 
    
        if root: 
    
            # First print the data of node 
            print(root.key), 
    
            # Then recur on left child 
            self.printPreorder(root.left) 
    
            # Finally recur on right child 
            self.printPreorder(root.right)                       
treeObj = treeSolution()
root = treeNode(10)  
root.left = treeNode(11)  
root.left.left = treeNode(7)  
root.right = treeNode(9)  
root.right.left = treeNode(15)  
root.right.right = treeNode(8)  
# obj = [{{l:7}{l:11}10:ro{l:15}{9:r}{8:r}}]
treeObj.insert(root, 12)  
treeObj.inorder(root)  #check if left child is empty insert it otherwise insert to right
# treeObj.insertData(16, root) #binary search tree insertion
# treeObj.inorder(root)
# treeObj.deletion(root, 11) #For deletion in binary tree find right most node, replace delete node data with right most node, delete rightmost node
# treeObj.inorder(root) # linked list representation
# treeObj.root(10)
# treeObj.set_left(11, 0)
# treeObj.set_left(7, 1)
# treeObj.set_left(15, 1)
# treeObj.set_right(9, 0)
# treeObj.set_right(8, 1)
# treeObj.print_tree()
# treeObj.root('A')
# treeObj.set_right('C', 0)
# treeObj.set_left('D', 1)
# treeObj.set_right('E', 1)
# treeObj.set_right('F', 2)
# treeObj.print_tree()
# print(treeObj.findval(7, root))
# print ("Preorder traversal of binary tree is")
# treeObj.printPreorder(root) 
  
# print ("\nInorder traversal of binary tree is")
# treeObj.printInorder(root) 
  
# print ("\nPostorder traversal of binary tree is")
# treeObj.printPostorder(root)

# Traversing a Tree without Recursion and without a stack (Morris Traversal)
# Traversing a Binary Tree