from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        arr = [root]
        depth = 1
        while arr:
            temp = []
            for node in arr:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            depth += 1
            arr = temp
        return depth
