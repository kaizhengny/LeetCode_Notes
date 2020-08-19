'''
1008. Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
'''

#I was trying to find a way to trace back to the parent if the val of current node is larger than the val of the parent. But there is no self.paren in the TreeNode class.

#The below solution used a stack structure to keep track of each node and gives your a way to trace back to previous nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root
        
        
 #another way to solve the problem would be to find the index of the first node to the right of the root node.
 #Then use recursion to attach nodes to the left and right respectively.
 
 class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        i = 1
        while i<len(preorder) and preorder[i]<root.val:
            i+=1
            
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])

        return root
                
 
 
 
 
