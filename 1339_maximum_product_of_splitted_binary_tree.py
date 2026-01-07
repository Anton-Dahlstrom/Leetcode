from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.res = 0

        def dfs(node, calc):
            res = 0
            if node.left:
                res += dfs(node.left, calc)
            if node.right:
                res += dfs(node.right, calc)
            res += node.val
            if calc:
                self.res = max(self.res, res * (self.sum-res))
            return res
        self.sum = dfs(root, False)
        dfs(root, True)
        return self.res % MOD
