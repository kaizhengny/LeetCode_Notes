### Array
**LC1:**  
    Two Sum to a target: Use a dictionary to store the current index with the complement number as the key.  
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

**LC26:** To change the array **in place** without creating a new array could be achieved by two pointers by assigning array[i] = array[j]
**LC283:** 
          
          Two pointers. Slow and fast pointer. Only 1 iteration to achieve time complexity of O(n)
           i = j = 0
           for i in len(array):
                    if ___:
                              j+=1
                              array[i], array[j] = array[j] array[i]
                        
                          
**LC189:**
* To rotate array by k: k %=len(array)
* Use temp var to store value and assign value to array[(i+k)%len(array)] to achieve time complexity of O(n) and space complexity of O(1)
          
**LC136:** Bitwise operation XOR
           3   ^   5   =   6
          0B11 ^ 0B101 = 0B110
          
            6   ^   5   =   3
          0B110 ^ 0B101 = 0B11
          Any int1 ^ int2 ^ int2 = int1. Thus bitwise operation XOR could be used when to eliminate items appear even times.

          



### Binary Search Tree

**LC1008:** Preorder/inorder/postorder traversals all belong to DFT. 
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

