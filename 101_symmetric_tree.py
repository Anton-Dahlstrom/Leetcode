from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(l, r):
            if l.val != r.val:
                return False
            if l.left:
                if not r.right or not dfs(l.left, r.right):
                    return False
            elif r.right:
                return False
            if l.right:
                if not r.left or not dfs(l.right, r.left):
                    return False
            elif r.left:
                return False
            return True
        if root.left and root.right:
            return dfs(root.left, root.right)
        elif not root.left and not root.right:
            return True
        return False
