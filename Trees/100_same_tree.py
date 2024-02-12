from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = True
        right = True
        if p and q:
            if p.val == q.val:
                if p.left and q.left:
                    left = self.isSameTree(p.left, q.left)
                elif p.left or q.left:
                    return False
                if p.right and q.right:
                    right = self.isSameTree(p.right, q.right)
                elif p.right or q.right:
                    return False
            else:
                return False
        elif p or q:
            return False
        if left and right:
            return True
        return False
