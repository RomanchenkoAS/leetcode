"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if (not root or ( (not root.left) and (not root.right) )) :
            return True
        
        max = float('inf')
        min = float('-inf')
        
        def validate(root, min, max):
            if not root:
                return True
            
            if root.val < min or root.val > max:
                return False
            
            return (validate(root.left, min, root.val)) and (validate(root.right, root.val, max))
        
        
        return validate(root, min, max)
        
        # nodelist = []
        
        # def build_nodelist(root):
            
        #     if root.left:
        #         build_nodelist(root.left)
            
        #     nodelist.append(root.val)
            
        #     if root.right:
        #         build_nodelist(root.right)
            
        # build_nodelist(root)
        # for i in range(1,len(nodelist)-1):
        #     if nodelist[i] <= nodelist[i-1]:
        #         return False
        