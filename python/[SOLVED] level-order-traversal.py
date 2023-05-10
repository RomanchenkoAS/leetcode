# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return None
        
        level = [root, None]
        result = [[]]
        while level:
            node = level.pop(0)
            
            if node == None:
                if not level:
                    break
                else:
                    level.append(None)
                    result.append([])
                
            else:
                result[-1].append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        
        return result
    
    
s = Solution()

a15 = TreeNode(15, None, None)