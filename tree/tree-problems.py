
# Tree  Algorithms
# topics to cover
# Binary Search Tree, N-ary Tree
# Given a n-ary tree. zigzag level order traversal.
# Print BT from Different View
# Conversion of BT, Post-Order, InOrder, PreOrder Operations
# Mirror Operations, Leaf Nodes Distances,Lowest Common Ansesters/ancestor
# Recursive and Iterative Operations

# Note : Un-important topic in Tree is B* Tree, Red Black Tree,AVL tree, Segment Tree

# interviewers indirectly ask this
# “given a binary tree.” Other times it’s implicit, like “we want to track the number of books associated with each author.”''

# Traversing a Tree without Recursion and without a stack (Morris Traversal)
# Traversing a Binary Tree

# Trees:
# Trees are non-linear data structures that represent nodes connected by edges. It may have more than 2 leaf nodes. Trees are hierarchical data structures. 

# Benefits:
# One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer, you can use this to track the number of books associated with each author.
# Trees (with some ordering e.g., BST) provide moderate access/search which is quicker than Linked List and slower than arrays. 
# Trees provide moderate insertion/deletion which is quicker than Arrays and slower than Unordered Linked Lists. 
# Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on the number of nodes as nodes are linked using pointers. 

#  Main applications of trees include: 
# 1. Manipulate hierarchical data. 
# 2. Make information easy to search (see tree traversal). 
# 3. Manipulate sorted lists of data. 
# 4. As a workflow for compositing digital images for visual effects. 
# 5. Router algorithms 
# 6. Form of multi-stage decision-making (see business chess). 

# Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways like- 

# Depth First Traversals: 
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3 
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3 
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1 

# The common in three different types of traversals (Inorder, Preorder and Postorder)  Left subtree is always visited before right subtree. 

# Breadth-First or Level Order Traversal: 
# Travel through level
# 1 2 3 4 5 

# Trees application-
# Trees (  Trie, Segment Tree, Red-Black tree)

# problem
# Trees, Tries: total number of words in Trie, find all words stored in Trie?
# Segment Tree
# Segment Tree (with lazy propagation)
# Persistent Segment Tree
# Lazy segment tree 

# tree- DLL interconversion

# B-Tree and B+ Tree: 
# They are used to implement indexing in databases.

# Syntax Tree: 
# Used in Compilers.

# Suffix Tree: 
# For quick pattern searching in a fixed text.

# Suffix The arrangement 

# continuous tree:
# A tree is a Continuous tree if in each root to leaf path, the absolute difference between keys of two adjacent is 1.

# Binary tree: 
# A tree whose elements have at most two children is called a binary tree. Each element in a binary tree can have only two children.  
# Note: Tree and binary trees are different things. 
# You can print the binary tree in all orders, insert a node, delete the node.

# Binary tree types:

# Full Binary Tree - 
# 0 or 2 children.   L(leaf nodes) = I + 1

# Complete Binary Tree -
#  all levels completely filled except the last level.

# Perfect Binary Tree - 
# all leaf nodes are at the same level.

# Balanced Binary Tree
# A degenerate (or pathological) tree - every internal node has one child.

# AVL tree:
# Named after their inventor Adelson, Velski & Landis. AVL trees are height balancing binary search tree.
# AVL tree checks the height of the left and the right sub-trees and assures that the difference is not more than 1. This difference is called the Balance Factor. 

# Heap is a tree data structure that is implemented using arrays and used to implement priority queues. A Heap is a special Tree-based data structure in which the tree is a complete binary tree.
# Max-Heap - key represent maximum data comparison to children nodes.
# Min-Heap - key represent Minumum data comparison to children nodes.

# Save all leaf nodes of a Binary tree in a Doubly Linked List by using Right node as Next node and Left Node as Previous Node.

# Find all nodes at k-distance from a given node in a binary tree

# Construct a binary tree from given inorder and preorder traversals.

# Return a tree such that each internal node stores the sum of all its child nodes. Each leaf node stores zero.

# Check whether a given binary tree is balanced or not. Definition was no two leaves should have height differences of greater than one.

# Connect nodes on the same level in a binary tree.
# Find the sum of data of all leaves of a binary tree on the same level and then multiply sums obtained of all levels.


# Least common ancestor of two nodes in a binary tree

# Given the root to a binary tree, a value n and k.Find the sum of nodes at distance k from node with value n


# Given a binary search tree , print the path which has the sum equal to k and has minimum hops. i.e if there are multiple paths with the sum equal to k then print the path with minimum number of nodes.
#
# Write a program to connect the next left node in a binary tree. Also the first node of each level should be pointing to the last node of the next level? (Without using Queue)
# Convert a binary tree to its sum tree(each node is the sum of its children) 

# Given a tree with edge weights, find any path in the tree with maximum sum of edges.

#  KD-tree 
#  Splay tree 