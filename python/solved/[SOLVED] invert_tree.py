# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if root:                
#             root.left, root.right = root.right, root.left
            
#             if root.left:
#                 self.invertTree(root.left)
#             else:
#                 root.left = None
                
#             if root.right:
#                 self.invertTree(root.right)
#             else:
#                 root.right = None

#             return root


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def swap(node):

            if (not node.left and not node.right):
                return node

            # Swap
            node.left, node.right = node.right, node.left

            if node.left:
                swap(node.left)
            else:
                node.left = None
                
            if node.right:
                swap(node.right)
            else:
                node.right = None

            return node

        if root:
            return swap(root)
        
