# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:                
            root.left, root.right = root.right, root.left
            
            if root.left:
                self.invertTree(root.left)
            else:
                root.left = None
                
            if root.right:
                self.invertTree(root.right)
            else:
                root.right = None

            return root
        
