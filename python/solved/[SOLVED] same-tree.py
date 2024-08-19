"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q

        if p.val != q.val:
            return False

        # This is a leaf in both trees
        if (not p.left and not q.left) and (not p.right and not q.right):
            return True

        # This is a root of subtree
        else:
            # Fast fail
            if (p.left and not q.left) or (q.left and not p.left) or (p.right and not q.right) or (
                    q.right and not p.right):
                return False

            res = True
            # Subtree to the left
            if p.left and q.left:
                res = res and self.isSameTree(p.left, q.left)

            # Subtree to the right
            if p.right and q.right:
                res = res and self.isSameTree(p.right, q.right)

            return res


p = [1, 2, 3, None, None, 4, 5]
q = [1, 2, 3]

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.right = TreeNode(4)

g = TreeNode(1)
g.left = TreeNode(2)
g.right = TreeNode(3)

sol = Solution()
res = sol.isSameTree(t, g)
print(res)
