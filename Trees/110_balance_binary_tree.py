from typing import Optional


root = [3, 9, 20, None, None, 15, 7]
Output: True

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l = 0
        r = 0
        if root.left:
            l = self.dfs(root.left)
            if not l:
                return False
        if root.right:
            r = self.dfs(root.right)
            if not r:
                return False
        if l - r in range(-1, 2):
            return True
        return False

    def dfs(self, node):
        l = 0
        r = 0
        if node.left:
            l = self.dfs(node.left)
            if not l:
                return False
        if node.right:
            r = self.dfs(node.right)
            if not r:
                return False
        if l - r not in range(-1, 2):
            return False
        return max(l, r) + 1


a = -1
b = 0
if a - b in range(-1, 1):
    print(25)
if b - a in range(-1, 1):
    print(55)
