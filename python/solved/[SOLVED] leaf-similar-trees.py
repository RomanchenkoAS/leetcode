"""
872. Leaf-Similar Trees
Consider all the leaves of a binary tree, from left to right order, the values of those
 leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root: Optional[TreeNode], leaf_sequence: List) -> None:
    if not root.left and not root.right:
        leaf_sequence.append(root.val)

    if root.left:
        dfs(root.left, leaf_sequence)
    if root.right:
        dfs(root.right, leaf_sequence)


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list_1 = list()
        dfs(root1, list_1)

        list_2 = list()
        dfs(root2, list_2)

        if len(list_1) != len(list_2):
            return False

        for n1, n2 in zip(list_1, list_2):
            if n1 != n2:
                return False

        return True
