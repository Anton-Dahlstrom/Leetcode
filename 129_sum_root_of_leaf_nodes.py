from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return self.res

        def dfs(node, nums):
            nums += str(node.val)
            if not node.left and not node.right:
                self.res += int(nums)
                return

            if node.left:
                dfs(node.left, nums)
            if node.right:
                dfs(node.right, nums)

        dfs(root, "")
        return self.res

input = root = [1,2,3]
Output: 25