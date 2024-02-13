from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return False
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if type(left) != bool:
            print(type(left))
            return left
        if type(right) != bool:
            print(type(right))
            return right
        if left and right:
            return root
        match = False
        if root.val == p.val or root.val == q.val:
            match = True
        if match and left or match and right:
            return root
        if match or left or right:
            return True
        return False
