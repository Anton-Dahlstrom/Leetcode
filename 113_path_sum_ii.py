from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        self.res = []
        if not root:
            return self.res

        def dfs(node, total, nums, targetSum):
            total += node.val
            nums.append(node.val)
            if not node.left and not node.right:
                if targetSum == total:
                    self.res.append(nums.copy())
                nums.pop()
                return
            if node.left:
                dfs(node.left, total, nums, targetSum)
            if node.right:
                dfs(node.right, total, nums, targetSum)
            nums.pop()

        dfs(root, 0, [], targetSum)
        return self.res

root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
output = [[5,4,11,2],[5,8,4,5]]
