'''Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)'''



# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        
        if not root.children:
            return [root.val]
        
        result = []
        # nodestack = []

        def push_children(node):
            if not node:
                return
            else:
                result.append(node.val)
                for child in node.children:
                    push_children(child)
                    
            return 
        
        push_children(root)
                
        return result
    
# input = [1,3,5,6,2,4]
# s = Solution()

# print(s.preorder(input))