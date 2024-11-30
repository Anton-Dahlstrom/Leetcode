from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, total):
            total += node.val
            if total == targetSum and not(node.right or node.left):
                return True

            if node.right:
                if dfs(node.right, total):
                    return True
            if node.left:
                if dfs(node.left, total):
                    return True
            return False
        if root:
            return dfs(root, 0)
        return False
