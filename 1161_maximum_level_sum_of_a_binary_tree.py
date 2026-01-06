from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        arr = [root]
        maximal = float("-inf")
        res = -1
        level = 1
        while arr:
            temp = []
            cur = 0
            for node in arr:
                cur += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if cur > maximal:
                maximal = cur
                res = level
            level += 1
            arr = temp
        return res
