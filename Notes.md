### Binary Search Tree

Preorder/inorder/postorder traversals all belong to DFT. 
DFT could use stack structure or recursion to achive it.
BFT could use queue structure to achive it.

Also, binary search tree is sorted. 

In a preorder or post order traversal, it could help to find out the index which seperates root.left and root.right


Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways. Following are the generally used ways for traversing trees.
1
  2 
    4
    5
  3


Depth First Traversals:
* (a) Inorder (Left, Root, Right) : 4 2 5 1 3
* (b) Preorder (Root, Left, Right) : 1 2 4 5 3
* (c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth First or Level Order Traversal : 1 2 3 4 5

